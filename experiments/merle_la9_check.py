#!/usr/bin/env python3
"""merle_la9_check.py -- independent verification for the L-A9 check
(briefs/merle-la9-check-brief.md; findings in briefs/merle-la9-check-findings.md).

Verifies, in fresh code importing nothing from either Merle repository and
nothing from any earlier check of ours:

  PART 0  canaries (printed first; every external pin stated with its source)
  PART 1  the L-A9 entry's own figures under HIS operational definitions:
          c* = 0.9617 / 0.9622, the deficits (7159.5, 2^38.4, ~37 million),
          k_max(c=6) = 1322 and k_max(c=5.125) = 3693
  PART 2  the clean-room derivation: the sharp Product-Bound chain, the
          convention adjudication (linear-form exponent vs irrationality
          measure), and the required exponent in every convention
  PART 3  the scissors race: raw Crandall 3.49e10 / factor 3.9, ratios 1817
          and 9e19, his alpha = 0.482..0.511 on his own grid; then the second
          regime chosen against the claim (extension to 2^2000, rung-cycle
          slopes, grid-dependence of alpha, and two synthetic negative
          controls: the golden ratio and a Liouville-flavoured constant)
  PART 4  REQ-067: the dps=400 divergence index 385, the corrected 0.00078,
          and the six-number table under the confirmed binning convention
          (classes {1},...,{B-1},{>=B}, dof = B-1)
  PART 5  the 052bis load-bearing rows, reimplemented (not his script):
          the ten rows, the four ledger figures, medians, and an independent
          200-draw control at a different seed

Logs are computed with mpmath at two working precisions with agreement
asserted for every reported figure; every pass/fail that can be an exact
integer comparison is one.
"""

import math
import random
import sys
from fractions import Fraction

from mpmath import mp, mpf, log as mlog, floor as mfloor

CHECKS = 0
FAILS = []


def check(label, ok, detail=""):
    global CHECKS
    CHECKS += 1
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(label)


def log2_frac(num, den=1):
    """log2 of a positive rational, as a float, safely for huge integers."""
    def lg(n):
        b = n.bit_length()
        shift = max(0, b - 900)
        return math.log2(n >> shift) + shift
    return lg(num) - lg(den)


# ---------------------------------------------------------------------------
# continued fraction of log2(3), exact-integer Euclid on a fixed-point value,
# stabilised across two precisions
# ---------------------------------------------------------------------------

def cf_of_log23(digits, nterms):
    """Partial quotients of log2 3 = ln3/ln2 via exact Euclid on the
    fixed-point integers floor(ln3 * 10^d), floor(ln2 * 10^d)."""
    mp.dps = digits + 30
    S = 10 ** digits
    num = int(mfloor(mlog(3) * S))
    den = int(mfloor(mlog(2) * S))
    a = []
    x, y = num, den
    for _ in range(nterms):
        if y == 0:
            break
        q, r = divmod(x, y)
        a.append(q)
        x, y = y, r
    return a


def denoms(a):
    """Convergent denominators, q0 = q1 = 1 both counted (the pinned
    OUT-054/056 convention: q_j from a_0 = 1, a_1 = 1, ...)."""
    qs = []
    qm1, qm2 = 0, 1
    for ai in a:
        q = ai * qm1 + qm2
        qs.append(q)
        qm2, qm1 = qm1, q
    return qs


print("=" * 78)
print("PART 0 -- CANARIES (written against externally recorded numbers)")
print("=" * 78)

A1 = cf_of_log23(3400, 6800)
A2 = cf_of_log23(3800, 7600)
NSTAB = 0
while NSTAB < min(len(A1), len(A2)) and A1[NSTAB] == A2[NSTAB]:
    NSTAB += 1
A = A1[:NSTAB]
Q = denoms(A)

check("stable CF prefix of log2 3 covers >= 2100 terms (two precisions)",
      NSTAB >= 2100, f"{NSTAB} stable terms")
check("first 28 partial quotients match the committed record "
      "(merle_r11_hygiene_check.py)",
      A[:28] == [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1,
                 15, 1, 9, 2, 5, 7, 1, 1])
check("q13 = 190537 (external pin: cycles.md / la8 record)", Q[13] == 190537)
check("q21 = 6586818670, q22 = 65470613321, q23 = 137528045312 "
      "(external pin: la8 record / Lean file)",
      (Q[21], Q[22], Q[23]) == (6586818670, 65470613321, 137528045312))
check("q21 + q22 = 72057431991, Hercher's Table-1 all-m semiconvergent "
      "(external pin: la8 Hercher adjudication)", Q[21] + Q[22] == 72057431991)

# Gauss-Kuzmin closure
gk_head = sum(math.log2(1 + 1 / (k * (k + 2))) for k in range(1, 9))
gk_tail9 = math.log2(10 / 9)  # P(a >= 9) = log2((9+1)/9)
check("Gauss-Kuzmin masses: sum_{k=1..8} P(k) + P(>=9) = 1 exactly",
      abs(gk_head + gk_tail9 - 1) < 1e-12)

# constants used throughout
X0_PAPER = 2 ** 71                    # Barina, J. Supercomputing 81 (2025)
X0_COUNTER = 2075 * 2 ** 60           # the figure the entry calls "exact Barina"
KH = 137500000000                     # Hercher Cor. 29 printed display value
LN2_F = math.log(2)


def kmax_his(c_str, X0):
    """Largest integer k with (k^(c+1) + k)/3 < X0 under HIS chain, by
    integer bisection; the real-power comparison is run at two precisions
    with agreement asserted."""
    results = []
    for dps in (60, 110):
        mp.dps = dps
        c = mpf(c_str)
        lo, hi = 1, 10 ** 60
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if (mpf(mid) ** (c + 1) + mid) / 3 < X0:
                lo = mid
            else:
                hi = mid - 1
        results.append(lo)
    assert results[0] == results[1], f"kmax_his precision-unstable: {results}"
    assert results[0] < 10 ** 60 - 1, "kmax_his bisection ceiling reached"
    return results[0]


k6 = kmax_his('6', X0_PAPER)
k5125 = kmax_his('5.125', X0_PAPER)
check("his written-ahead canaries: k_max(c=6) = 1322, k_max(c=5.125) = 3693",
      (k6, k5125) == (1322, 3693), f"{k6}, {k5125}")

print()
print("=" * 78)
print("PART 1 -- the entry's figures under HIS operational definitions")
print("=" * 78)
print("  chain (his REQ-001):   m <= (k^(c+1) + k)/3   (m = cycle minimum,")
print("  k = odd-element count); closing the window = chain excludes k = K_H")


def cstar(X0):
    vals = []
    for dps in (60, 110):
        mp.dps = dps
        vals.append(float(mlog(3 * X0 - KH) / mlog(KH) - 1))
    assert abs(vals[0] - vals[1]) < 1e-12
    return vals[0]


cs_paper = cstar(X0_PAPER)
cs_counter = cstar(X0_COUNTER)
print(f"  c* (X0 = 2^71)        = {cs_paper:.6f}")
print(f"  c* (X0 = 2075*2^60)   = {cs_counter:.6f}")
check("c* = 0.9617 at X0 = 2^71 (entry's headline figure)",
      round(cs_paper, 4) == 0.9617, f"{cs_paper:.6f}")
check("c* = 0.9622 at X0 = 2075*2^60 (entry's parenthetical)",
      round(cs_counter, 4) == 0.9622, f"{cs_counter:.6f}")

k2 = kmax_his('2', X0_PAPER)
print(f"  k_max(c=2) = {k2}")
check("k_max(c=2) = 1.9205e7 (entry)", round(k2 / 1e7, 4) == 1.9205, f"{k2}")
check("missing factor on k at c=2 is 7159.5 (entry)",
      round(KH / k2, 1) == 7159.5, f"{KH / k2:.2f}")

X0req = (KH ** 3 + KH) // 3
lg_X0req = log2_frac(X0req)
print(f"  X0 required to close at c=2: 2^{lg_X0req:.4f}")
check("X0 required at c=2 is 2^109.4 (entry)", round(lg_X0req, 1) == 109.4,
      f"2^{lg_X0req:.4f}")
check("missing computation factor is 2^38.4 (entry)",
      round(lg_X0req - 71, 1) == 38.4, f"2^{lg_X0req - 71:.4f}")
check("k_max(c=5.125) = 3693, short by ~37 million (entry)",
      k5125 == 3693 and 3.6e7 < KH / k5125 < 3.8e7,
      f"factor {KH / k5125:.4g}")

print()
print("=" * 78)
print("PART 2 -- the clean-room derivation, and the convention adjudication")
print("=" * 78)
print("""  Sharp chain, derived from scratch (findings section 3 writes it out):
    product identity     prod(3x_i + 1) = 2^K prod x_i
    =>  2^K/3^k = prod(1 + 1/(3x_i)) <= exp(k/(3m)),   m = x_min
    =>  eps*ln2 <= k/(3m)  with  eps = K - k*log2(3) = ||k L||  (positive cycle)
    =>  m <= k / (3*ln2*eps).
  Diophantine input, MEASURE convention  |L - p/q| > kappa/q^mu:
    eps > kappa/k^(mu-1)   =>   m < k^mu / (3*kappa*ln2).
  HIS chain (k^(c+1)+k)/3 equals this at mu = c+1, kappa = 1/ln2: his 'c' is
  the LINEAR-FORM exponent (K*ln2 - k*ln3 > k^-c), one below the measure.""")

# the two chains agree at mu = c+1, kappa = 1/ln2 up to the +k term
for cc, kk in (('2', k2), ('5.125', k5125)):
    mu = float(cc) + 1
    sharp = (3 * (1 / LN2_F) * LN2_F * X0_PAPER) ** (1 / mu)  # kappa = 1/ln2
    check(f"his chain at c={cc} = sharp chain at mu={mu}, kappa=1/ln2 "
          "(within the +k term)", abs(sharp / kk - 1) < 1e-4,
          f"sharp {sharp:.6g} vs his {kk}")

lgKH = math.log(KH)


def mu_required(kappa, X0):
    """Measure exponent mu at which the sharp chain's k_max reaches K_H."""
    return math.log(3 * kappa * LN2_F * X0) / lgKH


rows = [("his own constant convention (kappa = 1/ln2 = 1.4427)", 1 / LN2_F),
        ("kappa = 1 (the entry's implicit normalisation)", 1.0),
        ("kappa = 1/sqrt(5) (Hurwitz: best constant ANY irrational admits)",
         1 / math.sqrt(5))]
print("\n  required MEASURE exponent mu* to close the current window "
      "(X0 = 2^71, K_H = 1.375e11):")
for name, kap in rows:
    mu_star = mu_required(kap, X0_PAPER)
    print(f"    {name:62s} mu* = {mu_star:.4f}")
check("required measure exponent mu* < 2 in every constant convention "
      "(the route IS shut -- Dirichlet floor mu >= 2)",
      all(mu_required(kap, X0_PAPER) < 2 for _, kap in rows))
check("his c* + 1 equals mu* at his constant convention (0.9617 -> 1.9617)",
      abs((cs_paper + 1) - mu_required(1 / LN2_F, X0_PAPER)) < 2e-4,
      f"{cs_paper + 1:.4f} vs {mu_required(1 / LN2_F, X0_PAPER):.4f}")
margin = 2 - mu_required(1 / math.sqrt(5), X0_PAPER)
print(f"  Dirichlet margin in the measure convention: 2 - mu* = "
      f"{2 - mu_required(1 / LN2_F, X0_PAPER):.4f} (his kappa) ... "
      f"{margin:.4f} (Hurwitz kappa)")
check("the margin to the Dirichlet floor is ~0.04-0.09 in the exponent, "
      "NOT the ~1.04 the 0.9617-vs-2 pairing suggests",
      0.03 < 2 - mu_required(1 / LN2_F, X0_PAPER) < 0.05
      and 0.07 < margin < 0.10)

# deficits at the true dream (mu = 2), sharp chain
for name, kap in (("kappa = 1", 1.0), ("kappa = 1/sqrt(5), Hurwitz", 1 / math.sqrt(5))):
    kmax2 = math.sqrt(3 * kap * LN2_F * X0_PAPER)
    X0need = KH ** 2 / (3 * kap * LN2_F)
    print(f"    mu = 2, {name:28s}: k_max = {kmax2:.4g}, missing factor "
          f"{KH / kmax2:.3f} on k; X0 needed = 2^{log2_frac(int(X0need)):.2f}"
          f" (missing 2^{log2_frac(int(X0need)) - 71:.2f})")
check("at the TRUE dream (measure mu = 2) the deficit is a factor ~2-3 on k "
      "and ~2^2-2^3.2 of computation -- not 7159.5 / 2^38.4",
      1.5 < KH / math.sqrt(3 * 1.0 * LN2_F * X0_PAPER) < 3.5
      and KH / math.sqrt(3 * LN2_F * X0_PAPER / math.sqrt(5)) < 3.5)

print()
print("=" * 78)
print("PART 3 -- the scissors race: replication, then the second regime")
print("=" * 78)


def kmin_crandall(X0):
    """max_j (3/2) * min(q_j, 2 X0/(q_j + q_{j+1})) as an exact Fraction
    (his REQ-004 operational definition of the Crandall jaw)."""
    best = Fraction(0)
    for j in range(len(Q) - 1):
        s = Q[j] + Q[j + 1]
        v = min(Fraction(Q[j]), Fraction(2 * X0, s))
        if v > best:
            best = v
    return Fraction(3, 2) * best


km71 = kmin_crandall(2 ** 71)
print(f"  raw Crandall k_min(2^71) = {float(km71):.4g}; "
      f"Hercher/k_min = {float(KH / km71):.3f}")
check("raw Crandall at 2^71 = 3.49e10 (entry sanity figure)",
      round(float(km71) / 1e10, 2) == 3.49, f"{float(km71):.5g}")
check("factor below Hercher = 3.9 (entry)",
      round(float(KH / km71), 1) == 3.9, f"{float(KH / km71):.4f}")

HIS_GRID = [71, 100, 150, 200, 300, 400]
kmins = {e: kmin_crandall(2 ** e) for e in HIS_GRID}
r71 = kmins[71] / Fraction(k2)
r400 = kmins[400] / Fraction(kmax_his('2', 2 ** 400))
print(f"  window ratio k_min/k_max(c=2): {float(r71):.4g} at 2^71, "
      f"{float(r400):.4g} at 2^400")
check("ratio 1817 at 2^71 (entry)", round(float(r71)) == 1817,
      f"{float(r71):.2f}")
check("ratio 9e19 at 2^400 (entry)", 8.5e19 < float(r400) < 9.5e19,
      f"{float(r400):.4g}")

slopes_his = []
for i in range(1, len(HIS_GRID)):
    e0, e1 = HIS_GRID[i - 1], HIS_GRID[i]
    num = kmins[e1] / kmins[e0]
    sl = log2_frac(num.numerator, num.denominator) / (e1 - e0)
    slopes_his.append(sl)
print(f"  alpha on HIS grid (5 local slopes): "
      f"{', '.join(f'{s:.3f}' for s in slopes_his)}")
check("alpha on his grid spans 0.482..0.511 (entry: measured range)",
      round(min(slopes_his), 3) == 0.482 and round(max(slopes_his), 3) == 0.511,
      f"[{min(slopes_his):.4f}, {max(slopes_his):.4f}]")
check("his own measured band STRADDLES 1/2 (some local slopes < 0.5)",
      min(slopes_his) < 0.5 < max(slopes_his))

# --- second regime: extend to 2^2000 ---------------------------------------
EXT_GRID = list(range(400, 2001, 50))
kmins_ext = {e: kmin_crandall(2 ** e) for e in EXT_GRID}
slopes_ext = []
for i in range(1, len(EXT_GRID)):
    e0, e1 = EXT_GRID[i - 1], EXT_GRID[i]
    num = kmins_ext[e1] / kmins_ext[e0]
    slopes_ext.append(log2_frac(num.numerator, num.denominator) / (e1 - e0))
chord = kmins_ext[2000] / kmins[71]
chord_a = log2_frac(chord.numerator, chord.denominator) / (2000 - 71)
print(f"  extended regime [2^400, 2^2000], step 50 bits: local alpha in "
      f"[{min(slopes_ext):.3f}, {max(slopes_ext):.3f}]")
print(f"  full chord alpha over [2^71, 2^2000] = {chord_a:.4f}")
check("extended regime: every 50-bit local slope stays above 1/3",
      min(slopes_ext) > 1 / 3, f"min {min(slopes_ext):.4f}")
check("extended regime: local slopes below 1/2 occur there too "
      "(alpha > 1/2 is NOT established by measurement)",
      min(slopes_ext) < 0.5)
check("full chord alpha over [2^71, 2^2000] is ~0.5",
      0.48 < chord_a < 0.52, f"{chord_a:.4f}")

# sliding-window chord slopes at every 1-bit position: the grid-aware form
# of 'alpha', measured at several window widths.  log2(k_min(2^e)) computed
# exactly branch-by-branch (integer comparisons pick the branch).
LOG32 = math.log2(1.5)
lgQ = [log2_frac(q) for q in Q]
lgS = [log2_frac(Q[j] + Q[j + 1]) for j in range(len(Q) - 1)]
km_log = {}
for e in range(71, 2001):
    best = 0.0
    for j in range(len(Q) - 1):
        # plateau branch iff q_j*(q_j+q_{j+1}) <= 2^(e+1), exact in integers
        if Q[j] * (Q[j] + Q[j + 1]) <= 2 ** (e + 1):
            v = lgQ[j]
        else:
            v = (e + 1) - lgS[j]
        if v > best:
            best = v
    km_log[e] = best + LOG32
check("1-bit log-k_min table agrees with the exact Fraction evaluator at "
      "e = 71, 400, 2000",
      all(abs(km_log[e] - log2_frac(kmin_crandall(2 ** e).numerator,
                                    kmin_crandall(2 ** e).denominator)) < 1e-6
          for e in (71, 400, 2000)))

print("  sliding-window chord slopes of log2 k_min, every 1-bit start in "
      "[2^71, 2^2000]:")
width_min = {}
for W in (1, 30, 100, 200, 400):
    slopes = [(km_log[e + W] - km_log[e]) / W
              for e in range(71, 2001 - W)]
    width_min[W] = (min(slopes), max(slopes))
    print(f"    width {W:>4} bits: min {min(slopes):.4f}, max {max(slopes):.4f}"
          f", share below 1/3: "
          f"{sum(1 for s in slopes if s < 1/3)}/{len(slopes)}")
check("at 1-bit resolution the local slope hits both ~0 and ~1 -- "
      "'alpha' is a property of the sampling grid, not of the object",
      width_min[1][0] < 0.05 and width_min[1][1] > 0.95)
check("alpha > 1/3 FAILS on 30-bit windows (deserts around the large "
      "partial quotients)", width_min[30][0] < 1 / 3,
      f"min {width_min[30][0]:.4f}")
check("alpha > 1/3 holds at every 200-bit window over [2^71, 2^2000] -- "
      "the claim is width-dependent, and safe at the widths the entry uses",
      width_min[200][0] > 1 / 3, f"min {width_min[200][0]:.4f}")
check("alpha > 1/2 fails even at 400-bit windows -- the measurement cannot "
      "support 'widens forever at the Dirichlet floor'",
      width_min[400][0] < 1 / 2, f"min {width_min[400][0]:.4f}")

# negative control 1: the golden ratio (the most chain-favourable irrational)
PHI_A = [1] * 400
PHI_Q = denoms(PHI_A)


def kmin_generic(qs, X0):
    best = Fraction(0)
    for j in range(len(qs) - 1):
        s = qs[j] + qs[j + 1]
        v = min(Fraction(qs[j]), Fraction(2 * X0, s))
        if v > best:
            best = v
    return Fraction(3, 2) * best


phi_ratios = []
for e in range(100, 401, 10):
    kmn = kmin_generic(PHI_Q, 2 ** e)
    kmx = math.sqrt(3 * (1 / math.sqrt(5)) * LN2_F * 2 ** e)  # mu=2, Hurwitz
    phi_ratios.append(float(kmn) / kmx)
print(f"  control (phi): k_min/k_max at mu=2, kappa=1/sqrt5 over "
      f"2^100..2^400: min {min(phi_ratios):.3f}, max {max(phi_ratios):.3f}")
check("control (phi): for a badly approximable number at the exact "
      "Dirichlet-Hurwitz floor the window ratio sits in a fixed narrow band "
      "(a photo finish decided by constants) while the entry's c=2 race "
      "grows by 17 orders over the same span -- 'widens forever' is a "
      "property of mu > 2, not of the route",
      max(phi_ratios) / min(phi_ratios) < 1.25
      and all(0.9 < r < 1.6 for r in phi_ratios))

# negative control 2: a Liouville-flavoured constant
LIO_A = [1, 2, 1, 3, 2, 1, 2, 2, 1, 3] * 4
LIO_A = LIO_A[:10] + [10 ** 3] + LIO_A[10:20] + [10 ** 7] + LIO_A[20:30] + [10 ** 14]
LIO_Q = denoms(LIO_A)
lio_sig = []
for j in range(4, len(LIO_Q) - 2):
    Xj = LIO_Q[j] * (LIO_Q[j] + LIO_Q[j + 1])
    Xj1 = LIO_Q[j + 1] * (LIO_Q[j + 1] + LIO_Q[j + 2])
    lio_sig.append(log2_frac(LIO_Q[j + 1], LIO_Q[j])
                   / (log2_frac(Xj1) - log2_frac(Xj)))
print(f"  control (Liouville-flavoured): min rung slope = {min(lio_sig):.4f}")
check("control (Liouville-flavoured): the instrument DOES report alpha < 1/3 "
      "when the quotients explode -- log2 3's alpha > 1/3 is informative, "
      "not built into the formula", min(lio_sig) < 0.2)

print()
print("=" * 78)
print("PART 4 -- REQ-067: the volunteered defect, verified independently")
print("=" * 78)


def cf_float_loop(dps, nterms):
    """HIS procedure (floor/reciprocal loop on an mpf), reimplemented fresh:
    this is deliberately the fragile method, to locate where it breaks."""
    mp.dps = dps
    y = mlog(3) / mlog(2)
    a = []
    for _ in range(nterms):
        ai = int(mfloor(y))
        a.append(ai)
        y = 1 / (y - ai)
    return a


A400 = cf_float_loop(400, 2000)
TRUE2000 = A[:2000]
div_idx = next((i for i in range(2000) if A400[i] != TRUE2000[i]), None)
print(f"  dps=400 float-loop expansion diverges from the true one at index "
      f"{div_idx} (0-based)")
check("divergence index = 385 (his claim), i.e. 1615 of 2000 terms are noise",
      div_idx == 385, f"index {div_idx}, noise {2000 - (div_idx or 0)}")

# his P3 statistic: sum over k=1..8 of (p_obs - p_GK)^2 / p_GK, tail excluded
def p3_stat(seq):
    n = len(seq)
    s = 0.0
    for k in range(1, 9):
        obs = sum(1 for v in seq if v == k) / n
        att = math.log2(1 + 1 / (k * (k + 2)))
        s += (obs - att) ** 2 / att
    return s


p3_true = p3_stat(TRUE2000)
p3_wrong = p3_stat(A400)
print(f"  P3 eight-head-bin statistic: correct sequence {p3_true:.5f}, "
      f"dps=400 sequence {p3_wrong:.5f}")
check("corrected figure 0.00078 on the true sequence",
      round(p3_true, 5) == 0.00078, f"{p3_true:.6f}")
check("the withdrawn 0.00103 reproduces on the dps=400 sequence",
      round(p3_wrong, 5) == 0.00103, f"{p3_wrong:.6f}")


def gk_bins(seq, B):
    """Classes {1},...,{B-1},{>=B}; returns (chi2_stat, dof, per_n, dmax)
    under the confirmed convention dof = B - 1."""
    n = len(seq)
    obs = [sum(1 for v in seq if v == k) for k in range(1, B)]
    obs.append(sum(1 for v in seq if v >= B))
    exp = [n * math.log2(1 + 1 / (k * (k + 2))) for k in range(1, B)]
    exp.append(n * math.log2((B + 1) / B))
    stat = sum((o - e) ** 2 / e for o, e in zip(obs, exp))
    dmax = max(abs(o - e) / n for o, e in zip(obs, exp))
    return stat, len(obs) - 1, stat / n, dmax


# six-number table
s_t, _, pn_t, dm_t = gk_bins(TRUE2000, 10)
s_w, _, pn_w, dm_w = gk_bins(A400, 10)
max_red_t = max(gk_bins(TRUE2000, B)[0] / (B - 1) for B in range(3, 41))
max_red_w = max(gk_bins(A400, B)[0] / (B - 1) for B in range(3, 41))
dmax_t = max(gk_bins(TRUE2000, B)[3] for B in range(3, 41))
dmax_w = max(gk_bins(A400, B)[3] for B in range(3, 41))
print(f"  six-number table (rows: bin dev, chi2/N at B=10, max chi2/dof "
      f"B=3..40):")
print(f"    correct sequence : {dmax_t:.6f}  {pn_t:.6f}  {max_red_t:.4f}")
print(f"    dps=400 sequence : {dmax_w:.6f}  {pn_w:.6f}  {max_red_w:.4f}")
check("largest bin deviation 0.008425 on the correct sequence (his row 1)",
      round(dmax_t, 6) == 0.008425, f"{dmax_t:.6f}")
check("chi2/N = 0.001214 at B=10 on the correct sequence (his row 2)",
      round(pn_t, 6) == 0.001214, f"{pn_t:.6f}")
check("max chi2/dof over ALL B in 3..40 = 0.5666 on the correct sequence "
      "(his row 3 -- the exhaustive form of our printed < 0.567: IT HOLDS)",
      round(max_red_t, 4) == 0.5666 and max_red_t < 0.567, f"{max_red_t:.5f}")
check("wrong-sequence triple 0.004496 / 0.001249 / 1.0504 (his table)",
      round(dm_w, 6) == 0.004496 and round(pn_w, 6) == 0.001249
      and round(max_red_w, 4) == 1.0504,
      f"{dm_w:.6f} / {pn_w:.6f} / {max_red_w:.5f}")
# his convention-sensitivity check
max_dofB_t = max(gk_bins(TRUE2000, B)[0] / B for B in range(3, 41))
max_dofB_w = max(gk_bins(A400, B)[0] / B for B in range(3, 41))
max_dofB2_t = max(gk_bins(TRUE2000, B)[0] / (B - 2) for B in range(3, 41))
check("at dof = B the two maxima become 0.5524 / 1.0204 (his sensitivity note)",
      round(max_dofB_t, 4) == 0.5524 and round(max_dofB_w, 4) == 1.0204,
      f"{max_dofB_t:.5f} / {max_dofB_w:.5f}")
check("at dof = B-2 the correct sequence itself reaches 1.0793 (his note)",
      round(max_dofB2_t, 4) == 1.0793, f"{max_dofB2_t:.5f}")

print()
print("=" * 78)
print("PART 5 -- the 052bis load-bearing rows, reimplemented")
print("=" * 78)

# eps(n) = ceil(nL) - nL < 1e-4, exact fixed-point test at two scales
mp.dps = 140
S1 = 10 ** 90
S2 = 10 ** 120
mp.dps = 140
L_FP1 = int(mfloor(mlog(3) / mlog(2) * S1))
mp.dps = 190
L_FP2 = int(mfloor(mlog(3) / mlog(2) * S2))
hits = []
for n in range(1, 200000):
    f1 = (n * L_FP1) % S1
    f2 = (n * L_FP2) % S2
    t1 = (S1 - f1) * 10 ** 4 < S1
    t2 = (S2 - f2) * 10 ** 4 < S2
    assert t1 == t2, f"precision-unstable eps test at n={n}"
    if t1:
        hits.append(n)

DS_SMALL = sorted({q for q in Q if q <= 200000}, reverse=True)


def greedy(n):
    out, r = [], n
    for d in DS_SMALL:
        if d <= r:
            c = r // d
            out.append((d, c))
            r -= c * d
        if r == 0:
            break
    return out


exp_rows = {n: greedy(n) for n in hits[:10]}
small_d = [min(d for d, _ in exp_rows[n]) for n in hits[:10]]
med = sorted(small_d)[len(small_d) // 2 - 1:len(small_d) // 2 + 1]
med_val = sum(med) / 2
print(f"  first ten eps-small n: {hits[:10]}")
print(f"  smallest-denominator column: {small_d}, median {med_val:g}")
check("the four ledger rows: 14936 = [(665,22),(306,1)], 15601, 31202, 46803",
      hits[:4] == [14936, 15601, 31202, 46803]
      and exp_rows[14936] == [(665, 22), (306, 1)]
      and exp_rows[15601] == [(15601, 1)]
      and exp_rows[31202] == [(15601, 2)]
      and exp_rows[46803] == [(31867, 1), (665, 22), (306, 1)])
check("eps-small smallest-denominator column matches the committed one, "
      "median 15601",
      small_d == [306, 15601, 15601, 306, 15601, 15601, 306, 79335, 306, 15601]
      and med_val == 15601)
check("every eps-small n below 200000 has smallest denominator >= 306",
      all(min(d for d, _ in greedy(n)) >= 306 for n in hits))

# the seed-free version of the control first: the exact census
census_hi = sum(1 for n in range(1, 200000)
                if min(d for d, _ in greedy(n)) >= 306)
rate = census_hi / 199999
print(f"  census over ALL n < 200000: {census_hi} have smallest denominator "
      f">= 306 (rate {rate:.4%}); P(0 in 200 draws) = {(1-rate)**200:.3f}")
rng = random.Random(20260801)  # our own seed, deliberately not his
ctrl = [min(d for d, _ in greedy(rng.randrange(1, 200000))) for _ in range(200)]
ctrl_med = sorted(ctrl)[99:101]
ctrl_med_val = sum(ctrl_med) / 2
print(f"  independent 200-draw control (our seed): median {ctrl_med_val:g}, "
      f"max {max(ctrl)}, reaching 306: {sum(1 for d in ctrl if d >= 306)}/200")
check("the qualitative verdict is robust: typical-n median <= 5 against the "
      "eps-small 15601, and the census rate of >= 306 among all n < 200000 "
      "is ~1-2%", ctrl_med_val <= 5 and 0.001 < rate < 0.03,
      f"median {ctrl_med_val:g}, rate {rate:.4%}")
check("his printed '0/200 reaching 306' is a seed-typical but not "
      "seed-robust summary: P(0 in 200) sits well below certainty at the "
      "census rate", (1 - rate) ** 200 < 0.5,
      f"P = {(1-rate)**200:.3f}, our seed drew "
      f"{sum(1 for d in ctrl if d >= 306)}/200")

print()
print("=" * 78)
print(f"TOTAL: {CHECKS} checks, {len(FAILS)} failures")
for f in FAILS:
    print(f"  FAILED: {f}")
print("=" * 78)
sys.exit(0 if not FAILS else 1)
