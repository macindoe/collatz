# Findings: empirical probe — height growth on multi-letter periodic words with non-integral fixed point

Branch `multiletter-h-probe`, 2026-07-17, per `briefs/multiletter-h-probe-brief.md` (author-authorized bounded exception, 2026-07-17, to the standing stop lines 14.15.4(d)/14.15.6(e)/14.15.7(d); the exception covers exactly the brief's scope). Script: `experiments/multiletter_h_probe.py` — deterministic (no RNG), exact `int`/`Fraction` arithmetic for every pass/fail and minimality decision, runs end-to-end in ~11 s; the full per-row tables are its output. **Whole-period diagonal windows only** (window `(np, np)` in letters = `n` periods each side, 14.15.7.5's convention; no per-letter/period-cutting window anywhere). This document is findings-grade: no wiki page is edited, and nothing below is a theorem — closed forms are stated as **verified empirical identities over the tested range** only.

Notation, per word `P` (period `p ∈ {2,3}`), `W = P^∞`: `S_P = Σ(m_i+r_i)`, `M_P = Σm_i`, `y* = B_P/(1−A_P) = a/q` in lowest terms (14.14.8.2/14.14.8.4, application order = deepest-first, 14.15.5.1's order note), `Q_n = 2^{nS_P+1}·3^{nM_P}`, `ρ_n = a·q^{−1} mod Q_n`, `j_n = (qρ_n − a)/Q_n`, `g_P = 2^{S_P}·3^{M_P} mod q`, `v_n = H^σ_{np,np}/Q_n − σa/(qQ_n)` (exactly `j_n/q + k` for `σ=+`, `k − j_n/q` for `σ=−`), `t_n = (a + 2j_n)·q^{−1} mod 3`.

## 1. Instance grid (brief item 1)

**Period-2: all 16 ordered pairs with letters in {1,2}², `y*` exact, one line each.**

| word | y* | disposition |
|---|---|---|
| ((1,1),(1,1)) | `1` | integral — excluded (exact-law shelf, 14.15.7.5) |
| ((1,1),(1,2)) | `7/23` | probed |
| ((1,1),(2,1)) | `29/5` | probed |
| ((1,1),(2,2)) | `29/37` | probed |
| ((1,2),(1,1)) | `11/23` | rotation of an included word — excluded (used in M4) |
| ((1,2),(1,2)) | `1/5` | probed (constant pair — single-letter word (1,2) at doubled windows; consistency anchor) |
| ((1,2),(2,1)) | `49/37` | probed |
| ((1,2),(2,2)) | `49/101` | probed |
| ((2,1),(1,1)) | `23/5` | rotation — excluded (used in M4) |
| ((2,1),(1,2)) | `23/37` | rotation — excluded (kept for M4) |
| ((2,1),(2,1)) | `−5` | integral — excluded (exact-law shelf, 14.15.7.5) |
| ((2,1),(2,2)) | `85/47` | probed |
| ((2,2),(1,1)) | `31/37` | rotation — excluded (used in M4) |
| ((2,2),(1,2)) | `31/101` | rotation — excluded (kept for M4) |
| ((2,2),(2,1)) | `125/47` | rotation — excluded (kept for M4) |
| ((2,2),(2,2)) | `5/7` | probed (constant pair — single-letter word (2,2) at doubled windows; consistency anchor) |

No non-constant period-2 word in this alphabet has integral `y*`; the only integral cases are the two already on the exact-law shelf (`1`, `−5`).

**Period-3: 24 rotation classes of the 64 ordered triples** (full census printed by the script: 4 constant classes excluded as period-1 words — `y* = 1, 1/5, −5, 5/7` — no integral non-constant class exists in this alphabet). Deterministic selection walking canonical classes in lex order, taking each new denominator until 5 words: **selected** `((1,1),(1,1),(1,2))` (`37/101`), `((1,1),(1,1),(2,1))` (`143/47`), `((1,1),(1,1),(2,2))` (`143/175`), `((1,1),(1,2),(1,2))` (`53/229`), `((1,1),(1,2),(2,2))` (`223/431`). Denominators observed across the census range from `5` to `1805`, all coprime to 6 (as they must be: `q | 2^{S_P} − 3^{M_P}`).

**The probed grid (13 words):**

| word | p | y* = a/q | S_P | M_P | g_P | ord_q(g_P) |
|---|---|---|---|---|---|---|
| ((1,1),(1,2)) | 2 | 7/23 | 5 | 2 | 12 | 11 |
| ((1,1),(2,1)) | 2 | 29/5 | 5 | 3 | 4 | 2 |
| ((1,1),(2,2)) | 2 | 29/37 | 6 | 3 | 26 | 3 |
| ((1,2),(1,2)) | 2 | 1/5 | 6 | 2 | 1 | 1 |
| ((1,2),(2,1)) | 2 | 49/37 | 6 | 3 | 26 | 3 |
| ((1,2),(2,2)) | 2 | 49/101 | 7 | 3 | 22 | 50 |
| ((2,1),(2,2)) | 2 | 85/47 | 7 | 4 | 28 | 23 |
| ((2,2),(2,2)) | 2 | 5/7 | 8 | 4 | 2 | 3 |
| ((1,1),(1,1),(1,2)) | 3 | 37/101 | 7 | 3 | 22 | 50 |
| ((1,1),(1,1),(2,1)) | 3 | 143/47 | 7 | 4 | 28 | 23 |
| ((1,1),(1,1),(2,2)) | 3 | 143/175 | 8 | 4 | 86 | 15 |
| ((1,1),(1,2),(1,2)) | 3 | 53/229 | 8 | 3 | 42 | 19 |
| ((1,1),(1,2),(2,2)) | 3 | 223/431 | 9 | 4 | 96 | 43 |

Sanity anchors reproduced exactly at startup: `((1,1)) → 1`, `((2,1)) → −5`, `((4,1),(3,3)) → −17`, each checked to be a genuine `G`-cycle on its word by direct iteration.

## 2. Exact height tables (brief item 2)

Per word and sector, `H^σ_{np,np}` computed for `n = 1..n_max` with `n_max = max(12, min(ord_q(g_P)+12, 130))` (brief floor 10; extended so at least one full algebraic period beyond `ord` is observed for every word — largest table `n = 1..62`, heights reaching `~10^254`, all exact integers). Every candidate on the progression `ρ_n ± kQ_n` was verified by **direct simulation only**: forward stratum match over `np` letters via iterated `G`; backward letter-prescribed chain to depth `np` via the unique-predecessor formula with per-step integrality; liveness of `y₀` and the deepest door; sector sign; `y ≠ −1`. The deepest door was additionally derived from the exact affine identity `y_{−np} = y* + (y₀ − y*)/A_P^n` (`Fraction` arithmetic) and matched the simulated chain at **all 948 verified rows** (804 main + 144 M4), 0 mismatches. Every candidate rejected before the first viable one failed on **deepest-door liveness alone** (0 non-`deepest_dead` failures in the entire run; the script flags any loudly). No search-bound shortfall occurred anywhere.

**Brute-force cross-checks, 52/52 exact matches.** At `n = 1`: full scan of all odd integers of the sector in increasing `|y|`, no class construction, all 26 word/sector pairs. At `n = 2`: the same full scan where `H ≤ 2.5×10⁷` (12 of 26 pairs); for the 14 pairs marked `*` below the full scan is infeasible and the **forward-class-progression fallback** was used — the deviation 14.15.7.6's own verification already records for its `n = 2` check: scan restricted to the forward cylinder class mod `2^{2S_P+1}` (representative built by constructive lifting and then *verified by direct simulation*; completeness of the class is the merged cylinder theorem 14.15.1.5/14.15.6.5), every member below the class-scan value tested by full direct simulation, no CRT/3-adic class reasoning. Fallback member counts ranged 297–12,377.

| word | H⁺₁ | H⁺₂ | H⁻₁ | H⁻₂ |
|---|---|---|---|---|
| ((1,1),(1,2)) | 977 | 64,913 | 175 | 266,863 |
| ((1,1),(2,1)) | 2,425 | 895,801 | 1,031 | 597,191 |
| ((1,1),(2,2)) | 281 | 4,842,137 | 6,631 | 7,101,799 |
| ((1,2),(1,2)) | 461 | 265,421 | 691 | 398,131 |
| ((1,2),(2,1)) | 1,309 | 4,680,733 | 5,603 | 7,263,203 |
| ((1,2),(2,2)) | 6,365 | 4,257,245 | 7,459 | 43,518,499* |
| ((2,1),(2,2)) | 21,179 | 192,119,483* | 20,293 | 237,862,213* |
| ((2,2),(2,2)) | 23,699 | 1,105,667,219* | 17,773 | 614,259,565* |
| ((1,1),(1,1),(1,2)) | 1,985 | 38,315,201* | 4,927 | 9,460,543 |
| ((1,1),(1,1),(2,1)) | 22,945 | 100,634,017* | 18,527 | 329,347,679* |
| ((1,1),(1,1),(2,2)) | 25,121 | 226,047,521* | 16,351 | 633,915,871* |
| ((1,1),(1,2),(1,2)) | 785 | 38,804,753* | 13,039 | 152,298,223* |
| ((1,1),(1,2),(2,2)) | 90,065 | 6,488,633,297* | 75,823 | 391,073,839* |

**Consistency anchor vs the merged single-letter probe** (`briefs/h-nonintegral-probe-findings.md` §2): the two constant-pair words at `n` whole periods are the single-letter words at doubled windows, and the values match exactly — `((1,2),(1,2))` at `n=1` gives `(H⁺, H⁻) = (461, 691)` = single-letter `(1,2)` at `n=2`; `((2,2),(2,2))` gives `(23699, 17773)` = single-letter `(2,2)` at `n=2`.

## 3. Summary table and the mechanism (brief item 3)

All entries exact and verified per row (`min v` is over the word's full table; `1/q` and `j_min/q` for the M2 comparison; per-row check columns all passed — j-law, t/mod-3 law, k-rule, factor `Q_n/A_P^n = 2^{2nS_P+1} ≡ 2 (mod 3)` checked as an exact `Fraction` identity at every `n`, not assumed):

| word | y* | σ | ord | n_max | per(j) | per(v) | k-dist | min v | 1/q | j_min/q |
|---|---|---|---|---|---|---|---|---|---|---|
| ((1,1),(1,2)) | 7/23 | + | 11 | 23 | 11 | 11 | {0:14, 1:9} | 2/23 | 1/23 | 1/23 |
| ((1,1),(1,2)) | 7/23 | − | 11 | 23 | 11 | 11 | {1:13, 2:10} | 7/23 | 1/23 | 1/23 |
| ((1,1),(2,1)) | 29/5 | + | 2 | 14 | 2 | 2 | {0:7, 1:7} | 3/5 | 1/5 | 2/5 |
| ((1,1),(2,1)) | 29/5 | − | 2 | 14 | 2 | 2 | {1:14} | 2/5 | 1/5 | 2/5 |
| ((1,1),(2,2)) | 29/37 | + | 3 | 15 | 3 | 3 | {0:15} | 3/37 | 1/37 | 3/37 |
| ((1,1),(2,2)) | 29/37 | − | 3 | 15 | 3 | 3 | {1:5, 2:10} | 33/37 | 1/37 | 3/37 |
| ((1,2),(1,2)) | 1/5 | + | 1 | 13 | 1 | 1 | {0:13} | 2/5 | 1/5 | 2/5 |
| ((1,2),(1,2)) | 1/5 | − | 1 | 13 | 1 | 1 | {1:13} | 3/5 | 1/5 | 2/5 |
| ((1,2),(2,1)) | 49/37 | + | 3 | 15 | 3 | 3 | {0:10, 1:5} | 14/37 | 1/37 | 14/37 |
| ((1,2),(2,1)) | 49/37 | − | 3 | 15 | 3 | 3 | {1:5, 2:10} | 6/37 | 1/37 | 14/37 |
| ((1,2),(2,2)) | 49/101 | + | 50 | 62 | 50 | 50 | {0:47, 1:15} | 2/101 | 1/101 | 2/101 |
| ((1,2),(2,2)) | 49/101 | − | 50 | 62 | 50 | 50 | {1:36, 2:26} | 3/101 | 1/101 | 2/101 |
| ((2,1),(2,2)) | 85/47 | + | 23 | 35 | 23 | 23 | {0:22, 1:13} | 2/47 | 1/47 | 1/47 |
| ((2,1),(2,2)) | 85/47 | − | 23 | 35 | 23 | 23 | {1:20, 2:15} | 10/47 | 1/47 | 1/47 |
| ((2,2),(2,2)) | 5/7 | + | 3 | 15 | 3 | 3 | {0:10, 1:5} | 1/7 | 1/7 | 1/7 |
| ((2,2),(2,2)) | 5/7 | − | 3 | 15 | 3 | 3 | {1:15} | 3/7 | 1/7 | 1/7 |
| ((1,1),(1,1),(1,2)) | 37/101 | + | 50 | 62 | 50 | 50 | {0:48, 1:14} | 2/101 | 1/101 | 2/101 |
| ((1,1),(1,1),(1,2)) | 37/101 | − | 50 | 62 | 50 | 50 | {1:36, 2:26} | 3/101 | 1/101 | 2/101 |
| ((1,1),(1,1),(2,1)) | 143/47 | + | 23 | 35 | 23 | 23 | {0:19, 1:16} | 10/47 | 1/47 | 5/47 |
| ((1,1),(1,1),(2,1)) | 143/47 | − | 23 | 35 | 23 | 23 | {1:23, 2:12} | 2/47 | 1/47 | 5/47 |
| ((1,1),(1,1),(2,2)) | 143/175 | + | 15 | 27 | 15 | 15 | {0:19, 1:8} | 1/175 | 1/175 | 1/175 |
| ((1,1),(1,1),(2,2)) | 143/175 | − | 15 | 27 | 15 | 15 | {1:18, 2:9} | 24/175 | 1/175 | 1/175 |
| ((1,1),(1,2),(1,2)) | 53/229 | + | 19 | 31 | 19 | 19 | {0:20, 1:11} | 13/229 | 1/229 | 2/229 |
| ((1,1),(1,2),(1,2)) | 53/229 | − | 19 | 31 | 19 | 19 | {1:19, 2:12} | 8/229 | 1/229 | 2/229 |
| ((1,1),(1,2),(2,2)) | 223/431 | + | 43 | 55 | 43 | 43 | {0:36, 1:19} | 26/431 | 1/431 | 13/431 |
| ((1,1),(1,2),(2,2)) | 223/431 | − | 43 | 55 | 43 | 43 | {1:39, 2:16} | 10/431 | 1/431 | 13/431 |

(Full value sets of `v_n` per word/sector are printed by the script; long ones — up to 50 values for `q = 101` — are omitted here.)

**The mechanism, as verified empirical identities over all 804 main rows plus all 144 M4 rows, 0 failures** (not theorems; no proof attempted, per the stop line) — the single-letter probe's four identities carry over verbatim with `g` replaced by the composed unit `g_P`:

1. `j_n = −a·2^{−1}·g_P^{−n} mod q`, with `j_n ∈ {1,…,q−1}` always — purely periodic in `n` with period exactly `ord_q(g_P)`.
2. The deepest door of the `k`-th lift is `y* + (σkq + j_n)·2^{2nS_P+1}/q` exactly (equivalently `y_{−np} = y* + (y₀−y*)/A_P^n`, matched at every row), and `2^{2nS_P+1} ≡ 2 (mod 3)` for every `n` (odd exponent; checked as an exact identity, per the brief's parenthetical), so its mod-3 residue is `t_n + 2σk`.
3. Exactly one `k` in every three consecutive candidates has a dead deepest door: first-viable `k` obeys `k⁺ = [t_n = 0]`, `k⁻ = 1 + [t_n = 2]` — every row, so `k ≤ 2` throughout (global k-distributions over the main tables: `+` {0: 280, 1: 122}, `−` {1: 256, 2: 146}).
4. Hence `H⁺ = ρ_n + [t_n = 0]·Q_n`, `H⁻ = (1 + [t_n = 2])·Q_n − ρ_n` at every tested row, and `v_n` is purely periodic from `n = 1` (no pre-period observed anywhere) with period exactly `ord_q(g_P)`.

## 4. Verdicts on M1–M4

- **M1 — CONFIRMED.** `j_n ∈ {1,…,q−1}` and `j_n = −a·2^{−1}·g_P^{−n} mod q` at every row of every word and rotation; `j_n` and `v_n` both purely periodic from `n = 1` with detected period exactly `ord_q(g_P)` (each word observed for at least one full period beyond `ord`, up to `ord = 50` observed over 62 rows).
- **M2 — core CONFIRMED, sharp-constant clause REFUTED.** `v_n ≥ 1/q` holds exactly at every row (escape at the full CRT-modulus rate, denominator-bounded constant). But the claimed sharp constant `j_min/q` over the visited coset orbit is **wrong on 6 of 13 words** (`+` sector): `min v_n > j_min/q` for `((1,1),(1,2))` (2/23 vs 1/23), `((1,1),(2,1))` (3/5 vs 2/5), `((2,1),(2,2))` (2/47 vs 1/47), `((1,1),(1,1),(2,1))` (10/47 vs 5/47), `((1,1),(1,2),(1,2))` (13/229 vs 2/229), `((1,1),(1,2),(2,2))` (26/431 vs 13/431). Cause, visible in the exact data: at the row where `j_n = j_min`, the mod-3 rule can force `k = 1` (`t_n = 0`), so the true sharp constant is `min over the orbit of (j/q + k⁺(t(j)))` — a joint function of the coset orbit *and* the mod-3 law, not of the orbit alone. (In the single-letter probe's seven words this never happened, which is why its §4 wording survived there; the multi-letter grid is the first place it breaks.)
- **M3 — CONFIRMED.** `t_n = (a + 2j_n)·q^{−1} mod 3` predicts the first-viable `k` by `k⁺ = [t_n = 0]`, `k⁻ = 1 + [t_n = 2]` at all 948 verified rows; `k ≤ 2` always; the deepest-door factor is exactly `Q_n/A_P^n = 2^{2nS_P+1} ≡ 2 (mod 3)` at every `n` (checked, not assumed).
- **M4 — CONFIRMED** (5 words, `q = 23, 5, 37, 175, 229`, all rotations, `n = 1..6`, both sectors). Each rotation's fixed point, computed exactly from its own `A, B`, equals the `G`-affine image of the previous rotation's (`y*_{i+1} = α_i y*_i + β_i`, exact, all words) — the rotated fixed points are one `G_affine`-orbit of rationals. **All rotations of a word share the same denominator `q`** (numerators differ: e.g. `7/23 → 11/23`; `143/175 → 151/175 → 157/175`). Every rotation independently satisfies M1–M3 with its own numerator `a_i`: so one cyclic word carries a `p`-tuple of periodic escape constants, all with the same `q`, `g_P`, and period `ord_q(g_P)`, differing only in the coset offset. Observed corollary of the j-law (data, not forced): rotation `i+1`'s `j`-sequence is the unit multiple `(a_{i+1}/a_i mod q)` of rotation `i`'s, verified implicitly by the per-rotation j-law holding.

## 5. Obstructions, surprises, shortfalls

- **No shortfalls.** First-viable `k ≤ 2` at every one of 948 verified rows; no scan cap was hit; all 52 brute-force cross-checks completed and matched.
- **Refutation (the probe's main negative result): M2's sharp constant, §4 above.** The single-letter probe's `j_min/q` formula for the escape constant does not survive multi-letter words; the corrected empirical formula (min of `j/q + k(t(j))` over the orbit) is stated there.
- **Surprise: cross-word coincidence of the escape spectra.** Words sharing `(q, g_P)` whose numerators lie in the same coset of `⟨g_P⟩ ≤ (Z/q)^×` have **identical value sets of `v_n`** in both sectors, even across different periods `p`: `((1,2),(2,2))` (`49/101`, `p=2`) and `((1,1),(1,1),(1,2))` (`37/101`, `p=3`) have equal `+` and equal `−` value sets (checked exactly, full sets); `49/37 ∈ ⟨g_P⟩ mod 101`. And when the numerators lie in **opposite** cosets (`−a` in the other's coset, `−1 ∉ ⟨g_P⟩`), the sectors swap: `((2,1),(2,2))` (`85/47`) and `((1,1),(1,1),(2,1))` (`143/47`) satisfy (`+` set of one) = (`−` set of the other), both directions, exactly. Consistent with the j-law (`v` depends on the word only through the coset `−a·2^{−1}⟨g_P⟩` and the mod-3 rule), and recorded as data; labeled heuristic beyond the tested instances.
- **Deviation recorded: the `n = 2` brute-force fallback.** 14 of 26 word/sector pairs have `H₂ > 2.5×10⁷`, where a literal full odd scan is infeasible; the forward-class-progression fallback (§2) was used exactly as the brief permits, citing 14.15.7.6's recorded deviation. All other brute checks are literal full scans.
- **Deviation recorded: branch base.** The delegated worktree's checked-out HEAD predated the brief (it lacked `briefs/`'s probe files and reverse.md 14.15.7); the branch was created from the repository's current HEAD `ff35f0d` (the commit carrying this brief) so that the required context existed at the branch point. No other deviation from the brief's process occurred.
- **Heuristic (labeled as such):** the four identities of §3, and the rotation/coset structure of §4–§5, look derivable in a few lines from the merged class iffs (14.15.1.4–.5, 14.15.5.1/14.15.6.4) plus `2^{odd} ≡ 2 (mod 3)`, exactly as the single-letter probe's heuristic said of its own identities; no proof was attempted here (stop line), and until one is written they remain verified identities over the tested ranges only.
- **Off-brief findings:** none beyond the above.

## 6. Where this leaves the rigidity question (calibrated closing)

On the periodic shelf with `p ≤ 3`, the single-letter picture generalizes without resistance: the entire height behavior of a non-integral-fixed-point periodic word — both sectors, every whole-period window — is governed by the same two elementary arithmetic facts as before, now word-composed: the unit-group orbit of `Q_n mod q` (through the composed unit `g_P = 2^{S_P}3^{M_P}`) and `2^{2nS_P+1} ≡ 2 (mod 3)` for the deepest door; rotations add nothing structurally new (a `p`-tuple of coset offsets over one fixed denominator), and the escape spectrum is even coarser than per-word — it depends only on `(q, g_P, ±coset of a)`, identically across words of different periods. The one correction this grid forced (M2's sharp constant) makes the mechanism *more* elementary, not less: the constant is read off the coset orbit jointly with the mod-3 door law, nothing else. In the sorting question's terms: on the decided side of the boundary — periodic words, adelic limits pinned by one rational `y*` — realization/escape stays elementary arithmetic at every period tested, and the genuine rigidity content of height growth (the lower-bound species the frontier seed pointed at) continues to live entirely on **aperiodic** words, where no finite mechanism pins the limits. That is exactly the Bridge (bridge.md §16), and nothing here moves it: no bound, recurrence, or rate for `H` on any non-periodic word follows from anything above, and the stop lines (no aperiodic words, no period-cutting windows, period ≤ 3, no theorem-grade writes, no proof attempts) were respected throughout. One proposal sentence, per the cap: if the main session wants the shelf closed cleanly, the natural next step is not more words but the few-line proof of §3's identities in whole-period generality (the `14.15.8` lane's method applied once at the composed level), which the parallel theorem branch is already positioned to absorb.

**Verification record for this document:** all quoted numbers produced by `experiments/multiletter_h_probe.py` (exact arithmetic; direct simulation of every reported `H`; deepest-door formula cross-check at all 948 rows; 52/52 brute-force cross-checks at `n = 1, 2`, 14 via the recorded fallback; single-letter consistency anchors matched), run 2026-07-17, deterministic, ~11 s.
