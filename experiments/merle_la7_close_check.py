#!/usr/bin/env python3
# merle_la7_close_check.py -- round-10 L-A7 closure check (delegated session, 2026-07-26).
#
# Verifies the NUMERICS AND ALGEBRA of Merle's five round-10 L-A7 blocks (shared repo
# github.com/macindoe/one-obstruction-three-faces, commits 9c14824, 203aeb4, fa4acb5,
# 3797ecc, bd16011; HEAD 826970e) against fresh code. Brief:
# briefs/merle-la7-close-check-brief.md. Findings: briefs/merle-la7-close-check-findings.md.
#
# FRESH CODE: imports nothing from either Merle repository and nothing from
# experiments/merle_la7_check.py (the round-9 check). Merle's scripts
# (test_REQ-MATH-035/036/039/040/041/042 in his Lean repo) were read for OPERATIONAL
# DEFINITIONS ONLY and were never run.
#
# PRECISION POLICY (stated per the brief; each pass/fail decision is robust to rounding):
#   - Every q, word count, binomial, and assembly inequality that is *decided* is decided
#     in EXACT INTEGER arithmetic (Python ints / fractions.Fraction) wherever the decision
#     is exact by nature (sections f, g-integer, canaries).
#   - Logs of exact integers use log2i() below: bit-shift to <= 60 bits then math.log2;
#     relative truncation error < 2^-59, total absolute error < 3e-16 per call.
#   - Incremental log-binomial accumulation over <= 2400 steps: accumulated float error
#     < 3e-12 bits. The tightest float-based DECISION in this script (the L1 crossing at
#     n = 372: |f| ~ 5e-2; the route-margin positivity: min 1.66 bits) has margin
#     > 1e10 x the accumulated error. Constants that must match at 4 decimals (C0, slacks)
#     carry float error < 1e-9 << 5e-5.
#   - mpmath (dps stated inline, 40-80) is used for the epsilon scan (min 9.3e-8 decided
#     with ~50 guard digits), the gamma identity (50/80 digits), and the dps-40 slack
#     counts, where float64 would be arguable.
#   - Where a replicated figure is a match/mismatch CALL, the tolerance is printed.
#
# Canaries are printed first and the script aborts if any fails.

import math
from fractions import Fraction as F
from mpmath import mp, mpf, log as mlog, floor as mfloor, ceil as mceil

FAILS = []
def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(name)

def log2i(x):
    """log2 of a positive int; abs error < 3e-16."""
    b = x.bit_length()
    if b > 60:
        sh = b - 60
        return sh + math.log2(x >> sh)
    return math.log2(x)

def K_of(n, pow3=None):
    """Tuned K = bitlength(3^n) = ceil(n log2 3) for n >= 1 (exact)."""
    return (pow3 if pow3 is not None else 3**n).bit_length()

mp.dps = 60
L60 = mlog(3) / mlog(2)                    # log2 3 at 60 digits
CG6 = mpf('0.0793186')                     # the constant as Merle's scripts carry it (6 dp)
CGF = L60 - L60*mlog(L60)/mlog(2) + (L60-1)*mlog(L60-1)/mlog(2)   # full-precision c_gen
def H60(x):
    if x <= 0 or x >= 1: return mpf(0)
    return -x*mlog(x)/mlog(2) - (1-x)*mlog(1-x)/mlog(2)

# ============================================================================
print("=" * 78)
print("CANARIES (all must pass before anything else runs)")
print("=" * 78)
q5 = (1 << 8) - 3**5
q7 = (1 << 12) - 3**7
check("anchor (n=5,K=8) -> q = 13", q5 == 13, f"q={q5}")
check("anchor (n=7,K=12) -> q = 1909", q7 == 1909, f"q={q7}")
check("K_of = ceil(n log2 3) on samples",
      all(K_of(n) == int(mceil(n*L60)) for n in (1,2,3,5,7,12,53,100,1000)))
# margin(2): K=4, #words = C(2,1) = 2, margin = 4 - 1 = 3
m2 = K_of(2) - log2i(math.comb(2, 1))
check("margin(2) = 3 exactly", abs(m2 - 3) < 1e-12, f"{m2:.12f}")
# binomial one-term bound, exact fractions: C(m,k) x^k <= (1+x)^m at x = 12/7
c_bin = all(F(math.comb(m, k)) * F(12,7)**k <= F(19,7)**m
            for (m, k) in [(10,4), (20,8), (30,12), (7,3)])
check("C(m,k)(12/7)^k <= (19/7)^m exact on samples", c_bin)
# Pascal brute force vs math.comb
pas = [[1]]
for i in range(1, 13):
    row = [1] + [pas[-1][j-1] + pas[-1][j] for j in range(1, i)] + [1]
    pas.append(row)
check("Pascal triangle == math.comb, all (m<=12,k)",
      all(pas[m][k] == math.comb(m, k) for m in range(13) for k in range(m+1)))
# epsilon at n=2 (hand value): 2*log2 3 = 3.169925..., eps = ceil - x = 0.830075
e2 = mceil(2*L60) - 2*L60
check("eps_2 = 0.830075 (6 dp)", abs(e2 - mpf('0.830075')) < 5e-7, mp.nstr(e2, 8))
# c_gen closed form vs beta(1 - H(1/beta))
alt = L60 * (1 - H60(1/L60))
check("c_gen closed form == beta(1-H(1/beta)) to 1e-55", abs(CGF - alt) < mpf('1e-55'))
check("c_gen = 0.0793186 (canary vs 6-dp constant)", abs(CGF - CG6) < mpf('2e-8'),
      mp.nstr(CGF, 12))
if FAILS:
    print("\nCANARY FAILURE -- aborting.")
    raise SystemExit(1)
print("CANARIES: all pass\n")

# ============================================================================
print("=" * 78)
print("(a) CROSSINGS -- re-derive per-scale 372 / cumulative 440 (entry constants)")
print("=" * 78)
# Operational definitions (from the round-9 record + REQ-MATH-035, read not run):
#   best north cell R_best(n) = max over S in 1..floor(0.5849625 n)+3, q = 2^(n+S)-3^n > 0,
#   of log2 C(n+S-2, n-1) - log2 q.  Bound f(n) = -c n + p log2 n + C0 with C0 EXHIBITED
#   = max_n [R_best(n) + c n - p log2 n] on n <= NMAX.  L1 = first n past the peak of f
#   with f < 0 (per-scale, "bound < 1 ticket"); L2 = first n with sum_{m>n} 2^f(m) < 1.
NMAX = 4000
Rbest = {}
pow3 = 3
for n in range(2, NMAX + 1):
    pow3 *= 3
    Smax = int(0.5849625 * n) + 3
    # incremental log-binomial: S=1 -> C(n-1, n-1) = 1
    lc = 0.0
    best = None
    for S in range(1, Smax + 1):
        if S > 1:
            lc += math.log2(n + S - 2) - math.log2(S - 1)  # C(n+S-2,n-1) from C(n+S-3,n-1)
        K = n + S
        q = (1 << K) - pow3
        if q <= 0:
            continue
        R = lc - log2i(q)
        if best is None or R > best:
            best = R
    Rbest[n] = best
# spot-check the incremental binomial against exact comb at 3 places
for (nn, SS) in [(5, 3), (100, 20), (1000, 400)]:
    exact = log2i(math.comb(nn + SS - 2, nn - 1))
    lc = 0.0
    for S in range(2, SS + 1):
        lc += math.log2(nn + S - 2) - math.log2(S - 1)
    check(f"incremental log2 C({nn+SS-2},{nn-1}) == exact", abs(lc - exact) < 1e-9,
          f"diff={abs(lc-exact):.2e}")
print(f"  R_best computed on {len(Rbest)} scales, n <= {NMAX}")

def analyse(p, c, label, want_C0=None, want_L1=None, want_L2=None, tail600=None):
    """Replicates the REQ-MATH-035/043 method with our own chain."""
    c = float(c)
    C0 = max(Rbest[n] + c*n - p*math.log2(n) for n in Rbest)
    f = lambda n: -c*n + p*math.log2(n) + C0
    n_pk = p / (c * math.log(2))            # f increases before, decreases after
    L1 = None
    n = max(2, int(n_pk) + 1)
    while n <= NMAX:
        if f(n) < 0:
            L1 = n
            break
        n += 1
    # windowed variant (his 50-window rule) must agree
    L1w = None
    for n in range(2, NMAX + 1):
        if f(n) < 0 and all(f(m) < 0 for m in range(n, min(n + 50, NMAX + 1))):
            L1w = n
            break
    # cumulative: suffix sums of 2^f
    suf = [0.0] * (NMAX + 2)
    for n in range(NMAX, 1, -1):
        fn = f(n)
        suf[n] = suf[n + 1] + (2.0 ** fn if fn > -300 else 0.0)
    L2 = next((n for n in range(2, NMAX + 1) if suf[n + 1] < 1.0), None)
    t600 = suf[601]
    print(f"  {label}: C0 = {C0:.3f}, L1 (per-scale) = {L1}, L2 (cumulative) = {L2}, "
          f"tail(n>600) = {t600:.3e}")
    print(f"    decision margins: f(L1-1) = {f(L1-1):+.4f}, f(L1) = {f(L1):+.4f}; "
          f"suffix(L2) = {suf[L2+1]:.6f}, suffix(L2-1) = {suf[L2]:.6f}  "
          f"(all >> 1e-9 float error)")
    check(f"{label}: monotone L1 == windowed L1", L1 == L1w)
    if want_C0 is not None:
        check(f"{label}: C0 == {want_C0}", abs(C0 - want_C0) < 2e-3, f"{C0:.4f}")
    if want_L1 is not None:
        check(f"{label}: per-scale crossing == {want_L1}", L1 == want_L1)
    if want_L2 is not None:
        check(f"{label}: cumulative crossing == {want_L2}", L2 == want_L2)
    if tail600 is not None:
        check(f"{label}: tail beyond 600 ~ {tail600:.3e}",
              abs(t600 - tail600) < 0.02 * abs(tail600), f"{t600:.3e}")
    return C0, L1, L2, t600

# Entry constants: mu = 5.125 -> p = 4.125, c = c_gen (6 dp, as his scripts carry it)
analyse(4.125, CG6, "entry constants (p=4.125, c_gen)",
        want_C0=-5.774, want_L1=372, want_L2=440)
print("  (claim under check: his re-derivation 'per-scale n = 372, cumulative N = 440,")
print("   reproducing both Macindoe readings exactly' -- and our round-9 372/440.)\n")

# ============================================================================
print("=" * 78)
print("(b) SOUTH FLOOR -- eps + eps' = 1 identically; claimed values; scan to 200,000")
print("=" * 78)
print("  One-line proof: for irrational x, x is not an integer, so ceil(x) = floor(x)+1;")
print("  hence eps + eps' = (ceil(x)-x) + (x-floor(x)) = ceil(x)-floor(x) = 1.  nL is")
print("  irrational for every n >= 1 (L = log2 3 irrational), so eps_n + eps'_n = 1")
print("  identically, min(eps,eps') <= 1/2 <= max(eps,eps'), and both < 1/2 is impossible.")
mp.dps = 60
# claimed spot values
for n, wantN, wantS in [(15601, '2.6e-5', '0.999974'), (190537, None, None)]:
    x = n * L60
    eN = mceil(x) - x
    eS = x - mfloor(x)
    print(f"  n = {n}: eps = {mp.nstr(eN, 6)}, eps' = {mp.nstr(eS, 8)}, "
          f"eps+eps'-1 = {mp.nstr(eN+eS-1, 3)}")
    if n == 15601:
        check("n=15601: eps = 2.6e-5 (2 sf)", abs(eN - mpf('2.6e-5')) < mpf('5e-7'),
              mp.nstr(eN, 4))
        check("n=15601: eps' = 0.999974 (6 dp)", abs(eS - mpf('0.999974')) < mpf('5e-7'))
    else:
        check("n=190537: min(eps,eps') = 9.3e-8 (2 sf)",
              abs(min(eN, eS) - mpf('9.3e-8')) < mpf('5e-9'), mp.nstr(min(eN, eS), 4))
# scan all n <= 200000 (dps 60: error ~1e-53, decisions at 1e-8 scale are safe)
mn, mn_n, mx, mx_n, viol = mpf(1), 0, mpf(0), 0, 0
x = mpf(0)
for n in range(1, 200001):
    x += L60
    fr = x - mfloor(x)          # eps' (south); eps = 1 - fr
    m = min(fr, 1 - fr)
    if m < mn: mn, mn_n = m, n
    if m > mx: mx, mx_n = m, n
    if not (max(fr, 1 - fr) >= mpf('0.5')): viol += 1
# accumulated error of the incremental sum: 200000 additions at dps 60 -> < 1e-53
check("scan n <= 200000: 0 violations of {sum = 1, max >= 1/2}", viol == 0)
check("scan min of min(eps,eps') = 9.3e-8 at n = 190537",
      mn_n == 190537 and abs(mn - mpf('9.3e-8')) < mpf('5e-9'),
      f"min = {mp.nstr(mn, 4)} at n = {mn_n}")
print(f"  scan: min min(eps,eps') = {mp.nstr(mn, 4)} at n = {mn_n}; "
      f"max min(eps,eps') = {mp.nstr(mx, 6)} at n = {mx_n}")
print("  ('at most one shore < 1/2' is the identity itself: the two gaps sum to 1.)\n")

# ============================================================================
print("=" * 78)
print("(c) MARGIN + ENTROPY ROUTE -- min slack 2.8414 at n=2; domination/tightness to 200k")
print("=" * 78)
# (c1) exact margin slack, n <= 3000, exact binomials, mpmath logs (dps 40)
mp.dps = 40
L40 = mlog(3) / mlog(2)
mins, nmin, negs = None, 0, 0
pow3 = 1
for n in range(1, 3001):
    pow3 *= 3
    if n < 2: continue
    K = pow3.bit_length()
    d = math.comb(K - 2, n - 1)
    margin = K - mlog(d) / mlog(2)
    slack = margin - CG6 * n
    if mins is None or slack < mins: mins, nmin = slack, n
    if slack < 0: negs += 1
check("min_n<=3000 [margin - c_gen n] = 2.8414 at n = 2",
      nmin == 2 and abs(mins - mpf('2.8414')) < mpf('5e-5'),
      f"{mp.nstr(mins, 6)} at n = {nmin}")
check("margin - c_gen n >= 0: 0 violations, n <= 3000", negs == 0)
# (c2) entropy route to 200,000 (floats; error bound ~1e-9 bits, decisions at >= 1.66 bits)
def lg2C(m, k):
    return (math.lgamma(m + 1) - math.lgamma(k + 1) - math.lgamma(m - k + 1)) / math.log(2)
def Hf(x):
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x) if 0 < x < 1 else 0.0
cg6f = float(CG6)
# lgamma accuracy canary vs exact comb at n = 100 and n = 3000
for nn in (100, 3000):
    K = K_of(nn); m = K - 2; k = nn - 1
    check(f"lgamma log2C at n={nn} == exact (1e-9)",
          abs(lg2C(m, k) - log2i(math.comb(m, k))) < 1e-9)
stats = {}
minE, minE_n, maxE, maxE_n, negE = None, 0, None, 0, 0
minE3k, minE3k_n = None, 0
pow3 = 1
for n in range(1, 200001):
    pow3 *= 3
    if n < 2: continue
    K = pow3.bit_length()
    m = K - 2; k = n - 1
    ent_slack = (K - m * Hf(k / m)) - cg6f * n         # provable-route slack
    if ent_slack < 0: negE += 1
    if minE is None or ent_slack < minE: minE, minE_n = ent_slack, n
    if maxE is None or ent_slack > maxE: maxE, maxE_n = ent_slack, n
    if n <= 3000 and (minE3k is None or ent_slack < minE3k): minE3k, minE3k_n = ent_slack, n
    if n in (100, 100000):
        true_slack = (K - lg2C(m, k)) - cg6f * n
        stats[n] = (true_slack, ent_slack, true_slack - ent_slack, 0.5 * math.log2(n))
check("entropy route dominates c_gen n at every n <= 200,000 (0 violations)", negE == 0)
check("route minimum = 1.6647 at n = 16266 (4 dp)",
      minE_n == 16266 and abs(minE - 1.6647) < 5e-5, f"{minE:.5f} at n = {minE_n}")
print(f"  route slack over n = 2..200000: min {minE:.5f} at n = {minE_n}, "
      f"max {maxE:.5f} at n = {maxE_n}")
print(f"  (ledger interval [1.66, 2.10]: min matches at 2 dp; max {maxE:.4f} -> "
      f"{'inside' if maxE <= 2.105 else 'OUTSIDE'} the stated interval)")
check("route margin stays in [1.66, 2.10] (his interval, 2 dp rounding)",
      1.655 <= minE and maxE <= 2.105, f"[{minE:.4f}, {maxE:.4f}]")
print(f"  restricted to n <= 3000 (his REQ-036 sweep): min {minE3k:.5f} at n = {minE3k_n}"
      f"  (his printed 1.6647 at n = 1995 -- near-tie with n = 16266, see findings)")
for n in (100, 100000):
    t, e, gap, half = stats[n]
    print(f"  n = {n}: true slack {t:.4f}, route slack {e:.4f}, gap {gap:.4f} "
          f"vs (1/2)log2 n = {half:.4f}")
check("gap at n=100 = 3.92 vs 3.32", abs(stats[100][2] - 3.92) < 5e-3
      and abs(stats[100][3] - 3.32) < 5e-3)
check("gap at n=1e5 = 8.91 vs 8.30", abs(stats[100000][2] - 8.91) < 5e-3
      and abs(stats[100000][3] - 8.30) < 5e-3)
print("  full-precision c_gen instead of the 6-dp constant shifts the 200k-scan minimum by")
print(f"  {16266 * (float(CGF) - cg6f):+.2e} bits -- immaterial to every verdict above.\n")

# ============================================================================
print("=" * 78)
print("(d) THE GAMMA IDENTITY -- gamma log2 3 = c_gen: exact, symbolically")
print("=" * 78)
mp.dps = 80
L80 = mlog(3) / mlog(2)
def H80(x): return -x*mlog(x)/mlog(2) - (1-x)*mlog(1-x)/mlog(2)
gamma = 1 - H80(1 / L80)
cg80 = L80 - L80*mlog(L80)/mlog(2) + (L80-1)*mlog(L80-1)/mlog(2)
d80 = abs(gamma * L80 - cg80)
print(f"  gamma           = {mp.nstr(gamma, 55)}")
print(f"  gamma * log2 3  = {mp.nstr(gamma * L80, 55)}")
print(f"  c_gen           = {mp.nstr(cg80, 55)}")
print(f"  |difference| at 80 digits = {mp.nstr(d80, 3)}")
check("gamma * log2 3 == c_gen at >= 50 digits", d80 < mpf('1e-70'))
# symbolic derivation, each step asserted numerically at 80 digits:
#   H(1/b) = (1/b) log2 b - ((b-1)/b) log2((b-1)/b)
#          = log2 b - ((b-1)/b) log2(b-1)               [split the second log]
#   => b(1 - H(1/b)) = b - b log2 b + (b-1) log2(b-1) = c_gen  (round-8 closed form)
#   gamma = 1 - H(1/b)  =>  gamma * b = c_gen, EXACTLY.
b = L80
s1 = abs(H80(1/b) - ((1/b)*mlog(b)/mlog(2) - ((b-1)/b)*(mlog(b-1)-mlog(b))/mlog(2)))
s2 = abs(H80(1/b) - (mlog(b)/mlog(2) - ((b-1)/b)*mlog(b-1)/mlog(2)))
s3 = abs(b*(1 - H80(1/b)) - cg80)
check("step 1: H(1/b) expansion", s1 < mpf('1e-75'))
check("step 2: log-split form", s2 < mpf('1e-75'))
check("step 3: b(1-H(1/b)) == closed form", s3 < mpf('1e-75'))
print("  VERDICT: an EXACT identity, not a numerical coincidence. gamma = 1 - H(1/beta)")
print("  and c_gen = beta(1 - H(1/beta)) (round-8 (B) derivation), so gamma*beta = c_gen")
print("  by definition once H(1/beta) is expanded -- algebra above, asserted at 80 digits.")
mp.dps = 50
g50 = 1 - (-(1/(mlog(3)/mlog(2)))*mlog(1/(mlog(3)/mlog(2)))/mlog(2)
           - (1-1/(mlog(3)/mlog(2)))*mlog(1-1/(mlog(3)/mlog(2)))/mlog(2))
c50 = (mlog(3)/mlog(2)) - (mlog(3)/mlog(2))*mlog(mlog(3)/mlog(2))/mlog(2) \
      + ((mlog(3)/mlog(2))-1)*mlog((mlog(3)/mlog(2))-1)/mlog(2)
print(f"  at dps = 50 (his REQ-MATH-037 setting): |gamma*L - c_gen| = "
      f"{mp.nstr(abs(g50*(mlog(3)/mlog(2)) - c50), 3)}  (his committed value: 0.0)\n")

# ============================================================================
print("=" * 78)
print("(e) RATIONAL ROUTE CONSTANTS -- x = 12/7 asymptote, x* recovers c_gen")
print("=" * 78)
mp.dps = 50
L50 = mlog(3) / mlog(2)
# Derivation: C(m,k) <= (1+x)^m / x^k (one term of the binomial expansion), so
#   margin = K - log2 C >= K - m log2(1+x) + k log2 x, with m = K-2, k = n-1 and
#   3^n <= 2^K < 2*3^n forcing K/n -> beta. Dividing by n:
#   c(x) = beta - beta log2(1+x) + log2 x.
cx = lambda x: L50 - L50*mlog(1+x)/mlog(2) + mlog(x)/mlog(2)
cg50 = L50 - L50*mlog(L50)/mlog(2) + (L50-1)*mlog(L50-1)/mlog(2)
c127 = cx(mpf(12)/7)
loss = cg50 - c127
print(f"  c(12/7) = {mp.nstr(c127, 10)}   loss vs c_gen = {mp.nstr(loss, 5)}")
check("c(12/7) = 0.0793165 (7 dp)", abs(c127 - mpf('0.0793165')) < mpf('5e-8'))
check("loss = 2.1e-6 (2 sf)", abs(loss - mpf('2.1e-6')) < mpf('5e-8'), mp.nstr(loss, 4))
xstar = 1 / (L50 - 1)
print(f"  x* = 1/(log2 3 - 1) = {mp.nstr(xstar, 10)}")
check("x* = 1.7095 (4 dp)", abs(xstar - mpf('1.7095')) < mpf('5e-5'))
check("c(x*) == c_gen exactly (<= 1e-45)", abs(cx(xstar) - cg50) < mpf('1e-45'),
      mp.nstr(abs(cx(xstar) - cg50), 3))
# optimality: c'(x) = -beta/((1+x) ln 2) + 1/(x ln 2) = 0  <=>  x = 1/(beta-1)
h = mpf('1e-12')
deriv = (cx(xstar + h) - cx(xstar - h)) / (2 * h)
check("c'(x*) = 0 (numeric, |.| < 1e-8)", abs(deriv) < mpf('1e-8'), mp.nstr(deriv, 3))
print("  (symbolic: c'(x) = 1/(x ln2) - beta/((1+x) ln2) = 0 <=> 1 + x = beta x <=>")
print("   x = 1/(beta-1); then 1+x* = beta/(beta-1) and c(x*) = beta - beta log2 beta")
print("   + (beta-1) log2(beta-1) = c_gen -- the same closed form. EXACT recovery.)")
c113 = mpf(1) / 13
print(f"  proved constant 1/13 = {mp.nstr(c113, 8)}; "
      f"c_gen/13ths gap = {mp.nstr((cg50 - c113)/cg50 * 100, 3)} % below c_gen")
check("1/13 = 0.0769231 (7 dp)", abs(c113 - mpf('0.0769231')) < mpf('5e-8'))
check("1/13 is ~3% below c_gen", abs((cg50 - c113)/cg50 - mpf('0.0302')) < mpf('0.001'),
      mp.nstr((cg50-c113)/cg50, 4))
check("c(12/7) > 1/13 (the route's constant clears the proved target)", c127 > c113)
print()

# ============================================================================
print("=" * 78)
print("(f) ASSEMBLY ARITHMETIC -- window, smallest (s,t), atoms, key_core, error-catches")
print("=" * 78)
# Window derivation (operational source: REQ-MATH-041 header + DeficitLemma.lean):
#   scale the 13th-power route by s and absorb 19^(13s) via a power of 2:
#   (A_{s,t})  19^(13s) <= 14^(13s) * 2^t          => t >= 13 s log2(19/14)
#   (a_{s,t})  3^t * 2^s * 7^(13s) <= 12^(13s)     => t log2 3 + s <= 13 s log2(12/7)
#                                                  => t <= s (13 log2(12/7) - 1)/log2 3
#   so t/s must lie in [13 log2(19/14), (13 log2(12/7) - 1)/log2 3].
lo50 = 13 * (mlog(19) - mlog(14)) / mlog(2)
hi50 = (13 * (mlog(12) - mlog(7)) / mlog(2) - 1) / (mlog(3) / mlog(2))
print(f"  window = [{mp.nstr(lo50, 8)}, {mp.nstr(hi50, 8)}], width {mp.nstr(hi50-lo50, 5)}")
check("window = [5.727444, 5.747075] (6 dp)",
      abs(lo50 - mpf('5.727444')) < mpf('5e-7') and abs(hi50 - mpf('5.747075')) < mpf('5e-7'))
check("width = 0.0196 (ledger, 3 sf)", abs((hi50 - lo50) - mpf('0.0196')) < mpf('5e-5'),
      mp.nstr(hi50 - lo50, 5))
# smallest admissible pair: exhaust s = 1..15 in EXACT integers
print("  exhaustive s = 1..15 (exact integers; t_A = min t passing A, t_a = max t passing a):")
found = None
for s in range(1, 16):
    lhsA = 19 ** (13 * s)
    rhsA0 = 14 ** (13 * s)
    tA = 0
    while rhsA0 * (1 << tA) < lhsA:
        tA += 1
    rhs_a = 12 ** (13 * s)
    base_a = (1 << s) * 7 ** (13 * s)
    ta = -1
    t = 0
    while base_a * 3 ** t <= rhs_a:
        ta = t
        t += 1
    admissible = tA <= ta
    print(f"    s = {s:>2}: t_A = {tA:>3}, t_a = {ta:>3}  -> "
          f"{'ADMISSIBLE t in [' + str(tA) + ',' + str(ta) + ']' if admissible else 'empty'}")
    if admissible and found is None:
        found = (s, tA, ta)
check("no admissible t for s = 1..14; s = 15 gives exactly t = 86",
      found == (15, 86, 86), str(found))
# atom margins, exact integers + log2i
mA = log2i(14 ** 195 * 2 ** 86) - log2i(19 ** 195)
ma = log2i(12 ** 195) - log2i(3 ** 86 * 2 ** 15 * 7 ** 195)
check("atom A holds exactly: 19^195 <= 14^195 * 2^86", 19**195 <= 14**195 * 2**86)
check("atom a holds exactly: 3^86 * 2^15 * 7^195 <= 12^195",
      3**86 * 2**15 * 7**195 <= 12**195)
check("atom A margin = 0.088 bits (3 dp)", abs(mA - 0.088) < 5e-4, f"{mA:.4f}")
check("atom a margin = 0.327 bits (3 dp)", abs(ma - 0.327) < 5e-4, f"{ma:.4f}")
check("atom D holds exactly: 2^101 * 3^86 <= 2^562", 2**101 * 3**86 <= 2**562,
      f"margin {562 - log2i(2**101 * 3**86):.1f} bits")
# key_core: exact sweep over admissible (k, j) and hub non-vacuity
#   hub: 2^(k+j+2) <= 2 * 3^(k+1)
#   claim: 2^(86(k+j+2)) * 2^(15(k+1)) * 7^(195k) <= 2^562 * 12^(195k)
#   (derivation: hub^86 gives 2^(86(k+j+2)) <= 2^86 3^(86(k+1)); regroup per-k as
#    [3^86 2^15 7^195]^k * (2^(86+15) 3^86) <= [12^195]^k * 2^562 via atom_a^k + atom_D.)
tested, hub_fail_needed = 0, None
ok_all = True
pw3 = 3   # 3^(k+1) at k = 0
for k in range(0, 61):
    if k > 0:
        pw3 *= 3
    sevk = 7 ** (195 * k)
    twelvek = 12 ** (195 * k)
    j = 0
    while (1 << (k + j + 2)) <= 2 * pw3:
        lhs = (1 << (86 * (k + j + 2))) * (1 << (15 * (k + 1))) * sevk
        rhs = (1 << 562) * twelvek
        if lhs > rhs:
            ok_all = False
            print(f"    key_core FAILS at (k,j) = ({k},{j})")
        tested += 1
        j += 1
    # first j past the hub: does key_core eventually fail without the hypothesis?
    if hub_fail_needed is None:
        jj = j
        while jj < j + 40:
            lhs = (1 << (86 * (k + jj + 2))) * (1 << (15 * (k + 1))) * sevk
            if lhs > (1 << 562) * twelvek:
                hub_fail_needed = (k, jj)
                break
            jj += 1
check(f"key_core exact for ALL hub-admissible (k,j), k <= 60 ({tested} pairs)", ok_all)
check("hub is load-bearing: inequality fails for j past the hub",
      hub_fail_needed is not None, f"first failure found at (k,j) = {hub_fail_needed}")
# error-catch 1: the missing /log2 3 proposes s = 1, t = 6; the exact check refutes it
hi_bad = 13 * (mlog(12) - mlog(7)) / mlog(2) - 1
print(f"  uncorrected upper bound (no /log2 3) = {mp.nstr(hi_bad, 6)} -> window "
      f"[{mp.nstr(lo50, 6)}, {mp.nstr(hi_bad, 6)}] admits s = 1, t = 6")
A16 = 19 ** 13 <= 14 ** 13 * 2 ** 6
a16 = 3 ** 6 * 2 * 7 ** 13 <= 12 ** 13
check("error-catch 1: s=1,t=6 passes A but FAILS a (refuted exactly)",
      A16 and not a16,
      f"a-side: {3**6 * 2 * 7**13} > {12**13}")
# error-catch 2: 3^86 <= 4^86 = 2^172, trivially true and sufficient for atom_D
check("error-catch 2: 3^86 <= 4^86 = 2^172 exact", 3**86 <= 4**86 == 2**172)
check("... and sufficient where used (atom_D): 101 + 172 = 273 <= 562",
      2**101 * 2**172 <= 2**562)
print()

# ============================================================================
print("=" * 78)
print("(g) PROVED-CONSTANT CLAIMS -- n/13 slack, integer target, negative control")
print("=" * 78)
mp.dps = 40
l12_7 = mlog(mpf(12)/7) / mlog(2)
l19_7 = mlog(mpf(19)/7) / mlog(2)
# (g1) provable route bound mb(n) = K - m log2(19/7) + k log2(12/7) >= n/13, n = 1..3000
worst, nworst, failsg = None, 0, 0
worstT, nworstT = None, 0
pow3 = 1
for n in range(1, 3001):
    pow3 *= 3
    K = pow3.bit_length()
    m = K - 2; k = n - 1
    if m < 0 or k < 0 or k > m: continue
    mb = K - m * l19_7 + k * l12_7
    sl = mb - mpf(n) / 13
    if worst is None or sl < worst: worst, nworst = sl, n
    if sl < 0: failsg += 1
    tm = (K - mlog(math.comb(m, k)) / mlog(2)) - mpf(n) / 13
    if worstT is None or tm < worstT: worstT, nworstT = tm, n
check("route bound >= n/13, n = 1..3000: 0 failures", failsg == 0)
check("min slack = 1.700 at n = 12 (route bound, his P3)",
      nworst == 12 and abs(worst - mpf('1.7003')) < mpf('5e-4'),
      f"{mp.nstr(worst, 6)} at n = {nworst}")
print(f"  true margin - n/13: min = {mp.nstr(worstT, 6)} at n = {nworstT} "
      f"(the route bound is the binding one; margin(n) >= n/13 holds a fortiori)")
# (g2) integer target n = 1..1200 + route implication, exact integers
badA, minA = [], None
badB, minB = [], None
pow3 = 1
for n in range(1, 1201):
    pow3 *= 3
    K = pow3.bit_length()
    m = K - 2; k = n - 1
    if m < 0 or k < 0 or k > m: continue
    C = math.comb(m, k)
    lhsA = C ** 13 * (1 << n); rhsA = 1 << (13 * K)
    if lhsA > rhsA: badA.append(n)
    dA = rhsA.bit_length() - lhsA.bit_length()
    if minA is None or dA < minA[0]: minA = (dA, n)
    lhsB = (19 ** m * 7 ** k) ** 13 * (1 << n)
    rhsB = (1 << (13 * K)) * (7 ** m * 12 ** k) ** 13
    if lhsB > rhsB: badB.append(n)
    dB = rhsB.bit_length() - lhsB.bit_length()
    if minB is None or dB < minB[0]: minB = (dB, n)
check("integer target C(K-2,n-1)^13 2^n <= 2^(13K), n = 1..1200: 0 failures",
      len(badA) == 0, f"min bit-margin {minA}")
check("binomial route implies it, n = 1..1200: 0 failures, >= 22 bits spare",
      len(badB) == 0 and minB[0] >= 22, f"min bit-margin {minB}")
# (g3) negative control: c = 2/25 with his best rational x = 1709/1000 (his P3bis range
#      n = 1..3000); also x = 12/7 for the record
for xnum, xden in [(1709, 1000), (12, 7)]:
    lx = mlog(mpf(xnum)/xden) / mlog(2)
    l1x = mlog(1 + mpf(xnum)/xden) / mlog(2)
    failsN, worstN, nworstN = [], None, 0
    pow3 = 1
    for n in range(1, 3001):
        pow3 *= 3
        K = pow3.bit_length()
        m = K - 2; k = n - 1
        if m < 0 or k < 0 or k > m: continue
        sl = (K - m * l1x + k * lx) - mpf(2) * n / 25
        if sl < 0: failsN.append(n)
        if worstN is None or sl < worstN: worstN, nworstN = sl, n
    print(f"  negative control c = 2/25, x = {xnum}/{xden}: {len(failsN)} failures, "
          f"min slack {mp.nstr(worstN, 5)} at n = {nworstN}, first {failsN[:8]}")
    if (xnum, xden) == (1709, 1000):
        check("c = 2/25 fails at exactly 241 scales (x = 1709/1000, n = 1..3000)",
              len(failsN) == 241 and failsN[:8] == [2460, 2472, 2484, 2496, 2508, 2513,
                                                     2520, 2525])
print()

# ============================================================================
print("=" * 78)
print("(h) THRESHOLDS -- 1596/1655 per-scale, 1661/1722 cumulative (Rhin 13.3)")
print("=" * 78)
# His REQ-MATH-035/043 method: same R_best (n <= 4000), exponent p = 13.3 on log2 n,
# C0 EXHIBITED per constant, L1/L2 as in (a).
analyse(13.3, CG6, "Rhin x c_gen", want_C0=-14.949, want_L1=1596, want_L2=1661,
        tail600=3.863e19)
analyse(13.3, F(1, 13), "Rhin x 1/13 (proved)", want_C0=-14.954, want_L1=1655,
        want_L2=1722, tail600=1.096e20)
# Reconciliation with our round-9 headline "tail < 5.2e-4 beyond n ~ 2233":
#   different quantities. The four figures above use (i) C0 EXHIBITED from the data
#   (an empirical fit, max of the residual over n <= 4000), (ii) exponent 13.3 on
#   log2 n, (iii) target "< 1 ticket" (per-scale, or cumulative < 1). Our 2233 uses
#   (i) the THEOREM-FORM constant C0 = 1 - 2 log2 ln 2 = 2.06 plus 3 repair bits,
#   (ii) 13.3 on log2 K0 (per-n Rhin form, K0 = bitlength(3^n)), (iii) target
#   "provable BOTH-SHORE TAIL MASS < 5.2e-4" (the entry's headline number).
mp.dps = 40
C0_thm = 1 - 2 * mlog(mlog(2)) / mlog(2)
check("theorem-form C0 = 2.06 (2 dp)", abs(C0_thm - mpf('2.06')) < mpf('5e-3'),
      mp.nstr(C0_thm, 4))
bnd = lambda n, K: -cg6f * n + 13.3 * math.log2(K) + float(C0_thm) + 3.0
vals = []
pow3 = 1
for n in range(1, 6001):
    pow3 *= 3
    vals.append((n, bnd(n, pow3.bit_length())))
suf = 0.0
tails = {}
for n, v in reversed(vals):
    suf += 2.0 ** v if v > -300 else 0.0
    tails[n] = suf   # tail strictly beyond n-1... store sum_{m >= n}
minN = next(N for N in range(2, 6000) if tails.get(N + 1, 0.0) < 5.2e-4)
check("our round-9 headline reproduced: min N with provable tail < 5.2e-4 is 2233",
      minN == 2233, f"minN = {minN}")
print("  RECONCILIATION: 1596/1655/1661/1722 are ONE-TICKET crossings of the per-scale")
print("  best-cell bound with an EXHIBITED (fitted) C0 and exponent 13.3 on log2 n;")
print("  2233 is the smallest N with the THEOREM-FORM bound (C0 = 2.06 + 3 repair bits,")
print("  13.3 on log2 K0) giving provable both-shore tail mass < 5.2e-4. Different")
print("  constants, different exponent carrier, different target -- no contradiction.\n")

# ============================================================================
print("=" * 78)
print(f"SUMMARY: {len(FAILS)} failed checks" + ("" if not FAILS else " -- " + "; ".join(FAILS)))
print("=" * 78)
