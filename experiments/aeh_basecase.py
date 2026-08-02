#!/usr/bin/env python3
"""
Independent verification for aeh.md Lemma 13.2.4 (the unconditional base case,
theta < 1/4) and Proposition 13.2.5 (the dyadic-shell exceptional set).

Fresh implementation.  Imports nothing from experiments/aeh_calibration.py,
experiments/aeh_symbolic.py or experiments/itinerary_coding.py.  The door map
G, the stratum, the cylinder count, the Bernoulli reference law and the
descent bound are all rebuilt here from the definitions:
  - Definition 3.1 / Proposition 3.2 of paper/collatz-reduced-v3.tex
    (reduced state, block structure, x_exit);
  - itinerary.md 14.15.1.1 (stratum) and 14.15.1.5 (cylinder theorem);
  - aeh.md 13.6.1 (letter law) and 13.6.3 (dictionary).

Checks
  C0  G = T^m, and stratum(y_n) = (m_+ of block n, s of block n+1).
  C1  Exact cylinder count, exhaustive on all odd residues mod 2^J.
  C2  The same count on a general window [N, 2N) with N not a power of two:
      measured TV against the bound of Lemma 13.2.4(a).
  C3  The exact identity  P_B(S_n >= b) = P(Bin(b-1, 1/2) < 2n), and the
      entropy rate I(theta) = log 2 - H(2 theta).
  C4  Cylinder-class structure at the scale actually used (3000-bit starts):
      the length-n word is constant on residue classes mod 2^{S_n+1} and not
      on classes mod 2^{S_n}.
  C5  Concentration of multi-letter pattern frequencies at 3000-bit starts.
  C6  The past-boundary term: the law of the absorption a_n at n = 0, 1, 2, ...
      against the uniform-start law 2*3^{-(j+1)} and the bulk law 13.6.5.
  C7  The cut is non-binding, in door coordinates (Lemma 13.2.4(c)).
  C8  Window side: per-cell concentration of L-block window frequencies.

Run: python experiments/aeh_basecase.py     (date: 2026-08-02)
"""

import math
import random
from collections import Counter, defaultdict
from fractions import Fraction

# ----------------------------------------------------------------------------
# primitives
# ----------------------------------------------------------------------------


def v2(n):
    """2-adic valuation of a nonzero integer."""
    return (n & -n).bit_length() - 1


def v3(n):
    """3-adic valuation of a nonzero integer."""
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def T_odd(x):
    """The odd-to-odd Collatz map T(x) = (3x+1)/2^{v2(3x+1)} (paper L50)."""
    z = 3 * x + 1
    return z >> v2(z)


def stratum(y):
    """itinerary.md 14.15.1.1:  m = v2(y+1), q = (y+1)/2^m, r = v2(3^m q - 1)."""
    m = v2(y + 1)
    q = (y + 1) >> m
    return m, v2(pow(3, m) * q - 1)


def G(y):
    """The door map, reverse.md 14.14.3:  G(y) = (3^m q - 1)/2^r  = T^m(y)."""
    m = v2(y + 1)
    q = (y + 1) >> m
    z = pow(3, m) * q - 1
    return z >> v2(z)


def R(x):
    """The projection R of Definition 3.1: x+1 = 2^m 3^a w, R(x) = (w, m+a)."""
    u = x + 1
    m = v2(u)
    u >>= m
    a = v3(u)
    w = u // pow(3, a)
    return w, m + a


def step_labels(w, d):
    """Definition 3.1's per-step data for the state (w, d)."""
    A = pow(3, d) * w - 1
    s = v2(A)
    x_exit = A >> s
    C = A + (1 << s)
    sigma = v2(C)
    a_plus = v3(C)
    m_plus = sigma - s
    w_next = C // (pow(2, sigma) * pow(3, a_plus))
    return dict(A=A, s=s, x_exit=x_exit, C=C, sigma=sigma, a_plus=a_plus,
                m_plus=m_plus, w_next=w_next, d_next=m_plus + a_plus)


def word(x, n):
    """The length-n letter word of the odd integer x: (stratum(G^i x))_{i<n}."""
    out = []
    y = x
    for _ in range(n):
        out.append(stratum(y))
        y = G(y)
    return tuple(out)


# ----------------------------------------------------------------------------
# C0 -- the coding is the one the wiki describes
# ----------------------------------------------------------------------------


def check_C0(trials=4000, bits=64, seed=34001):
    rng = random.Random(seed)
    fail_gt, fail_seam, fail_exit = 0, 0, 0
    for _ in range(trials):
        x = rng.randrange(1 << (bits - 1), 1 << bits) | 1
        # G = T^m
        m = v2(x + 1)
        z = x
        for _ in range(m):
            z = T_odd(z)
        if z != G(x):
            fail_gt += 1
        # the door y_0 = G(x) is x_exit of the first block
        w, d = R(x)
        lab = step_labels(w, d)
        if lab["x_exit"] != G(x):
            fail_exit += 1
        # stratum(y_n) = (m_+ of block n, s of block n+1)
        y = G(x)
        lab2 = step_labels(lab["w_next"], lab["d_next"])
        if stratum(y) != (lab["m_plus"], lab2["s"]):
            fail_seam += 1
    return dict(trials=trials, bits=bits, seed=seed,
                fail_G_eq_Tm=fail_gt, fail_exit=fail_exit, fail_seam=fail_seam)


# ----------------------------------------------------------------------------
# C1 -- exact cylinder count, exhaustive over odd residues mod 2^J
# ----------------------------------------------------------------------------


def check_C1(J):
    """Every word W with S(W) + 1 <= J is realised by exactly 2^{J-1-S} of the
    2^{J-1} odd residues mod 2^J.  Exhaustive."""
    counts = defaultdict(int)
    for x in range(1, 1 << J, 2):
        y = x
        S = 0
        w = []
        while True:
            m, r = stratum(y)
            if S + m + r + 1 > J:
                break
            w.append((m, r))
            S += m + r
            counts[tuple(w)] += 1
            y = G(y)
    fails = 0
    worst = None
    for wd, c in counts.items():
        S = sum(m + r for m, r in wd)
        pred = 1 << (J - 1 - S)
        if c != pred:
            fails += 1
            worst = (wd, c, pred)
    by_len = Counter(len(w) for w in counts)
    return dict(J=J, odd_residues=1 << (J - 1), words=len(counts),
                failures=fails, worst=worst,
                words_by_length=dict(sorted(by_len.items())))


# ----------------------------------------------------------------------------
# C2 -- a general window [N, 2N), N not a power of two
# ----------------------------------------------------------------------------


def tv_word_law(N, n):
    """Exhaustive over odd x in [N, 2N): TV(Law(word_n(x)), B^{tensor n})."""
    cnt = Counter()
    tot = 0
    x = N | 1
    while x < 2 * N:
        cnt[word(x, n)] += 1
        tot += 1
        x += 2
    seen_B = Fraction(0)
    tv2 = Fraction(0)  # 2 * TV
    for wd, c in cnt.items():
        S = sum(m + r for m, r in wd)
        B = Fraction(1, 1 << S)
        seen_B += B
        tv2 += abs(Fraction(c, tot) - B)
    tv2 += (1 - seen_B)  # unobserved words carry only B-mass
    return float(tv2 / 2), tot, len(cnt)


def PB_S_ge(n, b):
    """P_B(S_n >= b) exactly, S_n = sum of 2n iid geom(1/2) on {1,2,...}."""
    if b <= 2 * n:
        return Fraction(1)
    tail = Fraction(1)
    for s in range(2 * n, b):
        tail -= Fraction(math.comb(s - 1, 2 * n - 1), 1 << s)
    return tail


def check_C2(Ns, n):
    rows = []
    for N in Ns:
        tv, tot, nw = tv_word_law(N, n)
        # Lemma 13.2.4(a) bound: 2^{J+2}/N + P_B(S_n >= J), minimised over J
        best = None
        for J in range(2 * n, 300):
            bd = float(Fraction(1 << (J + 1), tot)) + float(PB_S_ge(n, J))
            if best is None or bd < best[1]:
                best = (J, bd)
            if bd > 10:
                break
        b = N.bit_length()
        rows.append(dict(N=N, dyadic=(N == 1 << (b - 1)), n=n, odds=tot,
                         distinct_words=nw, TV_measured=round(tv, 6),
                         PB_S_ge_b=round(float(PB_S_ge(n, b)), 6),
                         J_star=best[0], lemma_bound=round(best[1], 4)))
    return rows


# ----------------------------------------------------------------------------
# C3 -- the exact tail identity and the entropy rate
# ----------------------------------------------------------------------------


def binom_lt(b, k):
    """P(Bin(b, 1/2) < k) exactly."""
    return Fraction(sum(math.comb(b, j) for j in range(0, k)), 1 << b)


def check_C3(cases):
    rows = []
    ok = True
    for (n, b) in cases:
        lhs = PB_S_ge(n, b)
        rhs = binom_lt(b - 1, 2 * n)
        if lhs != rhs:
            ok = False
        rows.append(dict(n=n, b=b, PB_S_ge=float(lhs), Bin=float(rhs),
                         exact_equal=(lhs == rhs)))
    return ok, rows


def I_rate(theta):
    """I(theta) = log 2 - H(2 theta), natural log; the Chernoff rate of
    P_B(S_{theta b} >= b).  Zero exactly at theta = 1/4."""
    p = 2 * theta
    if p <= 0 or p >= 1:
        return float("nan")
    H = -p * math.log(p) - (1 - p) * math.log(1 - p)
    return math.log(2) - H


# ----------------------------------------------------------------------------
# C4 -- the cylinder class structure at the scale actually used
# ----------------------------------------------------------------------------


def check_C4(bits=3000, n=600, trials=40, seed=34002):
    rng = random.Random(seed)
    fail_up, fail_down = 0, 0
    for _ in range(trials):
        x = rng.randrange(1 << (bits - 1), 1 << bits) | 1
        wd = word(x, n)
        S = sum(m + r for m, r in wd)
        t = rng.randrange(1, 1 << 20)
        if word(x + t * (1 << (S + 1)), n) != wd:
            fail_up += 1
        # the modulus is sharp: 2^S alone does not suffice for every shift
        sharp = False
        for tt in range(1, 40):
            xx = x + tt * (1 << S)
            if (xx & 1) and word(xx, n) != wd:
                sharp = True
                break
        if not sharp:
            fail_down += 1
    return dict(bits=bits, n=n, trials=trials, seed=seed,
                fail_class_invariance=fail_up, fail_sharpness=fail_down)


# ----------------------------------------------------------------------------
# C5 -- concentration of multi-letter pattern frequencies
# ----------------------------------------------------------------------------


def check_C5(bits=3000, theta=0.20, starts=1500, seed=34003,
             patterns=(((1, 1), (1, 1)),
                       ((1, 1), (1, 2)),
                       ((2, 1), (1, 1)),
                       ((1, 1), (1, 1), (1, 1)))):
    rng = random.Random(seed)
    N = rng.randrange(1 << (bits - 1), 1 << bits)  # generic, not a power of two
    b = math.log2(N)
    T = math.ceil(theta * b)
    freqs = {p: [] for p in patterns}
    S_max = 0
    exps = []           # per-start mean of m+r over the horizon
    budget_violations = 0
    for _ in range(starts):
        x = rng.randrange(N, 2 * N) | 1
        wd = word(x, T + 4)
        S = sum(m + r for m, r in wd[:T])
        S_max = max(S_max, S)
        if S + 1 > math.floor(b):
            budget_violations += 1
        exps.append(S / T)
        for p in patterns:
            Lp = len(p)
            hits = sum(1 for i in range(T - Lp + 1) if wd[i:i + Lp] == p)
            freqs[p].append(hits / (T - Lp + 1))
    out = dict(bits=bits, theta=theta, N_bits=N.bit_length(), T=T,
               starts=starts, seed=seed, S_max=S_max, b=b,
               budget_violations=budget_violations,
               mean_exponent_per_block=sum(exps) / len(exps))
    rows = []
    for p in patterns:
        Bp = 1.0
        for (m, r) in p:
            Bp *= 2.0 ** (-(m + r))
        f = freqs[p]
        mean = sum(f) / len(f)
        sd = (sum((v - mean) ** 2 for v in f) / (len(f) - 1)) ** 0.5
        z = (mean - Bp) / (sd / len(f) ** 0.5) if sd > 0 else float("nan")
        rows.append(dict(pattern=p, B=Bp, mean=round(mean, 6), sd=round(sd, 6),
                         z_of_mean=round(z, 2),
                         max_abs_dev=round(max(abs(v - Bp) for v in f), 5),
                         frac_dev_gt_0p02=sum(1 for v in f if abs(v - Bp) > 0.02) / len(f),
                         frac_dev_gt_0p03=sum(1 for v in f if abs(v - Bp) > 0.03) / len(f)))
    out["patterns"] = rows
    return out


# ----------------------------------------------------------------------------
# C8 -- the window side: per-cell concentration of L-block window frequencies
# ----------------------------------------------------------------------------


def check_C8(bits_list=(1500, 3000, 6000), theta=0.20, starts=400, L=2,
             seed=34006):
    """Coarse capped window V(n) = (min(s_n, 3), min(d_n, 3)), 9 letters, so
    9^L block cells.  s_n = r_{n-1} and d_n = m_{n-1} + v3(y_{n-1}+1) are read
    off the door orbit (13.6.3(i),(iii)).  We measure, per start, the empirical
    L-block law, and compare each start to the pooled reference: the claim
    under test is concentration, cell by cell and in total variation."""
    out = []
    for bits in bits_list:
        rng = random.Random(seed + bits)
        N = rng.randrange(1 << (bits - 1), 1 << bits)
        b = math.log2(N)
        T = math.ceil(theta * b)
        per_start = []
        pooled = Counter()
        pooled_tot = 0
        for _ in range(starts):
            x = rng.randrange(N, 2 * N) | 1
            y = x
            V = []
            for _ in range(T + L):
                m, r = stratum(y)
                a = v3(y + 1)
                V.append((min(r, 3), min(m + a, 3)))   # (s_{n+1}, d_{n+1})
                y = G(y)
            c = Counter(tuple(V[i:i + L]) for i in range(len(V) - L + 1))
            tot = sum(c.values())
            per_start.append((c, tot))
            pooled.update(c)
            pooled_tot += tot
        ref = {k: v / pooled_tot for k, v in pooled.items()}
        tvs = []
        for c, tot in per_start:
            keys = set(c) | set(ref)
            tvs.append(0.5 * sum(abs(c.get(k, 0) / tot - ref.get(k, 0.0))
                                 for k in keys))
        # per-cell spread on the busiest cells
        cells = sorted(ref.items(), key=lambda kv: -kv[1])[:6]
        cellrows = []
        for k, p in cells:
            vals = [c.get(k, 0) / tot for c, tot in per_start]
            mu = sum(vals) / len(vals)
            sd = (sum((v - mu) ** 2 for v in vals) / (len(vals) - 1)) ** 0.5
            cellrows.append(dict(cell=k, pooled=round(p, 5), mean=round(mu, 5),
                                 sd=round(sd, 5),
                                 sd_over_sqrtT_pred=round((p * (1 - p) / (T + 1)) ** 0.5, 5)))
        out.append(dict(bits=bits, T=T, starts=starts, cells_seen=len(ref),
                        TV_mean=round(sum(tvs) / len(tvs), 5),
                        TV_max=round(max(tvs), 5),
                        TV_mean_times_sqrtT=round(sum(tvs) / len(tvs) * T ** 0.5, 4),
                        busiest_cells=cellrows))
    return out


# ----------------------------------------------------------------------------
# C6 -- the past-boundary term
# ----------------------------------------------------------------------------


def check_C6(bits=400, starts=40000, depth=13, seed=34004):
    """a_n = v3(y_{n-1} + 1) with y_{-1} = x.  n = 0 is the uniform-start
    absorption v3(x+1); large n should be the bulk law of 13.6.5."""
    rng = random.Random(seed)
    N = 1 << (bits - 1)
    tal = [Counter() for _ in range(depth)]
    for _ in range(starts):
        x = rng.randrange(N, 2 * N) | 1
        y = x
        for n in range(depth):
            tal[n][min(v3(y + 1), 4)] += 1
            y = G(y)
    # collapse to (0, 1, >=2), where the record's exact values live
    bulk3 = (2 / 3, 19 / 63, 2 / 63)
    unif3 = (2 / 3, 2 / 9, 1 / 9)
    rows = []
    for n in range(depth):
        c = tal[n]
        tot = sum(c.values())
        emp = (c[0] / tot, c[1] / tot, (tot - c[0] - c[1]) / tot)
        rows.append(dict(n=n, P0=emp[0], P1=emp[1], Pge2=emp[2],
                         L1_to_bulk=sum(abs(a - b) for a, b in zip(emp, bulk3)),
                         L1_to_uniform_start=sum(abs(a - b) for a, b in zip(emp, unif3))))
    return dict(bits=bits, starts=starts, seed=seed, depth=depth,
                bulk=bulk3, uniform_start=unif3, rows=rows)


# ----------------------------------------------------------------------------
# C7 -- the cut is non-binding (Lemma 13.2.4(c)) in door coordinates
# ----------------------------------------------------------------------------


def check_C7(bits=1200, theta=0.20, starts=300, seed=34005):
    """Two claims:
       (a)  y_{i+1} + 1  >  (y_i + 1) * (3/2)^{m_i} * 2^{-r_i}   exactly;
       (b)  min_{n<=T} log2(y_n + 1)  >=  log2(x+1) - S_T,  and that this is
            already > (1 - 4 theta - o(1)) log2 N."""
    rng = random.Random(seed)
    N = rng.randrange(1 << (bits - 1), 1 << bits)
    b = math.log2(N)
    T = math.ceil(theta * b)
    fail_step, fail_bound = 0, 0
    worst_margin = None
    min_ratio = None
    min_ratio_core = None     # the code's stronger cut, on the core w_+
    max_m = 0
    max_a = 0
    for _ in range(starts):
        x = rng.randrange(N, 2 * N) | 1
        y = x
        S = 0
        lo = math.log2(x + 1)
        lo_core = None
        for n in range(T):
            m, r = stratum(y)
            y2 = G(y)
            if not (y2 + 1) * (1 << (m + r)) > (y + 1) * pow(3, m):
                # (y2+1) > (y+1) (3/2)^m 2^{-r}  <=>  (y2+1) 2^{m+r} > (y+1) 3^m
                fail_step += 1
            a = v3(y2 + 1)
            core = (y2 + 1) >> v2(y2 + 1)
            core //= pow(3, a)
            lc = math.log2(core)
            lo_core = lc if lo_core is None else min(lo_core, lc)
            max_m = max(max_m, m)
            max_a = max(max_a, a)
            S += m + r
            lo = min(lo, math.log2(y2 + 1))
            y = y2
        if lo < math.log2(x + 1) - S - 1e-9:
            fail_bound += 1
        margin = lo - (b - S)
        worst_margin = margin if worst_margin is None else min(worst_margin, margin)
        ratio = lo / b
        min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
        rc = lo_core / b
        min_ratio_core = rc if min_ratio_core is None else min(min_ratio_core, rc)
    return dict(bits=bits, theta=theta, T=T, starts=starts, seed=seed,
                fail_step_inequality=fail_step, fail_S1_bound=fail_bound,
                worst_margin_bits=round(worst_margin, 2),
                min_log2_exit_over_log2_N=round(min_ratio, 5),
                min_log2_core_over_log2_N=round(min_ratio_core, 5),
                max_m_seen=max_m, max_a_seen=max_a,
                predicted_floor_1_minus_4theta=1 - 4 * theta)


# ----------------------------------------------------------------------------


def main():
    print("=" * 78)
    print("C0  coding sanity: G = T^m, x_exit = G(x), stratum(y_n) = (m_+, s_+)")
    print(check_C0())

    print("=" * 78)
    print("C1  exact cylinder count, exhaustive over odd residues mod 2^J")
    for J in (18, 20, 22):
        r = check_C1(J)
        print({k: r[k] for k in ("J", "odd_residues", "words", "failures")},
              "words_by_length =", r["words_by_length"])

    print("=" * 78)
    print("C2  general window [N, 2N):  dyadic vs non-dyadic, same magnitude")
    Ns = [1 << 20, 1234567, 1500001, 1999999, 1 << 21, 2097153, 2999983]
    for row in check_C2(Ns, n=3):
        print(row)
    for row in check_C2([1 << 21, 2999983], n=4):
        print(row)

    print("=" * 78)
    print("C3  P_B(S_n >= b) = P(Bin(b-1,1/2) < 2n), exact; entropy rate")
    ok, rows = check_C3([(5, 40), (10, 60), (12, 100), (25, 120), (30, 121)])
    print("all exact:", ok)
    for r in rows:
        print(r)
    for th in (0.10, 0.15, 0.20, 0.24, 0.249, 0.2499, 0.25):
        print("  theta = %.4f   I(theta) = %.10f nats/bit" % (th, I_rate(th)))

    print("=" * 78)
    print("C4  cylinder class structure at 3000-bit starts, n = 600 letters")
    print(check_C4())

    print("=" * 78)
    print("C5  concentration of multi-letter pattern frequencies")
    for bits, starts in ((750, 1500), (1500, 1500), (3000, 1500), (6000, 600)):
        r = check_C5(bits=bits, starts=starts)
        print({k: r[k] for k in ("bits", "theta", "N_bits", "T", "starts",
                                 "seed", "S_max", "budget_violations",
                                 "mean_exponent_per_block")})
        for row in r["patterns"]:
            print("   ", row)

    print("=" * 78)
    print("C8  window side: L=2 blocks of (min(s,3), min(d,3)), concentration")
    for row in check_C8():
        print({k: row[k] for k in ("bits", "T", "starts", "cells_seen",
                                   "TV_mean", "TV_max", "TV_mean_times_sqrtT")})
        for cr in row["busiest_cells"]:
            print("   ", cr)

    print("=" * 78)
    print("C6  the past-boundary term: law of a_n at n = 0, 1, 2, ...")
    r = check_C6()
    print("bulk (13.6.5) =", r["bulk"], "  uniform start =", r["uniform_start"])
    for row in r["rows"]:
        print("   ", {k: (round(v, 5) if isinstance(v, float) else v)
                      for k, v in row.items()})

    print("=" * 78)
    print("C7  the cut is non-binding (Lemma 13.2.4(c)), door coordinates")
    print(check_C7())
    print(check_C7(bits=2400, theta=0.24, starts=200, seed=34007))


if __name__ == "__main__":
    main()
