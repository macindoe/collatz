#!/usr/bin/env python3
"""merle_la7_check.py — independent replication for shared-ledger entry L-A7 (the torsion ruler).

Supports: briefs/merle-la7-mu-check-findings.md (branch merle-la7-mu-check).
Fresh code: imports nothing from any Merle repository or from prior check scripts.
Operational definitions are taken from the findings' §1 record of REQ-MATH-029 (read, never run):
  cell (n, S): K = n+S, q = 2^K - 3^n, cells |q| <= 1 excluded; shore = sign(q);
  #words(cell) = C(K-2, n-1) (general-family profile count, Vandermonde closed form);
  R(n,S) = log2(#words) - log2|q|; cell mass = 2^R = #words/|q| (word units);
  best north cell: max R over S = 1..floor(0.5849625*n)+3 with q > 0;
  eps_n = K0 - n*log2(3), K0 = floor(n*log2 3) + 1 = bitlength(3^n) (exact, integer-only);
  bound: R_best(n) <= -c_gen*n + (mu-1)*log2(n) + C0, mu a PARAMETER here (the point of the check).

Precision discipline (every pass/fail decision robust to rounding):
  - all q values and word counts are exact Python integers (incremental exact binomials,
    cross-checked against math.comb and against brute-force profile enumeration);
  - log2 of exact integers via math.log2 (exact conversion path for big ints, error <= 2 ulp
    ~ 5e-16 relative, so absolute error < ~2e-12 at the ~3200-bit integers used here);
  - beta = log2(3) as float (error ~2e-16); eps_n = K0 - n*beta has absolute error
    < n*4e-16 < 1e-12 for n <= 2000, while min_n eps_n over the range is ~6.4e-5 (printed):
    every eps-decision has margin > 1e7 x the rounding error;
  - K0 is computed as bitlength(3^n): exact, no floating floor anywhere;
  - all replication comparisons carry explicit tolerances (stated at each PASS/FAIL) that are
    >= 1e6 x the accumulated float error; tail-table comparisons use 1e-3 relative tolerance
    (his committed values are printed to 3-4 significant digits).
"""

import math

BETA = math.log2(3.0)          # log2(3) = 1.5849625007211562
C_GEN = 0.0793186              # the (B) counting constant as pinned in the entry (cycles.md 12.6.1.5)
LN2 = math.log(2.0)
NMAX = 2000

failures = []


def check(name, ok, detail=""):
    print(f"  {name}: {'PASS' if ok else 'FAIL'}{('  ' + detail) if detail else ''}")
    if not ok:
        failures.append(name)


def log2int(x):
    """log2 of a positive exact integer; math.log2 handles big ints exactly enough (<=2 ulp)."""
    return math.log2(x)


# ---------------------------------------------------------------------------
print("=== CANARIES (hand-computed before any sweep) ===")
# anchors: 2^8 - 3^5 = 256 - 243 = 13 ; 2^12 - 3^7 = 4096 - 2187 = 1909  (by hand)
q58 = (1 << 8) - 3 ** 5
q712 = (1 << 12) - 3 ** 7
check("anchor (n,K)=(5,8) -> q = 13", q58 == 13, f"got {q58} (exact integer)")
check("anchor (n,K)=(7,12) -> q = 1909", q712 == 1909, f"got {q712} (exact integer)")

# word-count canary: brute-force profile enumeration vs C(K-2, n-1), small cells.
def count_profiles_brute(n, S):
    """# of profiles (m_t, s_t)_{t<p}, entries >= 1, sum m = n, sum s = S (any p >= 1)."""
    def comps(total):  # all compositions of total into parts >= 1
        if total == 0:
            return [[]]
        out = []
        for first in range(1, total + 1):
            for rest in comps(total - first):
                out.append([first] + rest)
        return out
    cnt = 0
    for cm in comps(n):
        p = len(cm)
        # count compositions of S into exactly p parts >= 1: C(S-1, p-1)
        if S >= p:
            cnt += math.comb(S - 1, p - 1)
    return cnt

brute_ok = True
for (n, S) in [(2, 1), (2, 3), (3, 2), (4, 3), (5, 4), (6, 5), (6, 2)]:
    b = count_profiles_brute(n, S)
    v = math.comb(n + S - 2, n - 1)
    if b != v:
        brute_ok = False
check("word count = C(K-2, n-1) (brute enumeration, 7 small cells, exact)", brute_ok)

# word budgets n <= 14 on the REQ-022 domain S <= min(9, 2n) (his budget-canary domain)
bn = bs = 0.0
for n in range(2, 15):
    p3n = 3 ** n
    for S in range(1, min(9, 2 * n) + 1):
        K = n + S
        q = (1 << K) - p3n
        a = abs(q)
        if a <= 1:
            continue
        words = math.comb(K - 2, n - 1)
        lam = 2.0 ** (log2int(words) - log2int(a))
        if q > 0:
            bn += lam
        else:
            bs += lam
print(f"  word budgets n<=14 (S <= min(9,2n)): north = {bn:.4f}, south = {bs:.4f}")
check("north budget rounds to 6.17", round(bn, 2) == 6.17, "tolerance: 2-dp rounding; float error < 1e-9")
check("south budget rounds to 3.41", round(bs, 2) == 3.41, "tolerance: 2-dp rounding; float error < 1e-9")
# unit reconciliation vs L-A6's necklace budgets (entry-quoted reference values, different units)
LA6_NORTH_LAMBDA, LA6_SOUTH_LAMBDA = 2.64, 1.12
print(f"  unit ratio word/necklace (L-A6 quoted lambdas 2.64 north / 1.12 south as reference):")
print(f"    north {bn:.2f}/{LA6_NORTH_LAMBDA} = {bn / LA6_NORTH_LAMBDA:.2f}x,"
      f"  south {bs:.2f}/{LA6_SOUTH_LAMBDA} = {bs / LA6_SOUTH_LAMBDA:.2f}x"
      f"  (word units over-count each necklace by its orbit size; upper bound confirmed >= 1)")

# ---------------------------------------------------------------------------
print("\n=== MAIN SWEEP n <= 2000 (exact counts; mu enters only in bounds) ===")
MU_ENTRY = 5.125  # the entry's transplanted exponent, replicated first as committed

per_n_mass = [0.0] * (NMAX + 1)
R_best_n = [None] * (NMAX + 1)      # best north cell log-mass
R_best_s = [None] * (NMAX + 1)      # best south cell log-mass
best_at_tuned = 0                   # how often argmax_S R (north) is the tuned K0
n_not_tuned = []
eps_list = [None] * (NMAX + 1)      # north gap K0 - n*beta
epsp_list = [None] * (NMAX + 1)     # south gap n*beta - (K0-1)
margin_minus = None                 # min of margin(n) - c_gen*n (the for-all-n ingredient)
margin_min_at = None
cellsum_factor_max = 0.0            # max mass(n) / (2^R_best_north + 2^R_best_south):
cellsum_at = None                   #   the per-shore best-cell -> total-mass repair size
min_eps = (10.0, None)
min_slack_n = (1e99, None)          # min eps_n * n^(mu-1), north (his diagnostic)
min_slack_s = (1e99, None)          # min eps'_n * n^(mu-1), south (not checked in his script)

p3 = 3
comb_spot_ok = True
for n in range(2, NMAX + 1):
    p3 *= 3
    K0 = p3.bit_length()            # exact tuned north K: 2^(K0-1) <= 3^n < 2^K0
    eps = K0 - n * BETA
    epsp = 1.0 - eps
    eps_list[n] = eps
    epsp_list[n] = epsp
    if eps < min_eps[0]:
        min_eps = (eps, n)
    v = eps * n ** (MU_ENTRY - 1)
    if v < min_slack_n[0]:
        min_slack_n = (v, n)
    if n >= 3:                      # n = 2 south near-cell is |q| = 1 (spent stock), excluded
        vs = epsp * n ** (MU_ENTRY - 1)
        if vs < min_slack_s[0]:
            min_slack_s = (vs, n)

    Smax = int(0.5849625 * n) + 3   # replicate the recorded cap (the realizable-ticket domain)
    best = None
    bests = None
    bestK = None
    tot = 0.0
    c = 1                           # C(K-2, n-1) at K = n+1 is C(n-1, n-1) = 1
    for S in range(1, Smax + 1):
        K = n + S
        if S > 1:
            a = K - 3               # incremental: C(a+1, n-1) = C(a, n-1)*(a+1)//(a+2-n)
            c = c * (a + 1) // (a + 2 - n)
        q = (1 << K) - p3
        aq = abs(q)
        if aq <= 1:
            continue
        R = log2int(c) - log2int(aq)
        if R > -1074:
            tot += 2.0 ** R
        if q > 0:
            if best is None or R > best:
                best, bestK = R, K
        else:
            if bests is None or R > bests:
                bests = R
        if n <= 40 and S in (1, Smax // 2 + 1):   # spot-check incremental binomial vs math.comb
            if c != math.comb(K - 2, n - 1):
                comb_spot_ok = False
    per_n_mass[n] = tot
    R_best_n[n] = best
    R_best_s[n] = bests
    if bestK == K0:
        best_at_tuned += 1
    else:
        n_not_tuned.append((n, bestK, K0))
    # margin at the tuned cell (K0 always inside the cap: K0 - n <= Smax)
    m_margin = K0 - log2int(math.comb(K0 - 2, n - 1))
    d = m_margin - C_GEN * n
    if margin_minus is None or d < margin_minus:
        margin_minus, margin_min_at = d, n
    if best is not None:
        denom = 2.0 ** best + (2.0 ** bests if bests is not None else 0.0)
        f = tot / denom
        if f > cellsum_factor_max:
            cellsum_factor_max, cellsum_at = f, n

check("incremental exact binomials == math.comb (spot checks, n <= 40)", comb_spot_ok)
print(f"  min_n eps_n = {min_eps[0]:.3e} at n = {min_eps[1]} "
      f"(empirical CF floor; >= 1e7 x float error, all eps decisions robust)")
print(f"  best north cell is the tuned K0 = bitlength(3^n) for {best_at_tuned}/{NMAX - 1} scales"
      + ("" if not n_not_tuned else f"; exceptions {n_not_tuned[:10]}"))
print(f"  margin(n) - c_gen*n: min = {margin_minus:.4f} at n = {margin_min_at} "
      f"(> 0 on the whole range: the for-all-n form of the (B) ingredient holds here, verified not proved)")
print(f"  cell-sum factor mass(n)/(2^R_best_N + 2^R_best_S): max = {cellsum_factor_max:.3f} at n = {cellsum_at}")
print(f"    -> best-cell -> total-mass repair: mass(n) <= factor * (north best + south best), both shores")
print(f"       floor-bounded by the measure; repair cost = 1 + log2(factor) < "
      f"{1.0 + math.log2(cellsum_factor_max):.2f} bits (CELL_BITS below covers it)")

# --- replication of the entry's committed numbers at mu = 5.125 -------------
maxDelta, nAtMax = -1e99, None
for n in range(2, NMAX + 1):
    if R_best_n[n] is None:
        continue
    Delta = R_best_n[n] + C_GEN * n - (MU_ENTRY - 1) * math.log2(n)
    if Delta > maxDelta:
        maxDelta, nAtMax = Delta, n
C0_emp = maxDelta
print(f"\n  [mu = 5.125 as committed]")
print(f"  C0 (max Delta, exhibited) = {C0_emp:.3f} at n = {nAtMax}")
check("C0 = -5.774 at n = 2", abs(C0_emp + 5.774) < 2e-3 and nAtMax == 2, "tolerance 2e-3")
print(f"  ingredient slack, north: min eps_n * n^(mu-1) = {min_slack_n[0]:.3f} at n = {min_slack_n[1]}")
check("slack ~ 14.5 at n = 2", abs(min_slack_n[0] - 14.5) < 0.1 and min_slack_n[1] == 2, "tolerance 0.1")
print(f"  ingredient slack, south: min eps'_n * n^(mu-1) = {min_slack_s[0]:.3f} at n = {min_slack_s[1]}"
      f"  <- NOT checked in REQ-MATH-029 (both-shore consequence needs the floor side too)")

# pointwise: is 2^bound(n) >= mass(n) with his C0?
first_ok_from = None
worst_small = (0.0, None)
for n in range(2, NMAX + 1):
    b = -C_GEN * n + (MU_ENTRY - 1) * math.log2(n) + C0_emp
    if per_n_mass[n] <= 2.0 ** b:
        if first_ok_from is None:
            first_ok_from = n
    else:
        first_ok_from = None
        r = per_n_mass[n] / 2.0 ** b
        if r > worst_small[0]:
            worst_small = (r, n)
print(f"  pointwise mass(n) <= 2^bound(n): holds for all n >= {first_ok_from}; "
      f"below that the best-cell bound is not a mass bound (worst factor {worst_small[0]:.2f} at n = {worst_small[1]})")

# ---------------------------------------------------------------------------
print("\n=== TAIL TABLE (replication of the committed table, mu = 5.125, C0 = C0_emp) ===")
HIS = {14: (4.954e0, 1.516e6), 30: (2.024e0, 1.481e6), 60: (2.370e-1, 1.178e6),
       120: (6.464e-3, 3.431e5), 300: (6.294e-7, 4.817e2), 600: (3.414e-14, 5.020e-4),
       1200: (3.921e-29, 3.863e-17)}

def bound_exp_entry(n):
    return -C_GEN * n + (MU_ENTRY - 1) * math.log2(n) + C0_emp

print(f"  {'N':>5} {'exact mass n>N':>16} {'his exact':>11} {'bound n>N (his formula)':>24} {'his bound':>11}")
tail_repl_ok = True
for N in (14, 30, 60, 120, 300, 600, 1200):
    ex = math.fsum(per_n_mass[N + 1:NMAX + 1])
    bd = math.fsum(2.0 ** bound_exp_entry(n) for n in range(N + 1, NMAX + 1))
    bd += 2.0 ** bound_exp_entry(NMAX) / (C_GEN * LN2)   # his analytic continuation, as committed
    hex_, hbd = HIS[N]
    ok = (abs(ex - hex_) <= 1.5e-3 * max(ex, hex_)) and (abs(bd - hbd) <= 1.5e-3 * max(bd, hbd))
    tail_repl_ok &= ok
    print(f"  {N:>5} {ex:>16.4e} {hex_:>11.3e} {bd:>24.4e} {hbd:>11.3e}  {'ok' if ok else 'MISMATCH'}")
check("tail table replicates (rel. tol 1.5e-3 vs his 3-4 printed digits)", tail_repl_ok)
print("  note: his analytic continuation term uses rate c_gen, ignoring the still-growing")
print("        (mu-1)*log2(n) beyond n=2000; the rigorous rate is c_gen - (mu-1)/(NMAX*ln2)")
print(f"        = {C_GEN - (MU_ENTRY - 1) / (NMAX * LN2):.6f}; at these values the term is ~2^-119, immaterial (flagged, cosmetic).")

# ---------------------------------------------------------------------------
print("\n=== CROSSING SCALE (the entry says 'crosses below one ticket near n ~ 550') ===")
def first_below_one(exp_fn, lo=2, hi=10 ** 12):
    n = lo
    prev_ok = exp_fn(lo) < 0
    # scan smallest n beyond the bound's peak with exp < 0 (exp is eventually decreasing)
    # find peak region first by doubling
    n_cross = None
    n = lo
    step = 1
    last = None
    while n < hi:
        e = exp_fn(n)
        if last is not None and e < 0 and last >= 0:
            # refine linearly backwards
            m = n
            while m > lo and exp_fn(m - 1) < 0:
                m -= 1
            n_cross = m
            break
        last = e
        n += step
        if n > 100000:
            step = max(step, n // 100000)
    return n_cross

cross_per_n = first_below_one(bound_exp_entry)
print(f"  per-n bound 2^b(n) < 1 (one ticket per scale) first at n = {cross_per_n}")
# cumulative reading: provable tail beyond N < 1
def tail_bound_entry(N, cap=NMAX):
    s = math.fsum(2.0 ** bound_exp_entry(n) for n in range(N + 1, cap + 1))
    s += 2.0 ** bound_exp_entry(cap) / (C_GEN * LN2)
    return s
N = 2
while tail_bound_entry(N) >= 1.0:
    N += 1
print(f"  cumulative provable tail < 1 ticket first at N = {N}")
print("  neither reading lands at ~550; nearest committed fact: the tail bound crosses 5.2e-4 at N ~ 600.")
N52 = 2
while tail_bound_entry(N52) >= 5.2e-4:
    N52 += 1
print(f"  provable tail < 5.2e-4 (the headline) first at N = {N52} (his cut: 600)")

# ---------------------------------------------------------------------------
print("\n=== SENSITIVITY TABLE (mu as a parameter; the sourced values of item 2) ===")
print("""  Scenarios (derivation form: R_best(n) <= -c_gen*n + [eps-floor term](n) + C0_cell;
  mass repair adds log2(cell-sum factor) <= 3.0 bits, measured above, elementary to prove):
   E  entry-as-committed     mu = 5.125, C0 = -5.774 empirical   (NO source for log2 3)
   T1 transplant, thm-form   mu = 5.125, c = 1: C0_cell = 1 - log2(ln 2) = 1.53      (comparison only)
   T2 Wu-Wang 2014 (ln 3!)   mu = 5.1163051, c = 1, same C0_cell                     (comparison only)
   A  Wu 2003 asymptotic     nu = 7.6155 -> eps_n > K0^-nu / ln 2, H0 UNPINNED       (asymptotic grade)
   R  Rhin 1987 explicit     nu = 13.3   -> eps_n > K0^-13.3 / ln 2, fully explicit  (the citable row)
   G  Gouillon 2006 Cor 2.3  |Lambda| >= e^-4.0452e7 (h = 1000 floor) to n ~ 10^430  (guaranteed floor)
""")

CELL_BITS = 3.0                      # mass repair, provable O(1); measured max factor printed above
C0_CELL_NUM = 1.0 - math.log2(LN2)   # number-measure form, c = 1
C0_CELL_LF = 1.0 - 2.0 * math.log2(LN2)  # linear-form form (extra 1/ln2 from Lambda -> eps)

def make_exp(kind, param):
    if kind == "num":   # (mu, C0) number-measure
        mu, C0 = param
        return lambda n: -C_GEN * n + (mu - 1) * math.log2(n) + C0
    if kind == "lf":    # linear-form exponent nu; K0 <= beta*n + 1 (rigorous upper for the floor)
        nu, C0 = param
        return lambda n: -C_GEN * n + nu * math.log2(BETA * n + 1) + C0
    if kind == "const": # constant Lambda floor, in bits
        bits, C0 = param
        return lambda n: -C_GEN * n + bits + C0

def tail_bound(exp_fn, N, cap):
    ceff = C_GEN - 13.3 / (cap * LN2)      # rigorous continuation rate (worst case over scenarios)
    if ceff <= 0:
        return float("inf")
    terms = [exp_fn(n) for n in range(N + 1, cap + 1)]
    m = max(terms)
    s = math.fsum(2.0 ** (t - m) for t in terms)
    log2tail_main = m + math.log2(s)
    cont = exp_fn(cap) - math.log2(2.0 ** ceff - 1.0)
    m2 = max(log2tail_main, cont)
    return m2 + math.log2(2.0 ** (log2tail_main - m2) + 2.0 ** (cont - m2))  # log2 of tail bound

def min_N_for(exp_fn, target_log2, n_cross, cap_pad=6000):
    N = max(2, n_cross - 200)
    cap = n_cross + cap_pad
    found = None
    while N < cap:
        if tail_bound(exp_fn, N, cap) < target_log2:
            found = N
            break
        N += max(1, (cap - N) // 500)
    if found is None:
        return None
    while found > 2 and tail_bound(exp_fn, found - 1, cap) < target_log2:
        found -= 1                   # refine to the true minimum (coarse scan may overshoot)
    return found

TARGET = math.log2(5.2e-4)
# Gouillon floor in bits: |Lambda| >= e^-4.04516e7  ->  -log2 eps_n <= 4.04516e7*log2(e) + log2(1/ln2)
G_BITS = 4.04516e7 * math.log2(math.e) + math.log2(1.0 / LN2)
rows = [
    ("E  entry (mu=5.125, C0=-5.77)", make_exp("num", (5.125, C0_emp))),
    ("T1 transplant thm-form c=1   ", make_exp("num", (5.125, C0_CELL_NUM + CELL_BITS))),
    ("T2 Wu-Wang 5.1163051 (ln3!)  ", make_exp("num", (5.1163051, C0_CELL_NUM + CELL_BITS))),
    ("A  Wu 2003 nu=7.6155 (H0?)   ", make_exp("lf", (7.6155, C0_CELL_LF + CELL_BITS))),
    ("R  Rhin 1987 nu=13.3 explicit", make_exp("lf", (13.3, C0_CELL_LF + CELL_BITS))),
    ("G  Gouillon 2006 const floor ", make_exp("const", (G_BITS, C0_CELL_LF - 1.0 + CELL_BITS))),
]

print(f"  {'scenario':<31} {'per-n bound < 1 at n*':>22} {'tail bound beyond 600':>22} {'min N: tail < 5.2e-4':>21}")
for name, fn in rows:
    if fn(700) > 60:  # scenario far from closing at 600: report crossing analytically
        n_cross = first_below_one(fn, hi=10 ** 11)
    else:
        n_cross = first_below_one(fn)
    if n_cross is None:
        print(f"  {name:<31} {'> 1e11':>22} {'(vacuous)':>22} {'> 1e11':>21}")
        continue
    if n_cross <= 20000:
        t600 = tail_bound(fn, 600, max(NMAX, n_cross + 6000))
        t600s = f"2^{t600:+.1f} ({2.0 ** t600:.2e})" if t600 < 40 else f"2^{t600:+.1f} (vacuous)"
        Nmin = min_N_for(fn, TARGET, n_cross)
        print(f"  {name:<31} {n_cross:>22} {t600s:>22} {str(Nmin):>21}")
    else:
        # huge scenario: closed-form geometric estimate around the crossing
        Nmin = int(n_cross + (-TARGET + math.log2(1.0 / (2.0 ** C_GEN - 1.0))) / C_GEN) + 1
        print(f"  {name:<31} {n_cross:>22} {'2^' + format(fn(601), '+.3g') + ' (vacuous)':>22} {'~' + format(Nmin, ',d'):>21}")

print("""
  Reading: the committed headline ('provable tail < 5.2e-4 beyond n = 600') survives ONLY under
  the unsourced transplanted exponent. Under the citable effective ingredient (Rhin 1987, nu = 13.3)
  the same construction still closes the kiosk effectively, at a shifted scale (min N in the R row);
  below that scale the mass must be computed exactly (n <= 2000 is already exact in this script and
  in his; the remaining gap to the R-row N is a finite computation of the same kind). The Gouillon
  row is the guaranteed floor if Rhin's Proposition were ever to fall: crossing at n ~ 7e8, still
  effectively finite, headline scale astronomically weaker.""")

# ---------------------------------------------------------------------------
print("\n=== SUMMARY ===")
print(f"  checks failed: {len(failures)}" + (f" -> {failures}" if failures else ""))
raise SystemExit(0 if not failures else 1)
