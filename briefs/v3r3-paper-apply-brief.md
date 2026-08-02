# Brief: apply round 3 to the paper (v3 round 3, Wave 3, second of two)

**Branch.** `v3r3-review-round3`. Work directly in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

**You run after the record delegate.** The wiki is settled before you start: read `briefs/v3r3-record-apply-findings.md` and `git log` on this branch first, then read the pages themselves. **The record is the authority — where your drop-in text and the landed record disagree, the record wins and the disagreement is a finding you report, not one you resolve by editing the wiki.** You do not touch any file outside `paper/`.

**This is an edit task.** The design is settled across four findings files. Where you believe a drop-in is wrong, stop and report; do not improvise.

## Read first

1. `briefs/v3r3-record-apply-findings.md` — what actually landed, and its deviation list.
2. `briefs/v3r3-aeh-object-findings.md` §7.1–§7.3 (LaTeX drop-ins) and §3 (the definitions the paper must now use).
3. `briefs/v3r3-inselmann-horizon-findings.md` §5.4–§5.6.
4. `briefs/v3r3-cut-weighting-findings.md` §8.7–§8.10 and §9 (which of A's and B's LaTeX it supersedes).
5. `briefs/v3r3-basecase-density-findings.md` §5.5 and its collision notes.

**Apply order A → B → C → D**, later superseding earlier where the findings say so. One collision is yours specifically: **A's §7.3 reproduces the defective density sentence at L301–304; D's §5.5 is the merged replacement.** The record delegate was told to flag this in its handover — check that it did.

## The sites

- **L241** — the `\pi_k` paragraph. Must now use the settled observable and law, show the cap in the notation, name the norm, and keep the Theorem `thm:onestep` window as a separate object.
- **L243–257** — `hypothesis` environment. The strengthened all-block form; the bulk cut and cut sequence leave the statement.
- **L259–277** — the ensemble paragraph and the cut sentence.
- **L279–299** — the base case, in exponent time, with the lemma's honest qualifications.
- **L301–324** — the consequences; the density claim; what AEH supplies beyond the unconditional line.
- **L149–165** — `thm:deltaM` / `thm:onestep`, only if the settled definitions move the window sentence. **Theorem statements are not to be strengthened, weakened or renumbered.**
- **L59** — Related work, wherever it states what Inselmann crosses.
- **L326–332** — the Calibration paragraph. It currently ends "Bulk uniformity stands unqualified at all tested depths." Two ceilings are now on the record (block length, and the pooled-versus-per-start scope). Print what the campaign tested.

## Two things easy to miss

**The version note at L42.** It is a paragraph describing what v3 changed, and it currently describes the state before this round. v3 is **unpublished**, so this is not an erratum — the note should describe the paper as it now stands. Rewrite it to match. Keep the v2 material and the DOIs intact; the v3 DOI `10.5281/zenodo.21730505` is reserved, not published.

**G3, a round-2 leftover the author put in scope.** `briefs/v3r2-round-findings.md` records that the paper's §5 still carries a drift clause that `aeh.md` §13.3.2 contradicts — the recommendation was to delete it or restate it as "the classical negative drift is the mean of `\pi_k`". Round 2 left it because the PDF was pinned. It is not pinned now. Fix it.

## The build

The source is currently clean and must stay clean: three `pdflatex -halt-on-error` passes, no overfull boxes, no unresolved references, and the committed PDF's text matching the source. Rebuild, and report:

- pass/fail of each pass;
- overfull/underfull box warnings, with locations if any;
- unresolved references or citations;
- **the page count, before and after.** The PDF is 15 pages against an earlier 12-page request from the reviewer. The author has set no reduction mandate, so do not cut content to hit a target — but report the delta, and if the round grows the paper, say by how much and where.

Commit the rebuilt PDF along with the source. Verify by extracting the PDF's text that the round's new passages are actually present in the built artifact, not only in the `.tex`.

## Constraints

- **Only files under `paper/`.** If a change appears to require editing a wiki page, stop and report it.
- **Branch `v3r3-review-round3` only.** You may `git add` and `git commit` on it. **No push, no merge, no rebase, no branch switching, no worktree.** If a commit is refused, stop and report.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`. The `.tex` is ASCII-safe in most places but the findings files you are copying from are not.
- **No numbered theorem's claim may be strengthened, weakened, or renumbered.** The hypothesis is being restated by the author's decision; theorems are not.
- No change logs or running journals; the version note at L42 is a version note, not a diary.
- Every number, section reference and cross-reference must be verified against the source or the record, not recalled.
- Do not attempt to prove AEH, and do not extend any claim past what the findings files and the landed record support.

## Deliverable

The edits and the rebuilt PDF, committed on the branch, plus `briefs/v3r3-paper-apply-findings.md` containing:

1. a site-by-site table: line, delegate text applied, deviation and reason;
2. the build report, including the page-count delta and where the length went;
3. every place the paper and the landed record disagreed, and how you resolved it;
4. confirmation that no theorem statement changed, listing what you checked;
5. what you changed that no delegate specified, and why.

Your final message to the main session should be a compact summary: what landed, the build result, the page count, and anything you stopped on.
