# Brief: empirical probe — height growth on multi-letter periodic words with non-integral fixed point (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — this brief operates under an explicit, recorded author exception, see Provenance), `AGENTS.md` (house norms), `reverse.md` §14.14.8 (composed affine maps `A_P, B_P`, fixed point of a period), §14.15.1.4–.5, §14.15.4–14.15.6 (heights, admissibility class, signed apparatus), §14.15.7 (the integer-fixed-point mechanism, **especially 14.15.7.5's whole-period window convention and its scope note** — windows that cut a period partway are out of bounds there and here), and `briefs/h-nonintegral-probe-findings.md` (the single-letter probe this brief extends; its §5 carries the one-sentence proposal this brief executes).

## Provenance and authorization

The single-letter probe (merged 2026-07-17) closed with one permitted proposal: multi-letter periodic words with non-integral composed fixed point, testing whether the same denominator mechanism governs `H/Q` with the unit `g` replaced by the word's composed unit. The author authorized executing it 2026-07-17. The authorization covers **exactly the scope in this brief**, nothing more. A parallel branch (`nonintegral-mechanism`) is proving the single-letter identities — do **not** coordinate with it, read it, or anticipate its results; your hypotheses below are stated from the merged probe findings alone.

## The framing mandate

Empirical, findings-grade, **no wiki page edited at all** (no reverse.md, bridge.md, index.md, HANDOFF.md changes — the main session records pointers at merge). Deliverables are exactly `experiments/multiletter_h_probe.py` and `briefs/multiletter-h-probe-findings.md`. Register flat; heuristics labeled; the closing paragraph states plainly that nothing here moves the Bridge (bridge.md §16). A refutation of any hypothesis is more valuable than a confirmation.

## Setup (cite, don't re-derive)

For a period `P = ((m_0,r_0),…,(m_{p−1},r_{p−1}))`, `W = P^∞`: `S_P = Σ(m_i+r_i)`, `M_P = Σ m_i`, composed constants `A_P, B_P` (14.14.8.2, deepest-first convention per 14.15.5.1's order note), fixed point `y* = B_P/(1−A_P)`, written `a/q` in lowest terms. **Whole-period diagonal windows only** (window = `n` periods each side, i.e. `(np, np)` in letters — 14.15.7.5's convention); `Q_n = 2^{nS_P+1}·3^{nM_P}`. Per-sector heights per Definition 14.15.6.8. The class facts (14.15.1.5 forward, 14.15.6.4 backward) are word-general iffs; the candidate progression is `ρ_n + kQ_n` with `ρ_n = a·q^{−1} mod Q_n` — but **verify every reported `H` by direct simulation only** (forward stratum match over `np` letters; backward letter-prescribed chain to depth `np` with per-step integrality; liveness of `y₀` and the deepest door; sector; `y ≠ −1`), never by class reasoning alone.

**Hypotheses to test** (from the single-letter probe's mechanism, `g` replaced by the composed unit `g_P := 2^{S_P}·3^{M_P} mod q`):

- **(M1)** `j_n := (qρ_n − a)/Q_n ∈ {1,…,q−1}` obeys `j_n = −a·2^{−1}·g_P^{−n} mod q`, purely periodic in `n` with period `ord_q(g_P)`; hence `v_n := H^σ_{np,np}/Q_n − σa/(qQ_n)` is purely periodic from `n = 1`.
- **(M2)** `v_n ≥ 1/q` exactly at every row — escape at the full CRT-modulus rate, denominator-bounded constant, sharp constant `j_min/q` over the visited coset orbit.
- **(M3)** First-viable `k` obeys the same mod-3 rule via `t_n := (a + 2j_n)·q^{−1} mod 3` — `k⁺ = [t_n = 0]`, `k⁻ = 1 + [t_n = 2]` — in particular `k ≤ 2`. (The deepest-door factor should again be `Q_n/A_P^n = 2^{2nS_P+1} ≡ 2 (mod 3)`; check it rather than assume it.)
- **(M4) Rotation dependence — the genuinely new question.** A cyclic word has `p` rotations, each its own bi-infinite word with its own fixed point (`y*` of the rotated period — the `G`-orbit of the original `y*` in `Q₂∩Q₃`, when it is rational... compute, don't assume). Anchoring whole-period windows at each rotation gives `p` height sequences. Hypothesis: each rotation independently obeys M1–M3 with its own `(a,q)` — same `q`? (the denominators of the `p` rotated fixed points: equal, or related by units? record what the data says) — so the "one word" has a `p`-tuple of periodic escape constants.

## Queue, in order

1. **Instance grid.** All period-2 words with letters in `{1,2}²` (16 ordered pairs; skip rotations of an already-included word except as needed for M4, and skip any with integral `y*` — record which, one line each), plus at least 4 period-3 words sampled with letters in `{1,2}²` chosen to vary `q`. Compute each `y* = a/q` exactly (`Fraction`); tabulate `(P, a, q, g_P, ord_q(g_P))`.
2. **Exact height tables.** Per word, both sectors, `n = 1` to at least `10` whole periods (further if cheap): `H^σ_{np,np}` by progression scan with direct-simulation verification; brute-force cross-check at `n = 1` for every word/sector (full odd scan, no class construction) and at `n = 2` where feasible (record where it is not, honestly — the single-letter probe's forward-class-progression fallback is acceptable there, cite it).
3. **M1–M3 verdicts** with per-row exact checks, same discipline as the single-letter probe (`j_n` against the formula; `v_n` periodicity by exact period detection; `k` distribution; any drift toward 0 or past the predicted band flagged loudly).
4. **M4: rotations.** For at least 4 words spanning different `q`: all `p` rotations' fixed points and height sequences at `n = 1..6`; verdict on M4 with the denominators' relationship recorded.
5. **Findings document** `briefs/multiletter-h-probe-findings.md`: grid, tables (summary + script output), M1–M4 verdicts with one-line evidence each, surprises/obstructions/shortfalls, the calibrated closing paragraph (where rigidity content now provably-or-empirically lives, in the sorting question's terms; Bridge unmoved). At most one proposal sentence for a next probe, if the data invites one.

## Success / stop criteria

- **Floor (expected):** items 1–2.
- **Primary:** items 3–5.
- **Stop:** after item 5, stop. Explicitly forbidden: **any aperiodic word**; per-letter (period-cutting) windows; period `> 3`; any theorem-grade wiki write; any proof attempt beyond exact per-row verified identities; any cycle-exclusion or equidistribution attempt. Off-brief findings go in the findings doc's own section; log them and stop anyway.

## Rules (non-negotiable, from AGENTS.md)

- Exact integer/`Fraction` arithmetic wherever a pass/fail or minimality decision is made; deterministic (no RNG, or fixed recorded seeds); date recorded; runs end-to-end in minutes.
- Code in `experiments/multiletter_h_probe.py`, importing nothing from `h_nonintegral_probe.py`, `height_exact_laws.py`, `realization_height.py`, `diagonal_converse.py`, `signed_diagonal.py`, `itinerary_coding.py`, `block_map.py`, or `door_seam.py`.
- Failures, shortfalls, and refuted hypotheses recorded, not deleted or smoothed.
- Work on branch **`multiletter-h-probe`** (create in your worktree from current HEAD), commit per queue item. Do **not** push or merge — the main session reviews and re-runs before merging.
- No scope expansion.

## Definition of done

The grid computed exactly (≥16 period-2 + ≥4 period-3 words, both sectors, `n ≥ 10` whole periods) with brute-force cross-checks; M1–M4 each given an explicit verdict with evidence; the findings doc written in the register with the calibrated closing paragraph; clean per-item commits on `multiletter-h-probe` with the script passing; no wiki page touched.
