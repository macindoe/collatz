---
status: REFERENCE — consolidates the anchor concept across the wiki (no proofs restated, pointers only); owns the new digit-structure search program (17.7+), not yet executed
scope: new section 17 (post-monolith); cross-cutting reference — owned by no single stage/reverse/cycles/aeh page
updated: 2026-07-12
source: consolidation of stage1.md 11.8.3.6/11.8.3.11/11.8.4.2, stage2.md 11.8.5.6, stage4.md 11.8.7, reverse.md 14.2/14.12–14.13, ladder.md §15, cycles.md 12.3/9.8.4, aeh.md §13, bridge.md §16, archive/appendix-a.md A.4.6–A.6; the author's request to centralize anchor exploration in one place (2026-07-12)
---

# 17. The Anchor: a consolidated reference

> **Current state.** This page does not prove anything and does not restate anything already proved elsewhere (one-fact-one-page, AGENTS.md) — it is the single findable place that says *where* every anchor-related fact lives, so the object doesn't stay scattered across eight pages. §17.1–17.6 are pointers only. §17.7 onward is new: a precisely scoped, not-yet-executed search for structure in the anchor's own digits, at the level of a single number rather than a statistic averaged over many — territory nothing in the wiki has touched (confirmed by checking every existing experiment script, 2026-07-12).

## 17.1. The object

Two anchors, one family, plus a mirror:

- **`N(ω)`, the 2-adic anchor** (stage1.md 11.8.3.6): defined by the congruence tower `9^n ≡ ω⁻¹ (mod 2^k)` for all `k`; identified as `N(ω) = -log ω / log 9`, a 2-adic logarithm. Native only to `ω ≡ 1 (mod 8)`.
- **`M(ω)`, the unified anchor** (stage2.md 11.8.5.6.1): `M(ω) = N(ω²)`, defined for every odd `ω`. This is the coordinate the rest of the program actually runs on — one number carries both lifting components.
- **`M₃(y)`, the 3-adic mirror anchor** (reverse.md 14.2.2): `2^(M₃(y)) = -1/y`, living in `Z/2 × Z₃` — an *affine* logarithm, not linear, the source of a real (not forced) forward/backward asymmetry.

Each is an infinite string of digits (base `2` for `N`/`M`, base `3` for `M₃`) computable to any finite precision but never in closed form.

## 17.2. Algebra

- `N` is a homomorphism (stage1.md 11.8.3.7.1) — the load-bearing fact that makes an increment law possible at all.
- `M(ω)`'s parity tracks the lifting branch (stage2.md 11.8.5.6.2).
- `M₃` is affine, not linear (reverse.md 14.2.3) — later identified (14.13) as the reason no stationary residue system exists backward.
- Computable by a convergent series to any precision (stage1.md, remark after 11.8.3.6.6) — the practical route to any actual digit, as opposed to the astronomically-large-but-effective Baker constants (17.4).

## 17.3. Per-step laws built on it

Pointers only, in dependency order:

- Global valuation law `s = 3 + v₂(n - N(ω))`, unified `s = 2 + v₂(d - M(ω))` (stage1.md 11.8.4.1, stage2.md 11.8.5.6.2).
- Increment identity `ΔM = N((ω_+/ω)²)` (stage2.md 11.8.5.6) — the fiber-to-orbit bridge is exactly "does `ΔM` have a usable law."
- Low-order law for `ΔM mod 2^k`, digit-determinacy lemmas (stage4.md 11.8.7.2.1–3, 11.8.7.3.1) — proved, `σ`-graded modulus, verified.
- One-step propagation trichotomy (stage4.md 11.8.7.6.1) — decide / decide / report-deep, error-free.
- The digit budget (stage4.md 11.8.7.7) — no bounded window decides infinite horizons; the anchor is spent, not regenerated.
- Backward valuation law `d = 1 + v₃(s - M₃(y))` (reverse.md 14.2.4) — the exact mirror.
- Steering laws (reverse.md 14.12) and the one-identity synthesis (14.12.3): the anchor is *placeable* backward to bounded modulus — literally the forward law read from the other end.
- Ladder law (ladder.md 15.1–15.3): at fixed anchor, adjacent depths are one Collatz step apart except at anchor digit-matches ("spikes"), where an affine kick tears them apart. Spikes = anchor digit matches, made fully explicit.

## 17.4. Effective bounds

- stage1.md 11.8.3.11: Bugeaud–Laurent (1996), Corollaire 2 — `C(ω) = 208·log9·logω`, exponent exactly `2`. Pinned and numerically checked 2026-07-12.
- Corollary 11.8.3.11.2: the same bound read as a digit-match cap — an integer of size `n` matches at most `O((log n)²)` leading anchor digits. This is an unconditional ceiling on how long an agreement can last; it says nothing about how often agreements of a given length actually occur (that's §17.6/17.7's territory).

## 17.5. Cycles: the anchor walk

- spine.md 9.8.4 (anchor-form remark): a nontrivial cycle is a finite closed walk in `Z₂` with `Σ ΔM_t = 0`.
- cycles.md §12.3: the stratum-sequence congruence system is this walk's finite-precision shadow.
- cycles.md 12.8.2's explicit `n_0(p)` (pinned 2026-07-12) is downstream of the anchor via `Λ = K log2 - n log3`, not itself a digit-structure argument — the rigidity *target* is anchor-walk closure, the tool used to bound it is classical Baker theory, not digit statistics.

## 17.6. Statistics: AEH (the existing, cross-sectional layer)

- stage1.md 11.8.4.2: first empirical hint — digit density `0.497` across `2,499` families.
- aeh.md §13: the real depth — bulk-form hypothesis (13.2.1), conditional theorems on what it buys and doesn't (13.3), an 8-round calibration campaign (13.4), one anomaly chased down and dissolved with a routing lemma (13.5).
- Every test in aeh.md is **cross-sectional**: it asks "averaged over many orbits/states, does this statistic match the coin-flip prediction?" None of it looks at one anchor's own bit string as a standalone object.
- Bulk-vs-bottom split (aeh.md 13.1): small numbers are known-structured; the hypothesis only claims to hold in the bulk.

## 17.7. The open question this page exists for: single-sequence structure

Everything in 17.1–17.6 either proves an exact law or checks an ensemble average. Nothing tests whether **one `M(ω)`, read as a single bit string, has internal structure** — autocorrelation, periodicity, compressibility, self-similarity. Confirmed by checking every experiment script in the repo (2026-07-12): none does intra-sequence testing; none even prints the raw bits for inspection.

**Historical precedent, and one already-closed door.** Appendix A.4.6 computed ones-counts in the first 24 digits for seven historically-flagged `ω` (`ω=25→14, ω=49→15, ω=73→15, ω=17→10, ω=41→12, ω=65→8, ω=89→8`), read them as a `Binomial(24, 1/2)` draw, and separately audited `2,499` families for a dependence of anchor digits on `ω mod 3` — found none. That rules out one specific candidate correlate; it is not evidence about autocorrelation, periodicity, or compressibility, which were never tested.

**Why this is in scope, not parked.** README's stopping rule on AEH is explicit: "proof effort waits until there is an idea, because 'grind harder' provably cannot work there" — but the same rule permits exactly this: "experiments may feed the ledger." A structure hunt is not proof effort; it either finds something (real progress, an idea to work) or comes back clean (strengthens the calibration on a new, harder axis). Both outcomes are legitimate per house norms (cf. cycles.md 12.8's own "a clean negative is a publishable result").

**A concrete worked example**, computed 2026-07-12 (first 24 bits of `M(ω)`, lsb first):

```text
ω= 1  000000000000000000000000   (M(1)=0 exactly — the fixed point)
ω= 3  111111111111111111111111   (M(3)=-1 exactly — 3²=9 is the log's own base)
ω= 5  101011110100001111101100
ω= 7  010010101101111111001101
ω=11  100110111000001010010011
ω=13  110111011010100100010110
ω=17  001100100100010001101100
ω=19  110000011010111111001110
ω=23  011001111111100000001110
ω=29  111011010111011110110011
ω=31  000101001100101110110001
ω=37  101101110100011110111111
```

`ω=1,3` are exact algebraic degeneracies (fixed point; `3²` is literally the log's base) — consistent with the known bottom/structured regime, not counterevidence to the bulk hypothesis. The rest is what an actual test battery needs to be run against, not eyeballed.

## 17.8. Search plan (scoped 2026-07-12, not yet executed)

In order of cost and how surprising a positive finding would be:

1. **Single-sequence statistics.** Run-length distribution of `0`/`1` runs within one `M(ω)` against the geometric null; autocorrelation `R(k)` for lags `k = 1..~64`; chi-squared on overlapping 3–5-bit windows within one long string (aeh.md only ever checked bit pairs, cross-sectionally).
2. **Compressibility.** Lempel–Ziv complexity or a standard compressor against the raw bit string — the cleanest single number: incompressible-within-noise supports randomness, any real compression *is* a discovered structure by construction. The NIST SP 800-22 battery (frequency, block-frequency, runs, DFT, approximate entropy, serial, cumulative sums) exists exactly for this — run it, don't reinvent it.
3. **Spectral.** DFT of the bit sequence (mapped to `±1`); check flatness. The anchor is built from a discrete log mod `2^k` — not obviously periodic, but untested, so check rather than assume.
4. **Cross-string, but structurally new.** A.4.6 ruled out `ω mod 3`; sweep a few more cheap candidate correlates (`ω mod 16`, `ω mod 32`, digit sum of `ω`) the same way, and separately test the *residual* high-order digits of `ΔM` beyond what the proved low-order law (11.8.7.3.1) already accounts for, so the test targets the genuinely open part.
5. **Literature, not computation.** Read what the Bernstein–Lagarias 2-adic shift conjugacy (cited in publication.md's landscape survey) actually delivers, and whether its natural invariant measure is provably aeh.md's `π_k` product law. If so, that is a real candidate route to an actual proof (Borel-normal-number style: almost every point is generic, even though no specific point is provably so) rather than more calibration. Scoped as a reading task, explicitly not required for the computational tiers above to proceed.

## 17.9. Visualization plan (scoped 2026-07-12, not yet built)

Two recommended first, cheap and complementary — one screens for self-similarity/periodicity, the other for general bias, and both are legible to the eye before any statistic is computed:

- **Recurrence plot ("fold it onto itself").** Compare length-`w` windows at every offset `i` against every offset `j`; darken `(i,j)` where they match closely. Random strings light up only the diagonal plus scattered noise; self-similarity or periodicity shows as off-diagonal stripes or blocks.
- **Chaos game representation.** Walk a point halfway toward one of two square corners per bit (corner `0` / corner `1`); plot every intermediate point. Standard bioinformatics technique for screening DNA for non-randomness. True randomness fills the square as uniform fog; bias or forbidden patterns show as visible gaps or genuinely fractal, self-similar structure in the fill.

Second tier, if the first pair turns up anything worth chasing:

- **Period-fold ("waterfall") plot.** Reshape the bit string into a `w`-column image, one row per `w` bits; sweep `w`. A real periodicity locks the image into stripes at the matching `w`; a wrong `w` looks like noise.
- **Delay embedding / return map.** Read non-overlapping `k`-bit windows as points in `[0,1)`; plot `(x_i, x_{i+1})`. Randomness scatters uniformly; hidden low-dimensional structure collapses the scatter onto a curve or sparse set — the natural visual companion to the ergodic/shift-conjugacy angle (17.8, item 5).

Deliverables should follow existing convention: interactive exploration in `viz/` (alongside `anchor_field_explorer.html`), raw analysis and any batteries in `experiments/`.

## 17.10. Standing

This page is a reference and a scoped, unexecuted program — not a result. When the search runs (see `briefs/anchor-digit-search-brief.md`), its findings update §17.7 in place (a discovery, or a documented clean pass) rather than adding a new page; the delegation pattern (mirror-queue, kl-lp) is the precedent for how that session should be run and reviewed.
