#!/usr/bin/env python3
"""Independent verification for reverse.md 14.15.9 (the periodic shelf closed by
theorem: whole-period height laws for every periodic word).

Fresh code, per briefs/periodic-shelf-brief.md: imports nothing from
multiletter_h_probe.py, h_nonintegral_probe.py, nonintegral_mechanism.py,
height_exact_laws.py, realization_height.py, diagonal_converse.py,
signed_diagonal.py, itinerary_coding.py, block_map.py, or door_seam.py.
Exact int/Fraction arithmetic at every pass/fail decision. Deterministic (no RNG).

Checks (each function states the claim it verifies):
  1. check_fixed_point_arithmetic  - Lemma 14.15.9.1 (N/D form, parity, 3-coprimality,
     the unconditional bound 4N < 2^S 3^M, sign law), algebraic scan over all periods
     p <= 3 with letters m,r <= 3 (819 words), plus rotation lemma 14.15.9.2 and the
     2-adic stratum facts of Corollary 14.15.9.4 on the same scan.
  2. check_adelic_anchor           - Theorem 14.15.9.3 on the mandated grid (13
     multi-letter probe words + 7 single-letter probe words + 3 integer-fixed-point
     words, all rotations): 3-adic offset bound, 2-adic follower membership of the
     fixed point's lift by direct simulation, integer orbits realize their words.
  3. check_class_theorem           - Theorem 14.15.9.5, exhaustively over full modulus
     widths at n = 1, both signs, on five words spanning periods 1-3 (integer and
     non-integral, positive and negative fixed points).
"""

from fractions import Fraction
from itertools import product
from math import gcd
import sys
import time

# --------------------------------------------------------------------------
# primitives (fresh implementations)
# --------------------------------------------------------------------------

def v2_int(x):
    x = abs(x)
    assert x != 0
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def v3_int(x):
    x = abs(x)
    assert x != 0
    c = 0
    while x % 3 == 0:
        x //= 3
        c += 1
    return c


def v2_frac(fr):
    assert fr != 0
    return v2_int(fr.numerator) - v2_int(fr.denominator)


def v3_frac(fr):
    assert fr != 0
    return v3_int(fr.numerator) - v3_int(fr.denominator)


def stratum(y):
    """(m, r) for odd y != -1, either sign (14.15.1.1 / 14.15.6.1)."""
    assert y % 2 == 1 and y != -1
    m = v2_int(y + 1)
    q2 = (y + 1) // 2 ** m
    return m, v2_int(3 ** m * q2 - 1)


def G(y):
    m, r = stratum(y)
    q2 = (y + 1) // 2 ** m
    return (3 ** m * q2 - 1) // 2 ** r


def unique_pred(z, m, r):
    """14.15.4.1/14.15.6.3 letter-prescribed predecessor, or None."""
    Nz = 2 ** r * z + 1
    if Nz % 3 ** m != 0:
        return None
    return 2 ** m * (Nz // 3 ** m) - 1


def compose(word):
    """(A, B) of the composed affine map, letters applied in index order
    (14.14.8.2's recursion; simultaneously the deepest-first reading of a
    whole-period past, 14.15.5.1's order note)."""
    A, B = Fraction(1), Fraction(0)
    for (m, r) in word:
        al = Fraction(3 ** m, 2 ** (m + r))
        be = Fraction(3 ** m - 2 ** m, 2 ** (m + r))
        A, B = al * A, al * B + be
    return A, B


def word_sums(word):
    S = sum(m + r for m, r in word)
    M = sum(m for m, r in word)
    return S, M


def N_D(word):
    """Lemma 14.15.9.1's explicit numerator/denominator: y* = N/D."""
    S, M = word_sums(word)
    N = 0
    for i, (m, r) in enumerate(word):
        Mgt = sum(mm for mm, _ in word[i + 1:])
        Slt = sum(mm + rr for mm, rr in word[:i])
        N += (3 ** m - 2 ** m) * 3 ** Mgt * 2 ** Slt
    return N, 2 ** S - 3 ** M


def fixed_point(word):
    A, B = compose(word)
    return B / (1 - A)


def rotations(word):
    p = len(word)
    return [tuple(word[i:]) + tuple(word[:i]) for i in range(p)]


def follows_prefix(y, word, nletters):
    """Direct simulation: does odd integer y follow the first nletters of word^inf?"""
    p = len(word)
    z = y
    for i in range(nletters):
        if z == -1 or z % 2 == 0:
            return False
        if stratum(z) != word[i % p]:
            return False
        z = G(z)
    return True


def backward_chain(y, word, depth):
    """Letter-prescribed chain behind y to the given depth (letters at positions
    -1, -2, ..., -depth of word^inf). Returns the full chain [y_{-1},...,y_{-depth}]
    or None if some step fails integrality."""
    p = len(word)
    z = y
    chain = []
    for j in range(1, depth + 1):
        m, r = word[(-j) % p]
        z = unique_pred(z, m, r)
        if z is None:
            return None
        chain.append(z)
    return chain


def in_R(y, word, n):
    """Direct-simulation membership in R^sigma_{np,np}(word^inf) (14.15.6.8),
    sign read off y itself: forward np letters, y live, backward chain to depth
    np with live deepest door."""
    p = len(word)
    if y % 3 == 0 or y == -1 or y == 0:
        return False
    if not follows_prefix(y, word, n * p):
        return False
    ch = backward_chain(y, word, n * p)
    if ch is None:
        return False
    return ch[-1] % 3 != 0


# --------------------------------------------------------------------------
# the instance grids (the two probes' words; no new empirical grid)
# --------------------------------------------------------------------------

SINGLE_WORDS = [((1, 2),), ((1, 3),), ((2, 2),), ((2, 3),),
                ((3, 1),), ((3, 2),), ((3, 3),)]

MULTI_WORDS = [
    ((1, 1), (1, 2)), ((1, 1), (2, 1)), ((1, 1), (2, 2)), ((1, 2), (1, 2)),
    ((1, 2), (2, 1)), ((1, 2), (2, 2)), ((2, 1), (2, 2)), ((2, 2), (2, 2)),
    ((1, 1), (1, 1), (1, 2)), ((1, 1), (1, 1), (2, 1)), ((1, 1), (1, 1), (2, 2)),
    ((1, 1), (1, 2), (1, 2)), ((1, 1), (1, 2), (2, 2)),
]

INTEGER_WORDS = [((1, 1),), ((2, 1),), ((4, 1), (3, 3))]  # y* = 1, -5, -17

ALL_GRID = SINGLE_WORDS + MULTI_WORDS + INTEGER_WORDS

CHECKS = {"count": 0}


def ok(cond, msg):
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)
    CHECKS["count"] += 1


# --------------------------------------------------------------------------
# CHECK 1 - Lemma 14.15.9.1, Lemma 14.15.9.2, Corollary 14.15.9.4 stratum facts
# (algebraic scan: all periods p <= 3, letters m,r <= 3 -> 819 words; plus the
#  mandated grid's words below in check 2, which include letters up to (4,1))
# --------------------------------------------------------------------------

def lemma_battery(word):
    """All algebraic clauses of 14.15.9.1/.2/.4 on one period and its rotations."""
    p = len(word)
    S, M = word_sums(word)
    Q1 = 2 ** (S + 1) * 3 ** M
    rots = rotations(word)
    ys = [fixed_point(w) for w in rots]
    q0 = ys[0].denominator
    for i, w in enumerate(rots):
        ystar = ys[i]
        N, D = N_D(w)
        # 14.15.9.1(1): N/D identity, positivity, parity, 3-coprimality, bound, sign
        ok(Fraction(N, D) == ystar, f"N/D identity {w}")
        ok(N > 0 and N % 2 == 1 and N % 3 != 0, f"N parity/sign {w}")
        ok(4 * N < 2 ** S * 3 ** M, f"bound 4N < 2^S 3^M {w}")
        ok((ystar > 0) == (D > 0), f"sign law {w}")
        # 14.15.9.1(2): reduced-form facts
        a, q = ystar.numerator, ystar.denominator
        ok((2 ** S - 3 ** M) % q == 0, f"q | 2^S-3^M {w}")
        ok(gcd(q, 6) == 1, f"gcd(q,6)=1 {w}")
        ok(a % 2 == 1 and a % 3 != 0, f"a odd, 3 coprime {w}")
        ok(2 * abs(a) < Q1, f"2|a| < Q1 {w}")
        # 14.15.9.2(i): affine rotation orbit
        m, r = w[0]
        al = Fraction(3 ** m, 2 ** (m + r))
        be = Fraction(3 ** m - 2 ** m, 2 ** (m + r))
        ok(ys[(i + 1) % p] == al * ystar + be, f"rotation orbit {w}")
        # 14.15.9.2(ii): shared denominator
        ok(q == q0, f"shared q {w}")
        # 14.15.9.2(iii): epsilon law (eps_{i+1} = -(-1)^{r_i} mod 3)
        nxt = ys[(i + 1) % p]
        eps_next = (nxt.numerator * pow(nxt.denominator, -1, 3)) % 3
        ok(eps_next == (-((-1) ** r)) % 3, f"epsilon law {w}")
        # Corollary 14.15.9.4(1): per-position 2-adic stratum facts
        ok(v2_frac(ystar + 1) == m, f"v2(y*+1)=m {w}")
        qstar = (ystar + 1) / 2 ** m
        ok(v2_frac(3 ** m * qstar - 1) == r, f"v2(3^m q*-1)=r {w}")
        # G fixes the orbit as rational arithmetic: 3^m q* - 1 = 2^r y*_{i+1}
        ok(3 ** m * qstar - 1 == 2 ** r * ys[(i + 1) % p], f"G(y*_i)=y*_{{i+1}} {w}")


def check_fixed_point_arithmetic():
    letters = [(m, r) for m in (1, 2, 3) for r in (1, 2, 3)]
    nwords = 0
    for p in (1, 2, 3):
        for word in product(letters, repeat=p):
            lemma_battery(word)
            nwords += 1
    print(f"check 1 (Lemma .1/.2, Cor .4 algebra): {nwords} words (all p<=3, letters<=3), "
          f"all rotations, all clauses exact - OK")


# --------------------------------------------------------------------------
# CHECK 2 - Theorem 14.15.9.3 (adelic anchor) on the mandated grid
# --------------------------------------------------------------------------

def check_adelic_anchor():
    n_words = 0
    n_rot = 0
    for word in ALL_GRID:
        lemma_battery(word)  # letters up to (4,1),(3,3) included via the grid
        for w in rotations(word):
            n_rot += 1
            p = len(w)
            S, M = word_sums(w)
            ystar = fixed_point(w)
            a, q = ystar.numerator, ystar.denominator
            # 3-adic half: A^n y* + B_n = y* and v3(y* - B_{P^k}) >= k*M
            for k in range(1, 5):
                Ak, Bk = compose(w * k)
                ok(Ak * ystar + Bk == ystar, f"fixed-point identity {w} k={k}")
                ok(v3_frac(ystar - Bk) >= k * M, f"3-adic offset bound {w} k={k}")
            # 2-adic half: the lift of y* mod 2^{nS+1} follows the length-np
            # prefix, by direct simulation, for n = 1..3, both a positive and a
            # negative representative (signed domain).
            for n in range(1, 4):
                mod2 = 2 ** (n * S + 1)
                rep = (a * pow(q, -1, mod2)) % mod2
                for cand in (rep, rep - 2 * mod2):
                    if cand == -1 or cand == 0:
                        cand -= 2 * mod2
                    ok(follows_prefix(cand, w, n * p),
                       f"2-adic lift follows prefix {w} n={n} cand={cand}")
            # integer case: the orbit realizes the word
            if q == 1:
                z = a
                for i in range(2 * p):
                    ok(stratum(z) == w[i % p], f"integer orbit stratum {w} i={i}")
                    z = G(z)
                ok(z == a, f"integer orbit closes {w}")
        n_words += 1
    print(f"check 2 (Theorem .3 adelic anchor): {n_words} grid words, {n_rot} rotations, "
          f"3-adic offsets k=1..4, 2-adic lifts followed by simulation n=1..3 both signs - OK")


# --------------------------------------------------------------------------
# CHECK 3 - Theorem 14.15.9.5 (class theorem), exhaustive at n = 1
# --------------------------------------------------------------------------

CLASS_WORDS = [((2, 2),),                 # p=1, y* = 5/7 > 0
               ((2, 1),),                 # p=1, y* = -5, integer
               ((1, 1), (1, 2)),          # p=2, y* = 7/23 > 0
               ((2, 1), (2, 2)),          # p=2, y* = 85/47 > 0
               ((1, 1), (1, 2), (1, 2))]  # p=3, y* = 53/229 > 0


def check_class_theorem():
    n = 1
    total = 0
    for word in CLASS_WORDS:
        p = len(word)
        S, M = word_sums(word)
        Qn = 2 ** (n * S + 1) * 3 ** (n * M)
        ystar = fixed_point(word)
        a, q = ystar.numerator, ystar.denominator
        rho = (a * pow(q, -1, Qn)) % Qn
        ok(rho % 2 == 1 and rho % 3 != 0 and 0 < rho < Qn, f"rho facts {word}")
        members = dead_doors = 0
        for y in range(-Qn + 1, Qn + 1, 2):
            if y == -1 or y == 0:
                # -1 must also fail the class congruence (structural exclusion)
                if y == -1:
                    ok((-1 - rho) % Qn != 0, f"-1 in class {word}")
                continue
            fwd = follows_prefix(y, word, n * p)
            ch = backward_chain(y, word, n * p)
            both = fwd and ch is not None
            inclass = (y - rho) % Qn == 0
            ok(both == inclass, f"class iff {word} y={y}")
            if inclass:
                members += 1
                ok(y % 3 != 0, f"member liveness {word} y={y}")
                # R^sigma description: class + sign + deepest-door liveness
                deep_live = ch[-1] % 3 != 0
                ok(in_R(y, word, n) == deep_live, f"R description {word} y={y}")
                if not deep_live:
                    dead_doors += 1
            total += 1
        ok(members == 2, f"member count {word}")  # one per full width per sign
    print(f"check 3 (Theorem .5 class theorem): 5 words (periods 1-3, integer and "
          f"non-integral, both signs scanned), {total} exhaustive iff decisions at n=1, "
          f"full modulus width each sign - OK")


# --------------------------------------------------------------------------

def main():
    t0 = time.time()
    check_fixed_point_arithmetic()
    check_adelic_anchor()
    check_class_theorem()
    print(f"ALL CHECKS PASSED: {CHECKS['count']} exact checks, {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
