#!/usr/bin/env python3
"""merle_la5_check.py — independent verification of shared-ledger entry L-A5
(adelic content invariant + separation lemma T1/T2), round 9.

Supports: briefs/merle-la5-check-findings.md (delegated session, 2026-07-24).
Brief: briefs/merle-la5-check-brief.md.

Fresh code: imports nothing from any Merle repository and nothing from prior
Merle-check scripts. Conventions re-implemented from cycles.md 12.6.1/12.6.1.1
only. Exact integer arithmetic at every pass/fail decision; floats appear only
in *reported* C values, never in a pass/fail test. Canaries hand-computed and
printed before any sweep.

Objects (cycles.md 12.6.1, 12.6.1.1):
  profile (m_t, s_t)_{t<p}, entries >= 1; n = sum m; K = sum s + n;
  q = 2^K - 3^n; sigma_t = s_t + m_{(t+1) mod p};
  M_t = sum_{j>t} m_j; S_t = sum_{j<t} sigma_j;
  R_0 = sum_t 3^{M_t} 2^{S_t} (2^{s_t} - 1).
L-A5's invariant: C(P) = log gcd(q, R_0) / log |q|  (defined for |q| > 1).
Lean-side object (ContentSeparation.lean, read this session):
  W0([]) = 0; W0((m,s)::rest) = 3^{msum rest} 2^m (2^s - 1) + 2^{m+s} W0(rest);
  bridge W0(l) = 2^{m_0} R_0(l).
"""

import math
import random
from fractions import Fraction

random.seed(20260724)

FAILURES = []
CHECKS = [0]


def check(label, ok):
    CHECKS[0] += 1
    if not ok:
        FAILURES.append(label)
        print(f"  FAIL: {label}")
    else:
        print(f"  PASS: {label}")
    return ok


# ---------------------------------------------------------------- conventions
def R0(m, s):
    """Rotation numerator R_0 per cycles.md 12.6.1 (independent implementation)."""
    p = len(m)
    sig = [s[t] + m[(t + 1) % p] for t in range(p)]
    tot = 0
    for t in range(p):
        M_t = sum(m[t + 1:])
        S_t = sum(sig[:t])
        tot += 3 ** M_t * 2 ** S_t * (2 ** s[t] - 1)
    return tot


def q_of(m, s):
    n = sum(m)
    return 2 ** (sum(s) + n) - 3 ** n


def rotate(m, s, r):
    return m[r:] + m[:r], s[r:] + s[:r]


def content_gcd(m, s):
    return math.gcd(q_of(m, s), R0(m, s))  # math.gcd handles negative q via abs


def C_of(m, s):
    q = q_of(m, s)
    g = content_gcd(m, s)
    assert abs(q) > 1, "C undefined at |q| = 1"
    return math.log(g) / math.log(abs(q))


def W0(l):
    """The Lean file's fold, re-implemented from its definition."""
    if not l:
        return 0
    (m, s), rest = l[0], l[1:]
    return 3 ** sum(x[0] for x in rest) * 2 ** m * (2 ** s - 1) \
        + 2 ** (m + s) * W0(rest)


def msum(l):
    return sum(x[0] for x in l)


def mssum(l):
    return sum(x[0] + x[1] for x in l)


def rand_comp(total, parts):
    """Uniform composition of `total` into `parts` positive parts."""
    if parts == 1:
        return [total]
    cuts = sorted(random.sample(range(1, total), parts - 1))
    pts = [0] + cuts + [total]
    return [pts[i + 1] - pts[i] for i in range(parts)]


def is_proper_power(m, s):
    p = len(m)
    w = list(zip(m, s))
    return any(w == w[:t] * (p // t) for t in range(1, p) if p % t == 0)


def rand_word(pmin=2, pmax=6, emax=8):
    p = random.randint(pmin, pmax)
    return ([random.randint(1, emax) for _ in range(p)],
            [random.randint(1, emax) for _ in range(p)])


# ------------------------------------------------------------------- canaries
print("=" * 72)
print("CANARIES (hand-computed before any sweep)")
print("=" * 72)

# H1: trivial word squared ([1,1],[1,1]): n=2, K=4, q=16-9=7.
#     sigma=(2,2); term0 = 3^1*2^0*(2-1)=3; term1 = 3^0*2^2*(2-1)=4; R_0=7.
check("H1 trivial^2: q=7", q_of([1, 1], [1, 1]) == 7)
check("H1 trivial^2: R_0=7", R0([1, 1], [1, 1]) == 7)
check("H1 trivial^2: C=1 (gcd=|q|)", content_gcd([1, 1], [1, 1]) == 7)

# H2 (THE SCOPE CANARY): the -17 cycle's primitive word, m=(4,3), s=(1,3)
#     (cycles.md 12.6.1.2 anchor (k,m,q)=(7,11,-139); door-word ((4,1),(3,3))).
#     n=7, K=4+7=11, q=2^11-3^7=2048-2187=-139.
#     sigma_0=s_0+m_1=1+3=4, sigma_1=s_1+m_0=3+4=7.
#     term0 = 3^{M_0}2^{S_0}(2^{s_0}-1) = 3^3*2^0*(2^1-1) = 27.
#     term1 = 3^0*2^{sigma_0}*(2^3-1) = 16*7 = 112.  R_0 = 27+112 = 139.
#     gcd(-139,139) = 139 = |q|  =>  C = log 139/log 139 = 1 EXACTLY.
m17, s17 = [4, 3], [1, 3]
check("H2 -17 word: q = -139", q_of(m17, s17) == -139)
check("H2 -17 word: R_0 = 139 (hand: 27+112)", R0(m17, s17) == 139)
check("H2 -17 word: gcd(q,R_0) = 139 = |q|  (C = 1 exactly)",
      content_gcd(m17, s17) == 139)
check("H2 -17 word: primitive (not a proper power)",
      not is_proper_power(m17, s17))
# tuned/untuned status: tuned K would be bitlength(3^7) = 12; this word has K=11.
K17 = sum(s17) + sum(m17)
check("H2 -17 word: UNTUNED (K=11 < bitlength(3^7)=12, q < 0)",
      K17 == 11 and (3 ** 7).bit_length() == 12 and q_of(m17, s17) < 0)
print(f"  -17 canary: q={q_of(m17, s17)}, R_0={R0(m17, s17)}, "
      f"gcd={content_gcd(m17, s17)}, C={C_of(m17, s17):.6f} (exact 1), "
      f"primitive, untuned")

# H3: the (-5)-shore word ([2],[1]): n=2, K=3, q=8-9=-1; R_0=2^1-1=1.
#     |q|=1: C is 0/0 UNDEFINED — the spent-stock domain edge (12.6.1.2).
check("H3 (-5)-shore word: q=-1, R_0=1 (C undefined at |q|=1)",
      q_of([2], [1]) == -1 and R0([2], [1]) == 1)
# trivial word ([1],[1]): q=1, R_0=1 — same domain edge.
check("H3 trivial word: q=1, R_0=1 (C undefined at |q|=1)",
      q_of([1], [1]) == 1 and R0([1], [1]) == 1)

# H4: the p=7 staircase seed (cycles.md 12.8.3 / 12.6.1.1: gcd(q,R_r)=7).
m7 = [4, 7, 9, 15, 23, 35, 1]
n7 = sum(m7)  # 94
K7 = (3 ** n7).bit_length()  # tuned: 149
s7 = [1] * 6 + [K7 - n7 - 6]
check("H4 staircase seed: n=94, K=149", n7 == 94 and K7 == 149)
check("H4 staircase seed: gcd(q,R_0) = 7", content_gcd(m7, s7) == 7)
print(f"  staircase C = log 7/log|q| = {C_of(m7, s7):.4f} (near 0)")

# H5: the L-A2 canary ([1,1],[3,3]) = (1,3)^2: q=2^8-9=247=13*19, gcd=19.
check("H5 (1,3)^2: q=247, gcd=19", q_of([1, 1], [3, 3]) == 247
      and content_gcd([1, 1], [3, 3]) == 19)
print(f"  (1,3)^2: C = log 19/log 247 = {C_of([1, 1], [3, 3]):.4f}")

# H6: hand-computed T1/T2 numeric instances (matching the Lean file's canaries,
#     recomputed by hand here, not copied):
#     W0[(2,4),(3,1)] = 3^3*2^2*15 + 2^6*(2^3*1) = 1620+512 = 2132
#     W0[(2,3),(3,2)] = 3^3*2^2*7  + 2^5*(2^3*3) =  756+768 = 1524; diff = 608
#     = 2^(2+3)*(3^3-2^3) = 32*19 (T1, pre=suf=[], m1=2,s1=3,m2=3).
check("H6 T1 numeric: W0[(2,4),(3,1)]-W0[(2,3),(3,2)] = 608",
      W0([(2, 4), (3, 1)]) - W0([(2, 3), (3, 2)]) == 608 == 2 ** 5 * 19)
#     W0[(2,1),(1,3)] = 3*4*1 + 2^3*(2*7) = 12+112 = 124
#     W0[(1,1),(2,3)] = 9*2*1 + 2^2*(4*7) = 18+112 = 130; diff = -6
#     = -(3^1*2^1*(2^1-1))*... = -(3^{1+0}*2^1*1) = -6 (T2 at position 0).
check("H6 T2 numeric: W0[(2,1),(1,3)]-W0[(1,1),(2,3)] = -6",
      W0([(2, 1), (1, 3)]) - W0([(1, 1), (2, 3)]) == -6)

# H7: the bridge on the trivial^2 word: W0 = 2^{m_0} R_0 = 2*7 = 14.
check("H7 bridge: W0[(1,1),(1,1)] = 14 = 2^1 * R_0",
      W0([(1, 1), (1, 1)]) == 14 == 2 * R0([1, 1], [1, 1]))

if FAILURES:
    print("CANARY FAILURE — stopping before sweeps")
    raise SystemExit(1)
print("CANARIES: ALL PASS")

# ------------------------------------------------------- (a) the invariant
print()
print("=" * 72)
print("(a) THE INVARIANT: rotation invariance; C = 1 <=> q | R_0; range")
print("=" * 72)

# rotation invariance of gcd(q, R_r), random profiles, both signs, tuned + not
n_rot = 0
for _ in range(400):
    m, s = rand_word()
    gs = {math.gcd(q_of(*rotate(m, s, r)), R0(*rotate(m, s, r)))
          for r in range(len(m))}
    qs = {q_of(*rotate(m, s, r)) for r in range(len(m))}
    n_rot += 1
    if not (len(gs) == 1 and len(qs) == 1):
        check(f"rotation invariance at {m},{s}", False)
# tuned draws too
for _ in range(200):
    n = random.randint(10, 40)
    K = (3 ** n).bit_length()
    S = K - n
    p = random.randint(2, min(6, S, n))
    m, s = rand_comp(n, p), rand_comp(S, p)
    gs = {math.gcd(q_of(*rotate(m, s, r)), R0(*rotate(m, s, r)))
          for r in range(p)}
    n_rot += 1
    if len(gs) != 1:
        check(f"rotation invariance (tuned) at {m},{s}", False)
check(f"gcd(q, R_r) rotation-invariant on {n_rot} random profiles", True)
print(f"  rotation invariance: {n_rot}/{n_rot} profiles, gcd constant "
      f"across all rotations (both signs of q, tuned and untuned)")

# C = 1 <=> q | R_0, and C in [0,1], on random words with |q| > 1
n_range = 0
for _ in range(600):
    m, s = rand_word()
    q, r = q_of(m, s), R0(m, s)
    if abs(q) <= 1:
        continue
    g = math.gcd(q, r)
    n_range += 1
    # C in [0,1] <=> 1 <= g <= |q| (exact integer form)
    if not (1 <= g <= abs(q)):
        check(f"C-range at {m},{s}", False)
    # C = 1 <=> gcd = |q| <=> q | R_0 (exact integer form)
    if (g == abs(q)) != (r % abs(q) == 0):
        check(f"C=1 iff q|R_0 at {m},{s}", False)
check(f"C in [0,1] and (C=1 <=> q | R_0) exact on {n_range} words", True)
print(f"  range + divisibility equivalence: {n_range}/{n_range} exact")
print(f"  knowns: trivial^2 C=1; -17 word C=1 (|q|=139); "
      f"staircase C={C_of(m7, s7):.4f}; (1,3)^2 C={C_of([1,1],[3,3]):.4f}")
print("  domain note (flat): C is 0/0-undefined at |q| = 1 — exactly the")
print("  spent-stock words of 12.6.1.2 (trivial, -5 shore); the entry's")
print("  'C in [0,1]' silently assumes |q| > 1.")

# --------------------------------------------------- (b) the landscape
print()
print("=" * 72)
print("(b) LANDSCAPE (reduced scale, labeled spot checks)")
print("=" * 72)

# (b1) aperiodic tuned words at three depths: max C vs his 0.11-0.50 band
print("(b1) max C over sampled aperiodic tuned words "
      "(his REQ-MATH-018 (A): 0.11-0.50 at n=17..63, N=20000)")
print(f"  {'n':>4} {'N':>6} {'max C':>8} {'#C>0.20':>8} {'#C>0.35':>8}")
for n in [17, 25, 40]:
    K = (3 ** n).bit_length()
    S = K - n
    N = 4000
    mx, c20, c35 = 0.0, 0, 0
    for _ in range(N):
        p = random.randint(2, min(8, S, n))
        m, s = rand_comp(n, p), rand_comp(S, p)
        if is_proper_power(m, s):
            continue
        c = C_of(m, s)
        mx = max(mx, c)
        c20 += c > 0.20
        c35 += c > 0.35
    print(f"  {n:>4} {N:>6} {mx:>8.4f} {c20:>8} {c35:>8}")
check("(b1) spot check ran (no pass/fail: sampled band, labeled)", True)
print("  reading: max C stays low, tracking q's factorization — consistent")
print("  with his band at reduced sample size (spot check, not a key turn).")

# (b2) B^j climb: exact law from the descent identity (12.6.1.4)
#   R_0(B^j) = R_0(B) * G_j and q_P = q_B * G_j with G_j > 0, so
#   gcd(q_P, R_0(P)) = G_j * gcd(q_B, R_0(B))  exactly, whence
#   C(B^j) = (ln G_j + ln g_B) / (ln G_j + ln |q_B|)  -> 1,  and
#   C(B^j) = 1  <=>  g_B = |q_B|  <=>  C(B) = 1 (base is a cycle).
print()
print("(b2) B^j climb: exact via the descent identity (his 'per the L-A2 law')")


def G_factor(mB, sB, j):
    nB, KB = sum(mB), sum(sB) + sum(mB)
    return sum(3 ** ((j - 1 - c) * nB) * 2 ** (c * KB) for c in range(j))


n_climb = 0
for mB, sB in [([1], [3]), ([1, 2], [3, 1]), ([2, 1], [1, 3]),
               ([2], [1]), ([4, 3], [1, 3])]:  # incl. negative-q bases
    qB, rB = q_of(mB, sB), R0(mB, sB)
    gB = math.gcd(qB, rB)
    for j in [2, 3, 4, 6, 8]:
        mP, sP = mB * j, sB * j
        Gj = G_factor(mB, sB, j)
        n_climb += 3
        if not (R0(mP, sP) == rB * Gj):
            check(f"(b2) R_0 multiplicativity at {mB},{sB},j={j}", False)
        if not (q_of(mP, sP) == qB * Gj):
            check(f"(b2) q multiplicativity at {mB},{sB},j={j}", False)
        if not (math.gcd(q_of(mP, sP), R0(mP, sP)) == Gj * gB):
            check(f"(b2) gcd law at {mB},{sB},j={j}", False)
check(f"(b2) exact climb law on {n_climb} (base, j) identity checks", True)

# reproduce his table for base (1|3), q_B = 13 (spot: values in OUT-018)
print(f"  base (1|3), q_B=13: ", end="")
for j in [2, 3, 4, 6, 8]:
    print(f"C(B^{j})={C_of([1]*j, [3]*j):.4f}", end="  ")
print()
print(f"  base (1,2|3,1), q_B=101: ", end="")
for j in [2, 3, 4, 6, 8]:
    print(f"{C_of([1,2]*j, [3,1]*j):.4f}", end="  ")
print()
print("  rate: 1 - C(B^j) = ln(|q_B|/g_B)/ln(G_j |q_B|) ~ c/j  (G_j has")
print("  ~ (j-1) K_B bits) — climbs to 1 for EVERY base, divisible or not;")
print("  C(B^j) = 1 at finite j  <=>  C(B) = 1: repetition reaches C = 1")
print("  only from a base already a cycle (the descent, L-A4).")
n_reach = 0
for mB, sB in [([1], [3]), ([1, 2], [3, 1]), ([1, 1], [1, 1]), ([4, 3], [1, 3])]:
    qB = q_of(mB, sB)
    gB = math.gcd(qB, R0(mB, sB))
    base_c1 = (abs(qB) > 1 and gB == abs(qB)) or abs(qB) == 1
    for j in [2, 3, 4]:
        mP, sP = mB * j, sB * j
        gP = math.gcd(q_of(mP, sP), R0(mP, sP))
        n_reach += 1
        if (gP == abs(q_of(mP, sP))) != base_c1:
            check(f"(b2) C(B^j)=1 iff base cycle at {mB},{sB},j={j}", False)
check(f"(b2) C(B^j)=1 <=> base divisible: {n_reach} exact checks "
      "(incl. trivial^2 and -17 word as bases)", True)

# (b3) single-letter change at fixed (n, K): collapse spot check
print()
print("(b3) single-letter change at fixed q (his (C) cliff, reduced scale)")
print(f"  {'word':>18} {'C(word)':>8} {'#pert':>6} {'max C pert':>11} "
      f"{'mean C pert':>11}")
for mB, sB, j in [([1, 2], [3, 1], 3), ([1, 2], [3, 1], 4), ([1], [3], 6)]:
    mP, sP = mB * j, sB * j
    q0 = q_of(mP, sP)
    c0 = C_of(mP, sP)
    mx, sm, cnt = 0.0, 0.0, 0
    while cnt < 100:
        m2, s2 = mP[:], sP[:]
        if random.random() < 0.5:
            i, k = random.sample(range(len(m2)), 2)
            if m2[k] < 2:
                continue
            m2[i] += 1
            m2[k] -= 1
        else:
            i, k = random.sample(range(len(s2)), 2)
            if s2[k] < 2:
                continue
            s2[i] += 1
            s2[k] -= 1
        assert q_of(m2, s2) == q0
        cp = C_of(m2, s2)
        mx, sm, cnt = max(mx, cp), sm + cp, cnt + 1
    print(f"  {'('+str(mB)+'|'+str(sB)+')^'+str(j):>18} {c0:>8.4f} "
          f"{cnt:>6} {mx:>11.4f} {sm/cnt:>11.4f}")
check("(b3) collapse spot check ran (labeled, sampled)", True)

# ------------------------------------------- (c) T1/T2 clean-room
print()
print("=" * 72)
print("(c) T1/T2 CLEAN-ROOM: derived closed forms, verified exactly")
print("=" * 72)
print("""  Derivation (this session, from the W0 fold alone — written out in the
  findings file):
   prefix lemma: if msum(r1) = msum(r2) then
     W0(pre++r1) - W0(pre++r2) = 2^{mssum pre} (W0(r1) - W0(r2))
   (prefix terms depend on the tail only through its m-mass; each prefix
   letter contributes the factor 2^{m+s} to the tail's contribution).
   Two-letter tails, sigma := msum suf, V := W0(suf):
   T1 (s-transfer): W0((m1,s1+1)::(m2,c)::suf) - W0((m1,s1)::(m2,c+1)::suf)
     = 3^{m2+sigma} 2^{m1}(2^{s1+1}-2^{s1})
       + 3^{sigma} 2^{m2} [2^{m1+s1+1}(2^c-1) - 2^{m1+s1}(2^{c+1}-1)]
       + V [2^{m1+s1+1+m2+c} - 2^{m1+s1+m2+c+1}]
     = 3^{sigma} 2^{m1+s1} (3^{m2} - 2^{m2})        (V-bracket = 0)
   T2 (m-transfer): W0((m1+1,s1)::(m2,s2)::suf) - W0((m1,s1)::(m2+1,s2)::suf)
     = (2^{s1}-1) 2^{m1} (2 - 3) 3^{m2+sigma} + 0
     = -3^{m2+sigma} 2^{m1} (2^{s1} - 1)
   With the prefix factor 2^{mssum pre}: exactly the Lean file's T1/T2.""")

# exhaustive grid: pre, suf of lengths 0..1 over {1,2}^2; core letters {1,2,3}
words01 = [[]] + [[(a, b)] for a in (1, 2) for b in (1, 2)]
nT1 = nT2 = 0
for pre in words01:
    for suf in words01:
        for m1 in (1, 2, 3):
            for s1 in (1, 2, 3):
                for m2 in (1, 2, 3):
                    for c in (1, 2, 3):
                        d = W0(pre + [(m1, s1 + 1), (m2, c)] + suf) \
                            - W0(pre + [(m1, s1), (m2, c + 1)] + suf)
                        pred = 2 ** mssum(pre) * 3 ** msum(suf) \
                            * 2 ** (m1 + s1) * (3 ** m2 - 2 ** m2)
                        nT1 += 1
                        if d != pred:
                            check(f"T1 exhaustive {pre},{suf},{m1},{s1},{m2},{c}",
                                  False)
                        d = W0(pre + [(m1 + 1, s1), (m2, c)] + suf) \
                            - W0(pre + [(m1, s1), (m2 + 1, c)] + suf)
                        pred = -(2 ** mssum(pre) * 3 ** (m2 + msum(suf))
                                 * 2 ** m1 * (2 ** s1 - 1))
                        nT2 += 1
                        if d != pred:
                            check(f"T2 exhaustive {pre},{suf},{m1},{s1},{m2},{c}",
                                  False)
check(f"T1 derived form exhaustive: {nT1}/{nT1} exact", True)
check(f"T2 derived form exhaustive: {nT2}/{nT2} exact", True)

# random draws, larger scale (target: his 713/604 or better)
nT1r = nT2r = 0
for _ in range(900):
    pre = [(random.randint(1, 9), random.randint(1, 9))
           for _ in range(random.randint(0, 4))]
    suf = [(random.randint(1, 9), random.randint(1, 9))
           for _ in range(random.randint(0, 4))]
    m1, s1, m2, c, s2 = (random.randint(1, 9) for _ in range(5))
    d = W0(pre + [(m1, s1 + 1), (m2, c)] + suf) \
        - W0(pre + [(m1, s1), (m2, c + 1)] + suf)
    nT1r += 1
    if d != 2 ** mssum(pre) * 3 ** msum(suf) * 2 ** (m1 + s1) \
            * (3 ** m2 - 2 ** m2):
        check("T1 random draw", False)
    d = W0(pre + [(m1 + 1, s1), (m2, s2)] + suf) \
        - W0(pre + [(m1, s1), (m2 + 1, s2)] + suf)
    nT2r += 1
    if d != -(2 ** mssum(pre) * 3 ** (m2 + msum(suf)) * 2 ** m1
              * (2 ** s1 - 1)):
        check("T2 random draw", False)
check(f"T1 random: {nT1r}/{nT1r} exact; T2 random: {nT2r}/{nT2r} exact", True)

# bridge W0 = 2^{m_0} R_0 (my two independent implementations)
n_br = 0
for _ in range(400):
    m, s = rand_word(pmin=1)
    n_br += 1
    if W0(list(zip(m, s))) != 2 ** m[0] * R0(m, s):
        check(f"bridge at {m},{s}", False)
check(f"bridge W0 = 2^(m_0) R_0: {n_br}/{n_br} exact", True)

# R0-frame forms (REQ-MATH-019's statement): interior transfers directly,
# i=0 m-transfer via rotation reduction (gcd rotation-invariant)
nR1 = nR2 = nR2a = 0
for _ in range(800):
    m, s = rand_word(pmin=3, pmax=8, emax=9)
    p = len(m)
    q = q_of(m, s)
    sig = [s[t] + m[(t + 1) % p] for t in range(p)]
    Ma = [sum(m[t + 1:]) for t in range(p)]
    Sp = [sum(sig[:t]) for t in range(p)]
    i = random.randint(0, p - 2)
    if s[i + 1] >= 2:
        s2 = s[:]
        s2[i] += 1
        s2[i + 1] -= 1
        assert q_of(m, s2) == q
        nR1 += 1
        if R0(m, s2) - R0(m, s) != 3 ** Ma[i + 1] * 2 ** (Sp[i] + s[i]) \
                * (3 ** m[i + 1] - 2 ** m[i + 1]):
            check("R0-frame T1", False)
    i = random.randint(1, p - 2)
    if m[i + 1] >= 2:
        m2 = m[:]
        m2[i] += 1
        m2[i + 1] -= 1
        assert q_of(m2, s) == q
        nR2 += 1
        if R0(m2, s) - R0(m, s) != -(3 ** (Ma[i] - 1)) * 2 ** Sp[i] \
                * (2 ** s[i] - 1):
            check("R0-frame T2 interior", False)
    # i = 0 m-transfer: no closed form in R0 (the wrap changes sigma_{p-1});
    # reduction: gcd(q, R_r) is rotation-invariant (12.6.1.1), so shared
    # content of the i=0 pair equals that of the rotated (interior) pair.
    if m[1] >= 2:
        m2 = m[:]
        m2[0] += 1
        m2[1] -= 1
        mr, sr = rotate(m, s, p - 1)
        mr2, _ = rotate(m2, s, p - 1)
        g_dir = math.gcd(math.gcd(q, R0(m, s)), R0(m2, s))
        g_rot = math.gcd(math.gcd(q, R0(mr, sr)), R0(mr2, sr))
        nR2a += 1
        if not (g_dir == g_rot and (2 ** s[0] - 1) % g_dir == 0):
            check("R0-frame T2 i=0 rotation reduction", False)
check(f"R0-frame T1: {nR1}, T2 interior: {nR2}, T2 i=0 via rotation: {nR2a} "
      "- all exact", True)

# corollary: shared divisor of q divides the letter-scale seam; m=1/s=1 isolation
nC = iso = 0
nM1 = 0
for _ in range(700):
    m, s = rand_word(pmin=2, pmax=8, emax=9)
    p = len(m)
    q = q_of(m, s)
    i = random.randint(0, p - 2)
    if random.random() < 0.5 and s[i + 1] >= 2:
        s2 = s[:]
        s2[i] += 1
        s2[i + 1] -= 1
        shared = math.gcd(math.gcd(q, R0(m, s)), R0(m, s2))
        seam = 3 ** m[i + 1] - 2 ** m[i + 1]
        if m[i + 1] == 1:
            nM1 += 1
            if shared != 1:
                check("m=1 total isolation (T1)", False)
    elif m[i + 1] >= 2:
        m2 = m[:]
        m2[i] += 1
        m2[i + 1] -= 1
        shared = math.gcd(math.gcd(q, R0(m, s)), R0(m2, s))
        seam = 2 ** s[i] - 1
        if s[i] == 1:
            nM1 += 1
            if shared != 1:
                check("s=1 total isolation (T2)", False)
    else:
        continue
    nC += 1
    if seam % shared != 0:
        check(f"corollary at {m},{s},i={i}", False)
    iso += shared == 1
check(f"corollary (shared | letter seam): {nC}/{nC}; total isolation "
      f"(shared=1): {iso}/{nC}; unit-seam cases (m=1 or s=1): {nM1}, all "
      "shared=1", True)

# ------------------------------------- (d) the gloss: computed exhibits
print()
print("=" * 72)
print("(d) GLOSS ADJUDICATION: the computed exhibits")
print("=" * 72)

# Exhibit 1: the -17 word is an EXISTING aperiodic (primitive) C=1 peak...
print(f"Exhibit 1 — the -17 word (m,s) = ({m17},{s17}):")
print(f"  primitive: {not is_proper_power(m17, s17)}; "
      f"C = {C_of(m17, s17):.1f} exactly (gcd = |q| = 139); untuned (q<0).")

# Exhibit 2: ...and it is TOTALLY ISOLATED: every adjacent-transfer neighbour
# shares content 1 with it — separation and peak existence coexist.
q17 = q_of(m17, s17)
g17 = content_gcd(m17, s17)
worst = 1
neigh = 0
for (mm, ss) in [(m17, s17)] + [rotate(m17, s17, r) for r in range(1, 2)]:
    p = len(mm)
    for i in range(p - 1):
        if ss[i + 1] >= 2:
            s2 = ss[:]
            s2[i] += 1
            s2[i + 1] -= 1
            sh = math.gcd(math.gcd(q17, R0(mm, ss)), R0(mm, s2))
            worst = max(worst, sh)
            neigh += 1
        if mm[i + 1] >= 2:
            m2 = mm[:]
            m2[i] += 1
            m2[i + 1] -= 1
            sh = math.gcd(math.gcd(q17, R0(mm, ss)), R0(m2, ss))
            worst = max(worst, sh)
            neigh += 1
        # reverse transfers
        if ss[i] >= 2:
            s2 = ss[:]
            s2[i] -= 1
            s2[i + 1] += 1
            sh = math.gcd(math.gcd(q17, R0(mm, ss)), R0(mm, s2))
            worst = max(worst, sh)
            neigh += 1
        if mm[i] >= 2:
            m2 = mm[:]
            m2[i] -= 1
            m2[i + 1] += 1
            sh = math.gcd(math.gcd(q17, R0(mm, ss)), R0(m2, ss))
            worst = max(worst, sh)
            neigh += 1
check(f"Exhibit 2: -17 peak totally isolated — worst shared content over "
      f"{neigh} adjacent-transfer neighbours (both rotations) = {worst}",
      worst == 1)
print(f"  consistency: T1 seam at the -17 word is 3^3-2^3 = 19; "
      f"gcd(139, 19) = {math.gcd(139, 19)} — the corollary FORCES isolation")
print("  => an aperiodic C = 1 peak EXISTS and IS totally isolated: the")
print("     separation lemma and the peak's existence coexist. Adjacency")
print("     isolation does not exclude isolated peaks.")

# Exhibit 3: what repetition does and does not reach (from (b2), restated):
print("Exhibit 3 — repetition: C(B^j) -> 1 for EVERY base (divisible or not),")
print("  and C(B^j) = 1 at finite j iff C(B) = 1 (checked exactly in (b2)).")
print("  So 'the only road to C = 1 is exact repetition' fails in both")
print("  directions: repetition is a road to the LIMIT 1 for every base but")
print("  REACHES 1 only from a cycle; and nothing in T1/T2 excludes an")
print("  isolated aperiodic peak — reaching C = 1 is exactly q | R_0.")

# ---------------------------------------------------------------- summary
print()
print("=" * 72)
print(f"TOTAL: {CHECKS[0]} recorded checks, {len(FAILURES)} failures")
if FAILURES:
    for f in FAILURES:
        print(f"  FAILED: {f}")
    raise SystemExit(1)
print("ALL PASS")
