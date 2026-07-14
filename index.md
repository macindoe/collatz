---
status: index
updated: 2026-07-14
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
| `stage4.md` | §11.8.7: the odd core `ω_+` / anchor increment — low-order law (11.8.7.3.1), one-step propagation (11.8.7.6.1), digit budget (11.8.7.7) | live front |
| `publication.md` | Novelty assessment (claim-by-claim verdicts), pinned citations for all #TODOs, 2024–26 landscape, framing recommendation | sweep complete |
| `aeh.md` | §13: the Anchor Equidistribution Hypothesis — precise bulk formulation (13.2), conditional theorems (13.3), calibration record (13.4), anomaly resolved with routing lemma (13.5) | formalized; calibration clean |
| `ladder.md` | §15: the depth ladder — exact dichotomy relating (ω,d) and (ω,d+1): one Collatz step off-spike, an affine kick at spikes; the divergence question answered | closed as local law |
| `bridge.md` | §16: the terminal open object — the anchor increment at unbounded depth; the core-extraction deficit (two-sided digit budget) as its observed mechanism; consolidates 11.8.5.6 / 11.8.7.7 / 14.13 | OPEN (consolidation) |
| `anchors.md` | §17: consolidated reference for the anchor across the wiki (pointers only, 17.1–17.6); single-sequence digit-structure search program (17.7–17.9), executed clean on two statistical axes — breadth (17.7.1) and a 32×-deeper single-anchor probe (17.7.2) — plus a structural automaticity screen (17.7.3, M(ω) not 2-automatic), three operation lenses (17.7.4), and PractRand to 1 GB (17.7.5), all clean | REFERENCE + executed search (clean; not 2-automatic) |
| `reverse.md` | §14: the reverse dynamics — predecessor characterization (14.1), 3-adic anchor + valuation law (14.2), duality (14.3), density program (14.4), dead ends (14.5), density bound (14.6, multi-door lift 14.6.5), dual per-step theory (14.7–14.10), steering + one-identity synthesis (14.12), KL–LP obstruction (14.13), the door/exit seam (14.14) | active; papers' canonical proofs in paper 2 |
| `cycles.md` | §12: cycles in reduced coordinates — cycle equation (12.1), period 1 = Steiner (12.2), congruence system (12.3), m-cycle translation (12.4), period 2 (12.5), general-p elimination + ceiling lemma (12.6), period 3 + trim (12.7), uniform trim resolution (12.8) | periods 1–3 closed; front PARKED |
| `open-problems.md` | §11–11.7: the open-questions layer, with calibration notes; §11.8: citation/constant debt (discharged) | open / calibrated |
| `archive/appendix-a.md` | Appendix A: discovery path, worked examples, refuted claims with audit data | archive |
| `sources/` | Immutable: drafts v000–v078, PDFs, residue data | never edited |

## Section-number resolver

Monolith section numbers remain the citation anchors throughout (`11.8.6.3` etc.). To find one:

§1–9 → `spine.md` · §10 → this page (below) · §11.1–11.7 → `open-problems.md` · §11.8 intro/guardrail/Stage-1 prospectus → `program.md` · §11.8.1–11.8.2 → `stage1.md` · §11.8.3 → `stage1-synthesis.md` · §11.8.4 → `stage1.md` · §11.8.5 → `stage2.md` · §11.8.6 → `stage3.md` · §11.8.7 → `stage4.md` · §11.8.8, §11.9 → `program.md` · §12 (post-monolith) → `cycles.md` · §13 (post-monolith) → `aeh.md` · §14 (post-monolith) → `reverse.md` · §15 (post-monolith) → `ladder.md` · §16 (post-monolith) → `bridge.md` · §17 (post-monolith) → `anchors.md` · Appendix A → `archive/appendix-a.md` · verification code → `experiments/`

## Current status (one paragraph)

The per-step arithmetic of the reduced transition is formal: the valuation `s` has an exact global law (stage1.md 11.8.4.1; unified form stage2.md 11.8.5.6.2), the 3-gain trigger is a theorem (stage2.md), the depth evolution `d_+ = m_+ + a_+` is closed on all residue classes (stage3.md 11.8.6.3.6), the anchor increment `ΔM` has an exact low-order law with `σ`-graded moduli (stage4.md 11.8.7.3.1), and one-step propagation decides the next `3`-gain from the window in an error-free trichotomy (stage4.md 11.8.7.6.1). The digit budget (stage4.md 11.8.7.7) splits the remaining content of the bridge: anchor equidistribution for typical orbits, rigidity of closed anchor walks for cycles. The cycle front (cycles.md §12) is closed out and parked: periods 1–3 completely classified (Steiner and Simons–de Weger contacts); the uniform-trim question resolved — a trim uniform in `p` exists and gives effective finiteness at every period (12.8.1–2), but the staircase family (12.8.3) proves its exponential weakening in `p` is intrinsic to size-counting, withdrawing the crossover plan (12.8.5). The residual content of cycle exclusion is anchor-walk rigidity — the same front as Stage 4 — and the staircase links the cycle and divergence halves of the difficulty (12.8.4). The mirror front (reverse.md §14) is active: the backward dynamics carry a 3-adic anchor and a full dual per-step theory, dead ends are classified, a rigorous density bound is proved (canonical proofs in paper 2), and the steering laws show the anchor walk — unsolved forward — is placeable in reverse, via the same identity as the forward valuation law read from the other end (14.12.3). The program's terminal open object is now consolidated as the bridge (bridge.md §16): the anchor increment at unbounded depth, forward and reverse, with the core-extraction deficit recorded as its observed mechanism — each step strips a prime power to extract a core and thereby spends anchor precision (σ digits forward, d reverse, ≥1 always), which is why no bounded method closes it in either direction. The bridge now also has a working formulation, the door/exit seam (reverse.md 14.14): `ΔM` is one fixed operation's mismatch across the live door shared by both directions (14.14.2), and the reduced map, conjugated to door coordinates (14.14.3), carries a total, constant-offset graded `3`-adic law (14.14.5) — with the reconciliation (14.14.6) showing the deficit is relocated onto the forward `(s, m_+)` digit data exactly, not dissolved. Two papers, both published: paper 1 (DOI 10.5281/zenodo.21273548) and the mirror paper (DOI 10.5281/zenodo.21303918), linked via a Continues relation. Full ledger: stage1.md 11.8.4.5. What Route A can and cannot deliver: stage1.md 11.8.4.4. The anchor concept itself, scattered across eight pages, now has one consolidated reference (anchors.md §17), which also ran a new experimental program: whether a *single* anchor's digit string has internal structure (autocorrelation, compressibility, self-similarity) — orthogonal to the cross-sectional statistics aeh.md already ran, and explicitly permitted under the stopping rules as an experiment rather than proof effort. Executed 2026-07-12 on branch `anchor-digits` (delegated per `briefs/anchor-digit-search-brief.md`): a clean pass across every planned test (anchors.md §17.7.1), strengthening the calibration on this new axis without moving AEH itself or the proof-effort stopping rule. A companion deep probe (§17.7.2, 2026-07-13) then read a *single* bulk anchor 32× deeper (`2^17` bits) — the axis normality actually lives on — and likewise came back a clean pass against matched fair-coin controls, with `ω=3`/`ω=25` as working negative controls. A third, structural screen (§17.7.3) then showed `M(ω)`'s bit sequence is not 2-automatic — hence (Christol) its generating function is not algebraic over `F_2(x)` — ruling out the automatic/algebraic family of hidden order; three further operation lenses (§17.7.4 — linear complexity, Walsh spectrum, LIL walk) are likewise clean, and PractRand — an industrial PRNG-killing battery — reports no anomalies in 135 tests at 1 GB on a concatenated stream of ~4.3 million bulk anchors' open-region digits (§17.7.5), three orders of magnitude more data than any prior test. The governing frame: `M(ω)` is computable, hence not Martin-Löf random, so these test pseudo-randomness, which it passes at every scale tried, on one specific 2-adic point where the measure-theoretic (AEH) question stays out of reach. §17.7.2/§17.7.3 were reproduced by delegated sessions; §17.7.4/§17.7.5 verified inline.

## Directory of empirical material (formerly §10)

The empirical layer has been progressively either formalized or relocated:

* Family-by-family tower analysis, halo geometry, and the discovery path of the primary-branch congruence picture: `archive/appendix-a.md` A.4–A.5; formal replacements in stage1.md 11.8.1 and stage1-synthesis.md 11.8.3.
* The refuted mod-3 tower-type conjecture, with the audit data that killed it: `archive/appendix-a.md` A.4.6.
* Empirical digit statistics of the anchors (fair-coin behavior, density 0.497): `archive/appendix-a.md` A.4.6, calibrated in stage1.md 11.8.4.2.
* Frequency and size ledgers — the `s`-distribution along real orbits, the 3-gain rate 1/3, drift accounting: stage1.md 11.8.4.4.
* Numerical confirmations of the convergence translation: spine.md §9.8.

What remains genuinely empirical is short: the anchor digit statistics and the orbit-level frequency ledger, both conjecturally pseudo-random, both attached to precise formal statements.
