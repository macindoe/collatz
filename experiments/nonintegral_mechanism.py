#!/usr/bin/env python3
"""Independent verification for reverse.md 14.15.8 — the non-integral single-letter
mechanism theorems (branch nonintegral-mechanism, per briefs/nonintegral-mechanism-brief.md).

Fresh code: imports nothing from h_nonintegral_probe.py, height_exact_laws.py,
realization_height.py, diagonal_converse.py, signed_diagonal.py, itinerary_coding.py,
block_map.py, or door_seam.py. Exact integer/Fraction arithmetic at every pass/fail
decision. Deterministic (no RNG).

What is checked (sections refer to reverse.md 14.15.8):
  1. Setup facts (Lemma 14.15.8.1): q > 1, gcd(q,6) = 1, a odd, 3 does not divide a,
     |a| < 3^m < Q_1; the 2-adic stratum identities y*+1 = 2^m(2^r-1)/d and
     3^m q* - 1 = 2^r y* as exact Fraction identities; y* == B_n/(1-A_n) and
     v3(y* - B_n) >= M_n for n = 1..6 (exact Fraction arithmetic).
  2. Class theorem (Theorem 14.15.8.2), exhaustively over full modulus widths, both
     signs, both directions of the iff: n = 1 for all seven words; n = 2 for the five
     words with Q_2 <= 5*10^5. Also: y0-liveness automatic on the class, -1 never in
     the class, and the R^sigma description (sign + deepest-door liveness only).
  3. The four mechanism identities (Theorem 14.15.8.3) and corollaries P1-P3
     (14.15.8.4-.6) against direct simulation on all seven words, both sectors,
     n = 1..25: every candidate on the class progression verified by direct simulation
     only (forward strata by iterating G; backward chain by the unique-predecessor
     formula with integrality checked at every step; liveness; sign; y != -1), and
     every rejected candidate verified to have failed on deepest-door liveness alone.
  4. Brute-force minimality at n = 1 and n = 2 on all 14 word/sector pairs: dumb scan
     of all odd integers of the sector in increasing |y|, no class reasoning, first
     member of R^sigma compared against the closed form.

Exit status 0 iff every check passes.
"""

from fractions import Fraction
from math import gcd
import sys

WORDS = [(1, 2), (1, 3), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
N_MAX = 25          # matches the probe's range
EXHAUSTIVE_N2_CAP = 500_000

CHECKS = 0
FAILURES = []


def check(cond, label):
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILURES.append(label)
        print("FAIL:", label)


def v2(x):
    """2-adic valuation of a nonzero integer."""
    x = abs(x)
    assert x != 0
    return (x & -x).bit_length() - 1


def v3_frac(fr):
    """3-adic valuation of a nonzero Fraction (exact)."""
    assert fr != 0
    num, den = fr.numerator, fr.denominator
    v = 0
    while num % 3 == 0:
        num //= 3
        v += 1
    while den % 3 == 0:
        den //= 3
        v -= 1
    return v


def stratum_and_G(y):
    """(m, r, G(y)) for odd y != -1, either sign (14.15.6.1's formulas)."""
    m = v2(y + 1)
    q = (y + 1) >> m if y > -1 else -((-(y + 1)) >> m)
    val = 3 ** m * q - 1
    r = v2(val)
    return m, r, val >> r if val > 0 else -((-val) >> r)


def follows_forward(y, m, r, n):
    """Does y follow ((m,r))^n forward? Direct simulation; -1 has no stratum."""
    cur = y
    for _ in range(n):
        if cur == -1:
            return False
        mm, rr, g = stratum_and_G(cur)
        if mm != m or rr != r:
            return False
        cur = g
    return True


def backward_chain(y, m, r, n):
    """Letter-prescribed backward chain to depth n (14.15.6.3's formula, integrality
    checked at every step). Returns [y_-1, ..., y_-n] or None."""
    chain = []
    z = y
    p3 = 3 ** m
    for _ in range(n):
        num = (z << r) + 1
        if num % p3 != 0:
            return None
        qq = num // p3
        pred = (qq << m) - 1
        chain.append(pred)
        z = pred
    return chain


def is_live(y):
    return y % 3 != 0


def in_R(y, m, r, n, sigma):
    """Membership in R^sigma_{n,n}(((m,r))^inf) by direct simulation only
    (Definition 14.15.6.8)."""
    if y == 0 or y == -1 or y % 2 == 0:
        return False
    if (y > 0) != (sigma > 0):
        return False
    if not is_live(y):
        return False
    if not follows_forward(y, m, r, n):
        return False
    ch = backward_chain(y, m, r, n)
    if ch is None:
        return False
    return is_live(ch[-1])


def mult_order(g, q):
    assert gcd(g, q) == 1
    o, x = 1, g % q
    while x != 1:
        x = x * g % q
        o += 1
    return o


def composed_constants(m, r, n):
    """(A_n, B_n) for the constant word, exact Fractions (the affine recursion of
    14.14.8.2; all orderings agree for a constant word)."""
    alpha = Fraction(3 ** m, 2 ** (m + r))
    beta = Fraction(3 ** m - 2 ** m, 2 ** (m + r))
    A, B = Fraction(1), Fraction(0)
    for _ in range(n):
        A, B = alpha * A, alpha * B + beta
    return A, B


def word_setup(m, r):
    ystar = Fraction(3 ** m - 2 ** m, 2 ** (m + r) - 3 ** m)
    return ystar.numerator, ystar.denominator, ystar


# ----------------------------------------------------------------------------
# 1. Setup facts (Lemma 14.15.8.1)
# ----------------------------------------------------------------------------

def test_setup_facts():
    print("== 1. setup facts (Lemma 14.15.8.1) ==")
    for (m, r) in WORDS:
        a, q, ystar = word_setup(m, r)
        tag = f"({m},{r})"
        check(q > 1, f"{tag} q>1 (non-integral)")
        check(gcd(q, 6) == 1, f"{tag} gcd(q,6)=1")
        check(a % 2 != 0, f"{tag} a odd")
        check(a % 3 != 0, f"{tag} 3 does not divide a")
        check(abs(a) < 3 ** m, f"{tag} |a| < 3^m")
        check(abs(a) < 2 ** (m + r + 1) * 3 ** m, f"{tag} |a| < Q_1")
        # 2-adic stratum identities, as exact Fraction identities
        d = 2 ** (m + r) - 3 ** m
        check(ystar + 1 == Fraction(2 ** m * (2 ** r - 1), d),
              f"{tag} y*+1 = 2^m(2^r-1)/d")
        qstar = (ystar + 1) / 2 ** m
        check(qstar.numerator % 2 != 0 and qstar.denominator % 2 != 0,
              f"{tag} q* a 2-adic unit")
        check(3 ** m * qstar - 1 == 2 ** r * ystar,
              f"{tag} 3^m q* - 1 = 2^r y*")
        check(ystar.numerator % 2 != 0 and ystar.denominator % 2 != 0,
              f"{tag} y* a 2-adic unit")
        # fixed point of the affine map, and the 3-adic congruence y* == B_n mod 3^{M_n}
        for n in range(1, 7):
            A, B = composed_constants(m, r, n)
            check(A * ystar + B == ystar, f"{tag} n={n} A_n y* + B_n = y*")
            check(ystar == B / (1 - A), f"{tag} n={n} y* = B_n/(1-A_n)")
            diff = ystar - B
            check(v3_frac(diff) >= m * n, f"{tag} n={n} v3(y*-B_n) >= M_n")
        print(f"  {tag}: y* = {a}/{q}  OK")


# ----------------------------------------------------------------------------
# 2. Class theorem (Theorem 14.15.8.2), exhaustive
# ----------------------------------------------------------------------------

def test_class_theorem():
    print("== 2. class theorem (Theorem 14.15.8.2), exhaustive full widths ==")
    total = 0
    for (m, r) in WORDS:
        a, q, _ = word_setup(m, r)
        for n in (1, 2):
            Q = 2 ** ((m + r) * n + 1) * 3 ** (m * n)
            if n == 2 and Q > EXHAUSTIVE_N2_CAP:
                continue
            rho = (a * pow(q, -1, Q)) % Q
            check(rho % 2 == 1, f"({m},{r}) n={n} rho odd")
            members = {+1: 0, -1: 0}
            for yy in range(1, Q + 1, 2):
                for y in (yy, -yy):
                    lhs = (y != -1 and follows_forward(y, m, r, n)
                           and backward_chain(y, m, r, n) is not None)
                    rhs = (y - rho) % Q == 0
                    if lhs != rhs:
                        check(False, f"({m},{r}) n={n} iff fails at y={y}")
                        continue
                    total += 1
                    if rhs:
                        sgn = +1 if y > 0 else -1
                        members[sgn] += 1
                        # y0-liveness automatic on the class; -1 never in the class
                        check(is_live(y), f"({m},{r}) n={n} member y={y} live")
                        check(y != -1, f"({m},{r}) n={n} -1 in class")
                        # R^sigma description: class + sign + deepest-door liveness
                        ch = backward_chain(y, m, r, n)
                        expected = is_live(ch[-1])
                        got = in_R(y, m, r, n, sgn)
                        check(got == expected,
                              f"({m},{r}) n={n} R-description at y={y}")
                        got_other = in_R(y, m, r, n, -sgn)
                        check(got_other is False,
                              f"({m},{r}) n={n} wrong-sector member y={y}")
            check(members[+1] == 1 and members[-1] == 1,
                  f"({m},{r}) n={n} one member per sign per width")
            print(f"  ({m},{r}) n={n}: full width Q_n={Q}, both signs, iff OK")
    print(f"  exhaustive iff decisions: {total}")


# ----------------------------------------------------------------------------
# 3. The four identities + P1-P3 against direct simulation, n = 1..25
# ----------------------------------------------------------------------------

def test_identities():
    print("== 3. mechanism identities (14.15.8.3) + P1-P3, n=1..%d ==" % N_MAX)
    summary = []
    for (m, r) in WORDS:
        a, q, ystar = word_setup(m, r)
        g = (2 ** (m + r) * 3 ** m) % q
        P = mult_order(g, q)
        tag = f"({m},{r})"
        j_seq = {}
        v_seq = {+1: {}, -1: {}}
        k_seq = {+1: {}, -1: {}}
        H12 = {}
        for n in range(1, N_MAX + 1):
            S1 = (m + r) * n + 1
            Q = 2 ** S1 * 3 ** (m * n)
            rho = (a * pow(q, -1, Q)) % Q
            # Identity 1: j_n well-defined, in {1,...,q-1}, closed form, periodic
            check((q * rho - a) % Q == 0, f"{tag} n={n} j_n well-defined")
            j = (q * rho - a) // Q
            check(1 <= j <= q - 1, f"{tag} n={n} j_n in 1..q-1")
            j_pred = (-a) * pow(2, -1, q) * pow(g, -n, q) % q
            check(j == j_pred, f"{tag} n={n} j_n closed form")
            j_seq[n] = j
            t = (a + 2 * j) * pow(q, -1, 3) % 3
            two_pow = 2 ** (2 * (m + r) * n + 1)
            check(two_pow % 3 == 2, f"{tag} n={n} 2^(2(m+r)n+1) = 2 mod 3")
            for sigma in (+1, -1):
                stag = "+" if sigma > 0 else "-"
                ks = range(0, 7) if sigma > 0 else range(1, 8)
                first_viable = None
                for k in ks:
                    y0 = rho + sigma * k * Q
                    # candidate facts, by direct simulation only
                    check(y0 % 2 == 1 and y0 != -1, f"{tag}{stag} n={n} k={k} odd, != -1")
                    check((y0 > 0) == (sigma > 0), f"{tag}{stag} n={n} k={k} sign")
                    check(follows_forward(y0, m, r, n),
                          f"{tag}{stag} n={n} k={k} follows forward")
                    ch = backward_chain(y0, m, r, n)
                    check(ch is not None, f"{tag}{stag} n={n} k={k} chain exists")
                    check(is_live(y0), f"{tag}{stag} n={n} k={k} y0 live")
                    deep = ch[-1]
                    # Identity 2: deepest-door formula and its mod-3 value
                    num = a + (j + sigma * k * q) * two_pow
                    check(num % q == 0 and deep == num // q,
                          f"{tag}{stag} n={n} k={k} deepest-door formula")
                    check(deep % 3 == (t + 2 * sigma * k) % 3,
                          f"{tag}{stag} n={n} k={k} deepest door mod 3")
                    # Identity 3: dead iff k in the predicted class mod 3
                    dead_pred = (k % 3 == t % 3) if sigma > 0 else (k % 3 == (-t) % 3)
                    check((not is_live(deep)) == dead_pred,
                          f"{tag}{stag} n={n} k={k} mod-3 death law")
                    if first_viable is None and is_live(deep):
                        first_viable = k
                # Identity 3, first-viable rule; Identity 4, closed form
                k_rule = (1 if t == 0 else 0) if sigma > 0 else (2 if t == 2 else 1)
                check(first_viable == k_rule, f"{tag}{stag} n={n} first-viable rule")
                H_sim = abs(rho + sigma * first_viable * Q)
                H_closed = (rho + k_rule * Q) if sigma > 0 else (k_rule * Q - rho)
                check(H_sim == H_closed, f"{tag}{stag} n={n} closed form H")
                check(in_R(H_sim if sigma > 0 else -H_sim, m, r, n, sigma),
                      f"{tag}{stag} n={n} H member of R")
                # P1 value: v_n
                v = Fraction(H_sim, Q) - sigma * Fraction(a, q * Q)
                v_pred = (Fraction(j, q) + k_rule) if sigma > 0 \
                    else (k_rule - Fraction(j, q))
                check(v == v_pred, f"{tag}{stag} n={n} v_n identity")
                v_seq[sigma][n] = v
                k_seq[sigma][n] = first_viable
                # P3: one extra progression step at most
                ok_k = first_viable in ((0, 1) if sigma > 0 else (1, 2))
                check(ok_k, f"{tag}{stag} n={n} P3 k bounded")
                # P2: lower bound
                check(v >= Fraction(1, q), f"{tag}{stag} n={n} P2 v_n >= 1/q")
                if n <= 2:
                    H12[(sigma, n)] = H_closed
        # Identity 1 / P1: pure periodicity from n=1 with period exactly P
        for n in range(1, N_MAX + 1 - P):
            check(j_seq[n + P] == j_seq[n], f"{tag} j period {P} at n={n}")
            for sigma in (+1, -1):
                check(v_seq[sigma][n + P] == v_seq[sigma][n],
                      f"{tag} v period {P} at n={n} sigma={sigma}")
        for p in range(1, P):
            check(any(j_seq[n + p] != j_seq[n] for n in range(1, N_MAX + 1 - p)),
                  f"{tag} j period exactly {P}: {p} is not a period")
            for sigma in (+1, -1):
                check(any(v_seq[sigma][n + p] != v_seq[sigma][n]
                          for n in range(1, N_MAX + 1 - p)),
                      f"{tag} v period exactly {P} sigma={sigma}: {p} not a period")
        # P2 sharp constant: min over rows == min over the orbit's closed form
        orbit = sorted({j_seq[n] for n in range(1, P + 1)})
        check(len(orbit) == P, f"{tag} orbit size = ord_q(g)")
        jmin = min(orbit)
        for sigma in (+1, -1):
            vals = set()
            for j in orbit:
                t = (a + 2 * j) * pow(q, -1, 3) % 3
                k_rule = (1 if t == 0 else 0) if sigma > 0 else (2 if t == 2 else 1)
                vals.add(Fraction(j, q) + k_rule if sigma > 0
                         else k_rule - Fraction(j, q))
            c = min(vals)
            c_obs = min(v_seq[sigma].values())
            check(c == c_obs, f"{tag} sigma={sigma} sharp constant from orbit")
            if sigma > 0:
                summary.append((tag, P, orbit, c, c == Fraction(jmin, q)))
        print(f"  {tag}: q={q} g={g} ord={P} orbit(j)={orbit} "
              f"k+ dist={sorted(set(k_seq[+1].values()))} "
              f"k- dist={sorted(set(k_seq[-1].values()))}  OK")
        # record H at n=1,2 for the brute-force cross-check
        test_identities.H12[(m, r)] = H12
    print("  sharp + sector constants:",
          ", ".join(f"{tag}: c={c} (=j_min/q: {eq})" for tag, P, orb, c, eq in summary))


test_identities.H12 = {}


# ----------------------------------------------------------------------------
# 4. Brute-force minimality at n = 1, 2 (dumb scan, no class reasoning)
# ----------------------------------------------------------------------------

def brute_force_H(m, r, n, sigma, cap):
    y = 1 if sigma > 0 else -1
    while abs(y) <= cap:
        if in_R(y, m, r, n, sigma):
            return abs(y)
        y += 2 * sigma
    return None


def test_brute_force():
    print("== 4. brute-force minimality, n=1,2, all 14 word/sector pairs ==")
    for (m, r) in WORDS:
        H12 = test_identities.H12[(m, r)]
        for n in (1, 2):
            for sigma in (+1, -1):
                stag = "+" if sigma > 0 else "-"
                expected = H12[(sigma, n)]
                got = brute_force_H(m, r, n, sigma, expected + 10)
                check(got == expected,
                      f"({m},{r}){stag} n={n} brute force: got {got}, closed form {expected}")
                print(f"  ({m},{r}){stag} n={n}: H = {got}  (dumb scan agrees)")


def main():
    test_setup_facts()
    test_class_theorem()
    test_identities()
    test_brute_force()
    print()
    print(f"TOTAL CHECKS: {CHECKS}")
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}")
        for f in FAILURES[:50]:
            print(" ", f)
        sys.exit(1)
    print("FAILURES: 0")
    print("ALL OK (2026-07-17, deterministic, exact arithmetic)")


if __name__ == "__main__":
    main()
