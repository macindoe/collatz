# Findings: empirical probe — height growth on periodic words with non-integral fixed point

Branch `h-nonintegral-probe`, 2026-07-17, per `briefs/h-nonintegral-probe-brief.md` (author-authorized bounded exception, 2026-07-17, to the standing stop lines 14.15.4(d)/14.15.6(e); the exception covers exactly the brief's scope). Script: `experiments/h_nonintegral_probe.py` — deterministic (no RNG), exact `int`/`Fraction` arithmetic for every pass/fail and minimality decision, runs end-to-end in under a second; the full per-row tables (`n = 1..25`, all 14 word/sector pairs) are its output. This document is findings-grade: no wiki page is edited, and nothing below is a theorem — closed forms are stated as **verified empirical identities over the tested range** only.

## 1. Instance grid (brief item 1)

All single-letter words `((m,r))^∞`, `1 ≤ m,r ≤ 3`, fixed point `y* = β/(1−α) = (3^m − 2^m)/(2^{m+r} − 3^m)` computed exactly:

| word | y* | status |
|---|---|---|
| (1,1) | `1` | integer — excluded (exact-law shelf, companion brief) |
| (2,1) | `−5` | integer — excluded (exact-law shelf, companion brief) |
| (1,2) | `1/5` | probed |
| (1,3) | `1/13` | probed |
| (2,2) | `5/7` | probed |
| (2,3) | `5/23` | probed |
| (3,1) | `−19/11` | probed |
| (3,2) | `19/5` | probed |
| (3,3) | `19/37` | probed |

Seven non-integral words, as the brief predicted; no additional integral case turned up. Every denominator `q` is coprime to `6`, so the CRT lift `ρ_n := y* mod Q_n`, `Q_n = 2^{(m+r)n+1}·3^{mn}`, is well defined throughout.

## 2. Exact height tables (brief item 2)

For each word and each sector `σ ∈ {+,−}`, `H^σ_{n,n}` was computed exactly for `n = 1..25` (brief floor: 15; extending was cheap) by scanning the progression `y₀ = ρ_n + kQ_n` (σ=+, `k = 0,1,…`) or `y₀ = ρ_n − kQ_n` (σ=−, `k = 1,2,…`) in increasing `|y₀|`, with **every candidate verified by direct simulation only**: forward stratum match letter by letter via iterated `G`; the letter-prescribed backward chain via the unique-predecessor formula with integrality checked at every step; liveness of `y₀` and of the deepest chain door; sector sign; `y ≠ −1`. In addition the deepest door was derived independently from the exact affine formula `y_{−n} = y* + (y₀ − y*)/A_n` (`Fraction` arithmetic) and matched the simulated chain at all 350 rows, 0 mismatches.

**Brute-force cross-checks** at `n = 1, 2`, every word/sector — full scan of all odd integers of the sector in increasing `|y|`, no class construction — 28/28 agree exactly with the class-scan values:

| word | H⁺₁ | H⁺₂ | H⁻₁ | H⁻₂ |
|---|---|---|---|---|
| (1,2) | 29 | 461 | 67 | 691 |
| (1,3) | 37 | 709 | 155 | 8,507 |
| (2,2) | 371 | 23,699 | 205 | 17,773 |
| (2,3) | 451 | 93,763 | 125 | 238,013 |
| (3,1) | 1,255 | 305,383 | 473 | 67,865 |
| (3,2) | 695 | 895,799 | 1,033 | 2,090,185 |
| (3,3) | 4,951 | 1,936,855 | 1,961 | 4,035,113 |

Full tables (per row: `H`, first-viable `k`, `j_n`, `ρ_n/Q_n`, `H/Q_n` to 6 decimals, count of rejected candidates) are printed by the script; heights at `n = 25` reach ~`2.5 × 10^81` (word `(3,3)`, `+` sector), all exact integers. Every candidate rejected before the first viable one failed on **deepest-door liveness alone** — no candidate ever failed the forward stratum match, the backward integrality, `y₀`-liveness, or the sign/singularity conditions (the script flags any such failure loudly; none occurred in 350 rows). No search-bound shortfall occurred anywhere.

## 3. Summary table and the mechanism found (brief item 3)

Notation: `y* = a/q` in lowest terms; `g := 2^{m+r}·3^m mod q`; `P_alg := ord_q(g)`; `j_n ∈ {1,…,q−1}` defined by `ρ_n/Q_n = j_n/q + a/(qQ_n)` exactly; `v_n := H^σ_{n,n}/Q_n − σ·a/(qQ_n)` (the exact "limit value": `v_n = j_n/q + k` for σ=+, `v_n = k − j_n/q` for σ=−). All entries below are exact and verified per row.

| word | y* | σ | P_alg | period of j_n | period of v_n | k-distribution (n=1..25) | value set of v_n | min H/Q_n | 1/q |
|---|---|---|---|---|---|---|---|---|---|
| (1,2) | 1/5 | + | 2 | 2 | 2 | {0: 25} | {2/5, 3/5} | 0.400000 | 0.200000 |
| (1,2) | 1/5 | − | 2 | 2 | 2 | {1: 12, 2: 13} | {3/5, 7/5} | 0.599826 | 0.200000 |
| (1,3) | 1/13 | + | 3 | 3 | 3 | {0: 25} | {2/13, 5/13, 6/13} | 0.153846 | 0.076923 |
| (1,3) | 1/13 | − | 3 | 3 | 3 | {1: 8, 2: 17} | {7/13, 21/13, 24/13} | 0.538461 | 0.076923 |
| (2,2) | 5/7 | + | 3 | 3 | 3 | {0: 16, 1: 9} | {1/7, 4/7, 9/7} | 0.142857 | 0.142857 |
| (2,2) | 5/7 | − | 3 | 3 | 3 | {1: 25} | {3/7, 5/7, 6/7} | 0.428554 | 0.142857 |
| (2,3) | 5/23 | + | 11 | 11 | 11 | {0: 21, 1: 4} | {1/23, 3/23, 4/23, 6/23, 9/23, 12/23, 13/23, 16/23, 18/23, 25/23, 31/23} | 0.043478 | 0.043478 |
| (2,3) | 5/23 | − | 11 | 11 | 11 | {1: 16, 2: 9} | {5/23, 11/23, 14/23, 15/23, 17/23, 20/23, 21/23, 30/23, 33/23, 42/23, 45/23} | 0.217014 | 0.043478 |
| (3,1) | −19/11 | + | 5 | 5 | 5 | {0: 20, 1: 5} | {1/11, 3/11, 4/11, 9/11, 16/11} | 0.090909 | 0.090909 |
| (3,1) | −19/11 | − | 5 | 5 | 5 | {1: 15, 2: 10} | {2/11, 6/11, 8/11, 18/11, 21/11} | 0.181818 | 0.090909 |
| (3,2) | 19/5 | + | 2 | 2 | 2 | {0: 25} | {2/5, 3/5} | 0.400000 | 0.200000 |
| (3,2) | 19/5 | − | 2 | 2 | 2 | {1: 13, 2: 12} | {3/5, 7/5} | 0.597801 | 0.200000 |
| (3,3) | 19/37 | + | 3 | 3 | 3 | {0: 16, 1: 9} | {9/37, 12/37, 53/37} | 0.243243 | 0.027027 |
| (3,3) | 19/37 | − | 3 | 3 | 3 | {1: 25} | {21/37, 25/37, 28/37} | 0.567419 | 0.027027 |

("min H/Q_n" is over `n = 1..25` of the actual ratio `H/Q_n`, which differs from `v_n` by the exact term `σa/(qQ_n) → 0`; for `(3,1)`, `a < 0` makes the `+`-sector ratio sit slightly *below* `j_n/q` at finite `n` — the `o(1)` in P2 is genuinely two-sided.)

**The mechanism, as verified empirical identities over `n = 1..25`, all 350 rows, 0 failures** (not theorems; no proof attempted, per the brief's stop line):

1. `j_n = −a·2^{−1}·g^{−n} mod q` — a unit-group orbit, purely periodic in `n` with period exactly `P_alg = ord_q(g)` (word periods: 2, 3, 3, 11, 5, 2, 3 for (1,2), (1,3), (2,2), (2,3), (3,1), (3,2), (3,3)).
2. The deepest door of the `k`-th lift is `y_{−n}(k) = (a + (j_n + σkq)·2^{2(m+r)n+1})/q` exactly, and since `2^{2(m+r)n+1} ≡ 2 (mod 3)` for every `n`, its mod-3 residue is `t_n + 2σk` where `t_n := (a + 2j_n)·q^{−1} mod 3` — checked at every row against the simulated chain.
3. Exactly one `k` in every three consecutive candidates has a dead deepest door, so the first-viable `k` obeys the closed rule `k⁺ = [t_n = 0]`, `k⁻ = 1 + [t_n = 2]` — checked at all 350 rows.
4. Consequently `H⁺_{n,n} = ρ_n + [t_n = 0]·Q_n` and `H⁻_{n,n} = (1 + [t_n = 2])·Q_n − ρ_n` exactly at every tested row, and `v_n` is **purely periodic from `n = 1`** (no pre-period observed anywhere) with period exactly `P_alg`, since `t_n` is a function of `j_n`.

## 4. Verdicts on P1–P3 (tested range `n = 1..25`, all seven words, both sectors)

- **P1 — CONFIRMED, slightly sharpened.** `H^σ_{n,n}/Q_n` is eventually periodic; in the exact form, `v_n = H/Q_n − σa/(qQ_n)` is *purely* periodic from `n = 1` with period exactly `ord_q(2^{m+r}3^m)`, and `H/Q_n` itself approaches the periodic value set with exact error `σa/(qQ_n)`. Values are exactly `j_n/q + k` (σ=+) and `k − j_n/q` (σ=−) with `k` given by the mod-3 rule — the brief's predicted shape `{j/q + small} ∪ {j/q + small + k}`.
- **P2 — CONFIRMED.** `v_n ≥ 1/q` holds exactly at every row (σ=+: `j_n ≥ 1`, `k ≥ 0`; σ=−: `j_n ≤ q−1`, `k ≥ 1`), so `H^σ_{n,n} ≥ (1/q − o(1))·Q_n` with the `o(1)` explicit (`|a|/(qQ_n)`). Escape is at the full CRT-modulus rate on the entire non-integral shelf, with a denominator-bounded constant. Calibration: the bound `1/q` is *attained* only when the orbit of `j_n` visits `1` (σ=+; it does for (2,2), (2,3), (3,1)) — otherwise the true constant is `j_min/q > 1/q` (e.g. (3,3): `9/37` vs `1/37`), i.e. P2 is a correct lower bound but not always the sharp constant.
- **P3 — CONFIRMED, sharpened.** First-viable `k` is bounded by 1 extra progression step, not 3: observed `k⁺ ∈ {0,1}` (148 vs 27 of 175 rows) and `k⁻ ∈ {1,2}` (114 vs 61) — exactly the mod-3 liveness mechanism (one dead candidate per three consecutive `k`), never two consecutive failures. Distribution per word/sector in the table above.

**No refutation occurred.** The one place the data corrects the brief's phrasing: the brief's P1 gloss "values essentially in `{j/q + small} ∪ {j/q + small + k}` for the first viable progression steps" is right, but the periodicity needs no "eventually" — in exact (`v_n`) form it is purely periodic from the first row.

## 5. Obstructions, surprises, shortfalls

- **No shortfalls.** No search bound was hit anywhere (first-viable `k ≤ 2` always; brute-force scans completed at `n = 1,2` for all 14 pairs).
- **Surprise (mild): sector asymmetry of the `k`-rule.** The `+` sector can succeed at `k = 0` (and does in 85% of rows) while the `−` sector starts at `k = 1` by construction and needs `k = 2` in 35% of rows; the two sectors' dead-`k` conditions (`t_n = 0` vs `t_n = 2`) are different residues of the same `t_n`, so the sectors' `k`-patterns are correlated but not mirror images.
- **Surprise (mild): the escape constant is `j_min/q`, not `1/q`.** Because `j_n` ranges over a coset of the subgroup `⟨g⟩ ≤ (Z/q)^×` rather than all of `{1,…,q−1}`, the sharp per-word constant is `min` over that orbit; `1/q` is attained only when the orbit contains `1`. For `(3,3)` (q = 37, orbit size 3) the sharp constant `9/37` is more than 9× the generic bound.
- **Heuristic (labeled as such):** the four identities of §3 look provable in a few lines from the already-proved class iffs (14.15.1.4–.5, 14.15.5.1/14.15.6.4) plus `2^{odd} ≡ 2 (mod 3)`; no proof was attempted here (stop line), and until one is written they remain verified identities over `n ≤ 25` only.
- **Off-brief findings:** none arose. (One sentence, per the brief's cap: the natural next probe, if the main session wants one, is multi-letter periodic words — period-`p` words with non-integral `y* = B_p/(1−A_p)` — to test whether the same `q`-denominator mechanism governs `H/Q` with `g` replaced by the word's composed unit `2^{S}3^{M} mod q`.)

## 6. Where this leaves the rigidity question (calibrated closing)

On the periodic single-letter shelf, height growth has no mystery left at the empirical level: the integer-fixed-point words obey exact laws (companion brief's territory), and the seven non-integral words escape at the full CRT-modulus rate `H^σ_{n,n} = Θ(Q_n)` with an explicitly periodic, denominator-bounded constant — the entire behavior is driven by two elementary arithmetic facts (the unit-group orbit of `Q_n mod q`, and `2^{2(m+r)n+1} ≡ 2 mod 3` for the deepest door). In the sorting question's terms: this is more evidence that on the *decided* side of the boundary — words whose adelic limits are pinned by finite data, here a single rational `y*` — realization/escape is elementary arithmetic, and the genuine rigidity content of height growth (the lower-bound species the frontier seed pointed at) lives entirely on **aperiodic** words, where no finite mechanism pins the limits. That is exactly the Bridge, and it is out of scope here: nothing in this probe moves the Bridge — no bound, recurrence, or rate for `H` on any non-periodic word follows from anything above, and the stop lines (no aperiodic words, no multi-letter execution, no theorem-grade writes) were respected throughout.

**Verification record for this document:** all quoted numbers produced by `experiments/h_nonintegral_probe.py` (exact arithmetic, direct simulation of every reported `H`, deepest-door formula cross-check at all 350 rows, 28/28 brute-force cross-checks at `n = 1,2`), run 2026-07-17, deterministic, ~0.7 s.
