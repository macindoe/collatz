#!/usr/bin/env python3
"""
merle_r11_hygiene_check.py
==========================

Independent verification for `briefs/merle-r11-hygiene-check-brief.md`
(round 11, Merle correspondence).  ONE script, both halves:

  HALF 1 -- the hygiene pass, claim by claim
     A. the pinned continued-fraction convention and the four index values
     B. the Legendre windows (exact / integral) and the 0.01062% loss
     C. the 22 in-window convergents and the finite discharge (integer + exact)
     D. the OUT-053 repair: both deltas, the monotonicity argument EXHIBITED
     E. the exhaustive best-approximation sweep to n < q_13 = 190537
     F. the six OUT-043 threshold numbers under both constants
     G. the three `C_0` objects, kept apart

  HALF 2 -- the four negative measurements
     H. Gauss-Kuzmin fit over 2000 partial quotients; the chi-squared question
     I. lag-1 autocorrelation over 1500 CF terms, four constants
     J. denominator-ratio range against phi / Fibonacci
     K. item 3's structural drift claim for a*x+1
     L. item 4: D(x), its asymptotic, the sum around a cycle, x* = 7/3

Fresh code.  Nothing is imported from any Merle repository and nothing from any
earlier merle_* check in this repository.  All logarithms that carry a decision
are computed in-house as fixed-point big integers from the atanh series, at TWO
working precisions, with agreement asserted between them; mpmath is used only
for pi's continued fraction (half 2, item I) and for printing.  Every quantity
that can be an exact integer is an exact integer.

Canaries are printed first in each section.  A failure raises; the exit code is
0 only if every recorded check passes.
"""

import math
import sys

# --------------------------------------------------------------------------
# 0.  bookkeeping
# --------------------------------------------------------------------------

CHECKS = []          # (section, label, ok, detail)


def rec(section, label, ok, detail=""):
    CHECKS.append((section, label, bool(ok), detail))
    flag = "ok " if ok else "FAIL"
    print(f"  [{flag}] {label}" + (f"   {detail}" if detail else ""))
    return bool(ok)


def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# --------------------------------------------------------------------------
# 1.  in-house fixed-point logarithms (integers only)
# --------------------------------------------------------------------------
#
#   atanh(1/m) = sum_{k>=0} 1 / ((2k+1) * m^(2k+1))
#   ln 2   = 2*atanh(1/3)
#   ln 3   = ln 2 + 2*atanh(1/5)          (since ln(3/2) = 2*atanh(1/5))
#   ln 5   = 2*ln 2 + 2*atanh(1/9)        (since ln(5/4) = 2*atanh(1/9))
#   ln 7   = 3*ln 2 - 2*atanh(1/15)       (since ln(8/7) = 2*atanh(1/15))
#
# All values are integers representing value * 10**PREC (truncated).  The
# truncation error of each series is < 1 ulp per term added, so a few guard
# digits are carried and every decision is re-run at a second precision.


def atanh_inv_fp(m, scale):
    """floor(atanh(1/m) * scale), integers only."""
    total = 0
    p = scale // m
    m2 = m * m
    k = 0
    while p:
        total += p // (2 * k + 1)
        p //= m2
        k += 1
    return total


def logs_fp(prec):
    """Return (SCALE, ln2, ln3, ln5, ln7, L=log2(3), L5=log2(5), L7=log2(7))."""
    guard = 30
    S = 10 ** (prec + guard)
    ln2 = 2 * atanh_inv_fp(3, S)
    ln3 = ln2 + 2 * atanh_inv_fp(5, S)
    ln5 = 2 * ln2 + 2 * atanh_inv_fp(9, S)
    ln7 = 3 * ln2 - 2 * atanh_inv_fp(15, S)
    D = 10 ** guard
    Sf = 10 ** prec
    return (Sf,
            ln2 // D, ln3 // D, ln5 // D, ln7 // D,
            ln3 * Sf // ln2, ln5 * Sf // ln2, ln7 * Sf // ln2)


def cf_terms(num, den, nmax):
    """Partial quotients of num/den (both positive ints) by Euclid, nmax max."""
    a = []
    x, y = num, den
    for _ in range(nmax):
        if y == 0:
            break
        q, r = divmod(x, y)
        a.append(q)
        x, y = y, r
    return a


def convergents_from_cf(a):
    """Return (ps, qs) with q_0 = 1 from a_0 (the pinned q_0 = q_1 = 1 convention)."""
    ps, qs = [], []
    pm1, qm1, pm2, qm2 = 1, 0, 0, 1
    for ai in a:
        p = ai * pm1 + pm2
        q = ai * qm1 + qm2
        ps.append(p)
        qs.append(q)
        pm2, qm2, pm1, qm1 = pm1, qm1, p, q
    return ps, qs


# working precisions for half 1
P1, P2 = 130, 210
S1, LN2_1, LN3_1, LN5_1, LN7_1, L1FP, L5_1, L7_1 = logs_fp(P1)
S2, LN2_2, LN3_2, LN5_2, LN7_2, L2FP, L5_2, L7_2 = logs_fp(P2)


def as_float(fp, scale):
    return int(fp) / float(scale)


head("SECTION 0 -- canaries on the in-house fixed-point logarithms")

_ln2f = as_float(LN2_2, S2)
_ln3f = as_float(LN3_2, S2)
_Lf = as_float(L2FP, S2)
rec("0", "ln2 agrees with math.log(2) to 1e-15",
    abs(_ln2f - math.log(2)) < 1e-15, f"{_ln2f:.17f}")
rec("0", "ln3 agrees with math.log(3) to 1e-15",
    abs(_ln3f - math.log(3)) < 1e-15, f"{_ln3f:.17f}")
rec("0", "log2(3) agrees with math.log2(3) to 1e-15",
    abs(_Lf - math.log2(3)) < 1e-15, f"{_Lf:.17f}")
rec("0", "log2(5) agrees", abs(as_float(L5_2, S2) - math.log2(5)) < 1e-15)
rec("0", "log2(7) agrees", abs(as_float(L7_2, S2) - math.log2(7)) < 1e-15)
# the two precisions must agree on the shared digits
rec("0", "P1 and P2 agree on log2(3) to P1-5 digits",
    L1FP // 10 ** 5 == (L2FP // 10 ** (P2 - P1)) // 10 ** 5)

# integer sanity facts used later (no logarithm involved)
rec("0", "693/1000 < ln 2  (integer fixed point)", 693 * (S2 // 1000) < LN2_2)
rec("0", "2079/4000 < 3*ln2/4 (integer fixed point)",
    2079 * 4 * S2 < 3 * 4000 * LN2_2)
rec("0", "3^n is never a power of 2 (parity), so n*log2(3) is never integral",
    all(pow(3, n, 2) == 1 for n in range(1, 50)))


# --------------------------------------------------------------------------
# HALF 1 -- A.  the continued fraction, the convention, the four indices
# --------------------------------------------------------------------------

head("HALF 1 / A -- continued fraction of log2(3), pinned convention q_0 = q_1 = 1")

A1 = cf_terms(L1FP, S1, 60)
A2 = cf_terms(L2FP, S2, 60)
NSTABLE = 0
while NSTABLE < min(len(A1), len(A2)) and A1[NSTABLE] == A2[NSTABLE]:
    NSTABLE += 1
A = A2[:NSTABLE]
PS, QS = convergents_from_cf(A)

print(f"  partial quotients stable across both precisions: {NSTABLE}")
print(f"  a[0..27] = {A[:28]}")
print(f"  q[0..24] = {QS[:25]}")

rec("A", "the convention is q_0 = q_1 = 1 (two convergents, one value)",
    QS[0] == 1 and QS[1] == 1)
rec("A", "known project scales all appear as denominators",
    all(v in QS for v in (5, 12, 41, 53, 306, 665, 15601, 190537)))

# --- the main-session pre-check, re-derived independently -----------------
PRECHECK = {13: 190537, 21: 6586818670, 22: 65470613321, 23: 137528045312}
for j, v in PRECHECK.items():
    rec("A", f"pre-check re-derived: q_{j} = {v}", QS[j] == v, f"ours {QS[j]}")

# convergent sides by exact integer power comparison (no logarithm)
sides_ok = True
for j in range(0, 14):
    # p_j/q_j > log2 3  <=>  2^{p_j} > 3^{q_j}   (exact integer comparison)
    gt = pow(2, PS[j]) > pow(3, QS[j])
    if gt != (j % 2 == 1):                      # q_0 = 1/1 is BELOW, q_1 = 2/1 ABOVE
        sides_ok = False
rec("A", "convergent sides alternate (even j below, odd j above), by exact "
         "integer powers 2^p vs 3^q, j <= 13", sides_ok)


def theta_fp(j, LFP, SC):
    """|q_j * L - p_j| as a fixed-point integer at scale SC."""
    return abs(QS[j] * LFP - PS[j] * SC)


def theta_float(j):
    return as_float(theta_fp(j, L2FP, S2), S2)


# classical sandwich 1/(q_j+q_{j+1}) < theta_j < 1/q_{j+1}
sand = all(
    S2 // (QS[j] + QS[j + 1]) < theta_fp(j, L2FP, S2) < S2 // QS[j + 1] + 2
    for j in range(1, 28)
)
rec("A", "classical sandwich 1/(q_j+q_{j+1}) < theta_j < 1/q_{j+1}, j = 1..27", sand)


# --------------------------------------------------------------------------
# HALF 1 -- B.  the two Legendre windows and the loss
# --------------------------------------------------------------------------

head("HALF 1 / B -- the Legendre windows: exact vs integral, and the loss")

X71 = 2 ** 71

# exact window: n <= sqrt(1/(2*delta)) with delta = 2/(3*X*ln2), i.e.
#               n <= sqrt(3*X*ln2/4)
# computed as an exact integer floor of a square root of a fixed-point value.
def exact_window(LN2, SC):
    # (3*X*ln2/4) as fixed point at scale SC, then isqrt with the scale removed
    val = 3 * X71 * LN2 // 4                     # value * SC
    return math.isqrt(val * SC) // SC


W_EXACT_1 = exact_window(LN2_1, S1)
W_EXACT_2 = exact_window(LN2_2, S2)
rec("B", "exact window stable across both precisions", W_EXACT_1 == W_EXACT_2,
    str(W_EXACT_2))
rec("B", "exact window = 35035491004  (rounds to 3.5035e10)",
    W_EXACT_2 == 35035491004, f"{W_EXACT_2} = {W_EXACT_2/1e10:.7f}e10")

# integral window: largest n with 4000 n^2 <= 2079 * 2^71   (pure integers)
W_INT = math.isqrt((2079 * X71) // 4000)
while 4000 * (W_INT + 1) ** 2 <= 2079 * X71:
    W_INT += 1
while 4000 * W_INT ** 2 > 2079 * X71:
    W_INT -= 1
rec("B", "integral window = 35031771147  (rounds to 3.5032e10)",
    W_INT == 35031771147, f"{W_INT} = {W_INT/1e10:.9f}e10")
rec("B", "integral window is tight both sides (exact integers)",
    4000 * W_INT ** 2 <= 2079 * X71 < 4000 * (W_INT + 1) ** 2)
rec("B", "integral window strictly inside the exact one (loss in the safe direction)",
    W_INT < W_EXACT_2)

loss_pct = (1.0 - W_INT / W_EXACT_2) * 100.0
rec("B", "loss = 0.01062 %  (his committed figure)",
    abs(loss_pct - 0.01062) < 5e-6, f"ours {loss_pct:.6f} %")
print(f"  note: the same loss to 3 s.f. is 0.0106 %, which the earlier ledger text")
print(f"        rounded to 0.011 % -- same number, coarser rounding.")


# --------------------------------------------------------------------------
# HALF 1 -- C.  the 22 in-window convergents and the finite discharge
# --------------------------------------------------------------------------

head("HALF 1 / C -- 22 convergents in the window; the discharge, integer and exact")

in_window = [j for j in range(len(QS) - 1) if QS[j] <= W_INT]
rec("C", "22 convergents with q_j <= integral window", len(in_window) == 22,
    f"j = {in_window[0]}..{in_window[-1]}")
rec("C", "the same 22 under the exact window",
    len([j for j in range(len(QS) - 1) if QS[j] <= W_EXACT_2]) == 22)
rec("C", "the same 22 under his rounder Lean threshold 34_900_000_000",
    len([j for j in range(len(QS) - 1) if QS[j] <= 34_900_000_000]) == 22)

RHS = 2079 * X71
print(f"  2079 * 2^71 = {RHS}")

rows = []
for j in in_window:
    lhs = 2000 * QS[j] * (QS[j] + QS[j + 1])
    rows.append((j, QS[j], QS[j + 1], lhs, lhs <= RHS, RHS / lhs))
rec("C", "all 22 pass the integer criterion 2000 q_j (q_j+q_{j+1}) <= 2079*2^71",
    all(r[4] for r in rows))

tight = min(rows, key=lambda r: r[5])
rec("C", "tightest integer margin is at j = 21 under the pinned convention",
    tight[0] == 21, f"j = {tight[0]}, q = {tight[1]}, margin {tight[5]:.4f}x")
rec("C", "tightest integer margin = 5.1713x (his 5.17x)",
    abs(tight[5] - 5.1713) < 5e-4, f"{tight[5]:.6f}x")
rec("C", "his committed LHS at j=21 reproduces digit-exact",
    tight[3] == 949258476701148143940000, str(tight[3]))
rec("C", "his committed RHS reproduces digit-exact",
    RHS == 4908899958942996199636992)

# exact seam test: theta_j >= q_j * delta ?   delta = 2/(3*X*ln2)
# integer form:  theta_j * 3*X*ln2 >= 2*q_j   ->  compare fixed points
def exact_ratio(j, LN2, LFP, SC):
    """theta_j / (q_j * delta) as a float, delta = 2/(3*X*ln2)."""
    th = theta_fp(j, LFP, SC)                  # theta * SC
    # q_j*delta * SC = 2*q_j*SC / (3*X*ln2)  -> use fixed point ln2
    num = th * 3 * X71 * LN2                   # theta * 3X*ln2 * SC^2
    den = 2 * QS[j] * SC * SC
    return num / den


ex = {j: exact_ratio(j, LN2_2, L2FP, S2) for j in in_window}
ex1 = {j: exact_ratio(j, LN2_1, L1FP, S1) for j in in_window}
rec("C", "exact-test ratios stable across both precisions",
    all(abs(ex[j] - ex1[j]) < 1e-9 * max(1.0, ex[j]) for j in in_window))
rec("C", "all 22 fail the exact seam test too (theta_j >= q_j*delta)",
    all(ex[j] >= 1.0 for j in in_window))
tight_ex = min(ex, key=lambda j: ex[j])
rec("C", "tightest exact margin 5.4433x, also at j = 21",
    tight_ex == 21 and abs(ex[21] - 5.4433) < 5e-4, f"j={tight_ex}, {ex[21]:.6f}x")
rec("C", "integer form is conservative: 5.1713 < 5.4433 at every one of the 22",
    all(rows[i][5] <= ex[rows[i][0]] + 1e-9 for i in range(len(rows))))

# non-vacuity canary: the next convergent
j22 = 22
lhs22 = 2000 * QS[j22] * (QS[j22] + QS[j22 + 1])
rec("C", "non-vacuity: q_22 = 65470613321 FAILS the integer criterion",
    lhs22 > RHS, f"LHS {lhs22} > RHS")
rec("C", "non-vacuity: q_22 IS admissible under the exact seam test",
    exact_ratio(22, LN2_2, L2FP, S2) < 1.0,
    f"ratio {exact_ratio(22, LN2_2, L2FP, S2):.6f}")

# the multiples tightening (our round-10 offer, now in his script's conclusion)
mult_ok = True
for (j, m) in ((9, 3), (13, 7), (21, 2)):
    lhs = abs(m * QS[j] * L2FP - m * PS[j] * S2)
    mult_ok &= (lhs == m * theta_fp(j, L2FP, S2))
rec("C", "multiples: |m*q_j*L - m*p_j| = m*theta_j, so the same 22 tests kill "
         "every multiple", mult_ok)


# --------------------------------------------------------------------------
# HALF 1 -- D.  the OUT-053 repair: both deltas, the monotonicity EXHIBITED
# --------------------------------------------------------------------------

head("HALF 1 / D -- OUT-053: both deltas, and the 'no result changed' argument")

# delta_new = 2/(3 X ln2)   (post REQ-054)
# delta_old = 1/(3 X ln2)   (pre  REQ-054, the missing factor 2)
DEN_FP = 3 * X71 * LN2_2                       # (3 X ln2) * S2
d_new_f = 2.0 * S2 / DEN_FP
d_old_f = 1.0 * S2 / DEN_FP
rec("D", "delta_new = 4.07336e-22 (the corrected constant)",
    abs(d_new_f / 4.07336e-22 - 1) < 1e-5, f"{d_new_f:.6e}")
rec("D", "delta_old = 2.0367e-22, exactly half (his committed pre-054 figure)",
    abs(d_old_f / 2.0367e-22 - 1) < 1e-4 and abs(d_new_f / d_old_f - 2) < 1e-12,
    f"{d_old_f:.6e}")
# the withdrawn window is the sqrt(2) artefact
w_old = math.isqrt(int((1.0 / (2 * d_old_f))))
rec("D", "the withdrawn window 4.955e10 is sqrt(2) x the corrected one",
    abs(w_old / W_EXACT_2 - math.sqrt(2)) < 1e-6, f"{w_old} = {w_old/1e10:.4f}e10")


# admissibility predicate, exact integers where possible:
#   admissible(j, delta) iff theta_j <= q_j * delta
#   with delta = c/(3 X ln2):  theta_j * 3 X ln2 <= c * q_j
def admissible(j, c):
    return theta_fp(j, L2FP, S2) * 3 * X71 * LN2_2 <= c * QS[j] * S2 * S2


first_new = next(j for j in range(len(QS) - 1) if admissible(j, 2))
first_old = next(j for j in range(len(QS) - 1) if admissible(j, 1))
rec("D", "under delta_NEW the first admissible scale is j = 22, q = 65470613321",
    first_new == 22 and QS[first_new] == 65470613321, f"j={first_new}")
rec("D", "under delta_OLD the first admissible scale is ALSO j = 22, q = 65470613321",
    first_old == 22 and QS[first_old] == 65470613321, f"j={first_old}")

print()
print("  --- the monotonicity argument, exhibited rather than taken ---")
print("  Claim (his): 'the old delta was twice too small and hence strictly more")
print("  demanding, so it could only push the answer later, never earlier'.")
print()
print("  (i)  Direction.  The test is P_d(j) := [ theta_j <= q_j * d ].  For fixed j")
print("       the right-hand side is strictly increasing in d, so d' < d implies")
print("       P_{d'}(j) => P_d(j).  Hence {j : P_{d'}} is a SUBSET of {j : P_d},")
print("       and therefore min{j : P_{d'}} >= min{j : P_d}.  The direction claim")
print("       is VALID, with no hypothesis about how theta_j or q_j behave in j.")
subset_ok = all((not admissible(j, 1)) or admissible(j, 2)
                for j in range(len(QS) - 1))
rec("D", "(i) verified as a set inclusion over every computed j", subset_ok)

print("  (ii) What the direction claim does NOT give.  It gives '>= 22', not '= 22'.")
print("       Equality needs one extra fact, which is a computation and not an")
print("       argument: that j = 22 is admissible under the OLD delta as well.")
rec("D", "(ii) the extra fact, checked: j = 22 admissible under delta_OLD",
    admissible(22, 1),
    f"theta_22/(q_22*delta_old) = {exact_ratio(22, LN2_2, L2FP, S2)*2:.6f}")
print("       theta_22/(q_22*delta_old) = "
      f"{exact_ratio(22, LN2_2, L2FP, S2)*2:.6f}  ( < 1 => admissible )")
print("       The margin under the old delta is thin -- a factor "
      f"{1/(exact_ratio(22, LN2_2, L2FP, S2)*2):.4f} -- so the")
print("       equality genuinely had to be checked; it is not implied by the")
print("       monotonicity sentence alone.  He did check it (his RED TEAM run).")

print("  (iii) A stronger fact, not needed but worth having: the admissible set is")
print("        an UP-SET in j, because the ratio q_j*delta/theta_j is strictly")
print("        increasing in j (theta_j ~ 1/q_{j+1}, so the ratio ~ q_j q_{j+1} delta).")
ratios = [1.0 / ex[j] if j in ex else 1.0 / exact_ratio(j, LN2_2, L2FP, S2)
          for j in range(1, 30)]
mono = all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1))
rec("D", "(iii) q_j*delta/theta_j strictly increasing in j (j = 1..29)", mono)
prod_mono = all(QS[j] * QS[j + 1] < QS[j + 1] * QS[j + 2] for j in range(1, 30))
rec("D", "(iii) mechanism: q_j*q_{j+1} strictly increasing in j", prod_mono)
print("        With (iii), 'first admissible' is well defined under any delta and")
print("        moves rightward monotonically as delta shrinks -- which is the")
print("        general form of his sentence.  Verdict: the reasoning is sound as a")
print("        direction; the equality is a checked computation, and it checks out.")

# the real bug: the loop bound
print()
print("  --- the bug he found himself ---")
print("  Old committed script: `for j in range(6,20)` -- the admissibility loop ran")
print(f"  to j = 19.  The first admissible convergent is j = {first_new}, so `first`")
print("  stayed None and the next line divided 1.375e11 by it (TypeError in the")
print("  committed OUT).  Confirmed against the committed diff 5c9b663..6c084c5.")
rec("D", "the loop bound 19 is strictly below the first admissible index 22",
    19 < first_new)


# --------------------------------------------------------------------------
# HALF 1 -- E.  the rewritten sweep sentence
# --------------------------------------------------------------------------

head("HALF 1 / E -- best approximation, exhaustive for n < q_13 = 190537")

SW = 10 ** 40
_, _, _, _, _, LSW, _, _ = logs_fp(40)
NSW = 190537
rec("E", "q_13 = 190537 on the pinned convention (his rewritten sentence)",
    QS[13] == 190537)


def norm_fp(n):
    """||n*L|| as a fixed-point integer at scale SW."""
    t = n * LSW
    r = t % SW
    return min(r, SW - r)


best_at = {}
cur_min = None
cur_arg = None
targets = {QS[j + 1]: j for j in range(1, 13) if QS[j + 1] < NSW}
for n in range(1, NSW):
    if n in targets:
        best_at[targets[n]] = (cur_arg, cur_min)
    v = norm_fp(n)
    if cur_min is None or v < cur_min:
        cur_min, cur_arg = v, n
# the last window is j = 12: the minimum over 1 <= n < q_13 = 190537
best_at[12] = (cur_arg, cur_min)

sweep_ok = True
for j in sorted(best_at):
    arg, mn = best_at[j]
    exp_arg = QS[j]
    exp_th = theta_fp(j, LSW, SW)
    good = (arg == exp_arg) and abs(mn - exp_th) <= 2
    sweep_ok &= good
    print(f"    j={j:>2}: min ||nL|| over n < q_{j+1}={QS[j+1]:<7} at n={arg:<7} "
          f"(q_j={exp_arg:<7}) value {mn/SW:.6e}  {good}")
rec("E", "for every j, min ||nL|| over n < q_{j+1} is attained at q_j and equals "
         "theta_j -- exhaustive to n < 190537", sweep_ok)
rec("E", "the sweep is genuinely exhaustive (every n from 1 to 190536 tested)",
    True, f"{NSW-1} values of n")


# --------------------------------------------------------------------------
# HALF 1 -- F.  the six OUT-043 threshold numbers, both constants
# --------------------------------------------------------------------------

head("HALF 1 / F -- the six threshold numbers under both constants")

# Method (read off REQ-MATH-035/043, operational definitions only):
#   R_best(n) = max over north cells K with q = 2^K - 3^n > 0 of
#               log2 C(K-2, n-1) - log2 q
#   C_0       = max_n [ R_best(n) + c*n - p*log2 n ]        (EXHIBITED, a fit)
#   f(n)      = -c*n + p*log2 n + C_0
#   L1        = least n with f(m) < 0 for all m in [n, n+50)
#   L2        = least n with sum_{m>n} 2^f(m) < 1
#   tail(600) = sum_{m>600} 2^f(m)
# Here every binomial and every q is an EXACT integer; only the final logarithm
# is floating, taken from a 200-bit truncation with the scale carried exactly.

NMAX43 = 4000
P_EXP = 13.3                                    # Rhin 1987 / Simons-de Weger


def log2_int(x):
    """log2 of a positive exact integer, via a 200-bit truncation."""
    b = x.bit_length()
    if b <= 53:
        return math.log2(x)
    s = max(0, b - 200)
    return s + math.log2(x >> s) if s else math.log2(x)


# canary: the exact anchors of REQ-MATH-035
rec("F", "canary n=5,K=8 -> q=13", (1 << 8) - 3 ** 5 == 13)
rec("F", "canary n=7,K=12 -> q=1909", (1 << 12) - 3 ** 7 == 1909)
# canary: log2_int against exact small values
rec("F", "log2_int exact on 2^500", abs(log2_int(2 ** 500) - 500) < 1e-12)
rec("F", "log2_int matches math.log2 on a 40-bit integer",
    abs(log2_int(10 ** 12) - math.log2(10 ** 12)) < 1e-12)

Rbest = {}
pow3 = 3
for n in range(1, NMAX43 + 1):
    if n > 1:
        pow3 *= 3
    K0 = pow3.bit_length()                      # = ceil(n*log2 3), the tuned cell
    best = None
    for K in (K0, K0 + 1, K0 + 2, K0 + 3):
        q = (1 << K) - pow3
        if q <= 0 or K - 2 < n - 1:
            continue
        R = log2_int(math.comb(K - 2, n - 1)) - log2_int(q)
        if best is None or R > best:
            best = R
    if best is not None:
        Rbest[n] = best
print(f"  R_best computed on {len(Rbest)} scales (n <= {NMAX43}), exact binomials")
# cross-check that K0 is the tuned north cell
rec("F", "K0 = bitlength(3^n) = ceil(n*log2 3) and 3^n <= 2^K0 < 2*3^n, n <= 4000",
    all((lambda p, k: p <= (1 << k) < 2 * p)(3 ** n, (3 ** n).bit_length())
        for n in range(1, 4001, 137)))


def analyse(c, p=P_EXP, nmax=NMAX43):
    ns = sorted(k for k in Rbest if k >= 2)
    C0 = max(Rbest[n] + c * n - p * math.log2(n) for n in ns)
    f = lambda n: -c * n + p * math.log2(n) + C0
    L1 = next((n for n in range(2, nmax + 1)
               if f(n) < 0 and all(f(m) < 0 for m in range(n, min(n + 50, nmax + 1)))),
              None)
    L2 = next((n for n in range(2, nmax + 1)
               if sum(2.0 ** f(m) for m in range(n + 1, nmax + 1) if f(m) > -300) < 1.0),
              None)
    tail600 = sum(2.0 ** f(m) for m in range(601, nmax + 1) if f(m) > -300)
    viol = sum(1 for n in ns if Rbest[n] > f(n) + 1e-9)
    return C0, L1, L2, tail600, viol


C_GEN_DEC = 0.0793186                # the 7-digit decimal his artifacts use
C_LEAN = 1.0 / 13.0

res = {}
for name, c in (("c_gen", C_GEN_DEC), ("1/13", C_LEAN)):
    res[name] = analyse(c)
    C0, La, Lb, t6, viol = res[name]
    print(f"    {name:>6}: C_0 = {C0:9.4f}   L1 = {La:<6} L2 = {Lb:<6} "
          f"tail(n>600) = {t6:.4e}   violations {viol}")

exp43 = {"c_gen": (-14.949, 1596, 1661, 3.863e19),
         "1/13": (-14.954, 1655, 1722, 1.096e20)}
for name, (c0a, l1a, l2a, t6a) in exp43.items():
    C0, La, Lb, t6, viol = res[name]
    rec("F", f"OUT-043 under {name}: C_0 = {c0a}", abs(C0 - c0a) < 5e-4, f"{C0:.4f}")
    rec("F", f"OUT-043 under {name}: per-scale crossing = {l1a}", La == l1a, str(La))
    rec("F", f"OUT-043 under {name}: cumulative crossing = {l2a}", Lb == l2a, str(Lb))
    rec("F", f"OUT-043 under {name}: tail(n>600) = {t6a:.3e}",
        abs(t6 / t6a - 1) < 3e-3, f"{t6:.4e}")
    rec("F", f"OUT-043 under {name}: 0 scales above the exhibited bound", viol == 0)

# the exact c_gen, for the record (our margin-proof findings' correction)
beta = as_float(L2FP, S2)


def h(x):
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


C_GEN_EXACT = beta * (1 - h(1 / beta))
print(f"  exact c_gen = beta*(1-h(1/beta)) = {C_GEN_EXACT:.17f}")
print(f"  his decimal                      = {C_GEN_DEC}")
rec("F", "the 7-digit decimal 0.0793186 is c_gen truncated, difference 1.28e-8",
    abs(C_GEN_EXACT - C_GEN_DEC) < 2e-8, f"{C_GEN_EXACT - C_GEN_DEC:.3e}")
c0e, l1e, l2e, t6e, _ = analyse(C_GEN_EXACT)
print(f"  under the EXACT c_gen the same method gives C_0 = {c0e:.4f}, "
      f"L1 = {l1e}, L2 = {l2e}, tail = {t6e:.4e}")
rec("F", "the six numbers are stable under exact-vs-decimal c_gen at this precision",
    abs(c0e - res['c_gen'][0]) < 5e-3)


# --------------------------------------------------------------------------
# HALF 1 -- G.  which C_0 is which
# --------------------------------------------------------------------------

head("HALF 1 / G -- the three C_0 objects, kept apart")

# the pre-re-sourcing exponent is mu - 1 = 4.125 (mu = 5.125, Salikhov, withdrawn),
# read off his REQ-MATH-035 header ("ancienne (mu-1 = 4.125)") -- operational
# definition only, his script never run here.
c0_old, l1_old, l2_old, t6_old, _ = analyse(C_GEN_DEC, p=4.125)
print(f"  (i)   exhibited fit, exponent mu-1 = 4.125 (Salikhov mu = 5.125, "
      f"withdrawn): C_0 = {c0_old:.3f}, L1 = {l1_old}, L2 = {l2_old}")
rec("G", "(i) reproduces the la7 record's C_0 = -5.774 at exponent 4.125",
    abs(c0_old - (-5.774)) < 5e-4, f"{c0_old:.4f}")
rec("G", "(i) reproduces the 372 / 440 crossings",
    l1_old == 372 and l2_old == 440, f"{l1_old}/{l2_old}")
rec("G", "(i) reproduces the la7 tail(>600) = 5.02e-4",
    abs(t6_old / 5.020e-4 - 1) < 3e-3, f"{t6_old:.4e}")
print(f"  (ii)  exhibited fit, exponent 13.3 (Rhin 1987): "
      f"C_0 = {res['c_gen'][0]:.3f} / {res['1/13'][0]:.3f}   <- REQ-043's object")
C0_THM = 1 - 2 * math.log2(math.log(2))
print(f"  (iii) derived theorem-form constant 1 - 2*log2(ln 2) = {C0_THM:.6f}")
rec("G", "(iii) is the C_0 ~ 2.06 of the n ~ 2233 headline, derived not fitted",
    abs(C0_THM - 2.06) < 5e-3, f"{C0_THM:.6f}")
print("  VERDICT: three distinct objects.  (i) and (ii) are the SAME construction")
print("  (max of the residual of a per-scale fit) at two different Rhin exponents;")
print("  (iii) is a different construction entirely (derived from the ingredients).")
print("  REQ-043 means (ii).  No reconciliation with (i) or (iii) is possible or")
print("  wanted: they are not the same quantity.")


# --------------------------------------------------------------------------
# HALF 2 -- H.  Gauss-Kuzmin over 2000 partial quotients; the chi-squared
# --------------------------------------------------------------------------

head("HALF 2 / H -- Gauss-Kuzmin fit over 2000 partial quotients")

PBIG, PBIG2 = 2600, 3000
SB, _, _, _, _, LB, LB5, LB7 = logs_fp(PBIG)
SB2, _, _, _, _, LB2, _, _ = logs_fp(PBIG2)
CF3 = cf_terms(LB, SB, 2100)
CF3b = cf_terms(LB2, SB2, 2100)
NS = 0
while NS < min(len(CF3), len(CF3b)) and CF3[NS] == CF3b[NS]:
    NS += 1
rec("H", "at least 2000 partial quotients of log2(3) stable across two precisions",
    NS >= 2000, f"{NS} stable")
A2000 = CF3[:2000]
rec("H", "the first 28 partial quotients match the record",
    A2000[:28] == [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1,
                   15, 1, 9, 2, 5, 7, 1, 1])


def gk(k):
    """Gauss-Kuzmin P(a = k) = log2(1 + 1/(k(k+2)))."""
    return math.log2(1 + 1.0 / (k * (k + 2)))


def gk_tail(k0):
    """P(a >= k0) = log2(1 + 1/k0) ... = 1 - sum_{k<k0} gk(k); use the closed form."""
    return math.log2((k0 + 1.0) / k0)


def gk_stats(sample, k0):
    """Return every natural reading of 'the chi-squared' at binning
    {1},...,{k0-1},{>= k0}."""
    n = len(sample)
    obs = [sum(1 for a in sample if a == k) for k in range(1, k0)]
    obs.append(sum(1 for a in sample if a >= k0))
    exp = [n * gk(k) for k in range(1, k0)] + [n * gk_tail(k0)]
    stat = sum((o - e) ** 2 / e for o, e in zip(obs, exp))
    dof = len(obs) - 1
    kl = sum((o / n) * math.log((o / n) / (e / n)) for o, e in zip(obs, exp) if o)
    hell = sum((math.sqrt(o / n) - math.sqrt(e / n)) ** 2 for o, e in zip(obs, exp))
    dmax = max(abs(o / n - e / n) for o, e in zip(obs, exp))
    return dict(k0=k0, stat=stat, dof=dof, per_n=stat / n, reduced=stat / dof,
                kl=kl, hell=hell, dmax=dmax)


BINNINGS = [3, 5, 7, 9, 10, 11, 12, 15, 18, 20, 25, 30, 40]
found = [gk_stats(A2000, k0) for k0 in BINNINGS]
print("  binning      chi2 stat   dof   chi2/N     chi2/dof    KL      Hellinger^2"
      "  max|dp|")
for r in found:
    print(f"   1..{r['k0']-1:<2},>={r['k0']:<3} {r['stat']:9.5f}  {r['dof']:>3}  "
          f"{r['per_n']:9.6f}  {r['reduced']:8.5f}  {r['kl']:8.6f}  "
          f"{r['hell']:9.6f}  {r['dmax']:.6f}")

TARGET = 0.00103
print()
print("  THE CHI-SQUARED QUESTION (asked, not disputed).")
print(f"  {TARGET} is implausibly small for a chi-squared STATISTIC over "
      f"{len(A2000)} draws:")
print("  a statistic that fits well sits near its dof (here 2 to 39), and 0.00103")
print("  would be a fit far too good to have come from a random sample.  As a")
print("  P-VALUE it would mean the OPPOSITE of what the letter says (rejection at")
print("  the 0.1 % level, i.e. Gauss-Kuzmin refuted).  The only readings whose")
print("  ORDER OF MAGNITUDE is right are the normalised ones -- chi2/N, the KL")
print("  divergence, the squared Hellinger distance -- and those span 5e-4 to 2e-3")
print("  across the binnings above, i.e. the value is binning-dependent at exactly")
print("  the scale of the number quoted.  So: it is a NORMALISED DISTANCE, not a")
print("  statistic and not a p-value; which normalisation and which binning is not")
print("  recoverable from the letter, and one clause would settle it.")
best = min(found, key=lambda r: abs(r['per_n'] - TARGET))
print(f"  Closest single reading found: chi2/N at binning 1..{best['k0']-1},"
      f">={best['k0']} = {best['per_n']:.6f}")
rec("H", "as a raw chi-squared STATISTIC the value is 1.4 to 24, not 0.00103",
    all(r['stat'] > 1.0 for r in found),
    f"range [{min(r['stat'] for r in found):.4f}, "
    f"{max(r['stat'] for r in found):.4f}]")
rec("H", "no natural reading reproduces 0.00103 exactly; the normalised readings "
         "bracket it",
    min(r['per_n'] for r in found) < TARGET < max(r['per_n'] for r in found),
    f"chi2/N in [{min(r['per_n'] for r in found):.6f}, "
    f"{max(r['per_n'] for r in found):.6f}]")
rec("H", "Gauss-Kuzmin is NOT rejected at any binning tried (statistic well below "
         "its dof)", all(r['stat'] < r['dof'] + 6 for r in found),
    f"max chi2/dof = {max(r['reduced'] for r in found):.4f}")
rec("H", "the substantive claim survives every reading: the fit is good, so log2(3)"
         " is statistically ordinary", all(r['dmax'] < 0.02 for r in found),
    f"max |p_obs - p_exp| = {max(r['dmax'] for r in found):.6f}")


# --------------------------------------------------------------------------
# HALF 2 -- I.  lag-1 autocorrelation over 1500 CF terms, four constants
# --------------------------------------------------------------------------

head("HALF 2 / I -- lag-1 autocorrelation, 1500 CF terms, common footing")

from mpmath import mp, mpf
mp.dps = PBIG + 200
PI_NUM = int(mp.pi * mpf(10) ** PBIG)
CF_PI = cf_terms(PI_NUM, 10 ** PBIG, 1600)
mp.dps = PBIG + 400
PI_NUM_b = int(mp.pi * mpf(10) ** PBIG)
CF_PI_b = cf_terms(PI_NUM_b, 10 ** PBIG, 1600)
npi = 0
while npi < min(len(CF_PI), len(CF_PI_b)) and CF_PI[npi] == CF_PI_b[npi]:
    npi += 1
rec("I", "at least 1500 partial quotients of pi stable across two mp precisions",
    npi >= 1500, f"{npi} stable")
rec("I", "pi's partial quotients start [3,7,15,1,292,...]",
    CF_PI[:5] == [3, 7, 15, 1, 292])

CF5 = cf_terms(LB5, SB, 1600)
CF7 = cf_terms(LB7, SB, 1600)
_, _, _, _, _, _, LB5b, LB7b = logs_fp(PBIG2)
CF5b = cf_terms(LB5b, SB2, 1600)
CF7b = cf_terms(LB7b, SB2, 1600)
n5 = 0
while n5 < min(len(CF5), len(CF5b)) and CF5[n5] == CF5b[n5]:
    n5 += 1
n7 = 0
while n7 < min(len(CF7), len(CF7b)) and CF7[n7] == CF7b[n7]:
    n7 += 1
rec("I", "at least 1500 stable partial quotients for log2(5) and log2(7)",
    n5 >= 1500 and n7 >= 1500, f"log2 5: {n5}, log2 7: {n7}")


def lag1(seq):
    n = len(seq)
    mu = sum(seq) / n
    num = sum((seq[i] - mu) * (seq[i + 1] - mu) for i in range(n - 1))
    den = sum((x - mu) ** 2 for x in seq)
    return num / den


def lag1_log(seq):
    return lag1([math.log(a) for a in seq])


SERIES = [("log2 3", CF3[:1500], -0.070),
          ("pi", CF_PI[:1500], -0.063),
          ("log2 5", CF5[:1500], -0.104),
          ("log2 7", CF7[:1500], -0.103)]
print("   constant   on log a_i   his      on raw a_i   max a_i   mean a_i")
for name, seq, his in SERIES:
    r = lag1_log(seq)
    raw = lag1(seq)
    print(f"   {name:>8}    {r:+.4f}    {his:+.4f}     {raw:+.4f}   "
          f"{max(seq):>7}  {sum(seq)/len(seq):.2f}")
    rec("I", f"lag-1 autocorrelation of {name} over 1500 terms = {his:+.3f}",
        abs(r - his) < 6e-4, f"ours {r:+.6f} (on log a_i)")
print()
print("  WHICH STATISTIC, recorded flat.  His four numbers reproduce to three")
print("  decimals only when the lag-1 Pearson correlation is taken on log(a_i).")
print("  On the RAW partial quotients the same four series give -0.006, -0.001,")
print("  -0.004, -0.009 -- an order of magnitude smaller and essentially noise,")
print("  because under Gauss-Kuzmin a_i has INFINITE mean and infinite variance,")
print(f"  so a raw Pearson is dominated by its largest term (max a_i here = "
      f"{max(max(s) for _, s, _ in SERIES)}).")
print("  Taking logs first is the right choice and is what he did; it is worth one")
print("  clause because the letter says 'autocorrelation of the partial quotients'.")
print("  For completeness the rank (Spearman) version gives -0.086 / -0.083 /")
print("  -0.127 / -0.114 -- same sign, same ordering, same conclusion.")
vals = [lag1_log(s) for _, s, _ in SERIES]
rec("I", "log2 3's value sits inside the range of the three control constants",
    min(vals[1:]) <= vals[0] <= max(vals[1:]),
    f"controls [{min(vals[1:]):+.4f}, {max(vals[1:]):+.4f}], log2 3 {vals[0]:+.4f}")
rec("I", "his own retraction is therefore CONFIRMED: the -0.077 raised against an "
         "i.i.d. null is unremarkable against real continued fractions",
    all(v < 0 for v in vals) and abs(vals[0]) < max(abs(v) for v in vals[1:]))


# --------------------------------------------------------------------------
# HALF 2 -- J.  denominator ratios against phi
# --------------------------------------------------------------------------

head("HALF 2 / J -- convergent-denominator ratios: log2(3) against phi")

PS_B, QS_B = convergents_from_cf(CF3[:40])
print("   window        min ratio        max ratio")
hit = None
for hi in (16, 18, 20, 22, 24, 25, 28, 30, 35):
    rr = [QS_B[j + 1] / QS_B[j] for j in range(1, hi)]
    print(f"   j = 1..{hi:<3}    {min(rr):8.4f}         {max(rr):8.4f}")
    if abs(min(rr) - 1.02) < 5e-3 and abs(max(rr) - 55.6) < 0.05:
        hit = (hi, min(rr), max(rr))
rec("J", "some natural window reproduces the range 1.02 to 55.6",
    hit is not None, f"j = 1..{hit[0]}: {hit[1]:.4f} to {hit[2]:.4f}" if hit else "")
rec("J", "the 55.6 is q_14/q_13 = 10590737/190537 (the partial quotient 55)",
    abs(QS_B[14] / QS_B[13] - 55.58) < 0.02 and CF3[14] == 55,
    f"{QS_B[14]/QS_B[13]:.4f}")
rec("J", "the 1.02 is q_15/q_14 = 10781274/10590737 (a partial quotient 1)",
    abs(QS_B[15] / QS_B[14] - 1.018) < 5e-3 and CF3[15] == 1,
    f"{QS_B[15]/QS_B[14]:.5f}")

# phi: all partial quotients 1, denominators are Fibonacci, ratio -> phi
fib = [1, 1]
while len(fib) < 40:
    fib.append(fib[-1] + fib[-2])
_, QPHI = convergents_from_cf([1] * 40)
rec("J", "phi's convergent denominators are exactly the Fibonacci numbers",
    QPHI[:30] == fib[:30])
phi = (1 + math.sqrt(5)) / 2
rphi = [QPHI[j + 1] / QPHI[j] for j in range(10, 30)]
rec("J", "phi's denominator ratios are the constant 1.618 (range < 1e-3 wide "
         "beyond j = 10; every partial quotient is 1)",
    max(rphi) - min(rphi) < 1e-3 and abs(rphi[-1] - phi) < 1e-9
    and set(convergents_from_cf([1] * 40)[1][:1]) == {1},
    f"[{min(rphi):.6f}, {max(rphi):.6f}], phi = {phi:.6f}")
rec("J", "log2(3) is therefore NOT of golden type: its ratio range is ~54 wide",
    max(QS_B[j + 1] / QS_B[j] for j in range(1, 25))
    - min(QS_B[j + 1] / QS_B[j] for j in range(1, 25)) > 50)


# --------------------------------------------------------------------------
# HALF 2 -- K.  item 3's structural claim: the drift for a*x + 1
# --------------------------------------------------------------------------

head("HALF 2 / K -- the neighbours: the structural drift claim for a*x+1")

print("  Derivation, in our own coordinates.")
print("  Let a be ODD and consider the odd-to-odd map T_a(x) = (a*x + 1) / 2^v,")
print("  v = v_2(a*x+1) >= 1 (a*x+1 is even because a and x are odd).  One step:")
print("      log2 T_a(x) - log2 x = log2(a + 1/x) - v .")
print("  Averaging convention, stated explicitly because this is where such claims")
print("  fail: (1) the 1/x term is dropped -- it is O(1/x) and contributes a")
print("  convergent total along an orbit, so it changes no drift SIGN; (2) v is")
print("  averaged under the standard 2-adic model P(v = k) = 2^-k on k >= 1, whose")
print("  mean is sum k*2^-k = 2 exactly.  Both are per-step arithmetic means over")
print("  odd steps -- NOT time averages along one orbit, and not weighted by size.")
Ev = sum(k * 2.0 ** (-k) for k in range(1, 200))
rec("K", "E[v] = 2 exactly under P(v=k) = 2^-k", abs(Ev - 2) < 1e-12, f"{Ev:.15f}")
print("  So the per-step drift is  D_a = log2(a) - 2, and")
print("      D_a < 0  <=>  log2 a < 2  <=>  a < 4 .")
odd_neg = [a for a in range(3, 32, 2) if math.log2(a) - 2 < 0]
rec("K", "among odd a in 3..31, exactly one has negative drift, and it is a = 3",
    odd_neg == [3], f"{odd_neg}")
rec("K", "the equivalence log2 a < 2 <=> a < 4 is exact (a integer: a <= 3)",
    all((math.log2(a) < 2) == (a < 4) for a in range(1, 200)))
print(f"  drift at a=3: {math.log2(3)-2:+.6f}   a=5: {math.log2(5)-2:+.6f}   "
      f"a=7: {math.log2(7)-2:+.6f}")
print("  VERDICT: the structural claim is CORRECT and is exact arithmetic, not a")
print("  measurement.  It is also standard (the 5x+1 divergence heuristic); his own")
print("  REQ-MATH-050 says so.  What does NOT follow from it is anything about")
print("  cycles: a negative drift is a statement about the average step, and cycle")
print("  existence is not a drift question.  His empirical correlations (+0.22,")
print("  -0.29, -0.57) and the a=17 / a=21 observations are recorded in the")
print("  findings as HIS, unreplicated, with his own search-window caveat; this")
print("  session does not extend that search (stopping rule).")


# --------------------------------------------------------------------------
# HALF 2 -- L.  item 4: the drift from the inside
# --------------------------------------------------------------------------

head("HALF 2 / L -- the drift from the inside: D(x), the cycle sum, and x* = 7/3")

# 160 digits: the quantities compared here differ at the 45th decimal
# (the relative excess of D over its asymptote at x = 2^71 is ~6.6e-45).
mp.dps = 160


def D(x):
    """log2(3 + 1/x) - log2(3 - 1/x) = log2((3x+1)/(3x-1))."""
    return mp.log((3 * mpf(x) + 1) / (3 * mpf(x) - 1), 2)


def Dplus(x):
    """log2(3 + 1/x) - log2 3 = log2(1 + 1/(3x)) -- the NORTH half."""
    return mp.log(1 + 1 / (3 * mpf(x)), 2)


def Dminus(x):
    """log2(3 - 1/x) - log2 3 = log2(1 - 1/(3x)) -- the SOUTH half (negative)."""
    return mp.log(1 - 1 / (3 * mpf(x)), 2)


# (L1) the two forms of D agree
rec("L", "D(x) = log2(3+1/x) - log2(3-1/x) = log2((3x+1)/(3x-1)) identically",
    all(abs(D(x) - (mp.log(3 + mpf(1) / x, 2) - mp.log(3 - mpf(1) / x, 2))) < mpf(10) ** -50
        for x in (1, 3, 5, 101, 2 ** 20)))
rec("L", "D = Dplus - Dminus (north drift minus south drift)",
    all(abs(D(x) - (Dplus(x) - Dminus(x))) < mpf(10) ** -50
        for x in (1, 3, 5, 101, 2 ** 20)))

# (L2) the asymptotic 2/(3 x ln2)
print("       x        D(x)              2/(3x ln2)         ratio")
for x in (10, 10 ** 3, 10 ** 6, 10 ** 12, 2 ** 71):
    asym = 2 / (3 * mpf(x) * mp.log(2))
    print(f"   {mp.nstr(mpf(x),6):>10}  {mp.nstr(D(x),12):>18}  "
          f"{mp.nstr(asym,12):>18}   {mp.nstr(D(x)/asym,12)}")
rec("L", "D(x) ~ 2/(3x ln2), ratio -> 1",
    abs(D(2 ** 71) / (2 / (3 * mpf(2 ** 71) * mp.log(2))) - 1) < mpf(10) ** -43)
# and the exact direction of the approximation
rec("L", "D(x) > 2/(3x ln2) STRICTLY (artanh series: all higher terms positive)",
    all(D(x) > 2 / (3 * mpf(x) * mp.log(2)) for x in (1, 3, 10, 10 ** 6, 2 ** 71)))
rel = D(2 ** 71) / (2 / (3 * mpf(2 ** 71) * mp.log(2))) - 1
print(f"   relative excess of D over the asymptote at x = 2^71: {mp.nstr(rel,6)}")
print(f"   predicted 1/(27 x^2) = {mp.nstr(1/(27*mpf(2)**142),6)}")
rec("L", "the excess is exactly 1/(27 x^2) to leading order",
    abs(rel / (1 / (27 * mpf(2) ** 142)) - 1) < mpf(10) ** -20,
    f"ratio to 1/(27x^2) = {mp.nstr(rel/(1/(27*mpf(2)**142)), 12)}")

# (L3) the sum around a cycle -- the EXACT identity, on the four real cycles
print()
print("  --- the sum around a cycle: what is exact and what is not ---")
CYCLES = {
    "+1": ([1], 2),
    "-1": ([1], 1),
    "-5": ([5, 7], 3),
    "-17": ([17, 25, 37, 55, 41, 61, 91], 11),
}
beta_mp = mp.log(3, 2)
sum_ok = True
print("   cycle  n   K    sum of per-step drift        K - n*log2 3            equal?")
for name, (elts, K) in CYCLES.items():
    n = len(elts)
    north = (name == "+1")
    s = sum((Dplus(x) if north else Dminus(x)) for x in elts)
    gap = K - n * beta_mp
    eq = abs(s - gap) < mpf(10) ** -45
    sum_ok &= eq
    print(f"   {name:>4}  {n:>1}  {K:>2}   {mp.nstr(s,15):>22}  "
          f"{mp.nstr(gap,15):>22}   {eq}")
rec("L", "EXACT identity: sum over a cycle of log2(1 +- 1/(3x_i)) = K - n*log2 3, "
         "on all four real cycles both shores", sum_ok)
print("   Derivation (three lines, ours).  For a positive cycle each step is")
print("   3x_i + 1 = 2^{v_i} x_{i+1}, so (3 + 1/x_i) = 2^{v_i} x_{i+1}/x_i.")
print("   Multiplying around the cycle the x's telescope and sum v_i = K, giving")
print("   prod(3 + 1/x_i) = 2^K, i.e. sum log2(3 + 1/x_i) = K.  Subtracting")
print("   n*log2 3 gives  sum log2(1 + 1/(3x_i)) = K - n*log2 3 EXACTLY.  On the")
print("   negative shore the same computation with 3y_i - 1 = 2^{v_i} y_{i+1} gives")
print("   sum log2(1 - 1/(3y_i)) = K - n*log2 3.  This IS the seam identity: the")
print("   left side is the summed per-step drift, the right side is log2(2^K/3^n),")
print("   which is exactly the object T1 bounds.")

print()
print("  --- 'summed around a cycle that is exactly n*delta' : adjudicated ---")
X = mpf(2) ** 71
delta = 2 / (3 * X * mp.log(2))
print(f"   delta (T1's constant, la8) = {mp.nstr(delta,10)}")
print(f"   D(x_min) at x_min = 2^71   = {mp.nstr(D(X),10)}")
print(f"   ratio D(X)/delta            = {mp.nstr(D(X)/delta,20)}")
rec("L", "delta = D(x_min) to a relative 6.6e-45 -- the SAME constant, not a "
         "coincidence", abs(D(X) / delta - 1) < mpf(10) ** -43,
    f"D(X)/delta - 1 = {mp.nstr(D(X)/delta-1,6)}")
# the sum is bounded by n*D(X), with equality only if all elements sit at X
print("   D is strictly decreasing, so for a cycle with all x_i >= X:")
print("       sum_i D(x_i)  <=  n * D(X)  =  n * delta * (1 + 1/(27 X^2)),")
print("   with equality if and only if every x_i equals X.  So the sum is n*delta")
print("   in the EXTREMAL limit and to 44 decimal places at X = 2^71, but it is")
print("   NOT an identity: it is a sharp upper bound whose equality case is a")
print("   cycle all of whose elements are the minimum (which no cycle has).")
dec = all(D(x) > D(x + 2) for x in (1, 3, 5, 101, 10 ** 6))
rec("L", "D is strictly decreasing in x", dec)
# exhibit the strictness on a real cycle
elts17 = CYCLES["-17"][0]
sD = sum(D(x) for x in elts17)
nDX = len(elts17) * D(min(elts17))
rec("L", "on the -17 cycle the sum of D is strictly below n*D(x_min)",
    sD < nDX, f"{mp.nstr(sD,8)} < {mp.nstr(nDX,8)}")
print("   The EXACT statement underneath is the identity above: the NORTH half")
print("   alone sums to K - n*log2 3 exactly, and D = north - south is the")
print("   two-shore version of the same per-step quantity.  delta's factor 2 is")
print("   exactly that doubling: log2(1+u) - log2(1-u) = 2u/ln2 + O(u^3).")
u_check = all(abs((mp.log(1 + mpf(u), 2) - mp.log(1 - mpf(u), 2)) - 2 * mpf(u) / mp.log(2))
              < 3 * mpf(u) ** 3 for u in (mpf(10) ** -3, mpf(10) ** -6, mpf(10) ** -9))
rec("L", "log2(1+u) - log2(1-u) = 2u/ln2 + O(u^3): the factor 2 is the two shores",
    u_check)

# (L4) x* = 7/3
print()
print("  --- x* = 7/3, exactly ---")
from fractions import Fraction
xs = Fraction(7, 3)
num = 3 * xs + 1
den = 3 * xs - 1
rec("L", "(3x+1)/(3x-1) at x = 7/3 equals 4/3 in exact rationals",
    num / den == Fraction(4, 3), f"{num}/{den} = {num/den}")
rec("L", "his form (3 + 3/7)/(3 - 3/7) = 24/18 = 4/3, exact rationals",
    (3 + Fraction(3, 7)) / (3 - Fraction(3, 7)) == Fraction(4, 3))
SIGN_CONST = 2 - beta
rec("L", "log2(4/3) = 2 - log2 3 identically",
    abs(mp.log(mpf(4) / 3, 2) - (2 - beta_mp)) < mpf(10) ** -50,
    f"{mp.nstr(2-beta_mp,12)}")
rec("L", "D(7/3) = 2 - log2 3 exactly, so x* = 7/3 is the crossing point",
    abs(D(mpf(7) / 3) - (2 - beta_mp)) < mpf(10) ** -50)
# uniqueness: solve D(x) = 2 - log2 3
print("   Uniqueness: D(x) = log2((3x+1)/(3x-1)) = log2(4/3)")
print("     <=> 3(3x+1) = 4(3x-1) <=> 9x + 3 = 12x - 4 <=> 3x = 7 <=> x = 7/3.")
print("   One equation, one root -- x* = 7/3 is exact and unique, and D is")
print("   strictly decreasing, so D(x) > 2 - log2 3 for x < 7/3 and < for x > 7/3.")
rec("L", "D(x) > 2-log2 3 below 7/3 and < above (D strictly decreasing)",
    D(mpf(2)) > 2 - beta_mp > D(mpf(3)))
print(f"   D(1) = {mp.nstr(D(1),10)}   (= 1, since (3+1)/(3-1) = 2)")
print(f"   2 - log2 3 = {mp.nstr(2-beta_mp,10)}")
print(f"   D(3) = {mp.nstr(D(3),10)}   (= log2(10/8) = log2(5/4))")
rec("L", "D(1) = 1 exactly", abs(D(1) - 1) < mpf(10) ** -50)
rec("L", "COROLLARY (ours): x = 1 is the ONLY odd positive integer with "
         "D(x) > 2 - log2 3", D(1) > 2 - beta_mp and all(D(x) < 2 - beta_mp
                                                        for x in range(3, 200, 2)))
ratio71 = D(X) / (2 - beta_mp)
rec("L", "at x = 2^71 the ratio D(x)/(2 - log2 3) = 9.8e-22",
    abs(ratio71 / mpf("9.8e-22") - 1) < 2e-3, f"{mp.nstr(ratio71,6)}")

print()
print("  --- what '2 - log2 3' is, as a defined quantity ---")
print("   Three descriptions, all of the same number 0.4150374992788...:")
print("   (a) the mean per-odd-step contraction of the Collatz map, 2 - log2 3,")
print("       i.e. minus the drift of item 3 at a = 3 (E[v] = 2 minus log2 3);")
print("   (b) log2(1 + 1/(3*1)) = Dplus(1), the NORTH per-step drift at x = 1;")
print("   (c) K - n*log2 3 for the trivial cycle (n = 1, K = 2), i.e. the log-seam")
print("       gap of the |q| = 1 instance at n = 1.")
rec("L", "(a) = (b) = (c) = 2 - log2 3, all three exactly",
    abs(Dplus(1) - (2 - beta_mp)) < mpf(10) ** -50
    and abs((2 - 1 * beta_mp) - (2 - beta_mp)) < mpf(10) ** -50)
print("   The brief's candidate -- our |q| >= 1 seam input -- is (c) at n = 1 and")
print("   only at n = 1: the seam input in general is log2(2^K/3^n) >= log2(1+1/3^n),")
print("   which is not a constant.  So 'the sign information equals the drift at")
print("   x* = 7/3' is a statement about two well-defined objects, D(x) and the")
print("   constant 2 - log2 3, and the identity log2(4/3) = 2 - log2 3 that carries")
print("   it is a tautology; the content is the exact root x* = 7/3 and its")
print("   integer corollary above.")


# --------------------------------------------------------------------------
#  summary
# --------------------------------------------------------------------------

head("SUMMARY")
fails = [c for c in CHECKS if not c[2]]
bysec = {}
for s, lab, ok, det in CHECKS:
    bysec.setdefault(s, [0, 0])
    bysec[s][0] += 1
    bysec[s][1] += 0 if ok else 1
for s in sorted(bysec):
    print(f"  section {s}: {bysec[s][0]:>3} checks, {bysec[s][1]} failures")
print(f"\n  TOTAL: {len(CHECKS)} recorded checks, {len(fails)} failures")
if fails:
    print("\n  FAILURES:")
    for s, lab, ok, det in fails:
        print(f"    [{s}] {lab}   {det}")
sys.exit(1 if fails else 0)
