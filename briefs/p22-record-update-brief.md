# Brief: recording the p = 22 resolution — cycles.md 12.8.6 update and ledger sweep (for a delegated session)

**Context required before starting (in order):** `README.md` (binding stopping rules — compliance note below), `AGENTS.md`, `briefs/merle-pincer-check-findings.md` entire (the evidence base; on main), `experiments/merle_pincer_check.py` (items 2b/2c print the certificates), `cycles.md` 12.8.6 entire and 12.8.3, `briefs/staircase-allp-findings.md`, `HANDOFF.md` item 2, `publication.md` (Sharpness-hedge entry), `TOUR.md`, `index.md`.

## Provenance

A two-key exchange with Eric Merle (correspondence 2026-07-16/17) resolved the recorded `p = 22` obstruction. Sequence, all on main: his falsifiable "Diophantine pincer" hypothesis → our delegated check (`briefs/merle-pincer-check-brief.md`) confirmed the **cause** (the candidate-generation machinery of 12.8.6.1 leaves a hole at `p = 22`'s scale: `(16266, 31867)` under the committed script's chain, `(15601, 47468)` under the lemma's strict sign-filtered grid) → a reviewer reproducibility fix (the correction runs had been silently deadline-limited at 40 s and mislabeled) flipped the recoverability conclusion: at the recorded algorithm's honest budgets, **Merle's own named candidates resolve `p = 22`** — `n = 25217` (in-scale, ratio 1.003) in 13 moves and `n = 31202` in 8 moves. Both certificates are **triple-verified**: the instrumented committed algorithm found them; `merle_pincer_check.py`'s independently written Section-2 code verified them; and the main-session reviewer's third implementation, written from Proposition 12.6.1's formula alone, confirms both exactly (22/22 size rotations, 0/22 divisibility, `γ = 11.1861` / `14.7462`, ratios `2.5084` / `3.3067`).

The certificates (from the findings file; re-verify, do not trust transcription):

```text
n = 25217: ms = [1,1,3,3,6,10,14,24,37,59,95,149,235,372,588,932,1475,2338,3704,5869,9301,1], ss = [1]*21 + [14730]
           K = 39968, gamma = 11.186, gamma/log2(22) = 2.508  (inside [1.828, 3.643])
n = 31202: ms = [1,2,3,4,8,11,18,29,46,73,115,182,290,460,728,1152,1826,2893,4584,7264,11512,1], ss = [1]*21 + [18231]
           K = 49454, gamma = 14.746, gamma/log2(22) = 3.307  (inside [1.828, 3.643])
```

**Stopping-rule compliance:** this brief records the outcome of an already-executed, already-merged check; it launches no search, no cycle-exclusion attempt, no equidistribution work. The cycle front stays parked. The passer was not sought — it emerged from a reproducibility fix at the correspondent's own named candidate.

## Queue, in order

1. **The standalone verifier (first, so every later claim can name it).** `experiments/p22_passer.py`, fresh code (imports nothing from `merle_pincer_check.py` or `staircase_allp.py`): both certificates hard-coded, checked from Proposition 12.6.1's formula with exact integers — `n = Σm`, `K = Σs + n`, `q = 2^K − 3^n > 0`, all `p` rotations `q ≤ R_r`, divisibility `q | R_r` count (expect 0), `γ = K − log₂q` (verify this is 12.8's own γ convention against the published `p = 7` instance, which the script must also include as a sanity anchor: `γ = 6.7438`). Runnable in seconds; this becomes the wiki's named verification line.

2. **cycles.md 12.8.6 update.** House style: the record states the current answer, history stays visible.
   - Rewrite the **Obstruction (`p = 22`)** paragraph as **Obstruction (`p = 22`) — resolved (2026-07-17)**: keep the original diagnosis text's substance (not resolved under the recorded budgets, across the candidates the script's own chain supplied), then the resolution: the failure was **candidate availability, not combinatorial resistance** — the chain's hole at this scale (both interval versions, from the findings) contained no usable `n`, and the in-scale candidates it did supply were infeasible or hopeless (−16 to −19 bits); at candidates outside the chain (`n = 25217 = 15601 + 9616`, `n = 31202 = 2·15601` — simple arithmetic on the CF's best convergent, named by Eric Merle in correspondence, his "Diophantine pincer" hypothesis), Construction 12.8.6.2 plus Algorithm 12.8.6.3 resolve at the committed move cap (13 and 8 moves). Credit the exchange explicitly (his hypothesis: cause confirmed, recovery-threshold half refuted; our record's "combinatorial, not Diophantine": refuted at `p = 22` in the complementary direction — the two-key protocol's first substantive product). Verification line names `experiments/p22_passer.py`.
   - Extend **12.8.6.4's verified record**: `p ∈ {2,...,23}`, now contiguous; add the two `p = 22` rows; the interval `[1.828, 3.643]` is **unchanged** (both new ratios inside). Note the correction-move observation (13 moves at `p = 22`) stays within the empirically-bounded-but-unproven move-count picture.
   - **Scope the "combinatorial, not Diophantine" sentence** (12.8.6.1's status paragraph): per the findings' erratum draft — the `p = 15` exhaustive-scan conclusion applies to the *choice among available* `n`; at `p = 22` the *availability* was the binding constraint, and the lemma's recorded coverage gap (the multiplicative-gap bound, still open) is precisely what bit. The sole remaining gap of the floor-grade result is now that one Diophantine lemma — state that plainly.
   - Grade sentence: still **floor grade** (the all-`p` theorem remains open on the Diophantine leg); the evidence is stronger and the obstruction anomaly is dissolved.
3. **`briefs/staircase-allp-findings.md`:** append a dated update section — item 3 ("Why p = 22 resists") superseded, pointer to `merle-pincer-check-findings.md`; original text untouched.
4. **Cross-page sweep.** `TOUR.md` (its two mentions of the `p = 22` obstruction and the `p ∈ {2,…,21} ∪ {23}` range); `index.md` (cycles.md row + status paragraph's 12.8.6 sentence); `HANDOFF.md` (Cycles front line: updated record `{2,...,23}`, obstruction dissolved via the Merle two-key exchange; item 2: correspondence state — second reply received 2026-07-16, verified, pincer check merged, reply pending); `publication.md` (Sharpness-hedge entry: contiguous verified range; **and one flagged line**: the merged-but-not-yet-uploaded paper v2 note still names `p = 22` as a persistent unresolved case — a pre-upload paper update is required, main-session/author decision, do not touch `paper/`). One register note: keep 12.8.6's own vocabulary consistent while you are in the file — the paper round found line 265's "non-per-period" and "dense" contradicting line 239's "per-period" (logged in `briefs/paper1-v2-findings.md`); align them with the "general per-period construction recipe" wording, minimal touches.

## Success / stop criteria

- **Floor = primary:** all four items.
- **Stop:** after item 4, stop. Explicitly forbidden: touching `paper/`; any new candidate search at any period (including "while we're here" checks at `p = 24, 25` beyond what the findings already record); any cycle-exclusion attempt; any equidistribution work; any attempt to prove the multiplicative-gap lemma (it stays the recorded open gap; a future brief's business). Off-brief findings to `briefs/p22-record-update-findings.md`; log and stop.

## Rules (non-negotiable, from AGENTS.md)

- `experiments/p22_passer.py` fresh, exact integers, seconds-fast, committed with item 1.
- Every changed claim's verification line updated to name the check that supports it; failures/history kept visible, not deleted (the original obstruction text remains readable inside the resolved paragraph).
- Register norm: flat. This dissolves a documented anomaly and extends a floor-grade record; it does not upgrade the hedge (the all-`p` claim stays assessed), does not unpark the cycle front, and does not claim the two-key exchange as more than what it is.
- Work on branch **`p22-record-update`**, one commit per item, do NOT merge — the main session reviews and re-runs before merging.
- No scope expansion.

## Definition of done

`experiments/p22_passer.py` passing with both certificates and the `p = 7` anchor; cycles.md 12.8.6 updated (resolved obstruction with history, extended contiguous record, scoped Diophantine sentence, consistent vocabulary, named verification); the staircase findings pointer; the four-page sweep with the paper-update flag recorded in publication.md; clean per-item commits on `p22-record-update`.
