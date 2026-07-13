"""
Automaticity / algebraicity screen on the anchor M(omega).

Motivation (anchors.md S17.7.2 follow-up, 2026-07-13): every test in S17.7 so
far is STATISTICAL -- it asks whether M(omega)'s bits look like a fair coin.
There is a different, STRUCTURAL notion of order that no statistical test sees:
is the bit sequence 2-AUTOMATIC -- i.e. produced by a finite automaton reading
the base-2 digits of the index n?

Why this is the right structural question. By CHRISTOL'S THEOREM (Christol 1979;
Christol-Kamae-Mendes France-Rauzy 1980), a sequence (a_n) over F_2 is
2-automatic IFF its generating function F(x) = sum a_n x^n is ALGEBRAIC over
F_2(x). And by Eilenberg's theorem, (a_n) is 2-automatic IFF its 2-KERNEL

    K_2(a) = { (a_{2^e n + r})_{n>=0} : e >= 0, 0 <= r < 2^e }

is FINITE. So "is M(omega) algebraic over F_2(x)?" = "is its 2-kernel finite?" =
a decidable-in-practice screen. A POSITIVE result (finite kernel) would be a
genuine, non-statistical structure -- far stronger than any correlation. A
NEGATIVE result (kernel grows without bound) rules out the whole algebraic /
automatic family of order, and is itself a clean, meaningful finding: it is the
structural complement to S17.7.2's statistical clean pass.

This is NOT a statement about AEH, and NOT proof effort -- it is a structure
hunt under README's "experiments may feed the ledger" clause, same standing as
S17.7.

Design. Two independent automaticity signatures, each run on THREE sequences so
the test's own discriminating power is visible:
  * THUE-MORSE  -- the textbook 2-automatic sequence (kernel size 2). POSITIVE
                   control: an honest automaticity test MUST flag it as automatic.
  * FAIR COIN   -- true pseudo-random. NEGATIVE pole: not automatic (a.s.),
                   maximal complexity.
  * M(omega)    -- the anchor under test, one bulk omega, deep.
If M(omega) tracks the coin and separates cleanly from Thue-Morse on both
signatures, it is (empirically, to the tested depth) NOT automatic.

Fresh generator per AGENTS.md: the M(omega) 2-adic-log series is re-implemented
here, imports nothing from other scripts, validated 12/12 vs anchors.md S17.7.
"""
import argparse
import math
import random
import numpy as np

# =====================================================================
# Fresh M(omega) generator (2-adic log via convergent series).
# =====================================================================

def _v2(x):
    v = 0
    while x & 1 == 0:
        x >>= 1
        v += 1
    return v


def _log1p(x, prec):
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
        term = ((xi >> e) * pow(i >> e, -1, mod)) & mask
        acc = (acc + term) & mask if (i & 1) else (acc - term) & mask
    return acc & mask


_L9 = {}

def _log9(prec):
    if prec not in _L9:
        _L9[prec] = _log1p(8, prec)
    return _L9[prec]


def anchor_bits(omega, nbits, margin=192):
    """M(omega) = N(omega^2), N(w) = -log(w)/log(9); low nbits digits (lsb first)
    as a list of 0/1 ints."""
    prec = nbits + margin
    mask = (1 << prec) - 1
    x = ((omega * omega) - 1) & mask
    if x == 0:
        return [0] * nbits
    Lw = _log1p(x, prec)
    L9 = _log9(prec)
    assert _v2(L9) == 3
    p = prec - 3
    pm = (1 << p) - 1
    N = (-((Lw >> 3) & pm) * pow((L9 >> 3) & pm, -1, 1 << p)) & pm
    return [(N >> i) & 1 for i in range(nbits)]


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
        got = "".join(str(b) for b in anchor_bits(w, 24))
        assert got == ref, f"gen mismatch omega={w}: {got} != {ref}"


def thue_morse(n):
    """The 2-automatic Thue-Morse sequence: a_k = parity of popcount(k)."""
    return [bin(k).count("1") & 1 for k in range(n)]


# =====================================================================
# Signature 1: 2-kernel growth (Eilenberg / Christol).
# =====================================================================

def kernel_growth(bits, max_depth, cmp_len):
    """Count DISTINCT 2-kernel subsequences a_{2^e n + r} (compared over their
    first cmp_len terms) as kernel depth e = 0..max_depth grows.

    Automatic  => distinct count PLATEAUS (<= number of automaton states).
    Non-automatic => distinct count keeps growing, tracking the number of
    kernel elements generated (2^{e+1}-1 through depth e).

    cmp_len is chosen so that even the sparsest subsequence (stride 2^max_depth)
    has >= cmp_len available terms: need 2^max_depth * cmp_len <= len(bits)."""
    N = len(bits)
    assert (1 << max_depth) * cmp_len <= N, "not enough bits for this depth/cmp_len"
    seen = set()
    per_depth = []
    total = 0
    for e in range(max_depth + 1):
        stride = 1 << e
        for r in range(stride):
            sub = tuple(bits[r + stride * n] for n in range(cmp_len))
            seen.add(sub)
            total += 1
        per_depth.append((e, total, len(seen)))
    return per_depth


# =====================================================================
# Signature 2: subword (factor) complexity p(k).
# =====================================================================

def subword_complexity(bits, kmax):
    """p(k) = number of distinct length-k factors. Automatic sequences have
    LINEAR complexity p(k) = O(k) (Cobham); a fair coin saturates at
    min(2^k, N-k+1). Reinterprets S17.7.2's block-entropy scaling as a
    complexity measurement, the cleanest automaticity signature."""
    N = len(bits)
    b = np.asarray(bits, dtype=np.int64)
    out = []
    cur = b.copy()                              # k=1 block values, aligned at i
    for k in range(1, kmax + 1):
        if k > 1:
            cur = cur[:N - k + 1] + (b[k - 1:N] << (k - 1))
        distinct = int(np.unique(cur).size)
        out.append((k, distinct, min(1 << k, N - k + 1)))
    return out


# =====================================================================
# Driver
# =====================================================================

def report(label, bits, max_depth, cmp_len, kmax):
    print(f"\n########## {label}  (N={len(bits)}) ##########")
    kg = kernel_growth(bits, max_depth, cmp_len)
    print(f"  [kernel] depth e: (#kernel elems generated -> #DISTINCT, over first {cmp_len} terms)")
    line = "   " + "  ".join(f"e{e}:{gen}->{dist}" for e, gen, dist in kg)
    print(line)
    final_gen, final_dist = kg[-1][1], kg[-1][2]
    frac = final_dist / final_gen
    print(f"  [kernel] distinct/generated at max depth = {final_dist}/{final_gen} = {frac:.3f}"
          f"  ({'PLATEAU -> automatic-like' if frac < 0.5 and final_dist < 40 else 'GROWING -> non-automatic-like'})")

    sc = subword_complexity(bits, kmax)
    print(f"  [subword] k: p(k)/min(2^k, N-k+1)  (1.0 = maximal complexity; ->0 = low/automatic)")
    print("   " + "  ".join(f"k{k}:{c}/{cap}={c/cap:.2f}" for k, c, cap in sc if k in (1, 4, 8, 12, kmax)))
    # linearity check: does p(k) look linear (automatic) or exponential?
    k_lin = sc[min(len(sc) - 1, 15)][0]
    return {"kernel_frac": frac, "kernel_final": (final_gen, final_dist),
            "subword": sc}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nbits", type=int, default=131072)
    ap.add_argument("--max-depth", type=int, default=10)
    ap.add_argument("--cmp-len", type=int, default=96)
    ap.add_argument("--kmax", type=int, default=18)
    ap.add_argument("--seed", type=int, default=20260713)
    args = ap.parse_args()

    print("Validating fresh generator against anchors.md S17.7 table...")
    _validate(); print("  OK: 12/12.")

    rng = random.Random(args.seed)
    while True:
        omega = rng.randrange(1 << 40, 1 << 64) | 1
        if omega % 3 != 0:
            break
    print(f"\nbulk omega = {omega}")
    print(f"nbits = {args.nbits} (2^{round(math.log2(args.nbits))}), kernel max_depth = "
          f"{args.max_depth}, cmp_len = {args.cmp_len}, subword kmax = {args.kmax}")
    print(f"kernel feasibility: 2^{args.max_depth} * {args.cmp_len} = "
          f"{(1<<args.max_depth)*args.cmp_len} <= {args.nbits}: "
          f"{(1<<args.max_depth)*args.cmp_len <= args.nbits}")

    M = anchor_bits(omega, args.nbits)
    coin = [rng.randint(0, 1) for _ in range(args.nbits)]
    tm = thue_morse(args.nbits)

    r_tm = report("THUE-MORSE (automatic positive control)", tm, args.max_depth, args.cmp_len, args.kmax)
    r_coin = report("FAIR COIN (non-automatic pole)", coin, args.max_depth, args.cmp_len, args.kmax)
    r_M = report(f"M(omega) bulk anchor", M, args.max_depth, args.cmp_len, args.kmax)

    print("\n" + "=" * 64)
    print("Read: Thue-Morse MUST plateau (kernel size 2, linear subword complexity)")
    print("-- that is the test working. If M(omega) instead tracks the fair coin")
    print("(kernel all-distinct, subword complexity saturating at 2^k), then M(omega)")
    print("is NOT 2-automatic to this depth, i.e. its generating function is NOT")
    print("algebraic over F_2(x) (Christol) -- a structural, non-statistical negative.")
    print("See anchors.md S17.7.3.")


if __name__ == "__main__":
    main()
