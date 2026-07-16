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
- [ ] Ledger sweep (item 7) — see the commit immediately following this one.
- [x] Clean per-item commits on `paper1-v2`, no merge to `main`.
