"""Independent verification for briefs/tree-language-families-brief.md.

Supports two items:

  A. itinerary.md, new Lemma 14.15.2.1 (the tree's language is the full
     shift): every finite word W is followed by some positive odd x whose
     T-orbit reaches 1. Checks:
       (a) the covering of residue classes mod 3^k by (4^i-1)/3, exact,
           k <= 7 -- the bijection f(i) = (4^i-1)/3 mod 3^k, derived here
           from reverse.md Lemma 14.2.1 (v_3(2^t-1) = 1+v_3(t), t even).
       (b) random words: the cylinder of itinerary.md Theorem 14.15.1.5 is
           exactly one residue class mod 2^(S+1); and a positive odd witness
           x following the word, with T-orbit reaching 1, built by the
           proof's own construction (the cylinder representative, the
           composed level shift of Lemma 14.15.1.4, and the covering of
           (a)) -- not by searching integers for the "reaches 1" property.
       (c) canaries: (1,1); a few hand-checked words; (4^i-1)/3 reaching 1.

  B. open-problems.md, new entry 11.14 (the family-frame weak conjecture):
       (c) the s=2 no-anchor classes (w = 5,7 mod 8): no s>2 ever, and the
           depth-two recurrence e(w,d+2) = T(6*e(w,d)+1) at spike depths
           (ladder.md Theorem 15.1.1, stage1.md Proposition 11.8.1.3.1).
       (d) the 4X+1 kick identity Theta(4X+1) = Theta(X) (general X, exact
           algebra), and the corrected scope: exact one-step merge with the
           orbit of 3e only at kick height s=3; an explicit counter-instance
           at s=4 showing the merge is not immediate there.
       (e) the x vs 3x orbit-merge measurement, fresh sample, bound printed.
       (f) the trivial family's exits e(1,d) = odd part of 3^d-1.

Fresh code: imports nothing from any other file in this repository (not
itinerary_coding.py, not door_seam.py, not ladder.py, not ladder_afterlife.py,
not ladder_family_graph.py, not top_door_lineage.py -- every primitive below,
including the reduced-map numerator/exit/valuation machinery and the T map,
is reimplemented from the wiki's own definitions). Exact Python-integer
arithmetic at every pass/fail decision (no floats anywhere in a check).
Canaries run first in every section. Single reproducing command:

    python experiments/tree_language_families.py

No phases, no flags. Seed 20260913 for every randomized check below.
"""

import random
import sys
import time

SEED = 20260913
random.seed(SEED)

TOTAL_CHECKS = 0
TOTAL_FAILURES = 0
FAILURE_LOG = []


def check(condition, label):
    global TOTAL_CHECKS, TOTAL_FAILURES
    TOTAL_CHECKS += 1
    if not condition:
        TOTAL_FAILURES += 1
        FAILURE_LOG.append(label)
    return condition


# ---------------------------------------------------------------------------
# Primitives, reimplemented from the wiki's own definitions.
# ---------------------------------------------------------------------------

def v2(n):
    """2-adic valuation of a nonzero integer n."""
    assert n != 0
    n = abs(n)
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def v3(n):
    """3-adic valuation of a nonzero integer n."""
    assert n != 0
    n = abs(n)
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def T(y):
    """The odd-to-odd Collatz map, spine.md Section 9.8: T(y) = (3y+1)/2^v2(3y+1).
    y must be a positive odd integer."""
    assert y > 0 and y % 2 == 1
    v = 3 * y + 1
    return v >> v2(v)


def Theta(y):
    """The same formula as T, extended to every positive integer (odd or
    even): Theta(y) = (3y+1)/2^v2(3y+1). Theta == T on odd y."""
    assert y > 0
    v = 3 * y + 1
    return v >> v2(v)


def reaches_1(y, cap=100000):
    """Whether the T-orbit of the positive odd y reaches 1, within cap steps.
    Returns (bool, steps_taken)."""
    x = y
    for i in range(cap):
        if x == 1:
            return True, i
        x = T(x)
    return x == 1, cap


def stratum(y):
    """itinerary.md Definition 14.15.1.1, extended to every odd y (the page's
    own remark: no coprimality hypothesis is used). m = v2(y+1),
    q = (y+1)/2^m, r = v2(3^m*q - 1)."""
    assert y > 0 and y % 2 == 1
    m = v2(y + 1)
    q = (y + 1) >> m
    r = v2(pow(3, m) * q - 1)
    return (m, r)


def G(y):
    """reverse.md Definition 14.14.3.1 / itinerary.md's total extension:
    G(y) = (3^m*q - 1) / 2^r on the stratum (m,r) = stratum(y)."""
    m, r = stratum(y)
    q = (y + 1) >> m
    return (pow(3, m) * q - 1) >> r


def state(y):
    """reverse.md 14.6.5.1: y+1 = 2^m * 3^a * Omega, state(y) = (Omega, m+a)."""
    assert y > 0 and y % 2 == 1
    n = y + 1
    m = v2(n)
    n >>= m
    a = v3(n)
    Omega = n // (3 ** a)
    return (Omega, m + a)


def A_num(omega, d):
    """spine.md: A(omega,d) = 3^d * omega - 1."""
    return pow(3, d) * omega - 1


def s_val(omega, d):
    """spine.md: s(omega,d) = v2(A(omega,d))."""
    return v2(A_num(omega, d))


def e_exit(omega, d):
    """spine.md: e(omega,d) = x_exit(omega,d) = A(omega,d) / 2^s."""
    A = A_num(omega, d)
    s = v2(A)
    return A >> s


def F_step(omega, d):
    """spine.md Section 3.7/9.8: F(omega,d) = R(x_exit(omega,d)) = state(e(omega,d))."""
    return state(e_exit(omega, d))


def odd_part(n):
    assert n != 0
    n = abs(n)
    while n % 2 == 0:
        n //= 2
    return n


# ---------------------------------------------------------------------------
# Canaries (run first, for both items).
# ---------------------------------------------------------------------------

def canaries():
    print("--- Canaries ---")
    # (1,1) fixed point.
    check(stratum(1) == (1, 1), "canary: stratum(1) == (1,1)")
    check(G(1) == 1, "canary: G(1) == 1")
    check(T(1) == 1, "canary: T(1) == 1")
    check(state(1) == (1, 1), "canary: state(1) == (1,1)")
    check(F_step(1, 1) == (1, 1), "canary: F(1,1) == (1,1)")

    # Hand-checked word [(1,1)]: cylinder is y == 1 (mod 8) (S=2, N=2^3=8).
    hand_reps_in = [1, 9, 17, 25, 33]
    hand_reps_out = [3, 5, 7, 11, 13, 15]
    for y in hand_reps_in:
        check(stratum(y) == (1, 1), f"canary: hand word [(1,1)] cylinder contains {y}")
    for y in hand_reps_out:
        check(stratum(y) != (1, 1), f"canary: hand word [(1,1)] cylinder excludes {y}")

    # Hand-checked word [(1,1),(1,1)]: composing G twice should also stay on
    # (1,1),(1,1), and 1's own orbit realizes it (G(1)=1, stratum(1)=(1,1)).
    check(stratum(G(1)) == (1, 1), "canary: word [(1,1),(1,1)] realized by x=1")

    # (4^i - 1)/3 reaches 1, i = 1..5, each in exactly one T-step, T(F)=1.
    for i in range(1, 6):
        F = (4 ** i - 1) // 3
        check(F % 2 == 1, f"canary: (4^{i}-1)/3 is odd")
        # T(F) == 1 always (i=1 gives F=1 itself, already the fixed point,
        # 0 T-steps needed; i>=2 gives F>1, reaching 1 in exactly 1 step).
        ok, steps = reaches_1(F, cap=5)
        expected_steps = 0 if F == 1 else 1
        check(ok and steps == expected_steps, f"canary: (4^{i}-1)/3={F} reaches 1 in {expected_steps} T-step(s)")
        check(T(F) == 1, f"canary: T((4^{i}-1)/3) == 1 directly, i={i}")

    # Trivial family sanity: e(1,1)=1.
    check(e_exit(1, 1) == 1, "canary: e(1,1) == 1")
    print(f"  canaries: {TOTAL_CHECKS} checks so far, {TOTAL_FAILURES} failures")


# ---------------------------------------------------------------------------
# Item A(a): the covering of residue classes mod 3^k by (4^i-1)/3, k <= 7.
# ---------------------------------------------------------------------------

def item_A_covering():
    print("--- Item A(a): covering of Z/3^k by f(i)=(4^i-1)/3, k=1..7 ---")
    for k in range(1, 8):
        period = 3 ** k
        modk = 3 ** k
        seen = {}
        val4 = 1  # 4^0 mod 3^(k+1)
        mod_kp1 = 3 ** (k + 1)
        for i in range(period):
            # val4 == 4^i (mod 3^(k+1)), so val4-1 is an honest representative
            # of 4^i-1 mod 3^(k+1); since 4 == 1 (mod 3), val4-1 is always
            # divisible by 3 as a residue in [0, 3^(k+1)).
            assert (val4 - 1) % 3 == 0
            fi_mod = ((val4 - 1) // 3) % modk
            seen.setdefault(fi_mod, []).append(i)
            val4 = (val4 * 4) % mod_kp1
        # Bijectivity: every residue in [0, 3^k) hit, exactly once, over one
        # full period i = 0..3^k-1.
        all_hit = set(seen.keys()) == set(range(modk))
        check(all_hit, f"item A(a): k={k}, f(i) mod 3^{k} covers every residue over one period")
        exactly_once = all(len(v) == 1 for v in seen.values())
        check(exactly_once, f"item A(a): k={k}, f(i) mod 3^{k} hits each residue exactly once per period")

        # Periodicity spot check: f(i) == f(i + period) for a sample of i.
        sample_is = random.sample(range(period), min(20, period))
        ok_period = True
        for i in sample_is:
            fi = pow(4, i, mod_kp1)
            fi = ((fi - 1) // 3) % modk
            fj = pow(4, i + period, mod_kp1)
            fj = ((fj - 1) // 3) % modk
            if fi != fj:
                ok_period = False
        check(ok_period, f"item A(a): k={k}, period {period} confirmed on {len(sample_is)} sampled i")

        # Order-of-4 fact used in the derivation: v3(4^i-1) = 1+v3(i), i=1..period.
        ok_order = True
        for i in range(1, min(period, 200) + 1):
            lhs = v3(4 ** i - 1)
            rhs = 1 + v3(i)
            if lhs != rhs:
                ok_order = False
        check(ok_order, f"item A(a): k={k}, v3(4^i-1)=1+v3(i) on i=1..{min(period,200)}")
    print(f"  running totals: {TOTAL_CHECKS} checks, {TOTAL_FAILURES} failures")


# ---------------------------------------------------------------------------
# Item A(b): cylinder construction and the constructive witness.
# ---------------------------------------------------------------------------

def build_first_letter(m, r):
    """The unique odd y in [1, 2^(m+r+1)) with stratum(y) == (m,r) -- found
    by direct evaluation over the (small, letter-sized) space Lemma 14.15.1.3(i)
    describes, not by searching for any dynamical ('reaches 1') property."""
    mod = 1 << (m + r + 1)
    for y in range(1, mod, 2):
        if stratum(y) == (m, r):
            return y, m + r, m, G(y)
    raise AssertionError("no representative found -- contradicts 14.15.1.5")


def extend_cylinder(a, S, M, z, m, r):
    """Extend a cylinder representative a (mod 2^(S+1), following n letters,
    with z = G^n(a)) by one more letter (m,r). Finds t in [0, 2^(m+r)) with
    stratum(z + 2*3^M*t) == (m,r) -- unique by Lemma 14.15.1.4/14.15.1.3(i);
    found by direct evaluation over this letter-sized space (<= 2^(m+r)
    candidates), not a search over many integers for a rare property."""
    K = 2 * (3 ** M)
    target = (m, r)
    found_t = None
    for t in range(1 << (m + r)):
        w = z + K * t
        if stratum(w) == target:
            found_t = t
            break
    assert found_t is not None, "no t found -- contradicts 14.15.1.4"
    newS = S + m + r
    a_new = (a + (1 << (S + 1)) * found_t) % (1 << (newS + 1))
    w_final = z + K * found_t
    z_new = G(w_final)
    return a_new, newS, M + m, z_new


def build_cylinder(W):
    """Build (a, S, M, z) for a word W: a is a representative mod 2^(S+1)
    following W, S = sum(m_i+r_i), M = sum(m_i), z = G^n(a)."""
    m0, r0 = W[0]
    a, S, M, z = build_first_letter(m0, r0)
    for (m, r) in W[1:]:
        a, S, M, z = extend_cylinder(a, S, M, z, m, r)
    return a, S, M, z


def follows(x, W):
    """Direct simulation: does x follow W (Definition 14.15.1.2)?"""
    y = x
    for (m, r) in W:
        if stratum(y) != (m, r):
            return False
        y = G(y)
    return True


TABLE_CACHE = {}


def f_table(k):
    """Precomputed lookup: residue mod 3^k -> the unique i in [0, 3^k) with
    f(i) = (4^i-1)/3 == residue (mod 3^k). Built once per k, reused."""
    if k in TABLE_CACHE:
        return TABLE_CACHE[k]
    modk = 3 ** k
    mod_kp1 = 3 ** (k + 1)
    table = [None] * modk
    val4 = 1
    for i in range(modk):
        fi = ((val4 - 1) // 3) % modk
        table[fi] = i
        val4 = (val4 * 4) % mod_kp1
    TABLE_CACHE[k] = table
    return table


def item_A_b_cylinder_structure():
    print("--- Item A(b): cylinder = arithmetic progression at modulus 2^(S+1) ---")
    # Exhaustive check on small words: length 1..2, letters (m,r) in {1,2,3}.
    exhaustive_words = []
    for m0 in range(1, 4):
        for r0 in range(1, 4):
            exhaustive_words.append([(m0, r0)])
    for m0 in range(1, 3):
        for r0 in range(1, 3):
            for m1 in range(1, 3):
                for r1 in range(1, 3):
                    exhaustive_words.append([(m0, r0), (m1, r1)])
    n_exhaustive_checks = 0
    for W in exhaustive_words:
        S = sum(m + r for m, r in W)
        modulus = 1 << (S + 1)
        followers = [y for y in range(1, modulus, 2) if follows(y, W)]
        n = len(W)
        # Every follower found must be congruent mod 2^(S+1) to every other
        # (exactly one residue class among the odd residues mod 2^(S+1)).
        ok = len(set(followers)) >= 1 and len(followers) == 1
        check(ok, f"item A(b): word {W} exhaustive cylinder is a single residue mod 2^{S+1}")
        n_exhaustive_checks += 1
    print(f"  exhaustive cylinder check: {n_exhaustive_checks} small words, "
          f"{TOTAL_CHECKS} checks so far, {TOTAL_FAILURES} failures")

    # Random larger words: build the cylinder representative via the
    # constructive method, verify a follows W directly, verify positive and
    # negative controls (nearby residues out of class do not follow W).
    n_random = 250
    max_len = 4
    letter_range = (1, 3)
    random_checks = 0
    for _ in range(n_random):
        n = random.randint(1, max_len)
        W = [(random.randint(*letter_range), random.randint(*letter_range)) for _ in range(n)]
        a, S, M, z = build_cylinder(W)
        modulus = 1 << (S + 1)
        check(0 < a < modulus and a % 2 == 1, f"item A(b): representative a={a} valid for word {W}")
        check(follows(a, W), f"item A(b): constructed representative follows word {W}")
        # Verify G^n(a) == z by direct n-fold simulation.
        y = a
        for _ in range(n):
            y = G(y)
        check(y == z, f"item A(b): G^n(a) matches recorded z for word {W}")
        # Positive control: a + modulus also follows W.
        check(follows(a + modulus, W), f"item A(b): a+2^(S+1) also follows word {W}")
        # Negative control: a shifted by a non-multiple of the modulus, if
        # still odd and positive, should not follow W (unless it happens to
        # coincide, which cylinder theorem forbids for a genuine offset in
        # (0, modulus)).
        offset = random.randrange(2, modulus, 2)  # even offset, nonzero, < modulus
        neg_candidate = a + offset
        if neg_candidate % 2 == 1 and neg_candidate > 0:
            check(not follows(neg_candidate, W), f"item A(b): a+offset (offset={offset}) does not follow word {W}")
            random_checks += 1
        random_checks += 3
    print(f"  random cylinder checks: {n_random} words, {random_checks} sub-checks, "
          f"{TOTAL_CHECKS} checks so far, {TOTAL_FAILURES} failures")


def item_A_b_constructive_witness():
    print("--- Item A(b): constructive witness reaching 1 (Lemma 14.15.2.1's own proof) ---")
    # Keep M small enough that (4^i-1)/3 stays a manageable integer:
    # word length 1..3, letters (m,r) in {1,2}, so M <= 6, 3^M <= 729.
    n_random = 150
    max_len = 3
    letter_range = (1, 2)
    built = 0
    for _ in range(n_random):
        n = random.randint(1, max_len)
        W = [(random.randint(*letter_range), random.randint(*letter_range)) for _ in range(n)]
        a, S, M, z0 = build_cylinder(W)
        table = f_table(M)
        target = z0 % (3 ** M)
        i0 = table[target]
        modk = 3 ** M
        i = i0 if i0 >= 1 else i0 + modk
        F = (4 ** i - 1) // 3
        # Advance by full periods until F >= z0 (guarantees t >= 0 below).
        tries = 0
        while F < z0:
            i += modk
            F = (4 ** i - 1) // 3
            tries += 1
            assert tries < 10000
        check(F % (3 ** M) == z0 % (3 ** M), f"item A(b): F congruent to z0 mod 3^{M} for word {W}")
        check(F >= z0, f"item A(b): F >= z0 for word {W}")
        diff = F - z0
        check(diff % 2 == 0, f"item A(b): F - z0 even for word {W}")
        t = diff // (2 * (3 ** M))
        check(t >= 0 and diff == 2 * (3 ** M) * t, f"item A(b): t is a valid nonnegative integer for word {W}")

        modulus = 1 << (S + 1)
        x = a + modulus * t
        check(x > 0 and x % 2 == 1, f"item A(b): witness x is a positive odd integer for word {W}")
        check(follows(x, W), f"item A(b): witness x follows word {W}")

        # Independent check: G^n(x) == F by direct n-fold simulation.
        y = x
        for _ in range(n):
            y = G(y)
        check(y == F, f"item A(b): G^n(x) == F (constructed value) for word {W}")

        # F reaches 1 in exactly one T-step.
        check(T(F) == 1, f"item A(b): T(F) == 1 directly for word {W}")

        # Hence x's T-orbit reaches 1: verify directly by iterating T from x
        # until it hits 1 (bounded steps; F itself is on x's T-orbit since
        # G(y) = T^m(y), so this must terminate quickly in practice, but the
        # cap is generous and the check is a genuine simulation, not asserted).
        ok, steps = reaches_1(x, cap=2000)
        check(ok, f"item A(b): x's T-orbit reaches 1 for word {W} (steps={steps})")
        built += 1
    print(f"  constructive witnesses built: {built} words (length<=3, letters<=2, M<=6), "
          f"{TOTAL_CHECKS} checks so far, {TOTAL_FAILURES} failures")


# ---------------------------------------------------------------------------
# Item B(c): the s=2 no-anchor classes.
# ---------------------------------------------------------------------------

def item_B_regime1():
    print("--- Item B(c): the s=2 no-anchor classes (w=5,7 mod 8) ---")
    n_cores = 200
    d_max = 60
    total_depth_checks = 0
    total_recurrence_checks = 0
    for _ in range(n_cores):
        base = random.choice([5, 7])
        # Random odd core === base (mod 8), coprime to 3 not required by the
        # brief's family definition, but avoid omega multiples of small
        # primes causing no special issue -- omega itself need not be prime.
        omega = base + 8 * random.randint(0, 10 ** 6)
        if omega % 2 == 0:
            omega += 1  # guard, should not trigger since base+8k stays odd
        s_values = {}
        for d in range(1, d_max + 1):
            s = s_val(omega, d)
            s_values[d] = s
            total_depth_checks += 1
            check(s in (1, 2), f"item B(c): s(omega={omega},d={d}) in {{1,2}} (omega%8={omega%8})")
        # Depth-two recurrence at every spike depth d (s(omega,d)==2) with
        # d+2 <= d_max.
        for d in range(1, d_max - 1):
            if s_values[d] == 2:
                e_d = e_exit(omega, d)
                e_d2 = e_exit(omega, d + 2)
                predicted = T(6 * e_d + 1)
                total_recurrence_checks += 1
                check(e_d2 == predicted,
                      f"item B(c): e(omega,{d}+2)==T(6*e(omega,{d})+1), omega={omega}")
    print(f"  {n_cores} cores, depths 1..{d_max}: {total_depth_checks} s-value checks, "
          f"{total_recurrence_checks} recurrence checks; "
          f"{TOTAL_CHECKS} checks so far, {TOTAL_FAILURES} failures")


# ---------------------------------------------------------------------------
# Item B(d): the 4X+1 kick identity, general and corrected scope.
# ---------------------------------------------------------------------------

def item_B_regime2():
    print("--- Item B(d): the 4X+1 identity Theta(4X+1)=Theta(X), and its corrected scope ---")
    # General identity, many X (odd and even), pure algebra.
    n_general = 3000
    for _ in range(n_general):
        X = random.randint(1, 10 ** 9)
        lhs = Theta(4 * X + 1)
        rhs = Theta(X)
        check(lhs == rhs, f"item B(d): Theta(4X+1)==Theta(X) for X={X}")

    # The kick family: for random e (odd) and s>=3, X = 3*2^(s-3)*e; verify
    # the kicked exit equals 4X+1 and the identity.
    n_kick = 3000
    for _ in range(n_kick):
        e = random.randrange(1, 10 ** 6, 2)
        s = random.randint(3, 12)
        X = 3 * (2 ** (s - 3)) * e
        kicked = 3 * (2 ** (s - 1)) * e + 1
        check(kicked == 4 * X + 1, f"item B(d): kicked exit == 4X+1, e={e}, s={s}")
        check(Theta(kicked) == Theta(X), f"item B(d): identity on the kick family, e={e}, s={s}")
        if s == 3:
            check(X % 2 == 1, f"item B(d): X odd exactly at s=3, e={e}")
            check(Theta(X) == T(3 * e), f"item B(d): s=3, Theta(X)==T(3e) exactly, e={e}")
        else:
            check(X % 2 == 0, f"item B(d): X even for s>=4, e={e}, s={s}")
            closed = 9 * (2 ** (s - 3)) * e + 1
            check(Theta(X) == closed, f"item B(d): s>=4 closed form Theta(X)=9*2^(s-3)*e+1, e={e}, s={s}")

    # Explicit counter-instance at s=4: the merge with 3e is NOT immediate.
    e, s = 1, 4
    X = 3 * (2 ** (s - 3)) * e
    kicked = 3 * (2 ** (s - 1)) * e + 1
    check((X, kicked) == (6, 25), "item B(d): counter-instance setup, X=6, kicked=25")
    check(T(kicked) == 19, "item B(d): T(25) == 19")
    check(T(3 * e) == 5, "item B(d): T(3e) == T(3) == 5")
    check(T(kicked) != T(3 * e), "item B(d): T(25) != T(3), the s=4 merge is not immediate")
    # But they do merge eventually (generic Collatz behavior, not claimed as
    # a proof of anything -- a direct simulation, recorded as calibration).
    orbit_from_kicked = []
    y = kicked
    for _ in range(20):
        y = T(y)
        orbit_from_kicked.append(y)
    check(5 in orbit_from_kicked, "item B(d): T-orbit of kicked exit (s=4) meets 3e's orbit eventually (at 5)")
    steps_to_merge = orbit_from_kicked.index(5) + 1
    check(steps_to_merge == 6, f"item B(d): eventual merge takes {steps_to_merge} steps from T(kicked), not 1")
    print(f"  {n_general} general-X checks, {n_kick} kick-family checks, 1 counter-instance; "
          f"{TOTAL_CHECKS} checks so far, {TOTAL_FAILURES} failures")


# ---------------------------------------------------------------------------
# Item B(e): the x vs 3x orbit-merge measurement.
# ---------------------------------------------------------------------------

def item_B_wall_measurement():
    print("--- Item B(e): the x vs 3x orbit-merge measurement ---")
    target_trials = 1300
    bound_steps = 400
    upper_x = 2 * 10 ** 6
    merged_above_1 = 0
    merged_only_at_1 = 0
    tested = 0
    attempts = 0
    while tested < target_trials:
        attempts += 1
        x = random.randrange(1, upper_x, 2)
        if x % 3 == 0:
            continue
        tested += 1
        y3 = 3 * x
        # Build the T-orbit of x and of 3x up to bound_steps, look for the
        # first common value.
        orbit_x = set()
        cur = x
        for _ in range(bound_steps):
            orbit_x.add(cur)
            cur = T(cur)
        orbit_3x = []
        cur = y3
        for _ in range(bound_steps):
            orbit_3x.append(cur)
            cur = T(cur)
        merge_val = None
        for v in orbit_3x:
            if v in orbit_x:
                merge_val = v
                break
        if merge_val is not None and merge_val > 1:
            merged_above_1 += 1
        else:
            merged_only_at_1 += 1
    check(tested >= target_trials, f"item B(e): at least {target_trials} valid trials run ({tested})")
    check(merged_above_1 + merged_only_at_1 == tested, "item B(e): trial bookkeeping consistent")
    print(f"  {tested} odd x < {upper_x}, coprime to 3: merged above 1 within {bound_steps} steps "
          f"in {merged_above_1} cases, only at 1 in {merged_only_at_1} cases "
          f"({merged_above_1}/{tested} = {merged_above_1/tested:.4f})")
    print(f"  {TOTAL_CHECKS} checks so far, {TOTAL_FAILURES} failures")


# ---------------------------------------------------------------------------
# Item B(f): the trivial family's own exits.
# ---------------------------------------------------------------------------

def item_B_trivial_family():
    print("--- Item B(f): e(1,d) == odd part of 3^d - 1 ---")
    expected_prefix = [1, 1, 13, 5, 121, 91, 1093]
    for d in range(1, 30):
        e = e_exit(1, d)
        op = odd_part(3 ** d - 1)
        check(e == op, f"item B(f): e(1,{d}) == odd_part(3^{d}-1)")
        if d <= 7:
            check(e == expected_prefix[d - 1], f"item B(f): e(1,{d}) matches the stated prefix value")
    print(f"  d=1..29 checked; {TOTAL_CHECKS} checks so far, {TOTAL_FAILURES} failures")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    print(f"tree_language_families.py -- seed {SEED}, {time.strftime('%Y-%m-%d', time.localtime())}")
    canaries()
    item_A_covering()
    item_A_b_cylinder_structure()
    item_A_b_constructive_witness()
    item_B_regime1()
    item_B_regime2()
    item_B_wall_measurement()
    item_B_trivial_family()
    elapsed = time.time() - t0
    print()
    print(f"TOTAL: checks={TOTAL_CHECKS}, failures={TOTAL_FAILURES}")
    if TOTAL_FAILURES:
        print("FAILURES:")
        for lab in FAILURE_LOG[:50]:
            print(f"  - {lab}")
    print(f"time={elapsed:.2f}s")
    if TOTAL_FAILURES:
        sys.exit(1)


if __name__ == "__main__":
    main()
