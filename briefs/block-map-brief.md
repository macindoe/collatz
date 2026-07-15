# Brief: the block-map identity and the composed door law — a §14.14 corollary layer (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — item 4 walks the edge of a parked front), `AGENTS.md` (binding house norms), `reverse.md` §14.14 entire (the door/exit seam — this brief adds a corollary layer to it), 14.2.2 (the exponent group `E₃` and `M₃`), 14.7.1 (fact `(a′)`), spine.md §9.8 (the odd Collatz map `T` and the reduction equivalence), cycles.md §12.1 (the cycle product equation — item 4(b) reconciles with it), stage4.md 11.8.7.7 (the digit budget), bridge.md §16 (charter: pointers only, no proof effort on the page).

## Provenance and pre-check

This brief packages an external suggestion (ChatGPT, 2026-07-15) reviewing the merged §14.14, assessed by the main session against the live pages before delegation. Pre-checked with fresh throwaway code (seed 20260715, 2026-07-15):

- **Block-map identity** `G(y) = T^{v₂(y+1)}(y)`: 4,000 random live doors (4–64 bits), 0 failures.
- **Valuation word:** the suggestion's claimed word `(1,…,1 [m−1 times], r)` is **wrong** — it failed on all 4,000 doors. The corrected word `(1,…,1 [m−1 times], r+1)` passed all 4,000. Target the corrected form; the suggestion's own example (`7→11→17→13`, valuations `(1,1,2)`, `r=1`) exhibits the off-by-one.
- **Fixed-stratum metric law:** `v₃(ΔM₃(z) − ΔM₃(y)) = v₃(z−y) − 1` on same-`(m,r)`-stratum pairs with `v₃(z−y) ≥ 1`: 2,802 pairs, 0 failures. The suggestion omits the hypothesis `v₃(z−y) ≥ 1`; the boundary case carries its own law — the **parity biconditional** `v₃(z−y) = 0 ⇔ ΔM₃(z) − ΔM₃(y) odd` was separately pre-checked on 4,000 same-stratum pairs (264 with `v₃ = 0`, 3,736 with `v₃ ≥ 1`), 0 failures.
- **Rejected criticism:** the suggestion claims 14.14.5's existing tightness argument is "not logically sufficient" (two terms could cancel their top-digit dependence). Examined and **rejected**: every live door has `m = v₂(y+1) ≥ 1`, so `M₃(G(y)) mod 3^k` is a function of `y mod 3^{k+1−m}` — flatly independent of the top digit — and cancellation would require *both* terms to depend on it. The existing tightness paragraph stands. Item 3 adds a strengthening *next to* it; **do not rewrite the existing paragraph as if it were broken.**

So the mathematical targets are true in their corrected forms; your job is to prove them at house standard and place them. Your verification code must be your own fresh implementation, per AGENTS.md — the pre-check scripts are deliberately not provided.

## The state you are starting from

§14.14 is closed and merged: the exit map `G` (14.14.3) is total and mortality-free, an exact `3`-adic contraction on fixed `(m,r)`-strata (14.14.4), carrying a constant-offset graded `ΔM₃` law (14.14.5), with the core-extraction deficit relocated — not evaded — onto the `2`-adic stratum word (14.14.6). Its closing status reserved one decision for the main session: composing the law along orbits. This brief is that decision, taken with a deliberately bounded scope: an interpretation (item 1), a wording repair (item 2), a metric-law strengthening (item 3), and the composition layer with its classical reconciliation (item 4). Nothing here changes the Bridge's status, and no item below is licensed to claim otherwise.

## Queue, in order

1. **The block-map identity.** New subsection **14.14.7**. Let `T(x) = (3x+1)/2^{v₂(3x+1)}` be the accelerated odd Collatz map (spine.md §9.8). For a live door `y` with `m = v₂(y+1)`, `q = (y+1)/2^m`, prove:

   ```text
   T^j(y) = 3^j 2^{m−j} q − 1   (0 ≤ j < m),      T^m(y) = G(y),
   ```

   so `G` is the **variable-return-time block map** of `T`, with return time `m = v₂(y+1)`. Prove the valuation word of the passage (the successive `v₂(3x+1)` values) is `(1,…,1 [m−1 times], r+1)` — note its sum is `m + r`, matching the `2`-power `2^{m+r}` in the affine law 14.14.4.1 (state this consistency check). Cross-checks, one sentence each: totality and live image of `G` (14.14.3.2(3)) also follow from `T`'s totality on odd integers; the worked instance `7 → 11 → 17 → 13` (`m = 3`, `r = 1`, word `(1,1,2)`). Optional remark, **do not force**: the relation between the return time `m` and the spine's block/cascade decomposition (§9.8), if it is clean; if it is not clean, record the obstruction instead of forcing the analogy.

2. **Terminology repair (wording-only, separate commit).** Theorem 14.14.3.2(1) is titled "`G` conjugates `F`". The proved identity `state ∘ G = F ∘ state`, with `state` many-to-one and `G` constant on its fibers (property 2 of the same theorem), is a **semiconjugacy**: `G` is an extension (factor presentation) of `F`, and the quotient of doors by "same state" induces a map conjugate to `F` — the one-step fiber collapse is part of the structure, not a defect. Retitle the theorem clause, adjust the gloss in 14.14.3's Content paragraph and the §14.14 intro if it repeats the word, and sweep the phrase elsewhere (HANDOFF.md's one-liner currently says "`F` conjugated to door coordinates"). **No mathematical content changes in this commit** — same register class as the unit/isometry fix already in the git history (d517d8f).

3. **The total two-case metric law.** Append to 14.14.5 (as Lemma/Theorem 14.14.5.4 — never renumber existing anchors). For `y, z` on the same `(m,r)`-stratum:

   ```text
   (i)  v₃(z−y) = 0  ⇔  ΔM₃(z) − ΔM₃(y) is odd        (parity component in E₃);
   (ii) v₃(z−y) ≥ 1  ⇒  the difference is even, and
        v₃(ΔM₃(z) − ΔM₃(y)) = v₃(z−y) − 1              (exactly).
   ```

   Proof route (verify, don't transcribe): put `H(y) = y/G(y)`, so `2^{ΔM₃(y)} = H(y)` (Lemma 14.14.5.2); on the stratum,

   ```text
   H(z)/H(y) − 1 = (3^m − 2^m)(z − y) / (y · (3^m z + 3^m − 2^m)),
   ```

   whose denominator is a `3`-adic unit (`3 ∤ y`; `3^m z + 3^m − 2^m = 2^{m+r} G(z)` with `3 ∤ G(z)`) and `v₃(3^m − 2^m) = 0`, so `v₃(H(z)/H(y) − 1) = v₃(z−y)`. Then in `E₃` (via `Z₃ˣ ≅ {±1} × (1+3Z₃)`): parity of the exponent detects `H(z)/H(y) ≡ 2 (mod 3)`, i.e. case (i); and for even exponents `e`, `v₃(2^e − 1) = 1 + v₃(e)` — prove this small lemma (e.g. `4 = 1+3` and the standard lifting argument), giving case (ii). **Register:** this *strengthens* the existing tightness paragraph (which stands — see pre-check) from an existence statement into an exact per-stratum metric law; present it flatly as a corollary-grade strengthening, and note in one sentence that it re-derives tightness quantitatively (take `v₃(z−y) = k`). It implies the constant offset `1` is an exact local law, not merely un-slack at the sampled points.

4. **Composition along fixed itineraries.** New subsection **14.14.8**. For a finite itinerary of strata `(m₀,r₀), …, (m_{n−1},r_{n−1})`, prove `Gⁿ` is affine over `Z₃` on the set of doors following that itinerary, with multiplier `Aₙ = Π 3^{mᵢ} 2^{−(mᵢ+rᵢ)}`, `v₃(Aₙ) = Σmᵢ`, hence

   ```text
   v₃(Gⁿ(y) − Gⁿ(z)) = v₃(y − z) + Σᵢ mᵢ
   ```

   for `y, z` sharing the itinerary. Then three corollaries, each proved:

   **(a) Synchronization.** Once `Σmᵢ ≥ k+1`, the door `yₙ mod 3^{k+1}` is determined by the itinerary alone, independent of `y₀`; consequently `M₃(yₙ) mod 3^k` (fact `(a′)`, 14.7.1) and every subsequent increment `ΔM₃ mod 3^k` (14.14.5.3) are word-determined. Stated flatly: along any orbit, the `3`-adic anchor's residues at every fixed precision are eventually a function of the `2`-adic stratum word alone.

   **(b) Periodic-word fixed point — with mandatory reconciliation.** For a periodic itinerary, `v₃(Aₙ) ≥ n ≥ 1`, so `1 − Aₙ` is a `3`-adic unit and the composed affine map has a unique fixed point `y* = Bₙ/(1−Aₙ) ∈ Z₃`; any cycle of `G` carrying that word has door `y*`. **Identify `y*` with the classical rational cycle candidate of cycles.md §12.1** — this is the classical cycle-equation fact ("the valuation word determines the unique rational cycle candidate") read in door coordinates, **not a new exclusion lever**; say so explicitly, with pointers to §12.1 and to README's stopping rule (the cycle front is parked and reopens only on a divisibility-aware idea *beyond* this classical candidate). Sanity instance for the verification code: the trivial fixed point `(1,1)` has the single door `y = 1`, word `(m,r) = (1,1)`, `A = 3/4`, `B = 1/4`, `y* = (1/4)/(1/4) = 1`. ✓

   **(c) Accounting sentence.** One flat sentence extending 14.14.6: the `3`-adic side of the ledger is not merely cheap per step but asymptotically *free* — beyond the first `k+1` accumulated `m`-digits, all information at precision `3^k` is the word — which sharpens, and does not change, the relocation verdict. Do not let (a) or (b) be quoted anywhere without this sentence next to them.

## Success / stop criteria

- **Floor (expected):** items 1–3 — checked-true statements with short proofs, plus a wording repair.
- **Primary:** item 4 with the reconciliation (b) and the accounting sentence (c).
- **Stop:** after item 4, stop. Explicitly forbidden, whatever item 4 suggests: any cycle-exclusion attempt launched from 4(b) (parked front; reopening is a main-session decision requiring a divisibility-aware idea beyond the classical candidate); any statistics of stratum words or numerical iteration of `G` (the §17.7 program is at its natural endpoint); any density-exponent computation (closed per 14.13's stop criterion); any equidistribution proof attempt (parked by the stopping rules). Off-brief findings go to `briefs/block-map-findings.md`; log them and stop anyway.

## Placement and numbering

- `reverse.md`: new subsections **14.14.7** (item 1) and **14.14.8** (item 4); item 2 edits inside 14.14.3 (wording only); item 3 appends inside 14.14.5. Never renumber existing anchors.
- `bridge.md` §16: a pointer-only sentence **iff** item 4 lands (its charter forbids proof effort on the page); update its `updated:` field.
- Cross-page status sweep per AGENTS.md when done, including the HANDOFF.md one-liner and item 2's phrase sweep.

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code, not the code that suggested the result; record what was checked, the range, seeds, and the date, inline in the owning section.
- Verification code goes in `experiments/` (suggested `experiments/block_map.py`), states which results it supports, stays runnable.
- Failures and obstructions are recorded, not deleted.
- Register norm: flat, calibrated prose. Item 1 is an *interpretation* of known dynamics; item 3 is a *strengthening*, not a repair; item 4(b) is a *reconciliation with a classical fact*, not a lever. The external suggestion called 4(b) "the most consequential result of the seam" — that framing is exactly the excitement inflation the house norms forbid; do not import it.
- Work on branch **`block-map`**, commit per item with verification in the same commit, and **do not merge to main** — the main session reviews and re-runs all verification code before merging (mirror-queue / door-seam precedent).
- No scope expansion.

## Definition of done

Items 1, 3, 4 as proved, verified additions to reverse.md §14.14; item 2's wording repair and phrase sweep; bridge.md pointer iff item 4 lands; clean per-item commits on `block-map` with `experiments/block_map.py` committed and passing; a closing sentence in 14.14.8 stating plainly what this layer changed (a corollary layer on the seam; the Bridge's status unchanged).
