#!/usr/bin/env python3
"""mirror_baker_cap.py -- verification for reverse.md Remark 14.2.5 (effective
bound: contact with 3-adic Baker theory), the mirror of stage1-synthesis.md
11.8.3.11 flagged by Brett Rubin (correspondence 2026-09-05).

Fresh, independent implementation (2026-09-08). Imports nothing from any
other script in this directory, and nothing from the main session's
scratchpad pre-check. Exact integer arithmetic at every pass/fail decision
in PARTS A-E; PARTS F-G evaluate the (real-valued) Baker bound formula
itself and are measurements, not pass/fail laws, exactly as
spentstock_digitcap.py's PART G and stage1-synthesis.md 11.8.3.11's own
numeric sanity check are.

Object under test:
  reverse.md Theorem 14.2.4: d = v3(2^s y + 1) = 1 + v3(s - M3(y)), for a
  door y (odd, 3 not| y) and s of the admissible parity (14.1.1: s odd if
  y == 1 mod 3, s even if y == 2 mod 3).

  Squaring reduction (mirrors 11.8.3.11's use of Lemma 3.2 of paper 1):
  for admissible (y,s), v3(2^s y + 1) >= 1 and v3(2^s y - 1) = 0 (the two
  differ by 2, a 3-adic unit), so
      d = v3(2^s y + 1) = v3(4^s y^2 - 1) = v3(alpha1^b1 - alpha2^b2)
  with alpha1 = 4, alpha2 = y^(-2), b1 = s, b2 = 1: both alpha1, alpha2 are
  rational (D = 1 in Bugeaud-Laurent's notation) and both principal units
  mod 3 (4 == 1, y^(-2) == 1 mod 3, since y^2 == 1 mod 3 by Fermat: g = 1,
  automatic, mirroring 11.8.3.11's "9 == 1 (mod 8), g = 1" at p = 2), and
  multiplicatively independent exactly when |y| != 1 (y odd): 4 = 2^2
  carries only the prime 2, y^(-2) (for |y| >= 5, y coprime to 6) carries
  none, so 4^a = y^(-2b) forces a = b = 0 unless y = +-1.

  Excluded case y = +-1 (Rubin's "e = 1 degeneration", his D = -1/2):
  Lemma 14.2.1 gives d = 1 + v3(s) directly (LTE, y = 1: 2^s+1^s with s
  odd; y = -1: 2^s - 1 with s even) -- exact, no Baker input, and in fact
  *sharper* than the general cap (linear in log s, not (log s)^2).

  Bugeaud-Laurent (1996) Corollaire 2, general-p statement restated in full
  by M. A. Bennett and Y. Bugeaud, "Effective results for restricted
  rational approximation to quadratic irrationals" (2011), Theorem 2.1 (a
  "slightly simplified" restatement of what they cite as Théorème 3 of
  the 1996 paper -- see the findings for the exact naming caveat): with
  D = [Q(alpha1,alpha2):Q], g the least positive integer with
  alpha1^g == alpha2^g == 1 (mod p), A1 >= max(h(alpha1), log(p)/D),
  A2 >= max(h(alpha2), log(p)/D), b' = b1/(D log A2) + b2/(D log A1),

      v_p(alpha1^b1 - alpha2^b2)
        <= [24 p g / ((p-1)(log p)^4)] D^4
           (max{log b' + log log p + 0.4, 10 log p / D, 10})^2
           log A1 log A2.

  PART G below checks this general formula, specialized at p=2, D=1, g=1,
  A1=9, A2=omega, b1=n, b2=1, reproduces 11.8.3.11's own pinned constant
  C(omega) = 208 log9 logomega and its three worked numeric values
  (omega=5: ~73555 up to n~34000, ~131500 at n=10^6, ~302500 at n=10^9) --
  the control the brief requires before trusting the p=3 specialization.

  PART F specializes at p=3, D=1, g=1, A1=4, A2=y^2, b1=s, b2=1, giving
      C3(y) := 144 log2 logy / (log3)^4   (~68.52 * log|y|)
  as the coefficient in d <= C3(y)*(log s)^2 (up to the floor, exactly as
  11.8.3.11's own C(omega) statement is qualified), and measures it against
  observed maxima of d(y,s) including Rubin's two named deep instances.

  PART D reproduces Rubin's two quoted valuations directly by integer
  computation (e=5,k=1 -> d=4; e=41,k=13 -> d=6), and PART C verifies his
  parametrization s = (e mod 3) + 2k, D_rubin = (M3(e) - e mod 3)/2 against
  a freshly built discrete-log table for M3 (not the anchor code of any
  other script), independent of the direct integer computation.

Output is written by this script itself to
experiments/mirror_baker_cap_output.txt (next to the script), and to
stdout. Seeded; no timestamps; re-runs are byte-identical.
"""

import os
import random
import sys
from math import exp, log

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "mirror_baker_cap_output.txt")

FAILURES = []


class Tee:
    def __init__(self, path):
        self.f = open(path, "w", encoding="utf-8", newline="\n")
        self.stdout = sys.stdout

    def write(self, s):
        self.stdout.write(s)
        self.f.write(s)

    def flush(self):
        self.stdout.flush()
        self.f.flush()

    def close(self):
        self.f.close()


def v3(x: int) -> int:
    assert x != 0
    n = 0
    while x % 3 == 0:
        x //= 3
        n += 1
    return n


def check(label: str, ok: bool, detail: str = "") -> None:
    if not ok:
        FAILURES.append((label, detail))
        print(f"  FAIL {label} {detail}")


def required_parity(y: int) -> int:
    """1 if s must be odd (y == 1 mod 3), 0 if s must be even (y == 2 mod 3)."""
    r = y % 3
    assert r != 0, f"3 | y = {y}, not a live door"
    return 1 if r == 1 else 0


def random_live_y(rng: random.Random, lo: int, hi: int) -> int:
    """A random odd y in [lo, hi] with 3 not| y, y != +-1."""
    while True:
        y = rng.randrange(lo, hi + 1)
        if y % 2 == 0:
            continue
        if y % 3 == 0:
            continue
        if abs(y) == 1:
            continue
        return y


def admissible_s(rng: random.Random, y: int, lo: int, hi: int) -> int:
    par = required_parity(y)
    s = rng.randrange(lo, hi + 1)
    if s % 2 != par:
        s += 1
    if s < lo:
        s = lo if lo % 2 == par else lo + 1
    return s


# ---------- discrete-log table for M3, built fresh, base 2 mod 3^k --------
def build_dlog_table(k: int):
    """2 generates (Z/3^k)*, of order ord = 2*3^(k-1). Returns (table, mod,
    ord) with table[value] = the unique exponent x in [0, ord) s.t. 2^x ==
    value (mod 3^k)."""
    mod = 3 ** k
    ordr = 2 * 3 ** (k - 1)
    table = {}
    cur = 1
    for x in range(ordr):
        table[cur] = x
        cur = (cur * 2) % mod
    assert len(table) == ordr, "2 failed to generate (Z/3^k)*: not a bug we expect"
    return table, mod, ordr


def M3_repr(y: int, table: dict, mod: int) -> int:
    """The representative of M3(y) in [0, ord): the x with 2^x == -1/y (mod 3^k)."""
    yy = y % mod
    inv = pow(yy, -1, mod)
    target = (-inv) % mod
    return table[target]


# =============================================================================
# PART 0: canaries (printed first; expected values written down before this
# code ran, from the brief's paraphrase of Rubin's letter and Lemma 14.2.1)
# =============================================================================
def part0_canaries():
    print("=" * 70)
    print("PART 0: canaries")
    print("=" * 70)
    # C1: Rubin's e=5, k=1 -> d=4.  s = (5 mod 3) + 2*1 = 4; N = 2^4*5+1 = 81 = 3^4.
    s = (5 % 3) + 2 * 1
    N = 2 ** s * 5 + 1
    print(f"  C1 e=5,k=1: s={s}, N=2^s*5+1={N}, v3(N)={v3(N)}  (expect s=4, N=81, d=4)")
    check("C1", (s, N, v3(N)) == (4, 81, 4))

    # C2: Rubin's e=41, k=13 -> d=6.  s = (41 mod 3) + 26 = 28.
    s = (41 % 3) + 2 * 13
    N = 2 ** s * 41 + 1
    print(f"  C2 e=41,k=13: s={s}, v3(N)={v3(N)}  (expect s=28, d=6)")
    check("C2", (s, v3(N)) == (28, 6))

    # C3: y=1 degenerate case, s=1 (odd, admissible): d = 1+v3(1) = 1.
    N = 2 ** 1 * 1 + 1
    print(f"  C3 y=1,s=1: N={N}, v3(N)={v3(N)}  (expect 3, d=1+v3(1)=1)")
    check("C3", v3(N) == 1)

    # C4: y=-1, s=2 (even, admissible): d = 1+v3(2) = 1; N = 1-4 = -3.
    N = 2 ** 2 * (-1) + 1
    print(f"  C4 y=-1,s=2: N={N}, v3(N)={v3(N)}  (expect -3, d=1)")
    check("C4", v3(N) == 1)

    # C5: M3(1) truncation, Prop 14.2.3: mod 2*3^(k-1) it equals 3^(k-1). k=4.
    table, mod, ordr = build_dlog_table(4)
    r = M3_repr(1, table, mod)
    print(f"  C5 M3(1) mod {ordr} = {r}  (expect {3**3} = 27)")
    check("C5", r == 27)

    # C6: M3(-1) = 0 exactly (2^0 = 1 = -1/-1).
    r = M3_repr(-1, table, mod)
    print(f"  C6 M3(-1) mod {ordr} = {r}  (expect 0)")
    check("C6", r == 0)
    print()


# =============================================================================
# PART A: squaring reduction v3(2^s y+1) = v3(4^s y^2 -1), and the two
# valuation facts it rests on, on a grid of admissible (y,s).
# =============================================================================
def partA(rng, n_y=200, s_lo=1, s_hi=80):
    print("=" * 70)
    print("PART A: squaring reduction on a grid of (y, s)")
    print("=" * 70)
    n_checks = 0
    ys = [random_live_y(rng, -5000, 5000) for _ in range(n_y)]
    ys += [1, -1]  # include the degenerate case: the identity itself needs no independence
    for y in ys:
        par = required_parity(y) if abs(y) != 1 else (1 if y == 1 else 0)
        for s in range(s_lo, s_hi + 1):
            if s % 2 != par:
                continue
            lhs_pre = 2 ** s * y - 1
            lhs = 2 ** s * y + 1
            check("A.pre.ge1", v3(lhs) >= 1 if lhs != 0 else False, f"y={y} s={s}")
            check("A.pre.eq0", v3(lhs_pre) == 0 if lhs_pre != 0 else False, f"y={y} s={s}")
            rhs = 4 ** s * y * y - 1
            check("A.square", v3(lhs) == v3(rhs), f"y={y} s={s} lhs={v3(lhs)} rhs={v3(rhs)}")
            n_checks += 3
    print(f"  {len(ys)} values of y, s in [{s_lo},{s_hi}] at admissible parity: "
          f"{n_checks} checks")
    print()
    return n_checks


# =============================================================================
# PART B: law 14.2.4 against a freshly built digit-lifting table for M3.
# =============================================================================
def partB(rng, k_table=10, n_pairs=3000, s_hi=200):
    print("=" * 70)
    print(f"PART B: d = 1 + v3(s - M3(y)), fresh discrete-log table mod 3^{k_table}")
    print("=" * 70)
    table, mod, ordr = build_dlog_table(k_table)
    guard = k_table - 2  # stay well inside precision; 3-part of ordr is 3^(k_table-1)
    n_checks = 0
    n_guarded = 0
    for _ in range(n_pairs):
        y = random_live_y(rng, -10 ** 6, 10 ** 6)
        s = admissible_s(rng, y, 1, s_hi)
        d_direct = v3(2 ** s * y + 1)
        m3 = M3_repr(y, table, mod)
        diff = (s - m3) % (3 ** (k_table - 1) * 2)
        # reduce to the Z3 part: diff is even (parity cancels, both share it)
        assert diff % 2 == 0, (y, s, m3, diff)
        val = v3(diff) if diff != 0 else k_table - 1
        if val >= guard:
            n_guarded += 1
            continue  # precision insufficient to certify this one; skip, don't fake a pass
        check("B.law", d_direct == 1 + val, f"y={y} s={s} d={d_direct} 1+v3={1+val}")
        n_checks += 1
    print(f"  {n_pairs} random (y,s) pairs, table depth 3^{k_table}: "
          f"{n_checks} certified checks, {n_guarded} skipped at the precision guard")
    print()
    return n_checks


# =============================================================================
# PART C: Rubin's parametrization s=(e mod 3)+2k, D=(M3(e)-e mod 3)/2, and
# the identity v3(k-D) = v3(s-M3(e)).
# =============================================================================
def partC(rng, k_table=10, n_pairs=2000, k_hi=500):
    print("=" * 70)
    print("PART C: Rubin's parametrization and v3(k-D) = v3(s-M3(e))")
    print("=" * 70)
    table, mod, ordr = build_dlog_table(k_table)
    mod3 = 3 ** (k_table - 1)
    guard = k_table - 2
    n_checks = 0
    n_guarded = 0
    for _ in range(n_pairs):
        e = random_live_y(rng, -10 ** 5, 10 ** 5)
        k = rng.randrange(0, k_hi + 1)
        s = (e % 3) + 2 * k
        m3e = M3_repr(e, table, mod)
        delta = (m3e - (e % 3)) % (2 * mod3)
        assert delta % 2 == 0, (e, m3e, delta)
        D_rubin = (delta // 2) % mod3
        diffA = (k - D_rubin) % mod3
        diffB = (s - m3e) % (2 * mod3)
        assert diffB % 2 == 0
        diffB_half = (diffB // 2) % mod3
        vA = v3(diffA) if diffA != 0 else guard
        vB = v3(diffB_half) if diffB_half != 0 else guard
        if vA >= guard or vB >= guard:
            n_guarded += 1
            continue
        check("C.identity", vA == vB, f"e={e} k={k} vA={vA} vB={vB}")
        # also cross-check against the direct integer law: d = 1 + v3(k-D) should
        # equal 1 + v3(s - M3(e)), i.e. the two readings of the same door step.
        d_direct = v3(2 ** s * e + 1)
        check("C.vs_direct", d_direct == 1 + vA, f"e={e} k={k} d={d_direct} 1+vA={1+vA}")
        n_checks += 2
    print(f"  {n_pairs} random (e,k) pairs, k <= {k_hi}, table depth 3^{k_table}: "
          f"{n_checks} certified checks, {n_guarded} skipped at the precision guard")
    print()
    return n_checks


# =============================================================================
# PART D: Rubin's two quoted valuations, direct integer computation.
# =============================================================================
def partD():
    print("=" * 70)
    print("PART D: Rubin's two quoted deep instances (direct integer check)")
    print("=" * 70)
    cases = [(5, 1, 4), (41, 13, 6)]
    n_checks = 0
    for e, k, expected_d in cases:
        s = (e % 3) + 2 * k
        N = 2 ** s * e + 1
        d = v3(N)
        print(f"  e={e} k={k}: s={s}, N={N}, d=v3(N)={d}  (expected d={expected_d})")
        check("D.rubin", d == expected_d, f"e={e} k={k}")
        n_checks += 1
    print(f"  {n_checks} checks")
    print()
    return n_checks


# =============================================================================
# PART E: the excluded case y = +-1, exact via lifting-the-exponent.
# =============================================================================
def partE(s_hi=2000):
    print("=" * 70)
    print("PART E: y = +-1, exact law d = 1 + v3(s), lifting-the-exponent")
    print("=" * 70)
    n_checks = 0
    for s in range(1, s_hi + 1, 2):  # odd s, y=1
        N = 2 ** s * 1 + 1
        d = v3(N)
        check("E.y1", d == 1 + v3(s), f"s={s} d={d}")
        n_checks += 1
    for s in range(2, s_hi + 1, 2):  # even s, y=-1
        N = 2 ** s * (-1) + 1
        d = v3(N)
        check("E.yminus1", d == 1 + v3(s), f"s={s} d={d}")
        n_checks += 1
    print(f"  y=1 (s odd) and y=-1 (s even), s <= {s_hi}: {n_checks} checks")
    print()
    return n_checks


# =============================================================================
# PART F: the specialized p=3 constant C3(y), and the observed texture
# against it (measurement, not a law -- exactly stage1-synthesis.md
# 11.8.3.11's own numeric sanity check, and spentstock_digitcap.py PART G).
# =============================================================================
def baker_bound(p, D, g, logA1, logA2, bprime):
    pref = 24 * p * g / ((p - 1) * (log(p) ** 4)) * (D ** 4)
    inner = max(log(bprime) + log(log(p)) + 0.4, 10 * log(p) / D, 10)
    return pref * inner ** 2 * logA1 * logA2


def C3(y: int) -> float:
    """Coefficient of (log s)^2 in the p=3 specialization, D=1,g=1,
    A1=4, A2=y^2: C3(y) = 144 log2 logy / (log3)^4."""
    return 144 * log(2) * log(abs(y)) / (log(3) ** 4)


def p3_bound(s, y):
    logA1 = log(4)
    logA2 = 2 * log(abs(y))
    bprime = s / logA2 + 1 / logA1
    return baker_bound(3, 1, 1, logA1, logA2, bprime)


def partF():
    print("=" * 70)
    print("PART F: C3(y), and observed max d(y,s) against the cap (texture)")
    print("=" * 70)
    print(f"  C3 coefficient 144*log2/(log3)^4 = {144*log(2)/log(3)**4:.6f}")
    for y in (5, 7, 11, 13, 41):
        print(f"  C3({y}) = {C3(y):.4f}")
    print()
    print("  Bounded texture: max_(s<=S, admissible parity) d(y,s), fresh integer scan,")
    print("  against the cap p3_bound(S,y) at the same S:")
    n_checks = 0
    ys = (5, 7, 11, 13, 41, -5, -7)
    S = 4000
    for y in ys:
        par = required_parity(y)
        best_d, best_s = 0, None
        for s in range(1 if par == 1 else 2, S + 1, 2):
            N = 2 ** s * y + 1
            d = v3(N)
            if d > best_d:
                best_d, best_s = d, s
        cap = p3_bound(S, y)
        print(f"    y={y:4d}: max d = {best_d:2d} at s = {best_s:5d}   "
              f"(cap at S={S}: {cap:,.1f})")
        check("F.texture", best_d <= cap, f"y={y} max_d={best_d} cap={cap}")
        n_checks += 1
    print()
    # Rubin's two named instances against the cap at their own s.
    for e, k in ((5, 1), (41, 13)):
        s = (e % 3) + 2 * k
        d = v3(2 ** s * e + 1)
        cap = p3_bound(s, e)
        print(f"    Rubin instance e={e},k={k}: s={s}, d={d}, cap(s,e)={cap:,.1f} "
              f"-- cap nowhere near binding")
        check("F.rubin_vs_cap", d <= cap, f"e={e} k={k}")
        n_checks += 1
    print(f"  {n_checks} checks (measurement: the cap is a ceiling, not a target)")
    print()

    # Sanity-check narrative, exactly mirroring stage1-synthesis.md 11.8.3.11's
    # own numeric paragraph: the floor-dominated value, and growth beyond it.
    print("  Sanity check (y=5), mirroring 11.8.3.11's own numeric paragraph:")
    checkpoints = [1, 100, 34000, 10 ** 5, 10 ** 6, 10 ** 9]
    prev = None
    for s in checkpoints:
        val = p3_bound(s, 5)
        print(f"    s={s:>12,}: bound = {val:>12,.1f}")
        if prev is not None:
            check("F.monotone_or_floor", val >= prev - 1e-6, f"s={s} val={val} prev={prev}")
        prev = val
        n_checks += 1
    # crossover: solve log(b')+log(log3)+0.4 = 10*log3 for y=5, report the s
    # at which the floor term stops dominating (informational).
    target = 10 * log(3) - log(log(3)) - 0.4
    bprime_thresh = exp(target)
    s_thresh = (bprime_thresh - 1 / log(4)) * (2 * log(5))
    print(f"    floor/log(b') crossover (y=5): s ~ {s_thresh:,.0f}")
    print()
    return n_checks


# =============================================================================
# PART G: the p=2 control -- the SAME general formula, specialized at p=2,
# must reproduce 11.8.3.11's pinned constant and its three worked values.
# =============================================================================
def partG():
    print("=" * 70)
    print("PART G: p=2 control against stage1-synthesis.md 11.8.3.11")
    print("=" * 70)
    n_checks = 0
    pref2 = 24 * 2 * 1 / ((2 - 1) * log(2) ** 4) * 1 ** 4
    print(f"  prefactor 24*2*1/((2-1)*log(2)^4)*1^4 = {pref2:.6f}  "
          f"(11.8.3.11 quotes 208; ratio {pref2/208:.6f})")
    check("G.prefactor", abs(pref2 - 208) < 1.0, f"pref2={pref2}")

    def p2_bound(n, omega):
        logA1 = log(9)
        logA2 = log(omega)
        bprime = n / log(omega) + 1 / log(9)
        return baker_bound(2, 1, 1, logA1, logA2, bprime)

    targets = [(34000, 5, 73555), (10 ** 6, 5, 131500), (10 ** 9, 5, 302500)]
    for n, omega, published in targets:
        val = p2_bound(n, omega)
        rel_err = abs(val - published) / published
        print(f"  n={n:>12,} omega={omega}: bound={val:>14,.1f}  "
              f"published~{published:>10,}  rel.err={rel_err:.4%}")
        check("G.reproduce", rel_err < 0.005, f"n={n} omega={omega} val={val}")
        n_checks += 1
    print(f"  {n_checks} checks: the general-p formula, at p=2, reproduces "
          f"11.8.3.11's own pinned constant and worked values to <0.5%")
    print()
    return n_checks


if __name__ == "__main__":
    sys.stdout = Tee(OUT_PATH)
    rng = random.Random(20260908)
    total_checks = 0
    part0_canaries()
    total_checks += partA(rng)
    total_checks += partB(rng)
    total_checks += partC(rng)
    total_checks += partD()
    total_checks += partE()
    total_checks += partF()
    total_checks += partG()
    n_fail = len(FAILURES)
    print("=" * 70)
    print(f"TOTAL: {total_checks} checks, {n_fail} failures")
    print("RESULT:", "PASS - 0 failures" if n_fail == 0 else f"{n_fail} FAILURES")
    print("=" * 70)
    tee = sys.stdout
    tee.flush()
    sys.stdout = tee.stdout  # restore real stdout before closing the file
    tee.close()
    raise SystemExit(0 if n_fail == 0 else 1)
