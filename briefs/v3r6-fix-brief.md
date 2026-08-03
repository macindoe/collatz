# Brief: close the pruning round (v3 round 6, fix pass)

**Branch.** `v3r6-prune`, at `0e50afb`. Work in `c:\Users\Ace\Documents\Collatz` on that branch. **Do not create a worktree.**

**Work order:** `briefs/v3r6-verify-findings.md`, defects D1–D11. **D12 is excluded** — it is a release-process decision with the author and must not be touched; leave the version note's closing pointer exactly as it stands.

## The pattern behind D1 and D2, and what it means for your pass

Both are **regressions**: the pre-prune paper was right and the round broke it. Both entered the same way — not by deleting a block, but by **rewriting a sentence shorter**. Compression dropped words that looked redundant and were carrying the scope:

- **D1** (`paper` L399–400): `29ecb1b` cited "Inselmann `\cite[Cor.~1.4]`; his `\cite[Thm.~1.10]` is…" as two separate citations, so "two-sided, uniform in the time" attached only to Thm. 1.10. The prune merged them into `\cite[Cor.~1.4, Thm.~1.10]` and applied both adjectives to the pair. Cor. 1.4 is a one-sided descent statement at a single time. Restore the split; the apply delegate's version is endorsed by verify and by the main session.
- **D2** (L274): `29ecb1b` read "given mass `$0$` **by** `$\pi^{(L)}_{k,D}$`". The agent phrase went, so the sentence now reads as the *empirical* distribution giving the cemetery symbol zero mass — wrong, and vacuous. Restore the two words.

**So: for every passage this round condensed rather than deleted, diff it against its `29ecb1b` original and check for semantic loss, not just the two above.** Verify read for orphans and found these; a compression casualty that leaves a grammatical sentence is exactly what an orphan sweep can miss. Report anything further you find in that class before fixing it.

## The rest

- **D3** — the calibration limits disagree across four sites: `aeh.md`'s front matter names three, its own L8 and L151 name one, `README.md` L40 names two, `bridge.md` L71 names one. `AGENTS.md` forbids exactly this. Bring them into agreement with what the record establishes; the paper is currently the most conservative document and is the reference for what is true. **Wiki edit, separate commit from the paper.**
- **D4** — §6 refers to "the exact window chain"; the passage naming it was cut, so the paper never introduces it.
- **D5** — L230 sends the continued-fraction route to `§12.8.6.3`; it is at `12.8.6.1`, *Superseded formulation*. Verify against `cycles.md` before changing.
- **D6** — "by a stronger density notion" is now unexplained and unpointed; its gloss moved to `aeh.md` §13.3.2 with no pointer left behind.
- **D7** — Thm 1.6's content was removed while the paper still asserts "neither theorem supplies" the two-letter statistic.
- **D8** — *bottom regime* is italicised at first use (L298) and glossed only at its second (L422).
- **D9** — "has since been proved … at a scope and a shape stronger" appears twice, four lines apart, on p. 9.
- **D10** — the justification for `P(s=j)=2^{-j}` was cut without being itemised in the design's cut list, so that item's "wording only" label was wrong. Decide whether it must be restored, and say why either way.
- **D11** — a blank line before `\subsection*{Author's note}` was lost. Renders fine; restore for source hygiene.

## What must not move

Everything verify confirmed byte-identical stays byte-identical: every numbered theorem statement, Hypothesis 5.1, the two-sided law, the base-case statement, the round-5 `gathered` display, Related work, the author's prefatory note, the responsibility and verification protocol, Theorem 4.4's proof outline. Remark 3.6's landed narrowing is **endorsed** — leave it.

**Do not re-expand the paper.** These are repairs, not restorations of cut material; D4, D6 and D7 are to be closed with the fewest words that make the text correct, not by reinstating the passages that went. **Report the page count; if it moves off 15, say so rather than compensating with another cut.**

Nothing may reintroduce, in any wording: that AEH supplies the mean exponent past the digit budget; that it converts a horizon into blocks per bit; that the finite bound is about a word beginning at the sampled start; that bulk uniformity stands unqualified; that `13.6.4`'s union mass is exact; or any conditional drift consequence. **Sweep for all six after editing.**

## Pin and build

Wiki commit first, then the paper, then re-point Appendix A's pin to the commit containing both, in its own commit; verify with `git show` — never the working tree — positively and negatively. Rebuild with three `pdflatex -halt-on-error` passes; report passes, box warnings with locations, unresolved references, and the page count. The build must stay at zero overfull boxes with no undefined references.

## Constraints

- **Branch `v3r6-prune` only.** `git add` and `git commit` permitted. **No push, no merge, no rebase, no branch switching, no worktree.**
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes `≤`, `—`, `ε`, `θ`, `τ`, `†`, `β`.
- Do not renumber any anchor. Do not attempt the indexing standardization (`open-problems.md` 11.12). Do not claim the deferred prefix result.
- **Do not touch D12 or the version note's closing pointer.**
- No change logs or dated journals in tracked pages.
- Every number and section reference verified against the file, not recalled.
- **Fix only D1–D11, plus any further compression casualty you find** — report those before fixing, and fix them the same way.

## Deliverable

The edits committed, plus `briefs/v3r6-fix-findings.md`: the disposition of D1–D11; the result of your compression-casualty sweep, including anything new; the six-claim sweep after editing; the build report and page count; the pin and its verification; and anything found and not fixed.

Your final message: the disposition, any further regressions found, the page count, the pin and build, and anything you stopped on.
