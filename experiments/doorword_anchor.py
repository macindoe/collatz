"""Independent verification for itinerary.md 14.15.10: the door-word <-> near-miss-anchor
dictionary.

Supports: Lemma 14.15.10.1 (per-letter affine form; composed slope / N_W/q(W) fixed
point with the order-convention reconciliation N_W = 2^S * B_P; rotation invariance
and the chained rotated fixed points; the anchor identification via the block-map
identity G = T^m; the per-cycle table with full cycle-membership checks) and
Corollary 14.15.10.2's |q| = 1 sentence (bounded instances), plus the bounded
census-consistency check: every integer fixed point in the stated scan is a
rotation/repetition member of the census cycles.md 12.6.1.2 records (its exhaustive
k <= 10 replication is the census authority) -- this is dictionary verification
against that recorded census, NOT a cycle search; the scan is filtered to
M(W) <= 10, at/below the census precedent.

Fresh implementation per AGENTS.md: imports nothing from
experiments/itinerary_coding.py, experiments/merle_round5_check.py, or
experiments/realization_height.py (or anything else in the repository).
Exact integer/Fraction arithmetic at every pass/fail decision. Deterministic
seeds stated per check.
"""

from fractions import Fraction
import random

FAILURES = []


def fail(msg):
    FAILURES.append(msg)
    print("FAIL:", msg)


# ---------------------------------------------------------------- primitives

def v2(n):
    """2-adic valuation of a nonzero integer."""
    assert n != 0
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def stratum_and_G(y):
    """(m, r, G(y)) by the defining formula (14.15.6.1 / 14.14.3.1), any odd y != -1, 0."""
    assert y % 2 != 0 and y != -1
    m = v2(y + 1)
    q = (y + 1) // 2 ** m
    val = 3 ** m * q - 1
    r = v2(val)
    return m, r, val // 2 ** r


def T_step(x):
    """Accelerated odd Collatz map on any odd integer x; returns (T(x), halvings)."""
    assert x % 2 != 0
    n = 3 * x + 1
    v = v2(n)
    return n // 2 ** v, v


def letter_affine(m, r):
    """Letter (m,r)'s affine map: alpha, beta with G(y) = alpha*y + beta on the stratum."""
    d = 2 ** (m + r)
    return Fraction(3 ** m, d), Fraction(3 ** m - 2 ** m, d)


def compose(word):
    """Composed affine constants (A, B) of a word, letters applied IN INDEX ORDER
    (letter 0 applied first, to the door itself) -- 14.14.8.2's recursion
    A_{i+1} = alpha_i A_i, B_{i+1} = alpha_i B_i + beta_i."""
    A, B = Fraction(1), Fraction(0)
    for (m, r) in word:
        a, b = letter_affine(m, r)
        A, B = a * A, a * B + b
    return A, B


def M_of(word):
    return sum(m for m, _ in word)


def S_of(word):
    return sum(m + r for m, r in word)


def q_of(word):
    return 2 ** S_of(word) - 3 ** M_of(word)


def N_formula(word):
    """N_W = sum_i (3^m_i - 2^m_i) * 3^{sum_{j>i} m_j} * 2^{sum_{j<i}(m_j+r_j)}
    (Lemma 14.15.9.1's numerator, recomputed independently)."""
    p = len(word)
    total = 0
    for i in range(p):
        mi, ri = word[i]
        e3 = sum(word[j][0] for j in range(i + 1, p))
        e2 = sum(word[j][0] + word[j][1] for j in range(i))
        total += (3 ** mi - 2 ** mi) * 3 ** e3 * 2 ** e2
    return total


def fixed_point(word):
    A, B = compose(word)
    return B / (1 - A)


def follows_and_returns(y0, word):
    """Does the integer door y0 follow word letter for letter under G and return?"""
    y = y0
    for (m, r) in word:
        if y == -1 or y % 2 == 0:
            return False
        mm, rr, gy = stratum_and_G(y)
        if (mm, rr) != (m, r):
            return False
        y = gy
    return y == y0


def rotations(word):
    return [tuple(word[i:]) + tuple(word[:i]) for i in range(len(word))]


# ------------------------------------------------------- check 1: per-letter

def check_per_letter(n=5000, seed=77001, ybits=40):
    """Per-letter affine form with exact divisibility, both signs, plus the
    block-map identity G = T^m with halving count m + r (14.14.7.1's mechanism,
    re-simulated), on random odd y (live or not; the formulas need neither
    liveness nor a sign)."""
    rng = random.Random(seed)
    n_live = 0
    for _ in range(n):
        y = rng.randrange(1, 2 ** ybits) | 1
        if rng.random() < 0.5:
            y = -y
        if y == -1:
            y = -3
        m, r, gy = stratum_and_G(y)
        if y % 3 != 0:
            n_live += 1
        # exact divisibility and the affine form
        num = 3 ** m * y + (3 ** m - 2 ** m)
        if num % 2 ** (m + r) != 0:
            fail(f"per-letter divisibility: y={y}")
        elif num // 2 ** (m + r) != gy:
            fail(f"per-letter value: y={y}")
        # block-map identity: T^m(y) = G(y), total halvings = m + r
        x, halvings = y, 0
        for _ in range(m):
            x, v = T_step(x)
            halvings += v
        if x != gy or halvings != m + r:
            fail(f"block-map: y={y} T^{m}={x} vs G={gy}, halvings={halvings} vs {m + r}")
    print(f"check 1 (per-letter affine + block-map): {n} random odd y "
          f"(|y| < 2^{ybits}, both signs, {n_live} live), seed {seed}: "
          f"{'OK' if not FAILURES else 'FAILURES'}")


# ------------------------------------------------------- check 2: dictionary

def check_dictionary(n=4000, seed=77002, pmax=3, lmax=4):
    """Composed slope 3^M/2^S; fixed point y* = N_W/q(W) with q unreduced and
    N_W = 2^S * B_P an integer matching Lemma 14.15.9.1's formula (the
    order-convention reconciliation); N_W positive, odd, 3-coprime; q(W)
    rotation-invariant; rotated fixed points one chained G-orbit."""
    rng = random.Random(seed)
    pre = len(FAILURES)
    for _ in range(n):
        p = rng.randint(1, pmax)
        word = tuple((rng.randint(1, lmax), rng.randint(1, lmax)) for _ in range(p))
        M, S, q = M_of(word), S_of(word), q_of(word)
        A, B = compose(word)
        if A != Fraction(3 ** M, 2 ** S):
            fail(f"slope: {word}")
        N = N_formula(word)
        # order-convention reconciliation: 2^S * B_P (index-order composition) == N
        if Fraction(2 ** S) * B != N:
            fail(f"N_W = 2^S*B_P mismatch (order convention): {word}")
        if not (N > 0 and N % 2 == 1 and N % 3 != 0):
            fail(f"N_W parity/positivity/3-coprimality: {word}")
        ystar = B / (1 - A)
        if ystar != Fraction(N, q):
            fail(f"N/q identity: {word}")
        # rotation invariance of q and the chained rotated fixed points
        rots = rotations(word)
        ys = [fixed_point(w) for w in rots]
        for i, w in enumerate(rots):
            if q_of(w) != q:
                fail(f"q rotation invariance: {word} rot {i}")
            a, b = letter_affine(*word[i])
            if a * ys[i] + b != ys[(i + 1) % p]:
                fail(f"rotated fixed points not chained: {word} rot {i}")
    print(f"check 2 (dictionary): {n} random words (p <= {pmax}, letters <= {lmax}), "
          f"seed {seed}: {'OK' if len(FAILURES) == pre else 'FAILURES'}")


# ------------------------------------------------- check 3: the known cycles

KNOWN_TABLE = [
    # word,               anchor (k, m, q),  y*,   classical T-cycle (in T-visit order)
    (((1, 1),), (1, 2, 1), 1, [1]),
    (((2, 1),), (2, 3, -1), -5, [-5, -7]),
    (((4, 1), (3, 3)), (7, 11, -139), -17,
     [-17, -25, -37, -55, -41, -61, -91]),
]


def check_known_cycle_table():
    """The per-cycle table: word -> (M, S, q) matches the recorded near-miss anchor
    (cycles.md 12.6.1.2, odd-step frame), y* = N_W/q(W) reduces to the recorded
    door, full cycle-membership under G (follows its word and returns), and the
    classical T-cycle is reproduced with exactly M odd steps and S halvings.
    Plus: {-1} outside the door coding, and ((4,1),(3,3)) primitive."""
    pre = len(FAILURES)
    for word, anchor, ydoor, tcycle in KNOWN_TABLE:
        M, S, q = M_of(word), S_of(word), q_of(word)
        if (M, S, q) != anchor:
            fail(f"anchor triple: {word} -> {(M, S, q)} != {anchor}")
        ystar = fixed_point(word)
        if ystar != Fraction(N_formula(word), q) or ystar != ydoor:
            fail(f"fixed point: {word} -> {ystar} != {ydoor}")
        if not follows_and_returns(ydoor, word):
            fail(f"cycle membership under G: {word}")
        # classical frame: iterate T from the door, M odd steps, S halvings, closed orbit
        x, halvings, visited = ydoor, 0, []
        for _ in range(M):
            visited.append(x)
            x, v = T_step(x)
            halvings += v
        if x != ydoor or halvings != S or visited != tcycle:
            fail(f"T-frame: {word}: visited {visited}, halvings {halvings}")
    # word primitivity of ((4,1),(3,3)): its two letters differ, so it is not a
    # repetition of a shorter (period-1) word
    if KNOWN_TABLE[2][0][0] == KNOWN_TABLE[2][0][1]:
        fail("((4,1),(3,3)) not primitive?")
    # {-1}: the singular point -- stratum/G undefined (y + 1 = 0 has no finite v2);
    # classically T(-1) = -1
    ok_singular = True
    try:
        stratum_and_G(-1)
        ok_singular = False
    except AssertionError:
        pass
    if not ok_singular:
        fail("stratum_and_G(-1) did not reject the singular point")
    if T_step(-1)[0] != -1:
        fail("T(-1) != -1")
    # the -41 rotation: ((3,3),(4,1)) has fixed point -41, chained with -17
    rot = ((3, 3), (4, 1))
    if fixed_point(rot) != -41 or not follows_and_returns(-41, rot):
        fail("rotation ((3,3),(4,1)) / -41")
    print(f"check 3 (known-cycle table): 3 anchors + T-frames + {{-1}} + rotation: "
          f"{'OK' if len(FAILURES) == pre else 'FAILURES'}")


# --------------------------------------- check 4: bounded census consistency

def check_census_consistency(n=4000, seed=77003, pmax=3, lmax=4, Mcap=10):
    """Bounded dictionary verification against the recorded census (cycles.md
    12.6.1.2, exhaustive at k <= 10 -- the census authority; this scan is capped
    at M(W) <= 10, at/below that precedent, and is NOT a cycle search): among
    random words, every one whose fixed point is an integer is odd, != -1, lies
    in {1, -5, -17, -41} (the recorded cycles' doors), and follows its word and
    returns -- no strays.  Corollary support: every scanned word with
    |q(W)| = 1 has an integer fixed point and is realized."""
    rng = random.Random(seed)
    pre = len(FAILURES)
    n_scanned = n_integer = n_q1 = 0
    census_doors = {1, -5, -17, -41}
    while n_scanned < n:
        p = rng.randint(1, pmax)
        word = tuple((rng.randint(1, lmax), rng.randint(1, lmax)) for _ in range(p))
        if M_of(word) > Mcap:
            continue  # stay at/below the census authority's k <= 10
        n_scanned += 1
        ystar = fixed_point(word)
        if abs(q_of(word)) == 1:
            n_q1 += 1
            if ystar.denominator != 1:
                fail(f"|q|=1 but non-integer fixed point: {word}")
        if ystar.denominator == 1:
            n_integer += 1
            y = int(ystar)
            if y % 2 == 0 or y == -1:
                fail(f"integer fixed point even or -1: {word} -> {y}")
            if y not in census_doors:
                fail(f"STRAY integer fixed point (not in recorded census): {word} -> {y}")
            if not follows_and_returns(y, word):
                fail(f"integer fixed point does not follow its word: {word} -> {y}")
    print(f"check 4 (bounded census consistency, M(W) <= {Mcap}): {n_scanned} words "
          f"(p <= {pmax}, letters <= {lmax}), seed {seed}: {n_integer} integer fixed "
          f"points, {n_q1} words with |q| = 1, 0 strays: "
          f"{'OK' if len(FAILURES) == pre else 'FAILURES'}")
    return n_integer, n_q1


if __name__ == "__main__":
    check_per_letter()
    check_dictionary()
    check_known_cycle_table()
    check_census_consistency()
    print()
    if FAILURES:
        print(f"TOTAL FAILURES: {len(FAILURES)}")
        raise SystemExit(1)
    print("ALL CHECKS PASSED")
