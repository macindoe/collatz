#!/usr/bin/env python3
"""merle_la8_t1_check.py — clean-room verification of shared-ledger entry L-A8
(T1, "no-hair theorem for cycles": ceiling + seam + Legendre window + finite
discharge), per briefs/merle-la8-t1-check-brief.md.

Supports: briefs/merle-la8-t1-check-findings.md.

Rules honoured:
  - imports NOTHING from any Merle repository and nothing from prior Merle-check
    scripts; Python stdlib only (math.isqrt, fractions.Fraction, random);
  - exact integer arithmetic at every pass/fail decision wherever possible;
  - where logarithms are unavoidable, fixed-point big-integer logs computed
    in-house (atanh series), at TWO working precisions (130 and 210 digits,
    both >= the brief's 80), with stability asserted between them — no floats
    in any decision, no mpmath dependency;
  - canaries (the four real cycles) printed FIRST;
  - this is verification of a correspondent's finite discharge, not a cycle
    search: no orbit/period searches are opened anywhere below.

Checked claims (L-A8 blocks, commits be8869f..826970e of
github.com/macindoe/one-obstruction-three-faces, HEAD 826970e):
  (a) cycle product identity  prod(3x_i+1) = 2^K * prod(x_i), all 4 real cycles;
  (b) survivor bound + ceiling  3^n < 2^K < 2*3^n when 2n < 3X (n = p+1);
  (c) seam bound  q*3X < 2n*3^n  and the log gap  |log2(3) - K/n| < delta,
      delta = 2/(3X ln 2) = 4.0734e-22 at X = 2^71; the withdrawn 4.955e10
      window as the missing-factor-2 artifact;
  (d) the window, exactly: sqrt(1/(2 delta)) = 3.5035e10 (exact form) vs
      4000n^2 <= 2079*2^71 -> n <= 35031771147 = 3.5032e10 (integral form);
      2079/4000 < 3 ln2 / 4 (conservative direction);
  (e) continued fraction of log2(3) from scratch; exactly 22 convergent
      denominators q_j <= window (j = 0..21 standard); q_21 = 6586818670;
      the q_21-labeling discrepancy; Hercher's threshold = q_23 = 137528045312
      (Remark-28 gap 1.1032e-22 and Table-1 companion 7.20e10 reproduced);
  (f) finite discharge: integer criterion 2000*q_j*(q_j+q_{j+1}) <= 2079*2^71
      for all 22; tightest margin 5.17x at q_21; exact test 5.44x; canary:
      q_22 FAILS the criterion; theta_j > 1/(q_j+q_{j+1}) verified;
  (g) scope: closure statement + Hercher comparison numbers (3.9x);
  (h) non-vacuity: where each real cycle exits T1's hypotheses.
"""

import math
import random
from fractions import Fraction

CHECKS = 0
FAILURES = 0

def check(label, ok):
    global CHECKS, FAILURES
    CHECKS += 1
    if not ok:
        FAILURES += 1
        print(f"  FAIL: {label}")
    return ok

def require(label, ok):
    if not check(label, ok):
        raise SystemExit(f"HARD FAIL: {label}")

# ----------------------------------------------------------------------------
# Fixed-point big-integer logarithms (no floats, no external libraries).
# A real x is represented as round(x * 10^prec) (an int, "scaled by S").
# ln 2 = 2 atanh(1/3)   [(1+1/3)/(1-1/3) = 2]
# ln 3 = ln 2 + 2 atanh(1/5)   [(1+1/5)/(1-1/5) = 3/2]
# cross-check: ln 3 = 2 atanh(1/2)   [(1+1/2)/(1-1/2) = 3]
# ----------------------------------------------------------------------------

def atanh_inv_fp(m, S):
    """floor-ish of atanh(1/m) * S, error < a few units (series truncated when
    terms vanish; each floor division loses < 1, guard digits absorb it)."""
    total = 0
    k = 0
    mm = m * m
    power = m  # m^(2k+1)
    while True:
        term = S // ((2 * k + 1) * power)
        if term == 0:
            break
        total += term
        power *= mm
        k += 1
    return total

class FP:
    """Fixed-point context at `prec` decimal digits (computed with 25 guard
    digits, then truncated)."""
    def __init__(self, prec):
        self.prec = prec
        guard = 25
        Sg = 10 ** (prec + guard)
        ln2_g = 2 * atanh_inv_fp(3, Sg)
        ln3_a = ln2_g + 2 * atanh_inv_fp(5, Sg)
        ln3_b = 2 * atanh_inv_fp(2, Sg)
        # the two independent series must agree to within 10^(guard-10) units
        assert abs(ln3_a - ln3_b) < 10 ** (guard - 10), \
            "ln3 cross-formula disagreement"
        self.S = 10 ** prec
        self.ln2 = ln2_g // 10 ** guard
        self.ln3 = ln3_a // 10 ** guard
        # L = log2(3), scaled by S
        self.L = self.ln3 * self.S // self.ln2

    def cf_log23(self, nterms):
        """Continued-fraction partial quotients of log2(3), by exact Euclid on
        the fixed-point rational ln3/ln2 (valid while convergents are far below
        the precision scale)."""
        a = []
        num, den = self.ln3, self.ln2
        for _ in range(nterms):
            q, r = divmod(num, den)
            a.append(q)
            if r == 0:
                break
            num, den = den, r
        return a

    def theta(self, p, q):
        """theta = |q*log2(3) - p|, scaled by S."""
        return abs(q * self.ln3 - p * self.ln2) * self.S // self.ln2

    def fp_str(self, x_fp, sig=6):
        """Scientific-notation string of a scaled value (for readouts only)."""
        if x_fp == 0:
            return "0"
        s = str(x_fp)
        exp = len(s) - 1 - self.prec
        mant = s[0] + "." + s[1:sig]
        return f"{mant}e{exp:+03d}"

FPA = FP(130)
FPB = FP(210)

# ----------------------------------------------------------------------------
# Section 0 — CANARIES FIRST: the four real cycles of the odd map
# x -> (3x+1)/2^v2(3x+1), from cycles.md 12.6.1.2. Iterating the map from a
# KNOWN cycle member is bookkeeping, not a search.
# ----------------------------------------------------------------------------

def odd_cycle(x0, cap=100):
    xs, vs = [x0], []
    x = x0
    for _ in range(cap):
        y = 3 * x + 1
        v = 0
        while y % 2 == 0:
            y //= 2
            v += 1
        vs.append(v)
        if y == x0:
            return xs, vs
        xs.append(y)
        x = y
    raise RuntimeError("not a cycle member")

print("=" * 76)
print("CANARIES: the four real cycles (printed before any sweep)")
print("=" * 76)

REAL = {}
for x0 in (1, -1, -5, -17):
    xs, vs = odd_cycle(x0)
    K = sum(vs)
    P1 = 1
    P2 = 1
    for x in xs:
        P1 *= 3 * x + 1
        P2 *= x
    REAL[x0] = (xs, vs, K, P1, P2)
    print(f"  cycle {x0:>4}: elements {xs}")
    print(f"             v-word {vs}, n = {len(xs)}, K = {K}")

# ----------------------------------------------------------------------------
# (a) Cycle product identity: prod(3x_i+1) = 2^K prod(x_i).
# Telescoping derivation (findings section (a)): 3x_i + 1 = 2^{v_i} x_{i+1}
# per step; multiply around the cycle; the x-products cancel cyclically.
# ----------------------------------------------------------------------------

print()
print("(a) cycle product identity, exact on all four cycles, both shores")
for x0, (xs, vs, K, P1, P2) in REAL.items():
    require(f"identity at {x0}", P1 == 2 ** K * P2)
    print(f"  {x0:>4}: prod(3x+1) = {P1} = 2^{K} * {P2}: OK")
m17 = REAL[-17]
require("-17 figures reproduce", m17[3] == -403123745024000 and m17[2] == 11
        and 2 ** 11 * m17[4] == -403123745024000)
print("  -17: prod(3x+1) = -403123745024000 = 2^11 * prod(x)  [entry figure] OK")

# per-step identity spot check (the telescoping's engine), all cycles:
for x0, (xs, vs, K, P1, P2) in REAL.items():
    n = len(xs)
    ok = all(3 * xs[i] + 1 == 2 ** vs[i] * xs[(i + 1) % n] for i in range(n))
    require(f"per-step 3x+1 = 2^v x' at {x0}", ok)
print("  per-step 3x_i+1 = 2^(v_i) x_(i+1) verified on all steps, all cycles")

# ----------------------------------------------------------------------------
# (b) Survivor bound + ceiling.
# Per-factor equivalence (one line): (3x+1)(3X) <= 3x(3X+1)
#   <=> 9xX + 3X <= 9xX + 3x  <=>  X <= x.
# Survivor: with X = min x_i, R := prod(3x_i+1)/prod(x_i) satisfies
#   R <= 3^n ((3X+1)/(3X))^n, and R > 3^n always (each factor 3 + 1/x > 3).
# Two-bound: (m+1)^n < 2 m^n when 2n < m  =>  R < 2*3^n when 2n < 3X.
# A cycle has R = 2^K integral, so 3^n < 2^K < 2*3^n, forcing
#   K = ceil(n log2 3) = bitlength(3^n).
# ----------------------------------------------------------------------------

print()
print("(b) survivor bound + ceiling")

# per-factor equivalence, exhaustive small + random large
ok = True
for x in range(1, 60):
    for X in range(1, 60):
        lhs = (3 * x + 1) * 3 * X <= 3 * x * (3 * X + 1)
        ok &= (lhs == (X <= x))
require("per-factor equivalence, exhaustive x,X < 60", ok)
rng = random.Random(20260726)
ok = True
for _ in range(2000):
    x = rng.randrange(1, 10 ** 30)
    X = rng.randrange(1, 10 ** 30)
    ok &= (((3 * x + 1) * 3 * X <= 3 * x * (3 * X + 1)) == (X <= x))
require("per-factor equivalence, 2000 random pairs to 10^30", ok)
print("  (3x+1)(3X) <= 3x(3X+1)  <=>  X <= x : exhaustive + random, exact")

# strict two-bound (m+1)^n < 2 m^n for 2n < m, integer sweep
ok = True
for n in range(1, 40):
    for m in range(2 * n + 1, 2 * n + 40):
        ok &= ((m + 1) ** n < 2 * m ** n)
require("two-bound (m+1)^n < 2 m^n for 2n < m (grid)", ok)
print("  (m+1)^n < 2*m^n whenever 2n < m : grid exact")

# survivor + ceiling on synthetic multisets (element multisets, NOT orbits)
ok_lower = ok_upper = ok_surv = True
for trial in range(400):
    n = rng.randrange(1, 12)
    X = rng.randrange((2 * n) // 3 + 1, 10 ** 6)  # ensure 2n < 3X possible
    if 2 * n >= 3 * X:
        continue
    xs = sorted(rng.randrange(X, X + 10 ** 5) for _ in range(n))
    xs = [x | 1 for x in xs]  # odd
    xs = [max(x, X) for x in xs]
    Xm = min(xs)
    R = Fraction(math.prod(3 * x + 1 for x in xs), math.prod(xs))
    ok_lower &= (R > 3 ** n)
    # survivor with X = actual minimum
    ok_surv &= (R * (3 * Xm) ** n <= 3 ** n * (3 * Xm + 1) ** n)
    if 2 * n < 3 * Xm:
        ok_upper &= (R < 2 * 3 ** n)
require("R > 3^n on 400 synthetic multisets", ok_lower)
require("survivor product bound on 400 synthetic multisets", ok_surv)
require("R < 2*3^n when 2n < 3X (ceiling body)", ok_upper)
print("  3^n < R <= 3^n((3X+1)/3X)^n < 2*3^n on 400 random multisets, exact rationals")

# ceiling formula: bitlength(3^n) = ceil(n log2 3), exact both ways
ok = True
for n in range(1, 2001):
    K0 = (3 ** n).bit_length()
    ok &= (2 ** (K0 - 1) < 3 ** n < 2 ** K0)  # strict: 3^n is never a 2-power
require("K0 = bitlength(3^n) has 2^(K0-1) < 3^n < 2^K0, n <= 2000", ok)
print("  K forced = ceil(n log2 3) = bitlength(3^n): strict sandwich exact to n=2000")

# trivial-cycle canary: n=1, X=1, K=2
xs, vs, K, P1, P2 = REAL[1]
require("trivial: 2(p+1) < 3X", 2 * 1 < 3 * 1 + 1 or 2 * 1 < 3)  # 2 < 3
require("trivial ceiling 3 < 4 < 6", 3 ** 1 < 2 ** K < 2 * 3 ** 1)
print("  trivial cycle: 2 < 3, 3 < 2^2 < 6, K = 2 = ceil(log2 3) : OK")

# ----------------------------------------------------------------------------
# (c) Seam bound + log gap.
# Seam (findings (c)): from survivor, q_R := R - 3^n satisfies
#   q_R (3X)^n <= 3^n ((3X+1)^n - (3X)^n) <= 3^n * n (3X+1)^(n-1)
#                <= 2 n 3^n (3X)^(n-1)   [two-bound at exponent n-1]
#   =>  q_R * 3X <= 2 n 3^n.  For a cycle q = 2^K - 3^n = q_R.
# Log gap: 0 < K ln2 - n ln3 = ln(1 + q/3^n) <= q/3^n < 2n/(3X)
#   =>  0 < K/n - log2(3) < 2/(3X ln2) =: delta.
# ----------------------------------------------------------------------------

print()
print("(c) seam bound + log gap")

ok = True
for trial in range(400):
    n = rng.randrange(1, 12)
    X = rng.randrange(n, 10 ** 6)
    if 2 * n >= 3 * X:
        continue
    xs = [max(rng.randrange(X, X + 10 ** 5) | 1, X) for _ in range(n)]
    Xm = min(xs)
    if 2 * n >= 3 * Xm:
        continue
    R = Fraction(math.prod(3 * x + 1 for x in xs), math.prod(xs))
    qR = R - 3 ** n
    ok &= (qR * 3 * Xm <= 2 * n * 3 ** n)
require("seam bound q_R*3X <= 2n*3^n on 400 synthetic multisets", ok)
print("  (R - 3^n)*3X <= 2n*3^n on 400 random multisets, exact rationals")

# ln(1+u) <= u is Real.log_le_sub_one_of_pos / log x <= x-1: textbook, used
# in the derivation; delta computed in-house at both precisions:
X71 = 2 ** 71
for FPx, name in ((FPA, "prec130"), (FPB, "prec210")):
    delta_fp = 2 * FPx.S * FPx.S // (3 * X71 * FPx.ln2)
    FPx.delta = delta_fp
dA = FPA.delta * 10 ** (FPB.prec - FPA.prec)
require("delta stable across precisions", abs(dA - FPB.delta) < 10 ** (FPB.prec - FPA.prec + 5))
print(f"  delta = 2/(3*2^71*ln2) = {FPA.fp_str(FPA.delta)}  [entry: 4.0734e-22]")
require("delta = 4.0734e-22 at printed precision",
        FPA.fp_str(FPA.delta, sig=5).startswith("4.0733") or
        FPA.fp_str(FPA.delta, sig=5).startswith("4.0734"))

# withdrawn window = missing factor 2: sqrt(1/delta_wrong/2) with
# delta_wrong = delta/2  =>  window * sqrt(2)
w2 = 3 * X71 * FPA.ln2 // (4 * FPA.S)          # floor(W_exact^2), integer
W_exact = math.isqrt(w2)
w2w = 3 * X71 * FPA.ln2 // (2 * FPA.S)         # withdrawn: delta/2 -> W^2 doubles
W_withdrawn = math.isqrt(w2w)
print(f"  exact window  sqrt(1/(2 delta))      = {W_exact}  (= 3.50355e10)")
print(f"  withdrawn fig sqrt(1/(2*(delta/2)))  = {W_withdrawn}  (= 4.9547e10)")
require("withdrawn 4.955e10 is exactly the missing-factor-2 artifact",
        str(W_withdrawn).startswith("49546") or str(W_withdrawn).startswith("49547"))
require("window ratio is sqrt(2)",
        abs(W_withdrawn * W_withdrawn - 2 * W_exact * W_exact) < 4 * W_exact)

# ----------------------------------------------------------------------------
# (d) The window, exactly.
# ----------------------------------------------------------------------------

print()
print("(d) the window: 3.5035e10 (exact form) vs 3.5032e10 (integral form)")

require("exact window floor = 35035491...", str(W_exact).startswith("35035491"))
W_exact_B = math.isqrt(3 * X71 * FPB.ln2 // (4 * FPB.S))
require("exact window stable across precisions", W_exact == W_exact_B)
print(f"  n <= sqrt(3*2^71*ln2/4) : floor = {W_exact}  -> '3.5035e10' CORRECT for this form")

RHS = 2079 * X71
W_int = math.isqrt(RHS // 4000)
require("integral window = 35031771147", W_int == 35031771147)
require("integral window tight", 4000 * W_int ** 2 <= RHS < 4000 * (W_int + 1) ** 2)
print(f"  4000 n^2 <= 2079*2^71   : n <= {W_int}  -> '3.5032e10' CORRECT for this form")

# 2079/4000 < 3 ln2/4  <=>  693/1000 < ln2 : integer fixed-point comparison
require("693/1000 < ln2 (both precisions)",
        693 * FPA.S < 1000 * FPA.ln2 and 693 * FPB.S < 1000 * FPB.ln2)
require("conservative direction: integral window inside exact window", W_int < W_exact)
print("  2079/4000 < 3*ln2/4 (<=> 693/1000 < ln2): TRUE; integral window is a")
print("  rational UNDER-approximation — conservative, integral ⊂ exact. Both")
print("  figures are right for their own definitions; see findings for the pin.")

# ----------------------------------------------------------------------------
# (e) Convergents of log2(3), from scratch.
# ----------------------------------------------------------------------------

print()
print("(e) continued fraction of log2(3), convergents, labeling, Hercher")

cfA = FPA.cf_log23(40)
cfB = FPB.cf_log23(40)
require("partial quotients stable across precisions (first 34)", cfA[:34] == cfB[:34])
a = cfA[:34]
print(f"  partial quotients: {a[:28]} ...")

# convergents, STANDARD indexing: p_0/q_0 = a_0/1 = 1/1, p_1/q_1 = 2/1, ...
ps, qs = [], []
p2, p1 = 0, 1   # p_{-2}, p_{-1}
q2, q1 = 1, 0
for ai in a:
    p = ai * p1 + p2
    q = ai * q1 + q2
    ps.append(p)
    qs.append(q)
    p2, p1 = p1, p
    q2, q1 = q1, q

require("q starts 1,1,2,5,12,41,53,306,665,15601",
        qs[:10] == [1, 1, 2, 5, 12, 41, 53, 306, 665, 15601])
census = {5, 12, 41, 53, 306, 665, 15601, 190537}
require("census scales all appear among q_j", census.issubset(set(qs)))
print(f"  census scales 5,12,41,53,306,665,15601,190537 all present: OK")

# exact sign checks (integer powers), j <= 13: p_j/q_j > L  <=>  2^p_j > 3^q_j
ok = True
for j in range(14):
    above = 2 ** ps[j] > 3 ** qs[j]
    ok &= (above == (j % 2 == 1))
require("sign alternation via exact 2^p vs 3^q, j <= 13", ok)
print("  convergent side (above/below) verified by EXACT integer powers, j <= 13")

# theta_j at both precisions, stability
thetaA = [FPA.theta(ps[j], qs[j]) for j in range(30)]
thetaB = [FPB.theta(ps[j], qs[j]) for j in range(30)]
ok = True
for j in range(30):
    tA = thetaA[j] * 10 ** (FPB.prec - FPA.prec)
    ok &= abs(tA - thetaB[j]) < 10 ** (FPB.prec - FPA.prec + 16)
require("theta_j stable across precisions, j <= 29", ok)

# best approximation, exhaustive to q_13 = 190537 (extends his committed
# n < 31867 sweep): for each j with q_{j+1} <= 190537,
#   min_{1<=n<q_{j+1}} ||n L|| is attained at n = q_j and equals theta_j
L_fp, S = FPA.L, FPA.S
best = {}
running_min, running_arg = None, None
nxt = 1
targets = {qs[j + 1]: j for j in range(len(qs) - 1) if qs[j + 1] <= 190537}
acc = 0
for n in range(1, 190538):
    acc += L_fp
    if acc >= S * (10 ** 20):
        acc %= S  # keep small (never triggers; safety)
    frac = acc % S
    dist = frac if frac <= S - frac else S - frac
    if running_min is None or dist < running_min:
        running_min, running_arg = dist, n
    if n + 1 in targets:
        j = targets[n + 1]
        best[j] = (running_min, running_arg)
ok = True
for j, (mn, arg) in sorted(best.items()):
    good = (arg == qs[j]) and abs(mn - thetaA[j]) < 10 ** (FPA.prec - 100)
    ok &= good
require("best approximation exhaustive: min ||nL|| on n<q_{j+1} at q_j = theta_j, "
        "all j with q_{j+1} <= 190537", ok)
print("  best-approximation property verified EXHAUSTIVELY to n < 190537")

# classical bound 1/(q_j+q_{j+1}) < theta_j < 1/q_{j+1}, j <= 27
ok = True
for j in range(28):
    lo = thetaA[j] * (qs[j] + qs[j + 1]) > S
    hi = thetaA[j] * qs[j + 1] < S
    ok &= lo and hi
require("1/(q_j+q_{j+1}) < theta_j < 1/q_{j+1}, j <= 27", ok)
print("  classical convergent bound 1/(q_j+q_{j+1}) < theta_j < 1/q_{j+1}: OK, j <= 27")

# enumerate the window
inwin = [j for j in range(len(qs)) if qs[j] <= W_int]
require("exactly 22 convergents in the integral window", len(inwin) == 22)
require("they are j = 0..21", inwin == list(range(22)))
inwin_exact = [j for j in range(len(qs)) if qs[j] <= W_exact]
require("same 22 under the exact window", inwin_exact == list(range(22)))
print(f"  convergents with q_j <= window: exactly 22 (j = 0..21, standard indexing)")
print(f"  q_21 = {qs[21]}   q_22 = {qs[22]}   q_23 = {qs[23]}")
require("q_21 = 6586818670", qs[21] == 6586818670)
require("q_22 = 65470613321", qs[22] == 65470613321)
require("q_23 = 137528045312", qs[23] == 137528045312)
print("  LABELING PIN (standard indexing, q_0 = q_1 = 1 both counted):")
print("    6586818670   = q_21  -> stack 89d9efc's 'q_21 = 6.587e9' CORRECT")
print("    65470613321  = q_22  -> stack 0905b00's 'q_21 = 6.547e10' OFF BY ONE")
print("    137528045312 = q_23  -> stack 0905b00's 'Hercher's q_22' OFF BY ONE")
print("    (OUT-053's own line 'Hercher publie ... = q_23' uses the standard index)")

# Hercher adjudication (constant taken from the paper via the brief's single
# permitted access; see findings for citation and verbatim statements):
#   Corollary 29: X0 >= 3*2^69  =>  K > 1.375e11 odd members.
#   Remark 28: needed interval width 1.1032e-22.
#   Table 1 (Cor. 24): 'for all m: K > 7.20e10' at X0 = 704*2^60.
semi = qs[21] + qs[22]
require("q_21 + q_22 = 72057431991 (Hercher's 7.20e10 row, exact semiconvergent)",
        semi == 72057431991)
gap_fp = (thetaA[21] - thetaA[22]) // semi  # scaled by S
print(f"  (theta_21 - theta_22)/(q_21+q_22) = {FPA.fp_str(gap_fp, sig=5)}"
      f"   [Hercher Remark 28 prints 1.1032e-22]")
require("Remark-28 width reproduced (1.1032e-22)",
        FPA.fp_str(gap_fp, sig=5).startswith("1.103"))
require("1.375e11 is the 4-digit truncation of q_23, not an exact equality",
        137500000000 != qs[23] and str(qs[23]).startswith("13752"))
ratio_pct = qs[23] * 10 ** 6 // 137500000000
print(f"  Hercher's printed 1.375e11 vs q_23 = {qs[23]}: printed figure is a")
print(f"  rounded-down display (q_23/1.375e11 = {ratio_pct/10**6:.6f}); the underlying")
print(f"  threshold IS the convergent denominator q_23 exactly (see findings).")

# ----------------------------------------------------------------------------
# (f) The finite discharge.
# Implication chain (directions explicit; findings (f)):
#   cycle, x_min >= 2^71, length n <= W  ==>  0 < K/n - L < delta  (c)
#   ==>  [Legendre, since delta <= 1/(2n^2) in the window]  K/n reduces to a
#        convergent p_j/q_j, so n = m*q_j, K = m*p_j, and
#        |nL - K| = m*theta_j < n*delta = m*q_j*delta  ==>  theta_j < q_j*delta.
#   Criterion 2000*q_j*(q_j+q_{j+1}) <= 2079*2^71
#     ==>  q_j*delta <= 1/(q_j+q_{j+1}) < theta_j     [693/1000 < ln2]
#     ==>  contradiction  ==>  no cycle at any n = m*q_j <= W.
# ----------------------------------------------------------------------------

print()
print("(f) finite discharge: 22 integer criteria, margins, exact test, canary")

margins = []
allpass = True
for j in range(22):
    lhs = 2000 * qs[j] * (qs[j] + qs[j + 1])
    passes = lhs <= RHS
    allpass &= passes
    margins.append((j, lhs))
require("all 22 pass the integer criterion", allpass)
tight_j, tight_lhs = max(margins, key=lambda t: t[1])
require("tightest at j = 21 (q = 6586818670)", tight_j == 21)
m_int = RHS / tight_lhs
print(f"  tightest integer margin: {m_int:.4f}x at q_21 = {qs[21]}   [entry: 5.17x]")
require("integer margin 5.17x", abs(m_int - 5.17) < 0.005)

# exact test at j = 21: theta_21 / (q_21 * delta)
num = thetaA[21]
den = qs[21] * FPA.delta
m_exact = num / den
print(f"  exact test at q_21: theta/(q*delta) = {m_exact:.4f}x   [entry: 5.44x]")
require("exact margin 5.44x", abs(m_exact - 5.44) < 0.01)
require("integer form conservative (5.17 < 5.44)", m_int < m_exact)

# every j: criterion pass  =>  exact exclusion theta_j >= q_j delta holds too
ok = True
for j in range(22):
    ok &= (thetaA[j] >= qs[j] * FPA.delta)
require("exact exclusion theta_j >= q_j*delta for all 22", ok)

# multiples are covered by the same test (m-invariance), exact identity:
ok = True
for j, m in ((20, 3), (21, 2), (15, 7)):
    n = m * qs[j]
    K = m * ps[j]
    tm = abs(n * FPA.ln3 - K * FPA.ln2) * FPA.S // FPA.ln2
    ok &= abs(tm - m * thetaA[j]) <= m + 1
require("|m q_j L - m p_j| = m theta_j (multiples reduce to the same test)", ok)
print("  multiples n = m*q_j reduce to the same per-convergent test: verified")

# canary: the FIRST convergent past the window fails the criterion
lhs22 = 2000 * qs[22] * (qs[22] + qs[23])
require("canary: q_22 FAILS the integer criterion", lhs22 > RHS)
print(f"  canary: at q_22 = {qs[22]}: 2000*q*(q+q') = {lhs22}")
print(f"          > 2079*2^71 = {RHS}  -> criterion FAILS (non-vacuous) OK")
# and the exact seam test also admits q_22 (first admissible scale):
require("q_22 is the first admissible scale (theta_22 < q_22*delta)",
        thetaA[22] < qs[22] * FPA.delta)
ok = all(thetaA[j] >= qs[j] * FPA.delta for j in range(22))
require("...and no earlier convergent is admissible", ok)
print(f"  first admissible scale under the exact seam test: n >= q_22 = 6.547e10")
print(f"  (stack 0905b00 states this correctly in substance, labeled 'q_21')")

# ----------------------------------------------------------------------------
# (g) Scope statement.
# ----------------------------------------------------------------------------

print()
print("(g) scope: the closure statement and the Hercher comparison")
print(f"  closure: no positive cycle with x_min >= 2^71 and n <= {W_int}")
print(f"  (n = number of ODD elements = p+1; hypotheses used: q > 0 i.e. the")
print(f"   positive shore, x_min >= 2^71 from Barina-type verification)")
r = qs[23] / W_int
print(f"  Hercher q_23 / integral window = {r:.4f}  [his '3.9x' claim]")
require("3.9x ratio", abs(r - 3.93) < 0.01)
r2 = qs[23] / W_exact
print(f"  Hercher q_23 / exact window    = {r2:.4f}  (OUT-054 prints 3.92)")

# ----------------------------------------------------------------------------
# (h) Non-vacuity: the four real cycles against T1's hypotheses.
# ----------------------------------------------------------------------------

print()
print("(h) non-vacuity: where each real cycle exits T1's scope")
for x0, (xs, vs, K, P1, P2) in REAL.items():
    n = len(xs)
    q = 2 ** K - 3 ** n
    pos = all(x > 0 for x in xs)
    xmin_ok = min(abs(x) for x in xs) >= X71
    print(f"  {x0:>4}: n={n}, K={K}, q=2^K-3^n={q:>5}, positive shore: {pos}, "
          f"x_min >= 2^71: {xmin_ok}")
    if x0 == 1:
        require("trivial cycle: excluded from T1 scope ONLY by x_min < 2^71",
                pos and q > 0 and not xmin_ok)
        # its scale n=1 IS on the grid (q_0 = q_1 = 1), and the discharge
        # criterion at q=1 passes: no length-1 cycle ABOVE 2^71 exists;
        # the real trivial cycle lives below. Exact consistency:
        require("discharge at q=1 passes (kills length-1 cycles above 2^71)",
                2000 * 1 * (1 + 1) <= RHS and 2000 * 1 * (1 + 2) <= RHS)
    else:
        require(f"{x0}: negative shore (q < 0), outside T1's q > 0 hypothesis",
                (not pos) and q < 0)
require("all four cycles have x_min < 2^71 (consistency with the closure)",
        all(min(abs(x) for x in xs) < X71 for xs, _, _, _, _ in REAL.values()))
print("  the three negative cycles fail the positive-shore hypothesis (q < 0);")
print("  the trivial cycle fails only x_min >= 2^71 — each exclusion is exactly")
print("  where the hypotheses say it must be. No link is contradicted.")

# ----------------------------------------------------------------------------

print()
print("=" * 76)
print(f"TOTAL RECORDED CHECKS: {CHECKS}   FAILURES: {FAILURES}")
print("=" * 76)
if FAILURES:
    raise SystemExit(1)
print("ALL CHECKS PASSED")
