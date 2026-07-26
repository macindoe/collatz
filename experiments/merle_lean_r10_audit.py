#!/usr/bin/env python3
"""
merle_lean_r10_audit.py — statement-level canaries for the round-10 read-not-built
Lean audit of Merle's DeficitLemma.lean and T1Structure.lean (repo
ericmerle3789/one-obstruction-three-faces-lean, HEAD 5c9b663), plus the independent
convergent-denominator computation for discharge_all / convPairs.

Supports: briefs/merle-lean-r10-audit-findings.md (brief: briefs/merle-lean-r10-audit-brief.md).

Protocol: fresh code — imports nothing from any Merle repository and runs none of his
scripts; every pass/fail decision on an inequality of integers is made in exact integer
arithmetic; the only floats are reporting margins (log2 of exact integers) and the
high-precision Decimal computation of log2(3), done at TWO precisions (150 and 250
digits, >= 60 guard digits beyond anything used) with a stability assertion.

This is a STATEMENT-level check: a false Lean *statement* would be caught here even
without a kernel. It does not re-run the kernel (no Lean toolchain on this machine).
"""

from fractions import Fraction
from decimal import Decimal, getcontext
from math import comb, log2, isqrt
import random

random.seed(20260726)

PASS = 0
FAIL = 0
def check(ok, label):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {label}")

print("=" * 78)
print("PART A — DeficitLemma.lean statement canaries (exact integers)")
print("=" * 78)

# ---------------------------------------------------------------- A1 deficit_term_le
# theorem deficit_term_le (m k : N) (h : k <= m) :
#   12^k * 7^(m-k) * C(m,k) <= 19^m
print("\n[A1] deficit_term_le: 12^k * 7^(m-k) * C(m,k) <= 19^m for k <= m")
n_checks = 0
for m in range(0, 26):                      # exhaustive small grid incl. m = 0
    for k in range(0, m + 1):               # includes edges k = 0 and k = m
        check(12**k * 7**(m - k) * comb(m, k) <= 19**m, f"deficit_term_le m={m} k={k}")
        n_checks += 1
for _ in range(40):                         # large random instances
    m = random.randint(26, 400)
    k = random.randint(0, m)
    check(12**k * 7**(m - k) * comb(m, k) <= 19**m, f"deficit_term_le m={m} k={k}")
    n_checks += 1
for m in (50, 100, 200, 400):               # forced edges at large m
    for k in (0, m):
        check(12**k * 7**(m - k) * comb(m, k) <= 19**m, f"deficit_term_le edge m={m} k={k}")
        n_checks += 1
print(f"  {n_checks} instances, exhaustive m<=25 + 40 random to m=400 + edges: all hold")

# The file's five canaries, reproduced independently:
check(comb(10, 4) == 210, "C(10,4) = 210")
check(12**4 * 7**6 * 210 < 19**10, "canary 3 strict")
check(12**10 * 7**15 * comb(25, 10) <= 19**25, "canary 4")
check(12**7 * 7**0 * comb(7, 7) <= 19**7, "canary 5 edge k=m")

# ---------------------------------------------------------------- A2 the three atoms
print("\n[A2] atoms (exact; margins in bits reported as floats of exact ints)")
lhs, rhs = 19**195, 14**195 * 2**86
check(lhs <= rhs, "atom_A: 19^195 <= 14^195 * 2^86")
print(f"  atom_A margin: {log2(rhs) - log2(lhs):.3f} bits (his: 0.088)")
lhs, rhs = 3**86 * 2**15 * 7**195, 12**195
check(lhs <= rhs, "atom_a: 3^86 * 2^15 * 7^195 <= 12^195")
print(f"  atom_a margin: {log2(rhs) - log2(lhs):.3f} bits (his: 0.327)")
lhs, rhs = 2**101 * 3**86, 2**562
check(lhs <= rhs, "atom_D: 2^101 * 3^86 <= 2^562")
print(f"  atom_D margin: {log2(rhs) - log2(lhs):.3f} bits (his: ~325)")
check(3**86 <= 2**461, "atom_D reduced form: 3^86 <= 2^461")
check(3**86 <= 4**86 and 4**86 == 2**172, "atom_D soft chain: 3^86 <= 4^86 = 2^172")

# ---------------------------------------------------------------- A3 assembly chain
# hub (k j) : 2^(k+j+2) <= 2 * 3^(k+1)
# key_core     : 2^(86(k+j+2)) * 2^(15(k+1)) * 7^(195k) <= 2^562 * 12^(195k)
# key_shifted  : 2^(86(k+j))   * 2^(15(k+1)) * 7^(195k) <= 2^390 * 12^(195k)
# key15        : 19^(195(k+j)) * 2^(15(k+1)) <= 2^(195(k+j+2)) * 12^(195k) * 7^(195j)
# margin_core  : C(k+j, k)^13 * 2^(k+1) <= 2^(13(k+j+2))
print("\n[A3] key_core / key_shifted / key15 / margin_core on all hub-valid (k,j), k<=40")
n_core = n_shift = n_15 = n_mc = 0
hub_boundary = []
for k in range(0, 41):
    j = 0
    while 2**(k + j + 2) <= 2 * 3**(k + 1):
        if k <= 12:  # the 195-exponent statements get big fast; exact but keep k modest
            check(2**(86*(k+j+2)) * 2**(15*(k+1)) * 7**(195*k) <= 2**562 * 12**(195*k),
                  f"key_core k={k} j={j}")
            n_core += 1
            check(2**(86*(k+j)) * 2**(15*(k+1)) * 7**(195*k) <= 2**390 * 12**(195*k),
                  f"key_shifted k={k} j={j}")
            n_shift += 1
            check(19**(195*(k+j)) * 2**(15*(k+1)) <= 2**(195*(k+j+2)) * 12**(195*k) * 7**(195*j),
                  f"key15 k={k} j={j}")
            n_15 += 1
        check(comb(k + j, k)**13 * 2**(k + 1) <= 2**(13*(k + j + 2)),
              f"margin_core k={k} j={j}")
        n_mc += 1
        j += 1
    hub_boundary.append((k, j - 1))
print(f"  key_core {n_core}, key_shifted {n_shift}, key15 {n_15} (k<=12), margin_core {n_mc} (k<=40): all hold")
# hub is load-bearing: just past the boundary, margin_core's conclusion can still hold
# (it is a weaker statement) but key15's must eventually fail; find one failure.
found = None
for k in range(0, 12):
    j = hub_boundary[k][1] + 1
    while found is None and j < hub_boundary[k][1] + 60:
        if not (19**(195*(k+j)) * 2**(15*(k+1)) <= 2**(195*(k+j+2)) * 12**(195*k) * 7**(195*j)):
            found = (k, j)
        j += 1
    if found:
        break
check(found is not None, "key15 fails somewhere outside hub (hypothesis load-bearing)")
print(f"  key15 first found failure outside hub: (k,j) = {found}")

# ---------------------------------------------------------------- A4 marginTarget
# theorem marginTarget (n K) (1 <= n) (3^n <= 2^K) (2^K < 2*3^n) :
#   C(K-2, n-1)^13 * 2^n <= 2^(13K)
print("\n[A4] marginTarget: hypothesis range pins K uniquely; conclusion exact, n = 1..300")
n_mt = 0
for n in range(1, 301):
    Ks = [K for K in range(1, 2 * n + 4) if 3**n <= 2**K < 2 * 3**n]
    check(len(Ks) == 1, f"K-range uniqueness at n={n}")
    K = Ks[0]
    check(K == (3**n).bit_length(), f"K = bitlength(3^n) (tuned north K0) at n={n}")
    check(comb(K - 2, n - 1)**13 * 2**n <= 2**(13 * K), f"marginTarget n={n} K={K}")
    n_mt += 1
print(f"  {n_mt} scales: hypothesis K is UNIQUE per n and equals the tuned north K0;")
print("  conclusion holds at every one (exact integers).")
# Hypotheses are load-bearing: outside the K-window the conclusion can fail.
bad = (100, 200)     # 2^200 = 4^100 > 2*3^100, outside the window
n, K = bad
outside = not (3**n <= 2**K < 2 * 3**n)
fails = not (comb(K - 2, n - 1)**13 * 2**n <= 2**(13 * K))
check(outside and fails, "conclusion FAILS at (n,K)=(100,200), which violates the K-window")
print(f"  load-bearing check: at (n,K)={bad} (outside window) the conclusion fails: {fails}")

# ---------------------------------------------------------------- A5 encoding checks
print("\n[A5] the encoding: C(K-2,n-1) IS the L-A7 word count; the unfolding to margin(n)")
# (a) word count as summed compositions (Vandermonde): the cell (n,S) word count of the
# general family — words of r two-part letters (m_i,s_i), all parts >= 1, sum m = n,
# sum s = S — is sum_r C(n-1,r-1)*C(S-1,r-1) = C(n+S-2, n-1).
n_vd = 0
for n in range(1, 13):
    for S in range(1, 13):
        direct = sum(comb(n - 1, r - 1) * comb(S - 1, r - 1)
                     for r in range(1, min(n, S) + 1))
        check(direct == comb(n + S - 2, n - 1), f"Vandermonde n={n} S={S}")
        n_vd += 1
print(f"  {n_vd} cells: sum-over-letter-counts equals C(n+S-2, n-1) = C(K-2, n-1) exactly")
# (b) the unfolding: margin(n) = K0 - log2 C(K0-2, n-1) >= n/13, n <= 2000
min_slack, argmin = None, None
for n in range(1, 2001):
    K0 = (3**n).bit_length()
    margin = K0 - log2(comb(K0 - 2, n - 1))
    slack = margin - n / 13
    check(slack > 0, f"margin(n) >= n/13 at n={n}")
    if min_slack is None or slack < min_slack:
        min_slack, argmin = slack, n
print(f"  margin(n) >= n/13 for n = 1..2000; min TRUE-margin slack {min_slack:.3f} bits"
      f" at n = {argmin}")
# his committed "minimum slack 1.700 bits at n = 12" is the slack of the ROUTE-implied
# bound (deficit_term_le => log2 C <= m*log2 19 - k*log2 12 - (m-k)*log2 7, m = K-2,
# k = n-1), i.e. the room the proof route has above n/13 — reproduce it:
rmin, rarg = None, None
for n in range(1, 3001):
    K0 = (3**n).bit_length()
    m, k = K0 - 2, n - 1
    route_logC = m * log2(19) - k * log2(12) - (m - k) * log2(7)
    rslack = (K0 - route_logC) - n / 13
    check(rslack > 0, f"route bound > n/13 at n={n}")
    if rmin is None or rslack < rmin:
        rmin, rarg = rslack, n
print(f"  ROUTE-implied slack: min {rmin:.3f} bits at n = {rarg}"
      f"  (his committed figure: 1.700 at n = 12 — same quantity)")
print(f"  constants: 1/13 = {1/13:.7f} vs c_gen = 0.0793186 "
      f"(proved constant {100*(0.0793186 - 1/13)/0.0793186:.1f}% below the asymptote)")
# domain note: at n = 1 the tuned cell has q = 2^2 - 3 = 1 (spent stock, excluded from
# the L-A7 cell domain |q| > 1); marginTarget includes n = 1 anyway — a harmless superset.
check((2**((3**1).bit_length()) - 3**1) == 1, "n=1 tuned cell is the spent-stock q=1 cell")

print("\n" + "=" * 78)
print("PART B — T1Structure.lean statement canaries")
print("=" * 78)

# ---------------------------------------------------------------- B1 helper lemmas
print("\n[B1] pow_succ_lt_two_mul_pow / mul_pow_succ_le / succ_pow_le_pow_add (exact grids)")
n_b1 = 0
for m in range(1, 121):
    for n in range(0, (m - 1) // 2 + 1):    # 2n < m
        check((m + 1)**n < 2 * m**n, f"pow_succ_lt_two_mul_pow m={m} n={n}")
        n_b1 += 1
for m in range(0, 61):
    for n in range(0, m // 2 + 1):          # 2n <= m
        check(m * (m + 1)**n <= m**(n + 1) + 2 * n * m**n, f"mul_pow_succ_le m={m} n={n}")
        n_b1 += 1
for b in range(0, 41):
    for n in range(0, 41):
        check((b + 1)**(n + 1) <= b**(n + 1) + (n + 1) * (b + 1)**n,
              f"succ_pow_le_pow_add b={b} n={n}")
        n_b1 += 1
print(f"  {n_b1} instances, all hold")
found = None
for m in range(2, 60):
    for n in range((m - 1) // 2 + 1, 3 * m):
        if not ((m + 1)**n < 2 * m**n):
            found = (m, n)
            break
    if found:
        break
check(found is not None, "pow_succ_lt_two_mul_pow fails somewhere with 2n >= m")
print(f"  load-bearing: first failure with 2n >= m at (m,n) = {found}")

# ---------------------------------------------------------------- B2 product identity
print("\n[B2] cycle_prod_identity: rotation algebra + trivial-cycle instance")
# algebraic content: prod_i 2^(v_i) * x_((i+1) mod L) = 2^(sum v) * prod_i x_i
n_b2 = 0
for _ in range(500):
    L = random.randint(1, 8)
    x = [random.randint(0, 50) for _ in range(L)]
    v = [random.randint(0, 10) for _ in range(L)]
    lhs = 1
    for i in range(L):
        lhs *= 2**v[i] * x[(i + 1) % L]
    rhs = 2**sum(v)
    for xi in x:
        rhs *= xi
    check(lhs == rhs, f"rotation product algebra L={L}")
    n_b2 += 1
print(f"  {n_b2} random (x, v): rotation-product law exact (zeros allowed)")
# trivial cycle x = 1, v = 2 on Fin 1: hstep 3*1+1 = 2^2*1; identity 4 = 4; ceiling 4 < 6
check(3 * 1 + 1 == 2**2 * 1, "trivial cycle satisfies hstep")
check(2**2 < 2 * 3**1, "ceiling_upper instance on trivial cycle")
check(2**2 * 3 < 3**1 * 5, "seam_bound instance on trivial cycle")

# ---------------------------------------------------------------- B3 survivor bound
print("\n[B3] survivor_bound: per-factor lemma + product step (exact)")
n_b3 = 0
for x in range(0, 40):
    for X in range(1, 40):
        holds = (3 * x + 1) * (3 * X) <= (3 * x) * (3 * X + 1)
        check(holds == (X <= x), f"per-factor iff x={x} X={X}")
        n_b3 += 1
for _ in range(300):
    L = random.randint(1, 7)
    X = random.randint(1, 30)
    xs = [random.randint(X, X + 40) for _ in range(L)]
    lhs = (3 * X)**L
    rhs = (3 * X + 1)**L
    for xi in xs:
        lhs *= 3 * xi + 1
        rhs *= 3 * xi
    check(lhs <= rhs, f"product step L={L} X={X}")
    n_b3 += 1
print(f"  {n_b3} instances: (3x+1)(3X) <= 3x(3X+1) iff X <= x, and the product form, exact")

# ---------------------------------------------------------------- B4 convergents
print("\n[B4] INDEPENDENT convergent computation for log2(3) (two precisions)")

def cf_of_log23(prec):
    getcontext().prec = prec
    L = Decimal(3).ln() / Decimal(2).ln()
    frac = Fraction(L)          # exact rational equal to the Decimal
    terms = []
    f = frac
    for _ in range(40):
        a = int(f)              # floor for positive f
        terms.append(a)
        f = f - a
        if f == 0:
            break
        f = 1 / f
    return terms

t150 = cf_of_log23(150)
t250 = cf_of_log23(250)
NCF = 30
check(t150[:NCF] == t250[:NCF], "CF terms of log2(3) stable across precisions 150/250")
terms = t250[:NCF]
print(f"  CF terms a_0..a_{NCF-1}: {terms}")

# convergents p_i/q_i
ps, qs = [], []
p0, p1 = 1, terms[0]
q0, q1 = 0, 1
ps.append(p1); qs.append(q1)
for a in terms[1:]:
    p2 = a * p1 + p0
    q2 = a * q1 + q0
    ps.append(p2); qs.append(q2)
    p0, p1, q0, q1 = p1, p2, q1, q2
print(f"  denominators q_0..q_25: {qs[:26]}")

convPairs = [(1,1), (1,2), (2,5), (5,12), (12,41), (41,53), (53,306), (306,665),
             (665,15601), (15601,31867), (31867,79335), (79335,111202),
             (111202,190537), (190537,10590737), (10590737,10781274),
             (10781274,53715833), (53715833,171928773), (171928773,225644606),
             (225644606,397573379), (397573379,6189245291), (6189245291,6586818670),
             (6586818670,65470613321)]

check(len(convPairs) == 22, "convPairs_length = 22")
ours = [(qs[i], qs[i + 1]) for i in range(22)]
check(ours == convPairs, "convPairs = (q_i, q_(i+1)) for i = 0..21, EXACTLY (independent CF)")
for i in range(21):
    check(convPairs[i][1] == convPairs[i + 1][0], f"pair chaining at i={i}")

# the windows
X = 2**71
getcontext().prec = 60
ln2 = Decimal(2).ln()
exact_window = (Decimal(3 * X) * ln2 / 4).sqrt()
int_window = isqrt(2079 * X * 1000 // 4000 // 1000)   # floor sqrt(2079*2^71/4000)
int_window_exact = isqrt(2079 * 2**71 // 4000)
print(f"  exact Legendre window sqrt(3*2^71*ln2/4)      = {float(exact_window):.6e}"
      f"  (file/ledger cite 3.5035e10)")
print(f"  integral window floor sqrt(2079*2^71/4000)     = {int_window_exact:.6e}"
      f"  (file/ledger cite 3.5032e10)")
print(f"  ratio exact/integral = {float(exact_window) / int_window_exact:.6f}"
      f"  (his: within 0.011%)")
# exactly the denominators inside the integral window are the 22 firsts
inside = [q for q in qs if q <= int_window_exact]
check(len(inside) == 22, "exactly 22 convergent denominators inside the integral window")
check(qs[22] > int_window_exact and qs[22] > exact_window,
      "q at index 22 (65470613321) is OUTSIDE both windows")
check(qs[22] == 65470613321, "next denominator = 65470613321 (the file's non-vacuity canary)")
check(qs[23] == 137528045312, "the one after = 137528045312 (Hercher's, in the canary)")

# ---------------------------------------------------------------- B5 discharge_all
print("\n[B5] discharge_all criterion, exact integers")
n_dis = 0
worst_margin, worst_q = None, None
for (q, qn) in convPairs:
    check(2000 * q * (q + qn) <= 2079 * 2**71, f"criterion at q={q}")
    m = (2079 * 2**71) / (2000 * q * (q + qn))
    if worst_margin is None or m < worst_margin:
        worst_margin, worst_q = m, q
    n_dis += 1
print(f"  all {n_dis} pairs pass; tightest integer-form margin {worst_margin:.2f}x at q = {worst_q}"
      f"  (his: 5.17x at 6586818670)")
q22, q23 = 65470613321, 137528045312
check(not (2000 * q22 * (q22 + q23) <= 2079 * 2**71),
      "criterion FAILS at the next convergent (non-vacuity, matches the file's canary)")

# classical bound and true-theta margins at high precision
getcontext().prec = 150
Lhi = Decimal(3).ln() / Decimal(2).ln()
print("  classical bound check + exact-test margins (Decimal, 150 digits):")
exact_worst, exact_worst_q = None, None
for i in range(23):
    q, p = qs[i], ps[i]
    theta = abs(Decimal(q) * Lhi - Decimal(p))
    lo = Decimal(1) / Decimal(q + qs[i + 1])
    hi = Decimal(1) / Decimal(qs[i + 1])
    check(lo < theta < hi, f"classical 1/(q_j+q_j+1) < theta_j < 1/q_j+1 at j={i}")
    if i < 22:
        # seam constraint at n = q_j requires theta_j < q_j * delta; verify it FAILS
        delta = Decimal(2) / (Decimal(3 * X) * ln2)
        ratio = theta / (Decimal(q) * delta)      # exact-test margin (>1 means seam fails)
        check(ratio > 1, f"seam constraint fails at n = q_j = {q}")
        if exact_worst is None or ratio < exact_worst:
            exact_worst, exact_worst_q = ratio, q
print(f"  exact-test tightest margin {float(exact_worst):.2f}x at q = {exact_worst_q}"
      f"  (his: 5.44x)")
print(f"  conservativity: 2079/2000 = {2079/2000:.6f} < 3*ln2/2 = {float(3 * ln2 / 2):.6f}"
      f"  (integer form strictly stronger criterion, from ln 2 > 693/1000)")

# ---------------------------------------------------------------- B6 Legendre
print("\n[B6] LegendreApprox statement canary: Legendre criterion, exhaustive q <= 200")
# |L - p/q| < 1/(2 q^2)  ==>  p/q is a convergent (in lowest terms).
conv_set = set()
for i in range(len(qs)):
    conv_set.add(Fraction(ps[i], qs[i]))
n_leg = 0
hits = 0
for q in range(1, 201):
    # p near q*L
    pc = int(Decimal(q) * Lhi)
    for p in (pc - 1, pc, pc + 1, pc + 2):
        if p <= 0:
            continue
        if abs(Fraction(p, q) - Fraction(Lhi)) < Fraction(1, 2 * q * q):
            hits += 1
            check(Fraction(p, q) in conv_set, f"Legendre: {p}/{q} must be a convergent")
        n_leg += 1
print(f"  {n_leg} rationals scanned near L, {hits} inside the 1/(2q^2) ball —"
      f" every one is a convergent")
# the reduced-denominator subtlety of abs_sub_ge_nat_div: 1/(2k^2) <= 1/(2 den^2)
for (S, k) in [(6, 4), (10, 4), (21, 14), (100, 60)]:
    f = Fraction(S, k)
    check(Fraction(1, 2 * k * k) <= Fraction(1, 2 * f.denominator**2),
          f"nat_div weakening sound at S/k = {S}/{k}")

print("\n" + "=" * 78)
print(f"TOTAL: {PASS} checks passed, {FAIL} failed")
print("=" * 78)
