"""
INDEPENDENT verification of anchors.md S17.7.3 (automaticity / Christol screen).

This script is written from scratch for a delegated verification session
(briefs/anchor-automaticity-verify-brief.md). It imports NOTHING from
experiments/anchor_automaticity.py, experiments/anchor_single_deep.py, or any
other repo script. The only things taken from the repo are (a) the public
12-value worked-example table in anchors.md S17.7, used as ground truth to
validate this generator, and (b) the theorem statement (stage1-synthesis.md,
Theorem 11.8.3.6.6): for omega == 1 (mod 8),

    N(omega) = - log(omega) / log(9)   in Z_2

where log is the 2-adic (Iwasawa) logarithm, convergent on 1 + 8*Z_2 via the
usual series log(1+x) = sum_{n>=1} (-1)^(n-1) x^n / n. The anchor under test
throughout the wiki is M(omega) := N(omega^2); since omega is odd, omega^2 ==
1 (mod 8) always, so this is well-defined for every odd omega without needing
omega itself to be 1 mod 8.

Everything below -- the log series implementation, the kernel counter, the
subword-complexity counter -- is a fresh implementation, deliberately using
different code shape from the repo script (plain Python rolling-window
integers instead of numpy shift-tricks for subword complexity; a direct
valuation-exact stopping rule for the log series instead of a fixed-margin
approximation).
"""
import argparse
import math
import random
import time


# =====================================================================
# Fresh 2-adic logarithm and M(omega) generator.
# =====================================================================

def v2(n):
    """2-adic valuation of a nonzero integer n."""
    if n == 0:
        raise ValueError("v2(0) undefined")
    n = abs(n)
    k = 0
    while n & 1 == 0:
        n >>= 1
        k += 1
    return k


def log2adic(x, prec):
    """2-adic logarithm log(1+x) mod 2^prec, for x with v2(x) >= 2
    (series converges because term n has valuation >= n*v2(x) - v2(n) -> oo).

    Stopping rule: accumulate terms n = 1, 2, 3, ... and stop as soon as the
    EXACT valuation of the n-th term, n*v2(x) - v2(n), is >= prec -- i.e. we
    verify term-by-term that what's left to add cannot affect any of the low
    `prec` bits, rather than relying on a fixed safety margin.
    """
    mod = 1 << prec
    mask = mod - 1
    x &= mask
    if x == 0:
        return 0
    vx = v2(x)
    assert vx >= 2, "log series requires v2(x) >= 2 for 2-adic convergence"

    acc = 0
    xn = 1          # x^n mod 2^prec, updated each iteration
    n = 0
    while True:
        n += 1
        xn = (xn * x) & mask
        vn = v2(n)
        term_valuation = n * vx - vn
        if term_valuation >= prec:
            break
        # term = x^n / n  (2-adically): pull out 2^vn from n, invert odd part
        n_odd = n >> vn
        inv_n_odd = pow(n_odd, -1, mod)
        term = ((xn >> vn) * inv_n_odd) & mask
        if n % 2 == 1:
            acc = (acc + term) & mask
        else:
            acc = (acc - term) & mask
    return acc & mask


_LOG9_CACHE = {}

def log9(prec):
    if prec not in _LOG9_CACHE:
        _LOG9_CACHE[prec] = log2adic(8, prec)   # log(9) = log(1+8)
    return _LOG9_CACHE[prec]


def M(omega, nbits, margin=256):
    """M(omega) = N(omega^2) = -log(omega^2) / log(9), as the low `nbits`
    bits (lsb first) of the 2-adic integer, computed to `nbits+margin`
    working precision."""
    assert omega % 2 == 1, "omega must be odd"
    prec = nbits + margin
    mod = 1 << prec
    mask = mod - 1

    x = (omega * omega - 1) & mask     # omega^2 - 1, v2 >= 3 since omega odd
    if x == 0:
        return [0] * nbits             # omega^2 == 1 exactly (omega = 1)

    log_w2 = log2adic(x, prec)
    log_9 = log9(prec)
    assert v2(log_9) == 3, "sanity: v2(log 9) must be exactly 3"

    # Both log_w2 and log_9 are in 8*Z_2 by the isometry (v2 >= 3); divide out
    # the common factor of 8 before inverting, exactly as the theorem's proof
    # requires ("dividing by log 9, valuation exactly 3").
    p = prec - 3
    pmask = (1 << p) - 1
    a = (log_w2 >> 3) & pmask
    b = (log_9 >> 3) & pmask
    inv_b = pow(b, -1, 1 << p)
    N = (-(a * inv_b)) & pmask

    return [(N >> i) & 1 for i in range(nbits)]


# =====================================================================
# Ground truth: anchors.md S17.7 worked-example table (first 24 bits, lsb
# first), used ONLY to validate the generator above -- not part of the
# generator itself.
# =====================================================================

REFERENCE_TABLE = {
    1:  "000000000000000000000000",
    3:  "111111111111111111111111",
    5:  "101011110100001111101100",
    7:  "010010101101111111001101",
    11: "100110111000001010010011",
    13: "110111011010100100010110",
    17: "001100100100010001101100",
    19: "110000011010111111001110",
    23: "011001111111100000001110",
    29: "111011010111011110110011",
    31: "000101001100101110110001",
    37: "101101110100011110111111",
}


def validate_generator():
    n_ok = 0
    for omega, ref in REFERENCE_TABLE.items():
        bits = M(omega, 24)
        got = "".join(str(b) for b in bits)
        ok = (got == ref)
        n_ok += ok
        status = "OK" if ok else "MISMATCH"
        print(f"  omega={omega:3d}  got={got}  ref={ref}  [{status}]")
    print(f"Generator validation: {n_ok}/{len(REFERENCE_TABLE)}")
    return n_ok == len(REFERENCE_TABLE)


# =====================================================================
# Thue-Morse (positive control) and fair coin (negative pole).
# =====================================================================

def thue_morse_bits(n):
    return [bin(k).count("1") & 1 for k in range(n)]


def fair_coin_bits(n, rng):
    return [rng.getrandbits(1) for _ in range(n)]


# =====================================================================
# Fresh signature 1: 2-kernel growth (Eilenberg criterion).
#
# The 2-kernel of (a_i) is the family of subsequences
#     K_{e,r} = (a_{r + 2^e * n})_{n=0,1,2,...}    for e>=0, 0<=r<2^e.
# (a_i) is 2-automatic iff this family has finitely many DISTINCT elements
# as a set of sequences. We can only ever test finite prefixes, so we
# compare the first `cmp_len` terms of each K_{e,r} and count how many are
# pairwise distinct as depth e grows. Plateauing distinct-count is the
# automatic signature; unbounded growth (tracking the number of kernel
# elements generated) is the non-automatic signature.
# =====================================================================

def kernel_distinct_counts(bits, max_depth, cmp_len):
    """Returns list of (e, num_generated, num_distinct) for e=0..max_depth.
    Implementation: for each depth e, build the cmp_len-term prefix of each
    of the 2^e strided subsequences as a plain Python tuple, and track
    distinctness with a dict keyed by tuple (no numpy)."""
    N = len(bits)
    need = (1 << max_depth) * cmp_len
    assert need <= N, f"need {need} bits, have {N}"

    results = []
    seen = {}
    total_generated = 0
    for e in range(max_depth + 1):
        stride = 1 << e
        for r in range(stride):
            # subsequence K_{e,r}[n] = bits[r + stride*n], n=0..cmp_len-1
            key = tuple(bits[r + stride * n] for n in range(cmp_len))
            seen[key] = seen.get(key, 0) + 1
            total_generated += 1
        results.append((e, total_generated, len(seen)))
    return results


# =====================================================================
# Fresh signature 2: subword (factor) complexity p(k).
#
# p(k) = number of distinct length-k contiguous factors (substrings) of the
# sequence. Cobham: automatic sequences have p(k) = O(k) (linear). A fair
# coin saturates the combinatorial maximum p(k) = min(2^k, N-k+1). Implemented
# here as a rolling-window integer built with plain Python big ints (a
# different technique from any numpy shift-based vectorization).
# =====================================================================

def subword_complexity(bits, kmax):
    N = len(bits)
    out = []
    for k in range(1, kmax + 1):
        cap = min(1 << k, N - k + 1)
        if cap <= 0:
            out.append((k, 0, 0))
            continue
        mask = (1 << k) - 1
        window = 0
        for i in range(k - 1):
            window = ((window << 1) | bits[i]) & mask
        distinct = set()
        for i in range(k - 1, N):
            window = ((window << 1) | bits[i]) & mask
            distinct.add(window)
        out.append((k, len(distinct), cap))
    return out


# =====================================================================
# Driver
# =====================================================================

def run_battery(label, bits, max_depth, cmp_len, kmax, verbose=True):
    t0 = time.time()
    kg = kernel_distinct_counts(bits, max_depth, cmp_len)
    sc = subword_complexity(bits, kmax)
    dt = time.time() - t0

    final_e, final_gen, final_dist = kg[-1]
    kernel_frac = final_dist / final_gen

    if verbose:
        print(f"\n---- {label} (N={len(bits)}) [{dt:.1f}s] ----")
        print("  kernel e: gen->distinct  " +
              "  ".join(f"e{e}:{g}->{d}" for e, g, d in kg))
        print(f"  kernel final: {final_dist}/{final_gen} distinct "
              f"({'PLATEAU' if kernel_frac < 0.25 else 'GROWING'})")
        print("  subword p(k)/cap  " +
              "  ".join(f"k{k}:{d}/{c}" for k, d, c in sc))

    return {"kernel": kg, "kernel_frac": kernel_frac, "subword": sc}


def verdict_line(name, res):
    kf = res["kernel_frac"]
    sc = res["subword"]
    # crude linear-vs-exponential subword check: ratio p(kmax)/kmax vs 2^kmax
    k_last, d_last, cap_last = sc[-1]
    saturated = (d_last == cap_last)
    return (f"{name}: kernel_frac={kf:.3f}  subword@k={k_last}: {d_last}/{cap_last} "
            f"({'SATURATED' if saturated else 'not saturated'})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nbits", type=int, default=131072)
    ap.add_argument("--omega", type=int, default=4996160569905494617)
    ap.add_argument("--seed", type=int, default=987654321)
    ap.add_argument("--skip-deep-probe", action="store_true")
    args = ap.parse_args()

    print("=" * 70)
    print("STEP 1: validate fresh generator against anchors.md S17.7 table")
    print("=" * 70)
    ok = validate_generator()
    if not ok:
        print("GENERATOR VALIDATION FAILED -- stopping.")
        return
    print()

    rng = random.Random(args.seed)
    N = args.nbits
    print(f"N = {N} bits, omega under test = {args.omega}")

    tm = thue_morse_bits(N)
    coin = fair_coin_bits(N, rng)
    m_bits = M(args.omega, N)

    print("\n" + "=" * 70)
    print("STEP 2: linchpin -- Thue-Morse control at repo-matching settings")
    print("        (max_depth=10, cmp_len=96, kmax=18)")
    print("=" * 70)
    r_tm = run_battery("THUE-MORSE (must be flagged automatic)", tm, 10, 96, 18)
    r_coin = run_battery("FAIR COIN (must be flagged non-automatic)", coin, 10, 96, 18)
    r_M = run_battery(f"M(omega={args.omega})", m_bits, 10, 96, 18)

    tm_kernel_plateau = (r_tm["kernel"][-1][2] == 2)
    tm_subword_linear = (r_tm["subword"][-1][1] < 100)  # well below any saturation
    print(f"\nLINCHPIN CHECK: Thue-Morse kernel plateaus at exactly 2? "
          f"{'YES' if tm_kernel_plateau else 'NO -- ' + str(r_tm['kernel'][-1][2])}")
    print(f"LINCHPIN CHECK: Thue-Morse subword complexity stays low (non-saturated)? "
          f"{'YES' if tm_subword_linear else 'NO'}")

    if not (tm_kernel_plateau and tm_subword_linear):
        print("\n*** LINCHPIN FAILED: independent test does not flag Thue-Morse as")
        print("*** automatic. STOPPING -- no conclusion about M(omega) is valid.")
        return

    print("\n" + "=" * 70)
    print("STEP 3: side-by-side summary at repo-matching settings")
    print("=" * 70)
    print(" ", verdict_line("Thue-Morse", r_tm))
    print(" ", verdict_line("Fair coin ", r_coin))
    print(" ", verdict_line("M(omega)  ", r_M))

    if args.skip_deep_probe:
        return

    print("\n" + "=" * 70)
    print("STEP 4: false-negative probe -- push kernel depth and subword k")
    print("        further than the repo script, to see if a plateau ever")
    print("        starts appearing for M(omega) that was hidden at shallower")
    print("        depth. Kernel depth 12 needs cmp_len <= N/2^12 = 32.")
    print("        Subword k up to 20: note 2^20 > N, so p(k) is CEILING-")
    print("        capped at N-k+1 regardless of any structure -- that cap")
    print("        must not be mistaken for a plateau.")
    print("=" * 70)
    r_tm2 = run_battery("THUE-MORSE deep (depth=12,cmp=32,kmax=20)", tm, 12, 32, 20)
    r_coin2 = run_battery("FAIR COIN deep (depth=12,cmp=32,kmax=20)", coin, 12, 32, 20)
    r_M2 = run_battery(f"M(omega) deep (depth=12,cmp=32,kmax=20)", m_bits, 12, 32, 20)

    print("\nFinite-N saturation ceiling check (subword):")
    for k, d, cap in r_M2["subword"]:
        ceiling_bound = N - k + 1
        combinatorial_bound = 1 << k
        print(f"  k={k:2d}: p(k)={d:7d}  cap=min(2^k, N-k+1)={cap:7d}  "
              f"(2^k={combinatorial_bound}, N-k+1={ceiling_bound})")

    print("\n" + "=" * 70)
    print("STEP 5: final side-by-side, deep probe")
    print("=" * 70)
    print(" ", verdict_line("Thue-Morse (deep)", r_tm2))
    print(" ", verdict_line("Fair coin  (deep)", r_coin2))
    print(" ", verdict_line("M(omega)   (deep)", r_M2))

    # Explicit plateau check for M(omega) at deepest kernel depth
    e_last, gen_last, dist_last = r_M2["kernel"][-1]
    print(f"\nM(omega) kernel at deepest depth e={e_last}: {dist_last}/{gen_last} distinct "
          f"({'ALL DISTINCT -- no plateau' if dist_last == gen_last else 'SOME COLLISION -- check'})")


if __name__ == "__main__":
    main()
