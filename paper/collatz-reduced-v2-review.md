# Review bundle: paper 1 v2 (*Reduced coordinates for the Collatz map*)

Self-contained for an external reviewer with no access to the repository. Everything a reviewer needs to evaluate the v2 changes — what changed, why, the exact diff, and the fidelity checks — is below; no other file needs to be opened.

**Branch:** `paper1-v2`, off `main`. **Not merged** — this branch awaits review by the project's main session before the author sees it, per standing convention (Zenodo upload/publication is the author's act alone; this branch prepares files only).

## Background, in one paragraph

Paper 1 (*Reduced coordinates for the Collatz map*, Zenodo DOI [10.5281/zenodo.21273548](https://doi.org/10.5281/zenodo.21273548)) is published. Eric Merle — author of a related Lean 4 formalization of conditional Collatz cycle-exclusion (Zenodo DOI [10.5281/zenodo.19790406](https://doi.org/10.5281/zenodo.19790406)) — sent a referee-grade reading by correspondence (2026-07-15/16, author's mailbox, not in the repository) that found two issues: a citation of his preprint dropped its subtitle, and the paper's staircase-sharpness hedge (Theorem `thm:staircase`) was flagged as possibly reachable by a general construction. The author's reply committed, publicly, to two things for a v2: restoring the subtitle, and evidencing the hedge better without closing it ("the hedge stays in any v2 — better evidenced, not closed"). A delegated research session (`briefs/staircase-allp-brief.md`) then attempted the general construction and reached a documented **floor grade** — extended verified evidence plus two open gaps, not a proof — recorded in the project wiki at `cycles.md` §12.8.6. This v2 packages both commitments.

## Changelog (flat, three items)

1. **Subtitle restored.** The `merle` bibliography entry now carries the preprint's full title, including the subtitle v1 dropped: "...a conditional formal proof in Lean 4, **with documented structural obstructions**". The DOI was already correct and is untouched.
2. **Hedge-evidence note added.** A short, clearly-marked "Note added in v2 (July 2026)" follows Remark `rem:staircase` (the staircase-divergence link), reporting the floor-grade construction attempt: the recipe in one sentence, the verified range `p ∈ {2,...,21} ∪ {23}` with `γ/log₂(p) ∈ [1.828, 3.643]`, and the two open gaps (the `p = 22` obstruction; no closed-form guarantee the Diophantine step skips no period). **The theorem's hedge sentence itself is untouched, verbatim** — the note reports evidence, it does not upgrade the claim.
3. **Version line updated.** `\date` now reads "v2, July 2026" with a one-line version-history footnote. The existing Zenodo concept DOI is left as-is; no v2-specific DOI is invented (the author assigns that at upload, per standing convention).

No mathematical claim in the paper changes strength anywhere in this diff.

## Full unified diff (the content-edit commit)

Commit `383688cc4c4bff4f4f1625ee06540f81f3ddbdcc`, applied on top of a byte-identical seed copy of v1 (commit `1462774`, itself copied from the archived v1 at commit `4f5e843b3a1224a4926da0a32943466e355379bd`). This is the *entire* content diff between v1 and v2 — nothing else in the file differs.

```diff
diff --git a/paper/collatz-reduced-v2.tex b/paper/collatz-reduced-v2.tex
index 3d09b91..10c14b8 100644
--- a/paper/collatz-reduced-v2.tex
+++ b/paper/collatz-reduced-v2.tex
@@ -23,7 +23,7 @@
 
 \title{Reduced coordinates for the Collatz map:\\ exact per-step laws, anchor dynamics,\\ and the limits of counting arguments for cycles}
 \author{Ben Macindoe\thanks{\texttt{macindoebenjamin@gmail.com}. Developed through extensive AI-assisted research (Claude, Anthropic); the division of labor and the verification protocol are stated in Appendix~\ref{app:method}.}}
-\date{July 2026 \;\cdot\; DOI: \href{https://doi.org/10.5281/zenodo.21273548}{10.5281/zenodo.21273548}}
+\date{v2, July 2026 \;\cdot\; DOI: \href{https://doi.org/10.5281/zenodo.21273548}{10.5281/zenodo.21273548}\footnote{Version history: v1, July 2026 (original publication). v2, July 2026: restored the subtitle of the \texttt{merle} citation; added a note evidencing the sharpness hedge of Theorem~\ref{thm:staircase} (Section~\ref{sec:cycles}), prompted by correspondence with Eric Merle. No mathematical claim changes strength. The v2-specific Zenodo DOI is assigned at upload.}}
 
 \begin{document}
 \maketitle
@@ -213,6 +213,11 @@ No trim uniform in $p$ can extend the small-period constants: there exist config
 The staircase profile --- geometric depth growth with shallow exits --- is exactly the growth regime of divergent orbits. Size analysis cannot forbid it as a cycle for the same reason drift analysis cannot forbid divergence. The two halves of the residual difficulty meet in one configuration.
 \end{remark}
 
+\subsection*{Note added in v2 (July 2026)}
+Prompted by correspondence with Eric Merle on this theorem's sharpness hedge \cite{merle}, we attempted a general, non-per-period construction toward the assessed claim of Theorem~\ref{thm:staircase}. The recipe, in one sentence: semiconvergents of $\LL$ select the exponent $n$; a rounded geometric profile builds the climb; a bounded correction closes the last bits. Exact big-integer verification by this recipe produced a passing size-condition witness ($q \le R_r$ at every rotation) at every period
+\[ p \in \{2,\dots,21\} \cup \{23\}, \qquad \gamma/\log_2 p \in [1.828,\ 3.643] \]
+over that range, extending the two isolated instances above to a dense verified record. Two gaps remain open, and are recorded rather than closed: an unexplained combinatorial obstruction at $p = 22$, where the correction algorithm finds no passing configuration within the tested budgets; and the absence of a closed-form guarantee that the underlying Diophantine (semiconvergent) step never skips a period. The hedge sentence above is therefore unchanged: the claim remains assessed, supported by a substantially larger verified range, not proved, for all $p$. The construction, the verified instance record, and the obstruction's diagnosis are recorded at \texttt{cycles.md} \S12.8.6 of the project's public repository (\url{https://github.com/macindoe/collatz}).
+
 \section{The equidistribution hypothesis, made exact}\label{sec:aeh}
 
 Why is a product law the right comparison object? By Theorem~\ref{thm:onestep}, all dynamical decisions at horizon one are functions of the depth-$k$ window; the natural null model is therefore a measure on windows, and the natural choice of measure is forced by the structure: the $\w$-residues carry the anchor digits, for which Haar measure is the canonical reference (this is where the classical $2$-adic shift-conjugacy heuristics live), while the depth $d$ is \emph{dynamical} --- it is produced by Theorem~\ref{thm:depth} --- and so receives not Haar measure but the stationary law of the exact window chain. Let $\pi_k$ denote this product law. The class skeleton of the chain is computable exactly: e.g.\ from class $(\w\equiv1\ (8),\ d$ odd$)$ the next depth is exactly $1$ (since $m_+ = 1$, $a_+ = 0$ there), and from $(\w \equiv 5\ (8),\ d$ odd$)$, $P(\dnext \text{ even}) = \tfrac23$ exactly. Under $\pi_k$, unconditionally: $P(s = j) = 2^{-j}$ (four of eight classes give $s=1$, two give $s=2$, and the lifting shells are geometric); the $3$-gain rate is $\sum_{j\,\mathrm{even}} 2^{-j} = \tfrac13$ by Lemma~\ref{lem:absorption}; and the classical negative drift follows. The folklore ``ledger'' is thus a theorem \emph{about} $\pi_k$; the empirical question is only whether orbits follow $\pi_k$.
@@ -250,7 +255,7 @@ This work was developed through extensive AI-assisted research over three years
 \bibitem{bl} Y.~Bugeaud, M.~Laurent, \emph{Minoration effective de la distance $p$-adique entre puissances de nombres alg\'ebriques}, J.\ Number Theory 61 (1996), 311--342.
 \bibitem{rhin} G.~Rhin, \emph{Approximants de Pad\'e et mesures effectives d'irrationalit\'e}, S\'emin.\ Th\'eor.\ Nombres Paris (1987); see also Q.~Wu, Math.\ Comp.\ 72 (2003), 901--911.
 \bibitem{barina} D.~Barina, \emph{Improved verification limit for the convergence of the Collatz conjecture}, J.\ Supercomputing (2025).
-\bibitem{merle} E.~Merle, \emph{On the non-existence of non-trivial Collatz cycles: a conditional formal proof in Lean 4}, preprint, Zenodo DOI 10.5281/zenodo.19790406 (2026).
+\bibitem{merle} E.~Merle, \emph{On the non-existence of non-trivial Collatz cycles: a conditional formal proof in Lean 4, with documented structural obstructions}, preprint, Zenodo DOI 10.5281/zenodo.19790406 (2026).
 \bibitem{llmcollatz} \emph{Exploring Collatz Dynamics with Human--LLM Collaboration}, arXiv:2603.11066 (2026).
 \end{thebibliography}
```

## The added note, quoted in full

> **Note added in v2 (July 2026)**
>
> Prompted by correspondence with Eric Merle on this theorem's sharpness hedge [merle], we attempted a general, non-per-period construction toward the assessed claim of Theorem 4.6 (`thm:staircase`). The recipe, in one sentence: semiconvergents of log₂3 select the exponent *n*; a rounded geometric profile builds the climb; a bounded correction closes the last bits. Exact big-integer verification by this recipe produced a passing size-condition witness (*q* ≤ *R_r* at every rotation) at every period
>
> *p* ∈ {2, …, 21} ∪ {23}, γ/log₂ *p* ∈ [1.828, 3.643]
>
> over that range, extending the two isolated instances above to a dense verified record. Two gaps remain open, and are recorded rather than closed: an unexplained combinatorial obstruction at *p* = 22, where the correction algorithm finds no passing configuration within the tested budgets; and the absence of a closed-form guarantee that the underlying Diophantine (semiconvergent) step never skips a period. The hedge sentence above is therefore unchanged: the claim remains assessed, supported by a substantially larger verified range, not proved, for all *p*. The construction, the verified instance record, and the obstruction's diagnosis are recorded at `cycles.md` §12.8.6 of the project's public repository (https://github.com/macindoe/collatz).

## Build

Built with `pdflatex` (MiKTeX pdfTeX-1.40.28), two passes, in a temp directory outside the repository mount (a documented Windows quirk: the mount can lock LaTeX aux files) and copied into `paper/collatz-reduced-v2.pdf`. Output: 10 pages, matching v1's page count exactly. Title page, the new note (page 8), and the corrected Merle bibliography entry (page 10) were each rendered to PNG and visually inspected; all display correctly.

**Build obstruction (recorded, not blocking).** `pdflatex` exits with status 1 on *both* v2 and the pristine, unedited archived v1 source (`sources/paper/collatz-reduced-v1.tex`) — confirmed by a side-by-side rebuild of the archived v1 file, which reproduces the identical error signature at the identical relative location. The errors ("Missing $ inserted", "Extra }, or forgotten $", "Command \end{center} invalid in math mode") occur during `\maketitle`'s processing of the `\date`/`\thanks` fields and are auto-recovered by TeX's own error recovery ("Proceed, with fingers crossed"); the resulting PDF is complete and correct in both cases. This is toolchain version drift, not a defect introduced by the v2 edits: the archived v1.pdf's metadata records it was built with pdfTeX-1.40.22, and this machine's MiKTeX carries pdfTeX-1.40.28. Diagnostic detail: moving the added footnote between `\date` and `\title` (`\footnote` vs. `\thanks`) made no difference to the error, which confirmed it predates and is independent of the v2 edit.

**`latexdiff` obstruction (recorded, not blocking).** The `latexdiff` binary is present (MiKTeX-bundled) but non-functional in this environment: it fails at startup with `Can't locate Algorithm/Diff.pm in @INC (you may need to install the Algorithm::Diff module)`. Installing a new Perl module was judged out of scope for an editorial task (no network/package-manager action was taken). No marked-up diff PDF (`paper/collatz-reduced-v2-diff.pdf`) was produced. Per the brief's own fallback, the unified diff above is the deliverable in its place.

## Fidelity-check transcript (item 6)

This item introduces no new mathematics — the check is fidelity to `cycles.md` §12.8.6 and to v1, not proof. All three checks pass.

**(a) Every number in the added note appears verbatim in `cycles.md` §12.8.6.**

```
$ grep -n "2, ..., 21\|{2, 3, ..., 21}\|p = 22\|1.828\|3.643" cycles.md

cycles.md:8:  ...verified instances for `p ∈ {2,...,21} ∪ {23}`, with a combinatorial
              obstruction precisely located at `p = 22`...
cycles.md:258: p  ∈  {2, 3, ..., 21} ∪ {23},   with   γ / log_2 p  ∈  [1.828, 3.643]
cycles.md:263: **Obstruction (`p = 22`).** At `p = 22`, the bounded correction of
              `12.8.6.3` does not find a passing configuration within the tested
              budgets...
cycles.md:265: ...with the obstruction precisely located at `p = 22`...
```

The set `{2,...,21} ∪ {23}`, the value `22`, and the interval endpoints `1.828` and `3.643` all appear verbatim in `cycles.md` §12.8.6 (Proposition 12.8.6.4 and the paragraph immediately following it). **PASS.**

**(b) The hedge sentence in v2 is byte-identical to v1's.**

```
$ diff <(sed -n '/\\begin{theorem}\[sharpness: the staircase\]/,/\\end{theorem}/p' sources/paper/collatz-reduced-v1.tex) \
       <(sed -n '/\\begin{theorem}\[sharpness: the staircase\]/,/\\end{theorem}/p' paper/collatz-reduced-v2.tex)

(no output — identical)
```

The entire `thm:staircase` theorem environment, including the hedge clause ("we assess (supported by the verified instances, though not proved here for all `p`) that it passes all size conditions with `γ = O(log p)` for every `p`"), is byte-identical between v1 and v2. **PASS.**

**(c) The archived v1 is byte-identical to the original (SHA-256, both files).**

```
Recorded before the git mv (paper/collatz-reduced-v1.*):
  collatz-reduced-v1.tex  5f2a8d5c3866da8ffa2baa9fe881956661ce4c3c59a2afe99138e0041aa612b5
  collatz-reduced-v1.pdf  4bd0c36d16b711b99ca924822517c8a9685f5c38b18d9ea137cbff9b875feaa0

Recomputed after the git mv (sources/paper/collatz-reduced-v1.*):
  collatz-reduced-v1.tex  5f2a8d5c3866da8ffa2baa9fe881956661ce4c3c59a2afe99138e0041aa612b5
  collatz-reduced-v1.pdf  4bd0c36d16b711b99ca924822517c8a9685f5c38b18d9ea137cbff9b875feaa0
```

Both hashes match exactly, before and after the archive move. As a corollary, the v2 seed copy (`paper/collatz-reduced-v2.tex` immediately after item 2, before any edit) also hashed identically to both: `5f2a8d5c3866da8ffa2baa9fe881956661ce4c3c59a2afe99138e0041aa612b5`. **PASS.**

## Register check

The added note avoids "settles" / "establishes" / "confirms sharpness" and every other upgrade-implying word; it reports an attempt's floor-grade outcome ("assessed... not proved"), states the two open gaps without softening them, and repeats — twice — that the hedge is unchanged. This matches `AGENTS.md`'s register norm and `publication.md`'s ledger entry for the sharpness-hedge status.

## Off-brief findings

See `briefs/paper1-v2-findings.md`: paper 2 (`collatz-mirror-v1.tex`) carries the identical `merle` bibitem subtitle omission. Out of scope for this brief; logged only, not touched.

## Definition-of-done checklist

- [x] v1 archived byte-identical under `sources/paper/` (hashes above).
- [x] `paper/collatz-reduced-v2.tex` differs from v1 in exactly the two edits plus the version line (diff above is the complete diff).
- [x] A built v2 PDF (`paper/collatz-reduced-v2.pdf`, 10 pages) with the one pre-existing, non-blocking build obstruction recorded.
- [x] This self-contained review bundle.
- [x] Fidelity checks recorded (three for three, all pass).
- [x] Ledger sweep (item 7) — done in the commit immediately following this bundle.
- [x] Clean per-item commits on `paper1-v2`, no merge to `main`.

## Revision round (2026-07-16)

The pushed bundle above was read by an external reviewer (ChatGPT, 2026-07-16). The main session verified every checkable claim in that review against the ledger (`cycles.md` 12.8.6, `briefs/staircase-allp-findings.md`, `publication.md`) before delegating this round; the resulting brief (`briefs/paper1-v2-revision-brief.md`) corrected four of the review's recommendations against the ledger, and **where the brief and the external review differed, the brief won.**

### External verdicts adopted (register improvements, applied as suggested)

- **Per-period phrasing.** "a general, non-per-period construction" (self-contradictory against the wiki's own "general per-period construction recipe") replaced by "a single period-parametrized construction procedure... applied separately at each period."
- **`p = 22` softening.** "unexplained combinatorial obstruction" (internal delegation vocabulary, and a phrase that reads as inviting more compute) replaced by "a persistent unresolved case," carrying the neighbour-contrast fact (see pushback below).
- **Diophantine wording.** The gap statement was sharpened to name the actual missing object: "no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs — the bound that would certify no period is skipped."
- **Evidence calibration.** "supported by a substantially larger verified range, not proved" replaced by "supported by finite-range evidence consistent with the assessed `γ = O(log p)` behaviour, not a proof" — a more precise statement of what finite-range verification licenses.
- **"dense" removed.** "dense verified record" (internal informalism) replaced by "substantially extended verified range."
- **Declaration sentence.** "No mathematical claim changes strength" (not literally true — v2 adds new computational claims) replaced, everywhere it appeared, by "No theorem or universal claim is strengthened; v2 adds a finite computational evidence record."
- **Citation placement.** The note's opening clause now reads "Prompted by correspondence with Eric Merle, whose related formal work is cited in \cite{merle}, on this theorem's sharpness hedge" — separating the (undocumented) correspondence from the (documented, citable) preprint.
- **Version-note restructure.** The long footnote crowding `\date` is removed; `\date` is now a plain one-line date/DOI field, and an unnumbered "Version note" paragraph immediately after the abstract carries the version history.
- **Pinned URL.** The note's repository pointer now reads `https://github.com/macindoe/collatz/blob/b566e4d/cycles.md` (§12.8.6) — commit `b566e4d` is the `paper1-v2` branch point and contains the full 12.8.6 record, instead of the mutable root URL. **The author may re-pin this to a `paper1-v2` release tag at Zenodo upload time**, once one exists.

### Pushbacks applied (where the brief overrode the external review)

- **The `p = 22` neighbour-contrast requirement.** The external review's softening language, taken alone, would have read as ordinary budget-limitedness. The ledger (`briefs/staircase-allp-findings.md` §3, lines ~41–57) records that `p = 22` is **not resolved even with the move budget enlarged to 60 and the time limit removed**, across several `n` candidates and both crash depths — while `p = 24, 25` fail only the *default* budget and **are** resolved by a modest enlargement (8 moves each). This contrast is exactly what distinguishes `p = 22` from an ordinary budget artifact, so the brief required the note to carry it explicitly: "a persistent unresolved case at `p = 22`, which the present procedure fails to resolve under budgets that resolve all neighbouring periods, including with the search budget greatly enlarged." Softening without this contrast would have been a *loss* of information relative to the pre-revision note, not a register fix.
- **"never skips a period" was ledger-faithful, upgraded not retracted.** The phrase is `cycles.md` 12.8.6's own status language (12.8.6.1: "this is not the same as a proof that no period is ever skipped"), so it was not an error to begin with. The revision keeps its substance but states it in the more informative closed-form-bound language above, per the brief — an upgrade in precision, not a correction of a mistake.
- **`\ref{thm:staircase}` kept over a hardcoded number.** The external review's suggested replacement text hardcoded "Theorem 4.6." The theorem number is not stable under any future section reflow; `Theorem~\ref{thm:staircase}` was kept throughout, as in the pre-revision note.
- **Build-error localization corrected.** The external review's reading of the build obstruction is not reproduced here in detail because the localization was already correct in the prior bundle (the error occurs during `\maketitle`'s processing of `\date`, confirmed independent of the added footnote content by a diagnostic swap); this round's rebuild (below) reproduces the identical error signature after removing that footnote entirely, which is a stronger confirmation of the same conclusion, not a new one.

### Full unified diff of this revision round

Commits `cbb8628` (note rewrite, pinned URL) and `18fb898` (version-note restructure), applied on top of the previously reviewed tip (`4de619d`). This is the entire content diff of the revision round; the PDF rebuild (`77ee6b1`) is a binary artifact of these two commits and is not separately diffed.

```diff
diff --git a/paper/collatz-reduced-v2.tex b/paper/collatz-reduced-v2.tex
index 10c14b8..7a3dfb4 100644
--- a/paper/collatz-reduced-v2.tex
+++ b/paper/collatz-reduced-v2.tex
@@ -23,7 +23,7 @@
 
 \title{Reduced coordinates for the Collatz map:\\ exact per-step laws, anchor dynamics,\\ and the limits of counting arguments for cycles}
 \author{Ben Macindoe\thanks{\texttt{macindoebenjamin@gmail.com}. Developed through extensive AI-assisted research (Claude, Anthropic); the division of labor and the verification protocol are stated in Appendix~\ref{app:method}.}}
-\date{v2, July 2026 \;\cdot\; DOI: \href{https://doi.org/10.5281/zenodo.21273548}{10.5281/zenodo.21273548}\footnote{Version history: v1, July 2026 (original publication). v2, July 2026: restored the subtitle of the \texttt{merle} citation; added a note evidencing the sharpness hedge of Theorem~\ref{thm:staircase} (Section~\ref{sec:cycles}), prompted by correspondence with Eric Merle. No mathematical claim changes strength. The v2-specific Zenodo DOI is assigned at upload.}}
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
@@ -214,9 +217,9 @@ The staircase profile --- geometric depth growth with shallow exits --- is exact
 \end{remark}
 
 \subsection*{Note added in v2 (July 2026)}
-Prompted by correspondence with Eric Merle on this theorem's sharpness hedge \cite{merle}, we attempted a general, non-per-period construction toward the assessed claim of Theorem~\ref{thm:staircase}. The recipe, in one sentence: semiconvergents of $\LL$ select the exponent $n$; a rounded geometric profile builds the climb; a bounded correction closes the last bits. Exact big-integer verification by this recipe produced a passing size-condition witness ($q \le R_r$ at every rotation) at every period
+Prompted by correspondence with Eric Merle, whose related formal work is cited in \cite{merle}, on this theorem's sharpness hedge, we attempted a single period-parametrized construction procedure toward the assessed claim of Theorem~\ref{thm:staircase}: semiconvergents of $\LL$ select the exponent $n$, a rounded geometric profile builds the climb, and a bounded correction closes the last bits, applied separately at each period. Exact big-integer verification by this recipe produced a passing size-condition witness ($q \le R_r$ at every rotation) at every period
 \[ p \in \{2,\dots,21\} \cup \{23\}, \qquad \gamma/\log_2 p \in [1.828,\ 3.643] \]
-over that range, extending the two isolated instances above to a dense verified record. Two gaps remain open, and are recorded rather than closed: an unexplained combinatorial obstruction at $p = 22$, where the correction algorithm finds no passing configuration within the tested budgets; and the absence of a closed-form guarantee that the underlying Diophantine (semiconvergent) step never skips a period. The hedge sentence above is therefore unchanged: the claim remains assessed, supported by a substantially larger verified range, not proved, for all $p$. The construction, the verified instance record, and the obstruction's diagnosis are recorded at \texttt{cycles.md} \S12.8.6 of the project's public repository (\url{https://github.com/macindoe/collatz}).
+over that range, extending the two isolated instances above to a substantially extended verified range. Two gaps remain open, and are recorded rather than closed: a persistent unresolved case at $p = 22$, which the present procedure fails to resolve under budgets that resolve all neighbouring periods, including with the search budget greatly enlarged; and no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs --- the bound that would certify no period is skipped. The hedge sentence above is therefore unchanged: the claim remains assessed, supported by finite-range evidence consistent with the assessed $\gamma = O(\log p)$ behaviour, not a proof, for all $p$. The construction, the verified instance record, and the diagnosis of both gaps are recorded at \texttt{cycles.md} \S12.8.6 of the project's public repository (\url{https://github.com/macindoe/collatz/blob/b566e4d/cycles.md}).
 
 \section{The equidistribution hypothesis, made exact}\label{sec:aeh}
```

### Fidelity checks, re-run for this revision round

**(a) The `thm:staircase` theorem environment, including its hedge sentence, is byte-identical to v1 — unaffected by this revision round (the round only touches the `\date` field, the abstract-adjacent Version note, and the Note-added-in-v2 paragraph, none of which is inside the theorem environment).**

```
$ diff <(sed -n '/\\begin{theorem}\[sharpness: the staircase\]/,/\\end{theorem}/p' sources/paper/collatz-reduced-v1.tex) \
       <(sed -n '/\\begin{theorem}\[sharpness: the staircase\]/,/\\end{theorem}/p' paper/collatz-reduced-v2.tex)

(no output — identical)
```

**PASS.**

**(b) All numbers in the rewritten note appear verbatim in `cycles.md` §12.8.6.**

```text
$ grep -n "2, ..., 21\|{2, 3, ..., 21}\|p = 22\|1.828\|3.643" cycles.md

cycles.md:8:   ...verified instances for `p ∈ {2,...,21} ∪ {23}`, with a combinatorial
               obstruction precisely located at `p = 22`...
cycles.md:258: p  ∈  {2, 3, ..., 21} ∪ {23},   with   γ / log_2 p  ∈  [1.828, 3.643]
cycles.md:263: **Obstruction (`p = 22`).** At `p = 22`, the bounded correction of
               `12.8.6.3` does not find a passing configuration within the tested
               budgets...
cycles.md:265: ...with the obstruction precisely located at `p = 22`...
```

The set `{2,...,21} ∪ {23}`, the value `22`, and the interval endpoints `1.828` and `3.643` all still appear verbatim in `cycles.md` §12.8.6 (unchanged by this round — `cycles.md` was not touched). **PASS.**

**(c) Three new register greps, run against the rewritten note in `paper/collatz-reduced-v2.tex` (lines 216–219).**

```text
$ sed -n '216,219p' paper/collatz-reduced-v2.tex > /tmp/note.txt

$ grep -c "per-period\|period-parametrized" /tmp/note.txt
1

$ grep -c "non-per-period" /tmp/note.txt
0

$ grep -c "dense" /tmp/note.txt
0

$ grep -c "combinatorial obstruction" /tmp/note.txt
0
```

The note contains "per-period" (via "period-parametrized"), and contains none of "non-per-period", "dense", or "combinatorial obstruction". **PASS, all three.**

### Build (revision round)

Rebuilt with `pdflatex` (MiKTeX-pdfTeX 4.23, MiKTeX 25.12 — a newer MiKTeX release than the prior round's 1.40.28 build), two passes, in a temp directory outside the repo mount, copied into `paper/collatz-reduced-v2.pdf`. Output: **11 pages** (grew from the prior round's 10, from the relocated version-history prose now living in its own paragraph rather than a footnote). The Version note (page 1), the rewritten Note added in v2 (page 8), and the corrected Merle bibitem (page 11) were rendered to PNG and visually inspected; all display correctly and contain every language fix listed above.

`pdflatex` again exits with status 1, reproducing the identical error signature at the identical location (`Missing $ inserted` / `Extra }, or forgotten $` / `Command \end{center} invalid in math mode`, during `\maketitle`'s processing of `\date`, line 30) as both the prior round and the pristine archived v1. This round removes the footnote from `\date` entirely (rather than merely moving it, as the prior round's diagnostic swap did) — the error persists identically, which is a strictly stronger confirmation that the obstruction is pdfTeX-version drift independent of the `\date` field's content, not a new data point requiring re-diagnosis.

### Re-pin note

The repository pointer in the note is pinned to commit `b566e4d` (the `paper1-v2` branch point on the public remote), per the brief. **The author may re-pin this to a `paper1-v2` release tag at Zenodo upload time**, once the release exists, in place of the raw commit hash.

### Reviewer wording fixes (main session, 2026-07-16, disclosed)

Three small wording touches applied at review, none changing content: (1) the correspondence clause reordered so \cite{merle} no longer splits it ("Prompted by correspondence with Eric Merle on this theorem's sharpness hedge (his related formal work is cited in [merle]), ..."); (2) "substantially extended verified range" -> "nearly consecutive verified range" (removing the "extending...extended" redundancy); (3) the doubled "assessed" in the closing sentence reduced to one. PDF rebuilt after the fixes (11 pages; the pre-existing five-line toolchain error signature unchanged); all fidelity checks re-run on the final text (hedge byte-identity, cycles.md numbers, the three revision greps) — all pass.
