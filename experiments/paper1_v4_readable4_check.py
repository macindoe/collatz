#!/usr/bin/env python3
"""
paper1_v4_readable4_check.py -- scope-drift check of readability round 4 of paper 1 v4
(paper/collatz-reduced-v4.tex at 190b6af against round 3 at cbcc8b8).

Supports: briefs/paper1-v4-readable-4-check-findings.md (sections 1, 2 and 5).

Written for this check from the paper's text alone (main text; Definitions B.1, C.1; Theorem D.5's
Rhin display; the definition of p1(X0) in the proof of Theorem D.6(iii)).  It imports nothing from
the repository and reuses no code from experiments/.  Exact integers and Fractions for every
integer decision; mpmath at 400 digits for real constants, gamma and p1(X0).  The TeX and the
claims ledger are read from git at pinned commits, so the result does not depend on the checkout.

Parts:
  A. The round-3 check's 12 fixes (904dcc6 findings section 4) and its navigation notes: each new
     wording present in the 190b6af main text, each old wording gone.
  B. Unchanged text: Version note + Author's note; everything from \\appendix to the Symbol index
     (Technical summary, Appendices A-H, so B-E in particular) identical character for character
     between cbcc8b8 and 190b6af; Appendix I differs by exactly the word after -> before.
  C. Worked numbers new in round 4 (sections 1-6), recomputed.
  D. Witnesses for the findings (section 4 of the findings).
  E. Negative controls: each must be rejected by the same code.

Scope (README stopping rules): no cycle search, no divisibility test; size-only arithmetic on
the paper's own printed examples.

Reproduce (one command; deterministic; about a minute):

    python experiments/paper1_v4_readable4_check.py

It writes experiments/paper1_v4_readable4_check_output.txt (UTF-8, no BOM) and exits 0 iff every
check passes and every control is rejected.
"""

import os
import re
import subprocess
import sys
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 400

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "paper1_v4_readable4_check_output.txt")

NEW = "190b6af"   # round 4 head
OLD = "cbcc8b8"   # round 3 head
TEX = "paper/collatz-reduced-v4.tex"
LEDGER = "paper/collatz-reduced-v4-claims.md"

lines_out = []
n_pass = 0
n_fail = 0
n_ctrl_ok = 0
n_ctrl_bad = 0


def say(s=""):
    lines_out.append(s)
    print(s.encode("ascii", "replace").decode("ascii"))


def check(label, ok, detail=""):
    global n_pass, n_fail
    if ok:
        n_pass += 1
    else:
        n_fail += 1
    say(("  PASS  " if ok else "  FAIL  ") + label + (("   [" + detail + "]") if detail else ""))


def control(label, rejected, detail=""):
    """A negative control: `rejected` must be True (the wrong claim is caught)."""
    global n_ctrl_ok, n_ctrl_bad
    if rejected:
        n_ctrl_ok += 1
    else:
        n_ctrl_bad += 1
    say(("  CTRL rejected  " if rejected else "  CTRL NOT REJECTED  ") + label
        + (("   [" + detail + "]") if detail else ""))


def git_show(rev, path):
    r = subprocess.run(["git", "show", rev + ":" + path], cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("git show failed for %s:%s" % (rev, path))
    return r.stdout.decode("utf-8")


def norm(s):
    return re.sub(r"\s+", " ", s)


def between(text, start, end):
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


# ---------------------------------------------------------------- arithmetic helpers

def v2(n):
    n = abs(n)
    if n == 0:
        raise ValueError("v2(0)")
    return (n & -n).bit_length() - 1


def v3(n):
    n = abs(n)
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def T(x):
    """odd-to-odd map; returns (next odd, number of halvings)."""
    y = 3 * x + 1
    h = v2(y)
    return y >> h, h


def state(x):
    m = v2(x + 1)
    u = (x + 1) >> m
    a = v3(u)
    w = u // 3 ** a
    return w, m + a, m, a


def F(w, d):
    A = 3 ** d * w - 1
    s = v2(A)
    xe = A >> s
    C = A + (1 << s)
    sig = v2(C)
    ap = v3(C)
    wp = C // ((1 << sig) * 3 ** ap)
    mp_ = sig - s
    return dict(s=s, exit=xe, C=C, sigma=sig, a=ap, w=wp, m=mp_, d=mp_ + ap)


def valid(w, d):
    return w > 0 and w % 2 == 1 and w % 3 != 0 and d >= 1


def anchor_mod(w, K):
    """M(w) = N(w^2) mod 2^K, N(u) the t with 9^t = u^{-1} in Z_2 (Definition C.1)."""
    mod = 1 << (K + 3)
    u = (w * w) % mod
    target = pow(u, -1, mod)
    t = 0
    for i in range(K):
        mi = 1 << (i + 4)
        if pow(9, t, mi) != target % mi:
            t += 1 << i
    assert pow(9, t, mod) == target
    return t


L = mp.log(3) / mp.log(2)


def phi(x):
    return -mp.log(1 - mp.power(2, -x)) / mp.log(2)


def convergents(x, count):
    P, Q = [], []
    pm2, pm1 = 0, 1
    qm2, qm1 = 1, 0
    y = x
    for _ in range(count):
        a = int(mp.floor(y))
        p = a * pm1 + pm2
        q = a * qm1 + qm2
        P.append(p)
        Q.append(q)
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
        frac = y - a
        if frac == 0:
            break
        y = 1 / frac
    return P, Q


CP, CQ = convergents(L, 160)
THETA = [abs(CQ[j] * L - CP[j]) for j in range(len(CQ))]
LAM0 = L / (L - 1) + mp.power(2, -20)


LP = [mp.power(L, p) for p in range(0, 600)]
_P1 = {}


def p1_of(X0):
    """p1(X0) as defined in the proof of Theorem D.6(iii) (ledger C-4.6.pf.iii)."""
    X0 = mp.mpf(X0)
    key = mp.nstr(X0, 120)
    if key not in _P1:
        _P1[key] = _p1_raw(X0)
    return _P1[key]


def _p1_raw(X0):
    g = 1 + max(mp.log(X0 + 1) / mp.log(2), LAM0)
    Delta = phi(g) - phi(g + 1)
    k = None
    for kk in range(1, len(CQ)):
        if THETA[kk - 1] <= Delta:
            k = kk
            break
    Nstar = CQ[k] + CQ[k - 1]
    p = 1
    while True:
        lhs = (LP[p] - 1) / (2 * (L - 1))
        if lhs >= max(Nstar, 3 * p + 40):
            return p, g, Nstar
        p += 1


def gamma_n(n):
    """gamma at K = ceil(nL): gamma = phi(K - nL)."""
    K = int(mp.ceil(n * L))
    return phi(K - n * L), K


# =============================================================================================
def main():
    tex_new = git_show(NEW, TEX)
    tex_old = git_show(OLD, TEX)
    ledger = git_show(NEW, LEDGER)
    ledger_old = git_show(OLD, LEDGER)

    main_new = norm(between(tex_new, r"\begin{abstract}", r"\appendix"))
    main_old = norm(between(tex_old, r"\begin{abstract}", r"\appendix"))

    say("paper1_v4_readable4_check.py -- round 4 (%s) against round 3 (%s)" % (NEW, OLD))
    say("")

    # ------------------------------------------------------------------ A
    say("A. The round-3 check's 12 fixes and navigation notes")
    fixes = [
        ("1 abstract: no cycles other than 1, 4, 2, 1 (one, two or three blocks)",
         ["there are no cycles other than $1, 4, 2, 1$ made of one, two or three blocks"],
         ["there are no cycles made of one"]),
        ("1/7 section 1 (v): no cycles other than 1, 4, 2, 1",
         ["no cycles other than $1, 4, 2, 1$ with one, two or three blocks"],
         ["no cycles of one, two or three blocks"]),
        ("2 abstract: odd steps (multiplications by 3)",
         ["on how many odd steps (multiplications by $3$) a cycle with a given number of blocks can have"],
         ["how many rising steps"]),
        ("3 abstract: measure of closeness exceeds the bound's own exponent",
         ["with their measure of closeness exceeding the classical bound's own exponent by at most a fixed amount"],
         ["own requirement by at most"]),
        ("4 abstract: of every length at once",
         ["the conclusion that ruling out cycles of every length at once needs divisibility and not size alone"],
         ["ruling out cycles needs divisibility"]),
        ("5 abstract: record's length a fixed multiple of the bit length",
         ["and of the record's length, itself a fixed multiple of the start's number of binary digits"],
         []),
        ("6 abstract: shows the fair-coin conjecture holds outright (proof assembled in the record)",
         ["shows that the fair-coin conjecture holds outright while the orbit is still within the start's own supply of binary digits (the proof is assembled in the project record)"],
         ["proves the conjecture outright"]),
        ("8 section 4: the three outcomes run along real orbits, not 'so were'",
         ["(Remark~\\ref{rem:verify1}). The three outcomes were run along real orbits"],
         ["so were the three outcomes"]),
        ("9 section 5: multiplications by 3 (the larger n)",
         ["the more multiplications by $3$ a cycle has (the larger $n$), the closer $2^K$ must be to $3^n$"],
         ["the more rising steps"]),
        ("10 section 5: weaker at seven than at three; exponential weakening is part (i)",
         ["at seven blocks the requirement must be weaker than at three. (That it must weaken exponentially as the number of blocks grows is part~(i) below.)"],
         ["and the requirement must weaken as the number of blocks grows"]),
        ("11 section 5: every one tested fails divisibility",
         ["The staircases pass every size condition, and every one tested fails the divisibility conditions."],
         ["condition yet fail the divisibility"]),
        ("12 section 4: no cost claim",
         ["The law describes a step; it is not offered as a faster way to compute one."],
         ["shortcut", "costs about as much", "williams-letter-findings", "briefs/"]),
        ("nav: symbols page names p-adic and m-cycle",
         ["(Two letters also appear in fixed phrases with their usual meanings: `$p$-adic', and Simons and de~Weger's `$m$-cycle', which this paper calls a $p$-cycle.)"],
         []),
        ("nav: running example Sections 2-4, blocks return in 6",
         ["runs through Sections~\\ref{sec:block}--\\ref{sec:anchor}, and its blocks return in Section~\\ref{sec:aeh}"],
         ["runs through Sections~\\ref{sec:block}--\\ref{sec:cycles}"]),
        ("nav: section 8 cascade gloss",
         ["elsewhere in this paper `cascade' means only the block's final burst of halvings"],
         []),
        ("nav (optional): H25 proportion of odd steps",
         ["for the proportion of its steps that are odd"],
         []),
    ]
    for label, must, mustnot in fixes:
        ok = all(norm(s) in main_new for s in must) and not any(norm(s) in main_new for s in mustnot)
        check(label, ok)
    appI_new = norm(tex_new[tex_new.index(r"\section{Symbol index}"):])
    check("nav: Appendix I says 'before Section 1'",
          "Main-text symbols are also in ``Symbols at a glance'', before Section~\\ref{sec:intro}." in appI_new)
    # no out-of-paper file pointers left in the main text body (sections 1-8)
    body = norm(between(tex_new, r"\section{What this paper is about}", r"\appendix"))
    check("no aeh.md / briefs/ pointers left in sections 1-8",
          ".md" not in body and "briefs/" not in body)
    check("ledger unchanged between %s and %s" % (OLD, NEW), ledger == ledger_old)
    say("")

    # ------------------------------------------------------------------ B
    say("B. Unchanged text")
    pre_new = between(tex_new, r"\subsection*{Version note}", r"\section*{Symbols at a glance}")
    pre_old = between(tex_old, r"\subsection*{Version note}", r"\section*{Symbols at a glance}")
    check("Version note + Author's note identical", pre_new == pre_old)
    app_new = between(tex_new, r"\appendix", r"\section{Symbol index}")
    app_old = between(tex_old, r"\appendix", r"\section{Symbol index}")
    check("\\appendix .. Symbol index (Technical summary, App A-H) identical",
          app_new == app_old, "%d chars" % len(app_new))
    be_new = between(tex_new, r"\section{The reduced system", r"\section{Related work in detail}")
    be_old = between(tex_old, r"\section{The reduced system", r"\section{Related work in detail}")
    check("Appendices B-E identical", be_new == be_old, "%d chars" % len(be_new))
    ai_new = tex_new[tex_new.index(r"\section{Symbol index}"):].split()
    ai_old = tex_old[tex_old.index(r"\section{Symbol index}"):].split()
    diffs = [(a, b) for a, b in zip(ai_old, ai_new) if a != b]
    check("Appendix I: exactly one token changed, after -> before",
          len(ai_new) == len(ai_old) and diffs == [("after", "before")], str(diffs))
    say("")

    # ------------------------------------------------------------------ C
    say("C. Worked numbers new in round 4")

    # C1 section 2: rising step halves once and rises
    ok = True
    for x in range(3, 200001, 4):
        y = 3 * x + 1
        if v2(y) != 1 or y // 2 <= x:
            ok = False
            break
    check("sec 2: x = 3 mod 4 (x < 200001): 3x+1 halves exactly once and (3x+1)/2 > x", ok)
    check("sec 2: 3*8 = 24, 22 = 24-2 -> 11", 3 * 8 == 24 and 22 == 24 - 2 and T(7) == (11, 1))

    # C2 section 3: x_{m-1} + 1 = 2 * w * 3^(d-1)
    ok = True
    for x in range(1, 100001, 2):
        w, d, m, a = state(x)
        y = x
        for _ in range(m - 1):
            y, h = T(y)
            if h != 1:
                ok = False
        if y + 1 != 2 * w * 3 ** (d - 1):
            ok = False
            break
    check("sec 3: after m-1 rising steps, x+1 = 2*w*3^(d-1) (odd x < 100001)", ok)
    w, d, m, a = state(17)
    check("sec 3: 17 + 1 = 18 = 2 * 1 * 3^2 (d - 1 = 2 threes)", 18 == 2 * 1 * 3 ** 2 and (w, d) == (1, 3))
    # 'Put together': reaching 1 <=> states reach (1,1); fibre of (1,1) is {1}
    fib11 = [2 ** (1 - aa) * 3 ** aa * 1 - 1 for aa in range(0, 1)]
    ok = fib11 == [1]
    for x in range(1, 20001, 2):
        y = x
        st = state(y)[:2]
        for _ in range(2000):
            if st == (1, 1):
                break
            y = F(*st)["exit"]
            st = state(y)[:2]
        if st != (1, 1) or y != 1:
            ok = False
            break
    check("sec 3: odd x < 20001: state orbit reaches (1,1) and the number there is 1; fibre(1,1) = {1}", ok)

    # C3 section 4: the eight-kind table
    table = {(1, 0): "L", (3, 0): 1, (5, 0): 2, (7, 0): 1,
             (1, 1): 1, (3, 1): "L", (5, 1): 1, (7, 1): 2}
    tex_table_even = "$d$ even & lifting & $s = 1$ & $s = 2$ & $s = 1$"
    tex_table_odd = "$d$ odd & $s = 1$ & lifting & $s = 1$ & $s = 2$"
    check("sec 4: printed table rows are those coded here",
          tex_table_even in tex_new and tex_table_odd in tex_new)
    ok = True
    cnt = 0
    for w in range(1, 3001, 2):
        if w % 3 == 0:
            continue
        for d in range(1, 41):
            s = F(w, d)["s"]
            kind = table[(w % 8, d % 2)]
            cnt += 1
            if kind == "L":
                if s < 3 or (3 ** d * w) % 8 != 1:
                    ok = False
            elif s != kind:
                ok = False
    check("sec 4: eight-kind table and s >= 3 on lifting kinds", ok, "%d states, w < 3001, d <= 40" % cnt)
    # why the table holds: powers of 3 mod 8, remainders
    check("sec 4: powers of 3 mod 8 are 3,1,3,1,...", [pow(3, k, 8) for k in range(1, 9)] == [3, 1] * 4)
    ok = True
    for w in (1, 3, 5, 7):
        for par in (0, 1):
            r = (pow(3, 2 + par, 8) * w) % 8
            kind = table[(w, par)]
            if kind == "L":
                ok &= (r == 1)
            else:
                ok &= r in (3, 5, 7) and ((r - 1) % 8) in (2, 4, 6) and kind == (v2(r - 1) if r != 1 else None)
    check("sec 4: kind fixes 3^d w mod 8; lifting <-> 1; else 3,5,7 -> remainder 2,4,6 -> s = 1 or 2", ok)
    check("sec 4: (1,3): 27 - 1 = 26 = 2*13, s = 1", 27 - 1 == 26 == 2 * 13 and F(1, 3)["s"] == 1)
    # anchor rule: s = 2 + (number of low binary digits on which d agrees with M(w))
    ok = True
    cnt = 0
    for w in range(1, 3001, 2):
        if w % 3 == 0:
            continue
        M = anchor_mod(w, 64)
        for d in range(1, 41):
            if (3 ** d * w) % 8 != 1:
                continue
            agree = 0
            while agree < 64 and ((d >> agree) & 1) == ((M >> agree) & 1):
                agree += 1
            cnt += 1
            if F(w, d)["s"] != 2 + agree or agree != v2((d - M) % (1 << 64)):
                ok = False
    check("sec 4: lifting kinds: s = 2 + (low digits on which d agrees with the anchor)", ok,
          "%d lifting states, w < 3001, d <= 40, anchor mod 2^64" % cnt)
    check("sec 4: the anchor of w = 1 is all zeros (mod 2^64)", anchor_mod(1, 64) == 0)
    # the omega = 1 table
    rows = [(2, "10", 1, 3), (4, "100", 2, 4), (6, "110", 1, 3), (8, "1000", 3, 5)]
    ok = True
    for d, b, tz, s in rows:
        ok &= bin(d)[2:] == b and v2(d) == tz and F(1, d)["s"] == s and 2 + tz == s
        ok &= (3 ** d) % 8 == 1
        ok &= ("$%d$ & \\texttt{%s} & $%d$ & $%d$" % (d, b, tz, s)) in tex_new
    check("sec 4: omega = 1 table d = 2,4,6,8 -> binary, trailing zeros 1,2,1,3 -> s = 3,4,3,5 (printed)", ok)
    check("sec 4: 3^d - 1 = 8, 80, 728, 6560 = 8*1, 16*5, 8*91, 32*205",
          [3 ** d - 1 for d in (2, 4, 6, 8)] == [8, 80, 728, 6560] == [8 * 1, 16 * 5, 8 * 91, 32 * 205])
    y = 3 * 5 + 1
    check("sec 4: (1,2): 3*5+1 = 16 halves four times = 1 + s, s = 3",
          y == 16 and v2(y) == 4 and state(5)[:2] == (1, 2) and F(1, 2)["s"] == 3 and 1 + 3 == 4)
    check("sec 4: (1,3),(1,1) kind (1,odd) s = 1; (7,1) kind (7,odd) s = 2",
          F(1, 3)["s"] == 1 and F(1, 1)["s"] == 1 and F(7, 1)["s"] == 2)
    # factor of 3
    ok = True
    for w in range(1, 601, 2):
        if w % 3 == 0:
            continue
        for d in range(1, 21):
            f = F(w, d)
            s = f["s"]
            ok &= (f["exit"] + 1) * 2 ** s == 3 ** d * w + 2 ** s - 1 == f["C"]
            ok &= v3(f["C"]) == f["a"]
            ok &= (f["a"] > 0) == (s % 2 == 0)
    check("sec 4: (exit+1)*2^s = 3^d w + 2^s - 1, its threes = a+, gain iff s even (w < 601, d <= 20)", ok)
    check("sec 4: powers of 2 mod 3 are 2,1,2,1,...", [pow(2, k, 3) for k in range(1, 9)] == [2, 1] * 4)
    f71 = F(7, 1)
    check("sec 4: (7,1): s = 2, exit 5, (5+1)*4 = 24 = 21 + 3, next state (1,2), a = 1",
          f71["s"] == 2 and f71["exit"] == 5 and (5 + 1) * 4 == 24 == 21 + 3 and (f71["w"], f71["d"]) == (1, 2)
          and f71["a"] == 1 and state(13)[:2] == (7, 1) and T(13) == (5, 3))
    check("sec 4: s = 1 and s = 3 blocks gain none", F(1, 3)["a"] == 0 and F(1, 2)["a"] == 0)
    check("sec 4: next depth from (7,1): 5+1 = 6 = 2*3, entry depth 1, absorption 1, next depth 2",
          f71["m"] == 1 and f71["a"] == 1 and f71["d"] == 2 and v2(6) == 1 and v3(6) == 1)
    ok = True
    for w in range(1, 601, 2):
        if w % 3:
            for d in range(1, 21):
                ok &= F(w, d)["m"] >= 1
    check("sec 4: next entry depth never below 1 (w < 601, d <= 20)", ok)
    # digit budget: window depth + 6 per step under the model
    Es = sum(Fraction(j, 2 ** j) for j in range(1, 200))
    check("sec 4: under the model E[s] + E[m+] + 2 = 6 (so 'window depth plus 6')",
          abs(2 * Es + 2 - 6) < Fraction(1, 10 ** 50))
    # check counts quoted from the record are the ledger's
    for num in ("8{,}000", "62{,}937", "327{,}980", "21{,}296"):
        plain = num.replace("{,}", ",")
        check("sec 4: '%s' in main text and in ledger C-3.6/C-3.10" % plain,
              num in main_new and plain in ledger)
    check("sec 4: 'w below 3000 and d below 64' matches the ledger's w < 3000, d < 64",
          "$\\w$ below $3000$ and $d$ below $64$" in main_new and "`ω < 3000`, `d < 64`" in ledger)

    # C4 section 5
    check("sec 5: 0.1157 * 94 - 2 = 8.8758 (printed 'about 8.9')",
          Fraction(1157, 10000) * 94 - 2 == Fraction(88758, 10000))
    # Rhin step (b): from Lambda > exp(-13.3(0.46057 + ln n)), gamma < 1 + 13.3(0.46057 + ln n)/ln 2
    ok = True
    worst = mp.mpf(0)
    with mp.workdps(60):
        Lw = mp.log(3) / mp.log(2)
        for n in range(1, 20001):
            K = int(mp.ceil(n * Lw))
            g = phi(K - n * Lw)
            lam = -mp.log(1 - mp.power(2, -g))
            B = 1 + 13.3 * (0.46057 + mp.log(n)) / mp.log(2)
            ok &= (g < B) and (g < 1 or lam <= 2 * mp.power(2, -g))
            worst = max(worst, g / B)
    for j in range(1, 70):
        for n in (CQ[j], CQ[j] + CQ[j - 1]):
            if n < 1:
                continue
            g, K = gamma_n(n)
            B = 1 + 13.3 * (0.46057 + mp.log(n)) / mp.log(2)
            ok &= g < B
            worst = max(worst, g / B)
    check("sec 5 (b): gamma < 1 + (13.3/ln 2)(0.46057 + ln n) at every n <= 20000 and at the "
          "convergent denominators up to Q_69 (Rhin in gamma terms: a fixed multiple of log n)", ok,
          "max gamma/bound = %s" % mp.nstr(worst, 6))
    # (c): n0(p) of order p L^p
    ratios = []
    for p in range(2, 61):
        kap = (L - 1) / (mp.power(L, p) - 1)
        f = lambda n: kap * n - mp.log(p) / mp.log(2) - (p + 13.3 * (0.46057 + mp.log(n))) / mp.log(2)
        lo, hi = mp.mpf(1), mp.mpf(10) ** 40
        for _ in range(400):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                hi = mid
            else:
                lo = mid
        ratios.append(hi / (p * mp.power(L, p)))
    check("sec 5 (c): n0(p)/(p L^p) bounded over p = 2..60 and non-increasing (order p times 1.585^p)",
          max(ratios) < 64 and all(ratios[i] >= ratios[i + 1] for i in range(len(ratios) - 1)),
          "from %s at p = 2 down to %s at p = 60" % (mp.nstr(ratios[0], 5), mp.nstr(ratios[-1], 5)))
    # p1 samples and monotonicity
    vals = {}
    for X0 in (1, 2, 10, 16):
        vals[X0] = p1_of(X0)[0]
    check("sec 5: p1 = 10 at X0 = 1, 2, 10, 16", all(v == 10 for v in vals.values()), str(vals))
    v22 = [p1_of(mp.power(2, e))[0] for e in (8, 9, 10, mp.mpf(10.5), 11, 12)]
    check("sec 5: p1 = 22 for X0 = 2^8 .. 2^12 (sampled 8, 9, 10, 10.5, 11, 12)", all(v == 22 for v in v22), str(v22))
    p20 = p1_of(mp.power(2, 20))[0]
    p_sdw = p1_of(5 * mp.power(2, 60))[0]
    p71 = p1_of(mp.power(2, 71))[0]
    p200 = p1_of(mp.power(2, 200))[0]
    check("sec 5: p1 = 36 at 2^20, 98 at 5*2^60, 110 at 2^71, 309 at 2^200",
          (p20, p_sdw, p71, p200) == (36, 98, 110, 309), str((p20, p_sdw, p71, p200)))
    grid = [mp.power(2, mp.mpf(e) / 4) for e in range(0, 801)] + [5 * mp.power(2, 60)]
    grid.sort()
    seq = [p1_of(X)[0] for X in grid]
    mono = all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1))
    check("sec 5: p1 never decreases (X0 = 2^(e/4), e = 0..800, plus 5*2^60)", mono,
          "%d points, p1 from %d to %d" % (len(seq), seq[0], seq[-1]))
    deltas = []
    for j in range(0, 201):
        X = mp.power(2, j)
        deltas.append((p1_of(X)[0] - mp.log(X) / mp.log(L), j))
    check("sec 5: p1 computed at every 2^j, j <= 200; p1 - log_L X0 in the ledger's [2.783, 10.630]",
          min(deltas)[0] >= 2.783 and max(deltas)[0] <= 10.630,
          "min %s at j=%d, max %s at j=%d" % (mp.nstr(min(deltas)[0], 8), min(deltas)[1],
                                              mp.nstr(max(deltas)[0], 8), max(deltas)[1]))
    xo = git_show(NEW, "experiments/x0_threshold_independent_check_output.txt")
    check("sec 5: the record's committed output covers every j <= 200",
          "X0 = 2^j, j = 0..200" in xo)
    check("sec 5: 2^-(lambda0 + 1.5) = 0.0540... >= 0.054 (unchanged constant, recomputed)",
          mp.power(2, -(LAM0 + 1.5)) >= mp.mpf("0.054"), mp.nstr(mp.power(2, -(LAM0 + 1.5)), 8))

    # C5 section 6: the base-case example
    def letters(x, maxS):
        out = []
        S = 0
        y = x
        while S <= maxS:
            w, d, m, a = state(y)
            s = v2(3 ** d * w - 1)
            out.append((m, s))
            S += m + s
            y = (3 ** d * w - 1) >> s
        return out

    def words_upto(S):
        res = []

        def rec(prefix, tot):
            if prefix:
                res.append(tuple(prefix))
            for m in range(1, S + 1):
                for s in range(1, S + 1):
                    if tot + m + s <= S:
                        rec(prefix + [(m, s)], tot + m + s)
        rec([], 0)
        return res

    W9 = words_upto(9)
    ok = True
    starts = [0, 1, 777, 12345, 10 ** 6 + 7, 2 ** 40 + 3, 3 ** 30]
    for st in starts:
        odds = [x for x in range(st, st + 1024) if x % 2 == 1 and x > 0]
        if len(odds) != 512:
            odds = [x for x in range(st + 1, st + 1025) if x % 2 == 1]
        seqs = [letters(x, 9) for x in odds]
        for wd in W9:
            S = sum(m + s for m, s in wd)
            c = sum(1 for sq in seqs if tuple(sq[:len(wd)]) == wd)
            if Fraction(c, 512) != Fraction(1, 2 ** S):
                ok = False
    check("sec 6: in 7 runs of 1024 consecutive integers, every pattern with fewer than ten halvings "
          "(start's block included) occurs exactly its fair-coin share 2^-S of the 512 odd numbers", ok,
          "%d patterns" % len(W9))
    ok = True
    classes = {}
    for x in range(1, 1 << 15, 2):
        sq = letters(x, 9)
        for ln in range(1, len(sq) + 1):
            wd = tuple(sq[:ln])
            S = sum(m + s for m, s in wd)
            if S > 9:
                break
            classes.setdefault(wd, set()).add(x % (1 << (S + 1)))
    ok = all(len(v) == 1 for v in classes.values()) and len(classes) == len(W9)
    ok &= all((1 << (sum(m + s for m, s in wd) + 1)) <= 1024 for wd in classes)
    check("sec 6: each such pattern is one residue class mod 2^(S+1), a power of 2 at most 2^10 "
          "(odd x < 2^15)", ok)
    lets = [(state(y)[2], F(*state(y)[:2])["s"]) for y in (7, 13, 5, 1)]
    check("sec 6: the running example's letters (3,1),(1,2),(1,3),(1,1); blocks of 7 return",
          lets == [(3, 1), (1, 2), (1, 3), (1, 1)])
    say("")

    # ------------------------------------------------------------------ D witnesses
    say("D. Witnesses for the findings")
    vs = sum(1 for w in range(1, 3000) for d in range(1, 64) if valid(w, d))
    vs1 = sum(1 for w in range(2, 3000) for d in range(1, 64) if valid(w, d))
    check("witness (finding 4.5): valid states with w < 3000, 1 <= d < 64 number %d, not 62,937; "
          "excluding w = 1 gives %d" % (vs, vs1), vs == 63000 and vs1 == 62937)
    ok = True
    worst = None
    for j in range(0, 201):
        X = mp.power(2, j)
        p, g, _ = p1_of(X)
        # kappa_p n <= gamma - lambda0 <= g + 1 - lambda0 at every p >= p1
        margin = p - (g + 1 - LAM0)
        ok &= margin > 0
        worst = margin if worst is None else min(worst, margin)
    check("witness (finding 4.3): at every X0 = 2^j, j <= 200, p1 > g + 1 - lambda0 >= kappa_p n, "
          "so 2^p exceeds 2^(kappa_p n) (the ledger's comparand)", ok, "min margin %s" % mp.nstr(worst, 6))
    cal = norm(between(tex_new, r"\paragraph{How it was tested.}", r"\section{What remains open}"))
    check("witness (finding 4.4): section 6 adds 'which the sharper control set aside'; "
          "Appendix E and the ledger do not",
          "which the sharper control set aside" in cal and "set aside" not in norm(app_new)
          and "set aside" not in ledger)
    aeh = git_show(NEW, "aeh.md")
    check("witness (finding 4.4): aeh.md names the controls 'larger starts, per-orbit statistics, "
          "bulk/bottom separation'", "(larger starts, per-orbit statistics, bulk/bottom separation)" in aeh)
    s6 = norm(between(tex_new, r"\paragraph{What it would not give.}", r"\paragraph{How it was tested.}"))
    check("witness (finding 4.2): section 6 'older and broader' now attaches to 'the digits of the anchors'",
          "a question about the digits of the anchors of Section~\\ref{sec:anchor}" in s6
          and "2$-adic" not in s6)
    check("witness (finding 4.1): not-claimed bullet says 'weaker than'; ledger says 'not a null set of orbits'",
          "that is weaker than saying that almost no orbits misbehave" in main_new
          and "not a null set of orbits" in ledger and "weaker than" not in ledger)
    check("witness (finding 4.3): Lemma 4 clause has no comparand in the main text; ledger has 2^(kappa_p n)",
          "whose extra term, $2$ to the power $p$, is larger throughout this range." in main_new
          and "exceeds `2^{κ_p n}` throughout this range" in ledger)
    say("")

    # ------------------------------------------------------------------ E controls
    say("E. Negative controls")
    control("omega = 1 table with d = 6 -> s = 4", F(1, 6)["s"] != 4)
    control("table cell (5, even) -> s = 1", F(5, 2)["s"] != 1)
    control("exit of 13 is 7 / (5+1)*4 = 25", T(13)[0] != 7 and (5 + 1) * 4 != 25)
    control("p1(2^20) = 35", p1_of(mp.power(2, 20))[0] != 35)
    control("a decreasing sequence passes the monotonicity test",
            not all(a <= b for a, b in zip([10, 22, 21], [22, 21])))
    g41, _ = gamma_n(41)
    control("gamma < 1 + ln n (multiplier 1) at n = 41", not (g41 < 1 + mp.log(41)),
            "gamma(41) = %s" % mp.nstr(g41, 6))
    r2 = []
    for p in (10, 30, 60):
        kap = (L - 1) / (mp.power(L, p) - 1)
        f = lambda n: kap * n - mp.log(p) / mp.log(2) - (p + 13.3 * (0.46057 + mp.log(n))) / mp.log(2)
        lo, hi = mp.mpf(1), mp.mpf(10) ** 40
        for _ in range(400):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                hi = mid
            else:
                lo = mid
        r2.append(hi / mp.power(L, p))
    control("n0(p) of order 1.585^p alone (n0/L^p bounded by its p = 10 value)", r2[2] > 2 * r2[0],
            "n0/L^p = %s" % [mp.nstr(r, 4) for r in r2])
    # exactness fails at S = 10 in some window of 1024
    W10 = [wd for wd in words_upto(10) if sum(m + s for m, s in wd) == 10]
    bad = False
    for st in (1, 777, 12345):
        odds = [x for x in range(st, st + 1024) if x % 2 == 1]
        seqs = [letters(x, 10) for x in odds]
        for wd in W10:
            c = sum(1 for sq in seqs if tuple(sq[:len(wd)]) == wd)
            if Fraction(c, len(odds)) != Fraction(1, 2 ** 10):
                bad = True
                break
        if bad:
            break
    control("exact fair-coin share at S = 10 in a run of 1024", bad)
    control("62,937 is the full count of valid states w < 3000, d < 64", vs != 62937)
    control("p1 > log2 X0 + 200 throughout (a comparand that fails)",
            not all(p1_of(mp.power(2, j))[0] > j + 200 for j in (0, 100, 200)))
    control("Appendices B-E unchanged detects a one-character edit",
            be_new.replace("Proposition", "Propositon", 1) != be_old)
    say("")

    say("Totals: %d checks, %d failures; %d controls, %d rejected, %d not rejected."
        % (n_pass + n_fail, n_fail, n_ctrl_ok + n_ctrl_bad, n_ctrl_ok, n_ctrl_bad))
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines_out) + "\n")
    return 0 if (n_fail == 0 and n_ctrl_bad == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
