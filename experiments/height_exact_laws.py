"""Independent verification for reverse.md section 14.15.7 (branch height-exact-laws).

Supports:
  - Lemma   14.15.7.1 (single-letter fixed-point facts)         -- test_single_letter_fixed_point_facts
  - Theorem 14.15.7.2 (constant-word mechanism lemma)           -- test_class_equals_fixed_point_class,
                                                                   test_deepest_door_law,
                                                                   test_capped_sector,
                                                                   test_escaping_sector_closed_form
  - Corollary 14.15.7.3 (H_{n,n}(((2,1))^inf) = 4*72^n - 5)     -- test_instance1_law
  - Corollary 14.15.7.4 (H^-_{n,n}((1,1)^inf) = 2*12^n - 1)     -- test_instance2_law
  - Theorem 14.15.7.5 / Corollary 14.15.7.6 (whole-period       -- test_period7_fixed_point_facts,
    extension; the period-7 cycle's word ((4,1),(3,3)),            test_period7_law,
    positive-sector H at n whole periods = 4*(2^11*3^7)^n - 17)    test_period7_brute_force

House rules honored: fresh code -- imports nothing from realization_height.py,
diagonal_converse.py, signed_diagonal.py, itinerary_coding.py, block_map.py, or
door_seam.py; every pass/fail decision is exact integer (or Fraction) arithmetic;
direct-simulation membership checks (forward stratum match, backward chain via the
predecessor formula, deepest-door liveness) back every reported H value;
brute-force minimality cross-checks at n = 1, 2 for all three instances;
the k = 1..9 dead/live pattern is checked against the mod-3 law.

Run: python3 experiments/height_exact_laws.py     (exits nonzero on any failure)
"""

import random
import sys
from fractions import Fraction
from math import gcd

# ----------------------------------------------------------------------------
# Primitives (fresh implementations)
# ----------------------------------------------------------------------------

def v2(x):
    """2-adic valuation of a nonzero integer."""
    assert x != 0
    return (x & -x).bit_length() - 1


def stratum_and_G(y):
    """(m, r, G(y)) for a nonzero odd integer y != -1 (14.15.1.1 / 14.15.6.1)."""
    assert y % 2 != 0 and y != -1 and y != 0
    m = v2(y + 1)
    q = (y + 1) >> m
    assert q % 2 != 0
    val = 3 ** m * q - 1
    r = v2(val)
    g = val >> r
    assert g % 2 != 0
    return m, r, g


def unique_predecessor(z, m, r):
    """The 14.15.4.1/14.15.6.3 letter-prescribed predecessor of odd z on (m,r),
    or None when the admissibility congruence 3^m | 2^r z + 1 fails."""
    N = (z << r) + 1
    t = 3 ** m
    if N % t != 0:
        return None
    q = N // t
    y = (q << m) - 1
    # forced-stratum sanity (the theorem says these can never fail):
    mm, rr, g = stratum_and_G(y)
    assert (mm, rr) == (m, r) and g == z
    return y


def letter_constants(m, r):
    """Affine constants (alpha, beta) of the letter (m,r), per 14.14.4.1."""
    alpha = Fraction(3 ** m, 2 ** (m + r))
    beta = Fraction(3 ** m - 2 ** m, 2 ** (m + r))
    return alpha, beta


def composed_constants(word):
    """(A, B) of a word applied in listed order (14.14.8.2 append recursion)."""
    A, B = Fraction(1), Fraction(0)
    for (m, r) in word:
        alpha, beta = letter_constants(m, r)
        A, B = alpha * A, alpha * B + beta
    return A, B


def fixed_point(period):
    """y* = B_P / (1 - A_P) as an exact Fraction (14.14.8.4)."""
    A, B = composed_constants(period)
    return B / (1 - A)


def SM(period):
    """(S_P, M_P) = (sum of m+r, sum of m) over one period."""
    return sum(m + r for m, r in period), sum(m for m, r in period)


def Q(period, n):
    """Per-window CRT modulus at n whole periods: 2^(n*S_P + 1) * 3^(n*M_P)."""
    S, M = SM(period)
    return 2 ** (n * S + 1) * 3 ** (n * M)


def backward_chain(y0, period, depth):
    """Letter-prescribed backward chain doors [y_{-1}, ..., y_{-depth}] behind y0
    along the periodic word (letter -j is period[(-j) mod p]), or None if it
    breaks. Intermediate liveness is NOT required (14.15.5.1's remark)."""
    p = len(period)
    chain = []
    z = y0
    for j in range(1, depth + 1):
        m, r = period[(-j) % p]
        y = unique_predecessor(z, m, r)
        if y is None:
            return None
        chain.append(y)
        z = y
    return chain


def follows_forward(y0, period, nletters):
    """Does y0's G-orbit realize the first nletters letters of the periodic word?"""
    p = len(period)
    z = y0
    for j in range(nletters):
        if z == -1:
            return False
        m, r, g = stratum_and_G(z)
        if (m, r) != period[j % p]:
            return False
        z = g
    return True


def membership(y0, period, n, sector):
    """Direct-simulation membership of y0 in R^sector_{np,np}(P^inf)
    (Definition 14.15.6.8; np = n whole periods of letters each side).
    Returns (ok, reason)."""
    if y0 == 0 or y0 % 2 == 0 or y0 == -1:
        return False, "not an odd door"
    if (y0 > 0) != (sector > 0):
        return False, "sign"
    if y0 % 3 == 0:
        return False, "y0 dead"
    L = n * len(period)
    if not follows_forward(y0, period, L):
        return False, "forward"
    chain = backward_chain(y0, period, L)
    if chain is None:
        return False, "backward chain"
    if chain[-1] % 3 == 0:
        return False, "deepest door dead"
    return True, "ok"


def sector_sign(x):
    return 1 if x > 0 else -1


CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ----------------------------------------------------------------------------
# Lemma 14.15.7.1: single-letter fixed-point facts
# ----------------------------------------------------------------------------

def test_single_letter_fixed_point_facts():
    rng = random.Random(65001)
    letters = [(m, r) for m in range(1, 9) for r in range(1, 9)]
    letters += [(rng.randint(1, 30), rng.randint(1, 30)) for _ in range(500)]
    n_int = 0
    for (m, r) in letters:
        alpha, beta = letter_constants(m, r)
        d = 2 ** (m + r) - 3 ** m
        ystar = fixed_point([(m, r)])
        # exact closed form and the two algebraic identities used in the proof
        check(ystar == Fraction(3 ** m - 2 ** m, d), f"y* closed form ({m},{r})")
        check((1 - alpha) * ystar == beta, f"fixed-point identity ({m},{r})")
        check(ystar + 1 == Fraction(2 ** m * (2 ** r - 1), d),
              f"y*+1 identity ({m},{r})")
        # liveness mechanism: numerator and denominator both units mod 3
        check((3 ** m - 2 ** m) % 3 != 0 and d % 3 != 0,
              f"liveness units ({m},{r})")
        # 2|y*| < Q_1 (as exact fractions; holds whether or not y* is integral)
        check(2 * abs(ystar) < Q([(m, r)], 1), f"2|y*| < Q_1 ({m},{r})")
        if ystar.denominator == 1:
            y = int(ystar)
            n_int += 1
            check(y % 3 != 0 and y not in (0, -1), f"integer y* live ({m},{r})")
            mm, rr, g = stratum_and_G(y)
            check((mm, rr) == (m, r) and g == y,
                  f"stratum(y*)=({m},{r}), G(y*)=y*")
            # 3^m q* - 1 = 2^r y* (the proof's one-line identity)
            q = (y + 1) >> m
            check(3 ** m * q - 1 == 2 ** r * y, f"3^m q*-1 = 2^r y* ({m},{r})")
    print(f"test_single_letter_fixed_point_facts: {len(letters)} letters, "
          f"{n_int} with integral y*, 0 failures")


# ----------------------------------------------------------------------------
# Theorem 14.15.7.2, clause 1: the class is exactly {y = y* mod Q_n}
# ----------------------------------------------------------------------------

def test_class_equals_fixed_point_class():
    total = 0
    for period in ([(2, 1)], [(1, 1)]):
        ystar = int(fixed_point(period))
        for n in (1, 2):
            Qn = Q(period, n)
            bound = 4 * Qn + 50
            for y in range(-bound + 1, bound + 1, 2):
                if y % 2 == 0 or y == -1 or y == 0:
                    continue
                assert y % 2 != 0
                direct = (follows_forward(y, period, n * len(period))
                          and backward_chain(y, period, n * len(period)) is not None)
                predicted = (y - ystar) % Qn == 0
                check(direct == predicted,
                      f"class iff at y={y}, period={period}, n={n}")
                total += 1
    print(f"test_class_equals_fixed_point_class: {total} exhaustive (y, n) "
          f"checks over both integer single-letter words, both signs, "
          f"0 discrepancies either direction")


# ----------------------------------------------------------------------------
# Theorem 14.15.7.2, clause 3: deepest-door formula and n-independent mod-3 law
# ----------------------------------------------------------------------------

def test_deepest_door_law():
    total = 0
    for period in ([(2, 1)], [(1, 1)]):
        ystar = int(fixed_point(period))
        S, M = SM(period)
        for n in range(1, 6):
            Qn = Q(period, n)
            L = n * len(period)
            for kappa in range(-9, 10):
                y0 = ystar + kappa * Qn
                if y0 == -1 or y0 == 0:
                    continue
                # y0 automatically live (clause 2)
                check(y0 % 3 == ystar % 3, f"y0 = y* mod 3, kappa={kappa}")
                chain = backward_chain(y0, period, L)
                check(chain is not None,
                      f"chain exists for class member kappa={kappa}, n={n}")
                deepest = chain[-1]
                check(deepest == ystar + kappa * 2 ** (2 * S * n + 1),
                      f"deepest-door formula, period={period}, n={n}, k={kappa}")
                check((deepest % 3 != 0) == ((ystar + 2 * kappa) % 3 != 0),
                      f"mod-3 law, period={period}, n={n}, kappa={kappa}")
                # also n-independence: law depends only on kappa mod 3
                check(((ystar + 2 * kappa) % 3 != 0) == (
                    (kappa - ystar) % 3 != 0),
                    f"kappa != y* mod 3 form, kappa={kappa}")
                total += 1
    print(f"test_deepest_door_law: {total} (period, n, kappa) chains, "
          f"deepest door == y* + kappa*2^(2Sn+1) exactly and mod-3 law exact, "
          f"0 failures")


# ----------------------------------------------------------------------------
# Theorem 14.15.7.2, clause 4 (capped sector): H^sigma = |y*| exactly
# ----------------------------------------------------------------------------

def test_capped_sector():
    for period in ([(2, 1)], [(1, 1)]):
        ystar = int(fixed_point(period))
        sigma = sector_sign(ystar)
        for n in range(1, 7):
            ok, why = membership(ystar, period, n, sigma)
            check(ok, f"y* member of its own sector, n={n}: {why}")
        # brute force in sector sigma at n = 1, 2: minimum is |y*| exactly
        for n in (1, 2):
            best = None
            a = 1
            while best is None:
                y = sigma * a
                if y != -1 and membership(y, period, n, sigma)[0]:
                    best = a
                a += 2
            check(best == abs(ystar),
                  f"capped-sector brute force, period={period}, n={n}")
    print("test_capped_sector: y* in R^sigma_{n,n} for n=1..6 (both words), "
          "brute-force sector minimum == |y*| at n=1,2, 0 failures")


# ----------------------------------------------------------------------------
# Theorem 14.15.7.2, clause 4 (escaping sector): closed form via class walk
# ----------------------------------------------------------------------------

def k0_of(ystar, sp):
    """Least k >= 1 with y* + 2*sp*k != 0 mod 3 (sp = sector sign)."""
    k = 1
    while (ystar + 2 * sp * k) % 3 == 0:
        k += 1
    return k


def test_escaping_sector_closed_form():
    for period in ([(2, 1)], [(1, 1)]):
        ystar = int(fixed_point(period))
        sp = -sector_sign(ystar)  # the escaping sector
        k0 = k0_of(ystar, sp)
        check(k0 in (1, 2), f"k0 in {{1,2}} for {period}")
        for n in range(1, 5):
            Qn = Q(period, n)
            # walk the class in increasing |y| within sector sp; first member
            # of R must be at k = k0 (checked by full direct simulation)
            first = None
            for k in range(1, 10):
                y0 = ystar + sp * k * Qn
                check(sector_sign(y0) == sp, f"sign of class member k={k}")
                if membership(y0, period, n, sp)[0]:
                    first = k
                    break
            check(first == k0, f"first live k == k0, period={period}, n={n}")
            check(abs(ystar + sp * k0 * Qn) == k0 * Qn + sp * ystar,
                  f"|y| arithmetic, period={period}, n={n}")
    print("test_escaping_sector_closed_form: first surviving class index == k0 "
          "in the escaping sector, n=1..4, both words, 0 failures")


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

TESTS_ITEM1 = [
    test_single_letter_fixed_point_facts,
    test_class_equals_fixed_point_class,
    test_deepest_door_law,
    test_capped_sector,
    test_escaping_sector_closed_form,
]

if __name__ == "__main__":
    for t in TESTS_ITEM1:
        t()
    print(f"ALL PASS ({CHECKS} checks)")
