# Brief: the itinerary language — the cylinder theorem and the two-sided coding (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules**), `AGENTS.md` (binding house norms), `reverse.md` §14.14 entire (the door/exit seam and its block-map corollary layer — this brief opens the layer that 14.14.8's closing status reserved for a main-session decision), spine.md §9.1/§9.8 (blocks, the odd map `T`, the reduction equivalence), stage3.md 11.8.6.3 (`m₊`), stage4.md 11.8.7.7 (the digit budget), bridge.md §16 (charter: pointers only), publication.md (the novelty register — item 1's framing mandate depends on it), aeh.md 13.2 (`π_k`, for one pointer sentence only).

## Provenance and pre-check

This brief packages an external suggestion (ChatGPT, 2026-07-16) reviewing the merged block-map layer, assessed by the main session against the live pages before delegation. The suggestion's reading of §14.14.7–14.14.8 is accurate (corrected valuation word, return-time caveat, classical-candidate reconciliation all correctly reported). Pre-checked with fresh throwaway code (2026-07-16):

- **Cylinder theorem:** over *all* odd `y < 2^21`, itinerary length 3: **5,005 distinct stratum words, every one exactly one odd residue class mod `2^(S+1)`** (`S = Σ(mᵢ+rᵢ)`), in both directions — every follower lies in the class, every odd class member follows the word — 0 failures; all 81 length-2 words over `m, r ≤ 3` occur. The suggestion's modulus claim is exact, including the `+1`.
- **Framing miss, not an error (item 0):** the suggestion presents 14.14.5.4 as "genuinely two-case." The author's standing observation (pre-dating this brief) is sharper: the law is intrinsically **one-case** — line `(*)` of 14.14.5.4's own proof plus Lemma 14.14.5.2 give `v₃(2^(ΔM₃(z)−ΔM₃(y)) − 1) = v₃(z−y)` unconditionally — and the two-case form is its expression in `(parity, v₃)` coordinates on `E₃`, where the boundary level would read "`v₃ = −1`," which is meaningless; the parity clause is what carries that level. This is currently implicit in the proof and recorded nowhere as a statement. Item 0 records it.

So the mathematical target of item 1 is true as stated; your job is to prove it at house standard, frame it honestly against the classical literature, and place it. Your verification code must be your own fresh implementation, per AGENTS.md — the pre-check script is deliberately not provided.

## The framing mandate (read before item 1)

The cylinder theorem is **not new mathematics**. It is the classical coding fact for the Collatz map — Terras (1976; already cited in paper 1's bibliography) and Everett (1977) proved the parity-vector version: the first `n` parities are periodic in the start value with period `2^n`, each vector realized on exactly one class. The accelerated valuation-word form is standard (Lagarias's survey; Wirsching). What is being added is only: the same fact read in the door/`(m,r)` alphabet, tied to the seam's own strata, with its consequences for *this program's* search space stated once. Present it exactly so — "the classical coding, in door coordinates" — and update publication.md's register accordingly. Any prose implying a new discovery about `T` violates the house register norm.

## Queue, in order

0. **The one-case remark (wording-only, separate commit).** Append one flat remark to 14.14.5.4's Content paragraph: the two-case statement is the coordinate expression of the single law `v₃(2^(ΔM₃(z)−ΔM₃(y)) − 1) = v₃(z−y)` (immediate from line `(*)` and Lemma 14.14.5.2 — cite, don't re-derive); in `(parity, v₃)` coordinates the `k = 0` level would read "`v₃(Δ) = −1`," which is meaningless, and the parity biconditional (i) is what carries that level. No mathematical content changes; the proof already contains the fact. One-sentence verification note permitted (the unified form is what `test_metric_law_algebra` in `experiments/block_map.py` already checked via `(*)`); no new code required for this item.

1. **The finite-itinerary cylinder theorem.** New top-level subsection **14.15** (the seam 14.14 is closed; never renumber existing anchors). For every finite word `W = ((m₀,r₀), …, (m_{n−1},r_{n−1}))` with all `mᵢ, rᵢ ≥ 1`, writing `S = Σᵢ (mᵢ + rᵢ)`:

   ```text
   The odd integers following W (yᵢ on stratum (mᵢ,rᵢ) for all i, y_{i+1} = G(yᵢ))
   form exactly one odd residue class mod 2^(S+1).
   ```

   Corollaries, each proved: **(a) completeness** — every finite word over the alphabet `{(m,r) : m, r ≥ 1}` is realized (the class is nonempty); **(b) liveness** — the class, having modulus coprime to 3, contains infinitely many live doors (`3 ∤ y`); only the initial door needs this check, since `G`-images are never divisible by 3 (14.14.7.1 cross-check); **(c) the single-stratum base case** — stratum `(m,r)` alone is one class mod `2^(m+r+1)`.

   Proof route (verify, don't transcribe): the stratum conditions are `y ≡ 2^m − 1 (mod 2^(m+1))` and `q ≡ 3^(−m)(1 + 2^r) (mod 2^(r+1))` for `q = (y+1)/2^m` — one class mod `2^(m+r+1)`; on that class the affine law 14.14.4.1 gives the 2-adic parametrization `G(y₀ + 2^(m+r+1) t) = G(y₀) + 2·3^m t`, so `G` is a level-shifting bijection of cylinders (`y mod 2^(m+r+1+j)` ↔ `G(y) mod 2^(1+j)`, all odd classes hit); induct along the word. An equivalent route pulls back through the block-map identity 14.14.7.1 letter by letter (each `(mᵢ,rᵢ)` expands to the `T`-valuation word `(1,…,1, rᵢ+1)`, and `3x+1 = 2^a x'` pulls cylinders back uniquely since 3 is a unit mod every power of 2) — state in one sentence that the two routes agree because the expansion has sum `mᵢ + rᵢ`, matching 14.14.4.1's denominator. Frame per the mandate above, with citations.

2. **Consequences, recorded as calibration (flat, one short block, same subsection).**
   - The itinerary language is the **full shift** on the alphabet `{(m,r) : m, r ≥ 1}`: no forbidden words, no finite forbidden transitions, hence **no finite-state admissibility graph exists to supply rigidity** — the search region "hidden finite-level order in the stratum word" is closed by proof, not by testing. Cross-reference the finite-state-chart remark (stage4.md 11.8.7.3.1) and sweep open-problems.md for any entry this calibrates.
   - One pointer sentence, no more: the cylinder's natural measure `2^(−(S+1))` is exactly what aeh.md's product law `π_k` (13.2) quantifies along orbits; AEH is thereby *precisely* the statement that actual orbits' words equidistribute against the cylinder measure. Do not restate aeh.md's content (one fact, one page) and do not run any statistic.
   - The accounting sentence, mandatory wherever items 1–3 are quoted (extends 14.14.6/14.14.8): completeness means the word carries **no structural discount** — the Bridge's remaining content is the word at unbounded length, and the word is free at every finite level; nothing here reduces how much of it an infinite orbit requires.

3. **The two-sided coding (formulation-grade only).** Same subsection, sequel block. Three precise statements with proofs, plus one definition:
   - **(a) The future determines the 2-adic coordinate.** A right-infinite word gives nested cylinders with strictly increasing moduli (`S` grows by `≥ 2` per letter), hence a unique `y₂ ∈ Z₂`; distinct integers have distinct words (injectivity on odd integers). State plainly that this is the accelerated form of the classical 2-adic coding (Lagarias 1985's conjugacy `Φ`); whether `G` itself extends continuously to the limit point is *optional* — if it is not clean (e.g. at `y₂ = −1`, where `v₂(y+1) = ∞`), record the obstruction instead of forcing it.
   - **(b) The past determines the 3-adic coordinate.** A left-infinite word determines the present door mod `3^(k+1)` for every `k` — synchronization (14.14.8.3) is the finite-precision version; prove the limit statement (the accumulated offsets converge in `Z₃`, independent of the deep-past seed).
   - **(c) The diagonal compatibility locus — definition and trivial direction only.** A bi-infinite word yields `(y₂, y₃) ∈ Z₂ × Z₃`. Define: the word is *integrally realized* iff some integer live door `y₀` has that bi-infinite `G`-itinerary (backward steps integral and live — note every live door has integer predecessors in infinitely many strata, so bi-infinite integer orbits exist in abundance). Prove the trivial direction: an integrally realized word has `y₂ = y₃ = y₀` under the diagonal embeddings. **Mandatory identifications, stated flatly:** for periodic words this is exactly 14.14.8.4's fixed point = the classical rational cycle candidate (cycles.md §12.1) — not a lever; and characterizing the locus in general **is the Bridge in symbolic form** (bridge.md §16) — the formulation is the deliverable, and no attempt to characterize the locus beyond the definition, the trivial direction, and the periodic reconciliation is licensed here.
   - **(d) Literature check (mandatory, bounded).** The 2-adic future side is classical; search specifically for prior *two-sided* `Z₂ × Z₃` treatments of Collatz coding (Wirsching's 3-adic averages; Monks–Yazinski-type 3-adic work; solenoid/adelic formulations). One paragraph in publication.md's register style, pinned citations where found, "not found in this form" recorded honestly where not.

## Success / stop criteria

- **Floor (expected):** items 0–2 — the remark, the cylinder theorem with classical framing, the calibration block.
- **Primary:** item 3 (a)–(d) at formulation grade with both mandatory identifications.
- **Stop:** after item 3, stop. Explicitly forbidden, whatever the results suggest: **any statistics of stratum words** (frequency counts, correlation scans, PractRand-style batteries — the §17.7 program is at its natural endpoint, and item 2 proves finite-level structure search is empty); **any cycle-exclusion attempt** from periodic words (parked front; classical candidate already reconciled); **any density-exponent computation** (closed per 14.13); **any equidistribution proof attempt** (parked by the stopping rules); **any ergodic-theoretic expansion** (Bernoullicity, natural extensions, solenoid dynamics) beyond the citations item 3(d) requires. Off-brief findings go to `briefs/itinerary-coding-findings.md`; log them and stop anyway.

## Placement and numbering

- `reverse.md`: new top-level subsection **14.15** holding items 1–3; item 0 edits inside 14.14.5.4's Content paragraph (wording only, separate commit). Never renumber existing anchors.
- `bridge.md` §16: pointer-only sentences (16.1's door-centred paragraph and 16.4.5) **iff** item 3 lands; update its `updated:` field. Its charter forbids proof effort on the page.
- `publication.md`: the item 1 framing entry and the item 3(d) paragraph.
- Cross-page status sweep per AGENTS.md when done: index.md (resolver + reverse.md row + status paragraph), HANDOFF.md one-liner, open-problems.md calibration sweep from item 2.

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code, not the code that suggested the result; record what was checked, the range, seeds, and the date, inline in the owning section.
- Verification code goes in `experiments/` (suggested `experiments/itinerary_coding.py`), imports nothing from `block_map.py` or `door_seam.py`, states which results it supports, stays runnable.
- Failures and obstructions are recorded, not deleted.
- Register norm: flat, calibrated prose. Item 1 is a *classical fact in new coordinates*; item 2 closes a search region, it does not open one; item 3 is a *formulation*, and its honest closing sentence is that the Bridge is exactly as open as before, now with a symbolic name for its locus. The external suggestion's boxed slogan ("integer dynamics live on their diagonal compatibility locus") is presentation, not a theorem — do not import it as if it settled anything.
- Work on branch **`itinerary-coding`**, commit per item with verification in the same commit, and **do not merge to main** — the main session reviews and re-runs all verification code before merging (mirror-queue / door-seam / block-map precedent).
- No scope expansion.

## Definition of done

Item 0's remark in place; items 1–2 as proved, verified, classically-framed additions in a new reverse.md §14.15; item 3 at formulation grade with the two mandatory identifications and the literature paragraph; publication.md updated; clean per-item commits on `itinerary-coding` with `experiments/itinerary_coding.py` committed and passing; a closing status in §14.15 stating plainly what this layer changed (the itinerary language is fully characterized at finite level — a full shift; the Bridge unchanged, now stated symbolically) and what it forecloses (finite-level word-structure searches, by proof).
