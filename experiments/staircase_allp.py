# Staircase family at every period (cycles.md 12.8.6): fresh, independent
# verification. Imports nothing from uniform_trim.py (which produced the
# original p in {6,7} instances of Remark 12.8.3) -- this script is the
# independent check, built from the theorem statement alone.
#
# Supports: cycles.md 12.8.6 (Diophantine input lemma, explicit staircase
# construction, bounded correction algorithm, verified-instance record).
#
# Exact big-integer arithmetic in every pass/fail decision:
#   - K = (3**n).bit_length() is the exact ceiling of n*log2(3) (no floats).
#   - q = 2**K - 3**n is computed exactly.
#   - every rotation sum R_r is computed exactly and compared to q by
#     ordinary Python integer comparison.
# The only place floating/decimal arithmetic appears is in *choosing* which
# candidate n to try (the Diophantine step) -- never in a pass/fail decision.
#
# Structure:
#   Part A. Diophantine candidate generator: continued-fraction convergents
#           and semiconvergents of L = log2(3), via decimal.Decimal at high
#           precision (candidate generation only).
#   Part B. Exact rotation-sum machinery R_r (cycles.md 12.6.1), independent
#           implementation.
#   Part C. The explicit construction: p-1 "climb" blocks with unit exit
#           valuation and depths rounded from a geometric profile of ratio
#           L (by rounding the *partial sums*, which keeps the rounding
#           error bounded by 1/2 at every prefix rather than accumulating),
#           closed by one "crash" block of small depth and the leftover
#           exit-valuation budget.
#   Part D. A bounded, deterministic correction procedure: when the base
#           construction falls short of q on some rotation by a small
#           margin, it moves single units of depth between climb blocks,
#           always accepting the move that most improves the worst rotation
#           margin, until every rotation passes or a move budget is
#           exhausted. This is not a cycle search: it constructs a single
#           witness configuration per period from an explicit starting
#           point, with a capped, auditable number of local moves recorded
#           alongside every instance.
#   Part E. Driver: for every period p in the verified range, find a
#           passing configuration, check q > 0, all p rotation conditions,
#           gamma, and (bounded observation only) whether it also happens
#           to pass the full divisibility system -- expected never.
#   Part F. Cross-check against the published p = 7 instance (12.8.3).
#
# Verified range and result: see the printed table and cycles.md 12.8.6 for
# the date and range this was last run over.

import decimal
import math
import sys
import time

decimal.getcontext().prec = 600
L = decimal.Decimal(3).ln() / decimal.Decimal(2).ln()   # log2(3), high precision
LF = float(L)


# ---------------------------------------------------------------------
# Part A. Diophantine candidates: continued fraction of L = log2(3).
# ---------------------------------------------------------------------

def cf_terms(x, nterms):
    """Partial quotients of x (a decimal.Decimal), candidate generation only."""
    terms = []
    for _ in range(nterms):
        a = int(x)
        terms.append(a)
        frac = x - a
        if frac == 0:
            break
        x = 1 / frac
    return terms


def build_candidate_chain(max_n, cf_depth=30):
    """All convergent and semiconvergent denominators n of L up to max_n,
    i.e. n = q_{k-1} + j*q_k for j = 1..a_{k+1} (j = a_{k+1} being the next
    full convergent). These are exactly the n at which K = ceil(n*L)
    approximates n*L unusually well from above or below (candidate
    generation only -- every claim about a specific n below is re-verified
    exactly)."""
    terms = cf_terms(L, cf_depth)
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


# ---------------------------------------------------------------------
# Part B. Exact rotation sums (cycles.md 12.6.1), independent
# implementation of R_r = sum_t 3^(M_t) 2^(S_t) (2^(s_t)-1).
# ---------------------------------------------------------------------

def R_rot(ms, ss):
    """R_r for the rotation r = 0 of the given (already-rotated) sequences."""
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


def all_R(ms, ss):
    p = len(ms)
    return [R_rot(ms[r:] + ms[:r], ss[r:] + ss[:r]) for r in range(p)]


# ---------------------------------------------------------------------
# Part C. The explicit construction.
# ---------------------------------------------------------------------

def climb_partial_sum_round(climb_n, blocks, rounding=decimal.ROUND_HALF_EVEN):
    """Round the geometric profile m_j ~ c * L^j (j = 0..blocks-1, ratio L,
    total climb_n) to integers by rounding the PARTIAL SUMS T_j = c*(L^{j+1}
    - 1)/(L-1) to the nearest integer at every prefix, then differencing.
    This keeps the rounding error bounded by 1/2 at every prefix, instead of
    letting per-term rounding errors accumulate additively over p terms."""
    c = decimal.Decimal(climb_n) * (L - 1) / (L ** blocks - 1)
    prev = 0
    ms = []
    for j in range(blocks):
        Tj = c * (L ** (j + 1) - 1) / (L - 1)
        Mj = int(Tj.to_integral_value(rounding=rounding))
        ms.append(Mj - prev)
        prev = Mj
    diff = climb_n - sum(ms)
    ms[-1] += diff          # exact by construction of c; this is always 0
    return ms


def base_construct(p, n, K, crash_depth=1):
    """p-1 climb blocks (unit exit valuation, geometric depths of ratio L)
    plus one crash block of depth crash_depth and exit valuation
    S - (p-1) (the whole remaining exit-valuation budget). Returns
    (ms, ss) or None if this (p, n, crash_depth) combination is infeasible
    (too little climb mass, or too little exit-valuation budget)."""
    S = K - n
    if p < 2 or S <= p - 1:
        return None
    climb_n = n - crash_depth
    if climb_n < p - 1:
        return None
    ms = climb_partial_sum_round(climb_n, p - 1)
    if min(ms) < 1:
        return None
    ms = ms + [crash_depth]
    ss = [1] * (p - 1) + [S - (p - 1)]
    if ss[-1] < 1:
        return None
    return ms, ss


# ---------------------------------------------------------------------
# Part D. Bounded deterministic correction.
# ---------------------------------------------------------------------

def bounded_correction(ms, ss, q, max_moves=40, escalate_after=15, deadline=None):
    """Repeatedly identify the worst (minimal-R_r) rotation and move one
    unit of climb depth from some donor block to some recipient block,
    accepting whichever single-unit move most increases the worst-rotation
    margin. Never touches the crash block's depth. Uses a small, cheap
    candidate set (offsets relative to the worst rotation) for the first
    `escalate_after` moves, then escalates to the full O(p^2) donor x
    recipient search if the cheap set has stalled. Returns
    (ms, ss, moves_used) on success, None if the move budget is exhausted
    without every rotation passing.

    This is a fixed, auditable local-search procedure applied to ONE
    candidate configuration -- it is not a search over cycles or over the
    divisibility system, and every move is logged in moves_used."""
    p = len(ms)
    crash_idx = p - 1
    moves = 0
    while moves < max_moves:
        if deadline is not None and time.time() > deadline:
            return None
        Rs = all_R(ms, ss)
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
            m2 = min(all_R(ms2, ss))
            if best is None or m2 > best[0]:
                best = (m2, i, j)
        if best is None or best[0] <= minR:
            if cheap:
                # fall straight through to the full search on the next
                # iteration by forcing escalate_after down to 0
                escalate_after = 0
                continue
            return None
        _, i, j = best
        ms[i] -= 1
        ms[j] += 1
        moves += 1
    Rs = all_R(ms, ss)
    if min(Rs) >= q:
        return ms, ss, moves
    return None


# ---------------------------------------------------------------------
# Part E. Driver: find a verified passer for every p in a range.
# ---------------------------------------------------------------------

def find_passer(p, chain, n_tries=8, crash_depths=(1, 2), max_moves=40,
                 wall_clock_budget=25.0):
    """Try the top n_tries candidate n (closest in log-scale to L**p) from
    the Diophantine chain, each with a couple of crash depths, applying the
    bounded correction. Returns a dict with the full record, or None.

    wall_clock_budget caps the total time spent on this p (seconds) so an
    unusually hard period degrades to a fast, honest UNRESOLVED instead of
    an unbounded hang -- it does not change any pass/fail decision, which
    stays exact throughout; it only stops trying further candidates."""
    deadline = time.time() + wall_clock_budget
    target = LF ** p
    cands = sorted(
        (n for n in chain if 0.3 * target <= n <= 3.5 * target),
        key=lambda n: abs(math.log(n) - math.log(target)),
    )
    for n in cands[:n_tries]:
        if time.time() > deadline:
            break
        T3 = 3 ** n
        K = T3.bit_length()          # exact ceil(n log2 3), no floats
        q = (1 << K) - T3            # exact; always > 0 since K = ceil
        assert q > 0
        for cd in crash_depths:
            if time.time() > deadline:
                break
            res = base_construct(p, n, K, cd)
            if res is None:
                continue
            ms0, ss0 = res
            fixed = bounded_correction(list(ms0), list(ss0), q,
                                        max_moves=max_moves, deadline=deadline)
            if fixed is None:
                continue
            ms, ss, moves = fixed
            Rs = all_R(ms, ss)
            assert min(Rs) >= q                      # re-verify, exact
            assert sum(ms) == n and sum(ss) == K - n  # budget conservation
            gamma = K - math.log2(q)
            div_ok = all(R % q == 0 for R in Rs)      # bounded observation
            if div_ok:
                print(f"!!! HALT: p={p} n={n} passes size AND divisibility "
                      f"-- this reconstructs a genuine cycle candidate. "
                      f"Stopping immediately for main-session review.")
                sys.exit(1)
            return dict(p=p, n=n, K=K, q=q, gamma=gamma, crash_depth=cd,
                        moves=moves, ms=ms, ss=ss, div_ok=div_ok)
    return None


def run(pmin=2, pmax=25, n_tries=8, max_moves=40, wall_clock_budget=25.0):
    max_n = int(4 * LF ** pmax) + 10
    chain = build_candidate_chain(max_n)
    print(f"Diophantine candidate chain: {len(chain)} convergents/"
          f"semiconvergents of log2(3) up to n={max_n}")
    print(f"{'p':>3} {'n':>10} {'gamma':>8} {'gamma/log2p':>12} "
          f"{'crash_d':>7} {'moves':>6}  n/1.585^p")
    records = []
    unresolved = []
    for p in range(pmin, pmax + 1):
        rec = find_passer(p, chain, n_tries=n_tries, max_moves=max_moves,
                           wall_clock_budget=wall_clock_budget)
        if rec is None:
            unresolved.append(p)
            print(f"{p:>3}  UNRESOLVED (top-{n_tries} candidate n, "
                  f"<= {max_moves} correction moves each, "
                  f"<= {wall_clock_budget:.0f}s)", flush=True)
            continue
        records.append(rec)
        ratio = rec["gamma"] / math.log2(p) if p > 1 else float("nan")
        print(f"{p:>3} {rec['n']:>10} {rec['gamma']:>8.3f} {ratio:>12.3f} "
              f"{rec['crash_depth']:>7} {rec['moves']:>6}  "
              f"{rec['n'] / LF**p:5.2f}", flush=True)
    return records, unresolved


# ---------------------------------------------------------------------
# Part F. Cross-check against the published p = 7 instance (12.8.3).
# ---------------------------------------------------------------------

def crosscheck_p7():
    m = [4, 7, 9, 15, 23, 35, 1]
    n = sum(m)
    K = (3 ** n).bit_length()
    q = (1 << K) - 3 ** n
    S = K - n
    s = [1, 1, 1, 1, 1, 1, S - 6]
    assert sum(s) == S
    Rs = all_R(m, s)
    gamma = K - math.log2(q)
    ok = min(Rs) >= q
    print(f"Cross-check, published p=7 instance (12.8.3): n={n}, "
          f"gamma={gamma:.3f} (published: 6.74), all rotations pass: {ok}")
    assert ok
    assert abs(gamma - 6.744) < 0.01
    div_ok = all(R % q == 0 for R in Rs)
    print(f"  divisibility (expected False, matching 12.8.3): {div_ok}")
    assert not div_ok
    return gamma


# ---------------------------------------------------------------------
# Part G. Sanity identity (cf. cycles.md 12.6.1 remark): the trivial cycle
# treated as a fake period-p cycle gives R = 4^p - 3^p = q exactly.
# ---------------------------------------------------------------------

def sanity_identity():
    ok = True
    for p in (1, 2, 3, 4, 7):
        ms = [1] * p
        ss = [1] * p
        Rs = all_R(ms, ss)
        q = 4 ** p - 3 ** p
        if not all(R == q for R in Rs):
            ok = False
    print(f"Sanity identity (trivial cycle, R = 4^p - 3^p, p in "
          f"{{1,2,3,4,7}}): {'pass' if ok else 'FAIL'}")
    assert ok


if __name__ == "__main__":
    sanity_identity()
    print(flush=True)
    crosscheck_p7()
    print(flush=True)
    records, unresolved = run(pmin=2, pmax=25, n_tries=6, max_moves=40,
                               wall_clock_budget=75.0)
    print(flush=True)
    if records:
        ratios = [r["gamma"] / math.log2(r["p"]) for r in records if r["p"] > 1]
        print(f"Resolved periods: {sorted(r['p'] for r in records)}")
        print(f"gamma/log2(p) over resolved range: "
              f"min={min(ratios):.3f} max={max(ratios):.3f}")
    if unresolved:
        print(f"Unresolved periods (obstruction; see cycles.md 12.8.6): "
              f"{unresolved}")
    else:
        print("All periods in range resolved.")
