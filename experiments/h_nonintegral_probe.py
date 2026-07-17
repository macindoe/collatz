#!/usr/bin/env python3
"""
h_nonintegral_probe.py — empirical probe: per-sector realization heights
H^sigma_{n,n} on constant words ((m,r))^inf whose composed-affine fixed point
y* = beta/(1-alpha) is a NON-INTEGRAL rational.

Supports: briefs/h-nonintegral-probe-findings.md (branch h-nonintegral-probe,
2026-07-17, per briefs/h-nonintegral-probe-brief.md — an author-authorized
bounded exception to the standing stop lines 14.15.4(d)/14.15.6(e)).

Definitions are implemented FRESH from the wiki text (cited per function):
  - stratum(y), G(y)                       reverse.md 14.15.1.1 / 14.15.6.1
  - unique predecessor formula             reverse.md 14.15.4.1 / 14.15.6.3
  - R^sigma_{p,q}, H^sigma_{p,q}           reverse.md 14.15.6.8
  - composed affine constants, y*          reverse.md 14.14.8.2 / 14.14.8.4
This file imports NOTHING from realization_height.py, diagonal_converse.py,
signed_diagonal.py, itinerary_coding.py, block_map.py, or door_seam.py
(brief rule / AGENTS.md).

Method notes (binding, from the brief):
  - All pass/fail and minimality decisions use exact int/Fraction arithmetic.
  - Every reported H value is re-verified by DIRECT SIMULATION, never by class
    reasoning alone: forward stratum match letter by letter via iterated G;
    backward chain via the unique-predecessor formula with integrality checked
    at every step; liveness of y0 and of the deepest chain door; sector sign;
    y != -1 throughout.
  - Brute-force cross-checks at n = 1, 2 for every word/sector scan all odd
    integers of the sector in increasing |y| with no class construction.
  - The deepest chain door's value and mod-3 residue are DERIVED (exact
    Fraction formula y_{-n} = y* + (y0 - y*)/A_n) and CHECKED against the
    simulated chain, not assumed.

Deterministic throughout: no randomness is used anywhere (no seeds to record).
Date of run recorded in output. Runs end-to-end in minutes.
"""

from fractions import Fraction
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


# ----------------------------------------------------------------------------
# Word data: constant word ((m,r))^inf
# ----------------------------------------------------------------------------


def affine_constants(m: int, r: int):
    """(alpha, beta) with G(y) = alpha*y + beta on stratum (m,r) (14.14.4.1,
    as restated in 14.14.8.2): alpha = 3^m/2^(m+r), beta = (3^m-2^m)/2^(m+r)."""
    alpha = Fraction(3**m, 2 ** (m + r))
    beta = Fraction(3**m - 2**m, 2 ** (m + r))
    return alpha, beta


def fixed_point(m: int, r: int) -> Fraction:
    """y* = beta/(1-alpha) = (3^m - 2^m)/(2^(m+r) - 3^m)   (14.14.8.4)."""
    alpha, beta = affine_constants(m, r)
    return beta / (1 - alpha)


def modinv(a: int, mod: int) -> int:
    return pow(a, -1, mod)


def class_data(m: int, r: int, n: int):
    """(Q_n, rho_n, j_n) for the constant word ((m,r))^inf at window (n,n).

    Q_n = 2^((m+r)n+1) * 3^(mn)  (forward cylinder modulus 2^(S_n+1),
    S_n = (m+r)n, per 14.15.1.5; backward admissibility modulus 3^(M_n),
    M_n = mn, per 14.15.5.1/14.15.6.4).

    rho_n = the CRT lift of y* = a/q into Z/Q_n (q coprime to 6, so y* is a
    2-adic and 3-adic integer); j_n = (q*rho_n - a)/Q_n in {0..q-1}, so that
    rho_n/Q_n = j_n/q + a/(q Q_n) exactly.
    """
    ystar = fixed_point(m, r)
    a, q = ystar.numerator, ystar.denominator
    Q = 2 ** ((m + r) * n + 1) * 3 ** (m * n)
    rho = (a % Q) * modinv(q, Q) % Q
    jq, rem = divmod(q * rho - a, Q)
    assert rem == 0
    assert 0 <= jq < q
    return Q, rho, jq


# ----------------------------------------------------------------------------
# Direct-simulation membership test (no class reasoning)
# ----------------------------------------------------------------------------


def member_direct(y0: int, m: int, r: int, n: int, sigma: int):
    """Direct test: y0 in R^sigma_{n,n}(((m,r))^inf)?  (14.15.6.8)

    Returns (ok, reason, deepest) where reason names the first failed
    condition ('sign', 'singular', 'y0_dead', 'forward', 'backward',
    'deepest_dead') and deepest is the simulated deepest chain door y_{-n}
    (None unless the backward chain fully exists).
    Every condition is checked by direct computation on y0 itself.
    """
    if y0 == 0 or y0 % 2 == 0 or (sigma > 0) != (y0 > 0):
        return False, "sign", None
    if y0 == -1:
        return False, "singular", None
    if y0 % 3 == 0:
        return False, "y0_dead", None
    # forward: stratum(G^j(y0)) == (m,r) for j = 0..n-1, by iterating G
    y = y0
    for _ in range(n):
        if y == -1:  # singular point mid-orbit (14.15.6.2(4)); cannot continue
            return False, "forward", None
        mm, rr, gy = stratum_and_G(y)
        if (mm, rr) != (m, r):
            return False, "forward", None
        y = gy
    # backward: letter-prescribed chain to depth n via 14.15.4.1's formula,
    # integrality checked at every step (intermediate liveness NOT required,
    # per 14.15.5.1's remark)
    z = y0
    for _ in range(n):
        z = unique_predecessor(z, m, r)
        if z is None:
            return False, "backward", None
    if z % 3 == 0:
        return False, "deepest_dead", z
    return True, "ok", z


# ----------------------------------------------------------------------------
# Height via candidate scan (class representative + increasing |y0|),
# every candidate verified by direct simulation
# ----------------------------------------------------------------------------


def height_scan(m: int, r: int, n: int, sigma: int, k_cap: int = 50):
    """H^sigma_{n,n} for the constant word, by scanning the CRT progression
    rho_n + k*Q_n in increasing |y0| within the sector, testing every
    candidate by direct simulation (member_direct).

    Returns dict with H, first-viable k, Q, rho, j, failures (list of
    (k, reason) for candidates rejected before the first viable one),
    deepest (simulated deepest door), deepest_mod3.

    k convention: sigma=+1: y0 = rho + k*Q, k = 0,1,2,...
                  sigma=-1: y0 = rho - k*Q, k = 1,2,3,...
    """
    Q, rho, jq = class_data(m, r, n)
    failures = []
    ks = range(0, k_cap) if sigma > 0 else range(1, k_cap + 1)
    for k in ks:
        y0 = rho + k * Q if sigma > 0 else rho - k * Q
        ok, reason, deepest = member_direct(y0, m, r, n, sigma)
        if ok:
            return {
                "H": abs(y0), "y0": y0, "k": k, "Q": Q, "rho": rho, "j": jq,
                "failures": failures, "deepest": deepest,
                "deepest_mod3": deepest % 3,
            }
        failures.append((k, reason))
    raise RuntimeError(
        f"SHORTFALL: no viable candidate within k_cap={k_cap} "
        f"for (m,r)=({m},{r}) n={n} sigma={sigma:+d}"
    )


def deepest_door_formula(m: int, r: int, n: int, y0: int) -> Fraction:
    """Deepest door via the composed-affine relation, derived not assumed:
    y0 = A_n y_{-n} + B_n on the class (14.14.8.2), i.e.
    y_{-n} = y* + (y0 - y*)/A_n with A_n = alpha^n (14.15.5.1's own algebra).
    Exact Fraction arithmetic; caller compares against the simulated chain.
    """
    alpha, _ = affine_constants(m, r)
    ystar = fixed_point(m, r)
    return ystar + (Fraction(y0) - ystar) / alpha**n


# ----------------------------------------------------------------------------
# Brute-force cross-check (no class construction at all)
# ----------------------------------------------------------------------------


def brute_force_height(m: int, r: int, n: int, sigma: int, limit: int):
    """Scan ALL odd integers of sign sigma in increasing |y|, no class
    construction, returning the first member of R^sigma_{n,n} found (or None
    if |y| reaches limit first). A cheap direct prefilter (the first forward
    letter, i.e. stratum(y0) == (m,r)) is applied before the full test; it is
    itself part of the direct membership definition, not class reasoning.
    """
    three_m = 3**m
    mask = (1 << (m + 1)) - 1
    bit = 1 << m
    for ay in range(1, limit + 1, 2):
        y = ay * sigma
        if y == -1:
            continue
        # prefilter: v2(y+1) == m, computed directly
        if (y + 1) & mask != bit:
            continue
        ok, _, _ = member_direct(y, m, r, n, sigma)
        if ok:
            return abs(y)
    return None


# ----------------------------------------------------------------------------
# Item 1+2 driver: the grid and the exact height tables
# ----------------------------------------------------------------------------

GRID = [(m, r) for m in (1, 2, 3) for r in (1, 2, 3)]
N_MAX = 25          # brief: n = 1 to at least 15, further if cheap (it is)
BRUTE_N = (1, 2)    # brute-force cross-check windows


def compute_instance_grid():
    """Item 1: all single-letter words 1<=m,r<=3; y* computed exactly;
    integer-fixed-point words identified and excluded (they belong to the
    exact-law mechanism, companion brief's shelf)."""
    rows = []
    for (m, r) in GRID:
        ystar = fixed_point(m, r)
        integral = ystar.denominator == 1
        rows.append((m, r, ystar, integral))
    return rows


def compute_tables(words, n_max=N_MAX, verbose=True):
    """Item 2: exact height tables for each word, each sector, n = 1..n_max.
    Returns results[(m,r)][sigma] = list of per-n row dicts."""
    results = {}
    for (m, r) in words:
        results[(m, r)] = {}
        for sigma in (+1, -1):
            rows = []
            for n in range(1, n_max + 1):
                row = height_scan(m, r, n, sigma)
                # derive-and-check: deepest door from the exact affine formula
                dd = deepest_door_formula(m, r, n, row["y0"])
                assert dd.denominator == 1 and int(dd) == row["deepest"], (
                    f"deepest-door formula mismatch at (m,r)=({m},{r}) "
                    f"n={n} sigma={sigma:+d}")
                # every pre-viable failure should be deepest_dead only;
                # anything else violates the class setup — flag loudly
                for (k, reason) in row["failures"]:
                    if reason != "deepest_dead":
                        print(f"*** SURPRISE: candidate k={k} failed with "
                              f"'{reason}' at (m,r)=({m},{r}) n={n} "
                              f"sigma={sigma:+d} ***")
                rows.append(row)
            results[(m, r)][sigma] = rows
            if verbose:
                ystar = fixed_point(m, r)
                a, q = ystar.numerator, ystar.denominator
                print(f"\nword ((m,r))=(({m},{r}))^inf   y* = {a}/{q}   "
                      f"sector {'+' if sigma > 0 else '-'}")
                print(f"{'n':>3} {'H':>42} {'k':>2} {'j_n':>4} "
                      f"{'rho_n/Q_n':>10} {'H/Q_n':>10} {'nfail':>5}")
                for n, row in enumerate(rows, 1):
                    print(f"{n:>3} {row['H']:>42} {row['k']:>2} "
                          f"{row['j']:>4} "
                          f"{float(Fraction(row['rho'], row['Q'])):>10.6f} "
                          f"{float(Fraction(row['H'], row['Q'])):>10.6f} "
                          f"{len(row['failures']):>5}")
    return results


def run_brute_checks(words, results):
    """Brute-force cross-checks at n = 1, 2 for every word/sector."""
    print("\n" + "=" * 72)
    print("Brute-force cross-checks (n = 1, 2; full odd scan, no class "
          "construction)")
    print("=" * 72)
    n_checked = n_failed = 0
    for (m, r) in words:
        for sigma in (+1, -1):
            for n in BRUTE_N:
                H_class = results[(m, r)][sigma][n - 1]["H"]
                H_brute = brute_force_height(m, r, n, sigma, limit=H_class)
                n_checked += 1
                status = "OK" if H_brute == H_class else "MISMATCH"
                if H_brute != H_class:
                    n_failed += 1
                print(f"  (m,r)=({m},{r}) sigma={sigma:+d} n={n}: "
                      f"class H={H_class}  brute H={H_brute}  {status}")
    print(f"\nbrute-force cross-checks: {n_checked} run, {n_failed} mismatches")
    return n_failed == 0


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------


def main():
    t0 = time.time()
    print("h_nonintegral_probe.py — run date 2026-07-17 (deterministic, "
          "no RNG)")
    print("=" * 72)
    print("Item 1: instance grid (1 <= m,r <= 3), y* = (3^m-2^m)/(2^(m+r)-3^m)"
          " exact")
    print("=" * 72)
    words = []
    for (m, r, ystar, integral) in compute_instance_grid():
        tag = "INTEGER fixed point — excluded (exact-law shelf, companion " \
              "brief)" if integral else "non-integral — probed"
        print(f"  (m,r)=({m},{r}):  y* = {ystar}   [{tag}]")
        if not integral:
            words.append((m, r))
    assert len(words) == 7, "expected exactly seven non-integral words"

    print("\n" + "=" * 72)
    print(f"Item 2: exact height tables H^sigma_(n,n), n = 1..{N_MAX} "
          f"(every H verified by direct simulation)")
    print("=" * 72)
    results = compute_tables(words)

    brute_ok = run_brute_checks(words, results)

    print(f"\ntotal time: {time.time() - t0:.1f} s")
    print("brute-force cross-checks all matched:", brute_ok)
    return 0 if brute_ok else 1


if __name__ == "__main__":
    sys.exit(main())
