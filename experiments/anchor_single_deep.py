"""
Single-anchor DEEP structure search on one M(omega) bit string.

Brief lineage: briefs/anchor-digit-search-brief.md and anchors.md S17.7-17.9
ran a BREADTH search -- 200 anchors x 4096 bits, a cross-cut that is shallow
per anchor. This file is the complementary DEPTH probe requested 2026-07-13:
take a SINGLE bulk omega, compute M(omega) to 2^17 bits, and ask whether that
one number's own digit string -- read as long as we can afford -- has internal
structure. Normality (every k-block equidistributes as length -> infinity) is a
single-sequence, length -> infinity statement, so DEPTH on one omega is the
faithful probe of it; the breadth battery never went past 4096 bits (=32x
shallower than here).

This is an experiment under README's "experiments may feed the ledger" clause,
NOT parked AEH proof effort, and NOT a claim about AEH's truth. A clean pass is
a recordable calibration gain on the deep single-sequence axis; a rejection
would be a genuine find to verify before believing (KL-LP precedent).

Null model (stated before any result): the bits of M(omega) are i.i.d. fair
coin -- independent, P(bit=1)=1/2. Every test states its statistic's null
distribution, and every test is ALSO run on a matched-length i.i.d.-fair-coin
control through identical code, so a test artifact shows up on the control too
and is not mistaken for structure in M(omega).

Fresh generator, per AGENTS.md fresh-code-per-claim: the 2-adic log is
re-implemented here from the definition (9^N(w) = w^-1, M(w) = N(w^2); log via
its convergent series). It imports nothing from anchor_digit_structure.py or any
repo script, and is validated against the independently-recorded 12-value table
in anchors.md S17.7 before use (_validate).

Honest note on discriminating power: the window-#ones "bell curve" (Test 2) is
the WEAKEST test here -- by the CLT almost any sum of many bounded terms looks
Gaussian, so a bell curve confirms the marginal (mean/variance) but is blind to
correlations that preserve it. The run-length tail (Test 1), autocorrelation
(Test 3), and block-entropy scaling (Test 4) are what actually catch dependence.
TestU01/PractRand (higher-power PRNG batteries) are noted as an un-run stronger
follow-up, not hand-rolled here.
"""
import argparse
import math
import random
import zlib
import numpy as np

# =====================================================================
# Fresh M(omega) generator: 2-adic logarithm via its convergent series.
# (Pure Python big-int; bit extraction to numpy happens after.)
# =====================================================================

def _v2(x):
    v = 0
    while x & 1 == 0:
        x >>= 1
        v += 1
    return v


def _log1p_2adic(x, prec):
    """log(1+x) mod 2^prec for v2(x) >= 1, via sum_{i>=1} (-1)^(i+1) x^i / i.
    Terms with i*v2(x) >= prec vanish mod 2^prec; division by i splits into a
    right-shift (its 2-part) and a modular inverse of its odd part."""
    mod = 1 << prec
    mask = mod - 1
    x &= mask
    if x == 0:
        return 0
    vx = _v2(x)
    acc = 0
    xi = 1
    i = 0
    while True:
        i += 1
        xi = (xi * x) & mask
        if i * vx >= prec:
            break
        e = _v2(i)
        odd = i >> e
        term = ((xi >> e) * pow(odd, -1, mod)) & mask
        acc = (acc + term) & mask if (i & 1) else (acc - term) & mask
    return acc & mask


_LOG9 = {}

def _log9(prec):
    if prec not in _LOG9:
        _LOG9[prec] = _log1p_2adic(8, prec)   # log(1+8), v2 = 3
    return _LOG9[prec]


def anchor_int(omega, nbits, margin=192):
    """M(omega) mod 2^nbits as a Python int, bit i (lsb first) = 2-adic digit i.
    M(omega) = N(omega^2), N(w) = -log(w)/log(9). `margin` absorbs the
    valuation-3 division by log(9) plus truncation slack."""
    prec = nbits + margin
    mod = 1 << prec
    mask = mod - 1
    y = (omega * omega) & mask
    x = (y - 1) & mask
    if x == 0:
        return 0                              # omega==1: fixed point, M=0
    Lw = _log1p_2adic(x, prec)
    L9 = _log9(prec)
    assert _v2(L9) == 3
    p = prec - 3
    pm = (1 << p) - 1
    N = (-((Lw >> 3) & pm) * pow((L9 >> 3) & pm, -1, 1 << p)) & pm
    return N & ((1 << nbits) - 1)


def anchor_bits(omega, nbits):
    """M(omega) as an int8 numpy array of 0/1, lsb first."""
    n = anchor_int(omega, nbits)
    b = n.to_bytes((nbits + 7) // 8, "little")
    arr = np.unpackbits(np.frombuffer(b, dtype=np.uint8), bitorder="little")
    return arr[:nbits].astype(np.int8)


_REFERENCE = {
    1: "000000000000000000000000", 3: "111111111111111111111111",
    5: "101011110100001111101100", 7: "010010101101111111001101",
    11: "100110111000001010010011", 13: "110111011010100100010110",
    17: "001100100100010001101100", 19: "110000011010111111001110",
    23: "011001111111100000001110", 29: "111011010111011110110011",
    31: "000101001100101110110001", 37: "101101110100011110111111",
}

def _validate():
    for w, ref in _REFERENCE.items():
        got = "".join(str(int(b)) for b in anchor_bits(w, 24))
        assert got == ref, f"generator mismatch omega={w}: {got} != {ref}"


# =====================================================================
# Tests (numpy-vectorized). Each is also run on a matched i.i.d. control.
# =====================================================================

def _run_lengths(bits):
    """Lengths of maximal runs of identical bits (numpy, O(N))."""
    ends = np.append(np.nonzero(np.diff(bits))[0], len(bits) - 1)
    return np.diff(np.concatenate(([-1], ends)))


def test_runlength(bits, kmax=20):
    """Run lengths vs Geometric(1/2): P(L=k)=2^-k. Chi-square, cells 1..kmax-1
    plus a pooled tail (P(L>=kmax)=2^-(kmax-1)); df=(#cells)-1, no fitted params.
    Also longest run vs the ~log2(N) fair-coin expectation."""
    R = _run_lengths(bits)
    total = len(R)
    capped = np.minimum(R, kmax)
    obs = np.bincount(capped, minlength=kmax + 1)
    chi2 = 0.0
    for k in range(1, kmax + 1):
        pk = 2.0 ** (-k) if k < kmax else 2.0 ** (-(kmax - 1))
        e = total * pk
        chi2 += (obs[k] - e) ** 2 / e
    df = kmax - 1
    return {"total_runs": int(total), "chi2": chi2, "df": df,
            "p": _chi2_sf(chi2, df), "longest": int(R.max()),
            "log2N": math.log2(len(bits))}


def test_window_counts(bits, W=256):
    """Non-overlapping windows width W; #ones ~ Binomial(W,1/2) ~ Normal(W/2,W/4)
    -- the 'bell curve'. Chi-square of the count histogram vs the exact Binomial
    (cells merged to expected>=5), plus sample mean/sd vs W/2, sqrt(W)/2."""
    n = len(bits) // W
    counts = bits[:n * W].reshape(n, W).sum(axis=1)
    mean = float(counts.mean())
    sd = float(counts.std())
    pmf = np.array([_binom_pmf(W, c) for c in range(W + 1)])
    edges = _bins_expected_ge5(n * pmf, 5.0)
    hist = np.bincount(counts, minlength=W + 1)
    chi2 = 0.0
    for lo, hi in edges:
        e = n * pmf[lo:hi].sum()
        o = hist[lo:hi].sum()
        chi2 += (o - e) ** 2 / e
    df = len(edges) - 1
    return {"n_windows": n, "W": W, "mean": mean, "exp_mean": W / 2,
            "sd": sd, "exp_sd": (W ** 0.5) / 2, "chi2": chi2, "df": df,
            "p": _chi2_sf(chi2, df), "hist": counts.tolist()}


def test_autocorr(bits, maxlag=512):
    """Autocorrelation lags 1..maxlag. s=2*bit-1; R(k)=mean(s_i s_{i+k}).
    Under the null R(k)~N(0,1/(N-k)), z=R(k)*sqrt(N-k). Bonferroni over maxlag
    lags, alpha=0.01 two-sided."""
    s = (2 * bits.astype(np.float64) - 1)
    N = len(s)
    zmax, argmax = 0.0, 0
    for k in range(1, maxlag + 1):
        r = float(np.dot(s[:N - k], s[k:])) / (N - k)
        z = abs(r) * math.sqrt(N - k)
        if z > zmax:
            zmax, argmax = z, k
    thresh = _norm_ppf(1 - (0.01 / maxlag) / 2)
    return {"maxlag": maxlag, "max_absz": zmax, "at_lag": argmax,
            "bonf_thresh": thresh, "significant": zmax > thresh}


def test_block_entropy(bits, kmax=16):
    """Empirical block entropy H_k over overlapping k-blocks (numpy, O(N*kmax)).
    Under the null H_k = k, so H_k/k -> 1. Finite-N undercounting biases H_k
    DOWN identically for the control, so the discriminating quantity is the
    difference H_k(M) - H_k(control) (computed by the caller)."""
    N = len(bits)
    b = bits.astype(np.int64)
    cur = b.copy()                            # k=1 block values
    out = {}
    for k in range(1, kmax + 1):
        if k > 1:
            cur = cur[:N - k + 1] + (b[k - 1:N] << (k - 1))
        _, counts = np.unique(cur, return_counts=True)
        tot = counts.sum()
        p = counts / tot
        out[k] = float(-(p * np.log2(p)).sum())
    return out


def test_compress(bits):
    """zlib ratio of the packed bytes; >1 within control noise = incompressible
    = supports randomness."""
    b = np.packbits(bits.astype(np.uint8), bitorder="little").tobytes()
    return len(b) / max(1, len(zlib.compress(b, 9)))


# ---------------------------------------------------------------------
# Dependency-free stats helpers (so this file stands alone re: scipy).
# ---------------------------------------------------------------------

def _chi2_sf(x, k):
    if x <= 0:
        return 1.0
    return _gammaq(k / 2.0, x / 2.0)


def _gammaq(a, x):
    if x < a + 1:
        term = 1.0 / a
        summ = term
        n = a
        for _ in range(10000):
            n += 1
            term *= x / n
            summ += term
            if abs(term) < abs(summ) * 1e-15:
                break
        return 1.0 - summ * math.exp(-x + a * math.log(x) - math.lgamma(a))
    tiny = 1e-300
    b = x + 1 - a
    c = 1 / tiny
    d = 1 / b
    h = d
    for i in range(1, 10000):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1 / d
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-15:
            break
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h


def _binom_pmf(n, k):
    if k < 0 or k > n:
        return 0.0
    return math.exp(math.lgamma(n + 1) - math.lgamma(k + 1)
                    - math.lgamma(n - k + 1) - n * math.log(2))


def _bins_expected_ge5(exp, min_exp=5.0):
    edges = []
    lo = 0
    acc = 0.0
    for c in range(len(exp)):
        acc += exp[c]
        if acc >= min_exp:
            edges.append((lo, c + 1)); lo = c + 1; acc = 0.0
    if edges and acc > 0:
        l, _ = edges[-1]
        edges[-1] = (l, len(exp))
    elif not edges:
        edges = [(0, len(exp))]
    return edges


def _norm_ppf(p):
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    pl = 0.02425
    if p < pl:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
               ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p <= 1 - pl:
        q = p - 0.5; r = q * q
        return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5]) * q / \
               (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)
    q = math.sqrt(-2 * math.log(1 - p))
    return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
            ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)


# =====================================================================
# Driver
# =====================================================================

def run_one(label, bits, control, autocorr_lag, be_kmax):
    print(f"\n########## {label}  (N={len(bits)} bits) ##########")
    ones = int(bits.sum())
    print(f"  monobit density = {ones/len(bits):.6f}  "
          f"(z = {(2*ones-len(bits))/math.sqrt(len(bits)):+.3f})")

    rl, rlc = test_runlength(bits), test_runlength(control)
    print(f"  [1] run-length vs Geometric(1/2): chi2={rl['chi2']:.2f} df={rl['df']} "
          f"p={rl['p']:.3f} | control p={rlc['p']:.3f}")
    print(f"      longest run = {rl['longest']} (control {rlc['longest']}); "
          f"log2(N) = {rl['log2N']:.1f}")

    wc, wcc = test_window_counts(bits), test_window_counts(control)
    print(f"  [2] window #ones (W={wc['W']}): mean={wc['mean']:.2f} (exp {wc['exp_mean']:.1f}), "
          f"sd={wc['sd']:.2f} (exp {wc['exp_sd']:.2f}); vs Binomial chi2={wc['chi2']:.2f} "
          f"df={wc['df']} p={wc['p']:.3f} | control p={wcc['p']:.3f}")

    ac, acc = test_autocorr(bits, autocorr_lag), test_autocorr(control, autocorr_lag)
    print(f"  [3] autocorr lags 1..{ac['maxlag']}: max|z|={ac['max_absz']:.2f} at lag "
          f"{ac['at_lag']} (Bonferroni {ac['bonf_thresh']:.2f}) -> "
          f"{'SIGNIFICANT' if ac['significant'] else 'clean'} | control max|z|={acc['max_absz']:.2f}")

    beM, beC = test_block_entropy(bits, be_kmax), test_block_entropy(control, be_kmax)
    worst = max(range(1, be_kmax + 1), key=lambda k: abs(beM[k] - beC[k]))
    print(f"  [4] block entropy (overlapping): H_1={beM[1]:.4f}, H_8/8={beM[8]/8:.4f}, "
          f"H_{be_kmax}/{be_kmax}={beM[be_kmax]/be_kmax:.4f}")
    print(f"      max |H_k(M)-H_k(control)| = {abs(beM[worst]-beC[worst]):.4f} at k={worst} "
          f"(M {beM[worst]:.3f} vs ctrl {beC[worst]:.3f})")

    cM, cC = test_compress(bits), test_compress(control)
    print(f"  [5] zlib ratio = {cM:.4f} (control {cC:.4f})")
    return {"density": ones / len(bits), "runlength": rl, "window": wc,
            "autocorr": ac, "block_entropy": beM, "block_entropy_control": beC,
            "zlib": cM}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nbits", type=int, default=131072)   # 2^17, 32x the battery
    ap.add_argument("--autocorr-lag", type=int, default=512)
    ap.add_argument("--be-kmax", type=int, default=16)
    ap.add_argument("--seed", type=int, default=20260713)
    ap.add_argument("--emit-json", type=str, default="")
    args = ap.parse_args()

    print("Validating fresh generator against anchors.md S17.7 table...")
    _validate(); print("  OK: 12/12.")

    rng = random.Random(args.seed)
    def pick_bulk():
        while True:
            w = rng.randrange(1 << 40, 1 << 64) | 1
            if w % 3 != 0:
                return w
    primary = pick_bulk()
    second = pick_bulk()
    print(f"\nprimary bulk omega = {primary}\nsecond  bulk omega = {second}")
    print(f"depth = {args.nbits} bits (2^{round(math.log2(args.nbits))}); "
          f"seed = {args.seed}\n")

    anchors = [("BULK omega (primary)", primary),
               ("BULK omega (second)", second),
               ("DEGENERATE omega=3 (M=-1 exactly)", 3),
               ("BOTTOM omega=25 (A.4.6 regular tower)", 25)]

    control = np.array([rng.randint(0, 1) for _ in range(args.nbits)], dtype=np.int8)
    bits_by_label = {}
    results = {}
    for label, w in anchors:
        bits = anchor_bits(w, args.nbits)
        bits_by_label[label] = bits
        results[label] = run_one(label, bits, control, args.autocorr_lag, args.be_kmax)

    if args.emit_json:
        import json
        plabel = anchors[0][0]
        pbits = bits_by_label[plabel]
        rlM = np.bincount(np.minimum(_run_lengths(pbits), 20), minlength=21).tolist()
        rlC = np.bincount(np.minimum(_run_lengths(control), 20), minlength=21).tolist()
        payload = {
            "nbits": args.nbits, "primary_omega": str(primary), "seed": args.seed,
            "window": {"W": results[plabel]["window"]["W"],
                       "hist": results[plabel]["window"]["hist"]},
            "runlength_M": rlM, "runlength_ctrl": rlC,
            "block_entropy_M": results[plabel]["block_entropy"],
            "block_entropy_ctrl": results[plabel]["block_entropy_control"],
        }
        with open(args.emit_json, "w") as f:
            json.dump(payload, f)
        print(f"\nwrote viz payload -> {args.emit_json}")

    print("\n" + "=" * 62)
    print("Read: a CLEAN pass = both BULK anchors match the fair-coin null on every")
    print("test (and the control), while the DEGENERATE/BOTTOM anchors visibly do not")
    print("-- proving the battery discriminates. Deep single-sequence axis, not a")
    print("statement about AEH. See anchors.md S17.7.2.")


if __name__ == "__main__":
    main()
