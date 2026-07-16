# Brief: paper 1 v2, final polish — one sentence, and the bundle regenerated as a current-state artifact (for a delegated session)

**Context required before starting (in order):** `briefs/paper1-v2-brief.md` and `briefs/paper1-v2-revision-brief.md` (all hard constraints still bind), the branch `paper1-v2` at its current head (tex, PDF, bundle), `cycles.md` 12.8.6, `AGENTS.md`.

## Provenance

Second external review pass (ChatGPT, 2026-07-17): paper judged merge-ready; two residual items. The main session verified both against the branch: the reviewer's first sentence-level complaint was aimed at text **already fixed** at the previous review (the reviewer had read the bundle's stale embedded quote, not the tex) — which itself demonstrates the second item: the bundle's top half preserves superseded text under a "self-contained" heading, against the repository convention that tracked files state the current answer while history lives in git.

## Queue

### 1. Two sentence touches in the note (one commit)

In `paper/collatz-reduced-v2.tex`, "Note added in v2" only:

- `"correspondence with Eric Merle on this theorem's sharpness hedge"` → `"correspondence with Eric Merle concerning this theorem's sharpness hedge"` (one word; the parenthetical cite stays as is).
- The closing sentence `"the claim remains assessed, supported by finite-range evidence consistent with $\gamma = O(\log p)$ behaviour, not a proof, for all $p$."` → `"finite-range evidence supports the assessed $\gamma = O(\log p)$ behaviour, but does not prove it for all $p$."` — so the full sentence reads: *"The hedge sentence above is therefore unchanged: finite-range evidence supports the assessed $\gamma = O(\log p)$ behaviour, but does not prove it for all $p$."* Nothing else in the note changes.

### 2. Regenerate the review bundle as a current-state artifact (one commit)

Rewrite `paper/collatz-reduced-v2-review.md` from scratch as the review artifact for the branch **as it now stands** — not a history:

- current background paragraph and changelog (subtitle restored; hedge-evidence note added, register-calibrated; version history as a "Version note" after the abstract; repo pointer commit-pinned);
- **one final complete unified diff** of the v2 tex against archived v1 (`sources/paper/collatz-reduced-v1.tex`) — not the original diff plus a revision diff;
- the final note and the final Version note, quoted in full;
- the current build result (11 pages; the five-line pre-existing toolchain error signature, diagnosed as present on pristine v1);
- the final fidelity transcript, re-run fresh: hedge environment byte-identical to v1; the set `{2,...,21} ∪ {23}`, `22`, `1.828`, `3.643` verbatim in cycles.md §12.8.6; the three register greps (note contains "period-parametrized"; contains none of "non-per-period", "dense", "combinatorial obstruction");
- **one line** acknowledging that the note's wording was revised after two external review passes (register calibration; evidence record unchanged) — no verdict/pushback history, no superseded quotes; git holds the history.

Keep the bundle's self-containment promise honest: an external reader with no repository access gets only current statements.

### 3. Rebuild the PDF (one commit, or fold into 1)

Same temp-dir procedure and known toolchain quirk. Item 1's edits change rendered text, so the PDF must be rebuilt and the page count re-confirmed.

### 4. Ledger touch (one commit, only if needed)

`publication.md`/`HANDOFF.md` already say "revised after external review, pending author upload" — extend only if the wording no longer covers a second pass (a two-word touch at most).

## Rules (non-negotiable)

- The `thm:staircase` environment including the hedge sentence: byte-identical to v1 (re-checked at review).
- No other tex changes beyond item 1's two touches. No new content anywhere. sources/ untouched; paper 2 untouched; no Zenodo interaction; no push.
- Register norm: flat, calibrated.
- Work on branch **`paper1-v2`** (checkout in your worktree; do not pull, push, or merge). One commit per item as specified. The main session reviews, then pushes.

## Definition of done

The two sentence touches exactly as specified; the regenerated current-state bundle with one final diff and fresh fidelity transcript; the rebuilt PDF; the ledger touch if needed; clean commits on `paper1-v2`.
