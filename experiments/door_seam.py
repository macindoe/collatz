# Verification for reverse.md 14.14 (the door/exit seam), branch door-seam.
# Fresh, independent implementation (AGENTS.md house norm) -- does not import
# from any other file in this repository. Grows one section per item, in the
# order items are proved (see reverse.md 14.14 for the theorem statements).
#
#   14.14.1  global edge parameterization: exit equation + door-recovery
#            dictionary (C = 2^s(y+1), sigma = s+m, a_+ = a)
import random


def v2(x):
    return (x & -x).bit_length() - 1


def v3(x):
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def forward_step(w, d):
    """One reduced-map step (ω,d) -> (ω_+,d_+); returns full derived data."""
    A = 3 ** d * w - 1
    s = v2(A)
    C = A + (1 << s)
    sigma = v2(C)
    ap = v3(C)
    wp = (C >> sigma) // 3 ** ap
    dp = sigma - s + ap
    return wp, dp, s, sigma, ap, C


def random_odd_not3(rng, hi):
    while True:
        y = rng.randrange(1, hi, 2)
        if y % 3 != 0:
            return y


# ---------------------------------------------------------------------------
# 14.14.1  global edge parameterization
# ---------------------------------------------------------------------------

def test_item1(trials=6000, seed=1001):
    rng = random.Random(seed)
    bad = checked = 0
    for _ in range(trials):
        w = random_odd_not3(rng, 10 ** 6)
        d = rng.randrange(1, 45)
        wp, dp, s, sigma, ap, C = forward_step(w, d)
        y = ((3 ** d) * w - 1) >> s
        if y % 2 == 0:
            continue
        checked += 1
        ok = (3 ** d * w == 1 + (1 << s) * y)
        m = v2(y + 1)
        a = v3(y + 1)
        ok &= (y + 1 == (1 << m) * 3 ** a * wp)
        ok &= (dp == m + a)
        ok &= (C == (1 << s) * (y + 1))
        ok &= (sigma == s + m)
        ok &= (ap == a)
        if not ok:
            bad += 1
    return checked, bad


if __name__ == "__main__":
    print("== 14.14.1 global edge parameterization ==")
    checked, bad = test_item1()
    print(f"exit equation + recovery dictionary: {checked} checked, {bad} failures")
