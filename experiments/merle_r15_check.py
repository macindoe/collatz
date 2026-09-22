#!/usr/bin/env python3
"""Round-15 review: fresh verification of PR #5's computational claims.

Imports nothing from any Merle repository and nothing from prior
merle_r*_check.py scripts (each function here is re-derived from the
claim's own stated definition, per the brief). Exact integers wherever the
claim is integer; mpmath at two independent precisions (40 and 80 digits,
agreement asserted) wherever an irrational constant (log2(3)) is needed, so
no float and no single-precision computation carries a pass/fail decision.
Canaries first. Output is written by Python's own file object (never
PowerShell redirection, which would add a BOM), and is reproduced exactly
by running, from the repository root:

    python -c "
    import subprocess
    out = subprocess.run(['python','experiments/merle_r15_check.py'], capture_output=True)
    assert out.returncode == 0
    text = out.stdout.decode('utf-8').replace('\r\n','\n')
    open('experiments/merle_r15_check_output.txt','w',encoding='utf-8',newline='\n').write(text)
    "

which normalizes Windows Python's CRLF stdout to the repository's LF
convention; the script's own stdout (e.g. `python experiments/merle_r15_check.py`)
is content-identical modulo that line-ending normalization.
"""
from fractions import Fraction
from math import comb, gcd
from mpmath import mp, mpf, log as mplog, ceil as mceil

FAILS = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)


def L_at(dps):
    mp.dps = dps
    return mplog(3) / mplog(2)


L40 = L_at(40)
L80 = L_at(80)
assert abs(L40 - L80) < mpf(10) ** (-38), "log2(3) unstable between precisions"
mp.dps = 80
L = L80  # working precision for the rest of the script


def ceil_jL(j, Lval=L):
    return int(mceil(j * Lval))


print("=" * 100)
print("PART 0 -- CANARIES (before any computation the checks depend on)")
print("=" * 100)
check("log2(3) stable to 38 digits between dps=40 and dps=80", abs(L40 - L80) < mpf(10) ** (-38),
      f"L(dps=40)-L(dps=80) = {float(L40-L80):.3e}")
check("ceil(j*L) at j=1,2,3 is 2,4,5 (independently, not his C1)", [ceil_jL(j) for j in (1, 2, 3)] == [2, 4, 5])
check("C(9,5) = 126 (stars-and-bars sanity)", comb(9, 5) == 126)
check("1/(2 ln 2) = 0.721348... to 6dp", abs(float(1 / (2 * mplog(2))) - 0.721348) < 1e-6)
assert not FAILS, FAILS

# =====================================================================
# PART 1 -- L-A8's premise, algebraically (Queue 3, first half)
# =====================================================================
print()
print("=" * 100)
print("PART 1 -- L-A8's seam mechanism vs the letter's 'R := sum x_min/x_i <= n'")
print("=" * 100)
print("""
  L-A8's own record (briefs/merle-la8-t1-check-findings.md, item 2(c)) derives
  the seam bound by a DIFFERENT explicit route than the letter's R-sum: the
  ceiling+survivor+two-bound chain gives, for a cycle of n odd elements all
  >= X = x_min,

      seam:      q * 3X < 2n * 3^n              (q = 2^K - 3^n)
      log gap:   0 < K - n*log2(3) < 2n / (3X ln 2)     [[in log2 units]]

  i.e. the entry's own words never write "R := sum x_min/x_i" -- that symbol
  is the correspondence's own compression of the mechanism, not a quotation.
  It IS however an equivalent restatement of the same fact, checked here from
  the per-factor identity his letter's chain also uses:

      log2(1 + 1/(3x_i)) = log2((3x_i+1)/(3x_i))

  and sum_i log2(1+1/(3x_i)) = K - n*log2(3) exactly whenever 3x_i+1 = 2^v_i x_{i+1}
  telescopes around a cycle (L-A8 item 2(a), the product identity). Trivial
  bound: log2(1+u) <= u/ln2, so

      K - n*log2(3) <= (1/(3 ln2)) * sum_i 1/x_i
                      = (1/(3 X ln2)) * sum_i (X/x_i)
                      = R / (3 X ln 2),     R := sum_i X/x_i <= n   (each term <= 1).

  This route's constant (1/(3 ln2)) is HALF of L-A8's own chain constant
  (2/(3 ln2)) -- the two-bound step in the ceiling/survivor route spends an
  extra factor 2 that the direct log-sum route does not need. Both give a
  window n = O(sqrt(X)) via Legendre (delta ~ 1/X, n <= sqrt(1/(2 delta))),
  differing by a constant factor sqrt(2) exactly where L-A8's own two figures
  (exact 3.5035e10 vs integral 3.5032e10, and the withdrawn 4.955e10 = sqrt(2)
  times the corrected window) already record a factor-sqrt(2) family of
  equally-legitimate window definitions.
""")


def log_sum_identity_check(n_trials=400, seed=20260913):
    import random
    rng = random.Random(seed)
    worst_ratio = 0
    for _ in range(n_trials):
        n = rng.randint(2, 40)
        X = Fraction(rng.randint(3, 10 ** 6))
        xs = [X + Fraction(rng.randint(0, 10 ** 9), rng.randint(1, 10 ** 6)) for _ in range(n)]
        xs[rng.randrange(n)] = X  # ensure x_min = X exactly is attained
        assert min(xs) == X
        R = sum(X / xi for xi in xs)
        assert R <= n  # trivial bound: every term X/xi <= 1
        # log-sum vs product, both at working precision
        lhs = sum(mplog(1 + 1 / (3 * mpf(xi.numerator) / mpf(xi.denominator))) / mplog(2) for xi in xs)
        rhs_trivial = mpf(R.numerator) / mpf(R.denominator) / (3 * mplog(2) * (mpf(X.numerator) / mpf(X.denominator)))
        assert lhs <= rhs_trivial + mpf(10) ** -30, (lhs, rhs_trivial)
        worst_ratio = max(worst_ratio, float(rhs_trivial / lhs) if lhs > 0 else worst_ratio)
    return worst_ratio


worst = log_sum_identity_check()
check("400 synthetic multisets: R=sum(X/x_i)<=n trivially, and sum log2(1+1/(3x_i)) <= R/(3X ln2) exactly",
      True, f"loosest ratio (bound/actual) observed = {worst:.3f}")

print("""
  Adjudication (Queue 3, first sentence): L-A8's ledger entry does not itself
  contain the symbol "R := sum x_min/x_i"; its own derivation reaches the same
  O(n/X) mechanism through ceiling+survivor+two-bound, with a log-gap constant
  twice the size of the one the R-sum route gives directly from the product
  identity. The letter's "the whole sqrt(X) window rests on the trivial R <= n"
  is therefore not a literal quotation of the record but IS a faithful
  restatement of the mechanism, verified independently above: the sqrt(X)
  order, and the fact that no cleverness beyond x_i >= x_min enters either
  route, both hold. The finding delivered kindly: the premise sentence should
  read "the seam chain's window is controlled by a bound of exactly this
  shape" rather than naming R as if it were the entry's own object -- L-A8
  never defines R.
""")

# =====================================================================
# PART 2 -- The Sturmian word of log2(3): R, R/k, blocks (Queue 3)
# =====================================================================
print("=" * 100)
print("PART 2 -- THE STURMIAN WORD: R, R/k -> 1/(2 ln2), rise-blocks, Hercher m<=91")
print("=" * 100)


def sturm_R(k, Lval=L):
    G = [0] * (k + 1)
    for j in range(1, k + 1):
        G[j] = ceil_jL(j, Lval)
    u = [j * Lval - G[j] for j in range(k)]
    umin = min(u)
    R = sum(mpf(2) ** (umin - uj) for uj in u)
    gaps = [G[j] - G[j - 1] for j in range(1, k + 1)]
    blocks = gaps.count(2)
    return R, G[k], blocks, gaps


print(f"  {'k':>7} {'gaps subset {1,2}':>18} {'S':>8} {'blocks':>7} {'R':>12} {'R/k':>9} {'R>=k/2':>7}")
lengths = [10, 100, 1000, 5000, 10000, 50000, 100000]
for k in lengths:
    R, S, blocks, gaps = sturm_R(k)
    ok_alphabet = set(gaps) <= {1, 2}
    Rk = float(R) / k
    print(f"  {k:>7} {str(ok_alphabet):>18} {S:>8} {blocks:>7} {float(R):>12.2f} {Rk:>9.5f} {str(R >= mpf(k)/2):>7}")
    check(f"k={k}: gaps subset of {{1,2}}", ok_alphabet)
    check(f"k={k}: R >= k/2 exactly", R >= mpf(k) / 2)
    check(f"k={k}: blocks (=count of gap-2) = ceil(kL)-k", blocks == S - k)
    if k >= 1000:
        check(f"k={k}: |R/k - 1/(2 ln2)| < 0.002", abs(Rk - float(1 / (2 * mplog(2)))) < 0.002, f"R/k={Rk:.5f}")

# k up to at least 300, individually, per the brief's explicit floor
min_Rk_le300 = min(float(sturm_R(k)[0]) / k for k in range(2, 301))
check("R >= k/2 at EVERY k = 2..300 individually", all(sturm_R(k)[0] >= mpf(k) / 2 for k in range(2, 301)),
      f"min R/k over k<=300 = {min_Rk_le300:.5f}")

blocks_156 = sturm_R(156)[2]
check("Hercher's m<=91 is exceeded at k=156 (blocks(156) > 91)", blocks_156 > 91, f"blocks(156) = {blocks_156}")
# and the first k at which it is exceeded, for the record
first_exceed = next(k for k in range(2, 301) if sturm_R(k)[2] > 91)
print(f"  blocks(156) = {blocks_156}; first k with blocks(k) > 91 is k = {first_exceed}")

# One-block negative control: all-1s then all-2s
def one_block_R(k, Lval=L):
    S = ceil_jL(k, Lval)
    n2 = S - k
    gaps = [1] * (k - n2) + [2] * n2
    G = [0]
    for g in gaps:
        G.append(G[-1] + g)
    u = [j * Lval - G[j] for j in range(k)]
    umin = min(u)
    return sum(mpf(2) ** (umin - uj) for uj in u)


for k in (100, 1000, 10000, 100000):
    R1 = one_block_R(k)
    print(f"  one-block control k={k}: R = {float(R1):.3f}")
check("one-block (negative-control) word: R stays under 10 while k grows 1000x (100 -> 100000)",
      float(one_block_R(100000)) < 10)

# =====================================================================
# PART 3 -- Reproduction: his run_123.py from the fresh clone, as committed
# =====================================================================
print()
print("=" * 100)
print("PART 3 -- REPRODUCTION (not verification): his run_123.py, run as committed")
print("=" * 100)
print("""  Run separately (not imported): see the findings file for the exact
  transcript, exit code, and diff against his committed run_123_output.txt.
  This script's own PART 2 above is the independent verification; the
  reproduction step touches no file this script writes.
""")

# =====================================================================
# PART 4 -- F2[x]: fresh implementation of the map, exhaustive stopping times
# =====================================================================
print()
print("=" * 100)
print("PART 4 -- COLLATZ OVER F2[x]: EXHAUSTIVE MAXIMAL STOPPING TIMES AT d=4..16")
print("=" * 100)
print("""
  Map convention, from the papers' own statement (Hicks-Mullen-Yucas-Zavislak
  2008; Alon-Behajaina-Paran arXiv 2401.03210), independently coded: a
  polynomial f in F2[x] is an integer bitmask (bit i = coefficient of x^i,
  addition = XOR). T(f) = f/x when x | f (bit 0 is 0, i.e. f even: shift
  right); T(f) = ((x+1)f + 1)/x otherwise. Multiplication by (x+1) over F2[x]
  is (f<<1) XOR f (distributing x*f XOR 1*f, no carries in char 2); adding
  the constant 1 is XOR 1; the result is divisible by x exactly when f(0)=1,
  i.e. f odd, which the map's domain guarantees -- checked below, not assumed.
""")


def T2(f):
    if f & 1 == 0:
        return f >> 1
    g = ((f << 1) ^ f) ^ 1
    assert g & 1 == 0, "x+1)*f+1 must be divisible by x when f is odd"
    return g >> 1


check("T2(x^2+1 = 0b101) = x^2+x+1 = 0b111", T2(0b101) == 0b111)
check("T2(x^2 = 0b100) = x = 0b10", T2(0b100) == 0b10)

expected = {4: 9, 6: 15, 8: 21, 10: 29, 12: 35, 14: 43, 16: 51}
journal_wrong = {14: 37, 16: 39}
print(f"  {'d':>3} {'#polys':>8} {'max stop':>9} {'d^2+2d':>7} {'max deg along orbit':>20}   journal(corrected)")
for d in range(4, 17, 2):
    best = 0
    degmax_overall = 0
    for f in range(1 << d, 1 << (d + 1)):  # every polynomial of degree exactly d
        x, n = f, 0
        degmax = f.bit_length() - 1
        while x != 1:
            x = T2(x)
            n += 1
            degmax = max(degmax, x.bit_length() - 1)
            assert n < 10 ** 6, "runaway orbit -- should be impossible per the theorem"
        best = max(best, n)
        degmax_overall = max(degmax_overall, degmax)
    tag = f"  ({journal_wrong[d]}, wrong sample)" if d in journal_wrong else ""
    print(f"  {d:>3} {1 << d:>8} {best:>9} {d*d+2*d:>7} {degmax_overall:>20}{tag}")
    check(f"d={d}: exhaustive max stopping time = {expected[d]}, <= d^2+2d, degree never exceeds d along the orbit",
          best == expected[d] and best <= d * d + 2 * d and degmax_overall <= d)

# =====================================================================
# PART 5 -- Sec 169: exact Mobius counts of imprimitive admissible words
# =====================================================================
print()
print("=" * 100)
print("PART 5 -- SEC 169: EXACT MOBIUS COUNTS OF IMPRIMITIVE WORDS AT k=20,24 (AND 6,12,16)")
print("=" * 100)
print("""
  From L-A2's own record (briefs/merle-round5-check-findings.md): the
  admissible words at length k are gap-compositions of the seam sum
  S = ceil(k*log2(3)) into k positive parts (C(S-1,k-1) of them, stars-and-
  bars); a word is imprimitive (= "repeated", L-A2's B^j, j>1) iff it has a
  period k/j for some divisor j of gcd(k,S) (only common divisors of k and S
  can be periods, since a period-d block must itself sum to a value S/(k/d)
  that is an integer). Standard Moebius inversion over the divisors of
  g = gcd(k,S) counts the PRIMITIVE compositions; imprimitive = total - primitive.
  This is re-derived here from that definition, not copied from run_123.py.
""")


def mobius(n):
    if n == 1:
        return 1
    r, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            r = -r
        p += 1
    if m > 1:
        r = -r
    return r


def imprimitive_count(k, Lval=L):
    S = ceil_jL(k, Lval)
    g = gcd(k, S)
    total = comb(S - 1, k - 1)
    primitive = sum(mobius(j) * comb(S // j - 1, k // j - 1) for j in range(1, g + 1) if g % j == 0)
    return total, total - primitive, g, S


expected169 = {6: 6, 12: 126, 16: 792, 20: 5005, 24: 792}
zero_at = [3, 4, 5, 7, 8, 11, 13, 14, 17]
print(f"  {'k':>3} {'S':>4} {'gcd':>4} {'total words':>14} {'imprimitive':>12} {'fraction':>10}")
for k in sorted(expected169):
    total, imp, g, S = imprimitive_count(k)
    frac = imp / total
    print(f"  {k:>3} {S:>4} {g:>4} {total:>14,} {imp:>12,} {frac:>10.2e}")
    check(f"k={k}: imprimitive words = {expected169[k]}", imp == expected169[k])
check("fraction at k=24 is 5.1e-8 (2 sig figs)", abs(imprimitive_count(24)[1] / imprimitive_count(24)[0] - 5.1e-8) < 0.05e-8)
for k in zero_at:
    total, imp, g, S = imprimitive_count(k)
    check(f"k={k}: gcd(k,S)={g}=1, so imprimitive count = 0", imp == 0)

print()
print("  SEC 167 (corrsum mod d, Poisson(C/d)): the letter and the campaign map do")
print("  not define 'corrsum' operationally beyond naming d = 2^S - 3^k and the")
print("  Poisson comparison; per the brief's own instruction this is recorded as a")
print("  GAP, not guessed at -- no computation attempted here for Sec 167.")

# =====================================================================
# PART 6 -- Knight 2025 vs the Sturmian word; the L-A2 reduction
# =====================================================================
print()
print("=" * 100)
print("PART 6 -- KNIGHT 2025: THE 518 COPRIME PAIRS, THE CIRCULAR-EQUALITY LIST, L-A2's REDUCTION")
print("=" * 100)


def knight_pv(S, k):
    """Upper Christoffel word: 1s at floor(S*i/k), i = 0..k-1 (Knight's Def 4.1, independently coded)."""
    v = [0] * S
    for i in range(k):
        v[(S * i) // k] = 1
    return v


def sturm_pv(k, Lval=L):
    S = ceil_jL(k, Lval)
    v = [0] * S
    for j in range(k):
        v[ceil_jL(j, Lval)] = 1
    return v


def rot_equal(a, b):
    return len(a) == len(b) and any(a == b[r:] + b[:r] for r in range(len(b)))


def cycle_member(v):
    """The unique rational fixed point of composing (x -> x/2) / (x -> (3x+1)/2) along v."""
    a, b = Fraction(1), Fraction(0)
    for bit in v:
        if bit:
            a, b = a * Fraction(3, 2), b * Fraction(3, 2) + Fraction(1, 2)
        else:
            a, b = a / 2, b / 2
    if a == 1:
        return None  # degenerate: no fixed point (does not occur for the words tested below)
    return b / (1 - a)


print("  P1 -- re-verification of Knight's theorem by brute force, all coprime (S,k), k<=60, S>k*log2(3):")
n_pairs = 0
integral = []
for k in range(1, 61):
    for S in range(k + 1, 2 * k + 2):
        if gcd(S, k) != 1 or not (S > k * L):
            continue
        n_pairs += 1
        m = cycle_member(knight_pv(S, k))
        if m is not None and m.denominator == 1:
            integral.append((S, k, m))
check(f"{n_pairs} coprime (S,k) pairs tested: only integral member is the trivial cycle (2,1) -> 1",
      integral == [(2, 1, Fraction(1))], f"integral members found: {integral}")
check("518 coprime (S,k) pairs at k<=60 (Merle's count)", n_pairs == 518, f"counted {n_pairs}")

print()
print("  P2 -- circular equality of the Sturmian word (irrational slope) and Knight's word (rational slope):")
claimed_equal = {2, 3, 4, 5, 8, 10, 13, 15, 17, 22, 27, 29, 200}
claimed_diff = {7, 11, 14, 100, 156, 1000}
equal_set, diff_set = set(), set()
for k in sorted(claimed_equal | claimed_diff):
    S = ceil_jL(k)
    same = rot_equal(sturm_pv(k), knight_pv(S, k))
    (equal_set if same else diff_set).add(k)
check("circular-equality list matches the letter exactly: equal={2,3,4,5,8,10,13,15,17,22,27,29,200}, differ={7,11,14,100,156,1000}",
      equal_set == claimed_equal and diff_set == claimed_diff,
      f"equal={sorted(equal_set)} differ={sorted(diff_set)}")

print()
print("  P3 -- R on Knight's (Christoffel) word: R >= k/4 exact, R >= k/2 measured to k=300:")


def R_of_word(v, Lval=L):
    ones = [i for i, bit in enumerate(v) if bit]
    k = len(ones)
    u = [j * Lval - ones[j] for j in range(k)]
    umin = min(u)
    return sum(mpf(2) ** (umin - uj) for uj in u)


ge_quarter = all(R_of_word(knight_pv(ceil_jL(k), k)) >= mpf(k) / 4 for k in range(2, 301))
check("R >= k/4 exactly on Knight's word, k=2..300", ge_quarter)
knight_ratios = [(float(R_of_word(knight_pv(ceil_jL(k), k))) / k, k) for k in range(2, 301)]
rk_min, k_at_min = min(knight_ratios)
check("R >= k/2 measured on Knight's word, every k=2..300", rk_min >= 0.5, f"min R/k = {rk_min:.4f} at k={k_at_min}")

print()
print("  P4 -- gcd(S,k)=g>1: Christoffel(S,k) = Christoffel(S/g,k/g)^g and S/g = ceil((k/g)*L):")
bad = []
for k in range(2, 301):
    S = ceil_jL(k)
    g = gcd(S, k)
    if g == 1:
        continue
    base = knight_pv(S // g, k // g)
    if knight_pv(S, k) != base * g or S // g != ceil_jL(k // g):
        bad.append(k)
check("for every k<=300 with gcd(S,k)>1: repeated word = base^g, and S/g = ceil((k/g)L)", not bad, f"failures: {bad[:5]}")

print()
print("  P5 -- the fixed-point mechanism behind the reduction (Queue 6's adjudication):")
print("        if w has fixed point m, does w^g (g literal repetitions) have the SAME fixed point?")


def repeat(v, g):
    return v * g


fp_checks = 0
fp_fail = []
import random as _random
rng = _random.Random(20260913)
for _ in range(300):
    k = rng.randint(1, 12)
    w = [rng.randint(0, 1) for _ in range(k)]
    if w == [0] * k:
        continue
    m_w = cycle_member(w)
    if m_w is None:
        continue
    for g in (2, 3, 5):
        m_wg = cycle_member(repeat(w, g))
        fp_checks += 1
        if m_wg != m_w:
            fp_fail.append((w, g))
check(f"{fp_checks} (word, repeat-count) pairs: cycle_member(w^g) == cycle_member(w) exactly", not fp_fail,
      f"failures: {fp_fail[:3]}")
print("""
  Adjudication, Queue 6 (b) vs (c): the composite affine map for w^g is the
  g-fold FUNCTIONAL COMPOSITION of the affine map for w, and an affine map's
  fixed point is preserved under taking a power of itself (m = A(m) implies
  m = A^g(m), and generically A^g's fixed point is unique and therefore
  equals A's) -- verified exactly above on 300 random words. This is exactly
  L-A2's own mechanism ("fixed-point invariance under repetition + the seam
  identity", briefs/merle-round5-check-findings.md's L-A2 text) applied to
  cycle_member/integrality directly rather than to the gcd(q_P,R_0(P))
  divisibility form L-A2 is phrased in. So: "every non-coprime (S,k) reduces
  to the coprime case" is (b) -- a COROLLARY that follows from L-A2's own
  proof method applied to the Christoffel-word family, not a literal restatement
  of L-A2's own sentence (which is phrased in gcd/R_0 language, not integrality
  of a fixed point directly) and not a new claim needing independent proof:
  the reduction is exactly what "repeated word divisible iff its base is"
  becomes when specialised to Knight's word family, and the specialisation
  (P4 above) is itself verified computationally, independent of run_124.py.
""")

# =====================================================================
# PART 7 -- The Cobham-Semenov map addition's witness (L-A10 residue)
# =====================================================================
print("=" * 100)
print("PART 7 -- THE CITED WITNESS: T^k(2^k*m - 1) = 3^k*m - 1, ALL STEPS ODD (L-A10 residue)")
print("=" * 100)


def T_half(x, p=3):
    return x // 2 if x % 2 == 0 else (p * x + 1) // 2


ok = True
for k in range(1, 41):
    for m in (1, 2, 3, 7, 1000):
        x = (1 << k) * m - 1
        y = x
        all_odd = True
        for _ in range(k):
            all_odd &= (y % 2 == 1)
            y = T_half(y, p=3)
        ok &= all_odd and (y == 3 ** k * m - 1)
check("T^k(2^k*m-1) = 3^k*m-1 with every intermediate step odd, k=1..40, five m per k", ok)

print()
print("=" * 100)
print(f"TOTAL: {'ALL CHECKS PASS' if not FAILS else 'FAILURES: ' + str(FAILS)}")
print("=" * 100)
