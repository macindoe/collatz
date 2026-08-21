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
