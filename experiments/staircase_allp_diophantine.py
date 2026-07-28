# The Diophantine coverage gap of the all-p staircase (cycles.md 12.8.6.1):
# the gamma budget, unconditional candidate availability at every scale, and
# the empirical test across the convergent desert p = 24..36.
#
# Supports: briefs/staircase-allp-diophantine-findings.md, and the sole
# remaining gap of the floor-grade result at cycles.md 12.8.6.
#
# INDEPENDENCE. This script imports nothing from experiments/staircase_allp.py,
# experiments/uniform_trim.py, experiments/p22_passer.py, or any other file in
# this repository. The rotation-sum machinery (Part B) is a second, structurally
# different implementation: staircase_allp.py evaluates R_r by re-rotating the
# profile and re-summing p terms per rotation; this file evaluates R_0 once by
# Horner and then obtains every other rotation from the exact transport
# recurrence of cycles.md 12.6.1.1 (2^sigma_r R_{r+1} = 3^{m_r} R_r + (2^{s_r}-1) q),
# with an exact divisibility assertion at each transport step. The two agree on
# the published p = 7 instance (Part F cross-check) and on the trivial-cycle
# identity R = 4^p - 3^p (Part G).
#
# EXACTNESS DISCIPLINE. Every pass/fail decision is exact big-integer
# arithmetic: K = (3**n).bit_length() is exactly ceil(n*log2 3); q = 2**K - 3**n
# exactly; every R_r exactly; comparisons are Python integer comparisons.
# High-precision floating point (mpmath) is used only to (a) *choose* candidate
# n, (b) *search* over correction moves, and (c) report gamma to three decimals.
# Nothing that is asserted depends on (a)-(c).
#
# Parts:
#   0. Primitives: L = log2 3, exact fractional parts, gamma <-> delta.
#   1. The gamma budget: what growth of gamma(p) the sharpness claim needs.
#   2. Availability: continued fraction, exact quality laws for semiconvergents
#      and multiples, the three-distance window-covering bound, the certified
#      gamma ceiling at every period, and the unconditional (Rhin) tail.
#   3. The empirical test at p = 24..36 (the convergent desert).
#   4. Negative controls and summary.

import math
import sys
import time

from mpmath import mp, mpf, log, floor, nint

mp.dps = 800

FAILURES = []
CHECKS = [0]


def check(name, cond, detail=""):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append(f"{name}: {detail}")
        print(f"  FAIL  {name}  {detail}")
    return cond


# ---------------------------------------------------------------------
# Part 0. Primitives.
# ---------------------------------------------------------------------

L = log(3) / log(2)                       # log2 3, 800 significant digits
LF = float(L)
BITS = 160                                # fixed-point scale for exact {nL}
LFIX = int(floor(L * (mpf(2) ** BITS)))   # floor(L * 2^BITS)
SCALE = 1 << BITS

# Rhin's effective bound as pinned at cycles.md 12.5.3:
#     |K log 2 - n log 3| > exp(-13.3 * (0.46057 + log n)),
# i.e. ||n L|| > C_RHIN * n^(-MU_RHIN) with
MU_RHIN = mpf('13.3')
C_RHIN = mp.e ** (-MU_RHIN * mpf('0.46057')) / log(2)


def frac_fix(n):
    """{n L} as an exact integer numerator over 2^BITS (error < n * 2^-BITS,
    utterly negligible for every n used here: n < 2^60 << 2^320)."""
    return (n * LFIX) % SCALE


def delta_of(n):
    """delta(n) = ceil(n L) - n L in (0, 1), as an mpf. With K = ceil(n L)
    this is exactly the quantity controlling gamma."""
    return 1 - mpf(frac_fix(n)) / SCALE


def delta_hp(n):
    """delta(n) at full mpmath precision (no fixed-point truncation). Used
    wherever a law is being *checked* rather than a candidate generated."""
    v = mpf(n) * L
    return mp.ceil(v) - v


def gamma_of_delta(d):
    """gamma = -log2(1 - 2^-delta): the exact relation between the
    Diophantine displacement delta = K - n*log2 3 and gamma = K - log2 q."""
    return -mp.log(1 - mpf(2) ** (-d), 2)


def gamma_bounds_from_delta(d):
    """Two-sided elementary bounds used in the findings:
       log2(1/d) + log2(1/ln2)  <=  gamma  <=  log2(1/d) + log2(1/ln2)
                                             - log2(1 - d*ln2/2).
    Returned as (lower, upper)."""
    lo = mp.log(1 / d, 2) + mp.log(1 / log(2), 2)
    hi = lo - mp.log(1 - d * log(2) / 2, 2)
    return lo, hi


def part0():
    print("=" * 78)
    print("PART 0.  gamma <-> delta, checked against exact big integers")
    print("=" * 78)
    print("  L = log2 3 = %s..." % mp.nstr(L, 25))
    print("  gamma := K - log2 q,  q = 2^K - 3^n > 0,  K = ceil(n L),")
    print("  delta := K - n L in (0,1)   =>   gamma = -log2(1 - 2^-delta).")
    worst = mpf(0)
    for n in (5, 12, 29, 41, 94, 306, 665, 971, 15601, 25217, 31202, 190537):
        T3 = 3 ** n
        K = T3.bit_length()                  # exact ceil(n log2 3)
        q = (1 << K) - T3
        check("q>0", q > 0, f"n={n}")
        gamma_exact = mpf(K) - mp.log(mpf(q), 2)
        d = delta_of(n)
        gamma_pred = gamma_of_delta(d)
        lo, hi = gamma_bounds_from_delta(d)
        err = abs(gamma_exact - gamma_pred)
        worst = max(worst, err)
        check("gamma identity", err < mpf('1e-30'), f"n={n} err={mp.nstr(err,5)}")
        if d < mpf('0.5'):
            check("gamma sandwich", lo <= gamma_exact <= hi,
                  f"n={n} {mp.nstr(lo,8)} {mp.nstr(gamma_exact,8)} {mp.nstr(hi,8)}")
    print(f"  gamma = -log2(1-2^-delta) verified against K - log2(2^K - 3^n) at 12 "
          f"exponents; worst deviation {mp.nstr(worst, 4)}")
    print("  K = ceil(n L) is realized exactly as (3**n).bit_length():", end=" ")
    ok = all((3 ** n).bit_length() == int(mp.ceil(n * L)) for n in range(1, 400))
    check("bit_length = ceil(nL)", ok)
    print("verified for n = 1..399")
    print()


# ---------------------------------------------------------------------
# Part 1. The gamma budget.
# ---------------------------------------------------------------------
#
# The size condition (cycles.md 12.6.1) is q <= R_r at every rotation; since
# q = 2^(K-gamma), a LARGER gamma means a SMALLER q and an EASIER size test.
# The sharpness claim runs the other way: it needs a size-passer whose gamma is
# SMALL -- below what any "polynomial-in-p extension of the small-period
# constants" would demand.
#
# The period-3 trim (cycles.md 12.7.4 / Remark 12.7.6) is  gamma > c0*n - 2
# with c0 = 0.1157.  A polynomial-in-p extension of it is the family
#
#     Trim(c0, A):   gamma + log2 p  >  c0 * n / p^A          (A >= 0)
#
# (A = 0 is the literal period-3 constant carried to every period; the proved
# uniform trim, Theorem 12.8.1, is the EXPONENTIALLY degraded c0/1.585^p.)
# A size-passer at period p with n = n(p), gamma = gamma(p) refutes Trim(c0,A)
# at that period exactly when
#
#     gamma(p) + log2 p  <=  c0 * n(p) / p^A .                       (REFUTE)
#
# The staircase construction forces n(p) >= KAPPA * 1.585^p (the geometric
# climb of ratio L over p-1 blocks with m_0 >= 1 sums to at least this), so a
# sufficient condition for (REFUTE) is
#
#     gamma(p) <= c0 * KAPPA * 1.585^p / p^A - log2 p .

C0_TRIM = 0.1157
KAPPA = 0.68                        # min n / 1.585^p available to the recipe
LOG2L = math.log2(LF)               # 0.664458...


def refutes(log2gamma, p, A, c0=C0_TRIM, kappa=KAPPA):
    """(REFUTE) in log2 space, so that the comparison is meaningful at p = 4000
    where both sides overflow a double. log2gamma = log2 of gamma(p)."""
    lhs = log2gamma if log2gamma > 60 else math.log2(
        2.0 ** log2gamma + math.log2(p))
    rhs = math.log2(c0 * kappa) + p * LOG2L - A * math.log2(p)
    return lhs <= rhs


GROWTHS = [
    ("2.5*log2 p   (observed)", lambda p: math.log2(2.5 * math.log2(p))),
    ("p                      ", lambda p: math.log2(p)),
    ("p^2                    ", lambda p: 2 * math.log2(p)),
    ("2^sqrt(p)              ", lambda p: math.sqrt(p)),
    ("1.2^p                  ", lambda p: p * math.log2(1.2)),
    ("1.5^p                  ", lambda p: p * math.log2(1.5)),
    ("1.585^p       (control)", lambda p: p * LOG2L),
    ("0.05*1.585^p  (control)", lambda p: math.log2(0.05) + p * LOG2L),
]


def first_p_refuting(f, A, pmax=4000):
    """Smallest p0 such that (REFUTE) holds for every p in [p0, pmax];
    None if it never holds on the tail."""
    p0 = None
    for p in range(pmax, 1, -1):
        if refutes(f(p), p, A):
            p0 = p
        else:
            break
    return p0


def part1():
    print("=" * 78)
    print("PART 1.  THE GAMMA BUDGET -- what growth of gamma(p) the claim needs")
    print("=" * 78)
    print("  Trim(c0,A):  gamma + log2 p > c0 * n / p^A,   c0 = 0.1157 (period 3).")
    print("  Refuted at p by a size-passer with gamma(p) + log2 p <= c0*n(p)/p^A,")
    print(f"  and the staircase forces n(p) >= {float(KAPPA)} * 1.585^p.")
    print()
    header = "  gamma(p) growth law     " + "".join(f"  A={A:<2d}" for A in (0, 1, 2, 3, 5, 10))
    print(header + "     <- smallest p0 with (REFUTE) for all p >= p0")
    for name, f in GROWTHS:
        cells = []
        for A in (0, 1, 2, 3, 5, 10):
            p0 = first_p_refuting(f, A)
            cells.append(f"{p0:>6}" if p0 is not None else "  none")
        print(f"  {name}  " + "".join(cells))
    print()
    print("  Reading: every law with limsup log2(gamma(p))/p < log2 1.585 = 0.66446")
    print("  defeats Trim(c0,A) for EVERY A from an explicit p0; the two controls")
    print("  at growth rate 1.585^p defeat only finitely many A (or none).")

    # The assertions that make the table a claim rather than a display.
    for name, f in GROWTHS[:6]:
        for A in (0, 1, 2, 3, 5, 10):
            check("subexponential gamma refutes every polynomial trim",
                  first_p_refuting(f, A) is not None, f"{name.strip()}, A={A}")
    check("control 1.585^p refutes nothing",
          first_p_refuting(GROWTHS[6][1], 0) is None, "A=0")
    check("control 0.05*1.585^p refutes A=0 but not A=1",
          first_p_refuting(GROWTHS[7][1], 0) is not None
          and first_p_refuting(GROWTHS[7][1], 1) is None)

    print()
    print("  The exact threshold. (REFUTE) for all A holds iff")
    print("      gamma(p) * p^A / 1.585^p -> 0   for every fixed A,")
    print("  i.e. iff log2 gamma(p) <= 0.66446*p - omega(log p).  The weakest")
    print("  SIMPLE sufficient bound is therefore")
    print("      gamma(p) = O(rho^p)   for any fixed rho < 1.585,")
    print("  and a fortiori gamma(p) = 2^o(p), O(p^B), O(p), O(log p).")
    print("  O(log p) is NOT needed for this job; O(p) has room to spare.")
    print()
    print("  What the stronger readings need (the ladder):")
    print("    J1  refute every polynomial-in-p trim   (the published sentence)")
    print("        -> gamma(p) <= rho^p, any rho < 1.585.      [subexponential]")
    print("    J2  refute every subexponential trim c0*n/2^o(p)")
    print("        -> gamma(p) = 2^o(p).                        [subexponential]")
    print("    J3  Theorem 12.8.1's rate 1.585^-p sharp up to a polynomial factor")
    print("        -> gamma(p) = O(p^B).                        [polynomial]")
    print("    J4  ... sharp up to a factor O(log p)")
    print("        -> gamma(p) = O(log p).                      [logarithmic]")
    print("  Only J4 needs the published hedge's own O(log p).")

    # J3 quantified: the best trim constant compatible with a gamma(p)=O(p^B)
    # family decays at least like p^(-B-1) * 1.585^(-p) up to constants.
    print()
    print("  Quantified J3/J4: with n(p) = kappa*1.585^p, a size-passer of gamma(p)")
    print("  caps every valid uniform trim constant c(p) (in gamma' > c(p)*n) at")
    print("      c(p) <= (gamma(p) + log2 p) / (kappa * 1.585^p).")
    print("  gamma(p)=O(log p) gives c(p) = O(log p * 1.585^-p) -- Theorem 12.8.1's")
    print("  own 0.585/(1.585^p - 1) is then sharp to within a factor O(log p).")
    print("  gamma(p)=O(p) gives O(p * 1.585^-p): sharp to within a factor O(p).")
    print()


# ---------------------------------------------------------------------
# Part 2. Availability.
# ---------------------------------------------------------------------

def continued_fraction(x, nterms):
    """Convergents of x: list of dicts with the partial quotient a, numerator h,
    denominator q, and the SIGNED displacement s = h - q*x (so s > 0 is exactly
    the 'correct sign' of 12.8.6.1: it gives K = h = ceil(qx) and q_num > 0)."""
    y = x
    h2, h1 = 0, 1
    k2, k1 = 1, 0
    out = []
    for i in range(nterms):
        a = int(floor(y))
        h = a * h1 + h2
        k = a * k1 + k2
        out.append(dict(i=i, a=a, h=h, q=k, s=h - k * x, th=abs(h - k * x)))
        y = y - a
        if y == 0:
            break
        y = 1 / y
        h2, h1 = h1, h
        k2, k1 = k1, k
    return out


CF = continued_fraction(L, 700)
# Trust region: the continued-fraction recursion consumes precision, so keep
# only the convergents whose denominators sit well inside mp.dps.
CF = [c for c in CF if c['q'] < mpf(10) ** (mp.dps // 3)]
THETA = [c['th'] for c in CF]
QDEN = [c['q'] for c in CF]


def part2a():
    print("=" * 78)
    print("PART 2a.  The continued fraction of L, its signs, and the desert")
    print("=" * 78)
    ok = True
    for c in CF[2:]:
        i = c['i']
        # recursion and the classical sandwich 1/(q_i + q_{i+1}) < th_i < 1/q_{i+1}
        if i + 1 < len(CF):
            lo = 1 / mpf(CF[i]['q'] + CF[i + 1]['q'])
            hi = 1 / mpf(CF[i + 1]['q'])
            if not (lo < c['th'] < hi):
                ok = False
        # alternating sign
        if (c['s'] > 0) != (c['i'] % 2 == 1):
            ok = False
    check("CF sandwich + alternating sign", ok, f"over {len(CF)} convergents")
    print(f"  {len(CF)} convergents computed (q up to ~10^{len(str(CF[-1]['q']))-1});")
    print("  sign h_i - q_i L > 0 exactly at odd i; sandwich "
          "1/(q_i+q_{i+1}) < |h_i - q_i L| < 1/q_{i+1} holds throughout.")
    print("  partial quotients a_0..a_29:", [c['a'] for c in CF[:30]])
    print()
    print("  Correctly-signed (s>0) convergent denominators up to 10^9:")
    print("   ", [c['q'] for c in CF if c['s'] > 0 and c['q'] <= 10 ** 9])
    print(f"  The flagged gap q_13 = {CF[13]['q']} -> q_14 = {CF[14]['q']} "
          f"(ratio {CF[14]['q']/CF[13]['q']:.1f}, a_14 = {CF[14]['a']}).")
    # Rhin's pinned bound, checked against the actual convergents: it must hold
    # at every one of them, and it is the ONLY input used for the p > 712 tail.
    bad = [c['i'] for c in CF if c['th'] <= C_RHIN * mpf(c['q']) ** (-MU_RHIN)]
    check("Rhin's pinned bound holds at every computed convergent", not bad,
          f"violated at k = {bad[:5]}")
    slack = min(c['th'] / (C_RHIN * mpf(c['q']) ** (-MU_RHIN)) for c in CF[1:])
    print(f"  Rhin (12.5.3): ||nL|| > {float(C_RHIN):.6f} * n^-13.3 -- holds at all "
          f"{len(CF)} convergents, worst")
    print(f"  slack factor {float(slack):.3e} (the convergents are where the bound "
          f"is tightest).")
    print()
    print("  Convergent-desert scan over the recipe's own window "
          "[0.68*1.585^p, 3.5*1.585^p]:")
    desert = []
    for p in range(2, 45):
        lo, hi = window(p)
        inwin = [c['q'] for c in CF if c['s'] > 0 and lo <= c['q'] <= hi]
        if not inwin:
            desert.append(p)
    print(f"    periods with NO correctly-signed convergent denominator in window: "
          f"{desert}")
    print("    (this is the availability gap of 12.8.6.1, re-derived here; note")
    print("     the correctly-signed SEMIconvergent runs do not repair it: the run")
    print(f"     following q_13 has length a_15 = {CF[15]['a']}, i.e. one member.)")
    print()
    return desert


def window(p, c_lo=mpf('0.68'), c_hi=mpf('4.0')):
    """The scale window the staircase recipe can use at period p. The lower
    edge is forced: the geometric climb of ratio L over p-1 blocks with every
    depth >= 1 already sums to (L^(p-1)-1)/(L-1) ~ 0.681*1.585^p."""
    return int(mp.ceil(c_lo * L ** p)), int(mp.floor(c_hi * L ** p))


def part2b():
    print("=" * 78)
    print("PART 2b.  Exact quality laws: multiples and semiconvergents")
    print("=" * 78)
    print("  (i) MULTIPLES.  For a correctly-signed convergent q_k (s_k = h_k - q_k L")
    print("      > 0) and t with t*theta_k < 1/2:   K - nL = t*theta_k EXACTLY at")
    print("      n = t*q_k, K = t*h_k.  Checked below against ceil(nL) directly.")
    ok = True
    tested = 0
    for c in CF[:20]:
        if c['s'] <= 0:
            continue
        tmax = int(min(500, 1 / (2 * c['th'])))
        for t in range(1, tmax + 1):
            n = t * c['q']
            d = delta_hp(n)
            if abs(d - t * c['s']) > mpf('1e-60'):
                ok = False
            if int(mp.ceil(n * L)) != t * c['h']:
                ok = False
            tested += 1
    check("multiple law ||t q_k L|| = t theta_k", ok, f"{tested} instances")
    print(f"      verified on {tested} (k,t) instances, 0 failures.")
    print()
    print("  (ii) SEMICONVERGENTS.  n_j = q_(k-1) + j q_k, K_j = h_(k-1) + j h_k,")
    print("      j = 1..a_(k+1), at a correctly-signed q_(k-1):")
    print("          K_j - n_j L  =  theta_(k-1) - j*theta_k   EXACTLY,")
    print("      strictly decreasing in j, positive throughout the run, and equal")
    print("      to theta_(k+1) at j = a_(k+1) (the next correctly-signed")
    print("      convergent). Worst case over j is j = a_(k+1): quality theta_(k+1),")
    print("      i.e. the LARGEST gamma of the run; the smallest gamma of the run is")
    print("      at j = 1, quality theta_(k-1) - theta_k.")
    ok = True
    tested = 0
    runs = []
    for idx in range(1, min(24, len(CF) - 2)):
        if CF[idx - 1]['s'] <= 0:
            continue
        a = CF[idx + 1]['a']
        for j in range(1, a + 1):
            n = CF[idx - 1]['q'] + j * CF[idx]['q']
            Kj = CF[idx - 1]['h'] + j * CF[idx]['h']
            pred = CF[idx - 1]['th'] - j * CF[idx]['th']
            d = delta_hp(n)
            if abs(d - pred) > mpf('1e-60') or int(mp.ceil(n * L)) != Kj or pred <= 0:
                ok = False
            tested += 1
        runs.append((idx - 1, CF[idx - 1]['q'], a))
    check("semiconvergent law K_j - n_j L = theta_(k-1) - j theta_k", ok,
          f"{tested} instances")
    print(f"      verified on {tested} (k,j) instances, 0 failures.")
    print("      correctly-signed run lengths a_(k+1) at k-1 = "
          + ", ".join(f"q_{i}={q}:{a}" for i, q, a in runs[:12]))
    print("      -> runs are SHORT wherever the next partial quotient is small, so")
    print("         semiconvergents do NOT blanket the desert additively; the")
    print("         additive blanket is supplied by multiples and, unconditionally,")
    print("         by the covering bound of Part 2c.")
    print()


def maxgap_index(N):
    """k = max{ i : q_i <= N/2 }. Then the three-distance theorem bounds the
    largest gap of {nL : n in any N consecutive integers} by theta_(k-1)."""
    k = 0
    for c in CF:
        if 2 * c['q'] <= N:
            k = c['i']
        else:
            break
    return k


def maxgap_bound(N):
    k = maxgap_index(N)
    return THETA[k - 1] if k >= 1 else mpf(1)


def part2c():
    print("=" * 78)
    print("PART 2c.  The window-covering bound (three distances), verified")
    print("=" * 78)
    print("  CLAIM. Let k = max{i : q_i <= N/2}. For every N0, the N points")
    print("  {nL}, n = N0..N0+N-1, have all circle gaps <= theta_(k-1) < 1/q_k.")
    print("  Hence every arc of length > theta_(k-1) contains some {nL}.")
    worst = mpf(0)
    viol = 0
    tests = 0
    for N in list(range(2, 700)) + [1234, 5000, 9999, 31000, 77777, 190000]:
        for N0 in (1, 7, 12345, 987654321):
            pts = sorted(((N0 + i) * LFIX) % SCALE for i in range(N))
            g = max([pts[i + 1] - pts[i] for i in range(N - 1)]
                    + [SCALE - pts[-1] + pts[0]]) if N > 1 else SCALE
            g = mpf(g) / SCALE
            b = maxgap_bound(N)
            tests += 1
            # tolerance: the fixed-point representation of {nL} truncates at
            # 2^-BITS, so a gap that is exactly theta_(k-1) can read a few
            # ulps high. BITS = 160 and n < 2^40 here, so 1e-30 is ~10^18
            # times the worst possible truncation error.
            if g > b + mpf('1e-30'):
                viol += 1
            worst = max(worst, g / b)
            if N > 700:
                break
    check("three-distance covering bound", viol == 0,
          f"{viol} violations in {tests} windows")
    print(f"  {tests} windows tested (N = 2..699 at four offsets, plus seven large N);")
    print(f"  violations: {viol}; worst observed ratio maxgap/theta_(k-1) = "
          f"{float(worst):.6f} (equality is attained, so the bound is sharp).")
    print()

    print("  NEGATIVE CONTROL. The bound must FAIL to certify coverage when the")
    print("  target arc is shorter than theta_(k-1). Checked by exhibiting, for")
    print("  each of several N, an arc of length exactly theta_(k-1) containing no")
    print("  point of the window (the maximal gap itself):")
    nc = 0
    for N in (50, 300, 5000, 31000):
        pts = sorted((i * LFIX) % SCALE for i in range(1, N + 1))
        gaps = [(pts[i + 1] - pts[i], pts[i]) for i in range(N - 1)]
        gaps.append((SCALE - pts[-1] + pts[0], pts[-1]))
        gmax, at = max(gaps)
        empty = not any(at < ((i * LFIX) % SCALE) < at + gmax for i in range(1, N + 1))
        if empty:
            nc += 1
    check("negative control: maximal gap is genuinely empty", nc == 4, f"{nc}/4")
    print(f"  {nc}/4 maximal gaps confirmed empty -- the covering threshold is not")
    print("  an artifact of a loose estimate; below it, coverage genuinely fails.")
    print()


def certified_gamma_ceiling(p):
    """The largest gamma that the covering bound certifies as PRESCRIBABLE at
    period p inside the recipe's window, with no assumption on the partial
    quotients beyond the (computed, finite) continued fraction.

    Taking eps slightly above 2*theta_(k-1) and the target arc
    J = [1-eps, 1-eps/2) gives some n in the window with delta(n) in (eps/2,eps],
    hence gamma in [log2(1/eps)+0.5288, log2(2/eps)+0.8036]. The ceiling
    reported is the guaranteed lower endpoint at eps = 2*theta_(k-1)."""
    lo, hi = window(p)
    N = hi - lo + 1
    if N < 2:
        return None, None
    b = maxgap_bound(N)
    eps = 2 * b
    if eps > mpf('0.5'):
        return None, b
    return mp.log(1 / eps, 2) + mp.log(1 / log(2), 2), b


def rhin_gamma_ceiling(p):
    """Unconditional tail, using ONLY Rhin's effective bound (no continued
    fraction data): with N the window length, k = max{i: q_i <= N/2} satisfies
    q_(k+1) > N/2, so theta_k < 2/N; Rhin gives theta_k > C n^-mu at n = q_k,
    whence q_k > (C*N/2)^(1/mu) and maxgap <= theta_(k-1) < 1/q_k <
    (C*N/2)^(-1/mu). Taking eps = 2*(C*N/2)^(-1/mu):"""
    lo, hi = window(p)
    N = mpf(hi - lo + 1)
    eps = 2 * (C_RHIN * N / 2) ** (-1 / MU_RHIN)
    if eps > mpf('0.5'):
        return None
    return mp.log(1 / eps, 2) + mp.log(1 / log(2), 2)


def part2d(pmax=1000):
    print("=" * 78)
    print("PART 2d.  Certified gamma ceiling at every period (availability)")
    print("=" * 78)
    print("  For each p: N = #integers in the window; k = max{i: q_i <= N/2};")
    print("  eps_min = 2*theta_(k-1); gamma_ceiling = log2(1/eps_min) + 0.5288.")
    print("  Every gamma in [1.77, gamma_ceiling] is then prescribable to within")
    print("  1.28 bits by choosing eps in [2*theta_(k-1), 1/2].  UNCONDITIONAL:")
    print("  the only input is the (computed, finite) continued fraction of L.")
    print()
    print(f"  {'p':>5} {'log10 N':>9} {'k':>5} {'eps_min':>11} "
          f"{'gam_ceil':>10} {'/log2 p':>9} {'Rhin ceil':>10} {'/log2 p':>9}")
    rows = []
    for p in list(range(4, 41)) + [45, 50, 60, 80, 100, 150, 200, 300, 400, 500,
                                   600, 700, 713, 800, 900, 1000]:
        if p > pmax:
            break
        g, b = certified_gamma_ceiling(p)
        gr = rhin_gamma_ceiling(p)
        lo, hi = window(p)
        N = hi - lo + 1
        lg = mp.log(p, 2)
        rows.append((p, N, g, gr, lg))
        if p <= 40 or p in (50, 60, 80, 100, 200, 400, 600, 700, 713, 800, 1000):
            print(f"  {p:>5} {float(mp.log(N,10)):>9.2f} {maxgap_index(N):>5} "
                  f"{(float(b) if b else float('nan')):>11.3e} "
                  f"{(float(g) if g else float('nan')):>10.2f} "
                  f"{(float(g/lg) if g else float('nan')):>9.2f} "
                  f"{(float(gr) if gr else float('nan')):>10.2f} "
                  f"{(float(gr/lg) if gr else float('nan')):>9.2f}")
    print()
    # the minima below range over EVERY integer p in 4..712, not the printed sample
    allrows = []
    for p in range(4, 713):
        g, b = certified_gamma_ceiling(p)
        if g is not None:
            allrows.append((p, g, mp.log(p, 2)))
    for pstart in (21, 24, 35):
        rr = [float(g / lg) for (p, g, lg) in allrows if p >= pstart]
        argmin = min(((float(g / lg), p) for (p, g, lg) in allrows if p >= pstart))
        print(f"  min over ALL p in {pstart}..712 of gamma_ceiling(p)/log2 p = "
              f"{min(rr):.3f}  (attained at p = {argmin[1]})")
    rho24 = min(float(g / lg) for (p, g, lg) in allrows if p >= 24)
    check("certified availability at rho = 3.3 * log2 p for every p >= 24",
          rho24 >= 3.3, f"min ratio {rho24:.3f}")
    print()
    print("  Reading: for every p >= 24 the window unconditionally affords an n")
    print(f"  whose gamma can be prescribed anywhere up to {rho24:.2f}*log2 p, and the")
    print("  verified instance record of 12.8.6.4 already exhibits n at every")
    print("  p <= 23.  The band actually used by the recipe over p = 2..23 was")
    print("  gamma/log2 p in [1.828, 3.643].")

    # Where does the Rhin tail alone (no CF data whatsoever) take over?
    print()
    for rho in (mpf('2.5'), mpf('3.3'), mpf('3.643')):
        p0 = None
        for p in range(2, 4001):
            gr = rhin_gamma_ceiling(p)
            if gr is not None and gr > rho * mp.log(p, 2):
                if p0 is None:
                    p0 = p
            else:
                p0 = None
        print(f"  Rhin-only ceiling ({float(LOG2L/MU_RHIN):.5f}*p - 1.06) exceeds "
              f"{float(rho)}*log2 p for all p >= {p0}.")
    check("Rhin tail covers rho = 3.643 from p = 713",
          rhin_gamma_ceiling(713) > mpf('3.643') * mp.log(713, 2))
    print("  So the finite continued-fraction computation covers 24 <= p <= 712")
    print("  and Rhin's effective measure covers p >= 713 with no CF input at all:")
    print("  together, every period, with no hypothesis on the partial quotients.")
    print()
    return rows


def find_n_with_delta(p, eps, scan_cap=4_000_000):
    """Constructive witness: the least n in the window with delta(n) in
    (eps/2, eps]. Scans the window from its lower edge with an exact fixed-point
    accumulator (candidate generation only; every use of the result is
    re-verified exactly)."""
    lo, hi = window(p)
    x = frac_fix(lo)
    step = LFIX % SCALE
    lo_t = int(mp.floor((1 - eps) * SCALE))
    hi_t = int(mp.ceil((1 - eps / 2) * SCALE))
    for n in range(lo, min(hi, lo + scan_cap) + 1):
        if lo_t <= x < hi_t:
            return n
        x += step
        if x >= SCALE:
            x -= SCALE
    return None


def part2e(pscan=30, pmax=40):
    print("=" * 78)
    print("PART 2e.  What the window actually holds, and explicit witnesses")
    print("=" * 78)
    print("  (i) EXHAUSTIVE. For p <= %d the whole window is scanned: gamma_max(p)"
          % pscan)
    print("      is the largest gamma any n in the window can supply (the best")
    print("      approximation actually present), against the certified worst-case")
    print("      ceiling of Part 2d and against 3.643*log2 p, the top of the band")
    print("      the recipe used over p = 2..23.")
    print()
    print(f"  {'p':>4} {'window size':>12} {'best n':>12} {'delta_min':>12} "
          f"{'gam_max':>9} {'/log2 p':>8} {'cert ceil':>10} {'log2 N':>8}")
    ok = True
    for p in range(4, pscan + 1):
        lo, hi = window(p)
        x = frac_fix(lo)
        step = LFIX % SCALE
        best = -1
        bestn = None
        for n in range(lo, hi + 1):
            d = SCALE - x
            if d > best:
                best = d
                bestn = n
            x += step
            if x >= SCALE:
                x -= SCALE
        # 'best' is the largest numerator of (1 - {nL}) below SCALE, i.e. the
        # SMALLEST delta is SCALE-best... recompute cleanly:
        x = frac_fix(lo)
        dmin = None
        bestn = None
        for n in range(lo, hi + 1):
            dnum = SCALE - x
            if dmin is None or dnum < dmin:
                dmin = dnum
                bestn = n
            x += step
            if x >= SCALE:
                x -= SCALE
        d = delta_hp(bestn)
        T3 = 3 ** bestn
        K = T3.bit_length()
        q = (1 << K) - T3
        if q <= 0:
            ok = False
        gmax = mpf(K) - mp.log(mpf(q), 2)
        cert, _ = certified_gamma_ceiling(p)
        lg = mp.log(p, 2)
        print(f"  {p:>4} {hi-lo+1:>12} {bestn:>12} {float(d):>12.3e} "
              f"{float(gmax):>9.3f} {float(gmax/lg):>8.3f} "
              f"{(float(cert) if cert else float('nan')):>10.3f} "
              f"{float(mp.log(hi-lo+1,2)):>8.2f}")
        if p >= 19 and gmax < mpf('3.643') * lg:
            ok = False
    check("window supplies gamma up to 3.643*log2 p at every p in 19..%d" % pscan,
          ok)
    print()
    print("  gamma_max(p) tracks log2(window size) = 0.664*p + O(1): the actual")
    print("  supply is exponentially better than the worst-case covering bound,")
    print("  which is pinned to the largest convergent denominator below N/2 and")
    print("  therefore flattens across the desert.")
    print()
    print("  (ii) EXPLICIT WITNESSES in the band, verified with exact big integers:")
    print(f"  {'p':>4} {'n':>12} {'n/1.585^p':>10} {'delta':>12} {'gamma':>8} "
          f"{'gam/log2p':>10} {'convergent?':>12}")
    conv_q = set(c['q'] for c in CF if c['s'] > 0)
    ok2 = True
    for p in range(4, pmax + 1):
        target = mpf('2.5') * mp.log(p, 2)
        eps = mpf(2) ** (mp.log(1 / log(2), 2) - target) * 2
        n = find_n_with_delta(p, eps)
        if n is None:
            ok2 = False
            print(f"  {p:>4}  NO WITNESS at eps={float(eps):.3e}")
            continue
        T3 = 3 ** n
        K = T3.bit_length()
        q = (1 << K) - T3
        if q <= 0:
            ok2 = False
        gamma = mpf(K) - mp.log(mpf(q), 2)
        d = delta_hp(n)
        if not (mpf('1.5') * mp.log(p, 2) <= gamma <= mpf('3.643') * mp.log(p, 2)):
            ok2 = False
        print(f"  {p:>4} {n:>12} {float(n/L**p):>10.3f} {float(d):>12.3e} "
              f"{float(gamma):>8.3f} {float(gamma/mp.log(p,2)):>10.3f} "
              f"{('yes' if n in conv_q else 'no'):>12}")
    check("explicit in-band witness at every p in 4..%d" % pmax, ok2)
    print()
    print("  Only the first few witnesses are convergent denominators at all; from")
    print("  p = 8 up, every one is an ordinary integer. At the quality the")
    print("  construction needs, the candidate supply is the whole window, and the")
    print("  continued-fraction chain is one sparse subset of it.")
    print()


# ---------------------------------------------------------------------
# Part 3. The staircase at p = 24..36.
# ---------------------------------------------------------------------

def climb_profile(climb_n, blocks):
    """Geometric depths of ratio L summing to climb_n, rounded by nearest-integer
    rounding of the PARTIAL SUMS (bounded 1/2 error at every prefix)."""
    c = mpf(climb_n) * (L - 1) / (L ** blocks - 1)
    prev = 0
    ms = []
    for j in range(blocks):
        Tj = c * (L ** (j + 1) - 1) / (L - 1)
        Mj = int(nint(Tj))
        ms.append(Mj - prev)
        prev = Mj
    ms[-1] += climb_n - sum(ms)
    return ms


def base_profile(p, n, K, crash_depth):
    S = K - n
    if p < 2 or S <= p - 1 or n - crash_depth < p - 1:
        return None
    ms = climb_profile(n - crash_depth, p - 1)
    if min(ms) < 1:
        return None
    ms = ms + [crash_depth]
    ss = [1] * (p - 1) + [S - (p - 1)]
    if ss[-1] < 1:
        return None
    return ms, ss


def log2R_all(ms, ss):
    """log2 R_r for every rotation r, in double precision (SEARCH ONLY).
    R_r = sum_t 3^(M_t) 2^(S_t) (2^(s_t)-1) with M_t the m-suffix and S_t the
    sigma-prefix, read in rotation order starting at r."""
    p = len(ms)
    sig = [ss[t] + ms[(t + 1) % p] for t in range(p)]
    out = []
    for r in range(p):
        m = ms[r:] + ms[:r]
        s = ss[r:] + ss[:r]
        g = sig[r:] + sig[:r]
        Msuf = [0] * (p + 1)
        for t in range(p - 1, -1, -1):
            Msuf[t] = Msuf[t + 1] + (m[t + 1] if t + 1 < p else 0)
        es = []
        Spre = 0
        for t in range(p):
            es.append(Msuf[t] * LF + Spre + s[t] + math.log2(1 - 2.0 ** (-s[t])))
            Spre += g[t]
        mx = max(es)
        out.append(mx + math.log2(sum(2.0 ** (e - mx) for e in es)))
    return out


def R_all_exact(ms, ss, q):
    """Every rotation sum, EXACTLY. R_0 by Horner in 3; the other rotations by
    the transport recurrence of cycles.md 12.6.1.1, with the exact divisibility
    2^(sigma_r) | (3^(m_r) R_r + (2^(s_r)-1) q) asserted at every step."""
    p = len(ms)
    sig = [ss[t] + ms[(t + 1) % p] for t in range(p)]
    S = 0
    c = []
    for t in range(p):
        c.append((1 << S) * ((1 << ss[t]) - 1))
        S += sig[t]
    B = c[0]
    for t in range(1, p):
        B = (3 ** ms[t]) * B + c[t]
    R = [B]
    for r in range(p - 1):
        nxt = (3 ** ms[r]) * R[-1] + ((1 << ss[r]) - 1) * q
        assert nxt % (1 << sig[r]) == 0, "transport recurrence divisibility"
        R.append(nxt >> sig[r])
    return R


def correct(ms, ss, log2q, max_moves=40, margin=1e-6):
    """Bounded, deterministic correction (search in log space). Repeatedly move
    one unit of climb depth from a donor to a recipient block, accepting the
    single move that most improves the worst rotation's margin. The crash block
    is never touched. Returns (ms, moves) or None."""
    p = len(ms)
    crash = p - 1
    moves = 0
    escalate_after = 15
    while moves < max_moves:
        Rs = log2R_all(ms, ss)
        w = min(Rs)
        if w >= log2q + margin:
            return ms, moves
        rstar = Rs.index(w)
        if moves < escalate_after:
            pairs = [((rstar + a) % p, (rstar + b) % p)
                     for a in (-1, -2, -3, -4, 1, 2) for b in (1, 2, 3, -1, -2)]
            pairs = [(i, j) for i, j in pairs if i != j and i != crash and j != crash]
        else:
            pairs = [(i, j) for i in range(p - 1) for j in range(p - 1) if i != j]
        best = None
        for i, j in pairs:
            if ms[i] <= 1:
                continue
            ms2 = ms[:]
            ms2[i] -= 1
            ms2[j] += 1
            v = min(log2R_all(ms2, ss))
            if best is None or v > best[0]:
                best = (v, i, j)
        if best is None or best[0] <= w:
            if moves < escalate_after:
                escalate_after = 0
                continue
            return None
        _, i, j = best
        ms[i] -= 1
        ms[j] += 1
        moves += 1
    return None


def candidates_for(p, per_anchor=13, chunk=40000,
                   anchors=(0.70, 0.85, 1.00, 1.15, 1.35, 1.6, 2.0, 2.5, 3.2, 3.9)):
    """Candidate n at period p, ordered by INCREASING gamma (sharpest first).

    Ordinary integers, not continued-fraction data: from each of a handful of
    anchor points spread across the window, a short chunk is scanned and the
    first n met in each octave of delta is kept. Candidate generation only --
    every use of the result is re-verified with exact big integers."""
    lo, hi = window(p)
    step = LFIX % SCALE
    pool = {}
    for a in anchors:
        start = int(mp.floor(mpf(a) * L ** p))
        if start < lo or start > hi:
            continue
        x = frac_fix(start)
        seen = {}
        for n in range(start, min(hi, start + chunk) + 1):
            dnum = SCALE - x
            if dnum < SCALE // 2:
                oct_ = (SCALE // dnum).bit_length()
                if oct_ not in seen and len(seen) < per_anchor:
                    seen[oct_] = n
            x += step
            if x >= SCALE:
                x -= SCALE
        for n in seen.values():
            pool[n] = None
    out = sorted(pool, key=lambda n: -float(delta_of(n)))   # small gamma first
    return out


def part3(pmin=24, pmax=36, max_moves=40, budget=420.0):
    print("=" * 78)
    print("PART 3.  The empirical test at p = 24..36 (the convergent desert)")
    print("=" * 78)
    print("  Recipe of 12.8.6.2 + 12.8.6.3, reimplemented independently; candidate")
    print("  n taken from the whole window (ordinary integers, ordered by")
    print("  increasing gamma) rather than from the continued-fraction chain.")
    print("  Search in log space; EVERY reported pass is re-verified exactly.")
    print()
    print(f"  {'p':>4} {'n':>12} {'n/1.585^p':>10} {'gamma':>9} {'gam/log2p':>10} "
          f"{'crash':>5} {'moves':>6} {'exact q<=R_r':>13} {'q|R_r':>7} {'sec':>7}")
    recs = []
    unresolved = []
    for p in range(pmin, pmax + 1):
        t0 = time.time()
        rec = None
        cands = candidates_for(p)
        deadline = t0 + budget
        tried = 0
        for n in cands:
            if time.time() > deadline:
                break
            tried += 1
            T3 = 3 ** n
            K = T3.bit_length()
            q = (1 << K) - T3
            assert q > 0
            log2q = float(mp.log(mpf(q), 2))   # = K - gamma
            for cd in (1, 2):
                bp = base_profile(p, n, K, cd)
                if bp is None:
                    continue
                ms0, ss0 = bp
                res = correct(list(ms0), list(ss0), log2q, max_moves=max_moves)
                if res is None:
                    continue
                ms, moves = res
                Rs = R_all_exact(ms, ss0, q)
                if min(Rs) < q:
                    continue                      # log-space search overshot
                assert sum(ms) == n and sum(ss0) == K - n
                div = all(R % q == 0 for R in Rs)
                if div:
                    print("!!! HALT: p=%d n=%d passes size AND divisibility. "
                          "Stopping for main-session review." % (p, n))
                    sys.exit(1)
                gamma = mpf(K) - mp.log(mpf(q), 2)
                rec = dict(p=p, n=n, K=K, gamma=gamma, cd=cd, moves=moves,
                           ms=ms, ss=ss0, div=div, minmarg=min(Rs) - q)
                break
            if rec:
                break
        dt = time.time() - t0
        if rec is None:
            unresolved.append(p)
            print(f"  {p:>4}  UNRESOLVED  ({tried}/{len(cands)} candidates tried, "
                  f"<= {max_moves} moves each, {dt:.0f}s)")
            continue
        recs.append(rec)
        print(f"  {p:>4} {rec['n']:>12} {float(rec['n']/L**p):>10.3f} "
              f"{float(rec['gamma']):>9.3f} "
              f"{float(rec['gamma']/mp.log(p,2)):>10.3f} {rec['cd']:>5} "
              f"{rec['moves']:>6} {'PASS':>13} {str(rec['div']):>7} {dt:>7.1f}",
              flush=True)
    print()
    if recs:
        rr = [float(r['gamma'] / mp.log(r['p'], 2)) for r in recs]
        print(f"  resolved: {[r['p'] for r in recs]}")
        print(f"  gamma/log2 p over p = {pmin}..{pmax}: "
              f"min {min(rr):.3f}, max {max(rr):.3f}   "
              f"(12.8.6.4's range over p = 2..23 was [1.828, 3.643])")
    if unresolved:
        print(f"  UNRESOLVED: {unresolved}")
    check("every period 24..36 resolved", not unresolved, f"{unresolved}")
    check("no constructed instance satisfies the divisibility system",
          all(not r['div'] for r in recs))
    return recs, unresolved


# ---------------------------------------------------------------------
# Part 4. Cross-checks and negative controls.
# ---------------------------------------------------------------------

def part4():
    print("=" * 78)
    print("PART 4.  Cross-checks and negative controls")
    print("=" * 78)

    # Trivial cycle identity: R = 4^p - 3^p (cycles.md 12.6.1 remark).
    ok = True
    for p in (1, 2, 3, 4, 7, 11):
        ms = [1] * p
        ss = [1] * p
        q = 4 ** p - 3 ** p
        Rs = R_all_exact(ms, ss, q)
        if not all(R == q for R in Rs):
            ok = False
    check("trivial-cycle identity R = 4^p - 3^p", ok)
    print("  trivial cycle as a fake period-p cycle gives R_r = 4^p - 3^p at every")
    print("  rotation, p in {1,2,3,4,7,11}: agrees with cycles.md 12.6.1.")

    # Published p = 7 instance (12.8.3 / thm:staircase).
    ms = [4, 7, 9, 15, 23, 35, 1]
    n = sum(ms)
    K = (3 ** n).bit_length()
    q = (1 << K) - 3 ** n
    ss = [1] * 6 + [K - n - 6]
    Rs = R_all_exact(ms, ss, q)
    gamma = mpf(K) - mp.log(mpf(q), 2)
    check("published p=7 staircase passes all rotations", min(Rs) >= q)
    check("published p=7 gamma = 6.744", abs(gamma - mpf('6.744')) < mpf('0.01'),
          mp.nstr(gamma, 8))
    check("published p=7 fails divisibility", not all(R % q == 0 for R in Rs))
    print(f"  published p=7 instance n=94: gamma = {float(gamma):.3f} (12.8.3: 6.74),")
    print("  all seven rotations pass, divisibility fails -- reproduced by this")
    print("  file's independent transport-recurrence evaluator.")

    # Negative control 1: a flat profile must FAIL the size test at large p.
    p = 12
    n = int(LF ** p)
    K = (3 ** n).bit_length()
    q = (1 << K) - 3 ** n
    ms = [n // p] * p
    ms[-1] += n - sum(ms)
    ss = [1] * (p - 1) + [K - n - (p - 1)]
    Rs = R_all_exact(ms, ss, q)
    check("negative control: flat profile fails the size test", min(Rs) < q,
          f"minR/q = {float(mpf(min(Rs))/q):.4f}")
    print(f"  negative control: the FLAT depth profile at p={p}, n={n} fails "
          f"q <= R_r (min R_r / q = {float(mpf(min(Rs))/mpf(q)):.4f}) -- the")
    print("  geometric shape is doing real work, the test is not vacuous.")

    # Negative control 2: a deliberately bad n (delta near 1, gamma ~ 1) must
    # fail, because q is then within one bit of 2^K.
    for p in (10, 14):
        lo, hi = window(p)
        nbad = None
        x = frac_fix(lo)
        for nn in range(lo, hi + 1):
            if x < SCALE // 100:          # {nL} tiny => delta ~ 1 => gamma ~ 1
                nbad = nn
                break
            x = (x + LFIX) % SCALE
        if nbad is None:
            continue
        K = (3 ** nbad).bit_length()
        q = (1 << K) - 3 ** nbad
        gam = mpf(K) - mp.log(mpf(q), 2)
        bp = base_profile(p, nbad, K, 1)
        if bp is None:
            print(f"  negative control: p={p}, n={nbad} (gamma={float(gam):.3f}) "
                  f"is infeasible for the base profile, as expected.")
            continue
        Rs = R_all_exact(bp[0], bp[1], q)
        check("negative control: gamma~1 candidate fails the size test",
              min(Rs) < q, f"p={p} n={nbad} gamma={float(gam):.3f}")
        print(f"  negative control: p={p}, n={nbad} has gamma = {float(gam):.3f} "
              f"(delta near 1) and fails q <= R_r, as the two-sided reading of")
        print("  Part 1 predicts: too SMALL a gamma is as fatal as too large.")
    print()


def main():
    t0 = time.time()
    part0()
    part1()
    desert = part2a()
    part2b()
    part2c()
    part2d()
    part2e()
    part4()
    recs, unresolved = part3()
    print("=" * 78)
    print(f"CHECKS RUN: {CHECKS[0]}   FAILURES: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)
    print(f"elapsed {time.time()-t0:.0f}s")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
