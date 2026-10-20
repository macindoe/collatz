#!/usr/bin/env python3
"""
paper1_v4_readable5_check.py -- scope-drift check of readability round 5 (option A) of paper 1 v4
(paper/collatz-reduced-v4.tex at 678ebff against round 4 at 190b6af).

Supports: briefs/paper1-v4-readable-5-check-findings.md (sections 1-5).

Written for this check from the paper's text alone (main text; Definition C.1; Theorem C.5;
Proposition D.1).  It imports nothing from the repository and reuses no code from experiments/.
Exact integers and Fractions for every integer decision.  The TeX, the claims ledger, v3's TeX and
the committed output of experiments/depth_law_reverify.py are read from git at pinned commits, so
the result does not depend on the checkout.

Parts:
  A. The round-4 check's four fixes (98665e3 findings section 4) and cold read 3's four
     inconsistencies (briefs/paper1-v4-coldread-3.md; as recorded in
     briefs/paper1-v4-readable-findings.md section 7e): new wording present, old wording gone.
  B. Unchanged text: abstract, Version note, Author's note identical; everything from \\appendix on,
     with the three guided accounts removed, differs from round 4 in exactly five declared lines
     (three appendix lead-ins, Remark C.6, Appendix G's first row); a one-character edit is caught.
  C. Moved text: round 4's sections 4, 5, 6 against the guided accounts opening Appendices C, D, E,
     word by word; every difference must be in the declared list below, and each is printed.
  D. The entry-depth verification sentence: 63,000 states, omega = 1 included, in all three places;
     the script named; the committed output of depth_law_reverify.py says so; and a fresh check of
     Theorem C.5 on the 63 states with omega = 1.
  E. Worked numbers of the new sections 4-6, recomputed: the (7,1) factor-of-3 example and the (1,2)
     valuation example; the anchor rule on lifting states; the seven-block staircase (n, K, gamma,
     the seven size conditions and the divisibility conditions of Proposition D.1, cross-checked
     against the rational fixed point of the block map); the letters of the orbit of 7; P = 1/8;
     the 1/3 gain rate.
  F. Negative controls: each must be rejected by the same code.

Scope (README stopping rules): no cycle search.  Size and divisibility are evaluated only on the
paper's own printed seven-block configuration and on the trivial cycle, as a check of printed
sentences.

Reproduce (one command; deterministic; a few seconds):

    python experiments/paper1_v4_readable5_check.py

It writes experiments/paper1_v4_readable5_check_output.txt (UTF-8, no BOM) and exits 0 iff every
check passes and every control is rejected.
"""

import difflib
import math
import os
import re
import subprocess
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "paper1_v4_readable5_check_output.txt")

NEW = "678ebff"   # round 5 (merged, with the 63,000 restatement)
OLD = "190b6af"   # round 4
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


r4 = show(OLD, TEX)
r5 = show(NEW, TEX)
led5 = show(NEW, LEDGER)
v3 = show(NEW, "paper/collatz-reduced-v3.tex")
dlr_out = show(NEW, "experiments/depth_law_reverify_output.txt")

APPX = r"\appendix"
GA = r"\subsection*{A guided account}"
FS = r"\subsection*{The formal statements}"
WL = r"\subsection*{The window law}"

main4 = between(r4, r"\section*{Symbols at a glance}", APPX)
main5 = between(r5, r"\section*{Symbols at a glance}", APPX)
sec = {}
for tag, a, b in [("1", r"\section{What this paper is about}", r"\section{One rising run"),
                  ("4", r"\section{The exact laws of one step}", r"\section{Cycles: what counting"),
                  ("5", r"\section{Cycles: what counting", r"\section{The fair-coin hypothesis}"),
                  ("6", r"\section{The fair-coin hypothesis}", r"\section{What remains open}"),
                  ("7", r"\section{What remains open}", r"\section{Credit and provenance}"),
                  ("8", r"\section{Credit and provenance}", APPX)]:
    sec[tag] = between(r5, a, b)
    sec["r4_" + tag] = between(r4, a, b)
symbols5 = between(r5, r"\section*{Symbols at a glance}", r"\section{What this paper is about}")
iC = r5.index(r"\section{The exact laws: statements and proofs}")
iD = r5.index(r"\section{Cycles: the apparatus and the proofs}")
iE = r5.index(r"\section{The equidistribution hypothesis in full}")
gC = r5[r5.index(GA, iC):r5.index(FS, iC)]
gD = r5[r5.index(GA, iD):r5.index(FS, iD)]
gE = r5[r5.index(GA, iE):r5.index(WL, iE)]
assert iC < iD < iE and r5.index(GA, iC) < iD and r5.index(GA, iD) < iE

say("paper1_v4_readable5_check.py -- readability round 5 (option A) scope check")
say(f"new = {NEW} (round 5), old = {OLD} (round 4); TeX {TEX}; ledger {LEDGER} at {NEW}")
say()

# ---------------------------------------------------------------------------------------------
say("PART A. The round-4 check's four fixes and cold read 3's four inconsistencies")
# Round-4 fix 1 (section 1, not-claimed bullet 5)
check("R4-1 section 1: 'that is not the same as saying that almost no orbits misbehave'",
      "that is not the same as saying that almost no orbits misbehave" in sec["1"])
check("R4-1 old 'weaker than saying' gone from the whole TeX", "weaker than saying" not in r5)
# Round-4 fix 2 (older and broader attached to 2-adic logarithms)
fix2 = (r"the anchors of Section~\ref{sec:anchor} --- in the usual terms, digits of $2$-adic "
        r"logarithms of whole numbers (Appendix~\ref{app:laws} names them precisely) --- and "
        r"questions of that kind are older and broader than the Collatz problem")
check("R4-2 App E guided account: the round-4 fix wording verbatim", fix2 in gE)
check("R4-2 old 'and that question is older' gone", "and that question is older" not in r5)
check("R4-2 section 7: 'digits of $2$-adic logarithms of whole numbers, of which the anchors are instances'",
      r"digits of $2$-adic logarithms of whole numbers, of which the anchors are instances" in sec["7"])
ob = [m.start() for m in re.finditer("older and broader", r5)]
check("R4-2 'older and broader' twice (App E guided account; App E formal text), both after '2-adic logarithms', none in sections 1-8",
      len(ob) == 2 and all("logarithms" in r5[i - 160:i] for i in ob) and "older and broader" not in main5)
# Round-4 fix 3 (Lemme 4 comparand)
fix3 = r"is larger throughout this range than $2$ to the power ($n$ times the shrinking factor)"
check("R4-3 App D guided account: Lemme 4 comparand restored", fix3 in gD)
check("R4-3 the comparand-less form gone", "is larger throughout this range." not in r5)
# Round-4 fix 4 (calibration clause)
check("R4-4 ', which the sharper control set aside' gone from the whole TeX",
      "sharper control set aside" not in r5)
check("R4-4 item (2) now ends 'both artifacts of including small starting values;'",
      "both artifacts of including small starting values;" in gE)
# Cold read 3 (a): halvings beyond the first
check("CR3-a section 1 (ii): 'the number of halvings, beyond the first, that end each block'",
      "the number of halvings, beyond the first, that end each block" in sec["1"])
check("CR3-a section 4: 'how many halvings, beyond the first, end the block'",
      "how many halvings, beyond the first, end the block" in sec["4"])
check("CR3-a Symbols page row for s: 'how many halvings, beyond the first, end the block'",
      "how many halvings, beyond the first, end the block" in symbols5)
check("CR3-a old 'the number of halvings that end each block' gone",
      "the number of halvings that end each block" not in r5)
# Cold read 3 (b): the p = 7 staircase marked as v3's instance outside part (i)'s bracket
check("CR3-b section 5 marks the instance as v3's, outside 3.68-5.14, with 6.74",
      "This instance is v3's" in sec["5"] and "$3.68$ and $5.14$" in sec["5"] and "$6.74$" in sec["5"])
check("CR3-b App D guided account marks it the same way",
      "This seven-block instance is v3's" in gD and "$3.68$ and $5.14$" in gD)
check("CR3-b v3's TeX carries the instance m = (4,7,9,15,23,35,1) with gamma = 6.74",
      "m = (4,7,9,15,23,35,1)" in v3 and r"\gamma = 6.74" in v3)
check("CR3-b ledger C-4.6(i)a bracket is 3.683012 <= gamma <= 5.140212",
      "3.683012 ≤ γ ≤ 5.140212" in led5)
# Cold read 3 (c): section 8 split
s8 = sec["8"]
check("CR3-c section 8: three sentences as recorded in 7e",
      r"answers it in part. It gives exact laws for where a trajectory leaving a row lands --- the exit valuation and the entry position, and hence which row is entered. It gives no law for which skeleton is entered: on that question, $F$ only restates Williams's Proposition~3.10." in s8)
check("CR3-c old self-contradicting wording gone", "hence the row entered" not in r5)
# Cold read 3 (d): 62,937 -- superseded by 4ee9029 (63,000); markers removed
check("CR3-d no PENDING-REVERIFY marker remains", "PENDING-REVERIFY" not in r5)
check("CR3-d 62,937 no longer appears in the TeX", "62{,}937" not in r5 and "62,937" not in r5)
say()

# ---------------------------------------------------------------------------------------------
say("PART B. Unchanged text")
abs4 = between(r4, r"\begin{abstract}", r"\end{abstract}")
abs5 = between(r5, r"\begin{abstract}", r"\end{abstract}")
check("plain abstract identical", abs4 == abs5, f"{len(abs5)} chars")
vn4 = between(r4, r"\subsection*{Version note}", r"\section*{Symbols at a glance}")
vn5 = between(r5, r"\subsection*{Version note}", r"\section*{Symbols at a glance}")
check("Version note and Author's note identical", vn4 == vn5, f"{len(vn5)} chars")
sec23_4 = between(r4, r"\section{One rising run", r"\section{The exact laws of one step}")
sec23_5 = between(r5, r"\section{One rising run", r"\section{The exact laws of one step}")
check("sections 2 and 3 identical", sec23_4 == sec23_5, f"{len(sec23_5)} chars")


def strip_guided(t):
    out = t
    for end, keep in [(FS, False), (FS, False), (WL, True)]:
        i = out.index(GA)
        j = out.index(end, i)
        out = out[:i] + (out[j:] if keep else out[j + len(end):])
    return out


app4 = r4[r4.index(APPX):]
app5 = strip_guided(r5[r5.index(APPX):])
la, lb = app4.splitlines(), app5.splitlines()
sm = difflib.SequenceMatcher(None, la, lb, autojunk=False)
changed_old, changed_new = [], []
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != "equal":
        changed_old += [x for x in la[i1:i2] if x.strip()]
        changed_new += [x for x in lb[j1:j2] if x.strip()]
expected_new_markers = [
    r"This appendix states formally what Section~\ref{sec:anchor} tells in words. It opens with a guided account",
    r"This appendix states formally what Section~\ref{sec:cycles} tells in words. It opens with a guided account",
    r"This appendix states formally what Section~\ref{sec:aeh} tells in words. It opens with a guided account",
    r"Each law above was checked by independently written code",
    r"Theorem~\ref{thm:vlaw}, Lemma~\ref{lem:absorption}, Theorem~\ref{thm:depth} (Remark~\ref{rem:verify1}) &",
]
ok_set = (len(changed_new) == 5 and len(changed_old) == 5 and
          all(any(l.startswith(m) for l in changed_new) for m in expected_new_markers))
check("appendices (guided accounts removed) differ from round 4 in exactly the 5 declared lines", ok_set,
      f"{len(changed_old)} old / {len(changed_new)} new non-blank lines")
for l in changed_new:
    say("        changed: " + l[:110] + " ...")
# the two content lines change only the count, the omega = 1 clause and the script name
rem4 = [l for l in changed_old if l.startswith("Each law above")][0]
rem5 = [l for l in changed_new if l.startswith("Each law above")][0]
REM_EDITS = [
    (r"all $62{,}937$ valid states with $\w < 3000$, $d < 64$,",
     r"all $63{,}000$ valid states with $\w < 3000$, $1 \le d < 64$ ($\w = 1$ included, where every law holds as stated),"),
    (r"the code is \texttt{experiments/absorption\_law.py}",
     r"the code is \texttt{experiments/depth\_law\_reverify.py} and \texttt{experiments/absorption\_law.py}"),
]
rem_applied = rem4
for a_, b_ in REM_EDITS:
    rem_applied = rem_applied.replace(a_, b_, 1) if rem4.count(a_) == 1 else rem_applied + "#MISSING"
check("Remark C.6: exactly two edits (count/range/omega = 1 clause; script named)", rem_applied == rem5)
g4 = [l for l in changed_old if l.startswith(r"Theorem~\ref{thm:vlaw}")][0]
g5 = [l for l in changed_new if l.startswith(r"Theorem~\ref{thm:vlaw}")][0]
G_EDITS = [
    (r"all $62{,}937$ valid states with $\w < 3000$, $d < 64$;",
     r"all $63{,}000$ valid states with $\w < 3000$, $1 \le d < 64$ ($\w = 1$ included, where every law holds as stated);"),
    (r"& \texttt{absorption\_law.py};", r"& \texttt{depth\_law\_reverify.py}, \texttt{absorption\_law.py};"),
]
g_applied = g4
for a_, b_ in G_EDITS:
    g_applied = g_applied.replace(a_, b_, 1) if g4.count(a_) == 1 else g_applied + "#MISSING"
check("Appendix G row: exactly two edits (count/range/omega = 1 clause; script named)", g_applied == g5)
# formal statement environments of B-E identical as a set
def envs(t):
    return re.findall(r"\\begin\{(?:theorem|proposition|lemma|corollary|definition|hypothesis|heuristic)\}.*?\\end\{(?:theorem|proposition|lemma|corollary|definition|hypothesis|heuristic)\}", t, re.S)
e4, e5 = envs(app4), envs(app5)
check("every formal statement environment (theorem/proposition/lemma/corollary/definition/hypothesis/heuristic) identical",
      e4 == e5, f"{len(e5)} environments")
# control: a one-character edit inside the formal part is caught
k = app5.index(r"\begin{theorem}[depth closure]")
tampered = app5[:k + 40] + ("X" if app5[k + 40] != "X" else "Y") + app5[k + 41:]
control("a one-character edit inside Theorem C.5 passes as unchanged", envs(tampered) == e4)
say()

# ---------------------------------------------------------------------------------------------
say("PART C. Moved text: round-4 sections 4-6 against the guided accounts of Appendices C-E")
# Each edit: (round-4 phrase, guided-account phrase, reason), with enough context to be unique.
# The round-4 text with exactly these edits applied must equal the guided account (whitespace
# normalised).  'UNDECLARED' marks an edit that section 7e does not record.
DECLARED = {
    "C": [
        (r"\section{The exact laws of one step}\label{sec:anchor} \emph{What this section is about.}",
         GA, "header: section opening -> guided-account heading (the move)"),
        ("how many halvings end the block", "how many halvings, beyond the first, end the block",
         "cold read 3 (a)"),
        (r"give the next state. The statements, formulas and proofs are in Appendix~\ref{app:laws}. The running",
         "give the next state. The running", "self-pointer dropped (the move)"),
        (r"all $62{,}937$ valid states with $\w$ below $3000$ and $d$ below $64$, and the absorption",
         r"all $63{,}000$ valid states with $\w$ below $3000$ and $d$ below $64$, $\w = 1$ included, and the absorption",
         "4ee9029: the re-run count, omega = 1 included"),
    ],
    "D": [
        (r"\section{Cycles: what counting can and cannot do}\label{sec:cycles} \emph{What this section is about.}",
         GA, "header (the move)"),
        ("This section explains what the classical", "This account explains what the classical",
         "self-reference (the move)"),
        ("achieve against cycles, and proves that they go no further:",
         "achieve against cycles, and why they go no further:",
         "UNDECLARED wording: 'and proves that they go no further' -> 'and why they go no further'"),
        (r"staircase of seven blocks. Appendix~\ref{app:cycles} has the statements, formulas and proofs.",
         "staircase of seven blocks.", "self-pointer dropped (the move)"),
        ("bent into a loop by one crash. It passes",
         r"bent into a loop by one crash. This seven-block instance is v3's, found by an earlier search and stated "
         r"as part~(iv) of Theorem~\ref{thm:staircase}; it is not one of the family of part~(i) below, whose "
         r"$\gamma$ lies between about $3.68$ and $5.14$. It passes", "cold read 3 (b)"),
        ("falls below that three-block threshold (each", "falls below that three-block bound (each",
         "UNDECLARED wording: the round-4 check's optional note on C-13 ('threshold' -> 'bound')"),
        (r"(``The threshold, explicitly'', Appendix~\ref{app:cycles}).", r"(``The threshold, explicitly'', below).",
         "pointer -> 'below' (the move)"),
        ("is larger throughout this range. This is",
         r"is larger throughout this range than $2$ to the power ($n$ times the shrinking factor). This is",
         "round-4 fix 3"),
        (r"(Appendix~\ref{app:cycles}, ``Verification and record''; Appendix~\ref{app:verify})",
         r"(``Verification and record'', below; Appendix~\ref{app:verify})", "pointer -> 'below' (the move)"),
    ],
    "E": [
        (r"\section{The fair-coin hypothesis}\label{sec:aeh} \emph{What this section is about.}", GA,
         "header (the move)"),
        ("This section states that picture exactly", "This account states that picture exactly",
         "self-reference (the move)"),
        (r"(Appendix~\ref{app:aeh} also states it as", "(the formal account below also states it as",
         "pointer (the move)"),
        (r"how it was tested. Appendix~\ref{app:aeh} has it in full.", "how it was tested.",
         "self-pointer dropped (the move)"),
        (r"the \emph{window law} of Appendix~\ref{app:aeh};", r"the \emph{window law} below;",
         "pointer -> 'below' (the move)"),
        (r"Admissible means two things (Appendix~\ref{app:aeh}).", "Admissible means two things.",
         "pointer dropped (the move)"),
        (r"(Appendix~\ref{app:aeh}, ``The unconditional base case''; proof",
         r"(``The unconditional base case'', below; proof", "pointer -> 'below' (the move)"),
        (r"explicitly bounded (Appendix~\ref{app:aeh});", "explicitly bounded (below);",
         "pointer -> 'below' (the move)"),
        (r"(given the hypothesis; Appendix~\ref{app:aeh}, ``What the hypothesis implies''; proof",
         r"(given the hypothesis; ``What the hypothesis implies'', below; proof", "pointer -> 'below' (the move)"),
        (r"Section~\ref{sec:anchor} (Appendix~\ref{app:laws} names them precisely), and that question is older",
         r"Section~\ref{sec:anchor} --- in the usual terms, digits of $2$-adic logarithms of whole numbers "
         r"(Appendix~\ref{app:laws} names them precisely) --- and questions of that kind are older",
         "round-4 fix 2"),
        ("small starting values, which the sharper control set aside;", "small starting values;",
         "round-4 fix 4"),
        (r"at the sizes tested (Appendix~\ref{app:aeh}, ``Calibration'').",
         r"at the sizes tested (``Calibration'', below).", "pointer -> 'below' (the move)"),
    ],
}


def word_diffs(a, b):
    wa, wb = a.split(), b.split()
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, wa, wb, autojunk=False).get_opcodes():
        if op != "equal":
            out.append((" ".join(wa[i1:i2]), " ".join(wb[j1:j2])))
    return out


def apply_edits(old_text, edits):
    """Apply each (old phrase, new phrase) once; each old phrase must occur exactly once."""
    t = " ".join(old_text.split())
    missing = []
    for frm, to, why in edits:
        if t.count(frm) != 1:
            missing.append((frm[:60], t.count(frm)))
            continue
        t = t.replace(frm, to, 1)
    return " ".join(t.split()), missing


undeclared = []
applied_by_tag = {}
for tag, old, new in [("C", sec["r4_4"], gC), ("D", sec["r4_5"], gD), ("E", sec["r4_6"], gE)]:
    o = " ".join(old.split())
    n = " ".join(new.split())
    applied, missing = apply_edits(old, DECLARED[tag])
    applied_by_tag[tag] = applied
    all_d = word_diffs(o, n)
    say(f"  Appendix {tag}: round-4 section {dict(C='4', D='5', E='6')[tag]} {len(o.split())} words, "
        f"guided account {len(n.split())} words, {len(all_d)} word-level differences:")
    for a_, b_ in all_d:
        say(f"        - {a_[:100]!r}")
        say(f"        + {b_[:100]!r}")
    for frm, to, why in DECLARED[tag]:
        say(f"     edit [{why}]")
        if "UNDECLARED" in why:
            undeclared.append((tag, why))
    rest = word_diffs(applied, n)
    check(f"Appendix {tag}: round-4 text with exactly the listed {len(DECLARED[tag])} edits applied equals the guided account",
          applied == n and not missing, f"residual differences {rest[:3]}; missing {missing}")
check("exactly two of the edits are not declared in section 7e (both noted; neither changes a claim)",
      len(undeclared) == 2, str(undeclared))
# control: an undeclared number change in a guided account is caught by the same comparison
tam = " ".join(gD.replace("at least $0.698$", "at least $0.689$").split())
control("an undeclared number change (0.698 -> 0.689) in App D's guided account passes",
        applied_by_tag["D"] == tam)
say()

# ---------------------------------------------------------------------------------------------
say("PART D. The entry-depth verification sentence (63,000, omega = 1 included)")
remC6 = between(r5, r"Each law above was checked by independently written code", "\n")
appG = between(r5, r"Theorem~\ref{thm:vlaw}, Lemma~\ref{lem:absorption}, Theorem~\ref{thm:depth} (Remark~\ref{rem:verify1}) &", "\n")
chk = between(gC, r"\paragraph{Checks.}", r"\paragraph{Where the difficulty is.}")
for name, txt in [("App C guided account 'Checks'", chk), ("Remark C.6", remC6), ("Appendix G row", appG)]:
    check(f"{name}: 'all $63{{,}}000$ valid states' and omega = 1 included",
          r"all $63{,}000$ valid states" in txt and r"$\w = 1$ included" in txt)
check("Remark C.6 names experiments/depth_law_reverify.py",
      r"\texttt{experiments/depth\_law\_reverify.py}" in remC6)
check("Appendix G row names depth_law_reverify.py", r"\texttt{depth\_law\_reverify.py}" in appG)
check("App C guided account points to Remark C.6 and to Appendix G for the scripts (it names no script itself)",
      r"(Remark~\ref{rem:verify1})" in chk and r"Appendix~\ref{app:verify} lists the scripts" in chk
      and r"depth\_law" not in chk)
check("ledger C-3.6 and C-3.5(a) say 63,000 with omega = 1 included",
      led5.count("63,000 valid states") >= 2 and "`ω = 1` included" in led5)
check("committed output: 'valid states checked: 63000'", "valid states checked: 63000" in dlr_out)
check("committed output: omega = 1 checked separately, 63 states, 0 failures",
      "W = 1 SEPARATELY" in dlr_out and "states: 63; checks: 784; failures: 0" in dlr_out)
check("committed output: 'TOTAL: 669250 checks on 63000 states, 0 failures'",
      "TOTAL: 669250 checks on 63000 states, 0 failures" in dlr_out)
nvalid = sum(1 for w in range(1, 3000) if w % 2 and w % 3) * len(range(1, 64))
check("fresh count of valid states (omega < 3000 odd, prime to 3; 1 <= d < 64) is 63,000", nvalid == 63000, str(nvalid))
control("62,937 taken as the full count", 62937 == nvalid)


def v2(x):
    x = abs(x)
    return (x & -x).bit_length() - 1


def v3_(x):
    c = 0
    while x % 3 == 0:
        x //= 3
        c += 1
    return c


def N_mod(u, k):
    """t mod 2^k with 9^t = u^{-1} in Z_2, for u = 1 (mod 8); by bit lifting mod 2^(k+3)."""
    E = k + 3
    mod = 1 << E
    target = pow(u % mod, -1, mod)
    assert target % 8 == 1
    t = 0
    for i in range(k):
        m = 1 << (i + 4)
        if pow(9, t, m) != target % m:
            t += 1 << i
    assert pow(9, t, mod) == target
    return t


def state_of(x):
    u = x + 1
    m = v2(u)
    r = u >> m
    a = v3_(r)
    return (r // 3 ** a, m + a), m, a


def step_F(w, d):
    """next state from the definition: cascade at 2(3^d w - 1); exit = (3^d w - 1)/2^s."""
    C = 3 ** d * w - 1
    s = v2(C)
    e = C >> s
    (w2, d2), m2, a2 = state_of(e)
    return s, e, (w2, d2), m2, a2


# fresh Theorem C.5 on omega = 1, 1 <= d < 64 (M(1) = 0, N(1) = 0)
bad = 0
for d in range(1, 64):
    s, e, nxt, mp_, ap_ = step_F(1, d)
    if d % 2 == 0:                      # lifting class of omega = 1
        n_ = d // 2
        delta = N_mod((1 - 2 ** s) % (1 << 300), 260)  # 1 - 2^s = 1 (mod 8) for s >= 3
        xi = n_ - 0
        pred = 3 - s + v2((xi + delta) % (1 << 260)) if (xi + delta) % (1 << 260) else None
    else:
        pred = 1 + v2(d - 0) if s == 1 else v2((d - 1) - 0)
    if pred != mp_ or nxt[1] != mp_ + ap_:
        bad += 1
check("fresh: Theorem C.5's entry-depth law and d+ = m+ + a+ on the 63 states (1, d), 1 <= d < 64",
      bad == 0, f"{bad} mismatches")
bad_ctrl = 0
for d in range(2, 64, 2):
    s, e, nxt, mp_, ap_ = step_F(1, d)
    if 3 - s + v2(d // 2) != mp_:       # the law with the delta_s term dropped
        bad_ctrl += 1
control("the omega = 1 lifting law with delta_s dropped (m+ = 3 - s + v2(n)) holds on every even d < 64",
        bad_ctrl == 0, f"{bad_ctrl} mismatches")
say()

# ---------------------------------------------------------------------------------------------
say("PART E. Worked numbers of the new sections 4-6")
# Section 4: the table, the anchor rule, (1,2), (7,1)
TABLE = {(1, 0): None, (3, 0): 1, (5, 0): 2, (7, 0): 1, (1, 1): 1, (3, 1): None, (5, 1): 1, (7, 1): 2}
bad = 0
for w in range(1, 3001, 2):
    if w % 3 == 0:
        continue
    for d in range(1, 41):
        s = v2(3 ** d * w - 1)
        cell = TABLE[(w % 8, d % 2)]
        if cell is None:
            if s < 3:
                bad += 1
        elif s != cell:
            bad += 1
check("the eight-kind rule of section 4 (six fixed at 1 or 2, lifting >= 3) on all valid states w < 3001, d <= 40",
      bad == 0, f"{bad} mismatches")
K64 = 64
bad = nl = 0
for w in range(1, 3001, 2):
    if w % 3 == 0:
        continue
    M = N_mod(w * w, K64 + 8) % (1 << K64)
    for d in range(1, 41):
        if (w % 8, d % 2) in [(1, 0), (3, 1)]:
            nl += 1
            s = v2(3 ** d * w - 1)
            diff = (d - M) % (1 << K64)
            agree = v2(diff) if diff else K64
            if s != 2 + agree:
                bad += 1
check("lifting kinds: s = 2 + (number of lowest binary digits on which d agrees with the anchor M(w) = N(w^2))",
      bad == 0, f"{nl} lifting states, w < 3001, d <= 40, anchor mod 2^64; {bad} mismatches")
check("anchor of omega = 1 is all zeros (9^0 = 1)", N_mod(1, 64) == 0)
s12 = v2(3 ** 2 * 1 - 1)
check("(1,2): d = 2 = 0b10 has one trailing zero, s = 2 + 1 = 3 = v2(3^2 - 1)",
      bin(2) == "0b10" and v2(2) == 1 and s12 == 3)
check("(1,2): 3*5 + 1 = 16 halves four times (the first halving plus three more), to 1",
      3 * 5 + 1 == 16 and v2(16) == 4 and 16 >> 4 == 1 and state_of(5)[0] == (1, 2))
check("13 has state (7,1); (7,1) is of kind (7, odd), table s = 2",
      state_of(13)[0] == (7, 1) and TABLE[(7 % 8, 1 % 2)] == 2)
s71, e71, nxt71, m71, a71 = step_F(7, 1)
check("(7,1): s = v2(3*7 - 1) = v2(20) = 2, even; exit 5", s71 == 2 and e71 == 5 and s71 % 2 == 0)
check("orbit: 3*13 + 1 = 40 halves three times (1 + s) to 5", 3 * 13 + 1 == 40 and v2(40) == 3 and 40 >> 3 == 5)
check("next state gains a factor of 3: 5 + 1 = 6 = 2*3, next state (1,2) with a = 1",
      5 + 1 == 2 * 3 and nxt71 == (1, 2) and a71 == 1 and m71 == 1)
check("(5 + 1) * 2^s = 3^d w + 2^s - 1: 24 = 21 + 3",
      (5 + 1) * 2 ** s71 == 3 * 7 + 2 ** s71 - 1 == 24)
# Section 5: the seven-block staircase
mm = [4, 7, 9, 15, 23, 35, 1]
ss = [1, 1, 1, 1, 1, 1, 49]
p = len(mm)
n = sum(mm)
K = sum(mm) + sum(ss)
check("n = 4+7+9+15+23+35+1 = 94", n == 94)
check("exit valuations total 6*1 + 49 = 55; K = 94 + 55 = 149", sum(ss) == 55 and K == 149)
check("K = sum over blocks of (entry depth + exit valuation): each block halves once per step plus s",
      K == sum(m_ + s_ for m_, s_ in zip(mm, ss)))
q = 2 ** K - 3 ** n
check("q = 2^149 - 3^94 > 0 (2^K only slightly larger than 3^n)", q > 0 and q < 2 ** K // 100)
gamma = K - math.log2(q)
check("gamma = K - log2 q = 6.74 (to 2 decimals)", round(gamma, 2) == 6.74, f"gamma = {gamma:.6f}")
check("gamma lies outside part (i)'s bracket [3.683012, 5.140212]", not (3.683012 <= gamma <= 5.140212))
check("3^n = 2^K (1 - 2^-gamma) (definition of gamma, to double precision)",
      abs(3 ** n / 2 ** K - (1 - 2 ** -gamma)) < 1e-12)


def R_rot(ms, svals, r):
    m_ = ms[r:] + ms[:r]
    s_ = svals[r:] + svals[:r]
    P = len(m_)
    sig = [s_[j] + m_[(j + 1) % P] for j in range(P)]
    tot = 0
    for t in range(P):
        Mt = sum(m_[t + 1:])
        St = sum(sig[:t])
        tot += 3 ** Mt * 2 ** St * (2 ** s_[t] - 1)
    return tot


def fixed_point_u(ms, svals, r):
    """u = x_r + 1 as the rational fixed point of the composed block map u -> 3^m u / 2^(m+s) + 1 - 2^-s."""
    m_ = ms[r:] + ms[:r]
    s_ = svals[r:] + svals[:r]
    A, B = Fraction(1), Fraction(0)          # u_out = A u + B
    for m1, s1 in zip(m_, s_):
        a = Fraction(3 ** m1, 2 ** (m1 + s1))
        b = 1 - Fraction(1, 2 ** s1)
        A, B = a * A, a * B + b
    return B / (1 - A)


Rs = [R_rot(mm, ss, r) for r in range(p)]
size_ok = [q <= R for R in Rs]
div_ok = [R % q == 0 for R in Rs]
check("all seven size conditions q <= R_r hold (Proposition D.1)", all(size_ok), f"{sum(size_ok)}/7")
check("divisibility q | R_r fails (so not a cycle)", not all(div_ok), f"q | R_r at {sum(div_ok)} of 7 rotations")
cross = all(Fraction(R, q) == fixed_point_u(mm, ss, r) / 2 ** (mm[r:] + mm[:r])[0] for r, R in enumerate(Rs))
check("cross-check: R_r / q = (x_r + 1) / 2^(m_r) from the rational fixed point of the block map, every rotation",
      cross)
check("trivial cycle (m, s) = (1, 1): R = q = 1, size and divisibility both hold",
      R_rot([1], [1], 0) == 1 == 2 ** 2 - 3 and fixed_point_u([1], [1], 0) == 2)
check("first six blocks climb (s = 1), the last falls 49 extra halvings", ss[:6] == [1] * 6 and ss[6] == 49)
# Section 6: letters of the orbit of 7, P(1,2) = 1/8, 1/3 gain rate
letters = []
x = 7
for _ in range(6):
    (w_, d_), m_, a_ = state_of(x)
    C = 3 ** d_ * w_ - 1
    s_ = v2(C)
    letters.append((m_, s_))
    x = C >> s_
check("letters of the orbit of 7: (3,1), (1,2), (1,3), (1,1), then (1,1) forever",
      letters[:4] == [(3, 1), (1, 2), (1, 3), (1, 1)] and letters[4:] == [(1, 1), (1, 1)], str(letters))
P12 = Fraction(1, 2) * Fraction(1, 4)
check("P(letter (1,2)) = 1/2 * 1/4 = 1/8 under the coin model", P12 == Fraction(1, 8))
gain = Fraction(1, 4) / (1 - Fraction(1, 4))
partial = sum(Fraction(1, 2 ** j) for j in range(2, 41, 2))
check("1/4 + 1/16 + ... = 1/3 exactly (geometric sum), partial sums to 2^-40 within 2^-40",
      gain == Fraction(1, 3) and 0 < Fraction(1, 3) - partial < Fraction(1, 2 ** 40))
bad = 0
for w in range(1, 601, 2):
    if w % 3 == 0:
        continue
    for d in range(1, 21):
        s_ = v2(3 ** d * w - 1)
        e = (3 ** d * w - 1) >> s_
        gained = ((e + 1) * 2 ** s_) % 3 == 0 and v3_(((e + 1) >> v2(e + 1))) > 0
        if gained != (s_ % 2 == 0):
            bad += 1
check("a factor of 3 is gained exactly when s is even (w < 601, d <= 20)", bad == 0, f"{bad} mismatches")
# main text uses none of the symbols dropped from the Symbols page
main_sections = main5[main5.index(r"\section{What this paper is about}"):]
check("main text sections 1-8 use none of q, gamma, X_0, p_1 (dropped from the Symbols page)",
      all(tok not in main_sections for tok in [r"\gamma", "X_0", "p_1", "$q$", "$q "]))
check("Symbols page: 'p-adic' occurs in the Author's note, and '$m$-cycle' nowhere in sections 1-8",
      "$p$-adic" in vn5 and "$m$-cycle" not in main_sections)
check("App D guided account uses q, gamma, X_0 and p_1(X_0), as the Symbols page says",
      all(tok in gD for tok in ["$q$", r"\gamma", "X_0", "p_1(X_0)"]))
say()

# ---------------------------------------------------------------------------------------------
say("PART F. Negative controls")
control("letter list with (1,2) replaced by (2,1)", [(3, 1), (2, 1), (1, 3), (1, 1)] == letters[:4])
control("K = 148 for the staircase", 148 == K)
control("P(1,2) = 1/6", Fraction(1, 6) == P12)
control("(7,1) given s = 1", v2(3 * 7 - 1) == 1)
mm_bad = [4, 7, 9, 15, 23, 35, 1]
ss_bad = [1, 1, 1, 1, 1, 1, 48]   # K = 148 < n log2 3: q < 0, no size-passer
q_bad = 2 ** (sum(mm_bad) + sum(ss_bad)) - 3 ** sum(mm_bad)
control("the staircase with last exit valuation 48 passes the size conditions",
        q_bad > 0 and all(q_bad <= R_rot(mm_bad, ss_bad, r) for r in range(7)), f"q = {'neg' if q_bad < 0 else 'pos'}")
ss_far = [1, 1, 1, 1, 1, 1, 60]   # 2^K far above 3^n: some rotation's size condition must fail
q_far = 2 ** (sum(mm_bad) + sum(ss_far)) - 3 ** sum(mm_bad)
control("the staircase with last exit valuation 60 passes every size condition",
        all(q_far <= R_rot(mm_bad, ss_far, r) for r in range(7)))
M3_flipped = (N_mod(9, 72) % (1 << 64)) ^ (1 << 3)
bad = 0
for d in range(1, 200, 2):
    s = v2(3 ** d * 3 - 1)
    diff = (d - M3_flipped) % (1 << 64)
    if s != 2 + (v2(diff) if diff else 64):
        bad += 1
control("anchor of w = 3 with one digit flipped satisfies the lifting rule on d odd < 200", bad == 0, f"{bad} mismatches")
say()

say(f"TOTAL: {n_pass} checks passed, {n_fail} failed; controls {n_ctrl_ok} rejected, {n_ctrl_bad} not rejected")
verdict = n_fail == 0 and n_ctrl_bad == 0
say("VERDICT: " + ("PASS" if verdict else "FAIL"))
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines_out) + "\n")
print("\n".join(lines_out))
sys.exit(0 if verdict else 1)
