#!/usr/bin/env python3
"""Round-8 independent verification (brief: briefs/merle-round8-check-brief.md).

Supports: briefs/merle-round8-check-findings.md.

Fresh code: imports nothing from any Merle repository and nothing from prior
Merle-check scripts (merle_round3_check.py, merle_round5_check.py,
merle_pincer_check.py, merle_aeh_key_check.py). Exact integer arithmetic at
every pass/fail decision. Canaries hand-computed first, printed before sweeps.

Conventions (cycles.md 12.6.1 / Remark 12.6.1.1): a profile is
(m_t, s_t)_{t<p}, entries >= 1; n = sum m, K = sum s + n, q = 2^K - 3^n;
sigma_t = s_t + m_{(t+1) mod p}; M_t = sum_{j>t} m_j; S_t = sum_{j<t} sigma_j;
R_0 = sum_t 3^{M_t} 2^{S_t} (2^{s_t} - 1). Transport recurrence:
2^{sigma_r} R_{r+1} = 3^{m_r} R_r + (2^{s_r} - 1) q.

Parts (per the brief, item 3):
  (a) L-A4 clean-room: R_0(B^k) = R_0(B) * (q_P / q_B) exactly, whence
      q_P | R_0(P) <=> q_B | R_0(B). Derivation in the findings file;
      verified here on an explicit grid (no tuning hypothesis needed).
  (b) L3 correction instance: v_7(q) = 3 > v_7(R_r) = 1 at every rotation of
      the recorded p = 7 staircase seed (n = 94); gcd(q, R_r) = 7.
  (c) Margin replication: margin(n) = K - log2(#profiles), the definition of
      Merle artifact REQ-MATH-014 (the ledger entry itself gives no
      operational definition -- flagged in the findings). Exact counts,
      deterministic, stated n grid. Stratum = all s_t odd ("no 3-absorption":
      3 | 2^s - 1 iff s even). General = all s_t >= 1.
  (d) Door-closure spot checks, reduced scale: degenerate-mass fraction of
      the near-integer mass (R_0/q < 1), and the mod-5 vs mod-7 contrast.
"""

import math
import random
import sys
from fractions import Fraction

FAILURES = []


def check(label, ok):
    if not ok:
        FAILURES.append(label)
        print(f"    FAIL: {label}")
    return ok


# ---------------------------------------------------------------- primitives

def profile_qK(m, s):
    n = sum(m)
    K = sum(s) + n
    return 2 ** K - 3 ** n, K, n


def R0(m, s):
    """R_0 per cycles.md 12.6.1 (sigma_t = s_t + m_{t+1 mod p})."""
    p = len(m)
    sigma = [s[t] + m[(t + 1) % p] for t in range(p)]
    total = 0
    S_pre = 0
    for t in range(p):
        M_after = sum(m[t + 1:])
        total += 3 ** M_after * 2 ** S_pre * (2 ** s[t] - 1)
        S_pre += sigma[t]
    return total


def rotations(m, s):
    p = len(m)
    return [R0(m[r:] + m[:r], s[r:] + s[:r]) for r in range(p)]


def v_p(x, p):
    if x == 0:
        return math.inf
    x = abs(x)
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v


def compositions(total, parts):
    """All compositions of `total` into `parts` integers >= 1."""
    if parts == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def rand_composition(total, parts, rng):
    """Uniform over compositions of `total` into `parts` positive integers."""
    if parts == 1:
        return [total]
    cuts = sorted(rng.sample(range(1, total), parts - 1))
    pts = [0] + cuts + [total]
    return [pts[i + 1] - pts[i] for i in range(parts)]


def rand_odd_composition(S, parts, rng):
    """Uniform over compositions of S into `parts` odd positive integers.

    s_i = 2 a_i + 1, sum a_i = A = (S - parts)/2 >= 0: uniform composition of
    A into `parts` nonneg integers via a uniform bar placement (stars and
    bars), so the draw is uniform over the C(A + parts - 1, parts - 1)
    compositions -- NOT the multinomial ensemble.
    """
    A = (S - parts) // 2
    if A < 0 or (S - parts) % 2:
        return None
    if parts == 1:
        return [S]
    bars = sorted(rng.sample(range(A + parts - 1), parts - 1))
    pts = [-1] + bars + [A + parts - 1]
    return [2 * (pts[i + 1] - pts[i] - 1) + 1 for i in range(parts)]


# ---------------------------------------------------------------- canaries

def canaries():
    print("=== CANARIES (hand-computed first) ===")
    # C0: implementation vs hand-computed R_0 values.
    #   B = ([1],[1]): q = 2^2-3 = 1, R_0 = 2^1-1 = 1.
    #   B^2 = ([1,1],[1,1]): M=(1,0), sigma_0 = 1+1 = 2, terms 3*1*1 + 1*4*1
    #   = 7; q = 2^4-3^2 = 7.  (12.6.1's own sanity identity R = 4^p - 3^p.)
    q, _, _ = profile_qK([1], [1])
    check("C0a triv base q=1", q == 1)
    check("C0b triv base R0=1", R0([1], [1]) == 1)
    qP, _, _ = profile_qK([1, 1], [1, 1])
    check("C0c triv^2 q=7", qP == 7)
    check("C0d triv^2 R0=7 (hand: 3+4)", R0([1, 1], [1, 1]) == 7)
    print("  C0  trivial word and its square: q,R = (1,1) and (7,7)  [hand]")

    # C1 (his canary): trivial-cycle inheritance. q_B | R_0(B) and
    # q_P | R_0(P) both hold; identity R_0(P) = R_0(B) * q_P/q_B: 7 = 1*7.
    check("C1 trivial-cycle inheritance", 7 % 7 == 0 and 1 % 1 == 0
          and R0([1, 1], [1, 1]) == R0([1], [1]) * (qP // q))
    print("  C1  trivial-cycle inheritance: base cycle -> B^2 cycle, "
          "R_0(B^2) = R_0(B) * q_P/q_B = 1*7")

    # C2 (our canary): B = ([2],[1]) -- the -5-shore word. Hand:
    #   q_B = 2^3-3^2 = -1, R_0(B) = 2^1-1 = 1, so q_B | R_0(B) ("cycle",
    #   |q|=1 free lock).  P = B^2: q_P = 2^6-3^4 = -17;
    #   R_0(P): m=(2,2), s=(1,1): M=(2,0), sigma_0 = 1+2 = 3,
    #   terms 9*1*1 + 1*8*1 = 17; G_2 = q_P/q_B = 17; 17 = 1*17; -17 | 17.
    qB, _, _ = profile_qK([2], [1])
    qP2, _, _ = profile_qK([2, 2], [1, 1])
    check("C2a qB=-1", qB == -1)
    check("C2b qP=-17", qP2 == -17)
    check("C2c R0(B)=1", R0([2], [1]) == 1)
    check("C2d R0(P)=17 (hand: 9+8)", R0([2, 2], [1, 1]) == 17)
    check("C2e inheritance at negative q", (R0([2], [1]) % abs(qB) == 0)
          and (R0([2, 2], [1, 1]) % abs(qP2) == 0)
          and R0([2, 2], [1, 1]) == R0([2], [1]) * (qP2 // qB))
    print("  C2  (-5)-shore word ([2],[1]): q=-1, R=1; square: q=-17, R=17 "
          "= 1 * 17  [hand]")

    # C3 (our canary, non-cycle): B = ([2,1],[3,1]). Hand:
    #   n=3, K=7, q = 128-27 = 101. M=(1,0); sigma_0 = s_0+m_1 = 4;
    #   R_0 = 3*1*(2^3-1) + 1*16*(2^1-1) = 21+16 = 37. 101 does not divide 37.
    #   B^2: q_P = 2^14-3^6 = 15655 = 101*155 (G_2 = 2^7+3^3 = 155);
    #   R_0(P) = 37*155 = 5735; 15655 does not divide 5735.
    qB3, _, _ = profile_qK([2, 1], [3, 1])
    check("C3a q=101", qB3 == 101)
    check("C3b R0=37 (hand: 21+16)", R0([2, 1], [3, 1]) == 37)
    qP3, _, _ = profile_qK([2, 1, 2, 1], [3, 1, 3, 1])
    check("C3c qP=15655=101*155", qP3 == 15655)
    check("C3d R0(P)=5735=37*155", R0([2, 1, 2, 1], [3, 1, 3, 1]) == 5735)
    check("C3e non-cycle base -> non-cycle square",
          R0([2, 1], [3, 1]) % 101 != 0
          and R0([2, 1, 2, 1], [3, 1, 3, 1]) % 15655 != 0)
    print("  C3  non-cycle base ([2,1],[3,1]): q=101, R=37; square: "
          "q=15655, R=5735 = 37*155  [hand]")

    # C4: transport recurrence 12.6.1.1 on C3's base (hand-checkable) plus
    # random profiles -- calibrates the implementation against the recurrence.
    rng = random.Random(20260724)
    ok = True
    for _ in range(200):
        p = rng.randint(1, 6)
        m = [rng.randint(1, 6) for _ in range(p)]
        s = [rng.randint(1, 6) for _ in range(p)]
        q, _, _ = profile_qK(m, s)
        R = rotations(m, s)
        for r in range(p):
            sigma_r = s[r] + m[(r + 1) % p]
            if 2 ** sigma_r * R[(r + 1) % p] != 3 ** m[r] * R[r] + (2 ** s[r] - 1) * q:
                ok = False
    check("C4 transport recurrence, 200 random profiles, all rotations", ok)
    print("  C4  transport recurrence (12.6.1.1) holds on 200 random "
          f"profiles, all rotations: {ok}")

    # C5: the recorded p=7 staircase seed reproduces its published record
    # (L2 two-key content): gamma = 6.7438, size 7/7, divisibility 0/7.
    m7 = [4, 7, 9, 15, 23, 35, 1]
    s7 = [1, 1, 1, 1, 1, 1, 49]
    q7, K7, n7 = profile_qK(m7, s7)
    check("C5a n=94,K=149", n7 == 94 and K7 == 149)
    check("C5b K = bitlength(3^94)", K7 == (3 ** 94).bit_length())
    R7 = rotations(m7, s7)
    gamma = K7 - math.log2(q7)
    check("C5c gamma=6.7438", abs(gamma - 6.7438) < 5e-5)
    check("C5d size 7/7", all(R >= q7 for R in R7))
    check("C5e divisibility 0/7", all(R % q7 != 0 for R in R7))
    print(f"  C5  p=7 staircase seed: gamma={gamma:.4f} (record 6.7438), "
          f"size {sum(R >= q7 for R in R7)}/7, "
          f"divisibility {sum(R % q7 == 0 for R in R7)}/7")
    print()


# ---------------------------------------------------------------- part (a)

def part_a():
    print("=== (a) L-A4 clean-room: q_P | R_0(P) <=> q_B | R_0(B) ===")
    print("  Identity verified at every draw: R_0(B^k) = R_0(B) * (q_P/q_B),")
    print("  with q_P/q_B = sum_{c<k} 3^{(k-1-c) n_B} 2^{c K_B} in Z (exact).")

    def one_check(m, s, k):
        """Exact identity + biconditional for P = B^k. Returns checks run."""
        qB, KB, nB = profile_qK(m, s)
        RB = R0(m, s)
        mP, sP = m * k, s * k
        qP, _, _ = profile_qK(mP, sP)
        RP = R0(mP, sP)
        G = sum(3 ** ((k - 1 - c) * nB) * 2 ** (c * KB) for c in range(k))
        check(f"G_k integer factorization q_P = q_B*G {m},{s},{k}",
              qB * G == qP)
        check(f"identity R_0(P)=R_0(B)*G {m},{s},{k}", RP == RB * G)
        check(f"biconditional {m},{s},{k}",
              (RP % qP == 0) == (RB % qB == 0))
        return 3

    total = 0
    bicond = 0
    div_pairs = 0
    # Grid 1 (exhaustive): all bases of length 1..3 with m_i, s_i in 1..3,
    # repetitions k in 2..5.  819 bases x 4 = 3,276 biconditional checks.
    for length in (1, 2, 3):
        for m in compositions_grid(length, 3):
            for s in compositions_grid(length, 3):
                for k in (2, 3, 4, 5):
                    one_check(list(m), list(s), k)
                    bicond += 1
                    qB, _, _ = profile_qK(list(m), list(s))
                    if R0(list(m), list(s)) % qB == 0:
                        div_pairs += 1
    total += bicond
    print(f"  Grid 1 (exhaustive): bases length 1..3, m_i,s_i in 1..3, "
          f"k in 2..5: {bicond} (base,k) pairs, "
          f"{div_pairs} with a divisible base (all inherited)")

    # Grid 2 (random, larger): 300 draws, length 4..6, entries 1..8, k 2..4.
    rng = random.Random(20260808)
    n2 = 0
    for _ in range(300):
        length = rng.randint(4, 6)
        m = [rng.randint(1, 8) for _ in range(length)]
        s = [rng.randint(1, 8) for _ in range(length)]
        k = rng.randint(2, 4)
        one_check(m, s, k)
        n2 += 1
    print(f"  Grid 2 (random): 300 draws, length 4..6, entries 1..8, k 2..4")
    total += n2

    # Grid 3 (tuned, mirroring his REQ-MATH-016(B) grid at reduced scale):
    # n in {24,36,60}, repetitions d with d | n and d | S, base lengths 1..3,
    # 40 random tuned bases each -- the ledger entry's own regime.
    n3 = 0
    for n in (24, 36, 60):
        K = (3 ** n).bit_length()
        S = K - n
        for d in range(2, 7):
            if n % d or S % d:
                continue
            nb, Sb = n // d, S // d
            for ell in (1, 2, 3):
                if nb < ell or Sb < ell:
                    continue
                for _ in range(40):
                    mb = rand_composition(nb, ell, rng)
                    sb = rand_composition(Sb, ell, rng)
                    one_check(mb, sb, d)
                    n3 += 1
    total += n3
    print(f"  Grid 3 (tuned regime, d | gcd(n,S)): n in {{24,36,60}}, "
          f"d = 2..6, base lengths 1..3: {n3} draws")
    print(f"  TOTAL (base,k) pairs: {total}; checks 3 each "
          f"(factorization, identity, biconditional) = {3 * total}; "
          f"failures so far: {len(FAILURES)}")
    print()


def compositions_grid(length, cap):
    """All tuples of given length with entries in 1..cap."""
    if length == 0:
        yield ()
        return
    for first in range(1, cap + 1):
        for rest in compositions_grid(length - 1, cap):
            yield (first,) + rest


# ---------------------------------------------------------------- part (b)

def part_b():
    print("=== (b) L3 correction instance: the p=7 seed fails in Z_7 ===")
    m7 = [4, 7, 9, 15, 23, 35, 1]
    s7 = [1, 1, 1, 1, 1, 1, 49]
    q7, K7, n7 = profile_qK(m7, s7)
    v7q = v_p(q7, 7)
    check("b1 v_7(q) = 3", v7q == 3)
    print(f"  q = 2^149 - 3^94; v_7(q) = {v7q} (claim: 3); "
          f"7^3 = 343 divides q: {q7 % 343 == 0}; 7^4 divides q: "
          f"{q7 % 2401 == 0}")
    R7 = rotations(m7, s7)
    all_v1 = True
    all_gcd7 = True
    for r, R in enumerate(R7):
        v = v_p(R, 7)
        g = math.gcd(q7, R)
        if v != 1:
            all_v1 = False
        if g != 7:
            all_gcd7 = False
        print(f"    rot {r}: v_7(R_r) = {v}, gcd(q, R_r) = {g}, "
              f"Z_7-solvable (v_7(R) >= v_7(q)): {v >= v7q}")
    check("b2 v_7(R_r) = 1 at every rotation", all_v1)
    check("b3 gcd(q, R_r) = 7 at every rotation", all_gcd7)
    check("b4 Z_7-insoluble at every rotation",
          all(v_p(R, 7) < v7q for R in R7))
    # The old two-key distance profile, recomputed (calibration against the
    # L3 entry's recorded [0.0538, 0.4784]).
    dists = sorted(min(R % q7, q7 - R % q7) / q7 for R in R7)
    print(f"  distance profile (recomputed): min {dists[0]:.4f}, "
          f"max {dists[-1]:.4f} (record: 0.0538, 0.4784)")
    check("b5 distance profile matches record",
          abs(dists[0] - 0.0538) < 5e-4 and abs(dists[-1] - 0.4784) < 5e-4)
    print()


# ---------------------------------------------------------------- part (c)

def count_general(n, S):
    """# profiles (m,s), p parts each, sum m = n, sum s = S: direct sum
    (independent of the closed form REQ-MATH-014 uses)."""
    return sum(math.comb(n - 1, p - 1) * math.comb(S - 1, p - 1)
               for p in range(1, min(n, S) + 1))


def odd_comp_count(S, p):
    """# compositions of S into p odd positive parts."""
    if S < p or (S - p) % 2:
        return 0
    return math.comb((S - p) // 2 + p - 1, p - 1)


def odd_comp_count_dp(S):
    """DP cross-check: total # compositions of S into odd parts (any p)."""
    ways = [0] * (S + 1)
    ways[0] = 1
    for total in range(1, S + 1):
        ways[total] = sum(ways[total - part]
                          for part in range(1, total + 1, 2))
    return ways[S]


def count_stratum(n, S):
    return sum(math.comb(n - 1, p - 1) * odd_comp_count(S, p)
               for p in range(1, min(n, S) + 1))


def part_c():
    print("=== (c) Margin replication (definition: Merle REQ-MATH-014; the "
          "ledger entry states no operational definition -- flagged) ===")
    print("  margin(n) = K - log2(#profiles), K = bitlength(3^n) = log2 q + "
          "o(1), S = K - n;")
    print("  stratum = all s_t odd; general = all s_t >= 1. Exact counts, "
          "deterministic (no sampling).")
    # Cross-check the odd-composition closed form against a DP, S <= 24.
    ok = all(sum(odd_comp_count(S, p) for p in range(1, S + 1))
             == odd_comp_count_dp(S) for S in range(1, 25))
    check("c0 odd-composition closed form vs DP (S <= 24)", ok)
    print(f"  cross-check odd-composition count (closed form vs DP, "
          f"S <= 24): {ok}")
    print(f"  {'n':>5} {'K':>6} {'log2 St':>10} {'mSt':>8} {'mSt/n':>8} "
          f"{'log2 Gen':>10} {'mGen':>8} {'mGen/n':>8}")
    results = {}
    for n in (10, 20, 40, 80, 160, 320, 640, 1280, 2560):
        K = (3 ** n).bit_length()
        S = K - n
        St = count_stratum(n, S)
        Gen = count_general(n, S)
        lSt = math.log2(St)
        lG = math.log2(Gen)
        mSt, mG = K - lSt, K - lG
        results[n] = (mSt / n, mG / n)
        print(f"  {n:>5} {K:>6} {lSt:>10.1f} {mSt:>8.1f} {mSt / n:>8.4f} "
              f"{lG:>10.1f} {mG:>8.1f} {mG / n:>8.4f}")
    # Agreement with his stated numbers (letter: ~0.27 n stratum, ~0.08 n
    # general; his table at n = 1280: 0.2730 and 109.3/1280 = 0.0854).
    mSt1280, mG1280 = results[1280]
    check("c1 stratum margin/n at n=1280 near 0.273",
          abs(mSt1280 - 0.2730) < 5e-4)
    check("c2 general margin/n at n=1280 near 0.0854",
          abs(mG1280 - 0.0854) < 5e-4)
    print(f"  n=1280: margin/n = {mSt1280:.4f} (his 0.2730) stratum, "
          f"{mG1280:.4f} (his 109.3/1280 = 0.0854) general")
    print(f"  n=2560 (our extension): {results[2560][0]:.4f} stratum, "
          f"{results[2560][1]:.4f} general -- both still declining slowly; "
          f"'~0.27 n' / '~0.08 n' are the n ~ 10^3 values, not limits.")
    print()


# ---------------------------------------------------------------- part (d)

def part_d():
    print("=== (d) Door-closure SPOT CHECKS (reduced scale; not key turns) "
          "===")
    rng = random.Random(20260809)
    # d1: near-integer degenerate-mass fraction, stratum, n in {40, 63},
    # N = 12,000 (his: 30,000 at n in {24,40,63,90}; multinomial odd-part
    # sampler -- ours is uniform over compositions; ensemble noted).
    print("  d1: fraction of the u < 0.01 mass with R_0/q < 1 "
          "(claim: 0.94-0.98)")
    for n in (40, 63):
        K = (3 ** n).bit_length()
        S = K - n
        q = 2 ** K - 3 ** n
        p = None
        for cand in range(min(6, S, n), 1, -1):
            if (S - cand) % 2 == 0:
                p = cand
                break
        N = 12000
        near = 0
        near_lt1 = 0
        for _ in range(N):
            ss = rand_odd_composition(S, p, rng)
            ms = rand_composition(n, p, rng)
            if ss is None:
                continue
            R = R0(ms, ss)
            r = R % q
            u = min(r, q - r) / q
            if u < 0.01:
                near += 1
                if R < q:
                    near_lt1 += 1
        frac = near_lt1 / max(near, 1)
        print(f"    n={n}: p={p}, N={N}, u<0.01 count {near}, "
              f"of which R_0/q<1: {frac:.2f}")
        check(f"d1 degenerate fraction at n={n} in [0.90, 1.00]",
              0.90 <= frac <= 1.00)
    # d2: mod-5 vs mod-7 contrast, stratum, n = 63, N = 12,000.
    print("  d2: R_0 mod 5 vs mod 7 (claim: 5 equidistributes, 7 biased; "
          "ord_5(2)=4, ord_7(2)=3)")
    n = 63
    K = (3 ** n).bit_length()
    S = K - n
    p = None
    for cand in range(min(6, S, n), 1, -1):
        if (S - cand) % 2 == 0:
            p = cand
            break
    samples = []
    for _ in range(12000):
        ss = rand_odd_composition(S, p, rng)
        ms = rand_composition(n, p, rng)
        if ss is not None:
            samples.append(R0(ms, ss))
    for ell in (5, 7):
        cnt = [0] * ell
        for R in samples:
            cnt[R % ell] += 1
        exp = len(samples) / ell
        chi2 = sum((c - exp) ** 2 / exp for c in cnt) / (ell - 1)
        verdict = "biased" if chi2 > 2 else "uniform"
        print(f"    mod {ell}: chi2/df = {chi2:.2f} -> {verdict}")
        if ell == 5:
            check("d2 mod 5 uniform (chi2/df < 2)", chi2 < 2)
        else:
            check("d2 mod 7 biased (chi2/df > 2)", chi2 > 2)
    print()


def main():
    canaries()
    if FAILURES:
        print("CANARY FAILURE -- stopping before sweeps.")
        sys.exit(1)
    part_a()
    part_b()
    part_c()
    part_d()
    print("=" * 60)
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}")
        for f in FAILURES:
            print(f"  - {f}")
        sys.exit(1)
    print("ALL CHECKS PASSED (0 failures)")


if __name__ == "__main__":
    main()
