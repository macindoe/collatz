"""Clean-room statement check for ContentDescent.lean (Merle Lean repo, commit 67c428a).

Supports: briefs/merle-la5-closure-findings.md (delegated session, 2026-07-25;
brief: briefs/merle-la5-closure-check-brief.md, item 5).

Fresh code: imports nothing from any Merle repository and nothing from prior
Merle-check scripts. Conventions re-implemented from cycles.md 12.6.1 /
12.6.1.1 / 12.6.1.4 only:

    profile (word) = ((m_0, s_0), ..., (m_{p-1}, s_{p-1})), entries >= 1
    n = sum m_t,  K = sum s_t + n,  q = 2^K - 3^n
    sigma_t = s_t + m_{(t+1) mod p}
    M_t = sum_{j>t} m_j,  S_t = sum_{j<t} sigma_j
    R_0 = sum_t 3^{M_t} 2^{S_t} (2^{s_t} - 1)
    W0  = 2^{m_0} * R_0  (nonempty; W0([]) := 0 by convention)

Note S_t = sum_{j<t} s_j + sum_{j=1..t} m_j never involves the wrap term, so
R_0 and hence W0 are well defined on a *linear* word; the wrap convention only
matters for rotations, which this script does not use.

The Lean statements checked, as read at 67c428a (exact integer arithmetic at
every pass/fail decision):

    W0_append  (cocycle):   W0(l1 ++ l2) = 3^{msum l2} W0(l1) + 2^{mssum l1} W0(l2)
    power_mult:             W0(B^k) = G_k * W0(B)
    q_pow_factor:           q(B^k) = G_k * q(B)
    cycle_iff  (k >= 1):    q(B^k) | W0(B^k)  <=>  q(B) | W0(B)
    gcd_climb:              gcd(q(B^k), W0(B^k)) = G_k * gcd(q(B), W0(B))

with G_k = geom(B, k) defined recursively as in the Lean file
(geom 0 = 0; geom (k+1) = 3^{k*msum} + 2^{mssum} * geom k), checked at every
use against 12.6.1.4's closed form G_k = sum_{c<k} 3^{(k-1-c) n_B} 2^{c K_B}
and against the cofactor q(B^k)/q(B) the descent identity produces.

Domain note, flat: the Lean file quantifies over List (N x N) with zero entries
allowed — a superset of the wiki's entries->=1 convention. This script checks
the laws on the wiki's domain (entries >= 1), where the two agree; the Lean
statements are strictly more general.

Canaries are hand-computed and printed before any sweep.
"""

import math
import random
from itertools import product

FAILURES = []
CHECKS = 0


def check(label, ok):
    global CHECKS
    CHECKS += 1
    if not ok:
        FAILURES.append(label)
        print("FAIL:", label)


# ---------------------------------------------------------------- conventions

def msum(word):
    return sum(m for m, s in word)


def mssum(word):
    return sum(m + s for m, s in word)


def q_of(word):
    n = msum(word)
    K = mssum(word)  # K = sum s + sum m
    return 2 ** K - 3 ** n


def R0(word):
    """cycles.md 12.6.1: R_0 = sum_t 3^{M_t} 2^{S_t} (2^{s_t} - 1)."""
    p = len(word)
    total = 0
    for t in range(p):
        M_t = sum(word[j][0] for j in range(t + 1, p))
        S_t = sum(word[j][1] for j in range(t)) + sum(word[j][0] for j in range(1, t + 1))
        total += 3 ** M_t * 2 ** S_t * (2 ** word[t][1] - 1)
    return total


def W0(word):
    if not word:
        return 0
    return 2 ** word[0][0] * R0(word)


def geom_rec(word, k):
    """The Lean file's recursive G_k."""
    g = 0
    for j in range(k):  # g goes geom(0) -> geom(k)
        g = 3 ** (j * msum(word)) + 2 ** mssum(word) * g
    return g


def geom_closed(word, k):
    """12.6.1.4: G_k = sum_{c<k} 3^{(k-1-c) n_B} 2^{c K_B}."""
    n, K = msum(word), mssum(word)
    return sum(3 ** ((k - 1 - c) * n) * 2 ** (c * K) for c in range(k))


def gcd(a, b):
    return math.gcd(abs(a), abs(b))


def divides(a, b):
    return a != 0 and b % a == 0


# ------------------------------------------------------------------- canaries

print("=" * 72)
print("CANARIES (hand-computed first, printed before any sweep)")
print("=" * 72)

# C1: trivial word. R_0 = 3^0 2^0 (2^1-1) = 1; W0 = 2^1 * 1 = 2; q = 2^2-3 = 1.
w = ((1, 1),)
print(f"C1 trivial word ((1,1)): R0 = {R0(w)} (hand: 1), W0 = {W0(w)} (hand: 2), q = {q_of(w)} (hand: 1)")
check("C1 R0", R0(w) == 1)
check("C1 W0", W0(w) == 2)
check("C1 q", q_of(w) == 1)

# C2: trivial square. sigma_0 = 2; terms 3^1*1*1 = 3 and 2^2*1 = 4; R_0 = 7;
# W0 = 14; q = 2^4 - 3^2 = 7. Lean canary 1: W0(B^2) = 7 * W0(B) = 14.
w2 = ((1, 1), (1, 1))
print(f"C2 trivial square: R0 = {R0(w2)} (hand: 7), W0 = {W0(w2)} (hand: 14), q = {q_of(w2)} (hand: 7)")
check("C2 R0", R0(w2) == 7)
check("C2 W0", W0(w2) == 14)
check("C2 q", q_of(w2) == 7)
check("C2 Lean canary 1: W0(B^2) = 7*W0(B)", W0(w2) == 7 * W0(w))
check("C2 Lean canary 2: q(B^2) | W0(B^2)", divides(q_of(w2), W0(w2)))

# C3: cocycle by hand. l1 = ((1,2),), l2 = ((2,1),).
# W0(l1) = 2*(2^2-1) = 6; W0(l2) = 4*(2^1-1) = 4.
# l1++l2 = ((1,2),(2,1)): terms 3^2*1*(2^2-1) = 27 and 2^4*(2^1-1) = 16;
# R_0 = 43, W0 = 2*43 = 86. RHS = 3^2*6 + 2^3*4 = 54 + 32 = 86.
l1, l2 = ((1, 2),), ((2, 1),)
lhs = W0(l1 + l2)
rhs = 3 ** msum(l2) * W0(l1) + 2 ** mssum(l1) * W0(l2)
print(f"C3 cocycle ((1,2)) ++ ((2,1)): LHS = {lhs} (hand: 86), RHS = {rhs} (hand: 86)")
check("C3 cocycle hand instance", lhs == 86 and rhs == 86)

# C4: the -17 word, m = (4,3), s = (1,3) => ((4,1),(3,3)).
# n = 7, K = 11, q = 2048 - 2187 = -139; R_0 = 27 + 112 = 139; W0 = 16*139 = 2224.
# G_2 = 3^7 + 2^11 = 4235; q(B^2) = 2^22 - 3^14 = -588665 = -139 * 4235.
wm17 = ((4, 1), (3, 3))
print(f"C4 -17 word: q = {q_of(wm17)} (hand: -139), R0 = {R0(wm17)} (hand: 139), W0 = {W0(wm17)} (hand: 2224)")
check("C4 q", q_of(wm17) == -139)
check("C4 R0", R0(wm17) == 139)
check("C4 W0", W0(wm17) == 2224)
g2 = geom_rec(wm17, 2)
print(f"C4 G_2 = {g2} (hand: 4235), q(B^2) = {q_of(wm17 * 2)} (hand: -588665)")
check("C4 G_2", g2 == 4235)
check("C4 q factorization", q_of(wm17 * 2) == g2 * q_of(wm17))
check("C4 cycle: q | R0", divides(q_of(wm17), R0(wm17)))

# C5: geom recursive = closed, small hand values. B = ((1,1)): G_1 = 1, G_2 = 3+4 = 7.
print(f"C5 geom(trivial, 1) = {geom_rec(w, 1)} (hand: 1); geom(trivial, 2) = {geom_rec(w, 2)} (hand: 7)")
check("C5 G_1", geom_rec(w, 1) == 1 and geom_closed(w, 1) == 1)
check("C5 G_2", geom_rec(w, 2) == 7 and geom_closed(w, 2) == 7)

# C6: cycle_iff, one instance each direction.
# Forward (cycle base): trivial word, q = 1 | W0 = 2; square q = 7 | 14. (C2 above.)
# Non-cycle base: ((1,2)): q = 5, W0 = 6, 5 does not divide 6;
# square: q = 2^6 - 3^2 = 55, G_2 = 3 + 8 = 11, W0 = 66, 55 does not divide 66.
wnc = ((1, 2),)
print(f"C6 non-cycle base ((1,2)): q = {q_of(wnc)} (hand: 5), W0 = {W0(wnc)} (hand: 6), "
      f"q(B^2) = {q_of(wnc * 2)} (hand: 55), W0(B^2) = {W0(wnc * 2)} (hand: 66)")
check("C6 base non-divisible", not divides(q_of(wnc), W0(wnc)))
check("C6 square non-divisible", not divides(q_of(wnc * 2), W0(wnc * 2)))
check("C6 cycle_iff forward (trivial)", divides(q_of(w), W0(w)) and divides(q_of(w2), W0(w2)))

print(f"\nCanaries: {CHECKS} checks, {len(FAILURES)} failures")
assert not FAILURES, "canary failure -- stop before sweeps"

# --------------------------------------------------- sweep 1: cocycle W0_append

print()
print("=" * 72)
print("SWEEP 1 -- cocycle W0(l1 ++ l2) = 3^msum(l2) W0(l1) + 2^mssum(l1) W0(l2)")
print("=" * 72)

# Exhaustive: all words of length 0..2 with entries in {1,2} (1 + 4 + 16 = 21
# words), all ordered pairs: 441 checks.
small_words = [()]
for length in (1, 2):
    for letters in product(product((1, 2), (1, 2)), repeat=length):
        small_words.append(tuple(letters))

count0 = CHECKS
for a in small_words:
    for b in small_words:
        ok = W0(a + b) == 3 ** msum(b) * W0(a) + 2 ** mssum(a) * W0(b)
        check(f"cocycle exhaustive {a} ++ {b}", ok)
print(f"exhaustive pairs: {CHECKS - count0} checks")

# Random: 300 draws, lengths 0..4 each side, entries 1..9 (both signs of q occur).
rng = random.Random(20260725)


def rand_word(rng, lmin, lmax, emax=9):
    length = rng.randint(lmin, lmax)
    return tuple((rng.randint(1, emax), rng.randint(1, emax)) for _ in range(length))


count0 = CHECKS
signs = {1: 0, -1: 0}
for i in range(300):
    a = rand_word(rng, 0, 4)
    b = rand_word(rng, 0, 4)
    if a + b:
        signs[1 if q_of(a + b) > 0 else -1] += 1
    ok = W0(a + b) == 3 ** msum(b) * W0(a) + 2 ** mssum(a) * W0(b)
    check(f"cocycle random #{i}", ok)
print(f"random pairs: {CHECKS - count0} checks (concatenated q > 0: {signs[1]}, q < 0: {signs[-1]})")

# ------------------------------- sweep 2: power laws on a grid (12.6.1.4 frame)

print()
print("=" * 72)
print("SWEEP 2 -- power_mult / q_pow_factor / gcd_climb / cycle_iff on a grid,")
print("          geom checked recursive == closed == q-cofactor at every pair")
print("=" * 72)

# Grid A, exhaustive: bases of length 1..2, entries in {1,2,3} (9 + 81 = 90),
# k in {1,2,3,4}. Grid B, random: 60 bases of length 3..6, entries 1..8,
# k in {2,3,4}.
bases = []
for length in (1, 2):
    for letters in product(product((1, 2, 3), (1, 2, 3)), repeat=length):
        bases.append(tuple(letters))
grid = [(b, k) for b in bases for k in (1, 2, 3, 4)]
rand_bases = [rand_word(rng, 3, 6, 8) for _ in range(60)]
grid += [(b, k) for b in rand_bases for k in (2, 3, 4)]

count0 = CHECKS
div_bases = 0
neg_q = 0
for b, k in grid:
    P = b * k
    g_r, g_c = geom_rec(b, k), geom_closed(b, k)
    qb, qP = q_of(b), q_of(P)
    if qb < 0:
        neg_q += 1
    check(f"geom rec==closed {b} k={k}", g_r == g_c)
    check(f"geom is q-cofactor {b} k={k}", qP == g_r * qb)
    check(f"power_mult {b} k={k}", W0(P) == g_r * W0(b))
    check(f"R0 descent identity {b} k={k}", R0(P) == g_r * R0(b))
    check(f"gcd_climb {b} k={k}", gcd(qP, W0(P)) == g_r * gcd(qb, W0(b)))
    check(f"gcd(q,W0)==gcd(q,R0) {b} k={k}",
          gcd(qb, W0(b)) == gcd(qb, R0(b)) and gcd(qP, W0(P)) == gcd(qP, R0(P)))
    check(f"cycle_iff {b} k={k}", divides(qP, W0(P)) == divides(qb, W0(b)))
    if divides(qb, W0(b)):
        div_bases += 1
print(f"grid: {len(grid)} (base, k) pairs, {CHECKS - count0} checks "
      f"({div_bases} divisible-base pairs, all inherited; {neg_q} negative-q bases)")

# ------------------------------------------------------------------- summary

print()
print("=" * 72)
print(f"TOTAL: {CHECKS} exact checks, {len(FAILURES)} failures")
print("=" * 72)
if FAILURES:
    for f in FAILURES:
        print("  FAILED:", f)
    raise SystemExit(1)
print("All checks passed: the Lean statements of ContentDescent.lean, as read,")
print("are exactly the laws of cycles.md 12.6.1.4 (descent identity, q-cofactor,")
print("gcd law one level up) plus the cocycle, on the wiki's domain.")
