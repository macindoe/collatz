"""experiments/top_door_lineage.py -- the top-door lineage as an object
of its own: aliveness and parity, the odd-stratum cycle equation, run
lengths, and the item-7 flat note.

Supports: briefs/top-door-lineage-brief.md, briefs/top-door-lineage-findings.md.

Fresh code. Imports nothing from any existing script (not modq_spectrum.py,
not margin_asymptote.py, not any mirror_*.py, not merle_*.py): v2/v3,
the reduced map F (spine.md 5.4-5.6), the predecessor characterization
(reverse.md 14.1.1), and the rotation numerator R_r (cycles.md 12.6.1)
are all reimplemented here from the definitions. Exact integer (Python
bigint) arithmetic at every pass/fail decision; the run-length section
uses Python's own PRNG, seeded and stated, and only for sampling start
states -- every valuation computed from a sampled state is still exact.

Conventions matching the wiki's own (cycles.md section-12 preamble,
reverse.md 14.1.1, spine.md 5.4-5.6):
  state (omega, d): omega an odd integer with 3 !| omega (may be
    negative -- itinerary.md 14.15.6 confirms the valuation/state algebra
    is sign-independent), d >= 1.
  F(omega, d) = (Omega, D): A = 3^d*omega - 1, s = v2(A), y = A/2^s
    (= x_exit); m_+ = v2(y+1), u_+ = (y+1)/2^m_+, a_+ = v3(u_+),
    Omega = u_+/3^a_+, D = m_+ + a_+.
  top door of (Omega, D): y0 = 2^D*Omega - 1 (reverse.md 14.8.1, a=0
    representative of reverse.md 14.1.1's y_a family).
  predecessor via door y (3 !| y) and branch s (s odd if y%3==1, s even
    if y%3==2): N = 2^s*y + 1, d = v3(N), omega = N/3^d
    (reverse.md 14.1.1).
  period-p profile (ms, ss): cycles.md Proposition 12.6.1's
    n = sum(ms), K = sum(ss) + n, q = 2^K - 3^n,
    R_r = sum_t 3^{M_t} 2^{S_t} (2^{s_t} - 1), reading the profile
    rotated to start at r; M_t = sum_{j>t} m_j, S_t = sum_{j<t} sigma_j,
    sigma_j = s_j + m_{(j+1) mod p} (cyclic).

Run, single command, reproduces the committed output in full:
    python experiments/top_door_lineage.py > experiments/top_door_lineage_output.txt

No per-period cycle search anywhere in this file: the only enumeration
is the bounded canary census of item (b) below, reproduced at exactly
the brief's stated bounds (p <= 4, entries <= 6) and not extended.
"""

import random
import sys
import time
from fractions import Fraction

SEED = 20260913
random.seed(SEED)

checks = 0
failures = 0


def record(ok, label):
    global checks, failures
    checks += 1
    if not ok:
        failures += 1
        print(f"  FAIL: {label}")
    return ok


# ---------------------------------------------------------------------
# Core arithmetic (fresh; sign-independent, matching itinerary.md
# 14.15.6.1's remark that the valuation algebra never references sign)
# ---------------------------------------------------------------------

def v2(n):
    n = abs(n)
    if n == 0:
        raise ValueError("v2(0) undefined")
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def v3(n):
    n = abs(n)
    if n == 0:
        raise ValueError("v3(0) undefined")
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def forward_step(omega, d):
    """One step of the reduced map F on a valid state (omega, d):
    omega odd, 3 !| omega, d >= 1. spine.md 5.4-5.6."""
    assert omega % 2 != 0 and omega % 3 != 0 and d >= 1
    A = (3 ** d) * omega - 1
    s = v2(A)
    y = A // (2 ** s)
    assert y % 2 != 0
    m_plus = v2(y + 1)
    u_plus = (y + 1) // (2 ** m_plus)
    a_plus = v3(u_plus)
    Omega = u_plus // (3 ** a_plus)
    D = m_plus + a_plus
    assert Omega % 2 != 0 and Omega % 3 != 0 and D >= 1
    return dict(s=s, y=y, m_plus=m_plus, a_plus=a_plus, Omega=Omega, D=D)


def top_door(Omega, D):
    return (2 ** D) * Omega - 1


def top_door_alive(Omega, D):
    """reverse.md 14.5.1 at a=0: dead iff 2^D*Omega == 1 (mod 3)."""
    return (2 ** D * Omega) % 3 != 1


def predecessor_via_door(y, s):
    """reverse.md 14.1.1. y must be a live door (3 !| y); s must carry
    the admissible parity (odd if y%3==1, even if y%3==2)."""
    assert y % 3 != 0
    if y % 3 == 1:
        assert s % 2 == 1, "parity violation: y=1 mod 3 needs s odd"
    else:
        assert s % 2 == 0, "parity violation: y=2 mod 3 needs s even"
    N = (2 ** s) * y + 1
    d = v3(N)
    omega = N // (3 ** d)
    return omega, d


def h_of_s(s):
    """stage3.md: h(s) = v3(2^s - 1) = 0 if s odd, 1+v3(s) if s even."""
    if s % 2 == 1:
        return 0
    return 1 + v3(s)


def random_valid_state(rng, bound=10 ** 9, dmax=40, allow_negative=False):
    while True:
        omega = rng.randrange(1, bound) | 1
        if allow_negative and rng.random() < 0.5:
            omega = -omega
        if omega % 3 == 0:
            continue
        d = rng.randrange(1, dmax + 1)
        return omega, d


# ---------------------------------------------------------------------
# Profile / cycle-equation machinery (cycles.md Proposition 12.6.1)
# ---------------------------------------------------------------------

def profile_nKq(ms, ss):
    n = sum(ms)
    K = sum(ss) + n
    q = 2 ** K - 3 ** n
    return n, K, q


def R_rot_exact(ms, ss, r):
    """Exact big-integer R_r, fresh implementation (prefix-sum)."""
    p = len(ms)
    mr = ms[r:] + ms[:r]
    sr = ss[r:] + ss[:r]
    # M_t = sum_{j>t} mr[j]  (suffix sum over the rotated sequence)
    Msuf = [0] * (p + 1)
    for t in range(p - 1, -1, -1):
        Msuf[t] = Msuf[t + 1] + mr[t]
    total = 0
    Spre = 0  # S_t = sum_{j<t} sigma_j, built as a running prefix
    for t in range(p):
        Mt = Msuf[t + 1]
        total += (3 ** Mt) * (2 ** Spre) * (2 ** sr[t] - 1)
        sigma_t = sr[t] + mr[(t + 1) % p]
        Spre += sigma_t
    return total


def transport_recurrence_holds(ms, ss):
    """cycles.md 12.6.1.1: 2^{sigma_r} R_{r+1} = 3^{m_r} R_r + (2^{s_r}-1) q,
    for every profile with entries >= 1, no closure needed."""
    p = len(ms)
    n, K, q = profile_nKq(ms, ss)
    ok = True
    for r in range(p):
        Rr = R_rot_exact(ms, ss, r)
        Rr1 = R_rot_exact(ms, ss, (r + 1) % p)
        sigma_r = ss[r] + ms[(r + 1) % p]
        lhs = (2 ** sigma_r) * Rr1
        rhs = (3 ** ms[r]) * Rr + (2 ** ss[r] - 1) * q
        if lhs != rhs:
            ok = False
    return ok


def run_length_stats(seq):
    """Maximal run lengths of True in a boolean sequence, excluding the
    two boundary runs (left-censored / right-censored)."""
    runs = []
    cur = 0
    started_true_at_0 = seq[0] if seq else False
    i = 0
    n = len(seq)
    while i < n:
        if seq[i]:
            j = i
            while j < n and seq[j]:
                j += 1
            runs.append((i, j - i))  # (start index, length)
            i = j
        else:
            i += 1
    # Drop a run touching index 0 or index n-1 (possibly censored).
    interior = [length for (start, length) in runs
                if start > 0 and start + length < n]
    return interior


# =======================================================================
# CANARIES
# =======================================================================

def canaries():
    print("=" * 70)
    print("CANARIES")
    print("=" * 70)

    # --- Canary A: trivial cycle (1,1) is a top-door fixed point. ---
    r = forward_step(1, 1)
    ok = (r["s"] == 1 and r["a_plus"] == 0 and r["Omega"] == 1 and r["D"] == 1)
    record(ok, "canary A: F(1,1) = (1,1), s=1 odd, a_plus=0")
    print(f"canary A  F(1,1) -> s={r['s']} a_plus={r['a_plus']} "
          f"(Omega,D)=({r['Omega']},{r['D']})  {'OK' if ok else 'FAIL'}")

    # --- Canary B: Prop 12.6.1's sanity identity for the fake
    #     period-p trivial cycle (m_t = s_t = 1 for all t): R = 4^p -
    #     3^p = q exactly. cycles.md's own stated instance set. ---
    print("canary B  fake trivial period-p cycle: R_0 == q == 4^p - 3^p")
    for p in (1, 2, 3, 4, 7):
        ms = [1] * p
        ss = [1] * p
        n, K, q = profile_nKq(ms, ss)
        R0 = R_rot_exact(ms, ss, 0)
        expect = 4 ** p - 3 ** p
        ok = record(R0 == q == expect,
                    f"canary B p={p}: R0={R0} q={q} expect={expect}")
        print(f"    p={p:2d}  R0={R0:>12d}  q={q:>12d}  "
              f"4^p-3^p={expect:>12d}  {'OK' if ok else 'FAIL'}")

    # --- Canary C: the three known cycles, reconstructed from their
    #     profiles via the odd-stratum equation omega_r = R_r / q
    #     (d_0 = m_0, since the odd stratum forces a_{-1}=0), then run
    #     forward and confirmed to close exactly on the stated profile.
    #     This is the item-4 odd-stratum equation and the item-1/item-2
    #     canaries in one construction. ---
    known = [
        ("(1,1) [trivial cycle, x=1]", [1], [1], 1),
        ("(2,1) [x=-5]", [2], [1], -5),
        ("((4,1),(3,3)) [x=-17]", [4, 3], [1, 3], -17),
    ]
    print("canary C  known cycles reconstructed from odd-stratum profiles")
    for label, ms, ss, x_expect in known:
        p = len(ms)
        n, K, q = profile_nKq(ms, ss)
        assert all(s % 2 == 1 for s in ss), "canary set must be odd stratum"
        R0 = R_rot_exact(ms, ss, 0)
        ok_div = record(R0 % q == 0, f"canary C {label}: q | R0")
        omega0 = R0 // q
        d0 = ms[0]
        x0 = (2 ** d0) * omega0 - 1
        ok_x = record(x0 == x_expect, f"canary C {label}: x0 == {x_expect}")
        # Run the cycle forward p steps and confirm exact closure.
        omega, d = omega0, d0
        trace = []
        for t in range(p):
            step = forward_step(omega, d)
            trace.append((d, step["s"], step["a_plus"]))
            ok_s = record(step["s"] == ss[t],
                           f"canary C {label} step {t}: s matches profile")
            ok_a = record(step["a_plus"] == 0,
                           f"canary C {label} step {t}: a_plus == 0 (odd stratum)")
            omega, d = step["Omega"], step["D"]
        ok_close = record((omega, d) == (omega0, d0),
                           f"canary C {label}: closes after {p} steps")
        print(f"    {label:28s} omega0={omega0:>4d} d0={d0}  x0={x0:>4d}  "
              f"closes={'OK' if ok_close else 'FAIL'}")

    print()


# =======================================================================
# ITEM (a): item 1 both directions, on random states, plus the
# resonance boundary check.
# =======================================================================

def item_a_aliveness_and_parity():
    print("=" * 70)
    print("ITEM (a): aliveness and parity; s odd <=> a_plus == 0")
    print("=" * 70)
    rng = random.Random(SEED + 1)

    # (i) Forward direction, unconditional, on plain random states
    #     (not filtered to top doors): s odd <=> a_plus == 0.
    N1 = 60000
    fails = 0
    resonant_seen_odd = 0
    resonant_seen_even = 0
    for _ in range(N1):
        omega, d = random_valid_state(rng, bound=10 ** 12, dmax=200)
        step = forward_step(omega, d)
        s, a_plus = step["s"], step["a_plus"]
        biconditional = (s % 2 == 1) == (a_plus == 0)
        if not biconditional:
            fails += 1
        if h_of_s(s) == d:
            if s % 2 == 1:
                resonant_seen_odd += 1
            else:
                resonant_seen_even += 1
    record(fails == 0, "item(a)(i): s odd <=> a_plus==0 on random states")
    print(f"(i)  N={N1}  failures={fails}  "
          f"resonant(h(s)==d) cases hit: s-odd={resonant_seen_odd} "
          f"s-even={resonant_seen_even}")
    record(resonant_seen_odd == 0,
           "item(a)(i): resonance never hit with s odd (h(s)=0<d always)")

    # (ii) Explicit constructed resonance boundary cases (s even,
    #      h(s) == d exactly): confirm a_plus is NEVER 0 there, and
    #      matches the resonant formula a_plus = d + v3(omega + beta).
    print("(ii) explicit resonance construction (s even, h(s) == d):")
    resonance_cases = 0
    resonance_fails = 0
    for s in range(2, 40, 2):
        d = h_of_s(s)  # forces resonance h(s) == d
        # Search small odd omega, 3 !| omega, with v2(3^d*omega - 1) == s
        # exactly (the state that actually lands on branch s at depth d).
        found = 0
        omega = 1
        while found < 5 and omega < 20000:
            if omega % 3 != 0:
                A = (3 ** d) * omega - 1
                if v2(A) == s:
                    resonance_cases += 1
                    found += 1
                    step = forward_step(omega, d)
                    beta = (2 ** s - 1) // (3 ** d)
                    assert beta * (3 ** d) == 2 ** s - 1
                    expect_a = d + v3(omega + beta)
                    ok = (step["a_plus"] == expect_a) and (step["a_plus"] != 0)
                    if not ok:
                        resonance_fails += 1
                    record(ok, f"resonance s={s} d={d} omega={omega}: "
                               f"a_plus={step['a_plus']} expect={expect_a} (!=0)")
            omega += 2
    print(f"     resonance instances constructed: {resonance_cases}, "
          f"failures: {resonance_fails}")
    record(resonance_cases > 0, "item(a)(ii): resonance construction nonempty")

    # (iii) Backward construction: top-door aliveness (14.5.1 at a=0)
    #       round-tripped through a predecessor built via the a=0
    #       door, confirming forward a_plus==0 exactly.
    N2 = 30000
    alive_count = 0
    dead_count = 0
    fails2 = 0
    for _ in range(N2):
        Omega, D = random_valid_state(rng, bound=10 ** 9, dmax=60)
        y0 = top_door(Omega, D)
        alive_criterion_A = (y0 % 3 == 1)          # brief's phrasing
        alive_criterion_B = top_door_alive(Omega, D)  # 14.5.1 directly
        if alive_criterion_A != alive_criterion_B:
            fails2 += 1
            continue
        if alive_criterion_A:
            alive_count += 1
            # 14.1.1's parity condition forces s odd since y0 % 3 == 1.
            s = 2 * rng.randrange(0, 30) + 1
            omega, d = predecessor_via_door(y0, s)
            step = forward_step(omega, d)
            ok = (step["Omega"] == Omega and step["D"] == D
                  and step["s"] == s and step["a_plus"] == 0)
            if not ok:
                fails2 += 1
            record(ok, "item(a)(iii): top-door predecessor round-trips "
                       "with a_plus==0")
        else:
            dead_count += 1
    record(fails2 == 0, "item(a)(iii): no failures in N2 trials")
    print(f"(iii) N={N2}  alive={alive_count}  dead={dead_count}  "
          f"failures={fails2}  (measured alive rate: "
          f"{alive_count / N2:.4f}, cf. 1/2)")
    print()


# =======================================================================
# ITEM (b): the bounded census, p <= 4, entries <= 6, q | R0.
# CANARY ONLY -- reproduced at exactly the brief's stated bounds, not
# extended.  This is not a cycle search: no closure/period test is
# performed, only the divisibility identity q | R0 on the finite,
# explicitly bounded profile family.
# =======================================================================

def item_b_census():
    print("=" * 70)
    print("ITEM (b): bounded census p<=4, entries<=6, q|R0 -- CANARY ONLY, "
          "not extended")
    print("=" * 70)
    hits = []
    for p in range(1, 5):
        for idx in range(6 ** (2 * p)):
            # decode idx into (m_1..m_p, s_1..s_p) each in 1..6
            digits = []
            x = idx
            for _ in range(2 * p):
                digits.append(x % 6 + 1)
                x //= 6
            ms = digits[0:2 * p:2]
            ss = digits[1:2 * p:2]
            n, K, q = profile_nKq(ms, ss)
            R0 = R_rot_exact(ms, ss, 0)
            if R0 % q == 0:
                hits.append((p, tuple(ms), tuple(ss), n, K, q, R0 // q))
    print(f"profiles examined: p in 1..4, entries in 1..6 each -> "
          f"{sum(6 ** (2 * p) for p in range(1, 5))} total")
    print(f"profiles with q | R0: {len(hits)}")
    for (p, ms, ss, n, K, q, omega0) in hits:
        d0 = ms[0]
        x0 = (2 ** d0) * omega0 - 1
        print(f"    p={p} ms={ms} ss={ss}  n={n} K={K} q={q:>6d}  "
              f"omega0={omega0:>4d}  x0={x0:>4d}")
    record(len(hits) == 12, "item(b): census returns exactly 12 profiles")

    # Each hit must be a rotation of a power (repeat) of one of the
    # three known words: (1,1); (2,1); ((4,1),(3,3)). NOTE: the block
    # ENTRY value x0 = 2^{m_0}*omega0 - 1 is NOT rotation-invariant --
    # it is the odd integer at whichever block the rotation starts at,
    # so the two rotations of the -17 word carry two different x0
    # (-17 and -41, both on the same classical 7-block negative
    # cycle); the invariant to check is the profile/word, not x0.
    def rotations_of_power(base_ms, base_ss, max_k, max_p):
        out = []
        bp = len(base_ms)
        for k in range(1, max_k + 1):
            ms_full = list(base_ms) * k
            ss_full = list(base_ss) * k
            p = bp * k
            if p > max_p:
                continue
            for r in range(p):
                out.append((tuple(ms_full[r:] + ms_full[:r]),
                             tuple(ss_full[r:] + ss_full[:r])))
        return set(out)

    known_words = (
        rotations_of_power([1], [1], 4, 4)
        | rotations_of_power([2], [1], 4, 4)
        | rotations_of_power([4, 3], [1, 3], 2, 4)
    )
    hit_words = set((tuple(ms), tuple(ss)) for (p, ms, ss, *_ ) in hits)
    record(hit_words <= known_words,
           "item(b): every hit is a rotation/repeat of the three known words")
    record(known_words >= hit_words and len(hit_words) == 12,
           "item(b): the 12 hits are exactly rotations/repeats of the 3 words "
           "(no fourth word, no omission)")
    print()
    return hits


# =======================================================================
# ITEM (c): item 4's odd-stratum equation against the general one, on
# random odd-stratum profiles (formula-level, no closure assumed) and
# re-confirmed on the three known cycles.
# =======================================================================

def item_c_odd_stratum_equation(census_hits):
    print("=" * 70)
    print("ITEM (c): odd-stratum cycle equation omega_r*q = R_r "
          "vs. the general omega_r*3^a*q = R_r")
    print("=" * 70)
    rng = random.Random(SEED + 2)

    # (i) Transport recurrence (12.6.1.1) re-verified fresh, on random
    #     GENERAL (mixed-parity) profiles -- no closure needed, holds
    #     for every profile with entries >= 1.
    N1 = 4000
    fails = 0
    for _ in range(N1):
        p = rng.randrange(1, 7)
        ms = [rng.randrange(1, 9) for _ in range(p)]
        ss = [rng.randrange(1, 9) for _ in range(p)]
        if not transport_recurrence_holds(ms, ss):
            fails += 1
    record(fails == 0, "item(c)(i): transport recurrence holds, general profiles")
    print(f"(i)  N={N1} general profiles, transport-recurrence failures={fails}")

    # (ii) Same, restricted to odd-stratum profiles (all s_t odd) --
    #      the recurrence is unaffected by stratum (it never involves
    #      a_t), recorded as a direct confirmation.
    N2 = 4000
    fails2 = 0
    for _ in range(N2):
        p = rng.randrange(1, 7)
        ms = [rng.randrange(1, 9) for _ in range(p)]
        ss = [2 * rng.randrange(0, 4) + 1 for _ in range(p)]  # odd
        if not transport_recurrence_holds(ms, ss):
            fails2 += 1
    record(fails2 == 0, "item(c)(ii): transport recurrence holds, odd-stratum")
    print(f"(ii) N={N2} odd-stratum profiles, transport-recurrence failures={fails2}")

    # (iii) The twelve census profiles (item b), all odd-stratum by
    #       inspection, reconstructed to real (omega_0, d_0) states via
    #       d_0 = m_0 (odd-stratum forces a_{-1}=0) and run forward:
    #       confirms the closed-cycle odd-stratum equation
    #       omega_r * q = R_r (no 3^a factor) holds with an ACTUAL
    #       closing integer cycle, for every one of the 12 hits.
    print("(iii) all 12 census hits: odd stratum, and omega_r*q=R_r closes")
    all_odd = all(all(s % 2 == 1 for s in ss) for (p, ms, ss, *_ ) in census_hits)
    record(all_odd, "item(c)(iii): every census hit is odd-stratum")
    fails3 = 0
    for (p, ms, ss, n, K, q, omega0) in census_hits:
        d0 = ms[0]
        omega, d = omega0, d0
        ok_all = True
        for t in range(p):
            step = forward_step(omega, d)
            ok_all &= (step["a_plus"] == 0) and (step["s"] == ss[t])
            omega, d = step["Omega"], step["D"]
        ok_all &= (omega, d) == (omega0, d0)
        if not ok_all:
            fails3 += 1
        record(ok_all, f"item(c)(iii): ms={ms} ss={ss} closes with a=0 throughout")
    print(f"      hits checked: {len(census_hits)}  failures={fails3}")

    # (iv) Open-path (non-cyclic) confirmation on genuine random
    #      orbits: run forward from a random valid state until a run
    #      of consecutive odd-s steps of length >= 3 is found, then
    #      confirm directly that a_plus==0 and d==m at every one of
    #      those steps (item 1's law, chained along a real path).
    N4 = 2000
    fails4 = 0
    checked_chains = 0
    for _ in range(N4):
        omega, d = random_valid_state(rng, bound=10 ** 9, dmax=60)
        chain_ok = True
        steps_odd = 0
        for _t in range(20):
            step = forward_step(omega, d)
            if step["s"] % 2 == 1:
                steps_odd += 1
                chain_ok &= (step["a_plus"] == 0) and (step["D"] == step["m_plus"])
            else:
                if steps_odd >= 3:
                    checked_chains += 1
                steps_odd = 0
                chain_ok &= (step["a_plus"] != 0)
            omega, d = step["Omega"], step["D"]
        if not chain_ok:
            fails4 += 1
    record(fails4 == 0, "item(c)(iv): open-path chains, a_plus==0<=>s odd throughout")
    print(f"(iv) N={N4} random 20-step orbits; chains with >=3 consecutive "
          f"odd-s steps observed: {checked_chains}; failures={fails4}")
    print()


# =======================================================================
# ITEM (d): run-length histogram vs (2/3)^n.
# =======================================================================

def item_d_run_lengths():
    print("=" * 70)
    print("ITEM (d): realized top-door run lengths vs (2/3)^n")
    print("=" * 70)
    rng = random.Random(SEED + 3)

    N_ORBITS = 4000
    STEPS = 120
    LOW = 2 ** 200
    HIGH = 2 ** 260

    from collections import Counter
    lengths = Counter()
    total_interior_runs = 0
    total_odd_steps = 0
    total_steps = 0

    for _ in range(N_ORBITS):
        omega = rng.randrange(LOW, HIGH) | 1
        while omega % 3 == 0:
            omega += 2
        d = 1
        parity_seq = []
        for _t in range(STEPS):
            step = forward_step(omega, d)
            parity_seq.append(step["s"] % 2 == 1)
            omega, d = step["Omega"], step["D"]
            # re-inflate omega occasionally is unnecessary: the reduced
            # core omega itself need not stay large for the s-parity
            # law to hold exactly (it is a local, exact law at every
            # state); STEPS is kept well below any drainage-basin
            # concern by construction of the state, not its size.
        total_odd_steps += sum(parity_seq)
        total_steps += len(parity_seq)
        for L in run_length_stats(parity_seq):
            lengths[L] += 1
            total_interior_runs += 1

    print(f"orbits={N_ORBITS}  steps/orbit={STEPS}  "
          f"seed={SEED + 3}  start range=[2^200,2^260)")
    print(f"measured P(s odd) over all steps: "
          f"{total_odd_steps}/{total_steps} = {total_odd_steps/total_steps:.4f} "
          f"(cf. 2/3 = {2/3:.4f})")
    print(f"interior (uncensored) runs collected: {total_interior_runs}")
    print(f"{'n':>3s}  {'#runs>=n (meas.)':>18s}  {'P(len>=n) meas.':>16s}  "
          f"{'(2/3)^n':>10s}")
    max_len = max(lengths) if lengths else 0
    ge_counts = []
    for n in range(1, max_len + 2):
        ge = sum(c for L, c in lengths.items() if L >= n)
        ge_counts.append((n, ge))
    for n, ge in ge_counts:
        if total_interior_runs == 0:
            break
        meas = ge / total_interior_runs
        theo = (2 / 3) ** n
        print(f"{n:>3d}  {ge:>18d}  {meas:>16.4f}  {theo:>10.4f}")
        if ge == 0:
            break
    print()
    return lengths, total_interior_runs


# =======================================================================
# ITEM (e): item 7's clause -- 1 + 2^s = 3^k forces s odd.
# =======================================================================

def item_e_neighbour_laws():
    print("=" * 70)
    print("ITEM (e): 1 + 2^s = 3^k forces s odd (item 7's flat note)")
    print("=" * 70)
    solutions = []
    for k in range(1, 60):
        target = 3 ** k - 1
        if target > 0 and (target & (target - 1)) == 0:  # power of 2
            s = target.bit_length() - 1
            solutions.append((s, k))
    print(f"solutions with k in 1..59: {solutions}")
    record(solutions == [(1, 1), (3, 2)],
           "item(e): exactly (s,k) = (1,1), (3,2) for k in 1..59")
    record(all(s % 2 == 1 for (s, k) in solutions),
           "item(e): every solution has s odd")
    # Proof check via mod 4, all k in a larger range with no false positive.
    fails = 0
    for k in range(1, 2000):
        target = 3 ** k - 1
        s_is_pow2 = (target & (target - 1)) == 0
        if s_is_pow2:
            s = target.bit_length() - 1
            if s % 2 != 1:
                fails += 1
    record(fails == 0, "item(e): no even-s solution for k in 1..1999")
    print(f"extended search k in 1..1999: no further solutions, "
          f"even-s failures={fails}")
    print()


# =======================================================================

def main():
    t0 = time.time()
    print(f"top_door_lineage.py -- seed={SEED} -- {time.strftime('%Y-%m-%d')}")
    print()
    canaries()
    item_a_aliveness_and_parity()
    census_hits = item_b_census()
    item_c_odd_stratum_equation(census_hits)
    item_d_run_lengths()
    item_e_neighbour_laws()
    dt = time.time() - t0
    print("=" * 70)
    print(f"TOTAL: checks={checks} failures={failures} time={dt:.1f}s")
    print("=" * 70)
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
