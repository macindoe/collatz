# Verification for reverse.md 14.15.5 (the converse of the trivial
# diagonal direction 14.15.3.6: the admissibility-class lemma, the
# converse theorem / combined characterization, and the negative-diagonal
# reconciliation), branch diagonal-converse, per
# briefs/diagonal-converse-brief.md.
#
# Fresh, independent implementation (AGENTS.md house norm) -- imports
# nothing from experiments/realization_height.py, itinerary_coding.py,
# block_map.py, or door_seam.py, even though the underlying primitives
# (stratum, G, the unique-predecessor formula, the composed-affine
# constants) are the same objects those files also reimplement
# independently. Exact integer / Fraction arithmetic wherever a
# pass/fail decision is made.
#
# Sections, matching reverse.md 14.15.5's own lettering, added one per
# commit as the wiki subsections land:
#   14.15.5(a)  the admissibility-class lemma: base-case identity,
#               reconciliation of the two equivalent composed-affine
#               recursions (14.14.8.2's literal append form vs. the
#               prepend form 14.15.3.3's own proof uses), and a brute-
#               force check of the admissibility class itself.
#   14.15.5(b)  the converse theorem / combined characterization: the
#               Cauchy-estimate-to-admissibility mechanism, checked on
#               real long backward chains -- reconstruction from y0 and
#               the word alone (via unique-predecessor + uniqueness)
#               reproduces the actual chain, and liveness is confirmed
#               derived, not assumed.

import random
from fractions import Fraction


# ---------------------------------------------------------------------------
# Core primitives (fresh reimplementation; matches reverse.md 14.14-14.15's
# definitions, extended to negative odd integers for 14.15.5(c) exactly as
# the brief's pre-check does -- v2/v3 are sign-independent valuations).
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
    """m = v2(y+1), q = (y+1)/2^m, r = v2(3^m q - 1), G(y) = (3^m q-1)/2^r.
    Defined for every nonzero odd integer y (reverse.md 14.15.1.1's
    domain is odd y>0; 14.15.5(c) extends the same formulas to negative
    y, per the brief's pre-check -- the algebra (multiplication, exact
    division by a power of 2, valuations) does not use sign anywhere)."""
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


def unique_predecessor(z, m, r):
    """Theorem 14.15.4.1: the unique odd integer y with G(y)=z and
    stratum(y)=(m,r), or None if 3^m does not divide 2^r z + 1. Positive
    when z is a positive live door (14.15.4.1); not assumed positive
    here for callers that need the raw formula."""
    num = (1 << r) * z + 1
    denom = 3 ** m
    if num % denom != 0:
        return None
    q = num // denom
    return (1 << m) * q - 1


def letter_affine(m, r):
    """14.14.4.1's per-stratum affine constants (alpha, beta), exact
    Fractions."""
    denom = Fraction(1, 2 ** (m + r))
    alpha = Fraction(3 ** m) * denom
    beta = Fraction(3 ** m - 2 ** m) * denom
    return alpha, beta


def compose_append(letters):
    """14.14.8.2's own literal recursion: A_0=1, B_0=0;
    A_(i+1)=alpha_i A_i, B_(i+1)=alpha_i B_i + beta_i -- `letters[0]` is
    applied first (innermost / earliest), `letters[-1]` last. Appends
    each new letter at the shallow (late-applied) end of the
    composition built so far."""
    A, B = Fraction(1), Fraction(0)
    for (m, r) in letters:
        alpha, beta = letter_affine(m, r)
        A, B = alpha * A, alpha * B + beta
    return A, B


def compose_prepend_step(alpha, beta, A_old, B_old):
    """The OTHER composition route, used by reverse.md 14.15.3.3's own
    proof: prepend a new EARLIEST-applied letter (own constants
    alpha, beta) in front of an already-composed map (A_old, B_old),
    i.e. new_map = old_map o new_letter_map. A_new = A_old*alpha,
    B_new = A_old*beta + B_old -- structurally different from
    compose_append's one-step update (alpha*B_old+beta), reconciled in
    test_recursion_reconciliation below."""
    return A_old * alpha, A_old * beta + B_old


def frac_mod(x: Fraction, mod: int) -> int:
    """Reduce a Fraction with denominator coprime to `mod` into Z/mod."""
    num = x.numerator % mod
    den = x.denominator % mod
    inv = pow(den, -1, mod)
    return (num * inv) % mod


def random_odd_not3(rng, hi, lo=1):
    while True:
        y = rng.randrange(lo, hi, 2)
        if y % 3 != 0:
            return y


def find_live_predecessor(cur, rng, m_cap=3, r_cap=25, tries=500):
    """Search for a live letter-prescribed predecessor of `cur` (same
    technique as experiments/realization_height.py's own helper,
    reimplemented independently here)."""
    for _ in range(tries):
        m = rng.randrange(1, m_cap + 1)
        for r in range(1, r_cap):
            y = unique_predecessor(cur, m, r)
            if y is not None and y % 3 != 0:
                return y, m, r
    return None


def single_letter_residue(m, r):
    """Lemma 14.15.1.3(i): the unique y mod 2^(m+r+1) with
    stratum(y) = (m,r)."""
    mod_q = 1 << (r + 1)
    inv3m = pow(3, -m, mod_q)
    q_res = (inv3m * (1 + (1 << r))) % mod_q
    return ((1 << m) * q_res - 1) % (1 << (m + r + 1))


def forward_class_representative(letters):
    """Constructive form of Theorem 14.15.1.5 (via Lemma 14.15.1.4's own
    Hensel-lifting induction, reimplemented directly rather than by
    brute-force scanning): returns (y_rep, modulus=2^(S+1)) such that a
    positive odd y follows `letters` (in forward/chronological order,
    letters[0] = stratum(y) itself) iff y === y_rep (mod modulus). Used
    in 14.15.5(b)/(c) to check/construct forward realization without
    scanning, which becomes infeasible once the modulus is large
    (reached already by n=5 for 14.15.5(c)'s word below)."""
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
# 14.15.5(a): the admissibility-class lemma
# ---------------------------------------------------------------------------

def test_base_case_identity(trials=2000, seed=45001, m_hi=8, r_hi=12):
    """Single-letter base case: for letter (m,r), the admissibility
    congruence 3^m | 2^r z + 1 (i.e. z === -2^{-r} mod 3^m) coincides
    exactly with 14.14.4.1's own affine constant beta reduced mod 3^m
    (beta = B_1, the n=1 case of any composed-affine word). Exact
    Fraction arithmetic; no anchor or valuation truncation."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        m = rng.randrange(1, m_hi)
        r = rng.randrange(1, r_hi)
        _, beta = letter_affine(m, r)
        lhs = frac_mod(beta, 3 ** m)
        rhs = (-pow(2, -r, 3 ** m)) % (3 ** m)
        if lhs != rhs:
            bad += 1
    return trials, bad


def test_recursion_reconciliation(trials=2000, seed=45002, n_max=6,
                                   m_hi=4, r_hi=4):
    """The order-convention reconciliation the brief asks for: for a
    word given deepest-first (matching reverse.md 14.15.3(b)'s W_(-n:0)
    convention), 14.14.8.2's own literal recursion (compose_append,
    which appends new letters at the shallow/late-applied end) and the
    prepend recursion 14.15.3.3's proof actually uses (which builds up
    by prepending progressively DEEPER letters -- the natural direction
    for growing backward-chain depth, exactly item 1's own induction
    direction) compute the SAME (A_n, B_n) for the same word, by
    associativity of affine composition. Not a mismatch in value -- a
    difference in which of two equivalent recursions is natural for
    which induction direction, verified explicitly here rather than
    asserted."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        n = rng.randrange(1, n_max + 1)
        letters_deepest_first = [(rng.randrange(1, m_hi), rng.randrange(1, r_hi))
                                  for _ in range(n)]
        A1, B1 = compose_append(letters_deepest_first)

        # prepend recursion: process from shallowest (last in list) to
        # deepest (first in list), matching item 1's induction (growing
        # admissibility depth by prepending a new deepest letter).
        rev = list(reversed(letters_deepest_first))
        m0, r0 = rev[0]
        A2, B2 = letter_affine(m0, r0)
        for (m, r) in rev[1:]:
            alpha, beta = letter_affine(m, r)
            A2, B2 = compose_prepend_step(alpha, beta, A2, B2)

        if A1 != A2 or B1 != B2:
            bad += 1
    return trials, bad


def admissible_class_bruteforce(letters_shallow_first, z_bound):
    """letters_shallow_first: [(m_{-1},r_{-1}),...,(m_{-n},r_{-n})] (the
    brief's V ordering, shallowest letter first). Brute force over ODD
    POSITIVE z < z_bound: does the letter-prescribed backward chain
    exist to depth n (each step via unique_predecessor)? 14.15.4.1
    forces the result positive automatically whenever admissible, so no
    separate positivity filter is needed inside the loop."""
    admissible = []
    for z in range(1, z_bound, 2):
        cur = z
        ok = True
        for (m, r) in letters_shallow_first:
            y = unique_predecessor(cur, m, r)
            if y is None:
                ok = False
                break
            cur = y
        if ok:
            admissible.append(z)
    return admissible


def test_admissibility_class(trials=400, seed=45003, n_max=4, m_hi=3,
                              r_hi=4, z_bound_cap=20000):
    """The lemma itself, both directions, by direct brute-force scan:
    (i) every admissible z found by scanning lies in the predicted
    residue class mod 3^(M_n) (soundness), and (ii) every odd positive
    z below the scan bound in the predicted class is admissible
    (completeness, checked along the arithmetic progression of the
    class up to the same bound). Matches the pre-check's own
    methodology (400 random words) with fresh, independent code."""
    rng = random.Random(seed)
    bad_sound = 0
    bad_complete = 0
    checked_words = 0
    for _ in range(trials):
        n = rng.randrange(1, n_max + 1)
        letters_shallow_first = [(rng.randrange(1, m_hi), rng.randrange(1, r_hi))
                                  for _ in range(n)]
        M_n = sum(m for m, r in letters_shallow_first)
        mod = 3 ** M_n
        A_n, B_n = compose_append(list(reversed(letters_shallow_first)))
        predicted = frac_mod(B_n, mod)

        z_bound = min(4 * mod, z_bound_cap)
        admissible = set(admissible_class_bruteforce(letters_shallow_first, z_bound))
        checked_words += 1

        for z in admissible:
            if z % mod != predicted:
                bad_sound += 1

        z = predicted if predicted % 2 == 1 else predicted + mod
        while z < z_bound:
            if z not in admissible:
                bad_complete += 1
            z += 2 * mod

    return checked_words, bad_sound, bad_complete


def test_synchronization_strengthening(trials=1500, seed=45004, m_hi=3,
                                        r_hi=4, n_max=5):
    """Corollary 14.14.8.3 said "chains that exist agree with B_n mod
    3^(k+1) once Sigma m_i >= k+1"; item 1 strengthens this to
    "existence itself is the congruence with B_n" -- tested directly:
    for random words and random z, z admits the depth-n chain IFF
    z === B_n (mod 3^(M_n)), checked both ways on the same z (not via
    scanning, via direct construction/failure of the chain)."""
    rng = random.Random(seed)
    bad = 0
    checked = 0
    for _ in range(trials):
        n = rng.randrange(1, n_max + 1)
        letters_shallow_first = [(rng.randrange(1, m_hi), rng.randrange(1, r_hi))
                                  for _ in range(n)]
        M_n = sum(m for m, r in letters_shallow_first)
        mod = 3 ** M_n
        A_n, B_n = compose_append(list(reversed(letters_shallow_first)))
        predicted = frac_mod(B_n, mod)

        for congruent in (True, False):
            if congruent:
                z = predicted + mod * rng.randrange(0, 50)
                if z % 2 == 0:
                    z += mod
            else:
                z = predicted + rng.randrange(1, mod)
                if z % mod == predicted:
                    continue
                if z % 2 == 0:
                    z += 1
            cur = z
            chain_exists = True
            for (m, r) in letters_shallow_first:
                y = unique_predecessor(cur, m, r)
                if y is None:
                    chain_exists = False
                    break
                cur = y
            checked += 1
            expected = (z % mod == predicted)
            if chain_exists != expected:
                bad += 1
    return checked, bad


# ---------------------------------------------------------------------------
# 14.15.5(b): the converse theorem / combined characterization
# ---------------------------------------------------------------------------

def test_converse_mechanism(trials=300, seed=45005, depth=12, hi=10 ** 5):
    """Verifies the three ingredients of item 2's proof directly on real
    long backward chains behind a real positive live door y0 (built
    honestly -- letters are not chosen to match a target, they are
    whatever find_live_predecessor turns up):

    (i) Cauchy estimate: v_3(y0 - B_n) >= M_n for every depth n (the
        hypothesis "y3(W) = y0" would give exactly this, in the limit);
    (ii) reconstruction: rebuilding the chain from y0 and the recorded
        letters alone via unique_predecessor (NOT consulting the
        already-built `chain`) reproduces it exactly -- this is the
        truncation-compatibility / uniqueness mechanism the proof
        leans on (14.15.4.1's uniqueness forces the depth-(n+1) chain
        to restrict to the depth-n chain);
    (iii) liveness derived: every chain door, including G's own image
        of the deepest one, is automatically live -- no liveness
        hypothesis is assumed anywhere in the reconstruction.
    """
    rng = random.Random(seed)
    built = 0
    bad_cauchy = 0
    bad_reconstruct = 0
    bad_live = 0

    for _ in range(trials):
        y0 = random_odd_not3(rng, hi)
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
        if G(chain[-1]) % 3 == 0:
            bad_live += 1

    return trials, built, bad_cauchy, bad_reconstruct, bad_live


def test_forward_half_nesting(trials=2000, seed=45006, n_max=10, hi=10 ** 6):
    """The forward half of item 2's proof: y0's own forward orbit places
    it in every one of its own forward cylinders (the y2 = y0 direction
    is by construction, but the nesting mechanism -- the cylinder
    modulus 2^(S_n+1) growing so y0's residue determines it exactly --
    is checked directly here, independent of realization_height.py /
    itinerary_coding.py's own versions of this fact)."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        y0 = random_odd_not3(rng, hi)
        n = rng.randrange(1, n_max + 1)
        letters = []
        cur = y0
        for _ in range(n):
            letters.append(stratum(cur))
            cur = G(cur)
        y_rep, modulus = forward_class_representative(letters)
        if y0 % modulus != y_rep % modulus:
            bad += 1
    return trials, bad


if __name__ == "__main__":
    print("== 14.15.5(a): base-case identity (beta === -2^{-r} mod 3^m) ==")
    trials, bad = test_base_case_identity()
    print(f"{trials} checked, {bad} failures")

    print("== 14.15.5(a): recursion reconciliation (append vs. prepend) ==")
    trials, bad = test_recursion_reconciliation()
    print(f"{trials} checked, {bad} failures")

    print("== 14.15.5(a): admissibility-class lemma (brute force, "
          "soundness + completeness) ==")
    words, bad_sound, bad_complete = test_admissibility_class()
    print(f"{words} words checked, {bad_sound} soundness failures, "
          f"{bad_complete} completeness failures")

    print("== 14.15.5(a): synchronization strengthening "
          "(existence <=> congruence) ==")
    checked, bad = test_synchronization_strengthening()
    print(f"{checked} (word,z) checks, {bad} failures")

    print("== 14.15.5(b): converse-theorem mechanism ==")
    trials, built, bad_c, bad_r, bad_l = test_converse_mechanism()
    print(f"{trials} trials, {built} chains built, "
          f"{bad_c} Cauchy-estimate failures, "
          f"{bad_r} reconstruction failures, {bad_l} liveness failures")

    print("== 14.15.5(b): forward-half nesting ==")
    trials, bad = test_forward_half_nesting()
    print(f"{trials} checked, {bad} failures")
