# Brief: paper 1 v2, pre-upload update — the p = 22 resolution reaches the note (for a delegated session)

**Context required before starting (in order):** `briefs/paper1-v2-brief.md`, `briefs/paper1-v2-revision-brief.md`, and `briefs/paper1-v2-final-polish-brief.md` (every hard constraint in them still binds), `paper/collatz-reduced-v2.tex` and `paper/collatz-reduced-v2-review.md` on main (v2 is merged; nothing is on Zenodo yet), `cycles.md` 12.8.6 as of main (the updated record: contiguous range, resolved obstruction), `briefs/merle-pincer-check-findings.md`, `experiments/p22_passer.py`, `publication.md` (the flagged pre-upload line), `AGENTS.md`.

## Provenance

After v2 was merged (but before the author's Zenodo upload), a two-key exchange with Eric Merle resolved the `p = 22` case the note names as its first remaining gap: the failure was a candidate-generation gap in the Diophantine chain (his "pincer" hypothesis — cause confirmed), and at his named candidates outside the chain (`n = 25217`, `n = 31202`) the recipe's own recorded correction algorithm resolves in 13 and 8 moves. Both certificates are triple-verified (`experiments/p22_passer.py`, from Proposition 12.6.1 alone). The verified record is now the **contiguous** `p ∈ {2,…,23}`, interval `[1.828, 3.643]` unchanged (new ratios `2.508` and `3.307`, both inside). The paper's note is therefore stale in exactly one sentence-cluster, and the fix must land before upload. Source of truth for every number and claim: `cycles.md` 12.8.6 as of main commit `72ec88e`.

## Queue, in order (branch `paper1-v2-p22` from main)

### 1. Update the "Note added in v2" (one commit)

Three changes, nothing else in the tex:

- The displayed range becomes `p ∈ \{2,\dots,23\}` (contiguous), interval unchanged.
- Replace the two-gaps sentence-cluster. The current text names two gaps (the `p = 22` persistent case; the semiconvergent-gap bound). New content: **one remaining gap**, with the `p = 22` story told in one or two sentences — required shape: *initially the recipe's own candidate chain left `p = 22` unresolved; correspondence with Eric Merle identified the cause as a gap in that chain's coverage at the required scale (not a failure of the correction step), and at candidates outside the chain (`n = 25217`, `n = 31202`) the same recipe resolves it (13 and 8 correction moves), closing the range; the remaining gap is the one already named — no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs, the bound that would certify no period is skipped — and the `p = 22` episode is a demonstration that this gap bites in practice rather than only in principle.* Credit Merle plainly, in one clause (e.g. "identified in correspondence with Eric Merle"); no protocol narration, no "two-key" vocabulary in the paper.
- Re-pin the repository URL from `blob/b566e4d/cycles.md` to `blob/72ec88e/cycles.md` (a public main commit containing the updated §12.8.6).

Register requirements carried over from the revision rounds, all still binding: "period-parametrized"/"per-period" (never "non-per-period"), no "dense", no "combinatorial obstruction", no "persistent unresolved case" surviving anywhere in the note, hedge conclusions stay "assessed … not a proof", `Theorem~\ref{thm:staircase}` by reference only. The hedge sentence and the whole `thm:staircase` environment stay **byte-identical** to v1 (re-checked at review). The "Version note" after the abstract stays accurate as written (its description of v2's changes still covers this); touch it only if a sentence there becomes false, and then minimally.

### 2. Rebuild the PDF (one commit)

Same temp-dir procedure; same known pre-existing five-line toolchain signature; confirm page count and probe the changed sentences in the extracted text.

### 3. Refresh the review bundle as current-state (one commit)

`paper/collatz-reduced-v2-review.md` stays a current-state artifact: update the changelog (one added item: the p = 22 resolution reached the note pre-upload), regenerate the single complete v1→v2 diff, re-quote the final note, re-run and transcribe the fidelity checks — hedge byte-identity; every number in the note verbatim in cycles.md §12.8.6 (now including `25217`, `31202`, `13`, `8` if quoted, and `{2,\dots,23}`); the register greps extended by two (no "persistent unresolved case", no "combinatorial obstruction"). Keep the one-line revision acknowledgment, extended to cover this round ("…and a pre-upload factual update after the p = 22 resolution").

### 4. Ledger sweep (one commit)

`publication.md`: resolve the flagged pre-upload line (v2 updated, awaiting the author's Zenodo upload). `HANDOFF.md` item 2: one clause. Off-brief findings, if any, to `briefs/paper1-v2-findings.md` (append).

## Rules (non-negotiable)

- No new mathematical claims; the note reports the updated record with corrected register. sources/ untouched; paper 2 untouched; cycles.md and all wiki pages untouched; no Zenodo interaction; no push.
- One commit per item, on `paper1-v2-p22`, no merge — the main session reviews (re-running every check) before merging; upload stays with the author.
- Register norm: flat, calibrated. The resolution is an extension of a floor-grade evidence record; the hedge is unchanged; the sole remaining gap is stated without softening.

## Definition of done

The note updated exactly as specified with all register requirements passing; rebuilt PDF; refreshed current-state bundle with the extended fidelity transcript; ledger sweep; clean commits on `paper1-v2-p22`.
