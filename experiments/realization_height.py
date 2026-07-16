# Verification for reverse.md 14.15.4 (the unique-predecessor lemma, the
# finite bicylinder corollary, and the positive realization height), branch
# bicylinder-height, per briefs/bicylinder-height-brief.md.
#
# Fresh, independent implementation (AGENTS.md house norm) -- imports
# nothing from experiments/itinerary_coding.py, experiments/block_map.py,
# or experiments/door_seam.py, even though the underlying objects (the
# stratum labels, the exit map G) are the same ones those files also
# reimplement independently.
#
# Sections, matching reverse.md 14.15.4's own lettering, added one per
# commit as the wiki subsections land:
#
#   14.15.4(a)  the unique-predecessor lemma: round-trip correctness
#               (formula reproduces the source door, forced positivity /
#               oddness / stratum), exhaustive uniqueness (injectivity of
#               G jointly with stratum), and a direct probe of the
#               external suggestion's claimed failure mode (negativity --
#               does not occur)
#   14.15.4(b)  the finite bicylinder corollary: a positive live door with
#               an actual prescribed finite past (letter-prescribed
#               backward chain, live deepest door, intermediate doors live
#               automatically) and prescribed finite future
#   14.15.4(c)  the positive realization height: R_{p,q}/H_{p,q} sanity on
#               the two families the brief permits -- the trivial
#               all-(1,1) word has H = 1 at every window tried, and
#               fixed-origin nested-window monotonicity over random words.
#               No growth study of H is performed (out of scope per the
#               brief's stop line).
import random


def v2(x):
    x = abs(x)
    if x == 0:
        return None
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def v3(x):
    x = abs(x)
    if x == 0:
        return None
    c = 0
    while x % 3 == 0:
        x //= 3
        c += 1
    return c


def stratum_and_G(y):
    """m = v2(y+1), q = (y+1)/2^m, r = v2(3^m q - 1), G(y) = (3^m q - 1)/2^r.
    Defined for every odd y > 0 (reverse.md 14.15.1.1 / 14.14.7.1), live
    door or not."""
    m = v2(y + 1)
    q = (y + 1) >> m
    val = 3 ** m * q - 1
    r = v2(val)
    return val >> r, m, r


def G(y):
    return stratum_and_G(y)[0]


def stratum(y):
    _, m, r = stratum_and_G(y)
    return m, r


def unique_predecessor(z, m, r):
    """Theorem 14.15.4.1: the unique odd integer y with G(y) = z and
    stratum(y) = (m,r), or None if 3^m does not divide 2^r z + 1. No
    liveness claim is made or checked here -- that is a separate condition
    (14.15.4(b)/(c))."""
    num = (1 << r) * z + 1
    denom = 3 ** m
    if num % denom != 0:
        return None
    q = num // denom
    return (1 << m) * q - 1


def random_odd(rng, hi, lo=1):
    return rng.randrange(lo, hi, 2)


def random_odd_not3(rng, hi):
    while True:
        y = rng.randrange(1, hi, 2)
        if y % 3 != 0:
            return y


# ---------------------------------------------------------------------------
# 14.15.4(a): the unique-predecessor lemma
# ---------------------------------------------------------------------------

def test_predecessor_roundtrip(trials=6000, seed=35001, hi=10 ** 7):
    """Random live y -> (m,r)=stratum(y), z=G(y) -> unique_predecessor(z,m,r)
    must reproduce y exactly, land on stratum (m,r), and have G-image z --
    all forced by the theorem's construction, not separately imposed. Also
    confirms positivity and oddness (never assumed, always re-derived)."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        y = random_odd_not3(rng, hi)
        m, r = stratum(y)
        z = G(y)
        y2 = unique_predecessor(z, m, r)
        if (y2 != y or y2 <= 0 or y2 % 2 == 0
                or stratum(y2) != (m, r) or G(y2) != z):
            bad += 1
    return trials, bad


def test_exhaustive_uniqueness(y_max=2 ** 21, m_cap=6, r_cap=6):
    """Group every odd y < y_max by (stratum(y), G(y)); confirm every group
    has at most one member. This is the uniqueness half of Theorem
    14.15.4.1 checked directly by exhaustive collision search, independent
    of the formula (which is checked separately in
    test_predecessor_roundtrip)."""
    seen = {}
    groups = 0
    violations = 0
    for y in range(1, y_max, 2):
        m, r = stratum(y)
        if m > m_cap or r > r_cap:
            continue
        z = G(y)
        key = (m, r, z)
        prev = seen.get(key)
        if prev is None:
            seen[key] = y
            groups += 1
        elif prev != y:
            violations += 1
    return groups, violations


def test_no_negativity(trials=8000, seed=35002, m_hi=8, r_hi=25, z_hi=10 ** 6):
    """Direct probe of the external suggestion's claimed failure mode
    ("negative ... deep predecessors"): for random (m,r,z) -- z drawn
    independently of any real door construction, not just as a G-image of
    a well-behaved input -- wherever the admissibility congruence holds,
    confirm y is always positive. (m up to 8 exercises deep strata, per
    the brief's "even at large m" framing.)"""
    rng = random.Random(seed)
    checked = 0
    bad = 0
    for _ in range(trials):
        m = rng.randrange(1, m_hi)
        r = rng.randrange(1, r_hi)
        z = random_odd_not3(rng, z_hi)
        y = unique_predecessor(z, m, r)
        if y is None:
            continue
        checked += 1
        if y <= 0:
            bad += 1
        # forced stratum/oddness, checked here too since z was not
        # constructed from a real door this time
        if y % 2 == 0 or stratum(y) != (m, r) or G(y) != z:
            bad += 1
    return checked, bad


# ---------------------------------------------------------------------------
# 14.15.4(b): the finite bicylinder corollary
# ---------------------------------------------------------------------------

def find_live_predecessor(cur, rng, m_cap=3, r_cap=30, tries=400):
    """Search for a live letter-prescribed predecessor of `cur`: try a
    random small m, scan r (2 is a primitive root mod 3^m of order
    2*3^(m-1) <= 2*3^(m_cap-1), so r_cap comfortably covers one full period
    for m <= m_cap = 3) until unique_predecessor succeeds AND the result is
    live (3 does not divide it -- unique_predecessor itself makes no
    liveness claim). Returns (y, m, r) or None."""
    for _ in range(tries):
        m = rng.randrange(1, m_cap + 1)
        for r in range(1, r_cap):
            y = unique_predecessor(cur, m, r)
            if y is not None and y % 3 != 0:
                return y, m, r
    return None


def test_bicylinder(trials=2000, seed=35003, p_max=3, q_max=3, hi=10 ** 5):
    """Theorem 14.15.4.2: build a random positive live door y0, a real
    q-step forward realization U (always exists), and a real p-step
    letter-prescribed backward chain V with live deepest door -- then check
    every claimed property directly: chain consistency (G(y_{-i})=y_{-i+1}),
    liveness of every chain door (not just the deepest -- the intermediate
    doors are claimed live automatically as G-images), stratum match
    against the recorded letters, and the forward realization of U."""
    rng = random.Random(seed)
    built = 0
    bad = 0
    for _ in range(trials):
        p = rng.randrange(0, p_max + 1)
        q = rng.randrange(0, q_max + 1)
        y0 = random_odd_not3(rng, hi)

        # forward realization U (always succeeds -- G is total)
        U = []
        cur = y0
        for _ in range(q):
            U.append(stratum(cur))
            cur = G(cur)

        # backward chain V, nearest-to-farthest: chain[0] = y_{-1}, ...
        chain = []
        V_near_to_far = []
        cur_b = y0
        ok = True
        for _ in range(p):
            res = find_live_predecessor(cur_b, rng)
            if res is None:
                ok = False
                break
            y_prev, m, r = res
            chain.append(y_prev)
            V_near_to_far.append((m, r))
            cur_b = y_prev
        if not ok:
            continue
        built += 1

        # (i) y0 itself positive and live
        if y0 <= 0 or y0 % 3 == 0:
            bad += 1
        # (ii) deepest door live (already ensured at construction; recheck)
        if chain and chain[-1] % 3 == 0:
            bad += 1
        # (iii) every chain door live, not just the deepest
        if any(c % 3 == 0 for c in chain):
            bad += 1
        # (iv) chain consistency and stratum match against recorded letters
        cprev = y0
        for y_prev, (m, r) in zip(chain, V_near_to_far):
            if G(y_prev) != cprev or stratum(y_prev) != (m, r):
                bad += 1
            cprev = y_prev
        # (v) forward realization of U
        cur_f = y0
        for (m, r) in U:
            if stratum(cur_f) != (m, r):
                bad += 1
            cur_f = G(cur_f)

    return trials, built, bad


# ---------------------------------------------------------------------------
# 14.15.4(c): the positive realization height -- sanity families only
# ---------------------------------------------------------------------------

def in_R(y0, W_future, W_past_near_to_far, p, q):
    """Direct membership test for R_{p,q}(W) (Definition 14.15.4.3): y0 a
    positive live door, forward q-step realization of W_future[:q], and a
    letter-prescribed backward chain to depth p (using
    W_past_near_to_far[:p], nearest first) with live deepest door (p=0:
    vacuous, y0 itself already checked live)."""
    if y0 <= 0 or y0 % 2 == 0 or y0 % 3 == 0:
        return False
    cur = y0
    for j in range(q):
        if stratum(cur) != W_future[j]:
            return False
        cur = G(cur)
    cur = y0
    deepest_live = True
    for i in range(p):
        m, r = W_past_near_to_far[i]
        y_prev = unique_predecessor(cur, m, r)
        if y_prev is None:
            return False
        deepest_live = (y_prev % 3 != 0)
        cur = y_prev
    return deepest_live


def height(W_future, W_past_near_to_far, p, q, bound):
    """Brute-force H_{p,q}(W): the minimum positive odd y0 < bound with
    y0 in R_{p,q}(W), or None if none found below the bound."""
    for y0 in range(1, bound, 2):
        if in_R(y0, W_future, W_past_near_to_far, p, q):
            return y0
    return None


def test_trivial_word_height(p_max=4):
    """Item 3's named check (C): the all-(1,1) word has H_{p,q} = 1 at
    every window p=q<=p_max tried. y0=1 is the smallest positive odd
    integer, so confirming 1 in R_{n,n} directly (stratum(1)=G(1)=1, the
    trivial fixed point) proves H_{n,n}=1 exactly, with no search needed."""
    W_future = [(1, 1)] * p_max
    W_past = [(1, 1)] * p_max
    results = []
    bad = 0
    for n in range(0, p_max + 1):
        member = in_R(1, W_future, W_past, n, n)
        results.append(member)
        if not member:
            bad += 1
    return results, bad


def test_monotonicity(trials=20, seed=35004, letter_cap=2, levels=(1, 2),
                       bound=2 ** 17):
    """Fixed-origin nested-window monotonicity (the brief's correction:
    windows grow around one fixed pivot, never re-centred). Build a random
    word from a real backward/forward construction (so realizability at
    the deepest level tried is not begged -- the word is the actual
    itinerary of a real integer), compute H at increasing (n,n) for n in
    `levels` using the SAME underlying word and pivot, confirm
    nondecreasing, and report how many strictly grew (matching the
    pre-check's "10 of 15 strictly grew" finding)."""
    rng = random.Random(seed)
    n_max = max(levels)
    checked = 0
    bad = 0
    grew = 0
    for _ in range(trials):
        y0 = random_odd_not3(rng, 10 ** 4)

        W_future = []
        cur = y0
        for _ in range(n_max):
            W_future.append(stratum(cur))
            cur = G(cur)

        W_past = []
        cur_b = y0
        ok = True
        for _ in range(n_max):
            res = find_live_predecessor(cur_b, rng, m_cap=letter_cap, r_cap=20)
            if res is None:
                ok = False
                break
            y_prev, m, r = res
            W_past.append((m, r))
            cur_b = y_prev
        if not ok:
            continue
        checked += 1

        hs = [height(W_future, W_past, n, n, bound) for n in levels]
        if any(h is None for h in hs):
            # search bound too small for this trial's word -- a search
            # limitation, not a mathematical failure; recorded, not
            # counted as a violation, and not silently dropped
            bad += 1
            continue
        if any(hs[i] > hs[i + 1] for i in range(len(hs) - 1)):
            bad += 1
        elif hs[-1] > hs[0]:
            grew += 1

    return trials, checked, bad, grew


if __name__ == "__main__":
    print("== 14.15.4(a): predecessor round-trip ==")
    trials, bad = test_predecessor_roundtrip()
    print(f"{trials} checked, {bad} failures")

    print("== 14.15.4(a): exhaustive uniqueness (injectivity of G jointly "
          "with stratum) ==")
    groups, violations = test_exhaustive_uniqueness()
    print(f"{groups} (stratum,G-image) groups found among odd y < 2^21 "
          f"(m,r <= 6), {violations} collisions")

    print("== 14.15.4(a): no-negativity probe ==")
    checked, bad = test_no_negativity()
    print(f"{checked} admissible (m,r,z) checked, {bad} failures "
          f"(negativity or forced-condition violations)")

    print("== 14.15.4(b): finite bicylinder corollary ==")
    trials, built, bad = test_bicylinder()
    print(f"{trials} trials, {built} chains successfully built "
          f"(remainder: admissibility failed within the search budget), "
          f"{bad} failures")

    print("== 14.15.4(c): trivial all-(1,1) word, H_{p,q} = 1 ==")
    results, bad = test_trivial_word_height()
    print(f"membership of y0=1 at windows n=0..4: {results}, {bad} failures")

    print("== 14.15.4(c): fixed-origin nested-window monotonicity ==")
    trials, checked, bad, grew = test_monotonicity()
    print(f"{trials} trials, {checked} words built, {bad} violations "
          f"(incl. search-bound shortfalls), {grew} strictly grew")
