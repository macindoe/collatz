# Brief: L-A8 / T1 clean-room verification (no-hair theorem for cycles) — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules — note especially: no per-period cycle searches; this session verifies a correspondent's finite discharge, which is not a cycle search, and opens no new front), `AGENTS.md`, `HANDOFF.md` item 1, `cycles.md` §12 (our PARKED cycles front — read for the records T1's scope statement must be checked against, e.g. known cycle bounds and the four real cycles), `briefs/merle-la6-check-findings.md` (the census/necklace context and the −17 cycle data).

## Provenance

Merle seeded **L-A8** in the shared repo `github.com/macindoe/one-obstruction-three-faces` (HEAD `826970e`; L-A8 blocks at commits `be8869f`, `0905b00`, `9428663`, `a37743f`, `5773bd0`, `826970e`), one key (his), our key invited. T1 — "a surviving cycle has no freedom of shape left." The claimed chain (all integer until the last steps):

1. **Cycle product identity:** `∏(3xᵢ+1) = 2^K·∏xᵢ` over a positive cycle with `p+1` odd elements (telescoping). Claimed exact on all four real cycles, both shores; the `−17` instance: `∏(3x+1) = −403123745024000 = 2^11·∏x`.
2. **Survivor bound:** `2^K(3X)^{p+1} ≤ 3^{p+1}(3X+1)^{p+1}`, per-factor `(3x+1)(3X) ≤ 3x(3X+1) ⟺ X ≤ x`, `X = x_min`.
3. **Ceiling:** `3^{p+1} < 2^K < 2·3^{p+1}` whenever `2(p+1) < 3X` — `K` pinned to `⌈(p+1)log₂3⌉`, no logarithm in the statement.
4. **Seam bound:** `q·3X < 2(p+1)·3^{p+1}` where `q = 2^K − 3^{p+1}` — seam gap crushed inversely to the minimum element.
5. **Ratio/log gap:** `0 < K·log2 − (p+1)·log3 < 2(p+1)/(3X)` via `log x ≤ x − 1`; dividing: `|log₂3 − K/n| < δ`, `δ = 2/(3X·ln2)`; at `X = 2^71`: `δ = 4.0734·10⁻²²`.
6. **Legendre:** inside the integral window `4000·n² ≤ 2079·X`, `K/n` must be a **convergent** of `log₂3`.
7. **Discharge:** every convergent denominator in the window fails the seam criterion, via the classical bound `θ_j > 1/(q_j + q_{j+1})` turning each check into one integer inequality `2000·q·(q+q′) ≤ 2079·2^71`. Claimed: all 22 pass, tightest margin `5.17×` at `q = 6586818670` (exact test `5.44×`), non-vacuity canary failing at the very next convergent.

**Claimed closure:** *no positive cycle with `x_min ≥ 2^71` and length `n ≤ 3.5032·10^10`.* Plus one flourish worth checking exactly: **Hercher's bound `1.375·10^11` is claimed to be `q₂₂`, itself a convergent denominator of `log₂3`**, with the window ending at `q₂₁`.

**Known internal discrepancies to pin (found at orientation; hand them back flatly, they may be nothing or something):**
- The window appears as **`3.5035·10^10`** in stacks `9428663`/`89d9efc` (and REQ-MATH-054) but **`3.5032·10^10`** in the final entry and his letter. Which is right under the exact definition, and did the definition shift (`√(1/2δ)` vs the integral `4000n² ≤ 2079X` form)?
- `q₂₁` appears as **`6.547·10^10`** (stack `0905b00`: "first admissible scale `n ≥ q₂₁ = 6.547e10`") and the tightest-margin denominator as **`q = 6586818670 ≈ 6.587·10^9`**, ALSO labeled `q₂₁` in stack `89d9efc`. Same-name different-value: establish the true convergent index of each from your own continued-fraction computation and say which labels in his text are off (indexing conventions differ by the initial term — pin the convention).

The Lean statement-match is a **sibling session, not yours** (`merle-lean-r10-audit`). This session is the independent mathematics: derive and verify every link in fresh code.

## Queue

1. **Shared repo, read-only.** Fresh clone (scratchpad). Record HEAD (expected `826970e`; if moved, record and continue read-only at `826970e`). Record the six L-A8 blocks verbatim in the findings. Read his `experiments/OUT_REQ-MATH-052..056` outputs (Lean repo `ericmerle3789/one-obstruction-three-faces-lean`, HEAD expected `5c9b663`) for operational definitions ONLY; never run his code as verification.

2. **Replication, fresh code** (`experiments/merle_la8_t1_check.py`; imports nothing from his repos or prior checks; exact integers everywhere possible; `mpmath` with stated guard digits + two-precision stability checks where logs are unavoidable):
   - (a) **Identity.** Derive the telescoping proof of the product identity in the findings (three lines), then verify it exactly on all four real cycles, both shores (the cycles are in `cycles.md`; the `−17` figures above must reproduce).
   - (b) **Survivor + ceiling.** Prove the per-factor equivalence `(3x+1)(3X) ≤ 3x(3X+1) ⟺ X ≤ x` (one line); verify the ceiling implication numerically on a sweep (random synthetic "cycles" satisfying the hypotheses — element multisets, not orbit searches — plus the trivial cycle canary) and confirm `K = ⌈(p+1)log₂3⌉` is forced when `2(p+1) < 3X`.
   - (c) **Seam + log gap.** Derive the seam bound from (b) (record the derivation); derive the log-gap chain via `log x ≤ x − 1`; verify `δ = 2/(3·2^71·ln2) = 4.0734·10⁻²²` and the earlier factor-2 correction (his withdrawn `4.955·10^10` window vs corrected — confirm the withdrawn figure is exactly the missing-factor-2 artifact).
   - (d) **The window, exactly.** Compute Legendre's applicability bound `n ≤ √(1/(2δ))` in high precision AND the integral form `4000n² ≤ 2079·2^71`; derive where 2000/2079 (and 4000) come from (rational under-approximation of `3·ln2/4` — verify `2079/4000 < 3·ln2/4` and its conservativeness direction); **pin 3.5032 vs 3.5035** and state which figure is right for which definition.
   - (e) **Convergents.** Compute the continued fraction of `log₂3` from scratch (≥ 80 digits working precision, verified stable at two precisions; cross-check the small denominators against the census scales 5, 12, 41, 53, 306, 665, 15601, 190537 that this project already knows); enumerate all convergent denominators `q_j ≤` the window; confirm there are exactly **22**; resolve the `q₂₁` labeling discrepancy and index Hercher's `1.375·10^11` — is it EXACTLY a convergent denominator (integer equality against his published figure, not ≈)? Our `cycles.md` §12 records the published cycle-length bounds — take Hercher's exact published constant from there if present; if it is not on file, bounded web access is granted for THIS single constant (Hercher's paper, exact bound and statement; record the citation); no other web use.
   - (f) **Discharge.** For each of the 22: verify the integer criterion `2000·q_j·(q_j+q_{j+1}) ≤ 2079·2^71`, compute the margin, confirm tightest `5.17×` at `q = 6586818670`; compute the EXACT test (via `θ_j` at full precision) and confirm `5.44×` there, i.e. the integer form conservative; verify the canary — the first convergent PAST the window fails the criterion. Derive `θ_j > 1/(q_j+q_{j+1})` (textbook; two lines in the findings) and trace the full implication: criterion holds at `q_j` ⟹ no cycle of length `q_j` with `x_min ≥ 2^71` — directions explicit.
   - (g) **Scope statement.** Confirm the closure statement follows from (a)–(f) exactly as stated: length `n` = number of odd elements; `x_min ≥ 2^71` (note in the findings how this sits against the verified-convergence bound this constant comes from — Barina-type exhaustive verification — and against Hercher's `1.375·10^11` length bound: his claim "3.9× further, but on paper" — is the comparison apples-to-apples, i.e. same length convention, same `x_min` hypothesis? If Hercher's theorem needs no `x_min` hypothesis, say so — that is a real scope difference the co-edit language must keep honest).
   - (h) **Non-vacuity.** Confirm the four real cycles do not contradict any link (they all have `x_min < 2^71`, so they must pass through the hypotheses' cracks exactly where expected — show where each hypothesis excludes them from T1's scope).

3. **Record** (branch commits, per-item):
   - `experiments/merle_la8_t1_check.py` + committed output (one commit; canaries — the four real cycles — printed first).
   - `briefs/merle-la8-t1-check-findings.md` — verbatim blocks; every derivation written out (this entry is proof-shaped, so the findings are the clean-room proof record); replication results match/mismatch flat; the two discrepancies pinned; the Hercher adjudication with citation; key recommendation (expected shape: turn-with-scope — the mathematics confirmable in the clean room, the kernel claims deferred to the sibling audit, the two named glue facts + any figure corrections as offers; recommendation only, no turn).
   - `HANDOFF.md` item 1 — ONE scoped paragraph on this check's state; siblings `merle-la7-close-check` and `merle-lean-r10-audit` edit item 1 in parallel — keep your edit to your own lines.

## Rules

- Branch **`merle-la8-t1-check`** from your worktree HEAD (verify it contains this brief; state the base SHA in the findings). Per-item commits; do NOT merge — the main session reviews (re-runs the script) and merges.
- Read-only everywhere outside this repo: no pushes, no shared-repo writes; web access ONLY per item 2(e)'s single-constant bound.
- Discrepancies recorded and flagged, never disputed in prose. The two pinned discrepancies are handed back as findings, with the correct values computed, nothing more.
- No reply paragraphs; no key turns (recommendation only); no co-edit commits; stop after item 3.
