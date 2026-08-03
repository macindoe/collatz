# Brief: apply the pruning plan (v3 round 6, apply)

**Branch.** Cut `v3r6-prune` from `main` at `29ecb1b` and work on it, directly in `c:\Users\Ace\Documents\Collatz`. **Do not create a worktree.**

**Work order:** `briefs/v3r6-prune-design-findings.md`. Its cut list, drop-in LaTeX and drop-in Markdown are settled. You land them.

## The author's decisions, which are binding

- **One paper. 15 pages. Typography unchanged** — the body stays at its current size and the margins stay as they are. The design pass established by compilation that 12–13 pages is reachable only by changing the type size, and the author has declined that. **Do not alter `\documentclass` options, margins, font sizes, or spacing to chase a page count.**
- **The repair history goes to the Zenodo release description.** It is published externally and the author writes it. Produce it as a plain-text block in your findings, ready to paste; the shortened version note points there.
- **The reviewer's literal calibration wording is declined**, in favour of the design pass's version, which keeps the improvement and names all three limits rather than folding them into "under the stated protocol".

## Order of work

**1. Land the paper-only material in the wiki first.** The `*`-density parenthetical describing what Inselmann's argument buys exists only in the paper and in round-3 brief files. Land the design pass's drop-in Markdown at `aeh.md` §13.3.2 **before** cutting it from the paper. One fact, one page (`AGENTS.md`). If for any reason it cannot land, keep the parenthetical in the paper and report.

**2. Fix the status-line asymmetry.** `aeh.md`'s status line names one calibration ceiling (`L ≤ 2`) where the paper names two — the block length and the pooled-versus-per-start scope. Bring the status line into line with what the record actually establishes. This is a status field, not a diary.

**3. Apply the cut list.** Every item in the design findings, using its drop-in text. Two items to handle exactly:

- **The version note** shrinks to one paragraph and its closing sentence points at the Zenodo release description.
- **The v2 staircase note and its correction** become one current-status paragraph. The design pass tabulated eleven claims from those blocks against their locations in `cycles.md` §12.8.6 — spot-check that table rather than trusting it, and confirm each claim survives in the record before the block goes.

**4. Do not cut beyond the list.** If the build comes in above 15 pages, **report it — do not find further savings.** The design pass compiled this plan and got 15; a discrepancy is information, not a problem to be solved by cutting.

## What must not move

- Any numbered theorem's statement — no strengthening, weakening, renumbering, or removal.
- Hypothesis 5.1, the two-sided law, the base-case statement.
- The round-5 `gathered` display, which is deliberately two lines to avoid an overfull box and carries the clause closing a silent step. **Byte-identical.**
- The Appendix A pin's format, the responsibility and verification protocol, the author's prefatory note.
- Related work, and Theorem 4.4's proof outline — the design pass recommends against cutting either, and the author has accepted the plan as designed.

**Nothing may reintroduce, in any wording:** that AEH supplies the mean exponent past the digit budget; that it converts a horizon into blocks per bit; that the finite bound is about a word beginning at the sampled start; that bulk uniformity stands unqualified; that `13.6.4`'s union mass is exact; or any conditional drift consequence. **After the cuts, sweep the paper for all six** — a deletion can strand a qualification as easily as a claim.

## The pin and the build

Commit the wiki changes first, then the paper, then re-point Appendix A's pin to the commit containing both, in its own commit. Verify with `git show` — never the working tree — positively and negatively.

Rebuild with three `pdflatex -halt-on-error` passes. Report every pass, all box warnings with locations, unresolved references or citations, and the page count. **The build must be at least as clean as it is now: zero overfull boxes, no undefined references.** Confirm from the built PDF's text that the cut passages are gone and the replacements present.

## Constraints

- **Branch `v3r6-prune` only.** `git add` and `git commit` permitted. **No push, no merge, no rebase, no branch switching, no worktree.**
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes `≤`, `—`, `ε`, `θ`, `τ`, `†`, `β`.
- Do not renumber any anchor. Do not attempt the indexing standardization (`open-problems.md` 11.12). Do not claim the deferred prefix result. Change nothing in `13.3.2` beyond the `*`-density addition.
- No change logs or dated journals in tracked pages. The paper's version note is a version note.
- Every number and section reference verified against the file, not recalled. Five rounds have rewritten §5; earlier findings' quotations are stale.

## Deliverable

The edits committed, plus `briefs/v3r6-prune-apply-findings.md`:

1. item-by-item disposition of the cut list, with any deviation and its reason;
2. your spot-check of the eleven-claim survival table;
3. the six-claim sweep result after cutting;
4. **the plain-text repair history, ready for the author to paste**;
5. the build report and the page count, with an explanation if it is not 15;
6. the pin and your verification of its claim;
7. anything you found and did not fix.

Your final message: the page count, what landed, the sweep result, the pin and build, and anything you stopped on.
