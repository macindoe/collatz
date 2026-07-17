# Brief: empirical probe — height growth on periodic words with non-integral fixed point (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — this brief operates under an explicit, recorded author exception, see Provenance), `AGENTS.md` (binding house norms), `reverse.md` §14.14.8 (composed affine maps, fixed point `y* = β/(1−α)`), §14.15.1.4–.5 (forward cylinder class, an iff), §14.15.4 (window/height definitions), §14.15.5(a) (backward admissibility class, an iff), §14.15.5(c) and §14.15.6 (the signed apparatus, per-sector heights, the two published escape tables).

## Provenance and authorization

A frontier seed handed forward from the previous session framed height growth's **lower bound** as the rigidity statement — the same species as the collaboration thread's "R mod q far from 0." The main session's 2026-07-17 pre-check showed that on the two published instances (integer fixed point) both bounds are trivially exact (see `briefs/height-exact-laws-brief.md`, running separately — do **not** coordinate with that branch or read it). The nearest genuinely unexplored family is periodic words whose fixed point is a **non-integral rational**. Systematic `H` statistics sit behind a standing stop line (14.15.4(d), 14.15.6(e)); the author explicitly authorized this bounded probe 2026-07-17 ("it's genuinely unexplored and even partial exploration — especially empirical — can reveal patterns"). That authorization covers **exactly the scope in this brief**, nothing more.

## The framing mandate

This is an **empirical probe, findings-grade, not wiki-grade**. The deliverable is a findings document plus a runnable script — **no wiki page is edited at all** (no reverse.md subsection, no bridge.md pointer, no index/HANDOFF sweep; the main session and author decide placement later, if any). Register flat: report measured tables and exact verified identities; label every extrapolation a heuristic; no claim that any pattern found moves the Bridge. The sorting question (external reviewer's lens, adopted by the program): anything found here is about *which itineraries are arithmetically realized* — the open side — but a pattern on periodic words is evidence about the decided-versus-open boundary, not leverage on aperiodic words.

## Setup (established, cite rather than re-derive)

For a constant word `W = ((m,r))^∞` and diagonal window `n`: `R^σ_{n,n}(W)` is one residue class mod `Q_n = 2^{(m+r)n+1}·3^{mn}` intersected with the sector, liveness of `y₀`, and liveness of the deepest chain door (both class facts are iff's: 14.15.1.4–.5 forward, 14.15.5.1/14.15.6.4 backward). The class representative is the CRT lift `ρ_n := y* mod Q_n` of the fixed point `y* = β/(1−α)` — a rational with denominator `q` coprime to `6`, hence a `2`-adic and `3`-adic integer, so `ρ_n` is well defined; the constant chain at `y*` satisfying every window is the same one-line argument as in the integer case, run in `Z₂ × Z₃`. Since `y*` is **not** an integer here, `ρ_n` is not a small constant: writing `ρ_n = (a + k_n Q_n)/q` form, `ρ_n/Q_n ≈ j_n/q` where `j_n ≡ −a·Q_n^{−1} (mod q)`, `j_n ∈ {1,…,q−1}` — and since `Q_n mod q` is **eventually periodic in `n`** (powers of `2` and `3` mod `q`), so is `j_n`. Deepest chain door: `y_{−n} = y* + (y₀ − y*)/A_n`; for `y₀ = ρ_n + kQ_n` this is an integer whose mod-3 residue the script should derive and check rather than assume.

**Main-session hypotheses to test (stated up front so they are tested, not rediscovered):**

- **(P1)** `H^σ_{n,n}/Q_n` is **eventually periodic in `n`** (driven by the periodicity of `j_n` and of the liveness pattern), with values essentially in `{j/q + small} ∪ {j/q + small + k}` for the first viable progression steps.
- **(P2)** Consequently `H^σ_{n,n} ≥ (1/q − o(1))·Q_n` — i.e. for **all** periodic single-letter words, escape at the full CRT-modulus rate with a denominator-bounded constant, making the rigidity lower bound elementary on the whole periodic-word shelf (integer case: exact laws; non-integral case: denominator bound). If P1/P2 hold empirically, the genuine rigidity content of height growth is confined to **aperiodic** words — which is exactly the Bridge, and out of scope here.
- **(P3)** The first-viable `k` is bounded (conjecturally `≤ 3`, by the mod-3 liveness pattern); record its distribution.

A refutation of any of P1–P3 is a **more** valuable finding than a confirmation; do not force the data to fit.

## Queue, in order

1. **Instance grid.** All single-letter words `((m,r))^∞` with `1 ≤ m, r ≤ 3` except the two integer-fixed-point cases `(1,1)` (`y* = 1`) and `(2,1)` (`y* = −5`) — seven words (compute each `y*` exactly with `Fraction`; e.g. `(1,2): 1/5`, `(2,2): 5/7`, `(1,3): 1/13`, `(3,1): −19/11`, `(3,2): 19/5`... derive, don't trust this list). Wait — recompute every `y*` yourself; if any turns out integral, note it and treat it under the exact-law mechanism instead (do not develop it — one sentence, it belongs to the companion brief's shelf).
2. **Exact height tables.** For each word, each sector `σ ∈ {+, −}`: `H^σ_{n,n}` exactly, `n = 1` to at least `15` (further if cheap; candidates are `ρ_n + kQ_n` scanned in increasing `|y₀|`, membership verified by **direct simulation** — forward stratum match, backward chain via the predecessor formula, deepest-door liveness — never by the class reasoning alone). Brute-force cross-check at `n = 1, 2` for every word/sector (scan all odd integers in range, no class construction). Record per row: `H`, first-viable `k`, `ρ_n/Q_n`, `H/Q_n` (to 6 decimals).
3. **Pattern analysis against P1–P3.** Periodicity detection on `j_n` and on `H/Q_n` (exact, via `Q_n mod q` cycle lengths — compute the multiplicative structure, don't curve-fit); the `k` distribution; any word/sector where `H/Q_n` drifts toward `0` or grows past the predicted band (either would refute P2/P3 — flag loudly). Tabulate one summary: per word/sector, the eventual period and the value set of `H/Q_n`.
4. **Findings document.** `briefs/h-nonintegral-probe-findings.md`: the tables (or their summary with full data in the script's output), verdicts on P1–P3 (confirmed at the tested ranges / refuted with the counterexample row), the exact mechanism found (if the eventual periodicity admits a clean closed form per word, state it as a verified empirical identity over the tested range — **not** as a theorem), obstructions and surprises, and a calibrated closing paragraph: what this says about where the rigidity content of height growth actually lives, in the sorting question's terms.

## Success / stop criteria

- **Floor (expected):** items 1–2 (the grid and exact tables, cross-checked).
- **Primary:** items 3–4.
- **Stop:** after item 4, stop. Explicitly forbidden, whatever the results suggest: **any aperiodic word** (that is the Bridge/AEH, parked by the stopping rules the author's exception does not touch); multi-letter words (record as the natural next probe if the data invites it — a proposal sentence in the findings doc, not an execution); any theorem-grade wiki write; any proof attempt on P2 beyond exact per-word verified identities; any cycle-exclusion or equidistribution attempt; any growth study of anything other than `H^σ_{n,n}` on the named grid. Off-brief findings go in the findings doc's own section; log them and stop anyway.

## Rules (non-negotiable, from AGENTS.md)

- Exact integer/`Fraction` arithmetic wherever a pass/fail or minimality decision is made; every reported `H` value re-verified by direct simulation; seeds and date recorded.
- Code goes in `experiments/h_nonintegral_probe.py`, imports nothing from `realization_height.py`, `diagonal_converse.py`, `signed_diagonal.py`, `itinerary_coding.py`, `block_map.py`, or `door_seam.py`, states which findings it supports, stays runnable end-to-end in minutes.
- Failures, shortfalls (search bounds hit), and refuted hypotheses are recorded, not deleted or smoothed.
- Register norm: flat, calibrated prose; heuristics labeled heuristics; the findings doc's closing paragraph must state plainly that nothing here moves the Bridge.
- Work on branch **`h-nonintegral-probe`** (create it in your worktree from the current HEAD), commit per item, and **do not merge or push** — the main session reviews and re-runs the script before merging.
- No scope expansion.

## Definition of done

The seven-word × two-sector grid computed exactly to `n ≥ 15` with brute-force cross-checks at `n = 1, 2`; P1–P3 each given an explicit verdict with evidence; `briefs/h-nonintegral-probe-findings.md` written in the register with the calibrated closing paragraph; clean per-item commits on `h-nonintegral-probe` with `experiments/h_nonintegral_probe.py` committed and passing; no wiki page touched.
