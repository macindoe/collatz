# Brief: the ladder law as a face of the target-shift lemma (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules**), `AGENTS.md` (binding house norms), `ladder.md` §15 entire (especially 15.1's dichotomy and proof, 15.2's braid, 15.4's standing paragraph), `stage3.md` §11.8.6.3 entire (the target-shift lemma 11.8.6.3.1, the shift constant 11.8.6.3.2, and **the third reading of the Interpretation paragraph** — the sentence unifying boundary-shell localization and forced carry as two faces of the target-shift mechanism; your result adds a third face to that exact sentence), stage1.md §11.8.3.6.5 (the isometry), §11.8.4.1 (the c = 1 global valuation law).

## Provenance and pre-check

Main-session exploration (2026-07-23) of knowledge-opportunity #1 from the post-cleanup flag list: ladder.md §15.1's affine spike kick and stage3's target-shift lemma 11.8.6.3.1 look like two views of one shift mechanism, and neither page cites the other. Pre-checked with fresh throwaway code (main session, 2026-07-23; script deliberately not provided):

- **Depth step = target shift (exact, verified):** `s(ω, d+1) = v₂(3^(d+1)ω − 1) = v₂(3^d ω − 3⁻¹)` since `3` is a `2`-adic unit; more generally `s(ω, d+k) = v₂(3^d ω − 3^(−k))`. Climbing the ladder is sliding the valuation target along the family `c = 3^(−k)`. **2,742 random states, 0 failures.**
- **Two ladder steps are a literal instance of Lemma 11.8.6.3.1:** for `ω ≡ 1 (mod 8)`, `d = 2n`, `c = 9^(−j) ∈ 1 + 8 Z₂` has `N(c) = j`, and the lemma gives `v₂(3^d ω − 9^(−j)) = 3 + v₂(n + j − N(ω))` — pure translation by `j` in the anchor coordinate, trivially consistent with the `c = 1` law re-indexed. **1,318 instances (ω ≡ 1 mod 8, n ≤ 24, j ≤ 11, 2-adic precision 2^200), 0 failures.**
- **The dichotomy's valuation half is ultrametric:** the adjacent targets satisfy `v₂(1 − 3⁻¹) = v₂(2/3) = 1`. If `s(ω,d) ≥ 2` the triangle inequality forces `v₂(3^d ω − 3⁻¹) = 1`, i.e. `s(ω,d+1) = 1` — the spike branch's conclusion with no computation. If `s(ω,d) = 1` the ultrametric ties and the valuation is resolved by `v₂(3e+1)`: `s(ω,d+1) = 1 + v₂(3e+1)` (which is `≥ 2` always, since `e` is odd — this **re-derives 15.2's alternation** from the dichotomy alone). **2,742 states (1,365 spike / 1,377 off-spike), 0 failures, including the exact kick identity.**

So the flagged connection is true as pre-checked; your job is to record it at house standard. Your verification code must be your own fresh implementation, per AGENTS.md.

## The framing mandate (read before item 1)

This is a **unification note, not a new lever**. Nothing about any open problem moves. Two calibration constraints are binding:

1. **The ladder law is NOT a corollary of the target-shift lemma and must not be demoted.** The valuation half of the dichotomy (`s ≥ 2 ⟹ s' = 1`; `s = 1 ⟹ s' = 1 + v₂(3e+1)`) follows from the target-shift frame. The **integer-level half** — the exact affine kick `e ↦ 3·2^(s−1)e + 1` and the exact identity `e' = T(e)` — is content about exits, not valuations, and the valuation frame does not recover it. 15.1.1's elementary one-line proof stays as the proof of record; do not touch it.
2. The correct summary sentence is: *the depth ladder is the target-shift mechanism read in the depth variable* — the third face of the mechanism stage3's Interpretation already names twice (boundary-shell localization, forced carry). Any prose implying the ladder is "explained away", or that the unification advances the fiber-to-orbit bridge, is a register violation.

## Queue, in order

1. **The unification lemma.** New subsection **ladder.md §15.5** (15.4 "Standing" stays; never renumber existing anchors). State and prove:
   - *(a)* `s(ω, d+k) = v₂(3^d ω − 3^(−k))` for all `k ≥ 1` (one line: `3^k` is a `2`-adic unit).
   - *(b)* For even shifts on the even component (`ω ≡ 1 mod 8`, `d = 2n`, `k = 2j`): the target `9^(−j)` lies in `1 + 8 Z₂` with `N(9^(−j)) = j`, and Lemma `11.8.6.3.1` gives `v₂(3^d ω − 9^(−j)) = 3 + v₂(n + j − N(ω))` — the ladder's even steps are anchor-coordinate translations, literally instances of the target-shift lemma. Odd steps flip the residue-parity component (`3ω` bookkeeping as in `11.8.1.6.2`); state the component bookkeeping, don't belabor it.
   - *(c)* The ultrametric reading of the dichotomy: `v₂(1 − 3⁻¹) = 1`, so `s ≥ 2` forces `s(ω,d+1) = 1` by the triangle inequality; `s = 1` is the ultrametric tie, resolved exactly by the Collatz step's `v₂(3e+1)`, giving `s(ω,d+1) = 1 + v₂(3e+1) ≥ 2` — whence 15.2's alternation is a corollary of the dichotomy, not only of the first-layer classification. (Record that cross-check in one sentence.)
2. **The calibration paragraph.** Same subsection, mandatory: the integer-level kick is not recovered by the valuation frame (framing mandate item 1, in the page's own words); the unification adds understanding, not leverage; the fiber-to-orbit bridge (`11.8.5.6`) is exactly as open as before.
3. **The pointer sweep (both directions — this is the flagged gap).**
   - `stage3.md` `11.8.6.3` Interpretation, third reading: extend the existing "two faces" sentence by one clause naming the depth ladder as the third face, with a pointer to ladder.md §15.5. One clause, not a paragraph.
   - `ladder.md` front matter (`updated:`), Current-state paragraph (one added sentence), and §15.4's standing paragraph (the "second exact mechanism" sentence may now point at 15.5 for the valuation identification).
   - Do **not** restate the content in stage3 — every fact lives in exactly one page; ladder.md §15.5 owns it.

## Success / stop criteria

- **Floor:** item 1 proved and verified, item 3's pointers placed.
- **Primary (expected, given the pre-check):** all three items.
- **Stop:** after item 3, stop. Explicitly forbidden, whatever the results suggest: any attempt to compose the ladder with the per-step depth laws along orbits (that is the fiber-to-orbit bridge, `11.8.5.6`, the terminal open problem — parked); any study of the target family `c = 3^(−k)` beyond what items 1a–1c need (residue-chasing guardrail of `11.8`); any modification of 15.1's statement or proof; any touch of the other three flagged knowledge opportunities (they are separate explorations). Off-brief findings go to `briefs/ladder-targetshift-findings.md`; log them and stop anyway.

## Placement and numbering

- `ladder.md`: new subsection **15.5** holding items 1–2. Existing anchors 15.1–15.4 untouched except §15.4's one permitted pointer sentence.
- `stage3.md`: the one-clause extension of the Interpretation's third reading + pointer. `updated:` field.
- Cross-page status sweep per AGENTS.md when done: index.md (ladder.md row if its status line changes; likely a no-op — this closes no problem), HANDOFF.md one-liner. publication.md: nothing (bookkeeping-level unification; do not inflate).

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code, not the pre-check's constructions; record what was checked, the range, seeds, and the date, inline in the owning section (overwriting style, no journals).
- Verification code goes in `experiments/ladder_targetshift.py`, states which results it supports, stays runnable, imports nothing from `experiments/ladder.py` (independence). Exact integer arithmetic wherever a pass/fail decision is made; 2-adic quantities at explicit stated precision.
- Register norm: flat, calibrated prose. This is a unification note; the framing mandate's two constraints are binding.
- Work on branch **`ladder-targetshift`**, commit per item with verification in the same commit, and **do not merge to main** — the main session reviews and re-runs all verification code before merging.
- No scope expansion.

## Definition of done

Item 1 as a proved, verified lemma in a new ladder.md §15.5; item 2's calibration paragraph stating plainly what is unified (three faces of one shift mechanism at the valuation level) and what is not (the integer-level kick; the bridge); item 3's pointers in both directions so the two pages cite each other; clean per-item commits on `ladder-targetshift` with `experiments/ladder_targetshift.py` committed and passing.
