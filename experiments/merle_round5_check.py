#!/usr/bin/env python3
"""
merle_round5_check.py -- round-5 verification of Eric Merle's fifth letter.

Brief: briefs/merle-round5-check-brief.md.  Fresh code per AGENTS.md: imports
nothing from any committed project script.  Exact integer arithmetic decides
every pass/fail; high-precision decimal appears only in section 2's labeled
density displays and threshold guards.

Frame (fixed once): the T-map on nonzero odd integers,
    T(x) = (3x+1) / 2^{v2(3x+1)}.
A k-cycle with odd elements x_0..x_{k-1}, exponent word s = (s_0..s_{k-1})
(s_i = v2(3 x_i + 1)), and m = sum(s) satisfies, by unrolling
x_{i+1} 2^{s_i} = 3 x_i + 1 around the cycle,

    x_r * q = R_r,   q = 2^m - 3^k,
    R_r = sum_{i=0}^{k-1} 3^{k-1-i} * 2^{S_i}   (word rotated to start at r,
                                                 S_i = s_r + ... + s_{r+i-1}).

This is Merle's (k, m) labelling: k odd (tripling) steps, m total halvings.
cycles.md 12.6.1's (n, K) corresponds under the block dictionary (n = k,
K = m); the transport recurrence / rotation-invariance of gcd(q, R_r)
(Remark 12.6.1.1 / reverse.md 14.15.9.2) applies verbatim: q | R_0 iff
q | R_r for all r.

Sections:
  1  the four anchored loops, |2^a - 3^b| = 1 exhaustive, the |q| = 1
     "free lock" mechanism, the ticket mapping and the -17 lottery win
  2  the envelope identity q+ + q- = 2^floor(kL) and the Benford
     side-asymmetry (added in a later commit)
  3  the exhaustive k <= 10 cycle map, both sectors (added later)

Run: python experiments/merle_round5_check.py [1|2|3|all]
Deterministic throughout, no RNG.  Session date 2026-07-19 (thread date;
the environment clock runs a day behind the thread -- git order is
authoritative, per the brief's provenance note).
"""

import sys
from math import comb

CHECKS = 0
FAILS = 0


def chk(cond, msg=""):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print(f"FAIL: {msg}")
    return cond


def v2(y):
    return (y & -y).bit_length() - 1


def T_step(x):
    y = 3 * x + 1
    s = v2(y)
    return y >> s, s   # arithmetic shift is exact division here (2^s | y)


def cycle_from_seed(x0, maxlen=1000):
    """Iterate T from odd x0 until it returns to x0; return (elements, s-word)."""
    xs, ss = [x0], []
    x = x0
    for _ in range(maxlen):
        x, s = T_step(x)
        ss.append(s)
        if x == x0:
            return xs, ss
        xs.append(x)
    raise RuntimeError(f"no cycle within {maxlen} steps from {x0}")


def R0(k, s_word):
    """Cycle numerator: sum_{i<k} 3^{k-1-i} 2^{S_i}, S_i = s_0+...+s_{i-1}."""
    S, tot = 0, 0
    for i in range(k):
        tot += 3 ** (k - 1 - i) << S
        S += s_word[i]
    return tot


def rotations(word):
    k = len(word)
    return [tuple(word[r:]) + tuple(word[:r]) for r in range(k)]


def compositions(m, k):
    """All k-tuples of positive integers summing to m (lexicographic)."""
    if k == 1:
        if m >= 1:
            yield (m,)
        return
    for first in range(1, m - k + 2):
        for rest in compositions(m - first, k - 1):
            yield (first,) + rest


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def factorize(n):
    n = abs(n)
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


# --------------------------------------------------------------------------
# Section 1: the anchored loops and the |q| = 1 lock
# --------------------------------------------------------------------------

def section1():
    print("=" * 72)
    print("Section 1: anchored loops, |2^a - 3^b| = 1, the free lock, -17")
    print("=" * 72)

    # (a) The four known cycles, fresh forward iteration ------------------
    # Expected anchor table (his labels): +1:(1,2,+1)  -1:(1,1,-1)
    # -5:(2,3,-1) (8-vs-9)  -17:(7,11,-139).
    expected = {
        1:   (1, 2, 1),
        -1:  (1, 1, -1),
        -5:  (2, 3, -1),
        -17: (7, 11, -139),
    }
    anchor_data = {}
    print("\n(a) anchor table from fresh orbits:")
    for seed, (ek, em, eq) in expected.items():
        xs, ss = cycle_from_seed(seed)
        k, m = len(xs), sum(ss)
        q = (1 << m) - 3 ** k
        chk(k == ek, f"{seed}: k={k} expected {ek}")
        chk(m == em, f"{seed}: m={m} expected {em}")
        chk(q == eq, f"{seed}: q={q} expected {eq}")
        # cycle equation at every rotation
        for r in range(k):
            w = tuple(ss[r:]) + tuple(ss[:r])
            chk(xs[r] * q == R0(k, w), f"{seed}: cycle eq at rotation {r}")
        anchor_data[seed] = (k, m, q, xs, ss)
        print(f"  seed {seed:>4}: k={k}, m={m}, q={q:>5}, elements={xs}, s-word={tuple(ss)}")

    # -5 lives on 8-vs-9: q = 2^3 - 3^2
    chk(anchor_data[-5][2] == 8 - 9, "-5 is the 8-vs-9 near-miss")

    # (b) |2^a - 3^b| = 1 exhaustive, a <= 200, b <= 130 ------------------
    sols = [(a, b) for a in range(1, 201) for b in range(1, 131)
            if abs((1 << a) - 3 ** b) == 1]
    chk(sols == [(1, 1), (2, 1), (3, 2)],
        f"|2^a-3^b|=1 solutions: {sols}")
    print(f"\n(b) |2^a - 3^b| = 1 for 1<=a<=200, 1<=b<=130: solutions {sols}")
    print("    (2-3, 4-3, 9-8 -- exactly his three; elementary proof in findings)")

    # computational support for the two elementary proof steps:
    #   3^b + 1 = 2^a: 3^b mod 8 in {1,3}, so 3^b+1 in {2,4} mod 8 => a <= 2.
    for b in range(1, 131):
        chk(pow(3, b, 8) in (1, 3), f"3^{b} mod 8")
    #   3^b - 1 = 2^a: b odd => 3^b-1 == 2 (mod 8) => a = 1;
    #                  b even => (3^{b/2}-1)(3^{b/2}+1), gcd of factors = 2.
    for b in range(1, 131):
        if b % 2 == 1:
            chk((3 ** b - 1) % 8 == 2, f"3^{b}-1 mod 8 (b odd)")
        else:
            c = b // 2
            import math
            chk(math.gcd(3 ** c - 1, 3 ** c + 1) == 2, f"gcd factors b={b}")

    # (c) the free lock: |q| = 1  =>  every composition at (k, m) is a cycle
    # "free" means: divisibility q | R_r is automatic (|q| = 1 divides
    # everything), so every profile's rational cycle is integral; what must
    # still be checked -- and is, exhaustively below -- is the bookkeeping:
    # every element odd, nonzero, of one sign, and forward closure with
    # v2(3x+1) matching the prescribed s at every step.
    print("\n(c) the free lock at the three |q| = 1 anchors:")
    lock_table = [(1, 1), (1, 2), (2, 3)]   # (k, m) for near-miss (a,b)->(b,a)
    for (k, m) in lock_table:
        q = (1 << m) - 3 ** k
        chk(abs(q) == 1, f"(k,m)=({k},{m}) has |q|=1")
        n_comps = 0
        for s in compositions(m, k):
            n_comps += 1
            elems = []
            for w in rotations(s):
                num = R0(k, w)
                chk(num % q == 0, f"({k},{m}) {s}: divisibility (free)")
                elems.append(num // q)
            chk(all(e % 2 != 0 for e in elems), f"({k},{m}) {s}: all odd")
            chk(all(e != 0 for e in elems), f"({k},{m}) {s}: nonzero")
            chk(len({e > 0 for e in elems}) == 1, f"({k},{m}) {s}: one sign")
            for i in range(k):
                y = 3 * elems[i] + 1
                chk(v2(y) == s[i], f"({k},{m}) {s}: v2 match at {i}")
                chk(y >> s[i] == elems[(i + 1) % k],
                    f"({k},{m}) {s}: closure at {i}")
            print(f"    (k,m)=({k},{m}), q={q:+d}, word {s}: genuine cycle "
                  f"{sorted(set(elems))}")
        chk(n_comps == comb(m - 1, k - 1), f"({k},{m}): composition count")

    # (d) ticket mapping and the -17 lottery win --------------------------
    print("\n(d) ticket mapping and -17:")
    # 4-3 -> (k,m)=(1,2), q=+1, cycle {+1} (north);
    # 2-3 -> (1,1), q=-1, cycle {-1}; 9-8 -> (2,3), q=-1, cycle {-5,-7} (south)
    chk(anchor_data[1][2] == 1 and anchor_data[1][3] == [1], "4-3 -> +1 north")
    chk(anchor_data[-1][2] == -1 and anchor_data[-1][3] == [-1], "2-3 -> -1 south")
    chk(anchor_data[-5][2] == -1 and sorted(anchor_data[-5][3]) == [-7, -5],
        "9-8 -> -5 south")
    # -17 is the only known cycle with |q| > 1
    chk(sum(1 for s in expected if abs(anchor_data[s][2]) > 1) == 1
        and abs(anchor_data[-17][2]) == 139, "-17 alone has |q| > 1")
    k, m, q, xs, ss = anchor_data[-17]
    r0 = R0(k, tuple(ss))
    import math
    g = math.gcd(abs(q), r0)
    chk(g == 139, f"-17: gcd(q, R_0) = {g}")
    chk(is_prime(139), "139 prime")
    chk(r0 == 17 * 139, f"-17: R_0 = {r0} = 17*139")
    # gcd is rotation-invariant (12.6.1.1); confirm at every rotation
    for w in rotations(ss):
        chk(math.gcd(abs(q), R0(k, w)) == 139, "-17: gcd rotation-invariant")
    # word primitivity: (1,1,1,2,1,1,4) is not a repetition of a shorter word
    prim = all(tuple(ss) != tuple(ss[d:] + ss[:d]) for d in range(1, k))
    chk(prim, "-17: s-word primitive (all 7 rotations distinct)")
    print(f"    -17: q = {q}, R_0 = {r0} = 17*139, gcd(q, R_0) = 139 (prime),")
    print(f"         s-word {tuple(ss)} primitive; the single |q| > 1 cycle.")

    print(f"\nSection 1 done.")


# --------------------------------------------------------------------------
# Section 2: the envelope identity and the Benford side-asymmetry
# --------------------------------------------------------------------------
#
# L = log2 3.  q+ = 2^ceil(kL) - 3^k > 0,  q- = 3^k - 2^floor(kL) > 0.
# (a) Envelope: kL is never an integer (2^m = 3^k is impossible), so
#     ceil(kL) = floor(kL) + 1 and
#         q+ + q- = 2^{floor(kL)+1} - 3^k + 3^k - 2^{floor(kL)} = 2^{floor(kL)}.
#     One line; verified exactly below for k = 1..3000.
# (b) Two distance notions, pinned:
#     ABSOLUTE: the negative side (the lower tower) wins iff q- < q+
#       iff 2*3^k < 2^{floor} + 2^{ceil} = 3*2^{floor(kL)}
#       iff 3^k / 2^{floor(kL)} < 3/2  iff  2^{frac(kL)} < 3/2
#       iff frac(kL) < log2(3/2).  Density log2(3/2) = 0.5849625...
#       by Weyl equidistribution (L irrational).
#     RATIO (multiplicative): the lower tower is nearer iff
#       3^k/2^{floor} < 2^{ceil}/3^k  iff  2^{frac} < 2^{1-frac}
#       iff frac(kL) < 1/2.  Density 1/2 -- the machine's 50/50 first
#       draft is the correct answer to THIS question.
#     Second-binary-digit reading: 3^k's leading bit is at floor(kL);
#     its second bit is 0 iff 3^k < 1.5 * 2^{floor(kL)} iff the same
#     event as "negative side wins" -- base-2 Benford second-digit law,
#     P = log2(3/2).  Checked as an exact per-k equivalence below.

K_ENVELOPE = 3000
K_EXACT = 100_000          # exact integer comparisons up to here
K_HP = 10_000_000          # high-precision fractional parts up to here
HP_BITS = 200              # working precision (bits) for the guard


def section2():
    print("=" * 72)
    print("Section 2: envelope identity + Benford side-asymmetry")
    print("=" * 72)

    from decimal import Decimal, getcontext, ROUND_FLOOR
    getcontext().prec = 150   # ~498 bits; display/guard only, labeled

    # High-precision integer approximation of L (guard apparatus).
    # A = floor(L * 2^HP_BITS); decimal error ~1e-148 * 2^200 ~ 1e-88 ulp,
    # so A is the exact floor with enormous margin.  Consistency with the
    # exact big-integer world is checked at every k of the exact passes.
    L_dec = Decimal(3).ln() / Decimal(2).ln()
    A = int((L_dec * (1 << HP_BITS)).to_integral_value(rounding=ROUND_FLOOR))
    T_int = A - (1 << HP_BITS)          # floor(frac(L) * 2^HP_BITS)
    mask = (1 << HP_BITS) - 1

    # (a) envelope identity, exact, k = 1..3000 ---------------------------
    t = 1
    for k in range(1, K_ENVELOPE + 1):
        t *= 3
        fl = t.bit_length() - 1                  # floor(kL), exact
        qp = (1 << (fl + 1)) - t
        qn = t - (1 << fl)
        chk(qp > 0 and qn > 0, f"envelope k={k}: positivity")
        chk(qp + qn == 1 << fl, f"envelope k={k}: q+ + q- = 2^floor(kL)")
        chk((k * A) >> HP_BITS == fl, f"A-consistency k={k}")
    print(f"\n(a) q+ + q- = 2^floor(kL) exact for k = 1..{K_ENVELOPE}; "
          f"q+, q- > 0 throughout;")
    print(f"    floor(k*A/2^{HP_BITS}) == floor(kL) for all these k "
          f"(guard consistency).")

    # (b) exact integer pass, k = 1..K_EXACT ------------------------------
    # Tie analysis, exact: 2*3^k = 3*2^e  iff  3^{k-1} = 2^{e-1}  iff k = 1
    # (e = 1).  So k = 1 is an exact tie -- q+ = q- = 1: the near-misses
    # 4-3 and 2-3 are both at distance 1 from 3^1 -- and no tie exists for
    # any k >= 2.  Win counts below are over k >= 2; the tie is reported.
    t = 1
    neg_wins_exact = 0
    exact_counts = {}
    for k in range(1, K_EXACT + 1):
        t *= 3
        fl = t.bit_length() - 1
        lhs = 2 * t                      # 2 * 3^k
        rhs = 3 << fl                    # 3 * 2^floor(kL)
        if k == 1:
            chk(lhs == rhs, "k=1 is an exact tie (q+ = q- = 1)")
            continue
        chk(lhs != rhs, f"k={k}: no tie for k >= 2")
        neg = lhs < rhs
        # second binary digit of 3^k: bit fl-1 (below the leading bit fl)
        d2 = (t >> (fl - 1)) & 1
        chk((d2 == 0) == neg, f"k={k}: second-digit equivalence")
        neg_wins_exact += neg
        if k in (10**4, 10**5):
            exact_counts[k] = neg_wins_exact
    print(f"\n(b) exact integer comparisons (2*3^k vs 3*2^floor(kL)), "
          f"2 <= k <= {K_EXACT}:")
    print(f"    k = 1 is an EXACT TIE: q+ = q- = 1 (4-3 and 2-3 both at "
          f"distance 1); no other tie exists.")
    for kk, c in exact_counts.items():
        print(f"    2 <= k <= {kk:>7,}: negative side wins {c:>7,} "
              f"of {kk - 1:,} ({c / (kk - 1):.7f})")
    print(f"    second-binary-digit-of-3^k = 0 coincides with "
          f"'negative side wins' at every k >= 2 (exact).")

    # (b') high-precision pass to K_HP with margin guard ------------------
    s = 0
    neg_wins_hp = 0
    ratio_wins_hp = 0
    half = 1 << (HP_BITS - 1)
    min_margin, argmin_k = None, None
    decades = {}
    next_decade = 10
    for k in range(1, K_HP + 1):
        s = (s + A) & mask               # frac(kL) * 2^B, error < (k+1) ulp
        diff = s - T_int
        if k == 1:
            # the exact tie: frac(1*L) IS the threshold log2(3/2)
            chk(diff == 0, "hp pass sees the k=1 tie exactly (0 ulp)")
        else:
            if diff < 0:
                neg_wins_hp += 1
                m_ = -diff
            else:
                m_ = diff
            if min_margin is None or m_ < min_margin:
                min_margin, argmin_k = m_, k
        if s < half:
            ratio_wins_hp += 1
        if k == next_decade:
            decades[k] = (neg_wins_hp, ratio_wins_hp)
            next_decade *= 10
    decades[K_HP] = (neg_wins_hp, ratio_wins_hp)

    # guard: every decision safe iff |integer margin| > k+1 ulp error bound
    chk(min_margin > K_HP + 1,
        f"threshold guard: min margin {min_margin} ulp > {K_HP + 1}")
    # cross-check hp vs exact at 10^5
    chk(decades[10**5][0] == exact_counts[10**5],
        "hp count at 1e5 == exact count")

    log2_3_2 = float(Decimal(3).ln() / Decimal(2).ln() - 1)
    print(f"\n(b') high-precision pass to k = {K_HP:,} "
          f"({HP_BITS}-bit fractional parts; labeled measurement; "
          f"absolute column over k >= 2, tie at k = 1 excluded):")
    print(f"    {'k':>12}  {'absolute: frac < log2(3/2)':>28}  "
          f"{'ratio: frac < 1/2':>18}")
    for kk in sorted(decades):
        a_, r_ = decades[kk]
        print(f"    {kk:>12,}  {a_ / (kk - 1):>28.7f}  {r_ / kk:>18.7f}")
    print(f"    log2(3/2) = {log2_3_2:.10f}; ratio-side limit = 0.5")

    # closest call, exactly confirmed ------------------------------------
    marg_real = Decimal(min_margin) / Decimal(1 << HP_BITS)
    tstar = pow(3, argmin_k)
    fl = tstar.bit_length() - 1
    lhs, rhs = 2 * tstar, 3 << fl
    chk(lhs != rhs, "closest call (k >= 2): no tie")
    neg_exact = lhs < rhs
    s_hp = (argmin_k * A) & mask
    chk((s_hp - T_int < 0) == neg_exact,
        "closest call: hp side == exact side")
    print(f"\n    closest call in the guard: k = {argmin_k:,}, "
          f"|frac(kL) - log2(3/2)| = {marg_real:.3E}")
    print(f"    ({min_margin} ulp at 2^-{HP_BITS}; safety bound {K_HP + 1} "
          f"ulp; side exactly confirmed by big-integer comparison: "
          f"negative wins = {neg_exact})")

    print("\nSection 2 done.")


def main():
    args = sys.argv[1:] or ["all"]
    run = args[0]
    if run in ("1", "all"):
        section1()
    if run in ("2", "all"):
        section2()
    print(f"\nTOTAL: {CHECKS} checks, {FAILS} failures")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
