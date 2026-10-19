# Brief: independent check of cycles.md 12.8.7 (the staircase at threshold X₀) before it is offered to Merle as L-A12 — for a delegated session

**Why.** AGENTS.md: before anything is marked proved, an independent numerical check — a fresh implementation, not the one quoted in the text. 12.8.7's only check so far is `experiments/staircase_x0_threshold.py`, written by the session that wrote the proof; review re-ran it and re-derived 12.8.7.1(i) and (iv) by hand; its `Λ` constant was corrected 0.0541 → 0.054 on 2026-10-19. The round-19 PR to Merle (prepared, held) offers it as ledger entry L-A12.

**Read first:** `README.md` (stopping rules: size-only, no cycle search, no divisibility test), `AGENTS.md`, `cycles.md` 12.1, 12.8.1, 12.8.6 (Construction B, `12.8.6.1`–`12.8.6.2`), 12.8.7 in full. Do **not** read or import `experiments/staircase_x0_threshold.py` or its output until your own check is committed; then compare.

## Items

1. From 12.8.7's text alone, implement in exact arithmetic (integers / `fractions.Fraction`; `log₂3` by a rigorous enclosure): the size test (S) `q ≤ R_r` and (X) `(X₀+1)·q ≤ 2^{m_r} R_r` at every rotation; Construction B under (H1′); `p₁(X₀)`; `γ`, `ε_p n`, `x_min`, `Λ`.
2. Check each numbered claim of 12.8.7 on your own grid (record it): Prop 12.8.7.1 (i)–(iv) on random configurations including size-passers; Thm 12.8.7.2 (all entries ≥ 1, `Σ m_t = n`, crash depth ≥ 1, every rotation passes, the Rozier quantity `= m_0 ≤ γ − η`, (X) when `γ ≥ log₂(X₀+1) + 1`); Thm 12.8.7.4's availability and its bounds, including `Λ ≥ 0.054·2^{−ε_p n}`; the `p₁` table for at least `X₀ ∈ {16, 2^12, 2^20, 2^60, 5·2^60}`; Remark 12.8.7.5's unit-crash exclusion. Negative controls that must fail.
3. Then read the original script and output and reconcile every number they share with yours; any discrepancy is a finding, diagnosed, not smoothed.
4. Re-derive by hand the proof of Thm 12.8.7.2 (the step review did not re-derive) and say whether each step holds as written.

## Rules and deliverables

Nothing outward; if a command is denied, stop and report. Edit/Write only; encoding scan before the last commit; foreground until committed; one documented command reproduces the committed output. Do not edit `cycles.md` — findings only. Branch `x0-threshold-independent-check` from current `main` (`git merge --ff-only main` first if behind; record the base SHA). Deliverables: `experiments/x0_threshold_independent_check.py` + output, `briefs/x0-threshold-independent-check-findings.md` (grid, per-claim verdict, reconciliation, the hand re-derivation, and a one-line verdict: ripe to offer as L-A12 / not, with reasons).
