# Brief: the finite bicylinder corollary and the positive realization height (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules**), `AGENTS.md` (binding house norms), `reverse.md` §14.14–14.15 entire (the door/exit seam, the block-map layer, the itinerary language — this brief adds a fourth block to 14.15), stage3.md 11.8.6.3 (`m₊`), stage4.md 11.8.7.7 (the digit budget), bridge.md §16 (charter: pointers only), cycles.md §12.1 (the classical cycle candidate, for one reconciliation sentence).

## Provenance and pre-check

This brief packages an external suggestion (ChatGPT, 2026-07-16, post-dating the merged 14.15), reviewed and corrected by the author and the main session before delegation. The suggestion's surviving content is two items: a finite **bicylinder corollary** of the cylinder theorem, and a **positive realization height** giving the diagonal compatibility locus (14.15.3(c)) an equivalent boundedness criterion. A third suggestion (a synthesis layer restating 14.14.6's edge/door dictionary in new notation) was **declined** by the main session — one fact, one page; do not implement it.

Pre-checked with fresh throwaway code (2026-07-16, main session; script deliberately not provided):

- **Unique predecessor (A):** for a target door `z` and letter `(m,r)`, the formal predecessor is `y = 2^m(2^r z + 1)/3^m − 1`, existing iff `3^m | 2^r z + 1`; over 2,042 random existing cases it was in every case **positive, odd, on stratum exactly `(m,r)`, with `G(y) = z`** — 0 failures; exhaustive uniqueness over all odd `y < 2^16` (no two same-stratum doors share a `G`-image): 0 violations.
- **Bicylinder (B):** 60 random two-sided windows (letters ≤ 3, `p,q ≤ 3`), follower class built by cylinder lifting, live representative advanced `p` steps: prescribed past and future both realized, 0 failures.
- **Height sanity (C):** the all-`(1,1)` word has `H_{p,q} = 1` at every window tried (`p = q ≤ 4`); fixed-origin nested windows gave 0 monotonicity violations over 15 random words (10 strictly grew).

**Two corrections to the external suggestion, both established by the pre-check — build on these, not on its text:**

1. The suggestion names "negative or non-live" deep predecessors as the failure modes. **Negativity does not occur**: the letter-prescribed predecessor of a positive door is automatically positive (algebra above — `y + 1 = 2^m(2^r z + 1)/3^m > 0` whenever integral). The true failure modes are exactly two: the **admissibility congruence** `3^m | 2^r z + 1` failing at some depth, and **liveness of the deepest door only** (intermediate chain doors are `G`-images, hence live automatically, 14.14.7.1).
2. Nested-window monotonicity holds only for windows growing around a **fixed origin** (`R_{p+1,q+1} ⊆ R_{p,q}` with the same pivot). A first pre-check draft slid the origin along the word and saw spurious violations. State the definition with the origin explicit, and make your verification code grow windows around a fixed pivot.

## The framing mandate

Everything here is **formulation grade on an already-formulated object** (14.15.3(c)). The height renames the Bridge's open locus as a boundedness question at the archimedean place; it does not move it, estimate it, or supply leverage. The honest headline for the corollary is one sentence: *there is no finite two-sided obstruction either.* The honest headline for the height is one sentence: *integral realization is equivalent to boundedness of the positive realization height — the archimedean condition that the `Z₂ × Z₃` diagonal forgets.* Any prose implying the Bridge has narrowed is a register violation.

## Queue, in order

1. **The unique-predecessor lemma.** New subsection **14.15.4** (14.15.1–14.15.3 are merged and closed; never renumber existing anchors). For a live door `z` and letter `(m,r)` (`m,r ≥ 1`): `G(y) = z` with `stratum(y) = (m,r)` has **at most one** solution, namely `y = 2^m(2^r z + 1)/3^m − 1`, which is an odd integer iff `3^m | 2^r z + 1`, and is then automatically positive and on stratum exactly `(m,r)` (both `v₂` conditions forced, no separate check — prove this, it is three lines from 14.14.4.1's affine form). Injectivity of `G` on each stratum is the content; state it as such. One reconciliation sentence, no more: this is the door-coordinate form of the backward branching law (14.2.4) — cite, don't re-derive, and record any mismatch as a finding rather than forcing agreement.

2. **The finite bicylinder corollary.** Same subsection. For any finite words `V` (past, length `p`) and `U` (future, length `q`): the concatenation `VU` has, by 14.15.1.5 + 14.15.1.7, infinitely many live followers `y₋ₚ`; advancing `p` steps gives a live door `y₀` with prescribed past `V` (realized by an actual positive live chain — intermediate doors live automatically) and prescribed future `U`. State the consequence flatly, as calibration in 14.15.2's register: **every finite two-sided itinerary window is realized by a positive live integer segment — there is no finite two-sided obstruction.** This extends 14.15.2's verdict (the word is free at every finite *forward* depth) to finite windows with prescribed past. One proof paragraph; it is a corollary, not a front.

3. **The positive realization height.** Same subsection. For a bi-infinite word `W` and a window `(p,q)` around `W`'s fixed origin, define `R_{p,q}(W)` := the set of positive live doors `y₀` whose forward orbit realizes letters `0..q−1` and whose (unique, by item 1) letter-prescribed backward chain exists to depth `p` with live deepest door. Then:
   - `R_{p,q}(W) ≠ ∅` (item 2), and `R_{p+1,q+1}(W) ⊆ R_{p,q}(W)` (fixed origin);
   - `H_{p,q}(W) := min R_{p,q}(W)` is finite and nondecreasing in `(p,q)`;
   - **Equivalence theorem:** `W` is integrally realized (14.15.3.5) ⟺ `(H_{p,q}(W))` is bounded ⟺ eventually constant. Forward direction: a realizing `y₀` caps every window. Reverse: a bounded nondecreasing integer net stabilizes at some `y₀ ∈ ∩R_{p,q}`; its depth-`p` backward chains are **compatible under truncation because the prescribed predecessor is unique** (item 1 — this is the step the external suggestion asserted without mechanism; make it explicit), so they union into one infinite chain, and the forward half is deterministic. Handle the liveness edge honestly: `y₀ ∈ ∩R_{p,q}` is live by definition of `R`; note in one sentence why every chain door is live (`G`-images).
   - **The three-notion separation, stated once:** finite symbolic legality — always (14.15.2, full shift); finite positive realization — always (item 2); realization at all depths — equivalent to bounded height, and its failure mode is `H_{p,q} → ∞`: **archimedean escape**, the precise sense in which a word can be finitely compatible everywhere yet realized by no single integer.

4. **Accounting and closing status.** Extend the mandatory accounting line: the height is another exact name for the Bridge (bridge.md §16) — *Bridge ⟷ boundedness versus escape of the positive realization height* — and supplies no estimate, recurrence, or bound on `H`. Periodic words: one sentence reconciling with 14.15.3's mandatory identification (the classical cycle candidate; not a lever; the trivial word all-`(1,1)` has `H ≡ 1`, the trivial cycle). The Bridge is exactly as open as 14.15.3's closing status left it.

## Success / stop criteria

- **Floor (expected):** items 1–2 proved and verified.
- **Primary:** items 3–4 — the definition, the equivalence theorem with the uniqueness mechanism explicit, the three-notion separation, the closing status.
- **Stop:** after item 4, stop. Explicitly forbidden, whatever the results suggest: **any empirical study of `H`'s growth** (sampling `H` on random words, growth-rate fits, distribution scans — the definition is the deliverable; growth study is the parked statistical front in new clothes); any characterization attempt on the diagonal locus beyond the equivalence theorem (that is the converse question, reserved for a separate main-session decision); any cycle-exclusion attempt; any equidistribution proof attempt. Verification code may compute `H` only on the small sanity families named in item 3's checks. Off-brief findings go to `briefs/bicylinder-height-findings.md`; log them and stop anyway.

## Placement and numbering

- `reverse.md`: new subsection **14.15.4** holding items 1–4. Never renumber existing anchors; 14.15.3's own text is not edited (its closing status stands; your closing status extends, not replaces).
- `bridge.md` §16: one pointer sentence in 16.4.5 **iff** item 3 lands (the height as a further symbolic name); update its `updated:` field. Its charter forbids proof effort on the page.
- Cross-page status sweep per AGENTS.md when done: index.md (reverse.md row + status paragraph), HANDOFF.md one-liner.
- `publication.md`: one sentence at most (the height formulation is elementary bookkeeping on 14.15.3; the adelic-versus-integer gap at the archimedean place is standard folklore — claim nothing).

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code, not the pre-check's constructions; record what was checked, the range, seeds, and the date, inline in the owning section.
- Verification code goes in `experiments/realization_height.py`, imports nothing from `itinerary_coding.py`, `block_map.py`, or `door_seam.py`, states which results it supports, stays runnable. Exact integer arithmetic wherever a pass/fail decision is made.
- Failures and obstructions are recorded, not deleted.
- Register norm: flat, calibrated prose. Item 2 closes a question (no finite two-sided obstruction); item 3 is a *formulation*, and its honest closing sentence is that the Bridge is exactly as open as before, now with a boundedness criterion naming its archimedean content.
- Work on branch **`bicylinder-height`**, commit per item with verification in the same commit, and **do not merge to main** — the main session reviews and re-runs all verification code before merging (mirror-queue / door-seam / block-map / itinerary-coding precedent).
- No scope expansion.

## Definition of done

Items 1–2 as proved, verified additions in a new reverse.md §14.15.4; items 3–4 at formulation grade with the equivalence theorem's uniqueness mechanism explicit and the three-notion separation stated once; clean per-item commits on `bicylinder-height` with `experiments/realization_height.py` committed and passing; a closing status stating plainly what this block changed (the diagonal locus has an equivalent boundedness criterion; no finite two-sided obstruction exists) and what it did not (the Bridge, unmoved).
