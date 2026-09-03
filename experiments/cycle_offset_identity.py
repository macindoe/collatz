#!/usr/bin/env python3
"""cycle_offset_identity.py -- the parked cycle condition is Tao's n-Syracuse
offset map evaluated mod q: the exact identity between cycles.md 12.6.1's
rotation numerator R_0 and Tao's F_n(a) (arXiv:1909.03562v7, eq. 1.5 p.5) on
arbitrary profiles, the divisibility biconditional, the known cycles recovered
from their valuation words, the p = 7 staircase, and 12.6.1.4's repetition
factor.

Supports: cycles.md Remark 12.6.1.7. Filed from the fresh-eyes assessment of
2026-09-04 (briefs/fresh-eyes-assessment-findings.md, finding 4).

Objects.  A profile is (m_t, s_t)_{t<p} with entries >= 1, no closure imposed.
  n = sum m_t,  K = n + sum s_t,  q = 2^K - 3^n   (either sign; never 0).
  R_0 = sum_t 3^{M_t} 2^{S_t} (2^{s_t} - 1),  M_t = sum_{j>t} m_j,
        S_t = sum_{j<t} sigma_j,  sigma_j = s_j + m_{(j+1) mod p}     (12.6.1)
  a = the Syracuse valuation word read from block 0: block (m_t, s_t)
      contributes (1, ..., 1, 1 + s_t), m_t entries; so len(a) = n, |a| = K.
  F_n(a) = sum_{i=1}^{n} 3^{n-i} 2^{-a_{[i,n]}}                     (Tao 1.5)
The identity, on every profile:   2^{m_0} R_0 = 2^K F_n(a) + q.
Derivation: on a cycle, R_0 = u_0 q with u_0 the odd seed of block 0's entry
e_0 = 2^{m_0} u_0 - 1 (12.6.1 gives R_0 = omega_0 3^{a_{p-1}} q, and
omega_0 3^{a_{p-1}} = u_0); Tao's eq. 1.7 at x = e_0 with Syr^n(e_0) = e_0
gives e_0 q = 2^K F_n(a). Substituting e_0 gives the display, which is then a
polynomial identity in the profile and needs no closure. In the record it is
the seam identity of Remark 12.6.1.1 / itinerary.md 14.15.9.2 (integer form),
N_0 + q = 2^{m_0} R_0, with the mirror-frame numerator N_0 = 2^K F_n(a): the
constant term of the composed block maps y -> (3^m y + 3^m - 2^m)/2^{m+s},
cleared of denominators -- checked here by composing those maps directly.
Consequence: q | R_0  <=>  2^K F_n(a) = 0 (mod q), since 2 is a unit mod q.

Fresh code: imports nothing from any other script here; exact integer and
rational arithmetic at every pass/fail decision. Deterministic (seed 1); a
re-run from the repo root reproduces
experiments/cycle_offset_identity_output.txt byte for byte.

  PART 1  3000 random profiles (p <= 6, entries 1..6): the identity, the
          composed-block-map numerator N_0 = 2^K F_n(a), the biconditional
  PART 2  the known cycles from their valuation words: x = 2^K F_n(a)/q
          returns 1, -5, -17; the block dictionary agrees with direct
          Syracuse iteration; R_0 = u_0 q
  PART 3  the p = 7 staircase of 12.8.3 fails both conditions; gcd(q, R_r) = 7
          at every rotation, as 12.6.1.6 records
  PART 4  12.6.1.4's repetition factor G_k carries over to the offset:
          2^{K_P} F(a^k) = G_k 2^{K_B} F(a)
"""

import os
import random
import sys
from fractions import Fraction
from math import gcd

DATE = "2026-09-04"          # assessment date; fixed so that re-runs are byte-identical
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "cycle_offset_identity_output.txt")
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


def R0(ms, ss):
    """cycles.md 12.6.1, rotation r = 0."""
    p = len(ms)
    sig = [ss[t] + ms[(t + 1) % p] for t in range(p)]
    return sum(3 ** sum(ms[t + 1:]) * 2 ** sum(sig[:t]) * (2 ** ss[t] - 1) for t in range(p))


def syr_word(ms, ss):
    """Block (m, s) -> Syracuse valuations (1, ..., 1, 1 + s), m entries."""
    a = []
    for m, s in zip(ms, ss):
        a += [1] * (m - 1) + [1 + s]
    return a


def F_tao(a):
    """Tao (1.5): F_n(a) = sum_{i=1}^{n} 3^{n-i} 2^{-a_{[i,n]}}."""
    n = len(a)
    return sum(Fraction(3 ** (n - i), 2 ** sum(a[i - 1:])) for i in range(1, n + 1))


def block_map(m, s):
    """The block on the odd integer: entry y = 2^m u - 1 -> cascade 3^m u - 1 ->
    exit (3^m u - 1)/2^s, i.e. y -> A y + B with A = 3^m/2^{m+s},
    B = (3^m - 2^m)/2^{m+s}."""
    return Fraction(3 ** m, 2 ** (m + s)), Fraction(3 ** m - 2 ** m, 2 ** (m + s))


def composed(ms, ss):
    """Composite of the block maps, block 0 applied first: y -> A y + B."""
    A, B = Fraction(1), Fraction(0)
    for m, s in zip(ms, ss):
        a, b = block_map(m, s)
        A, B = a * A, a * B + b
    return A, B


def profile_data(ms, ss):
    n = sum(ms)
    K = sum(ss) + n
    q = 2 ** K - 3 ** n
    a = syr_word(ms, ss)
    assert len(a) == n and sum(a) == K
    f = F_tao(a) * 2 ** K
    assert f.denominator == 1
    return n, K, q, a, f.numerator


def syr(x):
    y = 3 * x + 1
    v = v2(y)
    return y >> v, v


def blocks_of_cycle(x0):
    """Block-decompose the odd cycle through x0 (positive or negative):
    returns (ms, ss, us, entries)."""
    ms, ss, us, es = [], [], [], []
    x = x0
    while True:
        es.append(x)
        m = v2(x + 1)
        u = (x + 1) >> m                     # e = 2^m u - 1, u odd, either sign
        casc = 3 ** m * u - 1
        s = v2(casc)
        x = casc >> s
        ms.append(m)
        ss.append(s)
        us.append(u)
        if x == x0:
            return ms, ss, us, es


def main():
    say("cycle_offset_identity.py -- assessment date %s" % DATE)
    say()

    # ---------------------------------------------------------------- PART 1
    say("PART 1 -- 3000 random profiles, p in 1..6, entries m_t, s_t in 1..6, no closure")
    random.seed(1)
    tot = bad = bad_map = agree = ndiv = nneg = 0
    divs = {}
    for _ in range(3000):
        p = random.randrange(1, 7)
        ms = [random.randrange(1, 7) for _ in range(p)]
        ss = [random.randrange(1, 7) for _ in range(p)]
        n, K, q, a, f = profile_data(ms, ss)
        r0 = R0(ms, ss)
        tot += 1
        if 2 ** ms[0] * r0 != f + q:
            bad += 1
        A, B = composed(ms, ss)
        if A != Fraction(3 ** n, 2 ** K) or B * 2 ** K != f:
            bad_map += 1
        if (r0 % q == 0) == (f % q == 0):
            agree += 1
        if r0 % q == 0:
            ndiv += 1
            key = (tuple(ms), tuple(ss), Fraction(f, q))
            divs[key] = divs.get(key, 0) + 1
        if q < 0:
            nneg += 1
    say("  profiles %d (q < 0 on %d of them; q | R_0 on %d)" % (tot, nneg, ndiv))
    say("  the profiles with q | R_0, and the integer x = 2^K F_n(a)/q each returns (count in the sample):")
    for key in sorted(divs, key=lambda t: (len(t[0]), t)):
        say("    m = %s, s = %s: x = %s  (x%d)" % (list(key[0]), list(key[1]), key[2], divs[key]))
    KNOWN = {1, -1, -5, -7, -17, -25, -37, -55, -41, -61, -91}
    check("every divisible profile returns an element of a known cycle ({1}, {-1}, {-5, -7}, the period-7 negative cycle)",
          all(x.denominator == 1 and x.numerator in KNOWN for (_, _, x) in divs))
    check("identity 2^{m_0} R_0 = 2^K F_n(a) + q on every profile", bad == 0, "%d failures" % bad)
    check("the composed block maps give Aff_a exactly: slope 3^n/2^K, constant F_n(a); so N_0 = 2^K F_n(a)",
          bad_map == 0, "%d failures" % bad_map)
    check("biconditional q | R_0  <=>  q | 2^K F_n(a): agreement %d/%d" % (agree, tot), agree == tot)
    say()

    # ---------------------------------------------------------------- PART 2
    say("PART 2 -- the known cycles, from their valuation words (Lagarias 1985 lists them; Boehm-Sontacchi 1978 is the classical cycle equation)")
    for x0 in (1, -5, -17):
        ms, ss, us, es = blocks_of_cycle(x0)
        n, K, q, a, f = profile_data(ms, ss)
        # direct Syracuse iteration for n odd steps
        x = x0
        word = []
        for _ in range(n):
            x, v = syr(x)
            word.append(v)
        r0 = R0(ms, ss)
        xr = Fraction(f, q)
        say("  x0 = %d: blocks (m, s) = %s, entries %s; a = %s, n = %d, K = %d, q = %d; 2^K F_n(a)/q = %s"
            % (x0, list(zip(ms, ss)), es, a, n, K, q, xr))
        check("x0 = %d: the block dictionary word equals the direct Syracuse valuation word, and Syr^n returns to x0" % x0,
              word == a and x == x0)
        check("x0 = %d: x = 2^K F_n(a)/q returns the cycle element" % x0, xr == x0)
        check("x0 = %d: R_0 = u_0 q with u_0 = %d, and the identity holds" % (x0, us[0]),
              r0 == us[0] * q and 2 ** ms[0] * r0 == f + q)
    say()

    # ---------------------------------------------------------------- PART 3
    say("PART 3 -- the p = 7 staircase of 12.8.3: m = (4, 7, 9, 15, 23, 35, 1), s = (1, 1, 1, 1, 1, 1, 49)")
    ms = [4, 7, 9, 15, 23, 35, 1]
    ss = [1, 1, 1, 1, 1, 1, 49]
    n, K, q, a, f = profile_data(ms, ss)
    r0 = R0(ms, ss)
    say("  n = %d, K = %d, q = 2^%d - 3^%d > 0 with bit length %d" % (n, K, K, n, q.bit_length()))
    check("K = 149 is the ceiling: 2^148 < 3^94 < 2^149", 2 ** 148 < 3 ** 94 < 2 ** 149)
    check("identity holds on the staircase", 2 ** ms[0] * r0 == f + q)
    check("q does not divide R_0, and q does not divide 2^K F_n(a) (both conditions fail together)",
          r0 % q != 0 and f % q != 0)
    gs = []
    for r in range(7):
        gs.append(gcd(q, R0(ms[r:] + ms[:r], ss[r:] + ss[:r])))
    check("gcd(q, R_r) = 7 at every rotation (12.6.1.6)", all(g == 7 for g in gs), "gcds %s" % gs)
    say()

    # ---------------------------------------------------------------- PART 4
    say("PART 4 -- 12.6.1.4's repetition factor on the offset: for P = B^k,")
    say("  G_k = sum_{c<k} 3^{(k-1-c) n_B} 2^{c K_B},  q_P = q_B G_k,  R_0(P) = R_0(B) G_k,  and  2^{K_P} F(a^k) = G_k 2^{K_B} F(a)")
    fails = cases = 0
    for _ in range(50):
        ell = random.randrange(1, 5)
        msB = [random.randrange(1, 6) for _ in range(ell)]
        ssB = [random.randrange(1, 6) for _ in range(ell)]
        nB, KB, qB, aB, fB = profile_data(msB, ssB)
        for k in (2, 3):
            nP, KP, qP, aP, fP = profile_data(msB * k, ssB * k)
            G = sum(3 ** ((k - 1 - c) * nB) * 2 ** (c * KB) for c in range(k))
            cases += 1
            if not (qP == qB * G and R0(msB * k, ssB * k) == R0(msB, ssB) * G and fP == G * fB and aP == aB * k):
                fails += 1
    check("repetition factor: q, R_0 and 2^K F_n(a) all scale by G_k on %d (B, k) pairs" % cases, fails == 0,
          "%d failures" % fails)
    say()

    say("SUMMARY: %d checks, %d failures%s" % (CHECKS, len(FAILS),
                                                (": " + "; ".join(FAILS)) if FAILS else ""))
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(LINES) + "\n")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
