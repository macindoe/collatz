---
status: index
updated: 2026-07-07
---

# Collatz Reduction — Wiki Index

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
| `cycles.md` | §12: cycles in reduced coordinates — cycle equation (12.1), period 1 = Steiner (12.2), congruence system (12.3), m-cycle translation (12.4), period 2 (12.5), general-p elimination + ceiling lemma (12.6), period 3 + trim lemma (12.7) | periods 1–3 closed |
| `open-problems.md` | §11–11.7: the open-questions layer, with calibration notes | open / calibrated |
| `archive/appendix-a.md` | Appendix A: discovery path, worked examples, refuted claims with audit data | archive |
| `sources/` | Immutable: drafts v000–v078, PDFs, residue data | never edited |

## Section-number resolver

Monolith section numbers remain the citation anchors throughout (`11.8.6.3` etc.). To find one:

§1–9 → `spine.md` · §10 → this page (below) · §11.1–11.7 → `open-problems.md` · §11.8 intro/guardrail/Stage-1 prospectus → `program.md` · §11.8.1–11.8.4 → `stage1.md` · §11.8.5 → `stage2.md` · §11.8.6 → `stage3.md` · §11.8.7 → `stage4.md` · §11.8.8, §11.9 → `program.md` · §12 (post-monolith) → `cycles.md` · Appendix A → `archive/appendix-a.md` · verification code → `experiments/`

## Current status (one paragraph)

The per-step arithmetic of the reduced transition is formal: the valuation `s` has an exact global law (stage1.md 11.8.4.1; unified form stage2.md 11.8.5.6.2), the 3-gain trigger is a theorem (stage2.md), the depth evolution `d_+ = m_+ + a_+` is closed on all residue classes (stage3.md 11.8.6.3.6), the anchor increment `ΔM` has an exact low-order law with `σ`-graded moduli (stage4.md 11.8.7.3.1), and one-step propagation decides the next `3`-gain from the window in an error-free trichotomy (stage4.md 11.8.7.6.1). The digit budget (stage4.md 11.8.7.7) splits the remaining content of the bridge: anchor equidistribution for typical orbits, rigidity of closed anchor walks for cycles. The cycle front (cycles.md §12): periods 1, 2, and 3 are completely classified — no nontrivial cycles — via the general-`p` elimination, the ceiling lemma, and per-period budget-trim lemmas (`K − n·log_2 3 < 2^(−0.115n+3)` at `p = 3`), with Steiner and Simons–de Weger as external contacts. Scaling is mild. Next: the uniform-in-`p` trim lemma, then `p = 4, 5, …` toward the crossover target `p > 91`, beyond the current `m`-cycle record. Full ledger: stage1.md 11.8.4.5. What Route A can and cannot deliver: stage1.md 11.8.4.4.

## Directory of empirical material (formerly §10)

The empirical layer has been progressively either formalized or relocated:

* Family-by-family tower analysis, halo geometry, and the discovery path of the primary-branch congruence picture: `archive/appendix-a.md` A.4–A.5; formal replacements in stage1.md 11.8.1 and 11.8.3.
* The refuted mod-3 tower-type conjecture, with the audit data that killed it: `archive/appendix-a.md` A.4.6.
* Empirical digit statistics of the anchors (fair-coin behavior, density 0.497): `archive/appendix-a.md` A.4.6, calibrated in stage1.md 11.8.4.2.
* Frequency and size ledgers — the `s`-distribution along real orbits, the 3-gain rate 1/3, drift accounting: stage1.md 11.8.4.4.
* Numerical confirmations of the convergence translation: spine.md §9.8.

What remains genuinely empirical is short: the anchor digit statistics and the orbit-level frequency ledger, both conjecturally pseudo-random, both attached to precise formal statements.
