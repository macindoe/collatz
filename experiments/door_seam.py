# Verification for reverse.md 14.14 (the door/exit seam), branch door-seam.
# Fresh, independent implementation (AGENTS.md house norm) -- does not import
# from any other file in this repository. Grows one section per item, in the
# order items are proved (see reverse.md 14.14 for the theorem statements).
#
#   14.14.1  global edge parameterization: exit equation + door-recovery
#            dictionary (C = 2^s(y+1), sigma = s+m, a_+ = a)
#   14.14.2  the door-centred Bridge identity  Delta M = J(n1) - J(n2)
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


def N_anchor(u, k):
    """9^n = u^-1 (mod 2^(k+3)); n mod 2^k. Requires u == 1 (mod 8)."""
    n = 0
    for j in range(k):
        m = 1 << (j + 4)
        if pow(9, n, m) != pow(u % m, -1, m):
            n += 1 << j
    return n


def M_anchor(w, k):
    """M(w) = N(w^2) mod 2^k, well-defined for every odd w."""
    u = (w * w) % (1 << (k + 3))
    return N_anchor(u, k)


def J(n, k):
    """J(n) = M(n / 3^v3(n)) mod 2^k, for odd n."""
    core = n // 3 ** v3(n)
    return M_anchor(core, k)


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


# ---------------------------------------------------------------------------
# 14.14.2  door-centred Bridge identity
# ---------------------------------------------------------------------------

def test_item2(trials=6000, seed=1002, K=8):
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
        dM_true = (M_anchor(wp, K) - M_anchor(w, K)) % (1 << K)
        n1 = (y + 1) >> v2(y + 1)
        n2 = 1 + (1 << s) * y
        rhs = (J(n1, K) - J(n2, K)) % (1 << K)
        if rhs != dM_true:
            bad += 1
    return checked, bad


def test_M3_facts(trials=1000, seed=1003):
    """M(3) = -1 (M(ω) = -2 log ω / log 9, ω=3) and complete multiplicativity of M."""
    rng = random.Random(seed)
    m3 = M_anchor(3, 12) % 4096
    bad_m3 = 0 if m3 == (-1) % 4096 else 1
    bad_mult = 0
    for _ in range(trials):
        a = random_odd_not3(rng, 5000)
        b = random_odd_not3(rng, 5000)
        k = 10
        if (M_anchor(a * b, k) - M_anchor(a, k) - M_anchor(b, k)) % (1 << k) != 0:
            bad_mult += 1
    return bad_m3, trials, bad_mult


if __name__ == "__main__":
    print("== 14.14.1 global edge parameterization ==")
    checked, bad = test_item1()
    print(f"exit equation + recovery dictionary: {checked} checked, {bad} failures")

    print("== 14.14.2 door-centred Bridge identity ==")
    checked, bad = test_item2()
    print(f"Delta M = J(n1) - J(n2): {checked} checked, {bad} failures")
    bad_m3, nmult, bad_mult = test_M3_facts()
    print(f"M(3) = -1 check: {'ok' if bad_m3 == 0 else 'FAIL'}; "
          f"multiplicativity of M: {nmult} checked, {bad_mult} failures")
