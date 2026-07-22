---
status: REFERENCE (pointers only) + the single-sequence digit-structure search (17.7), executed clean on every axis; M(ω) not 2-automatic
scope: new section 17 (post-monolith); cross-cutting reference — owned by no single stage/reverse/cycles/aeh page
updated: 2026-07-22
source: consolidation of stage1-synthesis.md 11.8.3.6/11.8.3.11, stage1.md 11.8.4.2, stage2.md 11.8.5.6, stage4.md 11.8.7, reverse.md 14.2/14.12–14.13, ladder.md §15, cycles.md 12.3/9.8.4, aeh.md §13, bridge.md §16, archive/appendix-a.md A.4.6–A.6; the author's request to centralize anchor exploration in one place (2026-07-12)
---

# 17. The Anchor: a consolidated reference

> **Current state.** This page does not prove anything and does not restate anything already proved elsewhere (one-fact-one-page, AGENTS.md) — it is the single findable place that says *where* every anchor-related fact lives, so the object doesn't stay scattered across eight pages. §17.1–17.6 are pointers only. §17.7 records a precisely scoped search for structure in the anchor's own digits, at the level of a single number rather than a statistic averaged over many — territory nothing in the wiki had touched before this. **Executed** (scoped by `briefs/anchor-digit-search-brief.md`): a clean pass across every planned test — run-length, autocorrelation, overlapping-window chi-squared, Lempel-Ziv complexity, zlib compression, the full NIST SP 800-22 battery, and spectral flatness, each against fresh independently-generated samples and, where relevant, against matched true-random controls. See §17.7.1 for the full record. This is an empirical clean pass, not a proof of anything about AEH — the brief's own scope, held to here.

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
- Whole-period realization-height laws along fixed periodic words (reverse.md 14.15.9) — the anchor's height bookkeeping over a full period, both sectors, one unified law.

## 17.4. Effective bounds

- stage1-synthesis.md 11.8.3.11: Bugeaud–Laurent (1996), Corollaire 2 — `C(ω) = 208·log9·logω`, exponent exactly `2`. Pinned and numerically checked 2026-07-12.
- Corollary 11.8.3.11.2: the same bound read as a digit-match cap — an integer of size `n` matches at most `O((log n)²)` leading anchor digits. This is an unconditional ceiling on how long an agreement can last; it says nothing about how often agreements of a given length actually occur (that's §17.6/17.7's territory).

## 17.5. Cycles: the anchor walk

- spine.md 9.8.4 (anchor-form remark): a nontrivial cycle is a finite closed walk in `Z₂` with `Σ ΔM_t = 0`.
- cycles.md §12.3: the stratum-sequence congruence system is this walk's finite-precision shadow.
- cycles.md 12.8.2's explicit `n_0(p)` (pinned 2026-07-12) is downstream of the anchor via `Λ = K log2 - n log3`, not itself a digit-structure argument — the rigidity *target* is anchor-walk closure, the tool used to bound it is classical Baker theory, not digit statistics.
- cycles.md 12.6.1.2: the near-miss anchors of the four known cycles — the spent `|q| = 1` stock and the side-asymmetry.

## 17.6. Statistics: AEH (the existing, cross-sectional layer)

- stage1.md 11.8.4.2: first empirical hint — digit density `0.497` across `2,499` families.
- aeh.md §13: the real depth — bulk-form hypothesis (13.2.1), conditional theorems on what it buys and doesn't (13.3), an 8-round calibration campaign (13.4), one anomaly chased down and dissolved with a routing lemma (13.5).
- Every test in aeh.md is **cross-sectional**: it asks "averaged over many orbits/states, does this statistic match the coin-flip prediction?" None of it looks at one anchor's own bit string as a standalone object.
- Bulk-vs-bottom split (aeh.md 13.1): small numbers are known-structured; the hypothesis only claims to hold in the bulk.
- External replication (aeh.md 13.4, measured grade): an independent implementation reproduces the class skeleton's exact values and the ledger.

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

### 17.7.1. Search executed: a clean pass

The plan in §17.8–17.9 was run in full, including the "if time remains" spectral item. Four independent implementations of the `M(ω)` generator were written (one per code file below, none imported from another, per AGENTS.md's fresh-code-per-claim rule) — each computes the 2-adic logarithm directly from its convergent series (stage1-synthesis.md, remark after Theorem 11.8.3.6.6: `9^N(ω) = ω⁻¹`, `M(ω) = N(ω²)`), and each was validated exactly against the 12-value worked-example table above before use. Every test's null model is stated precisely as in the brief: `M(ω)`'s bits modeled as i.i.d. fair-coin (independent, `P(bit=1)=1/2`).

**Single-sequence statistics** (`experiments/anchor_digit_structure.py`; 200 independent `ω`, uniform random in `[2²⁰, 2⁶⁴)`, odd, `3∤ω`, seed `20260712`, 4096 bits each):

- Monobit density `0.49999` (`z=-0.02`).
- Run-length distribution vs. `Geometric(1/2)`: pooled `chi2=12.93`, `df=13`, `p=0.45`; per-sequence meta-check (proportion-passing + p-value uniformity across the 200 sequences) clean.
- Autocorrelation, lags `1..64`: pooled `chi2=46.4`, `df=64`, `p=0.95`; no single lag exceeds the Bonferroni-corrected threshold (`max|z|=2.47` vs. `3.36`); meta-check clean.
- Overlapping `3/4/5`-bit window chi-squared: pooled `p ∈ [0.80, 0.94]`; the per-sequence *uniformity* meta-check fails for all three widths — diagnosed as an artifact of the test itself (overlapping windows share bits, so the naive `df=2^w-1` null is only approximate, flagged in the code's docstring *before* running) and **confirmed** by running the identical test on a matched true-random control: the control fails in exactly the same way. Not evidence about `M(ω)`.
- Cross-string correlate sweep (`ω mod 16`, `ω mod 32`, digit-sum parity of `ω`), extending the already-closed `ω mod 3` audit (archive/appendix-a.md A.4.6): significant (Bonferroni-corrected) at bits 0–24 — but this is the *already-proven* digit-determinacy law (stage4.md 11.8.7.2.1–3), not a discovery, since low-order `M(ω)` bits are a bounded, deterministic function of low-order `ω` bits by construction. **Not significant** at bits 2000–2024, the genuinely open region per the brief's own framing (S17.8 item 4) — no correlate found once past the proven bounded-reach law.

**Compressibility** (`experiments/anchor_compressibility.py`; independent sample, seed `20260713`, 200 `ω`, 4096 bits each; every comparison against a matched-length i.i.d.-fair-coin Monte Carlo control run through identical code, not a hand-derived asymptotic formula):

- Lempel–Ziv (1976) complexity (Kaspar–Schuster parsing, validated against the literature example `c('1001111011000010')=6`): mean `353.8` (`M(ω)`) vs. `354.1` (control), Mann–Whitney `p=0.46`.
- zlib compression ratio: `1.0215` vs. `1.0215`, `p=1.00`.
- NIST SP 800-22 battery via `nistrng` (standard package, not hand-rolled, per the brief's instruction): 11 tests eligible at `n=4096`. 7 clean outright; 4 (longest-run, non-overlapping-template, random-excursion, random-excursion-variant) show a meta-check artifact from `nistrng` reporting a *mean* of several internal p-values as its score (not itself uniform under the null by the CLT) — **confirmed** artifactual: the matched control fails the identical 4 tests the identical way, and `M(ω)` never fails a test the control passes. Two `nistrng` library quirks found and worked around (not silently patched): `MonobitTest` requires `0/1` input, not `±1` (uses `count_nonzero`); `cumulative_sums` overflows on `int8` input (widened to `int64`).

**Visualizations** (`experiments/anchor_visualize.py` → `viz/anchor_digit_visualizer.html`; 10 representative `ω` to 8192 bits — 6 "bottom" including the exact degeneracies `ω=1,3` and A.4.6's regular/irregular towers `ω=25,49,17,41`, 4 "bulk"): interactive recurrence plot (grayscale Hamming-distance heatmap) and chaos-game representation, the latter in both the brief's literal 2-corner spec (documented as provably confined to one line segment regardless of input — a property of the construction) and a standard 4-corner/2-bits-per-step CGR variant. Qualitative only, no p-values; confirms visually that the bottom/bulk distinction is real (the degenerate `ω=1,3` cases are visibly non-random) before looking at the bulk, per the brief's instruction.

**Spectral** (`experiments/anchor_spectral.py`, if-time item S17.8.3; independent sample, seed `20260714`, 200 `ω`, 4096 bits each): pooled periodogram of `M(ω)` vs. a matched i.i.d.-coin control, two-sample KS `D=0.00197`, `p=0.40` (409,400 ordinates each side); NIST-style per-sequence peak-count `d`-statistic, two-sample KS `D=0.05`, `p=0.96`.

**Conclusion.** Every planned test, in the genuinely open regime (past the already-proven bounded-reach digit-determinacy law and past the already-known bottom-regime algebraic degeneracies), is consistent with the fair-coin null. No autocorrelation, run-length bias, non-uniform window structure, compressibility gain, or spectral peak was found in a single `M(ω)`'s own bit string. This is a **clean pass**, recorded per the brief's explicit stop criterion — not a proof that AEH holds, not a claim that no structure could ever be found with a different test or at a different scale, and not itself a step toward proving the conjecture. It strengthens the calibration on a genuinely new axis (single-sequence, not cross-sectional) alongside aeh.md §13's existing cross-sectional calibration. Every artifact encountered during the search (the overlapping-window meta-check, the `nistrng` mean-of-p-values effect, two library bugs) was diagnosed by comparison against a matched control rather than either dismissed or over-interpreted, and is recorded here rather than smoothed over, per house norms.

**Verification (2026-07-12):** all four scripts (`anchor_digit_structure.py`, `anchor_compressibility.py`, `anchor_spectral.py`, plus the `anchor_visualize.py` generator) independently re-run; each generator revalidates 12/12 against the §17.7 worked-example table, and every statistic above reproduces exactly under its recorded seed. Clean pass confirmed.

### 17.7.2. Deep single-anchor probe: one `M(ω)` to `2^17` bits

§17.7.1 was **breadth** — 200 anchors × 4096 bits, shallow per anchor. But normality (every `k`-block equidistributing as length → ∞) is a *single-sequence, length → ∞* property, so its faithful probe is **depth on one anchor**, not breadth. This item reads a single bulk anchor 32× deeper. Fresh generator (`experiments/anchor_single_deep.py`, numpy-vectorized tests, imports nothing from other scripts; 2-adic-log series, validated 12/12 against the §17.7 table); every test is stated against the i.i.d. fair-coin null and run in parallel on a matched fair-coin control (seed `20260713`, `2^17 = 131072` bits per string).

**Bulk anchors `ω = 4996160569905494617` (primary) and `ω = 10041561047145933445` (replication):**

- Monobit density `0.49936` / `0.50047` (`|z| < 0.5`).
- Run-length vs `Geometric(1/2)`: `chi2=22.4, df=19, p=0.27` (primary). The second reads `p=0.026` — an isolated mild low, unreplicated on that anchor's other four tests and fully expected across the 4×5 = 20 tests run under the null (≈1 in 20 falls below 0.05); not structure. Longest run `14`/`21` vs `log2 N = 17` (control `22`).
- Window `#`-ones (`W=256`, 512 windows) vs `Binomial(256,1/2)`: `p=0.34`/`0.84`; mean/sd `127.8/8.09`, `128.1/8.35` vs the predicted `128/8`. This "bell curve" is the **weakest** test here (by the CLT almost any bit-sum looks Gaussian even under correlation) — reported for legibility, not discriminating power.
- Autocorrelation, lags `1..512`: `max|z| = 2.78`/`3.10` vs the Bonferroni bar `4.27` — clean, matching the control's `3.16`.
- Block-entropy `H_k/k`, `k=1..16`: `|H_k(M) − H_k(control)|` never exceeds `0.004` bits; the finite-sample droop past `k≈10` is identical to the control's.
- zlib ratio equal to the control to four places.

**Discrimination checked with negative controls** (so a clean bulk pass means the tests *can* fail, not that they are blind). The exact degeneracy `ω=3` (`M=−1`, all ones) is flagged by *every* test — density `1.0`, one run of length `2^17`, autocorr `z=362`, block entropy `0`, zlib ratio `420`. The one non-trivial wrinkle: the bottom anchor `ω=25` (A.4.6's "regular tower") shows a **mild global density deficit** — `z = −3.40` monobit, window `p=0.057` in the same direction — while its run-length, autocorrelation, and block-entropy are clean. `ω=25` is a *bottom* anchor, exactly where the bulk/bottom split (aeh.md 13.1) already expects small-number structure that says nothing about the bulk hypothesis; recorded as observed, not read as bulk evidence, and flagged as a candidate for a wider bottom-regime sweep if the bottom ever becomes the question. The two **bulk** anchors — the actual target — are clean on all five tests.

**Conclusion.** A **clean pass on the deep single-sequence axis for bulk anchors**, extending §17.7.1 by 32× in depth. It does not prove AEH (a measure-zero statement about integer orbits, §17.8 item 5), does not touch the proof-effort stopping rule, and leaves two higher-power follow-ups explicitly **un-run**: the TestU01/PractRand PRNG batteries (stronger statistical detectors than anything here) and an **automaticity / algebraicity screen** (Christol's theorem — is the bit sequence 2-automatic?), a *structural*, non-statistical notion of order that no test in §17.7 addresses. Visualization: `viz/anchor_single_deep_visualizer.html` (run-length vs geometric, the window bell curve, block-entropy scaling — all against the matched control).

**Independently verified 2026-07-13** (`experiments/anchor_single_deep_verify.py`, no import from the code under review): a second `M(ω)` implementation — the 2-adic-log series cross-checked against a *brute-force discrete-log search* (two disjoint algorithms, agreeing on 16 values mod `2^17`), validated 12/12 against the §17.7 table — reproduces the primary anchor's monobit density (`z=−0.464`) and run-length chi-square (`chi2=22.40, df=19, p=0.265`) exactly, and the `ω=25` deficit (`z=−3.397`).

### 17.7.3. Automaticity / algebraicity screen: `M(ω)` is not 2-automatic (2026-07-13)

Everything in §17.7.1–17.7.2 is **statistical** — does `M(ω)` look like a fair coin. There is a sharper, **structural** notion of order that no statistical test can see: is the bit sequence **2-automatic**, i.e. output by a finite automaton reading the base-2 digits of the index `n`? This matters because of a chain of classical theorems:

- **Christol's theorem** (Christol 1979; Christol–Kamae–Mendès France–Rauzy, *Bull. SMF* 108 (1980), 401–419): `(a_n)` over `F_2` is 2-automatic **iff** its generating function `F(x) = Σ a_n x^n` is **algebraic over `F_2(x)`**.
- **Eilenberg:** 2-automatic **iff** the 2-kernel `{(a_{2^e n + r}) : e≥0, 0≤r<2^e}` is **finite**.
- **Cobham:** an automatic sequence has **linear subword complexity** `p(k) = O(k)` (number of distinct length-`k` factors).

So "does `M(ω)`'s bit string hide algebraic structure over `F_2(x)`?" is a decidable-in-practice screen — and it is the exact structural meaning of §17.7.2's block-entropy observation `H_k ≈ k`.

**Method** (`experiments/anchor_automaticity.py`, fresh generator validated 12/12): two automaticity signatures — 2-kernel growth and subword complexity `p(k)` — each run on **three** sequences so the test's discriminating power is visible: **Thue–Morse** (the textbook 2-automatic sequence, positive control), a **fair coin** (non-automatic pole), and one bulk `M(ω)` to `2^17` bits.

**Result — the test works, and `M(ω)` fails to be automatic.** Thue–Morse's 2-kernel plateaus at exactly **2** distinct elements through depth 10 (of 2047 generated), and its subword complexity is flat (52 distinct factors at `k=18`) — the test correctly detects automaticity. `M(ω)` instead tracks the fair coin on both signatures:

- **2-kernel:** all **2047/2047** subsequences through depth 10 distinct (coin: 2047/2047; Thue–Morse: 2/2047). A ≥2047-element kernel means the minimal automaton, were there one, would need >2047 states.
- **Subword complexity:** `p(k) = 2^k` **fully saturated** for `k ≤ 12` (all 4096 length-12 factors present), matching the coin (Thue–Morse: 36). Exponential subword complexity is flatly incompatible with the linear `p(k)=O(k)` Cobham forces on any automatic sequence.

**Conclusion.** To the tested depth, `M(ω)`'s bit sequence is **not 2-automatic**, hence (Christol) its generating function is **not algebraic over `F_2(x)`**. This is the **first structural, non-statistical** order test in the §17.7 program, and it comes back negative — ruling out the entire automatic/algebraic family of hidden structure, not merely a correlation. It is the rigorous content of §17.7.2's `H_k ≈ k`: maximal subword complexity. A finite computation is not a proof, but the signature (saturated `2^k` complexity, all-distinct kernel, exact tracking of the coin against a *working* positive control) is unambiguous, and it is consistent with expectation — `M(ω)` is a 2-adic logarithm of an algebraic number, an object nothing suggested would be automaton-generated. Does not touch AEH or the proof-effort stopping rule.

**Independently verified 2026-07-13** (`experiments/anchor_automaticity_verify.py`, no import from the code under review): fresh generator validates 12/12; fresh plain-Python 2-kernel and subword-complexity counters flag Thue–Morse as automatic in both signatures (the linchpin control passes) and cross-check the §17.7.3 table bit-for-bit for the same `ω = 4996160569905494617`; a false-negative probe pushed kernel depth to 12 and subword `k` to 20 — `M(ω)` stays all-distinct (`8191/8191`) and keeps tracking the coin (`123117` vs `123327` at `k=20`, far above Thue–Morse's `60`), with the finite-`N` ceiling past `k=17` checked separately from the saturation signature. Confirmed, no discrepancy found.

### 17.7.4. Three operation lenses: linear complexity, Walsh spectrum, LIL walk

§17.7.1–17.7.3 asked *frequency* questions (does `M(ω)` look like a coin) and one *structural* question (is it automatic). This item applies three different **operations** to the bit string, each a distinct lens, prompted by two framing questions: *what rigorous definitions does "fair-coin noise" have*, and *what operations can be done on an infinite bit string*. The governing observation is the sharpest available: **`M(ω)` is computable** (the 2-adic-log series), so it is **not Martin-Löf random** — a computable sequence has `K(x_{1:n}) = O(log n)`, maximally compressible in the limit. What these lenses test is therefore **pseudo-randomness** — whether the finite description leaves a *detectable* fingerprint — not randomness, which is settled negatively a priori.

Method (`experiments/anchor_lenses.py`, fresh generator validated 12/12): one bulk `M(ω)` at `2^17` bits against a matched fair-coin control, plus two structured positive controls chosen to trip specific lenses — `ω=3` (`M=−1`, all ones) and Thue–Morse (its `±1` form is a single Walsh function).

- **Lens 1 — linear-complexity profile** (Berlekamp–Massey over `F_2`): `L_n` = shortest LFSR generating the first `n` bits. Fair-coin null: `L_n ≈ n/2`. This is the *rational*-generating-function subcase of the algebraicity ruled out in §17.7.3, but the profile is a finer quantitative statistic. **Result:** `M(ω)` `L_final = 16384 = n/2` exactly (mean deviation `+0.25`, the known BM bias; `8073` jumps) — identical to the coin. Positive control `ω=3` collapses to `L≡1`.
- **Lens 2 — Walsh–Hadamard spectrum**: the native harmonic analysis on `{0,1}^n`, sharper than the ordinary DFT (§17.7.1's spectral item). Normalized coefficients `w_k = W_k/√N ~ N(0,1)` under the null. **Result:** `M(ω)` `max|w_k| = 4.68`, coin `4.33`, both below the extreme-value scale `√(2 ln N) = 4.85` — flat. Positive control Thue–Morse spikes a *single* coefficient at `362 = √N` (off-axis entirely), proving the lens sees a Walsh-structured string.
- **Lens 3 — partial-sum / LIL walk**: `S_n = Σ(2a_k−1)`. Fair-coin null: stays within `±√(2n ln ln n)` and `S_N/√N ~ N(0,1)`. **Result:** `M(ω)` `max|S| = 541`, LIL ratio `1.085`, terminal `z = −0.46` — matches the coin. Positive control `ω=3` ramps linearly to `+131072` (drift, ratio `163`); Thue–Morse stays pinned at `|S|≤1` (bounded sums). **Honest scope note:** this is a randomness lens on the *digits*; it is **not** the cycle anchor-walk (spine.md 9.8.4: a cycle is a closed walk `Σ ΔM_t = 0` over orbit *increments*, different data). It is the same *operation* — partial summation — so it is background for that front, not a test of it.

**Conclusion.** A clean pass on all three lenses: `M(ω)` is indistinguishable from a fair coin on linear-complexity growth, Walsh flatness, and the LIL walk, while both positive controls trip the lenses they should. This confirms **pseudo-randomness on three new axes** and completes the picture from the randomness-definition hierarchy: `M(ω)` passes normality-style and pseudorandomness tests, is provably *not* Martin-Löf random (computable), and the one structural family (automatic/algebraic) was already excluded (§17.7.3). The obstruction is unchanged — it remains one specific computable 2-adic point, nice in `Z_2` arithmetic (where the proved laws live) and opaque in the measure-theoretic reading (where AEH lives). Does not touch AEH or the stopping rule. The stronger PRNG batteries (TestU01/PractRand, noted §17.7.2) remain the only un-run statistical tool. Visualization: `viz/anchor_lenses_visualizer.html`.

**Verified 2026-07-13:** a second Berlekamp–Massey implementation, validated on known LFSR test vectors (deg-4 `x^4+x+1` and deg-6 m-sequences → `L=4`/`6`), reproduces the linear-complexity result on `M(ω)` exactly (`L=1026` on 2048 bits); the FWHT matches a direct Hadamard-matrix multiply to zero error and yields the single Thue–Morse spike; the LIL walk is a cumulative sum.

### 17.7.5. PractRand to 1 GB on the concatenated-anchor stream: no anomalies

The one un-run statistical tool flagged in §17.7.2/§17.7.4 — a modern PRNG-killing battery, far stronger than the NIST SP 800-22 set — is now run. **PractRand 0.94** (`RNG_test`, core test set, standard 8-bit folding), built from source with the author-installed msys2 gcc 16.1.0 after the TestU01 autotools route was assessed and set aside (POSIX-header port burden; PractRand streams from stdin and compiles clean).

**Stream design (the author's choice of option (b), AEH-aligned).** Not one deep anchor but a **concatenation of many independent bulk anchors**: random `ω ∈ [2^40, 2^64)` (odd, `3∤ω`, seed `20260713`), each contributing bits `[64, 2048)` of `M(ω)` — the low 64 bits are dropped so the proven bounded-reach digit-determinacy law (stage4.md 11.8.7.2) is excluded and the battery sees only the genuinely-open bulk. AEH is a bulk/ensemble claim, so the family stream is the more relevant object, and it plays to the generator's fast-per-anchor regime (a single deep anchor is `O(D²)`-capped, cf. §17.7.2). Emitter: `experiments/anchor_bitstream.py`, fresh generator validated 12/12 against the §17.7 table, plus a byte-for-byte cross-check against §17.7.4's independent implementation on the first five ω of the actual stream; generation parallelized over 10 processes with order preserved (parallel output md5-identical to single-threaded).

**Pipe validated both ways before the run** (the controls that make a pass meaningful): an incrementing-counter stream **fails** immediately and catastrophically (18 distinct FAILs at 4 MB, p-values to `1e-6062`); an `os.urandom` stream **passes** (no anomalies in 76 tests at 8 MB). The battery detects structure and does not false-alarm on this pipe.

**Result.** `RNG_test stdin8 -tlmax 1GB`: **no anomalies in 135 test results at 1 GB** (2^30 bytes = 2^33 bits ≈ 4.3 million anchors' open-region digits; 1,939 s). Every interim cumulative report (128 MB, 256 MB, 512 MB) likewise clean. One transient `unusual` (DC6-9x1Bytes-1, `p = 1−1.7e-3`, the mildest flag PractRand issues) appeared at the 64 MB checkpoint and vanished from all later cumulative reports — the signature of a statistical fluctuation, not a bias (a real bias grows with sample size; PractRand's docs expect occasional `unusual`s on clean generators). Recorded, not smoothed over. Logging quirk recorded likewise: the emitter's stderr and the battery's stdout briefly shared a log file, mangling the earliest (2–32 MB) report blocks in the file; the verdict is unaffected because PractRand reports are cumulative and the 1 GB block covers the entire stream.

**Conclusion.** The anchor family's open-region digits are **indistinguishable from a fair coin by the strongest practical distinguisher battery available to us**, at three orders of magnitude more data than any previous test in §17.7. This is the strongest pseudo-randomness statement in the program's calibration record, and the natural endpoint of the §17.7 statistical program: normality-style tests (17.7.1–2), structural/algebraic exclusion (17.7.3), operation lenses (17.7.4), and now an industrial-strength distinguisher family (17.7.5) all agree, while Martin-Löf randomness remains excluded a priori (computability). It does not move AEH — the stream is an ensemble object, and AEH's difficulty is the specific arithmetic point — and does not touch the stopping rule. TestU01 (Alphabit/Rabbit on a captured file) remains possible now that a toolchain exists, but would be weaker than what PractRand just passed; noted as available, not queued.

## 17.8. Search plan (scoped 2026-07-12; executed — results in §17.7.1)

The plan below is retained as the record of what was scoped and why. Items 1–4 were executed (a clean pass, §17.7.1); item 5 (the reading task) is closed (verdict inline below). In order of cost and how surprising a positive finding would be:

1. **Single-sequence statistics.** Run-length distribution of `0`/`1` runs within one `M(ω)` against the geometric null; autocorrelation `R(k)` for lags `k = 1..~64`; chi-squared on overlapping 3–5-bit windows within one long string (aeh.md only ever checked bit pairs, cross-sectionally).
2. **Compressibility.** Lempel–Ziv complexity or a standard compressor against the raw bit string — the cleanest single number: incompressible-within-noise supports randomness, any real compression *is* a discovered structure by construction. The NIST SP 800-22 battery (frequency, block-frequency, runs, DFT, approximate entropy, serial, cumulative sums) exists exactly for this — run it, don't reinvent it.
3. **Spectral.** DFT of the bit sequence (mapped to `±1`); check flatness. The anchor is built from a discrete log mod `2^k` — not obviously periodic, but untested, so check rather than assume.
4. **Cross-string, but structurally new.** A.4.6 ruled out `ω mod 3`; sweep a few more cheap candidate correlates (`ω mod 16`, `ω mod 32`, digit sum of `ω`) the same way, and separately test the *residual* high-order digits of `ΔM` beyond what the proved low-order law (11.8.7.3.1) already accounts for, so the test targets the genuinely open part.
5. **Literature, not computation — read 2026-07-13; closed.** The Bernstein–Lagarias 2-adic shift conjugacy is **D. J. Bernstein & J. C. Lagarias, *The 3x+1 Conjugacy Map*, Canad. J. Math. 48 (1996), 1154–1169** (MSC 11B75): the conjugacy map `Φ: Z₂ → Z₂` with `Φ ∘ S ∘ Φ⁻¹ = T`, `S` the 2-adic shift. Its ergodicity/strong-mixing is proved in **J. C. Lagarias, *The 3x+1 problem and its generalizations*, Amer. Math. Monthly 92 (1985), 3–23** (ref [8] there). **Verdict on the item-5 question.** Its natural invariant measure is the **2-adic Haar measure** — exactly the fair-coin product measure that makes the binary digits i.i.d. `Bernoulli(1/2)` — and `Φ` (which preserves that measure, §1 eq. 1.3 remark) carries the shift's Bernoulli structure onto `T`, so "`T` is Bernoulli." So item 5's premise holds: the product law *is* the invariant measure (modulo the routine check that Haar, read in the block/anchor coordinates, equals aeh.md's `π_k`). But it is **not** a proof route to AEH: "`T` is Bernoulli" is genericity **Haar-almost-everywhere**, and the integer orbits AEH concerns are a **Haar-null** set (`Z ⊂ Z₂`), on which an a.e. statement says nothing. This is the Borel-normal-number obstruction the item anticipated, now concrete — the same measure-zero / specific-point wall as aeh.md 13.1's bulk/bottom split and bridge.md §16's core-extraction deficit. Closed: reference pinned, invariant measure identified, route diagnosed as obstructed (a.e.-genericity is free, the difficulty is entirely at the arithmetic points), not a lever. The paper's own headline results — `Φₙ` has order `2ⁿ⁻⁴` for `n ≥ 6`, its cycle/fixed-point counts, the `ax+b` and solenoidal-conjugacy generalizations — are permutation combinatorics of the truncated map and bear on none of this.

## 17.9. Visualization plan (scoped 2026-07-12; first tier built — `viz/anchor_digit_visualizer.html`, §17.7.1)

Two recommended first, cheap and complementary — one screens for self-similarity/periodicity, the other for general bias, and both are legible to the eye before any statistic is computed:

- **Recurrence plot ("fold it onto itself").** Compare length-`w` windows at every offset `i` against every offset `j`; darken `(i,j)` where they match closely. Random strings light up only the diagonal plus scattered noise; self-similarity or periodicity shows as off-diagonal stripes or blocks.
- **Chaos game representation.** Walk a point halfway toward one of two square corners per bit (corner `0` / corner `1`); plot every intermediate point. Standard bioinformatics technique for screening DNA for non-randomness. True randomness fills the square as uniform fog; bias or forbidden patterns show as visible gaps or genuinely fractal, self-similar structure in the fill.

Second tier, if the first pair turns up anything worth chasing:

- **Period-fold ("waterfall") plot.** Reshape the bit string into a `w`-column image, one row per `w` bits; sweep `w`. A real periodicity locks the image into stripes at the matching `w`; a wrong `w` looks like noise.
- **Delay embedding / return map.** Read non-overlapping `k`-bit windows as points in `[0,1)`; plot `(x_i, x_{i+1})`. Randomness scatters uniformly; hidden low-dimensional structure collapses the scatter onto a curve or sparse set — the natural visual companion to the ergodic/shift-conjugacy angle (17.8, item 5).

Deliverables should follow existing convention: interactive exploration in `viz/` (alongside `anchor_field_explorer.html`), raw analysis and any batteries in `experiments/`.

## 17.10. Standing

This page is a reference, and §17.7 also records five executed empirical programs — none a proof nor a step toward one, all clean against the fair-coin null: the breadth battery (§17.7.1), the 32×-deeper single-anchor probe (§17.7.2), the automaticity/algebraicity screen (§17.7.3 — `M(ω)` is not 2-automatic, hence by Christol not algebraic over `F_2(x)`), the three operation lenses (§17.7.4, under the governing framing that `M(ω)`, being computable, is not Martin-Löf random, so these test pseudo-randomness), and PractRand to 1 GB (§17.7.5). Each carries its own current verification line in its subsection. Together they strengthen the calibration on the single-sequence and structural axes, alongside aeh.md §13's cross-sectional calibration; they do not move AEH itself and do not touch the proof-effort stopping rule (README). The one out-of-scope follow-up — the Bernstein–Lagarias literature read (§17.8 item 5) — is closed: the conjugacy's natural invariant measure is the 2-adic Haar (fair-coin product) measure and `T` is Bernoulli, but only Haar-almost-everywhere, so on the measure-zero set of integer orbits it is the Borel-normality obstruction, not a proof route to AEH.
