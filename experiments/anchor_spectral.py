"""
Spectral flatness of M(omega) as a single bit string.

Brief: briefs/anchor-digit-search-brief.md. Scope: anchors.md S17.8 item
3 (spectral test), queued as a "if time remains" item after the core
battery and compressibility stages -- included since time allowed.

The anchor is built from a discrete log mod 2^k, not obviously periodic
but untested (S17.8.3's own framing) -- this checks rather than assumes.
Rather than deriving the periodogram's exact theoretical null
distribution by hand (risk of mis-deriving a scaling constant, same
concern that motivated the Monte-Carlo-control approach in
anchor_compressibility.py), this compares the pooled periodogram of
M(omega) against the pooled periodogram of a matched-length i.i.d.-coin
control via a two-sample Kolmogorov-Smirnov test -- directly answers
"does M(omega)'s spectrum look like noise's spectrum" without needing a
closed-form null.

Independent sample (fresh seed, disjoint from the two earlier stages)
and independent generator re-implementation, re-validated against the
same anchors.md S17.7 table, per AGENTS.md's fresh-code-per-claim rule.
"""
import random
import numpy as np
from scipy import stats


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


def periodogram_pm1(bits):
    """Periodogram of the +-1-mapped sequence, positive frequencies only
    (excluding DC and, for even n, the Nyquist bin), normalized by n so
    the scale is comparable across sequences."""
    pm = np.array(bits, dtype=np.float64) * 2 - 1
    n = len(pm)
    X = np.fft.rfft(pm)
    mag2 = (np.abs(X) ** 2) / n
    return mag2[1:-1] if n % 2 == 0 else mag2[1:]


def main():
    print("Validating generator against anchors.md S17.7 worked example...")
    validate_against_reference()
    print("  OK.\n")

    N = 200
    BITS = 4096
    SEED = 20260714  # fresh, disjoint from 20260712 (Stage 1) and 20260713 (Stage 2)
    LO, HI = 1 << 20, 1 << 64
    print(f"Generating {N} independent omega (seed={SEED}) and a matched i.i.d.-coin control...")
    omegas = sample_omegas(N, SEED, LO, HI)
    sequences = [bits_lsb_first(compute_M_omega(w, BITS), BITS) for w in omegas]
    rng = random.Random(SEED + 1)
    controls = [[rng.randint(0, 1) for _ in range(BITS)] for _ in range(N)]
    print("  done.\n")

    print("=== Spectral flatness: pooled periodogram, M(omega) vs matched i.i.d.-coin control ===")
    pooled_m = np.concatenate([periodogram_pm1(s) for s in sequences])
    pooled_c = np.concatenate([periodogram_pm1(s) for s in controls])
    ks_stat, ks_p = stats.ks_2samp(pooled_m, pooled_c)
    print(f"  pooled periodogram ordinates: {len(pooled_m)} (M(omega)), {len(pooled_c)} (control)")
    print(f"  mean|X_k|^2/n: M(omega)={pooled_m.mean():.3f}  control={pooled_c.mean():.3f}  "
          f"(both should be near 1.0 for a fair-coin sequence)")
    print(f"  two-sample KS: D={ks_stat:.5f}  p={ks_p:.4f}  "
          f"(H0: M(omega)'s periodogram and the control's are draws from the same distribution)")

    print("\n  Per-sequence peak check (NIST-style: count ordinates exceeding the 95th-percentile")
    print("  threshold T=sqrt(n*ln(1/0.05)) under the null; d=(N1-N0)/sqrt(n*0.95*0.05/4) ~ N(0,1)):")
    # mag2 here is |X_k|^2/n; NIST's own threshold on |X_k| (not squared, not /n) is
    # sqrt(n*log(1/0.05)); squaring and dividing by n gives threshold log(1/0.05) on our mag2 scale.
    thresh = np.log(1 / 0.05)
    d_m = []
    for s in sequences:
        p = periodogram_pm1(s)
        n1 = np.sum(p < thresh)
        n0 = 0.95 * len(p)
        d = (n1 - n0) / np.sqrt(len(p) * 0.95 * 0.05 / 4)
        d_m.append(d)
    d_c = []
    for s in controls:
        p = periodogram_pm1(s)
        n1 = np.sum(p < thresh)
        n0 = 0.95 * len(p)
        d = (n1 - n0) / np.sqrt(len(p) * 0.95 * 0.05 / 4)
        d_c.append(d)
    d_m, d_c = np.array(d_m), np.array(d_c)
    print(f"  d-statistic mean/std: M(omega)={d_m.mean():.3f}/{d_m.std():.3f}  "
          f"control={d_c.mean():.3f}/{d_c.std():.3f}  (both ~N(0,1) under the null)")
    ks_stat2, ks_p2 = stats.ks_2samp(d_m, d_c)
    print(f"  two-sample KS on d-statistics: D={ks_stat2:.5f}  p={ks_p2:.4f}")
    print("\nDone.")


if __name__ == "__main__":
    main()
