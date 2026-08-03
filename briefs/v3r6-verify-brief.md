# Brief: verify the pruned paper (v3 round 6, last gate)

**Branch.** `v3r6-prune`, at `0e50afb`. `main` is `29ecb1b`. Work in `c:\Users\Ace\Documents\Collatz` on the branch. **Do not create a worktree.**

**Read-only on tracked files** except your findings file. You may run code and rebuild. **Do not fix anything — report it.**

This round removed roughly three pages of prose from a paper carrying five rounds of corrections. **The characteristic failure of a pruning pass is not a wrong claim but an orphaned one**: a qualification whose subject was cut, a cross-reference to a deleted passage, a "as noted above" pointing at nothing, a claim that was scoped by a sentence that is now gone. Hunt those.

## Read

`git log 29ecb1b..HEAD` and the full diff. `briefs/v3r6-prune-design-findings.md` (the plan), `briefs/v3r6-prune-apply-findings.md` (what landed, its deviations and its handed-back items).

## 1. Read the pruned paper end to end

Not a diff — the whole document, as a reader would. Then report:

- every cross-reference, "above"/"below", or forward pointer that no longer resolves;
- every claim whose scoping sentence was removed;
- any passage that now reads as a non-sequitur because its connective tissue went;
- anything that reads as introduced-but-never-used, or used-but-never-introduced.

## 2. The six-claim sweep, independently

None of these may appear in any wording. Sweep the paper yourself; do not inherit the apply delegate's result.

- AEH supplies the mean exponent, or `E_B[m+r] = 4`, past the digit budget;
- AEH converts a horizon into blocks per bit, or carries Inselmann's endpoint into block units;
- the finite bound is about a word beginning at the sampled start (it is the extended `(n+1)`-letter word);
- bulk uniformity stands unqualified;
- `13.6.4`'s union-bound mass is exact;
- any conditional drift consequence.

Note the apply delegate reports it verified two of three copies of the block-time correction were present *before* cutting the third. Confirm the survivors say what the cut one said.

## 3. Two known items — confirm and assess, do not fix

Both were handed back by the apply delegate and confirmed by the main session:

- **`paper` L399–400** cites Inselmann's `[Cor.~1.4, Thm.~1.10]` and calls the pair "two-sided". Cor. 1.4 is the one-sided descent statement; only Thm. 1.10 is the envelope. `briefs/v3r3-inselmann-horizon-findings.md` read the source — check against it. Say what the minimal correct repair is.
- **`aeh.md` L8 and L151** name one calibration limit (`L ≤ 2`) while the same page's status line now names three. An internal inconsistency in one page, which `AGENTS.md`'s status discipline forbids. Say what should change, and whether the paper or the wiki is now the more conservative document.

## 4. What must not have moved

Verify each, by comparison against `29ecb1b`:

- every numbered theorem's statement — no strengthening, weakening, renumbering or removal;
- Hypothesis 5.1, the two-sided law, the base-case statement;
- the round-5 `gathered` display — **byte-identical**;
- the responsibility and verification protocol, and the author's prefatory note;
- Related work, and Theorem 4.4's proof outline.

Also check the apply delegate's one deliberate deviation from the settled drop-in — it narrowed a Remark 3.6 clause about which branches make `a_+` a `3`-adic function of `ω`, on the grounds that Lemma 3.4 supports only the boundary branch. Adjudicate: was the design's text wrong, and is the landed text right?

## 5. The eleven-claim survival table

Nearly a page was removed on the strength of a table showing eleven claims survive in `cycles.md` §12.8.6. The apply delegate spot-checked it. **Check it yourself, in full** — all eleven, each located in the file. This is the only evidence that content was moved rather than lost.

## 6. Build, layout, pin

- Rebuild from clean, three `pdflatex -halt-on-error` passes. Report passes, box warnings with locations, unresolved references, page count, and whether the rebuilt PDF is content-identical to the committed one.
- **Render every page to an image and look at it.** Cuts move page breaks, and this is where the damage shows: a heading stranded at a page foot, a display split, a widow, an equation running into a margin. Report with page numbers.
- Verify the pin `881c92e` with `git show` — never the working tree — positively and negatively, covering every wiki section and script the paper names.

## 7. Housekeeping

Cross-page consistency per `AGENTS.md`'s status pass over every page the round touched. UTF-8 integrity of `≤ — ε θ τ † β`. No renumbered anchors. No change logs in tracked pages. And confirm the two passages the design pass identified as paper-only and deliberately kept — the `1 − β/4 = log₄3` identity and Wirsching's "siblings in shape" comparison — are still present.

## Deliverable

Write **only** `briefs/v3r6-verify-findings.md`:

1. a defect list, most severe first, each with what is wrong, where, and what would fix it;
2. the orphan report from your end-to-end read;
3. the six-claim sweep result;
4. the eleven-claim table, checked;
5. verdicts on the two known items and on the Remark 3.6 deviation;
6. the build, layout and pin reports;
7. **a merge recommendation** — merge as-is, merge after named fixes, or do not merge;
8. what you could not check. Mandatory.

## Constraints

- Read-only on tracked files; scratch to `C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\7ee86884-4e62-4eca-b73c-3d997568403a\scratchpad`
- Rebuilding modifies `paper/*.aux`, `*.log`, `*.pdf` — expected; **do not commit them**.
- No `git` write operations of any kind.
- Never `Get-Content | Set-Content` or PowerShell redirection.
- Every number you report is one you read or computed, not recalled.
