"""Round-12 drift/rotation check (brief: briefs/merle-r12-drift-check-brief.md).

Supports: briefs/merle-r12-drift-check-findings.md.

Verifies, with fresh code importing nothing from any earlier check:
  PART 0 - canaries and negative controls FIRST (regime-column spirit: every
           asserted equality is tested in a regime chosen against it - small x
           for the series, spread configurations for the sums, both rescaled
           and real cycles for section 4(b), and failing J for the sweep).
  PART 1 - section 4(d): the artanh series D(x)/delta_x = 1 + 1/(27x^2)
           + 1/(405x^4) + 1/(5103x^6) + ..., Merle's relative-error figures,
           the leading gap at 2^71, and the corrected strict chain
           D(x) > delta_x*(1 + 1/(27x^2)) > delta_x.
  PART 2 - section 4(b): scale-invariance of Sum_i D(x_i) / (n*D(x_min)) on
           the -17 cycle shape (his 0.4755266037564546...), the leading-order
           shape identity (1/n)*Sum_i(x_min/x_i), and the real cycles with
           >= 2 elements; which pairing actually agrees to 44 decimals.
  PART 3 - section 4(e)/(f): the two-shore factor 2, x* = 7/3 uniqueness,
           D strictly decreasing, D(1) = 1 exact, D(3) = log2(5/4) < s,
           D(2^71)/s = 9.8145e-22.
  PART 4 - section 9: the rotation reformulation, every claim:
           5L = 8 - theta; the mod-1 advance and the 150/2000 wrap count;
           the Sturmian step sequence at slope L-1 (frequency and factor
           complexity); maxgap(J) = max(theta, 1 - J*theta) for J <= 13;
           maxgap = theta for J = 13..25, first fall at J = 26 to
           14*theta - 1; the identity 13(14theta-1) + 14(1-13theta) = 1;
           the margin l - theta; the 66 -> 131 sweep cost and the
           p >= 16 -> p >= 18 shift.
  PART 5 - the CRLF arithmetic behind 3,100 vs 3,175 (blob facts themselves
           are established from the read-only clones and recorded in the
           findings; here only the mechanism's arithmetic is checked).

Rounding robustness: every verdict is computed at TWO working precisions
(dps = 120 and dps = 240; 240 carries ~150 guard digits past the finest
quantity compared, the 7.94e-89 relative error at 2^71) and the two verdict
lists are asserted identical before the summary prints.

Exit code 0 iff all checks pass. Run: python experiments/merle_r12_drift_check.py
"""

import sys
from fractions import Fraction

from mpmath import mp, mpf, log, atanh, ceil as mpceil, floor as mpfloor

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  -- {detail}" if detail else ""))
    return bool(ok)


# ---------------------------------------------------------------- primitives

def D(x):
    """Per-step north-south gap D(x) = log2(3 + 1/x) - log2(3 - 1/x),
    computed as (2/ln2)*artanh(1/(3x)) -- the identical function (verified
    against the log-ratio form in check 1.6), with no cancellation at large x
    (the log-ratio form computes 3 +/- 1/x, which rounds to 3 once 1/x falls
    below the working precision; artanh(u) keeps full relative accuracy)."""
    return 2 * atanh(1 / (3 * mpf(x))) / log(2)


def D_logratio(x):
    """The definitional log-ratio form, usable at moderate x only."""
    return (log(3 + 1 / mpf(x)) - log(3 - 1 / mpf(x))) / log(2)


def delta(x):
    """The T1 constant at scale x: 2/(3 x ln 2)."""
    return 2 / (3 * mpf(x) * log(2))


def odd_cycle(seed):
    """Iterate x -> (3x+1)/2^v from a (negative) odd seed until it closes.
    Returns (abs_elements, valuations, n, K)."""
    xs, vs = [], []
    x = seed
    while True:
        xs.append(abs(x))
        y = 3 * x + 1
        v = 0
        while y % 2 == 0:
            y //= 2
            v += 1
        vs.append(v)
        x = y
        if x == seed:
            break
        assert len(xs) < 100, "did not close"
    return xs, vs, len(xs), sum(vs)


def K_exact(n):
    """K(n) = ceil(n log2 3) exactly, as the bit length of 3^n."""
    return (3 ** n).bit_length()


def maxgap(theta, J):
    """max gap of {j*theta mod 1 : 0 <= j <= J} on the circle."""
    pts = sorted((j * theta) % 1 for j in range(J + 1))
    gaps = [pts[i + 1] - pts[i] for i in range(len(pts) - 1)]
    gaps.append(1 - pts[-1] + pts[0])
    return max(gaps), sorted(gaps)


def sig(x, k):
    """Round to k significant digits, returned as an mpf-comparable string."""
    return mp.nstr(mpf(x), k, strip_zeros=False)


def sig_matches(x, printed):
    """True iff x rounds to the printed figure at the printed figure's own
    number of significant digits (e.g. sig_matches(0.00258121, '2.58e-3'))."""
    want = mpf(printed)
    digits = len(printed.split("e")[0].replace(".", "").replace("-", "").lstrip("0"))
    # round both to `digits` significant figures and compare the renderings
    return mp.nstr(mpf(x), digits) == mp.nstr(want, digits)


def truncated_digits(x, k):
    """First k significant digits of x by TRUNCATION (what an '...'-suffixed
    printed figure asserts), as a string '0.dddd...' for 0 < x < 1."""
    s = mp.nstr(mpf(x), k + 8, strip_zeros=False)
    assert s.startswith("0.")
    frac = s[2:].lstrip("0")
    lead = len(s) - 2 - len(frac)
    return "0." + "0" * lead + frac[:k]


# ---------------------------------------------------------------- the run

def run(dps):
    mp.dps = dps
    verdicts_start = len(CHECKS)
    L = log(3) / log(2)
    theta = 8 - 5 * L
    s_const = 2 - L  # 2 - log2 3

    print(f"\n{'=' * 74}\nWORKING PRECISION dps = {dps}\n{'=' * 74}")

    # ================================================================ PART 0
    print("\n-- PART 0: canaries and negative controls (before anything) --")

    # C0.1 the display read as an equality is FALSE, and visibly so at small x.
    lhs = D(1)
    rhs = delta(1) * (1 + Fraction(1, 27))
    rel = (lhs - rhs) / lhs
    check("C0.1 display-as-equality REFUTED at x=1 (relative gap ~2.58e-3)",
          rel > mpf("2.5e-3") and rel < mpf("2.7e-3"),
          f"rel gap = {sig(rel, 6)}")

    # C0.2 the regime trap: at 2^71 the same falsehood is invisible to any
    # <= 80-digit comparison.
    X = mpf(2) ** 71
    rel71 = (D(X) - delta(X) * (1 + 1 / (27 * X ** 2))) / D(X)
    check("C0.2 the same gap at 2^71 is below 1e-88 (invisible in-regime)",
          rel71 > 0 and rel71 < mpf("1e-88"),
          f"rel gap = {sig(rel71, 6)}")

    # C0.3 sum canary: the degenerate configuration achieves equality
    # (ratio 1); a spread configuration does not, at ANY scale.
    xs17, vs17, n17, K17 = odd_cycle(-17)
    for k in (20, 200):
        sc = 2 ** k
        degen = sum(D(17 * sc) for _ in xs17) / (n17 * D(17 * sc))
        spread = sum(D(x * sc) for x in xs17) / (n17 * D(17 * sc))
        check(f"C0.3 degenerate ratio == 1, spread ratio ~0.4755 (k={k})",
              abs(degen - 1) < mpf(10) ** (-(dps - 10))
              and abs(spread - mpf("0.4755266")) < mpf("1e-6"),
              f"degen = {sig(degen, 8)}, spread = {sig(spread, 8)}")

    # C0.4 the 44-decimals explanation predicts ratio -> 1 as scale grows;
    # measured: it does not move at all.
    r20 = sum(D(x * 2 ** 20) for x in xs17) / (n17 * D(17 * 2 ** 20))
    r1000 = sum(D(x * 2 ** 1000) for x in xs17) / (n17 * D(17 * 2 ** 1000))
    check("C0.4 ratio does NOT drift toward 1 with scale (refutes 44-dec diagnosis)",
          abs(r1000 - r20) < mpf("1e-12") and abs(r1000 - 1) > mpf("0.5"),
          f"|r(1000)-r(20)| = {sig(abs(r1000 - r20), 4)}")

    # C0.5 sweep negative controls: maxgap(11) misses both arcs; J = 12
    # genuinely fails the two-sided arc (explicit counterexample); the
    # sortedness device fails at J = 14 (wrap).
    ell_two = mpf("0.1169390665") - mpf("0.0415")
    mg11, _ = maxgap(theta, 11)
    check("C0.5a maxgap(11) = 0.1729375397... > both arc lengths",
          abs(mg11 - mpf("0.1729375397")) < mpf("1e-9")
          and mg11 > mpf("0.1169390665"),
          f"maxgap(11) = {sig(mg11, 11)}")
    dlo, dhi = mpf("0.0415"), mpf("0.1169390665")
    fails12 = []
    for N in range(1, 4001):
        hit = any(dlo <= (K_exact(N + 5 * j) - (N + 5 * j) * L) <= dhi
                  for j in range(13))
        if not hit:
            fails12.append(N)
    check("C0.5b J=12 (61 integers) genuinely fails two-sided arc, first at N=22",
          len(fails12) > 0 and fails12[0] == 22,
          f"{len(fails12)} failing starts in N <= 4000, first = "
          f"{fails12[0] if fails12 else 'none'}")
    check("C0.5c sortedness device breaks at J=14 (14*theta wraps past 1)",
          13 * theta < 1 < 14 * theta,
          f"13*theta = {sig(13 * theta, 8)}, 14*theta = {sig(14 * theta, 8)}")

    # ================================================================ PART 1
    print("\n-- PART 1: section 4(d) - the series, his figures, the chain --")

    # 1.1 the coefficients 27, 405, 5103 are exact: term k of artanh(u)/u
    # at u = 1/(3x) is 1/((2k+1)*9^k) * x^(-2k).
    coeffs = [(2 * k + 1) * 9 ** k for k in (1, 2, 3)]
    check("1.1 series denominators (2k+1)*9^k = 27, 405, 5103 exactly",
          coeffs == [27, 405, 5103], f"{coeffs}")

    # 1.2 D/delta equals the truncated series to O(x^-8), coefficient checked.
    x = mpf(10)
    resid = D(x) / delta(x) - (1 + 1 / (27 * x ** 2) + 1 / (405 * x ** 4)
                               + 1 / (5103 * x ** 6))
    next_term = 1 / (9 * mpf(9) ** 4 * x ** 8)  # 1/((2*4+1)*9^4 x^8)
    check("1.2 residual after three terms ~ 1/(59049 x^8) at x=10",
          mpf("0.98") < resid / next_term < mpf("1.02"),
          f"resid/next_term = {sig(resid / next_term, 6)}")

    # 1.3 his relative-error figures for the truncation 1 + 1/(27x^2).
    targets = [(1, "2.58e-3"), (3, "3.06e-5"), (17, "2.96e-8")]
    for xv, want in targets:
        xm = mpf(xv)
        r = (D(xm) - delta(xm) * (1 + 1 / (27 * xm ** 2))) / D(xm)
        check(f"1.3 relative error at x={xv} is {want}", sig_matches(r, want),
              f"computed {mp.nstr(r, 6)}")
    X71 = mpf(2) ** 71
    r71 = (D(X71) - delta(X71) * (1 + 1 / (27 * X71 ** 2))) / D(X71)
    check("1.3 relative error at x=2^71 is 7.94e-89",
          sig_matches(r71, "7.94e-89"), f"computed {mp.nstr(r71, 6)}")

    # 1.4 leading gap at 2^71: D/delta - 1 = 6.6432e-45, and it IS 1/(27x^2)
    # to leading order.
    gap = D(X71) / delta(X71) - 1
    check("1.4 leading gap D/delta - 1 at 2^71 = 6.6432e-45 (his recomputation)",
          mp.nstr(gap, 5) == "6.6432e-45", f"computed {mp.nstr(gap, 8)}")
    check("1.4 record's 6.643193e-45 also correct at its own precision",
          mp.nstr(gap, 7) == "6.643193e-45", f"computed {mp.nstr(gap, 8)}")
    # the second-order term itself: gap = 1/(27x^2) + 1/(405x^4) + ..., so
    # gap*(27x^2) - 1 = 27/(405x^2) = 1/(15x^2). Check the coefficient.
    second = gap * 27 * X71 ** 2 - 1
    check("1.4 gap / (1/(27x^2)) = 1 + 1/(15x^2) + O(x^-4)",
          abs(second * 15 * X71 ** 2 - 1) < mpf("1e-2"),
          f"second-order coeff*(15x^2) = {sig(second * 15 * X71 ** 2, 6)}")

    # 1.5 the corrected chain is strict everywhere tested, both differences
    # positive with margin (the regime list includes the adversarial small x).
    for xv in (1, Fraction(7, 3), 3, 17, 100, 2 ** 71):
        xm = mpf(xv.numerator) / xv.denominator if isinstance(xv, Fraction) else mpf(xv)
        a, b, c = D(xm), delta(xm) * (1 + 1 / (27 * xm ** 2)), delta(xm)
        check(f"1.5 strict chain D > delta*(1+1/(27x^2)) > delta at x={xv}",
              a > b > c and (a - b) > 0 and (b - c) > 0,
              f"D-mid = {sig(a - b, 4)}, mid-delta = {sig(b - c, 4)}")

    # 1.6 the two forms of D agree (log-ratio vs artanh) at moderate x,
    # where the log-ratio form is numerically usable.
    agree = all(abs(D(v) - D_logratio(v)) < mpf(10) ** (-(dps - 8))
                for v in (1, 3, 17, 1000, 10 ** 12))
    check("1.6 log2-ratio and (2/ln2)artanh forms identical", agree)

    # ================================================================ PART 2
    print("\n-- PART 2: section 4(b) - scale invariance of the sum ratio --")

    # 2.1 the cycles, derived here from their seeds.
    check("2.1 -17 cycle: n=7, K=11, elements {17,25,37,55,41,61,91}",
          (n17, K17) == (7, 11) and sorted(xs17) == [17, 25, 37, 41, 55, 61, 91],
          f"n={n17}, K={K17}")
    xs5, vs5, n5, K5 = odd_cycle(-5)
    check("2.1 -5 cycle: n=2, K=3, elements {5,7}",
          (n5, K5) == (2, 3) and sorted(xs5) == [5, 7])
    xs1, vs1, n1, K1 = odd_cycle(-1)
    check("2.1 -1 cycle: n=1, K=1", (n1, K1) == (1, 1))

    # 2.2 the exact shape constant (1/n) Sum(x_min/x_i) for the -17 shape.
    shape17 = Fraction(0)
    for xv in xs17:
        shape17 += Fraction(17, xv)
    shape17 = shape17 / 7
    shape17_mp = mpf(shape17.numerator) / shape17.denominator
    # his '0.4755266037564546...' carries an ellipsis, i.e. asserts the first
    # 16 significant digits by truncation (the 17th is a 7, so a 16-digit
    # ROUNDING would print ...4547).
    check("2.2 (1/7)Sum(17/x_i) = 0.4755266037564546... (16 digits, truncated)",
          truncated_digits(shape17_mp, 16) == "0.4755266037564546",
          f"exact = {mp.nstr(shape17_mp, 22)}")

    # 2.3 the ratio at his four scales.
    print("   ratio R(k) = Sum D(x_i*2^k) / (7*D(17*2^k)):")
    for k in (20, 71, 200, 1000):
        r = sum(D(xv * 2 ** k) for xv in xs17) / (7 * D(17 * 2 ** k))
        dev = abs(r - shape17_mp)
        print(f"     k = {k:5d}: R = {mp.nstr(r, 22)}   |R - shape| = {sig(dev, 3)}")
        # his claim: 0.4755266037564546... at every scale (16 digits)
        check(f"2.3 R(17*2^{k}) begins 0.4755266037564546 (16 digits, truncated)",
              truncated_digits(r, 16) == "0.4755266037564546",
              f"R = {mp.nstr(r, 18)}")

    # 2.4 leading order: R(k) - shape = O(x_min^-2) (deviation * x_min^2 bounded,
    # and consecutive k drop by ~4x).
    d20 = abs(sum(D(xv * 2 ** 20) for xv in xs17) / (7 * D(17 * 2 ** 20)) - shape17_mp)
    d21 = abs(sum(D(xv * 2 ** 21) for xv in xs17) / (7 * D(17 * 2 ** 21)) - shape17_mp)
    check("2.4 deviation falls ~4x per doubling (O(scale^-2) confirmed)",
          mpf("3.5") < d20 / d21 < mpf("4.5"),
          f"d(k=20)/d(k=21) = {sig(d20 / d21, 5)}")

    # 2.5 the real cycles with >= 2 elements, at native scale and rescaled.
    r17_native = sum(D(xv) for xv in xs17) / (7 * D(17))
    check("2.5 -17 native ratio 0.4754... within O(1/(27*17^2)) of shape",
          abs(r17_native - shape17_mp) < mpf("2e-4"),
          f"native = {mp.nstr(r17_native, 10)}, shape = {mp.nstr(shape17_mp, 10)}")
    shape5 = (Fraction(5, 5) + Fraction(5, 7)) / 2
    shape5_mp = mpf(shape5.numerator) / shape5.denominator
    r5_native = sum(D(xv) for xv in xs5) / (2 * D(5))
    check("2.5 -5 native ratio within O(1/(27*25)) of shape 6/7",
          abs(r5_native - shape5_mp) < mpf("2e-3"),
          f"native = {mp.nstr(r5_native, 10)}, shape 6/7 = {mp.nstr(shape5_mp, 10)}")
    r5_scaled = [sum(D(xv * 2 ** k) for xv in xs5) / (2 * D(5 * 2 ** k))
                 for k in (20, 71, 200)]
    check("2.5 -5 shape ratio scale-invariant at 6/7 = 0.857142857...",
          all(mp.nstr(r, 15) == mp.nstr(shape5_mp, 15) for r in r5_scaled),
          f"R(k=20,71,200) = {[mp.nstr(r, 12) for r in r5_scaled]}")
    # also the -17 sum against n*D(x_min), his 0.188336 / 0.396085 / 2.103.
    sum17 = sum(D(xv) for xv in xs17)
    nd17 = 7 * D(17)
    check("2.5 on -17: Sum D = 0.188336, n*D(x_min) = 0.396085, factor 2.103",
          mp.nstr(sum17, 6) == "0.188336" and mp.nstr(nd17, 6) == "0.396085"
          and mp.nstr(nd17 / sum17, 4) == "2.103",
          f"{mp.nstr(sum17, 6)}, {mp.nstr(nd17, 6)}, {mp.nstr(nd17 / sum17, 4)}")

    # 2.6 which pairing agrees to 44 decimals at 2^71: the per-step pair
    # D(X) vs delta as a RATIO (1 + 6.64e-45), not the summed pair.
    ratio_gap = D(X71) / delta(X71) - 1
    check("2.6 D(X)/delta at 2^71 = 1 + 6.64e-45 (44 zero decimals in the ratio)",
          mpf("6e-45") < ratio_gap < mpf("7e-45"),
          f"D/delta - 1 = {sig(ratio_gap, 6)}")
    summed_ratio = sum(D(xv * 2 ** 67) for xv in xs17) / (7 * delta(17 * 2 ** 67))
    check("2.6 the summed pair does NOT converge: Sum D/(n*delta(x_min)) ~ 0.4755 at 17*2^67",
          abs(summed_ratio - shape17_mp) < mpf("1e-6"),
          f"summed ratio = {mp.nstr(summed_ratio, 10)}")

    # ================================================================ PART 3
    print("\n-- PART 3: sections 4(e)/(f) - flat confirms, small numbers --")

    # 3.1 two-shore factor 2: log2(1+u) - log2(1-u) = 2u/ln2 + O(u^3),
    # third-order coefficient 2/(3 ln 2).
    u = mpf("1e-4")
    two_shore = (log(1 + u) - log(1 - u)) / log(2)
    resid3 = (two_shore - 2 * u / log(2)) / u ** 3
    check("3.1 two-shore reading: residual coefficient = 2/(3 ln2)",
          abs(resid3 - 2 / (3 * log(2))) < mpf("1e-6"),
          f"coeff = {sig(resid3, 8)} vs 2/(3ln2) = {sig(2 / (3 * log(2)), 8)}")

    # 3.2 uniqueness of x* = 7/3, in exact rationals.
    xstar = Fraction(7, 3)
    check("3.2 3(3x+1) = 4(3x-1) has the single root x = 7/3",
          3 * (3 * xstar + 1) == 4 * (3 * xstar - 1)
          and Fraction(3 * 1 + 3, 3) != 0
          and (3 * (3 * Fraction(2) + 1) - 4 * (3 * Fraction(2) - 1)) != 0)
    ratio_at_xstar = (3 * xstar + 1) / (3 * xstar - 1)
    check("3.2 (3x*+1)/(3x*-1) = 4/3 exactly", ratio_at_xstar == Fraction(4, 3))
    check("3.2 log2(4/3) = 2 - log2 3 identically",
          abs((log(4) - log(3)) / log(2) - s_const) < mpf(10) ** (-(dps - 5)))

    # 3.3 D strictly decreasing on (1/3, inf): u = 1/(3x) decreasing, artanh
    # increasing => D decreasing; numeric grid confirms.
    grid = [mpf(v) / 10 for v in range(4, 200, 7)]
    dec = all(D(grid[i]) > D(grid[i + 1]) for i in range(len(grid) - 1))
    check("3.3 D strictly decreasing on sampled grid (0.4 .. 19.8)", dec)

    # 3.4 D(1) = 1 exactly: (3+1)/(3-1) = 2, log2 2 = 1.
    check("3.4 D(1) = 1 EXACT ((3+1)/(3-1) = 2 in rationals)",
          Fraction(4, 2) == 2 and abs(D(1) - 1) < mpf(10) ** (-(dps - 5)),
          f"D(1) - 1 = {sig(D(1) - 1, 3)}")

    # 3.5 D(3) = log2(5/4) = 0.321928 < s = 0.415037.
    check("3.5 D(3) = log2(5/4) exactly (10/8 = 5/4 in rationals)",
          Fraction(3 * 3 + 1, 3 * 3 - 1) == Fraction(5, 4))
    check("3.5 D(3) = 0.321928 and s = 0.415037 (his printed digits)",
          mp.nstr(D(3), 6) == "0.321928" and mp.nstr(s_const, 6) == "0.415037",
          f"D(3) = {mp.nstr(D(3), 8)}, s = {mp.nstr(s_const, 8)}")

    # 3.6 D(2^71)/s = 9.8145e-22.
    check("3.6 D(2^71)/s = 9.8145e-22",
          mp.nstr(D(X71) / s_const, 5) == "9.8145e-22",
          f"computed {mp.nstr(D(X71) / s_const, 7)}")

    # ================================================================ PART 4
    print("\n-- PART 4: section 9 - the rotation reformulation, every claim --")

    # 4.1 theta and 1/theta.
    # his '0.0751874964...' is a 9-significant-digit ROUNDING carrying an
    # ellipsis (true digits 0.07518749639...); both readings are recorded.
    check("4.1 theta = 8 - 5*log2(3) rounds to 0.0751874964 (9 sig digits)",
          sig_matches(theta, "0.0751874964"),
          f"theta = {mp.nstr(theta, 14)} (truncated digits 0.0751874963...)")
    check("4.1 1/theta = 13.3000838",
          sig_matches(1 / theta, "13.3000838"),
          f"1/theta = {mp.nstr(1 / theta, 12)}")

    # 4.2 K(n) = ceil(nL) = bitlength(3^n), exact, n = 1..2000.
    ok42 = all(K_exact(n) == int(mpceil(n * L)) for n in range(1, 2001))
    check("4.2 K(n) = bitlength(3^n) = ceil(nL) for n = 1..2000", ok42)

    # 4.3 delta(n+5) advances by theta MOD 1, wrap iff delta(n) >= 1 - theta;
    # wrap count over n = 1..2000 is 150, fraction 0.075 ~ theta.
    wraps = 0
    ok_adv, ok_cond = True, True
    for n in range(1, 2001):
        dn = K_exact(n) - n * L
        dn5 = K_exact(n + 5) - (n + 5) * L
        step = dn5 - dn
        if abs(step - theta) < mpf("1e-30"):
            wrapped = False
        elif abs(step - (theta - 1)) < mpf("1e-30"):
            wrapped = True
            wraps += 1
        else:
            ok_adv = False
            wrapped = None
        if wrapped is not None and wrapped != (dn >= 1 - theta):
            ok_cond = False
    check("4.3 delta(n+5) - delta(n) is theta or theta-1, nothing else", ok_adv)
    check("4.3 wrap condition is exactly delta(n) >= 1 - theta", ok_cond)
    check("4.3 wrap count over n = 1..2000 is 150 (fraction 0.075 ~ theta)",
          wraps == 150, f"wraps = {wraps}, fraction = {wraps / 2000}")

    # 4.4 the step sequence: values in {1,2}; the ceil identity; frequency.
    word = [K_exact(n + 1) - K_exact(n) for n in range(1, 2001)]
    check("4.4 K(n+1) - K(n) in {1,2} for n = 1..2000",
          set(word) == {1, 2})
    ok_id = all(K_exact(n + 1) - K_exact(n)
                == 1 + (int(mpceil((n + 1) * (L - 1))) - int(mpceil(n * (L - 1))))
                for n in range(1, 2001))
    check("4.4 identity K(n+1)-K(n) = 1 + (ceil((n+1)(L-1)) - ceil(n(L-1)))", ok_id)
    twos = word.count(2)
    check("4.4 letter-2 frequency over 2000 steps = 0.585 (his figure)",
          twos == 1170, f"count = {twos}, freq = {twos / 2000}")
    check("4.4 slope L - 1 = 0.584963 (his digits)",
          mp.nstr(L - 1, 6) == "0.584963", f"L-1 = {mp.nstr(L - 1, 9)}")

    # 4.4 factor complexity p(m) = m + 1 for m = 1..12 (Sturmian signature),
    # on a 20000-letter word.
    word_long = "".join(str(K_exact(n + 1) - K_exact(n)) for n in range(1, 20001))
    complexities = []
    for m in range(1, 13):
        complexities.append(len({word_long[i:i + m]
                                 for i in range(len(word_long) - m + 1)}))
    check("4.4 factor complexity p(m) = m+1 for m = 1..12",
          complexities == [m + 1 for m in range(1, 13)],
          f"p(1..12) = {complexities}")

    # 4.5 sortedness for J <= 13 and the closed-form maxgap.
    ok_sorted = all((13 * theta) % 1 == 13 * theta for _ in (0,)) and 13 * theta < 1
    check("4.5 for J <= 13 the points {j*theta} have not wrapped (13*theta < 1)",
          ok_sorted, f"13*theta = {sig(13 * theta, 8)}")
    ok_closed = True
    for J in range(1, 14):
        mg, _ = maxgap(theta, J)
        closed = max(theta, 1 - J * theta)
        if abs(mg - closed) > mpf(10) ** (-(dps - 10)):
            ok_closed = False
    check("4.5 maxgap(J) = max(theta, 1 - J*theta) EXACTLY for J = 1..13", ok_closed)
    mg12, _ = maxgap(theta, 12)
    mg13, _ = maxgap(theta, 13)
    check("4.5 maxgap(12) = 0.0977500433 (his digits)",
          sig_matches(mg12, "0.0977500433"), f"maxgap(12) = {mp.nstr(mg12, 12)}")
    check("4.5 maxgap(13) = theta",
          abs(mg13 - theta) < mpf(10) ** (-(dps - 10)))

    # 4.6 the sweep criterion with l = 0.1169390665 - 0.0415.
    ell = mpf("0.1169390665") - mpf("0.0415")
    check("4.6 l = 0.0754390665 (exact difference of the two decimals)",
          sig_matches(ell, "0.0754390665"), f"l = {mp.nstr(ell, 12)}")
    crit = (1 - ell) / theta
    check("4.6 (1 - l)/theta = 12.2967, rounded up to J = 13",
          mp.nstr(crit, 6) == "12.2967" and int(mpceil(crit)) == 13,
          f"criterion = {mp.nstr(crit, 8)}")

    # 4.7 HIS NEW RESULT: maxgap stays exactly theta for J = 13..25 and first
    # falls at J = 26, to 14*theta - 1; the splitting is one interval at a time.
    ok_plateau = True
    for J in range(13, 26):
        mg, gaps = maxgap(theta, J)
        if abs(mg - theta) > mpf(10) ** (-(dps - 10)):
            ok_plateau = False
        # structurally: exactly 26 - J unsplit theta-gaps remain
        n_theta = sum(1 for g in gaps if abs(g - theta) < mpf(10) ** (-(dps - 10)))
        if n_theta != 26 - J:
            ok_plateau = False
    check("4.7 maxgap(J) = theta exactly for J = 13..25, "
          "with 26-J unsplit theta-gaps at each J", ok_plateau)
    mg26, gaps26 = maxgap(theta, 26)
    check("4.7 first fall at J = 26: maxgap = 14*theta - 1 = 0.0526249495",
          abs(mg26 - (14 * theta - 1)) < mpf(10) ** (-(dps - 10))
          and sig_matches(mg26, "0.0526249495"),
          f"maxgap(26) = {mp.nstr(mg26, 12)}")
    n_long = sum(1 for g in gaps26 if abs(g - (14 * theta - 1)) < mpf("1e-20"))
    n_short = sum(1 for g in gaps26 if abs(g - (1 - 13 * theta)) < mpf("1e-20"))
    check("4.7 gap multiset at J = 26: thirteen (14theta-1) + fourteen (1-13theta)",
          (n_long, n_short, len(gaps26)) == (13, 14, 27),
          f"({n_long}, {n_short}, {len(gaps26)})")
    # the identity 13(14theta - 1) + 14(1 - 13theta) = 1, SYMBOLICALLY:
    # coefficient of theta: 13*14 - 14*13 = 0; constant: -13 + 14 = 1.
    coeff_theta = 13 * 14 - 14 * 13
    const = -13 + 14
    check("4.7 13(14theta-1) + 14(1-13theta) = 1 identically (0*theta + 1)",
          coeff_theta == 0 and const == 1)
    # splitting one at a time: each point j = 14..26 lands in a distinct
    # original theta-interval [(j-14)*theta, (j-13)*theta).
    landed = []
    for j in range(14, 27):
        pos = (j * theta) % 1
        idx = int(mpfloor(pos / theta))
        frac_in = pos - idx * theta
        landed.append(idx)
        if not (abs(frac_in - (14 * theta - 1)) < mpf("1e-20")):
            landed.append(None)
    check("4.7 points j = 14..26 split the 13 theta-intervals one at a time, "
          "each at offset 14theta-1",
          None not in landed and sorted(landed) == list(range(13)),
          f"intervals hit = {sorted(x for x in landed if x is not None)}")

    # 4.8 margin l - theta = 2.5157e-4 = 0.3335% of the arc.
    margin = ell - theta
    check("4.8 l - theta = 2.5157e-4", mp.nstr(margin, 5) == "0.00025157",
          f"margin = {mp.nstr(margin, 8)}")
    check("4.8 margin = 0.3335% of arc length l",
          mp.nstr(100 * margin / ell, 4) == "0.3335",
          f"{mp.nstr(100 * margin / ell, 6)} %")

    # 4.9 cost, not failure: 66 -> 131 consecutive integers; p >= 16 -> p >= 18.
    check("4.9 sweep sizes: 5*13+1 = 66 and 5*26+1 = 131",
          5 * 13 + 1 == 66 and 5 * 26 + 1 == 131)
    check("4.9 window sizes 0.05*L^p: 125.7 at p = 17, 199.2 at p = 18",
          mp.nstr(mpf("0.05") * L ** 17, 4) == "125.7"
          and mp.nstr(mpf("0.05") * L ** 18, 4) == "199.2",
          f"{mp.nstr(mpf('0.05') * L ** 17, 6)}, {mp.nstr(mpf('0.05') * L ** 18, 6)}")
    counts = {}
    for p in (15, 16, 17, 18):
        lo = int(mpceil(L ** p))
        hi = int(mpfloor(mpf("1.05") * L ** p))
        counts[p] = hi - lo + 1
    check("4.9 exact integer counts: p=15,16 hold 66 first at 16; "
          "131 first at p = 18",
          counts[15] < 66 <= counts[16] and counts[16] < 131
          and counts[17] < 131 <= counts[18],
          f"counts = {counts}")

    # ================================================================ PART 5
    print("\n-- PART 5: the CRLF arithmetic --")
    check("5.1 3,100 bytes + 75 lines (LF -> CRLF, one byte per line) = 3,175",
          3100 + 75 == 3175)

    return [(name, ok) for name, ok in CHECKS[verdicts_start:]]


def main():
    v1 = run(120)
    v2 = run(240)
    names1 = [(n, ok) for n, ok in v1]
    names2 = [(n, ok) for n, ok in v2]
    robust = names1 == names2
    print(f"\n{'=' * 74}\nROUNDING ROBUSTNESS: verdict lists at dps=120 and dps=240 "
          f"{'IDENTICAL' if robust else 'DIFFER'}")
    total = len(CHECKS)
    fails = [n for n, ok in CHECKS if not ok]
    print(f"TOTAL CHECKS: {total} ({len(names1)} distinct x 2 precisions)")
    print(f"FAILURES: {len(fails)}")
    for n in fails:
        print(f"  FAILED: {n}")
    if fails or not robust:
        sys.exit(1)
    print("RESULT: ALL CHECKS PASS AT BOTH PRECISIONS")


if __name__ == "__main__":
    main()
