"""Verification of the margin inequality  margin(n) >= c_gen * n  at the TRUE constant.

Supports: briefs/margin-inequality-proof-findings.md -- our own, independent proof of the
for-all-n margin inequality that round 9 flagged as an unproved ingredient of ledger entry
L-A7, targeted at the true constant c_gen (not a rational below it) by the entropic route.

Definitions (tuned north cell only):
    beta      = log2 3
    K(n)      = ceil(n*beta) = bitlength(3^n)     (the unique K with 3^n <= 2^K < 2*3^n)
    m = K-2,  k = n-1,  j = m-k = K-n-1,  p = k/m,  theta = K - n*beta  in (0,1)
    margin(n) = K - log2 C(K-2, n-1)
    h(p)      = -p log2 p - (1-p) log2(1-p)
    c_gen     = beta*(1 - h(1/beta)) = beta - beta*log2 beta + (beta-1)*log2(beta-1)
    LAM       = h'(1/beta) = log2(beta-1)          (negative)
    L         = log2(beta/(beta-1)) = log2 beta - LAM     (> 1, because beta < 2)

The proof chain checked here, link by link:
    S2  entropy bound         log2 C(m,k) <= m*h(p)
    S3  concavity/tangent     m*h(p)      <= m*h(1/beta) + LAM*(k - m/beta)
    S4  assembled identity    K - [that tangent] == c_gen*n + (1-L)*theta + 2log2 b - LAM
    S5  uniform surplus       K - m*h(p) - c_gen*n  >  1 + log2 beta          (since theta<1)
    S6  THEOREM A             margin(n) - c_gen*n   >  1 + log2 beta
    S7  Robbins step          log2 C(m,k) <= m*h(p) - (1/2) log2(2 pi k j / m)
    S8  THEOREM B'            margin(n) - c_gen*n   >  (1/2)log2 n + (1/2)log2(3pi/5)
                                                       + 1 + log2 beta       (n >= 2)

This script is written from scratch and imports nothing from any earlier check in this
repository (stdlib + mpmath only).  Every link is checked SEPARATELY over the whole sweep,
so a broken link cannot be masked by slack in another.  Negative controls that must fail
are in Section 3.

Precision protocol.  mp.dps = 80 (>= 265 bits) for the main sweep; mp.dps = 30 for the
200k crude-route cross-check, where the quantities compared differ at 1e-6.  Every binomial
C(K-2, n-1) is an exact Python integer and its base-2 logarithm is enclosed rigorously,
never taken as a float:
    b = C.bit_length();  s = max(0, b - 200);  lo_i = C >> s
    lo_i * 2^s <= C < (lo_i + 1) * 2^s,   lo_i < 2^200 exactly representable at dps 80
    =>  log2(lo_i) + s <= log2 C < log2(lo_i + 1) + s
and when s = 0 the integer itself is exact, so the enclosure collapses to a point (widened
by 1e-70 for safety).  Every inequality is decided with the conservative end of the
enclosure.  The script prints the widest enclosure it used and the smallest slack of every
step; the gap between them is the robustness statement.
"""

import math
import sys
from mpmath import mp, mpf, log, pi

mp.dps = 80
GUARD_BITS = 200
NMAIN = 20000          # exact-binomial sweep
NCRUDE = 200000        # crude-route cross-check sweep (needs no binomials)


def lg(x):
    return log(x) / log(2)


# --------------------------------------------------------------------------------------
# constants
# --------------------------------------------------------------------------------------
BETA = lg(3)


def H(p):
    return -p * lg(p) - (1 - p) * lg(1 - p)


C_GEN_ENTROPY = BETA * (1 - H(1 / BETA))
C_GEN_CLOSED = BETA - BETA * lg(BETA) + (BETA - 1) * lg(BETA - 1)
C_GEN = C_GEN_ENTROPY
LAM = lg(BETA - 1)
LL = lg(BETA) - lg(BETA - 1)
CONST_A = 1 + lg(BETA)                     # proved uniform surplus (Theorem A)
CONST_TH0 = 2 * lg(BETA) - lg(BETA - 1)    # the theta -> 0 end of the surplus interval
CONST_B = lg(3 * pi / 5) / 2 + CONST_A     # proved constant in Theorem B'
H1B = H(1 / BETA)

_fail = []
_widest = mpf(0)


def report(tag, ok, detail=""):
    print(("  [PASS] " if ok else "  [FAIL] ") + tag + ("  " + detail if detail else ""))
    sys.stdout.flush()
    if not ok:
        _fail.append(tag)


def log2_int(C):
    """Rigorous enclosure (lo, hi) with lo <= log2(C) <= hi, C a positive Python int."""
    global _widest
    b = C.bit_length()
    s = max(0, b - GUARD_BITS)
    if s == 0:
        v = lg(mpf(C))
        eps = mpf(10) ** (-70)
        lo, hi = v - eps, v + eps
    else:
        lo = lg(mpf(C >> s)) + s
        hi = lg(mpf((C >> s) + 1)) + s
    if hi - lo > _widest:
        _widest = hi - lo
    return lo, hi


class Track(object):
    def __init__(self, name, want_positive=True):
        self.name = name
        self.want = want_positive
        self.lo = None
        self.lo_at = None
        self.hi = None
        self.hi_at = None
        self.count = 0

    def add(self, v, n):
        self.count += 1
        if self.lo is None or v < self.lo:
            self.lo, self.lo_at = v, n
        if self.hi is None or v > self.hi:
            self.hi, self.hi_at = v, n

    def line(self):
        return "%-56s min %s at n=%-7s (%d values)" % (
            self.name, mp.nstr(self.lo, 10), self.lo_at, self.count)


# ======================================================================================
print("=" * 92)
print("margin_inequality_proof_check.py  --  margin(n) >= c_gen*n at the true constant c_gen")
print("=" * 92)
print("mp.dps = %d, enclosure guard = %d bits, main sweep n = 1..%d, crude sweep n = 2..%d"
      % (mp.dps, GUARD_BITS, NMAIN, NCRUDE))
print()
print("beta                     = %s" % mp.nstr(BETA, 30))
print("c_gen (entropy form)     = %s" % mp.nstr(C_GEN_ENTROPY, 30))
print("c_gen (closed form)      = %s" % mp.nstr(C_GEN_CLOSED, 30))
print("log2 beta                = %s" % mp.nstr(lg(BETA), 30))
print("LAM = log2(beta-1)       = %s" % mp.nstr(LAM, 30))
print("L   = log2(beta/(beta-1))= %s" % mp.nstr(LL, 30))
print("1 - L                    = %s" % mp.nstr(1 - LL, 30))
print("Theorem A surplus  1 + log2 beta         = %s" % mp.nstr(CONST_A, 30))
print("theta->0 end   2 log2 beta - log2(beta-1)= %s" % mp.nstr(CONST_TH0, 30))
print("Theorem B' constant                      = %s" % mp.nstr(CONST_B, 30))
print()
sys.stdout.flush()

# --------------------------------------------------------------------------------------
print("-" * 92)
print("SECTION 0  --  canaries, and the exact-integer facts about beta the proof rests on")
print("-" * 92)

report("c_gen: entropy form == closed form",
       abs(C_GEN_ENTROPY - C_GEN_CLOSED) < mpf(10) ** (-60),
       "|diff| = %s" % mp.nstr(abs(C_GEN_ENTROPY - C_GEN_CLOSED), 5))
GAMMA = 1 - H1B
report("gamma*beta == c_gen   (gamma = 1 - h(1/log2 3), the Junction constant)",
       abs(GAMMA * BETA - C_GEN) < mpf(10) ** (-60),
       "|diff| = %s" % mp.nstr(abs(GAMMA * BETA - C_GEN), 5))
report("h(1/beta) == log2 beta - ((beta-1)/beta)*log2(beta-1)  (the expansion used)",
       abs(H1B - (lg(BETA) - ((BETA - 1) / BETA) * LAM)) < mpf(10) ** (-60))
XSTAR = 1 / (BETA - 1)
report("h'(1/beta) == log2(beta-1) == -log2(x*),  x* = 1/(beta-1)",
       abs(LAM + lg(XSTAR)) < mpf(10) ** (-60),
       "x* = %s  (Merle's rational 12/7 = %s)" % (mp.nstr(XSTAR, 12), mp.nstr(mpf(12) / 7, 12)))
report("beta < 2         <=>  3 < 4                (gives L > 1, i.e. 1 - L < 0)", 3 < 4)
report("beta > 3/2       <=>  3^2 > 2^3            (gives j = K-n-1 >= 1 for n >= 2)",
       3 ** 2 > 2 ** 3)
report("beta > 10/7      <=>  3^7 > 2^10           (gives 7*beta - 10 > 0)", 3 ** 7 > 2 ** 10)
report("beta >= 291/184  <=>  3^184 >= 2^291       (gives q(8) >= 0 in the S8a quadratic)",
       3 ** 184 >= 2 ** 291)
report("  (mirror: the high-precision beta satisfies exactly these four and nothing more is used)",
       BETA < 2 and BETA > mpf(3) / 2 and BETA > mpf(10) / 7 and BETA >= mpf(291) / 184)
report("hand instance n=2:  K=4, C(2,1)=2, margin=3",
       (3 ** 2).bit_length() == 4 and math.comb(2, 1) == 2)
report("hand instance n=8:  K=13, C(11,7)=330",
       (3 ** 8).bit_length() == 13 and math.comb(11, 7) == 330)

p3 = 1
uniq_ok = True
for n in range(1, 401):
    p3 *= 3
    K = p3.bit_length()
    if not (p3 <= 2 ** K < 2 * p3):
        uniq_ok = False
    for Kalt in (K - 1, K + 1):
        if Kalt >= 0 and (p3 <= 2 ** Kalt < 2 * p3):
            uniq_ok = False
report("K = bitlength(3^n) is the UNIQUE K with 3^n <= 2^K < 2*3^n  (n <= 400)", uniq_ok)

vand_ok = True
for n in range(1, 15):
    for S in range(1, 15):
        tot = sum(math.comb(n - 1, r - 1) * math.comb(S - 1, r - 1)
                  for r in range(1, min(n, S) + 1))
        if tot != math.comb(n + S - 2, n - 1):
            vand_ok = False
report("word count  sum_r C(n-1,r-1)C(S-1,r-1) == C(K-2,n-1)  (all n,S <= 14)", vand_ok)
print()
sys.stdout.flush()

# --------------------------------------------------------------------------------------
print("-" * 92)
print("SECTION 1  --  main sweep n = 1..%d; every link of the chain checked separately" % NMAIN)
print("-" * 92)

T = {}
for key, name in [
        ("S1a", "S1a domain:  min(k,j) - 1 >= 0 for n >= 2"),
        ("S1b", "S1b p-window: p - (1/b - 1/(b*m))"),
        ("S1c", "S1c p-window: (1/b + (2-b)/(b*m)) - p"),
        ("S1d", "S1d p identity residual  -|p - 1/b - (2-b-th)/(b*m)|"),
        ("S2",  "S2  entropy bound:  m*h(p) - log2 C(m,k)"),
        ("S3",  "S3  tangent bound:  tangent(m,k) - m*h(p)"),
        ("S4",  "S4  assembled identity residual (tracked as -|res|)"),
        ("S5",  "S5  K - m*h(p) - c_gen*n - (1 + log2 b)"),
        ("S5b", "S5b concavity gap: K - m*h(p) - [c_gen*n+(1-L)th+CONST_TH0]"),
        ("S6",  "S6  THEOREM A: margin - c_gen*n - (1 + log2 b)"),
        ("S7",  "S7  Robbins step: [m*h(p) - credit] - log2 C(m,k)"),
        ("S8a", "S8a k*j/m - 3n/10   (claimed for n >= 8)"),
        ("S8b", "S8b THEOREM B': margin - c_gen*n - (1/2)log2 n - CONST_B"),
        ("S9",  "S9  FINAL as stated: margin(n) - c_gen*n   (n >= 1)"),
        ("S9b", "S9b FINAL over the L-A7 cell domain n >= 2")]:
    T[key] = Track(name)

log_cache = {}      # n -> (lo, hi) enclosure of log2 C(K-2, n-1)
tight = []

p3 = 1
for n in range(1, NMAIN + 1):
    p3 *= 3
    K = p3.bit_length()
    m, k = K - 2, n - 1
    j = m - k
    theta = K - n * BETA

    lo_lc, hi_lc = log2_int(math.comb(m, k))
    log_cache[n] = (lo_lc, hi_lc, K)
    margin_lo = K - hi_lc               # conservative lower bound on margin(n)

    T["S9"].add(margin_lo - C_GEN * n, n)
    T["S6"].add(margin_lo - C_GEN * n - CONST_A, n)
    if n == 1:
        continue                        # degenerate cell m=k=j=0; handled separately
    T["S9b"].add(margin_lo - C_GEN * n, n)
    T["S1a"].add(mpf(min(k, j)) - 1, n)

    p = mpf(k) / m
    T["S1b"].add(p - (1 / BETA - 1 / (BETA * m)), n)
    T["S1c"].add((1 / BETA + (2 - BETA) / (BETA * m)) - p, n)
    T["S1d"].add(-abs(p - 1 / BETA - (2 - BETA - theta) / (BETA * m)), n)

    mh = m * lg(mpf(m)) - k * lg(mpf(k)) - j * lg(mpf(j))
    T["S2"].add(mh - hi_lc, n)

    tangent = m * H1B + LAM * (mpf(k) - mpf(m) / BETA)
    T["S3"].add(tangent - mh, n)

    T["S4"].add(-abs((K - tangent) - (C_GEN * n + (1 - LL) * theta + CONST_TH0)), n)
    T["S5"].add(K - mh - C_GEN * n - CONST_A, n)
    T["S5b"].add(K - mh - (C_GEN * n + (1 - LL) * theta + CONST_TH0), n)

    credit = lg(2 * pi * mpf(k) * j / m) / 2
    T["S7"].add((mh - credit) - hi_lc, n)

    if n >= 8:
        T["S8a"].add(mpf(k) * j / m - mpf(3) * n / 10, n)
    T["S8b"].add(margin_lo - C_GEN * n - lg(mpf(n)) / 2 - CONST_B, n)

    tight.append((margin_lo - C_GEN * n - CONST_A, n))

for key in ["S1a", "S1b", "S1c", "S1d", "S2", "S3", "S4", "S5", "S5b",
            "S7", "S8a", "S8b", "S6", "S9", "S9b"]:
    print("  " + T[key].line())
print()
for key in ["S1a", "S1b", "S1c", "S2", "S3", "S5", "S5b", "S7", "S8a", "S8b",
            "S6", "S9", "S9b"]:
    strict = key not in ("S1a", "S5b")
    ok = (T[key].lo > 0) if strict else (T[key].lo >= 0)
    report("%s holds over the whole sweep" % key, ok,
           "min = %s at n = %s" % (mp.nstr(T[key].lo, 10), T[key].lo_at))
report("S1d p-window identity residual < 1e-60", -T["S1d"].lo < mpf(10) ** (-60),
       "max |res| = %s" % mp.nstr(-T["S1d"].lo, 5))
report("S4 assembled identity residual < 1e-60", -T["S4"].lo < mpf(10) ** (-60),
       "max |res| = %s" % mp.nstr(-T["S4"].lo, 5))
report("S5b concavity gap >= 0 everywhere and decays: max %s at n = %s, min %s at n = %s"
       % (mp.nstr(T["S5b"].hi, 6), T["S5b"].hi_at,
          mp.nstr(T["S5b"].lo, 6), T["S5b"].lo_at),
       T["S5b"].lo >= 0 and T["S5b"].hi_at <= 3)
gap_tail = None
p3 = 1
for n in range(1, NMAIN + 1):
    p3 *= 3
    if n < NMAIN // 2:
        continue
    K = p3.bit_length()
    m, k = K - 2, n - 1
    j = m - k
    mh = m * lg(mpf(m)) - k * lg(mpf(k)) - j * lg(mpf(j))
    g = (K - mh) - (C_GEN * n + (1 - LL) * (K - n * BETA) + CONST_TH0)
    gap_tail = g if gap_tail is None or g > gap_tail else gap_tail
report("S5b concavity gap over the upper half of the sweep is below 1e-4 (O(1/n) decay)",
       gap_tail < mpf(10) ** (-4), "max over n >= %d : %s" % (NMAIN // 2, mp.nstr(gap_tail, 5)))
print()
print("  widest log2 enclosure used over the sweep: %s bits" % mp.nstr(_widest, 5))
smallest = min(T[k].lo for k in ("S1b", "S1c", "S2", "S3", "S5", "S7", "S8a",
                                 "S8b", "S6", "S9", "S9b"))
print("  smallest slack among the decided inequalities: %s bits" % mp.nstr(smallest, 8))
print("  ratio (smallest slack) / (widest enclosure)  : %s" % mp.nstr(smallest / _widest, 6))
print()
sys.stdout.flush()

# --------------------------------------------------------------------------------------
print("-" * 92)
print("SECTION 1b  --  precision robustness: the 50 tightest cases recomputed at dps = 160")
print("-" * 92)
tight.sort()
worst = mpf(0)
for s, n in tight[:50]:
    mp.dps = 160
    lgb = lambda x: log(x) / log(2)
    bb = lgb(3)
    hb = -(1 / bb) * lgb(1 / bb) - (1 - 1 / bb) * lgb(1 - 1 / bb)
    cg = bb * (1 - hb)
    Kb = (3 ** n).bit_length()
    Cb = math.comb(Kb - 2, n - 1)
    sb = max(0, Cb.bit_length() - 400)
    hib = lgb(mpf(Cb)) if sb == 0 else lgb(mpf((Cb >> sb) + 1)) + sb
    sl = (Kb - hib) - cg * n - (1 + lgb(bb))
    mp.dps = 80
    if abs(sl - s) > worst:
        worst = abs(sl - s)
report("dps-80 vs dps-160 Theorem-A slack agreement on the 50 tightest cases",
       worst < mpf(10) ** (-20), "max |diff| = %s" % mp.nstr(worst, 5))
print("  tightest 5 Theorem-A slacks: " +
      ", ".join("n=%d: %s" % (n, mp.nstr(s, 8)) for s, n in tight[:5]))
print()
sys.stdout.flush()

# --------------------------------------------------------------------------------------
print("-" * 92)
print("SECTION 1c  --  the finite closure of Corollary B' at n = 2..7 (part of the PROOF)")
print("-" * 92)
print("   n    K   C(K-2,n-1)      margin(n)        RHS            slack")
allpos = True
for n in range(2, 8):
    K = (3 ** n).bit_length()
    Cb = math.comb(K - 2, n - 1)
    lo_lc, hi_lc = log2_int(Cb)
    Mg = K - hi_lc
    R = C_GEN * n + lg(mpf(n)) / 2 + CONST_B
    print("  %2d  %3d  %10d   %s   %s   %s"
          % (n, K, Cb, mp.nstr(Mg, 10), mp.nstr(R, 10), mp.nstr(Mg - R, 8)))
    if Mg - R <= 0:
        allpos = False
report("Corollary B' finite closure n = 2..7: all six slacks strictly positive", allpos)
print()

print("-" * 92)
print("SECTION 1d  --  THEOREM A' cell scope: all cells n+2 <= K <= n*beta + 4.79982787")
print("-" * 92)
KWIN = (2 * lg(BETA) - LAM) / (LL - 1)
print("  cell window half-width above n*beta: %s" % mp.nstr(KWIN, 12))
NCELL = 600
w_all = None
w_sur = None
boundviol = 0
cells = 0
for n in range(2, NCELL + 1):
    Ktuned = (3 ** n).bit_length()
    Kmax = int(mp.floor(n * BETA + KWIN))
    for K in range(n + 2, Kmax + 1):
        cells += 1
        m, k = K - 2, n - 1
        lo_lc, hi_lc = log2_int(math.comb(m, k))
        Mg = K - hi_lc
        bound = (1 - LL) * K - LAM * n + 2 * lg(BETA) - LAM
        if Mg < bound - mpf(10) ** (-30):
            boundviol += 1
        v = Mg - C_GEN * n
        if w_all is None or v < w_all[0]:
            w_all = (v, n, K)
        if K <= Ktuned:
            u = Mg - C_GEN * n - CONST_A
            if w_sur is None or u < w_sur[0]:
                w_sur = (u, n, K)
report("A' the K-form bound  margin(n,K) >= (1-L)K - LAM*n + 2log2 b - LAM  holds at every cell",
       boundviol == 0, "%d cells checked (n <= %d), %d violations" % (cells, NCELL, boundviol))
report("A' margin(n,K) >= c_gen*n at every cell in the window", w_all[0] > 0,
       "min %s at (n,K) = (%d,%d)" % (mp.nstr(w_all[0], 12), w_all[1], w_all[2]))
report("A' surplus 1+log2 b holds at every cell with K <= ceil(n*beta) (south shore + tuned)",
       w_sur[0] > 0, "min %s at (n,K) = (%d,%d)"
       % (mp.nstr(w_sur[0], 12), w_sur[1], w_sur[2]))
bad = None
for n in range(2, 201):
    K = int(mp.floor(n * BETA + KWIN)) + 3
    bound = (1 - LL) * K - LAM * n + 2 * lg(BETA) - LAM
    if bound - C_GEN * n >= 0:
        bad = n
        break
report("NC-A' just above the window the K-form bound no longer delivers c_gen*n "
       "(so the window edge is real)", bad is None,
       "no n <= 200 where the bound still reaches c_gen*n at K = floor(n*beta+w)+3")
print()

print("-" * 92)
print("SECTION 2  --  cross-checks against the round's published figures")
print("-" * 92)
report("min slack of margin(n) - c_gen*n over 2 <= n <= %d is 2.8414 at n = 2" % NMAIN,
       T["S9b"].lo_at == 2 and abs(T["S9b"].lo - mpf("2.8414")) < mpf("0.0001"),
       "measured %s at n = %s" % (mp.nstr(T["S9b"].lo, 12), T["S9b"].lo_at))
report("n = 1 (spent-stock cell, outside the L-A7 cell domain): margin(1) = 2, slack 1.9207",
       abs((2 - C_GEN) - mpf("1.920681")) < mpf("0.000001"),
       "margin(1) - c_gen = %s" % mp.nstr(2 - C_GEN, 12))

print("  ratio margin(n)/n, approaching c_gen from above (NUMERICAL, not part of the proof):")
for n in (100, 1000, 5000, 20000):
    lo_lc, hi_lc, K = log_cache[n]
    print("      n = %-6d margin/n = %s" % (n, mp.nstr((K - hi_lc) / n, 12)))
print("      c_gen    = %s" % mp.nstr(C_GEN, 12))

mp.dps = 30
BETA30 = lg(3)
C_GEN30 = BETA30 * (1 - H(1 / BETA30))
C_DEC = mpf("0.0793186")
best = {"exact": [None, None], "dec": [None, None]}
p3 = 3
for n in range(2, NCRUDE + 1):
    p3 *= 3
    K = p3.bit_length()
    m, k = K - 2, n - 1
    j = m - k
    base = K - (m * lg(mpf(m)) - k * lg(mpf(k)) - j * lg(mpf(j)))
    for tag, c in (("exact", C_GEN30), ("dec", C_DEC)):
        v = base - c * n
        if best[tag][0] is None or v < best[tag][0][0]:
            best[tag][0] = (v, n)
        if best[tag][1] is None or v > best[tag][1][0]:
            best[tag][1] = (v, n)
print("  crude route (Stirling credit DISCARDED)")
print("    with the EXACT c_gen        : min %s at n = %d ; max %s at n = %d"
      % (mp.nstr(best["exact"][0][0], 10), best["exact"][0][1],
         mp.nstr(best["exact"][1][0], 10), best["exact"][1][1]))
print("    with the 7-digit 0.0793186  : min %s at n = %d ; max %s at n = %d"
      % (mp.nstr(best["dec"][0][0], 10), best["dec"][0][1],
         mp.nstr(best["dec"][1][0], 10), best["dec"][1][1]))
ex_min, ex_min_n = best["exact"][0]
ex_max, ex_max_n = best["exact"][1]
dc_min, dc_min_n = best["dec"][0]
dc_max, dc_max_n = best["dec"][1]
mp.dps = 80
report("ledger crude-route min 1.6647 at n = 16266 reproduced under the DECIMAL constant",
       dc_min_n == 16266 and abs(dc_min - mpf("1.6647")) < mpf("0.0001"))
report("ledger crude-route max 2.10492 at n = 190537 reproduced under the DECIMAL constant",
       dc_max_n == 190537 and abs(dc_max - mpf("2.10492")) < mpf("0.00001"))
report("under the EXACT c_gen the crude-route min sits just above the proved floor 1+log2 b",
       ex_min > CONST_A, "proved floor %s <= measured min %s (at n = %d, excess %s)"
       % (mp.nstr(CONST_A, 12), mp.nstr(ex_min, 12), ex_min_n, mp.nstr(ex_min - CONST_A, 5)))
report("under the EXACT c_gen the crude-route max sits just above the theta->0 end",
       ex_max > CONST_TH0 and ex_max - CONST_TH0 < mpf("0.0001"),
       "theta->0 end %s, measured max %s (concavity gap %s)"
       % (mp.nstr(CONST_TH0, 12), mp.nstr(ex_max, 12), mp.nstr(ex_max - CONST_TH0, 5)))
print()
sys.stdout.flush()

# --------------------------------------------------------------------------------------
print("-" * 92)
print("SECTION 3  --  negative controls (each MUST fail; a pass here means a broken test)")
print("-" * 92)


def first_failure_final(c):
    for n in range(1, NMAIN + 1):
        lo_lc, hi_lc, K = log_cache[n]
        if (K - lo_lc) - c * n < 0:        # generous end: hardest to fail
            return n, (K - lo_lc) - c * n
    return None, None


for c, label in ((C_GEN + mpf("0.001"), "c_gen + 0.001"),
                 (C_GEN + mpf("0.00075"), "c_gen + 0.00075"),
                 (mpf(2) / 25, "2/25 = 0.08  (Merle's own negative control)")):
    n0, v = first_failure_final(c)
    report("NC1 margin(n) >= c*n FAILS for c = %s" % label, n0 is not None,
           "first failure at n = %s, value %s" % (n0, mp.nstr(v, 8) if v is not None else "-"))

n0, v = first_failure_final(C_GEN)
report("NC1b control-of-the-control: at c = c_gen itself there is NO failure", n0 is None)

bad = None
for n in range(1, NMAIN + 1):
    lo_lc, hi_lc, K = log_cache[n]
    if (K - lo_lc) - C_GEN * n - CONST_A - mpf("0.26") < 0:
        bad = n
        break
report("NC2 inflating the Theorem-A surplus by 0.26 FAILS (constant is near-sharp at n=1)",
       bad is not None, "first failure at n = %s" % bad)

bad = None
p3 = 3
for n in range(2, NMAIN + 1):
    p3 *= 3
    K = p3.bit_length()
    m, k = K - 2, n - 1
    j = m - k
    mh = m * lg(mpf(m)) - k * lg(mpf(k)) - j * lg(mpf(j))
    if K - mh - C_GEN * n - CONST_TH0 < 0:
        bad = n
        break
report("NC2b using the theta->0 end CONST_TH0 as if it were uniform FAILS "
       "(so the (1-L)*theta term is load-bearing)", bad is not None,
       "first failure at n = %s" % bad)

print()
for p0 in (mpf("0.55"), mpf("0.60"), mpf("0.65"), 1 / BETA):
    hp0, hpp0 = H(p0), lg((1 - p0) / p0)
    slope = BETA * (1 - hp0 + p0 * hpp0) - hpp0        # d/dn of  K - tangent_{p0}
    if abs(p0 - 1 / BETA) < mpf(10) ** (-30):
        report("NC3 slope at the tangent point p0 = 1/beta EQUALS c_gen exactly",
               abs(slope - C_GEN) < mpf(10) ** (-60),
               "slope - c_gen = %s" % mp.nstr(slope - C_GEN, 5))
    else:
        report("NC3 slope at p0 = %s is STRICTLY BELOW c_gen" % mp.nstr(p0, 6),
               slope < C_GEN, "slope = %s" % mp.nstr(slope, 12))

p0 = mpf("0.60")
hp0, hpp0 = H(p0), lg((1 - p0) / p0)
bad = None
p3 = 3
for n in range(2, NMAIN + 1):
    p3 *= 3
    K = p3.bit_length()
    m, k = K - 2, n - 1
    if (K - (m * hp0 + hpp0 * (mpf(k) - m * p0))) - C_GEN * n < 0:
        bad = n
        break
report("NC3b the p0 = 0.60 tangent bound drifts below c_gen*n inside the sweep",
       bad is not None, "first n = %s" % bad)

bad = None
p3 = 3
for n in range(2, NMAIN + 1):
    p3 *= 3
    K = p3.bit_length()
    m, k = K - 2, n - 1
    j = m - k
    mh = m * lg(mpf(m)) - k * lg(mpf(k)) - j * lg(mpf(j))
    lo_lc, hi_lc, _ = log_cache[n]
    if (mh - lg(2 * pi * mpf(k) * j / m)) - lo_lc < 0:
        bad = n
        break
report("NC4 doubling the Stirling credit BREAKS the Robbins step", bad is not None,
       "first violation at n = %s" % bad)

bad = None
p3 = 3
for n in range(2, NMAIN + 1):
    p3 *= 3
    K = p3.bit_length()
    m = K - 2
    p = mpf(n - 1) / m
    if not (1 / BETA - 1 / (10 * BETA * m) <= p <= 1 / BETA + 1 / (10 * BETA * m)):
        bad = n
        break
report("NC5 a 10x-too-narrow p-window FAILS (S1b/S1c are not vacuous)", bad is not None,
       "first violation at n = %s" % bad)

bad = None
for n in range(8, NMAIN + 1):
    lo_lc, hi_lc, K = log_cache[n]
    m, k = K - 2, n - 1
    j = m - k
    if mpf(k) * j / m - mpf(4) * n / 10 < 0:
        bad = n
        break
report("NC6 the S8a constant 3/10 cannot be raised to 4/10", bad is not None,
       "first violation at n = %s" % bad)
print()

# --------------------------------------------------------------------------------------
print("=" * 92)
if _fail:
    print("RESULT: %d CHECK(S) FAILED:" % len(_fail))
    for f in _fail:
        print("   - " + f)
    sys.exit(1)
print("RESULT: all checks passed.")
print()
print("Verified over n = 1..%d, tuned north cell K = ceil(n log2 3):" % NMAIN)
print("  THEOREM A (elementary; entropy bound + concavity of h; no external input):")
print("      margin(n) > c_gen*n + 1 + log2(log2 3)  =  c_gen*n + %s" % mp.nstr(CONST_A, 12))
print("  THEOREM B' (Robbins' Stirling cited; n >= 2):")
print("      margin(n) > c_gen*n + (1/2)log2 n + %s" % mp.nstr(CONST_B, 12))
print("  THEOREM A' (cell scope; n <= %d, all K in [n+2, n*beta + %s]):" % (NCELL, mp.nstr(KWIN, 10)))
print("      K - log2 C(K-2,n-1) >= c_gen*n   at every such cell (south shore included)")
print("=" * 92)
