"""Re-check of cycles.md 12.4's m-cycle translation (brief: briefs/cycles-12-4-recheck-brief.md).

Supports: cycles.md 12.4 (the m-cycle translation) and briefs/cycles-12-4-recheck-findings.md.

Question. Simons-de Weger 2005 (Acta Arith. 117, 51-70; v1.44 p. 2) define an m-cycle on the
Terras map T(x) = (3x+1)/2 (x odd), x/2 (x even): a periodic orbit with m local minima, the
period read as m sequences "each consisting of an increasing subsequence of odd numbers,
followed by a decreasing subsequence of even numbers"; k_i = rising steps, l_i = falling steps,
K = sum k_i odd terms, L = sum l_i even terms. cycles.md 12.4 translates a period-p reduced cycle
to an m-cycle with m = #{t : m_t >= 2}. This script counts SdW's m directly on raw Terras
orbits built from reduced block data and compares it with p and with the 12.4 formula.

Fresh code: imports nothing from experiments/ (in particular nothing from
ceiling_novelty_check.py). Exact Fraction arithmetic at every decision. Seeded, deterministic.

Method, per profile (m_t, s_t)_{t<p} with entries >= 1:
  1. Compose the Terras branches of the word 1^{m_0} 0^{s_0} ... 1^{m_{p-1}} 0^{s_{p-1}} into
     x -> A x + B and take the rational fixed point x0 = B / (1 - A) (odd denominator q).
  2. Iterate the Terras map on x0 with parity read off the orbit itself (parity of a rational
     with odd denominator = parity of its numerator, i.e. its 2-adic parity), for |word| steps;
     check closure and that the observed parity vector is the word.
  3. Spine check at every block start x: m_t = v_2(x+1), u = (x+1)/2^m_t odd,
     s_t = v_2(3^m_t u - 1), and the exit (3^m_t u - 1)/2^s_t is the next block start
     (spine.md 5.4-5.5; the block in Terras steps is exactly 1^{m_t} 0^{s_t}).
  4. Count, on the raw orbit: SdW's m as strict local minima of the cyclic value sequence
     (positive shore, q > 0), local maxima, and maximal odd runs of the observed parity vector;
     check the minima sit exactly at the block starts. On the negative shore (q < 0) value order
     is reversed by odd steps, so the structural count (odd runs) is used, plus value extrema.
  5. Compare with p and with the 12.4 formula #{t : m_t >= 2}.

Controls: the trivial cycle 1 (SdW's own 1-cycle {1,2}); the published p = 7 staircase of
cycles.md 12.8.3; the negative-shore integer cycles -5 and -17 traced from their integers
(profile recovered from the orbit, not supplied); -1 recorded as outside the block coding.

Run (one command, reproduces the committed output):
    python experiments/cycles_12_4_recheck.py > experiments/cycles_12_4_recheck_output.txt
"""

from fractions import Fraction
import math
import random

LOG2_3 = math.log2(3)
CHECKS = 0
FAILS = 0


def check(cond, label):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        print("FAIL:", label)


def v2_int(z):
    if z == 0:
        raise ValueError("v2(0)")
    z = abs(z)
    return (z & -z).bit_length() - 1


def v2(x):
    """2-adic valuation of a Fraction with odd denominator."""
    x = Fraction(x)
    assert x.denominator % 2 == 1
    return v2_int(x.numerator)


def is_odd(x):
    x = Fraction(x)
    assert x.denominator % 2 == 1
    return x.numerator % 2 != 0


def terras(x):
    return (3 * x + 1) / 2 if is_odd(x) else x / 2


def word_of(ms, ss):
    w = []
    for m, s in zip(ms, ss):
        w += [1] * m + [0] * s
    return w


def fixed_point(word):
    A, B = Fraction(1), Fraction(0)
    for b in word:  # apply branch after current composition
        if b:
            A, B = 3 * A / 2, (3 * B + 1) / 2
        else:
            A, B = A / 2, B / 2
    return B / (1 - A)


def runs_of_ones(bits):
    """Number of maximal runs of 1s in a cyclic bit vector (bits not all 1)."""
    n = len(bits)
    return sum(1 for i in range(n) if bits[i] == 1 and bits[i - 1] == 0)


def local_minima(vals):
    n = len(vals)
    return [i for i in range(n) if vals[i - 1] > vals[i] < vals[(i + 1) % n]]


def local_maxima(vals):
    n = len(vals)
    return [i for i in range(n) if vals[i - 1] < vals[i] > vals[(i + 1) % n]]


def formula_12_4(ms):
    return sum(1 for m in ms if m >= 2)


def analyse(ms, ss, label=None):
    """Build the raw Terras cycle of a profile; return a dict of counts. Runs all checks."""
    p = len(ms)
    word = word_of(ms, ss)
    n, K = sum(ms), sum(ms) + sum(ss)
    q = 2 ** K - 3 ** n
    x0 = fixed_point(word)
    check(x0.denominator % 2 == 1, f"{label}: odd denominator")
    # step 2: orbit with parity read from the orbit
    vals, bits = [], []
    x = x0
    for _ in range(len(word)):
        vals.append(x)
        bits.append(1 if is_odd(x) else 0)
        x = terras(x)
    check(x == x0, f"{label}: closure")
    check(bits == word, f"{label}: observed parity = block word")
    # step 3: spine block check
    starts = []
    pos = 0
    for t in range(p):
        starts.append(pos)
        xs = vals[pos]
        mt = v2(xs + 1)
        u = (xs + 1) / 2 ** mt
        A = 3 ** mt * u - 1
        st = v2(A)
        check(is_odd(xs) and is_odd(u), f"{label}: block {t} start and seed odd")
        check(mt == ms[t] and st == ss[t], f"{label}: block {t} (m,s) from orbit")
        pos += ms[t] + ss[t]
        check(A / 2 ** st == vals[pos % len(word)], f"{label}: block {t} exit = next start")
    # step 4: counts
    runs = runs_of_ones(bits)
    mins = local_minima(vals)
    maxs = local_maxima(vals)
    odd_vals = [vals[i] for i in range(len(vals)) if bits[i]]
    odd_mins = len(local_minima(odd_vals)) if len(odd_vals) > 2 else None
    out = dict(p=p, n=n, K=K, q=q, runs=runs, mins=len(mins), maxs=len(maxs),
               f124=formula_12_4(ms), shallow=sum(1 for m in ms if m == 1), odd_mins=odd_mins)
    check(runs == p, f"{label}: odd runs = p")
    if q > 0:
        check(all(v > 0 for v in vals), f"{label}: positive cycle")
        check(mins == starts, f"{label}: local minima are exactly the block starts")
        check(len(maxs) == p, f"{label}: local maxima = p")
    else:
        check(all(v < 0 for v in vals), f"{label}: negative cycle")
        # odd steps decrease value on the negative shore: value maxima sit at block starts
        check(maxs == starts, f"{label}: value maxima (|x| minima) are exactly the block starts")
    check(out["f124"] == p - out["shallow"], f"{label}: formula = p - #shallow")
    return out


def trace_integer_cycle(x0):
    """Trace an integer Terras cycle from x0; return (vals, bits)."""
    vals, bits, x = [], [], x0
    while True:
        vals.append(x)
        bits.append(x & 1)
        x = (3 * x + 1) // 2 if x & 1 else x // 2
        if x == x0:
            return vals, bits
        if len(vals) > 10 ** 4:
            raise RuntimeError("no cycle")


def profile_from_bits(bits):
    """Rotate so a block starts at index 0 (bit 1 preceded by 0); read (m_t, s_t)."""
    n = len(bits)
    start = next(i for i in range(n) if bits[i] == 1 and bits[i - 1] == 0)
    b = bits[start:] + bits[:start]
    ms, ss, i = [], [], 0
    while i < n:
        j = i
        while j < n and b[j] == 1:
            j += 1
        k = j
        while k < n and b[k] == 0:
            k += 1
        ms.append(j - i)
        ss.append(k - j)
        i = k
    return ms, ss, start


def main():
    print("cycles.md 12.4 recheck: SdW m on raw Terras orbits vs p vs #{t : m_t >= 2}")
    print("=" * 78)

    # Part A: controls
    print("\nPart A. Controls")
    print(f"{'cycle':<26}{'p':>3}{'runs':>6}{'SdW m':>7}{'12.4':>6}{'#m_t=1':>8}  note")
    # trivial cycle: SdW's own 1-cycle {1,2}
    r = analyse([1], [1], "trivial")
    check(r["q"] == 1, "trivial q = 1")
    print(f"{'trivial {1,2}':<26}{r['p']:>3}{r['runs']:>6}{r['mins']:>7}{r['f124']:>6}{r['shallow']:>8}"
          "  SdW call {1,2} a 1-cycle (v1.44 p.2)")
    check(r["mins"] == 1 and r["f124"] == 0, "trivial: SdW m = 1, formula = 0")
    # published p = 7 staircase (cycles.md 12.8.3 / 12.8.6 cross-check)
    ms = [4, 7, 9, 15, 23, 35, 1]
    n = sum(ms)
    K = math.ceil(n * LOG2_3)
    ss = [1] * 6 + [K - n - 6]
    r = analyse(ms, ss, "staircase p=7")
    check((n, K) == (94, 149), "staircase n = 94, K = 149")
    print(f"{'staircase p=7 (12.8.3)':<26}{r['p']:>3}{r['runs']:>6}{r['mins']:>7}{r['f124']:>6}{r['shallow']:>8}"
          f"  n={n}, K={K}, s_6={ss[6]}, rational (not integral)")
    check(r["mins"] == 7 and r["f124"] == 6, "staircase: SdW m = 7, formula = 6")
    # negative-shore integer cycles, traced from integers
    for x0, expect in ((-5, ([2], [1])), (-17, ([4, 3], [1, 3]))):
        vals, bits = trace_integer_cycle(x0)
        ms_, ss_, _ = profile_from_bits(bits)
        check((ms_, ss_) == expect, f"{x0}: profile recovered from integer orbit")
        r = analyse(ms_, ss_, f"cycle {x0}")
        check(r["q"] < 0, f"{x0}: q < 0")
        # rational fixed point of the recovered word is the integer cycle itself
        check(fixed_point(word_of(ms_, ss_)) in [Fraction(v) for v in vals], f"{x0}: fixed point on orbit")
        print(f"{'cycle ' + str(x0) + ' (traced)':<26}{r['p']:>3}{r['runs']:>6}{'-':>7}{r['f124']:>6}{r['shallow']:>8}"
              f"  profile m={ms_}, s={ss_}, q={r['q']}; runs counted")
    vals, bits = trace_integer_cycle(-1)
    check(bits == [1], "-1: Terras fixed point, word '1', no even step")
    print(f"{'cycle -1':<26}{'-':>3}{'-':>6}{'-':>7}{'-':>6}{'-':>8}"
          "  word '1' (no even term): v_2(x+1) undefined, outside the block coding")

    # Part B: random admissible block data
    print("\nPart B. Random profiles, entries >= 1, p = 2..20 (seed 20261019)")
    print("  pos: q > 0 (positive rational cycles, last s_t raised to K = ceil(n log2 3));")
    print("  raw: s_t as drawn, either sign of q. 'SdW m' = strict local minima by value (pos);")
    print("  'runs' = maximal odd runs of the observed parity vector (all draws).")
    rng = random.Random(20261019)
    hdr = (f"{'p':>3}{'draws':>7}{'pos':>5}{'runs=p':>8}{'minima=p':>10}{'12.4<p':>8}"
           f"{'12.4=p':>8}{'max gap':>9}{'oddseq min<p':>14}")
    print(hdr)
    tot = dict(draws=0, pos=0, runs=0, mins=0, lt=0, eq=0)
    for p in range(2, 21):
        row = dict(draws=0, pos=0, runs=0, mins=0, lt=0, eq=0, gap=0, oddlt=0)
        for j in range(60):
            ms = [rng.choice([1, 1, 2, 3, 4, 5, 6, 8, 12]) for _ in range(p)]
            ss = [rng.randint(1, 3) for _ in range(p)]
            if j % 2 == 0:  # positive shore
                n = sum(ms)
                need = math.ceil(n * LOG2_3) - (n + sum(ss))
                if need > 0:
                    ss[-1] += need
            if j == 0:  # force at least one all-deep draw per p (formula = p case)
                ms = [max(2, m) for m in ms]
                n = sum(ms)
                need = math.ceil(n * LOG2_3) - (n + sum(ss))
                if need > 0:
                    ss[-1] += need
            r = analyse(ms, ss, f"random p={p} #{j}")
            row["draws"] += 1
            row["runs"] += r["runs"] == p
            if r["q"] > 0:
                row["pos"] += 1
                row["mins"] += r["mins"] == p
            row["lt"] += r["f124"] < p
            row["eq"] += r["f124"] == p
            row["gap"] = max(row["gap"], p - r["f124"])
            if r["odd_mins"] is not None and r["odd_mins"] < p:
                row["oddlt"] += 1
            check((r["f124"] < p) == (r["shallow"] > 0), f"random p={p} #{j}: formula < p iff some m_t = 1")
        check(row["runs"] == row["draws"] and row["mins"] == row["pos"], f"p={p}: SdW m = p on every draw")
        print(f"{p:>3}{row['draws']:>7}{row['pos']:>5}{row['runs']:>8}{row['mins']:>10}{row['lt']:>8}"
              f"{row['eq']:>8}{row['gap']:>9}{row['oddlt']:>14}")
        for k in tot:
            tot[k] += row[k]
    print(f"{'all':>3}{tot['draws']:>7}{tot['pos']:>5}{tot['runs']:>8}{tot['mins']:>10}{tot['lt']:>8}{tot['eq']:>8}")

    print("\nReading. SdW's m (local minima, equivalently maximal odd runs) equals p on every")
    print("profile; the 12.4 formula equals p - #{t : m_t = 1} and is below p exactly when some")
    print("block has entry depth 1 (block start = 1 mod 4). The last column is informational:")
    print("local minima of the odd-only subsequence, the frame in which a depth-1 block 'falls'.")
    print(f"\nTotal: {CHECKS} checks, {FAILS} failures")
    print("ALL CHECKS PASS" if FAILS == 0 else "FAILURES PRESENT")


if __name__ == "__main__":
    main()
