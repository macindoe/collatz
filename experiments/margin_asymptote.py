"""Exact asymptotics of the capacity-demand margin, and the mod-7 mechanism table.

Supports: cycles.md 12.6.1.3 asymptote addendum, the mod-7 remark near 12.6.1.1,
and the shared-ledger L-A3 asymptote upgrade (briefs/merle-round8-coedit-*).

Fresh code: imports nothing from merle_round8_check.py or any Merle repository.
Every COUNT in this file is exact integer combinatorics (math.comb, integer DP,
direct enumeration). Floats appear ONLY in logarithms of exact quantities
(math.log2, math.lgamma) and in the variational search for the limit constant;
no pass/fail decision about an integer identity uses floats.

DEFINITIONS (from Merle artifact REQ-MATH-014, matching cycles.md 12.6.1
conventions). A period-p profile is (m_t, s_t)_{t<p} with all entries >= 1,
sum m = n, sum s = S; K = S + n, q = 2^K - 3^n. On the tuned family
K = bitlength(3^n) = floor(n log2 3) + 1, so K = log2 q + o(1) and
S = K - n ~ (beta - 1) n with beta = log2 3.

    margin(n) = K - log2(#profiles)

  general family : all s_t >= 1; #profiles = sum_p C(n-1,p-1) C(S-1,p-1)
                   = C(K-2, n-1)  (Vandermonde).
  odd-step stratum: all s_t odd;  #profiles = sum_p C(n-1,p-1) oddcomp(S,p),
                   oddcomp(S,p) = C((S+p)/2 - 1, p-1) for S >= p, S = p mod 2
                   (substitute s_i = 2a_i + 1), else 0.

DERIVATION OF THE LIMITS (elementary; recorded in wiki prose in
briefs/merle-round8-coedit-findings.md).

Entropy bounds for the binomial (standard; e.g. Cover-Thomas Lemma 17.5.1,
via the binary-type class):  for 0 <= b <= a,

    2^(a H(b/a)) / (a+1)  <=  C(a, b)  <=  2^(a H(b/a)),

with H(x) = -x log2 x - (1-x) log2 (1-x) the binary entropy.

GENERAL FAMILY. #profiles = C(K-2, n-1) exactly, K = floor(n beta) + 1. The
bounds give log2 C(K-2, n-1) = (K-2) H((n-1)/(K-2)) + O(log n), and
(n-1)/(K-2) -> 1/beta, H continuous, so (1/n) log2 #profiles -> beta H(1/beta).
Hence

    margin/n  ->  c_gen = beta - beta H(1/beta) = beta (1 - H(1/beta)).

Expanding H(1/beta) = (1/beta) log2 beta + ((beta-1)/beta)(log2 beta
- log2(beta-1)) gives the closed form

    c_gen = beta - beta log2 beta + (beta-1) log2 (beta-1).

ODD-STEP STRATUM. #profiles = sum over p (with S = p mod 2, p <= min(n, S))
of T(p) := C(n-1, p-1) C((S+p)/2 - 1, p-1). Put alpha = p/n; the constraint
S >= p forces alpha <= S/n -> beta - 1, so alpha ranges over (0, beta-1].
Termwise the entropy bounds give

    (1/n) log2 T(alpha n) -> g(alpha)
      := H(alpha) + ((beta-1+alpha)/2) H( 2 alpha / (beta-1+alpha) ),

uniformly on compact subsets, with O(log n)/n error. The sandwich
max_p T(p) <= sum_p T(p) <= n * max_p T(p) costs another log2(n)/n, and the
discrete grid alpha = p/n is (2/n)-dense in the parity class, g continuous, so

    (1/n) log2 #profiles -> max_{alpha in (0, beta-1]} g(alpha),
    margin/n -> c_strat = beta - max_alpha g(alpha).

The maximum is interior (checked below by bracketing at alpha* +- eps; at the
right endpoint g(beta-1) = H(beta-1) < g(alpha*)), located by ternary search.
Both limits are limits of exact counting expressions; nothing heuristic enters
the constants. What remains heuristic is only the *reading* of the margin as a
2^(-margin) expected-cycle-count decay -- that clause stays labeled heuristic
wherever it is quoted (cycles.md 12.6.1.3 register).

PRECISION ARGUMENT for the lgamma extension (part 3): lgamma has relative
error ~1e-15; at n = 163,840 the log-binomials are ~2.6e5, so each log-term
carries absolute error ~1e-9. The log-sum-exp subtracts the max before
exponentiating (all summands in (0, 1]), so no cancellation amplifies the
error; summing <= 1e5 terms keeps the total error in log2(#profiles) below
~1e-4 absolute, i.e. below 1e-9 in margin/n. Cross-checked against exact
integer counts at every n <= 2560 (tolerance 1e-6, comfortably met).

PART 4 ENSEMBLES, stated: the orbit table and the n = 12 / 15 distribution
tables are EXACT (exhaustive enumeration of every tuned profile; the chi2 and
total-variation numbers are properties of the full finite family, not sample
estimates -- with exhaustive counts any nonzero deviation is real structure,
so chi2/df is not comparable across different family sizes; TV distance is
the comparable number). The n = 63 depth scan and the REQ-MATH-017-window
replication are SAMPLED (uniform-over-compositions sampler, seeded rng,
labeled in the output); they are spot tables, not key turns.
"""

import math
import random
from math import comb, lgamma, log2

LN2 = math.log(2.0)
BETA = log2(3.0)

failures = []
checks = 0


def check(label, ok):
    global checks
    checks += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        failures.append(label)


def H(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


# ------------------------------------------------------------------ counts

def count_general(n, S):
    """Exact: # profiles (m, s), p >= 1 parts, all entries >= 1."""
    return sum(comb(n - 1, p - 1) * comb(S - 1, p - 1)
               for p in range(1, min(n, S) + 1))


def oddcomp(S, p):
    """Exact: # compositions of S into p odd positive parts."""
    if S < p or (S - p) % 2:
        return 0
    return comb((S + p) // 2 - 1, p - 1)


def count_stratum(n, S):
    return sum(comb(n - 1, p - 1) * oddcomp(S, p)
               for p in range(1, min(n, S) + 1))


def compositions(total, parts):
    """All compositions of `total` into `parts` positive parts."""
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


# ------------------------------------------------------------ part 0: canaries

def part0_canaries():
    print("=== Part 0: canaries (hand-computed / brute-force, before any"
          " sweep) ===")

    # (a) Brute-force profile counts vs the formulas, small n, true tuned
    # (n, S). Enumerate compositions directly and count.
    print("  (a) brute-force enumeration vs closed formulas, n <= 12:")
    for n in range(4, 13):
        K = (3 ** n).bit_length()
        S = K - n
        bf_gen = bf_str = 0
        for p in range(1, min(n, S) + 1):
            for mm in compositions(n, p):
                for ss in compositions(S, p):
                    bf_gen += 1
                    if all(x % 2 == 1 for x in ss):
                        bf_str += 1
        check(f"0a n={n:2d} (K={K}, S={S}): general brute {bf_gen} =="
              f" formula {count_general(n, S)} == C(K-2,n-1)"
              f" {comb(K - 2, n - 1)}",
              bf_gen == count_general(n, S) == comb(K - 2, n - 1))
        check(f"0a n={n:2d}: stratum brute {bf_str} == formula"
              f" {count_stratum(n, S)}", bf_str == count_stratum(n, S))

    # (b) Vandermonde identity, exact, several (n, S) beyond the tuned pairs.
    print("  (b) Vandermonde sum == C(K-2, n-1), exact:")
    for (n, S) in [(5, 4), (7, 10), (12, 8), (20, 12), (33, 19), (50, 30)]:
        lhs = count_general(n, S)
        rhs = comb(n + S - 2, n - 1)
        check(f"0b (n,S)=({n},{S}): {lhs} == {rhs}", lhs == rhs)

    # (c) Odd-composition closed form vs a 2-D DP (exact, per part count).
    print("  (c) odd-composition closed form vs DP, S <= 30, every p:")
    ok = True
    for S in range(1, 31):
        # dp[p][t] = # compositions of t into p odd positive parts
        dp = [[0] * (S + 1) for _ in range(S + 2)]
        dp[0][0] = 1
        for p in range(1, S + 1):
            for t in range(1, S + 1):
                dp[p][t] = sum(dp[p - 1][t - part]
                               for part in range(1, t + 1, 2))
        for p in range(1, S + 1):
            if dp[p][S] != oddcomp(S, p):
                ok = False
    check("0c oddcomp(S,p) == DP for all S <= 30, all p", ok)

    # (d) Hand-computed binomial-entropy-bound instance: C(10,3) = 120,
    # 2^(10 H(0.3)) = 2^8.813 = 449.8, /11 = 40.9 -- bounds hold.
    lo = 2.0 ** (10 * H(0.3)) / 11.0
    hi = 2.0 ** (10 * H(0.3))
    check(f"0d entropy bounds at C(10,3)=120: {lo:.1f} <= 120 <= {hi:.1f}",
          lo <= 120 <= hi)
    print()


# ---------------------------------------------------- part 1: limit constants

def g_strat(alpha):
    if alpha <= 0.0 or alpha >= 1.0:
        return float("-inf")
    a2 = (BETA - 1.0 + alpha) / 2.0
    x = alpha / a2 / 2.0 * 2.0  # = 2 alpha / (beta - 1 + alpha)
    x = 2.0 * alpha / (BETA - 1.0 + alpha)
    if x >= 1.0:
        return float("-inf")
    return H(alpha) + a2 * H(x)


def part1_constants():
    print("=== Part 1: the two limit constants (closed / variational"
          " forms) ===")
    beta = BETA
    c_gen_closed = beta - beta * log2(beta) + (beta - 1.0) * log2(beta - 1.0)
    c_gen_entropy = beta * (1.0 - H(1.0 / beta))
    print(f"  beta = log2 3 = {beta:.12f}")
    print(f"  c_gen (closed form)   = beta - beta log2 beta"
          f" + (beta-1) log2(beta-1) = {c_gen_closed:.10f}")
    print(f"  c_gen (entropy form)  = beta (1 - H(1/beta))"
          f"                        = {c_gen_entropy:.10f}")
    check("1a the two c_gen forms agree to 1e-12",
          abs(c_gen_closed - c_gen_entropy) < 1e-12)
    check(f"1b c_gen positive, unambiguously: {c_gen_closed:.10f} > 0.001",
          c_gen_closed > 1e-3)

    # Ternary search for alpha* on (0, beta-1); the odd-composition
    # constraint S >= p forces alpha <= beta-1 (the brief's "(0,1)" is the
    # same problem: g = -inf beyond beta-1).
    lo, hi = 1e-9, beta - 1.0 - 1e-9
    for _ in range(300):
        m1 = lo + (hi - lo) / 3.0
        m2 = hi - (hi - lo) / 3.0
        if g_strat(m1) < g_strat(m2):
            lo = m1
        else:
            hi = m2
    astar = (lo + hi) / 2.0
    gmax = g_strat(astar)
    c_strat = beta - gmax
    eps = 1e-4
    print(f"  alpha* = {astar:.10f}   g(alpha*) = {gmax:.10f}")
    print(f"  bracketing: g(a*-{eps}) = {g_strat(astar - eps):.10f},"
          f" g(a*) = {gmax:.10f}, g(a*+{eps}) = {g_strat(astar + eps):.10f}")
    print(f"  endpoint: g(beta-1) = H(beta-1) = {H(beta - 1.0):.10f}"
          f" < g(alpha*)  [interior max, not at the boundary]")
    check("1c interior maximum: g(a*) > g(a* +- eps) and > endpoint values",
          gmax > g_strat(astar - eps) and gmax > g_strat(astar + eps)
          and gmax > H(beta - 1.0) and 0.0 < astar < beta - 1.0)
    print(f"  c_strat = beta - g(alpha*) = {c_strat:.10f}")
    check(f"1d c_strat positive, unambiguously: {c_strat:.10f} > 0.01",
          c_strat > 1e-2)

    # Against the brief's scratchpad targets (recorded, not forced: a
    # disagreement would be a finding).
    check("1e c_gen matches the stated target 0.07932 to 5e-5",
          abs(c_gen_closed - 0.07932) < 5e-5)
    check("1f c_strat matches the stated target 0.26679 to 5e-5",
          abs(c_strat - 0.26679) < 5e-5)
    check("1g alpha* matches the stated target 0.37473 to 5e-5",
          abs(astar - 0.37473) < 5e-5)
    print()
    return c_gen_closed, c_strat, astar


# ------------------------------------- parts 2-3: exact counts and extension

def lg_comb(a, b):
    """log2 C(a, b) via lgamma (floats only in logs)."""
    if b < 0 or b > a:
        return float("-inf")
    return (lgamma(a + 1) - lgamma(b + 1) - lgamma(a - b + 1)) / LN2


def margins_exact(n):
    K = (3 ** n).bit_length()
    S = K - n
    return (K - log2(count_stratum(n, S))) / n, \
           (K - log2(count_general(n, S))) / n


def margins_lgamma(n):
    K = (3 ** n).bit_length()
    S = K - n
    # general: single binomial
    mgen = (K - lg_comb(K - 2, n - 1)) / n
    # stratum: log-sum-exp over p with S = p (mod 2)
    logs = []
    for p in range(1 + (S % 2 != 1), min(n, S) + 1):
        if (S - p) % 2 == 0:
            logs.append(lg_comb(n - 1, p - 1)
                        + lg_comb((S + p) // 2 - 1, p - 1))
    mx = max(logs)
    tot = mx + log2(sum(2.0 ** (v - mx) for v in logs))
    return (K - tot) / n, mgen


def part23_tables(c_gen, c_strat):
    print("=== Part 2: exact-count margins on the REQ-MATH-014 grid"
          " (exact integers; floats only in the final log2) ===")
    grid = [10, 20, 40, 80, 160, 320, 640, 1280, 2560]
    exact = {}
    print(f"  {'n':>7} {'K':>8} {'mSt/n':>8} {'mGen/n':>8}")
    for n in grid:
        st, gen = margins_exact(n)
        exact[n] = (st, gen)
        print(f"  {n:>7} {(3 ** n).bit_length():>8} {st:>8.4f} {gen:>8.4f}")
    check("2a digit-exact reproduction at n=1280: stratum 0.2730",
          f"{exact[1280][0]:.4f}" == "0.2730")
    check("2b digit-exact reproduction at n=1280: general 0.0854",
          f"{exact[1280][1]:.4f}" == "0.0854")
    check("2c n=2560 cross-anchor vs round-8 findings: 0.2701 / 0.0825",
          f"{exact[2560][0]:.4f}" == "0.2701"
          and f"{exact[2560][1]:.4f}" == "0.0825")
    print()

    print("=== Part 3: lgamma/log-sum-exp extension to n = 163,840 ===")
    # Cross-check lgamma path against the exact path everywhere feasible.
    worst = 0.0
    for n in grid:
        st_e, gen_e = exact[n]
        st_l, gen_l = margins_lgamma(n)
        worst = max(worst, abs(st_e - st_l), abs(gen_e - gen_l))
    check(f"3a lgamma vs exact on the full grid n <= 2560: max abs"
          f" deviation {worst:.2e} < 1e-6", worst < 1e-6)

    big = [5120, 10240, 20480, 40960, 81920, 163840]
    allrows = [(n, *exact[n]) for n in grid]
    for n in big:
        st, gen = margins_lgamma(n)
        allrows.append((n, st, gen))
    print(f"  {'n':>7} {'mSt/n':>9} {'mGen/n':>9}   (limits: c_strat ="
          f" {c_strat:.5f}, c_gen = {c_gen:.5f})")
    for n, st, gen in allrows:
        print(f"  {n:>7} {st:>9.4f} {gen:>9.4f}")
    st_last, gen_last = allrows[-1][1], allrows[-1][2]
    print(f"  n=163840: stratum {st_last:.5f} (limit {c_strat:.5f},"
          f" gap {st_last - c_strat:.5f}), general {gen_last:.5f}"
          f" (limit {c_gen:.5f}, gap {gen_last - c_gen:.5f})")
    mono = all(allrows[i][1] > allrows[i + 1][1]
               and allrows[i][2] > allrows[i + 1][2]
               for i in range(len(allrows) - 1))
    above = all(st > c_strat and gen > c_gen for _, st, gen in allrows)
    check("3b margin/n strictly decreasing along the doubling grid"
          " 10 .. 163840, both families", mono)
    check("3c margin/n stays strictly above its limit at every grid point,"
          " both families", above)
    print("  Reading, stated exactly: the exact counts approach the limits"
          " monotonically from above on this grid; 'margin positive and"
          " growing linearly' cashes out to (i) positivity of the limit"
          " constants (part 1, unambiguous digits) plus (ii) this"
          " monotone-from-above convergence of the exact counts. The"
          " 2^(-margin) cycle-count reading remains the no-conspiracy"
          " HEURISTIC (REQ-MATH-014's own label), not a theorem.")
    print()


# ------------------------------------------------- part 4: mod-7 mechanism

def ord_mod(a, p):
    x, t = a % p, 1
    while x != 1:
        x = x * a % p
        t += 1
    return t


def tv_dist(counts):
    """Total-variation distance of a residue-count vector from uniform."""
    N = sum(counts)
    k = len(counts)
    return 0.5 * sum(abs(c / N - 1.0 / k) for c in counts)


def chi2_df(counts):
    N = sum(counts)
    p = len(counts)
    exp = N / p
    return sum((c - exp) ** 2 / exp for c in counts) / (p - 1), N


def r0_mod(mm, ss, pr, pow2, pow3):
    """R_0 mod pr, conventions of cycles.md 12.6.1: M_t = sum_{j>t} m_j,
    sigma_t = s_t + m_{(t+1) mod p}, S_t = sum_{j<t} sigma_j."""
    p = len(mm)
    M_t = [0] * p
    for t in range(p - 2, -1, -1):
        M_t[t] = M_t[t + 1] + mm[t + 1]
    r0 = 0
    St = 0
    for t in range(p):
        if t:
            St += ss[t - 1] + mm[t % p]
        r0 += pow3[M_t[t]] * pow2[St] % pr * (pow2[ss[t]] - 1)
    return r0 % pr


def part4_mod7():
    print("=== Part 4: the mod-7 mechanism table ===")
    primes = [5, 7, 11, 13, 31, 127]
    print("  (a) orbit data (exact):")
    print(f"  {'p':>4} {'ord_p(2)':>9} {'ord_p(3)':>9} {'|V| all s':>10}"
          f" {'0 in V?':>8} {'|V| odd s':>10} {'0 in V_odd?':>12}")
    orbit = {}
    for pr in primes:
        o2, o3 = ord_mod(2, pr), ord_mod(3, pr)
        v_all = {(pow(2, s, pr) - 1) % pr for s in range(1, o2 + 1)}
        v_odd = {(pow(2, s, pr) - 1) % pr for s in range(1, 2 * o2 + 1, 2)}
        orbit[pr] = (o2, o3, v_all, v_odd)
        print(f"  {pr:>4} {o2:>9} {o3:>9} {len(v_all):>10}"
              f" {str(0 in v_all):>8} {len(v_odd):>10} {str(0 in v_odd):>12}")
    check("4a |valueset(2^s - 1 mod p)| == ord_p(2) for every listed p",
          all(len(orbit[pr][2]) == orbit[pr][0] for pr in primes))
    check("4b ord_7(2) = 3 and the orbit is {0, 1, 3}",
          orbit[7][0] == 3 and orbit[7][2] == {0, 1, 3})
    check("4c odd-s restriction: orbit halves iff ord_p(2) even (5 -> {1,2},"
          " zero EXCLUDED); full orbit kept iff ord odd (7 -> {0,1,3} with"
          " the zero atom KEPT; likewise 31, 127)",
          len(orbit[7][3]) == 3 and 0 in orbit[7][3]
          and orbit[5][3] == {1, 2}
          and len(orbit[31][3]) == 5 and 0 in orbit[31][3]
          and len(orbit[127][3]) == 7 and 0 in orbit[127][3]
          and all(len(orbit[pr][3])
                  == (orbit[pr][0] if orbit[pr][0] % 2
                      else orbit[pr][0] // 2) for pr in primes))
    # Uniqueness of 7, provable in one line: ord_p(2) = 1 is impossible
    # (p | 1); ord_p(2) = 2 forces p | 3 (structural, not in the family);
    # ord_p(2) = 3 forces p | 2^3 - 1 = 7, i.e. p = 7. So among primes >= 5
    # the minimum possible 2-orbit is 3 values, attained by p = 7 ALONE; the
    # next-coarsest 2-orbits are 5 (4 values) and 31 (5 values).
    check("4d uniqueness: ord_p(2) = 3 => p | 7 (7 is the only prime with"
          " a 3-element 2-orbit)", all(pow(2, 3, pr) != 1
                                       for pr in [5, 11, 13, 31, 127]))

    # Canary for the R_0 implementation, before any distribution sweep:
    # the trivial profile m = s = (1,)*p has R_0 = 4^p - 3^p (cycles.md
    # 12.6.1's sanity identity), checked mod every listed prime, p <= 7;
    # and ([1],[1]) gives R_0 = 1.
    cpow2 = {pr: [pow(2, e, pr) for e in range(40)] for pr in primes}
    cpow3 = {pr: [pow(3, e, pr) for e in range(20)] for pr in primes}
    ok = all(r0_mod((1,) * pb, (1,) * pb, pr, cpow2[pr], cpow3[pr])
             == (4 ** pb - 3 ** pb) % pr
             for pb in range(1, 8) for pr in primes)
    check("4-canary trivial profile: R_0 = 4^p - 3^p mod every listed"
          " prime, p <= 7; and R_0([1],[1]) = 1",
          ok and all(r0_mod((1,), (1,), pr, cpow2[pr], cpow3[pr]) == 1 % pr
                     for pr in primes))

    # (b) EXHAUSTIVE depth-resolved distributions at n = 15: R_0 mod p by
    # block count (depth) p_blocks, general family; plus family aggregates
    # at n = 12, 15 (general and stratum) and single-term aggregates.
    n = 15
    K = (3 ** n).bit_length()
    S = K - n
    print(f"  (b) exhaustive depth-resolved table, n = {n} (K = {K},"
          f" S = {S}); TV distance of R_0 mod p from uniform, general"
          f" family, by block count:")
    pow2 = {pr: [pow(2, e, pr) for e in range(K + 1)] for pr in primes}
    pow3 = {pr: [pow(3, e, pr) for e in range(n + 1)] for pr in primes}
    by_depth = {}
    agg = {pr: {"gen_r0": [0] * pr, "str_r0": [0] * pr,
                "gen_term": [0] * pr, "str_term": [0] * pr}
           for pr in primes}
    for pb in range(1, min(n, S) + 1):
        cnts = {pr: [0] * pr for pr in primes}
        s_comps = list(compositions(S, pb))
        for mm in compositions(n, pb):
            M_t = [0] * pb
            for t in range(pb - 2, -1, -1):
                M_t[t] = M_t[t + 1] + mm[t + 1]
            for ss in s_comps:
                odd = all(x % 2 == 1 for x in ss)
                for pr in primes:
                    p2, p3 = pow2[pr], pow3[pr]
                    r0 = 0
                    St = 0
                    for t in range(pb):
                        if t:
                            St += ss[t - 1] + mm[t % pb]
                        term = p3[M_t[t]] * p2[St] % pr \
                            * (p2[ss[t]] - 1) % pr
                        r0 += term
                        agg[pr]["gen_term"][term] += 1
                        if odd:
                            agg[pr]["str_term"][term] += 1
                    r0 %= pr
                    cnts[pr][r0] += 1
                    agg[pr]["gen_r0"][r0] += 1
                    if odd:
                        agg[pr]["str_r0"][r0] += 1
        by_depth[pb] = cnts
        nrow = sum(cnts[primes[0]])
        print(f"    depth {pb:>2} (N = {nrow:>7}): "
              + " ".join(f"p={pr}: {tv_dist(cnts[pr]):.4f}"
                         for pr in primes))
    # Cross-prime comparison at tiny depths is only well-posed where the
    # family size dwarfs the residue count: at depth 2 the whole family has
    # 112 elements, so its TV from uniform over 31 or 127 bins is dominated
    # by granularity, not structure -- those two rows are excluded from the
    # small-prime comparison (they get their fair test at n = 63, N = 40,000
    # below, where 7 leads all six).
    check("4e small-depth bias is maximal at p = 7 among the well-posed"
          " comparisons {5, 7, 11, 13}, depths 2 and 3 (exhaustive)",
          all(tv_dist(by_depth[d][7])
              == max(tv_dist(by_depth[d][pr]) for pr in (5, 7, 11, 13))
              for d in (2, 3)))
    decay_ok = all(max(tv_dist(by_depth[d][pr]) for d in (6, 7))
                   < tv_dist(by_depth[2][pr]) / 5.0 for pr in primes)
    check("4f the bias decays with depth for EVERY listed prime: TV at"
          " depths 6-7 < TV at depth 2 / 5", decay_ok)

    print("  family aggregates (exhaustive; chi2/df is significance against"
          " a same-size random sample -- with exact counts any deviation is"
          " real, so compare TV, not chi2, across families):")
    for nn in (12, 15):
        if nn == 12:
            KK = (3 ** nn).bit_length()
            SS = KK - nn
            agg12 = {pr: {"gen_r0": [0] * pr, "str_r0": [0] * pr}
                     for pr in primes}
            p2b = {pr: [pow(2, e, pr) for e in range(KK + 1)]
                   for pr in primes}
            p3b = {pr: [pow(3, e, pr) for e in range(nn + 1)]
                   for pr in primes}
            for pb in range(1, min(nn, SS) + 1):
                s_comps = list(compositions(SS, pb))
                for mm in compositions(nn, pb):
                    for ss in s_comps:
                        odd = all(x % 2 == 1 for x in ss)
                        for pr in primes:
                            r0 = r0_mod(mm, ss, pr, p2b[pr], p3b[pr])
                            agg12[pr]["gen_r0"][r0] += 1
                            if odd:
                                agg12[pr]["str_r0"][r0] += 1
            src = agg12
        else:
            src = agg
        print(f"    n = {nn}: "
              + " ".join(f"p={pr}: TVgen {tv_dist(src[pr]['gen_r0']):.4f}"
                         f"/TVstr {tv_dist(src[pr]['str_r0']):.4f}"
                         for pr in (5, 7, 11)))
    print("    recorded, flat: at these small n the family aggregate is"
          " dominated by its modal depths, and there the residual deviation"
          " is LARGER at p = 5 than at p = 7 (TV 0.01-0.03 vs 0.001-0.008)"
          " -- the 7-bias is a small-depth phenomenon, not a family-"
          "aggregate one; single-term distributions (below) are far from"
          " uniform at every prime, so what separates primes is mixing"
          " speed under summation, which the orbit coarseness controls.")
    print("    single-term aggregates, n = 15: "
          + " ".join(f"p={pr}: TV {tv_dist(agg[pr]['gen_term']):.3f}"
                     for pr in primes))

    # (c) SAMPLED depth scan at n = 63 (the REQ-MATH-017 scale), general
    # family, and the REQ-MATH-017-window replication (stratum, block count
    # 5 -- the round-8 d2 ensemble). Sampled, seeded, labeled: spot table.
    print("  (c) sampled depth scan, n = 63, general family, N = 40,000"
          " per depth (TV from uniform; sampling noise floor ~0.4*sqrt(p/N)"
          " ~ 0.004-0.02):")
    rng = random.Random(20260724)
    n63 = 63
    K63 = (3 ** n63).bit_length()
    S63 = K63 - n63
    p2c = {pr: [pow(2, e, pr) for e in range(K63 + 1)] for pr in primes}
    p3c = {pr: [pow(3, e, pr) for e in range(n63 + 1)] for pr in primes}

    def rand_comp(total, parts):
        if parts == 1:
            return (total,)
        cuts = sorted(rng.sample(range(1, total), parts - 1))
        pts = [0] + list(cuts) + [total]
        return tuple(pts[i + 1] - pts[i] for i in range(parts))

    scan = {}
    for pb in (2, 3, 4, 6, 10, 20, 30):
        cnts = {pr: [0] * pr for pr in primes}
        for _ in range(40000):
            mm = rand_comp(n63, pb)
            ss = rand_comp(S63, pb)
            for pr in primes:
                cnts[pr][r0_mod(mm, ss, pr, p2c[pr], p3c[pr])] += 1
        scan[pb] = cnts
        print(f"    depth {pb:>2}: "
              + " ".join(f"p={pr}: {tv_dist(cnts[pr]):.4f}"
                         for pr in primes))
    check("4g n = 63, depth 2 (N = 40,000, all six well-posed): TV(mod 7)"
          " is the largest of the six primes, and TV(5) > TV(11)",
          tv_dist(scan[2][7]) == max(tv_dist(scan[2][pr]) for pr in primes)
          and tv_dist(scan[2][5]) > tv_dist(scan[2][11]))
    check("4h n = 63, depths >= 10: every prime's TV within 2x its own"
          " sampling noise floor 0.4 sqrt(p/N)",
          all(tv_dist(scan[d][pr]) < 0.8 * math.sqrt(pr / 40000.0)
              for d in (10, 20, 30) for pr in primes))

    print("  REQ-MATH-017-window replication (stratum, n = 63, block count"
          " 5, N = 30,000 -- the ensemble where his solitary-7 verdict"
          " lives; sampled):")

    def rand_odd_comp(SS, parts):
        A = (SS - parts) // 2
        if parts == 1:
            return (SS,)
        bars = sorted(rng.sample(range(A + parts - 1), parts - 1))
        pts = [-1] + list(bars) + [A + parts - 1]
        return tuple(2 * (pts[i + 1] - pts[i] - 1) + 1
                     for i in range(parts))

    cnts = {pr: [0] * pr for pr in primes}
    for _ in range(30000):
        mm = rand_comp(n63, 5)
        ss = rand_odd_comp(S63, 5)
        for pr in primes:
            cnts[pr][r0_mod(mm, ss, pr, p2c[pr], p3c[pr])] += 1
    for pr in primes:
        c2, N = chi2_df(cnts[pr])
        print(f"    mod {pr:>3}: chi2/df = {c2:6.2f}  TV = "
              f"{tv_dist(cnts[pr]):.4f}"
              + ("  <-- the largest bias (see FINDING below)"
                 if pr == 7 else ""))
    check("4i his window: mod 7 is the LARGEST bias (max chi2/df of the six"
          " primes) and is above his chi2/df > 2 bar",
          chi2_df(cnts[7])[0] > 2.0
          and chi2_df(cnts[7])[0] == max(chi2_df(cnts[pr])[0]
                                         for pr in primes)
          and tv_dist(cnts[7]) == max(tv_dist(cnts[pr])
                                      for pr in (5, 7, 11, 13)))
    print("  FINDING, recorded flat (a refinement of the solitary-7"
          " verdict, visible only above his sample size): at N = 30,000 in"
          " this window mod 5 ALSO crosses the chi2/df > 2 bar"
          f" ({chi2_df(cnts[5])[0]:.2f}, TV {tv_dist(cnts[5]):.4f}, vs 7's"
          f" {chi2_df(cnts[7])[0]:.2f}, TV {tv_dist(cnts[7]):.4f});"
          " his REQ-MATH-017 values (5: 1.91, 7: 3.43) and our round-8"
          " N = 12,000 replication (5: 0.61, 7: 2.96) sit below that"
          " resolution. So 'solitary' is resolution-dependent at this"
          " window; what is structural and unique to 7 is the MAXIMAL"
          " collapse (the 3-element 2-orbit) and hence the largest,"
          " most robustly detectable bias, with 5 (4-element orbit)"
          " the next-coarsest and next-largest.")

    print("  Scope, stated exactly: what the table supports -- (i) provable:"
          " the 2^s - 1 factor ranges over an orbit of exactly ord_p(2)"
          " values, and p = 7 is the UNIQUE prime with the minimum possible"
          " 3-element orbit (ord 1, 2 are impossible for p >= 5); on the"
          " odd-s stratum the orbit halves iff ord is even, so mod 5 the"
          " zero value drops out while mod 7 the zero atom persists at"
          " density 1/3; (ii) measured: every small-orbit prime is biased"
          " at small block count, magnitude ordered by orbit coarseness"
          " with 7 the extreme, and the bias decays with depth for every"
          " prime; in the moderate-depth tuned-stratum window REQ-MATH-017"
          " tested, mod 7 is the largest bias and the only one his sample"
          " size resolves (the finding above records the finer structure)."
          " The bias is structural, not a lever (his letter's own"
          " conclusion). This explains a CLOSED door only; the open wall --"
          " generic equidistribution of R_0 mod q along the family -- is"
          " untouched and stays parked.")
    print()


def main():
    part0_canaries()
    c_gen, c_strat, astar = part1_constants()
    part23_tables(c_gen, c_strat)
    part4_mod7()
    print(f"TOTAL: {checks} checks, {len(failures)} failures.")
    for f in failures:
        print(f"  FAILED: {f}")


if __name__ == "__main__":
    main()
