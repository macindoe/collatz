---
status: novelty sweep COMPLETE (2026-07-09); verdicts per claim below; framing recommendation at end
scope: publication planning; citation pins for the wiki's #TODOs
updated: 2026-07-09
---

> **Current state.** Claim-by-claim novelty assessment done against the classical literature and the 2024–26 landscape. Headline: the program's *statistical* layer has classical shadows and contemporary company; the *exact-law* layer (anchor coordinates, global valuation law, window trichotomy, digit budget) appears distinctive as a framework; the *cycle* layer's results are subsumed but its sharpness dichotomy (uniform trim capped at `1.585^(-p)`, staircase witness) is the strongest candidate for a genuinely new theorem. Parallel human–LLM Collatz work now exists on arXiv — both a caution and a precedent.

# Novelty Assessment and Publication Plan

## Pinned citations (resolving the wiki's #TODOs)

* Steiner circuits: R. P. Steiner, *A theorem on the Syracuse problem*, Proc. 7th Manitoba Conf. (1977). (12.2.3)
* m-cycles: J. Simons, B. de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, Acta Arith. (2005), m <= 68/76; **current record**: C. Hercher, *There are no Collatz-m-Cycles with m <= 91*, [arXiv:2201.00406](https://arxiv.org/abs/2201.00406) (2022/23). Our crossover threshold "p > 91" was correctly calibrated. (12.4, 12.5.3, 12.7.3)
* Verification frontier: D. Barina, *Improved verification limit for the convergence of the Collatz conjecture*, [J. Supercomputing (2025)](https://link.springer.com/article/10.1007/s11227-025-07337-0): all n < 2^71 converge. (12.6.3)
* Cycle-length lower bounds via linear forms: S. Eliahou (1993), length >= 17,087,915; Baker–Wüstholz machinery. (12.1.2)
* Linear independence measures for logs of rationals (the `log_2 3` measure): G. Rhin, and Q. Wu / Salikhov-line improvements — [AMS Math. Comp. survey point](https://www.ams.org/journals/mcom/2003-72-242/S0025-5718-02-01442-4/S0025-5718-02-01442-4.pdf). Exact constant to be chosen at writeup; every use in 12.5.3/12.7.5/12.8.2 survives any published measure. 
* p-adic Baker: K. Yu, *Linear forms in p-adic logarithms*; Y. Bugeaud, M. Laurent, J. Number Theory 61 (1996). (11.8.3.11)

## The 2024–26 landscape (three neighbors)

1. **[arXiv:2603.11066](https://arxiv.org/abs/2603.11066), *Exploring Collatz Dynamics with Human–LLM Collaboration* (March 2026).** Burst–gap decomposition (≈ our blocks), geometric valuation/gap laws (≈ our ledger under `π_k`), an Orbit Equidistribution Conjecture (≈ AEH), explicitly exploratory and conditional. **No anchors, no 2-adic logarithms, no exact global laws, essentially no cycle content.** Overlap is real at the heuristic layer; our exact-law core is untouched. Also a precedent: arXiv accepts documented human–LLM mathematical exploration.
2. **A machine-verified conditional theory of Collatz (2025/26, Lean-formalized)** and the [Collatz formalization community](https://ccchallenge.org/): Diophantine skeleton with 1- and 2-cycle exclusion and reduction of cycle exclusion to effective `|2^S - 3^n|` gap bounds. This is our §12.1–12.5 spine in different coordinates. Our periods 1–2 should be presented as *rederivations in the reduced frame*, full stop.
3. **Classical foundations** (must be cited as the bedrock): Terras (1976) — parity-vector equidistribution, the ancestor of every "fair-coin" statement including AEH; Everett; Lagarias's surveys and annotated bibliographies; Wirsching; the 2-adic conjugacy of the Collatz map to the shift (Lagarias; Bernstein–Lagarias) — the deep reason bulk uniformity "wants" to be true, and prior art for §13's product law. A bachelor thesis (Rackl 2021) already applies 2-adic methods to Collatz cycles; must be checked in detail at writeup.

## Verdicts, claim by claim

* **Reduced blocks / states `(ω, d)`** — *new packaging of known material.* Block-like decompositions exist (burst–gap; parity vectors; jump functions). The specific `(odd core, depth)` state with its induced self-map and the 9.8 equivalence: not found in this exact form, but claim only "a convenient new coordinate system," not a new object.
* **The anchor `N(ω) = -log ω / log 9` in `Z_2` and the exact global law `s = 2 + v_2(d - M(ω))`** — *strongest framework claim.* LTE-type special cases are classical; 2-adic logs appear in cycle analyses; but the use of the anchor as a global dynamical coordinate, with the unified law on all classes, the target-shift lemma, entry-depth law, and the increment identity, was not found anywhere. This is the paper's core.
* **Window trichotomy + digit budget (11.8.7.6–7)** — *likely new as theorems*, though the digit budget's moral content ("finite information cannot decide infinite horizons") echoes the known 2-adic shift conjugacy. Frame as: the conjugacy made quantitative and per-step exact.
* **Cycles, periods 1–3** — *subsumed* (Steiner; Simons–de Weger; Hercher; and now Lean formalizations). Value: brevity of the reduced-frame derivations. Never claim priority.
* **Ceiling lemma (12.6.2)** — cute, elementary; possibly folklore; claim softly.
* **Uniform trim + staircase sharpness (12.8)** — *best candidate for a genuinely new result.* An explicit theorem that size-counting cycle exclusion is capped at exponential-in-`p`, with a constructive sharpness family, was not found in the literature. The staircase-divergence link (12.8.4) is a novel observation worth featuring.
* **AEH (§13)** — *a precise restatement of classical heuristics* (Terras; Haar-genericity), sharpened by: the exact product law `π_k` with computable chain, the bulk/bottom decomposition, the calibration methodology (four dissolved discoveries, the routing lemma 13.5.1). Frame as "the folklore hypothesis, made exact and calibrated," citing Terras and 2603.11066 prominently.

## Provenance (novelty-relevant)

The framework's origin is documented and predates all three contemporary neighbors: a hand-drawn note of 13 March 2023 (`sources/origin_scribble_2023-03-13.png`, transcribed in README) already contains the seed/odd-core concept, the block cascade, the base-9 structure, and the Stage-4 question. Independent origination, three years before arXiv:2603.11066, with a complete draft history (sources/drafts v000–v078) and verification records. For a methodology-documenting paper this provenance chain is itself an asset.

## Framing recommendation

One paper, honest title in the direction of *"Reduced coordinates for the Collatz map: exact per-step laws, anchor dynamics, and the limits of counting arguments for cycles."* Lead with the anchor machinery (the genuinely distinctive core), feature the uniform-trim/staircase dichotomy as the main new theorem, present cycles 1–3 as clean rederivations, and position AEH as formalized folklore with a calibration record. Document the human–LLM methodology openly (2603.11066 is the precedent; our AGENTS.md/verification-record discipline is arguably itself a contribution). Venue: arXiv first (math.NT + math.DS), then Experimental Mathematics or Integers, whose scope fits the verified-computation style. Pre-submission checklist: read Rackl 2021 and the Lean conditional-theory paper in full; sweep Lagarias's bibliographies for anchor-like coordinates; choose and state one concrete irrationality measure; convert spine + stages + §12 + §13 to LaTeX.
