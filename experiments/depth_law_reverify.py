"""Exhaustive re-verification of the Stage 3 laws on every valid state with
w < 3000, gcd(w, 6) = 1, 1 <= d < 64 -- all 63,000 of them, w = 1 included.

Supports:
  - stage3.md 11.8.6.3, "Numerical verification" (this run is the record there):
      Lemma 11.8.6.3.1 / Theorem 11.8.6.3.3  entry-depth law on the lifting branch
          m_+ = 3 - s + v_2(eps + delta_s)
      Corollary 11.8.6.3.4                  forced carry, v_2(eps) = s - 3 = v_2(delta_s)
      Definition 11.8.6.3.2                 v_2(delta_s) = s - 3
      Theorem 11.8.6.3.5                    entry-depth law off the lifting branch
          s = 1: m_+ = 1 + v_2(d - M(w));  s = 2: m_+ = v_2((d - 1) - M(w))
      Corollary 11.8.6.3.6                  d_+ = m_+ + a_+ with both terms from the laws
  - stage3.md 11.8.6.2, Proposition 11.8.6.2.1 (absorption a_+ = v_3(C), trichotomy)
  - stage1-synthesis.md 11.8.3 / stage2.md Proposition 11.8.5.6.2 (valuation law on
    the lifting classes: s = 3 + v_2(n - N(w)), s = 3 + v_2(n - N(3w)),
    and the unified s = 2 + v_2(d - M(w)))
  - stage1.md Proposition 11.8.1.3.1 (which (w mod 8, d mod 2) class has s = 1, 2, >= 3)
  - paper/collatz-reduced-v4.tex Remark C.6 (rem:verify1) and ledger row C-3.6

Fresh code: imports nothing from this repository. Every pass/fail decision is exact
integer arithmetic; there is no floating point anywhere.

The two sides never share a path. TRUTH: the next state is computed from the
definition of the reduced map (spine.md 5.6): x_exit = (3^d w - 1) / 2^s, then
R(x_exit) by stripping 2s and then 3s from x_exit + 1 by trial division.
PREDICTION: the laws, evaluated from (w, d) and the 2-adic anchors alone. The anchor
N(u) (9^N(u) = u^(-1), u = 1 mod 8) is computed mod 2^P by bit-by-bit lifting and
each result is certified by checking 9^N(u) * u = 1 mod 2^(P+3). M(w) = N(w^2) is
computed as its own discrete log, not as 2N(w) or 2N(3w) + 1 (those identities are
checked separately). Every anchor-side valuation is asserted to be far below the
precision P, so truncation can never decide a comparison.

w = 1 is reported separately: it is the trivial cycle's class (N(1) = M(1) = 0,
(1, 1) is the fixed point) and the Baker bound's exceptional case (stage1-synthesis.md
11.8.3.11), so the question asked of it is whether every law holds there as stated.

Run (one command; writes experiments/depth_law_reverify_output.txt and prints it):
    python experiments/depth_law_reverify.py
Exit status 0 iff every check passes and every negative control bites.
"""

import os
import sys
from collections import defaultdict
from math import gcd

W_MAX = 3000          # w < W_MAX
D_MAX = 64            # 1 <= d < D_MAX
P = 256               # anchor precision in bits (N known mod 2^P)
GUARD = 32            # anchor-side valuations must be < P - GUARD

OUT_LINES = []


def out(line=""):
    OUT_LINES.append(line)


# ---------------------------------------------------------------- arithmetic

def v2(x):
    if x == 0:
        raise ValueError("v2(0)")
    x = abs(x)
    return (x & -x).bit_length() - 1


def v3(x):
    if x == 0:
        raise ValueError("v3(0)")
    x = abs(x)
    k = 0
    while x % 3 == 0:
        x //= 3
        k += 1
    return k


def v2_mod(x):
    """v_2 of a 2-adic integer known mod 2^P; refuses to answer near the precision."""
    x %= (1 << P)
    if x == 0:
        raise AssertionError("anchor-side quantity is 0 mod 2^P")
    k = v2(x)
    if k >= P - GUARD:
        raise AssertionError("anchor-side valuation %d too close to precision %d" % (k, P))
    return k


ANCHOR_CACHE = {}
MOD_P3 = 1 << (P + 3)


def N(u):
    """N(u) mod 2^P with 9^N(u) = u^(-1) in Z_2, for u = 1 mod 8 (u may be negative)."""
    u %= MOD_P3
    if u % 8 != 1:
        raise ValueError("N needs u = 1 mod 8")
    if u in ANCHOR_CACHE:
        return ANCHOR_CACHE[u]
    # Lift t so that 9^t * u = 1 mod 2^(k+4), k = 0..P-1.  9^(2^k) = 1 + 2^(k+3) mod 2^(k+4).
    t = 0
    cur = u  # cur = 9^t * u mod 2^(P+3)
    for k in range(P):
        if (cur >> (k + 3)) & 1:
            t += 1 << k
            cur = (cur * pow(9, 1 << k, MOD_P3)) % MOD_P3
    if pow(9, t, MOD_P3) * u % MOD_P3 != 1:
        raise AssertionError("anchor certification failed for u = %d" % u)
    ANCHOR_CACHE[u] = t
    return t


def M(w):
    return N(w * w)


def h_trial(s):
    return v3((1 << s) - 1)


def h_formula(s):
    return 0 if s % 2 else 1 + v3(s)


# ---------------------------------------------------------------- truth

def direct_step(w, d):
    """The reduced map from its definition: x_exit, then R(x_exit) by trial division."""
    A = 3 ** d * w - 1
    s = v2(A)
    x_exit = A >> s
    y = x_exit + 1
    m = 0
    while y % 2 == 0:
        y //= 2
        m += 1
    a = 0
    while y % 3 == 0:
        y //= 3
        a += 1
    return dict(A=A, s=s, x_exit=x_exit, m=m, a=a, w_next=y, d_next=m + a)


# ---------------------------------------------------------------- bookkeeping

CHECKS = defaultdict(int)       # (class_label, law) -> count
FAILS = []                      # (w, d, law, detail)
W1_CHECKS = defaultdict(int)    # law -> count, at w = 1


def check(cls, w, d, law, ok, detail=""):
    CHECKS[(cls, law)] += 1
    if w == 1:
        W1_CHECKS[law] += 1
    if not ok:
        FAILS.append((w, d, law, detail))


def cls_label(w, d):
    return "w=%d mod 8, d %s" % (w % 8, "even" if d % 2 == 0 else "odd")


def expected_branch(w, d):
    """Proposition 11.8.1.3.1: 'L' (lifting, s >= 3), or the constant s = 1 / s = 2."""
    r, p = w % 8, d % 2
    if (r, p) in ((1, 0), (3, 1)):
        return "L"
    if (r, p) in ((1, 1), (5, 1), (7, 0), (3, 0)):
        return 1
    return 2  # (5, 0), (7, 1)


# ---------------------------------------------------------------- the sweep

def main():
    states = [(w, d) for w in range(1, W_MAX) if gcd(w, 6) == 1 for d in range(1, D_MAX)]
    n_w = len({w for w, _ in states})

    max_m = 0
    max_s = 0
    s_lift_seen = set()
    resonant = []
    resonant_extra = 0
    per_class_states = defaultdict(int)
    m_hist = defaultdict(int)
    w1_rows = []

    for (w, d) in states:
        cls = cls_label(w, d)
        per_class_states[cls] += 1
        T = direct_step(w, d)
        s, m, a = T["s"], T["m"], T["a"]
        max_m = max(max_m, m)
        max_s = max(max_s, s)
        m_hist[m] += 1

        # Next state is valid.
        check(cls, w, d, "next state valid", gcd(T["w_next"], 6) == 1 and T["d_next"] >= 1)

        # spine.md 5.6 identities through C.
        C = T["A"] + (1 << s)
        vC2, vC3 = v2(C), v3(C)
        check(cls, w, d, "C identities (spine 5.6)",
              vC2 - s == m and vC3 == a
              and C // (2 ** vC2 * 3 ** vC3) == T["w_next"] and vC2 - s + vC3 == T["d_next"])

        # Branch classification (Prop 11.8.1.3.1).
        br = expected_branch(w, d)
        if br == "L":
            check(cls, w, d, "branch class (11.8.1.3.1)", s >= 3, "s=%d" % s)
        else:
            check(cls, w, d, "branch class (11.8.1.3.1)", s == br, "s=%d" % s)

        # Absorption law, Prop 11.8.6.2.1, and the 3-gain trigger.
        h = h_trial(s)
        check(cls, w, d, "h(s) formula", h == h_formula(s))
        if h < d:
            a_pred = h
        elif h > d:
            a_pred = d
        else:
            beta = ((1 << s) - 1) // 3 ** d
            a_pred = d + v3(w + beta)
            resonant.append((w, d, s, a_pred))
            if a_pred != d:
                resonant_extra += 1
        check(cls, w, d, "absorption a_+ (11.8.6.2.1)", a_pred == a, "pred %d true %d" % (a_pred, a))
        check(cls, w, d, "3-gain iff s even", (a > 0) == (s % 2 == 0))

        # Entry-depth law and valuation law.
        Mw = M(w)
        if br == "L":
            s_lift_seen.add(s)
            if w % 8 == 1:
                n = d // 2
                eps = (n - N(w)) % (1 << P)
                # valuation law, even component
                check(cls, w, d, "valuation law s = 3 + v2(eps)", s == 3 + v2_mod(eps))
                check(cls, w, d, "M(w) = 2N(w)", Mw % (1 << P) == (2 * N(w)) % (1 << P))
            else:  # w = 3 mod 8, d odd
                n = (d - 1) // 2
                eps = (n - N(3 * w)) % (1 << P)
                check(cls, w, d, "valuation law s = 3 + v2(eps)", s == 3 + v2_mod(eps))
                check(cls, w, d, "M(w) = 2N(3w) + 1",
                      Mw % (1 << P) == (2 * N(3 * w) + 1) % (1 << P))
            check(cls, w, d, "unified law s = 2 + v2(d - M)", s == 2 + v2_mod(d - Mw))
            delta = N(1 - (1 << s))
            check(cls, w, d, "v2(delta_s) = s - 3", v2_mod(delta) == s - 3)
            check(cls, w, d, "forced carry v2(eps) = s - 3", v2_mod(eps) == s - 3)
            ve = v2_mod(eps + delta)
            check(cls, w, d, "forced carry v2(eps + delta) >= s - 2", ve >= s - 2)
            m_pred = 3 - s + ve
            check(cls, w, d, "entry depth m_+ (11.8.6.3.3)", m_pred == m,
                  "pred %d true %d" % (m_pred, m))
            # Lemma 11.8.6.3.1 directly on the even component, c = 1 - 2^s:
            if w % 8 == 1:
                check(cls, w, d, "target shift (11.8.6.3.1)",
                      v2(3 ** d * w - (1 - (1 << s))) == 3 + ve)
        elif br == 1:
            m_pred = 1 + v2_mod(d - Mw)
            check(cls, w, d, "entry depth m_+ (11.8.6.3.5, s=1)", m_pred == m,
                  "pred %d true %d" % (m_pred, m))
        else:
            m_pred = v2_mod((d - 1) - Mw)
            check(cls, w, d, "entry depth m_+ (11.8.6.3.5, s=2)", m_pred == m,
                  "pred %d true %d" % (m_pred, m))
        check(cls, w, d, "m_+ >= 1", m >= 1)

        # Corollary 11.8.6.3.6: d_+ from the two laws equals the true next depth.
        check(cls, w, d, "d_+ = m_+ + a_+ (11.8.6.3.6)", m_pred + a_pred == T["d_next"])

        if w == 1:
            w1_rows.append((d, s, m, a, T["w_next"], T["d_next"], br))

    # v2(delta_s) = s - 3 beyond the range met in the sweep.
    delta_range_fail = [s for s in range(3, 201) if v2_mod(N(1 - (1 << s))) != s - 3]

    # Worked cases quoted in stage3.md 11.8.6.3.
    worked = []
    T = direct_step(1, 4)
    eps = (2 - N(1)) % (1 << P)
    dl = N(1 - (1 << 4))
    worked.append(("(1,4): A=80 s=4 x_exit=5 m=1; eps=2, delta_4=2 mod 8, v2(eps+delta)=2",
                   T["A"] == 80 and T["s"] == 4 and T["x_exit"] == 5 and T["m"] == 1
                   and eps == 2 and dl % 8 == 2 and v2_mod(eps + dl) == 2))
    T = direct_step(17, 2)
    eps = (1 - N(17)) % (1 << P)
    dl = N(1 - (1 << 3))
    worked.append(("(17,2): A=152 s=3 x_exit=19 m=2; N(17)=6, eps=3, delta_3=1 mod 8, v2=2",
                   T["A"] == 152 and T["s"] == 3 and T["x_exit"] == 19 and T["m"] == 2
                   and N(17) % 8 == 6 and eps % 8 == 3 and dl % 8 == 1
                   and v2_mod(eps + dl) == 2))

    # Negative controls: each perturbed law must fail somewhere in the sweep.
    controls = []

    def bites(name, pred_fn, subset):
        # A perturbed law that is undefined at a state (argument 0) counts as wrong there.
        bad = 0
        for (w, d) in subset:
            try:
                ok = pred_fn(w, d) == direct_step(w, d)["m"]
            except AssertionError:
                ok = False
            bad += not ok
        controls.append((name, bad, len(subset)))

    lift = [(w, d) for (w, d) in states if expected_branch(w, d) == "L"]
    one = [(w, d) for (w, d) in states if expected_branch(w, d) == 1]
    two = [(w, d) for (w, d) in states if expected_branch(w, d) == 2]

    def lift_eps(w, d):
        if w % 8 == 1:
            return (d // 2 - N(w)) % (1 << P)
        return ((d - 1) // 2 - N(3 * w)) % (1 << P)

    def s_of(w, d):
        return v2(3 ** d * w - 1)

    bites("lifting law with delta_(s+1) for delta_s",
          lambda w, d: 3 - s_of(w, d) + v2_mod(lift_eps(w, d) + N(1 - (1 << (s_of(w, d) + 1)))),
          lift)
    bites("lifting law without the shift (m = 3 - s + v2(eps))",
          lambda w, d: 3 - s_of(w, d) + v2_mod(lift_eps(w, d)), lift)
    bites("s=1 law with d + 1 for d", lambda w, d: 1 + v2_mod(d + 1 - M(w)), one)
    bites("s=1 law with N(w^2)+1 for M(w)", lambda w, d: 1 + v2_mod(d - M(w) - 1), one)
    bites("s=2 law with d for d - 1", lambda w, d: v2_mod(d - M(w)), two)
    bites("s=2 law with M(3w) for M(w)", lambda w, d: v2_mod((d - 1) - M(3 * w)), two)
    # Subtle controls: a single high digit flipped, visible only on deep entries.
    bites("lifting law, digit s+1 of delta_s flipped (m >= 4 only)",
          lambda w, d: 3 - s_of(w, d) + v2_mod(lift_eps(w, d)
                                               + (N(1 - (1 << s_of(w, d))) ^ (1 << (s_of(w, d) + 1)))),
          lift)
    bites("s=1 law, digit 3 of M(w) flipped (m >= 4 only)",
          lambda w, d: 1 + v2_mod(d - (M(w) ^ 8)), one)

    # Absorption control: the resonant branch dropped (a_+ = min(d, h(s)) everywhere).
    bad_abs = 0
    for (w, d) in states:
        T = direct_step(w, d)
        bad_abs += min(d, h_trial(T["s"])) != T["a"]
    controls.append(("absorption with the resonant branch d = h(s) dropped", bad_abs, len(states)))

    # ------------------------------------------------------------ report
    total_checks = sum(CHECKS.values())
    out("depth_law_reverify.py -- Stage 3 laws on every valid state, w < %d, 1 <= d < %d"
        % (W_MAX, D_MAX))
    out("anchor precision 2^%d, certified; anchor-side valuations required < %d" % (P, P - GUARD))
    out()
    out("STATE COUNT")
    out("  values of w < %d with gcd(w, 6) = 1: %d" % (W_MAX, n_w))
    out("  depths 1 <= d < %d: %d" % (D_MAX, D_MAX - 1))
    out("  valid states checked: %d" % len(states))
    c_no1 = sum(1 for (w, d) in states if w != 1)
    c_lt2999 = sum(1 for (w, d) in states if w < 2999)
    out("  62,937 diagnosis: states with w > 1: %d; states with w < 2999 (largest w = 2999 dropped): %d"
        % (c_no1, c_lt2999))
    out("    63,000 - 62,937 = %d = one value of w times %d depths" % (len(states) - 62937, D_MAX - 1))
    out()
    out("PER RESIDUE-PARITY CLASS (w mod 8, d mod 2); branch per Prop 11.8.1.3.1")
    laws_order = sorted({law for (_, law) in CHECKS})
    for cls in sorted(per_class_states):
        w0, dpar = int(cls.split("=")[1].split()[0]), cls.endswith("even")
        br = expected_branch(w0, 0 if dpar else 1)
        tag = "lifting (s >= 3)" if br == "L" else "s = %d" % br
        n_checks = sum(v for (c, _), v in CHECKS.items() if c == cls)
        n_fail = sum(1 for (w, d, _, _) in FAILS if cls_label(w, d) == cls)
        out("  %-22s %-17s states %6d  checks %7d  failures %d"
            % (cls, tag, per_class_states[cls], n_checks, n_fail))
    out()
    out("PER LAW (all classes)")
    for law in laws_order:
        n = sum(v for (_, l2), v in CHECKS.items() if l2 == law)
        f = sum(1 for (_, _, l2, _) in FAILS if l2 == law)
        out("  %-42s checks %6d  failures %d" % (law, n, f))
    out()
    out("RANGES MET")
    out("  max m_+ = %d; max s = %d; lifting s values met: %d..%d"
        % (max_m, max_s, min(s_lift_seen), max(s_lift_seen)))
    out("  m_+ histogram: " + ", ".join("%d:%d" % (k, m_hist[k]) for k in sorted(m_hist)))
    out("  resonant states d = h(s) in the sweep: %d (with v3(w + beta) > 0: %d)"
        % (len(resonant), resonant_extra))
    out("  v2(delta_s) = s - 3 for 3 <= s <= 200: failures %d" % len(delta_range_fail))
    out()
    out("W = 1 SEPARATELY (N(1) = %d, M(1) = %d mod 2^%d)" % (N(1), M(1), P))
    out("  states: %d; checks: %d; failures: %d"
        % (len(w1_rows), sum(W1_CHECKS.values()), sum(1 for f in FAILS if f[0] == 1)))
    for law in sorted(W1_CHECKS):
        out("    %-42s %3d" % (law, W1_CHECKS[law]))
    out("  rows d: s m_+ a_+ -> (w_+, d_+)   [branch]")
    for (d, s, m, a, wn, dn, br) in w1_rows:
        out("    d=%2d: s=%2d m=%d a=%d -> (%d, %d)  [%s]"
            % (d, s, m, a, wn, dn, "lift" if br == "L" else "s=%d" % br))
    out()
    out("WORKED CASES (stage3.md 11.8.6.3)")
    for name, ok in worked:
        out("  %s: %s" % (name, "ok" if ok else "FAIL"))
    out()
    out("NEGATIVE CONTROLS (perturbed law; must disagree with the truth somewhere)")
    for name, bad, tot in controls:
        out("  %-48s wrong on %6d of %6d  %s" % (name, bad, tot, "bites" if bad else "DOES NOT BITE"))
    out()
    all_ok = (not FAILS and not delta_range_fail and all(ok for _, ok in worked)
              and all(bad > 0 for _, bad, _ in controls))
    out("TOTAL: %d checks on %d states, %d failures; controls %d/%d bite; verdict %s"
        % (total_checks, len(states), len(FAILS), sum(1 for c in controls if c[1]), len(controls),
           "PASS" if all_ok else "FAIL"))
    if FAILS:
        out()
        out("FIRST FAILURES")
        for f in FAILS[:20]:
            out("  %r" % (f,))

    text = "\n".join(OUT_LINES) + "\n"
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "depth_law_reverify_output.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    sys.stdout.write(text)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
