#!/usr/bin/env python3
"""
paper1_v4_readable_examples_check.py -- fresh check of the worked examples and quoted numbers in
the main text (Sections 1-6) of the readable rewrite of paper 1 v4 (paper/collatz-reduced-v4.tex,
branch paper1-v4-readable, commit d421851), for briefs/paper1-v4-readable-check-brief.md item 4.

Supports: briefs/paper1-v4-readable-check-findings.md section 4.

Written from the text of the paper alone (the main text and Definitions B.1, C.1, Proposition D.1,
Theorem D.6 and the proof of its part (iii)).  It imports nothing from the repository and reuses
no code from experiments/.  Exact integer / Fraction arithmetic for every pass/fail decision on
integers; mpmath at 400 significant digits for real constants and for p1(X0) (the comparisons
there are far from their thresholds; the margins are printed).

What it checks:
  A. Section 2: the x = 7 table (binary, factorisations), the rising-step identity
     T(x)+1 = (3/2)(x+1), "x ends in exactly m ones", the block 7, 11, 17 and exit 13 with s = 1,
     3*17+1 = 52 = 110100b, the one-division-map reading 7, 11, 17, 26, 13.
  B. Section 3: the representatives 7, 11, 17 of (1,3); the R-fibre of (1,1) is {1}; the state
     sequence (1,3) -> (7,1) -> (1,2) -> (1,1) with blocks beginning at 7, 13, 5, 1, computed both
     from the T-orbit and from the formulas of Definition B.1; F(1,1) = (1,1).
  C. Section 4: M(1) = 0; M(w) even iff w = +-1 mod 8; the eight-class table; the valuation law on
     the lifting classes; (1,2) has s = 3 and 3*5+1 = 16 halves four times; the displacement of
     Theorem C.5 equals (d - M(w))/2 (bearing on the paraphrase "the difference between the depth
     and the anchor"); the undecided-rate arithmetic 2^-(k+1).
  D. Section 5: the p = 7 staircase (n = 94, K = 149, last exit 49 = s_tot - 6, gamma = 6.74,
     all seven size tests, divisibility, the period-3 constant 0.1157n - 2 = 8.9, depth ratios,
     the sandwich of Theorem D.6(ii), the trim of Theorem D.5); the constants 3.683012, 5.140212,
     lambda_0 = 2.7095122..., 0.054; the p1(X0) values 10, 22, 36, 98, 110, 309 recomputed from
     the definition in the proof of Theorem D.6(iii), and the range of p1 - log_L X0 over
     X0 = 2^j, j <= 200.
  E. Section 6: E_B[m + r] = 4, the 3-gain rate 1/3, theta < 1/4 from 4 theta < tau < 1.
  F. Negative controls: each must be rejected by the same code.

Scope (README stopping rules): no cycle search; the one divisibility test is on the paper's own
printed p = 7 instance.  Nothing is excluded.

Reproduce (one command; deterministic; well under a minute):

    python experiments/paper1_v4_readable_examples_check.py

It writes experiments/paper1_v4_readable_examples_check_output.txt (ASCII) and prints the same
text.  Exit status 0 iff every check passes and every negative control is rejected.
"""
import os
import sys
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 400
OUT = []
RESULTS = {"pass": 0, "fail": 0, "ctrl_ok": 0, "ctrl_bad": 0}


def say(s=""):
    OUT.append(s)
    print(s)


def check(name, ok, detail=""):
    RESULTS["pass" if ok else "fail"] += 1
    say(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    return ok


def control(name, rejected, detail=""):
    RESULTS["ctrl_ok" if rejected else "ctrl_bad"] += 1
    say(f"  [{'REJECTED (good)' if rejected else 'NOT REJECTED (bad)'}] control: {name}"
        + (f" -- {detail}" if detail else ""))


# ---------------------------------------------------------------- arithmetic helpers
def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def v3(n):
    assert n != 0
    n, k = abs(n), 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def T(x):
    y = 3 * x + 1
    return y >> v2(y)


def R(x):
    """Projection of Definition B.1: x + 1 = 2^m 3^a w, 3 does not divide w -> (w, m + a)."""
    y = x + 1
    m = v2(y)
    u = y >> m
    a = v3(u)
    return (u // 3 ** a, m + a)


def F(w, d):
    """Reduced map of Definition B.1, from its formulas."""
    A = 3 ** d * w - 1
    s = v2(A)
    C = A + 2 ** s
    sigma = v2(C)
    ap = v3(C)
    mp_ = sigma - s
    wn = C // (2 ** sigma * 3 ** ap)
    return (wn, mp_ + ap), s


def N_mod(u, K):
    """N(u) mod 2^K for u = 1 mod 8: the t with 9^t = u^{-1} (mod 2^{K+3}), built bit by bit."""
    assert u % 8 == 1
    mod = 1 << (K + 3)
    target = pow(u, -1, mod)
    t = 0
    for i in range(K):
        # choose bit i so that 9^t = target mod 2^{i+4}
        m = 1 << (i + 4)
        if pow(9, t, m) != target % m:
            t |= 1 << i
        assert pow(9, t, m) == target % m
    return t


def M_mod(w, K):
    """Anchor M(w) = N(w^2) mod 2^K (Definition C.1)."""
    return N_mod((w * w) % (1 << (K + 3)), K)


# ---------------------------------------------------------------- A. Section 2
def part_A():
    say("A. Section 2 -- one rising run (x = 7)")
    rows = [(0, 7, "111", "1000", (3, 0, 1)), (1, 11, "1011", "1100", (2, 1, 1)),
            (2, 17, "10001", "10010", (1, 2, 1)), (3, 13, "1101", "1110", (1, 0, 7))]
    orbit = [7]
    for _ in range(3):
        orbit.append(T(orbit[-1]))
    check("T-orbit of 7 starts 7, 11, 17, 13", orbit == [7, 11, 17, 13], str(orbit))
    for step, x, bx, bx1, (e2, e3, rest) in rows:
        y = x + 1
        ok = (bin(x)[2:] == bx and bin(y)[2:] == bx1 and v2(y) == e2
              and v3(y >> v2(y)) == e3 and y == 2 ** e2 * 3 ** e3 * rest)
        check(f"table row {step}: x={x} binary {bx}, x+1 binary {bx1}, x+1 = 2^{e2}*3^{e3}*{rest}", ok)
    check("7->11 and 11->17 are rising steps (3x+1 divisible by 2 exactly once)",
          v2(3 * 7 + 1) == 1 and v2(3 * 11 + 1) == 1)
    check("3*17+1 = 52 = 110100 in binary, divisible by 4 (exactly), 52/4 = 13",
          3 * 17 + 1 == 52 and bin(52)[2:] == "110100" and v2(52) == 2 and 52 // 4 == 13)
    bad = [x for x in range(3, 200001, 4) if 2 * (T(x) + 1) != 3 * (x + 1)]
    check("T(x)+1 = (3/2)(x+1) for every x = 3 mod 4 below 200,001", not bad, f"{len(bad)} exceptions")
    bad = [x for x in range(1, 200001, 2)
           if not (bin(x)[2:].endswith("1" * v2(x + 1)) and (x >> v2(x + 1)) % 2 == 0)]
    check("x + 1 = 2^m u (u odd) <=> x ends in exactly m ones, odd x below 200,001", not bad)
    # block structure: m - 1 rising steps then one cascade to (3^m u - 1)/2^s
    bad = 0
    for x in range(1, 100001, 2):
        m = v2(x + 1)
        u = (x + 1) >> m
        y = x
        for j in range(m):
            if y + 1 != 2 ** (m - j) * 3 ** j * u:
                bad += 1
                break
            if j < m - 1:
                y = T(y)
        A = 3 ** m * u - 1
        if T(y) != A >> v2(A):
            bad += 1
    check("Prop B.2(i)-(ii): x_j + 1 = 2^(m-j) 3^j u, then exit (3^m u - 1)/2^s, odd x below 100,001",
          bad == 0, f"{bad} failures")
    m, u = v2(8), 8 >> v2(8)
    A = 3 ** m * u - 1
    check("x = 7: m = 3, u = 1, 3^3 - 1 = 26 = 2*13, s = 1, exit 13",
          (m, u, A, v2(A), A >> v2(A)) == (3, 1, 26, 1, 13))
    # one-division map
    seq, y = [7], 7
    while y != 13:
        y = (3 * y + 1) // 2 if y % 2 else y // 2
        seq.append(y)
    check("one-division map: 7, 11, 17 (odd), 26 (even), then 13", seq == [7, 11, 17, 26, 13], str(seq))
    say()


# ---------------------------------------------------------------- B. Section 3
def part_B():
    say("B. Section 3 -- blocks become states")
    reps = sorted(x for x in range(1, 200001, 2) if R(x) == (1, 3))
    check("odd x below 200,001 with R(x) = (1,3) are exactly 7, 11, 17", reps == [7, 11, 17], str(reps))
    formula = sorted(2 ** (3 - a) * 3 ** a * 1 - 1 for a in range(3))
    check("representative formula 2^(d-a) 3^a w - 1, 0 <= a <= d-1, gives 7, 11, 17", formula == [7, 11, 17])
    fib = [x for x in range(1, 200001, 2) if R(x) == (1, 1)]
    check("R-fibre of (1,1) below 200,001 is {1}", fib == [1], str(fib))
    check("F(1,1) = (1,1)", F(1, 1)[0] == (1, 1))
    # states along the T-orbit of 7, block by block
    states, entries, x = [], [], 7
    for _ in range(4):
        st = R(x)
        states.append(st)
        entries.append(x)
        m = v2(x + 1)
        for _ in range(m):
            x = T(x)
    check("block entries along the orbit of 7 are 7, 13, 5, 1", entries == [7, 13, 5, 1], str(entries))
    check("states along the orbit of 7 are (1,3), (7,1), (1,2), (1,1)",
          states == [(1, 3), (7, 1), (1, 2), (1, 1)], str(states))
    st, chain = (1, 3), [(1, 3)]
    for _ in range(3):
        st = F(*st)[0]
        chain.append(st)
    check("the same chain from the formulas of Definition B.1", chain == [(1, 3), (7, 1), (1, 2), (1, 1)], str(chain))
    bad = 0
    for x in range(1, 50001, 2):
        y = x
        for _ in range(v2(x + 1)):
            y = T(y)
        if R(y) != F(*R(x))[0]:
            bad += 1
    check("R(T^m(x)) = F(R(x)) for odd x below 50,001 (Prop B.2(iii))", bad == 0, f"{bad} failures")
    say()


# ---------------------------------------------------------------- C. Section 4
def part_C():
    say("C. Section 4 -- the exact laws (anchor, eight-class table, (1,2))")
    K = 64
    check("M(1) = 0 (mod 2^64)", M_mod(1, K) == 0)
    bad = [w for w in range(1, 4001, 2) if (M_mod(w, K) % 2 == 0) != (w % 8 in (1, 7))]
    check("M(w) even iff w = +-1 mod 8, odd w below 4001", not bad, f"{len(bad)} exceptions")
    # the printed table: rows d even / d odd, columns w = 1, 3, 5, 7 mod 8
    printed = {(1, 0): "L", (3, 0): 1, (5, 0): 2, (7, 0): 1,
               (1, 1): 1, (3, 1): "L", (5, 1): 1, (7, 1): 2}

    def table_holds(tab):
        seen = {}
        for w in range(1, 3001, 2):
            if w % 3 == 0:
                continue
            for d in range(1, 41):
                s = v2(3 ** d * w - 1)
                key = (w % 8, d % 2)
                lifting = (3 ** d * w) % 8 == 1
                want = tab[key]
                if want == "L":
                    if not (lifting and s >= 3):
                        return False, (w, d, s)
                elif lifting or s != want:
                    return False, (w, d, s)
                seen[key] = True
        return len(seen) == 8, None

    ok, bad = table_holds(printed)
    check("eight-class table of Section 4 (s = 1/2 constants; lifting s >= 3), w < 3001, 3 !| w, d <= 40",
          ok, str(bad) if bad else "")
    lif = (lambda w, d: (w % 8 == 1 and d % 2 == 0) or (w % 8 == 3 and d % 2 == 1))
    bad = 0
    tested = 0
    for w in range(1, 3001, 2):
        if w % 3 == 0:
            continue
        Mw = M_mod(w, K)
        for d in range(1, 41):
            if (3 ** d * w) % 8 == 1:
                tested += 1
                if not lif(w, d):
                    bad += 1
                    continue
                diff = (d - Mw) % (1 << K)
                if diff == 0 or v2(3 ** d * w - 1) != 2 + v2(diff):
                    bad += 1
    check("lifting <=> (w = 1 mod 8, d even) or (w = 3 mod 8, d odd); s = 2 + v2(d - M(w)) there",
          bad == 0, f"{tested} lifting states, {bad} failures")
    (nxt, s) = F(1, 2)
    check("(1,2): s = 3; 3*5+1 = 16 halves 1 + s = 4 times, down to 1",
          s == 3 and 3 * 5 + 1 == 16 and v2(16) == 4 and 16 >> 4 == 1 and nxt == (1, 1))
    # displacement of Theorem C.5: xi = n - N(w) on d = 2n (w = 1 mod 8), xi = n - N(3w) on d = 2n+1
    # (w = 3 mod 8).  Check 2*xi = d - M(w) mod 2^K.
    bad = 0
    tested = 0
    mod = 1 << K
    for w in range(1, 3001, 2):
        if w % 3 == 0 or w % 8 not in (1, 3):
            continue
        Mw = M_mod(w, K + 1)
        Nw = N_mod(w if w % 8 == 1 else 3 * w, K + 1)
        for d in range(1, 41):
            if not lif(w, d):
                continue
            tested += 1
            n = d // 2
            xi = (n - Nw) % (1 << (K + 1))
            if (2 * xi - (d - Mw)) % mod != 0:
                bad += 1
    check("Theorem C.5's displacement xi equals (d - M(w))/2 on both lifting components (mod 2^64)",
          bad == 0, f"{tested} lifting states, {bad} failures")
    for k, printed_rate in ((4, Fraction(3125, 100000)), (8, Fraction(195, 100000))):
        rate = Fraction(1, 2 ** (k + 1))
        tail = sum(Fraction(1, 2 ** j) for j in range(k + 2, 400)) + Fraction(1, 2 ** 399)
        check(f"undecided rate at k = {k}: sum_(j >= k+2) 2^-j = 2^-(k+1) = {float(rate):.6f}, "
              f"printed {float(printed_rate)}", tail == rate and abs(rate - printed_rate) < Fraction(1, 100000))
    say()


# ---------------------------------------------------------------- D. Section 5
L = mp.log(3) / mp.log(2)


def phi(x):
    return -mp.log(1 - mp.power(2, -x)) / mp.log(2)


def R_rot(ms, ss, r):
    """Rotation numerator of Proposition D.1: R_r = sum_t 3^{M_t} 2^{S_t} (2^{s_t} - 1), in rotation
    order from r, M_t = sum_{j>t} m_j, S_t = sum_{j<t} sigma_j, sigma_j = s_j + m_{j+1} (cyclic)."""
    p = len(ms)
    order = [(r + t) % p for t in range(p)]
    tot = 0
    for t in range(p):
        Mt = sum(ms[order[j]] for j in range(t + 1, p))
        St = sum(ss[order[j]] + ms[(order[j] + 1) % p] for j in range(t))
        tot += 3 ** Mt * 2 ** St * (2 ** ss[order[t]] - 1)
    return tot


def size_report(ms, ss):
    n = sum(ms)
    Kc = n + sum(ss)
    q = 2 ** Kc - 3 ** n
    if q <= 0:
        return None
    Rs = [R_rot(ms, ss, r) for r in range(len(ms))]
    return n, Kc, q, Rs


def p1_of(X0, conv):
    lam0 = L / (L - 1) + mp.power(2, -20)
    g = 1 + max(mp.log(X0 + 1) / mp.log(2), lam0)
    Delta = phi(g) - phi(g + 1)
    k = 1
    while not (conv[k - 1][2] <= Delta):
        k += 1
    Nstar = conv[k][1] + conv[k - 1][1]
    p = 1
    while not ((mp.power(L, p) - 1) / (2 * (L - 1)) >= max(Nstar, 3 * p + 40)):
        p += 1
    # the condition then holds at every larger p (both sides checked a little further)
    for pp in range(p, p + 30):
        assert (mp.power(L, pp) - 1) / (2 * (L - 1)) >= max(Nstar, 3 * pp + 40)
    return p


def convergents(x, count):
    out = []
    h0, h1, k0, k1 = 0, 1, 1, 0  # P_{-2}, P_{-1}, Q_{-2}, Q_{-1}
    y = x
    for _ in range(count):
        a = int(mp.floor(y))
        h0, h1 = h1, a * h1 + h0
        k0, k1 = k1, a * k1 + k0
        out.append((h1, k1, abs(k1 * x - h1)))
        y = 1 / (y - a)
    return out


def part_D():
    say("D. Section 5 -- the p = 7 staircase and the quoted constants")
    ms = [4, 7, 9, 15, 23, 35, 1]
    n = sum(ms)
    Kc = int(mp.ceil(n * L))
    stot = Kc - n
    ss = [1, 1, 1, 1, 1, 1, stot - 6]
    check("n = sum m = 94", n == 94)
    check("K = ceil(94 log2 3) = 149 (exact: 2^148 < 3^94 < 2^149)", Kc == 149 and 2 ** 148 < 3 ** 94 < 2 ** 149)
    check("last exit valuation s_tot - 6 = 49, so s = (1,1,1,1,1,1,49) and n + sum s = K",
          stot - 6 == 49 and n + sum(ss) == Kc)
    nn, KK, q, Rs = size_report(ms, ss)
    gamma = KK - mp.log(q) / mp.log(2)
    check("gamma = K - log2 q = 6.7438... (printed 6.74)", abs(gamma - mp.mpf("6.74")) < 0.005,
          mp.nstr(gamma, 8))
    check("all seven size tests q <= R_r hold (exact integers)", all(q <= Rr for Rr in Rs),
          "min R_r / q = " + mp.nstr(mp.mpf(min(Rs)) / q, 6))
    ndiv = sum(1 for Rr in Rs if Rr % q == 0)
    check("divisibility q | R_r fails (the configuration is not a cycle)", ndiv < len(Rs),
          f"q divides {ndiv} of the 7 R_r")
    p3 = Fraction(1157, 10000) * 94 - 2
    check("period-3 constant 0.1157 n - 2 at n = 94 is 8.8758 (printed 8.9) and exceeds gamma",
          abs(p3 - Fraction(89, 10)) < Fraction(5, 100) and gamma < float(p3), str(float(p3)))
    ratios = [Fraction(ms[i + 1], ms[i]) for i in range(5)]
    check("climb ratios m_{i+1}/m_i over the first six blocks lie in [1.28, 1.75] (log2 3 = 1.585)",
          min(ratios) >= Fraction(128, 100) and max(ratios) <= Fraction(175, 100),
          ", ".join(f"{float(r):.3f}" for r in ratios))
    xs = [Fraction(2 ** ms[r] * Rs[r], q) - 1 for r in range(7)]
    check("x_r = 2^{m_r} R_r / q - 1 are positive rationals (rational-cycle block entries)",
          all(x > 0 for x in xs))
    xmin = min(xs)
    lx = mp.log(mp.mpf(xmin.numerator) / xmin.denominator + 1) / mp.log(2)
    check("Theorem D.6(ii) sandwich: gamma - 1 <= log2(x_min + 1) < gamma + log2 7",
          gamma - 1 <= lx < gamma + mp.log(7) / mp.log(2), mp.nstr(lx, 6))
    kap = (L - 1) / (mp.power(L, 7) - 1)
    check("Theorem D.5 trim holds for this size-passer: gamma + log2 7 > kappa_7 * 94",
          gamma + mp.log(7) / mp.log(2) > kap * 94, f"{mp.nstr(gamma + mp.log(7)/mp.log(2), 6)} > {mp.nstr(kap*94, 6)}")
    # constants of the Sharpness bullets
    Gs = mp.mpf("1.05") * L * (L - 1) + 1 / (L - 1) + 1
    check("Gamma* = 1.05 L(L-1) + 1/(L-1) + 1 = 3.6830121..., printed lower bound 3.683012 <= Gamma*",
          mp.mpf("3.683012") <= Gs < mp.mpf("3.683013"), mp.nstr(Gs, 10))
    up = phi(mp.mpf("0.0415"))
    check("phi(0.0415) = 5.1402114..., printed upper bound 5.140212 >= it",
          mp.mpf("5.140211") < up <= mp.mpf("5.140212"), mp.nstr(up, 10))
    lam0 = L / (L - 1) + mp.power(2, -20)
    check("lambda_0 = L/(L-1) + 2^-20 = 2.7095122...", mp.nstr(lam0, 8) == "2.7095122", mp.nstr(lam0, 10))
    c = mp.power(2, -(lam0 + mp.mpf("1.5")))
    check("2^-(lambda_0 + 1.5) = 0.05405... > 0.054", mp.mpf("0.054") < c < mp.mpf("0.0541"), mp.nstr(c, 6))
    # p1(X0), recomputed from the definition in the proof of Theorem D.6(iii)
    conv = convergents(L, 300)
    check("convergents of log2 3 begin 1/1, 2/1, 3/2, 8/5, 19/12, 65/41",
          [(a, b) for a, b, _ in conv[:6]] == [(1, 1), (2, 1), (3, 2), (8, 5), (19, 12), (65, 41)])
    table = [("X0 = 1", 1, 10), ("X0 = 16", 16, 10), ("X0 = 2^8", 2 ** 8, 22), ("X0 = 2^12", 2 ** 12, 22),
             ("X0 = 2^20", 2 ** 20, 36), ("X0 = 5*2^60", 5 * 2 ** 60, 98), ("X0 = 2^71", 2 ** 71, 110),
             ("X0 = 2^200", 2 ** 200, 309)]
    for name, X0, want in table:
        got = p1_of(mp.mpf(X0), conv)
        check(f"p1({name}) = {want}", got == want, f"computed {got}")
    lo, hi = None, None
    for j in range(0, 201):
        d = p1_of(mp.power(2, j), conv) - j * mp.log(2) / mp.log(L)  # log base L = log2 3
        if lo is None or d < lo[0]:
            lo = (d, j)
        if hi is None or d > hi[0]:
            hi = (d, j)
    # Appendix D (not quoted in Section 5) prints [2.784, 10.629], rounded to nearest; the exact
    # extremes sit just outside it (see the detail), so the check is against the outward rounding.
    check("over X0 = 2^j, 0 <= j <= 200: p1 - log_L X0 in [2.783, 10.630] (Appendix D prints [2.784, 10.629])",
          mp.mpf("2.783") <= lo[0] and hi[0] <= mp.mpf("10.630"),
          f"min {mp.nstr(lo[0], 9)} at j = {lo[1]}, max {mp.nstr(hi[0], 9)} at j = {hi[1]}")
    check("the printed endpoints 2.784 and 10.629 are the extremes rounded to nearest (3 decimals)",
          abs(lo[0] - mp.mpf("2.784")) < mp.mpf("0.0005") and abs(hi[0] - mp.mpf("10.629")) < mp.mpf("0.0005"),
          f"both extremes lie just outside the printed closed interval: {mp.nstr(lo[0], 9)} < 2.784, "
          f"{mp.nstr(hi[0], 9)} > 10.629")
    say()
    return ms, ss, conv


# ---------------------------------------------------------------- E. Section 6
def part_E():
    say("E. Section 6 -- the model law")
    Em = sum(Fraction(j, 2 ** j) for j in range(1, 300)) + Fraction(301, 2 ** 299)  # exact tail of sum j/2^j
    check("E[geom(1/2)] = 2, so E_B[m + r] = 4", Em == 2)
    gain = sum(Fraction(1, 2 ** j) for j in range(2, 300, 2)) + Fraction(1, 3 * 2 ** 298)
    check("3-gain rate sum_(j even) 2^-j = 1/3", gain == Fraction(1, 3))
    grid = [Fraction(i, 1000) for i in range(1, 1000)]
    check("a tau with 4 theta < tau < 1 exists iff theta < 1/4 (theta on a 1/1000 grid; tau = (4 theta + 1)/2)",
          all(((4 * th < (4 * th + 1) / 2 < 1)) == (th < Fraction(1, 4)) for th in grid))
    say()


# ---------------------------------------------------------------- F. negative controls
def part_F(ms, ss, conv):
    say("F. Negative controls (each must be rejected)")
    wrong = {(1, 0): "L", (3, 0): 2, (5, 0): 2, (7, 0): 1,
             (1, 1): 1, (3, 1): "L", (5, 1): 1, (7, 1): 2}
    seen_bad = False
    for w in range(1, 200, 2):
        if w % 3 == 0 or w % 8 != 3:
            continue
        if v2(3 ** 2 * w - 1) != wrong[(3, 0)]:
            seen_bad = True
            break
    control("eight-class table with s = 2 at (w = 3 mod 8, d even)", seen_bad)
    st, chain = (1, 3), [(1, 3)]
    for _ in range(3):
        st = F(*st)[0]
        chain.append(st)
    control("state chain (1,3) -> (7,1) -> (1,1) -> (1,1)", chain != [(1, 3), (7, 1), (1, 1), (1, 1)])
    ss2 = ss[:-1] + [48]
    control("last exit 48 instead of 49 (n + sum s != K = 149)", sum(ms) + sum(ss2) != 149)
    ms3 = [1, 1, 1, 1, 1, 1, 88]
    rep = size_report(ms3, [1, 1, 1, 1, 1, 1, 149 - 94 - 6])
    control("flat profile m = (1,...,1,88) with the same s passes all size tests", rep is not None and
            min(rep[3]) < rep[2], "min R_r < q" if rep and min(rep[3]) < rep[2] else "")
    control("p1(2^20) = 35", p1_of(mp.power(2, 20), conv) != 35)
    ms4 = [4, 7, 9, 15, 23, 35, 1]
    Kw = 150
    q4 = 2 ** Kw - 3 ** 94
    g4 = Kw - mp.log(q4) / mp.log(2)
    control("K = 150 instead of 149 gives gamma = 6.74", abs(g4 - mp.mpf("6.74")) > 0.01, mp.nstr(g4, 6))
    control("xi = d - M(w) (without the factor 1/2) on the lifting class",
            any((((d // 2) - N_mod(w, 20)) - (d - M_mod(w, 20))) % (1 << 20) != 0
                for w in (17, 41, 73) for d in (2, 4, 6)))
    say()


def main():
    say("paper1_v4_readable_examples_check.py -- worked examples of the readable rewrite of paper 1 v4")
    say("(paper/collatz-reduced-v4.tex at d421851; main text Sections 2-6)")
    say()
    part_A()
    part_B()
    part_C()
    ms, ss, conv = part_D()
    part_E()
    part_F(ms, ss, conv)
    say(f"TOTAL: {RESULTS['pass']} checks passed, {RESULTS['fail']} failed; "
        f"{RESULTS['ctrl_ok']} negative controls rejected, {RESULTS['ctrl_bad']} not rejected")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "paper1_v4_readable_examples_check_output.txt"), "w", encoding="ascii",
              newline="\n") as fh:
        fh.write("\n".join(OUT) + "\n")
    return 0 if RESULTS["fail"] == 0 and RESULTS["ctrl_bad"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
