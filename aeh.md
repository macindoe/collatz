---
status: hypothesis FORMALIZED and calibrated — bulk uniformity confirmed UNQUALIFIED at all tested depths; the 13.5 anomaly RESOLVED as a protocol artifact (with an exact routing lemma); proof effort remains parked per stopping rules
scope: new section 13 (post-monolith)
updated: 2026-07-22
source: new material; builds on 11.8.4.4 (ledger), 11.8.7.6–7 (window/digit budget), 12.8.4 (staircase)
---

> **Current state.** The Anchor Equidistribution Hypothesis is now a precise statement (13.2) instead of a vibe: along orbits, *while values remain large*, the window states equidistribute under the exact product law — ω-digits Haar-uniform given the class, depths following the stationary law of the exact window chain. Calibration (13.4): confirmed in the bulk across every tested cell — marginals, pairs, digit conditionals — once the *bottom regime* (the fixed drainage basin of small integers, with enormous but finite-structural biases) is separated out. Conditional consequences are exact (13.3): AEH implies the frequency ledger with explicit error bounds, the 3-gain rate 1/3, and the drift picture. The one flagged anomaly is resolved (13.5): fixed-horizon unweighted sampling shows the cell is exactly flat; the apparent bias was a ratio-estimator artifact aimed at one cell by the deterministic routing lemma 13.5.1 — the fourth and most instructive dissolved discovery of the calibration campaign. Bulk uniformity stands unqualified.

# 13. The Anchor Equidistribution Hypothesis

The statistics door of the program (README; `11.8.7.7`). The digit-budget theorem shows bounded windows cannot decide infinite horizons; what typical-orbit control *needs* is a statistical hypothesis about the anchor digits. This section makes that hypothesis exact, derives its consequences as conditional theorems, and calibrates it empirically. Proof effort remains parked per the stopping rules: the underlying question — digit statistics of `2`-adic logarithms — is beyond current theory. The deliverable here is precision, not proof.

## 13.1. Two regimes, one lesson

Orbit statistics mix two different objects. The **bulk** — visits while `x` is large — behaves measure-like. The **bottom** — the fixed, finite drainage basin of small integers every convergent orbit funnels through — has wildly non-uniform statistics (e.g., `P(ω ≡ 1 mod 32 | class (1, 2))` is `0.499` there vs `0.25` uniform) because those are the digits of *specific small numbers*, not samples from a measure. Whole-orbit averages conflate the two: the apparent violations of fair-coin behavior found first in calibration (`13.4`, runs E4b/E6) dissolved almost entirely when the regimes were separated (E7). Any precise equidistribution statement must therefore be a *bulk* statement. The historic ledger (`11.8.4.4`) should be read the same way.

## 13.2. The hypothesis

Fix a depth `k`. The **depth-`k` window state** of `(ω, d)` is `(ω mod 2^(k+2), min(d, D_k))` together with validity data; by `11.8.7.6.1` it decides the next step's `s` and `3`-gain in an error-free trichotomy with undecided rate `~2^-(k+1)`. Let `π_k` denote the **exact product law**: ω-residues Haar-uniform among valid ones, depth distributed by the stationary law of the exact window chain (computed at depth `12`: `P(d = 1, 2, 3, …) ≈ 0.333, 0.302, 0.173, 0.093, 0.048, …`, matching orbits to `~1%`).

**Hypothesis 13.2.1 (AEH, bulk form).** For every `k` and every `X`, along the `F`-orbit of almost every state (in natural density of starting values), the empirical distribution of depth-`k` window states over the visits with `x_exit > X` converges to `π_k` as the orbit length and `X` grow.

Supporting exact facts (unconditional): under `π_k`, the marginal of `s` is exactly the ledger — `P(s = 1) = 1/2`, `P(s = 2) = 1/4`, `P(s = j) = 2^-j` — by the residue-class count (`11.8.1.3.1`) plus the geometric shell law on the lifting classes; `3`-gain has probability exactly `Σ_(j even) 2^-j = 1/3` (`9.3`); and `a_+ = 0` exactly when `s` is odd, so shallow blocks never absorb `3`s. The class process under `π_k` is an explicit finite Markov chain with computable entries (e.g., from class `(1 mod 8, d odd)` the next depth is exactly `1`; from `(5 mod 8, d odd)`, `P(d_+ even) = 2/3` exactly). A symbolic form of the hypothesis is recorded at reverse.md `14.15.2`: AEH is precisely the statement that actual orbits' stratum words equidistribute against the itinerary cylinder measure.

## 13.3. Conditional consequences (theorems modulo AEH)

**13.3.1 (ledger).** AEH at depth `k` implies the frequency ledger with explicit error `O(2^-k)`: the one-step trichotomy converts window frequencies into `s`-frequencies exactly, except on the undecided set of `π_k`-measure `~2^-(k+1)`. Letting `k → ∞`: the ledger holds exactly along bulk orbit segments.

**13.3.2 (3-gain and drift).** AEH implies the `3`-gain rate is exactly `1/3` (measured along orbits: `0.3352`, `1.1σ` from `1/3`) and the classical negative drift per block, hence contraction of `log x` at the classical rate along AEH-generic orbit segments.

**13.3.3 (what AEH does not give).** Even in full, AEH yields almost-everywhere statements only. The exceptional tails — sustained deviations of exactly the staircase profile (`12.8.4`) — have AEH-probability zero yet are not excluded for any *individual* orbit. AEH is the precise form of the missing statistical half; it is not a route to full convergence. This matches the program's honest scope (`11.8.4.4`, README). The staircase is simultaneously the cycle-sharpness family; the one-configuration-both-halves synthesis is charted at bridge.md `16.4.6`.

## 13.4. Calibration record (2026-07-08)

Eight experiment rounds, `experiments/aeh_calibration.py`. Statistics use per-orbit means with across-orbit standard errors (orbits independent; within-orbit pooling would overstate significance). Findings:

* **Bulk uniformity confirmed** (cut `ω > 2^24`, ~1,600 orbits/cell): digit conditionals flat — `P(bits 3–4 | class (1,2)) = 0.2533` vs `0.25` (`0.8σ`); `(7,1)` cell `0.5017` vs `0.5` (`0.4σ`); consecutive-pair cell `(s, s') = (4,3)` at `0.1277` vs independent prediction `0.128` (`-0.1σ`). The `s`-marginals, `d`-law, and class-transition structure all match the exact chain.
* **Bottom regime quantified**: the same cells at `ω <= 2^24` show deviations up to `z = 41` — finite structure, not measure. Methodological caution recorded: three successive apparent "discoveries" during calibration (an `s = 3` marginal excess, orbit pair correlations, digit biases) each dissolved under better controls (larger starts, per-orbit statistics, bulk/bottom separation). The controls are now standard for this page.
* **The exact chains work**: the `(class, d)`-chain reproduces the orbit `d`-law to `~1%` and the naive `2^-k` ledger emerges from pure counting — the ledger is a *theorem about* `π_k`, and the empirical question is only whether orbits follow `π_k`.
* **External replication (measured grade, 2026-07-18):** an independent implementation by Eric Merle (3,000 orbits, cuts 2^20 and 2^30) reproduces the class skeleton's two exact values and the `2^{−j}` ledger, and measures the 8-class transfer-matrix spectrum at `|λ₂| ≤ 0.06` (our re-run: `0.028/0.036` at the two cuts — `experiments/merle_aeh_key_check.py`); his flagged drift artifact (`−0.33/−0.36` vs `−0.415`) is confirmed to be survivorship bias from the cut protocol: under this page's fixed-horizon standing rule the drift is `−0.4166 ± 0.0037` per odd step (`log₂3 − 2 = −0.4150`) and `−0.8367 ± 0.0060` per block (`2(log₂3 − 2) = −0.8301`). Spectral numbers are measurements, not theorems; the generic-face scope of 13.3.3 is unchanged.

## 13.5. The `(1 mod 8, d = 1)` anomaly: resolved (protocol artifact), with an exact lemma as consolation

One cell initially refused to clear: bulk visits to class `(ω ≡ 1 mod 8, d = 1)` appeared to prefer `ω ≡ 25 (mod 32)` at `0.2677` vs `0.25` — `z = 5.0` over `2,610` independent orbits, surviving a `2^40` cut, unpredicted by the depth-5 chain. The follow-up (2026-07-08, `experiments/aeh_anomaly.py`) resolved it.

**The decisive test.** Fixed-horizon, unweighted sampling — uniform large starts, exactly `T` steps, no stopping rule, per-visit pooling — shows the cell is *flat*: `P(ω ≡ 25 mod 32 | class) = 0.2503 ± 0.0015` pooled over `84,739` visits, flat at every horizon `T = 1..32` and in every clean altitude band of a `150`-step run. The invariant law is uniform here. The anomaly lived in the measurement protocol, not the dynamics.

**Lemma 13.5.1 (deterministic routing from class `(1,1)`).** For `ω ≡ 1 (mod 8)`, `d = 1`, the residue `ω mod 32` exactly determines the next class: `1 → (1,1)` (immediate self-return), `9 → (7,1)`, `17 → (5,1)`, `25 → (3,1)` — the last being the lifting class. **Proof.** `s = 1` and `C = 3ω + 1`, so `v_2(C) = 2` and `ω_+ = (3ω+1)/4`, whose residue mod `24` is a fixed function of `ω mod 32`; `a_+ = 0` since `C ≡ 1 (mod 3)`. Verified exhaustively on `26,673` sampled states, zero exceptions. ∎

**The artifact mechanism.** The earlier estimator took per-orbit *ratios* over each orbit's qualifying visits, with early stopping. By Lemma `13.5.1`, residue `1` self-loops (creating runs of consecutive visits), while residue `25` routes into the deep-descent lifting class. Orbits drawing more `25`s therefore descend faster and accumulate *fewer* qualifying visits, so each `25` carries a larger per-orbit weight — a textbook ratio-estimator bias, aimed at exactly one residue of exactly one class by exact arithmetic. This also explains the cell-specificity: `(1,1)` is the unique class with a deterministic self-loop channel. The absorption tail of long runs (orbits reaching the fixed point and tallying `ω = 1` forever) produces the complementary distortion.

**Standing rule (added to the calibration methodology).** Statistics on this page use fixed-horizon, unweighted, per-visit sampling from uniform starts. Ratio estimators over correlated visit sequences are forbidden — this cell is the reason.

**Status: resolved.** This was the fourth and final apparent discovery of the calibration campaign, and the most instructive: the "anomaly" was the exact transition structure of the reduced map reflected back through a biased estimator. Bulk uniformity now stands **unqualified** at all tested depths and cells.
