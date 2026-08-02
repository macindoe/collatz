"""Independent check of aeh.md Lemma 13.2.4(g) and Corollary 13.2.4.1.

Supports: aeh.md `13.2.4`(g) -- the budget clause and the exponent mean -- and
the density `e^(-Theta(b))` that Corollary `13.2.4.1` quotes from it.

Fresh implementation.  Imports nothing from any other file in experiments/: the
block decomposition, the door letters, the exact tail law and the rate are all
built here from the definitions in the record (stage1.md's size ledger,
`x = 2^m u - 1` with exit `(3^m u - 1)/2^s`; aeh.md `13.2.3`'s `m + s` divisions
per block; aeh.md `13.2.4`(a)-(b)).

What is checked
  1. the exact tail identity  P_B(S_n >= J) = P(Bin(J-1,1/2) < 2n)  at ten
     (n, J) pairs, by exact rational convolution of 2n geometric(1/2) laws --
     no binomial coefficient enters that side of the comparison;
  2. the rate  I(theta, tau) = tau (log 2 - H(2 theta / tau))  of (g): its
     reduction to (b)'s  I(theta) = log 2 - H(2 theta)  at tau = 1, its values
     at the theta printed on the page, and that it is the measured exponential
     decay rate of the tail term;
  3. on real uniformly sampled odd starts: that the budget does not bind, that
     the empirical exponent mean converges to E_B[m + r] = 4, and that the
     printed bound 2 delta_N(tau) is respected;
  4. a negative control at tau < 4 theta, where (g) predicts the budget binds;
  5. the ingredients of (g)'s budget-versus-letter offset: the clock identity
     x_exit(n-1) = T_1^(S_n)(x), monotonicity of the budget count, the bound of
     the offset by the start's own block exponent m_0 + s_0, the exact law
     P_B(m + r >= t) = t 2^(1-t), and the composite bound the offset clause uses.

Run:  python aeh_budget_clause.py
"""

import math
import random
from fractions import Fraction

# ---------------------------------------------------------------- primitives


def v2(n):
    """2-adic valuation of a positive integer."""
    return (n & -n).bit_length() - 1


def block_step(y):
    """One reduced block from odd y.

    y + 1 = 2^m u with u odd; the block runs m odd steps of T and exits at
    (3^m u - 1)/2^s.  Returns (m, s, exit).  The block spends m + s divisions.
    """
    m = v2(y + 1)
    u = (y + 1) >> m
    A = 3**m * u - 1
    s = v2(A)
    return m, s, A >> s


def T1(y):
    """The one-division map y -> y/2 (y even), (3y+1)/2 (y odd)."""
    return y >> 1 if (y & 1) == 0 else (3 * y + 1) >> 1


def orbit_blocks(x, nblocks):
    """Lists m[i], s[i] and entries xs[i] (xs[0] = x) for the first nblocks."""
    ms, ss, xs = [], [], [x]
    y = x
    for _ in range(nblocks):
        m, s, y = block_step(y)
        ms.append(m)
        ss.append(s)
        xs.append(y)
    return ms, ss, xs


def rand_odd_start(rng, b):
    """Uniform odd integer of [2^b, 2^(b+1))."""
    return rng.randrange(1 << b, 1 << (b + 1)) | 1


# ------------------------------------------------- 1. the exact tail identity


def tail_by_convolution(n, J):
    """P_B(S_n >= J), S_n a sum of 2n iid geometric(1/2) on {1,2,...}.

    Exact rational forward convolution.  Only masses at k <= J-1 are kept; the
    answer is 1 minus their total, so nothing is lost at the truncation edge.
    """
    f = {0: Fraction(1)}
    for _ in range(2 * n):
        g = {}
        for k, p in f.items():
            j = 1
            while k + j <= J - 1:
                g[k + j] = g.get(k + j, Fraction(0)) + p * Fraction(1, 2**j)
                j += 1
        f = g
    return Fraction(1) - sum(f.values(), Fraction(0))


def tail_by_binomial(n, J):
    """P(Bin(J-1, 1/2) < 2n), exactly."""
    M = J - 1
    return Fraction(sum(math.comb(M, i) for i in range(min(2 * n, M + 1))), 2**M)


def check_tail_identity():
    pairs = [(1, 4), (2, 7), (3, 10), (4, 9), (5, 20), (6, 13),
             (7, 30), (9, 25), (11, 45), (12, 28)]
    print("1. exact tail identity  P_B(S_n >= J) = P(Bin(J-1,1/2) < 2n)")
    bad = 0
    for n, J in pairs:
        a = tail_by_convolution(n, J)
        c = tail_by_binomial(n, J)
        ok = (a == c)
        bad += (not ok)
        print("   (n=%2d, J=%2d)  %s   %s" % (n, J, a, "EQUAL" if ok else "MISMATCH"))
    print("   pairs: %d, mismatches: %d" % (len(pairs), bad))
    return bad


# --------------------------------------------------------- 2. the rate I(t,t)


def H_nats(p):
    """Binary entropy in nats."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log(p) + (1 - p) * math.log(1 - p))


def I_theta(theta):
    """(b)'s rate log 2 - H(2 theta)."""
    return math.log(2) - H_nats(2 * theta)


def I_theta_tau(theta, tau):
    """(g)'s rate tau (log 2 - H(2 theta / tau))."""
    return tau * (math.log(2) - H_nats(2 * theta / tau))


def log_binom_lower_tail(M, k):
    """log P(Bin(M, 1/2) < k), by log-sum-exp on exact log-binomials."""
    if k <= 0:
        return float("-inf")
    k = min(k, M + 1)
    terms = [math.lgamma(M + 1) - math.lgamma(i + 1) - math.lgamma(M - i + 1)
             for i in range(k)]
    mx = max(terms)
    return mx + math.log(sum(math.exp(t - mx) for t in terms)) - M * math.log(2)


def check_rate():
    print("\n2. the rate I(theta, tau) = tau (log 2 - H(2 theta / tau))")
    print("   (i) reduction to (b)'s I(theta) at tau = 1")
    worst = 0.0
    for th in (0.05, 0.10, 0.15, 0.18, 0.20, 0.22, 0.24, 0.245, 0.2499):
        d = abs(I_theta_tau(th, 1.0) - I_theta(th))
        worst = max(worst, d)
        print("       theta=%-7.4f  I(theta,1)=%.12f  I(theta)=%.12f  |diff|=%.2e"
              % (th, I_theta_tau(th, 1.0), I_theta(th), d))
    print("       worst |I(theta,1) - I(theta)| = %.3e" % worst)

    print("   (ii) the values printed on the page (aeh.md, the base-case paragraph)")
    for th in (0.20, 0.24, 0.25):
        print("       I(%.2f) = %.12f" % (th, I_theta(th)))

    print("   (iii) measured decay rate  -ln P(Bin(ceil(tau b)-1,1/2) < 2 ceil(theta b)) / b")
    for (th, tau) in ((0.20, 0.95), (0.22, 0.99), (0.20, 0.85), (0.24, 0.98)):
        row = []
        for b in (500, 2000, 8000, 32000, 128000):
            M = math.ceil(tau * b) - 1
            k = 2 * math.ceil(th * b)
            row.append(-log_binom_lower_tail(M, k) / b)
        print("       (theta,tau)=(%.2f,%.2f)  I=%.8f  measured: %s"
              % (th, tau, I_theta_tau(th, tau),
                 "  ".join("%.8f" % r for r in row)))

    print("   (iv) negative control: the tail term at tau < 4 theta does not vanish")
    for (th, tau) in ((0.20, 0.60), (0.24, 0.85), (0.15, 0.45)):
        row = [math.exp(log_binom_lower_tail(math.ceil(tau * b) - 1,
                                             2 * math.ceil(th * b)))
               for b in (500, 2000, 8000, 32000)]
        print("       (theta,tau)=(%.2f,%.2f)  4theta=%.2f  tail: %s"
              % (th, tau, 4 * th, "  ".join("%.10f" % r for r in row)))
    return worst


# --------------------------------------------------------------- delta_N(tau)


def delta_N(b, theta, tau):
    """(g)'s delta_N(tau): window term 2^(Lambda_N+2)/N + tail term, at N = 2^b."""
    Lam = math.ceil(tau * b)
    T_N = math.ceil(theta * b)
    window = math.exp((Lam + 2 - b) * math.log(2))
    tail = math.exp(log_binom_lower_tail(Lam - 1, 2 * T_N))
    return window + tail


# ---------------------------------------- 3./4./5. real orbits and the offset


def run_starts(b, theta, tau, ntrials, seed):
    """Measure the budget clause and the exponent mean on real odd starts."""
    rng = random.Random(seed)
    T_N = math.ceil(theta * b)
    Lam = math.ceil(tau * b)
    binds = 0
    means = []
    offs_ok = True
    mono_ok = True
    clock_ok = True
    first_exps = []
    for t in range(ntrials):
        x = rand_odd_start(rng, b)
        ms, ss, xs = orbit_blocks(x, T_N + 1)

        # budget count S^bud_n = sum_{i<n} (m_i + s_i): divisions x -> x_exit(n-1)
        Sbud = [0]
        for i in range(len(ms)):
            Sbud.append(Sbud[-1] + ms[i] + ss[i])
        mono_ok &= all(Sbud[i] <= Sbud[i + 1] for i in range(len(Sbud) - 1))

        # the clock identity of 13.2.3, on the first trial of each cell
        if t == 0:
            y = x
            for _ in range(Sbud[T_N]):
                y = T1(y)
            clock_ok &= (y == xs[T_N])

        # block n is tallied dagger iff S^bud_n >= Lambda_N, for n < T_N
        if Sbud[T_N - 1] >= Lam:
            binds += 1

        # letter word of x: letter i = stratum(G^i x) = (m_i, s_i); the shifted
        # reading of 13.2.1/13.2.4 is letter i = (m_{i+1}, s_{i+1}).  The offset
        # of the budget count from either is at most the start's own block
        # exponent m_0 + s_0 at every index -- which is what (g)'s clause needs.
        bound = ms[0] + ss[0]
        for n in range(1, T_N + 1):
            SletA = sum(ms[i] + ss[i] for i in range(n))
            SletB = sum(ms[i + 1] + ss[i + 1] for i in range(n))
            if not (Sbud[n] - SletA <= bound and Sbud[n] - SletB <= bound):
                offs_ok = False
        first_exps.append(bound)

        means.append(sum(ms[i] + ss[i] for i in range(T_N)) / T_N)

    mu = sum(means) / len(means)
    sd = (sum((m - mu) ** 2 for m in means) / len(means)) ** 0.5
    return dict(T_N=T_N, Lam=Lam, binds=binds, n=ntrials, mean=mu, sd=sd,
                offs_ok=offs_ok, mono_ok=mono_ok, clock_ok=clock_ok,
                first_exps=first_exps)


def check_orbits():
    print("\n3. real odd starts, 4 theta < tau < 1: the budget does not bind, and")
    print("   the empirical exponent mean converges to E_B[m + r] = 4")
    print("   %6s %5s %5s %6s %7s %14s %22s %10s" %
          ("b", "theta", "tau", "T_N", "Lam_N", "budget binds", "mean (s.d.)", "2 delta_N"))
    cells = [(400, 0.20, 0.90, 1000, 88001),
             (800, 0.20, 0.90, 1000, 88002),
             (1600, 0.20, 0.90, 200, 88003),
             (3200, 0.20, 0.90, 80, 88004),
             (1600, 0.10, 0.55, 200, 88005),
             (1600, 0.22, 0.95, 200, 88006)]
    flags = []
    for (b, th, tau, k, seed) in cells:
        r = run_starts(b, th, tau, k, seed)
        d2 = 2 * delta_N(b, th, tau)
        print("   %6d %5.2f %5.2f %6d %7d %8d / %-5d %10.5f (%.5f) %10.3e"
              % (b, th, tau, r["T_N"], r["Lam"], r["binds"], r["n"],
                 r["mean"], r["sd"], d2))
        flags.append((r, d2, b, th, tau))
    print("   clock identity x_exit(n-1) = T_1^(S_n)(x): %s" %
          ("0 failures" if all(f[0]["clock_ok"] for f in flags) else "FAILED"))
    print("   budget count nondecreasing:                %s" %
          ("0 failures" if all(f[0]["mono_ok"] for f in flags) else "FAILED"))
    print("   offset <= m_0 + s_0 at every index, both letter readings: %s" %
          ("0 failures" if all(f[0]["offs_ok"] for f in flags) else "FAILED"))
    for (r, d2, b, th, tau) in flags:
        obs = r["binds"] / r["n"]
        if obs > d2:
            # P(at least this many binds | p = the printed bound): a count this
            # small is not evidence against the bound unless this is tiny.
            n, k = r["n"], r["binds"]
            p_at_least = sum(math.comb(n, i) * d2 ** i * (1 - d2) ** (n - i)
                             for i in range(k, n + 1))
            print("   b=%d: observed %d/%d = %.5f above 2 delta_N = %.5f;"
                  " P(>= %d | p = bound) = %.3f"
                  % (b, k, n, obs, d2, k, p_at_least))

    print("\n4. negative control, tau < 4 theta: (g) predicts the budget binds")
    print("   %6s %5s %5s %7s %14s" % ("b", "theta", "tau", "4 theta", "budget binds"))
    for (b, th, tau, k, seed) in [(1600, 0.24, 0.90, 100, 88011),
                                  (1600, 0.20, 0.70, 100, 88012),
                                  (800, 0.25, 0.95, 100, 88013)]:
        r = run_starts(b, th, tau, k, seed)
        print("   %6d %5.2f %5.2f %7.2f %8d / %-5d"
              % (b, th, tau, 4 * th, r["binds"], r["n"]))
    return flags


# --------------------------------------------- 5. the offset clause's own law


def letter_exponent_tail(t):
    """P_B(m + r >= t) by exact rational convolution of two geometric(1/2)."""
    tot = Fraction(0)
    for k in range(2, t):
        # P(m + r = k) built by convolution, not by a closed form
        pk = sum(Fraction(1, 2**j) * Fraction(1, 2 ** (k - j))
                 for j in range(1, k))
        tot += pk
    return Fraction(1) - tot


def check_offset_law(flags):
    print("\n5. the offset clause: the law of the start's own block exponent")
    print("   P_B(m + r >= t) against the closed form t 2^(1-t)")
    bad = 0
    for t in range(2, 15):
        exact = letter_exponent_tail(t)
        closed = Fraction(t, 2 ** (t - 1))
        ok = exact == closed
        bad += (not ok)
        print("       t=%2d  P_B = %-22s  t 2^(1-t) = %-22s  %s"
              % (t, exact, closed, "EQUAL" if ok else "MISMATCH"))
    print("   mismatches: %d" % bad)

    print("   measured tail of m_0 + s_0 on uniform odd starts (b = 1600, 3000 starts)")
    rng = random.Random(88021)
    K = 3000
    vals = []
    for _ in range(K):
        x = rand_odd_start(rng, 1600)
        m, s, _ = block_step(x)
        vals.append(m + s)
    print("       %4s %12s %12s" % ("t", "measured", "t 2^(1-t)"))
    for t in (2, 3, 4, 5, 6, 8, 10, 12):
        meas = sum(1 for v in vals if v >= t) / K
        print("       %4d %12.5f %12.5f" % (t, meas, t / 2.0 ** (t - 1)))
    print("       mean m_0 + s_0 = %.5f  (E_B = 4),  max = %d"
          % (sum(vals) / K, max(vals)))

    print("\n   the composite bound of the repaired offset clause, at the")
    print("   midpoint choice rho = (1 - 4 theta / tau) / 2, so that")
    print("   (1-rho)tau = (tau + 4 theta)/2 lies strictly inside (4 theta, 1):")
    print("   P(S^bud_(T_N) >= Lam_N) <= 2 delta_N((1-rho)tau) + delta_N(tau)")
    print("                              + rho Lam_N 2^(1 - rho Lam_N)")
    print("   %6s %5s %5s %6s %10s %12s %12s" %
          ("b", "theta", "tau", "rho", "(1-rho)tau", "observed", "bound"))
    for (r, d2, b, th, tau) in flags:
        rho = (1 - 4 * th / tau) / 2
        tau2 = (1 - rho) * tau
        Lam = math.ceil(tau * b)
        bound = (2 * delta_N(b, th, tau2) + delta_N(b, th, tau)
                 + rho * Lam * 2.0 ** (1 - rho * Lam))
        obs = r["binds"] / r["n"]
        print("   %6d %5.2f %5.2f %6.4f %10.4f %12.6f %12.3e"
              % (b, th, tau, rho, tau2, obs, bound))
    return bad


if __name__ == "__main__":
    print("aeh.md Lemma 13.2.4(g) / Corollary 13.2.4.1 -- independent check")
    print("=" * 72)
    b1 = check_tail_identity()
    check_rate()
    fl = check_orbits()
    b2 = check_offset_law(fl)
    print("\n" + "=" * 72)
    print("structural failures: tail identity %d, offset law %d" % (b1, b2))
