# Brief: the staircase family at every period — upgrading sharpness from assessed to proved (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — read the compliance paragraph below against them), `AGENTS.md` (binding house norms), `cycles.md` §12 entire — especially 12.1 (cycle product equation), 12.6.1 (the period-`p` elimination and the rotation numbers `R_r`), 12.8.1 (uniform trim and its max-plus proof), 12.8.2 (effective finiteness), 12.8.3 (the staircase family, currently a *Remark* with verified instances), 12.8.4–12.8.5 (what the staircase means; the parked front). Also `paper/collatz-reduced-v1.tex` Theorem `thm:staircase` (read-only — see forbidden list) for the published hedge this brief targets.

## Provenance, authorization, and stopping-rule compliance

This brief packages an external suggestion from **Eric Merle** (correspondence, 2026-07-16), assessed by the main session against the ledger before delegation: his reading of the published paper is exactly accurate — the uniform trim (12.8.1) is proved; the sharpness half (a staircase family with `γ = O(log p)` at *every* `p`) is **assessed, not proved**, with evidence at `p = 6` (84 instances) and `p = 7` (one instance, `n = 94`). His suggestion: the max-plus extremal configuration in 12.8.1's proof looks finite and combinatorial enough that the all-`p` statement may be reachable by a genuine induction/construction. This brief is the attempt.

**Stopping-rule compliance (author-authorized, 2026-07-16).** The cycle front remains **PARKED**. The stopping rules forbid (a) per-period cycle searches and (b) reopening cycle *exclusion* without a divisibility-aware idea. This brief does neither: it proves a **negative structural result about size arguments** — that the wall recorded in 12.8.3 is real at every period — upgrading an existing resolved result's sharpness half from assessed to proved. No cycle is being searched for and no exclusion is being attempted. The author explicitly authorized this bounded item; treat any drift toward exclusion work as out of scope (see forbidden list).

## Pre-check (main session, 2026-07-16, fresh throwaway code — deliberately not provided)

The main session pre-checked the target before delegation with fresh throwaway code (validated two ways: the sanity identity of 12.6.1's remark reproduced exactly for `p ∈ {1,2,3,4,7}`, and the published `p = 7` instance reproduced exactly — `γ = 6.744`, all seven rotations pass). Results:

- **The family extends beyond the published `p ∈ {6, 7}`.** Size-passers (all rotations, exact big-int) found at: `p = 8` (`n = 41`, `γ = 6.46`), `p = 9` (`n = 94`, `γ = 6.74`), `p = 10` and `p = 12` (`n = 306`, `γ = 9.94`), and — after unit-level perturbation of the profile — `p = 11` (`n = 306`, `γ = 9.94`), `p = 13` and `p = 14` (`n = 971`, `γ = 10.00`). Over `6 ≤ p ≤ 14` the best found `γ / log₂ p` stays in `[1.8, 2.8]` — consistent with the assessed `O(log p)`.
- **The Diophantine mechanism is visible, not optional.** Every passer sits at an `n` whose fractional part `{n·log₂ 3}` is within `~2^{−γ}` of `1⁻`, and these `n` are exactly convergent/semiconvergent denominators of `log₂ 3` (`41`, `94 = 53 + 41`, `306`, `971 = 306 + 665`). The route-guidance lemma below is the proof-shaped version of this observation.
- **The rounding slack is the real content.** The naive largest-remainder rounding of the geometric profile *fails* at `p = 11, 13, 14` — but only by `1–2 bits` on one to three rotations, and redistributing single units among climb blocks (82–447 greedy moves) recovers a passer. Expect the proof's difficulty to live here: a clean explicit profile with provable slack, not naive rounding.
- **`p = 15–18` were not resolved by the pre-check** (no passer among the six best-δ `n` per window under a severely capped hill-climb — at `p = 18` the cap allowed ~1.4 sweeps, so this is suspected to be a search-budget artifact, not evidence against the claim). Settling `p ≤ 20` computationally is part of your floor grade either way; if genuine obstructions appear at these `p`, that is a major finding — record it, do not force the profile.

## The target

**Theorem (primary grade).** There are absolute constants `C₁, C₂` and, for every period `p ≥ 2`, an explicit configuration `(m_t, s_t)_{t=0..p-1}` with all `m_t, s_t ≥ 1`, `n = Σ m_t`, `K = n + Σ s_t`, `q = 2^K − 3^n > 0`, such that:

1. **(size-passer)** `q ≤ R_r` for *every* rotation `r`, with `R_r` exactly as in 12.6.1;
2. **(small trim)** `γ = K − log₂ q ≤ C₁ + C₂·log₂ p`;
3. **(staircase scale)** `n ≥ c·1.585^p` for an absolute `c > 0`.

**Corollary to state with it (the sharpness consequence):** any trim uniform in `p` of the form `γ + log₂ p > f(p)·n` valid for all size-passers must have `f(p) = O(log p / 1.585^p)` — the exponential degradation of Theorem 12.8.1 is intrinsic to size-counting, now by proof rather than by instances.

The staircase *shape* (geometric climb at ratio `≈ log₂ 3`, unit exits, one crash block) is instrumental, not part of the claim: if the proof wants a variant profile (perturbed roundings, different closing block), take it — conditions 1–3 are the deliverable.

## Route guidance (verify, don't transcribe)

- **Where the Diophantine input enters — flag this first.** A size-passer with `γ ≤ C log₂ p` forces `q = 2^K − 3^n ≤ 2^{K−γ}`, i.e. `0 < K − n·log₂ 3 ≲ 2^{−γ}/ln 2`. So `n` cannot be arbitrary: the fractional part `{n·log₂ 3}` must lie within `~p^{−C}` below `1`. Existence of such `n` at scale `n ≍ 1.585^p` for every `p` is elementary and effective (three-distance theorem / continued-fraction convergents of `log₂ 3`: among `N` consecutive `n` the points `{n·log₂ 3}` have max gap `≪ 1/N`, and the window at scale `1.585^p` contains `≫ p^C` integers for any fixed `C`). This is the one non-combinatorial ingredient; isolate it as its own lemma with explicit constants.
- **The combinatorial half.** With `n` chosen, set the staircase profile and verify all `p` rotation conditions `q ≤ R_r`. The max-plus analysis in 12.8.1's proof identifies the binding rotation (the reset walk); the construction tracks its extremal configuration, so the expected structure is: one rotation is tight (it determines the achievable `γ`), the others hold with slack that should be provable termwise (dominant-term estimates as in 12.7.4's three-route casework, but now with the staircase's explicit exponents). Rounding the geometric profile to integers costs `O(p)` in exponents — track where that cost lands and why it is absorbed.
- **Eric Merle's framing:** a genuine induction on `p` (extend a period-`p` staircase to `p+1` by adding one climb step and re-closing) is one route; a direct one-shot construction with explicit estimates is another. Take whichever closes; if the induction route fails for a structural reason, record the obstruction — that is a finding, not a failure.
- **Consistency checks along the way:** the published instances must fall out as special cases or near-misses of the construction: `p = 7`, `n = 94`, `m = (4, 7, 9, 15, 23, 35, 1)`, `s = (1,1,1,1,1,1, S−6)`, `γ = 6.74` (12.8.3). If the general construction at `p = 7` produces something materially different, understand why before proceeding.

## Grades

- **Primary:** the theorem above, all `p ≥ 2` (small `p` may be covered by the verified instances if the estimates need `p ≥ p₀`; then `p₀` is explicit and small).
- **Fallback A:** the theorem for all `p ≥ p₀` with `p₀` explicit but not small, instances covering `2 ≤ p < p₀` computationally.
- **Fallback B:** a weaker proved bound (`γ = O(p^α)`, `α < 1`, or `γ = O(p)`) with condition 3 intact. State the consequence honestly: this still proves no polynomial-in-`p` extension of the small-period constants exists (since `n` grows like `1.585^p`), but does not reach the paper's `O(log p)` sentence; the paper hedge would be *softened*, not removed.
- **Floor (if no proof closes):** a documented obstruction — which estimate breaks, on which rotation, and why — plus the instance record extended from `p ∈ {6, 7}` to every `p` in a feasible range (at least `p ≤ 20`; the construction is cheap, big-int `R_r` checks are the cost), with `γ(p)` tabulated against `log₂ p`. That upgrades the paper's evidence sentence and is publishable in the comparison note as an honest state-of-knowledge.

## Verification (non-negotiable, from AGENTS.md)

- Fresh script `experiments/staircase_allp.py`; **imports nothing from `uniform_trim.py`** (that script produced the existing instances — your code is the independent check). States which results it supports; stays runnable; exact big-integer arithmetic throughout (no floats in any `q ≤ R_r` decision — compare integers; `γ` may be reported as a float but decided via bit-lengths).
- For every `p` in the verified range: construct the configuration **by the proof's recipe** (not by search — the point is that the proof's own construction passes), check `q > 0`, all `p` rotation conditions, and the `γ` bound; record range, seeds (if any), and date inline in the owning section per house norms.
- Reproduce the published `p = 7` instance record as a cross-check (expect `γ = 6.74` to the stated precision).
- **Divisibility observation (bounded):** for constructed instances it is permitted to *record* whether any passes the full divisibility system `q | R_r` (expected: none, matching 12.8.3). If any instance ever passes all size AND all divisibility conditions, **halt immediately and report to the main session without further computation** — that configuration would reconstruct a genuine cycle (12.6.1 converse), which contradicts known verification for all remotely reachable `p`; it is therefore almost certainly a bug in your code, and either way it is far above this brief's pay grade.

## Forbidden, whatever the results suggest

- **No per-period cycle searches** (stopping rule; unchanged by this brief).
- **No divisibility-based exclusion attempts** — the anchor-rigidity front stays parked; divisibility appears in this brief only as the bounded observation above.
- **No edits to `paper/*.tex`** — the published papers are main-session property; the v2 edit happens after review and merge.
- **No edits to the recorded instances in 12.8.3** — add, don't rewrite; the Remark stays as the historical instance record with a pointer to the new theorem.
- **No statistics of any kind** (the §17.7 program is at its natural endpoint).
- No scope expansion. Off-brief findings go to `briefs/staircase-allp-findings.md`; log them and stop anyway.

## Placement and numbering

- `cycles.md`: new **Theorem 12.8.6** (statement, Diophantine lemma, proof, the sharpness corollary, verification line). Never renumber existing anchors. One pointer sentence added at the end of Remark 12.8.3 ("the family is now proved at every period: 12.8.6"). Front-matter `status` + `updated` + the "Current state" paragraph updated to reflect: sharpness **proved** (or the achieved grade). 12.8.5's strategic conclusion is *unchanged* by any grade of this brief — say so explicitly if you touch its neighborhood.
- `publication.md`: one flat entry — the paper's `thm:staircase` hedge ("we assess … though not proved here for all p") is now upgradable to the achieved grade in a v2; note this is the item Eric Merle's correspondence flagged.
- `open-problems.md`: sweep for any entry this calibrates.
- Cross-page status sweep per AGENTS.md when done: `index.md` (cycles.md row + status paragraph), `HANDOFF.md` one-liner.

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code, not the code that suggested the result; record what was checked, the range, and the date, inline in the owning section.
- Failures and obstructions are recorded, not deleted.
- Register norm: flat, calibrated prose. This brief *strengthens a negative result* — the honest closing sentence at any grade is that size-counting is now provably (or: still assessedly) unable to exclude the staircase, and the residual content of cycle exclusion remains anchor-walk rigidity, exactly as 12.8.5 recorded. No excitement inflation; the theorem closes a hedge, it does not open a path.
- Work on branch **`staircase-allp`**, commit per item (Diophantine lemma; main construction/theorem; verification script; cross-page sweep) with verification in the same commit as the claim it supports, and **do not merge to main** — the main session reviews and re-runs all verification code before merging (mirror-queue / door-seam / block-map / itinerary-coding precedent).

## Definition of done

Theorem 12.8.6 in `cycles.md` at the highest grade reached, with the Diophantine lemma isolated, the sharpness corollary stated, and an inline verification record; `experiments/staircase_allp.py` committed, passing, independent of `uniform_trim.py`, covering at least `p ≤ 20` by the proof's own construction plus the `p = 7` cross-check; `publication.md` and the cross-page sweep done; clean per-item commits on `staircase-allp`; a closing status paragraph stating plainly what changed (the sharpness half's grade), what did not (12.8.5's strategy; the parked front; the Bridge), and — if below primary grade — exactly where the proof stopped and why.
