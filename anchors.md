---
status: REFERENCE (pointers only); the single-sequence digit-structure search it formerly carried (§17.7–17.10) is executed and clean at every endpoint — see anchor-digit-search.md
scope: sections 17.1–17.6 (post-monolith); cross-cutting reference — owned by no single stage/reverse/cycles/aeh page; §17.7–17.10 split to anchor-digit-search.md 2026-07-23
updated: 2026-07-23
source: consolidation of stage1-synthesis.md 11.8.3.6/11.8.3.11, stage1.md 11.8.4.2, stage2.md 11.8.5.6, stage4.md 11.8.7, reverse.md 14.2/14.12–14.13, ladder.md §15, cycles.md 12.3/9.8.4, aeh.md §13, bridge.md §16, archive/appendix-a.md A.4.6–A.6; the author's request to centralize anchor exploration in one place (2026-07-12)
---

# 17. The Anchor: a consolidated reference

> **Current state.** This page does not prove anything and does not restate anything already proved elsewhere (one-fact-one-page, AGENTS.md) — it is the single findable place that says *where* every anchor-related fact lives, so the object doesn't stay scattered across eight pages. §17.1–17.6 are pointers only. The single-sequence digit-structure search this page formerly carried (§17.7–17.10) now lives at `anchor-digit-search.md`: executed, a clean pass at every endpoint.

## 17.1. The object

Two anchors, one family, plus a mirror:

- **`N(ω)`, the 2-adic anchor** (stage1-synthesis.md 11.8.3.6): defined by the congruence tower `9^n ≡ ω⁻¹ (mod 2^k)` for all `k`; identified as `N(ω) = -log ω / log 9`, a 2-adic logarithm. Native only to `ω ≡ 1 (mod 8)`.
- **`M(ω)`, the unified anchor** (stage2.md 11.8.5.6.1): `M(ω) = N(ω²)`, defined for every odd `ω`. This is the coordinate the rest of the program actually runs on — one number carries both lifting components.
- **`M₃(y)`, the 3-adic mirror anchor** (reverse.md 14.2.2): `2^(M₃(y)) = -1/y`, living in `Z/2 × Z₃` — an *affine* logarithm, not linear, the source of a real (not forced) forward/backward asymmetry.

Each is an infinite string of digits (base `2` for `N`/`M`, base `3` for `M₃`) computable to any finite precision but never in closed form.

## 17.2. Algebra

- `N` is a homomorphism (stage1-synthesis.md 11.8.3.7.1) — the load-bearing fact that makes an increment law possible at all.
- `M(ω)`'s parity tracks the lifting branch (stage2.md 11.8.5.6.2).
- `M₃` is affine, not linear (reverse.md 14.2.3) — later identified (14.13) as the reason no stationary residue system exists backward.
- Computable by a convergent series to any precision (stage1-synthesis.md, remark after 11.8.3.6.6) — the practical route to any actual digit, as opposed to the astronomically-large-but-effective Baker constants (17.4).

## 17.3. Per-step laws built on it

Pointers only, in dependency order:

- Global valuation law `s = 3 + v₂(n - N(ω))`, unified `s = 2 + v₂(d - M(ω))` (stage1.md 11.8.4.1, stage2.md 11.8.5.6.2).
- Increment identity `ΔM = N((ω_+/ω)²)` (stage2.md 11.8.5.6) — the fiber-to-orbit bridge is exactly "does `ΔM` have a usable law."
- Low-order law for `ΔM mod 2^k`, digit-determinacy lemmas (stage4.md 11.8.7.2.1–3, 11.8.7.3.1) — proved, `σ`-graded modulus, verified.
- One-step propagation trichotomy (stage4.md 11.8.7.6.1) — decide / decide / report-deep, error-free.
- The digit budget (stage4.md 11.8.7.7) — the anchor is provably spent per step, not regenerated; that no bounded window decides infinite horizons is the organizing heuristic, not a formalized theorem.
- Backward valuation law `d = 1 + v₃(s - M₃(y))` (reverse.md 14.2.4) — the exact mirror.
- Steering laws (reverse.md 14.12) and the one-identity synthesis (14.12.3): the anchor is *placeable* backward to bounded modulus — literally the forward law read from the other end.
- Ladder law (ladder.md 15.1–15.3): at fixed anchor, adjacent depths are one Collatz step apart except at anchor digit-matches ("spikes"), where an affine kick tears them apart. Spikes = anchor digit matches, made fully explicit.
- Door/exit seam (reverse.md 14.14): `ΔM` as one fixed operation's mismatch across the live door, with the door-anchor extension `J(n) = M(n) + v₃(n)` (closed form, reverse.md 14.14.2.3).
- Whole-period realization-height laws along fixed periodic words (itinerary.md 14.15.9) — the anchor's height bookkeeping over a full period, both sectors, one unified law.

## 17.4. Effective bounds

- stage1-synthesis.md 11.8.3.11: Bugeaud–Laurent (1996), Corollaire 2 — `C(ω) = 208·log9·logω`, exponent exactly `2`. Pinned and numerically checked 2026-07-12.
- Corollary 11.8.3.11.2: the same bound read as a digit-match cap — an integer of size `n` matches at most `O((log n)²)` leading anchor digits. This is an unconditional ceiling on how long an agreement can last; it says nothing about how often agreements of a given length actually occur (that's §17.6/17.7's territory — §17.7 at `anchor-digit-search.md`); the ceiling's rational-anchor instance is the spent `|q| = 1` stock (cycles.md 12.6.1.3).

## 17.5. Cycles: the anchor walk

- spine.md 9.8.4 (anchor-form remark): a nontrivial cycle is a finite closed walk in `Z₂` with `Σ ΔM_t = 0`.
- cycles.md §12.3: the stratum-sequence congruence system is this walk's finite-precision shadow.
- cycles.md 12.8.2's explicit `n_0(p)` (pinned 2026-07-12) is downstream of the anchor via `Λ = K log2 - n log3`, not itself a digit-structure argument — the rigidity *target* is anchor-walk closure, the tool used to bound it is classical Baker theory, not digit statistics.
- cycles.md 12.6.1.2: the near-miss anchors of the four known cycles — the spent `|q| = 1` stock and the side-asymmetry; the stock identified as the rational-anchor instance of the digit-match cap (cycles.md 12.6.1.3); the per-cycle door-word ↔ anchor correspondence stated as a lemma (itinerary.md 14.15.10.1).

## 17.6. Statistics: AEH (the existing, cross-sectional layer)

- stage1.md 11.8.4.2: first empirical hint — digit density `0.497` across `2,499` families.
- aeh.md §13: the real depth — bulk-form hypothesis (13.2.1), conditional theorems on what it buys and doesn't (13.3), an 8-round calibration campaign (13.4), one anomaly chased down and dissolved with a routing lemma (13.5), and the named symbolic equivalence (13.6, the genericity form): AEH ⟺ bulk Bernoulli-genericity of the door letter word.
- Every test in aeh.md is **cross-sectional**: it asks "averaged over many orbits/states, does this statistic match the coin-flip prediction?" None of it looks at one anchor's own bit string as a standalone object.
- Bulk-vs-bottom split (aeh.md 13.1): small numbers are known-structured; the hypothesis only claims to hold in the bulk.
- External replication (aeh.md 13.4, measured grade): an independent implementation reproduces the class skeleton's exact values and the ledger.

## 17.7. The single-sequence digit-structure search — split to `anchor-digit-search.md`

The search program this page formerly carried (§17.7–17.10) lives at `anchor-digit-search.md`:

- **§17.7** — the executed search: clean at every endpoint (breadth and depth statistical batteries, the automaticity screen — `M(ω)` not 2-automatic, three operation lenses, PractRand to 1 GB).
- **§17.8–17.9** — the planned search and visualization axes (scoped 2026-07-12; executed — results in §17.7.1).
- **§17.10** — standing.
