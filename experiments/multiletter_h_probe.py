#!/usr/bin/env python3
"""multiletter_h_probe.py — empirical probe: per-sector realization heights
H^sigma_{np,np} on multi-letter periodic words W = P^inf (period p in {2,3})
whose composed-affine fixed point y* = B_P/(1-A_P) is a NON-INTEGRAL rational.

Supports: briefs/multiletter-h-probe-findings.md (branch multiletter-h-probe,
2026-07-17, per briefs/multiletter-h-probe-brief.md — an author-authorized
bounded exception, 2026-07-17, to the standing stop lines 14.15.4(d)/
14.15.6(e)/14.15.7(d); the exception covers exactly the brief's scope).

WHOLE-PERIOD DIAGONAL WINDOWS ONLY (reverse.md 14.15.7.5's convention and its
scope note): window (np, np) in letters = n whole periods each side, anchored
at the word's fixed origin. Windows that cut a period partway (per-letter
refinement) are out of bounds there and here.

Definitions are implemented FRESH from the wiki text (cited per function):
  - stratum(y), G(y)                       reverse.md 14.15.1.1 / 14.15.6.1
  - unique predecessor formula             reverse.md 14.15.4.1 / 14.15.6.3
  - R^sigma_{p,q}, H^sigma_{p,q}           reverse.md 14.15.6.8
  - composed affine constants A_P, B_P     reverse.md 14.14.8.2 (application
    order = deepest-first for the backward window, per 14.15.5.1's order note)
  - fixed point y* = B_P/(1-A_P)           reverse.md 14.14.8.4
This file imports NOTHING from h_nonintegral_probe.py, height_exact_laws.py,
realization_height.py, diagonal_converse.py, signed_diagonal.py,
itinerary_coding.py, block_map.py, or door_seam.py (brief rule / AGENTS.md).

Method notes (binding, from the brief):
  - All pass/fail and minimality decisions use exact int/Fraction arithmetic.
  - Every reported H value is verified by DIRECT SIMULATION only, never by
    class reasoning alone: forward stratum match over np letters via iterated
    G; backward letter-prescribed chain to depth np via the unique-predecessor
    formula with integrality checked at every step; liveness of y0 and of the
    deepest chain door; sector sign; y != -1 throughout.
  - Brute-force cross-checks at n = 1 for every word/sector scan all odd
    integers of the sector in increasing |y| with no class construction; at
    n = 2 the same where feasible, else the forward-class-progression fallback
    (representative constructed and then VERIFIED by direct simulation; class
    completeness from the merged cylinder theorem 14.15.1.5/14.15.6.5 only —
    no CRT/3-adic class reasoning), the deviation 14.15.7.6's own verification
    already records for its n = 2 check.
  - The deepest chain door's value and mod-3 residue are DERIVED (exact
    Fraction formula y_{-np} = y* + (y0 - y*)/A_P^n) and CHECKED against the
    simulated chain, not assumed.

Deterministic throughout: no randomness is used anywhere (no seeds to record).
Date of run recorded in output. Runs end-to-end in minutes.
"""

from fractions import Fraction
from math import gcd
import sys
import time

# ----------------------------------------------------------------------------
# Core primitives (fresh implementations)
# ----------------------------------------------------------------------------


def v2(x: int) -> int:
    """2-adic valuation of a nonzero integer."""
    assert x != 0
    return (x & -x).bit_length() - 1


def v3(x: int) -> int:
    """3-adic valuation of a nonzero integer."""
    assert x != 0
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def stratum_and_G(y: int):
    """(m, r, G(y)) for a nonzero odd integer y != -1  (14.15.1.1 / 14.15.6.1).

    m = v2(y+1), q = (y+1)/2^m, r = v2(3^m q - 1), G(y) = (3^m q - 1)/2^r.
    Sign-blind algebra; undefined exactly at y = -1 (v2(0) = inf).
    """
    assert y % 2 != 0 and y != -1 and y != 0
    m = v2(y + 1)
    q = (y + 1) >> m
    val = 3**m * q - 1
    assert val != 0  # val ≡ 2 (mod 3), never zero
    r = v2(val)
    return m, r, val >> r


def unique_predecessor(z: int, m: int, r: int):
    """The letter-prescribed predecessor of z on letter (m, r), or None.

    14.15.4.1 / 14.15.6.3: y = 2^m (2^r z + 1)/3^m - 1, an odd integer iff
    3^m | 2^r z + 1; when it exists it automatically has the same sign as z,
    is never -1, and lies on stratum exactly (m, r).
    """
    N = (z << r) + 1
    if N % 3**m != 0:
        return None
    q = N // 3**m
    return (q << m) - 1


def modinv(a: int, mod: int) -> int:
    return pow(a, -1, mod)


def mult_order(g: int, q: int) -> int:
    """Multiplicative order of g mod q (gcd(g,q)=1), by direct search."""
    assert gcd(g, q) == 1
    x, k = g % q, 1
    while x != 1:
        x = x * g % q
        k += 1
        assert k <= q, "order search overran modulus"
    return k


# ----------------------------------------------------------------------------
# Word data: period P = ((m_0,r_0),...,(m_{p-1},r_{p-1})), W = P^inf
# ----------------------------------------------------------------------------


def word_sums(P):
    """(S_P, M_P) = (sum of m_i+r_i, sum of m_i)."""
    return sum(m + r for (m, r) in P), sum(m for (m, r) in P)


def letter_affine(m: int, r: int):
    """(alpha, beta) with G(y) = alpha*y + beta on stratum (m,r) (14.14.4.1,
    as restated in 14.14.8.2): alpha = 3^m/2^(m+r), beta = (3^m-2^m)/2^(m+r)."""
    return (Fraction(3**m, 2 ** (m + r)),
            Fraction(3**m - 2**m, 2 ** (m + r)))


def composed_constants(P):
    """(A_P, B_P) of 14.14.8.2, letters processed in APPLICATION order (the
    letter applied first — P_0, the origin letter — listed first; append
    recursion A <- alpha*A, B <- alpha*B + beta). Per 14.15.5.1's order note,
    for the whole-period backward window the past np letters read deepest-
    first are exactly P repeated n times (14.15.7.5's proof, step (iii)), so
    this single ordering serves both the forward and the backward half."""
    A, B = Fraction(1), Fraction(0)
    for (m, r) in P:
        alpha, beta = letter_affine(m, r)
        A = alpha * A
        B = alpha * B + beta
    return A, B


def fixed_point(P) -> Fraction:
    """y* = B_P/(1-A_P)  (14.14.8.4). A_P != 1 always (v3(A_P) = M_P >= 1)."""
    A, B = composed_constants(P)
    return B / (1 - A)


def rotations(P):
    """All p cyclic rotations of P, rotation i starting at letter P_i."""
    p = len(P)
    return [tuple(P[(i + j) % p] for j in range(p)) for i in range(len(P))]


def canonical_rotation(P):
    """Lexicographically least rotation — the rotation-class representative."""
    return min(rotations(P))


# ----------------------------------------------------------------------------
# Sanity anchors (known fixed points, cited; checked at startup)
# ----------------------------------------------------------------------------


def sanity_anchors():
    """Known composed fixed points, exact: ((1,1)) -> 1 (14.14.8.4's sanity
    instance), ((2,1)) -> -5 (14.15.5(c)), ((4,1),(3,3)) -> -17
    (14.15.6(d)(ii) / 14.15.7.6). Plus: each is a genuine G-cycle on its word,
    checked by direct iteration."""
    checks = [((( 1, 1),), Fraction(1)),
              ((( 2, 1),), Fraction(-5)),
              ((( 4, 1), (3, 3)), Fraction(-17))]
    for P, want in checks:
        got = fixed_point(P)
        assert got == want, f"fixed-point anchor failed: {P} -> {got} != {want}"
        y = int(want)
        for (m, r) in P:
            mm, rr, gy = stratum_and_G(y)
            assert (mm, rr) == (m, r), f"anchor stratum failed at {P}"
            y = gy
        assert y == int(want), f"anchor cycle failed at {P}"
    return len(checks)


# ----------------------------------------------------------------------------
# Item 1: the instance grid
# ----------------------------------------------------------------------------

LETTERS = [(1, 1), (1, 2), (2, 1), (2, 2)]  # {1,2}^2, lex order


def period2_grid():
    """All 16 ordered pairs of letters in {1,2}^2, y* exact, disposition:
      - integral y*            -> excluded (exact-law shelf, 14.15.7.5)
      - non-canonical rotation -> excluded from the main grid (kept for M4)
      - else                   -> probed (constant pairs noted as coinciding
                                  with the single-letter word at doubled
                                  windows — retained as consistency anchors)
    Returns (all_rows, probed_words)."""
    rows, probed = [], []
    for l0 in LETTERS:
        for l1 in LETTERS:
            P = (l0, l1)
            ystar = fixed_point(P)
            integral = ystar.denominator == 1
            canon = (P == canonical_rotation(P))
            constant = (l0 == l1)
            if integral:
                disp = "integral y* — excluded (exact-law shelf, 14.15.7.5)"
            elif not canon:
                disp = "rotation of an included word — excluded (kept for M4)"
            elif constant:
                disp = ("probed (constant pair — single-letter word at "
                        "doubled windows; consistency anchor)")
                probed.append(P)
            else:
                disp = "probed"
                probed.append(P)
            rows.append((P, ystar, disp))
    return rows, probed


def period3_census_and_selection(n_select: int = 5):
    """All 64 ordered triples of letters in {1,2}^2, deduped to canonical
    rotation classes; constant triples excluded (they are period-1 words,
    covered by the single-letter probe); integral y* excluded (recorded).
    Selection: walking the canonical classes in lex order, take each word
    whose denominator q has not yet been taken, until n_select words —
    deterministic, chosen to vary q per the brief."""
    classes = sorted({canonical_rotation((a, b, c))
                      for a in LETTERS for b in LETTERS for c in LETTERS})
    census, selected, taken_q = [], [], set()
    for P in classes:
        constant = len(set(P)) == 1
        ystar = fixed_point(P)
        integral = ystar.denominator == 1
        if constant:
            disp = "constant — period-1 word, excluded (single-letter shelf)"
        elif integral:
            disp = "integral y* — excluded (exact-law shelf, 14.15.7.5)"
        elif ystar.denominator in taken_q:
            disp = "q already represented — not selected"
        elif len(selected) < n_select:
            disp = "SELECTED"
            selected.append(P)
            taken_q.add(ystar.denominator)
        else:
            disp = "not selected (selection full)"
        census.append((P, ystar, disp))
    return census, selected


def word_str(P):
    return "(" + ",".join(f"({m},{r})" for (m, r) in P) + ")"


def print_item1():
    print("=" * 74)
    print("Item 1: instance grid")
    print("=" * 74)
    print(f"\nSanity anchors (known fixed points, exact): "
          f"{sanity_anchors()} checked, all OK "
          f"(((1,1))->1, ((2,1))->-5, ((4,1),(3,3))->-17)")

    rows2, probed2 = period2_grid()
    print("\nPeriod-2 grid: all 16 ordered pairs, letters in {1,2}^2")
    for (P, ystar, disp) in rows2:
        print(f"  {word_str(P):>18}  y* = {str(ystar):>8}   [{disp}]")

    census3, selected3 = period3_census_and_selection()
    print(f"\nPeriod-3 census: {len(census3)} rotation classes of the 64 "
          f"ordered triples")
    for (P, ystar, disp) in census3:
        print(f"  {word_str(P):>24}  y* = {str(ystar):>12}   [{disp}]")

    words = ([(P, 2) for P in probed2] + [(P, 3) for P in selected3])
    print(f"\nProbed words: {len(probed2)} period-2 + {len(selected3)} "
          f"period-3 = {len(words)} total")
    print(f"\n{'word':>24} {'p':>2} {'y* = a/q':>14} {'S_P':>4} {'M_P':>4} "
          f"{'g_P':>6} {'ord_q(g_P)':>10}")
    grid = []
    for (P, p) in words:
        S, M = word_sums(P)
        ystar = fixed_point(P)
        a, q = ystar.numerator, ystar.denominator
        assert q > 1 and gcd(q, 6) == 1, "probed word must have q>1, (q,6)=1"
        g = (2**S * 3**M) % q
        ordg = mult_order(g, q)
        grid.append((P, p, a, q, S, M, g, ordg))
        print(f"{word_str(P):>24} {p:>2} {f'{a}/{q}':>14} {S:>4} {M:>4} "
              f"{g:>6} {ordg:>10}")
    return grid


# ----------------------------------------------------------------------------
# main (extended per queue item)
# ----------------------------------------------------------------------------


def main():
    t0 = time.time()
    print("multiletter_h_probe.py — run date 2026-07-17 (deterministic, "
          "no RNG)")
    grid = print_item1()
    print(f"\ntotal time: {time.time() - t0:.1f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
