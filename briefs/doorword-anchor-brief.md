# Brief: the door-word ↔ near-miss-anchor dictionary as a stated lemma (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — in particular: no per-period cycle searches; the cycle front is PARKED; this brief states a dictionary, it does not search), `AGENTS.md` (binding house norms), `itinerary.md` §14.15 structure (find the current last numbered block after 14.15.9 — your lemma is the next number; especially 14.14.8.2-adjacent composition conventions as used in 14.15.9's height laws and 14.15.6(d)(iv)'s census, plus 14.15.5's three-way characterization and 14.15.6's signed version), `reverse.md` §14.14.3, §14.14.7–14.14.8 (the door map's affine form, `G = T^m`, the composed-affine constants and the **order convention** — a past brief hit an order-convention mismatch here; state yours explicitly and reconcile), `cycles.md` §12.1, 12.6.1–12.6.1.3 (the reduced cycle equation; the transport recurrence and seam identity; the near-miss anchors and spent stock; the new digit-cap remark), `anchors.md` §17.5, `bridge.md` §16.4.5 (charter: pointers only).

## Provenance and pre-check

Main-session exploration (2026-07-23) of knowledge-opportunity #4 from the post-cleanup flag list (the last of the four): the per-cycle correspondence between door-words and near-miss anchors — e.g. `((2,1)) ↔ (2,3,−1)` for `−5` — is pointered (cycles 12.6.1.2's census cross-frame sentence; the 12.6.1.1 ↔ 14.15.9.2 seam identity) but not stated as a lemma. Pre-checked with fresh throwaway code (main session, 2026-07-23; script deliberately not provided):

- **Per-letter affine form (exact):** on its stratum class, `G(y) = (3^m·y + 3^m − 2^m)/2^(m+r)` with exact divisibility — `5,000` random `y < 2^40`, 0 failures.
- **The dictionary:** for a periodic word `W = ((m_0,r_0),…,(m_{p−1},r_{p−1}))`, the composed map has slope `3^M/2^S` (`M = Σ m_i`, `S = Σ (m_i+r_i)`) and fixed point `y*(W) = N_W / q(W)` with `q(W) = 2^S − 3^M` the **unreduced denominator** and `N_W = 2^S·B_W` an integer — `4,000` random words (`p ≤ 3`, letters `≤ 4`), 0 failures on the `N/q` identity.
- **The known-cycle table reproduces exactly:** `((1,1)) → y* = 1, (M,S,q) = (1,2,+1)`; `((2,1)) → y* = −5, (2,3,−1)`; `((4,1),(3,3)) → y* = −17, (7,11,−139)` — matching cycles 12.6.1.2's odd-step-frame anchors `(k,m,q)` letter for letter, with full cycle-membership checks (each `y*` follows its word under `G` and returns). `{−1}` stays outside the coding (the singular point), as 14.15.6(d)(iv) records.
- **Rotation:** `q(W)` is rotation-invariant (500 trials, 0 failures), and integer fixed points of rotated words chain under `G` — consistent with 12.6.1.1's rotation story.
- **Census consistency (bounded):** among the 4,000 random words, exactly `185` had odd integer fixed points `≠ −1`, and every one followed its word and returned — i.e. every one is a rotation/repetition census member of the known cycles; no strays.

So the dictionary is mechanically exact; your job is to state it as a lemma at house standard. Your verification code must be your own fresh implementation, per AGENTS.md.

## The framing mandate (read before item 1)

This is the **last and lightest of the four knowledge-opportunity notes**: a naming, tying two existing pointer sentences into one stated lemma. Binding constraints:

1. **Nothing here is new leverage.** The frames were already identified in the large (the seam identity, 12.6.1.1 ↔ 14.15.9.2); the reconciliation of the composed fixed point with the classical cycle candidate is already on file (reverse.md 14.14.7–8, bridge 16.4.5's fifth-block sentence, cycles 12.1). What is missing is only the *per-cycle dictionary stated once, with the anchor triple explicit*. Any prose implying a new exclusion route, a reopened cycle front, or progress on `q | R₀` is a register violation.
2. **The stopping rules bind hard here.** No cycle search of any kind: your verification's census-consistency check must be a *bounded dictionary verification against the already-recorded census* (cycles 12.6.1.2 already did exhaustive replication `k ≤ 10` in the numerator frame — cite that as the census authority; your check verifies the dictionary maps it correctly, at comparable or smaller bounds, not beyond).
3. **Mind the order convention** in the composed-affine constants (14.14.8.2): the wiki composes deepest-first in some statements; your per-letter composition (applied in itinerary order) must state its convention explicitly and reconcile with `B_W`'s existing definition — if there is a mismatch, that is a finding to record precisely, not to paper over.

## Queue, in order

1. **The dictionary lemma.** New numbered block in itinerary.md directly after the current last block of §14.15 (verify the number in the worktree; never renumber existing anchors). State and prove, citing existing results wherever they carry the weight:
   - *(a)* The per-letter affine form on the stratum class: `G(y) = (3^m·y + (3^m − 2^m))/2^(m+r)` — a one-line consequence of the definitions (or a citation, if reverse.md 14.14.3's graded law already states this shape; check and cite rather than re-derive).
   - *(b)* For a periodic word `W` of period `p`: composed slope `3^(M(W))/2^(S(W))` with `M(W) = Σ m_i`, `S(W) = Σ (m_i+r_i)`; fixed point `y*(W) = N_W/q(W)`, `q(W) = 2^(S(W)) − 3^(M(W))`, `N_W ∈ Z` (the 2-power denominators clear — state the normalization against 14.14.8.2's `B` with the order convention made explicit); `q(W)` rotation-invariant with the fixed points of rotations chained by `G` — cite 12.6.1.1/14.15.9.2's transport identity for the numerator side, don't re-derive it.
   - *(c)* **The anchor identification (the point of the lemma):** the triple `(M(W), S(W), q(W))` *is* the near-miss anchor `(k, m, q)` of cycles.md 12.6.1.2's odd-step frame — `M` the odd steps (via `G = T^m`, reverse.md 14.14.7.1), `S` the halvings (the `T`-expansion `(m,r) → (1,…,1,r+1)` sums to `m+r`), `q` the tower gap. One displayed dictionary line, e.g.: *periodic door-word `W` ↦ near-miss anchor `(M(W), S(W), 2^(S(W)) − 3^(M(W)))`; fixed point `y*(W) = N_W/q(W)`.*
   - *(d)* **The per-cycle table**, one compact display: `((1,1)) ↔ (1,2,+1) ↔ y = 1`; `((2,1)) ↔ (2,3,−1) ↔ y = −5`; `((4,1),(3,3)) ↔ (7,11,−139) ↔ y = −17` (word primitive, the `G`-period-2 reading of the classical period-7 cycle); `{−1}` outside the door coding (singular point, 14.15.6). This is the flag's `((2,1)) ↔ (2,3,−1)` example stated as an instance of the lemma rather than a pointer.
2. **The characterization corollary (cited, not re-proved).** `W` is realized by an integer cycle iff `y*(W) = N_W/q(W)` reduces to an odd integer of the appropriate sector — the periodic case of the three-way characterization (14.15.5, signed per 14.15.6), which is cycles 12.1's classical integrality condition under the seam names (already recorded as a reconciliation; cite bridge 16.4.5's fifth block). Then one sentence each, tying the frames per-cycle: at `|q(W)| = 1` the denominator is `±1`, so *every* word with those `(M,S)` is integrally realized — the fixed-point-frame reading of 12.6.1.2's "at `|q| = 1` divisibility is free"; for `|q| > 1`, integrality of `N_W/q(W)` is the fixed-point-frame reading of the parked condition `q | R₀` (the seam identity's shared-denominator clause, 12.6.1.1) — parked exactly as before.
3. **Calibration.** Same block: the lemma names a correspondence both pages already point at; no exclusion is added or implied; the cycle front stays parked; the census cited is 12.6.1.2's (authority: its exhaustive replication), and the verification here checks the *dictionary*, not the census.
4. **The pointer sweep.**
   - `cycles.md` 12.6.1.2: extend the census cross-frame sentence by one clause — the per-cycle correspondence now stated as a lemma (itinerary.md `<number>`).
   - `anchors.md` §17.5: one clause on the 12.6.1.2 bullet.
   - `bridge.md` §16.4.5: only if a natural one-clause seat exists on the existing seam-identity or fifth-block sentence; otherwise skip (charter: pointers only, no inflation).
   - `HANDOFF.md`: at most one appended clause on the Reverse/mirror or Cycles line.
   - Front-matter `updated:` on touched pages; index.md — verify, likely no-op.

## Success / stop criteria

- **Floor:** item 1 proved and verified with the table, item 4's cycles.md pointer.
- **Primary (expected):** all four items.
- **Stop:** after item 4, stop. Explicitly forbidden, whatever the results suggest: any cycle search beyond the bounded census-consistency verification (stopping rules; 12.6.1.2's replication is the census authority); any divisibility (`q | R₀`) work; any extension of the height laws (14.15.9 is closed); any use of the dictionary to propose exclusion routes; any touch of the other knowledge opportunities (all three are merged — do not revisit them beyond citation). Off-brief findings go to `briefs/doorword-anchor-findings.md`; log them and stop anyway.

## Placement and numbering

- `itinerary.md`: one new numbered block after the current last block of §14.15, holding items 1–3. Existing anchors untouched.
- `cycles.md`, `anchors.md`, possibly `bridge.md`, `HANDOFF.md`: item 4's one-clause pointers. Front-matter `updated:` on every touched page.
- publication.md: nothing.

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code, not the pre-check's constructions; record what was checked, the range, seeds, and the date, inline in the owning block (overwriting style).
- Verification code goes in `experiments/doorword_anchor.py`, states which results it supports, stays runnable, imports nothing from `experiments/itinerary_coding.py`, `merle_round5_check.py`, or `realization_height.py` (independence). Exact integer/`Fraction` arithmetic wherever a pass/fail decision is made. Suggested coverage: the affine form; the `N/q` identity and rotation invariance on random words (stated bounds/seeds); the known-cycle table with full cycle-membership checks; the bounded census-consistency check (every integer fixed point in a stated small scan is a census member — bounds at or below 12.6.1.2's `k ≤ 10` precedent, framed as dictionary verification).
- Register norm: flat, calibrated prose; this is the lightest of the four notes and should read that way — one lemma, one corollary paragraph, one table, done.
- Work on branch **`doorword-anchor`**, based at current main **`95edd5b`** (verify with `git log --oneline -1 main`; if your worktree HEAD is older, branch from 95edd5b explicitly — shared object store). Commit per item with verification in the same commit, and **do not merge to main** — the main session reviews and re-runs all verification code before merging.
- No scope expansion.

## Definition of done

Item 1 as a proved, verified lemma with the explicit dictionary line and the per-cycle table; item 2's corollary paragraph with the two frame-tying sentences (`|q| = 1` divisibility-free ↔ denominator `±1`; `|q| > 1` integrality ↔ parked `q | R₀`), all by citation; item 3's calibration; item 4's pointers so the flag's "pointered but not stated" is closed in both directions; clean per-item commits on `doorword-anchor` with `experiments/doorword_anchor.py` committed and passing.
