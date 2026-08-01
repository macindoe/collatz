# Brief: apply round 2 to the paper (v3 round 2, Phase 2 — paper only)

**You edit exactly one tracked file: `paper/collatz-reduced-v3.tex`** (plus the PDF it builds). A sibling delegate is editing the wiki pages in the same working tree at the same time. Do not touch any `.md` file, and **run no `git` command of any kind** — no add, commit, branch, checkout, stash, status-changing operation, or push. The main session handles all version control.

## Where the decisions live

Five delegates produced this round's decisions. **Read these findings files and use their drop-in text**; do not re-derive or re-word their conclusions.

| file | supplies |
|---|---|
| `briefs/v3r2-aeh-formulation-findings.md` | §6.1 hypothesis + explanatory paragraph; §6.2 L247; §6.3 version-note clause |
| `briefs/v3r2-staircase-scope-findings.md` | §4 Edits 1–6 (Theorem 4.6, the new paragraph, the correction clause, three version-note sentences) |
| `briefs/v3r2-contraction-literature-findings.md` | Korec/Tao/Inselmann `\bibitem`s, Related-work sentence, the L247 replacement |
| `briefs/v3r2-syrac-identity-findings.md` | §9 — the `\bibitem{tao}` and the replacement for the paper's L239 clause |
| `briefs/v3r2-wirsching-check-findings.md`, `briefs/v3r2-thomas-check-findings.md` | optional Wirsching/Thomas `\bibitem`s and the related-work paragraph |

Where two findings files touch the same sentence, the later decision wins; the decision record is §"Decisions taken" below.

## Decisions taken (authoritative — these override any findings file that predates them)

1. **Staircase: the MINIMAL option.** Theorem 4.6 keeps its number and claim. No renumbering. Abstract and Contributions untouched.
2. **AEH: the ensemble form** of `v3r2-aeh-formulation-findings.md` §3.
3. **The descent/contraction consequence is DROPPED, and the drift rider with it.** This supersedes `v3r2-aeh-formulation-findings.md` §6.2's conservative variant and its rider proposal. Reason: Inselmann (arXiv:2402.03276) Cor. 1.4 proves the same conclusion unconditionally at natural density 1, so a conditional version carries nothing. Use `v3r2-contraction-literature-findings.md`'s recommended replacement for L247.
4. **Section 5 is reframed** around what survives: the exactness of `π_k`, the per-step laws, and equidistribution persisting *past the digit budget*. The ledger's fixed-window form is classical Terras and its first moment is unconditional — say so rather than claiming them.
5. **`13.6.5`'s law is Tao's `Syrac(Z_3)/2`.** Attribution is owed at the paper's `π_k` paragraph (L239). Correctness is unaffected — do not alter any value.
6. **Wirsching and Thomas are cleared.** Neither displaces Tao, neither touches the product law. Cite both anyway, briefly, in related work — a referee following Tao's footnote will find them, and answering pre-emptively reads as command of the literature.

## The work

**A. Section 5 (`sec:aeh`).**
- Replace `hyp:aeh` and its explanatory paragraph (L241–245) with §6.1's drop-in.
- Replace L247 per decision 3.
- L239: add the Tao attribution (`v3r2-syrac-identity-findings.md` §9), state that `π_k`'s **joint labelled law** — including `a_+`, which the finite `2`-adic residue window does not determine — is the Bernoulli construction of `aeh.md` `13.6.3`(v), and fix the grammatical error: it is the distribution of `d = m + a` that is the convolution, **not** the distribution of `a_+`.
- Consider adding the digit-budget/cylinder observation from `v3r2-aeh-formulation-findings.md` §4: `E[m+r] = 4` per block is the same `4` as Heuristic~\ref{prop:budget}'s `σ ≈ 4.0`, and the calibration record runs `2.3×`–`4.3×` past that budget, so it tests the hypothesis rather than re-measuring a theorem. **State the `θ < 1/4` frontier as the classical one** (it is Korec's exponent: `1 − β/4 = log₄3` identically) — not as a discovery of this project, and not with the "79% untouched" framing, which overclaims.

**B. Theorem 4.6 area.** Apply Edits 1, 2, 3 of `v3r2-staircase-scope-findings.md` §4 exactly as printed.

**C. Heuristic 3.9 (`prop:budget`, L168).** Delete the final sentence, "The consumption identity of the first two sentences is proved; only the conclusion drawn from it is the organizing heuristic." Nothing replaces it. Reason: the second sentence is not a formal identity, and the accounting omits the exact `3`-adic label `a_+`.

**D. Bibliography and related work.**
- Add `\bibitem`s for Korec, Tao, Inselmann (required) and Wirsching, Thomas (brief, per decision 6). Use the drafted entries. **Inselmann has no journal reference and its title differs between arXiv metadata and title page — follow `v3r2-contraction-literature-findings.md`'s note.**
- Add the related-work sentence(s) at L59.
- **Page-13 orphan:** the bibliography currently spills two lines onto a 13th page. Reduce the bibliography font (`\small`, or `\footnotesize` if `\small` is insufficient) to recover a 12-page ending. Adding five entries makes this harder — if 12 pages is unreachable without dropping below `\footnotesize`, stop at `\footnotesize`, report the page count, and do not delete or truncate any citation.

**E. Version note (L42).** This line takes **five** separate edits: Edits 4, 5, 6 of the staircase findings, plus `v3r2-aeh-formulation-findings.md` §6.3, plus the item count. Apply them as **string-match edits on whole sentences, re-reading the line between each** — never as a line replacement.
- The clause "Hypothesis~\ref{hyp:aeh} states the order of its two limits" is now false and must go.
- The note must describe what v3 actually does now, including the dropped consequence and the added attributions.
- **The count is wrong and was wrong before this round:** it says "four defects and three statements" (seven) and lists eight. Recount against the final list and state a correct number, or drop the count.

**F. Sweep.** L175 and L259 say "typical orbits"; the hypothesis is now about typical *starting values*. Fix both. Check for any other site that describes AEH's sample space or its consequences and bring it into line.

## Build and report

Two `pdflatex -halt-on-error` passes. Report: overfull/underfull boxes, undefined references, final page count, and whether the 12-page ending was achieved. Do not hand back a paper that fails to compile.

## Constraints

- **Only `paper/collatz-reduced-v3.tex` and its built PDF.** No `.md` file, no `experiments/`.
- **No `git` commands at all.**
- Write with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection.
- Do not renumber any theorem, and do not remove any `\label`.
- Do not alter any numerical value, constant, or verification figure anywhere in the paper.
- Match the surrounding prose register. This paper has a distinctive voice; drop-in text was drafted to match it.

## Report back

What you changed site by site; the build result; anything in a findings file you could not apply as printed and what you did instead; and anything you noticed that is wrong but out of scope.
