# Collatz, in reduced coordinates

**Papers:** (1) *Reduced coordinates for the Collatz map* — published preprint, DOI [10.5281/zenodo.21273548](https://doi.org/10.5281/zenodo.21273548) (July 2026). (2) *The 3-adic mirror of the reduced Collatz dynamics* — published preprint, DOI [10.5281/zenodo.21303918](https://doi.org/10.5281/zenodo.21303918) (July 2026), a companion continuing (1). Sources and PDFs in `paper/`. This repository is both papers' complete research record.

This repository is a live research program on the Collatz conjecture, kept as a wiki rather than a paper. Every page carries its current status at the top; history lives in git; nothing empirical is ever passed off as proved. If you are an agent, read `AGENTS.md` for the maintenance rules. If you are a human — probably Ben — this page is the map. If you are an external reader arriving from the papers or from correspondence, `TOUR.md` is your trailhead: paper-to-wiki mapping, how to run the verification, and what the status words mean.

## The idea, in plain language

The Collatz map wastes your attention on bookkeeping: long deterministic runs of halving and tripling that carry no information. This program compresses each such run into a single *block*, and each block into a small state `(ω, d)` — an odd core and a depth. The blocks chain into a new dynamical system, the reduced map `F`, and the compression is faithful: the conjecture is *exactly equivalent* to "every `F`-orbit reaches the state `(1,1)`," and hypothetical cycles correspond one-to-one (proved in `spine.md` §9.8). Nothing the conjecture depends on is lost. The bet is that in these coordinates, the arithmetic that matters becomes visible.

The bet has partially paid off. The per-step behavior of `F` — which used to look chaotic — is now *fully formal*: how long each block runs, when a factor of 3 appears, how the depth evolves, all follow exact laws governed by a single object: a 2-adic logarithm called the anchor, `M(ω)`. One step of the dynamics is now a theorem, not a mystery.

## What's proved (scoreboard)

In these coordinates, as of July 2026:

The exit valuation `s` obeys an exact global law (stage1.md, stage2.md). The 3-gain trigger is a theorem (stage2.md). The depth evolution is closed on every residue class (stage3.md). The anchor increment obeys an exact low-order law, and a finite "window" of digits decides the next step in an error-free trichotomy — it either answers exactly or correctly announces a rare deep event (stage4.md). Cycles of the reduced map with 1, 2, or 3 blocks do not exist, proved in-house, matching the classical results of Steiner and Simons–de Weger with far less apparatus; a uniform-in-`p` trim exists, and an explicit family shows counting arguments cannot do substantially better — sharp at the verified instances, assessed at every period (cycles.md).

## Where the difficulty actually lives

The program's most important negative statement is an organizing observation, and we treat it as load-bearing (stage4.md §11.8.7.7): each step provably *consumes* digits of the initial state and nothing regenerates them, which strongly suggests — as the organizing heuristic, not a formalized theorem — that no bounded amount of digit information can decide an orbit's behavior forever. So the remaining difficulty splits cleanly in two, and only two, places:

1. **Typical orbits** need a *statistical* fact: that the anchors of successive states equidistribute — the "fair-coin" behavior of 2-adic logarithm digits, empirically solid, theoretically untouched by anyone. This is a question about classical p-adic analysis, older and broader than Collatz.
2. **Cycles** need a *rigidity* fact: a closed orbit is a finite closed walk in anchor coordinates, and finite objects can be attacked with effective tools (Baker-type bounds) that genuinely beat unbounded depth.

Everything this program does is in service of making those two statements exact, and then attacking the second, because it is the only one where existing mathematics has traction.

## Strategy and stopping rules

This section exists because open-ended research programs die of drift. These rules are binding until deliberately revised.

**The cycle ladder is not the path.** Closing periods one at a time (p = 4, 5, 6, …) is an infinite-depth search; the literature spent decades on it without moving the conjecture. Our own guardrail (program.md) forbids indefinitely refined case-work that produces results without producing structure. Periods 1–3 were climbed for a specific purpose — validating the machinery and learning the shape of the general argument — and that purpose is **complete**.

**The uniform trim question is resolved — and the answer parked the front.** The uniform trim exists (cycles.md §12.8.1 — every period-`p` cycle forces `2^K` close to `3^n`), it gives effective finiteness at every period (§12.8.2), and its constant provably degrades like `1.585^(−p)` — with an explicit family of near-counterexamples (the *staircase*, §12.8.3) showing counting arguments cannot do substantially better. That refutes the crossover plan: the search bound at `p = 92` would be `n ~ 10^18`. Per the stopping rules below, the cycle ladder is retired and the front is parked. What the resolution bought: the residual content of cycle exclusion is now *precisely* the divisibility/anchor-rigidity conditions — the same front as Stage 4 — and the staircase itself (a divergent-orbit profile bent into a loop, §12.8.4) is concrete evidence that the cycle half and the divergence half of the conjecture's difficulty are one problem.

**Explicit stopping rules.** No per-period cycle search runs, period — the ladder is retired with the uniform question answered. The cycle front reopens only with a divisibility-aware (anchor-rigidity) idea, not more computation. The equidistribution question is treated as long-range: experiments may feed the ledger, but proof effort waits until there is an idea, because "grind harder" provably cannot work there.

**The third door: the mirror.** The entire forward machinery dualizes under the reduced map run backward (reverse.md, §14): predecessors are governed by a *3-adic* anchor — an affine logarithm base 2 — through a law that mirrors the forward 2-adic one with the roles of 2 and 3, and of `s` and `d`, exchanged. Backward reachability of everything from `(1,1)` is literally the conjecture, so no shortcut — but the backward tree is where the literature's rigorous *density* results live, and it has an exact local branching law it never had before. The front's defined target is the multi-type renewal equation; its defined temptation-to-refuse is exponent-grinding without it.

**The statistics door has an exact address.** The equidistribution hypothesis is formalized and calibrated (aeh.md, §13): in the *bulk* — while orbit values are large — every tested statistic matches the exact product law, and the folklore ledger is a theorem about that law; the wild deviations live entirely in the *bottom*, the fixed drainage basin of small numbers. A flagged 5σ anomaly is resolved (§13.5): a ratio-estimator artifact, aimed at exactly one cell by an exact routing lemma — the calibration's fourth dissolved discovery, and the reason fixed-horizon unweighted sampling is aeh.md's standing rule. Bulk uniformity stands unqualified at all tested depths. Conditional theorems record exactly what AEH buys (the ledger, the 1/3 rate, drift — almost-everywhere statements only) and what it cannot (individual staircase tails).

**What this program does not claim:** a path to the conjecture. Its honest product is the conversion of folklore into exact statements — a faithful reformulation, exact per-step laws, a precise localization of the difficulty, and cycle results with unusually little machinery. Realistic wins from here: the uniform cycle theorem, a crossover record, and a publishable spine. The conjecture itself would additionally require the statistical half, which nobody on Earth currently knows how to prove.

## Map of the repository

| File | What it is |
|---|---|
| `index.md` | Wiki index: page table, section-number resolver, current status paragraph |
| `spine.md` | The formal core (§1–9): definitions, the reduced map, all foundational theorems, the equivalence with the conjecture |
| `program.md` | The Route A research program: guardrails, stage architecture, strategic summary |
| `stage1.md`–`stage4.md` | The four stages: valuation law → 3-gain → depth evolution → the anchor increment (open residue owned by bridge.md §16) |
| `open-problems.md` | The open-questions layer, each entry calibrated against what's now proved |
| `cycles.md` | §12: cycles in reduced coordinates; periods 1–3 closed; the uniform trim lemma is the open objective |
| `archive/` | Discovery paths and refuted claims, kept with the evidence that killed them |
| `experiments/` | Runnable verification code for every computational claim in the wiki |
| `viz/` | Interactive visualizations — `block_family_decomposer.html`: any orbit unpacked into representative families, entries, and cascades (start here); `anchor_field_explorer.html`: the exit-valuation field over (ω, d) with click-to-trace orbits; `stratum_word_ticker.html`: the itinerary alphabet — read any orbit's stratum word letter by letter, or compose a word and watch its smallest witness grow at the modulus rate; `cycle_anchor_gateway.html`: the cycle-side gateway — the near-miss ladder, the anchored loops, the `k ≤ 10` verification strip (cycles.md 12.6.1.2); `anchor_digit_visualizer.html`, `anchor_single_deep_visualizer.html`, `anchor_lenses_visualizer.html`: the single-sequence digit-structure search's companion views (anchors.md §17.7) |
| `sources/` | Immutable history: drafts v000–v078, PDFs, data. Never edited |
| `AGENTS.md` | Maintenance schema: layers, workflows, verification records |

## Provenance

The framework originated as a hand-drawn note in Microsoft Paint, dated 13 March 2023, 1:49 AM — before this repository, before the drafts, before any AI collaboration (`sources/Collatz_conjecture_part1.png`, file timestamp 13 March 2023, 1:55 AM preserved in the copy). The scribble already contains, in embryo: the *seed* (the odd core, later `ω`) — "3x+1 only introduces factors of 3, all other prime factors are preserved"; the *block cascade* (later Layer 2) — "consecutive 3x+1÷2 operations continue until all factors of 2 are replaced with factors of 3"; the role of *base 9* — the iteration `9n−2 → 9(n/2)−1` with parity branching, which matured into the lifting congruence `9^n ≡ ω^(−1)` and the anchor `N(ω) = −log ω / log 9`; and the program's driving question, verbatim — "**Part Two: What does halving do to the Seed?**" — whose mature answer is the anchor increment law (stage4.md), and whose remaining depths are exactly what is still open. Everything since has been development of that page in collaboration with AI (2023–2026) — and the division is stated plainly: the coordinate system, the seed, the cascade, and the question are the human's; the anchors, the cycle machinery, the equidistribution formalization, and the proofs are the AI's construction on that foundation, under the human's direction and standards.

## House norms

Every "proved" claim has an independent numerical check recorded in `AGENTS.md`, run with fresh code rather than the code that suggested the result. Refuted conjectures are archived with their refutation data so they cannot quietly regenerate. Errors caught mid-work are documented in the record, not smoothed over — two search-filter bugs and one silent assumption are on file in the git history, found and fixed by the process working as intended. The section numbers (`11.8.6.3`, `12.7.4`, …) are permanent anchors; `index.md` resolves any number to its page.
