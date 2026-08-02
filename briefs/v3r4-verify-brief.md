# Brief: verify round 4 (v3 round 4, last gate)

**Branch.** `v3r4-review-round4`, at `3c30b61`. `main` is `fa9edf5`. Work in `c:\Users\Ace\Documents\Collatz` on the branch. **Do not create a worktree.**

**Read-only on every tracked file** except your findings file. You may run code and rebuild the PDF. **Do not fix anything — report it.** A fix applied by the verifier is a fix nobody verified.

Round 4 is a **subtraction**: the record and paper must say *less* about what AEH supplies. Your job is to find where it still says too much, and to check the one thing the round added.

## Read

`git log fa9edf5..HEAD` and the full diff. `briefs/v3r4-clock-findings.md` (the design) and `briefs/v3r4-apply-findings.md` (what landed, including its §6 list of five things found and not fixed).

## 1. The addition — check it as mathematics, not as text

`13.2.4`(g) is new, and it is an **unconditional theorem**: that the two clauses of admissibility are exactly the two terms of the base case's total-variation bound, so the budget does not bind and the exponent mean converges to `4`, for every `θ < 1/4`.

Nobody has checked this except the delegate that derived it and the delegate that landed it. Do it independently:

- Derive the claim yourself. Does the total-variation bound transfer the budget event as claimed? Is the stated rate `I(θ,τ) = τ(log 2 − H(2θ/τ))` correct, positive exactly when `τ > 4θ`, and equal to the record's printed `I(θ)` at `τ = 1`?
- Is the density bound in (g) right, including the `δ_N(τ)` term and the concentration term?
- Does Corollary `13.2.4.1` now follow, with its quantification over `τ`?
- **`AGENTS.md` requires an independent numerical check before anything is marked proved,** recorded as one current line in the owning page. `13.2.4`'s Verified line covers the earlier parts. Check whether (g) is covered by it. If it is not, that is a compliance defect and you should say so, and — since you may not fix it — state exactly what check would close it. Write and run that check yourself in the scratchpad so the finding is evidenced rather than asserted.

## 2. Did the retracted claim actually leave?

The blocker was that pattern genericity does not supply the unbounded moment. Sweep the whole record and paper for surviving instances, in any wording: that AEH gives the mean exponent, that zero cemetery mass implies the budget is met, that AEH converts Inselmann's endpoint into blocks per bit, or that the block-unit endpoint is carried by the hypothesis.

**Two specific sentences the apply delegate flagged and did not fix. Adjudicate both; do not inherit its verdict.**

- `aeh.md` `13.3.2`: "the endpoint `1/β` in block units is this page's own hypothesis, not his theorem." Read in context this may be about *attribution* — distinguishing our claim from Inselmann's — but as printed it asserts the page's hypothesis carries the block-unit endpoint, which is what round 4 retracted. Which is it, and does the sentence need to change?
- `paper` L433: "…consequence of Hypothesis~\ref{hyp:aeh} and not available to underwrite it." Read the full sentence and say whether it is consistent with L397–400, which correctly says the conversion is a theorem below the cylinder count and neither a theorem nor a consequence of the hypothesis past it.

## 3. Was the deferral honoured?

The author deferred the prefix result and the `13.3.2` rescoping. Check that:

- `13.3.2` is byte-identical to `fa9edf5` except where the round's *other* corrections legitimately touched it;
- nothing anywhere claims the prefix result or a conditional drift;
- `open-problems.md` 11.11 states **two checkable questions** and claims neither, and points at the drafted argument.

The apply delegate also left `aeh.md` L8, `paper` L246 and `publication.md` L41 unedited, reasoning that the design's drop-ins for them consisted solely of the deferred clause. **Verify that reasoning** — read each of those three sites and confirm it reads correctly with the prefix result absent, rather than still carrying the retracted claim.

## 4. The pin, the build, the pages

- The pin names `e634513`. Verify the claim independently: extract the sections and scripts the paper names from the `.tex` itself, and check each against `git show e634513:` — positively (present) and negatively (the retracted sentences absent, `13.2.4`(a) sharp, `13.6.4` reading "at most").
- Rebuild from clean, three `pdflatex -halt-on-error` passes. Report passes, box warnings with locations, unresolved references, page count, and whether the rebuilt PDF is content-identical to the committed one.
- **Render pages to images and look at them.** `13.2.4`(g) and the restated paragraphs are new text; a bad break or a broken display would not show in extracted text.

## 5. Housekeeping

Cross-page consistency per `AGENTS.md`'s status pass, over every page the round touched. UTF-8 integrity of `≤ — ε θ τ † β`. No renumbered anchors. No change logs or dated journals in tracked pages. No theorem statement strengthened, weakened or renumbered in the paper. And check the apply delegate's other three unfixed items are genuinely harmless.

## Deliverable

Write **only** `briefs/v3r4-verify-findings.md`:

1. a defect list, most severe first, each with what is wrong, where, and what would fix it;
2. your independent derivation and verdict on `13.2.4`(g), plus the numerical check you ran and its numbers;
3. verdicts on the two flagged sentences and on the three unedited sites;
4. the pin verification, the build report, and the rendered-layout report with page numbers;
5. **a merge recommendation** — merge as-is, merge after named fixes, or do not merge — with reasons;
6. what you could not check, named plainly. Mandatory; must not be empty unless you genuinely checked everything.

## Constraints

- Read-only on tracked files; scratch code to `C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\7ee86884-4e62-4eca-b73c-3d997568403a\scratchpad`
- Rebuilding will modify `paper/*.aux`, `*.log`, `*.pdf`. Expected; **do not commit them**.
- No `git` write operations of any kind.
- Never `Get-Content | Set-Content` or PowerShell redirection.
- Every number you report is one you read or computed, not recalled.
