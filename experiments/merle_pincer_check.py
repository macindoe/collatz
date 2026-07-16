# Merle pincer check (briefs/merle-pincer-check-brief.md): independent
# verification of Eric Merle's p = 22 "Diophantine pincer" hypothesis, two
# calibration rows (p = 21, p = 23), his p = 7 local-global
# distance-to-integrality re-run (his ledger seed #3), and the
# continued-fraction hole claim.
#
# Supports: briefs/merle-pincer-check-findings.md.
#
# Provenance and the one labeled exception (item 1): the brief permits
# running experiments/staircase_allp.py's OWN candidate-enumeration logic,
# instrumented, for the single purpose of reporting "which n did our stack
# try at p = 22" -- that is a factual question about what the committed
# script does, not a claim needing independent re-derivation. SECTION 1
# below is a verbatim-logic COPY of that script's Parts A/C/D (never an
# import, and experiments/staircase_allp.py is never modified), clearly
# labeled. Every other section (2 onward) is independently written, uses
# no code from experiments/staircase_allp.py, and answers each of items
# 2-4 with its own implementation of the wiki's stated formulas (cycles.md
# 12.6.1 rotation sums, 12.8.6.1 Diophantine input, 12.8.6.2 construction).
#
# Exact integer arithmetic for every pass/fail decision (q <= R_r,
# divisibility, feasibility of the rounded profile). Decimal/float
# arithmetic appears only in choosing/describing candidates -- log2 of a
# huge Python int is safe (CPython computes it without materializing a
# float from the full integer), so "margin in bits" is reported two ways:
# an exact integer bit_length difference (the corrected diagnostic of
# staircase-allp-findings.md item 2 -- the house convention) and a
# continuous log2 difference (display only, for direct numeric comparison
# against Merle's fractional-bit figures). Neither is used for a pass/fail
# decision; those are always plain integer comparisons.

import decimal
import math
import time

decimal.getcontext().prec = 600
L = decimal.Decimal(3).ln() / decimal.Decimal(2).ln()   # log2(3), high precision
LF = float(L)


def bit_margin(R, q):
    """Exact integer bit-length margin (house convention, staircase-allp-
    findings.md item 2): bit_length(R) - bit_length(q). Negative = R < q
    roughly by that many bits; this is NOT how pass/fail is decided (that
    is plain R >= q on the exact integers) -- it is a reporting figure."""
    return R.bit_length() - q.bit_length()


def log2_margin(R, q):
    """Continuous log2(R) - log2(q), display only. math.log2 on a Python
    int of arbitrary size does not overflow (CPython handles the exponent
    and mantissa separately), so this is safe and exact-enough for display
    -- but it is still never used to decide pass/fail."""
    return math.log2(R) - math.log2(q)


# =====================================================================
# SECTION 1 (ITEM 1 ONLY). Verbatim-logic instrumented copy of
# experiments/staircase_allp.py Parts A, B, C, D -- reporting what the
# committed script's own candidate enumeration and construction produce
# at p = 22. This section is the brief's one labeled exception; it is not
# used by any other item below, and it never imports from or edits the
# committed file.
# =====================================================================

def committed_cf_terms(x, nterms):
    terms = []
    for _ in range(nterms):
        a = int(x)
        terms.append(a)
        frac = x - a
        if frac == 0:
            break
        x = 1 / frac
    return terms


def committed_build_candidate_chain(max_n, cf_depth=30):
    """Verbatim copy of staircase_allp.py's build_candidate_chain: ALL
    convergent/semiconvergent denominators (both signs -- it does not
    filter by the sign condition of lemma 12.8.6.1), up to max_n."""
    terms = committed_cf_terms(L, cf_depth)
    h_prev2, h_prev1 = 0, 1
    k_prev2, k_prev1 = 1, 0
    chain = []
    for a in terms:
        for j in range(1, a):
            nn = k_prev1 * j + k_prev2
            if nn <= max_n:
                chain.append(nn)
        k = a * k_prev1 + k_prev2
        h = a * h_prev1 + h_prev2
        if k <= max_n:
            chain.append(k)
        h_prev2, h_prev1 = h_prev1, h
        k_prev2, k_prev1 = k_prev1, k
        if k > max_n:
            break
    return sorted(set(n for n in chain if n >= 1))


def committed_R_rot(ms, ss):
    p = len(ms)
    Msuf = [0] * (p + 1)
    for t in range(p - 1, -1, -1):
        Msuf[t] = Msuf[t + 1] + (ms[t + 1] if t + 1 < p else 0)
    R = 0
    Spre = 0
    for t in range(p):
        R += (3 ** Msuf[t]) * (1 << Spre) * ((1 << ss[t]) - 1)
        Spre += ss[t] + ms[(t + 1) % p]
    return R


def committed_all_R(ms, ss):
    p = len(ms)
    return [committed_R_rot(ms[r:] + ms[:r], ss[r:] + ss[:r]) for r in range(p)]


def committed_climb_partial_sum_round(climb_n, blocks, rounding=decimal.ROUND_HALF_EVEN):
    c = decimal.Decimal(climb_n) * (L - 1) / (L ** blocks - 1)
    prev = 0
    ms = []
    for j in range(blocks):
        Tj = c * (L ** (j + 1) - 1) / (L - 1)
        Mj = int(Tj.to_integral_value(rounding=rounding))
        ms.append(Mj - prev)
        prev = Mj
    diff = climb_n - sum(ms)
    ms[-1] += diff
    return ms


def committed_base_construct(p, n, K, crash_depth=1):
    S = K - n
    if p < 2 or S <= p - 1:
        return None
    climb_n = n - crash_depth
    if climb_n < p - 1:
        return None
    ms = committed_climb_partial_sum_round(climb_n, p - 1)
    if min(ms) < 1:
        return None
    ms = ms + [crash_depth]
    ss = [1] * (p - 1) + [S - (p - 1)]
    if ss[-1] < 1:
        return None
    return ms, ss


def committed_bounded_correction(ms, ss, q, max_moves=40, escalate_after=15, deadline=None):
    p = len(ms)
    crash_idx = p - 1
    moves = 0
    while moves < max_moves:
        if deadline is not None and time.time() > deadline:
            return None
        Rs = committed_all_R(ms, ss)
        minR = min(Rs)
        if minR >= q:
            return ms, ss, moves
        rstar = Rs.index(minR)
        cheap = (moves < escalate_after)
        if cheap:
            pairs = []
            for don_off in (-1, -2, -3, -4, 1, 2):
                for rec_off in (1, 2, 3, -1, -2):
                    i = (rstar + don_off) % p
                    j = (rstar + rec_off) % p
                    if i != j and i != crash_idx and j != crash_idx:
                        pairs.append((i, j))
        else:
            pairs = [(i, j) for i in range(p - 1) for j in range(p - 1) if i != j]
        best = None
        for i, j in pairs:
            if ms[i] <= 1:
                continue
            ms2 = ms[:]
            ms2[i] -= 1
            ms2[j] += 1
            m2 = min(committed_all_R(ms2, ss))
            if best is None or m2 > best[0]:
                best = (m2, i, j)
        if best is None or best[0] <= minR:
            if cheap:
                escalate_after = 0
                continue
            return None
        _, i, j = best
        ms[i] -= 1
        ms[j] += 1
        moves += 1
    Rs = committed_all_R(ms, ss)
    if min(Rs) >= q:
        return ms, ss, moves
    return None


def item1_report():
    """Item 1: for p = 22, report every candidate n the committed script's
    Diophantine chain supplies within its search window (the top n_tries=6
    it actually iterates, per the __main__ call run(pmin=2, pmax=25,
    n_tries=6, max_moves=40, wall_clock_budget=75.0) and find_passer's
    default crash_depths=(1,2)), plus a labeled reconstruction of the wider
    supplementary set from staircase-allp-findings.md item 3."""
    out = []
    p = 22
    pmax = 25
    max_n = int(4 * LF ** pmax) + 10
    chain = committed_build_candidate_chain(max_n)
    out.append(f"Committed chain: {len(chain)} convergent/semiconvergent "
                f"denominators of log2(3) up to n={max_n} (both signs -- "
                f"build_candidate_chain does not filter by the sign "
                f"condition of lemma 12.8.6.1).")

    target = LF ** p
    out.append(f"p=22 scale target L^22 = {target:.3f}")
    window = sorted(n for n in chain if 0.3 * target <= n <= 3.5 * target)
    out.append(f"Full committed search window [0.3,3.5]*target: "
                f"{len(window)} candidates -> {sorted(window)}")
    cands = sorted(window, key=lambda n: abs(math.log(n) - math.log(target)))
    top6 = cands[:6]
    out.append(f"Top-6 by log-closeness to target (what find_passer(22, ...) "
                f"actually iterates, n_tries=6): {top6}")
    out.append("")

    rows = []
    header = (f"{'n':>8} {'n/L^22':>8} {'cd':>3} {'feasible':>9} "
              f"{'fail_pre':>8} {'worst_bits':>10} {'worst_log2':>11} "
              f"{'resolved(<=40mv,75s)':>21} {'moves':>6}")
    out.append("Item 1 main table (committed script's actual top-6, both crash depths). "
                "The 'resolved' column shares ONE 75s deadline across the whole table, "
                "matching find_passer's actual semantics (deadline computed once per p, "
                "not per candidate) -- not 75s per row.")
    out.append(header)
    shared_deadline = time.time() + 75.0
    for n in top6:
        T3 = 3 ** n
        K = T3.bit_length()
        q = (1 << K) - T3
        for cd in (1, 2):
            res = committed_base_construct(p, n, K, cd)
            if res is None:
                out.append(f"{n:>8} {n/target:>8.3f} {cd:>3} {'NO':>9}  "
                           f"(rounded climb profile hits a depth < 1 block)")
                rows.append(dict(n=n, ratio=n/target, cd=cd, feasible=False))
                continue
            ms0, ss0 = res
            Rs0 = committed_all_R(ms0, ss0)
            fail_pre = sum(1 for R in Rs0 if R < q)
            worst_bits = min(bit_margin(R, q) for R in Rs0)
            worst_log2 = min(log2_margin(R, q) for R in Rs0)
            if time.time() > shared_deadline:
                resolved, moves = None, None
                out.append(f"{n:>8} {n/target:>8.3f} {cd:>3} {'yes':>9} "
                           f"{fail_pre:>8} {worst_bits:>10} {worst_log2:>11.2f} "
                           f"{'deadline exhausted':>21} {'--':>6}")
            else:
                fixed = committed_bounded_correction(list(ms0), list(ss0), q,
                                                      max_moves=40, deadline=shared_deadline)
                resolved = fixed is not None
                moves = fixed[2] if fixed else None
                out.append(f"{n:>8} {n/target:>8.3f} {cd:>3} {'yes':>9} "
                           f"{fail_pre:>8} {worst_bits:>10} {worst_log2:>11.2f} "
                           f"{str(resolved):>21} {str(moves):>6}")
            rows.append(dict(n=n, ratio=n/target, cd=cd, feasible=True,
                              fail_pre=fail_pre, worst_bits=worst_bits,
                              worst_log2=worst_log2, resolved=resolved,
                              moves=moves))

    out.append("")
    out.append("Reconstruction of the 'supplementary wider' set "
                "(staircase-allp-findings.md item 3: 'up to 60 correction "
                "moves, no wall-clock cap, a wider Diophantine candidate "
                "set' -- the exact candidate list was NOT recorded there, "
                "so this is a labeled best-effort reconstruction, not a "
                "literal replay: top-20 candidates by log-closeness within "
                "an expanded [0.15,5]*target window, both crash depths. "
                "Reporting the SAME COLUMNS the brief asks for -- n, scale "
                "ratio, pre-correction fail count, worst margin -- since "
                "that is what item 1 requires here; the correction/'moves "
                "to resolve' step is the separate, expensive question item "
                "2 addresses via its own resolved-status check on the "
                "actual top-6, not re-run here for cost reasons on 20 "
                "candidates x 2 crash depths x up to 60 moves each with "
                "big-integer R_r at this scale):")
    window_wide = sorted(n for n in chain if 0.15 * target <= n <= 5.0 * target)
    cands_wide = sorted(window_wide, key=lambda n: abs(math.log(n) - math.log(target)))
    top20 = cands_wide[:20]
    out.append(f"Widened window candidates: {sorted(window_wide)}")
    out.append(f"Top-20 tried: {top20}")
    header2 = (f"{'n':>8} {'n/L^22':>8} {'cd':>3} {'feasible':>9} "
               f"{'fail_pre':>8} {'worst_bits':>10} {'worst_log2':>11}")
    out.append(header2)
    wide_rows = []
    for n in top20:
        T3 = 3 ** n
        K = T3.bit_length()
        q = (1 << K) - T3
        for cd in (1, 2):
            res = committed_base_construct(p, n, K, cd)
            if res is None:
                out.append(f"{n:>8} {n/target:>8.3f} {cd:>3} {'NO':>9}")
                wide_rows.append(dict(n=n, ratio=n/target, cd=cd, feasible=False))
                continue
            ms0, ss0 = res
            Rs0 = committed_all_R(ms0, ss0)
            fail_pre = sum(1 for R in Rs0 if R < q)
            worst_bits = min(bit_margin(R, q) for R in Rs0)
            worst_log2 = min(log2_margin(R, q) for R in Rs0)
            out.append(f"{n:>8} {n/target:>8.3f} {cd:>3} {'yes':>9} "
                       f"{fail_pre:>8} {worst_bits:>10} {worst_log2:>11.2f}")
            wide_rows.append(dict(n=n, ratio=n/target, cd=cd, feasible=True,
                                   fail_pre=fail_pre, worst_bits=worst_bits,
                                   worst_log2=worst_log2))
    return "\n".join(out), rows, wide_rows, window, chain


# =====================================================================
# SECTION 2 (ITEMS 2-4). Independently written implementations. No code
# from experiments/staircase_allp.py (or Section 1 above) is reused here.
# =====================================================================

def R_single_fresh(ms, ss, r):
    """Independent implementation of cycles.md 12.6.1's rotation sum
    R_r = sum_t 3^(M_t) 2^(S_t) (2^(s_t) - 1), M_t = sum_{j>t} m_j,
    S_t = sum_{j<t} sigma_j, sigma_j = s_j + m_{j+1 mod p} (so that
    sum sigma_j = sum s_j + n, matching 12.1.1's K = sum s_t + n).
    O(p) per rotation via cumulative suffix/prefix sums (itertools-style
    accumulation, computed with running totals rather than
    staircase_allp.py's specific Msuf/Spre variable names/order -- an
    independent pass over the same closed-form definition, kept O(p) per
    rotation for the large-n cases item 1's supplementary reconstruction
    needs)."""
    p = len(ms)
    mm = ms[r:] + ms[:r]
    sss = ss[r:] + ss[:r]
    # M_t = sum_{j>t} mm[j], built back-to-front.
    M = [0] * p
    running = 0
    for t in range(p - 1, -1, -1):
        M[t] = running
        running += mm[t]
    total = 0
    S = 0
    for t in range(p):
        total += (3 ** M[t]) * (1 << S) * ((1 << sss[t]) - 1)
        S += sss[t] + mm[(t + 1) % p]
    return total


def R_all_fresh(ms, ss):
    return [R_single_fresh(ms, ss, r) for r in range(len(ms))]


def sanity_identity_fresh():
    """cf. cycles.md 12.6.1 remark: the trivial cycle as a fake period-p
    cycle gives R = 4^p - 3^p = q exactly."""
    ok = True
    detail = []
    for p in (1, 2, 3, 4, 7):
        ms = [1] * p
        ss = [1] * p
        Rs = R_all_fresh(ms, ss)
        q = 4 ** p - 3 ** p
        good = all(R == q for R in Rs)
        detail.append((p, good))
        ok = ok and good
    return ok, detail


def construct_12_8_6_2_fresh(p, n, K, crash_depth=1,
                              rounding=decimal.ROUND_HALF_EVEN):
    """Independent implementation of Construction 12.8.6.2: p-1 climb
    blocks of unit exit valuation, geometric depths of ratio L rounded by
    the partial-sum method, plus one crash block of the given depth and
    the whole remaining exit-valuation budget. Returns (ms, ss) or None."""
    S = K - n
    if p < 2 or S <= p - 1:
        return None
    climb_n = n - crash_depth
    blocks = p - 1
    if climb_n < blocks:
        return None
    c = decimal.Decimal(climb_n) * (L - 1) / (L ** blocks - 1)
    prev = 0
    ms = []
    for j in range(blocks):
        Tj = c * (L ** (j + 1) - 1) / (L - 1)
        Mj = int(Tj.to_integral_value(rounding=rounding))
        ms.append(Mj - prev)
        prev = Mj
    ms[-1] += climb_n - sum(ms)
    if min(ms) < 1:
        return None
    ms = ms + [crash_depth]
    ss = [1] * blocks + [S - blocks]
    if ss[-1] < 1:
        return None
    return ms, ss


# ---------------------------------------------------------------------
# Item 2: pincer hypothesis test + calibration cross-check.
# ---------------------------------------------------------------------

def item2_calibration_row(p, n, label):
    T3 = 3 ** n
    K = T3.bit_length()
    q = (1 << K) - T3
    out = [f"-- {label}: p={p}, n={n} --"]
    for cd in (1, 2):
        res = construct_12_8_6_2_fresh(p, n, K, cd)
        if res is None:
            out.append(f"  crash_depth={cd}: base construction infeasible "
                        f"(rounded profile has a climb block < 1)")
            continue
        ms, ss = res
        Rs = R_all_fresh(ms, ss)
        fail = sum(1 for R in Rs if R < q)
        worst_bits = min(bit_margin(R, q) for R in Rs)
        worst_log2 = min(log2_margin(R, q) for R in Rs)
        out.append(f"  crash_depth={cd}: fail_pre={fail}/{p}, "
                    f"worst_bit_margin={worst_bits}, "
                    f"worst_log2_margin={worst_log2:.2f}")
    return "\n".join(out)


def item2_full():
    out = []
    out.append(item2_calibration_row(21, 15601,
                "Merle calibration row (his numbers: 3 failing, worst -2.27)"))
    out.append("")
    target23 = LF ** 23
    out.append(f"p=23 candidate-n note: the brief flags Merle's 'n ~= 39468' "
                f"as a glyph-mangled reconstruction from scale arithmetic "
                f"(main session's guess), not a verbatim transmitted digit "
                f"string. L^23 = {target23:.2f}. Checking against our OWN "
                f"Diophantine chain (same sign-agnostic candidate logic "
                f"'our stack' uses, Section 1): the chain has NO candidate "
                f"anywhere near 39468 -- its two nearest neighbors are "
                f"31867 (below, ratio {31867/target23:.3f}) and 47468 "
                f"(above, ratio {47468/target23:.3f}), each roughly "
                f"8000 away from 39468, i.e. 39468 sits in the middle of a "
                f"chain gap, matching neither. This is evaluated at face "
                f"value below (his literal reconstructed digits, whatever "
                f"their provenance) since that is what item 2 asks to "
                f"cross-check; the chain-mismatch is a separate finding, "
                f"flagged here rather than silently substituting a "
                f"'nicer' n.")
    out.append(item2_calibration_row(23, 39468,
                "Merle's literal reconstructed value (his numbers: 4 failing, worst -3.77)"))
    return "\n".join(out)


# ---------------------------------------------------------------------
# Item 3: independent re-run of Merle's ledger seed #3 on the p=7 instance.
# ---------------------------------------------------------------------

def item3_full():
    out = []
    m = [4, 7, 9, 15, 23, 35, 1]
    n = sum(m)
    K = (3 ** n).bit_length()
    q = (1 << K) - 3 ** n
    S = K - n
    s = [1, 1, 1, 1, 1, 1, S - 6]
    assert sum(s) == S
    Rs = R_all_fresh(m, s)
    gamma = K - math.log2(q)
    out.append(f"p=7 instance (cycles.md 12.8.3): m={m}, n={n}, K={K}, "
                f"gamma={gamma:.4f} (published/12.8.6.4 cross-check: 6.7438/6.744)")
    out.append(f"q odd: {q % 2 == 1} (structural: q = 2^K - 3^n = even - odd, "
                f"true for every configuration)")
    out.append(f"3 does not divide q: {q % 3 != 0} "
                f"(structural: q = (-1)^K mod 3, true for every configuration)")
    ok = min(Rs) >= q
    assert ok
    div_ok = [R % q == 0 for R in Rs]
    out.append(f"Z-solvability (q | R_r) per rotation: {div_ok} "
                f"-- 0/7 solvable, matching 12.8.3's own divisibility record "
                f"('All fail the divisibility conditions q | R_r').")
    out.append("")
    out.append(f"{'rotation':>8} {'R_r mod q dist to nearest integer / q':>40}")
    dists = []
    for r, R in enumerate(Rs):
        rem = R % q
        dist = min(rem, q - rem)
        frac = dist / q
        dists.append(frac)
        out.append(f"{r:>8} {frac:>40.4f}")
    out.append(f"Range found: [{min(dists):.4f}, {max(dists):.4f}] "
                f"-- Merle's reported range: [0.05, 0.48]")
    return "\n".join(out), dists


# ---------------------------------------------------------------------
# Item 4: the continued-fraction hole claim.
# ---------------------------------------------------------------------

def cf_terms_fresh(x, nterms):
    """Independent CF routine (own control flow: collects convergents in
    the same pass rather than a separate recurrence call site)."""
    terms = []
    y = x
    for _ in range(nterms):
        a = int(y)
        terms.append(a)
        frac = y - a
        if frac == 0:
            break
        y = 1 / frac
    return terms


def cf_convergents_fresh(terms):
    h = [0, 1]
    k = [1, 0]
    hs, ks = [], []
    for a in terms:
        newh = a * h[-1] + h[-2]
        newk = a * k[-1] + k[-2]
        h.append(newh)
        k.append(newk)
        hs.append(newh)
        ks.append(newk)
    return hs, ks


def item4_full():
    out = []
    terms = cf_terms_fresh(L, 20)
    hs, ks = cf_convergents_fresh(terms)
    out.append(f"Continued fraction of log2(3), terms[0:20] = {terms}")
    idx23 = [i for i, a in enumerate(terms) if a == 23]
    out.append(f"Partial quotient 23 found at index/indices: {idx23}")
    for i in idx23:
        out.append(f"  convergent at that index: h_{i}={hs[i]}, k_{i}={ks[i]} "
                    f"-- denominator 15601 confirmed: {ks[i] == 15601}")

    signs = [hs[i] - ks[i] * L for i in range(len(terms))]
    out.append("")
    out.append(f"{'i':>3} {'a_i':>4} {'h_i':>10} {'q_i':>10} {'sign(h_i-q_iL)':>15}")
    for i in range(len(terms)):
        out.append(f"{i:>3} {terms[i]:>4} {hs[i]:>10} {ks[i]:>10} "
                    f"{'pos' if signs[i] > 0 else 'neg':>15}")

    # "Good n" grid per lemma 12.8.6.1: for index i (playing the role of
    # k-1) with sign[i] > 0, semiconvergents n_j = k_i + j*k_{i+1},
    # j = 1..a_{i+2} (a_{i+2} = terms[i+2]), inheriting the sign.
    lo, hi = 10 ** 4, 10 ** 5
    grid = set()
    for i in range(len(terms)):
        if signs[i] <= 0:
            continue
        if i + 2 >= len(terms):
            continue
        a_next = terms[i + 2]
        for j in range(0, a_next + 1):   # include j=0 (= k_i itself)
            nval = ks[i] + j * ks[i + 1]
            if lo <= nval <= hi:
                grid.add(nval)
    grid_sorted = sorted(grid)
    out.append("")
    out.append(f"Lemma 12.8.6.1 'good n' grid (sign-filtered semiconvergents) "
                f"in [{lo},{hi}]: {len(grid_sorted)} points")
    out.append(f"{grid_sorted}")
    gaps = [(grid_sorted[i], grid_sorted[i + 1], grid_sorted[i + 1] - grid_sorted[i],
             grid_sorted[i + 1] / grid_sorted[i])
            for i in range(len(grid_sorted) - 1)]
    gaps_sorted = sorted(gaps, key=lambda t: t[2], reverse=True)
    out.append("")
    out.append("Largest additive gaps in that grid (lo, hi, gap, ratio):")
    for g in gaps_sorted[:5]:
        out.append(f"  {g}")
    out.append("")
    out.append(f"Merle's stated hole: (15601, 31202). Is 31202 in our "
                f"sign-filtered good-n grid: {31202 in grid}")
    out.append(f"Is 15601 in the grid: {15601 in grid}; "
                f"its immediate successor in the grid: "
                f"{grid_sorted[grid_sorted.index(15601)+1] if 15601 in grid_sorted and grid_sorted.index(15601)+1 < len(grid_sorted) else 'n/a'}")

    # Also report the committed script's raw (sign-agnostic) chain gap in
    # the same window, since item 1's table shows the committed script's
    # OWN candidate list has a visible hole too -- a different, useful
    # comparison, not a substitute for the lemma's own grid above.
    max_n = int(4 * LF ** 25) + 10
    raw_chain = committed_build_candidate_chain(max_n)
    raw_window = sorted(n for n in raw_chain if lo <= n <= hi)
    raw_gaps = [(raw_window[i], raw_window[i + 1], raw_window[i + 1] - raw_window[i])
                for i in range(len(raw_window) - 1)]
    raw_gaps_sorted = sorted(raw_gaps, key=lambda t: t[2], reverse=True)
    out.append("")
    out.append("For comparison (not the lemma's grid): the COMMITTED "
                "script's raw, sign-agnostic candidate chain in the same "
                "window, and its largest gap:")
    out.append(f"{raw_window}")
    out.append(f"Largest raw-chain gaps: {raw_gaps_sorted[:3]}")

    return "\n".join(out), grid_sorted, gaps_sorted, raw_window, raw_gaps_sorted


if __name__ == "__main__":
    print("=" * 70)
    print("SANITY: fresh R_all_fresh reproduces the trivial-cycle identity")
    ok, detail = sanity_identity_fresh()
    print(f"  {'pass' if ok else 'FAIL'}: {detail}")
    assert ok

    print()
    print("=" * 70)
    print("ITEM 1: p=22 candidate/margin table (committed script's own logic, instrumented)")
    text1, rows, wide_rows, window, chain = item1_report()
    print(text1)

    print()
    print("=" * 70)
    print("ITEM 2: pincer hypothesis test + calibration cross-check")
    print(item2_full())

    print()
    print("=" * 70)
    print("ITEM 3: p=7 seed #3 independent re-run")
    text3, dists = item3_full()
    print(text3)

    print()
    print("=" * 70)
    print("ITEM 4: continued-fraction hole check")
    text4, grid_sorted, gaps_sorted, raw_window, raw_gaps_sorted = item4_full()
    print(text4)
