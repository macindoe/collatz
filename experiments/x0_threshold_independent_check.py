#!/usr/bin/env python3
"""
x0_threshold_independent_check.py -- independent numerical check of cycles.md 12.8.7
(the staircase at a size threshold X0), per AGENTS.md "Before marking anything proved".

Supports: cycles.md 12.8.7 (Prop 12.8.7.1, Thm 12.8.7.2, Cor 12.8.7.3, Thm 12.8.7.4 and the
p1 table, Remark 12.8.7.5).  Findings: briefs/x0-threshold-independent-check-findings.md.

Written from the text of cycles.md 12.1, 12.6.1, 12.8, 12.8.6.2 and 12.8.7 alone.  It imports
nothing from the repository and was written without reading experiments/staircase_x0_threshold.py
or its output.

Scope (README stopping rules): size-only.  No cycle search is run, no divisibility condition
q | R_r is ever tested, nothing is excluded.

Arithmetic: every pass/fail decision is an exact integer / Fraction comparison, or a comparison of
two rigorous dyadic intervals (fixed point, P bits, outward rounding; ln by atanh series with an
explicit tail bound, exp by Taylor series with an explicit tail bound).  An interval comparison
that cannot be decided raises Undecided; it never guesses.  log2(3) is enclosed from those series
and cross-certified against exact 3^b versus 2^a comparisons.

Reproduce (one command; deterministic; about 15 minutes):

    python experiments/x0_threshold_independent_check.py

It writes experiments/x0_threshold_independent_check_output.txt (ASCII) and prints the same text.
Exit status 0 iff every check passes and every negative control bites.
"""
import math
import os
import random
import sys
import time
from fractions import Fraction

P = 720            # fixed-point fraction bits of every interval
OUT = []
FAILS = []
NCHECK = [0]
T_START = time.time()


def out(line=""):
    OUT.append(line)
    print(line, flush=True)


def check(cond, label):
    NCHECK[0] += 1
    if not cond:
        FAILS.append(label)
        out("    FAIL: " + label)
    return cond


class Undecided(Exception):
    pass


# ---------------------------------------------------------------------------------------------
# Rigorous dyadic intervals [lo/2^P, hi/2^P]
# ---------------------------------------------------------------------------------------------

def _cdiv(a, b):           # ceil(a/b), b > 0
    return -((-a) // b)


class Iv:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi):
        if lo > hi:
            raise ValueError("bad interval")
        self.lo = lo
        self.hi = hi

    @staticmethod
    def of(x):
        if isinstance(x, Iv):
            return x
        x = Fraction(x)
        a, b = x.numerator, x.denominator
        return Iv((a << P) // b, _cdiv(a << P, b))

    def __add__(self, o):
        o = Iv.of(o)
        return Iv(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return Iv(-self.hi, -self.lo)

    def __sub__(self, o):
        o = Iv.of(o)
        return Iv(self.lo - o.hi, self.hi - o.lo)

    def __rsub__(self, o):
        return Iv.of(o) - self

    def __mul__(self, o):
        o = Iv.of(o)
        ps = (self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi)
        return Iv(min(ps) >> P, _cdiv(max(ps), 1 << P))

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = Iv.of(o)
        if o.lo <= 0 <= o.hi:
            raise Undecided("division by an interval containing 0")
        qs = [Fraction(a << P, b) for a in (self.lo, self.hi) for b in (o.lo, o.hi)]
        return Iv(math.floor(min(qs)), math.ceil(max(qs)))

    def __rtruediv__(self, o):
        return Iv.of(o) / self

    def width(self):
        return Fraction(self.hi - self.lo, 1 << P)

    def mid(self):
        return (self.lo + self.hi) / 2.0 / 2.0 ** P

    def __repr__(self):
        return "%.10f" % self.mid()


def lt(a, b):
    """certified a < b (True / False); raises if the enclosures overlap."""
    a, b = Iv.of(a), Iv.of(b)
    if a.hi < b.lo:
        return True
    if a.lo >= b.hi:
        return False
    raise Undecided("lt undecided")


def le(a, b):
    a, b = Iv.of(a), Iv.of(b)
    if a.hi <= b.lo:
        return True
    if a.lo > b.hi:
        return False
    raise Undecided("le undecided")


def imax(*xs):
    xs = [Iv.of(x) for x in xs]
    return Iv(max(x.lo for x in xs), max(x.hi for x in xs))


def atanh_frac(z):
    """atanh(z), z rational in [0, 1/2], as an interval."""
    z = Fraction(z)
    if z == 0:
        return Iv(0, 0)
    u, v = z.numerator, z.denominator
    W = P + 48
    lo_p = (u << W) // v
    hi_p = _cdiv(u << W, v)
    u2, v2 = u * u, v * v
    slo = shi = 0
    k = 0
    while True:
        d = 2 * k + 1
        slo += lo_p // d
        shi += _cdiv(hi_p, d)
        lo_p = (lo_p * u2) // v2
        hi_p = _cdiv(hi_p * u2, v2)
        k += 1
        if hi_p < (1 << 16):
            # tail sum_{j>=k} z^(2j+1)/(2j+1) <= z^(2k+1)/(1-z^2) <= (4/3) z^(2k+1)
            shi += _cdiv(4 * hi_p, 3) + 1
            break
    sh = W - P
    return Iv(slo >> sh, _cdiv(shi, 1 << sh))


LN2 = 2 * atanh_frac(Fraction(1, 3))
LN3 = LN2 + 2 * atanh_frac(Fraction(1, 5))       # ln 3 = ln 2 + ln(3/2), ln(3/2) = 2 atanh(1/5)
L = LN3 / LN2


def ln_frac(x):
    """ln of a positive rational of moderate size."""
    x = Fraction(x)
    if x <= 0:
        raise ValueError
    if x == 1:
        return Iv(0, 0)
    if x < 1:
        return -ln_frac(1 / x)
    e = x.numerator.bit_length() - x.denominator.bit_length()
    y = x / (Fraction(2) ** e)
    if y < 1:
        e -= 1
        y *= 2
    # 1 <= y < 2
    return LN2 * e + 2 * atanh_frac((y - 1) / (y + 1))


def _trunc(N):
    """positive integer N in [t*2^sh, (t+1)*2^sh] with t of about P+64 bits."""
    sh = max(0, N.bit_length() - (P + 64))
    t = N >> sh
    return t, sh, (t << sh) == N


def log2_pos(x):
    """log2 of a positive int or Fraction of any size, as an interval."""
    x = Fraction(x)
    a, b = x.numerator, x.denominator
    ta, sa, ea = _trunc(a)
    tb, sb, eb = _trunc(b)
    lo_r = Fraction(ta, tb + (0 if eb else 1))
    hi_r = Fraction(ta + (0 if ea else 1), tb)
    lo = ln_frac(lo_r) / LN2
    hi = ln_frac(hi_r) / LN2
    return Iv(lo.lo, hi.hi) + (sa - sb)


def ln_iv(x):
    x = Iv.of(x)
    if x.lo <= 0:
        raise Undecided("ln of nonpositive")
    a = ln_frac(Fraction(x.lo, 1 << P))
    b = ln_frac(Fraction(x.hi, 1 << P))
    return Iv(a.lo, b.hi)


def log2_iv(x):
    return ln_iv(x) / LN2


def _exp_series(y_lo, y_hi):
    """e^y for y in [y_lo, y_hi] (fixed point W bits), 0 <= y < 1; returns (lo, hi) at W."""
    W = P + 48
    one = 1 << W
    # lower
    t = one
    s = one
    j = 1
    while t > 0:
        t = (t * y_lo >> W) // j
        s += t
        j += 1
    lo = s
    t = one
    s = one
    j = 1
    while True:
        t = _cdiv(_cdiv(t * y_hi, one), j)
        s += t
        j += 1
        if t < (1 << 16) and j > 4:
            s += 2 * t + 1          # tail <= t * sum (y/j)^i <= 2t for y < 1, j >= 2
            break
    return lo, s


def exp2_frac(r):
    """2^r for rational r, as an interval."""
    r = Fraction(r)
    k = math.floor(r)
    f = r - k                              # [0, 1)
    y = LN2 * f                            # [0, 0.7)
    W = P + 48
    ylo = max(0, y.lo << 48)
    yhi = y.hi << 48
    lo, hi = _exp_series(ylo, yhi)
    sh = W - P
    lo >>= sh
    hi = _cdiv(hi, 1 << sh)
    if k >= 0:
        return Iv(lo << k, hi << k)
    return Iv(lo >> (-k), _cdiv(hi, 1 << (-k)))


def exp2_iv(x):
    x = Iv.of(x)
    a = exp2_frac(Fraction(x.lo, 1 << P))
    b = exp2_frac(Fraction(x.hi, 1 << P))
    return Iv(a.lo, b.hi)


def dfn(x):
    """delta(x) = -log2(1 - 2^(-x)), x > 0 (the involution of 12.8.7.4)."""
    return -log2_iv(1 - exp2_iv(-Iv.of(x)))


def Lpow(k):
    r = Iv.of(1)
    for _ in range(k):
        r = r * L
    return r


LM1 = L - 1
LAM = L / LM1 + Fraction(1, 2 ** 20)          # lambda


_EPS = {}
_LG = {}


def eps(p):
    if p not in _EPS:
        _EPS[p] = LM1 / (Lpow(p) - 1)
    return _EPS[p]


def lg_int(p):
    if p not in _LG:
        _LG[p] = log2_pos(p)
    return _LG[p]


# ---------------------------------------------------------------------------------------------
# Configurations: R_r (12.6.1), gamma, x_r (12.8.7)
# ---------------------------------------------------------------------------------------------

def R_direct(m, s, r):
    """12.6.1 by the definition: rotation order from block r; M_t = sum_{j>t} m_j,
    S_t = sum_{j<t} (s_j + m_{j+1}); R = sum_t 3^M_t 2^S_t (2^s_t - 1).  Evaluated by
    a forward Horner scheme H_t = H_{t-1} 3^{m_t} + 2^{S_t} (2^{s_t}-1)."""
    p = len(m)
    mm = m[r:] + m[:r]
    ss = s[r:] + s[:r]
    H = 0
    S = 0
    for t in range(p):
        if t > 0:
            S += ss[t - 1] + mm[t]
            H *= 3 ** mm[t]
        H += ((1 << ss[t]) - 1) << S
    return H


def R_direct_sum(m, s, r):
    """same, as the literal sum (small configurations only)."""
    p = len(m)
    mm = m[r:] + m[:r]
    ss = s[r:] + s[:r]
    tot = 0
    for t in range(p):
        M = sum(mm[t + 1:])
        S = sum(ss[j] + mm[j + 1] for j in range(t))
        tot += 3 ** M * 2 ** S * (2 ** ss[t] - 1)
    return tot


def all_R(m, s, q, big=False):
    """all p rotation numerators.  Small: direct at every rotation.  Big: direct Horner at
    r = 0 and r = p-1, the rest by the transport recurrence of 12.6.1.1 with an exact
    divisibility check, closed against the direct R_{p-1} and back to R_0."""
    p = len(m)
    if not big:
        return [R_direct(m, s, r) for r in range(p)]
    R0 = R_direct(m, s, 0)
    Rlast = R_direct(m, s, p - 1)
    Rs = [R0]
    for r in range(p - 1):
        sig = s[r] + m[(r + 1) % p]
        num = 3 ** m[r] * Rs[-1] + ((1 << s[r]) - 1) * q
        if num & ((1 << sig) - 1):
            raise AssertionError("transport recurrence: not divisible")
        Rs.append(num >> sig)
    if Rs[-1] != Rlast:
        raise AssertionError("transport recurrence disagrees with direct R_{p-1}")
    sig = s[p - 1] + m[0]
    num = 3 ** m[p - 1] * Rs[-1] + ((1 << s[p - 1]) - 1) * q
    if num & ((1 << sig) - 1) or (num >> sig) != R0:
        raise AssertionError("transport recurrence does not close at R_0")
    return Rs


def gamma_of_q(K, q):
    return K - log2_pos(q)


def delta_n(n):
    """delta(n) = ceil(nL) - nL, K = ceil(nL)."""
    nl = L * n
    K = nl.lo >> P
    if (nl.hi >> P) != K:
        raise Undecided("nL straddles an integer")
    return (K + 1) - nl, K + 1


# ---------------------------------------------------------------------------------------------
# Construction B (12.8.6.2), verbatim from the statement
# ---------------------------------------------------------------------------------------------

def construction_B(p, n):
    t3n = 3 ** n
    K = t3n.bit_length()            # ceil(nL)
    S = K - n
    q = (1 << K) - t3n
    if S < p:
        raise ValueError("S < p")
    sc = S - (p - 1)
    base = (1 << sc) - 1
    m = []
    T = 0
    p3T = 1
    binds = []
    caps = []
    for r in range(p - 1):
        X = (p3T * base) << (n - T + p - 1 - r)
        if X < q:
            raise AssertionError("cap_r undefined (X_r < q)")
        m0 = X.bit_length() - q.bit_length()
        cap = m0 if (q << m0) <= X else m0 - 1
        # cap = max{m >= 0 : q 2^m <= X}
        assert (q << cap) <= X < (q << (cap + 1))
        budget = n - 1 - T - (p - 2 - r)
        mr = min(cap, budget)
        binds.append(budget <= cap)
        caps.append(cap)
        m.append(mr)
        T += mr
        p3T *= 3 ** mr
    m.append(n - T)
    s = [1] * (p - 1) + [sc]
    return dict(m=m, s=s, K=K, S=S, q=q, n=n, p=p, sc=sc, binds=binds, caps=caps,
                Tlast=T)


def hyp(p, n, K, S, q):
    """gamma, eta, (H0), Gamma', Gamma, (H1'), (H1) as intervals / certified booleans."""
    gam = gamma_of_q(K, q)
    sc = S - (p - 1)
    eta = dfn(sc)
    H0 = (S >= p) and le(p + eta, LM1 * (n - p) + gam)
    Lp = Lpow(p)
    Lp1 = Lp / L
    Gp = 1 + eta + (Lp - L * L - LM1 * (p - 2) + LM1 * LM1 * n) / (LM1 * (Lp - 1))
    beta = 1 + eta
    G = ((n - 1) * LM1 * LM1 + Lp1 * (1 + beta * LM1) - (p - 2 + beta) * LM1 - L) \
        / (LM1 * (Lp1 - 1))
    H1p = le(imax(2 + eta, Gp), gam)
    H1 = le(imax(2 + eta, G), gam)
    return dict(gam=gam, eta=eta, H0=H0, Gp=Gp, G=G, H1p=H1p, H1=H1)


def rozier_max(m, start=0):
    """max_j (m_j - (L-1) M_{j-1}) in cyclic order from `start` (intervals)."""
    p = len(m)
    best = None
    M = 0
    for j in range(p):
        v = m[(start + j) % p] - LM1 * M
        best = v if best is None else imax(best, v)
        M += m[(start + j) % p]
    return best


# ---------------------------------------------------------------------------------------------
# Part 0: constants
# ---------------------------------------------------------------------------------------------

def part0():
    out("== Part 0: constants and the enclosure of L = log2 3 ==")
    out("  fixed point: P = %d bits; width(L) = 2^%.1f" % (P, math.log2(float(L.width()))))
    check(L.width() < Fraction(1, 2 ** (P - 12)), "L enclosure width")
    # cross-certify against exact 3^b vs 2^a at convergents (computed below) and random a/b
    cf = cont_frac_L()
    ok = True
    for (h, k) in cf[:16]:
        exact_gt = 3 ** k > 2 ** h          # L > h/k  iff 3^k > 2^h
        if exact_gt != lt(Fraction(h, k), L):
            ok = False
    rng = random.Random(7)
    for _ in range(300):
        b = rng.randint(1, 3000)
        a = rng.randint(b, 2 * b)
        if 3 ** b != 2 ** a:
            if (3 ** b > 2 ** a) != lt(Fraction(a, b), L):
                ok = False
    check(ok, "L enclosure vs exact 3^b vs 2^a (16 convergents, 300 random fractions)")
    # K = bitlength(3^n) = ceil(nL)
    ok = True
    for n in list(range(1, 3001)) + [rng.randint(3000, 4000000) for _ in range(40)]:
        _, K = delta_n(n)
        if (3 ** n).bit_length() != K:
            ok = False
    check(ok, "bitlength(3^n) = ceil(nL) for n <= 3000 and 40 random n <= 4e6")
    out("  L = %s, L/(L-1) = %.10f, lambda = %.10f" % (L, (L / LM1).mid(), LAM.mid()))
    check(lt(L / LM1, Fraction(27095114, 10 ** 7)) and lt(Fraction(27095112, 10 ** 7), L / LM1),
          "L/(L-1) = 2.7095113...")
    c = exp2_iv(-(LAM + Fraction(3, 2)))
    out("  2^-(lambda+1.5) = %.12f" % c.mid())
    check(lt(Fraction(54, 1000), c), "2^-(lambda+1.5) > 0.054")
    check(lt(Fraction(5405, 100000), c) and lt(c, Fraction(5406, 100000)),
          "2^-(lambda+1.5) = 0.05405...")
    check(lt(LAM, Fraction(271, 100)), "lambda <= 2.71 (so g+1 <= max(log2(X0+1), 2.71) + 2)")
    x = exp2_iv(LAM) - 1
    out("  2^lambda - 1 = %.8f  (threshold where g switches to 1+log2(X0+1))" % x.mid())
    out("  FINDING (minor): 2^lambda - 1 > 5.541, so the text's 'For X0 >= 5.541' should read X0 >= 5.5411:"
        " certified %s" % lt(Fraction(5541, 1000), x))
    check(lt(x, Fraction(55411, 10000)), "2^lambda - 1 <= 5.5411")
    out("  2L-3 = %.6f, 3(L-1)-1 = %.6f" % ((2 * L - 3).mid(), (3 * LM1 - 1).mid()))
    return cf


def cont_frac_L(nterms=140):
    """convergents (h_k, k_k) of L from the interval (common CF prefix of both ends)."""
    lo = Fraction(L.lo, 1 << P)
    hi = Fraction(L.hi, 1 << P)
    a_lo, a_hi = [], []
    for x, arr in ((lo, a_lo), (hi, a_hi)):
        for _ in range(nterms + 5):
            a = math.floor(x)
            arr.append(a)
            if x == a:
                break
            x = 1 / (x - a)
    pq = []
    hm1, h0 = 1, a_lo[0]
    km1, k0 = 0, 1
    pq.append((h0, k0))
    for i in range(1, min(len(a_lo), len(a_hi)) - 2):
        if a_lo[i] != a_hi[i]:
            break
        a = a_lo[i]
        hm1, h0 = h0, a * h0 + hm1
        km1, k0 = k0, a * k0 + km1
        pq.append((h0, k0))
        if len(pq) >= nterms:
            break
    return pq


# ---------------------------------------------------------------------------------------------
# Part 1: Prop 12.8.7.1 (i)-(iv) and Cor 12.8.7.3 on random configurations
# ---------------------------------------------------------------------------------------------

def x_plus_1(m, s, q, Rs):
    return [Fraction(R << m[r], q) for r, R in enumerate(Rs)]


def arc_sum(m, s, K, q, r):
    """2^gamma * sum over arcs A ending at block r-1 (incl. empty) of 2^w(A) (1 - 2^-s_t),
    t the block preceding the arc, written exactly: 2^gamma 2^w(A) = 3^m(A) 2^(K-m(A)-s(A))/q."""
    p = len(m)
    tot = Fraction(0)
    for ln in range(p):
        blocks = [(r - 1 - i) % p for i in range(ln)]
        mA = sum(m[b] for b in blocks)
        sA = sum(s[b] for b in blocks)
        t = (r - 1 - ln) % p
        tot += Fraction(3 ** mA * 2 ** (K - mA - sA), q) * (1 - Fraction(1, 2 ** s[t]))
    return tot


def check_config(m, s, stats, X0s=()):
    """all of 12.8.7.1 / 12.8.7.3 on one configuration (q > 0 required)."""
    p = len(m)
    n = sum(m)
    K = n + sum(s)
    q = (1 << K) - 3 ** n
    assert q > 0
    Rs = all_R(m, s, q)
    if p <= 4 and n <= 40 and stats["lit"] < 3000:
        stats["lit"] += 1
        if [R_direct_sum(m, s, r) for r in range(p)] != Rs:
            stats["fail"].append(("R literal", m, s))
    S_pass = all(q <= R for R in Rs)
    xp1 = x_plus_1(m, s, q, Rs)
    # (i) dictionary, every rotation
    for r in range(p):
        if arc_sum(m, s, K, q, r) != xp1[r]:
            stats["fail"].append(("(i) identity", m, s, r))
    xmin1 = min(xp1)
    # gamma - 1 <= log2(xmin+1)  <=>  2^(K-1) <= q (xmin+1)
    if not (Fraction(2 ** (K - 1)) <= q * xmin1):
        stats["fail"].append(("(i) lower", m, s))
    # log2(xmin+1) < gamma + log2 p  <=>  q (xmin+1) < p 2^K
    if not (q * xmin1 < p * 2 ** K):
        stats["fail"].append(("(i) upper", m, s))
    # the argmin rotation r0 = j* mod p has every term < 2^gamma
    W = [Iv.of(0)]
    for j in range(p):
        W.append(W[-1] + LM1 * m[j] - s[j])
    jstar = 1
    for j in range(2, p + 1):
        if lt(W[j], W[jstar]):
            jstar = j
    r0 = jstar % p
    for ln in range(p):
        blocks = [(r0 - 1 - i) % p for i in range(ln)]
        mA = sum(m[b] for b in blocks)
        sA = sum(s[b] for b in blocks)
        t = (r0 - 1 - ln) % p
        # term/2^gamma = 2^w(A)(1-2^-s_t) < 1  <=>  3^mA 2^(K-mA-sA)(1-2^-s_t) < 2^K
        if not (Fraction(3 ** mA * 2 ** (K - mA - sA)) * (1 - Fraction(1, 2 ** s[t])) < 2 ** K):
            stats["fail"].append(("(i) r0 term", m, s))
    stats["n"] += 1
    lg = lg_int(p)
    e = eps(p) * n
    # (iv) Rozier minimax at every cyclic start, on these integers (p = 1: equality, eps_1 = 1)
    for st in (range(p) if p > 1 else []):
        if not le(e, rozier_max(m, st)):
            stats["fail"].append(("(iv)", m, st))
    if S_pass:
        stats["S"] += 1
        gam = gamma_of_q(K, q)
        # (ii) the trim
        if not lt(e, gam + lg):
            stats["fail"].append(("(ii)", m, s))
        # (iii) unit block
        if p >= 2 and 1 in m:
            stats["unit"] += 1
            Lp1 = Lpow(p - 1)
            rhs = LM1 * (n - Lp1) / (Lp1 - 1)
            if not lt(rhs, gam + lg):
                stats["fail"].append(("(iii)", m, s))
        # Cor 12.8.7.3 necessity / consequence of 12.8.7.1, for (S)+(X) with X0 <= x_min
        for X0 in X0s:
            if (X0 + 1) * q <= min(R << m[r] for r, R in enumerate(Rs)):
                stats["SX"] += 1
                rhs = imax(e, log2_pos(X0 + 1)) - lg
                if not lt(rhs, gam):
                    stats["fail"].append(("Cor 12.8.7.3 necessity", m, s, X0))
    # "gamma >= log2(X0+1) + 1 forces x_min >= X0", at the largest such integer X0
    X0 = (2 ** (K - 1)) // q - 1
    if X0 >= 1:
        stats["Xforce"] += 1
        if not ((X0 + 1) * q <= min(R << m[r] for r, R in enumerate(Rs))):
            stats["fail"].append(("gamma>=log2(X0+1)+1 forces (X)", m, s))
        # negative control: with the "+1" dropped, X0' = floor(2^gamma) - 1
        X0b = (2 ** K) // q - 1
        if (X0b + 1) * q > min(R << m[r] for r, R in enumerate(Rs)):
            stats["nc_plus1"] += 1
    return S_pass


def rand_configs(rng, count):
    """three generators: uniform; staircase-shaped near K = ceil(nL); tiny p=2."""
    res = []
    while len(res) < count:
        kind = rng.random()
        if kind < 0.35:
            p = rng.randint(1, 8)
            m = [rng.randint(1, 14) for _ in range(p)]
            s = [rng.randint(1, 5) for _ in range(p)]
        else:
            p = rng.randint(2, 9)
            m = [rng.randint(1, 5)]
            for _ in range(p - 2):
                m.append(max(1, int(m[-1] * 1.585 * rng.uniform(0.75, 1.3)) + rng.randint(-1, 2)))
            m.append(rng.choice([1, 1, 2, rng.randint(1, 3 * m[-1] + 1)]))
            if rng.random() < 0.3:
                k = rng.randint(0, p - 1)
                m = m[k:] + m[:k]
            n = sum(m)
            K = math.ceil(float(n) * 1.584962500721156) + rng.choice([0, 0, 0, 0, 1, -1])
            if (3 ** n).bit_length() > K:
                K = (3 ** n).bit_length()
            S = K - n
            if S < p:
                continue
            s = [1] * p
            if rng.random() < 0.3:
                for _ in range(rng.randint(1, 2)):
                    s[rng.randrange(p)] += 1
            rest = S - sum(s)
            if rest < 0:
                continue
            c = (m.index(max(m)) + 1) % p if rng.random() < 0.2 else rng.randrange(p)
            s[c] += rest
        n = sum(m)
        K = n + sum(s)
        if (1 << K) <= 3 ** n:
            continue
        res.append((m, s))
    return res


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def part1():
    out("")
    out("== Part 1: Prop 12.8.7.1 (i)-(iv) and Cor 12.8.7.3 necessity ==")
    rng = random.Random(20261019)
    stats = dict(n=0, S=0, unit=0, SX=0, Xforce=0, nc_plus1=0, lit=0, fail=[])
    X0s = (1, 2, 3, 5, 10, 30, 100, 1000)
    # exhaustive: p <= 4, K = ceil(nL) and ceil(nL)+1, n <= 13
    ex = 0
    for p in range(1, 5):
        for n in range(p, 14):
            for Kx in (0, 1):
                K = (3 ** n).bit_length() + Kx
                S = K - n
                if S < p:
                    continue
                for m in compositions(n, p):
                    for s in compositions(S, p):
                        check_config(list(m), list(s), stats, X0s)
                        ex += 1
    out("  exhaustive grid: p <= 4, n <= 13, K in {ceil(nL), ceil(nL)+1}, all (m, s): %d configs" % ex)
    exS = stats["S"]
    out("    of which size-passers (S): %d" % exS)
    cfgs = rand_configs(rng, 30000)
    for m, s in cfgs:
        check_config(m, s, stats, X0s)
    out("  random: 30,000 configurations, p <= 9 (seed 20261019); size-passers %d" % (stats["S"] - exS))
    out("  totals: %d configurations, %d size-passers, %d with a unit block, %d (S)+(X) pairs,"
        % (stats["n"], stats["S"], stats["unit"], stats["SX"]))
    out("          %d forced-(X) instances, %d literal-sum R cross-checks" % (stats["Xforce"], stats["lit"]))
    check(not stats["fail"], "Prop 12.8.7.1 (i)-(iv), Cor 12.8.7.3 necessity: failures %s"
          % (stats["fail"][:3],))
    out("  (i) identity at every rotation, (i) bounds, r0 terms, (iv) at every start: 0 failures"
        if not stats["fail"] else "  failures: %d" % len(stats["fail"]))
    out("  NEGATIVE CONTROL (X) with the +1 dropped (X0 = floor(2^gamma) - 1): x_min < X0 at %d of %d"
        % (stats["nc_plus1"], stats["Xforce"]))
    check(stats["nc_plus1"] > 0, "NC: gamma >= log2(X0+1) alone does not force (X)")
    # (iv) on random positive rationals
    bad = 0
    for _ in range(3000):
        p = rng.randint(2, 12)
        ms = [Fraction(rng.randint(1, 10 ** 6), rng.randint(1, 1000)) for _ in range(p)]
        e = eps(p) * sum(ms)
        for st in range(p):
            if not le(e, rozier_max(ms, st)):
                bad += 1
    check(bad == 0, "(iv) on 3000 random positive-rational cyclic sequences, every start")
    out("  (iv) on 3,000 random positive-rational sequences (p <= 12), every cyclic start: %d failures" % bad)
    # (iv) extremal: m_j = c L^(j-1) (j=1..p-1), m_0 = c/(L-1)-ish ... real extremal attains equality
    # negative control: (iv) with eps_p replaced by L*eps_p fails on the real extremal
    p = 8
    ms = [Lpow(j) for j in range(p)]          # Rozier's m_j = c L^(j-1), j = 1..p, at c = 1
    tot = ms[0]
    for x in ms[1:]:
        tot = tot + x
    rz = rozier_max(ms, 0)
    eqgap = rz - eps(p) * tot
    out("  real extremal m_j = L^j (j = 0..7): max_j(...) - eps_p n = %.3e" % eqgap.mid())
    check(abs(eqgap.mid()) < 1e-100, "(iv) attained with equality by the geometric extremal")
    check(lt(rz, L * eps(p) * tot), "NC: (iv) with L*eps_p fails on the extremal")
    return stats


# ---------------------------------------------------------------------------------------------
# Part 2: Thm 12.8.7.2 on a (p, n) grid; algebra of its proof
# ---------------------------------------------------------------------------------------------

def check_B(p, n, X0=None, big=False, tag=""):
    """run Construction B at (p, n); verify every conclusion of Thm 12.8.7.2.
    Returns the record dict (with flags) or raises."""
    C = construction_B(p, n)
    m, s, K, S, q = C["m"], C["s"], C["K"], C["S"], C["q"]
    H = hyp(p, n, K, S, q)
    gam, eta = H["gam"], H["eta"]
    rec = dict(C)
    rec.update(H)
    res = {}
    res["entries"] = all(x >= 1 for x in m) and all(x >= 1 for x in s)
    res["sum_m"] = sum(m) == n and sum(s) + n == K
    c = n - C["Tlast"]
    rec["c"] = c
    res["crash>=1"] = c >= 1 and c == m[-1]
    Rs = all_R(m, s, q, big=big)
    res["S_all"] = all(q <= R for R in Rs)
    rz = rozier_max(m, 0)
    # max_j (m_j - (L-1) T_{j-1}) = m_0 : the max equals the j=0 term exactly
    others = [m[j] - LM1 * sum(m[:j]) for j in range(1, p)]
    res["rozier=m0"] = all(lt(o, m[0]) for o in others)
    res["m0<=gamma-eta"] = le(m[0], gam - eta)
    # (H0) / (H1') / (H1) and the deep-crash labelling
    rec["xp1"] = [Fraction(R << m[r], q) for r, R in enumerate(Rs)]
    xmin1 = min(rec["xp1"])
    rec["xmin1"] = xmin1
    if X0 is None:
        X0 = (2 ** (K - 1)) // q - 1            # largest X0 with log2(X0+1)+1 <= gamma
    rec["X0"] = X0
    if X0 >= 1 and (X0 + 1) * 2 * q <= 2 ** K:
        res["X"] = all((X0 + 1) * q <= (R << m[r]) for r, R in enumerate(Rs))
    rec["res"] = res
    rec["Rs"] = Rs
    rec["unit_block"] = 1 in m
    rec["ever_binds"] = any(C["binds"])
    return rec


def proof_algebra():
    """polynomial identities in the proof of 12.8.7.2, checked with exact rationals substituted
    for L, gamma, eta, n, p (they are identities in those symbols)."""
    rng = random.Random(5)
    ok = True
    for _ in range(200):
        Lr = Fraction(rng.randint(11, 30), 10)
        g = Fraction(rng.randint(-50, 400), 7)
        et = Fraction(rng.randint(0, 100), 997)
        b = 1 + et
        p = rng.randint(2, 30)
        n = rng.randint(1, 10 ** 6)
        A = [None] * (p - 1)
        prev = Fraction(0)
        for r in range(p - 1):
            prev = Lr * prev + g - r - b
            A[r] = prev
            cf = (Lr ** (r + 1) * ((g - b) * (Lr - 1) - 1) + (r + b - g) * (Lr - 1) + Lr) / (Lr - 1) ** 2
            if cf != prev:
                ok = False
        Gp = 1 + et + (Lr ** p - Lr ** 2 - (Lr - 1) * (p - 2) + (Lr - 1) ** 2 * n) / ((Lr - 1) * (Lr ** p - 1))
        lhs = Lr * A[p - 2] - (n + p - 1 - g + et)
        rhs = (Lr - 1) * (Lr ** p - 1) / (Lr - 1) ** 2 * (g - Gp)
        if lhs != rhs:
            ok = False
        # Gamma'_0(p) < L/(L-1)
        G0 = 1 + (Lr ** p - Lr ** 2 - (Lr - 1) * (p - 2)) / ((Lr - 1) * (Lr ** p - 1))
        if not G0 < Lr / (Lr - 1):
            ok = False
        epsr = (Lr - 1) / (Lr ** p - 1)
        if Gp != epsr * n + G0 + et:
            ok = False
    return ok


def part2():
    out("")
    out("== Part 2: Thm 12.8.7.2 (Construction B under (H1')) ==")
    ok = proof_algebra()
    check(ok, "proof algebra: closed form of A_r, the clearing identity "
              "L A_(p-2) - (n+p-1-gamma+eta) = (L^p-1)/(L-1) (gamma - Gamma'), "
              "Gamma' = eps_p n + Gamma'_0 + eta, Gamma'_0 < L/(L-1)")
    out("  proof algebra (200 exact-rational substitutions): %s" % ("ok" if ok else "FAIL"))
    rng = random.Random(8128)
    grid = []
    # candidate selection only (floats choose WHICH n to test; every decision below is certified):
    # per p, n in [3p+40, 40000]; keep n whose float gamma is within 0.5 of Gamma'(p,n) or above,
    # then sample up to 24 of them (half from below Gamma(p,n) when available), plus 8 random n.
    Lf = 1.584962500721156
    for p in range(2, 25):
        lo = 3 * p + 40
        Lpf = Lf ** p
        cand_hi, cand_lo = [], []
        for n in range(lo, 40001):
            d = math.ceil(n * Lf) - n * Lf
            if d <= 1e-9:
                continue
            gf = -math.log2(1 - 2.0 ** (-d))
            gpf = 1 + ((Lpf - Lf * Lf - (Lf - 1) * (p - 2) + (Lf - 1) ** 2 * n)
                       / ((Lf - 1) * (Lpf - 1)))
            Lp1f = Lpf / Lf
            gff = ((n - 1) * (Lf - 1) ** 2 + Lp1f * (1 + (Lf - 1)) - (p - 1) * (Lf - 1) - Lf) \
                / ((Lf - 1) * (Lp1f - 1)) if p > 1 else 0
            if gf >= gpf - 0.5:
                (cand_lo if gf < gff else cand_hi).append(n)
        pick = set(rng.sample(cand_lo, min(12, len(cand_lo))))
        pick |= set(rng.sample(cand_hi, min(24 - len(pick), len(cand_hi))))
        for _ in range(8):
            pick.add(rng.randint(lo, 40000))
        grid += [(p, n) for n in sorted(pick)]
    tally = dict(tried=0, hyp=0, deep=0, unit=0, H1=0, Xtested=0, binds_below_G=0,
                 below_G=0, c1_below_G=0)
    fails = []
    nc_trim = dict(tried=0, failed=0)
    for (p, n) in grid:
        tally["tried"] += 1
        t3n = 3 ** n
        K = t3n.bit_length()
        S = K - n
        q = (1 << K) - t3n
        if S < p:
            continue
        H = hyp(p, n, K, S, q)
        lg = log2_pos(p)
        # negative control: trim-forbidden n (gamma + log2 p <= eps_p n) -> (S) must fail
        if le(H["gam"] + lg, eps(p) * n):
            nc_trim["tried"] += 1
            try:
                rec = check_B(p, n)
                if not rec["res"]["S_all"]:
                    nc_trim["failed"] += 1
            except AssertionError:
                nc_trim["failed"] += 1
            continue
        if not (H["H0"] and H["H1p"]):
            continue
        tally["hyp"] += 1
        rec = check_B(p, n)
        r = rec["res"]
        for k, v in r.items():
            if not v:
                fails.append((p, n, k))
        if "X" in r:
            tally["Xtested"] += 1
        if rec["c"] > 1:
            tally["deep"] += 1
        else:
            tally["unit"] += 1
        if rec["H1"]:
            tally["H1"] += 1
            if rec["c"] != 1:
                fails.append((p, n, "12.8.6.2: (H1) but crash depth != 1"))
        if lt(rec["gam"], rec["G"]):
            tally["below_G"] += 1
            if rec["ever_binds"]:
                tally["binds_below_G"] += 1
            if rec["c"] == 1:
                tally["c1_below_G"] += 1
    out("  grid: p = 2..24, n in [3p+40, 40000], up to 24 near/above-(H1') n plus 8 random n per p"
        " (seed 8128): %d points" % tally["tried"])
    out("  meeting (H0) and (H1'): %d; deep crash (c > 1): %d; unit crash: %d; also (H1): %d"
        % (tally["hyp"], tally["deep"], tally["unit"], tally["H1"]))
    out("  (X) tested at X0 = floor(2^(K-1)/q) - 1 (largest with gamma >= log2(X0+1)+1): %d" % tally["Xtested"])
    check(not fails, "Thm 12.8.7.2 conclusions on the grid: %s" % (fails[:4],))
    out("  entries >= 1, sum m = n, crash depth >= 1, (S) at all p rotations, Rozier max = m_0 <= gamma - eta,"
        " (X): %d failures" % len(fails))
    out("  'the deep crash' paragraph ('where gamma < Gamma(p,n), the budget never binds and c is large'):")
    out("    of %d points with (H0), (H1') and gamma < Gamma(p,n): budget reached (budget <= cap at some r) at %d,"
        " crash depth c = 1 at %d" % (tally["below_G"], tally["binds_below_G"], tally["c1_below_G"]))
    out("  NEGATIVE CONTROL: trim-forbidden n (gamma + log2 p <= eps_p n): %d tried, (S) fails at %d"
        % (nc_trim["tried"], nc_trim["failed"]))
    check(nc_trim["tried"] > 0 and nc_trim["failed"] == nc_trim["tried"],
          "NC: Construction B fails (S) wherever the trim forbids")
    return tally


# ---------------------------------------------------------------------------------------------
# Part 3: Thm 12.8.7.4 -- sweep, p1 table, windows, Construction B end to end
# ---------------------------------------------------------------------------------------------

def gval(X0):
    X0 = Fraction(X0)
    lx = log2_pos(X0 + 1)
    if lt(lx, LAM):
        return 1 + LAM, False
    return 1 + lx, True


def arc_for(X0):
    """[delta(g+1), delta(g)] and ell; at g = 1 + log2(X0+1) both are logs of rationals."""
    g, is_log = gval(X0)
    if is_log:
        X0 = Fraction(X0)
        top = -log2_pos(1 - Fraction(1, 2 * (X0 + 1)))
        bot = -log2_pos(1 - Fraction(1, 4 * (X0 + 1)))
    else:
        top = dfn(g)
        bot = dfn(g + 1)
    return g, bot, top, top - bot


def thetas(cf):
    res = []
    for (h, k) in cf:
        x = k * L - h
        if x.lo > 0:
            res.append(x)
        elif x.hi < 0:
            res.append(-x)
        else:
            raise Undecided("theta sign")
    return res


def N_for(ell, cf, th):
    for k in range(1, len(cf)):
        if le(th[k - 1], ell):
            return cf[k][1] + cf[k - 1][1], k
    raise RuntimeError("CF too short")


def p1_for(N):
    p = 2
    while True:
        lhs = (Lpow(p) - 1) / (2 * LM1)
        if le(max(N, 3 * p + 40), lhs):
            return p
        p += 1


def part3_table(cf):
    out("")
    out("== Part 3a: the p1(X0) table (Thm 12.8.7.4 definitions, CF of L) ==")
    th = thetas(cf)
    out("  CF denominators: %s ..." % [k for (_, k) in cf[:16]])
    rows = {}
    def row(X0, label):
        g, bot, top, ell = arc_for(X0)
        N, k = N_for(ell, cf, th)
        p1 = p1_for(N)
        # log_L X0 = log2 X0 / log2 L
        logL = log2_pos(Fraction(X0)) / log2_iv(L) if X0 != 1 else Iv.of(0)
        rows[label] = dict(X0=X0, g=g, ell=ell, N=N, k=k, p1=p1, logL=logL)
        return rows[label]
    named = [(1, "1"), (2, "2"), (5, "5"), (6, "6"), (16, "16"), (17, "17"), (2 ** 8, "2^8"),
             (2 ** 12, "2^12"), (2 ** 20, "2^20"), (2 ** 60, "2^60"), (5 * 2 ** 60, "5*2^60"),
             (2 ** 71, "2^71"), (2 ** 200, "2^200")]
    out("  %-8s %-10s %-12s %-4s %-26s %-4s %s" % ("X0", "g", "ell", "k", "N", "p1", "p1 - log_L X0"))
    for X0, lab in named:
        r = row(X0, lab)
        out("  %-8s %-10.5f %-12.5e %-4d %-26d %-4d %.4f" % (lab, r["g"].mid(), r["ell"].mid(), r["k"],
                                                           r["N"], r["p1"], (r["p1"] - r["logL"]).mid()))
    claims = [("1", 10), ("16", 10), ("2^8", 22), ("2^12", 22), ("2^20", 36), ("2^60", 94),
              ("5*2^60", 98), ("2^71", 110), ("2^200", 309)]
    for lab, v in claims:
        check(rows[lab]["p1"] == v, "p1(%s) = %d (got %d)" % (lab, v, rows[lab]["p1"]))
    # integer sweep X0 = 1..16 and 2^8..2^12 at powers / endpoints
    allten = all(row(X0, "i%d" % X0)["p1"] == 10 for X0 in range(1, 17))
    check(allten, "p1 = 10 for every integer 1 <= X0 <= 16")
    mid22 = all(row(2 ** j, "j%d" % j)["p1"] == 22 for j in range(8, 13))
    check(mid22, "p1 = 22 at X0 = 2^8..2^12")
    # monotonicity of ell in g underpins 'for X0 <= 16' over reals: check ell(g) decreasing on a grid
    prev = None
    mono = True
    for X0 in [Fraction(k, 4) for k in range(4, 70)]:
        _, _, _, ell = arc_for(X0)
        same = prev is not None and (ell.lo, ell.hi) == (prev.lo, prev.hi)
        if prev is not None and not same and not le(ell, prev):
            mono = False
        prev = ell
    check(mono, "ell decreasing in X0 on X0 = 1, 1.25, ..., 17.25")
    # X0 = 2^j, j <= 200
    diffs = []
    p1s = []
    for j in range(0, 201):
        r = row(2 ** j, "pow%d" % j)
        p1s.append(r["p1"])
        diffs.append(((r["p1"] - r["logL"]).mid(), j))
    dl = [d for d, j in diffs]
    out("  X0 = 2^j, j = 0..200: p1 - log_L X0 in [%.4f, %.4f] (min at j=%d, max at j=%d)"
        % (min(dl), max(dl), min(diffs)[1], max(diffs)[1]))
    dl1 = [d for d, j in diffs if j >= 1]
    out("                         over j = 1..200: [%.4f, %.4f]" % (min(dl1), max(dl1)))
    named_d = [(rows[l]["p1"] - rows[l]["logL"]).mid() for _, l in named if l != "1"]
    out("  over the named rows other than X0 = 1: [%.4f, %.4f]" % (min(named_d), max(named_d)))
    check(all(p1s[i] <= p1s[i + 1] for i in range(len(p1s) - 1)), "p1(2^j) nondecreasing in j")
    return rows, th


def three_distance(cf, th):
    """direct enumeration: for N = q_k + q_{k-1} the points {-jL mod 1}, j < N, have exactly the
    gaps theta_(k-1) and theta_k; maximal gap theta_(k-1)."""
    ok = True
    reach = 0
    for k in range(1, len(cf)):
        N = cf[k][1] + cf[k - 1][1]
        if N > 400000:
            break
        one = 1 << P
        pts = []
        for j in range(N):
            x = -(L * j)
            lo = x.lo % one
            hi = lo + (x.hi - x.lo)
            if hi >= one:
                raise Undecided("point straddles 0")
            pts.append((lo, hi))
        pts.sort()
        a, b = th[k - 1], th[k]
        for i in range(N):
            lo1, hi1 = pts[i]
            lo2, hi2 = pts[(i + 1) % N]
            if i == N - 1:
                lo2 += one
                hi2 += one
            if lo2 <= hi1:
                raise Undecided("points overlap")
            gap = Iv(lo2 - hi1, hi2 - lo1)
            ga = not (gap.hi < a.lo or gap.lo > a.hi)
            gb = not (gap.hi < b.lo or gap.lo > b.hi)
            if not (ga or gb):
                ok = False
            if gap.lo > a.hi:            # certainly larger than theta_(k-1)
                ok = False
            if ga and gb and not (a.hi < b.lo or b.hi < a.lo):
                raise Undecided("theta_(k-1), theta_k not separated")
        reach = k
    return ok, reach


def longest_miss_runs(arcs, nmax):
    """brute force over n = 1..nmax: longest run of consecutive n with delta(n) outside each arc.
    delta(n) = ceil(nL) - nL at 128-bit fixed point with a certified error bound."""
    B = 160
    Llo = L.lo >> (P - B)
    Lhi = _cdiv(L.hi, 1 << (P - B))
    one = 1 << B
    ar = []
    for (bot, top) in arcs:
        ar.append((_cdiv(bot.hi, 1 << (P - B)) + 1, (top.lo >> (P - B)) - 1,
                   bot.lo >> (P - B), _cdiv(top.hi, 1 << (P - B))))
    runs = [0] * len(arcs)
    best = [0] * len(arcs)
    xlo = 0
    xhi = 0
    for n in range(1, nmax + 1):
        xlo += Llo
        xhi += Lhi
        K = xlo // one + 1
        if xhi // one + 1 != K:
            raise Undecided("nL straddles integer")
        dlo = K * one - xhi
        dhi = K * one - xlo
        for i, (in_lo, in_hi, out_lo, out_hi) in enumerate(ar):
            if dlo >= in_lo and dhi <= in_hi:
                inside = True
            elif dhi < out_lo or dlo > out_hi:
                inside = False
            else:
                raise Undecided("arc membership undecided at n=%d" % n)
            if inside:
                runs[i] = 0
            else:
                runs[i] += 1
                if runs[i] > best[i]:
                    best[i] = runs[i]
    return best


def find_window_n(p, X0, bot, top, N, g):
    """the top window [n*-N+1, n*]: all n with gamma(n) in [g, g+1], i.e. delta(n) in [bot, top]."""
    e = eps(p)
    nstar_iv = (g - LAM) / e
    nstar = nstar_iv.lo >> P
    if (nstar_iv.hi >> P) != nstar:
        raise Undecided("n* undecided")
    hits = []
    for n in range(nstar - N + 1, nstar + 1):
        d, K = delta_n(n)
        if le(bot, d) and le(d, top):
            hits.append(n)
    return nstar, hits


def part3_windows(rows, cf, th):
    out("")
    out("== Part 3b: the sweep (two-distance case) and brute-force miss runs ==")
    ok, reach = three_distance(cf, th)
    check(ok, "two-distance structure at N = q_k + q_(k-1)")
    out("  N = q_k + q_(k-1) points {-jL}: gaps are exactly theta_(k-1) or theta_k, max theta_(k-1);"
        " enumerated for k = 1..%d (N up to %d): %s" % (reach, cf[reach][1] + cf[reach - 1][1],
                                                      "ok" if ok else "FAIL"))
    labs = ["1", "16", "2^8", "2^12"]
    arcs = []
    for lab in labs:
        g, bot, top, ell = arc_for(rows[lab]["X0"])
        arcs.append((bot, top))
    nmax = 3000000
    best = longest_miss_runs(arcs, nmax)
    for lab, b in zip(labs, best):
        out("  X0 = %-5s: longest run of consecutive n <= %d with gamma(n) outside [g, g+1]: %d"
            " (sweep bound N - 1 = %d)" % (lab, nmax, b, rows[lab]["N"] - 1))
        check(b <= rows[lab]["N"] - 1, "miss run <= N-1 at X0=%s" % lab)
    # negative control: one CF level down (N' from theta_(k-2)) is too short somewhere
    nc = 0
    for lab, b in zip(labs, best):
        k = rows[lab]["k"]
        Nprev = cf[k - 1][1] + cf[k - 2][1]
        if b >= Nprev:
            nc += 1
        out("  NEGATIVE CONTROL X0 = %-5s: previous level N' = %d; a run of %d misses exists: %s"
            % (lab, Nprev, b, "bites" if b >= Nprev else "does not bite"))
    check(nc >= 3, "NC: the previous CF level's N' is too short (at least 3 of 4 arcs)")

    out("")
    out("== Part 3c: Thm 12.8.7.4 end to end: top windows [n*-N+1, n*], Construction B ==")
    grid = []
    for X0, pmax in ((1, 27), (2, 24), (5, 24), (6, 24), (16, 26), (100, 24), (256, 25), (1000, 24),
                     (4096, 24)):
        g, bot, top, ell = arc_for(X0)
        N, k = N_for(ell, cf, th)
        p1 = p1_for(N)
        for p in range(p1, pmax + 1):
            grid.append((X0, p, g, bot, top, N))
    tally = dict(windows=0, inst=0, empty=0, deep=0, unit_block=0)
    fails = []
    mins = dict(gm_e=[], gm_lx=[], up=[], lam=[])
    for (X0, p, g, bot, top, N) in grid:
        nstar, hits = find_window_n(p, X0, bot, top, N, g)
        tally["windows"] += 1
        if not hits:
            tally["empty"] += 1
            fails.append((X0, p, "empty window"))
            continue
        nlo = nstar - N + 1
        if not nlo >= 3 * p + 40:
            fails.append((X0, p, "window bottom < 3p+40"))
        sel = hits if (nstar < 200000) else [hits[-1]]
        for n in sel:
            rec = check_B(p, n, X0=X0, big=(n > 200000))
            tally["inst"] += 1
            r = rec["res"]
            gam, eta = rec["gam"], rec["eta"]
            e = eps(p) * n
            conds = dict(r)
            conds["H0"] = rec["H0"]
            conds["H1'"] = rec["H1p"]
            conds["eta<=2^-20"] = le(eta, Fraction(1, 2 ** 20))
            conds["X"] = all((X0 + 1) * rec["q"] <= (R << rec["m"][i])
                             for i, R in enumerate(rec["Rs"]))
            conds["X_direct"] = min(rec["xp1"]) >= X0 + 1
            conds["g<=gam<=g+1"] = le(g, gam) and le(gam, g + 1)
            conds["lam<=gam-eps n<=lam+1.5"] = le(LAM, gam - e) and le(gam - e, LAM + Fraction(3, 2))
            conds["eps n<=m0<=gam"] = le(e, rec["m"][0]) and le(rec["m"][0], gam)
            lx = log2_pos(rec["xmin1"])
            conds["gam-1<=log2(xmin+1)<=gam+1.874469"] = le(gam - 1, lx) and \
                le(lx, gam + Fraction(1874469, 10 ** 6))
            Lam = (rec["K"] - L * n) * LN2           # natural-log linear form
            conds["Lambda>=2^-gam"] = le(exp2_iv(-gam), Lam)
            conds["Lambda>0.054*2^-eps n"] = lt(Fraction(54, 1000) * exp2_iv(-e), Lam)
            if X0 >= 6:
                lxx = log2_pos(X0 + 1)
                conds["X0>=5.541 form"] = le(lxx + 1, gam) and le(gam, lxx + 2)
                mins["gm_lx"].append((gam - lxx).mid())
            for kk, v in conds.items():
                if not v:
                    fails.append((X0, p, n, kk))
            mins["gm_e"].append((gam - e).mid())
            mins["up"].append((lx - gam).mid())
            if rec["c"] > 1:
                tally["deep"] += 1
            if rec["unit_block"]:
                tally["unit_block"] += 1
    out("  grid: X0 in {1, 2, 5, 6, 16, 100, 256, 1000, 4096}, p = p1(X0) .. pmax (24-27): %d windows"
        % tally["windows"])
    out("  every window holds an n with gamma in [g, g+1]: empty windows %d" % tally["empty"])
    out("  Construction B instances: %d (all hits when n* < 2e5, else the largest hit); deep crash %d;"
        " instances with some m_t = 1: %d" % (tally["inst"], tally["deep"], tally["unit_block"]))
    out("  measured: gamma - eps_p n in [%.4f, %.4f]; log2(x_min+1) - gamma in [%.4f, %.4f];"
        % (min(mins["gm_e"]), max(mins["gm_e"]), min(mins["up"]), max(mins["up"])))
    out("            gamma - log2(X0+1) in [%.4f, %.4f] for X0 >= 6"
        % (min(mins["gm_lx"]), max(mins["gm_lx"])))
    check(not fails, "Thm 12.8.7.4 on the grid: %s" % (fails[:5],))
    out("  (H0), (H1'), eta <= 2^-20, (S) at all rotations, (X), every bracket, Lambda bounds: %d failures"
        % len(fails))
    # 'Every scale': windows of length N placed at random inside [3p+40, (g-lambda)/eps_p]
    rng = random.Random(4096)
    lfails = []
    lcount = 0
    for X0 in (1, 16, 4096):
        g, bot, top, ell = arc_for(X0)
        N, k = N_for(ell, cf, th)
        p1 = p1_for(N)
        for p in (p1, p1 + 2):
            nstar = ((g - LAM) / eps(p)).lo >> P
            for _ in range(4):
                nlo = rng.randint(3 * p + 40, nstar - N + 1)
                hit = None
                for n in range(nlo, nlo + N):
                    d, K = delta_n(n)
                    if le(bot, d) and le(d, top):
                        hit = n
                        break
                lcount += 1
                if hit is None:
                    lfails.append((X0, p, nlo, "empty"))
                    continue
                rec = check_B(p, hit, X0=X0, big=(hit > 200000))
                gam = rec["gam"]
                okk = (rec["H0"] and rec["H1p"] and rec["res"]["S_all"]
                       and all((X0 + 1) * rec["q"] <= (R << rec["m"][i]) for i, R in enumerate(rec["Rs"]))
                       and le(g, gam) and le(gam, g + 1) and le(LAM, gam - eps(p) * hit)
                       and all(rec["res"].values()))
                if not okk:
                    lfails.append((X0, p, hit))
    check(not lfails, "Thm 12.8.7.4 'every scale': %s" % (lfails[:4],))
    out("  'every scale': %d windows of length N placed at random in [3p+40, n*] (X0 in {1, 16, 4096},"
        " p in {p1, p1+2}, seed 4096): every window hit, Construction B passes (S), (X), (H0), (H1'),"
        " g <= gamma <= g+1: %d failures" % (lcount, len(lfails)))
    return tally, grid


# ---------------------------------------------------------------------------------------------
# Part 4: Remark 12.8.7.5 (the unit-crash exclusion at the Lemma 7 scale)
# ---------------------------------------------------------------------------------------------

def part4(rows):
    out("")
    out("== Part 4: Remark 12.8.7.5 -- unit-block exclusion at the Lemma 7 scale ==")
    out("  at p = p1(X0), n over the top window [n*-N+1, n*]; condition (L-1) eps_p n > lambda + 2.09 + log2 p;")
    out("  exact form: eps_p n + lambda + 1.5 + log2 p <= (L-1)(n - L^(p-1))/(L^(p-1) - 1)  (12.8.7.1(iii) negated)")
    out("  %-8s %-4s %-14s %-12s %-10s %s" % ("X0", "p", "(L-1)eps n", "rhs", "cond", "exact"))
    res = {}
    for lab in ["1", "16", "2^8", "2^12", "2^20", "2^60", "5*2^60", "2^71", "2^200"]:
        r = rows[lab]
        p = r["p1"]
        g = r["g"]
        e = eps(p)
        nstar = ((g - LAM) / e).lo >> P
        nlo = nstar - r["N"] + 1
        en = e * nlo                      # the weakest point of the window
        lhs = LM1 * en
        rhs = LAM + Fraction(209, 100) + log2_pos(p)
        cond = lt(rhs, lhs)
        Lp1 = Lpow(p - 1)
        exact = le(en + LAM + Fraction(3, 2) + log2_pos(p), LM1 * (nlo - Lp1) / (Lp1 - 1))
        res[lab] = (cond, exact)
        out("  %-8s %-4d %-14.4f %-12.4f %-10s %s" % (lab, p, lhs.mid(), rhs.mid(), cond, exact))
        if cond:
            check(exact, "2.09-condition implies the exact exclusion at X0=%s" % lab)
    check(all(res[l][0] for l in ["2^20", "2^60", "5*2^60", "2^71", "2^200"]),
          "Remark 12.8.7.5: condition holds from X0 = 2^20 through 2^200")
    out("  below 2^20 (informational): condition at X0 = 2^12: %s, at 2^8: %s"
        % (res["2^12"][0], res["2^8"][0]))
    # the slack constant: 2.09 >= 1.5 + (L-1)(1 + 1/(L^(p-1)-1)) for p >= 12
    for p in (10, 11, 12, 36):
        need = Fraction(3, 2) + LM1 * (1 + 1 / (Lpow(p - 1) - 1))
        out("  p = %d: 1.5 + (L-1)(1 + 1/(L^(p-1)-1)) = %.5f %s 2.09" % (p, need.mid(), "<=" if le(need, Fraction(209, 100)) else ">"))
    return res


# ---------------------------------------------------------------------------------------------

def main():
    cf = part0()
    part1()
    part2()
    rows, th = part3_table(cf)
    part3_windows(rows, cf, th)
    part4(rows)
    out("")
    out("== Summary ==")
    out("  checks: %d, failures: %d" % (NCHECK[0], len(FAILS)))
    for f in FAILS:
        out("  FAILED: " + f)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "x0_threshold_independent_check_output.txt")
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        fh.write("\n".join(OUT) + "\n")
    sys.stderr.write("elapsed %.1f s\n" % (time.time() - T_START))
    sys.exit(0 if not FAILS else 1)


if __name__ == "__main__":
    main()
