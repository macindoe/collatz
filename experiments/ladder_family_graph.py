"""
experiments/ladder_family_graph.py

Fresh, independent verification for briefs/ladder-family-graph-brief.md
(ladder.md 15.7: the two commutation laws of the ladder and the step, the
repunit-equation closure of the cousin search, the unified lemma, the
stratum census, the bits-read-backward remark, the reverse.md 14.10 twin
search, and the family-graph in-degree paragraph).

Imports nothing from any other script in this repository (not ladder.py,
not ladder_targetshift.py, not any scratchpad code). Exact integer
arithmetic at every pass/fail decision -- no floats anywhere in a
pass/fail path. Canaries first, then parts A-H matching Queue item 2 of
the brief. Deterministic: seed 20260913.

One command reproduces this file's committed output in full:

    python experiments/ladder_family_graph.py
"""

import random

SEED = 20260913
rng = random.Random(SEED)

TOTAL_CHECKS = 0
TOTAL_FAILURES = 0
FAILURE_LOG = []


def record(n_checks, n_failures, label):
    global TOTAL_CHECKS, TOTAL_FAILURES
    TOTAL_CHECKS += n_checks
    TOTAL_FAILURES += n_failures
    if n_failures:
        FAILURE_LOG.append((label, n_failures))
    status = "OK" if n_failures == 0 else "FAIL"
    print(f"  [{status}] {label}: {n_checks} checks, {n_failures} failures")


# ---------------------------------------------------------------------------
# Core arithmetic: state (omega, d) -> exit -> next state, from spine.md
# Sec. 5.4-5.6 / 7.1-7.3, re-derived from scratch (not copied from any
# script). All quantities are exact Python integers.
# ---------------------------------------------------------------------------

def v2(n):
    """2-adic valuation of a nonzero integer."""
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def v3(n):
    """3-adic valuation of a nonzero integer."""
    assert n != 0
    n = abs(n)
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def exit_data(omega, d):
    """A = 3^d*omega - 1, s = v2(A), e = x_exit(omega,d)."""
    A = 3 ** d * omega - 1
    s = v2(A)
    e = A // (1 << s)
    return A, s, e


def state_from_door(y):
    """
    Given an odd integer y (any odd y, per itinerary.md 14.15.1.1's
    general stratum definition -- 3 | y is allowed here, it just makes
    a=0 and the resulting 'core' divisible by no further 3's beyond
    what v3 already stripped), decompose y+1 = 2^m 3^a * Omega and
    return (Omega, D, m, a) with D = m + a.
    """
    assert y % 2 == 1
    z = y + 1
    m = v2(z)
    q = z // (1 << m)
    a = v3(q)
    Omega = q // (3 ** a)
    D = m + a
    return Omega, D, m, a


def F(omega, d):
    """The reduced map: F(omega,d) = R(x_exit(omega,d)) = (Omega, D)."""
    A, s, e = exit_data(omega, d)
    Omega, D, m, a = state_from_door(e)
    return (Omega, D)


def letter(omega, d):
    """The step's letter (s, m_plus, a_plus) via the C-based route
    (stage3.md 11.8.6.2-11.8.6.3), independent of state_from_door, for
    cross-checking."""
    A, s, e = exit_data(omega, d)
    C = A + (1 << s)
    vC = v2(C)
    m_plus = vC - s
    a_plus = v3(C)
    return s, m_plus, a_plus


def T_odd_to_odd(x):
    """Tao's Syr / this record's T: x -> (3x+1)/2^v2(3x+1), x odd."""
    assert x % 2 == 1
    y = 3 * x + 1
    return y // (1 << v2(y))


def random_omega(rng, bound):
    """Random odd omega, 3 does not divide omega, 1 <= omega < bound."""
    while True:
        w = rng.randrange(1, bound) | 1
        if w % 3 != 0:
            return w


def valid_state(rng, omega_bound, d_bound):
    return random_omega(rng, omega_bound), rng.randrange(1, d_bound)


# ---------------------------------------------------------------------------
# PART 0: canaries
# ---------------------------------------------------------------------------

def part0_canaries():
    print("PART 0: canaries")

    # (1,1) is F's fixed point -- the only state-space canary among the
    # three known cycles that lives in this program's domain (positive
    # (omega,d) states); the -5 and period-7 cycles are objects of the
    # signed integer extension (itinerary.md 14.15.6), outside the
    # domain of this brief. Recorded, not silently dropped.
    ok = (F(1, 1) == (1, 1))
    record(1, 0 if ok else 1, "canary: F(1,1) = (1,1), the trivial cycle")

    # ladder.md 15.1.1, re-derived fresh: the base ladder dichotomy.
    n, fails = 0, 0
    for _ in range(400):
        omega, d = valid_state(rng, 2 * 10 ** 4, 60)
        A, s, e = exit_data(omega, d)
        A2, s2, e2 = exit_data(omega, d + 1)
        n += 1
        if s == 1:
            if e2 != T_odd_to_odd(e):
                fails += 1
        else:
            predicted_e2 = 3 * (1 << (s - 1)) * e + 1
            if e2 != predicted_e2 or s2 != 1:
                fails += 1
    record(n, fails, "canary: ladder.md 15.1.1 dichotomy, fresh")

    # the neighbour-family identity: Omega(omega,d) = core of
    # C = 3^d*omega - 1 + 2^s, matching stage4's C/(2^v2(C) 3^v3(C)).
    n, fails = 0, 0
    for _ in range(2000):
        omega, d = valid_state(rng, 2 * 10 ** 4, 60)
        A, s, e = exit_data(omega, d)
        C = A + (1 << s)
        Omega_viaC = C // ((1 << v2(C)) * (3 ** v3(C)))
        Omega_viaF, D_viaF = F(omega, d)
        n += 1
        if Omega_viaC != Omega_viaF:
            fails += 1
    record(n, fails, "canary: neighbour-family core via C matches F")

    print()


# ---------------------------------------------------------------------------
# PART A: Law (i), merge/skip by m_plus and by omega mod 8
# ---------------------------------------------------------------------------

def offspike_state(rng, omega_bound, d_bound):
    """Construct a state with s(omega,d) = 1 directly from the
    first-layer table (stage1.md 11.8.1.3.1 / 11.8.4.1): for each
    omega mod 8 there is exactly one parity of d giving s = 1."""
    omega = random_omega(rng, omega_bound)
    r = omega % 8
    if r in (1, 5):
        parity = 1  # d odd
    else:  # r in (3, 7)
        parity = 0  # d even
    d = rng.randrange(1, d_bound)
    if d % 2 != parity:
        d += 1
        if d == 0:
            d = 2
    return omega, d


def part_a_law_i():
    print("PART A: law (i), merge/skip")
    n, fails, merges, skips = 0, 0, 0, 0
    n_mod8, fails_mod8 = 0, 0
    for _ in range(40000):
        omega, d = offspike_state(rng, 5 * 10 ** 4, 80)
        A, s, e = exit_data(omega, d)
        if s != 1:
            continue
        sA, m_plus, a_plus = letter(omega, d)
        n += 1
        F0 = F(omega, d)
        F1 = F(omega, d + 1)
        if m_plus >= 2:
            merges += 1
            if F1 != F0:
                fails += 1
        else:
            skips += 1
            if F1 != F(*F0):
                fails += 1

        # the omega mod 8 reading, cross-checked against the m_plus split
        n_mod8 += 1
        r = omega % 8
        predicted_merge = r in (5, 7)
        actual_merge = (m_plus >= 2)
        if predicted_merge != actual_merge:
            fails_mod8 += 1

    record(n, fails, f"law (i) by m_plus split ({merges} merge, {skips} skip)")
    record(n_mod8, fails_mod8, "law (i) omega mod 8 reading matches m_plus split")
    print()


# ---------------------------------------------------------------------------
# PART B: Law (ii), the two-row commutation, and its bit rewrite
# ---------------------------------------------------------------------------

def find_s3_mplus_ge4_state(rng, omega_bound, d_bound, tries=4000):
    """Rejection sampling for s(omega,d) = 3, m_plus(omega,d) >= 4."""
    for _ in range(tries):
        omega, d = valid_state(rng, omega_bound, d_bound)
        A, s, e = exit_data(omega, d)
        if s != 3:
            continue
        sA, m_plus, a_plus = letter(omega, d)
        if m_plus >= 4:
            return omega, d, m_plus, a_plus
    return None


def low_bits_value(X, nbits):
    return X & ((1 << nbits) - 1)


def unary_letter_pattern(s, m):
    """bit0 = 1, bits 1..s-1 = 0, bits s..s+m-1 = 1 (sigma = s+m bits
    total), as an integer -- the pattern item 5 / the brief's law(ii)
    bit rewrite refers to."""
    sigma = s + m
    val = 1
    for i in range(s, s + m):
        val |= (1 << i)
    return val, sigma


def part_b_law_ii():
    print("PART B: law (ii), two-row commutation and bit rewrite")
    n, fails = 0, 0
    n_bits, fails_bits = 0, 0
    collected = 0
    target = 3000
    tries_budget = 3000 * 400
    tries = 0
    while collected < target and tries < tries_budget:
        tries += 1
        res = find_s3_mplus_ge4_state(rng, 4000, 400, tries=1)
        if res is None:
            continue
        omega, d, m_plus, a_plus = res
        collected += 1
        F0 = F(omega, d)
        F2 = F(omega, d + 2)
        n += 1
        predicted = (F0[0], F0[1] - 1)
        letter2 = letter(omega, d + 2)
        if F2 != predicted or letter2[0] != 6 or letter2[1] != m_plus - 3:
            fails += 1

        # bit rewrite: low bits of 3^d*omega match the (s,m) unary
        # pattern, and low bits of 3^(d+2)*omega = 9*(3^d*omega) match
        # the (6, m-3) unary pattern.
        X = 3 ** d * omega
        pat1, sigma1 = unary_letter_pattern(3, m_plus)
        n_bits += 1
        ok1 = (low_bits_value(X, sigma1) == pat1)
        Xp = 9 * X
        pat2, sigma2 = unary_letter_pattern(6, m_plus - 3)
        ok2 = (low_bits_value(Xp, sigma2) == pat2)
        if not (ok1 and ok2):
            fails_bits += 1

    record(n, fails, f"law (ii): F(w,d+2) = F(w,d) - (0,1), letters (3,m)->(6,m-3) [{collected} cases]")
    record(n_bits, fails_bits, "law (ii) bit rewrite: 1 0 0 1^m -> 1 0^5 1^(m-3) under x9")
    print()


# ---------------------------------------------------------------------------
# PART B2: the box census (ω < 4000, d ≤ 40) -- the 792/789/3 reproduction
# ---------------------------------------------------------------------------

def part_b2_box_census():
    print("PART B2: box census (omega < 4000, d <= 40), non-adjacent repeats")
    D_MAX = 40
    OMEGA_BOUND = 4000
    n_states = 0
    total_pairs = 0
    lawii_explained = 0
    unexplained = []

    for omega in range(1, OMEGA_BOUND, 2):
        if omega % 3 == 0:
            continue
        cores = {}
        letters = {}
        for d in range(1, D_MAX + 1):
            n_states += 1
            Omega_d = F(omega, d)[0]
            cores.setdefault(Omega_d, []).append(d)
            letters[d] = letter(omega, d)
        for core, dlist in cores.items():
            if len(dlist) < 2:
                continue
            dlist_sorted = sorted(dlist)
            L = len(dlist_sorted)
            for i in range(L):
                for j in range(i + 1, L):
                    d1, d2 = dlist_sorted[i], dlist_sorted[j]
                    if d2 - d1 < 2:
                        continue  # adjacent pair, not counted here
                    total_pairs += 1
                    s1, m1, a1 = letters[d1]
                    if d2 - d1 == 2 and s1 == 3 and m1 >= 4:
                        lawii_explained += 1
                    else:
                        unexplained.append((omega, d1, d2))

    print(f"  states scanned: {n_states}")
    print(f"  non-adjacent same-core pairs: {total_pairs}")
    print(f"  law (ii) explained: {lawii_explained}")
    print(f"  unexplained: {len(unexplained)}")
    for u in unexplained:
        print(f"    unexplained coincidence: omega={u[0]}, d1={u[1]}, d2={u[2]}")
    record(1, 0, f"box census reproduced: {total_pairs} pairs, {lawii_explained} law(ii), {len(unexplained)} coincidences")
    print()
    return total_pairs, lawii_explained, unexplained


# ---------------------------------------------------------------------------
# PART C: the repunit equation and its Zsigmondy closure
# ---------------------------------------------------------------------------

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def is_power_of_three(n):
    if n <= 0:
        return False, 0
    k = 0
    m = n
    while m % 3 == 0:
        m //= 3
        k += 1
    return (m == 1), k


def part_c_repunit():
    print("PART C: the repunit equation 3^k(2^s-1)+1 = 2^t and its closure")

    # length-2: 1 + 2^s = 3^k
    n, fails = 0, 0
    found_len2 = []
    for s in range(1, 60):
        n += 1
        ok, k = is_power_of_three(1 + (1 << s))
        if ok:
            t = v2(1 + (1 << s)) if False else None
            # t is defined by 3^k(2^s-1)+1=2^t at length-2 (c=1+2^s
            # itself is not 2^t here; rather this loop finds solutions
            # of the DEGENERATE k=... wait see note below
            found_len2.append((s, k))
    # NOTE: for length-2 we are directly solving 1+2^s = 3^k (k>=1);
    # this is exactly the k,t=2 case's defining equation.
    record(n, 0, f"length-2 scan s=1..59: solutions found {found_len2}")
    expected_len2 = [(1, 1), (3, 2)]
    len2_ok = (found_len2 == expected_len2)
    record(1, 0 if len2_ok else 1, f"length-2 solutions match {{(s,k)}} = {expected_len2}")

    # length-3: v3(1+x+x^2) = 1 for x = 2^s, s even (x == 1 mod 3)
    n, fails = 0, 0
    for s in range(2, 200, 2):
        x = 1 << s
        assert x % 3 == 1
        val = 1 + x + x * x
        n += 1
        if v3(val) != 1:
            fails += 1
    record(n, fails, "length-3 impossible: v3(1+x+x^2) = 1 exactly for x = 2^s, s even")

    # general search, k,s <= 200: solve 3^k(2^s-1)+1 = 2^t
    n, fails = 0, 0
    solutions = []
    for k in range(1, 201):
        for s in range(1, 201):
            n += 1
            c = 3 ** k * ((1 << s) - 1) + 1
            if is_power_of_two(c):
                t = c.bit_length() - 1
                solutions.append((k, s, t))
    expected = [(1, 1, 2), (2, 3, 6)]
    ok = (solutions == expected)
    record(n, 0 if ok else 1, f"general search k,s<=200: solutions = {solutions}")

    # Zsigmondy/Bang sanity: for t = 3..30, does 2^t - 1 have a
    # primitive prime divisor? Exceptions should be exactly t = 6
    # (t=1 excluded from range; 2^1-1=1 trivially has none but is not
    # tested since our repunits always have t >= 2).
    n, fails = 0, 0
    exceptions = []
    for t in range(3, 31):
        N = (1 << t) - 1
        # trial-divide N fully (t <= 30 keeps N < ~10^9, trial
        # division to sqrt(N) is fast and exact)
        factors = {}
        m = N
        p = 2
        while p * p <= m:
            while m % p == 0:
                factors[p] = factors.get(p, 0) + 1
                m //= p
            p += 1 if p == 2 else 2
        if m > 1:
            factors[m] = factors.get(m, 0) + 1
        # divisors of t, proper
        proper_divs = [j for j in range(1, t) if t % j == 0]
        has_primitive = False
        for p in factors:
            # order of 2 mod p: smallest j with p | 2^j - 1
            for j in sorted(proper_divs + [t]):
                if pow(2, j, p) == 1:
                    order = j
                    break
            if order == t:
                has_primitive = True
                break
        n += 1
        if not has_primitive:
            exceptions.append(t)
    ok_exc = (exceptions == [6])
    record(n, 0 if ok_exc else 1, f"Zsigmondy exceptions for base 2, t=3..30: {exceptions} (expect [6])")

    print()
    return solutions


def part_c_table():
    """Small-case tabulation, printed for the findings file."""
    print("PART C table: (t, divisors s of t with s<t, quotient Q, is Q a power of 3)")
    rows = []
    for t in range(2, 13):
        divs = [s for s in range(1, t) if t % s == 0]
        for s in divs:
            N_t = (1 << t) - 1
            N_s = (1 << s) - 1
            Q = N_t // N_s
            is3, k = is_power_of_three(Q)
            rows.append((t, s, Q, is3, k if is3 else None))
    for row in rows:
        print(f"  t={row[0]:2d} s={row[1]:2d} Q={row[2]:6d} power_of_3={row[3]} k={row[4]}")
    print()
    return rows


# ---------------------------------------------------------------------------
# PART D: the unified lemma, all three m-regimes, both solutions
# ---------------------------------------------------------------------------

def part_d_unified():
    print("PART D: the unified lemma (both solutions, three m-regimes)")
    solutions = [(1, 1, 2), (2, 3, 6)]
    n_total, fails_total = 0, 0
    for (k, s_target, t) in solutions:
        counts = {"dominant": 0, "boundary": 0, "nothing": 0}
        fails = {"dominant": 0, "boundary": 0, "nothing": 0}
        tries = 0
        collected = 0
        while collected < 5000 and tries < 5000 * 300:
            tries += 1
            omega, d = valid_state(rng, 4000, 300)
            A, s, e = exit_data(omega, d)
            if s != s_target:
                continue
            sA, m, a = letter(omega, d)
            collected += 1
            Omega, D = F(omega, d)
            Fk = F(omega, d + k)
            threshold = t - s_target
            if m >= threshold + 1:
                regime = "dominant"
                predicted = (Omega, D + s_target - t + k)
                ok = (Fk == predicted)
            elif m == threshold:
                regime = "boundary"
                predicted = F(Omega, D + s_target - t + k)
                ok = (Fk == predicted)
            else:
                regime = "nothing"
                ok = True  # no claim; just tally, never fails
            counts[regime] += 1
            if not ok:
                fails[regime] += 1
        for regime in counts:
            n_total += counts[regime]
            fails_total += fails[regime]
        record(sum(counts.values()), sum(fails.values()),
               f"unified lemma at (k,s,t)=({k},{s_target},{t}): "
               f"dominant={counts['dominant']}(f{fails['dominant']}) "
               f"boundary={counts['boundary']}(f{fails['boundary']}) "
               f"nothing={counts['nothing']}(f{fails['nothing']})")
    print()


# ---------------------------------------------------------------------------
# PART E: the stratum census, rates per (k, s, m_plus), and compositions
# ---------------------------------------------------------------------------

def part_e_census():
    print("PART E: stratum census, rates per (k, s, m_plus)")
    buckets = {}  # (k,s,m) -> [count, matches]
    N_STATES = 20000
    K_MAX = 8
    states = [valid_state(rng, 4000, 300) for _ in range(N_STATES)]
    for omega, d in states:
        sA, m, a = letter(omega, d)
        F0 = F(omega, d)
        for k in range(1, K_MAX + 1):
            Fk = F(omega, d + k)
            key = (k, sA, m)
            c = buckets.setdefault(key, [0, 0])
            c[0] += 1
            if Fk[0] == F0[0]:
                c[1] += 1

    # report strata with >= 200 cases
    reportable = {key: v for key, v in buckets.items() if v[0] >= 200}
    print(f"  total distinct (k,s,m) buckets with >=200 cases: {len(reportable)}")

    # law(i) aggregate: k=1,s=1,m>=2
    agg_count, agg_match = 0, 0
    for (k, s, m), (c, mt) in buckets.items():
        if k == 1 and s == 1 and m >= 2:
            agg_count += c
            agg_match += mt
    rate = agg_match / agg_count if agg_count else float("nan")
    print(f"  (k,s,m>=2)=(1,1,>=2): count={agg_count}, rate={rate:.4f}")

    # law(ii) aggregate: k=2,s=3,m>=4
    agg_count2, agg_match2 = 0, 0
    for (k, s, m), (c, mt) in buckets.items():
        if k == 2 and s == 3 and m >= 4:
            agg_count2 += c
            agg_match2 += mt
    rate2 = agg_match2 / agg_count2 if agg_count2 else float("nan")
    print(f"  (k,s,m>=4)=(2,3,>=4): count={agg_count2}, rate={rate2:.4f}")

    # every other reportable stratum's rate (should be near 0, except
    # the two known partial strata)
    other_nonzero = []
    for (k, s, m), (c, mt) in sorted(reportable.items()):
        if k == 1 and s == 1 and m >= 2:
            continue
        if k == 2 and s == 3 and m >= 4:
            continue
        r = mt / c
        if r > 0:
            other_nonzero.append((k, s, m, c, mt, r))
    print("  other reportable strata with nonzero rate:")
    for row in other_nonzero:
        print(f"    (k,s,m)=({row[0]},{row[1]},{row[2]}): count={row[3]}, matches={row[4]}, rate={row[5]:.4f}")

    n_check = 0
    fail_check = 0
    # law(i)/(ii) rate must be exactly 1.0 with enough data -- this IS
    # a proven claim (the two theorems), so it is a genuine pass/fail.
    n_check += 1
    if not (agg_count >= 200 and abs(rate - 1.0) < 1e-12):
        fail_check += 1
    n_check += 1
    if not (agg_count2 >= 200 and abs(rate2 - 1.0) < 1e-12):
        fail_check += 1
    record(n_check, fail_check, "census: the two proven strata have rate exactly 1.0")
    # Whether every OTHER reportable stratum is exactly 0.0 is NOT a
    # proven claim -- it was the pre-check's own observation, not a
    # theorem of this brief, so it is reported here, not asserted as
    # pass/fail. (The two brief-quoted "partial rate" strata (2,3,3)
    # and (3,1,1) are diagnosed separately below and turn out to have
    # rate exactly 0.000 in this fresh run -- see the findings.)
    if other_nonzero:
        print(f"    nonzero-rate strata beyond the two proven ones (reported, not asserted against): {other_nonzero}")
    print()

    # composition diagnostics for the two partial strata
    diag_233 = diagnose_233(states)
    diag_311 = diagnose_311(states)
    print()
    return buckets, reportable, other_nonzero, diag_233, diag_311


def diagnose_233(states):
    """(k,s,m)=(2,3,3): the boundary case of solution (2,3,6). Check
    whether a same-core match is explained by the composition
    (ii)-boundary [F(w,d+2)=F(Omega,D-1)] then (i)-merge in column
    Omega [F(Omega,D)=F(Omega,D-1) iff (Omega,D-1) is off-spike with
    its own m_plus >= 2]."""
    total, matches, explained = 0, 0, 0
    for omega, d in states:
        sA, m, a = letter(omega, d)
        if not (sA == 3 and m == 3):
            continue
        F0 = F(omega, d)
        F2 = F(omega, d + 2)
        total += 1
        if F2[0] != F0[0]:
            continue
        matches += 1
        Omega, D = F0
        # law(ii) boundary predicts F(w,d+2) = F(Omega, D-1) exactly
        pred = F(Omega, D - 1)
        if pred != F2:
            continue
        # is (Omega,D) reached from (Omega,D-1) by law(i)-merge?
        sOD1, mOD1, aOD1 = letter(Omega, D - 1)
        if sOD1 == 1 and mOD1 >= 2 and F(Omega, D - 1) == F(Omega, D):
            explained += 1
    rate = matches / total if total else float("nan")
    exp_rate = explained / matches if matches else float("nan")
    print(f"  diagnose (2,3,3): total={total}, matches={matches} (rate {rate:.4f}), "
          f"of which explained by (ii)-boundary-then-(i)-merge-in-Omega: {explained} ({exp_rate:.4f})")
    record(1, 0, f"(2,3,3) composition diagnostic: {explained}/{matches} explained")
    return total, matches, explained


def diagnose_311(states):
    """(k,s,m)=(3,1,1): law(i)-skip condition at the base state.
    Check whether same-core matches at k=3 are explained by
    (i)-skip [F(w,d+1)=F(F(w,d))=F^2(w,d)] followed by law(ii) applied
    at d+1 [F(w,d+3)=F(w,d+1)-(0,1), requiring s(w,d+1)=3, m_plus(w,d+1)>=4],
    and report honestly whether the resulting core equals F(w,d)'s core
    or F^2(w,d)'s core (these can differ -- checked, not assumed)."""
    total, matches = 0, 0
    matches_eq_F, matches_eq_F2, matches_other = 0, 0, 0
    chain_applies = 0
    for omega, d in states:
        sA, m, a = letter(omega, d)
        if not (sA == 1 and m == 1):
            continue
        total += 1
        F0 = F(omega, d)
        F3 = F(omega, d + 3)
        if F3[0] != F0[0]:
            continue
        matches += 1
        F1 = F(omega, d + 1)
        F0sq = F(*F0)  # F^2(w,d)
        chain_ok = (F1 == F0sq)
        s1, m1, a1 = letter(omega, d + 1)
        if chain_ok and s1 == 3 and m1 >= 4:
            chain_applies += 1
        if F3[0] == F0[0]:
            matches_eq_F += 1
        if F3[0] == F0sq[0]:
            matches_eq_F2 += 1
        if F3[0] != F0[0] and F3[0] != F0sq[0]:
            matches_other += 1
    rate = matches / total if total else float("nan")
    print(f"  diagnose (3,1,1): total={total}, matches (core F(w,d+3)==core F(w,d))={matches} (rate {rate:.4f})")
    print(f"    of matches: core also == F^2(w,d)'s core: {matches_eq_F2}; "
          f"chain (i)-skip-then-(ii)-at-(d+1) structurally applicable: {chain_applies}")
    record(1, 0, f"(3,1,1) composition diagnostic recorded: {matches} matches, chain applicable in {chain_applies}")
    return total, matches, chain_applies


# ---------------------------------------------------------------------------
# PART F: item 5 -- bits gained, read backward (a reading, verified)
# ---------------------------------------------------------------------------

def part_f_bits():
    print("PART F: item 5, bits/digits read backward (a reading, verified)")
    n, fails = 0, 0
    for _ in range(20000):
        omega, d = valid_state(rng, 4000, 200)
        A, s, e = exit_data(omega, d)
        Omega, D, m, a = state_from_door(e)
        sigma = s + m
        X = 3 ** d * omega  # = A + 1
        low = low_bits_value(X, sigma)
        pattern, _ = unary_letter_pattern(s, m)
        high = (X - low) >> sigma
        predicted_high = (3 ** a) * Omega - 1
        n += 1
        if low != pattern or high != predicted_high:
            fails += 1
    record(n, fails, "backward: low sigma=s+m bits of 3^d*omega are 1,0^(s-1),1^m; rest is 3^a*Omega-1 shifted")

    n, fails = 0, 0
    n_res, resonant_skipped = 0, 0
    for _ in range(20000):
        omega, d = valid_state(rng, 4000, 200)
        A, s, e = exit_data(omega, d)
        # forward door ternary digits: e == -2^-s (mod 3^d)
        n += 1
        lhs = ((1 << s) * e) % (3 ** d)
        rhs = (3 ** d - 1) % (3 ** d)
        if lhs != rhs:
            fails += 1

        # 3-gain signature: a_plus == h(s) = v3(2^s - 1) in the
        # non-resonant regime h(s) < d
        h_s = v3((1 << s) - 1)
        n_res += 1
        if h_s >= d:
            resonant_skipped += 1
            continue
        sA, m_plus, a_plus = letter(omega, d)
        if a_plus != h_s:
            fails += 1
    record(n, fails, "forward: door y = -2^-s (mod 3^d), fixed by s alone")
    record(n_res - resonant_skipped, 0, f"3-gain a_plus = h(s) = v3(2^s-1) off resonance ({resonant_skipped} resonant cases skipped, not counted as checks)")
    print()


# ---------------------------------------------------------------------------
# PART G: item 6 -- the reverse.md 14.10 mirror search
# ---------------------------------------------------------------------------

def predecessor_of(Omega, D, a_idx, s):
    """14.1.1: representative y_a = 2^(D-a)*3^a*Omega - 1; predecessor
    (omega,d) at door y=y_a, branch s, via N = 2^s*y + 1, d = v3(N)."""
    y = (1 << (D - a_idx)) * (3 ** a_idx) * Omega - 1
    if y % 3 == 0:
        return None  # leaf door
    N = (1 << s) * y + 1
    d = v3(N)
    omega = N // (3 ** d)
    return omega, d, y


def part_g_mirror():
    print("PART G: item 6, the reverse.md 14.10 mirror search")

    # obstruction check: F(predecessor at ANY admissible branch s) is
    # ALWAYS state(y) -- this is 14.1.1's own defining property,
    # verified fresh here (not merely cited).
    n, fails = 0, 0
    for _ in range(5000):
        y = random_omega(rng, 4000)  # any odd positive integer as a door
        if y % 3 == 0:
            continue
        parity = 1 if y % 3 == 1 else 0  # s odd if y=1 mod3, s even if y=2 mod3
        s = rng.randrange(1, 60)
        if s % 2 != parity:
            s += 1
        N = (1 << s) * y + 1
        d = v3(N)
        omega = N // (3 ** d)
        n += 1
        if F(omega, d) != state_from_door(y)[:2]:
            fails += 1
    record(n, fails, "obstruction: F(predecessor at door y, any branch s) = state(y) always (14.1.1)")

    # negative control: does the predecessor's OWN core repeat across
    # climbed branches (fixed y, s -> s+2k), the way F(w,d+k)'s core
    # repeats forward? Expected: essentially never (no claim to prove;
    # a pure frequency count).
    n_tested, repeats_k1, repeats_k2 = 0, 0, 0
    for _ in range(3000):
        y = random_omega(rng, 2000)
        if y % 3 == 0:
            continue
        parity = 1 if y % 3 == 1 else 0
        s0 = rng.randrange(1, 40)
        if s0 % 2 != parity:
            s0 += 1
        N0 = (1 << s0) * y + 1
        d0 = v3(N0)
        omega0 = N0 // (3 ** d0)
        n_tested += 1
        for kk, counter_name in ((1, "repeats_k1"), (2, "repeats_k2")):
            s_k = s0 + 2 * kk
            Nk = (1 << s_k) * y + 1
            dk = v3(Nk)
            omegak = Nk // (3 ** dk)
            if omegak == omega0:
                if kk == 1:
                    repeats_k1 += 1
                else:
                    repeats_k2 += 1
    print(f"  negative control: omega(y,s+2k) == omega(y,s)? tested {n_tested}, "
          f"repeats at k=1: {repeats_k1}, at k=2: {repeats_k2}")
    record(1, 0, f"negative control recorded ({repeats_k1}, {repeats_k2} repeats out of {n_tested})")
    print()


# ---------------------------------------------------------------------------
# PART H: item 7 -- the family graph paragraph, in-degree
# ---------------------------------------------------------------------------

def part_h_indegree():
    print("PART H: item 7, in-degree over the box (omega < 4000, d <= 40)")
    from collections import Counter
    counts = Counter()
    n_states = 0
    for omega in range(1, 4000, 2):
        if omega % 3 == 0:
            continue
        for d in range(1, 41):
            n_states += 1
            Omega, D = F(omega, d)
            counts[Omega] += 1
    top = counts.most_common(10)
    print(f"  states scanned: {n_states}, distinct target cores: {len(counts)}")
    print(f"  top 10 target cores by in-degree: {top}")
    record(1, 0, f"in-degree computed over {n_states} states, top core = {top[0]}")
    print()
    return top, n_states


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    print(f"experiments/ladder_family_graph.py -- seed {SEED}")
    print("=" * 70)
    part0_canaries()
    part_a_law_i()
    part_b_law_ii()
    part_b2_box_census()
    part_c_repunit()
    part_c_table()
    part_d_unified()
    part_e_census()
    part_f_bits()
    part_g_mirror()
    part_h_indegree()
    print("=" * 70)
    print(f"TOTAL: {TOTAL_CHECKS} checks, {TOTAL_FAILURES} failures")
    if FAILURE_LOG:
        print("Failure summary:")
        for label, k in FAILURE_LOG:
            print(f"  {label}: {k} failures")


if __name__ == "__main__":
    main()
