#!/usr/bin/env python3
"""Independent check of aeh.md Lemma 13.2.4(a): which word it is about, and the
tail term that word needs.

Supports: aeh.md `13.2.4`(a) -- the word law
    TV(Law(l_0, ..., l_(n-1)), B^(x)n)  <=  2^(J+2)/N + P_B(S_(n+1) >= J)
-- and the altitude line of `13.2.4`(c).  `13.2.4` sets y_(-1) = x and
y_n = G^(n+1)(x), so l_n = stratum(G^(n+1)(x)): the word of (a) is the letter
word of the start with its FIRST letter deleted, and the cylinder count of
itinerary.md `14.15.1.5` therefore has to charge for the start's own letter.
The tail term is the B-mass of n+1 letters, not n.  This file measures the
exact total variation, in rationals, over every odd start of [2^b, 2^(b+1)),
and shows that the n-letter tail term is violated while the (n+1)-letter one
is not.

Fresh implementation.  Imports nothing from any other file in experiments/:
the stratum, the door map G, the accelerated map T, the Bernoulli reference
law and the tail law are all rebuilt here from the definitions in the record
(itinerary.md `14.15.1.1` stratum, `14.15.1.2` word/follower, `14.15.1.5`
cylinder theorem; reverse.md `14.14.7.1` block-map identity; aeh.md `13.6.1`
letter law, `13.2.3` clock identity, `13.2.4` its own indexing).

What is checked
  C0  G = T^m with m = v_2(y+1) (reverse.md 14.14.7.1), and the clock identity
      x_exit(k-1) = T_1^(S_k)(x) run literally, S_k the exponent of the start's
      own letter word -- the word of 13.2.3's budget sum.
  C1  The cylinder structure of the SHIFTED word, exhaustively: for a leading
      letter u and a word W, the odd x with stratum(x) = u whose G-image
      follows W are exactly one class mod 2^(|u|+S(W)+1); and the x whose
      G-image follows W, over all leading letters, are NOT one class mod
      2^(S(W)+1) -- so the n-letter count does not apply to this word.
  C2  Exact total variation over every odd start of [2^b, 2^(b+1)), in
      rationals, at b = 12, 16, 20, 24, under both readings:
        (A) (stratum(G^i x))_{i=0..n-1}   -- the word 14.15.1.5 is about;
        (B) (stratum(G^i x))_{i=1..n}     -- the word 13.2.4 defines.
      Compared against the n-letter tail P_B(S_n >= b) and the (n+1)-letter
      tail P_B(S_(n+1) >= b).  At N = 2^b the window term of (a) is 0.
  C3  The proof's own chain: TV_B(n) <= TV_A(n+1) <= P_B(S_(n+1) >= b).  The
      first inequality is that (a)'s word is a marginal of the extended word
      (stratum(x), l_0, ..., l_(n-1)); the second is 14.15.1.5 on the extended
      word.
  C4  A general (non-dyadic) window [N, 2N), where the full printed bound
      2^(J+2)/N + tail is tested with both tail terms.
  C5  The tail identity P_B(S_n >= J) = P(Bin(J-1,1/2) < 2n) by exact rational
      convolution of the one-letter law P(m + r = t) = (t-1)2^(-t).
  C6  13.2.4(c)'s altitude line: log2(y_n + 1) > log2 N - S_n as printed
      against log2(y_n + 1) > log2 N - (m_(-1) + r_(-1)) - S_n with the
      start's own letter, on real starts.

Run:  python aeh_word_shift.py
"""

from fractions import Fraction
from math import comb
import random
import time

# --------------------------------------------------------------- definitions


def v2(k):
    """2-adic valuation of a positive integer."""
    return (k & -k).bit_length() - 1


def stratum(y):
    """itinerary.md 14.15.1.1: m = v_2(y+1), q = (y+1)/2^m, r = v_2(3^m q - 1)."""
    m = v2(y + 1)
    q = (y + 1) >> m
    return m, v2(3 ** m * q - 1)


def G(y):
    """The door/exit map, reverse.md 14.14.3.1."""
    m = v2(y + 1)
    q = (y + 1) >> m
    val = 3 ** m * q - 1
    return val >> v2(val)


def T(x):
    """The accelerated odd Collatz map, spine.md 9.8."""
    z = 3 * x + 1
    return z >> v2(z)


def T1(y):
    """The one-division map of 13.2.3."""
    return (y >> 1) if y % 2 == 0 else (3 * y + 1) >> 1


# ----------------------------------------------------- C0  G = T^m, the clock


def check_blockmap(trials=2000, seed=93001):
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        y = 2 * rng.randrange(1, 1 << 60) + 1
        m, _ = stratum(y)
        z = y
        for _ in range(m):
            z = T(z)
        if z != G(y):
            bad += 1
    return trials, bad


def check_clock(trials=200, nsteps=10, seed=93002):
    """x_exit(k-1) = T_1^(S_k)(x), S_k the exponent of the start's own word."""
    rng = random.Random(seed)
    checks = bad = 0
    for _ in range(trials):
        x = 2 * rng.randrange(1, 1 << 200) + 1
        y = x
        tot = 0
        for _ in range(nsteps):
            m, r = stratum(y)
            tot += m + r
            y = G(y)
            z = x
            for _ in range(tot):
                z = T1(z)
            checks += 1
            if z != y:
                bad += 1
    return checks, bad


# -------------------------------------------- C1  the shifted word's cylinders


def check_shifted_cylinders(limit_bits=18, cap=12, wcap=8):
    """Exhaustive over odd x < 2^limit_bits, one-letter target words W.

    positive: {x : stratum(x) = u, stratum(G(x)) = W} is one class mod
              2^(|u|+|W|+1)  -- 14.15.1.5 on the two-letter word (u, W).
              Taken over the pairs with |u| + |W| <= cap, so that the scan
              range holds many members of each class.
    negative: {x : stratum(G(x)) = W}, over ALL leading letters u, is NOT one
              class mod 2^(|W|+1) -- the modulus the n-letter count would give.
              Taken over the words with |W| <= wcap, again so that the scan
              range is not itself the limitation.
    """
    pos_ok = pos_bad = 0
    neg_ok = neg_bad = 0
    by_pair = {}
    by_word = {}
    for x in range(1, 1 << limit_bits, 2):
        u = stratum(x)
        w = stratum(G(x))
        if u[0] + u[1] + w[0] + w[1] <= cap:
            by_pair.setdefault((u, w), []).append(x)
        if w[0] + w[1] <= wcap:
            by_word.setdefault(w, []).append(x)
    for (u, w), xs in by_pair.items():
        mod = 1 << (u[0] + u[1] + w[0] + w[1] + 1)
        if len(set(x % mod for x in xs)) == 1:
            pos_ok += 1
        else:
            pos_bad += 1
    spread = []
    for w, xs in by_word.items():
        mod = 1 << (w[0] + w[1] + 1)
        k = len(set(x % mod for x in xs))
        spread.append(k)
        if k == 1:
            neg_bad += 1
        else:
            neg_ok += 1
    return pos_ok, pos_bad, neg_ok, neg_bad, min(spread), max(spread)


# ---------------------------------------------------------- the reference law


def tail_binom(n, J):
    """P_B(S_n >= J) = P(Bin(J-1, 1/2) < 2n), exact."""
    return Fraction(sum(comb(J - 1, k) for k in range(min(2 * n, J))),
                    1 << (J - 1))


def tail_convolve(n, J):
    """The same quantity by exact convolution of n one-letter exponents,
    P(m + r = t) = (t-1) 2^(-t) for t >= 2.  No binomial coefficient enters."""
    dist = {0: Fraction(1)}
    for _ in range(n):
        nd = {}
        for s, p in dist.items():
            for t in range(2, J - s + 1):
                nd[s + t] = nd.get(s + t, Fraction(0)) + p * Fraction(t - 1, 1 << t)
        dist = nd
    return 1 - sum(p for s, p in dist.items() if s < J)


# ------------------------------------------------------- exact total variation


def exact_tv(counts, M):
    """TV between the empirical word law (counts over M starts) and B^(x)n.

    Exact: everything is put over a common power of two and the missing
    B-mass of the unrealized words is added in full.
    """
    e = M.bit_length() - 1                      # M = 2^e starts
    assert M == 1 << e
    D = e
    for w in counts:
        S = sum(a + b for a, b in w)
        if S > D:
            D = S
    tot = 0
    bmass = 0
    for w, c in counts.items():
        S = sum(a + b for a, b in w)
        tot += abs(c * (1 << (D - e)) - (1 << (D - S)))
        bmass += 1 << (D - S)
    tot += (1 << D) - bmass                      # words never realized
    return Fraction(tot, 1 << (D + 1))


def exact_tv_general(counts, M):
    """Same, for a window whose odd-integer count M is not a power of two."""
    D = 0
    for w in counts:
        S = sum(a + b for a, b in w)
        if S > D:
            D = S
    tot = Fraction(0)
    bmass = Fraction(0)
    for w, c in counts.items():
        S = sum(a + b for a, b in w)
        tot += abs(Fraction(c, M) - Fraction(1, 1 << S))
        bmass += Fraction(1, 1 << S)
    tot += 1 - bmass
    return tot / 2


def word_laws(lo, hi, nmax):
    """Collect both readings' length-n word laws for the odd x in [lo, hi)."""
    lawA = [None] + [dict() for _ in range(nmax)]
    lawB = [None] + [dict() for _ in range(nmax)]
    M = 0
    for x in range(lo if lo % 2 else lo + 1, hi, 2):
        M += 1
        y = x
        letters = []
        for _ in range(nmax + 1):
            letters.append(stratum(y))
            y = G(y)
        for n in range(1, nmax + 1):
            wa = tuple(letters[:n])
            lawA[n][wa] = lawA[n].get(wa, 0) + 1
            wb = tuple(letters[1:n + 1])
            lawB[n][wb] = lawB[n].get(wb, 0) + 1
    return lawA, lawB, M


# --------------------------------------------------- C6  (c)'s altitude line


def check_altitude(trials=200, nmax=25, seed=93003):
    """13.2.4(c): log2(y_n + 1) > log2 N - S_n as printed, against the same
    with the start's own letter (m_(-1) + r_(-1)) subtracted as well."""
    rng = random.Random(seed)
    printed_fail = corrected_fail = checks = 0
    for _ in range(trials):
        b = 400
        x = (1 << b) + 2 * rng.randrange(0, 1 << (b - 1)) + 1
        logN = b                                    # N = 2^b, x in [N, 2N)
        m1, r1 = stratum(x)                         # the start's own letter
        y = G(x)                                    # y_0 of 13.2.4
        S = 0
        for _ in range(nmax):
            checks += 1
            lo = (y + 1).bit_length() - 1           # <= log2(y+1)
            if not lo > logN - S:
                printed_fail += 1
            if not lo > logN - (m1 + r1) - S:
                corrected_fail += 1
            m, r = stratum(y)
            S += m + r
            y = G(y)
    return checks, printed_fail, corrected_fail


# ------------------------------------------------------------------- driver


def main():
    t0 = time.time()
    print("=" * 78)
    print("aeh.md 13.2.4(a): the word, and the tail term it needs")
    print("=" * 78)

    n, bad = check_blockmap()
    print("C0  G = T^(v_2(y+1)) on %d random doors: %d failures" % (n, bad))
    n, bad = check_clock()
    print("C0  clock identity x_exit(k-1) = T_1^(S_k)(x), %d checks: %d failures"
          % (n, bad))

    po, pb, no, nb, smin, smax = check_shifted_cylinders()
    print("C1  shifted word, exhaustive on odd x < 2^18:")
    print("      (u, W) one class mod 2^(|u|+S(W)+1):  %d ok, %d failures"
          % (po, pb))
    print("      W alone one class mod 2^(S(W)+1):     %d words correctly "
          "spread over more than one class, %d not" % (no, nb))
    print("      (classes mod 2^(S(W)+1) actually met: %d to %d)"
          % (smin, smax))

    mism = 0
    for n_ in (1, 2, 3, 4):
        for J in (12, 16, 20, 24):
            if tail_binom(n_, J) != tail_convolve(n_, J):
                mism += 1
    print("C5  tail identity, binomial vs convolution, 16 (n, J) pairs: "
          "%d mismatches" % mism)

    print()
    print("C2/C3  exact total variation over every odd start of [2^b, 2^(b+1)),")
    print("       N = 2^b and J = b, where (a)'s window term is 0")
    print()
    hdr = ("  b   n   TV_B (13.2.4's word)      printed P_B(S_n>=b)   "
           "repaired P_B(S_(n+1)>=b)  B/printed  B<=pr  B<=rep  B<=TV_A(n+1)")
    for b, nmax in ((12, 5), (16, 5), (20, 5), (24, 3)):
        lawA, lawB, M = word_laws(1 << b, 1 << (b + 1), nmax + 1)
        print(hdr)
        for k in range(1, nmax + 1):
            tvA1 = exact_tv(lawA[k + 1], M)
            tvB = exact_tv(lawB[k], M)
            printed = tail_binom(k, b)
            repaired = tail_binom(k + 1, b)
            print("  %-3d %-3d %-25s %-21s %-25s %-10.3f %-6s %-7s %s"
                  % (b, k, "%s = %.6e" % (tvB, float(tvB)),
                     "%s" % printed, "%s" % repaired,
                     float(tvB / printed), tvB <= printed, tvB <= repaired,
                     tvB <= tvA1 <= repaired))
        # reading (A), the control: inside the printed bound at every cell
        ctrl = all(exact_tv(lawA[k], M) <= tail_binom(k, b)
                   for k in range(1, nmax + 1))
        print("      reading (A) inside the printed bound at every n <= %d: %s"
              "   [%.1fs]" % (nmax, ctrl, time.time() - t0))
        print()

    print("C4  general window [N, 2N), N not a power of two")
    for N, J, nmax in ((1000003, 14, 3), (700001, 12, 3)):
        lawA, lawB, M = word_laws(N, 2 * N, nmax + 1)
        win = Fraction(1 << (J + 2), N)
        for k in range(1, nmax + 1):
            tvB = exact_tv_general(lawB[k], M)
            pr = win + tail_binom(k, J)
            rp = win + tail_binom(k + 1, J)
            print("      N=%d J=%d n=%d  TV_B=%.6e  printed=%.6e (%s)  "
                  "repaired=%.6e (%s)"
                  % (N, J, k, float(tvB), float(pr), tvB <= pr,
                     float(rp), tvB <= rp))
    print()

    checks, pf, cf = check_altitude()
    print("C6  13.2.4(c) altitude line, %d checks on 400-bit starts:" % checks)
    print("      printed   log2(y_n+1) > log2 N - S_n              : %d failures"
          % pf)
    print("      corrected log2(y_n+1) > log2 N - (m+r)_(-1) - S_n : %d failures"
          % cf)
    print()
    print("done in %.1fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
