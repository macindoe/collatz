# Verification for reverse.md 14.14.7-14.14.8 (the block-map corollary layer on
# the door/exit seam), branch block-map, per briefs/block-map-brief.md.
# Fresh, independent implementation (AGENTS.md house norm) -- does not import
# from any other file in this repository, including experiments/door_seam.py.
# Grows one section per item, in the order items are proved:
#
#   14.14.7  the block-map identity: T^j(y) formula, T^m(y) = G(y), the
#            valuation word, T's own totality/live-image facts, the worked
#            instance, and the block/cascade remark tying m to spine 9.1.1
#   14.14.5.4  the total two-case metric law for Delta M3 on shared strata
#   14.14.8  composition of G along fixed itineraries: the composed affine
#            law, synchronization, and the periodic-word fixed point
import random
from fractions import Fraction


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


def T(x):
    """Accelerated odd Collatz map: T(x) = (3x+1)/2^v2(3x+1)."""
    n = 3 * x + 1
    return n >> v2(n)


def random_odd_not3(rng, hi):
    while True:
        y = rng.randrange(1, hi, 2)
        if y % 3 != 0:
            return y


def G(y):
    """The exit map, Def 14.14.3.1: m=v2(y+1), q=(y+1)/2^m, G(y)=(3^m q-1)/2^r."""
    m = v2(y + 1)
    q = (y + 1) >> m
    val = 3 ** m * q - 1
    r = v2(val)
    return val >> r, m, r


# ---------------------------------------------------------------------------
# 14.14.7  the block-map identity
# ---------------------------------------------------------------------------

def test_block_map_iterates(trials=6000, seed=15001, hi=10 ** 6):
    """T^j(y) = 3^j 2^(m-j) q - 1 for 0<=j<m, T^m(y) = G(y), and the valuation
    word (1,...,1 [m-1 times], r+1)."""
    rng = random.Random(seed)
    bad = 0
    word_bad = 0
    for _ in range(trials):
        y = random_odd_not3(rng, hi)
        m = v2(y + 1)
        q = (y + 1) >> m
        x = y
        word = []
        for j in range(m):
            pred = 3 ** j * 2 ** (m - j) * q - 1
            if x != pred:
                bad += 1
            nxt = 3 * x + 1
            vv = v2(nxt)
            word.append(vv)
            x = nxt >> vv
        gy, gm, gr = G(y)
        if gm != m:
            bad += 1
        if x != gy:
            bad += 1
        expected_word = [1] * (m - 1) + [gr + 1]
        if word != expected_word:
            word_bad += 1
        if sum(word) != m + gr:
            word_bad += 1
    return trials, bad, word_bad


def test_T_general_facts(trials=8000, seed=15002, hi=10 ** 7):
    """T is total on every odd x and never outputs a multiple of 3 -- for any
    odd x, not only live doors; this alone re-derives 14.14.3.2(3)."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        x = rng.randrange(1, hi, 2)  # odd; may or may not be a multiple of 3
        y = T(x)
        if y % 2 == 0 or y <= 0:
            bad += 1
        if y % 3 == 0:
            bad += 1
    return trials, bad


def test_worked_instance():
    x = 7
    path = [x]
    for _ in range(3):
        x = T(x)
        path.append(x)
    gy, m, r = G(7)
    ok = (path == [7, 11, 17, 13]) and (m == 3) and (r == 1) and (gy == 13)
    return ok, path, m, r, gy


def test_block_remark(trials=4000, seed=15003, hi_om=10 ** 5, hi_D=25):
    """m = D-a for y at position a of state (Omega,D) = state(y) (spine 9.1.1's
    own indexing), and G(y) equals that block's x_exit for every position a,
    not only a=0 -- verified both via the direct x_exit formula and via
    literally iterating T m times from y."""
    rng = random.Random(seed)
    bad = 0
    checked = 0
    for _ in range(trials):
        Om = random_odd_not3(rng, hi_om)
        D = rng.randrange(1, hi_D)
        a = rng.randrange(0, D)
        y = (1 << (D - a)) * 3 ** a * Om - 1
        if y % 3 == 0:
            continue
        checked += 1
        m_expected = D - a
        gy, m, r = G(y)
        if m != m_expected:
            bad += 1
        A = 3 ** D * Om - 1
        s = v2(A)
        x_exit = A >> s
        if gy != x_exit:
            bad += 1
        x = y
        for _ in range(m):
            x = T(x)
        if x != x_exit:
            bad += 1
    return checked, bad


# ---------------------------------------------------------------------------
# 14.14.5.4  the total two-case metric law
# ---------------------------------------------------------------------------

def v3_rational(fr):
    """v3 of a Fraction (well-defined regardless of representation)."""
    if fr == 0:
        return None
    return v3(fr.numerator) - v3(fr.denominator)


def matched_stratum_pairs(rng, target, hi=10 ** 7, max_attempts=400000):
    """A batch of (y, z) live-door pairs sharing one (m, r)-stratum."""
    pairs = []
    attempts = 0
    while len(pairs) < target and attempts < max_attempts:
        attempts += 1
        y = random_odd_not3(rng, hi)
        z = random_odd_not3(rng, hi)
        if y == z:
            continue
        _, my, ry = G(y)
        _, mz, rz = G(z)
        if my == mz and ry == rz:
            pairs.append((y, z))
    return pairs, attempts


def test_metric_law_algebra(trials=3000, seed=15005, hi=10 ** 7):
    """The core algebraic step: v3(H(z)/H(y) - 1) = v3(z-y) exactly, for
    H(u) = u/G(u), on a shared (m,r)-stratum. Exact Fraction arithmetic --
    no anchor computation, no precision truncation."""
    rng = random.Random(seed)
    pairs, attempts = matched_stratum_pairs(rng, trials, hi=hi)
    bad = 0
    for y, z in pairs:
        gy, _, _ = G(y)
        gz, _, _ = G(z)
        Hy = Fraction(y, gy)
        Hz = Fraction(z, gz)
        lhs = Hz / Hy - 1
        if v3_rational(lhs) != v3(z - y):
            bad += 1
    return len(pairs), attempts, bad


def M3_full(y, K):
    """Integer representative of M3(y), mod 2*3^K -- both the parity (Z/2)
    and Z_3 components of the exponent group E_3 (Def 14.2.2), via digit-by-
    digit Hensel lifting of 2^t = -1/y."""
    t = 0 if pow(2, 0, 3) == (-pow(y, -1, 3)) % 3 else 1
    for j in range(1, K + 1):
        mod = 3 ** (j + 1)
        tgt = (-pow(y, -1, mod)) % mod
        stride = 2 * 3 ** (j - 1)
        for c in range(3):
            cand = t + c * stride
            if pow(2, cand, mod) == tgt:
                t = cand
                break
    return t


def test_metric_law_cases(trials=2500, seed=15006, K=10, hi=10 ** 7):
    """(i) v3(z-y)=0  <=>  Delta M3(z)-Delta M3(y) odd (parity in E_3).
    (ii) v3(z-y)>=1  =>  the difference is even and v3(Delta) = v3(z-y)-1."""
    rng = random.Random(seed)
    pairs, attempts = matched_stratum_pairs(rng, trials, hi=hi)
    mod = 2 * 3 ** K
    n_case1 = n_case2 = bad1 = bad2 = skipped = 0
    for y, z in pairs:
        gy, _, _ = G(y)
        gz, _, _ = G(z)
        dM_y = (M3_full(gy, K) - M3_full(y, K)) % mod
        dM_z = (M3_full(gz, K) - M3_full(z, K)) % mod
        Delta = (dM_z - dM_y) % mod
        vzy = v3(z - y)
        parity_odd = (Delta % 2 == 1)
        if vzy == 0:
            n_case1 += 1
            if not parity_odd:
                bad1 += 1
        else:
            n_case2 += 1
            if parity_odd:
                bad2 += 1
                continue
            if vzy - 1 >= K:
                skipped += 1
                continue
            Delta3 = Delta % (3 ** K)
            v_delta = v3(Delta3) if Delta3 != 0 else K
            if v_delta != vzy - 1:
                bad2 += 1
    return len(pairs), attempts, n_case1, n_case2, bad1, bad2, skipped


# ---------------------------------------------------------------------------
# 14.14.8  composition along fixed itineraries
# ---------------------------------------------------------------------------

def itinerary_of(y, n):
    """The actual n-step stratum itinerary [(m_0,r_0),...,(m_{n-1},r_{n-1})]
    realized by iterating G from y, plus the resulting door G^n(y)."""
    strata = []
    cur = y
    for _ in range(n):
        g, m, r = G(cur)
        strata.append((m, r))
        cur = g
    return strata, cur


def compose_affine(strata):
    """A_n, B_n (exact Fractions) for G^n(y) = A_n*y + B_n on doors following
    the given itinerary: A_0=1,B_0=0; A_{i+1}=alpha_i*A_i, B_{i+1}=alpha_i*B_i+beta_i."""
    A = Fraction(1)
    B = Fraction(0)
    for m, r in strata:
        alpha = Fraction(3) ** m / Fraction(2) ** (m + r)
        beta = (Fraction(3) ** m - Fraction(2) ** m) / Fraction(2) ** (m + r)
        B = alpha * B + beta
        A = alpha * A
    return A, B


def test_composed_affine(trials=1500, seed=15007, n=4, hi=10 ** 6):
    """G^n(y) = A_n y + B_n exactly (integer identity), and v3(A_n) = sum(m_i)."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        y0 = random_odd_not3(rng, hi)
        strata, yn_direct = itinerary_of(y0, n)
        A, B = compose_affine(strata)
        yn_formula = A * y0 + B
        if yn_formula != yn_direct:
            bad += 1
        Sm = sum(m for m, r in strata)
        if v3(A.numerator) != Sm or A.denominator % 3 == 0:
            bad += 1
    return trials, bad


def test_composed_difference(trials=800, seed=15008, n=3, hi=10 ** 6, max_attempts=900000):
    """v3(G^n(y) - G^n(z)) = v3(y-z) + sum(m_i) for y,z sharing an itinerary."""
    rng = random.Random(seed)
    bad = n_pairs = attempts = 0
    while n_pairs < trials and attempts < max_attempts:
        attempts += 1
        y = random_odd_not3(rng, hi)
        z = random_odd_not3(rng, hi)
        if y == z:
            continue
        sy, yn = itinerary_of(y, n)
        sz, zn = itinerary_of(z, n)
        if sy != sz:
            continue
        n_pairs += 1
        expected = v3(y - z) + sum(m for m, r in sy)
        if v3(yn - zn) != expected:
            bad += 1
    return n_pairs, attempts, bad


def test_synchronization(trials=600, seed=15009, n=3, hi=10 ** 6, max_attempts=1500000, k=2):
    """Once sum(m_i) >= k+1, y_n mod 3^(k+1) is itinerary-determined --
    matches across different y_0 sharing the itinerary, and matches B_n."""
    rng = random.Random(seed)
    bad = n_checked = n_pairs = attempts = 0
    while n_pairs < trials and attempts < max_attempts:
        attempts += 1
        y = random_odd_not3(rng, hi)
        z = random_odd_not3(rng, hi)
        if y == z:
            continue
        sy, yn = itinerary_of(y, n)
        sz, zn = itinerary_of(z, n)
        if sy != sz:
            continue
        n_pairs += 1
        Sm = sum(m for m, r in sy)
        if Sm < k + 1:
            continue
        n_checked += 1
        mod = 3 ** (k + 1)
        A, B = compose_affine(sy)
        Bmod = (B.numerator * pow(B.denominator, -1, mod)) % mod
        if yn % mod != zn % mod:
            bad += 1
        if yn % mod != Bmod:
            bad += 1
    return n_pairs, n_checked, attempts, bad


def test_periodic_fixed_point_algebra(trials=500, seed=15010, n_max=4, hi=10 ** 5):
    """For any itinerary (not necessarily from a real periodic orbit), the
    algebraic fixed point y* = B_n/(1-A_n) satisfies A_n*y*+B_n = y* exactly."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        n = rng.randrange(1, n_max + 1)
        y0 = random_odd_not3(rng, hi)
        strata, _ = itinerary_of(y0, n)
        A, B = compose_affine(strata)
        if A == 1:
            continue
        ystar = B / (1 - A)
        got = A * ystar + B
        if got != ystar:
            bad += 1
    return trials, bad


def test_trivial_fixed_point_sanity():
    """The sanity instance in the brief: door y=1, word (m,r)=(1,1), A=3/4,
    B=1/4, y* = (1/4)/(1/4) = 1."""
    gy, m, r = G(1)
    A = Fraction(3, 4)
    B = Fraction(1, 4)
    ystar = B / (1 - A)
    ok = (gy == 1 and m == 1 and r == 1 and ystar == 1)
    return ok, gy, m, r, ystar


if __name__ == "__main__":
    print("== 14.14.7 block-map identity ==")
    trials, bad, word_bad = test_block_map_iterates()
    print(f"T^j(y) formula + T^m(y)=G(y): {trials} checked, {bad} failures")
    print(f"valuation word (1,...,1[m-1],r+1), sum=m+r: {word_bad} failures")

    trials, bad = test_T_general_facts()
    print(f"T total + 3-nmid-T(x) for any odd x: {trials} checked, {bad} failures")

    ok, path, m, r, gy = test_worked_instance()
    print(f"worked instance 7->11->17->13: path={path}, m={m}, r={r}, G(7)={gy}, ok={ok}")

    checked, bad = test_block_remark()
    print(f"block remark (m=D-a, G(y)=block's x_exit for any position a): "
          f"{checked} checked, {bad} failures")

    print("== 14.14.5.4 total two-case metric law ==")
    n, attempts, bad = test_metric_law_algebra()
    print(f"algebra: v3(H(z)/H(y)-1) = v3(z-y): {n} pairs ({attempts} attempts), "
          f"{bad} failures")

    n, attempts, n1, n2, bad1, bad2, skipped = test_metric_law_cases()
    print(f"cases: {n} pairs ({attempts} attempts); case(i) v3=0: {n1} pairs, "
          f"{bad1} failures; case(ii) v3>=1: {n2} pairs, {bad2} failures, "
          f"{skipped} skipped (v3(z-y)-1 >= K)")

    print("== 14.14.8 composition along fixed itineraries ==")
    trials, bad = test_composed_affine()
    print(f"G^n(y)=A_n y+B_n, v3(A_n)=sum(m_i): {trials} checked, {bad} failures")

    n_pairs, attempts, bad = test_composed_difference()
    print(f"v3(G^n(y)-G^n(z))=v3(y-z)+sum(m_i): {n_pairs} pairs ({attempts} "
          f"attempts), {bad} failures")

    n_pairs, n_checked, attempts, bad = test_synchronization()
    print(f"synchronization: {n_pairs} shared-itinerary pairs ({attempts} "
          f"attempts), {n_checked} with sum(m_i)>=k+1, {bad} failures")

    trials, bad = test_periodic_fixed_point_algebra()
    print(f"periodic fixed point algebra (A y*+B=y*): {trials} checked, "
          f"{bad} failures")

    ok, gy, m, r, ystar = test_trivial_fixed_point_sanity()
    print(f"trivial fixed point sanity: G(1)={gy}, (m,r)=({m},{r}), "
          f"y*={ystar}, ok={ok}")
