"""Independent verification for ladder.md 15.6 (the tear afterlife).

Supports the seven statements of ladder.md 15.6, re-derived from the numerator
identity `A(w,d+1) = 3*A(w,d) + 2` (ladder.md 15.1) and the definitions of
spine.md Section 7 (the reduced map `F`), stage3.md 11.8.6.3 (the entry-depth
law), stage4.md 11.8.7.1-11.8.7.7 (the anchor `M(w)`, the digit cost
`sigma = s + m_+`), reverse.md 14.10 (the dual ladder) and 14.14.1.1 (the cost
identity), and stage2.md 11.8.5.6.1 (`M(w) = N(w^2)`):

  1. The torn state: at a spike s >= 3, F(w,d+1) = (3*2^(s-2)*e+1, 1), entry
     depth 1, no 3-gain, torn core = 1 (mod 2^(s-2)). s = 2 is a boundary case
     (entry depth >= 2).
  2. The opening run: the torn state's reduced word opens with exactly
     floor((s-1)/2) letters (1,1), ending at a depth-1 core = 5 (mod 8) [s
     even] or = 3 (mod 4) [s odd].
  3. The torn core's anchor: v2(M(Omega')) = s-4 for s >= 5, and the column of
     Omega' coincides with the column of 1 at every depth d' with
     v2(d') < s-4 (checked as an exact-integer statement, s(Omega',d') =
     s(1,d'), needing no anchor computation for the coincidence itself; the
     anchor valuation v2(M(Omega')) = s-4 is checked separately by digit-by-
     digit discrete log).
  4. The mirror tear: reverse.md 14.10.1's d >= 2 branch, fresh re-check,
     plus the reading Omega(y,s+2) = -1 (mod 3^(d-1)).
  6. Measured, not proved: the upper-sister non-return measurement, the
     one- and two-step sign lemma (T(e) < e' and T(T(e)) < e', checked as an
     exact inequality, not just non-equality), the reverse-direction and
     merge-point measurements, all with bounds printed.
  7. The tear-lines as level sets: the elementary identity s(w,d) >= k iff
     w = 3^(-d) (mod 2^k), plus the one-step total-variation measurement
     against uniform on height-k tear-lines, at k = 8, 12, 16, against the
     sampling noise floor (TV of a same-size uniform draw against uniform).

Item 5 (two metrics, one calibration) and item 8 (off-spike, out of scope for
this brief) are prose remarks with no independent numerical content beyond
items 1, 2, 4 and 7 above; they are not separately checked here.

Fresh code: imports nothing from any other file in this repository (not
ladder.py, not ladder_targetshift.py, not mirror_baker_cap.py -- every
primitive below, including the anchor's digit-by-digit discrete log, is
reimplemented from the definitions). Exact integer arithmetic at every
pass/fail decision that does not inherently involve a truncated anchor
residue; anchor residues are computed to an explicit, generous precision
(B = 96 bits), far above every valuation actually compared (s <= 30 in every
phase here), so a nonzero residue's valuation is exact.

Canaries first: (1,1) (the trivial fixed point / the only known cycle
realized on the positive-only domain of F); the two independently published
worked examples of stage3.md 11.8.6.3 -- (w,d) = (1,4) [A=80, s=4, m_+=1] and
(17,2) [A=152, s=3, m_+=2] -- used in place of the literal three known
T-cycles, which live on the negative/signed extension outside this brief's
required context (reverse.md 14.10/14.14.1 and stage3/stage4 only); and the
ladder law itself (15.1.1) on 500 random states.

Run: python experiments/ladder_afterlife.py   (single command, no flags,
reproduces this file's committed output in full; all phases run, ~1-2
minutes.)
"""

import random

SEED = 20260913
random.seed(SEED)

B = 96              # bits of 2-adic precision for anchor computations
MODB_FULL = 1 << (B + 3)


# ---------------------------------------------------------------------------
# Core reduced-map primitives (fresh; nothing imported from the repo).
# ---------------------------------------------------------------------------

def v2(n):
    """Exact 2-adic valuation of a nonzero integer."""
    assert n != 0
    return (n & -n).bit_length() - 1


def v3(n):
    """Exact 3-adic valuation of a nonzero integer."""
    assert n != 0
    t = 0
    while n % 3 == 0:
        n //= 3
        t += 1
    return t


def valid_core(w):
    return w % 2 == 1 and w % 3 != 0


def exit_data(w, d):
    """Exact (s, e) for state (w,d): A = 3^d*w - 1 = 2^s*e, e odd (spine 7)."""
    A = 3 ** d * w - 1
    s = v2(A)
    return s, A >> s


def next_state(w, d):
    """One reduced step F(w,d) -> (Omega, D); also returns (s,e,m,a)."""
    s, e = exit_data(w, d)
    x = e + 1
    m = v2(x)
    u = x >> m
    a = v3(u) if u % 3 == 0 else 0
    Omega = u // (3 ** a)
    D = m + a
    return Omega, D, s, e, m, a


def T(x):
    """The odd-to-odd Collatz map."""
    y = 3 * x + 1
    return y >> v2(y)


def anchor_N(u_res, bits):
    """N(u) mod 2^bits, for u = 1 (mod 8) given as a residue mod 2^(bits+3).

    Digit-by-digit discrete log base 9 in the cyclic group 1+8Z/2^(bits+3):
    9^N = u^(-1) (mod 2^(bits+3)); bit t of N is fixed at level 2^(t+4).
    Independent reimplementation of the technique used (for N) in
    experiments/ladder_targetshift.py -- written fresh here, for M.
    """
    assert u_res % 8 == 1
    m_full = 1 << (bits + 3)
    target = pow(u_res, -1, m_full)
    N = 0
    for t in range(bits):
        m = 1 << (t + 4)
        if pow(9, N, m) != target % m:
            N += 1 << t
    assert pow(9, N, m_full) == target
    return N


def anchor_M(w, bits):
    """M(w) mod 2^bits = N(w^2) mod 2^bits (stage2.md 11.8.5.6.1), any odd w."""
    m_full = 1 << (bits + 3)
    wsq = (w * w) % m_full
    return anchor_N(wsq, bits)


# ---------------------------------------------------------------------------
# Canaries
# ---------------------------------------------------------------------------

def run_canaries():
    checks = failures = 0

    # (1,1): trivial fixed point.
    checks += 1
    Om, D, s, e, m, a = next_state(1, 1)
    if not (Om == 1 and D == 1 and s == 1 and e == 1):
        failures += 1
        print("  CANARY FAIL (1,1):", Om, D, s, e)

    # stage3.md 11.8.6.3 worked example: (w,d) = (1,4), A=80, s=4, m_+=1.
    checks += 1
    s, e = exit_data(1, 4)
    Om, D, s2, e2, m, a = next_state(1, 4)
    if not (s == 4 and e == 5 and m == 1):
        failures += 1
        print("  CANARY FAIL (1,4):", s, e, m)

    # stage3.md 11.8.6.3 worked example: (w,d) = (17,2), A=152, s=3, m_+=2.
    checks += 1
    s, e = exit_data(17, 2)
    Om, D, s2, e2, m, a = next_state(17, 2)
    if not (s == 3 and e == 19 and m == 2):
        failures += 1
        print("  CANARY FAIL (17,2):", s, e, m)

    # Ladder law 15.1.1 on 500 random states (foundation of everything below).
    n1 = n2 = bad = 0
    for _ in range(500):
        w = random.randrange(1, 10 ** 6, 2)
        if not valid_core(w):
            continue
        d = random.randrange(1, 40)
        s, e = exit_data(w, d)
        s1, e1 = exit_data(w, d + 1)
        checks += 1
        if s == 1:
            n1 += 1
            if e1 != T(e):
                bad += 1
        else:
            n2 += 1
            if not (e1 == 3 * 2 ** (s - 1) * e + 1 and s1 == 1):
                bad += 1
    failures += bad
    print(f"  ladder law 15.1.1: {n1} off-spike + {n2} spike states, {bad} failures")

    return checks, failures


# ---------------------------------------------------------------------------
# Item 1: the torn state.
# ---------------------------------------------------------------------------

def random_spike(rng, w_max=2 * 10 ** 6, d_max=40, s_min=3):
    """A random valid (w,d) with s(w,d) >= s_min, by rejection."""
    while True:
        w = rng.randrange(1, w_max, 2)
        if not valid_core(w):
            continue
        d = rng.randrange(1, d_max)
        s, e = exit_data(w, d)
        if s >= s_min:
            return w, d, s, e


def check_item1(rng, n=8000):
    """F(w,d+1) = (3*2^(s-2)*e+1, 1) for s >= 3; s = 2 boundary has m_+ >= 2."""
    tested = failures = 0
    spikes3 = spikes2 = 0
    for _ in range(n):
        w, d, s, e = random_spike(rng, s_min=2)
        tested += 1
        s1, e1 = exit_data(w, d + 1)
        ekick = 3 * 2 ** (s - 1) * e + 1
        ok = (s1 == 1 and e1 == ekick)
        Om, D, s2, e2, m2, a2 = next_state(w, d + 1)
        if s >= 3:
            spikes3 += 1
            pred_Om = 3 * 2 ** (s - 2) * e + 1
            ok = ok and (Om == pred_Om and D == 1 and m2 == 1 and a2 == 0)
            ok = ok and ((Om - 1) % (2 ** (s - 2)) == 0)
        else:  # s == 2 boundary: bracket 3e+1 is even, entry depth >= 2
            spikes2 += 1
            bracket = 3 * e + 1
            ok = ok and (bracket % 2 == 0) and (m2 >= 2)
        if not ok:
            failures += 1
    return tested, spikes3, spikes2, failures


# ---------------------------------------------------------------------------
# Item 2: the opening run.
# ---------------------------------------------------------------------------

def check_item2(rng, n=6000, w_max=5 * 10 ** 7, d_max=12):
    """Torn state's word opens with exactly floor((s-1)/2) letters (1,1)."""
    tested = failures = 0
    for _ in range(n):
        w, d, s, e = random_spike(rng, w_max=w_max, d_max=d_max, s_min=3)
        tested += 1
        cw, cd = w, d + 1
        cnt = 0
        while True:
            Om, D, ss, ee, mm, aa = next_state(cw, cd)
            if ss == 1 and mm == 1:
                cnt += 1
                cw, cd = Om, D
            else:
                break
        pred = (s - 1) // 2
        ok = (cnt == pred)
        if s % 2 == 0:
            ok = ok and (cw % 8 == 5)
        else:
            ok = ok and (cw % 4 == 3)
        if not ok:
            failures += 1
    return tested, failures


# ---------------------------------------------------------------------------
# Item 3: the torn core's anchor.
# ---------------------------------------------------------------------------

def check_item3(rng, n_spikes=400, dprime_max=400):
    """v2(M(Omega')) = s-4 for s>=5 (anchor check), and s(Omega',d')=s(1,d')
    for every d' with v2(d') < s-4 (pure-integer coincidence check)."""
    anchor_tested = anchor_failures = 0
    coin_tested = coin_failures = 0
    boundary_tested = boundary_matches = 0
    for _ in range(n_spikes):
        w, d, s, e = random_spike(rng, w_max=10 ** 6, d_max=30, s_min=5)
        Omega_p = 3 * 2 ** (s - 2) * e + 1

        # Anchor valuation check: v2(M(Omega') mod 2^B) == s - 4.
        anchor_tested += 1
        assert s - 4 < B, "s too large for chosen anchor precision"
        Mval = anchor_M(Omega_p, B)
        r = Mval % (1 << B)
        if r == 0 or v2(r) != s - 4:
            anchor_failures += 1

        # Column-coincidence check, exact integers only, no anchor needed.
        for dprime in range(1, dprime_max):
            vd = v2(dprime)
            s_om, _ = exit_data(Omega_p, dprime)
            s_1, _ = exit_data(1, dprime)
            if vd < s - 4:
                coin_tested += 1
                if s_om != s_1:
                    coin_failures += 1
            elif vd == s - 4:
                boundary_tested += 1
                if s_om == s_1:
                    boundary_matches += 1
    return (anchor_tested, anchor_failures,
            coin_tested, coin_failures,
            boundary_tested, boundary_matches)


# ---------------------------------------------------------------------------
# Item 4: the mirror tear (reverse.md 14.10.1, fresh re-check).
# ---------------------------------------------------------------------------

def check_item4(rng, n=8000, y_bound=2 * 10 ** 6, s_max=30):
    """Theorem 14.10.1 on random (y,s), both branches; the d>=2 branch's
    reading Omega(y,s+2) = -1 (mod 3^(d-1))."""
    tested = failures = 0
    d1 = d2 = 0
    for _ in range(n):
        y = rng.randrange(-y_bound, y_bound)
        if y % 2 == 0 or y % 3 == 0:
            continue
        s = rng.randrange(1, s_max)
        N = 2 ** s * y + 1
        if N == 0 or N % 3 != 0:
            continue
        d = v3(N)
        w = N // (3 ** d)
        tested += 1
        Nprime = 4 * N - 3
        assert Nprime == 2 ** (s + 2) * y + 1
        dprime = v3(Nprime)
        wprime = Nprime // (3 ** dprime)
        if d == 1:
            d1 += 1
            # T3 branch: wprime = (4w-1)/3^v3(4w-1), dprime = 1+v3(4w-1)
            bracket = 4 * w - 1
            vb = v3(bracket) if bracket % 3 == 0 else 0
            ok = (dprime == 1 + vb) and (wprime == bracket // (3 ** vb))
        else:
            d2 += 1
            pred_w = 4 * (3 ** (d - 1)) * w - 1
            ok = (wprime == pred_w) and (dprime == 1)
            ok = ok and (pred_w % (3 ** (d - 1)) == (3 ** (d - 1) - 1))  # = -1
        if not ok:
            failures += 1
    return tested, d1, d2, failures


# ---------------------------------------------------------------------------
# Item 6: measured, not proved.
# ---------------------------------------------------------------------------

def check_item6(rng, n=4000, e_max=10 ** 6, s_max=20, orbit_bound=200):
    """(a) sign lemma, exact inequality: T(e) < e' and T(T(e)) < e' always.
    (b) bounded non-return measurement: e' never found in the first
        orbit_bound Collatz steps from e.
    (c) reverse measurement: is e found downstream of e' only in the
        drainage basin {1,5,13,23}, as the pre-check claimed? Measured, not
        enforced -- a rare generic (non-basin) hit does occur at this sample
        size (see findings; the pre-check's "only" is corrected to "usually,
        with rare generic coincidental merges outside the basin too").
    (d) merge measurement: the first common value of the two orbits, and
        whether it lies strictly below both e and e'."""
    sign_tested = sign_failures = 0
    nonreturn_tested = nonreturn_failures = 0
    reverse_hits_basin = reverse_hits_other = 0
    merge_found = merge_below_both = merge_total = 0
    basin = {1, 5, 13, 23}

    for _ in range(n):
        e = rng.randrange(1, e_max, 2)
        s = rng.randrange(2, s_max)
        ep = 3 * 2 ** (s - 1) * e + 1

        # (a) sign lemma
        sign_tested += 1
        Te = T(e)
        T2e = T(Te)
        if not (Te < ep and T2e < ep):
            sign_failures += 1

        # (b) non-return: walk e's orbit, e' should never appear
        nonreturn_tested += 1
        x = e
        orbit_e = [x]
        for _ in range(orbit_bound):
            x = T(x)
            orbit_e.append(x)
            if x == ep:
                nonreturn_failures += 1
                break

        # (c) reverse: walk e''s orbit, see if e appears
        y = ep
        orbit_ep = [y]
        hit = False
        for _ in range(orbit_bound):
            y = T(y)
            orbit_ep.append(y)
            if y == e:
                hit = True
                break
        if hit:
            if e in basin:
                reverse_hits_basin += 1
            else:
                reverse_hits_other += 1

        # (d) merge point: first common value of orbit_e and orbit_ep
        merge_total += 1
        set_e = set(orbit_e)
        merge_val = None
        for v in orbit_ep:
            if v in set_e:
                merge_val = v
                break
        if merge_val is not None:
            merge_found += 1
            if merge_val < e and merge_val < ep:
                merge_below_both += 1

    return {
        "sign_tested": sign_tested, "sign_failures": sign_failures,
        "nonreturn_tested": nonreturn_tested,
        "nonreturn_failures": nonreturn_failures,
        "reverse_hits_basin": reverse_hits_basin,
        "reverse_hits_other": reverse_hits_other,
        "merge_total": merge_total, "merge_found": merge_found,
        "merge_below_both": merge_below_both,
        "orbit_bound": orbit_bound,
    }


# ---------------------------------------------------------------------------
# Item 7: tear-lines as level sets.
# ---------------------------------------------------------------------------

def check_item7_identity(rng, n=15000, w_max=10 ** 6, d_max=40, k_max=20):
    """s(w,d) >= k iff w = 3^(-d) (mod 2^k)."""
    tested = failures = 0
    for _ in range(n):
        w = rng.randrange(1, w_max, 2)
        if w % 3 == 0:
            continue
        d = rng.randrange(0, d_max)
        k = rng.randrange(1, k_max)
        s, _ = exit_data(w, d)
        tested += 1
        lhs = (s >= k)
        rhs = (w % (1 << k)) == pow(3, -d, 1 << k)
        if lhs != rhs:
            failures += 1
    return tested, failures


def total_variation(counts, total, num_classes):
    """TV distance of the empirical distribution `counts` (over num_classes
    classes) from uniform, given `total` samples."""
    uniform_p = 1.0 / num_classes
    tv = 0.0
    seen = 0
    for c in counts.values():
        tv += abs(c / total - uniform_p)
        seen += 1
    # classes with zero count contribute |0 - uniform_p| each
    tv += (num_classes - seen) * uniform_p
    return tv / 2.0


def check_item7_tv(rng, k, n_starts, d_fixed=1, hi_blocks=6):
    """One-step TV from uniform mod 2^k, on a height-k tear-line at fixed
    depth d_fixed, plus the noise floor (same-size uniform draw vs uniform).

    States on the line are constructed directly (w = target_res + j*2^k for
    random j), not found by rejection -- rejection sampling against a
    density-2^(1-k) class is exponentially slow for k = 16 and is not used.

    The successor core Omega_+ is always odd (every reduced-state core is,
    by construction), so its residue mod 2^k ranges only over the 2^(k-1)
    odd classes; the comparison distribution is uniform over exactly those
    classes, not over all 2^k residues (the even half is structurally
    unreachable and is not noise).
    """
    modk = 1 << k
    n_classes = modk // 2  # Omega_+ mod modk is always odd: 2^(k-1) possible classes
    target_res = pow(3, -d_fixed, modk)  # the tear-line's residue class
    assert target_res % 2 == 1  # inverse of an odd number mod a power of 2 is odd
    from collections import Counter
    post_counts = Counter()
    noise_counts = Counter()
    hi_max = 1 << (k * hi_blocks)  # ample high-bit freedom above the fixed low bits
    produced = 0
    while produced < n_starts:
        j = rng.randrange(0, hi_max)
        w = target_res + j * modk  # odd automatically: modk even, target_res odd
        if w % 3 == 0:
            continue
        s, _ = exit_data(w, d_fixed)
        assert s >= k  # sanity: this state really is on the height->=k tear-line
        Om, D, s2, e2, m2, a2 = next_state(w, d_fixed)
        post_counts[Om % modk] += 1
        noise_counts[rng.randrange(n_classes) * 2 + 1] += 1  # a random odd residue
        produced += 1
    tv_post = total_variation(post_counts, produced, n_classes)
    tv_noise = total_variation(noise_counts, produced, n_classes)
    return produced, tv_post, tv_noise


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    total_checks = 0
    total_failures = 0

    print(f"ladder_afterlife.py  seed={SEED}  anchor precision B={B} bits")
    print()
    print("=== Canaries ===")
    c, f = run_canaries()
    total_checks += c
    total_failures += f
    print(f"  canaries: {c} checks, {f} failures")
    print()

    print("=== Item 1: the torn state ===")
    rng = random.Random(SEED + 1)
    tested, sp3, sp2, fail = check_item1(rng)
    print(f"  {tested} spikes tested ({sp3} with s>=3, {sp2} boundary s=2), "
          f"{fail} failures")
    total_checks += tested
    total_failures += fail
    print()

    print("=== Item 2: the opening run ===")
    rng = random.Random(SEED + 2)
    tested, fail = check_item2(rng)
    print(f"  {tested} spikes (s>=3) tested, {fail} failures")
    total_checks += tested
    total_failures += fail
    print()

    print("=== Item 3: the torn core's anchor ===")
    rng = random.Random(SEED + 3)
    (at, af, ct, cf, bt, bm) = check_item3(rng)
    print(f"  anchor valuation v2(M(Omega'))=s-4: {at} spikes (s>=5), "
          f"{af} failures")
    print(f"  column coincidence (v2(d') < s-4): {ct} (state,d') pairs, "
          f"{cf} failures")
    print(f"  boundary (v2(d') == s-4, not covered by the proposition): "
          f"{bt} pairs, {bm} still coincided ({bm}/{bt} = "
          f"{bm/bt if bt else 0:.4f}) -- measured, not claimed")
    total_checks += at + ct
    total_failures += af + cf
    print()

    print("=== Item 4: the mirror tear (reverse.md 14.10.1) ===")
    rng = random.Random(SEED + 4)
    tested, d1, d2, fail = check_item4(rng)
    print(f"  {tested} (y,s) trials ({d1} in d=1/T3 branch, "
          f"{d2} in d>=2/affine branch), {fail} failures")
    total_checks += tested
    total_failures += fail
    print()

    print("=== Item 6: measured, not proved ===")
    rng = random.Random(SEED + 6)
    r6 = check_item6(rng)
    print(f"  sign lemma (T(e)<e', T(T(e))<e', exact inequality): "
          f"{r6['sign_tested']} cases, {r6['sign_failures']} failures")
    print(f"  non-return (e' never in orbit of e, {r6['orbit_bound']} steps): "
          f"{r6['nonreturn_tested']} cases, "
          f"{r6['nonreturn_failures']} counterexamples found")
    print(f"  reverse (e downstream of e', {r6['orbit_bound']} steps): "
          f"{r6['reverse_hits_basin']} in drainage basin, "
          f"{r6['reverse_hits_other']} elsewhere")
    print(f"  merge point: found for {r6['merge_found']}/{r6['merge_total']}; "
          f"strictly below both sisters in {r6['merge_below_both']}/"
          f"{r6['merge_found']}")
    total_checks += r6['sign_tested'] + r6['nonreturn_tested']
    total_failures += r6['sign_failures'] + r6['nonreturn_failures']
    # NOTE: reverse_hits_other is NOT scored as a failure. The pre-check's
    # claim ("only in the drainage basin") is corrected here, not enforced:
    # at this sample size a rare generic merge (e outside {1,5,13,23} found
    # downstream of e' within the step bound) does occur -- see findings.
    if r6['reverse_hits_other'] > 0:
        print(f"  ** correction to the pre-check: {r6['reverse_hits_other']} "
              f"generic (non-basin) reverse hit(s) found -- 'only in the "
              f"drainage basin' does not hold at this sample size; recorded "
              f"as measured, not enforced as a failure (see findings) **")
    print()

    print("=== Item 7: tear-lines as level sets ===")
    rng = random.Random(SEED + 7)
    tested, fail = check_item7_identity(rng)
    print(f"  level-set identity: {tested} (w,d,k) triples, {fail} failures")
    total_checks += tested
    total_failures += fail
    for k in (8, 12, 16):
        rng_tv = random.Random(SEED + 100 + k)
        n_starts = 40000
        produced, tv_post, tv_noise = check_item7_tv(rng_tv, k, n_starts)
        print(f"  k={k}: {produced} starts on the tear-line, "
              f"one-step TV from uniform = {tv_post:.5f}, "
              f"noise floor (same-size uniform draw) = {tv_noise:.5f}")
    print()

    print(f"TOTAL: {total_checks} checks, {total_failures} failures")
    assert total_failures == 0, "verification FAILED"
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
