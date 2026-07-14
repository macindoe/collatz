# Verification for reverse.md 14.14 (the door/exit seam), branch door-seam.
# Fresh, independent implementation (AGENTS.md house norm) -- does not import
# from any other file in this repository. Grows one section per item, in the
# order items are proved (see reverse.md 14.14 for the theorem statements).
#
#   14.14.1  global edge parameterization: exit equation + door-recovery
#            dictionary (C = 2^s(y+1), sigma = s+m, a_+ = a)
#   14.14.2  the door-centred Bridge identity  Delta M = J(n1) - J(n2)
#   14.14.3  the exit map G = E o R: totality, live image, conjugacy to F,
#            fiber-constancy across a state's doors
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


def state_of_door(y):
    """Recover (Omega, D) from a live door y (reverse.md 14.6.5.1)."""
    m = v2(y + 1)
    a = v3(y + 1)
    Om = (y + 1) // ((1 << m) * 3 ** a)
    D = m + a
    return Om, D, m, a


def G(y):
    """The exit map, Def 14.14.3.1: m=v2(y+1), q=(y+1)/2^m, G(y)=(3^m q -1)/2^r."""
    m = v2(y + 1)
    q = (y + 1) >> m
    val = 3 ** m * q - 1
    r = v2(val)
    return val >> r, m, r


def random_odd_not3(rng, hi):
    while True:
        y = rng.randrange(1, hi, 2)
        if y % 3 != 0:
            return y


def random_valid_door(rng, hi_om, hi_d):
    """A live door y_a of a random valid state (Omega, D)."""
    Om = random_odd_not3(rng, hi_om)
    D = rng.randrange(1, hi_d)
    a = rng.randrange(0, D)
    y = (1 << (D - a)) * 3 ** a * Om - 1
    return y, Om, D, a


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


# ---------------------------------------------------------------------------
# 14.14.3  the exit map G: totality, live image, conjugacy, fiber-constancy
# ---------------------------------------------------------------------------

def test_item3(trials=6000, seed=1004):
    rng = random.Random(seed)
    n_total = bad_total = 0
    n_live = bad_live = 0
    n_conj = bad_conj = 0
    n_fiber = bad_fiber = 0
    for _ in range(trials):
        y, Om, D, a = random_valid_door(rng, 10 ** 5, 30)
        if y % 3 == 0:
            continue
        n_total += 1
        gy, m, r = G(y)
        if gy % 2 == 0:
            bad_total += 1
        n_live += 1
        if gy % 3 == 0:
            bad_live += 1
        n_conj += 1
        wp, dp, _, _, _, _ = forward_step(Om, D)
        Om2, D2, _, _ = state_of_door(gy)
        if (Om2, D2) != (wp, dp):
            bad_conj += 1
        if D >= 2:
            a2 = rng.randrange(0, D)
            y2 = (1 << (D - a2)) * 3 ** a2 * Om - 1
            if y2 % 3 != 0:
                n_fiber += 1
                gy2, _, _ = G(y2)
                if gy2 != gy:
                    bad_fiber += 1
    return dict(total=(n_total, bad_total), live=(n_live, bad_live),
                conj=(n_conj, bad_conj), fiber=(n_fiber, bad_fiber))


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

    print("== 14.14.3 the exit map G ==")
    res = test_item3()
    for k, (n, b) in res.items():
        print(f"  {k}: {n} checked, {b} failures")
