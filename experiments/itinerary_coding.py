# Verification for reverse.md 14.15 (the finite-itinerary cylinder theorem and
# the two-sided coding), branch itinerary-coding, per
# briefs/itinerary-coding-brief.md.
#
# Fresh, independent implementation (AGENTS.md house norm) -- does not import
# from any other file in this repository, including experiments/block_map.py
# or experiments/door_seam.py, even though the objects (G, stratum, T) are
# the same ones those files also reimplement independently.
#
# Sections, in the order the brief's items are proved:
#
#   14.15 item 1   the cylinder theorem: single-stratum congruence, the
#                  level-shifting bijection (single step and composed), the
#                  full theorem by exhaustive scan and by large-shift
#                  sampling, completeness, and liveness
#   14.15 item 3(a) the future determines the 2-adic coordinate: word
#                   injectivity on distinct integers
#   14.15 item 3(b) the past determines the 3-adic coordinate: real integer
#                   backward chains, the offset sequence B_n, and its
#                   convergence tested directly against the real door
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


def stratum_and_G(y):
    """m = v2(y+1), q = (y+1)/2^m, r = v2(3^m q - 1), G(y) = (3^m q - 1)/2^r.
    Defined for every odd y > 0, live door or not (Def 14.14.3.1 / 14.14.4,
    re-derived generally per 14.14.7.1's totality fact)."""
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


def itinerary(y0, n):
    """The actual n-step stratum word realized from y0, and G^n(y0)."""
    strata = []
    y = y0
    for _ in range(n):
        gy, m, r = stratum_and_G(y)
        strata.append((m, r))
        y = gy
    return strata, y


def random_odd(rng, hi, lo=1):
    return rng.randrange(lo, hi, 2)


def random_odd_not3(rng, hi):
    while True:
        y = rng.randrange(1, hi, 2)
        if y % 3 != 0:
            return y


# ---------------------------------------------------------------------------
# item 1: the finite-itinerary cylinder theorem
# ---------------------------------------------------------------------------

def test_single_stratum_exhaustive(y_max=2 ** 23, m_cap=7, r_cap=7):
    """Exhaustive scan: every odd y < y_max, bucketed by its own stratum
    (m,r) with m,r <= caps. Checks, for every bucket found: (i) all members
    share one residue mod 2^(m+r+1); (ii) distinct buckets have distinct
    residues mod their own moduli (checked implicitly -- each y falls in
    exactly one bucket by construction); (iii) completeness -- every (m,r)
    with m,r in [1,m_cap] is realized somewhere below y_max."""
    buckets = {}
    for y in range(1, y_max, 2):
        m, r = stratum(y)
        if m > m_cap or r > r_cap:
            continue
        buckets.setdefault((m, r), []).append(y)
    bad_class = 0
    for (m, r), ys in buckets.items():
        mod = 1 << (m + r + 1)
        reps = set(y % mod for y in ys)
        if len(reps) != 1:
            bad_class += 1
    missing = [(m, r) for m in range(1, m_cap + 1) for r in range(1, r_cap + 1)
               if (m, r) not in buckets]
    return len(buckets), bad_class, missing


def test_two_step_exhaustive(y_max=2 ** 21, s_cap=5):
    """Exhaustive scan for length-2 words: every odd y < y_max, bucketed by
    its 2-step stratum word, with each (m_i,r_i) capped at s_cap. Checks
    that each realized word's followers form exactly one residue class mod
    2^(S+1), S = m0+r0+m1+r1."""
    buckets = {}
    for y in range(1, y_max, 2):
        strata, _ = itinerary(y, 2)
        if any(m > s_cap or r > s_cap for m, r in strata):
            continue
        buckets.setdefault(tuple(strata), []).append(y)
    bad_class = 0
    checked_words = 0
    for word, ys in buckets.items():
        S = sum(m + r for m, r in word)
        mod = 1 << (S + 1)
        reps = set(y % mod for y in ys)
        checked_words += 1
        if len(reps) != 1:
            bad_class += 1
    return checked_words, bad_class


def test_single_stratum_level_shift(trials=15000, seed=25001, hi=10 ** 7,
                                     t_hi=10 ** 6):
    """Lemma: for y on stratum (m,r), G(y + 2^(m+r+1) t) = G(y) + 2*3^m*t
    exactly, for any integer t (tested with large random t, positive and
    negative, so the shift is not confused with a small perturbation)."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        y = random_odd(rng, hi)
        gy, m, r = stratum_and_G(y)
        t = rng.randrange(-t_hi, t_hi)
        y2 = y + (1 << (m + r + 1)) * t
        if y2 <= 0:
            continue
        gy2, m2, r2 = stratum_and_G(y2)
        if (m2, r2) != (m, r):
            bad += 1
        if gy2 != gy + 2 * 3 ** m * t:
            bad += 1
    return trials, bad


def compose_affine(strata):
    """A_n, B_n (exact Fractions) for G^n(y) = A_n*y + B_n on doors
    following the given itinerary (same recursion as 14.14.8.2)."""
    A = Fraction(1)
    B = Fraction(0)
    for m, r in strata:
        alpha = Fraction(3) ** m / Fraction(2) ** (m + r)
        beta = (Fraction(3) ** m - Fraction(2) ** m) / Fraction(2) ** (m + r)
        B = alpha * B + beta
        A = alpha * A
    return A, B


def test_composed_level_shift(trials=6000, seed=25002, n_max=6, hi=10 ** 6,
                               t_hi=10 ** 5):
    """Composed lemma: for y0 following an n-letter word with S=sum(m+r),
    M=sum(m), G^n(y0 + 2^(S+1) t) = G^n(y0) + 2*3^M*t exactly -- checked
    against direct n-fold iteration, not the affine formula, so this is an
    independent check of the induction step, not a restatement of it."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        n = rng.randrange(1, n_max + 1)
        y0 = random_odd(rng, hi)
        strata, yn = itinerary(y0, n)
        S = sum(m + r for m, r in strata)
        M = sum(m for m, r in strata)
        t = rng.randrange(-t_hi, t_hi)
        y0p = y0 + (1 << (S + 1)) * t
        if y0p <= 0:
            continue
        strata_p, ynp = itinerary(y0p, n)
        if strata_p != strata:
            bad += 1
        if ynp != yn + 2 * 3 ** M * t:
            bad += 1
    return trials, bad


def test_completeness_and_liveness(trials=1500, seed=25003, n_max=5,
                                    hi_mr=5, reps=400):
    """Corollary (a)+(b): for random finite words (built by sampling a real
    orbit's own itinerary, so realizability is not begged), the class mod
    2^(S+1) is checked to contain: (a) itself, trivially, plus a second,
    independently-found representative (nonemptiness beyond the seed);
    (b) at least one member with 3 does not divide y0 among a bounded
    scan of the class, i.e. a live door."""
    rng = random.Random(seed)
    bad_a = bad_b = 0
    for _ in range(trials):
        n = rng.randrange(1, n_max + 1)
        y0 = random_odd(rng, 10 ** 6)
        strata, _ = itinerary(y0, n)
        S = sum(m + r for m, r in strata)
        mod = 1 << (S + 1)
        rep = y0 % mod
        # (a) a second representative, found independently (rep + k*mod for
        # random k), must realize the identical word.
        k = rng.randrange(1, 10 ** 4)
        y1 = rep + k * mod
        if y1 % 2 == 0:
            y1 += mod
        strata1, _ = itinerary(y1, n)
        if strata1 != strata:
            bad_a += 1
        # (b) scan a bounded window of the class for a live (3-nmid) member.
        found_live = False
        for j in range(reps):
            cand = rep + j * mod
            if cand % 2 == 1 and cand % 3 != 0:
                found_live = True
                break
        if not found_live:
            bad_b += 1
    return trials, bad_a, bad_b


# ---------------------------------------------------------------------------
# item 3(a): the future determines the 2-adic coordinate -- injectivity
# ---------------------------------------------------------------------------

def test_word_injectivity(trials=8000, seed=25004, hi=10 ** 6, n_cap=200):
    """For distinct odd y != z, find the least n such that the n-letter
    itinerary's S_n exceeds v2(y-z); confirm the length-n words differ at
    or before that point (as the cylinder theorem forces), and confirm they
    do NOT necessarily differ earlier (both are possible) -- only that they
    cannot still agree once S_n > v2(y-z)."""
    rng = random.Random(seed)
    bad = 0
    checked = 0
    for _ in range(trials):
        y = random_odd(rng, hi)
        z = random_odd(rng, hi)
        if y == z:
            continue
        D = v2(y - z)
        sy, sz = [], []
        cy, cz = y, z
        S = 0
        n = 0
        while S <= D and n < n_cap:
            gy, my, ry = stratum_and_G(cy)
            gz, mz, rz = stratum_and_G(cz)
            sy.append((my, ry))
            sz.append((mz, rz))
            S += my + ry
            cy, cz = gy, gz
            n += 1
        checked += 1
        if sy == sz:
            bad += 1
    return checked, bad


# ---------------------------------------------------------------------------
# item 3(b): the past determines the 3-adic coordinate
# ---------------------------------------------------------------------------

def predecessor_door(y0, s):
    """Fresh reimplementation of reverse.md 14.1.1's predecessor formula
    (state (omega,d) recovered from y0 and an admissible exit valuation s,
    odd if y0 = 1 mod 3, even if y0 = 2 mod 3), reading off a live
    representative door via spine.md 9.1.1's chain x_a = 2^(d-a) 3^a omega
    - 1: try a=0 first (m=d); if that representative is dead (3 | x_0,
    reverse.md 14.5.1), fall back to a=1 (m=d-1), which 14.5.1 guarantees
    is never dead, whenever d >= 2. G(x_a) = y0 for every a, by
    fiber-constancy (14.14.3.2(2)) -- re-derived below, not assumed.
    Returns (y_prev, m, r) with r=s always, or (None, None, None) if d=1
    and the sole representative is dead (caller should redraw s)."""
    N = (1 << s) * y0 + 1
    d = v3(N)
    omega = N // (3 ** d)
    x0 = (1 << d) * omega - 1
    if x0 % 3 != 0:
        return x0, d, s
    if d >= 2:
        x1 = (1 << (d - 1)) * 3 * omega - 1
        return x1, d - 1, s
    return None, None, None


def admissible_s(rng, y0, s_hi=60):
    parity_needed = 1 if y0 % 3 == 1 else 0
    while True:
        s = rng.randrange(1, s_hi)
        if (s % 2) == parity_needed:
            return s


def build_backward_chain(y0, n, rng, max_redraws=200):
    """A genuine n-step chain of integer live doors y0, y_{-1}, ..., y_{-n}
    with G(y_{-(i+1)}) = y_{-i} exactly. Returns chain (chain[0]=y0, ...,
    chain[n]=y_{-n}) and strata_near_to_far[i] = stratum of y_{-(i+1)} =
    (m_{-(i+1)}, r_{-(i+1)}), i.e. index 0 is nearest the present. Redraws
    s whenever the d=1 dead-end case is hit (reverse.md 14.5.2's Garden of
    Eden edge, not a chain-building bug)."""
    chain = [y0]
    strata_near_to_far = []
    cur = y0
    for _ in range(n):
        for _ in range(max_redraws):
            s = admissible_s(rng, cur)
            y_prev, m, r = predecessor_door(cur, s)
            if y_prev is not None:
                break
        else:
            return None, None
        chain.append(y_prev)
        strata_near_to_far.append((m, r))
        cur = y_prev
    return chain, strata_near_to_far


def test_predecessor_sanity(trials=10000, seed=25005, hi=10 ** 6):
    """G(predecessor_door(y0,s)) = y0 exactly, and the predecessor's own
    stratum is exactly (m, s) with m as returned (d on the a=0 branch,
    d-1 on the a=1 fallback) -- checked directly against stratum_and_G,
    for both branches (forcing the d=1 dead case to be skipped, and
    otherwise letting whichever branch actually triggers be exercised)."""
    rng = random.Random(seed)
    bad = 0
    checked = 0
    fallback_used = 0
    for _ in range(trials):
        y0 = random_odd_not3(rng, hi)
        s = admissible_s(rng, y0)
        y_prev, m, r = predecessor_door(y0, s)
        if y_prev is None:
            continue
        checked += 1
        gy, gm, gr = stratum_and_G(y_prev)
        if gy != y0 or (gm, gr) != (m, r):
            bad += 1
        # detect which branch fired: a=0 has m=d=v3((1<<s)*y0+1); a=1 has m=d-1
        d_true = v3((1 << s) * y0 + 1)
        if m == d_true - 1:
            fallback_used += 1
    return checked, bad, fallback_used


def test_past_determines_3adic(trials=500, seed=25006, n_depth=100, K=8):
    """The convergence claim: for real backward chains of depth n_depth
    from a real live door y0, build the composed-affine offset B_{n'} of
    the nearest n' letters (n'=1..n_depth) and find, for each k=1..K, the
    least n' with M_{n'} = sum of the near m's >= k+1; confirm B_{n'} mod
    3^(k+1) equals y0 mod 3^(k+1) exactly, as 14.14.8.3 plus the limit
    argument predicts -- independent of the deep-past seed y_{-n_depth}."""
    rng = random.Random(seed)
    bad = 0
    checked = 0
    skipped_chain = 0
    for _ in range(trials):
        y0 = random_odd_not3(rng, 10 ** 5)
        chain, strata_near_to_far = build_backward_chain(y0, n_depth, rng)
        if chain is None or any(chain[i] % 3 == 0 for i in range(1, len(chain))):
            skipped_chain += 1
            continue
        for k in range(1, K + 1):
            M = 0
            nprime = 0
            for (m, r) in strata_near_to_far:
                M += m
                nprime += 1
                if M >= k + 1:
                    break
            if M < k + 1:
                continue
            sub_word_forward = list(reversed(strata_near_to_far[:nprime]))
            A, B = compose_affine(sub_word_forward)
            mod = 3 ** (k + 1)
            Bmod = (B.numerator * pow(B.denominator, -1, mod)) % mod
            checked += 1
            if y0 % mod != Bmod:
                bad += 1
    return trials, skipped_chain, checked, bad


def test_offset_cauchy(trials=1500, seed=25007, n_max=30):
    """Pure-algebra check of the derivation used above: for a random word,
    successively prepending letters, v3(B_{n+1}-B_n) = M_n (sum of m over
    the pre-prepend n-suffix) exactly, so (B_n) is 3-adically Cauchy since
    M_n >= n -> infinity. Exact Fraction arithmetic; no integer realization
    needed here."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        n = rng.randrange(1, n_max)
        # word_forward[0..n-1] will be prepended one at a time, so
        # word_forward is built back-to-front: index n-1 is nearest the
        # present (added first as the length-1 word), index 0 is added last
        # (farthest into the past).
        word_forward = [(rng.randrange(1, 6), rng.randrange(1, 6))
                         for _ in range(n)]
        B_prev = None
        M_running = 0
        for i in range(n - 1, -1, -1):
            sub = word_forward[i:]
            A, B = compose_affine(sub)
            if B_prev is not None:
                diff = B - B_prev
                Mn = sum(m for m, r in word_forward[i + 1:])
                if diff == 0:
                    bad += 1
                else:
                    num_v3 = v3(diff.numerator) or 0
                    den_v3 = v3(diff.denominator) or 0
                    if (num_v3 - den_v3) != Mn:
                        bad += 1
            B_prev = B
    return trials, bad


if __name__ == "__main__":
    print("== item 1: single-stratum exhaustive scan ==")
    n_buckets, bad_class, missing = test_single_stratum_exhaustive()
    print(f"{n_buckets} strata found, {bad_class} with non-unique residue, "
          f"missing (m,r) with m,r<=7: {missing}")

    print("== item 1: two-step exhaustive scan ==")
    n_words, bad_class2 = test_two_step_exhaustive()
    print(f"{n_words} length-2 words found, {bad_class2} with non-unique "
          f"residue")

    print("== item 1: single-stratum level-shift lemma ==")
    trials, bad = test_single_stratum_level_shift()
    print(f"{trials} checked, {bad} failures")

    print("== item 1: composed level-shift (induction step) ==")
    trials, bad = test_composed_level_shift()
    print(f"{trials} checked, {bad} failures")

    print("== item 1: completeness (a) and liveness (b) ==")
    trials, bad_a, bad_b = test_completeness_and_liveness()
    print(f"{trials} words; completeness failures: {bad_a}; "
          f"liveness failures: {bad_b}")

    print("== item 3(a): word injectivity ==")
    checked, bad = test_word_injectivity()
    print(f"{checked} distinct pairs checked, {bad} failures")

    print("== item 3(b): predecessor-door sanity ==")
    checked, bad, fallback_used = test_predecessor_sanity()
    print(f"{checked} checked ({fallback_used} used the a=1 fallback), "
          f"{bad} failures")

    print("== item 3(b): past determines the 3-adic coordinate ==")
    trials, skipped, checked, bad = test_past_determines_3adic()
    print(f"{trials} chains ({skipped} skipped: dead a=0 representative), "
          f"{checked} (chain,k) checks, {bad} failures")

    print("== item 3(b): offset sequence is 3-adically Cauchy (algebra) ==")
    trials, bad = test_offset_cauchy()
    print(f"{trials} checked, {bad} failures")
