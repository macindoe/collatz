---
status: hypothesis FORMALIZED and calibrated — bulk uniformity confirmed broadly; ONE flagged anomaly (13.5, open); proof effort remains parked per stopping rules
scope: new section 13 (post-monolith)
updated: 2026-07-08
source: new material; builds on 11.8.4.4 (ledger), 11.8.7.6–7 (window/digit budget), 12.8.4 (staircase)
---

> **Current state.** The Anchor Equidistribution Hypothesis is now a precise statement (13.2) instead of a vibe: along orbits, *while values remain large*, the window states equidistribute under the exact product law — ω-digits Haar-uniform given the class, depths following the stationary law of the exact window chain. Calibration (13.4): confirmed in the bulk across every tested cell — marginals, pairs, digit conditionals — once the *bottom regime* (the fixed drainage basin of small integers, with enormous but finite-structural biases) is separated out. Conditional consequences are exact (13.3): AEH implies the frequency ledger with explicit error bounds, the 3-gain rate 1/3, and the drift picture. One anomaly stands (13.5): class `(1 mod 8, d = 1)` shows a persistent ~1.8% digit bias at `z = 5.0` that survives a `2^40` bulk cut and is NOT predicted by finite-depth chains. Open and falsifiable.

# 13. The Anchor Equidistribution Hypothesis

The statistics door of the program (README; `11.8.7.7`). The digit-budget theorem shows bounded windows cannot decide infinite horizons; what typical-orbit control *needs* is a statistical hypothesis about the anchor digits. This section makes that hypothesis exact, derives its consequences as conditional theorems, and calibrates it empirically. Proof effort remains parked per the stopping rules: the underlying question — digit statistics of `2`-adic logarithms — is beyond current theory. The deliverable here is precision, not proof.

## 13.1. Two regimes, one lesson

Orbit statistics mix two different objects. The **bulk** — visits while `x` is large — behaves measure-like. The **bottom** — the fixed, finite drainage basin of small integers every convergent orbit funnels through — has wildly non-uniform statistics (e.g., `P(ω ≡ 1 mod 32 | class (1, 2))` is `0.499` there vs `0.25` uniform) because those are the digits of *specific small numbers*, not samples from a measure. Whole-orbit averages conflate the two: the apparent violations of fair-coin behavior found first in calibration (`13.4`, runs E4b/E6) dissolved almost entirely when the regimes were separated (E7). Any precise equidistribution statement must therefore be a *bulk* statement. The historic ledger (`11.8.4.4`) should be read the same way.

## 13.2. The hypothesis

Fix a depth `k`. The **depth-`k` window state** of `(ω, d)` is `(ω mod 2^(k+2), min(d, D_k))` together with validity data; by `11.8.7.6.1` it decides the next step's `s` and `3`-gain in an error-free trichotomy with undecided rate `~2^-(k+1)`. Let `π_k` denote the **exact product law**: ω-residues Haar-uniform among valid ones, depth distributed by the stationary law of the exact window chain (computed at depth `12`: `P(d = 1, 2, 3, …) ≈ 0.333, 0.302, 0.173, 0.093, 0.048, …`, matching orbits to `~1%`).

**Hypothesis 13.2.1 (AEH, bulk form).** For every `k` and every `X`, along the `F`-orbit of almost every state (in natural density of starting values), the empirical distribution of depth-`k` window states over the visits with `x_exit > X` converges to `π_k` as the orbit length and `X` grow.

Supporting exact facts (unconditional): under `π_k`, the marginal of `s` is exactly the ledger — `P(s = 1) = 1/2`, `P(s = 2) = 1/4`, `P(s = j) = 2^-j` — by the residue-class count (`11.8.1.3.1`) plus the geometric shell law on the lifting classes; `3`-gain has probability exactly `Σ_(j even) 2^-j = 1/3` (`9.3`); and `a_+ = 0` exactly when `s` is odd, so shallow blocks never absorb `3`s. The class process under `π_k` is an explicit finite Markov chain with computable entries (e.g., from class `(1 mod 8, d odd)` the next depth is exactly `1`; from `(5 mod 8, d odd)`, `P(d_+ even) = 2/3` exactly).

## 13.3. Conditional consequences (theorems modulo AEH)

**13.3.1 (ledger).** AEH at depth `k` implies the frequency ledger with explicit error `O(2^-k)`: the one-step trichotomy converts window frequencies into `s`-frequencies exactly, except on the undecided set of `π_k`-measure `~2^-(k+1)`. Letting `k → ∞`: the ledger holds exactly along bulk orbit segments.

**13.3.2 (3-gain and drift).** AEH implies the `3`-gain rate is exactly `1/3` (measured along orbits: `0.3352`, `1.1σ` from `1/3`) and the classical negative drift per block, hence contraction of `log x` at the classical rate along AEH-generic orbit segments.

**13.3.3 (what AEH does not give).** Even in full, AEH yields almost-everywhere statements only. The exceptional tails — sustained deviations of exactly the staircase profile (`12.8.4`) — have AEH-probability zero yet are not excluded for any *individual* orbit. AEH is the precise form of the missing statistical half; it is not a route to full convergence. This matches the program's honest scope (`11.8.4.4`, README).

## 13.4. Calibration record (2026-07-08)

Eight experiment rounds, `experiments/aeh_calibration.py`. Statistics use per-orbit means with across-orbit standard errors (orbits independent; within-orbit pooling would overstate significance). Findings:

* **Bulk uniformity confirmed** (cut `ω > 2^24`, ~1,600 orbits/cell): digit conditionals flat — `P(bits 3–4 | class (1,2)) = 0.2533` vs `0.25` (`0.8σ`); `(7,1)` cell `0.5017` vs `0.5` (`0.4σ`); consecutive-pair cell `(s, s') = (4,3)` at `0.1277` vs independent prediction `0.128` (`-0.1σ`). The `s`-marginals, `d`-law, and class-transition structure all match the exact chain.
* **Bottom regime quantified**: the same cells at `ω <= 2^24` show deviations up to `z = 41` — finite structure, not measure. Methodological caution recorded: three successive apparent "discoveries" during calibration (an `s = 3` marginal excess, orbit pair correlations, digit biases) each dissolved under better controls (larger starts, per-orbit statistics, bulk/bottom separation). The controls are now standard for this page.
* **The exact chains work**: the `(class, d)`-chain reproduces the orbit `d`-law to `~1%` and the naive `2^-k` ledger emerges from pure counting — the ledger is a *theorem about* `π_k`, and the empirical question is only whether orbits follow `π_k`.

## 13.5. Open anomaly: the `(1 mod 8, d = 1)` cell

One cell refuses to clear. Along bulk visits to class `(ω ≡ 1 mod 8, d = 1)`, the digit pair `bits 3–4 of ω` takes the value `3` (i.e., `ω ≡ 25 mod 32`) with frequency `0.2677` vs the uniform `0.25` — `z = 5.0` over `2,610` independent orbits, surviving a bulk cut of `2^40`, while the depth-5 window chain predicts flatness (`0.246–0.253`). Candidate explanations, none yet tested: Markov structure deeper than `(mod 32, d <= 12)` that finite-depth chains erase; a visit-weighting/selection effect coupling digits to local drift; or a genuine deviation of the orbit-invariant law from every finite-depth product — which would refine AEH itself. Follow-up design: transfer-operator computation at depth `(mod 128, d <= 20)` with exact kernels from the window laws; multiple independent seeds; return-time-weighted statistics. This is the page's live falsifiable target. **Status: open.**
