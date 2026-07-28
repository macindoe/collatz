"""Gate P1: the two-sided arc, and an unconditional upper bound on `gamma`.

Supports `briefs/staircase-gamma-upper-findings.md`.

WHAT THIS FILE PROVES (and what it does not)
--------------------------------------------
`briefs/staircase-allp-construction-findings.md` (Theorem B) builds a period-`p`
size-passer from any integer `n` whose quality parameter

        delta(n) := ceil(n*L) - n*L          (L = log_2 3)

is SMALL ENOUGH -- precisely, `gamma(n) := -log_2(1 - 2^-delta(n)) >= Gamma(p,n)`.
`briefs/staircase-allp-diophantine-findings.md` (Lemma D / Theorem D) supplies such
an `n` in every scale window.  Both are one-sided: `delta` small means `gamma`
LARGE, and a size-passer with large `gamma` is a WORSE witness, not a better one.
Neither record bounds `gamma` above; `gamma = O(1)` is asserted in both and proved
in neither (`briefs/staircase-status-audit-findings.md` 0.1).

This file closes that gap by replacing the half-line `delta <= delta_hi` with a
two-sided ARC `delta_lo <= delta <= delta_hi`, and re-doing the whole chain --
sup Gamma, delta_hi, theta, the arc length, the resulting gamma bounds, p_0 -- in
certified arithmetic.  It also records the correction the arc forces on the
pigeonhole's window size -- the sharp criterion, which the record's Lemma D does
not use, needs 66 consecutive integers for the two-sided arc and only 61 for the
recorded one-sided one -- the (H0) verdict, the optimal constant this method
allows, and the required negative controls.

ARITHMETIC DISCIPLINE
---------------------
* `L` is enclosed in an exact rational interval by an `atanh` series with an
  explicit remainder bound (Part 0), cross-certified by exact big-integer
  comparisons `3^b` vs `2^a` and by `mpmath.iv` (directed-rounding interval
  arithmetic).
* Every per-`n` decision (`K = ceil(nL)`, `delta(n)` against a threshold) is an
  exact integer comparison against the certified enclosure of `L`; a decision
  that the enclosure cannot resolve is reported as a failure, never guessed.
* The transcendental constants (`Gamma*`, `delta_hi`, the `gamma` bounds) are
  computed in `mpmath.iv` and immediately converted to exact rational endpoints;
  every inequality that the theorem depends on is then checked as an exact
  rational inequality.
* Construction B and every rotation sum `R_r` are exact big-integer arithmetic.

Fresh code: imports nothing from `staircase_allp.py`,
`staircase_allp_construction.py`, `staircase_allp_diophantine.py`,
`p22_passer.py` or `uniform_trim.py`.  Proposition 12.6.1's numerator is
re-implemented from the statement, with the `sigma_j = s_j + m_{j+1}` convention
of Prop 12.6.1 / `experiments/record_defects_check.py`.

Stopping rules: size-passers only, never cycles; the divisibility system is
touched only to confirm every constructed instance FAILS it.  The cycle front
stays parked and 12.8.5 is unaffected.

Usage:  python experiments/staircase_gamma_upper.py [PMAX_ENDTOEND]
"""

import sys
from fractions import Fraction

import mpmath
from mpmath import iv

# --------------------------------------------------------------------------
# bookkeeping
# --------------------------------------------------------------------------

CHECKS = []


def check(label, ok, detail=""):
    CHECKS.append((label, bool(ok)))
    print(("  [ OK ] " if ok else "  [FAIL] ") + label + (("   " + detail) if detail else ""))
    return bool(ok)


def head(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def f2s(x, nd=12):
    """Decimal string of a Fraction, truncated (never rounded up) at nd places."""
    neg = x < 0
    x = -x if neg else x
    scaled = (x.numerator * 10 ** nd) // x.denominator
    s = str(scaled).rjust(nd + 1, "0")
    return ("-" if neg else "") + s[:-nd] + "." + s[-nd:]


# --------------------------------------------------------------------------
# PART 0 -- certified constants
# --------------------------------------------------------------------------

def atanh_bounds(z, nterms):
    """Rigorous (lo, hi) rational enclosure of atanh(z) for 0 < z < 1.

    atanh(z) = sum_{k>=0} z^(2k+1)/(2k+1); the tail after `nterms` terms is
    positive and bounded by z^(2N+1) / ((2N+1) * (1 - z^2)).
    """
    z = Fraction(z)
    z2 = z * z
    s = Fraction(0)
    zp = z
    for k in range(nterms):
        s += zp / (2 * k + 1)
        zp *= z2
    rem = zp / ((2 * nterms + 1) * (1 - z2))
    return s, s + rem


def certified_L(nterms=140):
    """Exact rational enclosure (Llo, Lhi) of L = log_2 3, with Llo < L < Lhi."""
    # ln 2 = 2 atanh(1/3);  ln(3/2) = 2 atanh(1/5);  ln 3 = ln 2 + ln(3/2)
    a2lo, a2hi = atanh_bounds(Fraction(1, 3), nterms)
    a5lo, a5hi = atanh_bounds(Fraction(1, 5), nterms)
    ln2lo, ln2hi = 2 * a2lo, 2 * a2hi
    ln3lo, ln3hi = ln2lo + 2 * a5lo, ln2hi + 2 * a5hi
    return (ln3lo / ln2hi, ln3hi / ln2lo), (ln2lo, ln2hi)


def mpf_to_fraction(x):
    """Exact Fraction value of an mpmath mpf / raw mpf tuple (binary, so exact)."""
    raw = x if isinstance(x, tuple) else getattr(x, "_mpf_", None)
    if raw is None:
        raw = x._mpi_[0]
    sign, man, exp, _bc = raw
    if man == 0:
        # zero / inf / nan encodings
        return Fraction(0)
    v = Fraction(man) * (Fraction(2) ** exp)
    return -v if sign else v


def iv_to_fractions(x):
    """Exact rational endpoints (lo, hi) of an mpmath interval."""
    lo, hi = x._mpi_
    return mpf_to_fraction(lo), mpf_to_fraction(hi)


head("PART 0 -- certified constants: L, theta, and the enclosure discipline")

iv.dps = 80
mpmath.mp.dps = 80

(L_LO, L_HI), (LN2_LO, LN2_HI) = certified_L()
check("L enclosure is nonempty and tight (width < 1e-90)",
      L_LO < L_HI and (L_HI - L_LO) < Fraction(1, 10 ** 90),
      "width ~ 1e-%d" % (len(str((1 / (L_HI - L_LO)).numerator // (1 / (L_HI - L_LO)).denominator)) - 1))

# Canary 1: exact big-integer certification of L at continued-fraction convergents.
# L > a/b  <=>  3^b > 2^a  (both sides are 2^(bL) vs 2^a).
CONVERGENTS = [(2, 1), (3, 2), (8, 5), (19, 12), (65, 41), (84, 53), (485, 306),
               (1054, 665), (24727, 15601)]
conv_ok = True
for a, b in CONVERGENTS:
    exact_gt = 3 ** b > 2 ** a               # exact: is L > a/b ?
    encl_gt = L_LO > Fraction(a, b)
    encl_lt = L_HI < Fraction(a, b)
    if exact_gt and not encl_gt:
        conv_ok = False
    if (not exact_gt) and not encl_lt:
        conv_ok = False
check("L enclosure agrees with exact 3^b vs 2^a at 9 convergents", conv_ok)

# Canary 2: mpmath.iv (independent implementation, directed rounding).
L_IV = iv.log(3) / iv.log(2)
liv_lo, liv_hi = iv_to_fractions(L_IV)
check("L enclosure is consistent with mpmath.iv's log(3)/log(2)",
      L_LO < liv_hi and L_HI > liv_lo)

# theta = 8 - 5L.  Upper bound on theta is what the pigeonhole needs.
THETA_LO = 8 - 5 * L_HI
THETA_HI = 8 - 5 * L_LO
check("theta = 8 - 5L is positive and < 0.0752",
      THETA_LO > 0 and THETA_HI < Fraction(752, 10000),
      "theta in [%s, %s]" % (f2s(THETA_LO), f2s(THETA_HI)))

# Exact integer enclosure of L at scale 2^P, for the per-n work.
P_SCALE = 256
SCALE = 1 << P_SCALE
L_INT_LO = (L_LO.numerator * SCALE) // L_LO.denominator          # <= L*2^P
L_INT_HI = -((-L_HI.numerator * SCALE) // L_HI.denominator)      # >= L*2^P
check("integer enclosure L_INT_LO/2^256 < L < L_INT_HI/2^256",
      Fraction(L_INT_LO, SCALE) < L_LO and Fraction(L_INT_HI, SCALE) > L_HI)


def delta_scaled(n):
    """Exact (K, dlo_int, dhi_int) with dlo_int < delta(n)*2^P < dhi_int.

    K = ceil(n*L) is determined exactly (n*L is never an integer, L irrational).
    Raises if the enclosure cannot resolve the floor -- never guesses.
    """
    lo = n * L_INT_LO
    hi = n * L_INT_HI
    flo = lo >> P_SCALE
    fhi = hi >> P_SCALE
    if flo != fhi:
        raise RuntimeError("L enclosure too coarse to resolve floor(n*L) at n=%d" % n)
    K = flo + 1
    return K, K * SCALE - hi, K * SCALE - lo


def delta_ge(n, r):
    """Certified: delta(n) >= r ?  (r a Fraction).  Returns True/False, raises if unresolved."""
    _K, dl, dh = delta_scaled(n)
    if dl * r.denominator >= r.numerator * SCALE:
        return True
    if dh * r.denominator <= r.numerator * SCALE:
        return False
    raise RuntimeError("unresolved delta(n) vs r at n=%d" % n)


def delta_le(n, r):
    _K, dl, dh = delta_scaled(n)
    if dh * r.denominator <= r.numerator * SCALE:
        return True
    if dl * r.denominator >= r.numerator * SCALE:
        return False
    raise RuntimeError("unresolved delta(n) vs r at n=%d" % n)


def delta_fr(n):
    """A Fraction inside the certified enclosure of delta(n) (for display only)."""
    _K, dl, dh = delta_scaled(n)
    return Fraction(dl + dh, 2 * SCALE)


# Canary 3: K = ceil(nL) must equal bitlength(3^n) (exact, no floats).
kok = True
for n in list(range(1, 400)) + [1000, 1587, 1588, 10009, 25145]:
    K, _, _ = delta_scaled(n)
    if K != (3 ** n).bit_length():
        kok = False
check("K = ceil(n*L) from the enclosure equals bit_length(3^n), 405 values", kok)

# Canary 4: the step-5 rotation law delta(n+5) = delta(n) + theta (mod 1).
rot_ok = True
for n in range(1, 500):
    d0, d5 = delta_fr(n), delta_fr(n + 5)
    pred = d0 + (THETA_LO + THETA_HI) / 2
    if pred >= 1:
        pred -= 1
    if abs(pred - d5) > Fraction(1, 10 ** 20):
        rot_ok = False
check("delta(n+5) = delta(n) + theta (mod 1) at 499 values", rot_ok)


# --------------------------------------------------------------------------
# PART 1 -- sup Gamma, delta_hi, and the arc, in certified arithmetic
# --------------------------------------------------------------------------

head("PART 1 -- sup Gamma, the induced delta_hi, and the arc")

LN2_IV = iv.log(2)


def f_gamma(delta_iv):
    """gamma(delta) = -log_2(1 - 2^-delta); also delta(gamma) -- the map is an involution."""
    return -iv.log(1 - iv.exp(-delta_iv * LN2_IV)) / LN2_IV


def as_iv(fr):
    """Rigorous interval enclosure of an exact Fraction."""
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)


def gamma_bounds_from_delta(dlo, dhi):
    """Exact rational (glo, ghi) with glo <= gamma(delta) <= ghi for delta in [dlo,dhi]."""
    # gamma is strictly decreasing in delta
    g_hi = f_gamma(as_iv(dlo))
    g_lo = f_gamma(as_iv(dhi))
    return iv_to_fractions(g_lo)[0], iv_to_fractions(g_hi)[1]


def delta_bounds_from_gamma(g):
    """Exact rational (dlo, dhi) enclosing delta = -log_2(1 - 2^-g)."""
    return iv_to_fractions(f_gamma(as_iv(g)))


# Gamma(p,n) = Gamma0(p,n) + 1 + eta, with beta = 1 + eta appearing linearly.
def Gamma_iv(p, n, s_crash):
    """Gamma(p,n) of Theorem B, as an mpmath interval, eta included rigorously."""
    Lv = L_IV
    u = Lv - 1
    D = Lv ** (p - 1)
    if s_crash > 4000:
        eta = iv.mpf([0, mpmath.mpf(2) ** (-4000)])
    else:
        eta = -iv.log(1 - iv.exp(-iv.mpf(s_crash) * LN2_IV)) / LN2_IV
    beta = 1 + eta
    num = (n - 1) * u ** 2 + D * (1 + beta * u) - (p - 2 + beta) * u - Lv
    den = u * (D - 1)
    return num / den


def Gamma0_iv(p, n):
    """Gamma with beta := 1 (i.e. eta = 0); Gamma = Gamma0_plus1 + eta."""
    Lv = L_IV
    u = Lv - 1
    D = Lv ** (p - 1)
    num = (n - 1) * u ** 2 + D * (1 + u) - (p - 1) * u - Lv
    den = u * (D - 1)
    return num / den


# --- the uniform bound on Gamma, proved algebraically, then checked numerically.
#
#   Gamma(p,n) = Gamma0(p,n) + eta        where beta = 1 + eta enters linearly:
#   the beta-terms of the numerator are beta*u*(D-1), and the denominator is
#   u*(D-1), so beta contributes exactly +beta.  Hence with kappa_max = 1.05,
#
#     Gamma(p,n) <= kappa_max*L*(L-1) + 1/(L-1) + 1 + eta
#                     - (p - 1.3885.)/(L^(p-1) - 1)
#                 <  GAMMA_STAR   for every p >= 2 and every n <= 1.05*L^p.
#
KAPPA_MAX = Fraction(21, 20)
ETA_CAP = Fraction(1, 2 ** 900)          # certified bound on eta wherever the theorem applies
G_STAR_IV = as_iv(KAPPA_MAX) * L_IV * (L_IV - 1) + 1 / (L_IV - 1) + 1
G_STAR_NOETA = iv_to_fractions(G_STAR_IV)[1]
G_STAR = G_STAR_NOETA + ETA_CAP         # certified UPPER bound on sup Gamma, eta included
print("  Gamma* = 1.05*L*(L-1) + 1/(L-1) + 1 + eta  <=  %s  (eta < 2^-900 wherever used)"
      % f2s(G_STAR))

# beta enters Gamma linearly with coefficient exactly 1 -- checked numerically.
beta_lin_ok = True
for (p, n, sc) in [(6, 16, 9), (16, 1588, 913), (24, 63163, 36913), (30, 1001317, 585196)]:
    g_full = Gamma_iv(p, n, sc)
    g_zero = Gamma0_iv(p, n)
    eta = -iv.log(1 - iv.exp(-iv.mpf(sc) * LN2_IV)) / LN2_IV
    dlo_f, dhi_f = iv_to_fractions(g_full - (g_zero + eta))
    if not (abs(dlo_f) < Fraction(1, 10 ** 40) and abs(dhi_f) < Fraction(1, 10 ** 40)):
        beta_lin_ok = False
check("Gamma(p,n) = Gamma0(p,n) + eta exactly (beta enters with coefficient 1)", beta_lin_ok)

# The proof of the uniform bound, checked step by step.
#
#   Gamma0(p,n)  <=  1.05*L*u + 1/u  +  B(p)/(L^(p-1) - 1),
#   B(p) := 1.05*L*u + 1/u - u - (p-2) - L/u        (u = L-1)
#
# and B(p) < 0 for every p >= 2.  Both halves are checked below; together they
# give Gamma(p,n) = Gamma0 + eta < Gamma* for every p >= 2, n <= 1.05*L^p --
# an ALGEBRAIC bound, not a table.
u_lo, u_hi = L_LO - 1, L_HI - 1


def B_bracket_hi(p):
    """Certified upper bound on B(p)."""
    return iv_to_fractions(as_iv(KAPPA_MAX) * L_IV * (L_IV - 1) + 1 / (L_IV - 1)
                           - (L_IV - 1) - (p - 2) - L_IV / (L_IV - 1))[1]


bracket_ok = all(B_bracket_hi(p) < 0 for p in list(range(2, 200)) + [300, 1000, 2000])
check("the correction bracket B(p) is negative for every p in 2..199, 300, 1000, 2000",
      bracket_ok, "B(2) <= %s" % f2s(B_bracket_hi(2)))

TOL = Fraction(1, 10 ** 60)          # the interval engine's own resolution at dps = 80
sup_ok = True
deriv_ok = True
worst = Fraction(0)
worst_p = None
strict_upto = 0
for p in list(range(2, 200)) + [300, 500, 1000, 2000]:
    nmax_fr = mpf_to_fraction((L_IV ** p * KAPPA_MAX.numerator / KAPPA_MAX.denominator)._mpi_[1])
    nmax = nmax_fr.numerator // nmax_fr.denominator
    g0 = iv_to_fractions(Gamma0_iv(p, nmax))[1]
    D_lo = iv_to_fractions(L_IV ** (p - 1))[0]
    if D_lo > 1 and g0 > G_STAR_NOETA + B_bracket_hi(p) / (D_lo - 1) + TOL:
        deriv_ok = False                    # the derivation's bound must dominate Gamma0
    if g0 > G_STAR_NOETA + TOL:
        sup_ok = False
    if g0 < G_STAR_NOETA and p == strict_upto + 2:
        strict_upto = p
    if g0 > worst:
        worst, worst_p = g0, p
check("the derivation's bound Gamma* + B(p)/(L^(p-1)-1) dominates Gamma0(p, n_max) "
      "at every tested p", deriv_ok)
check("Gamma(p, floor(1.05*L^p)) <= Gamma* at every tested p (strictly, once resolvable)",
      sup_ok, "max %s, attained only in the p -> infinity limit (p = %d); the strict "
              "inequality is the negative bracket B(p), not this table"
              % (f2s(worst), worst_p))

D_HI_LO, D_HI_HI = delta_bounds_from_gamma(G_STAR)   # delta_hi = f(Gamma*)
print("  delta_hi = -log_2(1 - 2^-Gamma*) in [%s, %s]" % (f2s(D_HI_LO), f2s(D_HI_HI)))
D_HI = D_HI_LO                                       # certified LOWER bound: safe to use

check("delta_hi's certified lower bound exceeds the record's rounded 0.116939",
      D_HI > Fraction(116939, 10 ** 6),
      "0.116939 is a safe (low) rounding of %s" % f2s(D_HI))

# --- the arc.
DELTA_LO = Fraction(83, 2000)          # 0.0415
ARC_LEN = D_HI - DELTA_LO
check("arc [delta_lo, delta_hi] is longer than theta  (the pigeonhole's own hypothesis)",
      ARC_LEN > THETA_HI,
      "len %s > theta %s, margin %s" % (f2s(ARC_LEN), f2s(THETA_HI), f2s(ARC_LEN - THETA_HI)))

G_LO_ARC, G_HI_ARC = gamma_bounds_from_delta(DELTA_LO, D_HI)
print("  delta in [%s, %s]  =>  gamma in [%s, %s]" %
      (f2s(DELTA_LO), f2s(D_HI), f2s(G_LO_ARC), f2s(G_HI_ARC)))
C_CONST = G_HI_ARC
check("the arc's lower end still meets Theorem B's hypothesis (gamma >= Gamma*)",
      G_LO_ARC >= G_STAR, "gamma >= %s >= Gamma* = %s" % (f2s(G_LO_ARC), f2s(G_STAR)))
check("the arc's upper end is an absolute constant C < 5.1403", C_CONST < Fraction(51403, 10000),
      "C = %s" % f2s(C_CONST))

# --- the optimum this method allows.
DLO_OPT = D_HI - THETA_HI
_gl, C_OPT = gamma_bounds_from_delta(DLO_OPT, D_HI)
print("  method optimum: delta_lo -> delta_hi - theta = %s  =>  gamma < %s (infimum, not attained)"
      % (f2s(DLO_OPT), f2s(C_OPT)))
check("the chosen delta_lo = 0.0415 sits strictly inside the admissible range",
      DELTA_LO < DLO_OPT, "0.0415 < %s" % f2s(DLO_OPT))


# --------------------------------------------------------------------------
# PART 2 -- the two-sided pigeonhole: how many consecutive integers are needed
# --------------------------------------------------------------------------

head("PART 2 -- the two-sided pigeonhole, and the window-size correction")

# The mechanism, stated sharply.  delta(n+5) = delta(n) + theta (mod 1), so the
# J+1 values delta(N), delta(N+5), ..., delta(N+5J) are  delta(N) + j*theta (mod 1).
# For a CLOSED arc A of length L_arc, the set of starting phases that the sweep
# catches is the union of the J+1 translates  A - j*theta (mod 1), and that union
# covers the circle -- i.e. the guarantee holds for EVERY N -- exactly when
#
#      maxgap{ j*theta mod 1 : 0 <= j <= J }  <=  L_arc .
#
# This is an IF AND ONLY IF: a gap wider than L_arc is a set of uncaught phases.
# For J*theta < 1 the gaps are theta (J of them) and the wrap gap 1 - J*theta, so
#
#      minimal J  =  ceil( (1 - L_arc) / theta ),      valid whenever L_arc > theta,
#
# and the guarantee then covers any 5J + 1 consecutive integers.
#
# The recorded Lemma D uses the coarser sufficient condition "14*theta >= 1", i.e.
# 71 consecutive integers.  The sharp criterion needs only J = 12 there (61
# integers); for the SHORTER two-sided arc it needs J = 13, i.e. 66 consecutive
# integers -- so the two-sided refinement costs 5 integers of window, not the
# extra 5 the audit's "identical 71-integer argument" implicitly assumed, and the
# genuinely binding inequality is L_arc > theta, not the span.

def maxgap(J):
    """Exact maximal circular gap of {j*theta mod 1 : 0<=j<=J}, as (lo, hi) Fractions."""
    pts_lo = sorted(set((j * THETA_LO) % 1 for j in range(J + 1)))
    pts_hi = sorted(set((j * THETA_HI) % 1 for j in range(J + 1)))
    def mg(pts):
        gaps = [pts[i + 1] - pts[i] for i in range(len(pts) - 1)] + [1 - pts[-1] + pts[0]]
        return max(gaps)
    return min(mg(pts_lo), mg(pts_hi)), max(mg(pts_lo), mg(pts_hi))


def sweep_ok(J, arc_len):
    """Certified: does the (J+1)-point sweep catch every closed arc of length arc_len?"""
    return maxgap(J)[1] <= arc_len


def minimal_J(arc_len):
    J = 1
    while not sweep_ok(J, arc_len):
        J += 1
        if J > 100000:
            return None
    return J


ONE_SIDED_ARC = D_HI                           # [0, delta_hi], the recorded Lemma D
J_ONE = minimal_J(ONE_SIDED_ARC)
J_TWO = minimal_J(ARC_LEN)
check("maxgap{j*theta} for J*theta < 1 is max(theta, 1 - J*theta)  (three-distance check)",
      all(abs(maxgap(J)[1] - max(THETA_HI, 1 - J * THETA_LO)) < Fraction(1, 10 ** 60)
          for J in range(1, 14)))
check("one-sided arc: the sharp minimal sweep is J = 12, i.e. 61 consecutive integers "
      "(the recorded Lemma D's 71 is valid but not minimal)",
      J_ONE == 12, "J = %s -> %d integers" % (J_ONE, 5 * J_ONE + 1))
check("two-sided arc: the sharp minimal sweep is J = 13, i.e. 66 consecutive integers",
      J_TWO == 13, "J = %s -> %d integers" % (J_TWO, 5 * J_TWO + 1))
check("two-sided arc: J = 12 (61 integers) genuinely does NOT suffice",
      not sweep_ok(12, ARC_LEN),
      "maxgap(12) = %s > arc = %s" % (f2s(maxgap(12)[1]), f2s(ARC_LEN)))
check("the binding inequality is arc > theta, and it holds with certified margin",
      ARC_LEN > THETA_HI, "margin %s" % f2s(ARC_LEN - THETA_HI))

WINDOW_INTEGERS = 5 * J_TWO + 1                 # 66


def good_n(n, arc_lo=None, arc_hi=None):
    """delta(n) in the certified arc?  Exact."""
    arc_lo = DELTA_LO if arc_lo is None else arc_lo
    arc_hi = D_HI if arc_hi is None else arc_hi
    return delta_ge(n, arc_lo) and delta_le(n, arc_hi)


# Direct verification of the pigeonhole claim on the progression itself.
prog_fail = 0
prog_tested = 0
for N in range(1, 20001):
    prog_tested += 1
    if not any(good_n(N + 5 * j) for j in range(J_TWO + 1)):
        prog_fail += 1
check("pigeonhole holds on the step-5 progression: some n in {N,N+5,...,N+65} is good, "
      "N = 1..20000", prog_fail == 0, "%d/%d failures" % (prog_fail, prog_tested))

# The same test one step short -- must FAIL somewhere, since the criterion is sharp.
prog_short_fail = 0
first_bad = None
for N in range(1, 20001):
    if not any(good_n(N + 5 * j) for j in range(J_TWO)):
        prog_short_fail += 1
        if first_bad is None:
            first_bad = N
check("at J = 12 (61 integers) the two-sided sweep genuinely misses -- the criterion bites",
      prog_short_fail > 0,
      "%d failing starts in N=1..20000, first at N=%d" % (prog_short_fail, first_bad or -1))

# Brute force over all integers (not just one progression): the true worst run.
BRUTE = 3 * 10 ** 6
run = best_run = 0
best_at = 0
run1 = best_run1 = 0
for n in range(1, BRUTE + 1):
    K, dl, dh = delta_scaled(n)
    lo_ok = dl * DELTA_LO.denominator >= DELTA_LO.numerator * SCALE
    hi_ok = dh * D_HI.denominator <= D_HI.numerator * SCALE
    if lo_ok and hi_ok:
        run = 0
    else:
        run += 1
        if run > best_run:
            best_run, best_at = run, n
    if hi_ok:
        run1 = 0
    else:
        run1 += 1
        best_run1 = max(best_run1, run1)
check("brute force n <= 3e6: longest run of consecutive integers failing the TWO-SIDED arc",
      best_run < WINDOW_INTEGERS,
      "%d, against the proved bound %d (run ends at n=%d)" % (best_run, WINDOW_INTEGERS - 1, best_at))
check("brute force n <= 3e6: longest run failing the ONE-SIDED condition reproduces Lemma D's 11",
      best_run1 == 11, "%d" % best_run1)


# --------------------------------------------------------------------------
# PART 3 -- p_0 and the finite tail
# --------------------------------------------------------------------------

head("PART 3 -- p_0 from the window count, and the finite tail")


def window_int_range(p, kappa_hi=KAPPA_MAX):
    """Exact (n_first, n_last) integers inside [L^p, kappa_hi*L^p]."""
    lo_iv = L_IV ** p
    hi_iv = iv.mpf(kappa_hi.numerator) / iv.mpf(kappa_hi.denominator) * lo_iv
    lo = mpf_to_fraction(lo_iv.b)      # pessimistic: left edge as high as possible
    hi = mpf_to_fraction(hi_iv.a)      # pessimistic: right edge as low as possible
    n_first = -((-lo.numerator) // lo.denominator)      # ceil
    n_last = hi.numerator // hi.denominator             # floor
    return n_first, n_last


print("   p |   window [L^p, 1.05 L^p]        | #integers | >= %d ?" % WINDOW_INTEGERS)
print("  ---+---------------------------------+-----------+--------")
P0 = None
for p in range(2, 25):
    a, b = window_int_range(p)
    cnt = max(0, b - a + 1)
    flag = "yes" if cnt >= WINDOW_INTEGERS else "no"
    if cnt >= WINDOW_INTEGERS and P0 is None:
        P0 = p
    print("  %3d | %12d .. %-12d    | %9d | %s" % (p, a, b, cnt, flag))
check("p_0 = 16: the canonical window first holds %d consecutive integers at p = 16"
      % WINDOW_INTEGERS,
      P0 == 16, "p_0 = %s" % P0)
a16, b16 = window_int_range(16)
a15, b15 = window_int_range(15)
check("p = 15 falls short (the finite tail is genuinely finite, not vacuous)",
      b15 - a15 + 1 < WINDOW_INTEGERS,
      "p=15 holds %d integers, p=16 holds %d" % (b15 - a15 + 1, b16 - a16 + 1))


# --------------------------------------------------------------------------
# PART 4 -- (H0), and the witness table
# --------------------------------------------------------------------------

head("PART 4 -- the witness at each p, (H0), and the two-sided gamma bracket")


def gamma_iv_of_n(n):
    K, dl, dh = delta_scaled(n)
    return f_gamma(iv.mpf([dl, dh]) / iv.mpf(SCALE))


def gamma_bounds_of_n(n):
    return iv_to_fractions(gamma_iv_of_n(n))


def eta_bound(s_crash):
    """Certified upper bound (Fraction) on eta = -log_2(1 - 2^-s) <= 2^(1-s) for s >= 1."""
    return Fraction(1, 2 ** max(0, min(s_crash, 4000) - 1))


def H0_check(p, n):
    """(H0): S >= p and (L-1)(n-p) + gamma >= p + eta.  Certified rational inequality."""
    K, _, _ = delta_scaled(n)
    S = K - n
    if S < p:
        return False, S, None
    s_crash = S - (p - 1)
    lhs_lo = iv_to_fractions((L_IV - 1) * (n - p) + gamma_iv_of_n(n))[0]
    rhs_hi = p + eta_bound(s_crash)
    return lhs_lo > rhs_hi, S, lhs_lo - rhs_hi


def gamma_demand(p, n):
    """Certified upper bound (Fraction) on Gamma(p,n) = Gamma0(p,n) + eta."""
    K, _, _ = delta_scaled(n)
    s_crash = K - n - (p - 1)
    return iv_to_fractions(Gamma0_iv(p, n))[1] + eta_bound(s_crash)


def hypothesis_ok(p, n):
    """(H1): gamma(n) >= max(2 + eta, Gamma(p,n)), certified, on the EXACT Gamma."""
    K, _, _ = delta_scaled(n)
    S = K - n
    if S < p or S - (p - 1) < 1:
        return False
    g_lo = gamma_bounds_of_n(n)[0]
    e = eta_bound(S - (p - 1))
    return g_lo >= gamma_demand(p, n) and g_lo >= 2 + e


def first_witness(p, kappa_hi=KAPPA_MAX, scan_extra=0):
    """First n in the window satisfying the two-sided arc; returns None if absent."""
    a, b = window_int_range(p, kappa_hi)
    for n in range(a, b + 1 + scan_extra):
        if good_n(n):
            return n
    return None


print("   p |        n | offset | delta(n)     | gamma(n) | Gamma(p,n) | (H0) | gamma<=C")
print("  ---+----------+--------+--------------+----------+------------+------+---------")
WITNESS = {}
tail_ok = True
for p in list(range(16, 41)):
    a, _b = window_int_range(p)
    n = first_witness(p)
    if n is None:
        tail_ok = False
        print("  %3d |     ---- | none found in window" % p)
        continue
    WITNESS[p] = n
    G = gamma_demand(p, n)
    h0, _S, _slack = H0_check(p, n)
    glo, ghi = gamma_bounds_of_n(n)
    ok_c = ghi <= C_CONST
    ok_h1 = hypothesis_ok(p, n)
    if not (h0 and ok_c and ok_h1):
        tail_ok = False
    print("  %3d | %8d | %6d | %s | %8s | %10s | %4s | %s" %
          (p, n, n - a, f2s(delta_fr(n), 10), f2s(glo, 4), f2s(G, 4),
           "yes" if h0 else "NO", "yes" if ok_c else "NO"))
check("p = 16..40: window witness exists, meets (H1) and (H0), and has gamma <= C", tail_ok)

# (H0) is not a table: at the canonical scale it follows from n >= L^p alone, for every
# p >= 16, because S >= (L-1)*n and gamma >= Gamma* > 3.68 on the arc.
h0_alg = True
for p in list(range(16, 400)) + [1000, 2000]:
    Lp_lo = iv_to_fractions(L_IV ** p)[0]
    if not ((L_LO - 1) * Lp_lo >= p):                       # S >= (L-1)n >= (L-1)L^p >= p
        h0_alg = False
    if not ((L_LO - 1) * (Lp_lo - p) + G_STAR >= p + ETA_CAP):
        h0_alg = False
check("(H0) holds for EVERY p >= 16 and EVERY n in the window, from the scale alone: "
      "S >= (L-1)L^p >= p, and (L-1)(n-p) + Gamma* >= p + eta", h0_alg,
      "at p = 16 the two margins are %s and %s"
      % (f2s((L_LO - 1) * iv_to_fractions(L_IV ** 16)[0] - 16, 2),
         f2s((L_LO - 1) * (iv_to_fractions(L_IV ** 16)[0] - 16) + G_STAR - 16, 2)))
check("(H0)'s first clause is exactly what fails at the small p of the finite tail",
      not ((L_LO - 1) * iv_to_fractions(L_IV ** 2)[0] >= 2),
      "at p = 2, (L-1)L^p = %s < 2" % f2s((L_LO - 1) * iv_to_fractions(L_IV ** 2)[0], 4))

print("")
print("  finite tail 2 <= p <= 15 (window widened only where the canonical one is short):")
print("   p |        n | kappa   | gamma(n) | Gamma(p,n) | (H0) | (H1) | gamma<=C")
print("  ---+----------+---------+----------+------------+------+------+---------")
TAIL = {}
tail2_ok = True
for p in range(2, 16):
    a, _ = window_int_range(p)
    found = None
    for n in range(max(1, a - 1), max(60, 40 * a)):
        if n < 1:
            continue
        try:
            if not good_n(n):
                continue
        except RuntimeError:
            continue
        K, _, _ = delta_scaled(n)
        S = K - n
        if S < p:
            continue
        if not hypothesis_ok(p, n):
            continue
        h0, _S, _sl = H0_check(p, n)
        if not h0:
            continue
        found = n
        break
    if found is None:
        print("  %3d |     ---- | (no n in reach -- outside Construction B)" % p)
        if p not in (2, 4):
            tail2_ok = False
        continue
    n = found
    TAIL[p] = n
    G = gamma_demand(p, n)
    h0, _S, _sl = H0_check(p, n)
    glo, ghi = gamma_bounds_of_n(n)
    kappa = iv_to_fractions(iv.mpf(n) / L_IV ** p)[1]
    if ghi > C_CONST:
        tail2_ok = False
    print("  %3d | %8d | %7s | %8s | %10s | %4s | %4s | %s" %
          (p, n, f2s(kappa, 4), f2s(glo, 4), f2s(G, 4),
           "yes" if h0 else "NO", "yes", "yes" if ghi <= C_CONST else "NO"))
check("finite tail 3 <= p <= 15: an explicit witness with the same two-sided bracket", tail2_ok)
check("p in {2,4}: no witness anywhere in a wide scan -- outside Construction B's reach, "
      "as its own scope note records",
      2 not in TAIL and 4 not in TAIL,
      "Gamma(2,n) = n + eta and Gamma(4,n) ~ 0.196n + 1.507, so gamma <= C caps n at 5 "
      "and 18; no such n meets the arc and (H0).  Their canonical windows "
      "[L^p, 1.05L^p] = %s, %s hold no integer either."
      % (window_int_range(2), window_int_range(4)))


# --------------------------------------------------------------------------
# PART 5 -- Construction B, exact, and the end-to-end size/divisibility test
# --------------------------------------------------------------------------

head("PART 5 -- Construction B end to end (own evaluator, exact big integers)")


def construction_B(p, n):
    """Construction B of `staircase-allp-construction-findings` 4, exact integers."""
    three_n = 3 ** n
    K = three_n.bit_length()                 # = ceil(n*L), exactly
    S = K - n
    s_crash = S - (p - 1)
    if s_crash < 1:
        return None
    q = (1 << K) - three_n
    crash_factor = (1 << s_crash) - 1
    T_prev = 0
    m = []
    for r in range(p - 1):
        X = (3 ** T_prev) * (1 << (n - T_prev + p - 1 - r)) * crash_factor
        cap = (X // q).bit_length() - 1
        budget = n - 1 - T_prev - (p - 2 - r)
        mr = min(cap, budget)
        if mr < 1:
            return None
        m.append(mr)
        T_prev += mr
    c = n - T_prev
    if c < 1:
        return None
    m.append(c)
    s = [1] * (p - 1) + [s_crash]
    return m, s, K, q


def rotation_numerators(m, s):
    """Prop 12.6.1: R_r for every rotation r, exact.  sigma_j = s_j + m_{j+1}."""
    p = len(m)
    out = []
    for r in range(p):
        mm = [m[(r + j) % p] for j in range(p)]
        ss = [s[(r + j) % p] for j in range(p)]
        sig = [ss[j] + mm[(j + 1) % p] for j in range(p)]
        R = 0
        M_t = sum(mm)          # M_t = sum_{j>t} mm[j]
        S_t = 0                # S_t = sum_{j<t} sig[j]
        for t in range(p):
            M_t -= mm[t]
            R += (3 ** M_t) * (1 << S_t) * ((1 << ss[t]) - 1)
            S_t += sig[t]
        out.append(R)
    return out


# Canary A: the trivial cycle read as a fake period-p cycle gives R_r = q = 4^p - 3^p.
triv_ok = True
for p in (1, 2, 3, 4, 7, 11):
    m = [1] * p
    s = [1] * p
    Rs = rotation_numerators(m, s)
    q = (1 << (2 * p)) - 3 ** p
    if any(R != q for R in Rs) or q != 4 ** p - 3 ** p:
        triv_ok = False
check("canary: trivial cycle gives R_r = q = 4^p - 3^p at p in {1,2,3,4,7,11}", triv_ok)

# Canary B: 12.6.1.1's transport recurrence, on random profiles (audits the evaluator).
import random
random.seed(20260728)
rec_ok = True
for _ in range(120):
    p = random.randint(2, 7)
    m = [random.randint(1, 9) for _ in range(p)]
    s = [random.randint(1, 9) for _ in range(p)]
    n = sum(m)
    K = sum(s) + n
    q = (1 << K) - 3 ** n
    Rs = rotation_numerators(m, s)
    for r in range(p):
        lhs = (1 << (s[r] + m[(r + 1) % p])) * Rs[(r + 1) % p]
        rhs = (3 ** m[r]) * Rs[r] + ((1 << s[r]) - 1) * q
        if lhs != rhs:
            rec_ok = False
check("canary: 12.6.1.1 transport recurrence holds at every rotation of 120 random profiles",
      rec_ok)

# Canary C: the published p = 7 staircase of 12.8.3.
m7 = [4, 7, 9, 15, 23, 35, 1]
n7 = sum(m7)
K7 = (3 ** n7).bit_length()
s7 = [1] * 6 + [K7 - n7 - 6]
q7 = (1 << K7) - 3 ** n7
R7 = rotation_numerators(m7, s7)
g7 = gamma_bounds_of_n(n7)
check("canary: published p=7 staircase m=(4,7,9,15,23,35,1) passes all 7 size conditions",
      all(q7 <= R for R in R7), "n=%d, gamma=%s" % (n7, f2s(g7[0], 3)))
check("canary: it reproduces gamma = 6.744 and fails divisibility at all 7 rotations",
      g7[0] > Fraction(6743, 1000) and g7[1] < Fraction(6745, 1000)
      and all(R % q7 != 0 for R in R7))

PMAX_E2E = int(sys.argv[1]) if len(sys.argv) > 1 else 26
print("")
print("  end-to-end (window witness -> Construction B -> all p rotations, exact):")
print("   p |        n | gamma(n) | crash c | all q<=R_r | min R_r/q | any q|R_r")
print("  ---+----------+----------+---------+------------+-----------+----------")
e2e_ok = True
e2e_rows = 0
for p in sorted(set(list(TAIL.keys()) + [pp for pp in WITNESS if pp <= PMAX_E2E])):
    n = TAIL.get(p) or WITNESS.get(p)
    if n is None:
        continue
    built = construction_B(p, n)
    if built is None:
        e2e_ok = False
        print("  %3d | %8d | construction infeasible" % (p, n))
        continue
    m, s, K, q = built
    Rs = rotation_numerators(m, s)
    sizes = [q <= R for R in Rs]
    divs = [R % q == 0 for R in Rs]
    ratio = min(Fraction(R, q) for R in Rs)
    g = gamma_bounds_of_n(n)
    ok = (sum(m) == n and sum(s) + n == K and all(x >= 1 for x in m)
          and all(sizes) and not any(divs) and m[-1] == 1)
    if not ok:
        e2e_ok = False
    e2e_rows += 1
    print("  %3d | %8d | %8s | %7d | %10s | %9s | %s" %
          (p, n, f2s(g[0], 4), m[-1], "yes" if all(sizes) else "NO",
           f2s(ratio, 4), "yes" if any(divs) else "no"))
check("end-to-end: every witness builds, passes all p size conditions, has crash depth 1, "
      "and FAILS q | R_r at every rotation", e2e_ok, "%d periods" % e2e_rows)


# --------------------------------------------------------------------------
# PART 6 -- negative controls
# --------------------------------------------------------------------------

head("PART 6 -- negative controls (a bound that never bites has not been tested)")

# NC-1: an arc SHORTER than theta leaves an empty maximal gap at the licensed sweep
#       length.  (It does NOT fail for every J: lengthening the sweep past J*theta > 1
#       refines the grid by the three-distance theorem, and that refinement is exactly
#       the ladder of Part 7c.  The claim under test is the one the theorem uses.)
short_arc_len = THETA_LO * Fraction(9, 10)
short_lo = D_HI - short_arc_len
J_SHORT = minimal_J(short_arc_len)
check("NC-1a: an arc of length 0.9*theta is NOT caught by the licensed 14-point sweep "
      "-- its maximal gap theta is left empty",
      all(not sweep_ok(J, short_arc_len) for J in range(1, J_TWO + 1)),
      "maxgap(J) = theta = %s > 0.9*theta = %s for all J <= %d; the first J that "
      "would work is %s, costing %d integers"
      % (f2s(THETA_HI), f2s(short_arc_len), J_TWO, J_SHORT,
         5 * (J_SHORT or 0) + 1))
nc1_empty = 0
nc1_first = None
for N in range(1, 20001):
    hit = False
    for j in range(J_TWO + 1):
        n = N + 5 * j
        if delta_ge(n, short_lo) and delta_le(n, D_HI):
            hit = True
            break
    if not hit:
        nc1_empty += 1
        if nc1_first is None:
            nc1_first = N
check("NC-1b: and the failure is realised at actual N -- whole progressions are empty",
      nc1_empty > 0,
      "%d empty starts among N=1..20000 (first N=%d)" % (nc1_empty, nc1_first or -1))

# NC-1c: the same sweep, arc at full length -- must never be empty (control on the control).
nc1c_empty = 0
for N in range(1, 20001):
    if not any(good_n(N + 5 * j) for j in range(J_TWO + 1)):
        nc1c_empty += 1
check("NC-1c: the full arc with the same 14 sweep points is never empty, same 20000 starts",
      nc1c_empty == 0, "%d empty" % nc1c_empty)

# NC-2: an n with delta below delta_lo must exceed the gamma bound.
nc2_tested = nc2_viol = 0
nc2_worst = Fraction(0)
for p in [16, 18, 20, 22, 24, 26, 28, 30]:
    a, b = window_int_range(p)
    for n in range(a, min(b, a + 200) + 1):
        if delta_le(n, DELTA_LO) and not delta_ge(n, DELTA_LO):
            nc2_tested += 1
            glo, _ghi = gamma_bounds_of_n(n)
            if glo <= C_CONST:
                nc2_viol += 1
            nc2_worst = max(nc2_worst, glo)
check("NC-2: every n with delta < delta_lo has gamma > C  (the upper bound bites)",
      nc2_viol == 0 and nc2_tested > 0,
      "%d such n tested, %d violations, largest gamma seen %s"
      % (nc2_tested, nc2_viol, f2s(nc2_worst, 3)))

# NC-3: an n above delta_hi must fail Theorem B's hypothesis.
#       Two distinct statements, kept apart:
#         (a) above the EXACT per-(p,n) threshold f(Gamma(p,n)), (H1) must fail --
#             this tests the delta <-> gamma <-> Gamma conversion end to end;
#         (b) above the UNIFORM threshold delta_hi = f(Gamma*), (H1) may still hold,
#             because Gamma* > Gamma(p,n) strictly.  The count is the price of using
#             the supremum, and it is reported, not hidden.
#       Note also that (H1) is only SUFFICIENT: an n failing it may still yield a
#       passer, because Gamma is conservative by ~0.6-0.9 bits (the sibling's NC-A).
#       That count is reported too; it is not a soundness violation.
nc3a_tested = nc3a_viol = 0
nc3b_tested = nc3b_survive = 0
nc3_passer_anyway = nc3_construction_fails = 0
for p in [16, 18, 20, 22, 24]:
    a, b = window_int_range(p)
    for n in range(a, min(b, a + 120) + 1):
        K, _, _ = delta_scaled(n)
        S = K - n
        if S < p or S - (p - 1) < 1:
            continue
        thresh = delta_bounds_from_gamma(gamma_demand(p, n))[0]   # exact per-(p,n) delta_hi
        if not delta_le(n, thresh):
            nc3a_tested += 1
            if hypothesis_ok(p, n):
                nc3a_viol += 1
        if delta_le(n, D_HI):
            continue
        nc3b_tested += 1
        if hypothesis_ok(p, n):
            nc3b_survive += 1
            continue
        built = construction_B(p, n)
        if built is None:
            nc3_construction_fails += 1
            continue
        Rs = rotation_numerators(built[0], built[1])
        if all(built[3] <= R for R in Rs):
            nc3_passer_anyway += 1
        else:
            nc3_construction_fails += 1
check("NC-3a: every n above the EXACT threshold f(Gamma(p,n)) fails Theorem B's (H1)",
      nc3a_viol == 0 and nc3a_tested > 0,
      "%d tested, %d violations" % (nc3a_tested, nc3a_viol))
check("NC-3b: above the uniform delta_hi the hypothesis is nearly always lost too",
      nc3b_tested > 0 and nc3b_survive * 20 < nc3b_tested,
      "%d n above delta_hi: %d still meet (H1) on the exact Gamma (the cost of using "
      "sup Gamma), %d lose it -- of those, %d then fail a size condition and %d still "
      "build a passer (Gamma's known ~0.6-0.9 bit conservativeness, not a soundness break)"
      % (nc3b_tested, nc3b_survive, nc3b_tested - nc3b_survive,
         nc3_construction_fails, nc3_passer_anyway))

# NC-4: the arc's LOWER cut is what forces the constant -- drop it and gamma blows up.
worst_one_sided = Fraction(0)
worst_at = None
for p in range(16, 41):
    a, b = window_int_range(p)
    for n in range(a, b + 1):
        if delta_le(n, D_HI):                     # one-sided (Lemma D) condition only
            glo, _ = gamma_bounds_of_n(n)
            if glo > worst_one_sided:
                worst_one_sided, worst_at = glo, (p, n)
            break
check("NC-4: without the lower cut, the FIRST Lemma-D witness has unbounded-looking gamma",
      worst_one_sided > C_CONST,
      "worst first-witness gamma = %s at (p,n) = %s -- exceeds C = %s"
      % (f2s(worst_one_sided, 3), worst_at, f2s(C_CONST, 4)))


# --------------------------------------------------------------------------
# PART 7 -- optimisation: how good can this method's constant get?
# --------------------------------------------------------------------------

head("PART 7 -- the optimal constant, and the sweep-step ladder")

print("  (a) fixed sweep step 5, canonical window kappa <= 1.05:")
print("      delta_hi = %s   theta = %s" % (f2s(D_HI), f2s(THETA_HI)))
print("      admissible delta_lo < delta_hi - theta = %s" % f2s(DLO_OPT))
for dl in [Fraction(4, 100), Fraction(415, 10000), Fraction(4175, 100000), DLO_OPT]:
    if dl > DLO_OPT:
        continue
    _g, ch = gamma_bounds_from_delta(dl, D_HI)
    tag = "  <-- infimum (not attained)" if dl == DLO_OPT else ""
    print("      delta_lo = %-12s ->  gamma <= %s%s" % (f2s(dl, 7), f2s(ch, 6), tag))

print("")
print("  (b) using the exact Gamma(p,n) instead of its supremum Gamma*:")
print("      p |  Gamma(p,n_max) | delta_hi(p) | best gamma bound | gain vs C")
print("     ---+-----------------+-------------+------------------+----------")
for p in [16, 20, 24, 30, 60, 200]:
    a, b = window_int_range(p)
    Ghi = iv_to_fractions(Gamma0_iv(p, b))[1] + ETA_CAP
    dh_lo, _ = delta_bounds_from_gamma(Ghi)
    dl_opt = dh_lo - THETA_HI
    _g, cbound = gamma_bounds_from_delta(dl_opt, dh_lo)
    print("      %3d | %15s | %11s | %16s | %s" %
          (p, f2s(Ghi, 6), f2s(dh_lo, 7), f2s(cbound, 6), f2s(C_OPT - cbound, 6)))
print("      -> Gamma INCREASES in p, so the exact Gamma helps at SMALL p and not at large p;")
print("         the whole gain is ~0.04 bits at p = 16 and vanishes asymptotically.")

print("")
print("  (c) the refinement ladder.  Lengthening the SAME step-5 sweep past J*theta > 1")
print("      refines the grid (three-distance), so its maximal gap falls below theta and")
print("      the arc may be shortened to match -- a smaller gamma for a longer window,")
print("      hence a larger p_0.  This is the whole trade-off the method offers.")
print("      sweep J | integers | maximal gap  | delta_lo     | gamma bound | p_0")
print("     ---------+----------+--------------+--------------+-------------+----")


def gap_ladder(Jmax):
    """(J, maxgap) at every J where the maximal gap of {j*theta mod 1} strictly drops."""
    import bisect
    from collections import Counter
    th = THETA_HI
    pts = [Fraction(0), Fraction(1)]           # 1 as the wrap sentinel
    gaps = Counter({Fraction(1): 1})
    out = []
    cur = Fraction(1)
    for J in range(1, Jmax + 1):
        x = (J * th) % 1
        i = bisect.bisect_left(pts, x)
        lo, hi = pts[i - 1], pts[i]
        gaps[hi - lo] -= 1
        if gaps[hi - lo] == 0:
            del gaps[hi - lo]
        gaps[x - lo] += 1
        gaps[hi - x] += 1
        pts.insert(i, x)
        mg = max(gaps)
        if mg < cur:
            cur = mg
            out.append((J, mg))
    return out


ladder_rows = []
for J, g in gap_ladder(16000):
    if g >= D_HI:
        continue
    dl = D_HI - g
    if dl <= 0:
        continue
    _gg, cb = gamma_bounds_from_delta(dl, D_HI)
    need = 5 * J + 1
    p0 = None
    for p in range(2, 200):
        aa, bb = window_int_range(p)
        if bb - aa + 1 >= need:
            p0 = p
            break
    ladder_rows.append((J, need, g, dl, cb, p0))
# print the first row that reaches each successive constant, not all 138 rows
THRESH = [Fraction(13, 2), Fraction(26, 5), Fraction(9, 2), Fraction(4, 1),
          Fraction(39, 10), Fraction(19, 5), Fraction(37, 10), Fraction(369, 100),
          Fraction(3685, 1000), Fraction(3684, 1000)]
seen = set()
for (J, need, g, dl, cb, p0) in ladder_rows:
    tag = next((t for t in THRESH if cb <= t and t not in seen), None)
    if tag is None and J != ladder_rows[0][0]:
        continue
    seen.add(tag)
    print("      %7d | %8d | %s | %s | %11s | %3s" %
          (J, need, f2s(g, 10), f2s(dl, 10), f2s(cb, 6), str(p0)))
best = min(ladder_rows, key=lambda r: r[4])
check("ladder: the achieved gamma can be pushed to within 0.01 of the demand Gamma* "
      "at the cost of a larger p_0",
      best[4] - G_STAR < Fraction(1, 100),
      "best gamma bound %s vs Gamma* = %s, at J = %d (%d integers, p_0 = %s)"
      % (f2s(best[4], 6), f2s(G_STAR, 6), best[0], best[1], best[5]))

print("")
print("  (d) the true minimum gamma over ALL size-passers is a different question.")
print("      Recorded, not searched: over the window witnesses of Part 4 the achieved")
print("      gamma is bracketed in [Gamma*, C]; Gamma(p,n) itself is the demand, and no")
print("      profile of this shape can have gamma below Gamma(p,n) by Theorem B's (star).")
print("      12.8.3's own p = 6 record (84 size-passers) already shows the family is not")
print("      unique at a period; no search was launched (README stopping rules).")


# --------------------------------------------------------------------------
head("SUMMARY")
npass = sum(1 for _l, ok in CHECKS if ok)
for lab, ok in CHECKS:
    if not ok:
        print("  FAILED: " + lab)
print("  %d/%d checks passed." % (npass, len(CHECKS)))
print("")
print("  THEOREM (gate P1).  With L = log_2 3, theta = 8 - 5L, and")
print("      Gamma* = 1.05*L*(L-1) + 1/(L-1) + 1        (<= %s)" % f2s(G_STAR, 10))
print("      delta_hi = -log_2(1 - 2^-Gamma*)           (>= %s)" % f2s(D_HI, 10))
print("      delta_lo = 0.0415,  delta_hi - delta_lo = %s > theta = %s"
      % (f2s(ARC_LEN, 10), f2s(THETA_HI, 10)))
print("  among any %d consecutive integers there is an n with delta(n) in "
      "[delta_lo, delta_hi]," % WINDOW_INTEGERS)
print("  hence with  Gamma(p,n) < Gamma* <= gamma(n) <= %s.  The window" % f2s(C_CONST, 6))
print("  [L^p, 1.05 L^p] holds %d consecutive integers for every p >= 16, and (H0) holds"
      % WINDOW_INTEGERS)
print("  at every such n.  So Construction B yields, for every p >= 16, a period-p")
print("  size-passer with  %s <= gamma <= %s  --  gamma = O(1), proved."
      % (f2s(G_STAR, 4), f2s(C_CONST, 4)))
print("  3 <= p <= 15 by the explicit finite check above; p in {2,4} are outside")
print("  Construction B's reach (their canonical windows hold no integer).")
sys.exit(0 if npass == len(CHECKS) else 1)
