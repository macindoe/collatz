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
# Item 2: exact height tables — class scan with direct-simulation verification
# ----------------------------------------------------------------------------


def class_data(P, n):
    """(Q_n, rho_n, j_n) for W = P^inf at the whole-period window (np, np).

    Q_n = 2^(n S_P + 1) * 3^(n M_P): forward cylinder modulus 2^(S+1) over
    the signed domain (14.15.1.5 / 14.15.6.5), backward admissibility modulus
    3^M (14.15.5.1 / 14.15.6.4) — the brief's candidate progression.

    rho_n = a * q^{-1} mod Q_n (the CRT lift of y* = a/q; q coprime to 6);
    j_n = (q*rho_n - a)/Q_n, so that rho_n/Q_n = j_n/q + a/(q Q_n) exactly.
    """
    S, M = word_sums(P)
    ystar = fixed_point(P)
    a, q = ystar.numerator, ystar.denominator
    assert q > 1 and gcd(q, 6) == 1
    Q = 2 ** (n * S + 1) * 3 ** (n * M)
    rho = (a % Q) * modinv(q, Q) % Q
    j, rem = divmod(q * rho - a, Q)
    assert rem == 0
    assert 0 <= j < q
    return Q, rho, j


def member_direct(y0: int, P, n: int, sigma: int):
    """Direct test: y0 in R^sigma_{np,np}(P^inf)?  (Definition 14.15.6.8,
    whole-period window.) No class reasoning anywhere.

    Forward: stratum(G^j(y0)) = P_{j mod p} for j = 0..np-1, by iterating G.
    Backward: the letter-prescribed chain to depth np — the letter at depth i
    is W_{-i} = P_{(-i) mod p} — via 14.15.6.3's formula with integrality
    checked at every step (intermediate liveness not required, 14.15.5.1's
    remark); deepest door y_{-np} must be live.

    Returns (ok, reason, deepest): reason names the first failed condition
    ('sign', 'singular', 'y0_dead', 'forward', 'backward', 'deepest_dead').
    """
    p = len(P)
    if y0 == 0 or y0 % 2 == 0 or (sigma > 0) != (y0 > 0):
        return False, "sign", None
    if y0 == -1:
        return False, "singular", None
    if y0 % 3 == 0:
        return False, "y0_dead", None
    y = y0
    for j in range(n * p):
        if y == -1:  # singular point mid-orbit (14.15.6.2(4))
            return False, "forward", None
        mm, rr, gy = stratum_and_G(y)
        if (mm, rr) != P[j % p]:
            return False, "forward", None
        y = gy
    z = y0
    for i in range(1, n * p + 1):
        m, r = P[(-i) % p]
        z = unique_predecessor(z, m, r)
        if z is None:
            return False, "backward", None
    if z % 3 == 0:
        return False, "deepest_dead", z
    return True, "ok", z


def height_scan(P, n, sigma, k_cap: int = 60):
    """H^sigma_{np,np} by scanning the CRT progression rho_n + k*Q_n in
    increasing |y0| within the sector, testing every candidate by direct
    simulation (member_direct). Minimality over the full sector rests on the
    word-general class iffs (merged 14.15.1.5/14.15.6.5 forward,
    14.15.6.4 backward) and is cross-checked by brute force at n = 1, 2.

    k convention: sigma=+1: y0 = rho + k*Q, k = 0,1,2,...
                  sigma=-1: y0 = rho - k*Q, k = 1,2,3,...
    """
    Q, rho, j = class_data(P, n)
    failures = []
    ks = range(0, k_cap) if sigma > 0 else range(1, k_cap + 1)
    for k in ks:
        y0 = rho + k * Q if sigma > 0 else rho - k * Q
        ok, reason, deepest = member_direct(y0, P, n, sigma)
        if ok:
            return {"H": abs(y0), "y0": y0, "k": k, "Q": Q, "rho": rho,
                    "j": j, "failures": failures, "deepest": deepest,
                    "deepest_mod3": deepest % 3}
        failures.append((k, reason))
    raise RuntimeError(f"SHORTFALL: no viable candidate within k_cap={k_cap} "
                       f"for {word_str(P)} n={n} sigma={sigma:+d}")


def deepest_door_formula(P, n, y0) -> Fraction:
    """Deepest door via the composed-affine relation, derived not assumed:
    y0 = A_P^n y_{-np} + B_{np} on the chain (14.14.8.2) and
    A_P^n y* + B_{np} = y*, so y_{-np} = y* + (y0 - y*)/A_P^n.
    Exact Fraction arithmetic; caller compares against the simulated chain."""
    A, _ = composed_constants(P)
    ystar = fixed_point(P)
    return ystar + (Fraction(y0) - ystar) / A**n


def n_max_for(ordg: int) -> int:
    """Rows per word: at least 12 (brief floor 10), extended to ordg + 12
    when the algebraic period is longer (cheap: exact big-int arithmetic),
    capped at 130."""
    return max(12, min(ordg + 12, 130))


def compute_tables(grid, verbose=True):
    """Item 2: exact height tables, both sectors, n = 1..n_max(word).
    Per row: height_scan + deepest-door formula cross-check + loud flag on
    any pre-viable failure that is not deepest_dead."""
    results = {}
    surprises = 0
    for (P, p, a, q, S, M, g, ordg) in grid:
        nmax = n_max_for(ordg)
        results[P] = {}
        for sigma in (+1, -1):
            rows = []
            for n in range(1, nmax + 1):
                row = height_scan(P, n, sigma)
                dd = deepest_door_formula(P, n, row["y0"])
                assert dd.denominator == 1 and int(dd) == row["deepest"], (
                    f"deepest-door formula mismatch at {word_str(P)} "
                    f"n={n} sigma={sigma:+d}")
                for (k, reason) in row["failures"]:
                    if reason != "deepest_dead":
                        surprises += 1
                        print(f"*** SURPRISE: candidate k={k} failed with "
                              f"'{reason}' at {word_str(P)} n={n} "
                              f"sigma={sigma:+d} ***")
                rows.append(row)
            results[P][sigma] = rows
            if verbose:
                print(f"\nword {word_str(P)}^inf  y* = {a}/{q}  "
                      f"sector {'+' if sigma > 0 else '-'}  (n = 1..{nmax})")
                print(f"{'n':>4} {'H':>44} {'k':>2} {'j_n':>5} {'H/Q_n':>10} "
                      f"{'nfail':>5}")
                for n, row in enumerate(rows, 1):
                    hs = (str(row["H"]) if row["H"] < 10**40
                          else f"~10^{len(str(row['H'])) - 1} "
                               f"({str(row['H'])[:12]}...)")
                    print(f"{n:>4} {hs:>44} {row['k']:>2} {row['j']:>5} "
                          f"{float(Fraction(row['H'], row['Q'])):>10.6f} "
                          f"{len(row['failures']):>5}")
    return results, surprises


# ----------------------------------------------------------------------------
# Brute-force cross-checks (n = 1 always; n = 2 full scan where feasible,
# else forward-class-progression fallback)
# ----------------------------------------------------------------------------

FULL_SCAN_CAP = 25_000_000  # max |y| for a full odd scan (feasibility bound)


def brute_force_height(P, n, sigma, limit):
    """Scan ALL odd integers of sign sigma in increasing |y|, no class
    construction, returning the first member of R^sigma_{np,np} found (or
    None if |y| exceeds limit first). A cheap direct prefilter (v2(y+1) =
    m_0, part of the direct membership definition's first letter) is applied
    before the full test."""
    m0 = P[0][0]
    mask = (1 << (m0 + 1)) - 1
    bit = 1 << m0
    for ay in range(1, limit + 1, 2):
        y = ay * sigma
        if y == -1:
            continue
        if (y + 1) & mask != bit:  # Python & reduces negatives correctly
            continue
        ok, _, _ = member_direct(y, P, n, sigma)
        if ok:
            return abs(y)
    return None


def single_letter_rep(m, r):
    """The single residue mod 2^(m+r+1) of stratum (m,r), from 14.15.1.3(i):
    y = 2^m q - 1 with q ≡ 3^{-m}(1+2^r) (mod 2^{r+1})."""
    qres = ((1 + 2**r) * modinv(3**m, 2 ** (r + 1))) % 2 ** (r + 1)
    return 2**m * qres - 1


def forward_rep(P, nletters):
    """Constructive representative of the forward cylinder class of the first
    nletters letters of P^inf — 14.15.1.4's induction implemented directly
    (level-shift lemma for the lifting step), then VERIFIED by direct forward
    simulation before use. Returns (rep, mod) with mod = 2^(S+1)."""
    letters = [P[j % len(P)] for j in range(nletters)]
    m0, r0 = letters[0]
    rep = single_letter_rep(m0, r0)
    mod = 2 ** (m0 + r0 + 1)
    Mi = m0
    for i in range(1, nletters):
        m, r = letters[i]
        # z = G^i(rep), computed by direct iteration
        z = rep
        for jj in range(i):
            _, _, z = stratum_and_G(z)
        w = single_letter_rep(m, r)
        # level shift (14.15.1.4): G^i(rep + mod*t) = z + 2*3^Mi*t;
        # need z + 2*3^Mi*t ≡ w (mod 2^(m+r+1)); (w-z) even, 3^Mi a unit.
        t = (((w - z) // 2) * modinv(3**Mi, 2 ** (m + r))) % 2 ** (m + r)
        rep += mod * t
        mod <<= (m + r)
        Mi += m
    # verify by direct simulation: rep follows all nletters letters
    z = rep
    for (m, r) in letters:
        mm, rr, z = stratum_and_G(z)
        assert (mm, rr) == (m, r), "forward_rep failed direct verification"
    return rep, mod


def forward_class_height(P, n, sigma, limit):
    """Fallback minimality check where a full odd scan is infeasible (the
    deviation 14.15.7.6's verification records for its own n = 2 check):
    scan only the forward cylinder class (rep mod 2^(S+1), constructed above
    and verified by direct simulation; completeness of the class is the
    merged cylinder theorem 14.15.1.5/14.15.6.5 — every forward follower
    lies in it), testing every member by full direct simulation. No CRT or
    3-adic class reasoning. Returns (H or None, members_tested)."""
    rep, mod = forward_rep(P, n * len(P))
    count = 0
    if sigma > 0:
        y = rep if rep > 0 else rep + mod
        while y <= limit:
            count += 1
            ok, _, _ = member_direct(y, P, n, sigma)
            if ok:
                return y, count
            y += mod
    else:
        y = rep - mod
        while -y <= limit:
            count += 1
            ok, _, _ = member_direct(y, P, n, sigma)
            if ok:
                return -y, count
            y -= mod
    return None, count


def run_brute_checks(grid, results):
    """n = 1: full odd scan for every word/sector. n = 2: full odd scan where
    H <= FULL_SCAN_CAP, else the forward-class-progression fallback (recorded
    per word/sector). The scan limit is the class-scan H itself: any smaller
    member would be found first and reported as a mismatch."""
    print("\n" + "=" * 74)
    print("Brute-force cross-checks")
    print("=" * 74)
    n_checked = n_failed = n_fallback = 0
    for (P, p, a, q, S, M, g, ordg) in grid:
        for sigma in (+1, -1):
            for n in (1, 2):
                H_class = results[P][sigma][n - 1]["H"]
                if H_class <= FULL_SCAN_CAP:
                    H_brute = brute_force_height(P, n, sigma, limit=H_class)
                    method = "full odd scan"
                else:
                    H_brute, cnt = forward_class_height(P, n, sigma,
                                                        limit=H_class)
                    method = (f"forward-class fallback "
                              f"({cnt} members tested)")
                    n_fallback += 1
                n_checked += 1
                status = "OK" if H_brute == H_class else "MISMATCH"
                if H_brute != H_class:
                    n_failed += 1
                print(f"  {word_str(P):>24} sigma={sigma:+d} n={n}: "
                      f"class H={H_class}  brute H={H_brute}  "
                      f"[{method}]  {status}")
    print(f"\nbrute-force cross-checks: {n_checked} run "
          f"({n_fallback} via fallback), {n_failed} mismatches")
    return n_failed == 0


def consistency_vs_single_letter(results):
    """The two constant-pair period-2 words coincide with single-letter words
    at doubled windows: ((1,2),(1,2)) at n whole periods is the single-letter
    word (1,2) at window (2n,2n), so its n=1 heights must equal the published
    single-letter rows at n=2 — H+ = 461, H- = 691 for (1,2), and H+ = 23699,
    H- = 17773 for (2,2) (briefs/h-nonintegral-probe-findings.md §2, merged).
    """
    expect = {((1, 2), (1, 2)): (461, 691),
              ((2, 2), (2, 2)): (23699, 17773)}
    print("\nConsistency vs the merged single-letter probe "
          "(briefs/h-nonintegral-probe-findings.md §2):")
    ok = True
    for P, (hp, hm) in expect.items():
        got = (results[P][+1][0]["H"], results[P][-1][0]["H"])
        match = got == (hp, hm)
        ok &= match
        print(f"  {word_str(P)} n=1 -> H+={got[0]}, H-={got[1]} "
              f"(published single-letter n=2: {hp}, {hm}) "
              f"{'OK' if match else 'MISMATCH'}")
    return ok


# ----------------------------------------------------------------------------
# Item 3: M1-M3 analysis
# ----------------------------------------------------------------------------


def detect_period(seq):
    """Smallest p >= 1 with seq[i] == seq[i+p] for all valid i (exact
    comparison), or None if no period < len(seq) fits the observed range."""
    L = len(seq)
    for p in range(1, L):
        if all(seq[i] == seq[i + p] for i in range(L - p)):
            return p
    return None


def analyze(grid, results):
    """Item 3: M1-M3 checks, per word and sector, every row exact.

    M1: j_n in {1..q-1}; j_n = -a * 2^{-1} * g_P^{-n} mod q; purely periodic
        with period ord_q(g_P); v_n := H/Q_n - sigma*a/(q Q_n) purely
        periodic from n = 1.
    M2: v_n >= 1/q at every row; sharp constant j_min/q over the visited
        coset orbit (checked as: min v_n == j_min/q, + sector).
    M3: t_n := (a + 2 j_n) q^{-1} mod 3; k+ = [t_n = 0], k- = 1 + [t_n = 2];
        k <= 2; deepest-door factor Q_n/A_P^n == 2^(2 n S_P + 1) == 2 mod 3
        checked exactly, not assumed.
    """
    print("\n" + "=" * 74)
    print("Item 3: M1-M3 analysis (all rows exact)")
    print("=" * 74)
    summary = []
    m1_ok_all = m2_ok_all = m3_ok_all = True
    sharp_fail = []
    k_global = {+1: {}, -1: {}}
    for (P, p, a, q, S, M, g, ordg) in grid:
        nmax = n_max_for(ordg)
        A, _ = composed_constants(P)
        # M3 factor check (word-level, all n): Q_n/A_P^n == 2^(2nS+1) == 2 mod 3
        factor_ok = all(
            Fraction(results[P][+1][n - 1]["Q"]) / A**n == 2 ** (2 * n * S + 1)
            and pow(2, 2 * n * S + 1, 3) == 2
            for n in range(1, nmax + 1))
        # M1 j-law (sector-independent: j_n comes from class_data)
        jn_seq = [results[P][+1][n - 1]["j"] for n in range(1, nmax + 1)]
        jn_range_ok = all(1 <= j <= q - 1 for j in jn_seq)
        jn_alg = [(-a * modinv(2, q) * pow(modinv(g, q), n, q)) % q
                  for n in range(1, nmax + 1)]
        jn_law_ok = jn_seq == jn_alg
        pj = detect_period(jn_seq)
        for sigma in (+1, -1):
            rows = results[P][sigma]
            v_seq = [Fraction(row["H"], row["Q"])
                     - sigma * Fraction(a, q * row["Q"]) for row in rows]
            # exact identity v_n = j_n/q + k (+) or k - j_n/q (-)
            for n, row in enumerate(rows, 1):
                expect = (Fraction(row["j"], q) + row["k"] if sigma > 0
                          else row["k"] - Fraction(row["j"], q))
                assert v_seq[n - 1] == expect, (
                    f"limit-value identity failed {word_str(P)} "
                    f"sigma={sigma:+d} n={n}")
            pv = detect_period(v_seq)
            k_seq = [row["k"] for row in rows]
            # M3: deepest-door mod-3 identity and the k-rule, every row
            t_ok = kform_ok = True
            for row in rows:
                t_n = (a + 2 * row["j"]) * modinv(q, 3) % 3
                if row["deepest_mod3"] != (t_n + 2 * sigma * row["k"]) % 3:
                    t_ok = False
                k_pred = ((1 if t_n == 0 else 0) if sigma > 0
                          else (2 if t_n == 2 else 1))
                if row["k"] != k_pred:
                    kform_ok = False
            k_max = max(k_seq)
            # M2: v_n >= 1/q; sharp constant j_min/q over visited orbit (+)
            vmin = min(v_seq)
            m2_ok = vmin >= Fraction(1, q)
            j_min = min(jn_seq)
            sharp_ok = None
            if sigma > 0:
                sharp_ok = (vmin == Fraction(j_min, q))
                if not sharp_ok:
                    sharp_fail.append((P, vmin, Fraction(j_min, q)))
            m1_ok = (jn_range_ok and jn_law_ok and pj == ordg
                     and pv == ordg)
            m3_ok = t_ok and kform_ok and (k_max <= 2) and factor_ok
            m1_ok_all &= m1_ok
            m2_ok_all &= m2_ok
            m3_ok_all &= m3_ok
            kdist = {}
            for k in k_seq:
                kdist[k] = kdist.get(k, 0) + 1
                k_global[sigma][k] = k_global[sigma].get(k, 0) + 1
            vset = sorted(set(v_seq))
            summary.append({
                "word": P, "p": p, "sigma": sigma, "a": a, "q": q,
                "ordg": ordg, "nmax": nmax, "pj": pj, "pv": pv,
                "vset": vset, "vmin": vmin, "j_min": j_min,
                "kdist": dict(sorted(kdist.items())),
                "jn_law_ok": jn_law_ok, "jn_range_ok": jn_range_ok,
                "t_ok": t_ok, "kform_ok": kform_ok, "factor_ok": factor_ok,
                "m1_ok": m1_ok, "m2_ok": m2_ok, "m3_ok": m3_ok,
                "sharp_ok": sharp_ok,
            })
    # print summary
    print(f"\n{'word':>24} {'y*':>10} {'sec':>3} {'ord':>4} {'nmax':>4} "
          f"{'per(j)':>6} {'per(v)':>6} {'k-dist':>16} {'min v':>10} "
          f"{'1/q':>10} {'jmin/q':>10} {'M1':>3} {'M2':>3} {'M3':>3}")
    for s in summary:
        vals = ("{" + ", ".join(
            f"{v.numerator}/{v.denominator}" for v in s["vset"][:8])
            + (", ...}" if len(s["vset"]) > 8 else "}"))
        ystr = str(s["a"]) + "/" + str(s["q"])
        print(f"{word_str(s['word']):>24} {ystr:>10} "
              f"{'+' if s['sigma'] > 0 else '-':>3} {s['ordg']:>4} "
              f"{s['nmax']:>4} {s['pj']:>6} {s['pv']:>6} "
              f"{str(s['kdist']):>16} {float(s['vmin']):>10.6f} "
              f"{1 / s['q']:>10.6f} {s['j_min'] / s['q']:>10.6f} "
              f"{'ok' if s['m1_ok'] else 'FAIL':>3} "
              f"{'ok' if s['m2_ok'] else 'FAIL':>3} "
              f"{'ok' if s['m3_ok'] else 'FAIL':>3}")
        print(f"{'':>24}   value set of v_n: {vals}")
    print("\nVerdicts (whole-period windows, all rows exact):")
    print(f"  M1 (j-law, pure periodicity of j_n and v_n, period = "
          f"ord_q(g_P)): {'CONFIRMED' if m1_ok_all else 'REFUTED/SHORTFALL'}")
    print(f"  M2 (v_n >= 1/q at every row): "
          f"{'CONFIRMED' if m2_ok_all else 'REFUTED'}")
    n_sharp = sum(1 for s in summary if s["sharp_ok"] is True)
    n_sharp_tot = sum(1 for s in summary if s["sharp_ok"] is not None)
    print(f"  M2 sharp constant (min v_n == j_min/q, + sector): "
          f"{n_sharp}/{n_sharp_tot} words"
          + ("" if not sharp_fail else
             "  FAILURES: " + "; ".join(
                 f"{word_str(P)}: min v={vm} vs j_min/q={jq}"
                 for (P, vm, jq) in sharp_fail)))
    print(f"  M3 (t_n rule, k+ = [t=0], k- = 1+[t=2], k <= 2, factor "
          f"2^(2nS+1) = 2 mod 3): {'CONFIRMED' if m3_ok_all else 'REFUTED'}")
    print(f"  k distributions: + {dict(sorted(k_global[+1].items()))}, "
          f"- {dict(sorted(k_global[-1].items()))}")
    return summary, m1_ok_all, m2_ok_all, m3_ok_all


# ----------------------------------------------------------------------------
# Item 3 addendum: cross-word escape-spectrum coincidences (findings §5)
# ----------------------------------------------------------------------------


def subgroup(g, q):
    """The cyclic subgroup <g> of (Z/q)^x, as a set."""
    seen, y = set(), 1
    while y not in seen:
        seen.add(y)
        y = y * g % q
    return seen


def cross_word_spectra(grid, results):
    """Observed coincidence, checked exactly over the full tables: words
    sharing (q, g_P) with numerators in the same coset of <g_P> have equal
    v_n value sets per sector; numerators in opposite cosets (-a in the
    other's coset) swap the sectors. Raw data check, no interpretation."""
    info = {P: (a, q, g) for (P, p, a, q, S, M, g, o) in grid}

    def vset(P, sigma):
        a, q, _ = info[P]
        return {Fraction(row["H"], row["Q"])
                - sigma * Fraction(a, q * row["Q"])
                for row in results[P][sigma]}

    print("\nCross-word escape-spectrum checks (exact, full tables):")
    ok = True
    P1, P2 = ((1, 2), (2, 2)), ((1, 1), (1, 1), (1, 2))
    a1, q, g = info[P1]
    a2 = info[P2][0]
    H = subgroup(g, q)
    same_coset = (a2 * modinv(a1, q)) % q in H
    eq_p = vset(P1, +1) == vset(P2, +1)
    eq_m = vset(P1, -1) == vset(P2, -1)
    ok &= same_coset and eq_p and eq_m
    print(f"  {word_str(P1)} vs {word_str(P2)} (q={q}, same g): "
          f"a2/a1 in <g_P>: {same_coset}; v-sets equal: +:{eq_p} -:{eq_m}")
    P3, P4 = ((2, 1), (2, 2)), ((1, 1), (1, 1), (2, 1))
    a3, q2, g2 = info[P3]
    a4 = info[P4][0]
    H2 = subgroup(g2, q2)
    opp_coset = ((-a4 * modinv(a3, q2)) % q2 in H2
                 and (a4 * modinv(a3, q2)) % q2 not in H2)
    swap1 = vset(P3, +1) == vset(P4, -1)
    swap2 = vset(P3, -1) == vset(P4, +1)
    ok &= opp_coset and swap1 and swap2
    print(f"  {word_str(P3)} vs {word_str(P4)} (q={q2}, same g): "
          f"-a2/a1 in <g_P> (and a2/a1 not): {opp_coset}; sector-swapped "
          f"v-sets equal: {swap1} and {swap2}")
    return ok


# ----------------------------------------------------------------------------
# Item 4: M4 — rotation dependence
# ----------------------------------------------------------------------------

M4_WORDS = [((1, 1), (1, 2)),          # q = 23
            ((1, 1), (2, 1)),          # q = 5
            ((1, 1), (2, 2)),          # q = 37
            ((1, 1), (1, 1), (2, 2)),  # q = 175
            ((1, 1), (1, 2), (1, 2))]  # q = 229
M4_NMAX = 6


def m4_rotations():
    """Item 4: for words spanning 5 distinct q, all p rotations: each
    rotation's own fixed point (computed exactly from its own A, B — and
    separately checked against the G-affine image of the previous rotation's
    fixed point, compute-don't-assume), its own height rows n = 1..6 both
    sectors with the full direct-simulation battery, and per-rotation M1-M3
    row checks against its own (a_i, q_i)."""
    print("\n" + "=" * 74)
    print(f"Item 4: M4 rotation dependence ({len(M4_WORDS)} words, all "
          f"rotations, n = 1..{M4_NMAX}, both sectors)")
    print("=" * 74)
    m4_ok_all = True
    same_q_all = True
    reports = []
    for P in M4_WORDS:
        p = len(P)
        rots = rotations(P)
        ystars = [fixed_point(R) for R in rots]
        # G-affine orbit identity: y*_{i+1} = alpha_i y*_i + beta_i with
        # (alpha_i, beta_i) the affine constants of rotation i's first letter
        orbit_ok = True
        for i, R in enumerate(rots):
            alpha, beta = letter_affine(*R[0])
            if alpha * ystars[i] + beta != ystars[(i + 1) % p]:
                orbit_ok = False
        qs = [y.denominator for y in ystars]
        same_q = len(set(qs)) == 1
        same_q_all &= same_q
        S, M = word_sums(P)
        print(f"\nword {word_str(P)}^inf: rotations' fixed points "
              f"{[str(y) for y in ystars]}")
        print(f"  G-affine orbit identity (y*_(i+1) = alpha_i y*_i + "
              f"beta_i): {'OK' if orbit_ok else 'FAIL'}; denominators "
              f"{qs} {'(all equal)' if same_q else '(NOT equal)'}")
        rot_rows = []
        for i, R in enumerate(rots):
            a, q = ystars[i].numerator, ystars[i].denominator
            g = (2**S * 3**M) % q
            ordg = mult_order(g, q)
            rot_ok = True
            for sigma in (+1, -1):
                seq = []
                for n in range(1, M4_NMAX + 1):
                    row = height_scan(R, n, sigma)
                    dd = deepest_door_formula(R, n, row["y0"])
                    assert (dd.denominator == 1
                            and int(dd) == row["deepest"]), (
                        f"M4 deepest-door mismatch {word_str(R)} n={n}")
                    # per-rotation M1: j-law with this rotation's (a, q)
                    j_alg = (-a * modinv(2, q)
                             * pow(modinv(g, q), n, q)) % q
                    if row["j"] != j_alg:
                        rot_ok = False
                    # per-rotation M2 core: v_n >= 1/q
                    v = (Fraction(row["H"], row["Q"])
                         - sigma * Fraction(a, q * row["Q"]))
                    if v < Fraction(1, q):
                        rot_ok = False
                    # per-rotation M3: k-rule and k <= 2
                    t_n = (a + 2 * row["j"]) * modinv(q, 3) % 3
                    k_pred = ((1 if t_n == 0 else 0) if sigma > 0
                              else (2 if t_n == 2 else 1))
                    if row["k"] != k_pred or row["k"] > 2:
                        rot_ok = False
                    seq.append((n, row["H"], row["k"], row["j"], v))
                jseq = [s[3] for s in seq]
                kseq = [s[2] for s in seq]
                vseq = [s[4] for s in seq]
                print(f"  rot {i} {word_str(R):>24} y*={str(ystars[i]):>9} "
                      f"ord={ordg:>3} sec {'+' if sigma > 0 else '-'}: "
                      f"j={jseq} k={kseq}")
                print(f"        v_n = "
                      f"{['%s/%s' % (v.numerator, v.denominator) for v in vseq]}")
            m4_ok_all &= rot_ok and orbit_ok
            rot_rows.append((i, R, a, q, ordg, rot_ok))
        reports.append((P, ystars, qs, same_q, orbit_ok, rot_rows))
    print(f"\nM4 verdict inputs: every rotation obeys M1-M3 with its own "
          f"(a,q): {'YES' if m4_ok_all else 'NO'}; rotated fixed points "
          f"share one denominator q per word: "
          f"{'YES (all words)' if same_q_all else 'NO'}")
    return reports, m4_ok_all, same_q_all


# ----------------------------------------------------------------------------
# main (extended per queue item)
# ----------------------------------------------------------------------------


def main():
    t0 = time.time()
    print("multiletter_h_probe.py — run date 2026-07-17 (deterministic, "
          "no RNG)")
    grid = print_item1()

    print("\n" + "=" * 74)
    print("Item 2: exact height tables H^sigma_(np,np), whole-period windows "
          "(every H verified by direct simulation)")
    print("=" * 74)
    results, surprises = compute_tables(grid)
    brute_ok = run_brute_checks(grid, results)
    consist_ok = consistency_vs_single_letter(results)

    summary, m1_ok, m2_ok, m3_ok = analyze(grid, results)
    spectra_ok = cross_word_spectra(grid, results)
    print(f"  cross-word spectrum coincidences all hold: {spectra_ok}")

    reports, m4_ok, same_q = m4_rotations()

    print(f"\ntotal time: {time.time() - t0:.1f} s")
    print(f"non-deepest-door candidate failures (should be 0): {surprises}")
    print(f"brute-force cross-checks all matched: {brute_ok}")
    print(f"single-letter consistency: {consist_ok}")
    return 0 if (brute_ok and consist_ok and surprises == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
