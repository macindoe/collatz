"""Fresh-code check of paper 1 v4, readability round 3 (branch paper1-v4-readable-2, head cbcc8b8).

Supports: briefs/paper1-v4-readable-3-check-findings.md (the scope-drift check of the plain
abstract and main text against paper/collatz-reduced-v4-claims.md).

One command, from the repository root:

    python experiments/paper1_v4_readable3_check.py

It writes experiments/paper1_v4_readable3_check_output.txt (UTF-8) and exits 0 iff every check
passes and every negative control is rejected. Written from the paper's text; nothing is imported
from the repository's other scripts. Exact integers and Fractions throughout; mpmath (400 digits)
only for real constants, gamma and p1(X0). The TeX sources are read from git at pinned commits,
so the result does not depend on the working tree.

Parts:
  A. Technical summary == the pre-round-3 abstract (6eb5946) minus the one declared sentence;
     and its differences from the locked abstract (tag paper1-v4-content-lock) listed.
  B. Appendices B-E at cbcc8b8 against c7c3c69: only declared moved text differs.
  C. Every worked number in the main text (sections 1-8, Symbols page) recomputed.
  D. Witnesses for the findings (numbers that show a sentence's scope), and negative controls.
"""
import difflib
import math
import random
import re
import subprocess
import sys
from fractions import Fraction

import mpmath

mpmath.mp.dps = 400
HEAD = "cbcc8b8"
TEX = "paper/collatz-reduced-v4.tex"
OUT = "experiments/paper1_v4_readable3_check_output.txt"

lines_out = []
n_pass = n_fail = 0
n_ctrl_ok = n_ctrl_bad = 0
section_counts = {}
current = ["?"]


def say(s=""):
    lines_out.append(s)


def part(name):
    current[0] = name
    section_counts.setdefault(name, [0, 0])
    say()
    say("== " + name)


def check(label, cond, detail=""):
    global n_pass, n_fail
    if cond:
        n_pass += 1
        section_counts[current[0]][0] += 1
    else:
        n_fail += 1
        section_counts[current[0]][1] += 1
    say(("PASS " if cond else "FAIL ") + label + ((" -- " + detail) if detail else ""))


def control(label, rejected, detail=""):
    """A deliberately wrong claim; it must be rejected by the same code."""
    global n_ctrl_ok, n_ctrl_bad
    if rejected:
        n_ctrl_ok += 1
    else:
        n_ctrl_bad += 1
    say(("CONTROL rejected " if rejected else "CONTROL NOT REJECTED ") + label
        + ((" -- " + detail) if detail else ""))


def git_show(rev, path):
    return subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True,
                          check=True).stdout.decode("utf-8")


# ---------------------------------------------------------------- arithmetic primitives
def v2(n):
    n = abs(n)
    assert n != 0
    return (n & -n).bit_length() - 1


def v3(n):
    n = abs(n)
    assert n != 0
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def T(x):
    """Odd-to-odd Collatz map: 3x+1, then every factor of 2 removed."""
    y = 3 * x + 1
    return y >> v2(y)


def state(x):
    """(omega, d) of odd x: x+1 = 2^m 3^a omega."""
    m = v2(x + 1)
    u = (x + 1) >> m
    a = v3(u)
    return (u // 3 ** a, m + a), m, a


def block_by_iteration(x):
    """Walk the block of x with T itself: entry depth m, the T-iterates, and the cascade."""
    m = v2(x + 1)
    seq = [x]
    y = x
    for _ in range(m - 1):
        y = T(y)
        seq.append(y)
    z = 3 * y + 1                      # the cascade's start
    halvings = v2(z)
    return m, seq, z, halvings - 1, z >> halvings   # s = halvings beyond the first


def F(w, d):
    """The reduced map, from Definition B.1's formulas."""
    A = 3 ** d * w - 1
    s = v2(A)
    C = A + (1 << s)
    sig = v2(C)
    ap = v3(C)
    mp_ = sig - s
    return (C >> sig) // 3 ** ap, mp_ + ap, s, mp_, ap


def anchor_mod(w, k):
    """M(w) mod 2^k, where 9^{M(w)/2}... precisely M(w) = N(w^2), 9^{N(u)} = u^{-1} in Z_2.
    Solved by lifting one binary digit at a time: 9^t * w^2 == 1 (mod 2^(j+3))."""
    mod = 1 << (k + 3)
    target = pow(w * w, -1, mod)
    t = 0
    for j in range(k):
        if pow(9, t, 1 << (j + 4)) != target % (1 << (j + 4)):
            t += 1 << j
    assert pow(9, t, mod) == target
    return t


def one_division_orbit(x, steps):
    out = [x]
    for _ in range(steps):
        x = (3 * x + 1) // 2 if x % 2 else x // 2
        out.append(x)
    return out


# ---------------------------------------------------------------- configurations (cycles)
def rational_cycle(ms, ss):
    """Block entries x_r of the rational cycle a configuration defines, built from the
    one-division map: a block (m, s) is m steps y -> (3y+1)/2, then s steps y -> y/2."""
    p = len(ms)

    def blk(y, m, s):
        for _ in range(m):
            y = (3 * y + 1) / 2
        for _ in range(s):
            y = y / 2
        return y

    f0 = Fraction(0)
    for m, s in zip(ms, ss):
        f0 = blk(f0, m, s)
    n = sum(ms)
    K = n + sum(ss)
    q = 2 ** K - 3 ** n
    x0 = f0 * 2 ** K / q             # fixed point of y -> (3^n y + c)/2^K, c = f(0) 2^K
    xs = [x0]
    for r in range(p - 1):
        xs.append(blk(xs[-1], ms[r], ss[r]))
    assert blk(xs[-1], ms[-1], ss[-1]) == x0
    return xs, n, K, q


def rotation_numbers(ms, ss):
    """R_r of Proposition D.1: sum_t 3^{M_t} 2^{S_t} (2^{s_t} - 1), M_t = sum_{j>t} m_j,
    S_t = sum_{j<t} (s_j + m_{j+1}), indices in rotation order from r."""
    p = len(ms)
    out = []
    for r in range(p):
        m = ms[r:] + ms[:r]
        s = ss[r:] + ss[:r]
        R = 0
        for t in range(p):
            Mt = sum(m[t + 1:])
            St = sum(s[j] + m[(j + 1) % p] for j in range(t))
            R += 3 ** Mt * 2 ** St * (2 ** s[t] - 1)
        out.append(R)
    return out


def config_report(ms, ss):
    xs, n, K, q = rational_cycle(ms, ss)
    cof = [(x + 1) / 2 ** m for x, m in zip(xs, ms)]     # = R_r / q
    Rs = rotation_numbers(ms, ss)
    agree = all(Fraction(R, q) == c for R, c in zip(Rs, cof))
    size_pass = q > 0 and all(c >= 1 for c in cof)
    divisible = [c.denominator == 1 for c in cof]
    gamma = K - mpmath.log(q, 2) if q > 0 else None
    return dict(n=n, K=K, q=q, xs=xs, cof=cof, size_pass=size_pass, divisible=divisible,
                gamma=gamma, agree=agree, Rs=Rs)


L = mpmath.log(3, 2)


def phi(x):
    return -mpmath.log(1 - mpmath.power(2, -x), 2)


# ---------------------------------------------------------------- p1(X0), from the proof of D.6(iii)
def convergents(x, count=250):
    a = []
    y = x
    for _ in range(count):
        ai = int(mpmath.floor(y))
        a.append(ai)
        y = 1 / (y - ai)
    P, Q = [1, a[0]], [0, 1]          # P_{-1}=1, P_0=a0 ; Q_{-1}=0, Q_0=1
    for ai in a[1:]:
        P.append(ai * P[-1] + P[-2])
        Q.append(ai * Q[-1] + Q[-2])
    return P[1:], Q[1:]               # index j = 0, 1, 2, ...


PCONV, QCONV = convergents(L)
LAM0 = L / (L - 1) + mpmath.power(2, -20)


def p1(X0):
    X0 = mpmath.mpf(X0)
    g = 1 + max(mpmath.log(X0 + 1, 2), LAM0)
    Delta = phi(g) - phi(g + 1)
    Theta = [abs(Qj * L - Pj) for Pj, Qj in zip(PCONV, QCONV)]
    k = next(k for k in range(1, len(Theta)) if Theta[k - 1] <= Delta)
    Nstar = QCONV[k] + QCONV[k - 1]
    p = 2
    while (L ** p - 1) / (2 * (L - 1)) < max(Nstar, 3 * p + 40):
        p += 1
    return p


# =================================================================================== A
def strip_ws(s):
    return " ".join(s.split())


def main():
    head_tex = git_show(HEAD, TEX)
    pre3_tex = git_show("6eb5946", TEX)
    lock_tex = git_show("paper1-v4-content-lock", TEX)
    c7_tex = git_show("c7c3c69", TEX)

    part("A. Technical summary against the abstracts")
    m = re.search(r"\\section\*\{Technical summary\}.*?\\begin\{quote\}\\small\n(.*?)\\end\{quote\}",
                  head_tex, re.S)
    ts = m.group(1)
    pre3_abs = re.search(r"\\begin\{abstract\}\n(.*?)\\end\{abstract\}", pre3_tex, re.S).group(1)
    lock_abs = re.search(r"\\begin\{abstract\}\n(.*?)\\end\{abstract\}", lock_tex, re.S).group(1)
    dropped = (" The main text tells each idea in words; the statements, proofs and checks are in"
               " the appendices.")
    check("the dropped sentence is in the pre-round-3 abstract (6eb5946)", dropped in pre3_abs)
    check("Technical summary == 6eb5946 abstract minus that sentence, character for character "
          "(blank-line paragraph breaks included)",
          ts.strip() == pre3_abs.replace(dropped, "").strip())
    ts_paras = [p for p in ts.strip().split("\n\n")]
    check("Technical summary has the three paragraphs of the round-1 abstract", len(ts_paras) == 3)
    # differences from the locked abstract, word level
    a_tok, b_tok = strip_ws(lock_abs).split(), strip_ws(ts).split()
    sm = difflib.SequenceMatcher(None, a_tok, b_tok, autojunk=False)
    hunks = [op for op in sm.get_opcodes() if op[0] != "equal"]
    say(f"     word-level hunks between the locked abstract and the Technical summary: {len(hunks)}")
    for tag, i1, i2, j1, j2 in hunks:
        say(f"       {tag}: lock '{' '.join(a_tok[i1:i2])}' -> summary '{' '.join(b_tok[j1:j2])}'")
    # the round-1 changes the previous check (briefs/paper1-v4-readable-check-findings.md section 1)
    # verified as declared: the two plain opening sentences, "We study ... compresses" -> "We
    # compress each such", ", stated as a heuristic,", "(`fair-coin')"
    expected = [
        ("insert", "", "The Collatz map sends an odd number $x$ to $3x+1$ with every factor of $2$ "
                       "divided out. Much of an orbit is bookkeeping: while $x+1$ is divisible by $4$, "
                       "each step trades one factor of $2$ in $x+1$ for a factor of $3$."),
        ("replace", "study the Collatz dynamics in a reduced coordinate system that compresses", "compress"),
        ("insert", "", "such"),
        ("replace", "accounting", "accounting, stated as a heuristic,"),
        ("insert", "", "(`fair-coin')"),
    ]
    got = [(tag, " ".join(a_tok[i1:i2]), " ".join(b_tok[j1:j2])) for tag, i1, i2, j1, j2 in hunks]
    check("the Technical summary differs from the locked abstract by exactly the round-1 changes "
          "already checked as declared (5 word-level hunks)", got == expected, f"{len(hunks)} hunks")
    control("a summary that kept the round-1 layout sentence would not equal the declared text",
            (ts.strip() + dropped) != pre3_abs.replace(dropped, "").strip())

    # =============================================================================== B
    part("B. Appendices B-E: cbcc8b8 against c7c3c69")

    def app_be(tex):
        i = tex.index(r"\section{The reduced system: definitions and proofs}")
        j = tex.index(r"\section{Related work in detail}")
        return tex[i:j]

    old_be, new_be = app_be(c7_tex), app_be(head_tex)
    sm = difflib.SequenceMatcher(None, old_be.splitlines(), new_be.splitlines(), autojunk=False)
    ops = [op for op in sm.get_opcodes() if op[0] != "equal"]
    say(f"     line hunks in Appendices B-E: {len(ops)}")
    for tag, i1, i2, j1, j2 in ops:
        say(f"       {tag} old {i1+1}-{i2} new {j1+1}-{j2}")
    check("exactly one hunk in Appendices B-E", len(ops) == 1)
    tag, i1, i2, j1, j2 = ops[0]
    old_txt = "\n".join(old_be.splitlines()[i1:i2])
    new_txt = "\n".join(new_be.splitlines()[j1:j2])
    check("the hunk is App B's opening paragraph and keeps its old sentence",
          old_txt.strip() == r"This appendix states formally what Sections~\ref{sec:block} and~\ref{sec:reduced} tell in words."
          and new_txt.startswith(old_txt.strip()))
    moved = [
        r"\[ T(x) = \frac{3x+1}{2^{\vt{3x+1}}} \qquad (x \text{ odd and positive})",
        r"Tao's Syracuse map $\mathrm{Syr}$ \cite{tao}",
        r"the Collatz conjecture asserts that every $T$-orbit reaches $1$",
        r"$\vt{n}$, the \emph{$2$-adic valuation} of $n$, is the number of times $2$ divides $n$",
        r"T(x) + 1 = \tfrac{3}{2}\,(x+1)",
    ]
    c7_main = c7_tex[:c7_tex.index(r"\appendix")]
    for frag in moved:
        check("App B's added text was main text at c7c3c69: " + frag[:60],
              frag.replace(r"\tfrac{3}{2}\,", r"\tfrac{3}{2}\,") in c7_main
              or frag.lower() in c7_main.lower())
    check("App B's added text: the identity is now written \\tfrac32\\,(x+1) (same formula)",
          r"T(x) + 1 = \tfrac32\,(x+1)" in new_txt)
    check("App B's added text: the one clause not taken from the old main text is the definition "
          "of v_3 (a definition; v_3 was used undefined in the lock)",
          r"$\vth{n}$ is the number of times $3$ divides $n$" in new_txt
          and r"number of times $3$ divides" not in c7_main)
    check("Prop B.2(i)'s proof (the identity's new pointer) contains T(y)+1 = 2^{k-1}(3v)",
          r"T(y) + 1 = 2^{k-1}(3v)" in head_tex)
    # Appendix F: the moved contemporary-work paragraph
    c7_s8 = c7_tex[c7_tex.index(r"\section{Credit and provenance}"):c7_tex.index(r"\appendix")]
    contemp = [p for p in c7_s8.split("\n\n") if p.startswith("Two contemporary human--AI efforts")][0]
    appF = head_tex[head_tex.index(r"\section{Related work in detail}"):head_tex.index(r"\section{Verification index}")]
    check("Appendix F's new paragraph is c7c3c69's section 8 contemporary-work paragraph verbatim",
          contemp.strip() in appF)
    # section 8 provenance paragraph
    prov_old = [p for p in c7_s8.split("\n\n") if p.startswith("The division of labor")][0].strip()
    head_s8 = head_tex[head_tex.index(r"\section{Credit and provenance}"):head_tex.index(r"\appendix")]
    prov_new = [p for p in head_s8.split("\n\n") if p.startswith("The division of labor")][0].strip()
    check("section 8 provenance paragraph: c7c3c69 text with only 'Her open problem' -> "
          "'Williams's open problem'",
          prov_old.replace("Her open problem", "Williams's open problem") == prov_new)
    control("a provenance paragraph with any other word changed is detected",
            prov_old.replace("posted earlier", "posted later") != prov_new)

    # =============================================================================== C
    part("C1. Section 2: the orbit of 7, one rising run")
    rows = [(7, "111", "1000", (3, 0, 1)), (11, "1011", "1100", (2, 1, 1)),
            (17, "10001", "10010", (1, 2, 1)), (13, "1101", "1110", (1, 0, 7))]
    x = 7
    for i, (xx, bx, bx1, (e2, e3, rest)) in enumerate(rows):
        check(f"table row {i}: x = {xx}", x == xx, f"got {x}")
        check(f"  binary of {xx} is {bx}, of {xx}+1 is {bx1}",
              format(xx, "b") == bx and format(xx + 1, "b") == bx1)
        check(f"  {xx}+1 = 2^{e2} 3^{e3} * {rest}", xx + 1 == 2 ** e2 * 3 ** e3 * rest)
        x = T(x)
    check("3*8 = 24 is a multiple of 4 and 22 = 24 - 2 halves once, to 11",
          24 % 4 == 0 and 3 * 7 + 1 == 22 and v2(22) == 1 and 22 // 2 == 11)
    check("11+1 = 12 = (3/2)(7+1); 17+1 = 18 = (3/2)*12",
          Fraction(12) == Fraction(3, 2) * 8 and Fraction(18) == Fraction(3, 2) * 12)
    check("rising step: x+1 divisible by 4 => 3x+1 = 3(x+1) - 2 is 2 mod 4, halves once, result > x "
          "(every x = 3 mod 4 below 200001)",
          all((3 * y + 1) % 4 == 2 and T(y) > y and T(y) + 1 == Fraction(3, 2) * (y + 1)
              for y in range(3, 200001, 4)))
    check("trade stops: x+1 = 2*odd => 3x+1 divisible by 4 (every x = 1 mod 4 below 200001)",
          all((3 * y + 1) % 4 == 0 for y in range(1, 200001, 4)))
    check("3*17+1 = 52 = 110100 in binary, halves twice, to 13",
          3 * 17 + 1 == 52 and format(52, "b") == "110100" and v2(52) == 2 and 52 >> 2 == 13)
    m, seq, z, s, ex = block_by_iteration(7)
    check("block of 7: m = 3, numbers 7, 11, 17, cascade 52 -> 26 -> 13, s = 1, exit 13",
          (m, seq, z, s, ex) == (3, [7, 11, 17], 52, 1, 13))
    check("m = number of trailing 1s of x, and the next m-1 steps rise, then a cascade of >= 2 "
          "halvings (every odd x below 100001)",
          all(len(format(y, "b")) - len(format(y, "b").rstrip("1")) == v2(y + 1)
              and all(T(t) > t for t in block_by_iteration(y)[1][:-1])
              and block_by_iteration(y)[3] >= 1
              for y in range(1, 100001, 2)))
    check("one-division map from 7: odd 7, 11, 17, then even 26, then 13",
          one_division_orbit(7, 4) == [7, 11, 17, 26, 13])
    check("one-division map: a block (m, s) is m odd terms then s even terms (every odd x < 50001)",
          all((lambda mm, ss_, od: all(t % 2 == 1 for t in od[:mm]) and all(t % 2 == 0 for t in od[mm:mm + ss_])
               and od[mm + ss_] % 2 == 1)(block_by_iteration(y)[0], block_by_iteration(y)[3],
                                         one_division_orbit(y, block_by_iteration(y)[0] + block_by_iteration(y)[3]))
              for y in range(1, 50001, 2)))

    part("C2. Section 3: states and the reduced map")
    st, m7, a7 = state(7)
    check("x = 7: x+1 = 8, m = 3, a = 0, omega = 1, d = 3, state (1,3)", (st, m7, a7) == ((1, 3), 3, 0))
    check("17 + 1 = 18 = 2 * 1 * 3^2, with d - 1 = 2 threes", 18 == 2 * 1 * 3 ** 2)
    check("after the m-1 rising steps, x+1 = 2 * 3^(d-1) * omega (every odd x < 100001)",
          all((lambda st_, sq: sq[-1] + 1 == 2 * 3 ** (st_[0][1] - 1) * st_[0][0])(state(y), block_by_iteration(y)[1])
              for y in range(1, 100001, 2)))
    groups = {}
    for y in range(1, 1 << 17, 2):
        groups.setdefault(state(y)[0], []).append(y)
    check("numbers of state (1,3) below 2^17: exactly 7 (m=3), 11 (m=2, 12 = 4*3), 17 (m=1, 18 = 2*9)",
          groups[(1, 3)] == [7, 11, 17] and state(11)[1] == 2 and state(17)[1] == 1)
    check("all three exit at 13", {block_by_iteration(y)[4] for y in (7, 11, 17)} == {13})
    full = [(w, d) for (w, d) in groups if 2 * 3 ** (d - 1) * w - 1 < (1 << 17) and 2 ** d * w - 1 < (1 << 17)]
    check(f"exactly d odd numbers per state, all with one exit ({len(full)} states with every "
          f"representative below 2^17)",
          all(len(groups[s_]) == s_[1] and len({block_by_iteration(y)[4] for y in groups[s_]}) == 1
              for s_ in full))
    check("every valid state (omega < 3000, d <= 20) is the state of 2^d omega - 1",
          all(state(2 ** d * w - 1)[0] == (w, d) for w in range(1, 3000, 2) if w % 3 for d in range(1, 21)))
    chain = [(1, 3)]
    for _ in range(4):
        chain.append(F(*chain[-1])[:2])
    check("states run (1,3), (7,1), (1,2), (1,1), (1,1)", chain == [(1, 3), (7, 1), (1, 2), (1, 1), (1, 1)])
    check("13+1 = 14 = 2*7; 3*13+1 = 40 halves three times (s = 2) to 5",
          14 == 2 * 7 and 40 == 3 * 13 + 1 and v2(40) == 3 and 40 >> 3 == 5 and F(7, 1)[2] == 2)
    check("5+1 = 6 = 2*3; 3*5+1 = 16 halves four times (s = 3) to 1",
          state(5)[0] == (1, 2) and v2(16) == 4 and F(1, 2)[2] == 3 and block_by_iteration(5)[4] == 1)
    check("1+1 = 2: state (1,1); 3*1+1 = 4 halves twice (s = 1), back to 1",
          state(1)[0] == (1, 1) and v2(4) == 2 and F(1, 1)[2] == 1 and T(1) == 1)
    check("F(1,1) = (1,1) and the only number of state (1,1) is 1", F(1, 1)[:2] == (1, 1) and groups[(1, 1)] == [1])
    check("R(T^m x) = F(R x) for every odd x < 2^17",
          all(state(block_by_iteration(y)[4])[0] == F(*state(y)[0])[:2] for y in range(1, 1 << 17, 2)))

    part("C3. Section 4: the exact laws on the example")
    check("(1,3): 27 - 1 = 26 = 2*13, s = 1", 3 ** 3 - 1 == 26 == 2 * 13 and v2(26) == 1)
    check("cascade starts from 2(3^d omega - 1) (every odd x < 50001)",
          all(block_by_iteration(y)[2] == 2 * (3 ** state(y)[0][1] * state(y)[0][0] - 1) for y in range(1, 50001, 2)))
    check("powers of 3 mod 8: 3, 1, 3, 1, ...", [pow(3, j, 8) for j in range(1, 9)] == [3, 1] * 4)
    printed = {(1, 0): "lift", (3, 0): 1, (5, 0): 2, (7, 0): 1, (1, 1): 1, (3, 1): "lift", (5, 1): 1, (7, 1): 2}
    ok = True
    n_states = 0
    lifting_states = []
    for w in range(1, 3001, 2):
        if w % 3 == 0:
            continue
        for d in range(1, 41):
            n_states += 1
            s = v2(3 ** d * w - 1)
            cell = printed[(w % 8, d % 2)]
            r8 = (3 ** d * w) % 8
            if cell == "lift":
                ok &= (r8 == 1 and s >= 3)
                lifting_states.append((w, d, s))
            else:
                ok &= (s == cell and r8 in (3, 5, 7) and (3 ** d * w - 1) % 8 in (2, 4, 6))
    check(f"the printed eight-kind table, every cell ({n_states} states, omega < 3001, d <= 40)", ok)
    check("lifting = (1, even) or (3, odd)", all(((w % 8, d % 2) in ((1, 0), (3, 1))) for w, d, _ in lifting_states))
    check("example kinds: (1,3) and (1,1) are (1, odd) with s = 1; (7,1) is (7, odd) with s = 2",
          printed[(1, 1)] == 1 and printed[(7, 1)] == 2 and v2(3 ** 1 * 7 - 1) == 2)
    check("anchor of 1 is the all-zero string (M(1) = 0 mod 2^64)", anchor_mod(1, 64) == 0)
    agree_ok = True
    for w, d, s in lifting_states:
        M = anchor_mod(w, 64)
        k = 0
        while k < 64 and ((d >> k) & 1) == ((M >> k) & 1):
            k += 1
        agree_ok &= (k < 60 and s == 2 + k)
    check(f"s = 2 + (number of lowest binary digits on which d and the anchor agree), on all "
          f"{len(lifting_states)} lifting states of the table range", agree_ok)
    check("(1,2): d = 2 = 10b, one trailing zero, s = 3; 3*5+1 = 16 halves four times = 1 + s",
          format(2, "b") == "10" and v2(2) == 1 and F(1, 2)[2] == 3 and v2(16) == 1 + 3)
    check("powers of 2 mod 3: 2, 1, 2, 1, ...", [pow(2, j, 3) for j in range(1, 9)] == [2, 1] * 4)
    check("the next state gains a factor of 3 exactly when s is even (omega < 3001, d <= 40)",
          all((F(w, d)[4] > 0) == (F(w, d)[2] % 2 == 0)
              for w in range(1, 3001, 2) if w % 3 for d in range(1, 41)))
    check("(7,1): 21 + 3 = 24, a multiple of 3; next state (1,2) has a = 1",
          3 * 7 + (2 ** 2 - 1) == 24 and 24 % 3 == 0 and F(7, 1)[:2] == (1, 2) and F(7, 1)[4] == 1)
    check("blocks with s = 1 and s = 3 in the example gain none", F(1, 3)[4] == 0 and F(1, 2)[4] == 0)
    check("from (7,1): next number 5, 6 = 2*3: entry depth 1, absorption 1, next depth 2",
          F(7, 1)[3] == 1 and F(7, 1)[4] == 1 and F(7, 1)[1] == 2)
    check("next entry depth >= 1 (omega < 3001, d <= 40)",
          all(F(w, d)[3] >= 1 for w in range(1, 3001, 2) if w % 3 for d in range(1, 41)))
    check("on lifting states the displacement is half of d - M(omega): d - M(omega) is even "
          "(all lifting states of the range)",
          all((d - anchor_mod(w, 64)) % 2 == 0 for w, d, _ in lifting_states))
    for k, txt_frac, txt_pct in ((4, Fraction(1, 32), 3.125), (8, Fraction(1, 512), 0.195)):
        rates = set()
        for D in range(k + 2, k + 12):
            tail = sum(Fraction(1, 2 ** j) for j in range(k + 2, D)) + Fraction(1, 2 ** (D - 1))
            rates.add(tail)
        check(f"undecided rate at depth {k}: 1/2^{k+1} = {txt_frac} under the capped model for every cap "
              f"D >= k+2 (checked D = {k+2}..{k+11}); printed {txt_pct}%",
              rates == {txt_frac} and round(float(txt_frac) * 100, 3) == txt_pct)
    check("under the model s and the next entry depth each average 2, so s + m_+ averages 4 "
          "(closed form sum_j j 2^-j = 2; partial sums exact to 2 - (J+2)/2^J)",
          all(sum(Fraction(j, 2 ** j) for j in range(1, J + 1)) == 2 - Fraction(J + 2, 2 ** J) for J in (10, 40)))

    part("C4. Section 5: the trivial cycle and the p = 7 staircase")
    rep = config_report([1], [1])
    check("trivial cycle: n = 1, K = 2, q = 1, gamma = 2, R = 4 - 3 = 1 = q",
          (rep["n"], rep["K"], rep["q"]) == (1, 2, 1) and abs(rep["gamma"] - 2) < 1e-300
          and rep["Rs"] == [1] and rep["xs"] == [1])
    check("3 = 4 * (1 - 1/4)", 3 == 4 * (1 - Fraction(1, 4)))
    ms = [4, 7, 9, 15, 23, 35, 1]
    ss = [1, 1, 1, 1, 1, 1, 49]
    rep = config_report(ms, ss)
    check("staircase: p = 7, n = 94, exit valuations total 55, K = 94 + 55 = 149",
          len(ms) == 7 and rep["n"] == 94 and sum(ss) == 55 and rep["K"] == 149 == 94 + 55)
    check("K = 149 = ceil(94 log2 3): 2^148 < 3^94 < 2^149", 2 ** 148 < 3 ** 94 < 2 ** 149)
    check("the two cycle-cofactor computations agree (rational cycle vs Prop D.1's R_r)", rep["agree"])
    check("passes all seven size tests", rep["size_pass"],
          "min R_r/q = " + mpmath.nstr(min(mpmath.mpf(c.numerator) / c.denominator for c in rep["cof"]), 6))
    check("gamma = 6.74", mpmath.nstr(rep["gamma"], 3) == "6.74", mpmath.nstr(rep["gamma"], 10))
    p3 = Fraction(1157, 10000) * 94 - 2
    check("three-block constant 0.1157 n - 2 at n = 94 is 8.8758, printed 'above 8.9'",
          p3 == Fraction(88758, 10000) and round(float(p3), 1) == 8.9)
    check("fails divisibility at every rotation", not any(rep["divisible"]))
    ratios = [Fraction(ms[i + 1], ms[i]) for i in range(5)]
    check("first six depths grow roughly geometrically (ratios 1.75, 1.29, 1.67, 1.53, 1.52)",
          all(Fraction(5, 4) < r < Fraction(9, 5) for r in ratios),
          ", ".join(f"{float(r):.3f}" for r in ratios))
    # the seeded search at p = 6 (the procedure the record states, re-implemented)
    p = 6
    passers = []
    rnd = random.Random()
    random.seed(41)
    for n in range(20, 140):
        T3 = 3 ** n
        K = T3.bit_length()
        S = K - n
        if S < p:
            continue
        cands = set()
        for m0 in (1, 2, 3):
            for ratio in (1.45, 1.585, 1.7):
                mm = [max(1, round(m0 * ratio ** j)) for j in range(p - 1)]
                rest = n - sum(mm)
                if rest < 1:
                    continue
                mm = mm + [rest]
                for cp in range(p):
                    s_ = [1] * p
                    s_[cp] = S - (p - 1)
                    if s_[cp] < 1:
                        continue
                    cands.add((tuple(mm), tuple(s_)))
        more = set()
        for a_, b_ in cands:
            for _ in range(6):
                mm = list(a_)
                i, j = random.randrange(p), random.randrange(p)
                if mm[i] > 1:
                    mm[i] -= 1
                    mm[j] += 1
                more.add((tuple(mm), tuple(b_)))
        for a_, b_ in cands | more:
            if sum(a_) != n or sum(b_) != S or min(a_) < 1:
                continue
            r_ = config_report(list(a_), list(b_))
            if r_["size_pass"]:
                passers.append((n, a_, b_, r_))
    margins = [r_["gamma"] - (mpmath.mpf("0.1157") * n - 2) for n, _, _, r_ in passers]
    check("seeded search (seed 41) at six blocks: 84 staircase size-passers",
          len(passers) == 84 and len({(a_, b_) for _, a_, b_, _ in passers}) == 84, f"{len(passers)}")
    check("none below the three-block constant; each clears it by at least 0.698",
          min(margins) >= mpmath.mpf("0.698"), "min margin " + mpmath.nstr(min(margins), 6))
    check("all 84 fail the divisibility conditions", not any(any(r_["divisible"]) and all(r_["divisible"])
                                                            for *_, r_ in passers)
          and not any(all(r_["divisible"]) for *_, r_ in passers))
    check("the 84 at n in {20, 22, 27, 29, 34, 41, 46}", sorted({n for n, *_ in passers}) == [20, 22, 27, 29, 34, 41, 46])

    part("C5. Section 5: sharpness constants and the threshold p1(X0)")
    Gstar = mpmath.mpf("1.05") * L * (L - 1) + 1 / (L - 1) + 1
    phi_lo = phi(mpmath.mpf("0.0415"))
    check("Gamma* = 1.05 L (L-1) + 1/(L-1) + 1 = 3.68301..., 'about 3.68'; >= 3.683012",
          mpmath.nstr(Gstar, 3) == "3.68" and Gstar >= mpmath.mpf("3.683012"), mpmath.nstr(Gstar, 10))
    check("phi(0.0415) = 5.14021..., 'about 5.14'; <= 5.140212",
          mpmath.nstr(phi_lo, 3) == "5.14" and phi_lo <= mpmath.mpf("5.140212"), mpmath.nstr(phi_lo, 10))
    avail = True
    cross = True
    for pp in range(16, 61):
        lo = int(mpmath.ceil(L ** pp))
        hi = int(mpmath.floor(mpmath.mpf("1.05") * L ** pp))
        found = False
        for n in range(lo, min(hi, lo + 200) + 1):
            K = int(mpmath.ceil(n * L))
            g = phi(K - n * L)                    # gamma = phi(delta_n) since q/2^K = 1 - 2^-delta_n
            if mpmath.mpf("3.683012") <= g <= mpmath.mpf("5.140212"):
                found = True
                if pp <= 20:                      # exact big-integer cross-check where affordable
                    cross &= abs(g - (K - mpmath.log(2 ** K - 3 ** n, 2))) < mpmath.mpf(10) ** -300
                break
        avail &= found
    check("for every p = 16..60 some n in [L^p, 1.05 L^p] (within its first 200) has gamma(n, ceil(nL)) "
          "in [3.683012, 5.140212] (gamma via phi(delta_n); exact big-integer gamma agrees at p <= 20)",
          avail and cross)
    check("lambda_0 = L/(L-1) + 2^-20 = 2.70951..., 'about 2.71'; lambda_0 + 1.5 'about 4.21'",
          mpmath.nstr(LAM0, 3) == "2.71" and mpmath.nstr(LAM0 + 1.5, 3) == "4.21", mpmath.nstr(LAM0, 10))
    c054 = mpmath.power(2, -(LAM0 + 1.5))
    check("2^-(lambda_0 + 1.5) = 0.05405 >= 0.054 ('cannot be lowered below 0.054')",
          c054 >= mpmath.mpf("0.054") and c054 < mpmath.mpf("0.0541"), mpmath.nstr(c054, 6))
    p1vals = {}
    for lab, X0 in (("1", 1), ("2", 2), ("10", 10), ("16", 16), ("2^8", 2 ** 8), ("2^9", 2 ** 9),
                    ("2^10.5", mpmath.power(2, 10.5)), ("2^12", 2 ** 12), ("2^20", 2 ** 20),
                    ("5*2^60", 5 * 2 ** 60), ("2^71", 2 ** 71), ("2^200", 2 ** 200)):
        p1vals[lab] = p1(X0)
    say("     p1: " + ", ".join(f"{k}->{v}" for k, v in p1vals.items()))
    check("p1 = 10 for X0 <= 16 (X0 = 1, 2, 10, 16)", all(p1vals[k] == 10 for k in ("1", "2", "10", "16")))
    check("p1 = 22 for 2^8 <= X0 <= 2^12 (2^8, 2^9, 2^10.5, 2^12)",
          all(p1vals[k] == 22 for k in ("2^8", "2^9", "2^10.5", "2^12")))
    check("p1(2^20) = 36", p1vals["2^20"] == 36)
    check("p1(5 * 2^60) = 98", p1vals["5*2^60"] == 98)
    check("p1(2^71) = 110", p1vals["2^71"] == 110)
    check("p1(2^200) = 309", p1vals["2^200"] == 309)
    grid = [p1(mpmath.power(2, mpmath.mpf(j) / 4)) for j in range(0, 801, 7)]
    check("p1 nondecreasing in X0 (X0 = 2^(j/4), j = 0, 7, ..., 798)", all(a <= b for a, b in zip(grid, grid[1:])))

    part("C6. Section 6: letters, the tally example, the base case")
    letters = []
    y = 7
    for _ in range(4):
        m_, _, _, s_, ex = block_by_iteration(y)
        letters.append((m_, s_))
        y = ex
    check("letters of the running example: (3,1), (1,2), (1,3), (1,1)", letters == [(3, 1), (1, 2), (1, 3), (1, 1)])
    check("letter (1,2) has chance 1/2 * 1/4 = 1/8", Fraction(1, 2) * Fraction(1, 4) == Fraction(1, 8))
    check("1/4 + 1/16 + 1/64 + ... = 1/3 (geometric series, and the even-s mass under halving law)",
          Fraction(1, 4) / (1 - Fraction(1, 4)) == Fraction(1, 3)
          and abs(sum(Fraction(1, 2 ** j) for j in range(2, 80, 2)) - Fraction(1, 3)) < Fraction(1, 2 ** 78))
    for b in (39, 40):
        check(f"tally example, b = floor(log2 N) = {b} (a start with about 40 binary digits): horizon "
              f"ceil(b/10) = 4 blocks; budget ceil(b/2) = 20, 'fewer than 20 halvings'",
              math.ceil(Fraction(b, 10)) == 4 and math.ceil(Fraction(b, 2)) == 20)
    check("4 x 1/10 < 1/2", 4 * Fraction(1, 10) < Fraction(1, 2))
    check("a budget rate tau with 4 theta < tau < 1 exists iff theta < 1/4 (theta on a grid of 1/1000)",
          all((Fraction(t, 1000) < Fraction(1, 4)) == (4 * Fraction(t, 1000) < 1) for t in range(1, 1000)))
    check("1024 consecutive integers = ten binary digits' worth", 2 ** 10 == 1024)

    def compositions_even(total_max):
        out = []

        def rec(prefix, tot):
            if prefix and len(prefix) % 2 == 0:
                out.append(tuple(prefix))
            for v in range(1, total_max - tot + 1):
                rec(prefix + [v], tot + v)
        rec([], 0)
        return out

    pats = compositions_even(9)

    def itinerary(x, need):
        seq = []
        tot = 0
        while tot < need:
            m_, _, _, s_, ex = block_by_iteration(x)
            seq += [m_, s_]
            tot += m_ + s_
            x = ex
        return seq

    windows = [1, 2, 1025, 12345, 2 ** 40 + 777, 10 ** 12 + 3, 3 ** 30]
    rr = random.Random(20261020)
    windows += [rr.randrange(1, 2 ** 50) for _ in range(3)]
    base_ok = True
    for w0 in windows:
        odds = [x for x in range(w0, w0 + 1024) if x % 2]
        counts = {}
        for x in odds:
            it = itinerary(x, 10)
            for L_ in range(2, len(it) + 1, 2):
                pre = tuple(it[:L_])
                if sum(pre) <= 9:
                    counts[pre] = counts.get(pre, 0) + 1
        for pt in pats:
            if counts.get(pt, 0) != 2 ** (9 - sum(pt)):
                base_ok = False
    check(f"base-case example: in each of {len(windows)} windows of 1024 consecutive integers, every "
          f"pattern of first blocks (start's own block included) with fewer than ten halvings in all "
          f"({len(pats)} patterns) occurs among the 512 odd numbers exactly 512 / 2^S times",
          base_ok)

    # =============================================================================== D
    part("D. Witnesses for the findings")
    rep1 = config_report([1], [1])
    check("WITNESS abstract / What-is-new (v): the trivial cycle is a one-block cycle that meets "
          "every size and divisibility condition (so 'no cycles made of one ... block' needs "
          "'other than 1, 4, 2, 1')", rep1["size_pass"] and all(rep1["divisible"]) and rep1["xs"] == [1])
    check("WITNESS 'rising steps' for n: in the staircase n = 94 but its rising steps number "
          "n - p = 87", 94 - 7 == 87 and sum(m_ - 1 for m_ in ms) == 87)
    lo_gap = LAM0 + 1.5 + mpmath.log(10, 2)
    hi_gap = LAM0 + 1.5 + mpmath.log(309, 2)
    check("WITNESS abstract 'exceeding the classical bound's own requirement by at most a fixed "
          "amount': read as the trim's requirement on gamma (n kappa_p - log2 p), the D.6(iii) upper "
          "excess lambda_0 + 1.5 + log2 p is not fixed: 7.53 at p = 10, 12.48 at p = 309",
          mpmath.nstr(lo_gap, 3) == "7.53" and mpmath.nstr(hi_gap, 4) == "12.48")
    part("C7. Quoted figures: main text against the ledger (transcription)")
    ledger = git_show(HEAD, "paper/collatz-reduced-v4-claims.md")
    main_txt = head_tex[head_tex.index(r"\section*{Symbols at a glance}"):head_tex.index(r"\appendix")]
    pairs = [
        (r"$2.75\%$ at depth $4$", "0.0275", "measured undecided rate, depth 4"),
        (r"$0.19\%$ at depth $8$", "0.0019", "measured undecided rate, depth 8"),
        (r"$0.2503 \pm 0.0015$", "0.2503 ± 0.0015", "fourth anomaly statistic"),
        (r"$84{,}739$ visits", "84,739 visits", "fourth anomaly visits"),
        (r"up to $41$ standard deviations", "z = 41", "bottom-regime bias"),
        (r"below $2$ to the power $40$", "2^{40}", "the 2^40 cut"),
        (r"five standard deviations", "5σ", "the fourth anomaly"),
        (r"at most $91$ blocks", "p ≤ 91", "Hercher"),
        (r"$84$ further staircase size-passers", "84 further staircase size-passers", "p = 6 search"),
        (r"at least $0.698$", "at least 0.698", "p = 6 margin"),
        (r"below $0.054$", "below `0.054`", "prefactor"),
        (r"$110$ at $2^{71}$", "`110` at `2^{71}`", "p1 at 2^71"),
        (r"$309$ at $2^{200}$", "`309` at `2^{200}`", "p1 at 2^200"),
        (r"$98$ at the threshold Simons and de~Weger used", "`98` at SdW's", "p1 at 5*2^60"),
        (r"An eight-round test campaign", "An eight-round campaign", "calibration rounds"),
    ]
    for t_, l_, what in pairs:
        check(f"{what}: main text '{t_}' / ledger '{l_}'", t_ in main_txt and l_ in ledger)

    part("D. Negative controls")
    bad_table = dict(printed)
    bad_table[(5, 0)] = 1
    control("a table with (5, d even) -> s = 1", any(v2(3 ** d * w - 1) != bad_table[(w % 8, d % 2)]
                                                    for w in range(5, 400, 8) for d in range(2, 20, 2)))
    control("K = 150 for the staircase", config_report(ms, ss)["K"] != 150)
    rep48 = config_report(ms[:-1] + [1], ss[:-1] + [48])
    control("last exit 48 keeps K = 149", rep48["K"] != 149)
    control("a flat profile (13 x 7 ... ) passes the size tests",
            not config_report([13, 13, 13, 13, 13, 13, 16], ss)["size_pass"])
    control("p1(2^20) = 35", p1(2 ** 20) != 35)
    control("states run (1,3), (7,1), (1,1)", chain[:3] != [(1, 3), (7, 1), (1, 1)])
    control("letters (3,1), (1,3), (1,2), (1,1)", letters != [(3, 1), (1, 3), (1, 2), (1, 1)])
    w0 = 1025
    odds = [x for x in range(w0, w0 + 1024) if x % 2]
    c10 = {}
    for x in odds:
        it = itinerary(x, 12)
        tot = 0
        for L_ in range(2, len(it) + 1, 2):
            pre = tuple(it[:L_])
            if sum(pre) == 10:
                c10[pre] = c10.get(pre, 0) + 1
    control("patterns with ten halvings (S = 10, one past the range) are also exact in a 1024-window",
            any(c10.get(pt, 0) * 2 ** 10 != 512 for pt in [q_ for q_ in compositions_even(10) if sum(q_) == 10]))
    control("a two-block configuration (m, s) = ((1,1),(1,1)) is a cycle other than 1,4,2,1",
            config_report([1, 1], [1, 1])["xs"] == [1, 1])
    control("the tally example with b = 41 still follows 4 blocks", math.ceil(Fraction(41, 10)) != 4)

    say()
    say("== Totals")
    for k, (a_, b_) in section_counts.items():
        if k.startswith("D. Negative"):
            continue
        say(f"   {k}: {a_} pass, {b_} fail")
    say(f"   checks: {n_pass} pass, {n_fail} fail; negative controls: {n_ctrl_ok} rejected, "
        f"{n_ctrl_bad} not rejected")
    text = "\n".join(lines_out) + "\n"
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("paper 1 v4 readability round 3: fresh-code check at " + HEAD + "\n")
        fh.write("command: python experiments/paper1_v4_readable3_check.py\n")
        fh.write(text)
    sys.stdout.buffer.write(text.encode("utf-8"))
    return 0 if (n_fail == 0 and n_ctrl_bad == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
