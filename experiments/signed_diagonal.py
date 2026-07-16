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
