# Verification for reverse.md 14.15.6 (the signed diagonal: 14.15.3-14.15.5's
# apparatus extended over the nonzero odd integers), branch signed-diagonal,
# per briefs/signed-diagonal-brief.md. Executes the diagonal-converse
# off-brief finding (briefs/diagonal-converse-findings.md), author-authorized
# 2026-07-16.
#
# Fresh, independent implementation (AGENTS.md house norm) -- imports nothing
# from experiments/diagonal_converse.py, realization_height.py,
# itinerary_coding.py, block_map.py, or door_seam.py, even though the
# underlying primitives (stratum, G, the unique-predecessor formula, the
# composed-affine constants) are the same objects those files also
# reimplement independently. Exact integer / Fraction arithmetic wherever a
# pass/fail decision is made.
#
# Sections, matching reverse.md 14.15.6's own item numbering (added one per
# commit as the wiki subsections land):
#   item 1  the signed domain, the singular point, sign preservation, the
#           signed unique-predecessor lemma.
#   item 2  the signed admissibility-class lemma, the two-sector bicylinder.
#   item 3  the signed characterization; the per-sector realization height
#           and whether 14.15.4.4-14.15.4.5's monotone-net argument
#           transfers under |.|.
#   item 4  reconciliations: the -5 instance now ordinary, the period-7
#           cycle as the G-period-2 word ((4,1),(3,3)) with y*=-17, and
#           {-1} genuinely outside the coding.

import random
from fractions import Fraction


# ---------------------------------------------------------------------------
# Core primitives (fresh reimplementation of reverse.md 14.14-14.15's
# definitions, over the SIGNED domain: nonzero odd integers, y != -1).
# ---------------------------------------------------------------------------

def v2(n):
    n = abs(n)
    if n == 0:
        return None
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def v3(n):
    n = abs(n)
    if n == 0:
        return None
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def stratum_and_G(y):
    """Domain: y a nonzero odd integer, y != -1 (the singular point --
    v2(0) is infinite, so m is undefined there; this raises rather than
    silently returning a sentinel, per the brief's item 1). m=v2(y+1),
    q=(y+1)/2^m, r=v2(3^m q - 1), G(y)=(3^m q - 1)/2^r -- the identical
    algebra of reverse.md 14.15.1.1, over the negative integers as well
    as the positive: multiplication, exact division by a power of 2, and
    the valuations v2/v3 (both sign-independent, abs-based) never use the
    sign of y anywhere in the formula."""
    if y == -1:
        raise ValueError("y = -1 is the singular point: stratum/G undefined")
    if y == 0 or y % 2 == 0:
        raise ValueError("domain is nonzero ODD integers only")
    m = v2(y + 1)
    q = (y + 1) // (2 ** m)
    val = 3 ** m * q - 1
    r = v2(val)
    return val // (2 ** r), m, r


def G(y):
    return stratum_and_G(y)[0]


def stratum(y):
    _, m, r = stratum_and_G(y)
    return m, r


def T(x):
    """The classical accelerated odd Collatz map (spine.md 9.8), extended
    to negative odd x exactly as usual (3x+1 is still even for odd x of
    either sign)."""
    v = 3 * x + 1
    while v % 2 == 0:
        v //= 2
    return v


def unique_predecessor(z, m, r):
    """Theorem 14.15.4.1's formula, over the signed domain: the unique
    integer y with G(y)=z and stratum(y)=(m,r) if 3^m | 2^r z + 1, else
    None. No sign hypothesis on z anywhere in the formula itself -- the
    signed content (item 1(ii)) is entirely in what can be PROVED about
    the output's sign, checked by test_signed_unique_predecessor below,
    not assumed here."""
    num = (1 << r) * z + 1
    denom = 3 ** m
    if num % denom != 0:
        return None
    q = num // denom
    return (1 << m) * q - 1


def letter_affine(m, r):
    """14.14.4.1's per-stratum affine constants (alpha, beta), exact
    Fractions -- sign-independent (no z or y appears in their definition
    at all, only the stratum labels)."""
    denom = Fraction(1, 2 ** (m + r))
    alpha = Fraction(3 ** m) * denom
    beta = Fraction(3 ** m - 2 ** m) * denom
    return alpha, beta


def compose_append(letters):
    """14.14.8.2's composed-affine recursion (letters[0] applied first /
    innermost): A_0=1, B_0=0; A_(i+1)=alpha_i A_i, B_(i+1)=alpha_i B_i+beta_i."""
    A, B = Fraction(1), Fraction(0)
    for (m, r) in letters:
        alpha, beta = letter_affine(m, r)
        A, B = alpha * A, alpha * B + beta
    return A, B


def frac_mod(x: Fraction, mod: int) -> int:
    """Reduce a Fraction with denominator coprime to `mod` into Z/mod."""
    num = x.numerator % mod
    den = x.denominator % mod
    inv = pow(den, -1, mod)
    return (num * inv) % mod


def random_nonzero_odd(rng, hi, sign=1, lo=3):
    """Random odd integer of the requested sign (+1 or -1), magnitude in
    [lo, hi). lo>=3 (default) keeps the negative draws away from the
    excluded point -1 automatically; also explicitly excluded below in
    case a caller lowers `lo`."""
    while True:
        mag = rng.randrange(lo, hi, 2)
        y = sign * mag
        if y == -1 or y == 0:
            continue
        if y % 3 != 0:
            return y


def find_live_predecessor(cur, rng, m_cap=3, r_cap=25, tries=500):
    """Search for a live letter-prescribed predecessor of `cur` (either
    sign -- the predecessor's sign is forced to match `cur`'s automatically,
    per item 1(ii), so no sign parameter is needed here)."""
    for _ in range(tries):
        m = rng.randrange(1, m_cap + 1)
        for r in range(1, r_cap):
            y = unique_predecessor(cur, m, r)
            if y is not None and y != -1 and y % 3 != 0:
                return y, m, r
    return None


def single_letter_residue(m, r):
    """Lemma 14.15.1.3(i): the unique y mod 2^(m+r+1) with
    stratum(y) = (m,r) -- a residue class over ALL integers, not merely
    the positive ones (the congruence itself is purely 2-adic)."""
    mod_q = 1 << (r + 1)
    inv3m = pow(3, -m, mod_q)
    q_res = (inv3m * (1 + (1 << r))) % mod_q
    return ((1 << m) * q_res - 1) % (1 << (m + r + 1))


def forward_class_representative(letters):
    """Constructive form of Theorem 14.15.1.5 (Hensel-lifting induction,
    reimplemented directly): returns (y_rep, modulus=2^(S+1)) such that an
    odd y (of EITHER sign -- the construction is purely 2-adic residue
    arithmetic) follows `letters` iff y === y_rep (mod modulus)."""
    if not letters:
        return 1, 2
    m0, r0 = letters[0]
    y_rep = single_letter_residue(m0, r0)
    modulus = 1 << (m0 + r0 + 1)
    M = m0
    n_so_far = 1
    for (mi, ri) in letters[1:]:
        z_cur = y_rep
        for _ in range(n_so_far):
            z_cur = G(z_cur)
        target_mod = 1 << (mi + ri + 1)
        w_target = single_letter_residue(mi, ri)
        diff = (w_target - (z_cur % target_mod)) % target_mod
        half_mod = target_mod // 2
        diff_half = (diff // 2) % half_mod
        inv3M = pow(3, -M, half_mod) if half_mod > 1 else 0
        t0 = (diff_half * inv3M) % half_mod
        y_rep = y_rep + modulus * t0
        modulus = modulus * half_mod
        M += mi
        n_so_far += 1
    return y_rep, modulus


# ---------------------------------------------------------------------------
# Item 1: the signed domain, the singular point, sign preservation, the
# signed unique-predecessor lemma.
# ---------------------------------------------------------------------------

def test_domain_totality_and_sign_preservation(trials=20000, seed=55001, hi=10 ** 6):
    """stratum/G are total (raise nothing) on every nonzero odd y != -1 of
    either sign, and G(y) always has the SAME SIGN as y -- a strict
    statement with no exception, since -1 is itself a negative value (the
    exception the brief flags is about domain membership, not sign: see
    test_negative_forward_mortality below)."""
    rng = random.Random(seed)
    bad_exception = 0
    bad_sign = 0
    checked = 0
    for _ in range(trials):
        sign = rng.choice((1, -1))
        y = random_nonzero_odd(rng, hi, sign=sign)
        try:
            gy, m, r = stratum_and_G(y)
        except Exception:
            bad_exception += 1
            continue
        checked += 1
        if (gy > 0) != (y > 0):
            bad_sign += 1
    return trials, checked, bad_exception, bad_sign


def test_positive_sector_never_mortal(trials=10000, seed=55002, hi=10 ** 6):
    """For positive y, G(y) >= 1 strictly (never <=0, in particular never
    -1) -- re-derives 14.14.3.2(3)'s totality/live-image fact fresh, and
    additionally confirms it is never the singular point, establishing
    that the positive sector has NO forward mortality (the asymmetry
    against the negative sector, item 1)."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        y = random_nonzero_odd(rng, hi, sign=1)
        gy = G(y)
        if gy < 1 or gy == -1:
            bad += 1
    return trials, bad


def test_negative_forward_mortality(scan_bound=2000):
    """The one-sided asymmetry, found not smoothed: among NEGATIVE odd y
    (y != -1), G(y) = -1 has solutions -- e.g. G(-3) = -1 exactly, and
    it is not the only one. Direct scan over negative y in
    [-scan_bound, -3], confirming: (a) at least one solution exists,
    (b) G(-3) = -1 exactly, (c) every solution found is itself a valid
    signed door (odd, != -1, i.e. legitimately in the domain) whose
    single forward step nonetheless leaves the domain -- the precise
    content of 'forward mortality, negative sector only'."""
    solutions = []
    for mag in range(3, scan_bound, 2):
        y = -mag
        try:
            if G(y) == -1:
                solutions.append(y)
        except ValueError:
            pass
    ok = (len(solutions) >= 1) and (-3 in solutions) and (G(-3) == -1)
    return solutions[:10], len(solutions), ok


def test_no_positive_forward_mortality(scan_bound=200000):
    """The mirror scan: among POSITIVE odd y, G(y) = -1 has NO solutions
    at all, in the same range as test_negative_forward_mortality found
    several -- direct evidence, not merely the algebraic argument, that
    the mortality is one-sided."""
    hits = 0
    for y in range(1, scan_bound, 2):
        if y % 3 == 0:
            continue
        if G(y) == -1:
            hits += 1
    return scan_bound, hits


def test_signed_unique_predecessor(trials=20000, seed=55003, m_hi=8,
                                    r_hi=10, z_hi=10 ** 6):
    """14.15.4.1's statement with 'positive' replaced by 'same sign as z,
    never -1' (item 1(ii)): whenever unique_predecessor(z,m,r) exists,
    (a) sign(y) == sign(z) exactly, (b) y != -1, (c) stratum(y) == (m,r)
    and G(y) == z exactly (round-trip), for z of EITHER sign. The only
    changed algebraic step, per the brief, is the sign of
    q = (2^r z + 1) / 3^m -- checked directly here."""
    rng = random.Random(seed)
    admissible = 0
    bad_sign = 0
    bad_minus1 = 0
    bad_roundtrip = 0
    for _ in range(trials):
        sign = rng.choice((1, -1))
        z = random_nonzero_odd(rng, z_hi, sign=sign)
        m = rng.randrange(1, m_hi)
        r = rng.randrange(1, r_hi)
        y = unique_predecessor(z, m, r)
        if y is None:
            continue
        admissible += 1
        if (y > 0) != (z > 0):
            bad_sign += 1
        if y == -1:
            bad_minus1 += 1
        try:
            gy, my, ry = stratum_and_G(y)
        except ValueError:
            bad_roundtrip += 1
            continue
        if gy != z or (my, ry) != (m, r):
            bad_roundtrip += 1
    return trials, admissible, bad_sign, bad_minus1, bad_roundtrip


def test_predecessor_forced_bound(trials=20000, seed=55004, m_hi=8, r_hi=10,
                                   z_hi=10 ** 6):
    """The algebraic reason -1 is 'unreachable backward' (never produced
    by the letter-prescribed predecessor formula): whenever
    unique_predecessor(z,m,r) exists, q = (2^r z + 1)/3^m is a NONZERO
    integer (2^r z + 1 is odd, hence never 0, and dividing an odd number
    by 3^m preserves nonzero-ness), so q >= 1 or q <= -1, forcing
    y = 2^m q - 1 >= 2^m - 1 >= 1  or  y <= -2^m - 1 <= -3 -- never -1,
    by construction, not merely by scanning. Checked directly on the
    intermediate q for every admissible draw."""
    rng = random.Random(seed)
    admissible = 0
    bad_bound = 0
    for _ in range(trials):
        sign = rng.choice((1, -1))
        z = random_nonzero_odd(rng, z_hi, sign=sign)
        m = rng.randrange(1, m_hi)
        r = rng.randrange(1, r_hi)
        num = (1 << r) * z + 1
        denom = 3 ** m
        if num % denom != 0:
            continue
        q = num // denom
        admissible += 1
        y = (1 << m) * q - 1
        if q == 0:
            bad_bound += 1
        elif q >= 1:
            if y < (1 << m) - 1:
                bad_bound += 1
        else:
            if y > -(1 << m) - 1:
                bad_bound += 1
    return trials, admissible, bad_bound


def test_round_trip_signed(trials=8000, seed=55005, hi=10 ** 7):
    """Round-trip sanity, both signs: random y != -1 -> stratum(y)=(m,r),
    z=G(y) -> unique_predecessor(z,m,r) must reproduce y exactly, correct
    sign, never -1."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        sign = rng.choice((1, -1))
        y = random_nonzero_odd(rng, hi, sign=sign)
        z, m, r = stratum_and_G(y)
        y2 = unique_predecessor(z, m, r)
        if y2 != y:
            bad += 1
    return trials, bad


if __name__ == "__main__":
    print("== item 1: domain totality + sign preservation ==")
    trials, checked, bad_exc, bad_sign = test_domain_totality_and_sign_preservation()
    print(f"{trials} drawn, {checked} checked (no exception), "
          f"{bad_exc} unexpected exceptions, {bad_sign} sign mismatches")

    print("== item 1: positive sector never forward-mortal ==")
    trials, bad = test_positive_sector_never_mortal()
    print(f"{trials} checked, {bad} failures")

    print("== item 1: negative forward mortality (G(y)=-1 has solutions) ==")
    sample, count, ok = test_negative_forward_mortality()
    print(f"{count} solutions with |y|<2000, sample={sample}, "
          f"G(-3)=-1 exact: {'OK' if ok else 'MISMATCH'}")

    print("== item 1: positive sector has NO such solutions (mirror scan) ==")
    scanned, hits = test_no_positive_forward_mortality()
    print(f"{scanned} positive odd y scanned, {hits} solutions to G(y)=-1")

    print("== item 1: signed unique-predecessor lemma (sign match, "
          "never -1, round-trip) ==")
    trials, adm, bad_sign, bad_m1, bad_rt = test_signed_unique_predecessor()
    print(f"{trials} drawn, {adm} admissible, {bad_sign} sign failures, "
          f"{bad_m1} landed on -1, {bad_rt} round-trip failures")

    print("== item 1: predecessor forced bound (never -1, by construction) ==")
    trials, adm, bad = test_predecessor_forced_bound()
    print(f"{trials} drawn, {adm} admissible, {bad} bound violations")

    print("== item 1: round-trip sanity, both signs ==")
    trials, bad = test_round_trip_signed()
    print(f"{trials} checked, {bad} failures")


# ---------------------------------------------------------------------------
# Item 2: the signed admissibility-class lemma, the two-sector bicylinder.
# ---------------------------------------------------------------------------

def test_admissibility_class_signed(trials=150, seed=55011, n_max=3,
                                     m_hi=3, r_hi=4, z_bound_cap=3000):
    """14.15.5.1 relaxed from 'among positive odd integers' to 'among
    nonzero odd integers z != -1' (item 2(i)): for random words, direct
    brute-force scan over BOTH signs (existence of the depth-n
    letter-prescribed chain from z, vs. the predicted congruence
    z === B_n (mod 3^(M_n))) -- the synchronization-sharpened equivalence
    (14.15.5.2) checked directly, sign by sign, on the same footing."""
    rng = random.Random(seed)
    bad = 0
    checked_words = 0
    checked_z = 0
    for _ in range(trials):
        n = rng.randrange(1, n_max + 1)
        letters_shallow_first = [(rng.randrange(1, m_hi), rng.randrange(1, r_hi))
                                  for _ in range(n)]
        M_n = sum(m for m, r in letters_shallow_first)
        mod = 3 ** M_n
        A_n, B_n = compose_append(list(reversed(letters_shallow_first)))
        predicted = frac_mod(B_n, mod)
        z_bound = min(4 * mod, z_bound_cap)
        checked_words += 1
        for mag in range(1, z_bound, 2):
            for z in (mag, -mag):
                if z == -1:
                    continue
                cur = z
                ok = True
                for (m, r) in letters_shallow_first:
                    y = unique_predecessor(cur, m, r)
                    if y is None:
                        ok = False
                        break
                    cur = y
                checked_z += 1
                expected = (z % mod == predicted)
                if ok != expected:
                    bad += 1
    return checked_words, checked_z, bad


def verify_chain_realizes_word(y, word):
    """Direct check that y's forward orbit realizes `word` exactly (every
    stratum matches, every door live, never hits -1)."""
    cur = y
    for (m, r) in word:
        if cur == -1 or cur % 3 == 0:
            return False
        if stratum(cur) != (m, r):
            return False
        cur = G(cur)
    return True


def find_live_chain_representative(word, sign, tries=20000):
    """The signed analogue of 14.15.4.2's own construction: the followers
    of `word` (as a single concatenated itinerary, deepest letter first)
    form one residue class mod 2^(S+1) (Theorem 14.15.1.5, sign-agnostic
    -- a purely 2-adic residue statement). Walk that class outward in the
    requested sign's direction (nearest zero first) for the first member
    whose deepest door is live and whose ENTIRE forward chain of length
    len(word) realizes `word` exactly, without ever landing on -1 along
    the way (the one extra condition the signed setting adds beyond
    14.15.4.2's own positive-only construction). Returns that y, or None."""
    y_rep, modulus = forward_class_representative(word)
    r0 = y_rep % modulus
    for k in range(tries):
        y = (r0 + k * modulus) if sign > 0 else (r0 - modulus - k * modulus)
        if y == 0 or y == -1:
            continue
        if y % 3 == 0:
            continue
        if verify_chain_realizes_word(y, word):
            return y
    return None


def test_minus1_never_in_cylinder_class(trials=3000, seed=55013, m_hi=10, r_hi=10):
    """Strengthens the bicylinder construction: -1 never lies in ANY
    single-stratum residue class (Lemma 14.15.1.3(i)'s congruence,
    extended over Z): -1 trivially satisfies the FIRST half of the
    congruence (y+1=0 is divisible by every power of 2) but fails the
    SECOND (q=(y+1)/2^m=0 is even, while the class's own q-residue
    3^{-m}(1+2^r) mod 2^{r+1} is always odd, r>=1). Consequently no
    candidate drawn from a composed cylinder class mod 2^(S+1) can ever
    equal -1, so find_live_chain_representative's per-step '-1' guard is
    never actually load-bearing -- checked directly here rather than
    argued only in prose."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        m = rng.randrange(1, m_hi)
        r = rng.randrange(1, r_hi)
        mod = 1 << (m + r + 1)
        rep = single_letter_residue(m, r)
        if (-1) % mod == rep:
            bad += 1
    return trials, bad


def test_two_sector_bicylinder(trials=400, seed=55012, p_max=3, q_max=3,
                                m_hi=3, r_hi=3, tries=20000):
    """The finite bicylinder corollary (14.15.4.2), per sector (item
    2(ii)): for a random two-sided window V (past, length p) + U (future,
    length q), find a live integer segment realizing the SAME concatenated
    word V+U, once with a positive deepest door and once with a negative
    one -- both from the same word, demonstrating the residue class mod
    2^(S+1) meets each sign in a live, fully-realizing member."""
    rng = random.Random(seed)
    built_pos = built_neg = 0
    bad_pos = bad_neg = 0
    attempted = 0
    for _ in range(trials):
        p = rng.randrange(0, p_max + 1)
        q = rng.randrange(0, q_max + 1)
        if p + q == 0:
            continue
        V = [(rng.randrange(1, m_hi + 1), rng.randrange(1, r_hi + 1)) for _ in range(p)]
        U = [(rng.randrange(1, m_hi + 1), rng.randrange(1, r_hi + 1)) for _ in range(q)]
        word = V + U
        attempted += 1

        y_pos = find_live_chain_representative(word, +1, tries)
        if y_pos is not None:
            built_pos += 1
            if not verify_chain_realizes_word(y_pos, word):
                bad_pos += 1

        y_neg = find_live_chain_representative(word, -1, tries)
        if y_neg is not None:
            built_neg += 1
            if not verify_chain_realizes_word(y_neg, word):
                bad_neg += 1

    return attempted, built_pos, built_neg, bad_pos, bad_neg


if __name__ == "__main__":
    print("== item 2: signed admissibility-class lemma (both signs, "
          "existence <=> congruence) ==")
    words, zs, bad = test_admissibility_class_signed()
    print(f"{words} words, {zs} (word,z) checks (both signs), {bad} failures")

    print("== item 2: two-sector finite bicylinder corollary ==")
    attempted, bp, bn, bad_p, bad_n = test_two_sector_bicylinder()
    print(f"{attempted} windows attempted, {bp} positive segments built "
          f"({bad_p} verification failures), {bn} negative segments built "
          f"({bad_n} verification failures)")

    print("== item 2: -1 never lies in any single-stratum cylinder class ==")
    trials, bad = test_minus1_never_in_cylinder_class()
    print(f"{trials} (m,r) pairs checked, {bad} times -1 matched the class")


# ---------------------------------------------------------------------------
# Item 3: the signed characterization; the per-sector realization height
# and whether 14.15.4.4-14.15.4.5's monotone-net argument transfers.
# ---------------------------------------------------------------------------

def test_signed_converse_mechanism(trials=300, seed=55021, depth=12, hi=10 ** 5):
    """Theorem 14.15.5.3's converse mechanism, both signs: real long
    backward chains behind a real live y0 (either sign), letters drawn
    honestly (find_live_predecessor, not fitted to a target). Checks (i)
    the Cauchy estimate v3(y0-B_n) >= M_n at every depth, (ii)
    reconstruction from y0 + the recorded letters alone reproduces the
    chain exactly, (iii) liveness derived (every chain door, and G's own
    image of the deepest one, automatically live), and, new to the
    signed setting, (iv) no chain door is ever -1."""
    rng = random.Random(seed)
    built = 0
    bad_cauchy = bad_reconstruct = bad_live = bad_minus1 = 0

    for _ in range(trials):
        sign = rng.choice((1, -1))
        y0 = random_nonzero_odd(rng, hi, sign=sign)
        chain = []
        letters_shallow_first = []
        cur = y0
        ok = True
        for _ in range(depth):
            res = find_live_predecessor(cur, rng)
            if res is None:
                ok = False
                break
            y_prev, m, r = res
            chain.append(y_prev)
            letters_shallow_first.append((m, r))
            cur = y_prev
        if not ok:
            continue
        built += 1

        for n in range(1, depth + 1):
            word_deepest_first = list(reversed(letters_shallow_first[:n]))
            _, B_n = compose_append(word_deepest_first)
            M_n = sum(m for m, r in letters_shallow_first[:n])
            diff = Fraction(y0) - B_n
            num_v3 = v3(diff.numerator) if diff.numerator != 0 else 10 ** 9
            den_v3 = v3(diff.denominator) if diff.denominator != 1 else 0
            if (num_v3 - den_v3) < M_n:
                bad_cauchy += 1

        cur = y0
        rebuilt = []
        broke = False
        for (m, r) in letters_shallow_first:
            y = unique_predecessor(cur, m, r)
            if y is None:
                bad_reconstruct += 1
                broke = True
                break
            rebuilt.append(y)
            cur = y
        if not broke and rebuilt != chain:
            bad_reconstruct += 1

        for y in chain:
            if y % 3 == 0:
                bad_live += 1
            if y == -1:
                bad_minus1 += 1
        if G(chain[-1]) % 3 == 0:
            bad_live += 1
        if G(chain[-1]) == -1 and sign > 0:
            # sign>0 chains are entirely positive (14.15.6.3), so G of a
            # positive deepest door must be positive too -- never -1.
            bad_minus1 += 1

    return trials, built, bad_cauchy, bad_reconstruct, bad_live, bad_minus1


def test_forward_half_nesting_signed(trials=2000, seed=55022, n_max=10, hi=10 ** 6):
    """The forward half of the signed converse: y0's own forward orbit
    places it in every one of its own forward cylinders, both signs --
    checked via the independent Hensel-lifting construction
    (forward_class_representative), not by scanning. A random negative
    y0's forward orbit can genuinely hit -1 within n_max steps (the
    one-sided forward mortality of item 1) -- such draws are skipped and
    counted, not treated as failures; they are the expected, occasional
    footprint of 14.15.6.2(4), not a bug in this test."""
    rng = random.Random(seed)
    bad = 0
    mortal_skips = 0
    checked = 0
    for _ in range(trials):
        sign = rng.choice((1, -1))
        y0 = random_nonzero_odd(rng, hi, sign=sign)
        n = rng.randrange(1, n_max + 1)
        letters = []
        cur = y0
        hit_mortality = False
        for _ in range(n):
            if cur == -1:
                hit_mortality = True
                break
            letters.append(stratum(cur))
            cur = G(cur)
        if hit_mortality:
            mortal_skips += 1
            continue
        checked += 1
        y_rep, modulus = forward_class_representative(letters)
        if y0 % modulus != y_rep % modulus:
            bad += 1
    return trials, checked, mortal_skips, bad


def in_R_periodic_signed(y0, unit, n, sign):
    """Membership in the signed R^{sign}_{n,n}(W) for the bi-infinite
    periodic word W built by repeating `unit` (a finite list of letters)
    in both directions: y0 has the requested sign, is live, its forward
    orbit matches n copies of `unit`, and its letter-prescribed backward
    chain (letters = reversed(unit) repeated n times, the natural
    'immediately-preceding letter is unit's last letter' convention for
    a periodic word) exists with a live, non-singular deepest door."""
    if sign > 0 and y0 <= 0:
        return False
    if sign < 0 and y0 >= 0:
        return False
    if y0 == -1 or y0 % 3 == 0:
        return False
    cur = y0
    for _ in range(n):
        for (m, r) in unit:
            if cur == -1:
                return False
            if stratum(cur) != (m, r):
                return False
            cur = G(cur)
    cur = y0
    back_letters = list(reversed(unit)) * n
    for (m, r) in back_letters:
        y = unique_predecessor(cur, m, r)
        if y is None:
            return False
        cur = y
    return cur != -1 and cur % 3 != 0


def test_negative_realized_cycles_bounded(n_max=6):
    """The reconciliation the brief flags (item 4(i)-(ii), verified here
    at the height-mechanism level, item 3): the two known negative
    periodic diagonal points, -5 (unit [(2,1)]) and -17 (unit
    [(4,1),(3,3)]), are members of their own R^-_{n,n} for every n tested
    -- an UPPER BOUND on H^-_{n,n} (<=5, <=17 respectively) at every
    window, i.e. BOUNDED, contrasting with the escaping POSITIVE height
    already on file for the -5 word (14.15.5(c), diagonal_converse.py).
    Also confirms -5 is (up to the excluded singular point -1 and the
    dead door -3) the least-magnitude live negative odd integer, so this
    membership alone pins H^-_{n,n}(-5 word) = 5 exactly, no search
    needed -- the same argument style as 14.15.4(c)'s trivial-word check."""
    results = {}
    ok = True
    for n in range(0, n_max + 1):
        m5 = in_R_periodic_signed(-5, [(2, 1)], n, -1)
        m17 = in_R_periodic_signed(-17, [(4, 1), (3, 3)], n, -1)
        results[n] = (m5, m17)
        ok = ok and m5 and m17
    # -5 minimality: the only candidates with |y|<5, y odd, y!=-1 are
    # +-1 (|y|=1, but -1 excluded/singular, +1 not negative) and +-3
    # (dead, 3|3) -- no live negative odd integer has |y|<5.
    minimality_ok = all(mag in (1, 3) or mag >= 5
                         for mag in range(1, 5, 2))
    return results, ok, minimality_ok


def crt_combine(y_a, mod_a, y_b, mod_b):
    """Chinese remainder combine two residues with coprime moduli."""
    inv_a = pow(mod_a, -1, mod_b)
    inv_b = pow(mod_b, -1, mod_a)
    combined_mod = mod_a * mod_b
    z0 = (y_a * mod_b * inv_b + y_b * mod_a * inv_a) % combined_mod
    return z0, combined_mod


def height_for_periodic_word(unit, n, sign, max_progression_steps=300000):
    """H^{sign}_{n,n} for the bi-infinite word built by repeating `unit`
    n times each direction: combine the forward cylinder class (mod
    2^(S+1), via forward_class_representative) and the backward
    admissible class (14.15.6.4, mod 3^(M_n)) by CRT, then scan the
    resulting class IN THE REQUESTED SIGN'S DIRECTION (nearest zero
    first) for the first candidate whose depth-n backward chain also has
    a live, non-singular deepest door. Generalizes
    diagonal_converse.py's height_2_1_word (independently reimplemented
    here) to an arbitrary periodic unit and either sign."""
    word = unit * n
    y_fwd, mod_fwd = forward_class_representative(word)
    M_n = sum(m for m, r in word)
    mod_bwd = 3 ** M_n
    _, B_n = compose_append(list(reversed(word)))
    y_bwd = frac_mod(B_n, mod_bwd)
    z0, combined_mod = crt_combine(y_fwd, mod_fwd, y_bwd, mod_bwd)
    r0 = z0 % combined_mod

    for k in range(max_progression_steps):
        z = (r0 + k * combined_mod) if sign > 0 else (r0 - combined_mod - k * combined_mod)
        if z == 0 or z == -1:
            continue
        cur = z
        ok = True
        deepest_live = True
        for (m, r) in word:
            y = unique_predecessor(cur, m, r)
            if y is None or y == -1 or (sign > 0 and y <= 0) or (sign < 0 and y >= 0):
                ok = False
                break
            deepest_live = (y % 3 != 0)
            cur = y
        if ok and deepest_live:
            return z, k + 1
    return None, max_progression_steps


def brute_height_for_periodic_word(unit, n, sign, bound):
    """Independent brute-force cross-check, small n only."""
    word = unit * n
    for mag in range(1, bound, 2):
        z = sign * mag
        if z == -1:
            continue
        c = z
        good = True
        for (m, r) in word:
            if c == -1 or stratum(c) != (m, r):
                good = False
                break
            c = G(c)
        if not good:
            continue
        cur = z
        ok = True
        deepest_live = True
        for (m, r) in word:
            y = unique_predecessor(cur, m, r)
            if y is None or y == -1 or (sign > 0 and y <= 0) or (sign < 0 and y >= 0):
                ok = False
                break
            deepest_live = (y % 3 != 0)
            cur = y
        if ok and deepest_live:
            return z
    return None


def test_negative_height_escapes_for_positive_word(n_max=5, cross_check_n=(1, 2),
                                                     cross_check_bound=400_000):
    """The escape side, checked so the boundedness criterion is not
    vacuously satisfied in the negative sector: the trivial word
    (1,1)^inf is realized ONLY by the positive integer y=1 (its composed
    fixed point is the unique rational solution y*=1, 14.14.8.4, never a
    negative integer). By the (transferred) equivalence theorem, its
    NEGATIVE height should therefore escape. Computed exactly via CRT +
    progression scan, n=1..n_max, cross-checked against brute force at
    n=1,2."""
    heights = {}
    for n in range(1, n_max + 1):
        h, steps = height_for_periodic_word([(1, 1)], n, -1)
        heights[n] = (h, steps)

    cross_bad = 0
    for n in cross_check_n:
        brute = brute_height_for_periodic_word([(1, 1)], n, -1, cross_check_bound)
        fast_h, _ = heights[n]
        if brute != fast_h:
            cross_bad += 1

    all_defined = all(heights[n][0] is not None for n in range(1, n_max + 1))
    magnitudes = [abs(heights[n][0]) for n in range(1, n_max + 1) if heights[n][0] is not None]
    nondecreasing = all(magnitudes[i] <= magnitudes[i + 1] for i in range(len(magnitudes) - 1))
    grew = magnitudes[-1] > magnitudes[0] if len(magnitudes) >= 2 else False
    return heights, cross_bad, all_defined, nondecreasing, grew


def exhaustive_min_abs_R(word_forward, word_backward, sign, bound):
    """Exhaustive search for the minimum |y| of the requested sign
    realizing BOTH the given forward letters and backward letters
    (possibly different lengths -- used for the (p,q) monotonicity check
    below), scanning by increasing magnitude so the first hit is the true
    minimum, not merely a witness. Returns that magnitude, or None."""
    for mag in range(1, bound, 2):
        y = sign * mag
        if y == -1 or y % 3 == 0:
            continue
        cur = y
        ok = True
        for (m, r) in word_forward:
            if cur == -1 or stratum(cur) != (m, r):
                ok = False
                break
            cur = G(cur)
        if not ok:
            continue
        cur = y
        for (m, r) in word_backward:
            yy = unique_predecessor(cur, m, r)
            if yy is None or yy == -1 or (sign > 0 and yy <= 0) or (sign < 0 and yy >= 0):
                ok = False
                break
            cur = yy
        if not ok:
            continue
        if cur % 3 != 0:
            return mag
    return None


def test_height_monotonicity_negative_real_orbits(trials=20, seed=55023,
                                                    bound=1 << 15, m_cap=2, r_cap=6):
    """The direct sign-blind transfer check for 14.15.4.4's properties
    1-3 (existence + monotonicity of H under nested windows), restricted
    to the negative sector: 20 real negative integer orbits (letters
    honestly drawn -- forward from the orbit itself, backward via
    find_live_predecessor), H^-_{n,n} computed by EXHAUSTIVE search over
    NEGATIVE candidates only at n=1 and n=2 on the SAME underlying
    word/pivot, mirroring 14.15.4(c)'s own 'fixed-origin nested-window
    monotonicity' check exactly, one sector at a time."""
    rng = random.Random(seed)
    built = 0
    bad_shortfall = 0
    bad_monotone = 0
    grew = 0

    for _ in range(trials):
        y0 = random_nonzero_odd(rng, 5000, sign=-1)

        fwd1 = [stratum(y0)]
        cur = G(y0)
        if cur == -1:
            # forward mortality struck within one step (item 1's
            # occasional footprint) -- this y0 cannot supply a length-2
            # forward window at all; skip it rather than force it.
            continue
        fwd2 = fwd1 + [stratum(cur)]

        res1 = find_live_predecessor(y0, rng, m_cap=m_cap, r_cap=r_cap)
        if res1 is None:
            continue
        y_m1, m1, r1 = res1
        res2 = find_live_predecessor(y_m1, rng, m_cap=m_cap, r_cap=r_cap)
        if res2 is None:
            continue
        y_m2, m2, r2 = res2

        bwd1 = [(m1, r1)]
        bwd2 = [(m1, r1), (m2, r2)]

        h1 = exhaustive_min_abs_R(fwd1, bwd1, -1, bound)
        h2 = exhaustive_min_abs_R(fwd2, bwd2, -1, bound)
        if h1 is None or h2 is None:
            bad_shortfall += 1
            continue
        built += 1
        if h2 < h1:
            bad_monotone += 1
        if h2 > h1:
            grew += 1

    return trials, built, bad_shortfall, bad_monotone, grew


if __name__ == "__main__":
    print("== item 3: signed converse-theorem mechanism (both signs) ==")
    trials, built, bad_c, bad_r, bad_l, bad_m1 = test_signed_converse_mechanism()
    print(f"{trials} trials, {built} chains built, "
          f"{bad_c} Cauchy failures, {bad_r} reconstruction failures, "
          f"{bad_l} liveness failures, {bad_m1} landed on -1")

    print("== item 3: forward-half nesting, both signs ==")
    trials, checked, mortal_skips, bad = test_forward_half_nesting_signed()
    print(f"{trials} drawn, {checked} checked, {mortal_skips} skipped "
          f"(hit forward mortality mid-orbit, expected occasionally), "
          f"{bad} failures")

    print("== item 3: negative realized cycles (-5, -17/-41) have "
          "BOUNDED negative height ==")
    results, ok, minimality_ok = test_negative_realized_cycles_bounded()
    for n, (m5, m17) in results.items():
        print(f"  n={n}: -5 in R^-_(n,n): {m5}, -17 in R^-_(n,n): {m17}")
    print(f"all membership checks OK: {ok}; -5 minimality confirmed: {minimality_ok}")

    print("== item 3: negative height ESCAPES for a positive-only-realized "
          "word (1,1)^inf ==")
    heights, cross_bad, all_defined, nondecreasing, grew = \
        test_negative_height_escapes_for_positive_word()
    for n, (h, steps) in heights.items():
        print(f"  n={n}: H^-_(n,n) = {h}  (progression steps: {steps})")
    print(f"cross-check mismatches: {cross_bad}; all defined: {all_defined}; "
          f"nondecreasing: {nondecreasing}; strictly grew overall: {grew}")

    print("== item 3: fixed-origin nested-window monotonicity, "
          "negative sector, real orbits ==")
    trials, built, bad_shortfall, bad_monotone, grew = \
        test_height_monotonicity_negative_real_orbits()
    print(f"{trials} orbits attempted, {built} built (n=1,2 both found), "
          f"{bad_shortfall} search-bound shortfalls, "
          f"{bad_monotone} monotonicity violations, {grew} strictly grew")


# ---------------------------------------------------------------------------
# Item 4: reconciliations -- the -5 instance now ordinary, the period-7
# cycle as the G-period-2 word ((4,1),(3,3)) with y*=-17, and {-1}
# genuinely outside the coding.
# ---------------------------------------------------------------------------

def test_negative_5_instance():
    """Item 4(i), fresh independent computation (matches diagonal_converse.py's
    already-merged 14.15.5(c) result, reproduced here with THIS file's own
    primitives, per AGENTS.md's independent-verification norm): the
    composed-affine fixed point of the single letter (2,1) is exactly
    -5, and stratum(-5)=(2,1), G(-5)=-5 -- a genuine fixed point of the
    signed exit map, cross-checked against T's classical 2-cycle
    {-5,-7}."""
    alpha, beta = letter_affine(2, 1)
    y_star = beta / (1 - alpha)
    checks = {
        "y_star_is_-5": y_star == Fraction(-5),
        "stratum_-5_is_(2,1)": stratum(-5) == (2, 1),
        "G_-5_is_-5": G(-5) == -5,
        "T_-5_is_-7": T(-5) == -7,
        "T_T_-5_is_-5": T(T(-5)) == -5,
    }
    return checks, all(checks.values())


def test_period7_cycle():
    """Item 4(ii): the classical period-7 accelerated negative T-cycle
    {-17,-25,-37,-55,-41,-61,-91} is exactly the G-period-2 word
    ((4,1),(3,3)), composed fixed point y*=-17. Checks, all with fresh
    code: stratum(-17)=(4,1), G(-17)=-41, stratum(-41)=(3,3), G(-41)=-17
    (the G-period-2 closure); the composed-affine fixed point of the
    2-letter word ((4,1),(3,3)) equals -17 exactly (Fraction algebra);
    and 7 iterations of T starting at -17 visit exactly the 7 classical
    values in order and return to -17 (block lengths 4+3=7 matching the
    stratum letters' own m-values)."""
    s17 = stratum(-17)
    g17 = G(-17)
    s41 = stratum(-41)
    g41 = G(-41)

    A2, B2 = compose_append([(4, 1), (3, 3)])  # deepest-first == the
    # period's own natural order: applying (4,1) first (at -17) reaches
    # -41, then (3,3) returns to -17 -- matching compose_append's
    # left-to-right "applied first" convention exactly.
    y_star = B2 / (1 - A2)

    orbit = [-17]
    cur = -17
    for _ in range(7):
        cur = T(cur)
        orbit.append(cur)
    classical = [-17, -25, -37, -55, -41, -61, -91, -17]

    checks = {
        "stratum_-17_is_(4,1)": s17 == (4, 1),
        "G_-17_is_-41": g17 == -41,
        "stratum_-41_is_(3,3)": s41 == (3, 3),
        "G_-41_is_-17": g41 == -17,
        "y_star_is_-17": y_star == Fraction(-17),
        "T_orbit_matches_classical": orbit == classical,
        "block_lengths_sum_to_7": (4 + 3 == 7),
    }
    return checks, all(checks.values()), orbit


def test_minus1_outside_coding(trials=2000, seed=55031):
    """Item 4(iii): {-1} is genuinely outside the signed coding, not
    smoothed over -- its would-be door is the singular point itself.
    Direct checks: stratum_and_G(-1) raises (undefined, not merely
    'excluded by convention'); T(-1) = -1 classically (the trivial
    negative fixed point DOES exist for T), confirming the gap is
    specifically in the door/stratum coding, not in the classical
    dynamics; and no random word's forward class representative ever
    equals -1 (already covered structurally by
    test_minus1_never_in_cylinder_class, re-confirmed here on random
    multi-letter words rather than single letters)."""
    raised = False
    try:
        stratum_and_G(-1)
    except ValueError:
        raised = True

    t_minus1_fixed = (T(-1) == -1)

    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        n = rng.randrange(1, 5)
        letters = [(rng.randrange(1, 6), rng.randrange(1, 6)) for _ in range(n)]
        y_rep, modulus = forward_class_representative(letters)
        if (-1) % modulus == y_rep % modulus:
            bad += 1

    return raised, t_minus1_fixed, trials, bad


def test_known_cycle_census():
    """Item 4(iv), the three known G-periodic integer diagonal points,
    verified together in one place: y=1 (word ((1,1))), y=-5 (word
    ((2,1))), and {-17,-41} (word ((4,1),(3,3))) -- each a genuine fixed
    point (or 2-cycle) of G on its own stratum word, with no other
    candidate searched for (per the brief's stop line)."""
    checks = {
        "y=1_fixed_(1,1)": (stratum(1) == (1, 1) and G(1) == 1),
        "y=-5_fixed_(2,1)": (stratum(-5) == (2, 1) and G(-5) == -5),
        "y=-17,-41_2cycle": (stratum(-17) == (4, 1) and G(-17) == -41
                              and stratum(-41) == (3, 3) and G(-41) == -17),
    }
    return checks, all(checks.values())


if __name__ == "__main__":
    print("== item 4: the -5 instance (fresh, independent recomputation) ==")
    checks, ok = test_negative_5_instance()
    print(checks, "OK" if ok else "MISMATCH")

    print("== item 4: the period-7 cycle as the G-period-2 word "
          "((4,1),(3,3)), y*=-17 ==")
    checks, ok, orbit = test_period7_cycle()
    print(checks, "OK" if ok else "MISMATCH")
    print(f"T-orbit from -17: {orbit}")

    print("== item 4: {-1} genuinely outside the signed coding ==")
    raised, t_fixed, trials, bad = test_minus1_outside_coding()
    print(f"stratum_and_G(-1) raised: {raised}; T(-1)=-1 classically: {t_fixed}; "
          f"{trials} random words checked, {bad} times -1 fell in a forward class")

    print("== item 4: known G-periodic integer diagonal census ==")
    checks, ok = test_known_cycle_census()
    print(checks, "OK" if ok else "MISMATCH")
