# Brief: land the repair history in the repository (v3 round 6, closing)

**Branch.** `v3r6-prune`, at `43e7db2`. Work in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

Last step of the round. Small, and then the branch merges.

## Why

The prune moved the version note's repair history out of the paper and pointed it at a Zenodo release description the author writes at publication. That left a gap the verify pass caught: **the v2 commit pin `72ec88e` and the six itemised repairs now exist nowhere in the repository** — only in this round's findings files, which are working documents, not the record.

**The author has decided the repository keeps a copy.** Zenodo still receives the same text at publication; nothing in the paper is to depend on a document that does not yet exist.

## The task

**1. Land the history.** Create one file holding the version history: v1, v2 with its commit pin `72ec88e` and its six itemised repairs, and v3 with what this cycle changed. The text exists — `briefs/v3r6-prune-design-findings.md` and `briefs/v3r6-prune-apply-findings.md` both carry blocks written for this purpose. **Use them, but verify every claim and every commit hash against the record before landing it**; they are working documents and this round has already found stale claims in three of them.

Placement is yours to argue, within two constraints: `AGENTS.md` bars change logs and dated journals from **wiki pages**, so it does not go there; and it describes the paper's versions, so `paper/` is the natural home. If you place it, and if the file constitutes a new class of tracked content, consider whether `AGENTS.md`'s Layers list needs one line — it says to update it when the structure changes. Do not restructure anything else.

**2. Point the version note at it.** Its closing sentence currently points at the release description alone. It should reach the repository copy, which exists now, as well as or instead of the Zenodo one. Keep it to a sentence — **do not re-expand the note**, which is the passage the round worked hardest to shrink.

**3. Optional, and only if it costs almost nothing.** The status paragraph at `paper` L231 uses "the target arc's length" and "an admissible exponent"; the v2 correction that defined them inline was cut, so a reader meets them undefined. The fix delegate left them deliberately, reasoning the paragraph reports a result proved elsewhere and cites `cycles.md` §12.8.6 with its URL in the same sentence group. **If a three-to-five word gloss makes them readable without re-expanding the paragraph, add it. If it cannot be done that cheaply, leave them and say so.**

**4. Commit the round's briefs.** Six round-6 brief and findings files are untracked. Commit them in their own `briefs:` commit, as the round's convention has been.

## The pin and the build

The version note is in the paper, so: commit the history file and any `AGENTS.md` line first, then the paper, then re-point Appendix A's pin to the commit containing both, in its own commit. Verify with `git show` — never the working tree — positively and negatively.

Rebuild with three `pdflatex -halt-on-error` passes. **Report the page count; it must stay at 15.** If a one-sentence pointer pushes it to 16, say so and stop rather than cutting something to compensate. Zero overfull boxes, no undefined references.

## Constraints

- **Branch `v3r6-prune` only.** `git add` and `git commit` permitted. **No push, no merge, no rebase, no branch switching, no worktree.**
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes `≤`, `—`, `ε`, `θ`, `τ`, `†`, `β`.
- **No change log, dated journal or "was X, now Y" prose in any wiki page.** The new file is a version history for the paper and is the one place that genre belongs; keep it factual and undated beyond version labels.
- Do not renumber any anchor. Do not touch any numbered theorem, Hypothesis 5.1, the two-sided law, the base-case statement, the `gathered` display, Related work, the author's note, or the verification protocol.
- Nothing may reintroduce the six retracted claims; sweep after editing.
- Every commit hash and every claim in the history verified against `git log` and the record, not copied on trust.

## Deliverable

The edits committed, plus `briefs/v3r6-history-findings.md`: where you placed the file and why, what you verified in the history text and what you corrected, the version note's new sentence, the L231 decision, the build report and page count, and the pin verification.

Your final message: where the history landed, what you corrected in it, the L231 decision, the page count, the pin and build, and anything you stopped on.
