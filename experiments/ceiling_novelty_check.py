"""Ceiling novelty refresh: fresh checks behind briefs/ceiling-novelty-refresh-findings.md.

Supports: briefs/ceiling-novelty-refresh-findings.md (the novelty check of paper 1
Theorems 4.5/4.6 = cycles.md 12.8.1-12.8.2 and 12.8.3/12.8.6 against the literature).
No result of cycles.md is re-proved here; this script only checks the dictionary
between the record and two held sources:

  * Simons-de Weger, Acta Arith. 117 (2005) 51-70 ("SdW"): m-cycles are defined on
    the Terras map T(x) = (3x+1)/2 (x odd), x/2 (x even); m = number of maximal runs
    of odd numbers. Lemma 7 (p. 58): 0 < Lambda < m c_m 2^(-((d-1)/(d^m-1)) K),
    d = log2 3, K = number of odd terms, with
    c_m = 2^((m/d)(d-1)/(d^m-1)) * b^(d/(d-1) - m/(d^m-1)),  b = 2^(-1/d)(1 + 1/X0).
  * Halbeisen-Hungerbuehler, Acta Arith. 78 (1997) 227-239 ("HH"): the word
    s_i = ceil(i n/l) - ceil((i-1) n/l) maximizes the rotation-minimum of the
    rational cycle (Lemma 5, Corollary 1, p. 230-231).

Parts:
  A. The record's p = 7 staircase (cycles.md 12.8.3) as a rational Terras cycle:
     the record's size test q <= R_r (12.6.1) against SdW's a_i >= 1 at every block
     start; the SdW local-minimum count against cycles.md 12.4's #{t : m_t >= 2};
     and the staircase's Lambda against SdW Lemma 7's right-hand side.
  B. The same, for one staircase per period p = 8..18 built from cycles.md
     12.8.6.2's construction as stated there (fresh transcription; the record's own
     verification of it is experiments/staircase_allp_construction.py).
  C. HH's extremal word at several lengths: its rotation-minimum is >= 1 (a
     size-passer at every length) while its SdW m grows linearly in n, so n is far
     below d^m (the HH family says nothing about the exponential-in-m cap).

Exact rational arithmetic (fractions.Fraction, Python ints) for every cycle element
and every size decision; floats only for the logarithmic comparisons in the
Lemma 7 columns, which are reported, not decided.

One command reproduces the committed output:
    python experiments/ceiling_novelty_check.py > experiments/ceiling_novelty_check_output.txt
"""

from fractions import Fraction
import math
import sys

D = math.log2(3)  # log2 3 (SdW's delta, the record's L)

FAILS = []


def check(cond, label):
    print(("  PASS  " if cond else "  FAIL  ") + label)
    if not cond:
        FAILS.append(label)


def ceil_nL(n):
    """K = ceil(n log2 3) exactly: 3^n has bitlength ceil(n log2 3) (log2 3 irrational)."""
    return (3 ** n).bit_length()


def terras_word(ms, ss):
    """Block t = m_t odd Terras steps then s_t halvings (cycles.md 12.1/12.6.1:
    n = sum m_t odd steps, K = sum s_t + n halvings)."""
    w = []
    for m, s in zip(ms, ss):
        w += [1] * m + [0] * s
    return w


def rational_cycle(w):
    """The unique rational x0 whose Terras orbit follows the cyclic word w (HH Lemma 2,
    after Lagarias), and the whole orbit, exactly."""
    a, c = Fraction(1), Fraction(0)  # x -> a x + c
    for bit in w:
        if bit:
            a, c = a * 3 / 2, (3 * c + 1) / 2
        else:
            a, c = a / 2, c / 2
    x0 = c / (1 - a)
    xs = [x0]
    for bit in w[:-1]:
        x = xs[-1]
        xs.append((3 * x + 1) / 2 if bit else x / 2)
    # closure and parity consistency (pseudo-cycle = cycle, HH Lemma 1)
    x = xs[-1]
    last = (3 * x + 1) / 2 if w[-1] else x / 2
    assert last == x0
    for x, bit in zip(xs, w):
        assert x.denominator % 2 == 1
        assert (x.numerator % 2) == bit
    return xs


def R_rotation(ms, ss, r):
    """cycles.md 12.6.1: R_r = sum_t 3^(M_t) 2^(S_t) (2^(s_t) - 1), rotation order from r,
    M_t = sum_{j>t} m_j, S_t = sum_{j<t} sigma_j, sigma_j = s_j + m_(j+1)."""
    p = len(ms)
    m = [ms[(r + t) % p] for t in range(p)]
    s = [ss[(r + t) % p] for t in range(p)]
    sig = [s[j] + m[(j + 1) % p] for j in range(p)]
    R = 0
    for t in range(p):
        M_t = sum(m[t + 1:])
        S_t = sum(sig[:t])
        R += 3 ** M_t * 2 ** S_t * (2 ** s[t] - 1)
    return R


def odd_runs(w):
    """Number of maximal runs of 1s in the cyclic word = SdW's m (local minima)."""
    p = len(w)
    return sum(1 for i in range(p) if w[i] == 1 and w[i - 1] == 0)


def lemma7_rhs_log2(m, n, X0):
    """log2 of SdW Lemma 7's right-hand side m c_m 2^(-((d-1)/(d^m-1)) n)."""
    b = 2 ** (-1 / D) * (1 + 1 / X0)
    log2_cm = (m / D) * (D - 1) / (D ** m - 1) + (D / (D - 1) - m / (D ** m - 1)) * math.log2(b)
    return math.log2(m) + log2_cm - (D - 1) / (D ** m - 1) * n


def lambda_log2(K, n):
    """log2 Lambda, Lambda = K log 2 - n log 3 = -ln(1 - q/2^K), q = 2^K - 3^n."""
    q = 2 ** K - 3 ** n
    bl = q.bit_length()
    log2q = bl - 1 + math.log2((q >> max(0, bl - 53)) / 2 ** (min(bl, 53) - 1))
    gamma = K - log2q
    lam = -math.log1p(-(2.0 ** (-gamma)))
    return math.log2(lam), gamma


def analyse(ms, ss, label, verbose=True):
    p = len(ms)
    n = sum(ms)
    K = sum(ss) + n
    q = 2 ** K - 3 ** n
    w = terras_word(ms, ss)
    xs = rational_cycle(w)
    # block starts in the word
    starts, pos = [], 0
    for m, s in zip(ms, ss):
        starts.append(pos)
        pos += m + s
    Rs = [R_rotation(ms, ss, r) for r in range(p)]
    size_record = all(q <= R for R in Rs)
    a_vals = [(xs[st] + 1) / 2 ** ms[t] for t, st in enumerate(starts)]
    size_sdw = all(a >= 1 for a in a_vals)
    # the exact dictionary: a_t = R_t / q at every block start?
    exact = all(a_vals[t] == Fraction(Rs[t], q) for t in range(p))
    m_sdw = odd_runs(w)
    m_rec = sum(1 for m in ms if m >= 2)
    xmin = min(xs[st] for st in starts)
    lamlog, gamma = lambda_log2(K, n)
    rhs = lemma7_rhs_log2(m_sdw, n, float(max(xmin, Fraction(1))))
    expo = (D - 1) / (D ** m_sdw - 1) * n
    if verbose:
        print(f"{label}: p = {p}, n = {n}, K = {K}, gamma = {gamma:.3f}, crash depth m_(p-1) = {ms[-1]}")
        print(f"    record size test (all q <= R_r): {size_record};  SdW a_t >= 1 at every block start: {size_sdw}")
        print(f"    a_t == R_t/q exactly at every block start: {exact}")
        print(f"    SdW m (maximal odd runs) = {m_sdw};  cycles.md 12.4's #{{t : m_t >= 2}} = {m_rec}")
        print(f"    smallest block-start element x_min = {float(xmin):.4f}")
        print(f"    (d-1) n/(d^m-1) = {expo:.4f};  log2 Lambda = {lamlog:.3f};  log2 Lemma-7 RHS (X0 = x_min) = {rhs:.3f};  margin = {rhs - lamlog:.3f} bits")
    return dict(p=p, n=n, size_record=size_record, size_sdw=size_sdw, exact=exact,
                m_sdw=m_sdw, m_rec=m_rec, lamlog=lamlog, rhs=rhs, expo=expo, gamma=gamma)


def construct(p, n):
    """cycles.md 12.8.6.2's construction, transcribed from the statement."""
    K = ceil_nL(n)
    S = K - n
    q = 2 ** K - 3 ** n
    s_crash = S - (p - 1)
    if s_crash < 1:
        return None
    T = 0
    ms = []
    for r in range(p - 1):
        X = 3 ** T * 2 ** (n - T + p - 1 - r) * (2 ** s_crash - 1)
        cap = (X // q).bit_length() - 1
        budget = n - 1 - T - (p - 2 - r)
        m = min(cap, budget)
        if m < 1:
            return None
        ms.append(m)
        T += m
    ms.append(n - T)
    if ms[-1] < 1:
        return None
    ss = [1] * (p - 1) + [s_crash]
    return ms, ss


def gamma_of(n):
    K = ceil_nL(n)
    q = 2 ** K - 3 ** n
    bl = q.bit_length()
    return K - (bl - 1 + math.log2((q >> max(0, bl - 53)) / 2 ** (min(bl, 53) - 1)))


def main():
    print("Ceiling novelty refresh - dictionary checks (fresh code)")
    print("=" * 72)

    print("\nPart A - the record's p = 7 staircase (cycles.md 12.8.3)")
    ms = [4, 7, 9, 15, 23, 35, 1]
    n = sum(ms)
    K = ceil_nL(n)
    ss = [1] * 6 + [K - n - 6]
    A = analyse(ms, ss, "  p=7 staircase")
    check(n == 94 and K == 149, "n = 94, K = ceil(94 log2 3) = 149")
    check(A["size_record"] and A["size_sdw"], "passes all 7 record size tests and all 7 SdW a_t >= 1")
    check(A["exact"], "dictionary: SdW a_t = (x_t + 1)/2^(m_t) equals the record's R_t/q at every block start")
    check(abs(A["gamma"] - 6.74) < 0.01, "gamma = 6.74 as published")
    check(A["m_sdw"] == 7 and A["m_rec"] == 6, "SdW m = 7 = p, while cycles.md 12.4's formula gives 6")
    check(A["lamlog"] < A["rhs"], "SdW Lemma 7 holds on the configuration (its hypotheses a_i >= 1 hold)")

    print("\nPart B - one 12.8.6.2 staircase per period, p = 8..18 (first n >= L^p meeting (H1))")
    rows = []
    for p in range(8, 19):
        lo = math.ceil(D ** p)
        found = None
        for n in range(lo, int(1.70 * D ** p) + 2):
            K = ceil_nL(n)
            S = K - n
            if S < p:
                continue
            eta = -math.log2(1 - 2 ** (-(S - p + 1)))
            beta = 1 + eta
            L = D
            Gam = ((n - 1) * (L - 1) ** 2 + L ** (p - 1) * (1 + beta * (L - 1)) - (p - 2 + beta) * (L - 1) - L) / ((L - 1) * (L ** (p - 1) - 1))
            g = gamma_of(n)
            if g >= max(2 + eta, Gam) and (L - 1) * (n - p) + g >= p + eta:
                c = construct(p, n)
                if c is not None:
                    found = (n, c)
                    break
        if found is None:
            check(False, f"p = {p}: no witness found in [L^p, 1.70 L^p]")
            continue
        n, (ms, ss) = found
        R = analyse(ms, ss, f"  p={p:2d}", verbose=False)
        rows.append(R)
        print(f"  p={p:2d} n={n:7d} gamma={R['gamma']:.3f} crash={ms[-1]} size(record/SdW)={R['size_record']}/{R['size_sdw']} exact={R['exact']} "
              f"m_SdW={R['m_sdw']} 12.4-formula={R['m_rec']} expo={R['expo']:.3f} log2Lam={R['lamlog']:.3f} log2RHS={R['rhs']:.3f} margin={R['rhs'] - R['lamlog']:.3f}")
    check(all(R["size_record"] and R["size_sdw"] and R["exact"] for R in rows),
          "every Part-B staircase passes all size tests, in both dictionaries, with a_t = R_t/q exactly")
    check(all(R["m_sdw"] == R["p"] for R in rows), "SdW m = p for every Part-B staircase")
    check(all(R["m_rec"] < R["p"] for R in rows), "cycles.md 12.4's formula #{t : m_t >= 2} undercounts SdW's m at every Part-B p")
    check(all(R["gamma"] <= 5.140212 for R in rows if R["p"] >= 16),
          "p >= 16: these first-found witnesses have gamma <= 5.140212 (the record's upper bracket, 12.8.6.1)")
    check(all(R["expo"] < 1.1 for R in rows),
          "Lemma 7's exponent (d-1)n/(d^m-1) stays O(1) (< 1.1) along the family: the d^(-m) decay is met")
    check(all(R["lamlog"] < R["rhs"] for R in rows),
          "SdW Lemma 7 holds on every Part-B staircase (Lambda below its RHS)")

    print("\nPart C - Halbeisen-Hungerbuehler's extremal word (Lemma 5): size-passers at every length, m linear in n")
    for l in [41, 101, 211, 409, 1009]:
        n = int(math.floor(l * math.log(2) / math.log(3)))
        w = [math.ceil(i * n / l) - math.ceil((i - 1) * n / l) for i in range(1, l + 1)]
        assert sum(w) == n
        xs = rational_cycle(w)
        odd_min = min(x for x, b in zip(xs, w) if b == 1)
        m = odd_runs(w)
        # HH Corollary 1 closed form for M_{l,n}
        M = sum((math.ceil(j * n / l) - math.ceil((j - 1) * n / l)) * 2 ** (j - 1) * 3 ** (n - math.ceil(j * n / l)) for j in range(1, l + 1))
        hh = Fraction(M, 2 ** l - 3 ** n)
        rot_min = min(xs)
        print(f"  l={l:5d} n={n:4d} m_SdW={m:4d} min element={float(rot_min):10.3f}  M/(2^l-3^n)={float(hh):10.3f}  n/d^m={n / D ** m:.3e}")
        check(rot_min == hh, f"l = {l}: direct rotation-minimum equals HH's Corollary 1 value")
        check(rot_min >= 1 or l < 60, f"l = {l}: a size-passer (min element >= 1) once l >= 60")
        check(m >= n // 3, f"l = {l}: m grows linearly in n (m >= n/3), so n << d^m")

    print("\n" + "=" * 72)
    print(f"RESULT: {'ALL CHECKS PASS' if not FAILS else str(len(FAILS)) + ' FAILURE(S)'}")
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
