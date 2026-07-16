# Brief: paper 1 v2, revision round — external review applied with ledger corrections (for a delegated session)

**Context required before starting (in order):** `briefs/paper1-v2-brief.md` (the original v2 brief — its hard constraints all still bind), `paper/collatz-reduced-v2-review.md` on branch `paper1-v2` (the bundle the external reviewer read), `paper/collatz-reduced-v2.tex` on that branch, `cycles.md` 12.8.6 entire, `briefs/staircase-allp-findings.md` (especially the `p = 22` vs `p = 24, 25` budget paragraphs, lines ~50–57), `publication.md` (Sharpness-hedge + v2 status entry), `AGENTS.md`.

## Provenance

The v2 branch was reviewed externally (ChatGPT, 2026-07-16, reading the pushed bundle and the repository). The main session verified every checkable claim in that review against the ledger. Verdict: **minor-to-moderate revision, mostly accepted** — the review's two genuine catches are a fidelity error against the wiki ("non-per-period") and a citation-placement implication; several other points are register improvements consistent with house norms. Four of its recommendations were corrected against the ledger before reaching you; **where this brief and the external review differ, this brief wins.**

## What the revision must produce

All edits on branch **`paper1-v2`** (continue it; do not branch anew, do not merge to main). The `thm:staircase` theorem environment, including its hedge sentence, stays **byte-identical** — that constraint from the original brief is unchanged and will be re-checked at review.

### 1. Rewrite the "Note added in v2" (one commit)

Replace the current note with a version carrying the substance below. Language requirements, each verified against the ledger:

- **"a single period-parametrized construction procedure"** (or "a uniform algorithmic recipe, applied separately at each period") — NOT "general, non-per-period construction". The wiki says "general **per-period** construction recipe" (HANDOFF.md, cycles.md); the current note's "non-per-period" contradicts the ledger and is the revision's most important fix.
- **The `p = 22` sentence must carry the neighbour contrast**, not bare budget language. Ledger facts (`briefs/staircase-allp-findings.md`): `p = 22` is **not resolved even with the move budget enlarged to 60 and the time limit removed**, across several `n` candidates and both crash depths; `p = 24, 25` fail the default budget but **are** resolved by a modest enlargement — the contrast is exactly what distinguishes 22 from a budget artifact. Required shape: *"a persistent unresolved case at `p = 22`, which the present procedure fails to resolve under budgets that resolve all neighbouring periods, including with the search budget greatly enlarged."* Do NOT use "combinatorial obstruction" in the paper (house delegation vocabulary, wrong register for print), and do NOT imply it likely yields to more compute (the findings rule that reading out).
- **The Diophantine gap, merged wording.** The current "never skips a period" is cycles.md 12.8.6's own phrase, so it was not an error — but the more informative form is required: *"no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs — the bound that would certify no period is skipped."* (Both halves are verbatim-adjacent to cycles.md's own status paragraph.)
- **Evidence calibration:** *"finite-range evidence consistent with the assessed `γ = O(log p)` behaviour, not a proof."* Replace "dense verified record" with **"nearly consecutive verified range"** (or "substantially extended verified record") — "dense" is internal informalism, not print register.
- **Citation placement:** the correspondence is not documented by the preprint. Use *"Prompted by correspondence with Eric Merle, whose related formal work is cited in \cite{merle}, …"* or drop the cite from that sentence entirely (the bibliography entry stands on its own).
- **Theorem reference:** keep `Theorem~\ref{thm:staircase}` — never hardcode a number. (For your awareness: the published number is 4.6; the external review's replacement text hardcoded it, which is exactly the fragility to avoid.)
- Retain unchanged: the exact set `p ∈ {2,…,21} ∪ {23}`, the size-condition phrase (`q ≤ R_r` at every rotation), the exact interval `[1.828, 3.643]` (outward-honest endpoints; never re-round), and the two-gaps structure.

### 2. Restructure the version note (one commit)

Remove the long footnote from `\date`: plain date line (`v2, July 2026 · DOI …`), and an unnumbered **"Version note"** paragraph placed immediately after the abstract carrying the version history. Its claim-status sentence becomes: *"No theorem or universal claim is strengthened; v2 adds a finite computational evidence record."* (The current "No mathematical claim changes strength" is not literally true — the note adds new computational claims — and the same correction applies wherever the bundle says it.)

### 3. Pin the repository reference (same commit as 1 or separate)

The note's pointer to the public record must not be a mutable root URL. Pin it: `https://github.com/macindoe/collatz/blob/b566e4d/cycles.md` (§12.8.6) — commit `b566e4d` is on the public remote (the branch point of `paper1-v2`) and contains the full 12.8.6 record. Add one line to the review bundle noting the author may re-pin to a `paper1-v2` release tag at Zenodo upload time.

### 4. Rebuild the PDF (one commit)

Same procedure and known toolchain quirk as the original brief (build in a temp dir; the pre-existing exit-1 on pristine v1 is a toolchain-version artifact, already diagnosed — if it persists identically, note it and move on).

### 5. Update the review bundle (one commit)

Append a **"Revision round (2026-07-16)"** section to `paper/collatz-reduced-v2-review.md`: the external verdicts adopted (per-period phrasing; p=22 softening; Diophantine wording; evidence calibration; "dense"; declaration sentence; cite placement; version-note restructure; pinned URL) and the pushbacks applied (the p=22 neighbour-contrast requirement, with the findings-file facts; "never skips a period" was ledger-faithful, upgraded not retracted; `\ref` kept over the reviewer's hardcoded number; the build-error localization corrected). Include the full unified diff of this revision round in a fenced block, and re-run + transcribe the fidelity checks: hedge byte-identity v1↔v2, all numbers verbatim in cycles.md 12.8.6, plus three new greps — the note contains "per-period" (or "period-parametrized"), and contains neither "non-per-period" nor "dense" nor "combinatorial obstruction".

### 6. Ledger sweep (one commit)

`publication.md` v2-status sentence: extend with "revised after external review (register calibration; evidence record unchanged), pending author upload". `HANDOFF.md` item 2: same one-clause update. Off-brief findings, if any, to `briefs/paper1-v2-findings.md` (append; it exists).

## Rules (non-negotiable)

- The hedge sentence and the whole `thm:staircase` environment: byte-identical to v1. No new mathematical content anywhere; the note reports the same evidence record with corrected register.
- sources/ untouched. No Zenodo interaction. Paper 2 untouched.
- Register norm: flat, calibrated. The note is a finite computational evidence report with two named gaps; nothing in it "settles", "establishes", or "confirms".
- One commit per numbered item (items 1+3 may combine), on `paper1-v2`, no merge — the main session reviews (re-running every check) before pushing.
- No scope expansion; where the external review and this brief conflict, this brief wins.

## Definition of done

The rewritten note satisfying every language requirement in item 1; the version note relocated with the corrected declaration; the pinned URL; a rebuilt PDF or recorded obstruction; the bundle's revision-round section with diff and re-run fidelity checks including the three new greps; the ledger sweep; clean commits on `paper1-v2`.
