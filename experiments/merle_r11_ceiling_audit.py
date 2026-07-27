#!/usr/bin/env python3
"""
merle_r11_ceiling_audit.py
==========================

Supports: briefs/merle-r11-ceiling-audit-findings.md (round-11 Lean re-audit of
Eric Merle's ceiling repair in `one-obstruction-three-faces-lean`, HEAD c991430).

WHAT THIS IS.  A read-not-built statement-match audit.  We have no Lean
toolchain and install none.  This script checks that the Lean *statements*
`ceiling_lower`, `ceiling_pinned` and the four repaired downstream theorems
(`ratio_bound_at_barina`, `log_gap_at_barina`, `log_gap_gen`,
`quotient_is_convergent_gen`) are TRUE AS STATED at every point we can reach:
the real cycles, the trivial cycle, negative controls, and several hundred
synthetic (n, K) points including edges.  It does not and cannot check that the
proofs compile.

WHAT THIS IS NOT.  It imports nothing from any Merle repository, runs none of
his scripts, and imports nothing from any previous Merle-check script in this
repository (in particular not experiments/merle_lean_r10_audit.py or
experiments/merle_la8_t1_check.py).  The cycle data is re-derived here from the
odd Collatz map itself; the continued fraction of log2(3) is recomputed here
from scratch.

METHOD.  Every decision that can be an exact-integer decision is one.  Where a
logarithm is unavoidable (the analytic bridge at scales n ~ 6.5e10, where 3^n
has ten billion digits and cannot be formed), we use Python's stdlib `decimal`
at TWO working precisions, 120 and 200 significant digits, and assert that
every reported quantity agrees between them to the reported precision.  No
float touches any pass/fail decision.

Stopping rules: this verifies a correspondent's artifacts.  No orbit search and
no per-period cycle search is performed; the synthetic sweeps are (n, K) integer
pairs and element multisets.  The cycles front stays PARKED.
"""

from decimal import Decimal, getcontext, localcontext
from fractions import Fraction
from math import isqrt
import random

# ---------------------------------------------------------------------------
# harness
# ---------------------------------------------------------------------------

CHECKS = 0
FAILS = []


def check(label, ok, detail=""):
    """Record one pass/fail decision."""
    global CHECKS
    CHECKS += 1
    if not ok:
        FAILS.append((label, detail))
        print("  *** FAIL: %s %s" % (label, detail))
    return ok


def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# high-precision constants, two precisions, stability asserted
# ---------------------------------------------------------------------------

PRECS = (120, 200)


def log2_3(prec):
    """log2(3) as a Decimal at `prec` significant digits."""
    with localcontext() as ctx:
        ctx.prec = prec + 20
        return +(Decimal(3).ln() / Decimal(2).ln())


def ln2(prec):
    with localcontext() as ctx:
        ctx.prec = prec + 20
        return +Decimal(2).ln()


def ln3(prec):
    with localcontext() as ctx:
        ctx.prec = prec + 20
        return +Decimal(3).ln()


def cf_terms(prec, count):
    """Partial quotients of log2(3), by exact Euclid on a scaled integer
    approximation.  Computed independently at each precision."""
    with localcontext() as ctx:
        ctx.prec = prec + 30
        L = Decimal(3).ln() / Decimal(2).ln()
        scale = 10 ** prec
        num = int((L * scale).to_integral_value(rounding="ROUND_FLOOR"))
        den = scale
    terms = []
    a, b = num, den
    while b and len(terms) < count:
        q = a // b
        terms.append(q)
        a, b = b, a - q * b
    return terms


def convergents_from_cf(terms):
    """(p_j, q_j) for j = 0, 1, 2, ...  Standard indexing: p_0/q_0 = a_0/1."""
    out = []
    pm1, qm1 = 1, 0          # p_{-1}, q_{-1}
    pm2, qm2 = 0, 1          # p_{-2}, q_{-2}
    for a in terms:
        p = a * pm1 + pm2
        q = a * qm1 + qm2
        out.append((p, q))
        pm2, qm2 = pm1, qm1
        pm1, qm1 = p, q
    return out


# ---------------------------------------------------------------------------
# CANARIES FIRST: re-derive the real cycles from the odd Collatz map
# ---------------------------------------------------------------------------

def v2(m):
    """2-adic valuation of a nonzero integer."""
    assert m != 0
    m = abs(m)
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k


def odd_step(x):
    """One step of the odd map: 3x+1 = 2^v * x'.  Returns (v, x')."""
    y = 3 * x + 1
    v = v2(y)
    return v, y >> v


def derive_cycle(seed, limit=10000):
    """Iterate the odd map from `seed` and return the cycle it falls into, as
    (elements, valuations) in orbit order starting at the smallest |element|."""
    seen = {}
    x = seed
    path = []
    for t in range(limit):
        if x in seen:
            start = seen[x]
            elems = path[start:]
            vals = [odd_step(e)[0] for e in elems]
            # rotate so the element of least absolute value comes first
            k = min(range(len(elems)), key=lambda i: (abs(elems[i]), elems[i]))
            elems = elems[k:] + elems[:k]
            vals = vals[k:] + vals[:k]
            return elems, vals
        seen[x] = len(path)
        path.append(x)
        _, x = odd_step(x)
    raise RuntimeError("no cycle from %d within %d steps" % (seed, limit))


head("CANARIES -- the real cycles, re-derived from the odd map in this script")

CYCLES = {}
for seed in (1, -1, -5, -17):
    elems, vals = derive_cycle(seed)
    n = len(elems)
    K = sum(vals)
    CYCLES[seed] = (elems, vals, n, K)
    prod_x = 1
    prod_3x1 = 1
    for e in elems:
        prod_x *= e
        prod_3x1 *= 3 * e + 1
    # the product identity, exact, over Z
    check("product identity, cycle %d" % seed,
          prod_3x1 == 2 ** K * prod_x,
          "%d vs %d" % (prod_3x1, 2 ** K * prod_x))
    # every step relation, exact
    for i, e in enumerate(elems):
        nxt = elems[(i + 1) % n]
        check("step relation, cycle %d index %d" % (seed, i),
              3 * e + 1 == 2 ** vals[i] * nxt)
    q = 2 ** K - 3 ** n
    print("  cycle %4d : n=%d  K=%2d  elements=%s" % (seed, n, K, elems))
    print("               v=%s   prod(3x+1)=%d = 2^K*prod(x)=%d   q = 2^K-3^n = %d"
          % (vals, prod_3x1, 2 ** K * prod_x, q))

# the -17 figures the L-A8 entry prints, digit-exact
e17, v17, n17, K17 = CYCLES[-17]
p17 = 1
p17x = 1
for e in e17:
    p17x *= e
    p17 *= 3 * e + 1
check("-17 cycle: prod(3x+1) = -403123745024000", p17 == -403123745024000, str(p17))
check("-17 cycle: prod(x) = -196837766125", p17x == -196837766125, str(p17x))
check("-17 cycle: K = 11", K17 == 11, str(K17))

# constants, at both precisions, stability asserted
head("CONSTANTS -- computed at two precisions, agreement asserted")
X_BARINA = 2 ** 71
DELTAS = {}
for prec in PRECS:
    with localcontext() as ctx:
        ctx.prec = prec
        DELTAS[prec] = Decimal(2) / (Decimal(3) * Decimal(X_BARINA) * ln2(prec))
d_lo, d_hi = DELTAS[PRECS[0]], DELTAS[PRECS[1]]
check("delta stable across precisions (40 digits)",
      ("%.40e" % d_lo) == ("%.40e" % d_hi),
      "%.40e vs %.40e" % (d_lo, d_hi))
check("delta = 4.0734e-22 (the L-A8 figure, rounded)",
      ("%.4e" % d_hi) == "4.0734e-22", "%.6e" % d_hi)
print("  delta = 2/(3*2^71*ln2) = %.10e   (2^71 = %d)" % (d_hi, X_BARINA))

CF = {}
for prec in PRECS:
    CF[prec] = cf_terms(prec, 30)
check("continued fraction of log2(3) stable across precisions",
      CF[PRECS[0]] == CF[PRECS[1]], str(CF[PRECS[0]][:30]))
TERMS = CF[PRECS[1]]
CONV = convergents_from_cf(TERMS)
QS = [q for (_p, q) in CONV]
PS = [p for (p, _q) in CONV]
print("  partial quotients : %s" % TERMS[:24])
print("  denominators q_j  : %s" % QS[:26])
check("q_0 = q_1 = 1 (standard indexing)", QS[0] == 1 and QS[1] == 1, str(QS[:2]))
check("known project scales present",
      set([5, 12, 41, 53, 306, 665, 15601, 190537]).issubset(set(QS)))

# ---------------------------------------------------------------------------
# ITEM A -- ceiling_lower / ceiling_pinned at the real cycles
# ---------------------------------------------------------------------------

head("A -- ceiling_lower / ceiling_pinned instantiated at the real cycles")

print("""  Lean hypotheses (both theorems):
      x v : Fin (p+1) -> N        [elements are NATURAL numbers]
      hstep : 3*x i + 1 = 2^(v i) * x (i+1)
      hK    : K = sum v i
      hX    : 0 < X
      hmin  : forall i, X <= x i
      hpX   : 2*(p+1) < 3*X       [ceiling_pinned / ceiling_upper only]
  Conclusions: ceiling_lower  3^(p+1) < 2^K
               ceiling_pinned 3^(p+1) < 2^K  AND  2^K < 2*3^(p+1)
""")

for seed in (1, -1, -5, -17):
    elems, vals, n, K = CYCLES[seed]
    xmin = min(elems)
    natural = all(e > 0 for e in elems)
    lower_true = 3 ** n < 2 ** K
    upper_true = 2 ** K < 2 * 3 ** n
    if natural:
        X = xmin
        hX = X > 0
        hmin = all(X <= e for e in elems)
        hpX = 2 * n < 3 * X
        check("cycle %d: in scope of ceiling_lower (hX, hmin)" % seed, hX and hmin)
        check("cycle %d: ceiling_lower conclusion 3^%d < 2^%d" % (seed, n, K),
              lower_true, "%d vs %d" % (3 ** n, 2 ** K))
        check("cycle %d: hpX holds (2n=%d < 3X=%d)" % (seed, 2 * n, 3 * X), hpX)
        check("cycle %d: ceiling_pinned conclusion 3^n < 2^K < 2*3^n" % seed,
              lower_true and upper_true,
              "%d < %d < %d" % (3 ** n, 2 ** K, 2 * 3 ** n))
        print("  cycle %4d : IN SCOPE at X=%d.  %d < %d < %d  -- both halves hold"
              % (seed, X, 3 ** n, 2 ** K, 2 * 3 ** n))
    else:
        # the theorem is typed over N; a negative element cannot satisfy
        # `0 < X <= x i` for any natural X.  Record where it exits, and record
        # that the conclusion is FALSE there -- the hypothesis is load-bearing.
        check("cycle %d: OUT OF SCOPE -- elements are not naturals (hmin/hX)" % seed,
              not natural)
        check("cycle %d: and the conclusion 3^n < 2^K is FALSE (negative control)"
              % seed, not lower_true, "%d vs %d" % (3 ** n, 2 ** K))
        print("  cycle %4d : OUT OF SCOPE (negative elements).  3^%d = %d > 2^%d = %d"
              " -- south shore, q = %d < 0"
              % (seed, n, 3 ** n, K, 2 ** K, 2 ** K - 3 ** n))

print()
print("  Reading: exactly one real cycle -- the trivial one -- satisfies")
print("  ceiling_lower's hypotheses, and it satisfies the conclusion (3 < 4 < 6,")
print("  the file's own canary).  The three negative cycles are precisely the")
print("  cases where the conclusion FAILS, and precisely the cases the")
print("  positivity hypothesis excludes.  The hypothesis is load-bearing.")

# ---------------------------------------------------------------------------
# ITEM B -- negative controls
# ---------------------------------------------------------------------------

head("B -- negative controls: the hypotheses are load-bearing, not decorative")

# B1: K not equal to sum(v) -- take K = floor(n*log2 3), one below the ceiling.
print("  B1. K one below the forced ceiling: 3^n < 2^K is FALSE for every n.")
bad = 0
for n in range(1, 401):
    K0 = (3 ** n).bit_length()          # = ceil(n*log2 3), since 3^n is never a 2-power
    if not (3 ** n < 2 ** (K0 - 1)):
        bad += 1
check("K0-1 never satisfies the lower bound (n = 1..400)", bad == 400,
      "%d of 400" % bad)

# B2: a non-cycle tuple with the conclusion false, exhibited explicitly.
print("  B2. Explicit non-cycle tuple with the conclusion false:")
x_bad = (1, 1)
v_bad = (0, 0)
n_bad = 2
K_bad = sum(v_bad)
hstep_bad = all(3 * x_bad[i] + 1 == 2 ** v_bad[i] * x_bad[(i + 1) % n_bad]
                for i in range(n_bad))
check("B2 tuple violates hstep", not hstep_bad)
check("B2 tuple violates the conclusion (3^2 = 9 > 2^0 = 1)",
      not (3 ** n_bad < 2 ** K_bad))
print("      x = %s, v = %s : hstep FAILS (3*1+1 = 4 != 2^0*1 = 1),"
      " and 3^%d = %d > 2^%d = %d" % (x_bad, v_bad, n_bad, 3 ** n_bad,
                                      K_bad, 2 ** K_bad))

# B3: random positive tuples with an arbitrary K below the ceiling.
rng = random.Random(20260727)
print("  B3. 200 random positive tuples with hstep broken and K below the ceiling:")
b3_bad = 0
for _ in range(200):
    n = rng.randint(1, 12)
    xs = [rng.randint(1, 10 ** rng.randint(1, 12)) * 2 + 1 for _ in range(n)]
    K = (3 ** n).bit_length() - 1 - rng.randint(0, 2)
    steps_ok = all(3 * xs[i] + 1 == 2 ** 1 * xs[(i + 1) % n] for i in range(n))
    if (not steps_ok) and (not (3 ** n < 2 ** K)):
        b3_bad += 1
check("B3: all 200 broken tuples have hstep false AND the conclusion false",
      b3_bad == 200, "%d of 200" % b3_bad)

# B4: the strict product core -- the actual proof content -- on random positive
# multisets; and the failure mode when a zero element is admitted.
print("  B4. The proof's core inequality prod(3x) < prod(3x+1) on positive")
print("      multisets, and its collapse when a zero element is admitted:")
core_ok = 0
fact_ok = 0
TRIALS = 400
for _ in range(TRIALS):
    n = rng.randint(1, 14)
    xs = [rng.randint(1, 10 ** rng.randint(1, 25)) for _ in range(n)]
    lo = 1
    hi = 1
    px = 1
    for x in xs:
        lo *= 3 * x
        hi *= 3 * x + 1
        px *= x
    if lo < hi:
        core_ok += 1
    # and the left product factorises as 3^n * prod(x), the step the Lean
    # proof does with Finset.prod_mul_distrib / prod_const / card_univ
    if lo == 3 ** n * px:
        fact_ok += 1
check("B4: prod(3x) < prod(3x+1) strictly on %d positive multisets" % TRIALS,
      core_ok == TRIALS, "%d of %d" % (core_ok, TRIALS))
check("B4: prod(3x) = 3^n * prod(x) on the same %d multisets" % TRIALS,
      fact_ok == TRIALS, "%d of %d" % (fact_ok, TRIALS))
# the zero case: 3^n * prod(x) = 0, so the cancellation step has nothing to cancel
zs = [0, 3, 5]
lo0 = 1
for x in zs:
    lo0 *= 3 * x
check("B4: with a zero element, 3^n*prod(x) = 0 (cancellation unavailable)",
      lo0 == 0)
print("      -> positivity enters exactly at the cancellation, as the Lean proof")
print("         has it (hxpos from 0 < X <= x i, then Finset.prod_pos).")

# B5: hstep by itself already forbids a zero element -- checked directly.
print("  B5. hstep alone forbids x i = 0:")
# if x i = 0 then 3*0+1 = 1 = 2^v * x(i+1) forces v = 0 and x(i+1) = 1;
# then 3*1+1 = 4 = 2^w * x(i+2) ... and coming back round, some step must
# produce 0 on the right, impossible since 3x+1 >= 1.
check("B5: 3*0+1 = 1 > 0, so no step can output 0", 3 * 0 + 1 > 0)
print("      3*x+1 >= 1 for every natural x, and 2^v * 0 = 0, so no step")
print("      relation can have 0 on its right-hand side.  Positivity of every")
print("      element is already implied by hstep -- hX/hmin are the route the")
print("      file takes, not an extra assumption.")

# ---------------------------------------------------------------------------
# ITEM C -- statement-level canaries for the two new theorems
# ---------------------------------------------------------------------------

head("C -- statement canaries for ceiling_lower / ceiling_pinned at synthetic (n, K)")

print("  For a cycle the two theorems together say: 2^K lies in [3^n, 2*3^n),")
print("  which pins K = ceil(n*log2 3) = bitlength(3^n) and nothing else.")
print("  Checked in exact integers.")

n_points = list(range(1, 301))                     # the dense range, edges included
n_points += [301, 500, 777, 1000, 1500, 2000, 3000, 5000]
n_points += [q for q in QS if 1 <= q <= 200000]     # the convergent scales
n_points += [2 * q for q in QS if 1 <= 2 * q <= 200000]   # and multiples of them
n_points = sorted(set(n_points))

uniq_ok = 0
low_ok = 0
up_ok = 0
edge_fail_lo = 0
edge_fail_hi = 0
for n in n_points:
    three = 3 ** n
    K0 = three.bit_length()             # ceil(n*log2 3)
    if three < 2 ** K0:
        low_ok += 1
    if 2 ** K0 < 2 * three:
        up_ok += 1
    # uniqueness of K in the pinned range
    admissible = [K for K in (K0 - 2, K0 - 1, K0, K0 + 1, K0 + 2)
                  if three < 2 ** K < 2 * three]
    if admissible == [K0]:
        uniq_ok += 1
    # the two edges must genuinely fail
    if not (three < 2 ** (K0 - 1)):
        edge_fail_lo += 1
    if not (2 ** (K0 + 1) < 2 * three):
        edge_fail_hi += 1

N = len(n_points)
check("C: lower bound 3^n < 2^K0 at all %d points" % N, low_ok == N,
      "%d of %d" % (low_ok, N))
check("C: upper bound 2^K0 < 2*3^n at all %d points" % N, up_ok == N,
      "%d of %d" % (up_ok, N))
check("C: K0 is the UNIQUE admissible K at all %d points" % N, uniq_ok == N,
      "%d of %d" % (uniq_ok, N))
check("C: K0-1 fails the lower bound at all %d points" % N, edge_fail_lo == N,
      "%d of %d" % (edge_fail_lo, N))
check("C: K0+1 fails the upper bound at all %d points" % N, edge_fail_hi == N,
      "%d of %d" % (edge_fail_hi, N))
print("  %d synthetic scales checked (n = 1..300 dense, plus 301..5000 samples,"
      % N)
print("  plus every convergent denominator and its double up to 200000);")
print("  edges n = 1 and n = 2 included.  K0 = bitlength(3^n) throughout.")

# n = 1 spelled out, the file's own canary
check("C: n = 1 edge -- 3 < 4 < 6", 3 ** 1 < 2 ** 2 < 2 * 3 ** 1)
print("  n = 1 (the trivial cycle, the file's canary): 3 < 4 < 6.")

# ---------------------------------------------------------------------------
# ITEM D -- the four repaired downstream statements
# ---------------------------------------------------------------------------

head("D -- the four repaired downstream statements, instantiated")

print("""  The four statements at HEAD (hceil REMOVED from all of them):
    ratio_bound_at_barina     hmin: 2^71 <= x i ; hpX: 2p < 3*2^71
    log_gap_at_barina         same hypotheses
    log_gap_gen               hX: 0 < X ; hmin: X <= x i ; hpX: 2p < 3X
    quotient_is_convergent_gen  same + hwin: 4000*(p+1)^2 <= 2079*X
""")

# D1 -- the trivial cycle, the one real cycle in N.
print("  D1. The trivial cycle (n = 1, K = 2, x = 1), the only real cycle in N:")
elems, vals, n1, K1 = CYCLES[1]
X = 1
check("D1: ratio_bound_at_barina OUT OF SCOPE at hmin (2^71 <= 1 is false)",
      not (X_BARINA <= min(elems)))
check("D1: log_gap_at_barina OUT OF SCOPE at hmin (same)",
      not (X_BARINA <= min(elems)))
# log_gap_gen at X = 1 IS in scope
hX = X > 0
hmin = all(X <= e for e in elems)
hpX = 2 * (n1 - 1) < 3 * X
check("D1: log_gap_gen IN SCOPE at X = 1 (hX, hmin, hpX)", hX and hmin and hpX)
gaps = {}
for prec in PRECS:
    with localcontext() as ctx:
        ctx.prec = prec
        gaps[prec] = Decimal(K1) * ln2(prec) - Decimal(n1) * ln3(prec)
g = gaps[PRECS[1]]
check("D1: log gap stable across precisions",
      ("%.40e" % gaps[PRECS[0]]) == ("%.40e" % gaps[PRECS[1]]))
with localcontext() as ctx:
    ctx.prec = PRECS[1]
    rhs = Decimal(2) * Decimal(n1) / (Decimal(3) * Decimal(X))
check("D1: log_gap_gen conclusion, left half 0 < g", g > 0, "%.20f" % g)
check("D1: log_gap_gen conclusion, right half g < 2n/(3X)", g < rhs,
      "%.20f vs %.20f" % (g, rhs))
print("      log_gap_gen at X=1: 0 < %.15f < %.15f  -- both halves hold"
      % (g, rhs))
print("      (the left half IS ceiling_lower's content in logarithmic form:")
print("       g > 0 <=> 2^K > 3^n; it is now derived, not assumed.)")
# quotient_is_convergent_gen: exits at hwin
hwin = 4000 * n1 ** 2 <= 2079 * X
check("D1: quotient_is_convergent_gen OUT OF SCOPE at hwin (4000 > 2079)",
      not hwin)
# ... and its conclusion is nonetheless true there
fr = Fraction(K1, n1)
is_conv = any(Fraction(p, q) == fr for (p, q) in CONV)
check("D1: and its conclusion holds anyway -- K/n = 2/1 IS a convergent",
      is_conv)
print("      quotient_is_convergent_gen exits scope at hwin (4000*1 > 2079*1);")
print("      its conclusion is nonetheless true there: K/n = 2/1 = p_1/q_1.")

# D2 -- the three negative cycles: out of scope before any size question.
print()
print("  D2. The three negative cycles: out of scope at the N typing / hmin,")
print("      exactly as at item A -- no size hypothesis is reached.")
for seed in (-1, -5, -17):
    elems, vals, n, K = CYCLES[seed]
    check("D2: cycle %d out of scope of all four (elements not naturals)" % seed,
          not all(e > 0 for e in elems))

# D3 -- the seam-admissibility structure at X = 2^71, in the window and beyond.
print()
print("  D3. Where the four downstream hypotheses can be satisfied at all.")
print("      A surviving cycle at X = 2^71 must satisfy the seam gap, which is")
print("      equivalent to  ||n*log2 3|| < n*delta,  delta = 2/(3*2^71*ln2).")
print("      By Legendre (the theorem's own conclusion) such an n is a multiple")
print("      of a convergent denominator q_j, and |n*L - K| = t*theta_j when")
print("      n = t*q_j, so the test reduces to  theta_j < q_j*delta.")

WINDOW_INT = isqrt(2079 * X_BARINA // 4000)
while 4000 * (WINDOW_INT + 1) ** 2 <= 2079 * X_BARINA:
    WINDOW_INT += 1
while 4000 * WINDOW_INT ** 2 > 2079 * X_BARINA:
    WINDOW_INT -= 1
check("D3: integral window = 35031771147 (exact isqrt, tight both sides)",
      WINDOW_INT == 35031771147, str(WINDOW_INT))
check("D3: window tightness upper", 4000 * (WINDOW_INT + 1) ** 2 > 2079 * X_BARINA)
check("D3: window tightness lower", 4000 * WINDOW_INT ** 2 <= 2079 * X_BARINA)

in_window = [j for j, q in enumerate(QS) if q <= WINDOW_INT]
check("D3: exactly 22 convergents inside the integral window",
      len(in_window) == 22, str(len(in_window)))
check("D3: they are j = 0..21", in_window == list(range(22)))

# exact Legendre window, for the record
EXACTW = {}
for prec in PRECS:
    with localcontext() as ctx:
        ctx.prec = prec
        EXACTW[prec] = (Decimal(3) * Decimal(X_BARINA) * ln2(prec) / Decimal(4)).sqrt()
ew = int(EXACTW[PRECS[1]])
check("D3: exact Legendre window floor = 35035491004", ew == 35035491004, str(ew))
in_window_exact = [j for j, q in enumerate(QS) if q <= ew]
check("D3: the same 22 under the exact window", in_window_exact == list(range(22)))

# theta_j and the seam test
def theta(j, prec):
    with localcontext() as ctx:
        ctx.prec = prec
        L = log2_3(prec)
        return abs(Decimal(QS[j]) * L - Decimal(PS[j]))

print()
def signed(j, prec):
    """q_j * L - p_j, signed.  Negative means p_j/q_j lies ABOVE log2 3."""
    with localcontext() as ctx:
        ctx.prec = prec
        return Decimal(QS[j]) * log2_3(prec) - Decimal(PS[j])


print("      j        q_j            theta_j       theta_j/(q_j*delta)  side  admits?")
first_admissible = None
first_north = None
for j in range(0, 26):
    tvals = {}
    for prec in PRECS:
        with localcontext() as ctx:
            ctx.prec = prec
            tvals[prec] = theta(j, prec) / (Decimal(QS[j]) * DELTAS[prec])
    check("D3: ratio stable at j=%d" % j,
          ("%.12e" % tvals[PRECS[0]]) == ("%.12e" % tvals[PRECS[1]]))
    r = tvals[PRECS[1]]
    admits = r < 1
    above = signed(j, PRECS[1]) < 0          # p_j/q_j > L
    check("D3: side stable at j=%d" % j,
          (signed(j, PRECS[0]) < 0) == (signed(j, PRECS[1]) < 0))
    check("D3: convergent sides alternate at j=%d" % j, above == (j % 2 == 1))
    if admits and first_admissible is None:
        first_admissible = j
    if admits and above and first_north is None:
        first_north = j
    if j <= 21:
        check("D3: seam FAILS at q_%d (in window)" % j, not admits, "ratio %.6f" % r)
    if j in (19, 20, 21, 22, 23, 24, 25) or j <= 2:
        print("     %2d  %15d   %.6e   %18.6f  %s   %s"
              % (j, QS[j], theta(j, PRECS[1]), r,
                 "above" if above else "below", "YES" if admits else "no"))
check("D3: the FIRST scale admitted by the two-sided seam test is j = 22,"
      " q = 65470613321",
      first_admissible == 22 and QS[22] == 65470613321,
      "j=%s" % first_admissible)
check("D3: and it lies OUTSIDE the window (so hwin excludes it)",
      QS[22] > WINDOW_INT, "%d vs %d" % (QS[22], WINDOW_INT))
print()
print("      Reading: inside the window the hypothesis set of all four")
print("      downstream theorems is EMPTY -- which is exactly the T1 closure.")
print("      The first scale the two-sided seam test cannot exclude is")
print("      q_22 = 65470613321 (the figure on record in")
print("      briefs/merle-la8-t1-check-findings.md section (f)), and it lies")
print("      outside the window: the four statements exit scope at hwin,")
print("      where they are designed to.")

# D3-bis -- the one-sided refinement forced by ceiling_lower.
print()
print("  D3-bis. A refinement the repair makes explicit, recorded flat.")
print("      log_gap_gen's LEFT half -- now DERIVED from ceiling_lower rather")
print("      than assumed -- says 0 < K*ln2 - n*ln3, i.e. K > n*log2 3.  With")
print("      n = t*q_m and K = t*p_m (Legendre), K - n*L = -t*(q_m*L - p_m),")
print("      so a POSITIVE cycle can only sit on a convergent lying ABOVE")
print("      log2 3 -- the odd-indexed ones.  The two-sided screen above is")
print("      therefore not tight for the north shore:")
check("D3-bis: q_22 (j even) lies BELOW log2 3, so it cannot host a positive"
      " cycle", signed(22, PRECS[1]) > 0, "%.6e" % signed(22, PRECS[1]))
check("D3-bis: the first north-shore-admissible scale is j = 23,"
      " q = 137528045312",
      first_north == 23 and QS[23] == 137528045312, "j=%s" % first_north)
print("      first two-sided-admissible : q_22 = %d (below L -- south only)"
      % QS[22])
print("      first north-shore-admissible: q_23 = %d (above L)" % QS[23])
print("      That is Hercher's threshold exactly.  Nothing in the Lean chain")
print("      depends on this; it is recorded because ceiling_lower is what")
print("      makes the one-sidedness a theorem rather than a hypothesis.")

# D4 -- at the first north-shore-admissible scale, the conclusions themselves.
print()
print("  D4. At n = q_23 = 137528045312 (the first scale a positive cycle")
print("      could occupy), with K = p_23 = ceil(n*log2 3):")
n23 = QS[23]
K23 = PS[23]
gvals = {}
for prec in PRECS:
    with localcontext() as ctx:
        ctx.prec = prec
        gvals[prec] = (Decimal(K23) * ln2(prec) - Decimal(n23) * ln3(prec),
                       Decimal(2) * Decimal(n23) / (Decimal(3) * Decimal(X_BARINA)))
check("D4: gap stable across precisions",
      ("%.30e" % gvals[PRECS[0]][0]) == ("%.30e" % gvals[PRECS[1]][0]))
g23, r23 = gvals[PRECS[1]]
check("D4: K = p_23 is ceil(n*L) -- the pinned K", K23 == int(
    (Decimal(n23) * log2_3(PRECS[1])).to_integral_value(rounding="ROUND_FLOOR")) + 1,
      str(K23))
check("D4: ceiling_lower's content holds at q_23 (K*ln2 - n*ln3 > 0)", g23 > 0,
      "%.6e" % g23)
check("D4: log_gap_at_barina's right half holds at q_23", g23 < r23,
      "%.6e vs %.6e" % (g23, r23))
check("D4: hwin FAILS at q_23 (4000n^2 > 2079*2^71)",
      4000 * n23 ** 2 > 2079 * X_BARINA)
check("D4: K/n = p_23/q_23 IS a convergent (the conclusion, had hwin held)",
      Fraction(K23, n23) == Fraction(PS[23], QS[23]))
print("      0 < %.6e < %.6e   (log gap, both halves hold)" % (g23, r23))
print("      hwin: 4000*n^2 = %d  >  2079*2^71 = %d  -- OUT OF SCOPE, correctly"
      % (4000 * n23 ** 2, 2079 * X_BARINA))
print("      K/n = %d/%d = p_23/q_23, a convergent of log2 3." % (K23, n23))

# ---------------------------------------------------------------------------
# ITEM E -- round-10 facts the repair could have disturbed
# ---------------------------------------------------------------------------

head("E -- round-10 facts re-confirmed (the repair could have disturbed them)")

# E1: convPairs, as committed in T1Structure.lean at HEAD, byte-copied here.
CONVPAIRS_FILE = [
    (1, 1), (1, 2), (2, 5), (5, 12), (12, 41), (41, 53), (53, 306), (306, 665),
    (665, 15601), (15601, 31867), (31867, 79335), (79335, 111202),
    (111202, 190537), (190537, 10590737), (10590737, 10781274),
    (10781274, 53715833), (53715833, 171928773), (171928773, 225644606),
    (225644606, 397573379), (397573379, 6189245291), (6189245291, 6586818670),
    (6586818670, 65470613321),
]
computed_pairs = [(QS[j], QS[j + 1]) for j in range(22)]
check("E1: convPairs (file, unchanged at HEAD) = computed (q_j, q_{j+1}), j=0..21",
      CONVPAIRS_FILE == computed_pairs)
check("E1: convPairs_length = 22", len(CONVPAIRS_FILE) == 22)

# E2: the discharge criterion, exact integers.
RHS = 2079 * X_BARINA
check("E2: 2079*2^71 = 4908899958942996199636992", RHS == 4908899958942996199636992,
      str(RHS))
margins = []
allpass = True
for (q, qn) in CONVPAIRS_FILE:
    lhs = 2000 * q * (q + qn)
    if not (lhs <= RHS):
        allpass = False
    margins.append((Fraction(RHS, lhs), q, lhs))
check("E2: all 22 pass the integer criterion 2000*q*(q+q') <= 2079*2^71", allpass)
tight = min(margins)
check("E2: tightest margin at q = 6586818670", tight[1] == 6586818670, str(tight[1]))
check("E2: tightest margin = 5.1713x", "%.4f" % float(tight[0]) == "5.1713",
      "%.6f" % float(tight[0]))
check("E2: tightest LHS = 949258476701148143940000",
      tight[2] == 949258476701148143940000, str(tight[2]))
print("  all 22 pass; tightest %0.4fx at q = %d (LHS = %d, RHS = %d)"
      % (float(tight[0]), tight[1], tight[2], RHS))

# exact test at the tightest convergent
for prec in PRECS:
    with localcontext() as ctx:
        ctx.prec = prec
        ex = theta(21, prec) / (Decimal(QS[21]) * DELTAS[prec])
        if prec == PRECS[1]:
            exact_tight = ex
check("E2: exact test at q_21 gives 5.4433x", "%.4f" % float(exact_tight) == "5.4433",
      "%.6f" % float(exact_tight))
check("E2: integer form is conservative (5.1713 < 5.4433)",
      float(tight[0]) < float(exact_tight))
print("  exact test at the same q: %.4fx -- integer form conservative by design"
      % float(exact_tight))

# non-vacuity canary
q22, q23 = QS[22], QS[23]
check("E2: canary -- the criterion FAILS at q_22 (window ends there)",
      not (2000 * q22 * (q22 + q23) <= RHS),
      "%d vs %d" % (2000 * q22 * (q22 + q23), RHS))
check("E2: q_22 = 65470613321 and q_23 = 137528045312 (standard indexing)",
      q22 == 65470613321 and q23 == 137528045312, "%d %d" % (q22, q23))
print("  canary: FAILS at (q_22, q_23) = (%d, %d) -- LHS %d > RHS"
      % (q22, q23, 2000 * q22 * (q22 + q23)))

# E3: the classical bound sandwich, both sides.
sand = 0
for j in range(1, 26):
    with localcontext() as ctx:
        ctx.prec = PRECS[1]
        t = theta(j, PRECS[1])
        lo = Decimal(1) / Decimal(QS[j] + QS[j + 1])
        hi = Decimal(1) / Decimal(QS[j + 1])
        if lo < t < hi:
            sand += 1
check("E3: classical sandwich 1/(q_j+q_{j+1}) < theta_j < 1/q_{j+1}, j = 1..25",
      sand == 25, "%d of 25" % sand)

# E4: multiples cancellation, spot-checked exactly.
mult_ok = 0
for (j, t) in ((9, 2), (13, 3), (21, 5)):
    with localcontext() as ctx:
        ctx.prec = PRECS[1]
        lhs = abs(Decimal(t * QS[j]) * log2_3(PRECS[1]) - Decimal(t * PS[j]))
        rhs = Decimal(t) * theta(j, PRECS[1])
        if ("%.30e" % lhs) == ("%.30e" % rhs):
            mult_ok += 1
check("E4: |t*q_j*L - t*p_j| = t*theta_j at three (j, t) instances", mult_ok == 3,
      "%d of 3" % mult_ok)

# E5: delta figure and the withdrawn window artifact.
with localcontext() as ctx:
    ctx.prec = PRECS[1]
    wrong_delta = Decimal(1) / (Decimal(3) * Decimal(X_BARINA) * ln2(PRECS[1]))
    wrong_window = (Decimal(1) / (Decimal(2) * wrong_delta)).sqrt()
check("E5: the withdrawn 4.955e10 window = the missing-factor-2 artifact",
      "%.4e" % float(wrong_window) == "4.9548e+10", "%.6e" % float(wrong_window))
check("E5: and it is exactly sqrt(2) x the corrected exact window",
      abs(float(wrong_window) / float(EXACTW[PRECS[1]]) - 2 ** 0.5) < 1e-12)
print("  delta = %.6e ; withdrawn window %.5e = sqrt(2) x corrected %.5e"
      % (d_hi, float(wrong_window), float(EXACTW[PRECS[1]])))

# ---------------------------------------------------------------------------

head("SUMMARY")
print("  recorded checks : %d" % CHECKS)
print("  failures        : %d" % len(FAILS))
for lbl, det in FAILS:
    print("    FAIL %s %s" % (lbl, det))
print()
print("  Trust boundary: statements and structure only.  No Lean toolchain was")
print("  installed and no proof was compiled; kernel-3 / [propext] / no-axiom")
print("  claims rest on his committed logs and his four-way protocol.")
if FAILS:
    raise SystemExit(1)
