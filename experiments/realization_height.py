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
