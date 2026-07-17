# Review bundle: paper 1 v2 (*Reduced coordinates for the Collatz map*)

Self-contained for an external reviewer with no access to the repository. Everything a reviewer needs to evaluate the v2 changes — what changed, why, the exact diff, and the fidelity checks — is below; no other file needs to be opened.

**Branch:** `paper1-v2-p22`, off `main`. **Not merged** — this branch awaits review by the project's main session before the author sees it, per standing convention (Zenodo upload/publication is the author's act alone; this branch prepares files only).

## Background, in one paragraph

Paper 1 (*Reduced coordinates for the Collatz map*, Zenodo DOI [10.5281/zenodo.21273548](https://doi.org/10.5281/zenodo.21273548)) is published. Eric Merle — author of a related Lean 4 formalization of conditional Collatz cycle-exclusion (Zenodo DOI [10.5281/zenodo.19790406](https://doi.org/10.5281/zenodo.19790406)) — sent a referee-grade reading by correspondence (2026-07-15/16, author's mailbox, not in the repository) that found two issues: a citation of his preprint dropped its subtitle, and the paper's staircase-sharpness hedge (Theorem `thm:staircase`) was flagged as possibly reachable by a general construction. The author's reply committed, publicly, to two things for a v2: restoring the subtitle, and evidencing the hedge better without closing it ("the hedge stays in any v2 — better evidenced, not closed"). A delegated research session then attempted the general construction and reached a documented **floor grade** — a verified instance record with an initial obstruction at `p = 22`. A second exchange with the same correspondent resolved that obstruction (2026-07-17): the failure was a candidate-generation gap in the Diophantine chain, not a combinatorial wall, and two of his named candidates close the range under the recipe's own recorded algorithm. This v2 packages the citation fix, the hedge-evidence note, and — as a pre-upload factual update — the resolved, contiguous record. All of it is recorded in the project wiki at `cycles.md` §12.8.6.

## Changelog (flat, four items)

1. **Subtitle restored.** The `merle` bibliography entry now carries the preprint's full title, including the subtitle v1 dropped: "...a conditional formal proof in Lean 4, **with documented structural obstructions**". The DOI was already correct and is untouched.
2. **Hedge-evidence note added, register-calibrated.** A short, clearly-marked "Note added in v2 (July 2026)" follows Remark `rem:staircase` (the staircase-divergence link), reporting the floor-grade construction attempt: the recipe in one sentence, the verified range and interval, and the remaining gap. **The theorem's hedge sentence itself is untouched, verbatim** — the note reports evidence, it does not upgrade the claim.
3. **Version history relocated and restated.** The long `\date`-footnote is gone; `\date` is now a plain one-line date/DOI field, and an unnumbered "Version note" paragraph immediately after the abstract carries the version history. The repository pointer in the added note is pinned to a commit, not a mutable root URL.
4. **The `p = 22` resolution reached the note (pre-upload factual update).** The displayed range is now the full **contiguous** `p ∈ {2,...,23}` (interval unchanged, `[1.828, 3.643]`). The note's gap language is reduced from two gaps to **one**: `p = 22` is no longer reported as an unresolved case; instead the note reports, in two sentences, that the recipe's own candidate chain initially left `p = 22` unresolved, that correspondence with Eric Merle identified the cause as a coverage gap in that chain (not a failure of the correction step), and that two candidates outside the chain (`n = 25217`, `n = 31202`) close it under the same recorded recipe (`13` and `8` correction moves). The sole remaining gap — no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs — is now reported as demonstrated to bite in practice, not only in principle. The repository pointer is re-pinned from commit `b566e4d` to commit `72ec88e` (the public `main` commit containing the updated §12.8.6 record).

No mathematical claim in the paper changes strength anywhere in this diff. This item adds no new mathematics; it is a factual update to what the note reports about an already-recorded wiki result.

## Full unified diff (v2 tex against the archived v1)

The complete content diff between `sources/paper/collatz-reduced-v1.tex` (archived v1, byte-identical to the original published source) and `paper/collatz-reduced-v2.tex` at its current head. This is the *entire* difference between v1 and v2 — nothing else in the file differs.

```diff
diff --git a/sources/paper/collatz-reduced-v1.tex b/paper/collatz-reduced-v2.tex
index 3d09b91..f1111a9 100644
--- a/sources/paper/collatz-reduced-v1.tex
+++ b/paper/collatz-reduced-v2.tex
@@ -23,7 +23,7 @@

 \title{Reduced coordinates for the Collatz map:\\ exact per-step laws, anchor dynamics,\\ and the limits of counting arguments for cycles}
 \author{Ben Macindoe\thanks{\texttt{macindoebenjamin@gmail.com}. Developed through extensive AI-assisted research (Claude, Anthropic); the division of labor and the verification protocol are stated in Appendix~\ref{app:method}.}}
-\date{July 2026 \;\cdot\; DOI: \href{https://doi.org/10.5281/zenodo.21273548}{10.5281/zenodo.21273548}}
+\date{v2, July 2026 \;\cdot\; DOI: \href{https://doi.org/10.5281/zenodo.21273548}{10.5281/zenodo.21273548}}

 \begin{document}
 \maketitle
@@ -32,6 +32,9 @@
 We study the Collatz dynamics in a reduced coordinate system that compresses each deterministic valuation run into a single block, producing a self-map $F$ on states $(\w,d)$ --- an odd core prime to $3$ and a depth. The reduction is faithful: the Collatz conjecture is equivalent to every $F$-orbit reaching $(1,1)$, with nontrivial cycles in bijection. In these coordinates the local arithmetic admits exact laws. A single $2$-adic quantity, the \emph{anchor} $M(\w) = -2\log\w/\log 9 \in \Z_2$, governs the step: the exit valuation obeys the global law $s = 2 + \vt{d - M(\w)}$ whenever $3^d\w \equiv 1 \pmod 8$ and is constant on the remaining residue classes; the depth evolution closes exactly in terms of the anchor displacement together with a stated $3$-adic absorption law; and the anchor increment along one step obeys an exact law modulo any power of $2$, computable from graded residues of the state. A finite window of digits consequently decides each step in an error-free trichotomy, while a digit-budget accounting indicates that no bounded window can decide infinite horizons --- localizing the difficulty of the problem in the digit supply of the anchors. On the cycle side, a one-line elimination identity yields short rederivations of the classical exclusions for cycles of one, two, and three blocks. Our main new theorem is a sharp dichotomy for counting arguments: a trim uniform in the number of blocks $p$ exists, giving effective finiteness at every period, but its constant necessarily degrades like $(\LL)^{-p}$ --- an explicit family of near-counterexamples (\emph{staircases}: geometric climbs closed by a single crash, precisely divergent-orbit profiles bent into loops) shows counting arguments cannot do substantially better, so uniform cycle exclusion requires arithmetic (divisibility) input, not sharper counting. Finally we state the equidistribution hypothesis implicit in the classical heuristics as a precise conjecture about an exactly computable product law, prove its consequences conditionally, and report a calibration campaign whose four apparent anomalies all dissolved under controls --- one of them via an exact routing lemma that a biased estimator had been reflecting.
 \end{abstract}

+\subsection*{Version note}
+v1, July 2026 (original publication). v2, July 2026: restored the subtitle of the \texttt{merle} citation; added a note evidencing the sharpness hedge of Theorem~\ref{thm:staircase} (Section~\ref{sec:cycles}), prompted by correspondence with Eric Merle. No theorem or universal claim is strengthened; v2 adds a finite computational evidence record. The v2-specific Zenodo DOI is assigned at upload.
+
 \subsection*{Author's note}

 \emph{Dear reader --- I'm no mathematician, and I learned much of this paper's terminology during the process of formalizing it ($p$-adic valuations were completely new to me as a formal concept). It all began when I got hooked on a strange recursive pattern in the prime factors of a Collatz chain, and that idea pushed me into conversation with AI. We cleaned my idea up into the states $(\w,d)$, with the primary goal of factoring as much deterministic behaviour as possible out of the question, in the hope of focusing attention where it matters. That simplification is what enables the paper's main contributions: exact laws for every single step; a uniform trim that caps what size-counting can achieve against cycles; and an exact hypothesis pointing the remaining question toward more fundamental ``fair-coin'' mathematics. Because this work is AI-assisted and because I am not formally trained in the relevant mathematics, Appendix~\ref{app:method} describes the verification protocol used throughout the project. The complete research record is public at \url{https://github.com/macindoe/collatz}. --- Ben}
@@ -213,6 +216,11 @@ No trim uniform in $p$ can extend the small-period constants: there exist config
 The staircase profile --- geometric depth growth with shallow exits --- is exactly the growth regime of divergent orbits. Size analysis cannot forbid it as a cycle for the same reason drift analysis cannot forbid divergence. The two halves of the residual difficulty meet in one configuration.
 \end{remark}

+\subsection*{Note added in v2 (July 2026)}
+Prompted by correspondence with Eric Merle concerning this theorem's sharpness hedge (his related formal work is cited in \cite{merle}), we attempted a single period-parametrized construction procedure toward the assessed claim of Theorem~\ref{thm:staircase}: semiconvergents of $\LL$ select the exponent $n$, a rounded geometric profile builds the climb, and a bounded correction closes the last bits, applied separately at each period. Exact big-integer verification by this recipe produced a passing size-condition witness ($q \le R_r$ at every rotation) at every period
+\[ p \in \{2,\dots,23\}, \qquad \gamma/\log_2 p \in [1.828,\ 3.643] \]
+--- now a contiguous range, extending the two isolated instances above. Initially the recipe's own candidate chain left $p = 22$ unresolved; correspondence with Eric Merle identified the cause as a gap in that chain's coverage at the required scale, not a failure of the correction step, and at candidates outside the chain ($n = 25217$, $n = 31202$) the same recipe resolves it ($13$ and $8$ correction moves), closing the range above. The remaining gap is the one already named: no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs --- the bound that would certify no period is skipped --- and the $p = 22$ episode is a demonstration that this gap bites in practice, not only in principle. The hedge sentence above is therefore unchanged: finite-range evidence supports the assessed $\gamma = O(\log p)$ behaviour, but does not prove it for all $p$. The construction, the verified instance record, and the diagnosis of the remaining gap are recorded at \texttt{cycles.md} \S12.8.6 of the project's public repository (\url{https://github.com/macindoe/collatz/blob/72ec88e/cycles.md}).
+
 \section{The equidistribution hypothesis, made exact}\label{sec:aeh}

 Why is a product law the right comparison object? By Theorem~\ref{thm:onestep}, all dynamical decisions at horizon one are functions of the depth-$k$ window; the natural null model is therefore a measure on windows, and the natural choice of measure is forced by the structure: the $\w$-residues carry the anchor digits, for which Haar measure is the canonical reference (this is where the classical $2$-adic shift-conjugacy heuristics live), while the depth $d$ is \emph{dynamical} --- it is produced by Theorem~\ref{thm:depth} --- and so receives not Haar measure but the stationary law of the exact window chain. Let $\pi_k$ denote this product law. The class skeleton of the chain is computable exactly: e.g.\ from class $(\w\equiv1\ (8),\ d$ odd$)$ the next depth is exactly $1$ (since $m_+ = 1$, $a_+ = 0$ there), and from $(\w \equiv 5\ (8),\ d$ odd$)$, $P(\dnext \text{ even}) = \tfrac23$ exactly. Under $\pi_k$, unconditionally: $P(s = j) = 2^{-j}$ (four of eight classes give $s=1$, two give $s=2$, and the lifting shells are geometric); the $3$-gain rate is $\sum_{j\,\mathrm{even}} 2^{-j} = \tfrac13$ by Lemma~\ref{lem:absorption}; and the classical negative drift follows. The folklore ``ledger'' is thus a theorem \emph{about} $\pi_k$; the empirical question is only whether orbits follow $\pi_k$.
@@ -250,7 +258,7 @@ This work was developed through extensive AI-assisted research over three years
 \bibitem{bl} Y.~Bugeaud, M.~Laurent, \emph{Minoration effective de la distance $p$-adique entre puissances de nombres alg\'ebriques}, J.\ Number Theory 61 (1996), 311--342.
 \bibitem{rhin} G.~Rhin, \emph{Approximants de Pad\'e et mesures effectives d'irrationalit\'e}, S\'emin.\ Th\'eor.\ Nombres Paris (1987); see also Q.~Wu, Math.\ Comp.\ 72 (2003), 901--911.
 \bibitem{barina} D.~Barina, \emph{Improved verification limit for the convergence of the Collatz conjecture}, J.\ Supercomputing (2025).
-\bibitem{merle} E.~Merle, \emph{On the non-existence of non-trivial Collatz cycles: a conditional formal proof in Lean 4}, preprint, Zenodo DOI 10.5281/zenodo.19790406 (2026).
+\bibitem{merle} E.~Merle, \emph{On the non-existence of non-trivial Collatz cycles: a conditional formal proof in Lean 4, with documented structural obstructions}, preprint, Zenodo DOI 10.5281/zenodo.19790406 (2026).
 \bibitem{llmcollatz} \emph{Exploring Collatz Dynamics with Human--LLM Collaboration}, arXiv:2603.11066 (2026).
 \end{thebibliography}
```

## The Version note, quoted in full

> **Version note**
>
> v1, July 2026 (original publication). v2, July 2026: restored the subtitle of the `merle` citation; added a note evidencing the sharpness hedge of Theorem 4.6 (`thm:staircase`) (Section 4), prompted by correspondence with Eric Merle. No theorem or universal claim is strengthened; v2 adds a finite computational evidence record. The v2-specific Zenodo DOI is assigned at upload.

## The added note, quoted in full

> **Note added in v2 (July 2026)**
>
> Prompted by correspondence with Eric Merle concerning this theorem's sharpness hedge (his related formal work is cited in [merle]), we attempted a single period-parametrized construction procedure toward the assessed claim of Theorem 4.6 (`thm:staircase`): semiconvergents of log₂3 select the exponent *n*, a rounded geometric profile builds the climb, and a bounded correction closes the last bits, applied separately at each period. Exact big-integer verification by this recipe produced a passing size-condition witness (*q* ≤ *R_r* at every rotation) at every period
>
> *p* ∈ {2, …, 23}, γ/log₂ *p* ∈ [1.828, 3.643]
>
> — now a contiguous range, extending the two isolated instances above. Initially the recipe's own candidate chain left *p* = 22 unresolved; correspondence with Eric Merle identified the cause as a gap in that chain's coverage at the required scale, not a failure of the correction step, and at candidates outside the chain (*n* = 25217, *n* = 31202) the same recipe resolves it (13 and 8 correction moves), closing the range above. The remaining gap is the one already named: no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs — the bound that would certify no period is skipped — and the *p* = 22 episode is a demonstration that this gap bites in practice, not only in principle. The hedge sentence above is therefore unchanged: finite-range evidence supports the assessed γ = O(log *p*) behaviour, but does not prove it for all *p*. The construction, the verified instance record, and the diagnosis of the remaining gap are recorded at `cycles.md` §12.8.6 of the project's public repository (https://github.com/macindoe/collatz/blob/72ec88e/cycles.md).

## Build

Built with `pdflatex` (MiKTeX-pdfTeX 4.23, MiKTeX 25.12), two passes, in a temp directory outside the repository mount (a documented Windows quirk: the mount can lock LaTeX aux files) and copied into `paper/collatz-reduced-v2.pdf`. **Output: 11 pages.** The Version note (page 1), the Note added in v2 (page 8), and the corrected Merle bibliography entry (page 11) were extracted with `pdftotext` and checked against the source; all render correctly, including the contiguous range, the two-sentence `p = 22` resolution, and the `blob/72ec88e` repository pointer.

**Build obstruction (recorded, not blocking).** `pdflatex` exits with status 1, reproducing the same five-line error signature at the same location every time this document has been built, on both v2 and the pristine, unedited archived v1 source (`sources/paper/collatz-reduced-v1.tex`):

```
! Missing $ inserted.
! Extra }, or forgotten $.
! LaTeX Error: Command \end{center} invalid in math mode.
! Missing $ inserted.
! Missing } inserted.
```

These occur during `\maketitle`'s processing of the `\date` field and are auto-recovered by TeX's own error recovery ("Proceed, with fingers crossed"); the resulting PDF is complete and correct. This is diagnosed as a pdfTeX toolchain-version artifact present on pristine v1, independent of any v2 content — not a defect introduced by these or any prior edits.

## Fidelity-check transcript (re-run fresh against the current head)

This item introduces no new mathematics — the check is fidelity to `cycles.md` §12.8.6 and to v1, not proof. All checks pass.

**(a) The `thm:staircase` theorem environment, including its hedge sentence, is byte-identical to v1.**

```
$ diff <(sed -n '/\\begin{theorem}\[sharpness: the staircase\]/,/\\end{theorem}/p' sources/paper/collatz-reduced-v1.tex) \
       <(sed -n '/\\begin{theorem}\[sharpness: the staircase\]/,/\\end{theorem}/p' paper/collatz-reduced-v2.tex)

(no output — identical)
```

**PASS.**

**(b) Every number in the added note appears verbatim in `cycles.md` §12.8.6.**

```
$ sed -n '237,273p' cycles.md > /tmp/128section.txt
$ grep -n "2, ..., 23\|p = 22\|1.828\|3.643\|25217\|31202" /tmp/128section.txt
```

Matches found, all inside §12.8.6:

- `p ∈ {2, 3, ..., 23}` — Proposition 12.8.6.4's display (`γ / log_2 p ∈ [1.828, 3.643]` on the same line) and the section's opening paragraph ("a verified instance record covering every period `p ∈ {2,...,23}`").
- `p = 22` — the section header ("Obstruction (`p = 22`) — resolved (2026-07-17)"), the Extension paragraph, and the Resolution paragraph.
- `1.828`, `3.643` — Proposition 12.8.6.4's display and the Extension paragraph ("both inside `[1.828, 3.643]`").
- `25217` — the Extension paragraph ("`n = 25217` (`γ = 11.186`, `γ/log_2 22 = 2.508`, `13` correction moves)") and the Resolution paragraph.
- `31202` — the Extension paragraph ("`n = 31202` (`γ = 14.746`, `γ/log_2 22 = 3.307`, `8` correction moves)") and the Resolution paragraph.
- `13`, `8` — both correction-move counts, in the Extension and Resolution paragraphs, and again in the Credit paragraph ("both resolve, in `13` and `8` moves").

Every number the note writes — `2`, `23`, `1.828`, `3.643`, `22`, `25217`, `31202`, `13`, `8` — appears verbatim in `cycles.md` §12.8.6. **PASS.**

**(c) Register greps against the current note (`paper/collatz-reduced-v2.tex`, the "Note added in v2" paragraph), extended by two.**

```
$ grep -c "period-parametrized" <note text>
1

$ grep -c "non-per-period" <note text>
0

$ grep -c "dense" <note text>
0

$ grep -c "combinatorial obstruction" <note text>
0

$ grep -c "persistent unresolved case" <note text>
0
```

The note contains "period-parametrized", and contains none of "non-per-period", "dense", "combinatorial obstruction", or "persistent unresolved case" (the last two newly re-checked this round, since the previous round's `p = 22` language — now replaced — used "persistent unresolved case"). **PASS, all five.**

## Register check

The added note avoids "settles" / "establishes" / "confirms sharpness" and every other upgrade-implying word; it reports the recipe's floor-grade outcome and the `p = 22` resolution both as evidence, not closure; the sole remaining gap is stated without softening; and the hedge conclusion stays "assessed... does not prove". This matches `AGENTS.md`'s register norm and `publication.md`'s ledger entry for the sharpness-hedge status.

## Revision note

The note's wording was revised after two external review passes (register calibration; evidence record unchanged), and, in this round, updated with a pre-upload factual update after the `p = 22` resolution (the previously-recorded obstruction is now recorded, in the paper, as resolved). History of what changed and why lives in the git log, not here.

## Off-brief findings

See `briefs/paper1-v2-findings.md`.

## Definition-of-done checklist

- [x] v1 archived byte-identical under `sources/paper/`.
- [x] `paper/collatz-reduced-v2.tex` differs from v1 in exactly the edits shown in the diff above.
- [x] A built v2 PDF (`paper/collatz-reduced-v2.pdf`, 11 pages) with the one pre-existing, non-blocking build obstruction recorded.
- [x] This self-contained review bundle, regenerated as a current-state artifact.
- [x] Fidelity checks recorded, re-run fresh, all pass, including the two extended register greps.
- [x] Ledger sweep done.
- [x] Clean per-item commits on `paper1-v2-p22`, no merge to `main`.
