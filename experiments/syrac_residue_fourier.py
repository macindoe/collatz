#!/usr/bin/env python3
"""syrac_residue_fourier.py -- the 3-adic side of the parked cycle condition:
Tao's Syracuse random variables Syrac(Z/3^j) computed exactly, their Fourier
coefficients grouped by j - v_3(xi), and real orbits far past the digit budget
against that law.

Supports: cycles.md Remark 12.6.1.7 (the rotation numerator as Tao's offset;
one object, two moduli) and, read-only, the Tao attribution at aeh.md 13.6.5.
Filed from the fresh-eyes assessment of 2026-09-04
(briefs/fresh-eyes-assessment-findings.md, finding 3).

Tao, arXiv:1909.03562v7 (Forum Math. Pi 10 (2022) e12): eq. (1.5) p.5, the
n-Syracuse offset F_n(a) = sum_{m=1}^{n} 3^{n-m} 2^{-a_{[m,n]}}; eq. (1.22) p.9,
Syrac(Z/3^n) = F_n(Geom(2)^n) mod 3^n; Lemma 1.12 p.10, the recursion from
Syrac(Z/3^n) to Syrac(Z/3^{n+1}), with Syrac(Z/9) printed as
(0, 8, 16, 0, 11, 4, 0, 2, 22)/63; eq. (1.23) p.10, projection consistency;
Prop 1.14 p.11, fine-scale mixing (eqs. 1.26-1.27); Prop 1.17 p.12, decay of
the characteristic function at xi not divisible by 3 (eq. 1.28).

Fresh code: imports nothing from any other script here. The laws are exact
rationals and every pass/fail decision is an exact comparison; total-variation
distances and Fourier magnitudes are printed as floats (descriptive).
Deterministic (seed 11 for the orbit sample); a re-run from the repo root
reproduces experiments/syrac_residue_fourier_output.txt byte for byte.

  PART 1  the law, two ways, exactly: the j-step pushforward of a point mass
          under r -> (3r+1) 2^{-a} mod 3^j with weight 2^{-a} (any start is
          forgotten after j steps, eq. 1.21), against Tao's Lemma 1.12
          recursion; stationarity; projection consistency (1.23); the printed
          Syrac(Z/9); total variation from uniform-on-units
  PART 2  Fourier coefficients |pi^(xi)| grouped by f = j - v_3(xi), the
          number of fine digits (the dependence on f alone is exact, by 1.23);
          the top-digit conditional given the lower digits (Prop 1.14 in
          one-digit form)
  PART 3  real 64-bit orbits at Syracuse steps 35..120 (past the ~32-step
          budget): the empirical law of x_t mod 3^j against the exact law and
          against uniform-on-units
"""

import cmath
import math
import os
import random
import sys
from fractions import Fraction

DATE = "2026-09-04"          # assessment date; fixed so that re-runs are byte-identical
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "syrac_residue_fourier_output.txt")
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


def v3(x):
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def clean(pi):
    return {r: p for r, p in pi.items() if p != 0}


def chain_law(lev):
    """Syrac(Z/3^lev) as the exact lev-step pushforward of a point mass under
    r -> (3r+1) 2^{-a} mod 3^lev, weight 2^{-a}, a >= 1; exponents grouped by
    their class mod L = ord(2 mod 3^lev) = 2 * 3^{lev-1}. Returns (law, one more
    step of the law) so that stationarity can be checked exactly."""
    M = 3 ** lev
    L = 2 * 3 ** (lev - 1)
    inv2 = pow(2, -1, M)
    wts = {}
    for c in range(1, L + 1):                # total weight of the exponents a = c (mod L)
        wts[c % L] = Fraction(2 ** (L - c), 2 ** L - 1)
    pw = {c: pow(inv2, c, M) for c in range(L)}

    def push(pi):
        new = {}
        for r, p in pi.items():
            base = (3 * r + 1) % M
            for c, wt in wts.items():
                key = (base * pw[c]) % M
                new[key] = new.get(key, Fraction(0)) + p * wt
        return clean(new)

    pi = {1: Fraction(1)}
    for _ in range(lev):
        pi = push(pi)
    return pi, push(pi)


def tao_recursion(jmax):
    """Lemma 1.12: P(Syrac(Z/3^{n+1}) = x) = sum_{1<=a<=2*3^n, 2^a x = 1 mod 3}
    2^{-a} P(Syrac(Z/3^n) = (2^a x - 1)/3) / (1 - 2^{-2*3^n})."""
    laws = {0: {0: Fraction(1)}}
    for n in range(jmax):
        M = 3 ** n
        Mn = 3 * M
        prev = laws[n]
        L = 2 * M
        denom = 1 - Fraction(1, 2 ** L)
        new = {}
        for x in range(Mn):
            tot = Fraction(0)
            for a in range(1, L + 1):
                if (pow(2, a, 3) * x) % 3 != 1:
                    continue
                y = ((pow(2, a, Mn) * x - 1) % Mn) // 3     # (2^a x - 1)/3 as an element of Z/3^n
                tot += Fraction(1, 2 ** a) * prev.get(y % M, Fraction(0))
            if tot:
                new[x] = tot / denom
        laws[n + 1] = new
    return laws


def project(pi, lev_to):
    M = 3 ** lev_to
    out = {}
    for r, p in pi.items():
        out[r % M] = out.get(r % M, Fraction(0)) + p
    return clean(out)


def tv_uniform_units(pi, lev):
    M = 3 ** lev
    u = Fraction(1, 2 * 3 ** (lev - 1))
    return Fraction(1, 2) * sum(abs(pi.get(r, Fraction(0)) - (u if r % 3 else 0)) for r in range(M))


def fourier_groups(pi, lev):
    """|sum_r pi(r) e^{2 pi i xi r / 3^lev}| for xi = 1..3^lev - 1, grouped by
    f = lev - v_3(xi), the number of fine digits xi sees."""
    M = 3 ** lev
    groups = {}
    for xi in range(1, M):
        c = abs(sum(float(p) * cmath.exp(2j * math.pi * xi * r / M) for r, p in pi.items()))
        groups.setdefault(lev - v3(xi), []).append(c)
    return groups


def main():
    say("syrac_residue_fourier.py -- assessment date %s" % DATE)
    say()

    JMAX = 5
    laws = tao_recursion(JMAX)
    chain = {}

    # ---------------------------------------------------------------- PART 1
    say("PART 1 -- the law Syrac(Z/3^j), exactly, j = 1..%d" % JMAX)
    for lev in range(1, JMAX + 1):
        pi, pi_next = chain_law(lev)
        chain[lev] = pi
        check("j=%d: chain pushforward (%d steps from a point mass) = Tao's Lemma 1.12 recursion, exactly" % (lev, lev),
              pi == clean(laws[lev]))
        check("j=%d: the law is stationary under one more step, exactly" % lev, pi_next == pi)
        if lev > 1:
            check("j=%d: projection to Z/3^%d is Syrac(Z/3^%d), exactly (eq. 1.23)" % (lev, lev - 1, lev - 1),
                  project(pi, lev - 1) == chain[lev - 1])
    tao_mod9 = [Fraction(v, 63) for v in (0, 8, 16, 0, 11, 4, 0, 2, 22)]
    got9 = [chain[2].get(r, Fraction(0)) for r in range(9)]
    check("Syrac(Z/9) = (0, 8, 16, 0, 11, 4, 0, 2, 22)/63 as printed by Tao (p.10)", got9 == tao_mod9,
          "computed " + ", ".join(str(v) for v in got9))
    say("  total variation from uniform on the units of Z/3^j (the law is supported on the units and is not uniform):")
    for lev in range(1, JMAX + 1):
        say("    j=%d: TV(Syrac(Z/3^%d), Unif(units)) = %.4f" % (lev, lev, float(tv_uniform_units(chain[lev], lev))))
    say()

    # ---------------------------------------------------------------- PART 2
    say("PART 2 -- Fourier coefficients |pi^(xi)| of Syrac(Z/3^j), grouped by f = j - v_3(xi) (fine digits seen by xi)")
    groups = {lev: fourier_groups(chain[lev], lev) for lev in range(1, JMAX + 1)}
    say("  max |pi^(xi)| over the group:")
    say("    f \\ j " + "".join("%9d" % lev for lev in range(1, JMAX + 1)))
    for f in range(1, JMAX + 1):
        say("    %3d   " % f + "".join(("%9.4f" % max(groups[lev][f])) if f in groups[lev] else "%9s" % "" for lev in range(1, JMAX + 1)))
    say("  mean |pi^(xi)| over the group:")
    say("    f \\ j " + "".join("%9d" % lev for lev in range(1, JMAX + 1)))
    for f in range(1, JMAX + 1):
        say("    %3d   " % f + "".join(("%9.4f" % (sum(groups[lev][f]) / len(groups[lev][f]))) if f in groups[lev] else "%9s" % "" for lev in range(1, JMAX + 1)))
    say("  group sizes at j=%d: %s" % (JMAX, ", ".join("f=%d: %d" % (f, len(groups[JMAX][f])) for f in sorted(groups[JMAX]))))
    spread = 0.0
    for f in range(1, JMAX + 1):
        vals = [max(groups[lev][f]) for lev in range(f, JMAX + 1)]
        spread = max(spread, max(vals) - min(vals))
        vals = [sum(groups[lev][f]) / len(groups[lev][f]) for lev in range(f, JMAX + 1)]
        spread = max(spread, max(vals) - min(vals))
    check("the coefficient statistics depend on f = j - v_3(xi) alone: spread across j < 1e-9 (float; exact by the projection identity above)",
          spread < 1e-9, "spread %.1e" % spread)
    say("  the unit frequencies (v_3(xi) = 0, f = j) carry the fine-scale content of Prop 1.17: mean |pi^(xi)| at j = 3, 4, 5 = %.4f, %.4f, %.4f"
        % tuple(sum(groups[lev][lev]) / len(groups[lev][lev]) for lev in (3, 4, 5)))
    say("  top digit given the lower j-1 digits (Prop 1.14 in one-digit form): TV of the conditional law from (1/3, 1/3, 1/3),")
    say("  mass-weighted mean and worst class")
    for lev in range(2, JMAX + 1):
        pi = chain[lev]
        M = 3 ** lev
        Ml = 3 ** (lev - 1)
        worst = Fraction(0)
        avg = Fraction(0)
        for low in range(Ml):
            mass = [pi.get(low + t * Ml, Fraction(0)) for t in range(3)]
            tot = sum(mass)
            if tot == 0:
                continue
            tv = Fraction(1, 2) * sum(abs(m / tot - Fraction(1, 3)) for m in mass)
            worst = max(worst, tv)
            avg += tv * tot
        say("    j=%d: mean TV %.4f, worst %.4f" % (lev, float(avg), float(worst)))
    say()

    # ---------------------------------------------------------------- PART 3
    say("PART 3 -- real orbits far past the digit budget")
    random.seed(11)

    def syr(x):
        y = 3 * x + 1
        return y >> ((y & -y).bit_length() - 1)

    b = 64
    steps = (35, 120)
    say("  %d-bit odd starts, 4000 per level; Syracuse steps %d..%d sampled (budget ~ b/2 = %d steps); visits below 2^20 dropped (kept bulk)"
        % (b, steps[0], steps[1], b // 2))
    for lev in (3, 4):
        M = 3 ** lev
        pi_f = {r: float(p) for r, p in chain[lev].items()}
        emp = [0] * M
        n = 0
        nlo = 0
        for _ in range(4000):
            x = random.getrandbits(b) | 1 | (1 << (b - 1))
            for t in range(steps[1]):
                x = syr(x)
                if t >= steps[0]:
                    if x < 2 ** 20:
                        nlo += 1
                        continue
                    emp[x % M] += 1
                    n += 1
        tv_pi = 0.5 * sum(abs(emp[r] / n - pi_f.get(r, 0.0)) for r in range(M))
        unif = 1 / (2 * 3 ** (lev - 1))
        tv_un = 0.5 * sum(abs(emp[r] / n - (unif if r % 3 else 0)) for r in range(M))
        say("    j=%d (mod %d): n=%d visits (dropped %d low): TV(empirical, Syrac law) = %.4f, TV(empirical, uniform on units) = %.4f  [sampling noise ~ %.4f]"
            % (lev, M, n, nlo, tv_pi, tv_un, math.sqrt(M / n) / 2))
    say("  (descriptive; the orbit statistics carry no pass/fail)")
    say()

    say("SUMMARY: %d checks, %d failures%s" % (CHECKS, len(FAILS),
                                                (": " + "; ".join(FAILS)) if FAILS else ""))
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(LINES) + "\n")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
