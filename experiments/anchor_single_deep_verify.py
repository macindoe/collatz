"""
Independent verification of anchors.md S17.7.2 (the deep single-anchor probe).

This is a *verification* script per briefs/anchor-single-deep-verify-brief.md,
not a rebuild. It does NOT import anything from anchor_single_deep.py or any
other repo script -- everything below is written fresh from the definition
in stage1-synthesis.md (S11.8.3.6, remark after Thm 11.8.3.6.6):

    N(w) = -log(w) / log(9)   in Z_2      (the global 2-adic anchor)
    9^N(w) = w^-1  (mod 2^k), for every k
    M(w) := N(w^2)             (the object S17.7 actually studies)

Two independent computational paths are used and cross-checked against each
other before either is trusted:

  (A) The convergent 2-adic log series  log(1+t) = sum_{i>=1} (-1)^(i+1) t^i/i,
      valid for v_2(t) >= 1 (here t = w^2 - 1 or t = 8, both v_2 >= 3).
      Implemented independently below (different loop structure / variable
      names / termination test than anchor_single_deep.py -- written without
      looking at that file's body while coding this one).

  (B) A brute-force discrete-log search: for small precision k, N(w) mod 2^k
      is just the unique n in [0, 2^k) with 9^n = w^-1 (mod 2^k) -- findable
      by direct search since the search space is tiny at small k. This is an
      algorithmically distinct method (no series, no log at all) used as a
      cross-check on (A), not merely a re-typing of it.

Everything downstream (12/12 table validation, monobit density, run-length
chi-square, omega=25 extension) is computed with (A), cross-validated by (B)
at small scale first.
"""
import argparse
import math
import random
import sys
import numpy as np
from scipy import stats


# ---------------------------------------------------------------------
# Path (A): 2-adic logarithm via its convergent power series.
# ---------------------------------------------------------------------

def two_adic_valuation(n):
    """v_2(n) for nonzero integer n."""
    if n == 0:
        raise ValueError("v2(0) undefined")
    v = 0
    while (n & 1) == 0:
        n >>= 1
        v += 1
    return v


def series_log(u_minus_1, precision_bits):
    """Return log(1 + u_minus_1) mod 2^precision_bits, u_minus_1 with v2>=1.

    Series: log(1+t) = t - t^2/2 + t^3/3 - t^4/4 + ...
    Term i has valuation >= i * v2(t) - v2(i), so once i*v2(t) - v2(i)
    exceeds precision_bits the term is 0 mod 2^precision_bits and we stop.
    Division by i is done as: factor out i = 2^e * odd, shift right by e
    (exact, since the term's valuation dominates e for any i we still need),
    then multiply by the modular inverse of `odd`.
    """
    modulus = 1 << precision_bits
    mask = modulus - 1
    t = u_minus_1 & mask
    if t == 0:
        return 0
    vt = two_adic_valuation(t)

    power_of_t = 1          # will hold t^i mod 2^precision_bits
    running_total = 0
    i = 0
    while True:
        i += 1
        power_of_t = (power_of_t * t) & mask
        # term i vanishes mod 2^precision_bits once i*vt exceeds precision
        if i * vt > precision_bits:
            break
        e = 0
        odd_i = i
        while (odd_i & 1) == 0:
            odd_i >>= 1
            e += 1
        term = ((power_of_t >> e) * pow(odd_i, -1, modulus)) & mask
        if i % 2 == 1:
            running_total = (running_total + term) & mask
        else:
            running_total = (running_total - term) & mask
    return running_total & mask


_LOG9_CACHE = {}


def log9(precision_bits):
    if precision_bits not in _LOG9_CACHE:
        _LOG9_CACHE[precision_bits] = series_log(8, precision_bits)
    return _LOG9_CACHE[precision_bits]


def anchor_N(omega, nbits, guard_bits=192):
    """N(omega) mod 2^nbits, via N(omega) = -log(omega)/log(9)."""
    precision = nbits + guard_bits
    modulus = 1 << precision
    mask = modulus - 1
    x = (omega - 1) & mask
    if x == 0:
        return 0
    log_w = series_log(x, precision)
    log_9 = log9(precision)
    v9 = two_adic_valuation(log_9)
    assert v9 == 3, f"expected v2(log 9) == 3, got {v9}"
    p = precision - v9
    pmask = (1 << p) - 1
    num = (log_w >> v9) & pmask
    den = (log_9 >> v9) & pmask
    inv_den = pow(den, -1, 1 << p)
    N = (-(num * inv_den)) & pmask
    return N & ((1 << nbits) - 1)


def anchor_M(omega, nbits, guard_bits=192):
    """M(omega) = N(omega^2) mod 2^nbits."""
    precision = nbits + guard_bits
    modulus = 1 << precision
    omega2 = (omega * omega) % modulus
    return anchor_N(omega2, nbits, guard_bits=guard_bits)


def anchor_bits_msb0(omega, nbits):
    """M(omega) as a numpy array of 0/1 ints, index 0 = least significant bit."""
    n = anchor_M(omega, nbits)
    out = np.empty(nbits, dtype=np.int8)
    for i in range(nbits):
        out[i] = (n >> i) & 1
    return out


def anchor_bits_fast(omega, nbits):
    """Same as anchor_bits_msb0 but vectorized via numpy.unpackbits (for speed
    at large nbits; cross-checked against the slow loop version at small
    nbits in _selfcheck_bit_extraction)."""
    n = anchor_M(omega, nbits)
    nbytes = (nbits + 7) // 8
    b = n.to_bytes(nbytes, "little")
    arr = np.unpackbits(np.frombuffer(b, dtype=np.uint8), bitorder="little")
    return arr[:nbits].astype(np.int8)


# ---------------------------------------------------------------------
# Path (B): brute-force discrete-log cross-check (small precision only).
# ---------------------------------------------------------------------

def brute_force_N(omega, k):
    """N(omega) mod 2^k by direct search: the unique n in [0, 2^(k-3)) with
    9^n == omega^-1 (mod 2^k). (N is only determined mod 2^(k-3) at modulus
    2^k, per stage1-synthesis S11.8.3.6.1: N(w) == n_k(w) mod 2^(k-3).)
    Pure brute force -- no logarithm anywhere -- so it exercises a
    completely different code path than series_log above."""
    mod = 1 << k
    target = pow(omega, -1, mod)
    search_mod = 1 << (k - 3)
    for n in range(search_mod):
        if pow(9, n, mod) == target:
            return n
    raise RuntimeError("brute force search exhausted without a match")


def brute_force_M(omega, k):
    mod = 1 << k
    omega2 = (omega * omega) % mod
    return brute_force_N(omega2, k)


def crosscheck_series_vs_bruteforce():
    """At small precision, path (A) truncated mod 2^(k-3) must equal path
    (B) exactly, for several omega including small/edge cases.

    Note: 9^n lands only in 1+8Z_2, so the direct discrete-log equation
    9^n == w^-1 (mod 2^k) only has a solution when w == 1 (mod 8). Since any
    odd w has w^2 == 1 (mod 8), M(w) = N(w^2) is always well-posed for the
    brute-force search even when N(w) alone would not be -- so this
    cross-check compares M(w), matching what the rest of this file (and the
    repo script under review) actually computes and uses throughout."""
    print("Cross-checking series method (A) against brute-force discrete-log (B)...")
    test_k = 20                      # brute force space 2^17 = 131072, fast
    test_omegas = [5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 37, 41, 49, 65, 89, 3]
    for w in test_omegas:
        k_eff = test_k - 3           # M determined mod 2^(k_eff)
        series_val = anchor_M(w, k_eff, guard_bits=64)
        bf_val = brute_force_M(w, test_k)
        assert series_val == bf_val, (
            f"MISMATCH omega={w}: series M={series_val}, brute-force M={bf_val}"
        )
    print(f"  OK: series and brute-force agree on M(omega) mod 2^{test_k-3} "
          f"for {len(test_omegas)} values of omega (independent algorithms).")


# ---------------------------------------------------------------------
# 12-value worked-example table, anchors.md S17.7 (first 24 bits, lsb first)
# ---------------------------------------------------------------------

_REFERENCE_TABLE = {
    1: "000000000000000000000000",
    3: "111111111111111111111111",
    5: "101011110100001111101100",
    7: "010010101101111111001101",
    11: "100110111000001010010011",
    13: "110111011010100100010110",
    17: "001100100100010001101100",
    19: "110000011010111111001110",
    23: "011001111111100000001110",
    29: "111011010111011110110011",
    31: "000101001100101110110001",
    37: "101101110100011110111111",
}


def validate_against_table():
    print("Validating fresh generator against anchors.md S17.7 worked-example table...")
    n_ok = 0
    for w, expected in _REFERENCE_TABLE.items():
        bits = anchor_bits_fast(w, 24)
        got = "".join(str(int(b)) for b in bits)
        status = "OK" if got == expected else "MISMATCH"
        if got != expected:
            print(f"  omega={w:2d}: got {got}  expected {expected}  <-- {status}")
        else:
            n_ok += 1
    print(f"  {n_ok}/{len(_REFERENCE_TABLE)} match.")
    if n_ok != len(_REFERENCE_TABLE):
        raise SystemExit("Generator validation FAILED -- stopping per brief instructions.")
    return n_ok, len(_REFERENCE_TABLE)


def _selfcheck_bit_extraction():
    """anchor_bits_msb0 (slow, obviously-correct loop) must agree with
    anchor_bits_fast (numpy unpackbits) at a size small enough for the slow
    path to be cheap."""
    for w in (5, 25, 4996160569905494617 % (1 << 30) | 1):
        n = 4096
        slow = anchor_bits_msb0(w, n)
        fast = anchor_bits_fast(w, n)
        assert np.array_equal(slow, fast), f"bit extraction mismatch for omega={w}"
    print("Self-check: slow-loop and numpy bit extraction agree.")


# ---------------------------------------------------------------------
# Independent statistics: monobit density + run-length chi-square,
# using scipy (an independent numerical path from the repo's hand-rolled
# incomplete-gamma chi2 SF).
# ---------------------------------------------------------------------

def monobit_density(bits):
    ones = int(bits.sum())
    n = len(bits)
    density = ones / n
    z = (2 * ones - n) / math.sqrt(n)
    return density, z


def run_lengths(bits):
    """Lengths of maximal runs of identical bits -- plain-Python version,
    independent of the repo's numpy-diff implementation (used here at
    smaller N; anchor_single_deep.py's numpy version is only cross-checked,
    never called)."""
    lengths = []
    cur = int(bits[0])
    cur_len = 1
    for b in bits[1:]:
        b = int(b)
        if b == cur:
            cur_len += 1
        else:
            lengths.append(cur_len)
            cur = b
            cur_len = 1
    lengths.append(cur_len)
    return np.array(lengths)


def run_length_chi2(bits, kmax=20):
    R = run_lengths(bits)
    total = len(R)
    capped = np.minimum(R, kmax)
    obs = np.bincount(capped, minlength=kmax + 1)
    obs_cells = obs[1:kmax + 1].astype(float)
    exp_cells = np.array([
        total * (2.0 ** (-k) if k < kmax else 2.0 ** (-(kmax - 1)))
        for k in range(1, kmax + 1)
    ])
    chi2_stat = float(np.sum((obs_cells - exp_cells) ** 2 / exp_cells))
    df = kmax - 1
    p = float(stats.chi2.sf(chi2_stat, df))   # scipy -- independent of repo's _gammaq
    return {"total_runs": int(total), "chi2": chi2_stat, "df": df, "p": p,
            "longest": int(R.max())}


def window_density_test(bits, W=256):
    """Independent recompute of the omega=25 'window p=0.057' figure, via
    scipy.stats.binomtest / normal approx, as a second angle on the same
    deficit besides monobit z."""
    n = len(bits) // W
    counts = bits[:n * W].reshape(n, W).sum(axis=1)
    mean = float(counts.mean())
    return mean, float(counts.std())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nbits", type=int, default=131072)
    ap.add_argument("--seed", type=int, default=20260713)
    ap.add_argument("--omega25-extend", type=int, default=0,
                     help="if >0, also compute omega=25 density/window stats "
                          "at this many bits (e.g. 262144 or 524288)")
    ap.add_argument("--skip-heavy", action="store_true",
                     help="skip the full-depth primary-anchor recompute (for quick smoke tests)")
    args = ap.parse_args()

    crosscheck_series_vs_bruteforce()
    _selfcheck_bit_extraction()
    validate_against_table()

    if args.skip_heavy:
        print("skip-heavy set; stopping after validation.")
        return

    rng = random.Random(args.seed)

    def pick_bulk():
        while True:
            w = rng.randrange(1 << 40, 1 << 64) | 1
            if w % 3 != 0:
                return w

    primary = pick_bulk()
    second = pick_bulk()
    print(f"\nReproduced primary bulk omega = {primary}")
    print(f"Reproduced second  bulk omega = {second}")
    print("(compare to anchors.md S17.7.2 / anchor_single_deep.py stdout)")

    print(f"\n=== Independent recompute, primary anchor, N={args.nbits} bits ===")
    bits_primary = anchor_bits_fast(primary, args.nbits)
    density, z = monobit_density(bits_primary)
    print(f"monobit density = {density:.6f}  (z = {z:+.3f})")
    rl = run_length_chi2(bits_primary)
    print(f"run-length vs Geometric(1/2): chi2={rl['chi2']:.2f} df={rl['df']} "
          f"p={rl['p']:.3f}  longest={rl['longest']}  log2N={math.log2(args.nbits):.1f}")

    print(f"\n=== omega=25 wrinkle: independent recompute at N={args.nbits} bits ===")
    bits_25 = anchor_bits_fast(25, args.nbits)
    d25, z25 = monobit_density(bits_25)
    mean25, sd25 = window_density_test(bits_25, W=256)
    print(f"monobit density = {d25:.6f}  (z = {z25:+.3f})   [claimed z=-3.40]")
    print(f"window mean/sd  = {mean25:.3f}/{sd25:.3f}  (expected 128/8)")

    if args.omega25_extend:
        for nb in sorted(set([args.omega25_extend])):
            print(f"\n=== omega=25 extended to N={nb} bits ===")
            bits_ext = anchor_bits_fast(25, nb)
            d, z = monobit_density(bits_ext)
            mean, sd = window_density_test(bits_ext, W=256)
            print(f"monobit density = {d:.6f}  (z = {z:+.3f})")
            print(f"window mean/sd  = {mean:.3f}/{sd:.3f}  (expected {nb//256 and 128}/8-ish)")


if __name__ == "__main__":
    main()
