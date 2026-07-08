# Collatz, in reduced coordinates

This repository is a live research program on the Collatz conjecture, kept as a wiki rather than a paper. Every page carries its current status at the top; history lives in git; nothing empirical is ever passed off as proved. If you are an agent, read `AGENTS.md` for the maintenance rules. If you are a human — probably Ben — this page is the map.

## The idea, in plain language

The Collatz map wastes your attention on bookkeeping: long deterministic runs of halving and tripling that carry no information. This program compresses each such run into a single *block*, and each block into a small state `(ω, d)` — an odd core and a depth. The blocks chain into a new dynamical system, the reduced map `F`, and the compression is faithful: the conjecture is *exactly equivalent* to "every `F`-orbit reaches the state `(1,1)`," and hypothetical cycles correspond one-to-one (proved in `spine.md` §9.8). Nothing the conjecture depends on is lost. The bet is that in these coordinates, the arithmetic that matters becomes visible.

The bet has partially paid off. The per-step behavior of `F` — which used to look chaotic — is now *fully formal*: how long each block runs, when a factor of 3 appears, how the depth evolves, all follow exact laws governed by a single object: a 2-adic logarithm called the anchor, `M(ω)`. One step of the dynamics is now a theorem, not a mystery.

## What's proved (scoreboard)

In these coordinates, as of July 2026:

The exit valuation `s` obeys an exact global law (stage1.md, stage2.md). The 3-gain trigger is a theorem (stage2.md). The depth evolution is closed on every residue class (stage3.md). The anchor increment obeys an exact low-order law, and a finite "window" of digits decides the next step in an error-free trichotomy — it either answers exactly or correctly announces a rare deep event (stage4.md). Cycles of the reduced map with 1, 2, or 3 blocks do not exist, proved in-house, matching the classical results of Steiner and Simons–de Weger with far less apparatus (cycles.md).

## Where the difficulty actually lives

The program's most important result is negative, and we treat it as load-bearing (stage4.md §11.8.7.7): no bounded amount of digit information can decide an orbit's behavior forever, because each step *consumes* digits of the initial state and nothing regenerates them. So the remaining difficulty splits cleanly in two, and only two, places:

1. **Typical orbits** need a *statistical* fact: that the anchors of successive states equidistribute — the "fair-coin" behavior of 2-adic logarithm digits, empirically solid, theoretically untouched by anyone. This is a question about classical p-adic analysis, older and broader than Collatz.
2. **Cycles** need a *rigidity* fact: a closed orbit is a finite closed walk in anchor coordinates, and finite objects can be attacked with effective tools (Baker-type bounds) that genuinely beat unbounded depth.

Everything this program does is in service of making those two statements exact, and then attacking the second, because it is the only one where existing mathematics has traction.

## Strategy and stopping rules

This section exists because open-ended research programs die of drift. These rules are binding until deliberately revised.

**The cycle ladder is not the path.** Closing periods one at a time (p = 4, 5, 6, …) is an infinite-depth search; the literature spent decades on it without moving the conjecture. Our own guardrail (program.md) forbids indefinitely refined case-work that produces results without producing structure. Periods 1–3 were climbed for a specific purpose — validating the machinery and learning the shape of the general argument — and that purpose is **complete**.

**One objective remains on the cycle front:** the *uniform trim lemma* — a single theorem, for all periods `p` at once, of the form "any period-`p` cycle forces `2^K` exponentially close to `3^n`." The period-3 proof (cycles.md §12.7.4) has the right shape: its case analysis counts escape-configurations, not period-specific structure. If the uniform lemma lands, all cycle exclusion collapses to one bounded computation, and one crossover run past the current record (p > 91) is worth doing: a new result, a defined finish line. Then the ladder is retired regardless.

**Explicit stopping rules.** No per-period search runs unless it serves the uniform lemma. If the uniform lemma resists serious attempts, the cycle front is parked with its status recorded, not ground forward. The equidistribution question is treated as long-range: experiments may feed the ledger, but proof effort waits until there is an idea, because "grind harder" provably cannot work there.

**What this program does not claim:** a path to the conjecture. Its honest product is the conversion of folklore into exact statements — a faithful reformulation, exact per-step laws, a precise localization of the difficulty, and cycle results with unusually little machinery. Realistic wins from here: the uniform cycle theorem, a crossover record, and a publishable spine. The conjecture itself would additionally require the statistical half, which nobody on Earth currently knows how to prove.

## Map of the repository

| File | What it is |
|---|---|
| `index.md` | Wiki index: page table, section-number resolver, current status paragraph |
| `spine.md` | The formal core (§1–9): definitions, the reduced map, all foundational theorems, the equivalence with the conjecture |
| `program.md` | The Route A research program: guardrails, stage architecture, strategic summary |
| `stage1.md`–`stage4.md` | The four stages: valuation law → 3-gain → depth evolution → the anchor increment (live front) |
| `open-problems.md` | The open-questions layer, each entry calibrated against what's now proved |
| `cycles.md` | §12: cycles in reduced coordinates; periods 1–3 closed; the uniform trim lemma is the open objective |
| `archive/` | Discovery paths and refuted claims, kept with the evidence that killed them |
| `experiments/` | Runnable verification code for every computational claim in the wiki |
| `sources/` | Immutable history: drafts v000–v078, PDFs, data. Never edited |
| `AGENTS.md` | Maintenance schema: layers, workflows, verification records |

## House norms

Every "proved" claim has an independent numerical check recorded in `AGENTS.md`, run with fresh code rather than the code that suggested the result. Refuted conjectures are archived with their refutation data so they cannot quietly regenerate. Errors caught mid-work are documented in the record, not smoothed over — two search-filter bugs and one silent assumption are on file in cycles.md, found and fixed by the process working as intended. The section numbers (`11.8.6.3`, `12.7.4`, …) are permanent anchors; `index.md` resolves any number to its page.
