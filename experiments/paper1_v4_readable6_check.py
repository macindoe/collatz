#!/usr/bin/env python3
"""
paper1_v4_readable6_check.py -- scope-drift check of readability round 6 (final polish) of paper 1 v4
(paper/collatz-reduced-v4.tex at 73d51d4 against round 5 on main at 56d6b3b).

Supports: briefs/paper1-v4-readable-6-check-findings.md (all sections).

Written for this check from the paper's text alone (main text; Definition C.1; Lemma C.4; Theorem C.5;
Proposition D.1; Hypothesis E.1 and its terms).  It imports nothing from the repository and reuses
no code from experiments/.  Exact integers and Fractions for every integer decision.  The TeX and the
claims ledger are read from git at pinned commits, so the result does not depend on the checkout.

Parts:
  A. The round-5 check's required fix (section 4, verbatim) and its four optional notes (a)-(d),
     plus the two further notes applied (App C names depth_law_reverify.py; "the staircases of
     part (i)" in App D).
  B. Unchanged text: the 19 formal statement environments and the Technical summary are identical
     to 56d6b3b; from \\appendix on, exactly three non-blank lines differ (one in each guided account
     of C, D, E); Version note and Author's note identical.  A one-character edit is caught.
  C. The changed-sentence inventory: every sentence of the abstract, the Symbols page and
     sections 1-8 (and of the three guided accounts) that is new at 73d51d4 is listed, and each is
     matched to exactly one verdict entry of the findings (id, ledger rows, verdict).  An unmatched
     sentence fails the check.
  D. Worked numbers, recomputed fresh: section 2's "twice an odd number"; section 3's
     d - 1 count, (7,1) and (1,2) blocks of one odd number, the fibre of (1,1); section 4's (7,1);
     section 5's n = 94 as a sum, K = 149, gamma in words (gap = 2^K / 2^gamma), 6.74, divisibility
     failing at every rotation, Rhin's bound respected; section 6's letters m|s and 1/8; the
     base-case reason (the coding fact: starts with a given pattern of first blocks form exactly one
     residue class mod 2^(S+1), each in its coin share, in any window of 2^J integers with
     S + 1 <= J); a witness that the admissibility gloss needs its "all but a vanishing share"
     quantifier; the minimax gloss (best worst case over real block depths = kappa_p n, extremal
     ratio L); section 8's "laws give ... the depth k" (d+ from Lemma C.4 + Theorem C.5 against F).
  E. Negative controls: each must be rejected by the same code.

Scope (README stopping rules): no cycle search.  Size and divisibility are evaluated only on the
paper's own printed seven-block configuration; the coding fact is checked on a fixed range.

Reproduce (one command; deterministic; well under a minute):

    python experiments/paper1_v4_readable6_check.py

It writes experiments/paper1_v4_readable6_check_output.txt (UTF-8, no BOM) and exits 0 iff every
check passes and every control is rejected.
"""

import difflib
import math
import os
import random
import re
import subprocess
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "paper1_v4_readable6_check_output.txt")

NEW = "73d51d4"   # round 6 (paper1-v4-readable-6 head)
OLD = "56d6b3b"   # round 5 on main
TEX = "paper/collatz-reduced-v4.tex"
LEDGER = "paper/collatz-reduced-v4-claims.md"

lines_out = []
n_pass = n_fail = n_ctrl_ok = n_ctrl_bad = 0


def say(s=""):
    lines_out.append(s)


def check(label, cond, detail=""):
    global n_pass, n_fail
    if cond:
        n_pass += 1
        say(f"  PASS  {label}" + (f"  [{detail}]" if detail else ""))
    else:
        n_fail += 1
        say(f"  FAIL  {label}" + (f"  [{detail}]" if detail else ""))


def control(label, claim_holds, detail=""):
    """A deliberately false claim, evaluated by the same code; it must come out False (rejected)."""
    global n_ctrl_ok, n_ctrl_bad
    if not claim_holds:
        n_ctrl_ok += 1
        say(f"  CONTROL rejected  {label}" + (f"  [{detail}]" if detail else ""))
    else:
        n_ctrl_bad += 1
        say(f"  CONTROL NOT REJECTED  {label}" + (f"  [{detail}]" if detail else ""))


def show(commit, path):
    r = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git show {commit}:{path} failed: {r.stderr.decode()}")
    return r.stdout.decode("utf-8")


def between(t, a, b, start=0):
    i = t.index(a, start)
    j = t.index(b, i + len(a))
    return t[i:j]


def norm(t):
    return " ".join(t.split())


r5 = show(OLD, TEX)
r6 = show(NEW, TEX)
led = show(NEW, LEDGER)
check_led_same = show(OLD, LEDGER) == led

APPX = r"\appendix"
GA = r"\subsection*{A guided account}"
FS = r"\subsection*{The formal statements}"
WL = r"\subsection*{The window law}"

SECS = [("1", r"\section{What this paper is about}", r"\section{One rising run"),
        ("2", r"\section{One rising run", r"\section{Blocks become states}"),
        ("3", r"\section{Blocks become states}", r"\section{The exact laws of one step}"),
        ("4", r"\section{The exact laws of one step}", r"\section{Cycles: what counting"),
        ("5", r"\section{Cycles: what counting", r"\section{The fair-coin hypothesis}"),
        ("6", r"\section{The fair-coin hypothesis}", r"\section{What remains open}"),
        ("7", r"\section{What remains open}", r"\section{Credit and provenance}"),
        ("8", r"\section{Credit and provenance}", APPX)]
sec = {}
for tag, a, b in SECS:
    sec[tag] = between(r6, a, b)
    sec["old" + tag] = between(r5, a, b)
abs6 = between(r6, r"\begin{abstract}", r"\end{abstract}")
abs5 = between(r5, r"\begin{abstract}", r"\end{abstract}")
symbols6 = between(r6, r"\section*{Symbols at a glance}", r"\section{What this paper is about}")


def guided(t):
    iC = t.index(r"\section{The exact laws: statements and proofs}")
    iD = t.index(r"\section{Cycles: the apparatus and the proofs}")
    iE = t.index(r"\section{The equidistribution hypothesis in full}")
    return (t[t.index(GA, iC):t.index(FS, iC)], t[t.index(GA, iD):t.index(FS, iD)],
            t[t.index(GA, iE):t.index(WL, iE)])


gC, gD, gE = guided(r6)
gC5, gD5, gE5 = guided(r5)

say("paper1_v4_readable6_check.py -- readability round 6 (final polish) scope check")
say(f"new = {NEW} (round 6), old = {OLD} (round 5 on main); TeX {TEX}; ledger {LEDGER} at {NEW}")
say()

# ---------------------------------------------------------------------------------------------
say("PART A. The round-5 check's required fix and four optional notes")
FIX = (r"But, by an accounting stated as a heuristic and not proved (Heuristic~\ref{prop:budget}), each "
       r"decided step uses up binary digits of the starting number, and nothing restores them; this suggests "
       r"that no finite window of digits can decide an orbit's whole future without further input --- "
       r"statistical (Section~\ref{sec:aeh}) or about the structure of cycles (Section~\ref{sec:cycles}).")
check("required fix (A-9): section 4 'Why it matters' carries the fix verbatim", FIX in norm(sec["4"]))
check("required fix: the unhedged premise 'But each decided step uses up' is gone from the TeX",
      "But each decided step uses up" not in r6)
check("required fix: the hedge also reaches the premise in the order premise-after-label",
      norm(sec["4"]).index("stated as a heuristic and not proved") < norm(sec["4"]).index("each decided step uses up"))
check("optional (a): section 5 ties the closeness to size: 'and by less the larger the cycle's numbers are'",
      "only slightly larger than $3$ to the power $n$, and by less the larger the cycle's numbers are" in norm(sec["5"]))
check("optional (b): 'use only this closeness, through the cycle's size conditions (Appendix D)'",
      r"use only this closeness, through the cycle's size conditions (Appendix~\ref{app:cycles})" in norm(sec["5"]))
check("optional (c): 'passing examples only' in section 5; 'without that range' gone",
      "passing examples only" in sec["5"] and "without that range" not in r6)
check("optional (d): section 6's conjecture keeps the tolerance ('every finite pattern of letters and every tolerance')",
      "every finite pattern of letters and every tolerance" in norm(sec["6"])
      and "by more than the tolerance" in norm(sec["6"]))
check("further note: App C guided account names experiments/depth_law_reverify.py in its 63,000 sentence",
      r"$\w = 1$ included (\texttt{experiments/depth\_law\_reverify.py})" in gC and r"63{,}000" in gC)
check("further note: App D guided account 'Apply it to the staircases of part (i)'; 'Apply it to the staircase,' gone",
      "Apply it to the staircases of part (i), whose $\\gamma$ is at most about $5.14$ while their $n$" in gD
      and "Apply it to the staircase," not in r6)
check("the claims ledger is unchanged between 56d6b3b and 73d51d4 (the baseline is the same)", check_led_same)
say()

# ---------------------------------------------------------------------------------------------
say("PART B. Unchanged text and formal statements")
ENV = r"(?:theorem|proposition|lemma|corollary|definition|hypothesis|heuristic)"


def envs(t):
    return re.findall(r"\\begin\{" + ENV + r"\}.*?\\end\{" + ENV + r"\}", t, re.S)


e5, e6 = envs(r5), envs(r6)
check("19 formal statement environments, all identical to 56d6b3b",
      len(e6) == 19 and e5 == e6, f"{len(e5)} at {OLD}, {len(e6)} at {NEW}")
ts5 = between(r5, r"\section*{Technical summary}", r"\section{")
ts6 = between(r6, r"\section*{Technical summary}", r"\section{")
check("Technical summary identical", ts5 == ts6, f"{len(ts6)} chars")
vn5 = between(r5, r"\subsection*{Version note}", r"\section*{Symbols at a glance}")
vn6 = between(r6, r"\subsection*{Version note}", r"\section*{Symbols at a glance}")
check("Version note and Author's note identical", vn5 == vn6)
check("front matter before the abstract identical", r5[:r5.index(r"\begin{abstract}")] == r6[:r6.index(r"\begin{abstract}")])
la = r5[r5.index(APPX):].splitlines()
lb = r6[r6.index(APPX):].splitlines()
ch_old, ch_new = [], []
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes():
    if op != "equal":
        ch_old += [x for x in la[i1:i2] if x.strip()]
        ch_new += [x for x in lb[j1:j2] if x.strip()]
in_guided = all(any(l.strip() and l in g for g in (gC, gD, gE)) for l in ch_new)
check("from \\appendix on, exactly 3 non-blank lines differ, each inside a guided account (C, D, E)",
      len(ch_old) == 3 and len(ch_new) == 3 and in_guided, f"{len(ch_old)} old / {len(ch_new)} new")
for l in ch_new:
    say("        changed: " + l[:120] + " ...")
# word-level: the three appendix edits are exactly the declared ones
APP_EDITS = [
    (r"$\w = 1$ included, and the absorption", r"$\w = 1$ included (\texttt{experiments/depth\_law\_reverify.py}), and the absorption"),
    ("Apply it to the staircase, whose $\\gamma$ is at most about $5.14$ while its $n$",
     "Apply it to the staircases of part (i), whose $\\gamma$ is at most about $5.14$ while their $n$"),
    (r"Read each block as a \emph{letter}: the pair (entry depth, exit valuation).",
     r"Read each block as a \emph{letter}, written $m|s$: the block's entry depth and exit valuation (the bar keeps a letter from being mistaken for a state)."),
    (r"the letters are $(3,1)$, $(1,2)$, $(1,3)$, $(1,1)$.", r"the letters are $3|1$, $1|2$, $1|3$, $1|1$."),
    (r"the letter $(1,2)$ has chance", r"the letter $1|2$ has chance"),
]
app_old = norm(r5[r5.index(APPX):])
miss = [a for a, b in APP_EDITS if app_old.count(a) != 1]
for a, b in APP_EDITS:
    app_old = app_old.replace(a, b, 1)
check("appendices: 56d6b3b with exactly the 5 declared phrase edits equals 73d51d4", not miss and app_old == norm(r6[r6.index(APPX):]),
      f"missing {miss}")
k = r6.index(r"\begin{theorem}[depth closure]")
tam = r6[:k + 40] + ("X" if r6[k + 40] != "X" else "Y") + r6[k + 41:]
control("a one-character edit inside Theorem C.5 passes as unchanged", envs(tam) == e5)
say()

# ---------------------------------------------------------------------------------------------
say("PART C. Changed-sentence inventory (abstract, Symbols page, sections 1-8, guided accounts)")


def sents(t):
    t = re.sub(r"\\(begin|end)\{(itemize|enumerate|center|tabular)\}(\{[^}]*\})?", " ", t)
    t = t.replace("\\item", " \n").replace("\\paragraph", "\n").replace("\\\\", "\n")
    out = []
    for chunk in t.split("\n"):
        chunk = " ".join(chunk.split())
        if not chunk:
            continue
        for s in re.split(r"(?<=[.?!])\s+(?=[A-Z\\(`$])", chunk):
            s = s.strip()
            if s:
                out.append(s)
    return out


main6 = r6[r6.index(r"\begin{abstract}"):r6.index(APPX)] + gC + gD + gE
main5 = r5[r5.index(r"\begin{abstract}"):r5.index(APPX)] + gC5 + gD5 + gE5
old_set = set(sents(main5))
changed = [s for s in sents(main6) if s not in old_set]

# (id, key phrase unique to the sentence, rows, verdict) -- verdict in {same, SCOPE, nav}
INV = [
    ("AB-1", "(the sequence of numbers a start visits)", "C-Abs.1, C-2.3", "same"),
    ("AB-2", "with three numbers describing the step (Section~", "C-Abs.6, C-3.8", "same"),
    ("AB-3", "(how small the gap between the two powers is, compared with the larger one)", "C-Abs.11, C-4.cfg(a), N-19", "same"),
    ("AB-4", "they attain the optimum of Rozier's 1991 analysis", "C-Abs.13, C-4.thr.6, C-4.6.minimax, C-RW.17, N-7", "same"),
    ("AB-5", "Finally the paper states the `fair-coin' assumption", "C-Abs.15", "same"),
    ("AB-6", "record each block's (entry depth, exit valuation) pair", "C-Abs.15, C-5.1", "same"),
    ("AB-7", "The conjecture is that these pairs occur", "C-Abs.15, C-5.adm, C-5.1", "SCOPE"),
    ("SY-1", "$n$ & the sum of a cycle's entry depths", "C-4.setup", "same"),
    ("SY-2", "$K$ & a cycle's total number of halvings: $n$ plus", "C-4.setup", "same"),
    ("SY-3", r"$\gamma$ & a cycle's closeness measure", "C-4.cfg(a)", "same"),
    ("SY-4", "$m|s$ & a \\emph{letter}", "C-5.1", "same"),
    ("SY-5", "Three words are used as names", "C-3.1, C-3.3(a), C-3.4", "same"),
    ("I-1", "The paper proves that size arguments go no farther", "C-Int.2, C-Abs.10", "same"),
    ("I-2", "It also proves the same when every number in the cycle", "C-Int.2, C-Abs.12", "same"),
    ("I-3", "the trivial cycle $1, 4, 2, 1$ corresponds to the state of $1$", "C-2.3(a)(b)(c)", "same"),
    ("I-nav", "(This is the exit rule of Section~", "C-3.3 (pointer)", "nav"),
    ("I-4", "longer than those digits can determine", "C-3.8, C-Int.8", "same"),
    ("I-5", "(by proof from $16$ on, by computer check for $3$ to $15$; for $2$ and $4$ blocks, examples only)", "C-4.6(i)a-c, N-4, N-19", "same"),
    ("I-6", "there it reaches the optimum of Rozier's analysis", "C-Int.9, C-4.thr.6, C-RW.17, N-7", "same"),
    ("I-7", "It does not prove that no fixed, finite number", "N-1", "same"),
    ("I-8", "That is the paper's organizing heuristic", "N-1, C-3.9(e)", "same"),
    ("I-9", "with no claim about their closeness measure", "C-4.6(i)c, N-19", "same"),
    ("I-10", "drift downward or shrink follows from it", "N-11, C-5.piledger", "same"),
    ("I-11", "that almost every orbit falls below its start (`descent')", "C-5.descent, N-13, C-RW.2", "same"),
    ("I-12", "whose blocks it allows to stray from the coin pattern", "C-5.exc, N-15", "same"),
    ("B-1", "(a number $2$ more than a multiple of $4$ is twice an odd number)", "C-2.2(i)", "same"),
    ("B-2", "halvings, not counting its first", "C-2.1", "same"),
    ("R-1", "one more than the current number is $2$ times $\\w$ times $3$ to the power $d - 1$.", "C-2.2(i)", "same"),
    ("R-2", "The reason: $x+1$ had $a$ factors of $3$", "C-2.2(i)", "same"),
    ("R-3", "a block of one odd number ($m = 1$)", "C-2.1, C-2.2 (worked)", "same"),
    ("R-4", "again a block of one odd number", "C-2.1, C-2.2 (worked)", "same"),
    ("R-5", "since $1 + 1 = 2$ gives $m = 1$", "C-2.3(a), C-2.2(iii)", "same"),
    ("A-1", "(which is $1$, $3$, $5$ or $7$, since $\\w$ is odd)", "C-3.3", "same"),
    ("A-2", "called the \\emph{lifting} kinds", "C-3.3(a), C-3.1", "same"),
    ("A-3", "But, by an accounting stated as a heuristic and not proved", "C-3.9(a)(c)(e), C-Int.13, N-1", "same"),
    ("A-4", "and $s = 2$ is even, so the next state gains", "C-3.3(b), C-3.4", "same"),
    ("C-1", "($n$ is the sum of the blocks' entry depths)", "C-4.setup", "same"),
    ("C-2", "and by less the larger the cycle's numbers are", "C-4.1(a), C-4.2", "same"),
    ("C-3", "The closeness is measured by a number $\\gamma$", "C-4.cfg(a)", "same"),
    ("C-4", "use only this closeness, through the cycle's size conditions", "C-4.5(b), C-4.1(c)", "same"),
    ("C-5", "Classically they give a bound, the uniform \\emph{trim}", "C-4.5(a), C-Abs.9, C-RW.14", "same"),
    ("C-6", "(that there are only finitely many was first proved by Brox)", "C-4.5(c)(d), C-RW.15, C-4.5.cr", "SCOPE"),
    ("C-nav", "The paper does three things here.", "-", "nav"),
    ("C-7", "It rederives that bound by another route.", "C-4.5.cr, P-16", "same"),
    ("C-8", "It rederives the classical facts that there are no cycles", "C-4.4, N-2", "same"),
    ("C-9", "And it proves that the exponential weakening cannot be avoided", "C-Abs.10, C-4.6(i)d", "same"),
    ("C-10", "lists of block depths and exit valuations shaped like a cycle", "C-4.cfg(a), C-Abs.11", "same"),
    ("C-11", "They pass every size test, for every choice of starting block", "C-4.6(i)a-c, C-4.6(iii)a, N-4", "same"),
    ("C-12", "every staircase checked fails at least one of these divisibility conditions", "C-4.ver(c), C-4.6(iv), N-9", "same"),
    ("C-13", "Then $n = 94$, the sum of the entry depths", "C-4.6(iv)", "same"),
    ("C-14", "it is not a member of the family of Theorem~", "C-4.6(iv), C-4.6(i)a", "same"),
    ("H-1", "Read each block as a \\emph{letter}, written $m|s$: its entry depth", "C-5.1", "same"),
    ("H-2", "treats the two parts as independent coin-toss counts", "C-5.1, C-Int.16", "same"),
    ("H-3", "The paper states this as a precise conjecture (Hypothesis~", "C-Abs.15", "same"),
    ("H-4", "Draw a large odd starting value at random", "C-5.1", "same"),
    ("H-5", "the \\emph{horizon}: the record stops", "C-5.1 (T_N)", "same"),
    ("H-6", "the \\emph{budget}: a block's letter is recorded only while", "C-5.1 (Lambda_N)", "same"),
    ("H-7", "Call a choice of the two multiples \\emph{admissible}", "C-5.adm, C-5.cons", "SCOPE"),
    ("H-8", "The conjecture: for every admissible choice", "C-5.1", "same"),
    ("H-9", "because the start's lowest binary digits fix its first blocks exactly", "C-5.base, C-5.thm", "same"),
    ("H-10", "the part proved without assuming anything", "C-Abs.17, C-5.thm", "same"),
    ("H-11", "The running example's blocks $7, 11, 17$", "worked (C-2.1)", "same"),
    ("H-12", "Under the model the letter $1|2$ has chance", "C-5.1", "same"),
    ("O-nav", "Three directions are open:", "C-D.3 (heading)", "nav"),
    ("O-1", "\\emph{Going beyond size for cycles.}", "C-D.3, C-4.6.close", "same"),
    ("O-2", "One candidate: a cycle's anchors are rigid", "C-D.3", "same"),
    ("O-3", "\\emph{Following windows step by step.}", "C-D.3", "same"),
    ("O-4", "\\emph{The anchors' digits.}", "C-D.3, P-29, C-D.1", "same"),
    ("P-nav", "results about almost all starting values (`density results')", "C-RW.1-11 (pointer)", "nav"),
    ("P-1", "It uses three terms for objects of Sections~", "C-RW.22", "same"),
    ("P-2", "In Williams's picture a row is a pair", "C-RW.22", "same"),
    ("P-3", "When a trajectory leaves a row, Section~", "C-RW.23", "same"),
    ("P-4", "They give no law for the skeleton $\\lambda$ of that row", "C-RW.23", "same"),
    ("GC-1", "(\\texttt{experiments/depth\\_law\\_reverify.py})", "C-3.6, C-3.5(a)", "same"),
    ("GD-1", "Apply it to the staircases of part (i)", "C-4.6(i)a, C-4.6(i)d", "same"),
    ("GE-1", "written $m|s$: the block's entry depth and exit valuation", "C-5.1", "same"),
    ("GE-2", "In the running example the letters are $3|1$", "worked (C-2.1)", "same"),
    ("GE-3", "for example, the letter $1|2$ has chance", "C-5.1", "same"),
]
matched = {e[0]: [] for e in INV}
unmatched = []
for s in changed:
    hits = [e[0] for e in INV if e[1] in s]
    if len(hits) == 1:
        matched[hits[0]].append(s)
    else:
        unmatched.append((s, hits))
check(f"every changed sentence ({len(changed)}) matches exactly one inventory entry",
      not unmatched, f"{len(unmatched)} unmatched/ambiguous: {[u[0][:60] + ' ' + str(u[1]) for u in unmatched][:4]}")
check("every inventory entry matches exactly one changed sentence",
      all(len(v) == 1 for v in matched.values()), str([k for k, v in matched.items() if len(v) != 1]))
cnt = {"same": 0, "SCOPE": 0, "nav": 0}
for e in INV:
    cnt[e[3]] += 1
say(f"  inventory: {len(INV)} changed sentences; {cnt['nav']} navigation (not counted); "
    f"{cnt['same'] + cnt['SCOPE']} counted: {cnt['same']} same, {cnt['SCOPE']} scope changed, 0 unsupported")
for e in INV:
    if e[3] != "same":
        say(f"     {e[0]:6s} {e[3]:5s} rows {e[2]}: {matched[e[0]][0][:150] if matched[e[0]] else '?'}")
check("the scope-change verdicts are exactly AB-7, C-6, H-7",
      [e[0] for e in INV if e[3] == "SCOPE"] == ["AB-7", "C-6", "H-7"])
# ledger rows named in the inventory exist in the ledger
ids = set(re.findall(r"\| ((?:C|P|N)-[A-Za-z0-9.()+-]+?)(?: Δ| \+)? \|", led))
named = set()
for e in INV:
    for tok in re.findall(r"(?:C|P|N)-[A-Za-z0-9.]+", e[2]):
        named.add(tok.rstrip("."))
base_ids = {i.split("(")[0] for i in ids} | ids
missing_rows = sorted(t for t in named if t not in base_ids and not any(i.startswith(t) for i in ids))
check("every ledger row named in the inventory exists in the ledger at 73d51d4", not missing_rows, str(missing_rows))
# the ledger and record facts behind the three scope changes
check("ledger C-5.adm: protection quantifies 'all but a vanishing density of starts'",
      "`τ` is protected when all but a vanishing density of starts keep every in-budget exit above any `X_N`" in led)
check("ledger C-RW.15 says 'Brox proved finiteness for each `p`' (no priority word)",
      "| C-RW.15 | — | Brox proved finiteness for each `p`. |" in led)
sweep = show(NEW, "briefs/ceiling-ccchallenge-sweep-findings.md")
check("record: Rozier 1991, p. 8, Theoreme -- finitely many cycles for each number n of odd/even alternations (9 years before Brox)",
      "Pour chaque entier n, il n'y a qu'un nombre fini de cycles alternant n séquences d'entiers impairs" in sweep
      and "Brox 2000 by 9" in sweep)
check("App D guided account itself dates Rozier's bound 1991 and Brox's finiteness 2000",
      "In 1991 Rozier bounded" in gD and "In 2000 Brox proved that only finitely many cycles" in gD)
# the Symbols page's claims about where symbols are used
TABLE_SYMS = [r"$x", r"$T", r"$m", r"$s", r"$a", r"\w", r"$d", r"$F", r"$p", r"$n", r"$K", r"\gamma", r"\lambda", r"$k"]
s1_abs = abs6 + sec["1"]
check("Symbols page: 'Section 1 and the abstract use none of them' still holds",
      not any(tok in s1_abs for tok in TABLE_SYMS))
check("Symbols page parenthesis still lists gamma among appendix-only symbols although gamma is now in the table and in section 5 (optional note)",
      r"among them $q$, $\gamma$, $X_0$" in symbols6 and r"$\gamma$ &" in symbols6 and r"\gamma" in sec["5"])
say()

# ---------------------------------------------------------------------------------------------
say("PART D. Worked numbers, fresh")


def v2(x):
    x = abs(x)
    return (x & -x).bit_length() - 1


def v3_(x):
    c = 0
    while x % 3 == 0:
        x //= 3
        c += 1
    return c


def state_of(x):
    u = x + 1
    m = v2(u)
    r = u >> m
    a = v3_(r)
    return (r // 3 ** a, m + a), m, a


def F(w, d):
    A = 3 ** d * w - 1
    s = v2(A)
    e = A >> s
    st, m2, a2 = state_of(e)
    return s, e, st, m2, a2


# section 2
check("section 2: every number 2 more than a multiple of 4 (below 10^5) is twice an odd number",
      all((4 * j + 2) // 2 % 2 == 1 for j in range(25000)))
check("section 2: x = 7: 3*8 = 24 is a multiple of 4, 22 = 24 - 2 halves once, to 11",
      24 % 4 == 0 and v2(22) == 1 and 22 // 2 == 11)
# section 3: x + 1 had a factors of 3; each of m - 1 rising steps adds one; d - 1 in all
bad = 0
for x in range(1, 200001, 2):
    (w, d), m, a = state_of(x)
    y = x
    for _ in range(m - 1):
        y = (3 * y + 1) // 2
    if y + 1 != 2 * w * 3 ** (d - 1) or a + (m - 1) != d - 1:
        bad += 1
check("section 3: after the m - 1 rising steps, y + 1 = 2 * w * 3^(d-1), and a + (m - 1) = d - 1 (odd x < 200001)",
      bad == 0, f"{bad} mismatches")
check("section 3: 13 + 1 = 14 = 2*7, state (7,1), a block of one odd number (m = 1); 40 halves three times (s = 2) to 5",
      state_of(13) == ((7, 1), 1, 0) and F(7, 1)[:2] == (2, 5) and v2(40) == 3)
check("section 3: 5 + 1 = 6 = 2*3, state (1,2), again m = 1; 16 halves four times (s = 3) to 1",
      state_of(5) == ((1, 2), 1, 1) and F(1, 2)[:2] == (3, 1) and v2(16) == 4)
reps11 = [2 ** (1 - a) * 3 ** a * 1 - 1 for a in range(0, 1)]
check("section 3: the only number with state (1,1) is 1 (a depth-1 state has exactly one representative); F(1,1) = (1,1)",
      reps11 == [1] and [x for x in range(1, 100001, 2) if state_of(x)[0] == (1, 1)] == [1] and F(1, 1)[2] == (1, 1))
# section 4
check("section 4: odd w leaves remainder 1, 3, 5 or 7 on division by 8", {w % 8 for w in range(1, 1000, 2)} == {1, 3, 5, 7})
bad = sum(1 for w in range(1, 2000, 2) if w % 3 for d in range(1, 30)
          if ((3 ** d * w) % 8 == 1) != ((w % 8 == 1 and d % 2 == 0) or (w % 8 == 3 and d % 2 == 1)))
check("section 4: lifting in words (w = 1 mod 8 with d even, or 3 mod 8 with d odd) is exactly 3^d w = 1 mod 8",
      bad == 0, f"{bad} mismatches")
s71, e71, nxt71, m71, a71 = F(7, 1)
check("section 4: (7,1) is of kind (7, odd), s = 2, even; next state (1,2) gains a factor of 3 (a = 1); 6 = 2*3",
      7 % 8 == 7 and s71 == 2 and nxt71 == (1, 2) and a71 == 1 and 5 + 1 == 2 * 3)
# section 5
mm = [4, 7, 9, 15, 23, 35, 1]
ss = [1, 1, 1, 1, 1, 1, 49]
p, n, K = len(mm), sum(mm), sum(mm) + sum(ss)
q = 2 ** K - 3 ** n
gamma = K - math.log2(q)
check("section 5: n = 94 is the sum of the entry depths; exit valuations total 55; K = 94 + 55 = 149",
      n == 94 and sum(ss) == 55 and K == 149)
check("section 5: gamma in words -- the gap 2^K - 3^n equals 2^K divided by 2^gamma (relative error < 1e-12)",
      abs(2 ** (K - gamma) / q - 1) < 1e-12, f"gamma = {gamma:.6f}")
check("section 5: gamma = 6.74 (2 decimals), outside part (i)'s range [3.683012, 5.140212]",
      round(gamma, 2) == 6.74 and not (3.683012 <= gamma <= 5.140212))
gam_tr = 2 - math.log2(2 ** 2 - 3)
check("gloss sanity: larger gamma = closer approach (trivial cycle K = 2, n = 1: gap 1 = 4 / 2^2, gamma = 2 < 6.74)",
      gam_tr == 2.0 and gam_tr < gamma)


def R_rot(ms, svals, r):
    m_ = ms[r:] + ms[:r]
    s_ = svals[r:] + svals[:r]
    P = len(m_)
    sig = [s_[j] + m_[(j + 1) % P] for j in range(P)]
    return sum(3 ** sum(m_[t + 1:]) * 2 ** sum(sig[:t]) * (2 ** s_[t] - 1) for t in range(P))


Rs = [R_rot(mm, ss, r) for r in range(p)]
check("section 5: all seven size conditions q <= R_r hold", all(q <= R for R in Rs))
check("section 5: 'fails at least one of these divisibility conditions' -- q | R_r at 0 of 7 rotations",
      sum(R % q == 0 for R in Rs) == 0)
Lam = K * math.log(2) - n * math.log(3)
rhin = math.exp(-13.3 * (0.46057 + math.log(n)))
check("section 5: Rhin's limit (K log 2 - n log 3 > exp(-13.3(0.46057 + log n))) is respected by the staircase",
      Lam > rhin, f"Lambda = {Lam:.4e}, Rhin bound = {rhin:.4e}")
check("section 5: Lambda = -log(1 - 2^-gamma) > 2^-gamma (closeness in the paper's two forms)",
      abs(Lam + math.log(1 - 2 ** -gamma)) < 1e-12 and Lam > 2 ** -gamma)
# section 6: letters of the orbit of 7, by direct Syracuse steps (independent of the state formulas)


def letters_direct(x, nblocks=None, max_halvings=None):
    """Blocks by direct odd-to-odd steps: a block = maximal run of steps with v2(3y+1) = 1, then one with v >= 2.
    Letter = (m, s): m = number of odd numbers in the block, s = v - 1 of the last step.
    Returns list of (m, s, cumulative halvings after the block)."""
    out = []
    y, S = x, 0
    m = 0
    while True:
        v = v2(3 * y + 1)
        y = (3 * y + 1) >> v
        m += 1
        S += v
        if v >= 2:
            out.append((m, v - 1, S))
            m = 0
            if nblocks is not None and len(out) >= nblocks:
                return out
            if max_halvings is not None and S > max_halvings:
                return out


L7 = [(m, s) for m, s, _ in letters_direct(7, nblocks=6)]
check("section 6 / App E: letters of the orbit of 7 are 3|1, 1|2, 1|3, 1|1 (then 1|1 forever)",
      L7 == [(3, 1), (1, 2), (1, 3), (1, 1), (1, 1), (1, 1)], str(L7))
check("section 6: the blocks are 7, 11, 17; then 13; then 5; then 1",
      [7, 11, 17] == [7, (3 * 7 + 1) // 2, (3 * 11 + 1) // 2] and F(1, 3)[1] == 13 and F(7, 1)[1] == 5 and F(1, 2)[1] == 1)
check("section 6: P(1|2) = 1/2 * 1/4 = 1/8", Fraction(1, 2) * Fraction(1, 4) == Fraction(1, 8))
# base-case reason: the coding fact (one residue class mod 2^(S+1)) and its coin share, fresh
JB = 20
SMAX = 15                     # patterns with S + 1 <= 16
classes = {}
for x in range(1, 2 ** JB, 2):
    blocks = letters_direct(x, max_halvings=SMAX)
    for k, (m, s, S) in enumerate(blocks):
        if S > SMAX:
            break
        key = tuple((mm_, ss_) for mm_, ss_, _ in blocks[:k + 1])
        rec = classes.setdefault(key, [S, set(), 0])
        rec[1].add(x % 2 ** (S + 1))
        rec[2] += 1
one_class = all(len(r[1]) == 1 for r in classes.values())
exact_count = all(r[2] == 2 ** (JB - r[0] - 1) for r in classes.values())
coin = all(Fraction(r[2], 2 ** (JB - 1)) == Fraction(1, 2 ** r[0]) == Fraction(1, 2 ** sum(a + b for a, b in w))
           for w, r in classes.items())
check("base case: each pattern of first blocks (counting the start's own) with S + 1 <= 16 is ONE residue class mod 2^(S+1)",
      one_class, f"{len(classes)} patterns over odd x < 2^{JB}")
check("base case: each such class occurs exactly 2^(20-S-1) times below 2^20, i.e. in its coin share 2^-S = prod 2^-(m+s)",
      exact_count and coin)
rng = random.Random(6)
ok_win = True
J = 16
for _ in range(3):
    off = rng.randrange(10 ** 9, 10 ** 10)
    cnts = {}
    for x in range(off, off + 2 ** J):
        if x % 2:
            blocks = letters_direct(x, max_halvings=J - 2)
            for k, (m, s, S) in enumerate(blocks):
                if S + 1 > J:
                    break
                w = tuple((a, b) for a, b, _ in blocks[:k + 1])
                cnts[w] = cnts.get(w, 0) + 1
    ok_win &= all(c == 2 ** (J - 1 - sum(a + b for a, b in w)) for w, c in cnts.items())
check("base case: in 3 random windows of 2^16 consecutive integers, every pattern with S + 1 <= 16 occurs exactly in its coin share",
      ok_win)
# admissibility: the protected clause needs its 'all but a vanishing share' quantifier
b = 40
xw = (2 ** 42 - 1) // 3
blk = letters_direct(xw, nblocks=2)
tau = Fraction(11, 10)
budget = math.ceil(tau * b)
check("admissibility witness: x = (2^42 - 1)/3 is an odd start in [2^40, 2^41)", xw % 2 == 1 and 2 ** 40 <= xw < 2 ** 41)
check("admissibility witness: its first block ends at 1 after 42 halvings, inside the budget ceil(1.1 * 40) = 44 halvings",
      blk[0] == (1, 41, 42) and (3 * xw + 1) == 2 ** 42 and budget == 44 and blk[0][2] < budget)
check("so 'the budget keeps the orbit away from the small numbers' read for every start fails at tau = 1.1 "
      "(while every tau < 4.8188... is protected for all but a vanishing share, C-5.prot)",
      1 / (1 - math.log2(math.sqrt(3))) > 4.8188 and float(tau) < 4.8188)
check("consistency in words: 'the record fits inside the budget on the model's average (four halvings per block)' "
      "= 4 * theta < tau; under the coin model E[m] = E[s] = 2",
      sum(Fraction(j, 2 ** j) for j in range(1, 200)) > Fraction(2) - Fraction(1, 2 ** 190))
# minimax gloss: best worst case over real block depths
L = math.log2(3)
ok_mm = True
detail = []
for P in range(3, 9):
    nn = 1000.0
    kap = (L - 1) / (L ** P - 1)
    rho = kap * nn
    ext = [rho * L ** j for j in range(P)]

    def rho0(ms):
        T, best = 0.0, -1e300
        for mj in ms:
            best = max(best, mj - (L - 1) * T)
            T += mj
        return best

    ok_mm &= abs(sum(ext) - nn) < 1e-9 and abs(rho0(ext) - rho) < 1e-9
    worst = min(rho0([nn * g / sum(gs) for g in gs]) for gs in
                ([rng.expovariate(1.0) for _ in range(P)] for _ in range(3000)))
    ok_mm &= worst >= rho - 1e-9
    detail.append(f"p={P}: kappa_p n = {rho:.4f}, min over 3000 random real tuples = {worst:.4f}")
check("minimax gloss: over real block depths of sum n, the best worst case max_j (m_j - (L-1)(m_0+...+m_(j-1))) is kappa_p n, "
      "attained by the geometric tuple of ratio L (p = 3..8, n = 1000)", ok_mm, "; ".join(detail[:2]))
# section 8: the laws give the depth k of the row entered (d+ = m+ + a+ from Lemma C.4 and Theorem C.5)
KB = 96
MODB = 1 << KB


def N2(u):
    """t mod 2^KB with 9^t = u^-1 in Z_2 (u = 1 mod 8), by bit lifting modulo 2^(KB+3)."""
    E = KB + 3
    mod = 1 << E
    target = pow(u % mod, -1, mod)
    assert target % 8 == 1
    t = 0
    for i in range(KB):
        mm2 = 1 << (i + 4)
        if pow(9, t, mm2) != target % mm2:
            t += 1 << i
    return t


def h(s):
    return v3_(2 ** s - 1)


bad = tot = 0
for w in range(1, 400, 2):
    if w % 3 == 0:
        continue
    Mw = N2(w * w)
    for d in range(1, 41):
        s_true, e, (w2, d2), m2, a2 = F(w, d)
        lifting = (w % 8 == 1 and d % 2 == 0) or (w % 8 == 3 and d % 2 == 1)
        if lifting:
            s = 2 + v2((d - Mw) % MODB)
            nn_ = d // 2
            eps = (nn_ - N2(w)) if d % 2 == 0 else (nn_ - N2(3 * w))
            delta = N2((1 - 2 ** s) % (1 << (KB + 8)))
            mplus = 3 - s + v2((eps + delta) % MODB)
        else:
            s = {(3, 0): 1, (5, 0): 2, (7, 0): 1, (1, 1): 1, (5, 1): 1, (7, 1): 2}[(w % 8, d % 2)]
            mplus = 1 + v2((d - Mw) % MODB) if s == 1 else v2((d - 1 - Mw) % MODB)
        if s % 2:
            aplus = 0
        elif d != h(s):
            aplus = min(d, h(s))
        else:
            aplus = d + v3_(w + (2 ** s - 1) // 3 ** d)
        tot += 1
        if (s, mplus, aplus, mplus + aplus) != (s_true, m2, a2, d2):
            bad += 1
check("section 8: Section 4's laws give the exit valuation s, the entry position (m+, a+) and so the depth k = d+ = m+ + a+ "
      "of the row entered (Theorem C.3, Theorem C.5, Lemma C.4 against F)", bad == 0 and tot > 5000,
      f"{tot} states w < 400, d <= 40; {bad} mismatches")
pairs = {}
for w in range(1, 400, 2):
    if w % 3:
        for d in range(1, 41):
            s_, e_, (w2, d2), m2, a2 = F(w, d)
            pairs.setdefault((s_, m2, a2, d2), set()).add(w2)
check("section 8: the same (s, m+, a+, d+) occurs with different skeletons w+ (the laws do not fix the skeleton)",
      any(len(v) > 1 for v in pairs.values()))
say()

# ---------------------------------------------------------------------------------------------
say("PART E. Negative controls")
r0 = classes[((1, 1),)]
control("the pattern 1|1 is the FULL residue class mod 2^S (rather than one class mod 2^(S+1))",
        r0[2] == 2 ** (JB - r0[0]))
control("letters of 7 with 1|2 replaced by 2|1", [(3, 1), (2, 1), (1, 3), (1, 1)] == L7[:4])
control("K = 148 for the staircase", K == 148)
control("q | R_r at some rotation of the staircase", any(R % q == 0 for R in Rs))
control("protection for every start at tau = 1.1 (no start reaches 1 inside the budget)", blk[0][2] >= budget)
P = 5
kap = (L - 1) / (L ** P - 1)
ext2 = [2.0 ** j for j in range(P)]
ext2 = [1000.0 * g / sum(ext2) for g in ext2]
T, best = 0.0, -1e300
for mj in ext2:
    best = max(best, mj - (L - 1) * T)
    T += mj
control("the ratio-2 geometric tuple also attains the minimax value kappa_p n (p = 5)", abs(best - kap * 1000.0) < 1e-6)
bad_c = 0
for w in range(1, 200, 2):
    if w % 3:
        for d in range(1, 21):
            s_, e_, (w2, d2), m2, a2 = F(w, d)
            if d2 != m2:
                bad_c += 1
control("the depth of the row entered is the entry position m+ alone (absorption dropped)", bad_c == 0, f"{bad_c} mismatches")
control("gamma of the staircase lies inside part (i)'s range", 3.683012 <= gamma <= 5.140212)
say()

say(f"TOTAL: {n_pass} checks passed, {n_fail} failed; controls {n_ctrl_ok} rejected, {n_ctrl_bad} not rejected")
verdict = n_fail == 0 and n_ctrl_bad == 0
say("VERDICT: " + ("PASS" if verdict else "FAIL"))
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines_out) + "\n")
print("\n".join(lines_out))
sys.exit(0 if verdict else 1)
