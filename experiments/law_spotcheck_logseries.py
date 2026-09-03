#!/usr/bin/env python3
"""law_spotcheck_logseries.py -- fresh-code spot check of the core forward laws
with an INDEPENDENT anchor implementation: the 2-adic logarithm computed by its
power series in exact rationals, not by the discrete-log tower every other
script in this directory uses.

Supports: spine.md 9.8 (the reduced map F and the p-step unrolling used at
cycles.md 12.6.1), stage1-synthesis.md 11.8.4.1 (global valuation law; the
calibration values are the remark after 11.8.3.6.6), stage3.md 11.8.6.3
(entry-depth law), stage2.md 11.8.5.6 / stage4.md 11.8.7 (anchor increment
identity), cycles.md 12.6.1 (unrolled identity). Filed from the fresh-eyes
assessment of 2026-09-04 (briefs/fresh-eyes-assessment-findings.md, finding 1).

Fresh code: imports nothing from any other script in this repository; every
law was re-implemented from its statement. Exact integer and rational
arithmetic at every pass/fail decision (no floating point anywhere).
Deterministic (seed 20260904); a re-run from the repo root reproduces
experiments/law_spotcheck_logseries_output.txt byte for byte.

The anchor.  For u = 1 (mod 8), log u = sum_{i>=1} (-1)^{i+1} (u-1)^i / i;
each term is a 2-adic integer of valuation >= 3i - v_2(i), partial sums are
rationals with odd denominators, reduced mod 2^K by inverting the denominator.
N(u) = -log u / log 9 (mod 2^K), with v_2(log 9) = 3; the orbit anchor is
M(w) = N(w^2).

  PART 0  calibration: the series anchor must reproduce the published
          N(17) = 38, N(25) = 245, N(33) = 236 (mod 2^8)
  PART 1  the global valuation law: on the lifting classes (w mod 8, d mod 2)
          in {(1,0), (3,1)}, s = 2 + v_2(d - M(w)); the mod-8 table off them
  PART 2  the entry-depth law m_+ = v_2(x_exit + 1) on all six classes
  PART 3  the increment identity  M(w_+) - M(w) = N((w_+/w)^2)  (mod 2^24)
  PART 4  an independently derived unrolled p-step identity, p <= 8, and its
          corollary (w_p mod 3^(m_1+..+m_p+d_0-d_p) is a function of the
          letter word alone)
"""

import os
import random
import sys
from fractions import Fraction

DATE = "2026-09-04"          # assessment date; fixed so that re-runs are byte-identical
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "law_spotcheck_logseries_output.txt")
LINES = []
CHECKS = 0
FAILS = []


def say(s=""):
    print(s)
    LINES.append(s)


def check(label, ok, detail=""):
    global CHECKS
    CHECKS += 1
    if not ok:
        FAILS.append(label)
    say("  [%s] %s%s" % ("PASS" if ok else "FAIL", label,
                         ("  (" + detail + ")") if detail else ""))


def v2(x):
    return (x & -x).bit_length() - 1


def v3(x):
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def log2adic(u, K):
    """2-adic log of the integer u = 1 (mod 8), as a residue mod 2^K, by the
    series sum_{i>=1} (-1)^{i+1} (u-1)^i / i in exact rationals."""
    assert u % 8 == 1, u
    x = u - 1
    tot = Fraction(0)
    i = 1
    # term i has valuation >= 3i - v_2(i) >= 3i - bit_length(i) + 1; stop once that exceeds K + 2
    while 3 * i - i.bit_length() <= K + 2:
        tot += Fraction(x ** i, i) * (1 if i % 2 else -1)
        i += 1
    M = 1 << K
    assert tot.denominator % 2 == 1
    return (tot.numerator % M) * pow(tot.denominator % M, -1, M) % M


def N_mod(u, K):
    """N(u) = -log u / log 9  (mod 2^K), for u = 1 (mod 8)."""
    lu = log2adic(u, K + 3)
    l9 = log2adic(9, K + 3)
    assert lu % 8 == 0 and l9 % 8 == 0 and (l9 // 8) % 2 == 1
    M = 1 << K
    return (-(lu // 8) * pow(l9 // 8, -1, M)) % M


def M_mod(w, K):
    """Orbit anchor M(w) = N(w^2) (mod 2^K)."""
    return N_mod(w * w, K)


def F(w, d):
    """One reduced step (spine.md 9.8): returns (w_+, d_+, s, sigma, a_+)."""
    A = 3 ** d * w - 1
    s = v2(A)
    C = A + (1 << s)
    sig = v2(C)
    a = v3(C >> sig)
    return (C >> sig) // 3 ** a, sig - s + a, s, sig, a


def main():
    say("law_spotcheck_logseries.py -- assessment date %s" % DATE)
    say("anchor: 2-adic log SERIES in exact rationals, independent of the discrete-log tower")
    say()

    # ---------------------------------------------------------------- PART 0
    say("PART 0 -- calibration against the published values (stage1-synthesis.md, remark after 11.8.3.6.6)")
    for u, want in ((17, 38), (25, 245), (33, 236)):
        got = N_mod(u, 8)
        check("N(%d) = %d (mod 2^8)" % (u, want), got == want, "series gives %d" % got)
    check("N(17) = 6 (mod 8), the first visible lifting class of the family w = 17",
          N_mod(17, 8) % 8 == 6)
    say()

    random.seed(20260904)
    K = 40
    LIFT = {(1, 0), (3, 1)}                     # (w mod 8, d mod 2): the two lifting classes
    S1 = {(1, 1), (5, 1), (7, 0), (3, 0)}       # off-lifting classes with s = 1; the other two have s = 2

    # ---------------------------------------------------------------- PART 1
    say("PART 1 -- global valuation law: 4000 random states, w < 2^40 odd with 3 not dividing w, 1 <= d < 80, K = %d" % K)
    n_lift = n_off = fails = 0
    for _ in range(4000):
        w = random.randrange(1, 1 << 40, 2)
        if w % 3 == 0:
            continue
        d = random.randrange(1, 80)
        s = v2(3 ** d * w - 1)
        cls = (w % 8, d % 2)
        if cls in LIFT:
            Mw = M_mod(w, K)
            eps = (d - Mw) % (1 << K)
            if eps == 0 or s >= K - 2:
                continue
            pred = 2 + v2(eps)
            n_lift += 1
        else:
            pred = 1 if cls in S1 else 2
            n_off += 1
        if pred != s:
            fails += 1
    say("  lifting classes %d states, off-lifting %d states, failures %d" % (n_lift, n_off, fails))
    check("valuation law: 0 failures on %d states" % (n_lift + n_off), fails == 0)
    say()

    # ---------------------------------------------------------------- PART 2
    say("PART 2 -- entry-depth law m_+ = v_2(x_exit + 1) on all six classes (stage3.md 11.8.6.3), 4000 random states")
    n = fails = 0
    for _ in range(4000):
        w = random.randrange(1, 1 << 40, 2)
        if w % 3 == 0:
            continue
        d = random.randrange(1, 80)
        A = 3 ** d * w - 1
        s = v2(A)
        xexit = A >> s
        m_plus = v2(xexit + 1)
        if m_plus >= K - 4:
            continue
        cls = (w % 8, d % 2)
        Mw = M_mod(w, K)
        MOD = 1 << K
        if cls in LIFT:
            param = w if cls == (1, 0) else 3 * w      # companion anchor on the odd component
            nn = d // 2
            eps = (nn - N_mod(param, K)) % MOD
            if s >= K - 4:
                continue
            delta = N_mod(1 - (1 << s), K)             # shift constant delta_s (s >= 3 on the lifting classes)
            t = (eps + delta) % MOD
            pred = 3 - s + v2(t)
        elif s == 1:
            pred = 1 + v2((d - Mw) % MOD)
        else:
            pred = v2((d - 1 - Mw) % MOD)
        n += 1
        if pred != m_plus:
            fails += 1
    say("  %d states, failures %d" % (n, fails))
    check("entry-depth law: 0 failures on %d states" % n, fails == 0)
    say()

    # ---------------------------------------------------------------- PART 3
    say("PART 3 -- increment identity  M(w_+) - M(w) = N((w_+/w)^2)  (mod 2^24), 2000 random steps, w < 2^30, d < 40")
    n = fails = 0
    for _ in range(2000):
        w = random.randrange(1, 1 << 30, 2)
        if w % 3 == 0:
            continue
        d = random.randrange(1, 40)
        wp, dp, s, sig, a = F(w, d)
        k = 24
        BIG = 1 << (k + 20)
        ratio = (wp * pow(w, -1, BIG)) % BIG           # a representative of w_+/w in Z_2
        lhs = (M_mod(wp, k) - M_mod(w, k)) % (1 << k)
        rhs = N_mod((ratio * ratio) % BIG, k)
        n += 1
        if lhs != rhs:
            fails += 1
    say("  %d steps, failures %d" % (n, fails))
    check("increment identity mod 2^24: 0 failures on %d steps" % n, fails == 0)
    say()

    # ---------------------------------------------------------------- PART 4
    say("PART 4 -- unrolled p-step identity, 500 random orbits, w_0 < 2^60, d_0 < 12, 1 <= p <= 8")
    say("  step:  2^sigma_t 3^a_t w_{t+1} = 3^{d_t} w_t + (2^{s_t} - 1),  m_{t+1} = sigma_t - s_t")
    say("  hence  3^{d_p} w_p 2^{sum sigma} = 3^{m_1+..+m_p} 3^{d_0} w_0")
    say("                                   + sum_t (2^{s_t} - 1) 3^{m_{t+1}+..+m_p} 2^{sigma_0+..+sigma_{t-1}}")
    n = fails = 0
    for _ in range(500):
        w = random.randrange(1, 1 << 60, 2)
        if w % 3 == 0:
            continue
        d0 = random.randrange(1, 12)
        p = random.randrange(1, 9)
        ws, ds, ss, sigs, ms = [w], [d0], [], [], []
        for t in range(p):
            wp, dp, s, sig, a = F(ws[-1], ds[-1])
            ws.append(wp)
            ds.append(dp)
            ss.append(s)
            sigs.append(sig)
            ms.append(sig - s)
        lhs = 3 ** ds[p] * ws[p] * 2 ** sum(sigs)
        rhs = 3 ** (sum(ms) + d0) * w
        for t in range(p):
            rhs += (2 ** ss[t] - 1) * 3 ** sum(ms[t:]) * 2 ** sum(sigs[:t])
        n += 1
        if lhs != rhs:
            fails += 1
    say("  %d orbits, failures %d" % (n, fails))
    check("unrolled identity, p <= 8: 0 failures on %d orbits" % n, fails == 0)
    say("  corollary: w_p mod 3^(m_1+..+m_p + d_0 - d_p) is a function of the letter word (m_t, s_t) alone")
    say()

    say("SUMMARY: %d checks, %d failures%s" % (CHECKS, len(FAILS),
                                                (": " + "; ".join(FAILS)) if FAILS else ""))
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(LINES) + "\n")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
