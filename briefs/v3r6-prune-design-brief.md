# Brief: the pruning plan (v3 round 6, design)

**Round.** The fifth external review's pruning assessment, at `main` = `29ecb1b`. The mathematics is settled: four rounds of corrections have closed, and the reviewer's verdict is that the conceptual work is done and only length remains.

**This is a design task, not an edit task.** Produce a cut plan and drop-in text; change nothing. A separate delegate applies it.

**Target: 12–13 pages, from 18.** The reviewer judges this achievable without removing structural content.

## The reviewer's plan

> * Reduce the two-page version note to a short paragraph and put the full repair history in the release description.
> * Replace the original staircase note followed by its correction with one current-status paragraph.
> * Keep AEH's definition, two-sided law, and base-case statement; move most Chernoff algebra, time-unit discussion, and calibration qualifications back to `aeh.md`.
> * Change "uniformity stands unqualified" to "no residual discrepancy was detected within the tested `L ≤ 2` cells under the stated protocol." The current sentence immediately follows itself with three substantial qualifications.
> * Shorten the abstract, which is currently carrying almost the entire paper's argument.
> * These cuts will also eliminate the nearly empty final bibliography page.

Treat this as a strong starting proposal, not a specification. Where you think a cut costs more than it saves, say so with a reason.

## The two hazards

**1. "Move back to `aeh.md`" mostly means "delete from the paper."** Most of this material originated in the wiki and was summarized into the paper; a few passages were written for the paper and exist nowhere else. **For every candidate cut, establish which it is before proposing it**, and record the evidence — the `aeh.md` section and the sentences that carry it. Anything that exists *only* in the paper must either stay, or be given drop-in text landing it in the wiki first. Nothing may simply vanish.

**2. §5 is where every round's corrections live, and it is where the cutting is heaviest.** Four rounds removed a claim that AEH supplies the mean exponent, scoped the conversion to below the digit budget, corrected the finite bound to the extended `(n+1)`-letter word, and narrowed the calibration claim. A cut that removes a qualification, or restores a summary written before those corrections, silently reintroduces them.

**So: for every cut in §5, state what corrected content it touches and why the correction survives it.** The specific claims that must not come back, in any wording:

- that AEH supplies `E_B[m+r] = 4`, or the empirical exponent mean, past the digit budget;
- that AEH converts a horizon into blocks per bit, or carries Inselmann's endpoint into block units;
- that the finite bound is about a word beginning at the sampled start (it is the extended `(n+1)`-letter word);
- that bulk uniformity stands unqualified (the campaign reaches block length `L ≤ 2` and its flagship estimates are pooled);
- that the union-bound mass in `13.6.4` is exact;
- any conditional drift consequence (deferred; `open-problems.md` 11.12 and the round-4 open items).

## Where the pages are

Establish this yourself rather than trusting an estimate: measure the current 18 pages by section, and attribute the target reduction to specific passages with expected savings. A plan that names cuts without saying where the pages come from cannot be checked.

Note two structural facts. The bibliography's last page is nearly empty, so a modest body reduction removes a whole page at no cost to content. And the round-5 display is a two-line `gathered` construction that was widened deliberately to avoid an overfull box — **do not propose re-tightening it**; the clause it carries closes a silent step.

## What must not be touched

- Any numbered theorem's statement — no strengthening, weakening, renumbering, or removal.
- Hypothesis 5.1, `13.2.4`'s statement as reflected in the paper, and the two-sided law.
- The Appendix A pin, the responsibility and verification protocol, and the author's prefatory note.
- The declined-notation decision from round 5: the paper carries one exponent sum for the base case and it is the right one.

## The version note and the release description

The reviewer wants the repair history moved out of the paper and into the release description. **The release description is published externally and is the author's to write** — you cannot land it. So produce two things: the short version note as drop-in LaTeX, and, separately, the full history as a plain-text block the author can paste wherever they choose. Do not assume where it goes.

## Deliverable

Write **only** `briefs/v3r6-prune-design-findings.md`:

1. the current page budget by section, measured;
2. the cut list, each item with: what goes, expected saving, where the content survives (`aeh.md` section and sentences, or "paper only — must be landed first, drop-in below"), and for §5 items what corrected content it touches and why the correction survives;
3. **exact drop-in LaTeX** for every replacement passage — the version note, the staircase status paragraph, the calibration sentence, the abstract, and each condensed §5 passage;
4. **exact drop-in Markdown** for anything that must land in `aeh.md` first;
5. the plain-text repair history for the author;
6. the projected page count, with your confidence in it;
7. anything the reviewer proposes that you recommend against, with reasons;
8. anything you could not settle.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file.
- No `git` write operations. You are on `main` at `29ecb1b`; do not branch or commit.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes `≤`, `—`, `ε`, `θ`, `τ`, `†`, `β`.
- Do not renumber any anchor. Do not attempt the indexing standardization (`open-problems.md` 11.12). Do not claim the deferred prefix result.
- **Read the current text.** Five rounds have rewritten §5 and much of `aeh.md` §13; quotations in earlier findings files are stale and several are known wrong.
- Every number and section reference verified against the file, not recalled.
