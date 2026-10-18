"""The staircase at a size threshold X0: fresh checks for cycles.md 12.8.7.

Supports: cycles.md 12.8.7 and briefs/staircase-x0-threshold-findings.md. These are
the threshold-X0 form of the uniform-trim sharpness (Simons-de Weger 2005, p. 69;
Rozier 1991, p. 11).

Fresh code. It imports nothing from staircase_allp*.py, staircase_gamma_upper.py,
uniform_trim.py or ceiling_novelty_check.py. The construction is transcribed from
the statement of cycles.md 12.8.6.2 (Construction B), not from its code.

STOPPING RULES. This is a size-only construction. No cycle search is run and no
divisibility test is made: q | R_r is never evaluated anywhere in this file. No
per-period exclusion is computed. Every configuration built here is a size-passer
only.

Notation (cycles.md 12.1, 12.6.1, 12.8). The configuration has p blocks (m_t, s_t),
with n = sum m, K = n + sum s, q = 2^K - 3^n > 0 and gamma = K - log2 q. L = log2 3,
eps_p = (L-1)/(L^p - 1), and R_r is the rotation numerator of 12.6.1. Further
a_r = R_r/q (SdW's a_i), x_r = 2^{m_r} a_r - 1 (the block start, a local minimum)
and x_min = min_r x_r. lam = L/(L-1) + 2^-20.

Parts:
  A. Exact enclosure of L (integer atanh series, explicit remainder), its continued
     fraction, convergents q_k and theta_k = |q_k L - p_k|, cross-certified against
     exact 3^q vs 2^p comparisons.
  B. The algebra of Theorem 12.8.7.2 in exact rationals: the closed form of A_r, the
     identity reducing the crash condition to gamma >= Gamma'(p,n), and
     Gamma'(p,n) - eps_p n - eta < L/(L-1).
  C. Universal statements on random configurations (exact): the dictionary
     (rotation recurrence, Terras iteration, product identity), the sandwich
     gamma - 1 <= log2(x_min+1) < gamma + log2 p, the trim gamma + log2 p > eps_p n,
     the unit-block bound, and Rozier's minimax rho >= eps_p n in every order.
  D. The sweep lemma: two-distance structure at N = q_k + q_{k-1}, checked exactly,
     and brute force over n <= 3,000,000 (longest run missing each theorem arc).
  E. The period threshold p1(X0) from the continued fraction, for X0 = 2^j
     (j <= 200) and SdW's X0 = 5*2^60.
  F. The construction at threshold X0, end to end, exact. For each X0 and each p
     from p1(X0) up to the big-integer budget: the witness n in the window, all p
     size conditions, x_min >= X0, the gamma bracket, gamma - eps_p n, Rozier's rho,
     SdW Lemma 7 and Corollary 5, and the deep crash. Also the stronger (X') variant.
  G. Negative controls.

Exact arithmetic (Python ints, fractions.Fraction) decides every size condition,
threshold condition and witness selection. Floats appear only in reported
logarithms and in margin-guarded comparisons, which print UNDECIDED rather than
guess.

One command reproduces the committed output (about 10-20 minutes):
    python experiments/staircase_x0_threshold.py > experiments/staircase_x0_threshold_output.txt
"""

from fractions import Fraction
import math
import random
import sys

CHECKS = 0
FAILS = 0
QUICK = "--quick" in sys.argv     # development only; the committed output is the full run


def check(cond, label):
    global CHECKS, FAILS
    CHECKS += 1
    if cond:
        print("  PASS  " + label)
    else:
        FAILS += 1
        print("  FAIL  " + label)


def header(t):
    print()
    print("=" * 76)
    print(t)
    print("=" * 76)


# ---------------------------------------------------------------------------
# Part A. L = log2 3, rigorously enclosed.
# ---------------------------------------------------------------------------

header("Part A. Enclosure of L = log2 3, continued fraction, convergents")

P_HI = 1400


def atanh_inv_fixed(k, P):
    """Integers lo <= 2^P * atanh(1/k) <= hi.

    Each term floor(2^P/((2i+1)k^(2i+1))) is low by < 1. The loop stops at the
    first term that floors to 0, i.e. the first true term < 1. The remaining true
    terms then sum to < 1/(1 - 1/k^2) <= 9/8 < 2.
    """
    one = 1 << P
    s = 0
    i = 0
    pk = k
    k2 = k * k
    while True:
        t = one // ((2 * i + 1) * pk)
        if t == 0:
            break
        s += t
        i += 1
        pk *= k2
    return s, s + i + 2


a3 = atanh_inv_fixed(3, P_HI)      # ln 2   = 2 atanh(1/3)
a5 = atanh_inv_fixed(5, P_HI)      # ln 3/2 = 2 atanh(1/5)
LN2 = (2 * a3[0], 2 * a3[1])
LN3 = (2 * a3[0] + 2 * a5[0], 2 * a3[1] + 2 * a5[1])
L_LO = Fraction(LN3[0], LN2[1])
L_HI = Fraction(LN3[1], LN2[0])
width = L_HI - L_LO
check(0 < width < Fraction(1, 1 << 1380), "L enclosed in an interval of width < 2^-1380")
LF = float(L_LO)
print("  L = %.15f" % LF)


def cf_of(fr, maxlen=2000):
    out = []
    x = fr
    for _ in range(maxlen):
        a = x.numerator // x.denominator
        out.append(a)
        rem = x - a
        if rem == 0:
            break
        x = 1 / rem
    return out


cf_lo = cf_of(L_LO)
cf_hi = cf_of(L_HI)
common = []
for u, v in zip(cf_lo, cf_hi):
    if u != v:
        break
    common.append(u)
CF = common[:-1]   # drop the last common entry: safe prefix of the CF of L
print("  certified partial quotients: %d" % len(CF))
print("  first 20: %s" % CF[:20])
check(CF[:15] == [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55],
      "CF prefix matches SdW v1.44 p. 3: [1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,...]")

# convergents p_k/q_k, k >= 0
PK, QK = [], []
pm2, pm1, qm2, qm1 = 0, 1, 1, 0
for a in CF:
    pk = a * pm1 + pm2
    qk = a * qm1 + qm2
    PK.append(pk)
    QK.append(qk)
    pm2, pm1, qm2, qm1 = pm1, pk, qm1, qk


def theta_interval(k):
    """Rational interval for theta_k = |q_k L - p_k| (sign determined)."""
    lo = QK[k] * L_LO - PK[k]
    hi = QK[k] * L_HI - PK[k]
    assert (lo > 0) == (hi > 0) and lo != 0 and hi != 0
    if lo > 0:
        return lo, hi
    return -hi, -lo


THETA = []
for k in range(len(QK)):
    t0, t1 = theta_interval(k)
    THETA.append((t0, t1))
THETA_F = [float(t[0]) for t in THETA]

# cross-certify by exact power comparison at convergents with q <= 2*10^5
ok = True
cnt = 0
for k in range(len(QK)):
    if QK[k] > 200000:
        break
    sgn_exact = (3 ** QK[k] > 2 ** PK[k])          # q L > p  <=>  3^q > 2^p
    sgn_int = (QK[k] * L_LO - PK[k] > 0)
    ok = ok and (sgn_exact == sgn_int)
    cnt += 1
check(ok, "sign of q_k L - p_k agrees with exact 3^q vs 2^p at all %d convergents with q <= 2*10^5" % cnt)

# the identity q_k theta_{k-1} + q_{k-1} theta_k = 1 (bracketed)
ok = True
for k in range(1, 60):
    lo = QK[k] * THETA[k - 1][0] + QK[k - 1] * THETA[k][0]
    hi = QK[k] * THETA[k - 1][1] + QK[k - 1] * THETA[k][1]
    ok = ok and lo <= 1 <= hi
check(ok, "q_k theta_{k-1} + q_{k-1} theta_k = 1 bracketed exactly, k = 1..59")
print("  convergent denominators: %s ..." % QK[:16])

LAM = LF / (LF - 1) + 2.0 ** -20       # lam = L/(L-1) + 2^-20
print("  L/(L-1) = %.10f,  lam = L/(L-1) + 2^-20 = %.10f" % (LF / (LF - 1), LAM))
C_INF = 2.0 ** (-1 / (LF - 1))
print("  SdW's limiting constant c_inf = 2^(-1/(L-1)) = %.6f" % C_INF)

# fixed point L for fast scans
P_LO = 192
LFX_LO = (L_LO.numerator << P_LO) // L_LO.denominator
LFX_HI = -((-(L_HI.numerator << P_LO)) // L_HI.denominator)


def delta_interval(n):
    """(K, dlo, dhi) with K = ceil(nL), delta(n) = K - nL in [dlo, dhi] (floats),
    or None if undecided at this precision."""
    a_lo = n * LFX_LO
    a_hi = n * LFX_HI
    f = a_lo >> P_LO
    if (a_hi >> P_LO) != f:
        return None
    K = f + 1
    dlo = ((K << P_LO) - a_hi) / (1 << P_LO)
    dhi = ((K << P_LO) - a_lo) / (1 << P_LO)
    return K, dlo, dhi


def delta_of(g):
    """delta(g) = -log2(1 - 2^-g), the involution between gamma and delta."""
    return -math.log1p(-2.0 ** (-g)) / math.log(2)


# ---------------------------------------------------------------------------
# Part B. Algebra of Theorem 12.8.7.2, exact rationals.
# ---------------------------------------------------------------------------

header("Part B. Algebra: closed form of A_r, the crash identity, Gamma'(p,n) < eps n + L/(L-1) + eta")

rng = random.Random(20261019)
Lt = Fraction(L_LO.numerator, L_LO.denominator)   # any L != 1 suffices for identities
D = (Lt - 1) ** 2


def A_closed(r, g, beta):
    gg = g  # gamma
    return (Lt ** (r + 1) * ((gg - beta) * (Lt - 1) - 1) + (r + beta - gg) * (Lt - 1) + Lt) / D


ok = True
for trial in range(40):
    g = Fraction(rng.randint(200, 5000), 100)
    beta = 1 + Fraction(rng.randint(0, 1000), 10 ** 9)
    A = Fraction(0)
    for r in range(0, 25):
        A = Lt * A + g - r - beta
        ok = ok and (A == A_closed(r, g, beta))
check(ok, "A_r recursion (A_-1 = 0, A_r = L A_{r-1} + gamma - r - beta) equals its closed form, 40 x 25 exact")


def gstar(p, n):
    return (Lt ** p - Lt ** 2 - (Lt - 1) * (p - 2) + D * n) / ((Lt - 1) * (Lt ** p - 1))


ok = True
for trial in range(60):
    p = rng.randint(2, 30)
    n = rng.randint(p, 10 ** 6)
    beta = 1 + Fraction(rng.randint(0, 1000), 10 ** 9)
    gamma = Fraction(rng.randint(100, 4000), 100)
    g = gamma - beta
    Ap2 = A_closed(p - 2, gamma, beta)
    lhs = Lt * Ap2 - (n + p - 2 - g)
    rhs = ((Lt - 1) * (Lt ** p - 1) / D) * (g - gstar(p, n))
    ok = ok and (lhs == rhs)
check(ok, "L*A_{p-2} - (n+p-1-gamma+eta) = [(L-1)(L^p-1)/(L-1)^2](gamma - Gamma'(p,n)), 60 random exact")

ok = True
for Lx in (L_LO, L_HI):
    LL = Fraction(Lx)
    for p in range(2, 160):
        g0 = 1 + (LL ** p - LL ** 2 - (LL - 1) * (p - 2)) / ((LL - 1) * (LL ** p - 1))
        ok = ok and (g0 < LL / (LL - 1))
check(ok, "Gamma'_0(p) := Gamma'(p,n) - eps_p n - eta < L/(L-1) for p = 2..159 at both ends of the L interval")

# eps_p n coefficient of Gamma' is exactly eps_p
ok = True
for p in range(2, 40):
    slope = gstar(p, 1) - gstar(p, 0)
    ok = ok and slope == (Lt - 1) / (Lt ** p - 1)
check(ok, "the n-coefficient of Gamma'(p,n) is exactly eps_p = (L-1)/(L^p-1), p = 2..39")

# the record's crash-depth-1 demand Gamma(p,n) has n-coefficient (L-1)/(L^{p-1}-1) ~ L eps_p
for p in (10, 20, 30):
    lp = LF ** p
    s_rec = (LF - 1) / (LF ** (p - 1) - 1)
    s_new = (LF - 1) / (lp - 1)
    print("  p = %2d: n-slope of Gamma (crash depth 1) / n-slope of Gamma' (deep crash) = %.6f" % (p, s_rec / s_new))


# ---------------------------------------------------------------------------
# Shared exact machinery: R_r, rotation recurrence, construction.
# ---------------------------------------------------------------------------

def R_def(m, s, r):
    """R_r by the definition of cycles.md 12.6.1 (rotation order from r)."""
    p = len(m)
    mm = [m[(r + i) % p] for i in range(p)]
    ss = [s[(r + i) % p] for i in range(p)]
    sig = [ss[i] + mm[(i + 1) % p] for i in range(p)]
    total = 0
    Msuf = 0
    S_pref = [0] * p
    acc = 0
    for i in range(p):
        S_pref[i] = acc
        acc += sig[i]
    for t in range(p - 1, -1, -1):
        total += (3 ** Msuf) * ((1 << (S_pref[t] + ss[t])) - (1 << S_pref[t]))
        Msuf += mm[t]
    return total


def R_all_recurrence(m, s, q, R0):
    """R_{r+1} = (3^{m_r} R_r + (2^{s_r}-1) q) / 2^{sigma_r}: the chain equation
    times q. The 2-power division is checked to be exact (an identity, not a
    divisibility test of q). Returns the list R_0..R_{p-1} and whether R_p == R_0."""
    p = len(m)
    out = [R0]
    R = R0
    for r in range(p):
        sig = s[r] + m[(r + 1) % p]
        num = (3 ** m[r]) * R + ((1 << s[r]) - 1) * q
        if num & ((1 << sig) - 1):
            return None, False
        R = num >> sig
        if r < p - 1:
            out.append(R)
    return out, (R == R0)


def log2_int(x):
    b = x.bit_length()
    if b <= 64:
        return math.log2(x)
    return math.log2(x >> (b - 64)) + (b - 64)


def construct_B(p, n, K, q, Qmult=1):
    """Construction B of cycles.md 12.8.6.2, transcribed from its statement, with
    q replaced by Q = Qmult*q in the caps (Qmult = 1 is the construction as stated).
    Returns (m, s, bound_flag, pow3T) or None if it cannot be run."""
    S = K - n
    if S < p:
        return None
    sc = S - (p - 1)
    Q = Qmult * q
    T = 0
    pow3T = 1
    m = []
    bound = False
    qb = Q.bit_length()
    for r in range(p - 1):
        e2 = n - T + p - 1 - r
        # X_r = 3^T 2^{e2} (2^{sc}-1) = (3^T << (e2+sc)) - (3^T << e2)
        X = (pow3T << (e2 + sc)) - (pow3T << e2)
        if X < Q:
            return None
        c0 = X.bit_length() - qb
        while c0 >= 0 and (Q << c0) > X:
            c0 -= 1
        while (Q << (c0 + 1)) <= X:
            c0 += 1
        cap = c0
        budget = n - 1 - T - (p - 2 - r)
        mr = min(cap, budget)
        if budget < cap:
            bound = True
        if mr < 1:
            return None
        m.append(mr)
        T += mr
        pow3T *= 3 ** mr
    c = n - T
    if c < 1:
        return None
    m.append(c)
    s = [1] * (p - 1) + [sc]
    return m, s, bound, pow3T


def full_profile_check(m, s, n, K, q, X0, Qmult=1, def_all=False):
    """Exact checks on a built profile. Returns dict."""
    p = len(m)
    res = {}
    res["shape"] = (sum(m) == n and sum(s) + n == K and min(m) >= 1 and min(s) >= 1)
    R0 = R_def(m, s, 0)
    Rs, closes = R_all_recurrence(m, s, q, R0)
    res["closes"] = closes and Rs is not None
    if Rs is None:
        return res
    if def_all:
        res["def_all"] = all(R_def(m, s, r) == Rs[r] for r in range(p))
    res["size"] = all(q <= R for R in Rs)                        # (S)
    res["sizeQ"] = all(Qmult * q <= R for R in Rs)               # (X') if Qmult = X0
    vals = [Rs[r] << m[r] for r in range(p)]                     # q (x_r + 1)
    res["thresh"] = all((X0 + 1) * q <= v for v in vals)         # (X)
    imin = min(range(p), key=lambda r: vals[r])
    res["imin"] = imin
    lq = log2_int(q)
    gamma = K - lq
    res["gamma"] = gamma
    res["log2xmin1"] = log2_int(vals[imin]) - lq                 # log2(x_min + 1)
    res["log2x01"] = log2_int(vals[0]) - lq
    # sandwich, exact: 2^{K-1} <= 2^{m_r} R_r for all r; min < p 2^K
    res["sand_lo"] = all(v >= (1 << (K - 1)) for v in vals)
    res["sand_hi"] = vals[imin] < p * (1 << K)
    return res


# ---------------------------------------------------------------------------
# Part C. Universal statements on random configurations (exact).
# ---------------------------------------------------------------------------

header("Part C. Universal statements on random configurations (exact)")


def terras_check(m, s, a0):
    """Iterate the Terras map along 1^{m_0} 0^{s_0} ... from x_0 = 2^{m_0} a_0 - 1
    (Fractions). Return (closes, block_starts, product_ok_ratio)."""
    x0 = (1 << m[0]) * a0 - 1
    y = x0
    starts = []
    prod = Fraction(1)
    for t in range(len(m)):
        starts.append(y)
        for _ in range(m[t]):
            prod *= 1 + Fraction(1, 1) / (3 * y)
            y = (3 * y + 1) / 2
        for _ in range(s[t]):
            y = y / 2
    return y == x0, starts, prod


def rand_config(rng):
    p = rng.randint(1, 7)
    if rng.random() < 0.5:
        m = [rng.randint(1, 12) for _ in range(p)]
    else:   # staircase-like
        m = []
        v = rng.randint(1, 4)
        for _ in range(p):
            m.append(max(1, int(v)))
            v = v * rng.uniform(1.2, 1.8) + rng.uniform(0, 2)
        if rng.random() < 0.5:
            m[-1] = rng.randint(1, 3)
    n = sum(m)
    K0 = (3 ** n).bit_length()            # ceil(nL)
    S = K0 - n + rng.choice([0, 0, 0, 0, 1, 2])
    if S < p:
        return None
    # composition of S into p parts >= 1: mostly unit exits, mass on one block
    if rng.random() < 0.5:
        cuts = sorted(rng.sample(range(1, S), p - 1)) if p > 1 else []
        parts = [b - a for a, b in zip([0] + cuts, cuts + [S])]
    else:
        parts = [1] * p
        j = rng.randrange(p)
        parts[j] = S - (p - 1)
    return m, parts


ncfg = 0
npass = 0
nunit = 0
ok_chain = ok_terras = ok_prod = ok_sand = ok_trim = ok_unit = ok_roz = True
undec = 0
min_lo_gap = 1e9      # log2(x_min+1) - (gamma - 1)  >= 0
max_hi_gap = -1e9     # log2(x_min+1) - (gamma + log2 p) < 0
min_trim = 1e9
min_unit = 1e9
min_roz = 1e9
terras_done = 0
while ncfg < 30000:
    cfg = rand_config(rng)
    if cfg is None:
        continue
    m, s = cfg
    p = len(m)
    n = sum(m)
    K = n + sum(s)
    q = (1 << K) - 3 ** n
    if q <= 0:
        continue
    ncfg += 1
    Rs = [R_def(m, s, r) for r in range(p)]
    # chain recurrence (dictionary): 2^{sigma_r} R_{r+1} = 3^{m_r} R_r + (2^{s_r}-1) q
    for r in range(p):
        sig = s[r] + m[(r + 1) % p]
        if (Rs[(r + 1) % p] << sig) != (3 ** m[r]) * Rs[r] + ((1 << s[r]) - 1) * q:
            ok_chain = False
    if terras_done < 4000:
        closes, starts, prod = terras_check(m, s, Fraction(Rs[0], q))
        ok_terras = ok_terras and closes and all(
            starts[t] == Fraction(Rs[t] << m[t], q) - 1 for t in range(p))
        ok_prod = ok_prod and (prod == Fraction(1 << K, 3 ** n)) and all(x > 0 for x in starts)
        terras_done += 1
    vals = [Rs[r] << m[r] for r in range(p)]
    vmin = min(vals)
    ok_sand = ok_sand and all(v >= (1 << (K - 1)) for v in vals) and vmin < p * (1 << K)
    lq = log2_int(q)
    gamma = K - lq
    lx = log2_int(vmin) - lq
    min_lo_gap = min(min_lo_gap, lx - (gamma - 1))
    max_hi_gap = max(max_hi_gap, lx - (gamma + math.log2(p)))
    eps = (LF - 1) / (LF ** p - 1)
    # Rozier minimax in every rotation order (pure real inequality)
    for r in range(p):
        mm = [m[(r + i) % p] for i in range(p)]
        T = 0
        rho = -1e18
        for j in range(p):
            rho = max(rho, mm[j] - (LF - 1) * T)
            T += mm[j]
        d = rho - eps * n
        min_roz = min(min_roz, d)
        if d < -1e-9:
            ok_roz = False
    if all(q <= R for R in Rs):           # a size-passer
        npass += 1
        d = gamma + math.log2(p) - eps * n
        if abs(d) < 1e-9:
            undec += 1
        elif d < 0:
            ok_trim = False
        min_trim = min(min_trim, d)
        if 1 in m and p >= 2:
            nunit += 1
            Lp1 = LF ** (p - 1)
            bound = (LF - 1) * (n - Lp1) / (Lp1 - 1)
            d2 = gamma + math.log2(p) - bound
            if abs(d2) < 1e-9:
                undec += 1
            elif d2 < 0:
                ok_unit = False
            min_unit = min(min_unit, d2)

print("  random configurations: %d (q > 0), of which size-passers: %d, with a unit block: %d"
      % (ncfg, npass, nunit))
check(ok_chain, "rotation recurrence 2^sigma_r R_{r+1} = 3^{m_r} R_r + (2^{s_r}-1) q holds at every rotation, all configs")
check(ok_terras, "Terras iteration from x_0 = 2^{m_0} R_0/q - 1 closes and hits every block start x_r = 2^{m_r} R_r/q - 1 (%d configs)" % terras_done)
check(ok_prod, "product identity 2^K/3^n = prod over odd steps (1 + 1/(3y)), all elements > 0 (%d configs)" % terras_done)
check(ok_sand, "sandwich (exact integers): gamma - 1 <= log2(x_min+1) < gamma + log2 p, all %d configs" % ncfg)
print("    tightness: min of log2(x_min+1) - (gamma-1) = %.6f ; max of log2(x_min+1) - (gamma + log2 p) = %.6f"
      % (min_lo_gap, max_hi_gap))
check(ok_trim and undec == 0, "trim (12.8.1): gamma + log2 p > eps_p n at all %d size-passers (min margin %.4f)" % (npass, min_trim))
check(ok_unit, "unit-block bound: gamma + log2 p > (L-1)(n - L^{p-1})/(L^{p-1}-1) at all %d size-passers with some m_t = 1 (min margin %.4f)" % (nunit, min_unit))
check(ok_roz, "Rozier minimax: max_j (m_j - (L-1) M_{j-1}) >= eps_p n in every rotation order, all configs (min margin %.6f)" % min_roz)

# repeated-block family: the sandwich's upper end is approached (log2 p is real)
print("  repeated single block (m, s) x p: log2(x_min+1) - gamma  vs  log2 p")
for (mb, sb) in ((1, 1), (5, 3), (12, 8)):
    for p in (2, 8, 32):
        m = [mb] * p
        s = [sb] * p
        n = sum(m)
        K = n + sum(s)
        q = (1 << K) - 3 ** n
        R0 = R_def(m, s, 0)
        lx = log2_int(R0 << m[0]) - log2_int(q)
        g = K - log2_int(q)
        print("    (m,s)=(%2d,%2d) p=%2d: log2(x_min+1) - gamma = %8.4f, log2 p = %6.3f" % (mb, sb, p, lx - g, math.log2(p)))


# ---------------------------------------------------------------------------
# Part D. The sweep lemma.
# ---------------------------------------------------------------------------

header("Part D. Sweep lemma: two-distance structure at N = q_k + q_{k-1}; brute force n <= 3*10^6")

FX_ONE = 1 << P_LO
TOL = 1 << 40   # tolerance in fixed-point units (2^-152), far below any gap here
for k in range(1, len(QK)):
    N = QK[k] + QK[k - 1]
    if N > 400000:
        break
    pts = sorted(((j * LFX_LO) & (FX_ONE - 1)) for j in range(N))
    gaps = [pts[i + 1] - pts[i] for i in range(N - 1)] + [pts[0] + FX_ONE - pts[-1]]
    a = int(THETA[k - 1][0] * FX_ONE)
    b = int(THETA[k][0] * FX_ONE)
    na = sum(1 for g in gaps if abs(g - a) <= TOL)
    nb = sum(1 for g in gaps if abs(g - b) <= TOL)
    mg = max(gaps)
    good = (na + nb == N) and abs(mg - a) <= TOL and (na == QK[k] and nb == QK[k - 1] or a == b)
    check(good, "k=%2d N=q_k+q_{k-1}=%6d: gaps are theta_{k-1} (x%d) and theta_k (x%d); maxgap = theta_{k-1} = %.3e"
          % (k, N, na, nb, THETA_F[k - 1]))


def N_of(ell):
    """N(ell) = q_k + q_{k-1} for the least k >= 1 with theta_{k-1} <= ell."""
    for k in range(1, len(QK)):
        t = THETA_F[k - 1]
        if abs(t - ell) <= 1e-12 * ell:
            raise RuntimeError("UNDECIDED theta vs ell")
        if t <= ell:
            return QK[k] + QK[k - 1], k
    raise RuntimeError("CF too short")


GRID_X0 = [1, 10, 31, 100, 1000, 4096]   # every X0 <= 5 shares X0 = 1's level (lam dominates)


def g_lo_of(X0):
    return 1 + max(math.log2(X0 + 1), LAM)


def arc_of(glo):
    return delta_of(glo + 1), delta_of(glo)


# brute-force sweep over n = 1..NB
NB = 300000 if QUICK else 3000000
print("  computing delta(n) for n = 1..%d ..." % NB)
DLO = [0.0] * (NB + 1)
DHI = [0.0] * (NB + 1)
a_lo = 0
a_hi = 0
und = 0
for n in range(1, NB + 1):
    a_lo += LFX_LO
    a_hi += LFX_HI
    f = a_lo >> P_LO
    if (a_hi >> P_LO) != f:
        und += 1
        DLO[n] = -1.0
        DHI[n] = 2.0
        continue
    Kc = f + 1
    DLO[n] = ((Kc << P_LO) - a_hi) / FX_ONE
    DHI[n] = ((Kc << P_LO) - a_lo) / FX_ONE
check(und == 0, "delta(n) decided at every n <= %d (fixed point 2^-192)" % NB)


def longest_miss(e1, e2):
    """Longest run of consecutive n <= NB with delta(n) not certainly in [e1, e2]."""
    lo = e1 * (1 + 1e-11)
    hi = e2 * (1 - 1e-11)
    best = 0
    run = 0
    for n in range(1, NB + 1):
        if DLO[n] >= lo and DHI[n] <= hi:
            run = 0
        else:
            run += 1
            if run > best:
                best = run
    return best


for X0 in GRID_X0:
    glo = g_lo_of(X0)
    e1, e2 = arc_of(glo)
    ell = e2 - e1
    N, k = N_of(ell)
    if N > NB // 20:
        print("  X0 = %5d: N(ell) = %d too large for the brute-force range; skipped" % (X0, N))
        continue
    lm = longest_miss(e1, e2)
    check(lm <= N - 1, "X0 = %5d: arc [delta(g+1), delta(g)], g = %.4f, length %.3e: longest miss run %d <= N - 1 = %d"
          % (X0, glo, ell, lm, N - 1))
    # negative control: an arc of length 0.9 theta_{k-1} is missed for longer
    e2c = e1 + 0.9 * THETA_F[k - 1]
    if e2c < e2 and N < 2000:
        lmc = longest_miss(e1, e2c)
        check(lmc > N - 1, "   control: arc of length 0.9*theta_{k-1} = %.3e is missed by a run of %d > N - 1"
              % (0.9 * THETA_F[k - 1], lmc))


# ---------------------------------------------------------------------------
# Part E. The period threshold p1(X0).
# ---------------------------------------------------------------------------

header("Part E. Period threshold p1(X0): least p with (L^p-1)/(2(L-1)) >= max(N, 3p+40)")


def p1_of_level(glo):
    e1, e2 = arc_of(glo)
    N, k = N_of(e2 - e1)
    p = 2
    while True:
        lhs = (LF ** p - 1) / (2 * (LF - 1))
        rhs = max(N, 3 * p + 40)
        if abs(lhs - rhs) <= 1e-9 * rhs:
            raise RuntimeError("UNDECIDED p1")
        if lhs >= rhs:
            return p, N
        p += 1


def glo_big(log2X0p1):
    return 1 + max(log2X0p1, LAM)


print("   j  (X0 = 2^j)   level g      N(ell)          p1   p1 - log_L(X0)")
table = []
ok_mono = True
for j in list(range(0, 21)) + list(range(30, 201, 10)):
    l2 = j + math.log2(1 + 2.0 ** (-j))
    glo = glo_big(l2)
    p1, N = p1_of_level(glo)
    table.append((j, p1))
    # monotone: every p >= p1 satisfies the condition (checked to p1 + 60)
    for p in range(p1, p1 + 61):
        if not ((LF ** p - 1) / (2 * (LF - 1)) >= max(N, 3 * p + 40)):
            ok_mono = False
    print("  %3d            %8.4f  %12.5e   %4d   %8.3f" % (j, glo, N, p1, p1 - j / math.log2(LF)))
check(ok_mono, "the p1 condition holds at every p in [p1, p1 + 60] for every tabulated X0 (monotone)")
X0_SDW = 5 * 2 ** 60
p1s, Ns = p1_of_level(glo_big(math.log2(X0_SDW + 1)))
print("  SdW v1.44 X0 = 5*2^60: p1 = %d (N = %.4e)" % (p1s, Ns))
check(p1s >= 76, "p1(5*2^60) = %d >= 76: no conflict with SdW v1.44's 'no m-cycles for m <= 75' at that X0" % p1s)
X0_B = 2 ** 71
p1b, Nb = p1_of_level(glo_big(math.log2(X0_B + 1)))
print("  X0 = 2^71 (the verification bound cited in paper 1): p1 = %d (N = %.4e)" % (p1b, Nb))


# ---------------------------------------------------------------------------
# Part F. The construction at threshold X0, end to end.
# ---------------------------------------------------------------------------

header("Part F. Construction B at threshold X0: witness, all p size conditions, x_min >= X0, brackets")

NCAP = 60000 if QUICK else 4500000
# Theorem 12.8.7.4's uniform cap on Psi_0 = log2(x_0+1) - gamma: m_0 >= 3, p >= 10, n >= (L^p-1)/(2(L-1))
PSI_BAR = math.log2(1 + 2.0 ** (-(LF - 1) * 3) / (1 - 2.0 ** (-(2 * LF - 3))) + 2.0 ** -30)
print("  Psi_bar = log2(1 + 2^(-3(L-1))/(1 - 2^-(2L-3)) + 2^-30) = %.6f" % PSI_BAR)
ok = True
for p in range(10, 400):
    nlow = (LF ** p - 1) / (2 * (LF - 1))
    ok = ok and math.log2(p - 1) + p - 1 - (LF - 1) * (nlow - p + 1) <= -30
check(ok, "tail term (p-1) 2^(p-1-(L-1)(n-p+1)) <= 2^-30 for p = 10..399 at n >= (L^p-1)/(2(L-1))")


def sdw_cm(m, X0):
    d = LF
    b = 2.0 ** (-1 / d) * (1 + 1.0 / X0)
    return 2.0 ** ((m / d) * (d - 1) / (d ** m - 1)) * b ** (d / (d - 1) - m / (d ** m - 1))


def record_Gamma(p, n, eta):
    beta = 1 + eta
    L = LF
    return ((n - 1) * (L - 1) ** 2 + L ** (p - 1) * (1 + beta * (L - 1)) - (p - 2 + beta) * (L - 1) - L) / (
        (L - 1) * (L ** (p - 1) - 1))


def gamma_prime(p, n, eta):
    L = LF
    return 1 + eta + (L ** p - L ** 2 - (L - 1) * (p - 2) + (L - 1) ** 2 * n) / ((L - 1) * (L ** p - 1))


RUNS = []


def run_one(X0, p, level=None, label="", Qmult=1, record=True, ntop=None):
    """Find the witness in the theorem window and verify everything exactly.
    ntop = None: the window of Theorem 12.8.7.3 (top n* = floor((g - lam)/eps_p)).
    ntop given: the window [ntop - N + 1, ntop], valid when eps_p ntop + lam <= g."""
    glo = g_lo_of(X0) if level is None else level
    e1, e2 = arc_of(glo)
    N, k = N_of(e2 - e1)
    eps = (LF - 1) / (LF ** p - 1)
    if ntop is None:
        nstar_f = (glo - LAM) / eps
        nstar = int(math.floor(nstar_f))
        if abs(nstar_f - round(nstar_f)) < 1e-6:
            print("  UNDECIDED n* at X0=%d p=%d" % (X0, p))
            return None
    else:
        nstar = ntop
        if not (eps * ntop + LAM <= glo - 1e-9 and ntop - N + 1 >= 3 * p + 40):
            check(False, "X0=%d p=%d: the placed window is valid" % (X0, p))
            return None
    lo = e1 * (1 + 1e-11)
    hi = e2 * (1 - 1e-11)
    wit = None
    for off in range(N):
        n = nstar - off
        di = delta_interval(n)
        if di is None:
            continue
        Kc, dlo, dhi = di
        if dlo >= lo and dhi <= hi:
            wit = (n, Kc, off)
            break
    res = {"X0": X0, "p": p, "N": N, "nstar": nstar, "extra": (level is not None) or (ntop is not None)}
    if wit is None:
        check(False, "X0=%d p=%d: a witness exists in the window of N = %d integers" % (X0, p, N))
        return None
    n, Kc, off = wit
    three = 3 ** n
    K = three.bit_length()
    q = (1 << K) - three
    S = K - n
    eta = -math.log1p(-2.0 ** (-(S - p + 1))) / math.log(2)
    out = construct_B(p, n, K, q, Qmult)
    if out is None:
        check(False, "X0=%d p=%d n=%d: construction runs" % (X0, p, n))
        return None
    m, s, bound, pow3T = out
    pc = full_profile_check(m, s, n, K, q, X0, Qmult, def_all=(n <= 30000))
    gamma = pc["gamma"]
    gq = gamma - math.log2(Qmult)
    epsn = eps * n
    H0 = (S >= p) and ((LF - 1) * (n - p) + gq >= p + eta + 1e-9)
    H1p = gq >= max(epsn + LAM, 2 + eta) - 1e-12
    gp = gamma_prime(p, n, eta)
    # Rozier rho, order from block 0 and from the minimum block
    def rho_from(start):
        T = 0
        best = -1e18
        for j in range(p):
            mj = m[(start + j) % p]
            best = max(best, mj - (LF - 1) * T)
            T += mj
        return best
    rho0 = rho_from(0)
    rhomin = rho_from(pc["imin"])
    # growth claim (b): T_r > A_r for the uncapped run
    growth_ok = True
    crash_term_ok = True
    if not bound:
        A = 0.0
        T = 0
        beta = 1 + eta
        for r in range(p - 1):
            A = LF * A + gq - r - beta
            T += m[r]
            if not (T > A - 1e-6 * max(1.0, abs(A))):
                growth_ok = False
        # crash rotation's own term: Q <= 3^{T_{p-2}} (2^{s_c} - 1)
        sc = s[-1]
        crash_term_ok = (Qmult * q <= (pow3T << sc) - pow3T)
    # SdW Lemma 7 and Corollary 5 (floats, reported)
    Lam = -math.log1p(-2.0 ** (-gamma))
    cm = sdw_cm(p, X0)
    l7_rhs = p * cm * 2.0 ** (-epsn)
    l7_ok = Lam < l7_rhs
    xm = 2.0 ** pc["log2xmin1"] - 1
    cor5_ok = Lam < p / xm
    psi0 = pc["log2x01"] - gamma
    m0 = m[0]
    psi_bound = math.log2(1 + 9.01 * 2.0 ** (-(LF - 1) * m0) + (p - 1) * 2.0 ** (p - 1 - (LF - 1) * (n - p + 1)))
    rec_G = record_Gamma(p, n, eta)
    res.update(dict(n=n, off=off, gamma=gamma, epsn=epsn, c=m[-1], bound=bound, rho0=rho0, imin=pc["imin"],
                    Lam=Lam, l7ratio=l7_rhs / Lam, recG=rec_G, gp=gp, lx=pc["log2xmin1"], psi0=psi0,
                    rho_is_m0=(abs(rho0 - m[0]) < 1e-9)))
    allok = (pc["shape"] and pc["closes"] and pc.get("def_all", True) and pc["size"] and pc["thresh"]
             and pc["sand_lo"] and pc["sand_hi"] and H0 and H1p and gp <= gq + 1e-9 and growth_ok and crash_term_ok
             and (Qmult == 1 or pc["sizeQ"]))
    if Qmult == 1:
        allok = allok and (glo - 1e-9 <= gamma <= glo + 1 + 1e-9) \
            and (epsn - 1e-9 <= rho0 <= gamma - eta + 1e-9) and l7_ok and cor5_ok and psi0 <= psi_bound + 1e-9 \
            and gamma + math.log2(p) > epsn
        if ntop is None:
            allok = allok and (LAM - 1e-9 <= gamma - epsn <= LAM + 1.5 + 1e-9) and psi0 <= PSI_BAR + 1e-9 \
                and (gamma - 1 - 1e-9 <= pc["log2xmin1"] <= gamma + PSI_BAR + 1e-9)
    lab = ("X0=%5d p=%2d n=%8d off=%5d/%-6d gamma=%8.4f eps*n=%7.4f g-eps*n=%6.4f c=%7d %s rho0-eps*n=%6.3f "
           "min@%d L7/Lam=%7.2f g-Gamma_rec=%7.3f" %
           (X0, p, n, off, N, gamma, epsn, gamma - epsn, m[-1], "bind" if bound else "deep",
            rho0 - epsn, pc["imin"], l7_rhs / Lam, gamma - rec_G))
    if Qmult != 1:
        lab = "(X') X0=%d: " % Qmult + lab
    check(allok, label + lab)
    if record:
        RUNS.append(res)
    return res, m, s, n, K, q


ALL_RUNS = []
for X0 in GRID_X0:
    glo = g_lo_of(X0)
    p1, N = p1_of_level(glo)
    p = p1
    while True:
        eps = (LF - 1) / (LF ** p - 1)
        nstar = (glo - LAM) / eps
        if nstar > NCAP:
            break
        r = run_one(X0, p)
        if r is not None:
            ALL_RUNS.append(r)
        p += 1

# every scale: higher levels at fixed X0
print("  -- higher levels (larger scales eps_p n) at fixed X0 --")
for X0, extra, plist in ((1, 2.0, (14, 18, 22)), (1, 5.0, (18, 22)), (100, 3.0, (24, 26)), (10, 6.0, (24,))):
    glo = g_lo_of(X0) + extra
    p1, N = p1_of_level(glo)
    for p in plist:
        if p < p1:
            continue
        eps = (LF - 1) / (LF ** p - 1)
        if (glo - LAM) / eps > NCAP:
            continue
        r = run_one(X0, p, level=glo, label="[level +%.0f] " % extra)
        if r is not None:
            ALL_RUNS.append(r)

# the stronger (X') condition a_r >= X0: caps with Q = X0 q, level log2 X0 + lam + 1
print("  -- the stronger condition (X'): X0 q <= R_r, construction with Q = X0 q --")
for X0, plist in ((2, (12, 16)), (16, (14, 18)), (100, (18, 22))):
    glo = math.log2(X0) + LAM + 1     # gamma_Q = gamma - log2 X0 >= eps n + lam at eps n ~ 1
    e1, e2 = arc_of(glo)
    N, k = N_of(e2 - e1)
    for p in plist:
        eps = (LF - 1) / (LF ** p - 1)
        nstar = int(math.floor(1 / eps))
        lo = e1 * (1 + 1e-11)
        hi = e2 * (1 - 1e-11)
        wit = None
        for off in range(4 * N):
            n = nstar - off
            di = delta_interval(n)
            if di and di[1] >= lo and di[2] <= hi:
                wit = n
                break
        if wit is None:
            print("  (X') X0=%d p=%d: no witness in 4N below 1/eps (window not certified here)" % (X0, p))
            continue
        n = wit
        three = 3 ** n
        K = three.bit_length()
        q = (1 << K) - three
        out = construct_B(p, n, K, q, Qmult=X0)
        if out is None:
            check(False, "(X') X0=%d p=%d n=%d construction runs" % (X0, p, n))
            continue
        m, s, bound, pow3T = out
        pc = full_profile_check(m, s, n, K, q, X0, Qmult=X0, def_all=(n <= 30000))
        gamma = pc["gamma"]
        epsn = eps * n
        check(pc["shape"] and pc["closes"] and pc["sizeQ"] and pc["thresh"] and pc.get("def_all", True)
              and gamma - math.log2(X0) >= epsn + LAM - 1e-9,
              "(X') X0=%3d p=%2d n=%7d: X0 q <= R_r at all rotations; gamma = %.4f = log2 X0 + eps n + %.4f"
              % (X0, p, n, gamma, gamma - math.log2(X0) - epsn))

# the window placed at the canonical scale n ~ L^p: gamma in [g, g+1] still, but eps_p n ~ 0.6,
# so this family tests SdW's Corollary 5 (Lambda < m/X0), not Lemma 7
print("  -- canonical scale: window [ceil(L^p), ceil(L^p) + N - 1] (Corollary 5 regime, not Lemma 7) --")
CANON = []
for X0, plist in ((100, (16, 20)), (1000, (22, 25)), (4096, (24, 27))):
    glo = g_lo_of(X0)
    e1, e2 = arc_of(glo)
    N, k = N_of(e2 - e1)
    for p in plist:
        ntop = int(math.ceil(LF ** p)) + N - 1
        r = run_one(X0, p, label="[canonical] ", ntop=ntop, record=False)
        if r is not None:
            CANON.append(r[0])
if CANON:
    print("    canonical runs: gamma - eps_p n in [%.3f, %.3f] (grows with log2 X0: Lemma 7 not sharp here)"
          % (min(r["gamma"] - r["epsn"] for r in CANON), max(r["gamma"] - r["epsn"] for r in CANON)))

nr = len(RUNS)
print()
print("  summary over %d threshold runs (Qmult = 1):" % nr)
if nr:
    gm = [r["gamma"] - r["epsn"] for r in RUNS]
    print("    gamma - eps_p n in [%.4f, %.4f]   (theorem: [lam, lam + 1.5] = [%.4f, %.4f])"
          % (min(gm), max(gm), LAM, LAM + 1.5))
    rx = [r["gamma"] - math.log2(r["X0"] + 1) for r in RUNS if r["X0"] >= 6 and not r["extra"]]
    if rx:
        print("    for X0 >= 6: gamma - log2(X0+1) in [%.4f, %.4f]   (theorem: [1, 2])" % (min(rx), max(rx)))
    print("    SdW Lemma 7 bound / actual Lambda in [%.3f, %.3f]; divided by p: [%.4f, %.4f]"
          % (min(r["l7ratio"] for r in RUNS), max(r["l7ratio"] for r in RUNS),
             min(r["l7ratio"] / r["p"] for r in RUNS), max(r["l7ratio"] / r["p"] for r in RUNS)))
    lx = [r["lx"] - r["epsn"] for r in RUNS if not r["extra"]]
    print("    log2(x_min+1) - eps_p n in [%.4f, %.4f]   (theorem: [lam - 1, lam + 1.5 + Psi_bar] = [%.4f, %.4f])"
          % (min(lx), max(lx), LAM - 1, LAM + 1.5 + PSI_BAR))
    print("    Psi_0 = log2(x_0+1) - gamma: max %.4f (Psi_bar %.4f); Rozier rho = m_0 at %d of %d runs"
          % (max(r["psi0"] for r in RUNS), PSI_BAR, sum(1 for r in RUNS if r["rho_is_m0"]), nr))
    deep = sum(1 for r in RUNS if not r["bound"])
    print("    deep crash (budget never binds): %d of %d runs; minimum element at block 0: %d of %d"
          % (deep, nr, sum(1 for r in RUNS if r["imin"] == 0), nr))
    print("    record's crash-depth-1 hypothesis (H1) gamma >= Gamma(p,n) fails at %d of %d runs"
          % (sum(1 for r in RUNS if r["gamma"] < r["recG"]), nr))


# ---------------------------------------------------------------------------
# Part G. Negative controls.
# ---------------------------------------------------------------------------

header("Part G. Negative controls")

# G1. necessity bites: n with gamma(n) < eps_p n - log2 p -> no size-passer; the construction fails
print("  G1. scale eps_p n ~ log2 p + 3, n with gamma(n) < eps_p n - log2 p: Construction B must not pass")
tot = 0
bad = 0
for p in range(8, 17):
    eps = (LF - 1) / (LF ** p - 1)
    target = (math.log2(p) + 3) / eps
    for n in range(int(target), int(target) + 400):
        di = delta_interval(n)
        if di is None:
            continue
        Kc, dlo, dhi = di
        gam = -math.log2(-math.expm1(-dlo * math.log(2)))   # an upper bound for gamma(n): gamma decreases in delta
        if not (gam < eps * n - math.log2(p) - 1e-6):
            continue
        three = 3 ** n
        K = three.bit_length()
        q = (1 << K) - three
        out = construct_B(p, n, K, q)
        tot += 1
        if out is None:
            continue
        m, s, bnd, _ = out
        Rs = [R_def(m, s, r) for r in range(p)]
        if all(q <= R for R in Rs):
            bad += 1
check(tot > 0 and bad == 0, "G1: %d such n at p = 8..16; Construction B passes at %d of them (theorem: 0)" % (tot, bad))

# G2. the gap region eps n - log2 p < gamma < eps n + lam: informational pass rate
tot = 0
passed = 0
for p in range(8, 17):
    eps = (LF - 1) / (LF ** p - 1)
    target = (math.log2(p) + 3) / eps
    for n in range(int(target), int(target) + 400):
        di = delta_interval(n)
        if di is None:
            continue
        Kc, dlo, dhi = di
        glow = -math.log2(-math.expm1(-dhi * math.log(2)))
        ghigh = -math.log2(-math.expm1(-dlo * math.log(2)))
        if not (glow > eps * n - math.log2(p) + 1e-6 and ghigh < eps * n + LAM - 1e-6):
            continue
        three = 3 ** n
        K = three.bit_length()
        q = (1 << K) - three
        out = construct_B(p, n, K, q)
        tot += 1
        if out is None:
            continue
        m, s, bnd, _ = out
        if all(q <= R_def(m, s, r) for r in range(p)):
            passed += 1
print("  G2. gap region eps n - log2 p < gamma < eps n + lam: Construction B passes at %d of %d n (informational;"
      " the hypothesis is sufficient, not necessary)" % (passed, tot))

# G3. the threshold demand is load-bearing: X0 = 1 witnesses tested against X0 = 1024
fails = 0
tested = 0
for r in list(RUNS):
    if r["X0"] != 1 or r["n"] > 200000 or r["extra"]:
        continue
    out = run_one(1, r["p"], record=False, label="[G3 rebuild] ")
    if out is None:
        continue
    _, m, s, n, K, q = out
    Rs, _c = R_all_recurrence(m, s, q, R_def(m, s, 0))
    tested += 1
    if not all((1024 + 1) * q <= (Rs[i] << m[i]) for i in range(len(m))):
        fails += 1
check(tested > 0 and fails == tested, "G3: X0 = 1 witnesses fail x_min >= 1024 at %d of %d (the X0 demand is load-bearing)"
      % (fails, tested))

# G4. caps are saturated: one or two extra units of depth on a climb block, taken from the
# crash, break a size condition (deep-crash runs only, where every climb block sits at its cap)
tested = 0
broke = 0
for r in list(RUNS):
    if r["n"] > 60000 or r["bound"] or r["extra"]:
        continue
    out = run_one(r["X0"], r["p"], record=False, label="[G4 rebuild] ")
    if out is None:
        continue
    _, m, s, n, K, q = out
    p = len(m)
    for j in range(p - 1):
        if m[p - 1] < 3:
            continue
        tested += 1
        for dlt in (1, 2):
            mm = list(m)
            mm[j] += dlt
            mm[p - 1] -= dlt
            if not all(q <= R_def(mm, s, rr) for rr in range(p)):
                broke += 1
                break
check(tested > 0 and broke == tested, "G4: +1 or +2 depth on any climb block (from the crash) breaks a size condition at %d of %d"
      % (broke, tested))

# G5. crash depth 1 is excluded at large scale. Arithmetic only (no construction): at
# p = p1(X0) and p1(X0) + 20, at the bottom of the theorem window (smallest eps_p n), compare
# the unit-block necessity bound (L-1)(n - L^{p-1})/(L^{p-1}-1) - log2 p (Proposition 12.8.7.1(iii))
# with the family's ceiling gamma <= g + 1. Where the bound exceeds the ceiling, no size-passer
# with a unit block (crash depth 1) exists at any gamma the family uses: the deep crash is forced.
print("  G5. unit-block necessity bound vs the family's gamma ceiling (window bottom), X0 = 2^j:")
print("      j    p   eps*n    ceiling g+1   unit-block bound   forced deep?")
first_forced = None
ok_pred = True
for j in list(range(4, 21, 2)) + list(range(30, 201, 10)):
    l2 = j + math.log2(1 + 2.0 ** (-j))
    glo = glo_big(l2)
    p1, N = p1_of_level(glo)
    for p in (p1, p1 + 20):
        eps = (LF - 1) / (LF ** p - 1)
        epsn = (glo - LAM) - eps * N - eps          # eps * (bottom of the window), from below
        n = epsn / eps
        Lp1 = LF ** (p - 1)
        ub = (LF - 1) * (n - Lp1) / (Lp1 - 1) - math.log2(p)
        forced = ub > glo + 1
        # the predicted criterion: (L-1) eps n > lam + 1.5 + (L-1) - ... ; recorded as
        # eps n > (lam + 2.09 + log2 p)/(L-1) up to the o(1) of L^p/(L^p - 1)
        pred = epsn > (LAM + 2.09 + math.log2(p)) / (LF - 1) + 0.05
        if pred and not forced:
            ok_pred = False
        if forced and first_forced is None:
            first_forced = (j, p)
        print("    %3d  %3d  %7.3f  %10.3f   %14.3f      %s" % (j, p, epsn, glo + 1, ub, "yes" if forced else "no"))
check(ok_pred, "G5: wherever eps n > (lam + 2.09 + log2 p)/(L-1), the unit-block bound exceeds the family's ceiling")
check(first_forced is not None and first_forced[0] <= 20,
      "G5: crash depth 1 is excluded at the family's gamma from X0 = 2^%d (p = %d) on in this table"
      % (first_forced[0], first_forced[1]) if first_forced else "G5: no forced row")

print()
print("=" * 76)
print("CHECKS: %d   FAILURES: %d" % (CHECKS, FAILS))
print("RESULT: " + ("ALL CHECKS PASS" if FAILS == 0 else "FAILURES PRESENT"))
