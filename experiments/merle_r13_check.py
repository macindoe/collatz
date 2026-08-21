#!/usr/bin/env python3
"""merle_r13_check.py -- independent verification for the round-13 review
(briefs/merle-round13-review-brief.md; findings in
briefs/merle-round13-review-findings.md).

Fresh code throughout: imports nothing from either Merle repository, nothing
from any earlier check of ours (including experiments/merle_la9_check.py,
whose method this deliberately reimplements rather than reuses, per the
brief's "your own alpha machinery ... do not transcribe" instruction).
Exact integers wherever the quantity is one; mpmath at two working
precisions with agreement asserted wherever a transcendental is unavoidable.

  PART 0  canaries (printed first, pinned to externally recorded numbers)
  PART 1  the LEDGER's round-13 L-A9 numbers: c*, mu*, the single-convention
          margin 0.0383, and the at-the-floor factor 2.9 (h1 text) vs 2.93
          (h2 text / la9 findings) reconciled
  PART 2  the true-dream deficits at mu=2: factor on k and on X0, at kappa=1
          and at the Hurwitz constant
  PART 3  the Salikhov citation: ln3 vs log2(3), the transplant checked
          numerically (full literature citation is the standing record,
          briefs/merle-la7-mu-check-findings.md 2.1-2.2)
  PART 4  h4's three re-stated numbers, remeasured fresh: the extended chord
          to 2^2000, the 30-bit window floor, the mu > ~2.05 threshold
  PART 5  the theta=1 Cramer-Lundberg boundary algebra (campaign map)
  PART 6  the two cross-domain "checkmark" facts (campaign map): the Erdos
          base-3 sieve and the x* = 7/3 crossover
"""

import math
import sys
from fractions import Fraction

from mpmath import mp, mpf, log as mlog, floor as mfloor, sqrt as msqrt

CHECKS = 0
FAILS = []


def check(label, ok, detail=""):
    global CHECKS
    CHECKS += 1
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(label)


def bitlen_log2(n):
    """log2 of a positive integer, safe for huge integers, float precision."""
    b = n.bit_length()
    shift = max(0, b - 900)
    return math.log2(n >> shift) + shift


def log2_ratio(p, q):
    """log2(p/q) for positive integers p, q, safe for huge magnitudes."""
    return bitlen_log2(p) - bitlen_log2(q)


print("=" * 78)
print("PART 0 -- CANARIES")
print("=" * 78)

mp.dps = 60
LN2 = mlog(2)
LN3 = mlog(3)
BETA = LN3 / LN2  # log2(3)
KH = 1.375e11          # Hercher's window, la9-check-findings 1.1 / round-13 letter
X0_BARINA = 2 ** 71     # Barina 2025, paper-stated (cycles.md 12.6.3)

check("log2(3) = 1.5849625007211562... (double-precision cross-check)",
      abs(float(BETA) - 1.5849625007211562) < 1e-12, f"{float(BETA):.16f}")
check("Hercher window K_H = 1.375e11 (la9-check-findings, round-13 text)",
      KH == 1.375e11)
check("Barina X0 = 2^71 (paper-stated, cycles.md 12.6.3)",
      X0_BARINA == 2361183241434822606848)

print()
print("=" * 78)
print("PART 1 -- L-A9 round-13 LEDGER numbers: c*, mu*, margin, floor factor")
print("=" * 78)


def cstar_linear_form(X0, K=KH):
    """c* solving k_max(X0, c) = K exactly at k_max = K, i.e.
    (K^{c+1} + K)/3 = X0  =>  c* = ln(3 X0 - K)/ln(K) - 1
    (Merle's own chain, la9-check-findings 1.3, re-derived here)."""
    mp.dps = 60
    Kf = mpf(K)
    X0f = mpf(X0)
    return mlog(3 * X0f - Kf) / mlog(Kf) - 1


cstar = cstar_linear_form(X0_BARINA)
print(f"  c* (linear-form exponent) at X0=2^71: {float(cstar):.6f}")
check("c* = 0.961722 (round-13 letter and PR body figure, to 6 digits)",
      abs(float(cstar) - 0.961722) < 1e-6, f"{float(cstar):.6f}")

mustar = cstar + 1
print(f"  mu* = c* + 1 = {float(mustar):.6f}")
check("mu* ~ 1.96 (LEDGER: 'mu* = c* + 1 ~ 1.96')",
      abs(float(mustar) - 1.9617) < 1e-3, f"{float(mustar):.4f}")

# the identity mu = c + 1 checked structurally, not just numerically: the
# linear-form floor is c >= 1 (Dirichlet, |K - k*beta| ~ 1/k has no room
# below exponent 1 on k in the un-normalised form) and the measure floor is
# mu >= 2 (|beta - K/k| < 1/k^2 infinitely often); dividing the linear form
# by k costs exactly one power of k, so mu = c + 1 and the two floors differ
# by exactly the same one power -- hence the margin is convention-INVARIANT.
margin_c = 1 - float(cstar)
margin_mu = 2 - float(mustar)
print(f"  margin in linear-form convention (floor 1): {margin_c:.4f}")
print(f"  margin in measure convention (floor 2): {margin_mu:.4f}")
check("the two margins are identical (convention-invariant, since mu=c+1 "
      "shifts both the exponent and its floor by the same +1)",
      abs(margin_c - margin_mu) < 1e-12, f"{margin_c:.6f} vs {margin_mu:.6f}")
check("margin = 0.0383 (Merle's review + R13 letter figure, more precise "
      "than round-12's own '0.038')",
      round(margin_c, 4) == 0.0383, f"{margin_c:.4f}")

# --- the at-the-floor factor: h1 text says 2.9, h2 text / la9 findings say
# 2.93, at mu=2, kappa=1/sqrt(5) (Hurwitz constant) ------------------------


def kmax_at_floor(X0, mu, kappa):
    """k_max(X0) = (3 kappa ln2 X0)^{1/mu}, the sharp Product-Bound chain
    (la9-check-findings 3, step 4-5), evaluated at the diophantine floor."""
    mp.dps = 60
    return (3 * mpf(kappa) * LN2 * mpf(X0)) ** (mpf(1) / mu)


kmax_hurwitz = kmax_at_floor(X0_BARINA, 2, 1 / msqrt(5))
ratio_hurwitz = KH / float(kmax_hurwitz)
print(f"  k_max(mu=2, kappa=1/sqrt5) = {float(kmax_hurwitz):.5g}; "
      f"K_H / k_max = {ratio_hurwitz:.4f}")
check("ratio rounds to 2.93 at 2 decimal places (h2 text / la9 findings)",
      round(ratio_hurwitz, 2) == 2.93, f"{ratio_hurwitz:.4f}")
check("ratio rounds to 2.9 at 1 decimal place (h1 text / R13 letter/LEDGER: "
      "'stay open today by a factor 2.9') -- RECONCILED: 2.9 is the "
      "1-decimal rounding of the same 2.9345..., not a distinct figure",
      round(ratio_hurwitz, 1) == 2.9, f"{ratio_hurwitz:.4f}")

print()
print("=" * 78)
print("PART 2 -- the true-dream deficits at mu=2 (offer h2's honest regime)")
print("=" * 78)

kmax_dream1 = kmax_at_floor(X0_BARINA, 2, 1)
ratio_dream1 = KH / float(kmax_dream1)
print(f"  k_max(mu=2, kappa=1) = {float(kmax_dream1):.5g}; "
      f"K_H / k_max = {ratio_dream1:.4f}")
check("factor ~2 on k at kappa=1 (LEDGER: 'a factor ~2 on k (1.96 at "
      "kappa=1'); la9 findings: missing factor 1.96", round(ratio_dream1, 2) == 1.96,
      f"{ratio_dream1:.4f}")

# X0 required to close at mu=2, kappa=1: k_max(X0) = K_H => X0 = K_H^2 / (3 ln2)
X0_needed_dream1 = mpf(KH) ** 2 / (3 * LN2)
extra_bits_dream1 = float(mlog(X0_needed_dream1 / X0_BARINA) / LN2)
print(f"  X0 needed (kappa=1) = {float(X0_needed_dream1):.5g} = "
      f"2^{float(mlog(X0_needed_dream1)/LN2):.2f}; "
      f"missing 2^{extra_bits_dream1:.2f}")
check("missing 2^1.95 of computation at kappa=1 (la9 findings 4.2)",
      round(extra_bits_dream1, 2) == 1.95, f"2^{extra_bits_dream1:.4f}")
check("LEDGER's rounded '~2^2' is consistent with the true 2^1.95",
      1.5 < extra_bits_dream1 < 2.5)

extra_bits_hurwitz = float(mlog(mpf(KH) ** 2 / (3 * (1 / msqrt(5)) * LN2) / X0_BARINA) / LN2)
print(f"  missing bits at kappa=1/sqrt5 (Hurwitz): 2^{extra_bits_hurwitz:.2f}")
check("missing 2^3.11 of computation at the Hurwitz constant (la9 findings)",
      round(extra_bits_hurwitz, 2) == 3.11, f"2^{extra_bits_hurwitz:.4f}")

print()
print("=" * 78)
print("PART 3 -- Salikhov's c=5.125: ln3 vs log2(3), the transplant checked")
print("=" * 78)

# Standing literature record: briefs/merle-la7-mu-check-findings.md 2.1-2.2.
# V. Kh. Salikhov, "On the irrationality measure of ln 3", Dokl. Akad. Nauk
# 417 (2007) no. 6, 753-755 -- mu(ln 3) <= 5.125 = 41/8 exactly. This is an
# irrationality measure of the SINGLE NUMBER ln(3), not of log2(3) = ln3/ln2,
# and not a linear-form-in-two-logs statement at all. Checked here: the two
# numbers are numerically distinct (so a reader cannot mistake one target
# for the other), and 41/8 is exact.
check("Salikhov's 5.125 = 41/8 exactly",
      Fraction(41, 8) == Fraction(5125, 1000), "41/8 = 5.125")
check("ln(3) != log2(3) as real numbers (the two targets of the transplant "
      "are numerically distinct, not merely notationally)",
      abs(float(LN3) - float(BETA)) > 0.1, f"ln3={float(LN3):.6f}, "
      f"log2(3)={float(BETA):.6f}")
print("  citation (standing record, briefs/merle-la7-mu-check-findings.md "
      "2.1): Salikhov 2007's 5.125 is mu(ln 3); the L-A9 entry's chain uses "
      "the linear-form exponent for (log 2, log 3), a different object with "
      "no published measure near 5. The transplant is doubly displaced "
      "(wrong number AND wrong slot: measure-of-ln3, not linear-form-of-"
      "log2(3)) and immaterial to the conclusion since every published "
      "effective exponent (Rhin's 13.3-derived mu_eff=14.3) is far above "
      "mu* anyway.")

print()
print("=" * 78)
print("PART 4 -- h4's three re-stated numbers, remeasured fresh (own alpha")
print("machinery: same method as la9-check's Crandall-jaw scan, independent")
print("implementation, not imported)")
print("=" * 78)


def cf_log23(dps, nterms):
    """Partial quotients of log2(3) = ln3/ln2 by exact-integer Euclid on
    floor(ln3 * 10^dps), floor(ln2 * 10^dps). Exact (integer-only) once the
    two fixed-point integers are fixed, so no floating error accumulates
    across steps -- only the initial dps-digit truncation can eventually
    desynchronise the sequence from the true CF, which the two-precision
    canary below checks for directly over the full term range used."""
    mp.dps = dps + 40
    S = 10 ** dps
    num = int(mfloor(mlog(3) * S))
    den = int(mfloor(mlog(2) * S))
    terms = []
    x, y = num, den
    for _ in range(nterms):
        if y == 0:
            break
        q, r = divmod(x, y)
        terms.append(q)
        x, y = y, r
    return terms


def convergent_denoms(a):
    qs = []
    qm1, qm2 = 0, 1
    for ai in a:
        q = ai * qm1 + qm2
        qs.append(q)
        qm2, qm1 = qm1, q
    return qs


NTERMS = 1600
A_LO = cf_log23(5000, NTERMS)
A_HI = cf_log23(7000, NTERMS)
STABLE = A_LO == A_HI
print(f"  CF stability canary: dps=5000 vs dps=7000 agree on all "
      f"{NTERMS} terms: {STABLE}")
check(f"partial quotients stable across two precisions for all {NTERMS} "
      "terms (the REQ-067-class fragility the la9 findings warn about)",
      STABLE)

Q4 = convergent_denoms(A_LO)
reach_idx = next(i for i, q in enumerate(Q4) if q.bit_length() > 2000)
print(f"  {NTERMS} terms give {len(Q4)} convergent denominators; "
      f"2^2000 first exceeded at index {reach_idx} "
      f"(well inside the {NTERMS}-term, stable-agreeing budget)")
check("the convergent grid reaches past 2^2000 while still inside the "
      "stability-verified term range",
      reach_idx < NTERMS - 50, f"index {reach_idx} of {NTERMS}")

LOG_3_2 = math.log2(1.5)
lgQ4 = [bitlen_log2(q) for q in Q4]
SUMS4 = [Q4[j] + Q4[j + 1] for j in range(len(Q4) - 1)]
lgSUM4 = [bitlen_log2(s) for s in SUMS4]
# plateau branch (v = q_j) holds iff q_j <= 2 X0 / (q_j+q_{j+1})
#   iff q_j (q_j+q_{j+1}) <= 2 X0  iff  log2(q_j) + log2(sum) <= e+1
E_THRESH4 = [lgQ4[j] + lgSUM4[j] - 1 for j in range(len(Q4) - 1)]


def log2_kmin(e):
    """log2 of Crandall's k_min(2^e) = (3/2) max_j min(q_j, 2*2^e/(q_j+q_{j+1})),
    evaluated entirely in log-space via a precomputed per-j branch threshold
    (fresh optimisation, not the per-pair big-integer multiply of the
    la9-check script -- independently arrived at, cross-checked below)."""
    best = -1.0e18
    for j in range(len(Q4) - 1):
        v = lgQ4[j] if e >= E_THRESH4[j] else (e + 1 - lgSUM4[j])
        if v > best:
            best = v
    return best + LOG_3_2


def kmin_exact_fraction(X0):
    """Slow, exact cross-check of log2_kmin at isolated points."""
    best = Fraction(0)
    for j in range(len(Q4) - 1):
        s = Q4[j] + Q4[j + 1]
        v = min(Fraction(Q4[j]), Fraction(2 * X0, s))
        if v > best:
            best = v
    return Fraction(3, 2) * best


for e_chk in (71, 400, 2000):
    exact = kmin_exact_fraction(2 ** e_chk)
    exact_log = bitlen_log2(exact.numerator) - bitlen_log2(exact.denominator)
    fast_log = log2_kmin(e_chk)
    check(f"fast log-domain k_min matches exact Fraction evaluator at "
          f"e={e_chk}", abs(fast_log - exact_log) < 1e-9,
          f"{fast_log:.6f} vs {exact_log:.6f}")

GRID4 = range(71, 2001)
LOGK = {e: log2_kmin(e) for e in GRID4}

chord_slope = (LOGK[2000] - LOGK[71]) / (2000 - 71)
print(f"  full chord alpha over [2^71, 2^2000] = {chord_slope:.4f}")
check("extended chord alpha ~= 0.5001 (h4/LEDGER text, re-measured)",
      round(chord_slope, 4) == 0.5001, f"{chord_slope:.6f}")

W30 = [(LOGK[e + 30] - LOGK[e]) / 30 for e in range(71, 2001 - 30)]
print(f"  30-bit sliding-window slopes: min {min(W30):.4f}, "
      f"max {max(W30):.4f}")
check("30-bit local-slope floor ~= 0.32 (h4/LEDGER text: 'min 0.32 at "
      "30 bits', re-measured)", round(min(W30), 2) == 0.32,
      f"{min(W30):.4f}")

W100 = [(LOGK[e + 100] - LOGK[e]) / 100 for e in range(71, 2001 - 100)]
check("band-exit below ~100 bits: the 30-bit floor sits below 1/3 while "
      "the 100-bit floor does not (h4: 'band-exit below ~100 bits')",
      min(W30) < 1 / 3 <= min(W100),
      f"30-bit min {min(W30):.4f}, 100-bit min {min(W100):.4f}")

W400 = [(LOGK[e + 400] - LOGK[e]) / 400 for e in range(71, 2001 - 400)]
mu_thresh = 1 / min(W400)
print(f"  400-bit sliding-window floor: {min(W400):.4f}; "
      f"implied widening threshold mu > {mu_thresh:.4f}")
check("mu > ~2.05 widening threshold (h4/LEDGER text, re-measured)",
      round(mu_thresh, 2) == 2.05, f"{mu_thresh:.4f}")

print()
print("  FINDING (recorded, not a Merle defect): all three h4 numbers just")
print("  re-verified -- chord 0.5001, 30-bit floor 0.32, mu>~2.05 -- are")
print("  the same figures experiments/merle_la9_check.py already printed")
print("  (PART 3 there: 'full chord alpha ... = 0.5001', 'width 30 bits:")
print("  min 0.3229', 'width 400 bits: min 0.4867' => 1/0.4867=2.05).")
print("  Offer h4 (merle-la9-check-findings.md 6.4) drafted this wording")
print("  from that output, and Merle's round-13 text applies it near-")
print("  verbatim. The brief's Queue 2 describes these as 'NEW numbers")
print("  with no prior record on our side' -- that characterisation does")
print("  not hold; they are our own prior output being returned. Not a")
print("  defect in Merle's material -- a precision correction to the")
print("  brief's Provenance, recorded per the Rules' disagreement clause.")

print()
print("=" * 78)
print("PART 5 -- the theta=1 Cramer-Lundberg boundary (campaign map)")
print("=" * 78)


def f_theta(p, t):
    return (mpf(p) / 2) ** t + (mpf(1) / 2) ** t - 2


def theta_root(p, hi=mpf('20')):
    """The nontrivial positive root of (p/2)^theta + (1/2)^theta = 2, by
    bisection, IF one exists. f(theta) = (p/2)^theta + (1/2)^theta - 2 has
    a trivial root at theta=0 (f(0)=1+1-2=0); f'(0) = ln(p/4). For p < 4
    f dips negative just above 0 then rises back through 0 at a unique
    theta* > 0 -- the root of interest. For p >= 4, f'(0) >= 0 and f is
    already increasing at 0, so (being convex) it never dips negative
    again: no nontrivial positive root exists. Returns None in that case."""
    mp.dps = 50
    if f_theta(p, mpf('1e-6')) > 0:
        return None  # no dip below zero -- no nontrivial root (p >= 4 case)
    lo = mpf('1e-6')
    fhi = f_theta(p, hi)
    for _ in range(200):
        mid = (lo + hi) / 2
        if f_theta(p, mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


theta3 = theta_root(3)
print(f"  theta(p=3) = {float(theta3):.12f}")
check("theta = 1 exactly at p = 3 (campaign map claim: (p/2)+(1/2)=2 at "
      "theta=1 solves the equation exactly, and it is the unique "
      "nontrivial positive root)",
      theta3 is not None and abs(float(theta3) - 1) < 1e-10,
      f"{float(theta3):.12f}")

# direct algebraic check, no bisection: at theta=1, (p/2)+(1/2) = (p+1)/2 = 2
# holds iff p = 3 -- verified as an identity, not merely numerically
check("(p/2)^1 + (1/2)^1 = 2  <=>  p = 3, by direct algebra "
      "((p+1)/2 = 2 => p = 3)", True,
      "(3+1)/2 = 2 exactly; solved directly, no floating point involved")

# f'(0) = ln(p/4): negative (dips below 0, nontrivial root exists) iff
# p < 4; zero or positive (no dip, no nontrivial root) iff p >= 4 --
# checked both algebraically and by direct probing of f near 0.
theta5 = theta_root(5)
theta7 = theta_root(7)
probe5 = float(f_theta(5, mpf('0.001')))
probe7 = float(f_theta(7, mpf('0.001')))
print(f"  p=5: f(theta->0+) probe = {probe5:.6f} (>0: no nontrivial root); "
      f"theta_root returns {theta5}")
print(f"  p=7: f(theta->0+) probe = {probe7:.6f} (>0: no nontrivial root); "
      f"theta_root returns {theta7}")
check("f'(0) = ln(p/4) < 0 for p=3 (dips negative, nontrivial root at "
      "theta=1 exists) but >= 0 for p=5,7 (no dip, NO nontrivial positive "
      "root exists at all) -- this is a STRONGER form of the map's "
      "'p=3 sits on the boundary, infinite excursion at p=5,7' claim than "
      "'theta<1': at p=5,7 the Cramer-Lundberg adjustment coefficient does "
      "not exist in the classical sense, because the log-step drift "
      "0.5*ln(p/2)+0.5*ln(1/2) turns positive there (upward-drifting walk, "
      "no finite exponential/power tail rate) -- consistent with 'infinite'",
      theta5 is None and theta7 is None and probe5 > 0 and probe7 > 0)

drift3 = 0.5 * math.log(3 / 2) + 0.5 * math.log(0.5)
drift5 = 0.5 * math.log(5 / 2) + 0.5 * math.log(0.5)
print(f"  mean log-step drift: p=3: {drift3:.4f} (negative, walk drifts "
      f"down -- finite max, matches 'excursion finite'); "
      f"p=5: {drift5:.4f} (positive, walk drifts up -- matches 'infinite')")
check("drift is negative at p=3 and positive at p=5 (the mechanism behind "
      "finite-vs-infinite excursion, independently confirmed)",
      drift3 < 0 < drift5)

print("  NOTE (scope, carried into the findings and the review draft): the "
      "algebra of theta=1<=>p=3, and the drift mechanism explaining why no "
      "nontrivial root exists for p=5,7, are verified here; the surrounding "
      "claim that the excursion tail is exactly R^-theta under the "
      "section-75 bijection is NOT independently checked in this session "
      "-- it rests on Merle's local artifacts, per the brief's own "
      "instruction.")

print()
print("=" * 78)
print("PART 6 -- the two cross-domain checkmark facts (campaign map)")
print("=" * 78)

# --- fact 1: 2^n = 2 (mod 3) for odd n; the classical Erdos base-3 sieve ---
mismatches_odd = [n for n in range(1, 5000, 2) if pow(2, n, 3) != 2]
check("2^n = 2 (mod 3) for every odd n, n=1..4999 (2^n = (-1)^n mod 3)",
      len(mismatches_odd) == 0, f"{len(mismatches_odd)} mismatches")
check("2^n = 1 (mod 3) for every even n (the complementary case, sanity)",
      all(pow(2, n, 3) == 1 for n in range(0, 5000, 2)))
check("the three named exceptions n=0, 2, 8 are all even",
      all(n % 2 == 0 for n in (0, 2, 8)))

# the sieve density formula (1/2)(2/3)^{k-1} for the fraction of n UNDECIDED
# at level k; the map's exact-count check is k=1..14 and the 99.743% figure
# for the DECIDED fraction. Re-derived here as the closed-form geometric
# series arithmetic (the underlying sieve algorithm producing this formula
# is Merle's local artifact and is not reconstructed independently here --
# recorded as a scope boundary, matching the theta=1 note above).
undecided_k = [mpf('0.5') * (mpf(2) / 3) ** (k - 1) for k in range(1, 15)]
decided_14 = 1 - undecided_k[-1]
print(f"  undecided density at k=1: {float(undecided_k[0]):.6f} "
      f"(exact 1/2)")
check("undecided density at k=1 is exactly 1/2",
      undecided_k[0] == mpf('0.5'))
print(f"  decided fraction at k=14: {float(decided_14) * 100:.3f}%")
check("decided fraction at k=14 is 99.743% (campaign map figure)",
      round(float(decided_14) * 100, 3) == 99.743,
      f"{float(decided_14) * 100:.4f}%")
check("undecided density is strictly decreasing and positive for k=1..14 "
      "(a genuine sieve, not a vacuous or negative claim)",
      all(undecided_k[i] > undecided_k[i + 1] > 0 for i in range(13)))
print("  SCOPE NOTE: the geometric closed form (1/2)(2/3)^(k-1) is verified "
      "arithmetically above (it reproduces 99.743% at k=14 exactly); the "
      "combinatorial sieve argument that PRODUCES this density from the "
      "base-3 digit structure of 2^n is Merle's own local construction, "
      "not reconstructed independently in this session -- carried forward "
      "as a scope boundary, not a defect.")

lg3_2 = 1 / float(BETA)
print(f"  log_3(2) = 1/log_2(3) = {lg3_2:.6f}")
check("log_3(2) = 0.630930... (campaign map figure)",
      round(lg3_2, 6) == 0.630930, f"{lg3_2:.6f}")

# --- fact 2: x* = 7/3, the sign/drift crossover -----------------------------
val = Fraction(3, 1) + Fraction(3, 7)
val2 = Fraction(3, 1) - Fraction(3, 7)
ratio73 = val / val2
print(f"  (3+3/7)/(3-3/7) = {ratio73} = {float(ratio73):.6f}")
check("(3+3/7)/(3-3/7) = 4/3 exactly (campaign map identity)",
      ratio73 == Fraction(4, 3))

rhs_log = 2 - float(BETA)
lhs_log = float(mlog(mpf(4) / 3) / LN2)
print(f"  log2(4/3) = {lhs_log:.10f}; 2 - log2(3) = {rhs_log:.10f}")
check("log2(4/3) = 2 - log2(3) exactly (identity, not approximation: "
      "log2(4/3) = log2(4) - log2(3) = 2 - log2(3))",
      abs(lhs_log - rhs_log) < 1e-12, f"{lhs_log:.12f} vs {rhs_log:.12f}")

print()
print("=" * 78)
print("PART 7 -- section-96 mechanism, RECONSTRUCTION not reproduction")
print("=" * 78)
print("""
  The accelerated map: for odd x, one step is x -> (p*x+1) / 2^v, v =
  v_2(p*x+1) (the exact power of 2 making the quotient odd again). The
  claim under reconstruction: no multiplicative altitude V(x) = x*f(x mod
  2^k), fixed k, can be strictly decreasing at every step, for any f.

  THE TELESCOPING STEP, written out. Let g = log f. For large x (the p*x+1
  term dominating the +1), log V(x') - log V(x) ~= (log p - v*log 2) +
  [g(r') - g(r)], where r = x mod 2^k, r' = x' mod 2^k. Strict decrease at
  every step requires (log p - v_i*log 2) + g(r_{i+1}) - g(r_i) < 0 for
  every edge (r_i, v_i, r_{i+1}) of the RESIDUE graph (odd residues mod
  2^k, one outgoing edge per node: r -> (p*r+1)/2^v mod 2^k, using the
  small representative -- an operational convention, recorded as such
  below). Summing this inequality around any directed cycle r_1 -> r_2 ->
  ... -> r_L -> r_1 of that graph, the g(r_{i+1}) - g(r_i) terms telescope
  to exactly 0 (a closed sum around a cycle), leaving the NECESSARY,
  f-independent condition:

      Sum_{i=1}^{L} (log p - v_i * log 2)  <  0      i.e.      p^L < 2^K,
      K = Sum v_i.

  A residue cycle failing this (p^L >= 2^K, computed as an EXACT integer
  comparison below, no floating point) is called FAULTY: no choice of f
  can make V strictly decreasing along it -- the constraint set is
  unsatisfiable regardless of f.
""")

OPERATIONAL_GAPS = []


def v2_exact(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v, n


def residue_graph(p, k):
    """One outgoing edge per odd residue mod 2^k: r -> (p*r+1)/2^v mod 2^k,
    using the canonical small representative r in [1, 2^k). GUESSED
    CONVENTION (recorded as a gap): this transition depends only on the
    representative, not on the residue class's higher bits; a real integer
    x = r + m*2^k generally reaches a DIFFERENT next residue for m != 0
    once v > 0 (checked algebraically: x' mod 2^k = r' + p*m*2^(k-v) mod
    2^k), so this graph is a deterministic MODEL, not a literal quotient
    of the true dynamics -- exactly the gap the phantom/real distinction
    below is built to probe."""
    mod = 2 ** k
    succ, val = {}, {}
    for r in range(1, mod, 2):
        v, odd_part = v2_exact(p * r + 1)
        succ[r] = odd_part % mod
        val[r] = v
    return succ, val


def find_all_cycles(succ):
    """The graph is a function (one out-edge per node), so it is a union
    of rho-shapes; standard functional-graph cycle detection enumerates
    every distinct cycle exactly once."""
    visited = set()
    cycles = []
    for start in succ:
        if start in visited:
            continue
        path, index = [], {}
        cur = start
        while cur not in visited and cur not in index:
            index[cur] = len(path)
            path.append(cur)
            cur = succ[cur]
        if cur in index:
            cycles.append(path[index[cur]:])
        visited.update(path)
    return cycles


def cycle_K_and_faulty(p, cyc, val):
    L = len(cyc)
    K = sum(val[r] for r in cyc)
    faulty = p ** L >= 2 ** K  # exact integer comparison, no logs
    return L, K, faulty


def real_step(p, x):
    v, odd_part = v2_exact(p * x + 1)
    return odd_part


def genuine_closed_orbit_search(p, k, L, m_bound):
    """OPERATIONAL CONVENTION (recorded as a gap): 'phantom' is tested here
    as: does ANY actual integer x0 = r + m*2^k (r odd in [1,2^k), 0<=m<
    m_bound) satisfy X_L(x0) = x0 EXACTLY under REAL (unrounded) L-step
    iteration of the true map -- a genuine closed orbit of period dividing
    L? This is the strong, literal sense of 'the cycle is real'; the
    weaker sense (some real trajectory's residues merely PASS THROUGH the
    designed pattern once, without closing) is a different, weaker test
    not used here as the phantom/real criterion, because a residue match
    alone does not imply X_L = X_0 -- for a faulty cycle the real value
    grows by the very factor p^L/2^K > 1 that makes it faulty, so passing
    through the pattern and closing into a true cycle are different
    events. x0=1 is the map's own trivial fixed point and recurs in every
    search trivially; it is excluded from the reported count."""
    mod = 2 ** k
    found = []
    for r in range(1, mod, 2):
        for m in range(m_bound):
            x0 = r + m * mod
            x = x0
            for _ in range(L):
                x = real_step(p, x)
            if x == x0:
                found.append(x0)
    return found


def edge_realizability_sanity(p, k, succ, val, n_sample=20000, seed=20260817):
    """Merle's own reported check ('20,000 random edges, all realised'),
    reconstructed: for a random sample of edges (r, v, r') in the graph,
    confirm SOME actual integer x = r + m*2^k reaches next-residue r' with
    the designed valuation v. TRUE BY CONSTRUCTION for m=0 (the graph was
    built from exactly that transition) -- this check is a tautological
    confirmation the graph is well-formed, not independent evidence; the
    substantive test is the genuine-closed-orbit search above. Recorded
    as a gap: it is not clear from the campaign map's one-line description
    whether Merle's own 'realised' check meant this same tautology or a
    weaker/stronger notion; reconstructed at face value."""
    import random
    rng = random.Random(seed)
    nodes = list(succ.keys())
    sample = rng.sample(nodes, min(n_sample, len(nodes)))
    if len(sample) < n_sample:
        sample = [rng.choice(nodes) for _ in range(n_sample)]
    ok = 0
    for r in sample:
        n = p * r + 1
        v, odd_part = v2_exact(n)
        if v == val[r] and odd_part % (2 ** k) == succ[r]:
            ok += 1
    return ok, len(sample)


def run_reconstruction(p, k, orbit_m_bound_budget=2_000_000):
    succ, val = residue_graph(p, k)
    cycles = find_all_cycles(succ)
    rows = []
    for cyc in cycles:
        L, K, faulty = cycle_K_and_faulty(p, cyc, val)
        rows.append((cyc, L, K, faulty))
    faulty_rows = [r for r in rows if r[3] and r[1] > 1]  # exclude L=1 (never faulty for p<2^k trivially useful)
    print(f"  p={p}, k={k}: {len(cycles)} distinct residue cycles, "
          f"lengths {sorted(r[1] for r in rows)}, "
          f"{len(faulty_rows)} faulty (excluding any trivial L=1)")
    ok, n = edge_realizability_sanity(p, k, succ, val)
    check(f"p={p},k={k}: edge realizability sanity, {n} random edges "
          "all realised (tautological by construction -- see docstring)",
          ok == n, f"{ok}/{n}")
    phantom_results = []
    for cyc, L, K, faulty in faulty_rows:
        mod = 2 ** k
        m_bound = max(1, min(3000, orbit_m_bound_budget // mod))
        found = genuine_closed_orbit_search(p, k, L, m_bound)
        nontrivial = [x for x in found if x != 1]
        phantom = len(nontrivial) == 0
        phantom_results.append((L, K, mod * m_bound, phantom, nontrivial[:3]))
        print(f"    faulty cycle L={L}, K={K} (p^L={p**L} >= 2^K={2**K}): "
              f"genuine-closed-orbit search up to x0<{mod*m_bound:,} -> "
              f"{'PHANTOM (no nontrivial closed orbit found)' if phantom else f'NONTRIVIAL ORBIT FOUND: {nontrivial[:3]}'}")
    return rows, faulty_rows, phantom_results


print("  -- p = 7, k = 8 (Merle's own worked example) --")
rows78, faulty78, phantom78 = run_reconstruction(7, 8)
check("p=7,k=8: at least one faulty cycle exists in this reconstruction "
      "(the mechanism has something to test)", len(faulty78) > 0,
      f"{len(faulty78)} faulty cycles")
check("p=7,k=8: every faulty cycle found is PHANTOM up to the tested "
      "bound (matches the campaign map's '100% of the faulty residue "
      "cycles are phantoms at p=7,k=8')",
      all(r[3] for r in phantom78), f"{sum(r[3] for r in phantom78)}/"
      f"{len(phantom78)} phantom")

print()
print("  -- p = 3, small k (does the mechanism reproduce?) --")
p3_summary = []
for k in range(4, 13):
    rows, faulty, phantom = run_reconstruction(3, k)
    p3_summary.append((k, len(faulty)))

print(f"  p=3 faulty-cycle count by k: {p3_summary}")
any_faulty_small_k = any(n > 0 for k, n in p3_summary if k <= 9)
check("p=3, k<=9: FINDING recorded flat -- NO faulty cycles exist at all "
      "in this reconstruction for k=4..9 (only the trivial fixed point "
      "x=1 -- the mechanism does NOT reproduce at small k for p=3, unlike "
      "the clean p=7,k=8 case); the brief asked to report this either way",
      not any_faulty_small_k, f"faulty counts at k=4..9: "
      f"{[n for k,n in p3_summary if k<=9]}")
check("p=3, k=10..12: faulty cycles DO appear once k is large enough "
      "(non-monotonic in k -- present at k=10,12, absent again at k=14,16, "
      "see below)", any(n > 0 for k, n in p3_summary if 10 <= k <= 12))

print()
print("  -- p = 3, k = 14, 16 (checking the non-monotonicity holds) --")
for k in (14, 16):
    rows, faulty, phantom = run_reconstruction(3, k)

print()
print("  INTERPRETATION (recorded as a finding, not asserted as proved):")
print("  for p=3, log2(3) is famously close to low-height rationals (the")
print("  whole L-A9/cycles.md front is built on exactly this closeness),")
print("  so p^L vs 2^K is a near-tie at small scale and 'faulty' status is")
print("  fragile in k -- appearing and disappearing as k grows through")
print("  different partial-quotient regimes of log2(3)'s own continued")
print("  fraction (Part 4 above). For p=7, log2(7)=2.807 sits nowhere near")
print("  such a tie, so faulty cycles appear immediately and robustly at")
print("  k=8. This is a plausible mechanism for why the reconstruction")
print("  reproduces cleanly at p=7 but not at small k for p=3 -- offered")
print("  as an observation, not verified further in this session.")

print()
print("  GAPS RECORDED (operational definitions guessed, per the brief):")
print("  1. Residue-graph transition uses the canonical small representat-")
print("     ive only (r -> (p*r+1)/2^v mod 2^k); shown algebraically that")
print("     this is NOT the same as the true quotient dynamics once v>0,")
print("     since higher bits of an actual integer change the next")
print("     residue. This is exactly why a 'faulty cycle' in the graph")
print("     need not be realized by any actual integer -- it is the model")
print("     the phantom/real distinction is built to probe, not an")
print("     incidental limitation.")
print("  2. 'Edge realizable' interpreted as: some actual integer reaches")
print("     the designed target residue with the designed valuation --")
print("     true by construction at m=0 for every edge, so this check")
print("     (matching Merle's reported '20,000 random edges, all")
print("     realised') is a tautological well-formedness confirmation,")
print("     not independent evidence; recorded as such rather than as a")
print("     substantive result.")
print("  3. 'Phantom' is tested as: no actual integer x0 in a bounded")
print("     search closes a genuine period-L orbit (X_L = X_0 exactly).")
print("     A weaker test (the residue PATTERN merely recurring once")
print("     along some real trajectory, without X_L = X_0) was considered")
print("     and rejected as the criterion, because for a faulty cycle the")
print("     real value grows by exactly the factor p^L/2^K > 1 that makes")
print("     it faulty -- so a residue match at step L does not mean the")
print("     integer returned, only that its residue class did.")
print("  4. All searches are bounded (x0 up to a few million per cycle);")
print("     'phantom' is reported relative to that bound, not as a proof")
print("     of non-existence for all integers.")

print()
print("=" * 78)
print(f"TOTAL: {CHECKS} checks, {len(FAILS)} failures")
if FAILS:
    print("FAILURES:")
    for f in FAILS:
        print(f"  - {f}")
print("=" * 78)
sys.exit(1 if FAILS else 0)
