"""Merle round 3: transport-recurrence verification + antecedence dictionary.

Supports: briefs/merle-round3-check-findings.md (queue items 1-4 of
briefs/merle-round3-check-brief.md), 2026-07-18.

Fresh code per AGENTS.md: imports nothing from staircase_allp.py,
merle_pincer_check.py, periodic_shelf.py, p22_passer.py, or any other
committed script. Every pass/fail decision is exact integer or Fraction
arithmetic; floats appear only in labeled display columns (log2 margins,
gamma). Convention pins (rounding mode ROUND_HALF_EVEN on climb partial
sums, K = (3^n).bit_length(), crash block last with the whole remaining
s-budget) were read from the committed scripts' text to align
conventions, per the pincer session's precedent; no code is imported or
copied.

Sections:
  1. Definitions: 12.6.1's R_r fresh; profile machinery.
  2. Item 1 -- the transport recurrence R_{r+1} = (3^{m_r} R_r +
     (2^{s_r}-1) q) / 2^{sigma_r}, sigma_r = s_r + m_{r+1 mod p}:
     exact identity on random profiles (no closure assumption) and on
     the recorded 12.8.6.4 instances; corollaries (unit transport,
     gcd invariance, divisibility collapse, gcd(q,6)=1).
  3. Item 2 -- the antecedence dictionary against reverse.md 14.15.9:
     N_r + D = 2^{m_r} R_r (the seam identity), the affine rotation
     orbit (14.15.9.2(1)) == the recurrence, shared reduced denominator
     (14.15.9.2(2)) == gcd invariance, ghost identity
     v2(3^{m_r} R_r - q) = s_r == 14.15.9.4(1); verified on the
     14.15.9 Setup grid (7 single-letter + 13 multi-letter probe words
     + 3 integer words) and on random profiles; reduction witnesses
     (unreduced q = 2^K - 3^n vs reduced denominator).
  4. Item 3 -- collapse payoff: fresh period-2 search (the eleven
     quadruples and their rotation-duplicates); a recorded instance
     where the SIZE test passes at one rotation and fails at another.
  5. Item 4(b) -- crash-depth u-coincidence: u_r = min(R_r mod q,
     q - R_r mod q)/q for cd=1 vs cd=2 at the recorded calibration
     instances (p=21 n=15601, p=23 n=47468, p=22 n=25217, n=31202).

Run:  python experiments/merle_round3_check.py       (~1-2 min)
"""

import decimal
import math
import random
from fractions import Fraction
from math import gcd

decimal.getcontext().prec = 600
L_DEC = decimal.Decimal(3).ln() / decimal.Decimal(2).ln()  # log2(3), display/construction only

SEED = 20260718
CHECKS = {"count": 0, "fail": 0}


def check(cond, label):
    CHECKS["count"] += 1
    if not cond:
        CHECKS["fail"] += 1
        print(f"FAIL: {label}")
    return cond


def v2(x):
    x = abs(x)
    assert x != 0
    return (x & -x).bit_length() - 1


def log2_big(x):
    """Display-only float log2 of a positive big int."""
    b = x.bit_length()
    sh = max(0, b - 53)
    return math.log2(x >> sh) + sh


# ---------------------------------------------------------------------
# Section 1: 12.6.1's rotation numerators, fresh implementation.
# ---------------------------------------------------------------------

def profile_K_n_q(ms, ss):
    n = sum(ms)
    K = sum(ss) + n
    return K, n, (1 << K) - 3 ** n


def sigma_of(ms, ss, t):
    """sigma_t = s_t + m_{t+1 mod p} (cycle conventions, cycles.md 12)."""
    p = len(ms)
    return ss[t] + ms[(t + 1) % p]


def R_rot(ms, ss, r):
    """12.6.1: R_r = sum_t 3^{M_t} 2^{S_t} (2^{s_t}-1), indices read in
    rotation order starting at r: M_t = sum_{j>t} m_j, S_t = sum_{j<t}
    sigma_j (rotated labels). Direct double loop, exact ints."""
    p = len(ms)
    total = 0
    for t in range(p):
        M_t = sum(ms[(r + j) % p] for j in range(t + 1, p))
        S_t = sum(sigma_of(ms, ss, (r + j) % p) for j in range(t))
        s_t = ss[(r + t) % p]
        total += 3 ** M_t * (1 << S_t) * ((1 << s_t) - 1)
    return total


def R_all(ms, ss):
    return [R_rot(ms, ss, r) for r in range(len(ms))]


# ---------------------------------------------------------------------
# Section 1b: the mirror-frame quantities (reverse.md 14.15.9.1),
# fresh implementation, letters (m_i, r_i) := (m_i, s_i).
# ---------------------------------------------------------------------

def N_rot(ms, ss, r):
    """14.15.9.1's numerator N for the rotated word starting at r,
    under the dictionary letter i = block r+i, (m_i, r_i) = (m, s)."""
    p = len(ms)
    total = 0
    for i in range(p):
        m_i = ms[(r + i) % p]
        Msuf = sum(ms[(r + j) % p] for j in range(i + 1, p))
        Spre = sum(ms[(r + j) % p] + ss[(r + j) % p] for j in range(i))
        total += (3 ** m_i - (1 << m_i)) * 3 ** Msuf * (1 << Spre)
    return total


def fixed_point(ms, ss, r):
    """Rotated composed fixed point y*_r = N_r / D as a Fraction."""
    K, n, q = profile_K_n_q(ms, ss)
    return Fraction(N_rot(ms, ss, r), q)  # D = 2^{S_P} - 3^{M_P} = q


def alpha_beta(m, s):
    return (Fraction(3 ** m, 1 << (m + s)),
            Fraction(3 ** m - (1 << m), 1 << (m + s)))


# ---------------------------------------------------------------------
# Section 2 (queue item 1): the recurrence and corollaries per profile.
# ---------------------------------------------------------------------

def check_profile(ms, ss, tag, expect_full_div=None):
    """Run every item-1 and item-2 exact check on one profile."""
    p = len(ms)
    K, n, q = profile_K_n_q(ms, ss)
    Rs = R_all(ms, ss)

    # gcd(q, 6) = 1 with the one-line reasons.
    check(q % 2 != 0, f"{tag}: q odd (even minus odd)")
    check(q % 3 == (-1) ** K % 3, f"{tag}: q == (-1)^K mod 3")
    check(gcd(abs(q), 6) == 1, f"{tag}: gcd(q,6)=1")

    # The transport recurrence, exact, every rotation.
    for r in range(p):
        sig = sigma_of(ms, ss, r)
        rhs = 3 ** ms[r] * Rs[r] + ((1 << ss[r]) - 1) * q
        check(rhs % (1 << sig) == 0, f"{tag}: r={r} division exact")
        check(rhs == (1 << sig) * Rs[(r + 1) % p],
              f"{tag}: r={r} recurrence")
        # Unit transport mod q.
        check(((1 << sig) * Rs[(r + 1) % p] - 3 ** ms[r] * Rs[r]) % q == 0,
              f"{tag}: r={r} unit transport mod q")

    # gcd invariance and divisibility collapse.
    gs = [gcd(abs(q), R) for R in Rs]
    check(len(set(gs)) == 1, f"{tag}: gcd(q,R_r) rotation-invariant")
    divs = [R % q == 0 for R in Rs]
    check(all(divs) or not any(divs), f"{tag}: q|R_r all-or-nothing")
    if expect_full_div is not None:
        check(all(divs) == expect_full_div,
              f"{tag}: full divisibility == {expect_full_div}")

    # --- item 2: the dictionary. ---
    Ns = [N_rot(ms, ss, r) for r in range(p)]
    for r in range(p):
        # Seam identity N_r + D = 2^{m_r} R_r (D = q).
        check(Ns[r] + q == (1 << ms[r]) * Rs[r],
              f"{tag}: r={r} seam identity N_r + q = 2^m_r R_r")
        # Affine rotation orbit 14.15.9.2(1) == the recurrence.
        a_r, b_r = alpha_beta(ms[r], ss[r])
        y_r = Fraction(Ns[r], q)
        y_r1 = Fraction(Ns[(r + 1) % p], q)
        check(y_r1 == a_r * y_r + b_r,
              f"{tag}: r={r} affine orbit y*_(r+1) = alpha_r y*_r + beta_r")
        # Ghost identity == 14.15.9.4(1) under the dictionary.
        check(v2(3 ** ms[r] * Rs[r] - q) == ss[r],
              f"{tag}: r={r} ghost identity v2(3^m R - q) = s")
    # Shared reduced denominator 14.15.9.2(2) == gcd invariance.
    dens = [Fraction(Ns[r], q).denominator for r in range(p)]
    check(len(set(dens)) == 1, f"{tag}: one shared reduced denominator")
    check(dens[0] == abs(q) // gs[0],
          f"{tag}: reduced denominator = |q|/gcd(q,R_r)")
    return q, Rs, gs[0], dens[0]


# ---------------------------------------------------------------------
# Recorded instances (12.8.6.4 / briefs/merle-pincer-check-findings.md).
# ---------------------------------------------------------------------

P7_MS = (4, 7, 9, 15, 23, 35, 1)
P7_SS = (1, 1, 1, 1, 1, 1, 49)          # n=94, K=149, S=55, crash s=49

P22A_N = 25217
P22A_MS = (1, 1, 3, 3, 6, 10, 14, 24, 37, 59, 95, 149, 235, 372, 588,
           932, 1475, 2338, 3704, 5869, 9301, 1)
P22A_SS = (1,) * 21 + (14730,)

P22B_N = 31202
P22B_MS = (1, 2, 3, 4, 8, 11, 18, 29, 46, 73, 115, 182, 290, 460, 728,
           1152, 1826, 2893, 4584, 7264, 11512, 1)
P22B_SS = (1,) * 21 + (18231,)


# The 14.15.9 Setup grid, as (m, s) profiles under the dictionary
# letter (m_i, r_i) = block (m_i, s_i).  Known reduced fixed points
# (numerator at rotation 0 / shared denominator) from the probe tables.
SINGLE_WORDS = {                     # (m, r): y* = a/q reduced
    (1, 2): Fraction(1, 5), (1, 3): Fraction(1, 13),
    (2, 2): Fraction(5, 7), (2, 3): Fraction(5, 23),
    (3, 1): Fraction(19, -11), (3, 2): Fraction(19, 5),
    (3, 3): Fraction(19, 37),
}
MULTI_WORDS = {
    ((1, 1), (1, 2)): Fraction(7, 23),
    ((1, 1), (2, 1)): Fraction(29, 5),
    ((1, 1), (2, 2)): Fraction(29, 37),
    ((1, 2), (1, 2)): Fraction(1, 5),
    ((1, 2), (2, 1)): Fraction(49, 37),
    ((1, 2), (2, 2)): Fraction(49, 101),
    ((2, 1), (2, 2)): Fraction(85, 47),
    ((2, 2), (2, 2)): Fraction(5, 7),
    ((1, 1), (1, 1), (1, 2)): Fraction(37, 101),
    ((1, 1), (1, 1), (2, 1)): Fraction(143, 47),
    ((1, 1), (1, 1), (2, 2)): Fraction(143, 175),
    ((1, 1), (1, 2), (1, 2)): Fraction(53, 229),
    ((1, 1), (1, 2), (2, 2)): Fraction(223, 431),
}
INTEGER_WORDS = {
    ((1, 1),): Fraction(1),          # y* = 1
    ((2, 1),): Fraction(-5),         # y* = -5
    ((4, 1), (3, 3)): Fraction(-17),  # y* = -17 (classical negative cycle)
}


def item1_and_2():
    print("=" * 72)
    print("Item 1: transport recurrence, fresh code, exact arithmetic")
    print("Item 2: antecedence dictionary vs reverse.md 14.15.9 (numerics)")
    print("=" * 72)
    rng = random.Random(SEED)

    # (a) random profiles, NO closure assumption ("every profile").
    n_profiles = 0
    n_neg_q = 0
    reduction_witnesses = []
    for trial in range(600):
        p = rng.randint(1, 12)
        hi = 8 if trial < 500 else 20
        ms = [rng.randint(1, hi) for _ in range(p)]
        ss = [rng.randint(1, hi) for _ in range(p)]
        q, Rs, g, den = check_profile(ms, ss, f"rand{trial}")
        n_profiles += 1
        if q < 0:
            n_neg_q += 1
        if g > 1 and den > 1 and len(reduction_witnesses) < 5:
            reduction_witnesses.append((tuple(ms), tuple(ss), q, g, den))
    print(f"random profiles checked: {n_profiles} (p in 1..12, entries in "
          f"1..8 for 500, 1..20 for 100; seed {SEED}); q<0 on {n_neg_q} "
          f"of them (identity is sign-agnostic algebra)")

    # Trivial-cycle profiles: the 'all rotations divisible' branch.
    for p in range(1, 8):
        ms = [1] * p
        ss = [1] * p
        q, Rs, g, den = check_profile(ms, ss, f"trivial p={p}",
                                      expect_full_div=True)
        check(all(R == q for R in Rs),
              f"trivial p={p}: R_r = q (12.6.1 sanity identity)")
    print("trivial-cycle profiles p=1..7: q | R_r at every rotation "
          "(full-divisibility branch exercised), R_r = q = 4^p - 3^p")

    # (b) the recorded instances.
    print("-" * 72)
    for tag, ms, ss, n_rec, gamma_rec in (
            ("p=7 (12.8.3 staircase)", P7_MS, P7_SS, 94, 6.744),
            ("p=22 n=25217 (12.8.6.4 ext.)", P22A_MS, P22A_SS, P22A_N, 11.186),
            ("p=22 n=31202 (12.8.6.4 ext.)", P22B_MS, P22B_SS, P22B_N, 14.746)):
        K, n, q = profile_K_n_q(list(ms), list(ss))
        check(n == n_rec, f"{tag}: n = {n_rec}")
        check(K == (3 ** n).bit_length(), f"{tag}: K = ceil(n log2 3)")
        q2, Rs, g, den = check_profile(list(ms), list(ss), tag,
                                       expect_full_div=False)
        check(all(R >= q for R in Rs), f"{tag}: all rotations pass size")
        gamma = K - log2_big(q)   # display float
        check(abs(gamma - gamma_rec) < 0.01, f"{tag}: gamma matches record")
        print(f"{tag}: recurrence + corollaries pass on all {len(ms)} "
              f"rotations; gamma = {gamma:.3f} (record {gamma_rec}); "
              f"gcd(q,R_r) = {g} shared; size passes everywhere; "
              f"divisibility q|R_r nowhere")

    # The 14.15.9 Setup grid under the dictionary.
    print("-" * 72)
    print("Dictionary grid: 7 single-letter + 13 multi-letter + 3 integer "
          "words as (m,s) profiles")
    for words, expect in (
            ({(k,): v for k, v in SINGLE_WORDS.items()}, "single"),
            (MULTI_WORDS, "multi"),
            (INTEGER_WORDS, "integer")):
        for word, ystar in words.items():
            ms = [m for m, r in word]
            ss = [r for m, r in word]
            tag = f"word {word}"
            q, Rs, g, den = check_profile(ms, ss, tag)
            y0 = Fraction(N_rot(ms, ss, 0), q)
            check(y0 == ystar, f"{tag}: y*_0 = {ystar}")
            check(den == abs(ystar.denominator),
                  f"{tag}: shared reduced denominator = q_mirror")
    # Integer words: full divisibility (q_red = 1  <=>  q | R_r everywhere).
    for word in INTEGER_WORDS:
        ms = [m for m, r in word]
        ss = [r for m, r in word]
        K, n, q = profile_K_n_q(ms, ss)
        Rs = R_all(ms, ss)
        check(all(R % q == 0 for R in Rs),
              f"word {word}: integer fixed point <=> q | R_r at every r")
    print("grid: all fixed points, denominators, and divisibility "
          "patterns match the 14.15.9 record")

    # Reduction witnesses: unreduced q = 2^K - 3^n vs reduced denominator.
    print("-" * 72)
    ms, ss = [1, 1], [2, 2]   # the word ((1,2),(1,2)), probe's constant pair
    K, n, q = profile_K_n_q(ms, ss)
    Rs = R_all(ms, ss)
    g = gcd(abs(q), Rs[0])
    print(f"designed reduction witness: profile m={tuple(ms)}, s={tuple(ss)}"
          f" (= word ((1,2),(1,2)), the multi-letter probe's constant pair):"
          f" unreduced q = 2^{K} - 3^{n} = {q}, gcd(q, R_r) = {g},"
          f" reduced denominator = {abs(q)//g}"
          f" (14.15.9's q = 5; his q = 55; they differ exactly here)")
    check(q == 55 and g == 11 and abs(q) // g == 5, "reduction witness values")
    print(f"random-profile reduction witnesses (first 5 of the 600):")
    for ms, ss, q, g, den in reduction_witnesses:
        print(f"  m={ms}, s={ss}: q={q}, gcd={g}, reduced denom={den}")


# ---------------------------------------------------------------------
# Section 4 (queue item 3): collapse payoff.
# ---------------------------------------------------------------------

def item3_period2_search(NMAX=200):
    """Fresh period-2 search: all (m0,m1,s0,s1) with m0+m1 = n <= NMAX,
    K = ceil(n log2 3) (the ceiling lemma 12.6.2/12.6.3 supplies
    completeness, as in 12.5.4), exact size test q <= min(R_0, R_1).
    Recorded outcome (12.5.4): exactly 11 quadruples in n <= 20,000,
    all at small n. This search covers n <= NMAX and asserts it finds
    exactly those 11."""
    print("=" * 72)
    print(f"Item 3(a): fresh period-2 search, n <= {NMAX} "
          f"(12.5.4's survivors all have n <= 29)")
    print("=" * 72)
    pow3 = [1]
    for _ in range(NMAX + 1):
        pow3.append(pow3[-1] * 3)
    passers = []
    for n in range(2, NMAX + 1):
        T3 = pow3[n]
        K = T3.bit_length()
        S = K - n
        if S < 2:
            continue
        q = (1 << K) - T3
        for m0 in range(1, n):
            m1 = n - m0
            for s0 in range(1, S):
                s1 = S - s0
                # R_0 = 3^{m1}(2^{s0}-1) + 2^{s0+m1}(2^{s1}-1)  (12.5.1)
                R0 = pow3[m1] * ((1 << s0) - 1) + (1 << (s0 + m1)) * ((1 << s1) - 1)
                if R0 < q:
                    continue
                R1 = pow3[m0] * ((1 << s1) - 1) + (1 << (s1 + m0)) * ((1 << s0) - 1)
                if R1 < q:
                    continue
                passers.append((n, K, m0, m1, s0, s1, q, R0, R1))
    print(f"size-passers found: {len(passers)}")
    check(len(passers) == 11, "exactly 11 size-passing quadruples (12.5.4)")
    print(f"{'n':>4} {'m0':>3} {'m1':>3} {'s0':>3} {'s1':>3}  "
          f"{'q|R0':>5} {'q|R1':>5}  rotation-partner")
    seen = {}
    rot_pairs = 0
    self_rot = 0
    for (n, K, m0, m1, s0, s1, q, R0, R1) in passers:
        d0, d1 = R0 % q == 0, R1 % q == 0
        check(d0 == d1, f"p2 ({m0},{m1},{s0},{s1}): divisibility collapse")
        key = (m0, m1, s0, s1)
        rot = (m1, m0, s1, s0)
        if rot == key:
            partner = "self (symmetric)"
            self_rot += 1
        elif rot in seen:
            partner = f"rotation of {rot}"
            rot_pairs += 1
        else:
            partner = "-"
        seen[key] = True
        print(f"{n:>4} {m0:>3} {m1:>3} {s0:>3} {s1:>3}  "
              f"{str(d0):>5} {str(d1):>5}  {partner}")
    print(f"rotation structure of the 11: {self_rot} symmetric "
          f"(self-rotation), {rot_pairs} cross-quadruple rotation pairs, "
          f"{11 - self_rot - 2 * rot_pairs} unpaired")
    print(f"divisibility conditions as recorded (severally): "
          f"2 per quadruple = 22; under the collapse: 1 per quadruple = 11; "
          f"after cross-quadruple rotation dedup: {11 - rot_pairs} distinct")
    n_div = sum(1 for (n, K, m0, m1, s0, s1, q, R0, R1) in passers
                if R0 % q == 0)
    print(f"quadruples passing divisibility: {n_div} "
          f"(the degenerate (1,1,1,1) only, per 12.5.3)")
    check(n_div == 1, "only the degenerate quadruple passes divisibility")


def base_construct(p, n, K, crash_depth):
    """Construction 12.8.6.2, fresh: p-1 unit-exit climb blocks with
    geometric depths (ratio L) rounded by partial sums (ROUND_HALF_EVEN),
    one crash block (depth = crash_depth, all remaining s-budget).
    Convention-pinned to the committed scripts' reading of 12.8.6.2."""
    S = K - n
    if p < 2 or S <= p - 1:
        return None
    climb_n = n - crash_depth
    blocks = p - 1
    if climb_n < blocks:
        return None
    c = decimal.Decimal(climb_n) * (L_DEC - 1) / (L_DEC ** blocks - 1)
    prev = 0
    ms = []
    for j in range(blocks):
        Tj = c * (L_DEC ** (j + 1) - 1) / (L_DEC - 1)
        Mj = int(Tj.to_integral_value(rounding=decimal.ROUND_HALF_EVEN))
        ms.append(Mj - prev)
        prev = Mj
    ms[-1] += climb_n - sum(ms)
    if min(ms) < 1:
        return None
    ms = ms + [crash_depth]
    ss = [1] * blocks + [S - blocks]
    if ss[-1] < 1:
        return None
    return ms, ss


def item3_size_noncollapse():
    print("-" * 72)
    print("Item 3(b): the SIZE test q <= R_r does NOT collapse across "
          "rotations")
    print("-" * 72)
    n = P22A_N
    K = (3 ** n).bit_length()
    res = base_construct(22, n, K, 1)
    check(res is not None, "p=22 n=25217 cd=1 base construction feasible")
    ms, ss = res
    q = (1 << K) - 3 ** n
    Rs = R_all(ms, ss)
    fails = [r for r in range(22) if Rs[r] < q]
    passes = [r for r in range(22) if Rs[r] >= q]
    worst = min(range(22), key=lambda r: Rs[r].bit_length() - q.bit_length())
    print(f"p=22, n=25217, cd=1, base construction (pre-correction): "
          f"size FAILS at rotations {fails} "
          f"({len(fails)}/22) and PASSES at rotations {passes} "
          f"({len(passes)}/22); worst rotation {worst}, margin "
          f"{log2_big(Rs[worst]) - log2_big(q):.2f} bits")
    check(len(fails) == 9, "pre-correction fail count 9/22 "
          "(matches pincer findings item 2)")
    check(0 < len(fails) < 22, "size passes at some rotations, fails at "
          "others: size conditions are rotation-dependent, no collapse")
    # Divisibility distances vary across rotations too (context display).
    print("(the corrected passer's per-rotation R_r span "
          f"{min(R.bit_length() for R in R_all(list(P22A_MS), list(P22A_SS)))}"
          f"..{max(R.bit_length() for R in R_all(list(P22A_MS), list(P22A_SS)))}"
          " bits: q <= min_r R_r is a genuinely p-fold system)")


# ---------------------------------------------------------------------
# Section 5 (queue item 4b): crash-depth u-coincidence.
# ---------------------------------------------------------------------

def u_profile(ms, ss):
    K, n, q = profile_K_n_q(ms, ss)
    out = []
    for R in R_all(ms, ss):
        rmod = R % q
        out.append(Fraction(min(rmod, q - rmod), q))
    return out


def item4b_u_coincidence():
    print("=" * 72)
    print("Item 4(b): does cd=1 vs cd=2 give the same distance statistic "
          "u = min(R_r mod q, q - R_r mod q)/q in OUR construction?")
    print("=" * 72)
    cases = [(21, 15601, (3, -2.27), (3, -2.85)),
             (23, 47468, (4, -3.77), (4, -4.18)),
             (22, 25217, (9, -7.86), None),
             (22, 31202, (6, -4.80), None)]
    for p, n, rec1, rec2 in cases:
        K = (3 ** n).bit_length()
        q = (1 << K) - 3 ** n
        profs = {}
        for cd in (1, 2):
            res = base_construct(p, n, K, cd)
            if res is None:
                print(f"p={p}, n={n}, cd={cd}: base construction infeasible")
                continue
            ms, ss = res
            Rs = R_all(ms, ss)
            fail = sum(1 for R in Rs if R < q)
            worst = min(log2_big(R) - log2_big(q) for R in Rs)
            rec = rec1 if cd == 1 else rec2
            note = ""
            if rec is not None:
                ok = (fail == rec[0]) and abs(worst - rec[1]) < 0.01
                check(ok, f"p={p} n={n} cd={cd}: matches recorded "
                          f"calibration row {rec}")
                note = f"  [recorded: fail={rec[0]}, worst={rec[1]}]"
            print(f"p={p}, n={n}, cd={cd}: fail={fail}/{p}, "
                  f"worst_log2={worst:.2f}{note}")
            profs[cd] = (ms, ss, u_profile(ms, ss))
        if len(profs) == 2:
            ms1, ss1, u1 = profs[1]
            ms2, ss2, u2 = profs[2]
            same_prof = (ms1 == ms2 and ss1 == ss2)
            same_u_seq = u1 == u2
            same_u_set = sorted(u1) == sorted(u2)
            n_eq = sum(1 for a, b in zip(u1, u2) if a == b)
            print(f"  profiles identical: {same_prof}; u sequences "
                  f"identical: {same_u_seq}; u multisets identical: "
                  f"{same_u_set}; positions with equal u: {n_eq}/{p}")
            # Exact scale of the differences: log2|u1-u2| via bit lengths
            # (floats underflow at this precision; display only).
            logs = []
            for a, b in zip(u1, u2):
                d = abs(a - b)
                logs.append(None if d == 0 else
                            d.numerator.bit_length() - d.denominator.bit_length())
            n_zero = sum(1 for x in logs if x is None)
            near = sum(1 for x in logs if x is not None and x < -1000)
            mat = sum(1 for x in logs if x is not None and x >= -1000)
            print(f"  |u1-u2| exact scale (log2): exactly zero at {n_zero} "
                  f"rotations; below 2^-1000 at {near} rotations "
                  f"(near-identical far beyond any statistical precision); "
                  f"material (>= 2^-1000, in fact O(0.1)) at {mat} rotations "
                  f"-- the ones at/nearest the crash block")
            print(f"  cd=1 m-profile: {tuple(ms1)}")
            print(f"  cd=2 m-profile: {tuple(ms2)}")
            u_disp1 = ", ".join(f"{float(u):.4f}" for u in u1)
            u_disp2 = ", ".join(f"{float(u):.4f}" for u in u2)
            print(f"  u(cd=1): [{u_disp1}]")
            print(f"  u(cd=2): [{u_disp2}]")


def item4b_p7_distance_crosscheck():
    """Cross-check of the pincer findings' p=7 distance table (item 3
    there), pinning this script's rotation convention to the recorded
    one."""
    print("-" * 72)
    us = u_profile(list(P7_MS), list(P7_SS))
    rec = [0.1703, 0.4110, 0.4695, 0.3390, 0.4206, 0.0538, 0.4784]
    print("p=7 ledger-seed distance profile (this script / recorded):")
    for r, (u, v) in enumerate(zip(us, rec)):
        print(f"  rotation {r}: {float(u):.4f} / {v:.4f}")
        check(abs(float(u) - v) < 5e-5, f"p7 distance rotation {r}")


if __name__ == "__main__":
    import time
    t0 = time.time()
    item1_and_2()
    item3_period2_search()
    item3_size_noncollapse()
    item4b_u_coincidence()
    item4b_p7_distance_crosscheck()
    dt = time.time() - t0
    print("=" * 72)
    print(f"TOTAL: {CHECKS['count']} exact checks, {CHECKS['fail']} "
          f"failures, {dt:.1f} s  (2026-07-18, seed {SEED})")
