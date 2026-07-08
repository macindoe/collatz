# Schema and Maintenance Workflows

This repository follows the LLM-wiki pattern: three layers with different mutation rules.

## Layers

1. **`sources/`** — immutable. Historical drafts (v000–v078), PDFs, residue data. Read for provenance; never edit, never delete. New monolith drafts are no longer created — the wiki pages are the live document.
2. **Wiki pages** (`index.md`, `spine.md`, `program.md`, `stage1.md`–`stage3.md`, `open-problems.md`, `archive/`) — evergreen. Each carries front matter (`status`, `scope`, `updated`) and a "Current state" paragraph. Pages are rewritten in place to carry the current best answer; history is git's job, not the page's.
3. **`experiments/`** — verification and pilot code. Each script states which page/result it supports. Scripts are kept runnable; results (counts, ranges, dates) are quoted in the owning page.
4. **`README.md`** — the human-facing map, including the program's strategy and stopping rules. Those rules are binding on agents too: check them before opening new computational fronts (in particular: no per-period cycle searches unless they serve the uniform trim lemma).
5. **This file** — the schema. Update it when the structure or workflows change.

## Conventions

- Monolith section numbers (`11.8.6.3`, `9.8.3`, …) are the stable citation anchors. Do not renumber them. The resolver in `index.md` maps numbers to pages.
- Every fact lives in exactly one page. Other pages point to it; they do not restate it. (The staleness that motivated this wiki came from duplicated status claims.)
- Math statements are edited conservatively: never "improve" a proof while doing organizational work. Separate commits for content vs. structure.

## Workflows

### When a result's status changes (proved / refuted / dissolved)

1. Update the owning page: front matter `status` + `updated`, the "Current state" paragraph, and the statement itself.
2. Update the compact ledger (stage1.md 11.8.4.5).
3. Sweep `open-problems.md` for entries that posed the question as open; add a calibration note pointing to the closure.
4. If stage-level, update `program.md` and the status summary in `index.md`.
5. Refuted claims are not deleted: move the claim + refutation evidence to `archive/`, leave a pointer.

### When adding a new result

- Proved structural material about the formalism itself → `spine.md`.
- Stage results → the owning stage page.
- New open questions → `open-problems.md`, phrased so that closure is checkable.

### Before marking anything "proved"

Run an independent numerical check (not the one quoted in the text — a fresh implementation), and record what was checked, the range, and the date in the page. Precedent: the v077 laws were re-verified with independent code over 8,000 random states and orbit traces, zero discrepancies (2026-07-06).

### Periodic status pass

Occasionally diff every page's claims about *other* pages against those pages' own front matter. Any mismatch is a bug. This is the wiki's replacement for the monolith-era problem of §11.1–11.6 rotting while §11.8 moved on.

## Verification record

- 2026-07-06 — wiki split from `sources/drafts/collatz_reduction_rewrite_v078.md`; concatenation of page bodies reproduces the monolith byte-identically.
- 2026-07-06 — independent numeric verification of: unified depth-side law (11.8.5.6.2), entry-depth law all six classes (11.8.6.3), orbit projection + fiber of (1,1) (9.8), 8,000 random states + orbit traces, zero failures.
- 2026-07-07 — low-order anchor-increment law (11.8.7.3.1, stage4.md): predictor-from-truncations test (4,046 checks) and lift-invariance test (10,092 pairs), k ∈ {1,3,6}, zero failures. Code: experiments/anchor_increment.py.
- 2026-07-07 — one-step propagation (11.8.7.6.1, stage4.md): window-only decision along real orbits, k ∈ {4,8}, 21,296 steps — 21,000 decided with zero errors, 296 undecided with zero violations of the deep-cascade bound s_+ >= k+2. Code: experiments/one_step_propagation.py.
- 2026-07-07 — period-1 cycle classification (12.2.3, cycles.md): exact big-integer window+divisibility search, m <= 20,000, unique solution = trivial fixed point; independent direct F-orbit cycle search (ω < 3,000, d <= 32) finds only {(1,1)}. Code: experiments/period1_cycles.py.
- 2026-07-07 — period-2 cycle classification (12.5.3, cycles.md): two-step elimination identity verified on 3,000 random orbit pairs (zero failures); pruned exact search n <= 20,000 — 19 open windows, 11 size-passing quadruples, no nontrivial solutions. First search run had an off-by-one in 3^n, caught by an s-split consistency check and corrected; recorded run passes sanity assertions. Code: experiments/period2_cycles.py.
- 2026-07-07 — general-p elimination (12.6.1) verified on random orbits p ∈ {3,4,5} + trivial-cycle identity R = 4^p − 3^p for p ∈ {1,2,3,4,7}; period-3 search (12.7.1): n <= 20,000, 76 treated n, 886 exact evaluations, 51 size-passers, no nontrivial solutions; prune audited on 4,798 cells (skipped region + box boundary), zero violations. Two filter-constant errors caught and corrected in-session (0.138→0.098; missing box branch); corrected run changed no outcomes. Code: experiments/period3_cycles.py.
- 2026-07-08 — period-3 trim lemma (12.7.4): γ > 0.1157n − 2 for any period-3 candidate; verified against all 51 exact size-passers in the search range, worst margin +3.1 bits; completes the period-3 classification (Theorem 12.7.5). Code: experiments/period3_cycles.py part D.
- 2026-07-08 — AEH formalization + calibration (aeh.md §13): bulk uniformity confirmed across all tested cells with per-orbit statistics (~1,600 orbits/cell, |z| < 1 after bulk/bottom separation); bottom-regime biases quantified (z up to 41, finite-structural); three apparent discoveries dissolved under controls and are recorded as methodology; ONE open anomaly — class (1 mod 8, d=1), bits 3–4 = 3 at 0.2677 vs 0.25, z = 5.0, n = 2,610 orbits, survives 2^40 cut, unpredicted by depth-5 chain. Code: experiments/aeh_calibration.py.
- 2026-07-08 — anomaly resolution (aeh.md 13.5): fixed-horizon unweighted sampling flat (0.2503 ± 0.0015, 84,739 pooled visits, flat at T = 1..32 and all clean altitude bands); deterministic routing lemma 13.5.1 verified exhaustively (26,673 states, zero exceptions); artifact mechanism identified (ratio-estimator bias through routing-coupled excursion lengths). Standing rule adopted: fixed-horizon, unweighted, per-visit sampling only. Code: experiments/aeh_anomaly.py.
- 2026-07-08 — uniform trim resolution (12.8): Theorem 12.8.1 proved (arc-weight/reset argument); staircase sharpness family exhibited — p=7, n=94, γ=6.74 passes all 7 rotation size tests where the p=3 constant demands 8.9, plus 84 passers at p=6; all fail divisibility; all respect the uniform bound (max ratio 0.23). Crossover plan withdrawn; cycle front parked per stopping rules. Code: experiments/uniform_trim.py.
