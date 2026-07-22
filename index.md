---
status: index
updated: 2026-07-23
---

# Collatz Reduction — Wiki Index

New here? `README.md` is the plain-language map and carries the program's strategy and stopping rules.

A reduced structural formalism for the Collatz map: deterministic valuation blocks are factored out, and the induced dynamics are studied on reduced states `(ω, d)`. The reduced system is a faithful arena for the conjecture itself — the convergence translation (spine.md §9.8) proves the exact equivalence.

This repository is a wiki, not a versioned monolith. Each page carries its current status at the top; history lives in git. The last monolith draft is preserved at `sources/drafts/collatz_reduction_rewrite_v078.md`, and every page below was split from it with byte-identical content (verified 2026-07-06).

## Pages

| Page | Contents | Status |
|---|---|---|
| `spine.md` | §1–9: formalism, block determinism, the reduced map `F`, proved structural properties, convergence translation | proved |
| `program.md` | §11.8 intro, guardrail, stage architecture, 11.8.7–11.8.8, 11.9: the Route A program and strategy | program |
| `stage1.md` | §11.8.1–11.8.2, 11.8.4: valuation synthesis entry + summary — mod-8 classification, lifting-branch congruences, pre-synthesis tower map, ledgers, status snapshot (11.8.4.5) | closed |
| `stage1-synthesis.md` | §11.8.3: the Stage 1 synthesis proper — primary branch, halo law, boundary shell, the 2-adic anchor `N(ω)`, exact global law for `s`, imported `p`-adic Baker bounds (11.8.3.11) | closed |
| `stage2.md` | §11.8.5: 3-gain law, orbit anchor `M(ω)`, unified depth-side law, fiber-versus-orbit gap (11.8.5.6) | closed / bridge OPEN |
| `stage3.md` | §11.8.6: decomposition of `C`, target-shift lemma, entry-depth law, per-step depth law | closed per step |
| `stage4.md` | §11.8.7: the odd core `ω_+` / anchor increment — low-order law (11.8.7.3.1), one-step propagation (11.8.7.6.1), digit budget (11.8.7.7) | per-step results proved; open residue → bridge.md §16 |
| `publication.md` | Novelty assessment (claim-by-claim verdicts), pinned citations for all #TODOs, 2024–26 landscape, framing recommendation | sweep complete |
| `aeh.md` | §13: the Anchor Equidistribution Hypothesis — precise bulk formulation (13.2), conditional theorems (13.3), calibration record (13.4), anomaly resolved with routing lemma (13.5) | formalized; calibration clean |
| `ladder.md` | §15: the depth ladder — exact dichotomy relating (ω,d) and (ω,d+1): one Collatz step off-spike, an affine kick at spikes; the divergence question answered | closed as local law |
| `bridge.md` | §16: the terminal open object — the anchor increment at unbounded depth; the core-extraction deficit (two-sided digit budget) as its observed mechanism; consolidates 11.8.5.6 / 11.8.7.7 / 14.13 | OPEN (consolidation) |
| `anchors.md` | §17.1–17.6: consolidated reference for the anchor across the wiki (pointers only) | REFERENCE |
| `anchor-digit-search.md` | §17.7–17.10: the single-sequence digit-structure search program, executed clean on two statistical axes — breadth (17.7.1) and a 32×-deeper single-anchor probe (17.7.2) — plus a structural automaticity screen (17.7.3, M(ω) not 2-automatic), three operation lenses (17.7.4), and PractRand to 1 GB (17.7.5), all clean; plans (17.8–17.9) and standing (17.10) | executed search (clean; not 2-automatic) |
| `reverse.md` | §14.1–14.14: the reverse dynamics — predecessor characterization (14.1), 3-adic anchor + valuation law (14.2), duality (14.3), density program (14.4), dead ends (14.5), density bound (14.6, multi-door lift 14.6.5), dual per-step theory (14.7–14.10), steering + one-identity synthesis (14.12), KL–LP obstruction (14.13), the door/exit seam (14.14, block-map corollary layer 14.14.7–14.14.8) | active; papers' canonical proofs in paper 2 |
| `itinerary.md` | §14.15: the itinerary language — the finite-itinerary cylinder theorem, the full-shift calibration, the formulation-grade two-sided coding, the unique-predecessor/bicylinder/positive-realization-height block 14.15.4, the converse-of-the-trivial-direction block 14.15.5 — admissibility-class lemma, the combined three-way characterization, the `-5` negative-diagonal reconciliation — and the signed-diagonal block 14.15.6, restating 14.15.3–14.15.5 over the nonzero odd integers: sign-blind throughout apart from `-1`'s one-sided forward mortality, the per-sector realization height's transfer checked and found to hold, and the known negative cycles (`{-5,-7}`, the period-7 cycle as the `G`-period-2 word `((4,1),(3,3))`, `y*=-17`) now ordinary diagonal points rather than boundary exceptions — and the exact height laws 14.15.7, closing the integer-fixed-point periodic instances: the two published escape tables upgraded to laws (`4·72^n−5`, `2·12^n−1`) plus the period-7 word's (`4·(2^11·3^7)^n−17`), all at the CRT-modulus rate with the fixed point as offset — and the non-integral mechanism 14.15.8, closing the rest of the single-letter shelf: both sectors escape at the modulus rate with a purely periodic, denominator-bounded unit-orbit constant — and 14.15.9, classifying whole-period realization heights exactly for every fixed periodic word: both sectors, one unified law, conditional on whether the word's fixed-point denominator `q` is `1` | active (split from reverse.md); open front: periodic cycle exclusion (q = 1 beyond the known instances) |
| `cycles.md` | §12: cycles in reduced coordinates — cycle equation (12.1), period 1 = Steiner (12.2), congruence system (12.3), m-cycle translation (12.4), period 2 (12.5), general-p elimination + ceiling lemma (12.6), period 3 + trim (12.7), uniform trim resolution (12.8), staircase sharpness recipe at floor grade (12.8.6) | periods 1–3 closed; front PARKED |
| `open-problems.md` | §11–11.7: the open-questions layer, with calibration notes; §11.8: citation/constant debt (discharged); §11.9 (post-monolith): per-letter window height laws | open / calibrated |
| `archive/appendix-a.md` | Appendix A: discovery path, worked examples, refuted claims with audit data | archive |
| `sources/` | Immutable: drafts v000–v078, PDFs, residue data | never edited |

## Section-number resolver

Monolith section numbers remain the citation anchors throughout (`11.8.6.3` etc.). To find one:

§1–9 → `spine.md` · §10 → this page (below) · §11.1–11.7 → `open-problems.md` · §11.8 intro/guardrail/Stage-1 prospectus → `program.md` · §11.8.1–11.8.2 → `stage1.md` · §11.8.3 → `stage1-synthesis.md` · §11.8.4 → `stage1.md` · §11.8.5 → `stage2.md` · §11.8.6 → `stage3.md` · §11.8.7 → `stage4.md` · §11.8.8 → `program.md` · §11.9 (monolith: Closing Perspective) → `program.md` · §11.9 (post-monolith: per-letter window height laws) → `open-problems.md` · §12 (post-monolith) → `cycles.md` · §13 (post-monolith) → `aeh.md` · §14.1–14.14 (post-monolith) → `reverse.md` · §14.15 → `itinerary.md` · §15 (post-monolith) → `ladder.md` · §16 (post-monolith) → `bridge.md` · §17.1–17.6 (post-monolith) → `anchors.md` · §17.7–17.10 → `anchor-digit-search.md` · Appendix A → `archive/appendix-a.md` · verification code → `experiments/`

## Current status (one paragraph)

The per-step arithmetic of the reduced transition is fully formal — the valuation law, the 3-gain trigger, the depth evolution, and the anchor increment (spine.md §9.8; stage1.md–stage4.md; full ledger stage1.md 11.8.4.5, scope stage1.md 11.8.4.4) — and the digit budget (stage4.md 11.8.7.7) splits what remains into two halves: anchor equidistribution for typical orbits, anchor-walk rigidity for cycles. The cycle front (cycles.md §12) is closed and parked: periods 1–3 classified, the uniform trim resolved with its exponential weakening shown intrinsic to size-counting (12.8.1–12.8.5), and the all-`p` staircase sharpness held at floor grade — verified instances for the full contiguous range `p ∈ {2,...,23}` (12.8.6), the Diophantine coverage bound its sole remaining gap. AEH (aeh.md §13) is formalized and calibrated clean at bulk uniformity, with the single-sequence structural axis (anchor-digit-search.md §17.7) now at its endpoint; proof effort stays parked per the stopping rules. The mirror front (reverse.md §14) is active: the door/exit seam (14.14) relocates the core-extraction deficit onto the forward digit budget rather than dissolving it. The itinerary language (itinerary.md §14.15) then closes finite-level structure by proof — the itinerary language is a full shift — and completes a formulation-grade two-sided coding into a three-way diagonal characterization, extended sign-blind over the nonzero odd integers (14.15.6), with exact height laws closing the integer-fixed-point periodic instances (14.15.7), the non-integral mechanism closing the rest of the single-letter shelf (14.15.8), and whole-period realization heights now classified exactly for every periodic word (14.15.9) — height growth itself contributes no further obstruction once a word's fixed-point denominator is known, leaving periodic cycle exclusion (ruling out `q = 1` beyond the known instances) as the open front; the Bridge's status is unchanged throughout this arc. The program's terminal open object is the bridge (bridge.md §16): the anchor increment at unbounded depth, forward and reverse, with the core-extraction deficit as its observed mechanism. Both papers are published — paper 1 (DOI 10.5281/zenodo.21273548) and the mirror paper (DOI 10.5281/zenodo.21303918) — with paper 1's v2 uploaded (DOI 10.5281/zenodo.21421120, publication.md). The anchor concept itself has one consolidated reference (anchors.md §17.1–17.6), with the single-sequence digit-structure search program at anchor-digit-search.md (§17.7.1–17.7.5): breadth and depth batteries, a structural (non-automaticity) screen, further operation lenses, and a PractRand pass, all clean against the fair-coin null.

## Directory of empirical material (formerly §10)

The empirical layer has been progressively either formalized or relocated:

* Family-by-family tower analysis, halo geometry, and the discovery path of the primary-branch congruence picture: `archive/appendix-a.md` A.4–A.5; formal replacements in stage1.md 11.8.1 and stage1-synthesis.md 11.8.3.
* The refuted mod-3 tower-type conjecture, with the audit data that killed it: `archive/appendix-a.md` A.4.6.
* Empirical digit statistics of the anchors (fair-coin behavior, density 0.497): `archive/appendix-a.md` A.4.6, calibrated in stage1.md 11.8.4.2.
* Frequency and size ledgers — the `s`-distribution along real orbits, the 3-gain rate 1/3, drift accounting: stage1.md 11.8.4.4.
* Numerical confirmations of the convergence translation: spine.md §9.8.

What remains genuinely empirical is short: the anchor digit statistics and the orbit-level frequency ledger, both conjecturally pseudo-random, both attached to precise formal statements.
