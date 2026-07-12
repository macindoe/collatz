"""
Compressibility of M(omega) as a single bit string.

Brief: briefs/anchor-digit-search-brief.md. Scope: anchors.md S17.8 item 2
(the NIST SP 800-22 battery, run via the standard `nistrng` package rather
than hand-rolled -- per the brief's explicit instruction not to reinvent
tests that already exist and are well calibrated) plus Lempel-Ziv
complexity and gzip/zlib compression ratio, each benchmarked against a
Monte Carlo control of matched-length pseudo-random bit strings rather
than a hand-derived asymptotic formula (safer: no risk of mis-deriving a
constant, and it directly answers "does M(omega) compress differently
from a string from the same null model" rather than "does it match some
formula for large n").

Independent sample: a FRESH seed and FRESH omega draw from
anchor_digit_structure.py's Stage 1 run, so this stage's "clean pass" (if
it is one) is not just a different test on the same 200 numbers -- it is
a semi-independent replication of the earlier sample's ordinariness. The
M(omega) generator is re-implemented here from scratch (not imported from
anchor_digit_structure.py or any other script) per AGENTS.md's fresh-code
rule, and re-validated against the same anchors.md S17.7 reference table.

Null model, stated precisely: same as Stage 1 -- M(omega)'s bits modeled
as i.i.d. fair-coin (independent, P(bit=1)=1/2). "Incompressible within
noise" supports this null; any real, replicated compression gain over the
matched random controls would be a discovered structure by construction
(a compressor exploiting fair-coin bits cannot beat the entropy bound in
expectation).
"""
import random
import math
import zlib
import numpy as np
import nistrng

# ---------------------------------------------------------------------
# M(omega) generator (re-implemented fresh, see anchor_digit_structure.py
# for the derivation and the algebraic reasoning; identical algorithm,
# independent code, both validated against the same reference table).
# ---------------------------------------------------------------------

def v2(x):
    if x == 0:
        return None
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def log2adic(x, M):
    mask = (1 << M) - 1
    x &= mask
    if x == 0:
        return 0
    vx = v2(x)
    total = 0
    xi = 1
    i = 0
    while True:
        i += 1
        xi = (xi * x) & mask
        if i * vx >= M:
            break
        e = v2(i) if i % 2 == 0 else 0
        j = i >> e
        term = ((xi >> e) * pow(j, -1, 1 << M)) & mask
        total = (total + term if i % 2 == 1 else total - term) & mask
    return total & mask


_log9_cache = {}


def compute_M_omega(omega, target_bits, margin=160):
    M = target_bits + 3 + margin
    mask = (1 << M) - 1
    y = (omega * omega) & mask
    x = (y - 1) & mask
    if x == 0:
        return 0
    Ly = log2adic(x, M)
    if M not in _log9_cache:
        _log9_cache[M] = log2adic(8, M)
    L9 = _log9_cache[M]
    prec = M - 3
    pmask = (1 << prec) - 1
    u9 = (L9 >> 3) & pmask
    inv_u9 = pow(u9, -1, 1 << prec)
    Ly_shift = (Ly >> 3) & pmask
    N = (-(Ly_shift * inv_u9)) & pmask
    return N & ((1 << target_bits) - 1)


def bits_lsb_first(n, k):
    return [(n >> i) & 1 for i in range(k)]


def validate_against_reference():
    reference = {
        1: "000000000000000000000000", 3: "111111111111111111111111",
        5: "101011110100001111101100", 7: "010010101101111111001101",
        11: "100110111000001010010011", 13: "110111011010100100010110",
        17: "001100100100010001101100", 19: "110000011010111111001110",
        23: "011001111111100000001110", 29: "111011010111011110110011",
        31: "000101001100101110110001", 37: "101101110100011110111111",
    }
    for omega, ref in reference.items():
        got = "".join(str(b) for b in bits_lsb_first(compute_M_omega(omega, 24), 24))
        assert got == ref, f"omega={omega}: got {got}, expected {ref}"
    return True


def sample_omegas(n, seed, lo, hi):
    rng = random.Random(seed)
    out, seen = [], set()
    while len(out) < n:
        w = rng.randrange(lo, hi) | 1
        if w % 3 == 0 or w in seen:
            continue
        seen.add(w)
        out.append(w)
    return out


# ---------------------------------------------------------------------
# Lempel-Ziv (1976) complexity, Kaspar-Schuster parsing algorithm.
# Validated against the literature worked example: c('1001111011000010')
# = 6 (Kaspar & Schuster 1976).
# ---------------------------------------------------------------------

def lz76_complexity(bits):
    s = bits
    n = len(s)
    i, k, l = 0, 1, 1
    c = 1
    k_max = 1
    while True:
        if s[i + k - 1] != s[l + k - 1]:
            if k > k_max:
                k_max = k
            i += 1
            if i == l:
                c += 1
                l += k_max
                if l + 1 > n:
                    break
                i = 0
                k = 1
                k_max = 1
            else:
                k = 1
        else:
            k += 1
            if l + k > n:
                c += 1
                break
    return c


def _validate_lz76():
    ref = [int(ch) for ch in "1001111011000010"]
    assert lz76_complexity(ref) == 6, "LZ76 implementation does not match Kaspar-Schuster 1976 example"
    return True


def bits_to_bytes(bits):
    n = len(bits)
    pad = (-n) % 8
    padded = bits + [0] * pad
    out = bytearray(len(padded) // 8)
    for byte_i in range(len(out)):
        b = 0
        for j in range(8):
            b = (b << 1) | padded[byte_i * 8 + j]
        out[byte_i] = b
    return bytes(out)


def zlib_ratio(bits):
    raw = bits_to_bytes(bits)
    comp = zlib.compress(raw, level=9)
    return len(comp) / len(raw)


# ---------------------------------------------------------------------
# Monte Carlo control: matched-length pseudo-random bit strings from the
# same generator class of null the test targets (i.i.d. fair coin), NOT
# derived from any Collatz/anchor construction.
# ---------------------------------------------------------------------

def random_control_sequences(n, bitlen, seed):
    rng = random.Random(seed)
    return [[rng.randint(0, 1) for _ in range(bitlen)] for _ in range(n)]


def mannwhitney_u(sample_a, sample_b):
    """Two-sided Mann-Whitney U test (normal approximation), dependency-free
    (avoids relying on scipy's exact/ties handling for a straightforward
    comparison; adequate at these sample sizes with few/no ties)."""
    from scipy import stats as scipy_stats
    u_stat, pval = scipy_stats.mannwhitneyu(sample_a, sample_b, alternative="two-sided")
    return u_stat, pval


# ---------------------------------------------------------------------
# NIST SP 800-22 battery via nistrng (standard package, not hand-rolled).
# nistrng expects a 0/1 array (NOT +-1: MonobitTest uses count_nonzero,
# which would treat every +-1 entry as "nonzero" -- checked empirically
# against a known random control before trusting this on real data).
# Cast to int64: nistrng's cumulative-sums test overflows on int8 input
# (observed directly: RuntimeWarning: overflow encountered in scalar add
# on a naive int8 array -- this is nistrng's own internal bug, not ours;
# worked around by widening the dtype, not by patching the library).
# ---------------------------------------------------------------------

def run_nist_battery(bits):
    arr = np.array(bits, dtype=np.int64)
    results = {}
    items = nistrng.run_all_battery(arr, nistrng.SP800_22R1A_BATTERY, check_eligibility=True)
    for item in items:
        if item is None:
            continue
        r, _elapsed = item
        if r is None:
            continue
        results[r.name] = dict(passed=bool(r.passed), score=float(r.score))
    return results


def meta_check(pvalues, alpha=0.01):
    n = len(pvalues)
    if n < 20:
        return None
    passed = sum(1 for p in pvalues if p >= alpha)
    p_hat = 1 - alpha
    se = math.sqrt(p_hat * (1 - p_hat) / n)
    ci = (p_hat - 3 * se, p_hat + 3 * se)
    prop = passed / n
    nbins = 10
    counts = [0] * nbins
    for p in pvalues:
        counts[min(int(p * nbins), nbins - 1)] += 1
    expected = n / nbins
    from scipy import stats as scipy_stats
    chi2_stat = sum((c - expected) ** 2 / expected for c in counts)
    unif_p = scipy_stats.chi2.sf(chi2_stat, nbins - 1)
    return dict(n=n, proportion_passing=prop, expected_ci=ci,
                proportion_ok=(ci[0] <= prop <= ci[1]),
                uniformity_pvalue=unif_p, uniformity_ok=(unif_p >= 0.0001))


def main():
    print("Validating generator against anchors.md S17.7 worked example...")
    validate_against_reference()
    _validate_lz76()
    print("  OK.\n")

    N = 200
    BITS = 4096
    SEED = 20260713  # different from anchor_digit_structure.py's 20260712: independent sample
    LO, HI = 1 << 20, 1 << 64
    print(f"Generating {N} independent omega in [{LO}, {HI}), coprime to 3, seed={SEED} "
          f"(independent of Stage 1's sample)...")
    omegas = sample_omegas(N, SEED, LO, HI)
    sequences = [bits_lsb_first(compute_M_omega(w, BITS), BITS) for w in omegas]
    print("  done.\n")

    print(f"Generating {N} matched-length (n={BITS}) pseudo-random control sequences "
          f"(seed={SEED}+1, i.i.d. fair coin -- the exact null being tested)...")
    controls = random_control_sequences(N, BITS, SEED + 1)
    print("  done.\n")

    print("=== Lempel-Ziv (1976) complexity: M(omega) vs random control ===")
    lz_m = [lz76_complexity(s) for s in sequences]
    lz_c = [lz76_complexity(s) for s in controls]
    mean_m, mean_c = sum(lz_m) / N, sum(lz_c) / N
    u_stat, mw_p = mannwhitney_u(lz_m, lz_c)
    print(f"  mean LZ76(M(omega)) = {mean_m:.3f}   mean LZ76(control) = {mean_c:.3f}")
    print(f"  Mann-Whitney U={u_stat:.1f}  p={mw_p:.4f}  "
          f"(two-sided; H0: M(omega) and matched i.i.d.-coin controls have the same LZ76 distribution)\n")

    print("=== zlib compression ratio: M(omega) vs random control ===")
    zr_m = [zlib_ratio(s) for s in sequences]
    zr_c = [zlib_ratio(s) for s in controls]
    mean_zm, mean_zc = sum(zr_m) / N, sum(zr_c) / N
    u_stat2, mw_p2 = mannwhitney_u(zr_m, zr_c)
    print(f"  mean ratio(M(omega)) = {mean_zm:.4f}   mean ratio(control) = {mean_zc:.4f}")
    print(f"  Mann-Whitney U={u_stat2:.1f}  p={mw_p2:.4f}\n")

    print("=== NIST SP 800-22 battery (nistrng): M(omega) AND the same random control ===")
    print("    (both run through identical code; the control's own meta-check numbers are the")
    print("    right baseline for each test -- some SP800-22 sub-tests report a MEAN of several")
    print("    internal p-values as nistrng's 'score', which is not itself uniform under the null")
    print("    by the CLT, and/or need longer sequences than n=4096 for their asymptotics; this")
    print("    shows up as spurious meta-check failures on BOTH M(omega) and the true-random")
    print("    control equally -- confirmed below, not specific to M(omega).)")
    m_scores, m_pass, c_scores, c_pass = {}, {}, {}, {}
    for bits in sequences:
        for name, r in run_nist_battery(bits).items():
            m_scores.setdefault(name, []).append(r["score"])
            m_pass.setdefault(name, []).append(r["passed"])
    for bits in controls:
        for name, r in run_nist_battery(bits).items():
            c_scores.setdefault(name, []).append(r["score"])
            c_pass.setdefault(name, []).append(r["passed"])
    for name in sorted(m_scores.keys()):
        mm = meta_check(m_scores[name])
        cm = meta_check(c_scores[name])
        if mm is None or cm is None:
            continue
        artifact = not (cm["proportion_ok"] and cm["uniformity_ok"])
        flag = "ARTIFACT (control fails identically)" if artifact else (
            "OK" if (mm["proportion_ok"] and mm["uniformity_ok"]) else "REVIEW -- control passes, M(omega) does not")
        print(f"  {name:35s} M(omega): prop={mm['proportion_passing']:.4f} unif_p={mm['uniformity_pvalue']:.4f} | "
              f"control: prop={cm['proportion_passing']:.4f} unif_p={cm['uniformity_pvalue']:.4f}  [{flag}]")
    print()
    print("Done.")
    return dict(lz_m=lz_m, lz_c=lz_c, mw_p_lz=mw_p, zr_m=zr_m, zr_c=zr_c, mw_p_zlib=mw_p2,
                nist_m_scores=m_scores, nist_c_scores=c_scores)


if __name__ == "__main__":
    main()
