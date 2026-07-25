#!/usr/bin/env python3
"""Structural checks supporting `briefs/semigroup-priorart-findings.md`.

Exact `Fraction` arithmetic throughout; no floating point at any pass/fail
decision; deterministic (fixed seed).  Imports nothing from any other script in
`experiments/` (AGENTS.md house norm: fresh code).

What this supports.  The prior-art findings file makes three structural claims
about the affine composition semigroup `S` of the brief's section 1.  Each is a
claim about `S` itself, not about the literature, so each is checked here rather
than asserted:

  (1) THE EMBEDDING.  Each generator `g_{m,r}` of `S` equals the word
      `T_0^r . T_1^m` in the two raw affine branches of the Collatz map,
      `T_0(x) = x/2` and `T_1(x) = (3x+1)/2`, applied `T_1` first.  These are
      exactly the generators of the semigroup that Misiurewicz and Rodrigues,
      "Real 3x+1", Proc. Amer. Math. Soc. 133 (2005), 1109-1118, prove is free
      on two generators.  This is what places `S` inside a named, studied object
      rather than beside it.

  (2) THE COCYCLE CONVENTION.  With the order convention "leftmost letter
      applied first" -- the convention of reverse.md 14.14.8.2's recursion --
      the offset satisfies  beta(W.W') = alpha(W') * beta(W) + beta(W').  The
      brief flags this as easy to get backwards; it is checked, not assumed.

  (3) THE MULTIPLIER IMAGE.  alpha(S) consists exactly of the rationals
      3^M / 2^N with M >= 1 and N >= M+1.  In particular every element of
      alpha(S) is a {2,3}-unit, so alpha(S) omits the generator 3/5 of the
      Applegate-Lagarias 3x+1 semigroup.  This is the arithmetic behind the
      findings file's refutation of the brief's section 5 hypothesis.

Run:  python experiments/semigroup_priorart_check.py
"""

import random
from fractions import Fraction


# --------------------------------------------------------------------------
# The objects
# --------------------------------------------------------------------------

def gen(m, r):
    """Generator `g_{m,r}` of `S`, as the affine pair (alpha, beta).

    reverse.md 14.14.4.1:  alpha = 3^m / 2^(m+r),  beta = (3^m - 2^m) / 2^(m+r).
    """
    denom = Fraction(1, 2 ** (m + r))
    return (Fraction(3 ** m) * denom, Fraction(3 ** m - 2 ** m) * denom)


# The two raw affine branches of the Collatz map, as affine pairs.
T0 = (Fraction(1, 2), Fraction(0))          # x -> x/2
T1 = (Fraction(3, 2), Fraction(1, 2))       # x -> (3x+1)/2


def apply_map(f, y):
    a, b = f
    return a * y + b


def compose_word(letters):
    """Compose a list of affine pairs, LEFTMOST APPLIED FIRST.

    Returns (A, B) with  (letters[-1] o ... o letters[0])(y) = A*y + B.
    This is exactly reverse.md 14.14.8.2's recursion
        A_0 = 1, B_0 = 0;  A_{i+1} = alpha_i A_i,  B_{i+1} = alpha_i B_i + beta_i.
    """
    A, B = Fraction(1), Fraction(0)
    for a, b in letters:
        A, B = a * A, a * B + b
    return (A, B)


# --------------------------------------------------------------------------
# (1) The embedding into the Misiurewicz-Rodrigues generators
# --------------------------------------------------------------------------

def check_embedding(max_m=12, max_r=12):
    """g_{m,r} == T_1 applied m times, then T_0 applied r times."""
    checks = 0
    for m in range(1, max_m + 1):
        for r in range(1, max_r + 1):
            word = [T1] * m + [T0] * r          # leftmost applied first
            assert compose_word(word) == gen(m, r), (m, r)
            # and the multiplier is the advertised 3-adic/2-adic shape
            alpha, _ = gen(m, r)
            assert alpha == Fraction(3 ** m, 2 ** (m + r)), (m, r)
            checks += 2
    return checks


def check_embedding_pointwise(trials=4000, seed=90210):
    """The embedding holds pointwise, evaluated on random rationals."""
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        m = rng.randint(1, 8)
        r = rng.randint(1, 8)
        y = Fraction(rng.randint(-10 ** 6, 10 ** 6), rng.randint(1, 10 ** 4))
        direct = apply_map(gen(m, r), y)
        stepwise = y
        for _ in range(m):
            stepwise = apply_map(T1, stepwise)
        for _ in range(r):
            stepwise = apply_map(T0, stepwise)
        assert direct == stepwise, (m, r, y)
        checks += 1
    return checks


def check_embedding_on_real_doors(limit=20000):
    """On honest odd integers, the word T_1^m T_0^r really is the exit map.

    For odd y > 0 with m = v_2(y+1), q = (y+1)/2^m, r = v_2(3^m q - 1), the
    stratum law says G(y) = g_{m,r}(y).  Check that the raw-branch word
    reproduces it and lands on an integer -- i.e. the letters of `S` are honest
    Collatz blocks, not merely formal affine maps.
    """
    checks = 0
    y = 1
    while y < limit:
        m = 0
        t = y + 1
        while t % 2 == 0:
            t //= 2
            m += 1
        q = t
        u = 3 ** m * q - 1
        r = 0
        while u % 2 == 0:
            u //= 2
            r += 1
        assert m >= 1 and r >= 1, y
        image = apply_map(gen(m, r), Fraction(y))
        assert image.denominator == 1, y
        assert image == Fraction(u), y
        word = [T1] * m + [T0] * r
        assert apply_map(compose_word(word), Fraction(y)) == image, y
        checks += 1
        y += 2
    return checks


# --------------------------------------------------------------------------
# (2) The cocycle convention
# --------------------------------------------------------------------------

def check_cocycle(trials=3000, seed=90211):
    """beta(W.W') = alpha(W') beta(W) + beta(W'), leftmost applied first.

    Also checks the OPPOSITE convention fails, so the orientation is pinned
    rather than accidentally symmetric.
    """
    rng = random.Random(seed)
    checks = 0
    mismatches_under_reversed_convention = 0
    for _ in range(trials):
        nW = rng.randint(1, 5)
        nV = rng.randint(1, 5)
        W = [gen(rng.randint(1, 6), rng.randint(1, 6)) for _ in range(nW)]
        V = [gen(rng.randint(1, 6), rng.randint(1, 6)) for _ in range(nV)]
        aW, bW = compose_word(W)
        aV, bV = compose_word(V)
        aWV, bWV = compose_word(W + V)
        assert aWV == aW * aV
        assert bWV == aV * bW + bV
        if bWV != aW * bV + bW:
            mismatches_under_reversed_convention += 1
        checks += 1
    return checks, mismatches_under_reversed_convention


# --------------------------------------------------------------------------
# (3) The multiplier image alpha(S)
# --------------------------------------------------------------------------

def check_multiplier_image(max_len=5, trials=3000, seed=90212):
    """Every alpha(W) is 3^M/2^N with M >= 1 and N >= M + len(W).

    Consequently alpha(S) is contained in the group generated by 2 and 3, so it
    omits every rational with a prime factor outside {2,3} -- in particular the
    Applegate-Lagarias generator 3/5.
    """
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        n = rng.randint(1, max_len)
        letters = [(rng.randint(1, 7), rng.randint(1, 7)) for _ in range(n)]
        A, _ = compose_word([gen(m, r) for m, r in letters])
        M = sum(m for m, _ in letters)
        N = sum(m + r for m, r in letters)
        assert A == Fraction(3 ** M, 2 ** N), letters
        assert M >= n and N >= M + n
        # {2,3}-unit: numerator a power of 3, denominator a power of 2
        num, den = A.numerator, A.denominator
        while num % 3 == 0:
            num //= 3
        while den % 2 == 0:
            den //= 2
        assert num == 1 and den == 1, A
        checks += 1
    # 3/5 is an Applegate-Lagarias generator ((2k+1)/(3k+2) at k=1) and is not
    # a {2,3}-unit, hence lies outside alpha(S).
    al_gen = Fraction(3, 5)
    assert al_gen.denominator % 5 == 0
    checks += 1
    return checks


# --------------------------------------------------------------------------
# (4) Why the off-the-shelf IFS separation route does not open
# --------------------------------------------------------------------------
#
# S is a genuine countable IFS of similarities on Z_3: each g_{m,r} contracts
# 3-adically by exactly 3^{-m}.  So Mauldin-Urbanski-style infinite-alphabet IFS
# machinery is the right SHAPE for it.  It is nevertheless blocked at level one,
# for the two reasons checked here.  Neither is evidence against freeness -- two
# distinct affine maps may perfectly well share an image ball -- they only show
# that the standard separation and ping-pong routes do not open by inspection.

def check_image_balls_collide(max_m=6, max_r=40):
    """g_{m,r}(Z_3) = beta_{m,r} + 3^m Z_3, and for fixed m two letters share
    that ball exactly when 2*3^(m-1) divides r' - r.

    Consequence: the strong separation condition / OSC fails at the first level,
    so infinite-IFS theory does not hand over a separation hypothesis for free.
    """
    checks = 0
    for m in range(1, max_m + 1):
        mod = 3 ** m
        order = 2 * 3 ** (m - 1)            # multiplicative order of 2 mod 3^m
        assert pow(2, order, mod) == 1 and all(
            pow(2, d, mod) != 1 for d in range(1, order)), m
        # beta mod 3^m  ==  -2^{-r} mod 3^m, since 3^m == 0 there
        def beta_mod(r):
            inv = pow(pow(2, m + r, mod), -1, mod)
            return ((3 ** m - 2 ** m) * inv) % mod
        for r in range(1, max_r + 1):
            for rp in range(1, max_r + 1):
                same_ball = (beta_mod(r) == beta_mod(rp))
                predicted = ((rp - r) % order == 0)
                assert same_ball == predicted, (m, r, rp)
                checks += 1
        # and the collision is real, not vacuous: r and r + 2*3^(m-1) collide
        assert beta_mod(1) == beta_mod(1 + order), m
        checks += 1
    return checks


def check_fixed_points_are_units(max_m=15, max_r=15):
    """Every letter's fixed point p_{m,r} = (3^m - 2^m)/(2^(m+r) - 3^m) is a
    3-adic UNIT.

    They therefore all live in the compact set Z_3^x and accumulate, so
    inf over j of |p_i - p_j|_3 is 0 and single-ball ultrametric ping-pong
    cannot close on the infinite family.  (It closes fine on any finite
    sub-family; this is a statement about the whole alphabet at once.)
    """
    checks = 0
    for m in range(1, max_m + 1):
        for r in range(1, max_r + 1):
            alpha, beta = gen(m, r)
            p = beta / (1 - alpha)
            assert p == Fraction(3 ** m - 2 ** m, 2 ** (m + r) - 3 ** m), (m, r)
            # 3-adic unit: 3 divides neither numerator nor denominator
            assert p.numerator % 3 != 0 and p.denominator % 3 != 0, (m, r)
            checks += 1
    return checks


# --------------------------------------------------------------------------
# Cross-check against the wiki's own composed constants
# --------------------------------------------------------------------------

def check_fixed_point(trials=2000, seed=90213):
    """y* = B/(1-A) is the fixed point, and 1-A = q/2^S with q = 2^S - 3^M.

    itinerary.md 14.15.9's setup, re-derived here from the generators alone.
    """
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        n = rng.randint(1, 5)
        letters = [(rng.randint(1, 6), rng.randint(1, 6)) for _ in range(n)]
        A, B = compose_word([gen(m, r) for m, r in letters])
        M = sum(m for m, _ in letters)
        S = sum(m + r for m, r in letters)
        assert A != 1
        ystar = B / (1 - A)
        assert apply_map((A, B), ystar) == ystar, letters
        q_unreduced = 2 ** S - 3 ** M
        assert 1 - A == Fraction(q_unreduced, 2 ** S), letters
        # reduced denominator divides the unreduced one (14.15.9.1(2))
        assert q_unreduced % ystar.denominator == 0, letters
        checks += 1
    return checks


# --------------------------------------------------------------------------

def main():
    total = 0

    n = check_embedding()
    print(f"(1) embedding g_(m,r) = T_1^m T_0^r, algebraic grid m,r <= 12: {n} checks")
    total += n

    n = check_embedding_pointwise()
    print(f"(1) embedding, pointwise on random rationals:                  {n} checks")
    total += n

    n = check_embedding_on_real_doors()
    print(f"(1) embedding on odd integers y < 20000 (integrality too):     {n} checks")
    total += n

    n, rev = check_cocycle()
    print(f"(2) cocycle beta(WV) = alpha(V)beta(W) + beta(V):              {n} checks")
    print(f"    reversed convention fails on {rev}/{n} cases (orientation is pinned)")
    total += n

    n = check_multiplier_image()
    print(f"(3) alpha(W) = 3^M/2^N, a {{2,3}}-unit; 3/5 excluded:            {n} checks")
    total += n

    n = check_image_balls_collide()
    print(f"(4) image balls collide iff 2*3^(m-1) | r'-r (OSC fails):      {n} checks")
    total += n

    n = check_fixed_points_are_units()
    print(f"(4) every letter's fixed point is a 3-adic unit:               {n} checks")
    total += n

    n = check_fixed_point()
    print(f"(x) fixed point y* = B/(1-A), 1-A = q/2^S:                     {n} checks")
    total += n

    print(f"\nTotal: {total} checks, 0 failures (exact Fraction arithmetic).")


if __name__ == "__main__":
    main()
