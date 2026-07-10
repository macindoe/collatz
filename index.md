---
status: index
updated: 2026-07-12
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
| `stage1.md` | §11.8.1–11.8.4: valuation synthesis — mod-8 classification, anchor `N(ω)`, exact global law for `s`, Baker bounds, ledgers, status snapshot (11.8.4.5) | closed |
| `stage2.md` | §11.8.5: 3-gain law, orbit anchor `M(ω)`, unified depth-side law, fiber-versus-orbit gap (11.8.5.6) | closed / bridge OPEN |
| `stage3.md` | §11.8.6: decomposition of `C`, target-shift lemma, entry-depth law, per-step depth law | closed per step |
| `stage4.md` | §11.8.7: the odd core `ω_+` / anchor increment — low-order law (11.8.7.3.1), one-step propagation (11.8.7.6.1), digit budget (11.8.7.7) | live front |
| `publication.md` | Novelty assessment (claim-by-claim verdicts), pinned citations for all #TODOs, 2024–26 landscape, framing recommendation | sweep complete |
| `aeh.md` | §13: the Anchor Equidistribution Hypothesis — precise bulk formulation (13.2), conditional theorems (13.3), calibration record (13.4), anomaly resolved with routing lemma (13.5) | formalized; calibration clean |
| `ladder.md` | §15: the depth ladder — exact dichotomy relating (ω,d) and (ω,d+1): one Collatz step off-spike, an affine kick at spikes; the divergence question answered | closed as local law |
| `reverse.md` | §14: the reverse dynamics — predecessor characterization (14.1), 3-adic anchor + valuation law (14.2), duality (14.3), density program (14.4), dead ends (14.5), density bound (14.6), dual per-step theory (14.7–14.10), steering + one-identity synthesis (14.12) | active; papers' canonical proofs in paper 2 |
| `cycles.md` | §12: cycles in reduced coordinates — cycle equation (12.1), period 1 = Steiner (12.2), congruence system (12.3), m-cycle translation (12.4), period 2 (12.5), general-p elimination + ceiling lemma (12.6), period 3 + trim (12.7), uniform trim resolution (12.8) | periods 1–3 closed; front PARKED |
| `open-problems.md` | §11–11.7: the open-questions layer, with calibration notes | open / calibrated |
| `archive/appendix-a.md` | Appendix A: discovery path, worked examples, refuted claims with audit data | archive |
| `sources/` | Immutable: drafts v000–v078, PDFs, residue data | never edited |

## Section-number resolver

Monolith section numbers remain the citation anchors throughout (`11.8.6.3` etc.). To find one:

§1–9 → `spine.md` · §10 → this page (below) · §11.1–11.7 → `open-problems.md` · §11.8 intro/guardrail/Stage-1 prospectus → `program.md` · §11.8.1–11.8.4 → `stage1.md` · §11.8.5 → `stage2.md` · §11.8.6 → `stage3.md` · §11.8.7 → `stage4.md` · §11.8.8, §11.9 → `program.md` · §12 (post-monolith) → `cycles.md` · §13 (post-monolith) → `aeh.md` · §14 (post-monolith) → `reverse.md` · §15 (post-monolith) → `ladder.md` · Appendix A → `archive/appendix-a.md` · verification code → `experiments/`

## Current status (one paragraph)

The per-step arithmetic of the reduced transition is formal: the valuation `s` has an exact global law (stage1.md 11.8.4.1; unified form stage2.md 11.8.5.6.2), the 3-gain trigger is a theorem (stage2.md), the depth evolution `d_+ = m_+ + a_+` is closed on all residue classes (stage3.md 11.8.6.3.6), the anchor increment `ΔM` has an exact low-order law with `σ`-graded moduli (stage4.md 11.8.7.3.1), and one-step propagation decides the next `3`-gain from the window in an error-free trichotomy (stage4.md 11.8.7.6.1). The digit budget (stage4.md 11.8.7.7) splits the remaining content of the bridge: anchor equidistribution for typical orbits, rigidity of closed anchor walks for cycles. The cycle front (cycles.md §12) is closed out and parked: periods 1–3 completely classified (Steiner and Simons–de Weger contacts); the uniform-trim question resolved — a trim uniform in `p` exists and gives effective finiteness at every period (12.8.1–2), but the staircase family (12.8.3) proves its exponential weakening in `p` is intrinsic to size-counting, withdrawing the crossover plan (12.8.5). The residual content of cycle exclusion is anchor-walk rigidity — the same front as Stage 4 — and the staircase links the cycle and divergence halves of the difficulty (12.8.4). The mirror front (reverse.md §14) is active: the backward dynamics carry a 3-adic anchor and a full dual per-step theory, dead ends are classified, a rigorous density bound is proved (canonical proofs in paper 2), and the steering laws show the anchor walk — unsolved forward — is placeable in reverse, via the same identity as the forward valuation law read from the other end (14.12.3). Two papers: v1 published (DOI 10.5281/zenodo.21273548); the mirror paper finalized, awaiting its DOI. Full ledger: stage1.md 11.8.4.5. What Route A can and cannot deliver: stage1.md 11.8.4.4.

## Directory of empirical material (formerly §10)

The empirical layer has been progressively either formalized or relocated:

* Family-by-family tower analysis, halo geometry, and the discovery path of the primary-branch congruence picture: `archive/appendix-a.md` A.4–A.5; formal replacements in stage1.md 11.8.1 and 11.8.3.
* The refuted mod-3 tower-type conjecture, with the audit data that killed it: `archive/appendix-a.md` A.4.6.
* Empirical digit statistics of the anchors (fair-coin behavior, density 0.497): `archive/appendix-a.md` A.4.6, calibrated in stage1.md 11.8.4.2.
* Frequency and size ledgers — the `s`-distribution along real orbits, the 3-gain rate 1/3, drift accounting: stage1.md 11.8.4.4.
* Numerical confirmations of the convergence translation: spine.md §9.8.

What remains genuinely empirical is short: the anchor digit statistics and the orbit-level frequency ledger, both conjecturally pseudo-random, both attached to precise formal statements.
