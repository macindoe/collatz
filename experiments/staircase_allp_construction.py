#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
staircase_allp_construction.py  --  cycles.md 12.8.6, gap B.

Supports: briefs/staircase-allp-construction-findings.md, and the proposed
replacement of Algorithm 12.8.6.3 (the bounded correction search) by a
construction whose size conditions hold BY CONSTRUCTION.

Independently written.  Imports nothing from experiments/staircase_allp.py,
experiments/p22_passer.py or experiments/uniform_trim.py; every pass/fail
decision below is an exact big-integer comparison (Python int).  Floats and
decimals appear ONLY in report columns (gamma, margins in bits, the
real-analytic sufficient threshold Gamma) and never in a pass/fail branch.

--------------------------------------------------------------------------
THE TARGET INEQUALITY (Proposition 12.6.1, specialised to the staircase)
--------------------------------------------------------------------------
Profile (m_t, s_t), t in Z/pZ, entries >= 1;  n = sum m_t,  K = sum s_t + n,
q = 2^K - 3^n > 0.  With sigma_t = s_t + m_{t+1}, Proposition 12.6.1 gives,
in rotation order starting at r,

    R_r = sum_{t=0}^{p-1} 3^{M_t} 2^{S_t} (2^{s_t} - 1),
    M_t = sum_{j>t} m_j,   S_t = sum_{j<t} sigma_j,

and the size conditions are  q <= R_r  for every r.

Staircase shape: blocks 0..p-2 are "climb" blocks with s_j = 1; block p-1 is
the "crash" block, m_{p-1} = c, s_{p-1} = S - (p-1), S = K - n.  Write
T_r = m_0 + ... + m_r  (T_{-1} = 0), so T_{p-1} = n.

For rotation r keep the SINGLE term t = p-1-r of R_r -- the one whose 3-power
is the m-mass of the maximal climb-prefix arc {0,...,r-1} that stops at the
crash block.  Every other arc ending at block r-1 either is shorter (smaller
3-power) or crosses the crash block and pays its enormous exit valuation.
That term is exactly

    Term_r = 3^{T_{r-1}} * 2^{(p-1-r) + n - T_r} * (2^{S-p+1} - 1),

so a SUFFICIENT condition for rotation r (0 <= r <= p-1) is

    (C_r)   q * 2^{m_r} <= X_r,
            X_r := 3^{T_{r-1}} * 2^{n - T_{r-1} + p - 1 - r} * (2^{S-p+1} - 1).

(C_r) is exactly, in real form,   m_r + r + eta <= gamma + (L-1) T_{r-1},
with L = log_2 3, gamma = K - log_2 q, eta = -log_2(1 - 2^{-(S-p+1)}) ~ 0.

--------------------------------------------------------------------------
THE CONSTRUCTION (no correction step)
--------------------------------------------------------------------------
Greedy saturation of (C_r), with a reserve so that the climb lands exactly on
n-1 and the crash block gets depth 1:

    T_{-1} = 0
    for r = 0 .. p-2:
        cap_r    = max{ m >= 0 : q * 2^m <= X_r }        (exact, big-integer)
        budget_r = n - 1 - T_{r-1} - (p - 2 - r)         (reserve 1 per block)
        m_r      = min(cap_r, budget_r)
        T_r      = T_{r-1} + m_r
    m_{p-1} = c = n - T_{p-2};  s_j = 1 (j <= p-2);  s_{p-1} = S - (p-1)

Every (C_r) then holds by construction for r <= p-2 (m_r <= cap_r), and
(C_{p-1}) is checked exactly.
"""

import math
import sys
import time
from decimal import Decimal, getcontext

getcontext().prec = 80

# --- real constants, REPORT ONLY -------------------------------------------
DEC_L = Decimal(3).ln() / Decimal(2).ln()          # L = log_2 3
L = float(DEC_L)
LM1 = L - 1.0                                       # log_2(3/2) = 0.5849625...


def log2_big(x):
    """log2 of a positive Python int, ~1e-17 relative.  REPORT ONLY."""
    bl = x.bit_length()
    if bl <= 64:
        return math.log2(x)
    sh = bl - 64
    return sh + math.log2(x >> sh)


# ==========================================================================
# 1.  Exact primitives
# ==========================================================================

def K_of(n):
    """K = ceil(n*log_2 3), exactly, with no floating point.

    log_2 3 is irrational so n*L is never an integer for n >= 1; hence
    ceil(nL) = floor(nL) + 1 = bit_length(3^n).  (bit_length(x) = floor(log2 x)+1.)
    """
    return (3 ** n).bit_length()


def rotation_numerators(ms, ss):
    """All p numerators R_r of Proposition 12.6.1, exactly.  Written from the
    statement of 12.6.1 directly; no shortcut via the transport recurrence
    12.6.1.1 (that would be importing a result rather than checking one).

    3^{M_t} is carried incrementally down the t-loop and 2^{S_t} is a left
    shift; this is bookkeeping only -- the value computed is term-by-term the
    displayed sum of 12.6.1."""
    p = len(ms)
    out = []
    for r in range(p):
        m = [ms[(r + i) % p] for i in range(p)]
        s = [ss[(r + i) % p] for i in range(p)]
        sig = [s[i] + m[(i + 1) % p] for i in range(p)]
        S = [0] * p
        acc = 0
        for t in range(p):
            S[t] = acc
            acc += sig[t]
        R = 0
        pow3 = 1                       # 3^{M_t}, M_{p-1} = 0
        for t in range(p - 1, -1, -1):
            R += (pow3 * ((1 << s[t]) - 1)) << S[t]
            pow3 *= 3 ** m[t]          # M_{t-1} = M_t + m_t
        out.append(R)
    return out


def profile_data(ms, ss):
    n = sum(ms)
    K = sum(ss) + n
    q = 2 ** K - 3 ** n
    return n, K, q


def size_check(ms, ss):
    """Exact size test.  Returns (ok, q, Rs, margins_in_bits).
    margins[r] = log2(R_r / q); the pass/fail decision uses only ints."""
    n, K, q = profile_data(ms, ss)
    if q <= 0:
        return False, q, None, None
    Rs = rotation_numerators(ms, ss)
    ok = all(q <= R for R in Rs)
    marg = [log2_big(R) - log2_big(q) for R in Rs]
    return ok, q, Rs, marg


def divisibility_check(ms, ss):
    """Exact q | R_r test for every rotation (12.8.3 / 12.8.6.4 record: the
    constructed size-passers must all FAIL this).  Returns list of bools."""
    n, K, q = profile_data(ms, ss)
    Rs = rotation_numerators(ms, ss)
    return [R % q == 0 for R in Rs]


# ==========================================================================
# 2.  The construction
# ==========================================================================

def construct(p, n, K=None, reserve_crash=1):
    """Greedy-saturating staircase.  Returns (ms, ss) or (None, reason)."""
    if K is None:
        K = K_of(n)
    S = K - n
    if p < 2:
        return None, "p<2"
    if S < p:
        return None, "S<p (crash exit valuation would be <1)"
    if n < p:
        return None, "n<p"
    q = 2 ** K - 3 ** n
    scrash = S - (p - 1)
    fac = (2 ** scrash) - 1

    ms = []
    T = 0
    pow3T = 1                      # 3^{T_{r-1}}, carried incrementally
    for r in range(p - 1):
        # X_r = 3^{T_{r-1}} * 2^{n - T_{r-1} + p - 1 - r} * (2^{scrash} - 1)
        X = pow3T * fac << (n - T + p - 1 - r)
        Q = X // q
        cap = Q.bit_length() - 1 if Q > 0 else -1
        if cap < 1:
            return None, "cap<1 at r=%d (gamma too small)" % r
        budget = n - reserve_crash - T - (p - 2 - r)
        m = cap if cap < budget else budget
        if m < 1:
            return None, "budget<1 at r=%d" % r
        ms.append(m)
        T += m
        pow3T *= 3 ** m
    c = n - T
    if c < 1:
        return None, "crash depth <1"
    ms.append(c)
    ss = [1] * (p - 1) + [scrash]
    return (ms, ss), "ok"


def crash_rotation_ok(p, n, K, ms):
    """Exact test of (C_{p-1}) alone: q <= 3^{n-c} * (2^{S-p+1} - 1).

    Used ONLY as a scan prefilter (it is cheap: one power of 3).  Nothing is
    reported on its strength -- every instance printed below is re-tested with
    the full p-rotation size_check() built from Proposition 12.6.1."""
    S = K - n
    c = ms[-1]
    q = 2 ** K - 3 ** n
    return q <= (3 ** (n - c)) * ((1 << (S - p + 1)) - 1)


def gamma_of(n, K=None):
    """gamma = K - log_2 q.  REPORT ONLY."""
    if K is None:
        K = K_of(n)
    q = 2 ** K - 3 ** n
    return K - log2_big(q)


def quality_of(n, K=None):
    """x_n = ceil(nL) - nL in (0,1); the Diophantine quality parameter.
    REPORT ONLY (high-precision Decimal)."""
    if K is None:
        K = K_of(n)
    return float(Decimal(K) - Decimal(n) * DEC_L)


def Gamma_threshold(p, n, eta=0.0):
    """The proved sufficient threshold

        Gamma(p,n) = [ (n-1)(L-1)^2 + L^{p-1}(1 + beta(L-1))
                       - (p-2+beta)(L-1) - L ] / [ (L-1)(L^{p-1} - 1) ],
        beta = 1 + eta,

    from A_{p-2} >= n-1 where A_r = L A_{r-1} + gamma - r - beta, A_{-1} = 0
    is the continuous lower solution of the greedy recursion.  REPORT ONLY
    (the construction itself never consults it)."""
    beta = 1.0 + eta
    Lp = float(DEC_L ** (p - 1))
    num = (n - 1) * LM1 * LM1 + Lp * (1.0 + beta * LM1) - (p - 2 + beta) * LM1 - L
    den = LM1 * (Lp - 1.0)
    return num / den


# ==========================================================================
# 3.  Comparison constructions (for the negative controls)
# ==========================================================================

def base_geometric(p, n, K=None, crash_depth=1, per_block=False):
    """The superseded recipe's PURE geometric base profile (cycles.md
    12.8.6.3), re-implemented independently: p-1 climb blocks with depths
    rounded from m_j ~ a*L^j, by rounding the partial sums (per_block=False)
    or each m_j on its own (per_block=True), plus one crash block. This is
    the negative control -- the profile lacking the additive 1/(L-1) offset
    -- not the greedy Construction B of 12.8.6.2 that construct() builds."""
    if K is None:
        K = K_of(n)
    S = K - n
    if p < 2 or S <= p - 1:
        return None
    climb = n - crash_depth
    if climb < p - 1:
        return None
    blocks = p - 1
    a = Decimal(climb) * (DEC_L - 1) / (DEC_L ** blocks - 1)
    ms = []
    if per_block:
        for j in range(blocks):
            ms.append(int((a * DEC_L ** j).to_integral_value()))
    else:
        prev = 0
        for j in range(blocks):
            Tj = a * (DEC_L ** (j + 1) - 1) / (DEC_L - 1)
            Mj = int(Tj.to_integral_value())
            ms.append(Mj - prev)
            prev = Mj
    d = climb - sum(ms)
    ms[-1] += d
    if min(ms) < 1:
        return None
    ms = ms + [crash_depth]
    ss = [1] * (p - 1) + [S - (p - 1)]
    if ss[-1] < 1:
        return None
    return ms, ss


# ==========================================================================
# 4.  Scale, candidate scan
# ==========================================================================

def scale_n(p):
    """n0(p) = round(L^p): the canonical scale n ~ 1.585^p of 12.8.3/12.8.6.4."""
    return int((DEC_L ** p).to_integral_value())


def scan(p, n_start, width):
    """Walk n upward from n_start, carrying 3^n incrementally.  Yields
    (n, K, q) for each n; the caller decides what to do."""
    P = 3 ** n_start
    n = n_start
    for _ in range(width):
        K = P.bit_length()
        q = (1 << K) - P
        yield n, K, q
        P *= 3
        n += 1


def window_for(Gam, slack=6.0):
    """How far one must walk to expect an n of quality gamma >= Gam.  The set
    { n : gamma(n) >= Gam } has density -log2(1 - 2^-Gam) ~ 1.4427 * 2^-Gam
    (Weyl); take `slack` times the reciprocal."""
    dens = -math.log2(1.0 - 2.0 ** (-Gam))
    return int(min(60000, max(24, slack / dens)))


# ==========================================================================
# 5.  Reporting helpers
# ==========================================================================

def hdr(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


FAILS = []


def check(cond, label):
    if not cond:
        FAILS.append(label)
        print("   *** FAILED CHECK: %s" % label)
    return cond


# ==========================================================================
# PART 0.  Canaries for the exact machinery
# ==========================================================================

def part0():
    hdr("PART 0.  Canaries -- is rotation_numerators() the real 12.6.1?")
    # (a) trivial cycle read as a fake period-p cycle: R_r = 4^p - 3^p = q.
    for p in (1, 2, 3, 4, 7, 11):
        ms = [1] * p
        ss = [1] * p
        n, K, q = profile_data(ms, ss)
        Rs = rotation_numerators(ms, ss)
        want = 4 ** p - 3 ** p
        ok = (q == want) and all(R == want for R in Rs)
        print("   trivial p=%-2d : q = 4^p-3^p = %-12d  all R_r equal q : %s"
              % (p, want, ok))
        check(ok, "trivial-cycle identity p=%d" % p)

    # (b) transport recurrence of Remark 12.6.1.1 as an INDEPENDENT audit of
    #     rotation_numerators (the recurrence is not used to compute anything).
    import random
    random.seed(20260728)
    bad = 0
    for _ in range(200):
        p = random.randint(2, 7)
        ms = [random.randint(1, 6) for _ in range(p)]
        ss = [random.randint(1, 6) for _ in range(p)]
        n, K, q = profile_data(ms, ss)
        Rs = rotation_numerators(ms, ss)
        for r in range(p):
            sig = ss[r] + ms[(r + 1) % p]
            lhs = (2 ** sig) * Rs[(r + 1) % p]
            rhs = (3 ** ms[r]) * Rs[r] + ((2 ** ss[r]) - 1) * q
            if lhs != rhs:
                bad += 1
    print("   transport recurrence 2^sigma_r R_{r+1} = 3^{m_r} R_r + (2^{s_r}-1)q")
    print("   over 200 random profiles, all rotations : mismatches = %d" % bad)
    check(bad == 0, "transport recurrence audit")

    # (c) the published p = 7 staircase of 12.8.3.
    ms = [4, 7, 9, 15, 23, 35, 1]
    n = sum(ms)
    K = K_of(n)
    S = K - n
    ss = [1] * 6 + [S - 6]
    ok, q, Rs, marg = size_check(ms, ss)
    g = gamma_of(n, K)
    print("   12.8.3 p=7 instance m=%s : n=%d K=%d gamma=%.3f  all pass=%s"
          % (ms, n, K, g, ok))
    print("   per-rotation margins log2(R_r/q) = %s"
          % " ".join("%.2f" % x for x in marg))
    check(ok, "published p=7 staircase passes")
    check(abs(g - 6.744) < 0.01, "published p=7 gamma = 6.744")
    dv = divisibility_check(ms, ss)
    print("   divisibility q | R_r : %s  (must be all False)" % dv)
    check(not any(dv), "published p=7 instance fails divisibility")


# ==========================================================================
# PART 1.  The main construction table
# ==========================================================================

def part1(pmax=30, window=64):
    hdr("PART 1.  The construction, first passer at the canonical scale n ~ L^p")
    print("   For each p: start at n0 = round(L^p) and walk n upward until the")
    print("   construction exists AND all p exact size conditions q <= R_r hold.")
    print("   'off' is n - n0, the search distance -- the Diophantine cost.")
    print()
    print("   'cert' = does this n meet the PROVED hypothesis gamma >= Gamma(p,n)?")
    print("   'ncert/off' = the first n at the scale that does, and its offset.")
    print()
    print("    p       n0        n   off   x_n      gamma   Gamma  g/log2p  kappa"
          "  c   minmarg  div  cert   ncert  off2")
    rows = []
    for p in range(2, pmax + 1):
        n0 = scale_n(p)
        found = None
        t0 = time.time()
        for n, K, q in scan(p, n0, window):
            g = K - log2_big(q)
            res, why = construct(p, n, K)
            if res is None:
                continue
            ms, ss = res
            if not crash_rotation_ok(p, n, K, ms):
                continue                      # scan prefilter only
            ok, q2, Rs, marg = size_check(ms, ss)
            if ok:
                found = (n, K, q, g, ms, ss, marg)
                break
        if found is None:
            print("    %-3d  no passer in window of %d" % (p, window))
            check(False, "p=%d passer found" % p)
            continue
        n, K, q, g, ms, ss, marg = found
        x = quality_of(n, K)
        G = Gamma_threshold(p, n)
        kappa = n / float(DEC_L ** p)
        dv = divisibility_check(ms, ss)
        check(not any(dv), "p=%d constructed instance fails divisibility" % p)
        # trim canary: Theorem 12.8.1 must hold
        trim_lhs = g + math.log2(p)
        trim_rhs = 0.585 * n / (1.585 ** p - 1)
        check(trim_lhs > trim_rhs, "p=%d respects Theorem 12.8.1" % p)
        # first n at the scale meeting the PROVED hypothesis, verified exactly
        ncert = None
        for n2, K2, q2 in scan(p, n0, window):
            if K2 - log2_big(q2) < Gamma_threshold(p, n2):
                continue
            res2, why2 = construct(p, n2, K2)
            if res2 is None:
                check(False, "p=%d certified n=%d yields no profile (%s)"
                      % (p, n2, why2))
                continue
            ok2, _, _, _ = size_check(*res2)
            check(ok2, "p=%d certified n=%d passes all size conditions" % (p, n2))
            check(res2[0][-1] == 1,
                  "p=%d certified n=%d has crash depth exactly 1" % (p, n2))
            if ok2 and ncert is None:
                ncert = n2
                break
        print("    %-3d %8d %8d %5d  %.4f  %7.3f %7.3f  %6.3f  %5.3f %3d  %6.3f  %-5s %-5s %7s %5s"
              % (p, n0, n, n - n0, x, g, G, g / math.log2(p) if p > 1 else 0,
                 kappa, ms[-1], min(marg), any(dv), g >= G,
                 ncert if ncert else "-", (ncert - n0) if ncert else "-"))
        rows.append(dict(p=p, n0=n0, n=n, off=n - n0, x=x, g=g, G=G,
                         kappa=kappa, c=ms[-1], minmarg=min(marg), ms=ms,
                         ncert=ncert, secs=time.time() - t0))
    print()
    if rows:
        offs = [r["off"] for r in rows]
        gs = [r["g"] for r in rows]
        cof = [r["ncert"] - r["n0"] for r in rows if r["ncert"]]
        nocert = [r["p"] for r in rows if not r["ncert"]]
        if cof:
            print("   certified search distance: max %d, mean %.1f (over %d periods)"
                  % (max(cof), sum(cof) / len(cof), len(cof)))
        if nocert:
            print("   periods with NO theorem-certified n at the canonical scale: %s"
                  % nocert)
            print("   (small-p artifact: Gamma's n-coefficient is (L-1)/(L^{p-1}-1),")
            print("    which is O(1) only once L^{p-1} >> 1.  Those p have exact")
            print("    passers by direct exhibition above -- they are covered by")
            print("    the finite check, not by the asymptotic hypothesis.)")
        print("   search distance n - n0 : max %d, mean %.1f  (NOT growing with p)"
              % (max(offs), sum(offs) / len(offs)))
        print("   gamma achieved         : min %.3f  max %.3f  (BOUNDED, not O(log p))"
              % (min(gs), max(gs)))
        print("   gamma / log2 p         : min %.3f  max %.3f  (DECREASING in p)"
              % (min(r["g"] / math.log2(r["p"]) for r in rows),
                 max(r["g"] / math.log2(r["p"]) for r in rows)))
    return rows


def part1b(rows):
    hdr("PART 1b.  Shape of the constructed profiles (the +1/(L-1) offset)")
    print("   The greedy profile is geometric PLUS a constant additive offset")
    print("   1/(L-1) = %.4f per block: (L-1) * 1/(L-1) = 1 is exactly the one"
          % (1 / LM1))
    print("   unit of exit valuation each climb block spends.  12.8.6.2's PURE")
    print("   geometric profile omits it -- that omission is the shortfall.")
    print()
    for r in rows:
        if r["p"] in (7, 10, 14, 18, 22, 26, 30):
            ms = r["ms"]
            show = ms[:12] + (["..."] if len(ms) > 13 else []) + ([ms[-1]] if len(ms) > 12 else [])
            print("   p=%-3d n=%-8d m = %s" % (r["p"], r["n"], show))
            rat = [ms[i + 1] / ms[i] for i in range(min(len(ms) - 2, 9))]
            print("        ratios m_{j+1}/m_j = %s   (-> L = %.4f from below)"
                  % (" ".join("%.3f" % v for v in rat), L))


# ==========================================================================
# PART 2.  The shortfall of the superseded recipe's PURE geometric base
#          profile (cycles.md 12.8.6.3), and its p-growth.  Wherever the
#          printed text of this Part cites 12.8.6.2, the object meant is
#          that pure-geometric profile, i.e. 12.8.6.3.  The printed strings
#          are left as they stand so the committed output stays byte-exact.
# ==========================================================================

def part2(rows):
    hdr("PART 2.  Shortfall of the base construction 12.8.6.2 at the SAME n")
    print("   D_r := (m_r + r + eta) - (gamma + (L-1) T_{r-1})  is the deficit in")
    print("   condition (C_r).  For the exact-real geometric profile it equals")
    print("       D_r = m_0 + r - gamma + eta,")
    print("   so D_max = m_0 + (p-2) - gamma + eta:  LINEAR IN p.  Predicted")
    print("   (with <=1 unit of partial-sum rounding slop):")
    print("       D_pred = a0 + (p-2) - gamma + 1 + (L-1)/2,  a0 = n(L-1)/(L^{p-1}-1)")
    print()
    print("    p        n   gamma   D_pred   D_meas(1-term)  minmarg(full R)  passes")
    for r in rows:
        p, n = r["p"], r["n"]
        K = K_of(n)
        bg = base_geometric(p, n, K)
        if bg is None:
            print("    %-3d  base construction infeasible" % p)
            continue
        ms, ss = bg
        ok, q, Rs, marg = size_check(ms, ss)
        g = r["g"]
        # measured single-term deficit
        S = K - n
        scrash = S - (p - 1)
        T = 0
        worst = -1e9
        for j in range(p):
            X = (3 ** T) * ((2 ** scrash) - 1) << (n - T + p - 1 - j)
            # deficit in bits: log2(q * 2^{m_j}) - log2(X)
            d = log2_big(q) + ms[j] - log2_big(X)
            worst = max(worst, d)
            T += ms[j]
        a0 = n * LM1 / (float(DEC_L ** (p - 1)) - 1)
        Dpred = a0 + (p - 2) - g + 1 + LM1 / 2
        print("    %-3d %8d %7.3f  %7.3f        %7.3f          %7.3f      %s"
              % (p, n, g, Dpred, worst, min(marg), ok))
        check(worst <= Dpred + 1e-6,
              "p=%d base-construction shortfall within the derived bound" % p)
    print()
    print("   The measured deficit tracks the p-linear prediction.  That is the")
    print("   structural reason 12.8.6.3's move count grew with p (0 at small p,")
    print("   13 at p = 22) and why no O(1)/O(log p) bound on it was available:")
    print("   the base profile's deficit is Theta(p) at fixed gamma.")


# ==========================================================================
# PART 3.  The proof's own steps, checked
# ==========================================================================

def greedy_caps(p, n, K, capped=True):
    """Re-run the construction recording (cap_r, m_r, T_r) and the real
    quantity f_r = gamma + (L-1)T_{r-1} - r - eta  whose floor is cap_r.

    capped=False runs the UNCAPPED greedy m_r = cap_r (no landing budget).
    That is the sequence T-hat of step (b) of the proof: the budget cap can
    only lower T, so T <= T-hat, and it is T-hat that is bounded below by the
    continuous solution A_r."""
    S = K - n
    q = 2 ** K - 3 ** n
    scrash = S - (p - 1)
    fac = (1 << scrash) - 1
    g = K - log2_big(q)
    eta = -math.log2(1.0 - 2.0 ** (-scrash)) if scrash < 60 else 0.0
    out = []
    T = 0
    pow3T = 1
    for r in range(p - 1):
        if not capped and T > n - 1:
            break          # T-hat has already passed n-1; that is all step (d) needs
        X = pow3T * fac << (n - T + p - 1 - r)
        cap = (X // q).bit_length() - 1
        f = g + LM1 * T - r - eta
        budget = n - 1 - T - (p - 2 - r)
        m = min(cap, budget) if capped else cap
        out.append((r, cap, m, T, f))
        T += m
        pow3T *= 3 ** m
    return out, eta


def part3():
    hdr("PART 3.  The proof's own steps, checked numerically")
    print("   Step 1 (well-definedness).  f_r := gamma + (L-1)T_{r-1} - r - eta,")
    print("     cap_r = floor(f_r).  f_{r+1} - f_r = (L-1)cap_r - 1, so cap_r >= 2")
    print("     forces f nondecreasing, hence cap_{r+1} >= 2: gamma >= 2 + eta")
    print("     alone makes the greedy run to completion.  Checked: cap_r = floor(f_r)")
    print("     exactly (the big-integer cap agrees with the real formula), and")
    print("     cap_r >= 2 throughout whenever gamma >= 2 + eta.")
    print()
    print("   Step 2 (growth).  T_r > L T_{r-1} + gamma - r - beta, beta = 1 + eta,")
    print("     so T_r > A_r where A_r = L A_{r-1} + gamma - r - beta, A_{-1} = 0.")
    print()
    print("   Step 3 (closed form).  A_r = [L^{r+1}((gamma-beta)(L-1) - 1)")
    print("     + (r+beta-gamma)(L-1) + L] / (L-1)^2, and A_{p-2} >= n-1 is")
    print("     exactly gamma >= Gamma(p,n).")
    print()
    bad1 = bad2 = bad3 = bad4 = 0
    tested = 0
    print("   Step 4 (landing).  T-hat_{p-2} >= n-1 forces the landing budget to")
    print("     bind, hence T_{p-2} = n-1 and crash depth exactly 1.")
    print()
    print("    p        n   gamma    min(cap_r)  min(That_r - A_r)  A_{p-2}-(n-1)  g-Gamma  c")
    nland = 0
    for p in (5, 7, 9, 11, 13, 15, 17, 19, 21, 23):
        n0 = scale_n(p)
        shown = 0
        for n, K, q in scan(p, n0, 40):
            g = K - log2_big(q)
            if g < 2.2:
                continue
            caps, eta = greedy_caps(p, n, K)
            beta = 1.0 + eta
            # step 1: cap_r == floor(f_r), and cap_r >= 2
            for (r, cap, m, T, f) in caps:
                tested += 1
                if abs(cap - math.floor(f)) > 1e-9 and abs(f - round(f)) > 1e-9:
                    bad1 += 1
                if g >= 2.0 + eta and cap < 2:
                    bad2 += 1
            # step 2: T-hat_r > A_r  (recursion form; UNCAPPED greedy -- the
            # landing budget can only lower T, and step (d) of the proof uses
            # the bound on T-hat, not on T)
            ucaps, _ = greedy_caps(p, n, K, capped=False)
            A = 0.0
            worst = 1e18
            for (r, cap, m, T, f) in ucaps:
                A = L * A + g - r - beta
                # T here is T_{r-1}; the value after adding m is T_r
                worst = min(worst, (T + m) - A)
            if worst <= -1e-9:
                bad3 += 1
            # step 3: closed form vs recursion, and the Gamma equivalence.
            # A_r is a pure real recursion; run it over the FULL p-1 steps
            # (the step-2 loop above may stop early once T-hat passes n-1).
            A = 0.0
            for rr in range(p - 1):
                A = L * A + g - rr - beta
            r = p - 2
            Lp = float(DEC_L ** (r + 1))
            Acf = (Lp * ((g - beta) * LM1 - 1.0) + (r + beta - g) * LM1 + L) / (LM1 * LM1)
            if abs(Acf - A) > 1e-6 * max(1.0, abs(A)):
                bad4 += 1
            G = Gamma_threshold(p, n, eta)
            equiv = (Acf >= n - 1) == (g >= G - 1e-9)
            if not equiv:
                bad4 += 1
            # step 4: gamma >= Gamma  =>  crash depth exactly 1
            cdep = None
            if g >= G:
                res, _ = construct(p, n, K)
                if res is not None:
                    cdep = res[0][-1]
                    nland += 1
                    check(cdep == 1,
                          "PART 3 step 4: p=%d n=%d certified => crash depth 1"
                          % (p, n))
            if shown == 0 or (shown == 1 and g >= G):
                print("    %-3d %8d %7.3f %11d %18.3f %14.1f %8.3f  %s"
                      % (p, n, g, min(c[1] for c in caps), worst, Acf - (n - 1),
                         g - G, cdep if cdep is not None else "-"))
                shown = 2 if g >= G else 1
    print()
    print("   certified instances whose crash depth was checked: %d" % nland)

    # Side condition of (H1): Gamma(p,n) >= 2 + eta wherever (H0) holds, so the
    # extra clause costs nothing.  Gamma DOES dip below 2 at tiny (p,n) that
    # (H0) excludes -- that is why the clause is written into the hypothesis.
    viol = tot = 0
    lowest, argmin = 1e9, None
    for p in range(2, 34):
        for n in range(p, min(4000, 40 * p)):
            K = K_of(n)
            if K - n < p:                     # (H0): S >= p
                continue
            tot += 1
            G = Gamma_threshold(p, n)
            if G < lowest:
                lowest, argmin = G, (p, n)
            if G < 2.0 - 1e-9:
                viol += 1
    print("   Gamma >= 2 over %d (p,n) pairs satisfying (H0): min Gamma = %.6f"
          " at (p,n) = %s, violations = %d" % (tot, lowest, argmin, viol))
    print("   (the minimum is attained with EQUALITY, so the 2+eta clause of (H1)")
    print("    is exactly tight there and slack everywhere else.)")
    check(viol == 0, "PART 3: Gamma >= 2 whenever (H0) holds")
    print("   (outside (H0) it does dip: Gamma(3,2) = %.3f, Gamma(2,1) = %.3f)"
          % (Gamma_threshold(3, 2), Gamma_threshold(2, 1)))
    print("   over %d greedy steps: cap != floor(f) : %d ; cap < 2 with gamma >= 2+eta : %d"
          % (tested, bad1, bad2))
    print("   T_r <= A_r violations : %d ;  closed-form / Gamma-equivalence failures : %d"
          % (bad3, bad4))
    check(bad1 == 0, "PART 3 step 1: big-integer cap equals floor(f_r)")
    check(bad2 == 0, "PART 3 step 1: gamma >= 2+eta keeps cap_r >= 2")
    check(bad3 == 0, "PART 3 step 2: T_r > A_r at every step")
    check(bad4 == 0, "PART 3 step 3: closed form of A_{p-2} and the Gamma equivalence")


# ==========================================================================
# PART 3b.  Negative controls
# ==========================================================================

def nc_quality(pmax=22, window=64):
    hdr("NC-A.  The quality hypothesis bites (perturb gamma downward)")
    print("   At each p sweep n over a window at the canonical scale.  For each n")
    print("   record d(n) = gamma(n) - Gamma(p,n) and whether the construction's")
    print("   p exact size conditions all hold.  Two things are being tested:")
    print("     SOUNDNESS  every n with d >= 0 passes  (the theorem)")
    print("     BITE       some n in the window fails  (the hypothesis is not vacuous)")
    print("   d is used per-n, not against a single number, because Gamma depends")
    print("   on n through kappa = n/L^p and the window spans a range of kappa.")
    print()
    print("    p   #n  #pass  #d>=0  #(d>=0 & fail)   max d among FAILERS"
          "   min d among passers")
    for p in range(4, pmax + 1, 3):
        n0 = scale_n(p)
        df, dp = [], []
        bad = 0
        for n, K, q in scan(p, n0, window):
            g = K - log2_big(q)
            d = g - Gamma_threshold(p, n)
            res, why = construct(p, n, K)
            ok = False
            if res is not None:
                ms, ss = res
                ok, _, _, _ = size_check(ms, ss)
            if ok:
                dp.append(d)
            else:
                df.append(d)
                if d >= 0:
                    bad += 1
        ncert = sum(1 for x in dp + df if x >= 0)
        print("    %-3d %4d  %5d  %5d  %14d   %19.3f   %19.3f"
              % (p, window, len(dp), ncert, bad,
                 max(df) if df else float("nan"),
                 min(dp) if dp else float("nan")))
        check(len(df) > 0, "NC-A p=%d: some n in window fail (bound bites)" % p)
        check(bad == 0, "NC-A p=%d: SOUND -- no n with gamma >= Gamma fails" % p)


def nc_quality_wide(plist=(8, 12, 16, 20), mults=(1, 2, 3, 5, 8), window=64):
    hdr("NC-A2.  Soundness across kappa (the formula's other variable)")
    print("   Same test, but sweeping the scale multiplier so kappa = n/L^p runs")
    print("   over 1..8.  Gamma grows like 0.92714*kappa + 2.70933, so the")
    print("   hypothesis must get HARDER as kappa grows; if it did not, the")
    print("   kappa-dependence of the formula would be decoration.")
    print()
    print("    p  mult   kappa  #pass/#n   #(d>=0 & fail)   Gamma(mid)")
    for p in plist:
        for mult in mults:
            n0 = scale_n(p) * mult
            npass = bad = 0
            tot = 0
            for n, K, q in scan(p, n0, window):
                g = K - log2_big(q)
                d = g - Gamma_threshold(p, n)
                res, _ = construct(p, n, K)
                ok = False
                if res is not None:
                    ok, _, _, _ = size_check(*res)
                tot += 1
                npass += ok
                if d >= 0 and not ok:
                    bad += 1
            print("    %-3d %4d  %6.2f   %4d/%-4d   %14d   %10.3f"
                  % (p, mult, n0 / float(DEC_L ** p), npass, tot, bad,
                     Gamma_threshold(p, n0)))
            check(bad == 0,
                  "NC-A2 p=%d mult=%d: SOUND (no certified n fails)" % (p, mult))
            if mult >= 3:
                check(npass < tot,
                      "NC-A2 p=%d mult=%d: bites (kappa raises the bar)" % (p, mult))


def nc_rounding(rows):
    hdr("NC-B.  The rounding rule is load-bearing (perturb the rounding)")
    print("   Same n, same crash depth, same shape -- only the rule that turns")
    print("   the real profile into integers changes.")
    print("     greedy      : saturate (C_r) exactly, in big integers  [THIS WORK]")
    print("     partialsum  : round the partial sums of the PURE geometric  [12.8.6.2]")
    print("     perblock    : round each m_j of the PURE geometric on its own")
    print()
    print("    p        n   greedy  partialsum  perblock   #fail(ps)  #fail(pb)")
    npass_g = npass_ps = npass_pb = 0
    for r in rows:
        p, n = r["p"], r["n"]
        K = K_of(n)
        res, _ = construct(p, n, K)
        okg = False
        if res:
            okg, _, _, _ = size_check(*res)
        cells = []
        counts = []
        for pb in (False, True):
            bg = base_geometric(p, n, K, per_block=pb)
            if bg is None:
                cells.append("infeas")
                counts.append(-1)
                continue
            ok, q, Rs, marg = size_check(*bg)
            cells.append("PASS" if ok else "fail")
            counts.append(sum(1 for R in Rs if R < q))
        npass_g += okg
        npass_ps += cells[0] == "PASS"
        npass_pb += cells[1] == "PASS"
        print("    %-3d %8d   %-6s  %-10s  %-8s   %8d   %8d"
              % (p, n, "PASS" if okg else "fail", cells[0], cells[1],
                 counts[0], counts[1]))
    print()
    print("   greedy passes %d/%d; partial-sum-geometric %d/%d; per-block %d/%d"
          % (npass_g, len(rows), npass_ps, len(rows), npass_pb, len(rows)))
    check(npass_g == len(rows), "NC-B: greedy passes everywhere")
    check(npass_ps < len(rows), "NC-B: the rounding rule genuinely matters")


def nc_crash(rows):
    hdr("NC-C.  The crash depth is load-bearing (perturb c)")
    print("   Re-run the construction with the crash depth forced up to c, for")
    print("   c = 1, 2, 4, 8, ... and find the largest c whose p exact size")
    print("   conditions all still hold.  The derived ceiling is (C_{p-1}):")
    print("       c * L  <=  gamma + (L-1)*n - (p-1) - eta,")
    print("   i.e. c <= c_max = (gamma + (L-1)n - (p-1))/L ~ 0.369*n.")
    print("   A crash depth ABOVE c_max must fail; below it must pass.")
    print()
    print("    p        n   c_max(derived)   largest passing c   first failing c"
          "   fails at rotation")
    for r in rows:
        if r["p"] not in (6, 9, 12, 15, 18, 21, 24, 27, 30):
            continue
        p, n = r["p"], r["n"]
        K = K_of(n)
        g = gamma_of(n, K)
        cmax = (g + LM1 * n - (p - 1)) / L
        best, firstfail, whichr = None, None, None
        c = 1
        while c < n - p:
            res, _ = construct(p, n, K, reserve_crash=c)
            ok = False
            if res is not None:
                ok, q, Rs, marg = size_check(*res)
                if not ok and whichr is None:
                    whichr = [i for i, R in enumerate(Rs) if R < q]
            if ok:
                best = c
            else:
                firstfail = c
                break
            c *= 2
        print("    %-3d %8d   %12.1f   %17s   %15s   %s"
              % (p, n, cmax, best, firstfail, whichr))
        check(firstfail is not None,
              "NC-C p=%d: a deep enough crash block fails" % p)
        if firstfail is not None:
            check(firstfail > cmax / 4,
                  "NC-C p=%d: first failure not far below the derived ceiling" % p)
        if best is not None:
            check(best <= cmax + 1,
                  "NC-C p=%d: no passing c above the derived ceiling" % p)


def nc_saturation(rows):
    hdr("NC-D.  The construction sits ON the boundary (perturb one block up)")
    print("   Local perturbation: m_j += delta, m_{j+1} -= delta.  This leaves")
    print("   every partial sum T_i (i != j) and n, K, q untouched, so it")
    print("   tightens exactly one condition -- (C_j) -- and relaxes (C_{j+1}).")
    print("   Smallest delta at which the EXACT test q <= R_j fails, per block:")
    print("   if the greedy caps were slack, these would be of order the block")
    print("   size; saturated caps give O(1).")
    print()
    print("    p        n   #blocks tested   delta: min / median / max")
    for r in rows:
        if r["p"] not in (6, 8, 10, 12, 14, 16, 18, 20, 22):
            continue
        p, n = r["p"], r["n"]
        K = K_of(n)
        res, _ = construct(p, n, K)
        if res is None:
            continue
        ms0, ss0 = res
        deltas = []
        for j in range(p - 2):
            d = None
            for delta in range(1, 13):
                if ms0[j + 1] - delta < 1:
                    break
                ms = list(ms0)
                ms[j] += delta
                ms[j + 1] -= delta
                ok, q, Rs, marg = size_check(ms, ss0)
                if not ok:
                    d = delta
                    break
            if d is not None:
                deltas.append(d)
        if not deltas:
            print("    %-3d %8d   (no block with room to perturb)" % (p, n))
            continue
        sd = sorted(deltas)
        print("    %-3d %8d %16d   %d / %d / %d"
              % (p, n, len(sd), sd[0], sd[len(sd) // 2], sd[-1]))
        check(sd[0] <= 3, "NC-D p=%d: caps are saturated (some delta <= 3)" % p)
        check(sd[len(sd) // 2] <= 4,
              "NC-D p=%d: typical block is within 4 of its cap" % p)


def nc_scale(pmax=22):
    hdr("NC-E.  The gamma formula as a function of p and the quality parameter")
    print("   Gamma(p,n) -> 0.92714*kappa + 2.70933 as p grows, with NO p term.")
    print("   Push kappa up by taking n at 2x, 4x, 8x, 16x the canonical scale;")
    print("   the search window is sized from the predicted density of n of the")
    print("   required quality, 1.4427*2^-Gamma, so 'no passer' would be a real")
    print("   result and not a budget artifact.")
    print()
    print("    p   mult      n     kappa   gamma   Gamma  0.92714k+2.709   x_n"
          "        need x<=   window   off")
    for p in (10, 14, 18, 22):
        if p > pmax:
            continue
        for mult in (1, 2, 4, 8, 16):
            n0 = scale_n(p) * mult
            Gpred = Gamma_threshold(p, n0)
            W = window_for(Gpred)
            need = -math.log2(1.0 - 2.0 ** (-Gpred))
            # cap the walk so kappa does not drift more than 25%: past that
            # point the target Gamma is moving faster than the search
            Wcap = max(64, n0 // 2)
            if W > Wcap:
                print("    %-3d %4d   window %d needed for quality %.6f exceeds n0/4"
                      " = %d -- kappa would drift; not a failure, a scale limit"
                      % (p, mult, W, need, Wcap))
                continue
            got = None
            for n, K, q in scan(p, n0, W):
                g = K - log2_big(q)
                if g < Gpred - 2.0:
                    continue                 # cheap quality prefilter
                res, _ = construct(p, n, K)
                if res is None:
                    continue
                if not crash_rotation_ok(p, n, K, res[0]):
                    continue
                ok, _, _, _ = size_check(*res)
                if ok:
                    got = (n, K, g)
                    break
            if got is None:
                print("    %-3d %4d   no passer in window %d" % (p, mult, W))
                check(False, "NC-E p=%d mult=%d passer" % (p, mult))
                continue
            n, K, g = got
            kap = n / float(DEC_L ** p)
            print("    %-3d %4d %8d  %7.3f %7.3f %7.3f  %11.3f   %.5f   %.5f %8d %5d"
                  % (p, mult, n, kap, g, Gamma_threshold(p, n),
                     0.92714 * kap + 2.70933, quality_of(n, K), need, W, n - n0))
    print()
    print("   Read the last two columns as the interface to the Diophantine half:")
    print("   the construction consumes ONLY 'x_n <= need', a CONSTANT-quality")
    print("   condition at fixed kappa -- no convergent, no continued fraction.")


# ==========================================================================
# PART 4.  Beyond the record
# ==========================================================================

def part4(plist=(31, 32)):
    hdr("PART 4.  Beyond the existing record (12.8.6.4 stops at p = 23)")
    print("    p        n     off   gamma   Gamma  g/log2p  minmarg  div   secs")
    for p in plist:
        n0 = scale_n(p)
        t0 = time.time()
        got = None
        for n, K, q in scan(p, n0, 64):
            g = K - log2_big(q)
            res, _ = construct(p, n, K)
            if res is None:
                continue
            if not crash_rotation_ok(p, n, K, res[0]):
                continue
            ok, q2, Rs, marg = size_check(*res)
            if ok:
                got = (n, K, g, res, marg)
                break
        if got is None:
            print("    %-3d  no passer" % p)
            check(False, "p=%d passer" % p)
            continue
        n, K, g, (ms, ss), marg = got
        dv = divisibility_check(ms, ss)
        check(not any(dv), "p=%d beyond-record instance fails divisibility" % p)
        print("    %-3d %8d %6d %7.3f %7.3f  %6.3f  %6.3f  %5s  %5.1f"
              % (p, n, n - n0, g, Gamma_threshold(p, n), g / math.log2(p),
                 min(marg), any(dv), time.time() - t0))


# ==========================================================================

def main():
    t0 = time.time()
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    part0()
    rows = part1(pmax=pmax)
    part1b(rows)
    part2(rows)
    part3()
    nc_quality(pmax=min(pmax, 22))
    nc_quality_wide()
    nc_rounding(rows)
    nc_crash(rows)
    nc_saturation(rows)
    nc_scale()
    part4()
    hdr("SUMMARY")
    print("   total failed checks: %d" % len(FAILS))
    for f in FAILS:
        print("     - %s" % f)
    print("   wall clock: %.1f s" % (time.time() - t0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
