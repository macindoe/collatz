#!/usr/bin/env python3
"""merle_r16_check.py -- fresh verification of PR #6 (round 16),
github.com/macindoe/one-obstruction-three-faces, per
briefs/merle-round16-17-review-brief.md Queue 3 and Queue 5.

Supports: briefs/merle-round16-17-review-findings.md.

Rules honoured:
  - imports NOTHING from any Merle repository, and nothing from any prior
    Merle-check script in this repository; Python stdlib only
    (decimal.Decimal for high-precision logs/sqrt, fractions.Fraction,
    math.isqrt for exact integer square roots);
  - exact integer arithmetic at every decision that can be an integer one
    (the discharge inequalities, the product identity, the continued-fraction
    recurrence, the one-move C(w) formula);
  - where a real logarithm or square root is unavoidable, decimal.Decimal at
    TWO working precisions (150 and 280 significant digits) is used, with
    the continued-fraction partial quotients required to agree between the
    two precisions before any of them is trusted (a stability canary, run
    before any check that depends on them) -- no float anywhere, no mpmath
    dependency (not installed in this environment);
  - canaries (the four real cycles' ceiling/seam identities, and the window
    figures) printed FIRST;
  - this verifies a correspondent's re-derivation of an already-keyed window
    plus a finite discharge -- it opens no orbit or period search of any
    kind; the cycles front stays PARKED.

What this script checks (PR #6 / round 16 claims, quoted in the brief):
  PART 0 -- canaries: the four real cycles, product identity, both routes.
  PART 1 -- delta_direct and delta_chain derived from the product identity
            and the survivor+ceiling+two-bound chain respectively, in this
            script's own words; the two exact Legendre windows
            floor(sqrt(3*X*ln2/2)) = 49547666543 and
            floor(sqrt(3*X*ln2/4)) = 35035491004.
  PART 2 -- the integral (rational-under-approximation) forms:
            largest n with 2000*n^2 <= 2079*X (49542405870) and with
            4000*n^2 <= 2079*X (35031771147, the L-A8 record's own integral
            figure); the rational bound 693/1000 < ln2 and its consequence
            2079/2000 < 3*ln2/2.
  PART 3 -- continued fraction of log2(3) from scratch (Decimal-based,
            stability-checked between two precisions); convergents;
            confirm exactly 22 lie below each window; q_21 = 6586818670,
            q_22 = 65470613321, q_23 = 137528045312.
  PART 4 -- theta_j (defined per merle-la8-t1-check-findings.md item (f):
            theta_j = |q_j*log2(3) - p_j|) and the criterion theta_j >
            q_j*delta at q_21 (both routes) and q_22 (both routes, expect
            the direct-route margin 0.499, matching the round-16 letter).
  PART 5 -- the integer discharge criteria: chain's 2000*q(q+q') <= 2079*X
            (already keyed) and the new 1000*q(q+q') <= 2079*X (direct);
            both hold for all 22 window convergents and both fail at
            (q_22, q_23); the trivial implication chain-criterion-holds
            => direct-criterion-holds, stated and checked directly.
  PART 6 -- the multiples cancellation: |t*q_j*L - t*p_j| = t*theta_j
            exactly, and the discharge criterion is t-invariant, checked
            algebraically and numerically at several (j, t).
  PART 7 -- the negative control: floor(ln2*sqrt(3*X)) = 58337919180,
            derived from R/n -> 1/(2 ln2) (L-A11) substituted for the
            trivial R <= n bound; and the "R/n <= 0.5727" reading, tried
            under five distinct operational readings, one of which
            (window(rho) = q_22) reproduces 0.5727 to four significant
            digits -- reported, with the others recorded as candidates
            that did not reproduce it, per the brief's own instruction not
            to guess past one stated reading once a match is found.
  PART 8 -- the one-move observation's C(w) difference formula,
            2^p*(2^t-1)*3^(r-1-j), verified on random words and rotations
            (non-wrapping single-1-across-t-zeros moves, exact integers).
            The N <= 24 class count "56 / 233,324" is NOT computed: no
            reading of "cyclic zero-run sequence takes two values a, a+t
            and is balanced" recovers 233,324 from the standard primitive-
            necklace count (698,870 at N=24 alone; 1,465,020 summed over
            N = 1..24) -- recorded as a gap, per the brief's own
            instruction, rather than guessed at.

Reproduction: `python experiments/merle_r16_check.py > experiments/merle_r16_check_output.txt`
from the repository root reproduces the committed output byte-for-byte.
"""

import math
from decimal import Decimal, getcontext
from fractions import Fraction

CHECKS = 0
FAILURES = 0


def short(d, digits=30):
    """Truncate a Decimal's string form to a bounded number of characters for
    readable output -- printing only, never used in any decision."""
    s = str(d)
    return s if len(s) <= digits else s[:digits] + "..."


def check(label, ok):
    global CHECKS, FAILURES
    CHECKS += 1
    if not ok:
        FAILURES += 1
        print(f"  FAIL: {label}")
    return ok


def require(label, ok):
    if not check(label, ok):
        raise SystemExit(f"HARD FAIL: {label}")


# ----------------------------------------------------------------------------
# Shared constants

X = 2 ** 71  # Barina verification input, per cycles.md 12.6.3


def hi_precision_logs(prec_digits):
    """Compute ln2, ln3, log2_3 at the given Decimal precision (guard digits
    added). Returns (ln2, ln3, log2_3) as Decimal."""
    getcontext().prec = prec_digits + 20
    ln2 = Decimal(2).ln()
    ln3 = Decimal(3).ln()
    return ln2, ln3, ln3 / ln2


def decimal_to_fraction(d):
    """Exact conversion of a Decimal to a Fraction (no precision lost -- a
    Decimal's internal representation IS an exact rational)."""
    sign, digits, exp = d.as_tuple()
    num = int(''.join(map(str, digits)))
    if sign:
        num = -num
    if exp >= 0:
        return Fraction(num * 10 ** exp, 1)
    return Fraction(num, 10 ** (-exp))


def cf_terms_from_fraction(frac, nterms):
    """Continued-fraction partial quotients of an exact Fraction, standard
    algorithm (Euclid on numerator/denominator)."""
    terms = []
    a_num, a_den = frac.numerator, frac.denominator
    for _ in range(nterms):
        if a_den == 0:
            break
        a = a_num // a_den
        terms.append(a)
        a_num, a_den = a_den, a_num - a * a_den
    return terms


def convergents_from_terms(terms):
    """Standard recurrence, the convention pinned in merle-la8-t1-check-
    findings.md: p_{-1}=1, q_{-1}=0, p_0=a_0, q_0=1, then p_n = a_n p_{n-1}
    + p_{n-2}, q_n = a_n q_{n-1} + q_{n-2}."""
    convs = []
    p_prev, p_cur = 1, terms[0]
    q_prev, q_cur = 0, 1
    convs.append((p_cur, q_cur))
    for a in terms[1:]:
        p_next = a * p_cur + p_prev
        q_next = a * q_cur + q_prev
        convs.append((p_next, q_next))
        p_prev, p_cur = p_cur, p_next
        q_prev, q_cur = q_cur, q_next
    return convs


print("=" * 78)
print("merle_r16_check.py -- fresh verification of PR #6 (round 16)")
print("=" * 78)

# ----------------------------------------------------------------------------
print("\n--- PART 0: canaries -- the four real cycles, product identity, both routes ---")

# Walk the odd (Terras-style) map x -> (3x+1) with 2-adic valuation stripped,
# starting at each of the four known real cycles' smallest-magnitude element,
# using exact Python integers throughout.

def walk_cycle(x0, max_steps=200):
    """Return the list of odd elements of the cycle containing x0, and K, n."""
    xs = [x0]
    x = x0
    K = 0
    for _ in range(max_steps):
        y = 3 * x + 1
        v = 0
        while y % 2 == 0:
            y //= 2
            v += 1
        K += v
        if y == x0:
            return xs, K, len(xs)
        xs.append(y)
        x = y
    raise RuntimeError(f"cycle did not close from x0={x0} within {max_steps} steps")


real_cycles = {
    "+1": 1,
    "-1": -1,
    "-5": -5,
    "-17": -17,
}

ln2_lo, ln3_lo, log2_3_lo = hi_precision_logs(150)

cycle_data = {}
for name, x0 in real_cycles.items():
    xs, K, n = walk_cycle(x0)
    cycle_data[name] = (xs, K, n)
    # Product identity: prod(3x_i + 1) == 2^K * prod(x_i)
    prod_left = 1
    for x in xs:
        prod_left *= (3 * x + 1)
    prod_right = 1
    for x in xs:
        prod_right *= x
    prod_right *= 2 ** K
    check(f"canary {name}: product identity prod(3x+1) = 2^K prod(x)",
          prod_left == prod_right)

    # ceiling / chain route: q = 2^K - 3^n
    q = 2 ** K - 3 ** n
    # direct route: epsilon = K - n*log2(3) = sum_i log2(1 + 1/(3 x_i))
    # computed two ways at high (Decimal) precision and compared.
    eps_via_Kn = K - n * log2_3_lo
    eps_via_sum = sum((Decimal(1) + Decimal(1) / (3 * Decimal(x))).ln() / ln2_lo
                       for x in xs)
    diff = abs(eps_via_Kn - eps_via_sum)
    check(f"canary {name}: epsilon = K - n*log2(3) equals sum_i log2(1+1/(3x_i)) "
          f"to 100 digits (diff={diff:.2e})",
          diff < Decimal(10) ** -100)
    print(f"  {name}: n={n}, K={K}, q=2^K-3^n={q}, xs={xs}")

# ----------------------------------------------------------------------------
print("\n--- PART 1: delta_direct and delta_chain; the two exact Legendre windows ---")

print("""
Derivation, direct route (this script's own words):
  For a cycle of the odd map with n elements all >= X and K = sum_i v_2(3x_i+1),
  the product identity prod(3x_i+1) = 2^K prod(x_i) gives, dividing by
  prod(3x_i), the exact identity
      2^K / 3^n = prod_i (1 + 1/(3x_i))
  hence, taking log2 of both sides,
      epsilon := K - n log2(3) = sum_i log2(1 + 1/(3 x_i)).
  Using log2(1+u) = ln(1+u)/ln2 <= u/ln2 (from ln(1+u) <= u, u > 0):
      epsilon <= (1/ln2) * sum_i 1/(3 x_i) = (1/(3 ln2)) * sum_i 1/x_i
              <= (1/(3 ln2)) * n/X          (each x_i >= X, trivially)
              = n / (3 X ln2).
  So epsilon/n <= delta_direct := 1/(3 X ln2).

Derivation, chain route (L-A8's own, quoted from merle-la8-t1-check-findings.md
item (c)): via the survivor bound + ceiling + two-bound
(a "(m+1)^n < 2m^n" loss at 2n < 3X), the chain reaches
      0 < K ln2 - n ln3 <= q/3^n < 2n/(3X)      (q = 2^K - 3^n)
  and dividing by n ln2:
      0 < K/n - log2(3) < 2/(3 X ln2) =: delta_chain.

delta_direct is exactly HALF of delta_chain -- the "factor 2" the round-16
letter traces to the chain's own two-bound loss, not to a slip in the figure
that used delta_direct's value.
""")

delta_direct_check = Decimal(1) / (Decimal(3) * X * ln2_lo)
delta_chain_check = Decimal(2) / (Decimal(3) * X * ln2_lo)
check("delta_direct is exactly half of delta_chain",
      abs(delta_chain_check - 2 * delta_direct_check) < Decimal(10) ** -100)

# Legendre's criterion applies when delta <= 1/(2n^2), i.e. n <= sqrt(1/(2 delta)).
def window_floor(delta_expr_num_over_den, prec):
    """delta_expr_num_over_den: a Decimal representing delta.
    Returns floor(sqrt(1/(2*delta)))."""
    val = (1 / (2 * delta_expr_num_over_den)).sqrt()
    return int(val)


w_direct_at = {}
w_chain_at = {}
for prec in (150, 280):
    ln2_p, ln3_p, log2_3_p = hi_precision_logs(prec)
    w_direct_at[prec] = int((Decimal(3) * X * ln2_p / 2).sqrt())
    w_chain_at[prec] = int((Decimal(3) * X * ln2_p / 4).sqrt())

check("w_direct stable between 150 and 280 digit precision",
      w_direct_at[150] == w_direct_at[280])
check("w_chain stable between 150 and 280 digit precision",
      w_chain_at[150] == w_chain_at[280])

w_direct = w_direct_at[280]
w_chain = w_chain_at[280]
print(f"floor(sqrt(3*X*ln2/2)) [direct, exact window]  = {w_direct}")
print(f"floor(sqrt(3*X*ln2/4)) [chain,  exact window]   = {w_chain}")

check("w_direct == 49547666543 (the withdrawn REQ-MATH-054 figure)",
      w_direct == 49547666543)
check("w_chain == 35035491004 (L-A8's own corrected exact window)",
      w_chain == 35035491004)

ratio = Decimal(w_direct) / Decimal(w_chain)
check("w_direct / w_chain == sqrt(2) to 10 decimal places",
      abs(ratio - Decimal(2).sqrt()) < Decimal("1e-10"))

# ----------------------------------------------------------------------------
print("\n--- PART 2: integral (rational-under-approximation) forms ---")

# 693/1000 < ln2, exact rational-vs-Decimal comparison (Decimal computed to
# 280 digits far exceeds the precision needed to settle a 3-digit rational).
ln2_hi, ln3_hi, log2_3_hi = hi_precision_logs(280)
rational_693 = Fraction(693, 1000)
check("693/1000 < ln2 (exact rational vs 280-digit Decimal)",
      rational_693 < ln2_hi)

rational_2079_4000 = Fraction(2079, 4000)
check("2079/4000 < 3*ln2/4",
      rational_2079_4000 < Decimal(3) * ln2_hi / 4)
rational_2079_2000 = Fraction(2079, 2000)
check("2079/2000 < 3*ln2/2 (= 2 * 2079/4000 < 2 * 3ln2/4, doubling both sides "
      "of the previous inequality)",
      rational_2079_2000 < Decimal(3) * ln2_hi / 2)

def largest_n_isqrt(coef_n2, coef_X, X_val):
    """Largest n with coef_n2 * n^2 <= coef_X * X_val, via math.isqrt."""
    rhs = coef_X * X_val
    n = math.isqrt(rhs // coef_n2)
    while coef_n2 * (n + 1) ** 2 <= rhs:
        n += 1
    while coef_n2 * n ** 2 > rhs:
        n -= 1
    return n


n_direct_integral = largest_n_isqrt(2000, 2079, X)
n_chain_integral = largest_n_isqrt(4000, 2079, X)
print(f"largest n with 2000*n^2 <= 2079*X : {n_direct_integral}")
print(f"largest n with 4000*n^2 <= 2079*X : {n_chain_integral}")
check("largest n with 2000n^2 <= 2079X == 49542405870",
      n_direct_integral == 49542405870)
check("largest n with 4000n^2 <= 2079X == 35031771147 (L-A8's own integral figure)",
      n_chain_integral == 35031771147)
check("integral direct window is strictly inside the exact direct window",
      n_direct_integral <= w_direct)
check("integral chain window is strictly inside the exact chain window",
      n_chain_integral <= w_chain)

# ----------------------------------------------------------------------------
print("\n--- PART 3: continued fraction of log2(3), from scratch, stability-checked ---")

NTERMS = 30
frac_150 = decimal_to_fraction(hi_precision_logs(150)[2])
frac_280 = decimal_to_fraction(hi_precision_logs(280)[2])
terms_150 = cf_terms_from_fraction(frac_150, NTERMS)
terms_280 = cf_terms_from_fraction(frac_280, NTERMS)

stable_terms = []
for a, b in zip(terms_150, terms_280):
    if a == b:
        stable_terms.append(a)
    else:
        break

print(f"partial quotients (150-digit): {terms_150}")
print(f"partial quotients (280-digit): {terms_280}")
print(f"stable prefix ({len(stable_terms)} terms): {stable_terms}")

require("at least 24 continued-fraction terms are stable between precisions",
        len(stable_terms) >= 24)

convergents = convergents_from_terms(stable_terms)
qs = [q for (p, q) in convergents]
ps = [p for (p, q) in convergents]

print("convergents p_j/q_j, j = 0..%d:" % (len(convergents) - 1))
for j, (p, q) in enumerate(convergents):
    print(f"  j={j:2d}  p={p}  q={q}")

check("q_0 == q_1 == 1 (the a_0=1 convention)", qs[0] == 1 and qs[1] == 1)
check("q_21 == 6586818670", qs[21] == 6586818670)
check("q_22 == 65470613321", qs[22] == 65470613321)
check("q_23 == 137528045312", qs[23] == 137528045312)

count_below_direct = sum(1 for q in qs if q <= w_direct)
count_below_chain = sum(1 for q in qs if q <= w_chain)
print(f"convergents with q_j <= w_direct ({w_direct}): {count_below_direct}")
print(f"convergents with q_j <= w_chain  ({w_chain}): {count_below_chain}")
check("exactly 22 convergents lie below the direct window", count_below_direct == 22)
check("exactly 22 convergents lie below the chain window", count_below_chain == 22)
check("the same SET of 22 convergents lies below both windows "
      "(q_22 = 65470613321 lies above both)",
      qs[22] > w_direct and qs[22] > w_chain and qs[21] <= w_direct and qs[21] <= w_chain)

# ----------------------------------------------------------------------------
print("\n--- PART 4: theta_j and the criterion theta_j > q_j*delta, both routes ---")

print("""
theta_j defined per merle-la8-t1-check-findings.md item (f):
    theta_j = |q_j * log2(3) - p_j|
(the classical best-approximation defect of the j-th convergent).
""")

getcontext().prec = 300
ln2_300, ln3_300, alpha_300 = hi_precision_logs(280)

def theta(j):
    p, q = convergents[j]
    return abs(Decimal(q) * alpha_300 - Decimal(p))


delta_direct_300 = Decimal(1) / (Decimal(3) * X * ln2_300)
delta_chain_300 = Decimal(2) / (Decimal(3) * X * ln2_300)

theta21 = theta(21)
theta22 = theta(22)
margin_direct_21 = theta21 / (Decimal(qs[21]) * delta_direct_300)
margin_chain_21 = theta21 / (Decimal(qs[21]) * delta_chain_300)
margin_direct_22 = theta22 / (Decimal(qs[22]) * delta_direct_300)
margin_chain_22 = theta22 / (Decimal(qs[22]) * delta_chain_300)

print(f"theta_21 = {short(theta21)}")
print(f"margin at q_21, direct route (theta_21/(q_21*delta_direct)): {short(margin_direct_21)}")
print(f"margin at q_21, chain  route (theta_21/(q_21*delta_chain)) : {short(margin_chain_21)}")
print(f"theta_22 = {short(theta22)}")
print(f"margin at q_22, direct route: {short(margin_direct_22)}")
print(f"margin at q_22, chain  route: {short(margin_chain_22)}")

check("margin at q_21, direct route, rounds to 10.8865",
      abs(margin_direct_21 - Decimal("10.8865")) < Decimal("0.0001"))
check("margin at q_21, chain route, rounds to 5.4433 (matches merle-la8-t1-check-findings.md)",
      abs(margin_chain_21 - Decimal("5.4433")) < Decimal("0.0001"))
check("margin at q_22, direct route, rounds to 0.499 (matches the round-16 letter)",
      abs(margin_direct_22 - Decimal("0.499")) < Decimal("0.0005"))
check("direct-route margin is exactly double the chain-route margin at q_21",
      abs(margin_direct_21 - 2 * margin_chain_21) < Decimal("1e-50"))
check("direct-route margin is exactly double the chain-route margin at q_22",
      abs(margin_direct_22 - 2 * margin_chain_22) < Decimal("1e-50"))
check("criterion HOLDS at q_21 under both routes (margin > 1)",
      margin_direct_21 > 1 and margin_chain_21 > 1)
check("criterion FAILS at q_22 under both routes (margin < 1) -- non-vacuity",
      margin_direct_22 < 1 and margin_chain_22 < 1)

# ----------------------------------------------------------------------------
print("\n--- PART 5: the integer discharge criteria, both routes, all 22 + failure at q_22 ---")

def discharge_holds(coef, j):
    q_j = qs[j]
    q_j1 = qs[j + 1]
    return coef * q_j * (q_j + q_j1) <= 2079 * X


chain_all_pass = all(discharge_holds(2000, j) for j in range(22))
direct_all_pass = all(discharge_holds(1000, j) for j in range(22))
check("chain criterion 2000*q(q+q') <= 2079*X holds for all 22 window convergents",
      chain_all_pass)
check("direct criterion 1000*q(q+q') <= 2079*X holds for all 22 window convergents",
      direct_all_pass)
check("chain criterion FAILS at (q_22, q_23)", not discharge_holds(2000, 22))
check("direct criterion FAILS at (q_22, q_23)", not discharge_holds(1000, 22))

print("""
Trivial implication, stated: if 2000*q(q+q') <= 2079*X (chain criterion holds)
then, since 1000*q(q+q') = (1/2)*2000*q(q+q') <= (1/2)*2079*X <= 2079*X
(the last step because 1/2 <= 1 and both sides are nonnegative), the direct
criterion 1000*q(q+q') <= 2079*X holds automatically -- it needs no q-specific
fact at all, only that halving a quantity known to be <= something can only
make it <= that same something. Checked directly for all 22 convergents below
(not merely asserted): the chain criterion holding at each j implies the
direct criterion holds at the same j.
""")

check("chain-criterion-holds implies direct-criterion-holds, checked at every j "
      "of the 22 (not merely the trivial halving argument, the actual pairs)",
      all((not discharge_holds(2000, j)) or discharge_holds(1000, j) for j in range(22)))

print("What 'implies the direct one' means in the entry's own terms: the chain's "
      "discharge_all is the STRONGER (harder to satisfy, coefficient 2000) integer "
      "criterion; since it is exactly twice the direct criterion's coefficient, "
      "every (q_j, q_j+1) pair that clears the harder chain bar automatically "
      "clears the easier direct bar at half the margin. It is not evidence that "
      "the direct route needs no independent proof -- the direct route's own "
      "theorems (log_gap_direct, quotient_is_convergent_direct) still had to be "
      "proved -- only that, once both hold, the direct discharge is implied by "
      "the chain discharge as a matter of arithmetic, not of number theory.")

# ----------------------------------------------------------------------------
print("\n--- PART 6: multiples cancellation, |t*q_j*L - t*p_j| = t*theta_j, t-invariance ---")

for (j, t) in [(21, 2), (21, 3), (21, 5), (10, 7), (5, 11)]:
    p_j, q_j = convergents[j]
    th = theta(j)
    lhs = abs(Decimal(t * q_j) * alpha_300 - Decimal(t * p_j))
    rhs = t * th
    check(f"|t*q_{j}*L - t*p_{j}| == t*theta_{j} at t={t} (to 250 digits)",
          abs(lhs - rhs) < Decimal(10) ** -250)

    # t-invariance of the discharge criterion: theta_j > q_j*delta iff
    # t*theta_j > t*q_j*delta (dividing/multiplying both sides by t > 0).
    delta_here = delta_direct_300
    crit_before = th > Decimal(q_j) * delta_here
    crit_after = (t * th) > Decimal(t * q_j) * delta_here
    check(f"discharge criterion t-invariant at j={j}, t={t} "
          f"(theta_j > q_j*delta iff t*theta_j > t*q_j*delta)",
          crit_before == crit_after)

print("""
Algebra: the Legendre step delivers K/n in lowest terms as p_j/q_j (a REDUCED
convergent), so a priori n = t*q_j for some integer t >= 1 and K = t*p_j.
Then |n*L - K| = |t*q_j*L - t*p_j| = t*|q_j*L - p_j| = t*theta_j exactly
(L irrational, t > 0, so no cancellation surprises), and the cycle's demand
is |n*L - K| < n*delta = t*q_j*delta. Dividing both sides by t > 0:
theta_j < q_j*delta -- the SAME per-convergent test as at t=1. So the
discharge, once it kills q_j, kills every multiple of q_j in the window at
once; this is exactly why the entry's number of convergent denominators (22)
already accounts for every in-window n, not just the 22 denominators
themselves.
""")

# ----------------------------------------------------------------------------
print("\n--- PART 7: negative control (58337919180) and the 'R/n <= 0.5727' reading ---")

# R/n -> 1/(2 ln2) exactly (L-A11's Sturmian-word limit), substituted for the
# trivial R <= n bound: delta_eff = (1/(2 ln2)) / (3 X ln2) = 1/(6 X ln2^2),
# giving window'(rho=1/(2ln2)) = floor(sqrt(1/(2*delta_eff)))
#                              = floor(sqrt(3 X ln2^2)) = floor(ln2*sqrt(3X)).
w_neg = int(ln2_300 * (Decimal(3) * X).sqrt())
print(f"negative control window, floor(ln2*sqrt(3X)) = {w_neg}")
check("negative control window == 58337919180 (matches the round-16 letter)",
      w_neg == 58337919180)
check("negative control window is strictly bigger than the direct window "
      "(the L-A11 sup ratio would widen the window, if it could be used as a "
      "universal bound rather than merely a realized value)",
      w_neg > w_direct)
check("negative control window is still strictly below q_22 "
      "(so even this optimistic substitution does not reach the next convergent)",
      w_neg < qs[22])

print("""
Trying to reproduce 'reaching Hercher's bound by this route would need
R/n <= 0.5727' -- five distinct operational readings of what 'reaching
Hercher's bound' could mean, computed here rather than guessed at:

  A. rho such that window(rho) = q_23 (the window literally reaches
     Hercher's underlying threshold, per the L-A8 adjudication of what
     Hercher's printed 1.375e11 corresponds to exactly):
       rho = (w_direct / q_23)^2
  B. rho such that the EXACT discharge criterion at q_22 is at the boundary
     (theta_22 = q_22 * rho / (3 X ln2)):
       rho = theta_22 * 3 X ln2 / q_22
  C. rho such that the CONSERVATIVE (1/(q_22+q_23)) bound at q_22 is at the
     boundary:
       rho = 3 X ln2 / (q_22 * (q_22 + q_23))
  D. rho such that window(rho) = q_22 (the window reaches the LAST
     convergent before Hercher's, i.e. the point the round-16 letter's own
     negative control is measured against):
       rho = (w_direct / q_22)^2
  E. rho such that window(rho) reaches Hercher's Table-1 semiconvergent
     figure q_21+q_22 = 72057431991:
       rho = (w_direct / (q_21+q_22))^2
""")

q22_dec = Decimal(qs[22])
q23_dec = Decimal(qs[23])
q21_dec = Decimal(qs[21])
w_direct_dec = Decimal(w_direct)

rho_A = (w_direct_dec / q23_dec) ** 2
rho_B = theta22 * Decimal(3) * X * ln2_300 / q22_dec
rho_C = Decimal(3) * X * ln2_300 / (q22_dec * (q22_dec + q23_dec))
rho_D = (w_direct_dec / q22_dec) ** 2
rho_E = (w_direct_dec / (q21_dec + q22_dec)) ** 2

for label, rho in [("A (window reaches q_23)", rho_A),
                    ("B (exact discharge boundary at q_22)", rho_B),
                    ("C (conservative-bound boundary at q_22)", rho_C),
                    ("D (window reaches q_22)", rho_D),
                    ("E (window reaches q_21+q_22 semiconvergent)", rho_E)]:
    print(f"  reading {label}: rho = {short(rho)}")

target = Decimal("0.5727")
matches = [label for label, rho in
           [("A", rho_A), ("B", rho_B), ("C", rho_C), ("D", rho_D), ("E", rho_E)]
           if abs(rho - target) < Decimal("0.0001")]

check("exactly one of the five readings (D: window(rho) reaches q_22) "
      "reproduces 'R/n <= 0.5727' to four significant digits",
      matches == ["D"])

print(f"""
Result: reading D -- rho such that the direct-route Legendre window reaches
q_22 -- gives rho = {short(rho_D)}, which rounds to 0.5727 and is the ONLY one of the
five readings that matches. This is reported as the operational reading, not
asserted as definitionally certain: the archived text does not spell out
which of A-E (or some other construction) it means by 'reaching Hercher's
bound by this route'. The numerical match is exact to four significant
digits, which is strong evidence for reading D, but the entry itself is not
explicit enough to call this a closed derivation rather than a very likely
reconstruction -- recorded as such, per the brief's instruction not to guess
past one stated reading once a match is found, and not further chased.

Under reading D, the point of the negative control is now legible: the best
known R/n (L-A11's sup, 1/(2 ln2) =~ 0.7214) is LARGER than the 0.5727 that
reading D says would be needed to extend the window as far as q_22 -- so
"no admissible family provides" the tighter ratio the route would need, and
the window cannot be stretched that far by this method with any currently
known R bound.
""")

# ----------------------------------------------------------------------------
print("\n--- PART 8: the one-move observation's C(w) difference formula ---")


def C_of_word(w):
    """w: list of bits (0/1), NOT necessarily cyclic here -- linear index
    convention, per the LEDGER's own C(w) = sum_j 2^{p_j} 3^{r-1-j}
    with p_0 < p_1 < ... < p_{r-1} the positions of the 1s."""
    ones = [i for i, b in enumerate(w) if b == 1]
    r = len(ones)
    return sum(2 ** p * 3 ** (r - 1 - j) for j, p in enumerate(ones))


import random
rng = random.Random(20260926)

move_checks = 0
for _ in range(2000):
    N = rng.randint(6, 40)
    r = rng.randint(1, N - 1)
    # random word with r ones, N-r zeros, as a random permutation
    positions = rng.sample(range(N), r)
    w = [0] * N
    for p in positions:
        w[p] = 1
    ones = sorted(i for i, b in enumerate(w) if b == 1)
    # pick a random 1 (not at the last position) followed by >=1 zeros,
    # non-wrapping, and move it across t of those zeros
    candidates = []
    for idx, p in enumerate(ones):
        # count consecutive zeros immediately after p, without wrapping
        run = 0
        k = p + 1
        while k < N and w[k] == 0:
            run += 1
            k += 1
        if run >= 1:
            candidates.append((idx, p, run))
    if not candidates:
        continue
    idx, p, max_run = rng.choice(candidates)
    t = rng.randint(1, max_run)
    w2 = w[:]
    w2[p] = 0
    w2[p + t] = 1
    r_total = len(ones)
    j_rank = idx  # 0-indexed rank of the moved 1 among the sorted ones
    C1 = C_of_word(w)
    C2 = C_of_word(w2)
    expected_diff = (2 ** p) * (2 ** t - 1) * 3 ** (r_total - 1 - j_rank)
    move_checks += 1
    check(f"C(w') - C(w) == 2^p(2^t-1)3^(r-1-j) "
          f"[N={N}, r={r_total}, p={p}, t={t}, j={j_rank}]",
          (C2 - C1) == expected_diff)

print(f"one-move C(w) difference formula checked on {move_checks} random "
      f"(word, move) instances, non-wrapping single-1-across-t-zeros moves")

print("""
The N <= 24 class count '56 / 233,324' (the share of primitive necklaces
whose cyclic zero-run sequence takes two values a, a+t and is balanced) is
NOT computed here. Standard primitive (aperiodic) binary necklace counts,
via the Mobius formula (1/n) sum_{d|n} mu(d) 2^(n/d), give 698,870 necklaces
of length exactly 24, and 1,465,020 summed over lengths 1..24 -- neither
matches 233,324 under any reading tried. The archived text's own definition
("balanced blocks of 1s, every zero run equal to t" alongside "takes two
values a, a+t") is not internally consistent as a single operational
criterion (the first phrase describes a SINGLE zero-run length, the second
describes exactly TWO), and no reading recovers the stated denominator.
RECORDED AS A GAP, per the brief's own instruction, and not chased further --
this matches the treatment given to campaign-map section 167 in the round-15
window (merle-round15-review-findings.md Section 4).
""")

# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"TOTAL: {CHECKS} checks, {FAILURES} failures")
print("=" * 78)

if FAILURES:
    raise SystemExit(1)
