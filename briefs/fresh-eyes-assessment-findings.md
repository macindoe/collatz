# Findings: fresh-eyes assessment of the whole approach (2026-09-04)

Brief: `briefs/fresh-eyes-record-brief.md`. Branch **`fresh-eyes-record`**, cut from local `main` at `f4d2cd6`.

Register: flat, calibrated prose. Every number below is the output of one of the four scripts in §2 (committed outputs, reproduced byte for byte on a second run) or a quotation from Tao's paper with its page number. Where a fresh measurement differs from a number quoted in the brief, the script's number is the one recorded and the difference is stated (§3.2).

---

## 1. Purpose and scope

A critical re-read of the program by an assistant with no prior stake in it, asked for on 2026-09-04: are the core laws what the pages say they are, does the digit budget say what the pages say it says, is the statistics half correctly located against the literature, and is the parked cycle condition what it appears to be. This file is the assessment's record. It records; it decides nothing. Every front status is unchanged (§4).

Out of scope on this branch: `sources/`, `paper/`, `publication.md`, `aeh.md`. The one question that touches the AEH verdict — whether Tao's *proof* delivers the letter statistics past the digit budget at logarithmic density — was handed to a parallel read (`briefs/tao-section5-read-findings.md`, on `main` at `72b1a27`); its verdict is quoted in §3.3 and nowhere prejudged.

Stopping rules observed (README): no proof attempt on AEH or on any Fourier bound, no cycle-exclusion attempt, no per-period cycle search. The cycle computations below evaluate identities on profiles; none searches for a cycle.

## 2. What was checked

Four scripts, each fresh code (imports nothing from any other script in the repository; the laws re-implemented from their statements), each with a deterministic seed, exact integer or rational arithmetic at every pass/fail decision, an in-script assessment date so that re-runs are byte-identical, and a committed `experiments/<name>_output.txt` written by the script itself from the repo root.

| script | supports | summary line |
|---|---|---|
| `experiments/law_spotcheck_logseries.py` | spine.md 9.8; stage1-synthesis.md 11.8.4.1 (calibration values: the remark after 11.8.3.6.6); stage3.md 11.8.6.3; stage2.md 11.8.5.6 / stage4.md 11.8.7; cycles.md 12.6.1 | anchor by the 2-adic log series in exact rationals; `N(17) = 38`, `N(25) = 245`, `N(33) = 236 (mod 2^8)` reproduced; valuation law on `720` lifting + `1998` off-lifting states, entry-depth law on `2718`, increment identity on `1360` steps mod `2^24`, unrolled `p`-step identity on `309` orbits (`p ≤ 8`): `8` checks, `0` failures |
| `experiments/digit_budget_avalanche.py` | stage4.md 11.8.7.7 (the Calibration paragraph); pointed to from bridge.md 16.2 | `177` starts × `255` bit flips × `40` blocks; three change matrices (core, exit, letter); first letter effect at block `≈ j/4`; the sharp locality bound for exit and letter with `0` violations; all `2,263` high-`j` core changes diagnosed as a resonant-step coordinate artifact: `4` checks, `0` failures |
| `experiments/syrac_residue_fourier.py` | cycles.md Remark 12.6.1.7; aeh.md 13.6.5 (attribution, read only) | `Syrac(Z/3^j)`, `j ≤ 5`, exactly and two ways (chain pushforward against Tao's Lemma 1.12); stationarity, projection (1.23), the printed `Syrac(Z/9)`; TV from uniform-on-units; the Fourier table by `j − v_3(ξ)`; real orbits past the budget: `16` checks, `0` failures |
| `experiments/cycle_offset_identity.py` | cycles.md Remark 12.6.1.7 | `2^(m_0) R_0 = 2^K F_n(a) + q` on `3,000` random profiles; the composed block maps give `Aff_a` exactly (`N_0 = 2^K F_n(a)`); the biconditional `3000/3000`; the cycles `1`, `−5`, `−17` from their words; the `p = 7` staircase; the repetition factor on `100` pairs: `18` checks, `0` failures |

Total: `46` checks, `0` failures.

## 3. The five findings

### 3.1 The core laws hold under an independent anchor implementation

Every existing anchor script in `experiments/` computes `N(ω)` by the discrete-log tower (level-by-level congruence solving). The assessment computed it from the definition `N(u) = −log u / log 9` by the 2-adic logarithm *series*, `log u = Σ_(i≥1) (−1)^(i+1) (u−1)^i / i` for `u ≡ 1 (mod 8)`, in exact rationals: each term is a 2-adic integer of valuation `≥ 3i − v_2(i)`, so the series can be truncated at a valuation bound and the partial sum has an odd denominator, inverted mod `2^K`. The two implementations share nothing.

Checked, zero failures throughout: the calibration values of stage1-synthesis.md (`N(17) ≡ 38`, `N(25) ≡ 245`, `N(33) ≡ 236 (mod 2^8)`; `N(17) ≡ 6 (mod 8)`); the global valuation law `s = 2 + v_2(d − M(ω))` on the two lifting classes `(ω mod 8, d mod 2) ∈ {(1,0), (3,1)}` and the mod-8 table off them (`720 + 1998` states, `ω < 2^40`, `d < 80`); the entry-depth law `m_+ = v_2(x_exit + 1)` on all six classes (`2718` states); the increment identity `M(ω_+) − M(ω) = N((ω_+/ω)^2) (mod 2^24)` (`1360` steps); and an independently derived unrolled `p`-step identity (`309` orbits, `p ≤ 8`) whose corollary is that `ω_p mod 3^(m_1+…+m_p+d_0−d_p)` is a function of the letter word alone.

### 3.2 The digit budget is a delay line, not a fuel gauge

stage4.md 11.8.7.7 says each decided step consumes anchor digits and nothing regenerates them. The consumption identity is correct; the question was what it says about an orbit's *memory* of its start. Flipping one bit `j` of a `256`-bit starting core (`177` valid starts, `d_0 ∈ 1..4`, `40` blocks, `k = 8`):

* **First effect.** The letter word first differs at block `≈ j/4`: mean first-difference block `2.2` at `j = 8`, `4.4` at `16`, `8.3` at `32`, `16.4` at `64`, `32.0` at `128`, against `j/4 = 2, 4, 8, 16, 32`. No bit `j ≥ 200` changes any letter within `40` blocks (`4,950` start–bit pairs), the cumulative `σ` at block `40` averaging `160.7`. Bit `j` is not consulted until `Σσ` reaches it.
* **Never spent.** Flipping any of bits `1..8` changes the core `ω_t mod 2^8` with probability `0.942`–`0.988` at every block `t = 1..40`, the exit `x_exit(t) mod 2^8` with probability `0.943`–`0.993`, and the letter `s_t` with probability `0.60`–`0.70` at every block from `2` on; at `t = 16` the letter-change probability is `0.657` (bits `1..8`) and `0.653` (bits `1..32`), the value for two independent ledger draws being `1 − Σ_j 2^(−2j) = 2/3`. The normalized Hamming distance between the full cores is `0.47`–`0.49` from block `3` on: the whole core is scrambled by the carries of the multiplication by `3^d`, which reads no new digit. That carry propagation is what "regeneration" would have to mean; what is *not* regenerated is local (residue-class) determinism — the classical statement (Terras's cylinder count, Lagarias's shift conjugacy; pinned in publication.md).
* **Locality, sharp.** The underlying integer `X_t = 3^(d_t) ω_t` agrees with its flipped copy modulo `2^(j − Σ_(i<t) σ_i)`, so the exit and the letter at block `t` cannot move once `j ≥ Σ_(i<t) σ_i + k + s_t`. Checked per start: `0` exit changes and `0` letter changes at or beyond that bound. The smallest uniform `c` per block such that no change occurs at `j ≥ Σσ + k + c` is `6`–`12` for the exit and `−1`–`5` for the letter at the printed blocks (`t = 1, 2, 3, 5, 8, 12, 16, 20, 30, 40`), each bounded by the per-start `max s_t` (resp. `max s_t + 1 − k`) as the sharp bound predicts.
* **The coordinate artifact.** The *core* `ω_t mod 2^k` does move under high-`j` flips: `2,263` events with `j ≥ Σσ + k + s_t`, at blocks `1` (`1,929`), `2` (`217`) and `3` (`117`), none later. In every one of the `2,263`: the exit mod `2^k`, every letter `s_0..s_t`, and `X_t mod 2^k` are unchanged; `d_t` differs (by `1` to `7` factors of `3`); and the first earlier block at which the `3`-gain `a` differs is resonant — `d = h(s) = v_3(2^s − 1)` with the same `(s, d)` in both runs (stage3.md 11.8.6.2.1, case 3, where `a_+ = d + v_3(ω + β)` reads high bits of `ω`). A factor of `3` moves between `ω` and `d`; the integer and the letters do not move. Strict locality holds for the exit integer and the letters; the core in `(ω, d)` coordinates is not a local coordinate, by construction.

Differences from the brief's quoted numbers, the script being the authority: the brief quotes the never-spent core probability as `0.95`–`0.99`; over all `40` blocks the measured range is `0.942`–`0.988` (the brief's lower end was read off a subset of blocks). The brief's `≈ 0.67` for the letter is measured as `0.657` / `0.653`. Nothing else differs.

Reading, recorded at stage4.md 11.8.7.7 (Calibration paragraph): the budget bounds what a bounded window can *decide*, not how long the orbit remembers its start. The organizing heuristic is unchanged.

### 3.3 The statistical half is a mixing question, and Tao already worked it

The wiki's framing of the statistics half as "digit statistics of 2-adic logarithms, beyond current theory" is right as a statement about one anchor's digits and, as such, a dead end; as a statement about orbits it is a mixing question for an explicit multiply-and-shift map, which is the road Tao took (arXiv:1909.03562v7; §5 below lists the statements with pages). Fresh numbers on his object, `Syrac(Z/3^j) = F_j(Geom(2)^j) mod 3^j`, computed exactly:

* the law is not uniform on the units — total variation `0.346`, `0.371`, `0.389` from uniform-on-units at `j = 3, 4, 5`; his printed `Syrac(Z/9) = (0, 8, 16, 0, 11, 4, 0, 2, 22)/63` reproduced exactly, and his Lemma 1.12 recursion agrees exactly with the chain pushforward at every `j ≤ 5`;
* its Fourier coefficients depend only on `f = j − v_3(ξ)`, the number of fine digits the frequency sees (exact, by the projection identity 1.23): maxima `0.577`, `0.378`, `0.252`, `0.177`, `0.129` for `f = 1..5`; means over the unit frequencies `0.153`, `0.085`, `0.048` at `j = 3, 4, 5`; the conditional law of the top digit given the lower `j − 1` digits is at mass-weighted mean TV `0.238`, `0.203`, `0.171`, `0.149` from uniform at `j = 2..5` (worst class `0.211` at `j = 5`) — Proposition 1.14's oscillation in one-digit form, decaying with `j` at roughly the geometric rate Remark 1.15's heuristic predicts;
* along real `64`-bit orbits at Syracuse steps `35..120` — past the `≈ 32`-step budget — the empirical law of `x_t mod 27` is at TV `0.0125` from `Syrac(Z/27)` and `0.358` from uniform (sampling noise `≈ 0.005`); mod `81`: `0.018` against `0.385` (noise `≈ 0.009`). Descriptive; not a test of AEH.

The README clause "the fair-coin behavior of 2-adic logarithm digits, empirically solid, theoretically untouched by anyone" contradicted publication.md's AEH verdict (the descent consequence is unconditional: Tao 2019 at logarithmic density, Inselmann 2024 at natural density; the unfound residue is the distributional content past the budget). It is replaced by wording consistent with that verdict.

The assessment's suspicion — that Tao's *proof*, not his theorem, delivers the letter statistics along the whole descent for almost all `N` in logarithmic density — was checked in the parallel Section 5 read and did not hold: Proposition 1.9 is applied once per fresh scale, at his (5.4), to a fresh logarithmically uniform draw on `[y, y^α]`, never to a first-passage law; the stages are glued by the stabilisation (1.20) on a single monotone event; no displayed statement concerns along-orbit pattern frequencies past the first window; and the whole-descent statement would need an argument the paper does not give (grade (c) in that read's scale). publication.md's "unfound residue" therefore stands as written. Record: `briefs/tao-section5-read-findings.md` (on `main` at `72b1a27`); the nearest mechanism is now recorded in publication.md's AEH bullet and at aeh.md 13.2 / 13.3.3.

### 3.4 The parked cycle condition is Tao's offset map evaluated mod `q`

With the dictionary block `(m_t, s_t) → (1, …, 1, 1 + s_t)` (`m_t` entries; `n = Σ m`, `K = n + Σ s`), the word `a` read from block `0` on, and Tao's `F_n(a) = Σ_(i=1)^(n) 3^(n−i) 2^(−a_[i,n])` (his eq. 1.5), the exact identity on every profile with entries `≥ 1`, no closure, either sign of `q`, is `2^(m_0) R_0 = 2^K F_n(a) + q` with `q = 2^K − 3^n` (`3,000` random profiles, `p ≤ 6`, entries `1..6`, `335` of them with `q < 0`: `0` failures). Derivation: on a cycle `R_0 = u_0 q` (cycles.md 12.6.1: `R_0 = ω_0 3^(a_(p−1)) q`, and `ω_0 3^(a_(p−1)) = u_0`, the odd seed of block `0`'s entry `e_0 = 2^(m_0) u_0 − 1`); Tao's eq. 1.7 at `x = e_0` with `Syr^n(e_0) = e_0` gives `e_0 q = 2^K F_n(a)`; substitute. As a polynomial identity in the profile it needs no closure.

The identity was already in the record under another name: it is the seam identity `N_0 + q = 2^(m_0) R_0` of Remark 12.6.1.1 (itinerary.md Lemma 14.15.9.2, integer form) with the mirror-frame numerator `N_0` of Lemma 14.15.9.1 identified as `2^K F_n(a)`. Checked directly: composing the wiki's block maps `y ↦ (3^m y + 3^m − 2^m)/2^(m+s)` over the profile gives slope `3^n/2^K` and constant term exactly `F_n(a)` on all `3,000` profiles, so `N_0 = 2^(S_P) B_P = 2^K F_n(a)`. What is new is the name and the reading, not the identity.

Consequences, all checked exactly: `q | R_0 ⟺ 2^K F_n(a) ≡ 0 (mod q)` (`2` is a unit mod `q`), agreement `3000/3000`; `x = 2^K F_n(a)/q` returns `1` from `a = (2)`, `−5` from `a = (1, 2)` (`q = −1`), `−17` from `a = (1, 1, 1, 2, 1, 1, 4)` (`q = −139`), the block dictionary word matching direct Syracuse iteration from the integer cycle in each case and `R_0 = u_0 q` holding (`u_0 = 1, −1, −1`); the `20` random profiles with `q | R_0` are all instances of the two `|q| = 1` profiles, `(m, s) = (1, 1)` (`x = 1`, `9` draws) and `(2, 1)` (`x = −5`, `11` draws); the `p = 7` staircase of 12.8.3 (`m = (4, 7, 9, 15, 23, 35, 1)`, `s = (1, 1, 1, 1, 1, 1, 49)`, `n = 94`, `K = 149`, `2^148 < 3^94 < 2^149`) fails both conditions together and has `gcd(q, R_r) = 7` at all seven rotations, as 12.6.1.6 records; 12.6.1.4's repetition factor carries over to the offset, `2^(K_P) F(a^k) = G_k · 2^(K_B) F(a)` alongside `q_P = q_B G_k` and `R_0(P) = R_0(B) G_k` (`100` `(B, k)` pairs, `k ∈ {2, 3}`).

Reading: one object, two moduli. Modulo `3^j` the same `F_n(Geom(2)^n)` is `Syrac(Z/3^j)`, fine-scale equidistributed by Tao's Proposition 1.14 — proved. Modulo `q` the parked condition asks that it not concentrate at `0`; 12.6.1.5's margin heuristic is the equidistribution-mod-`q` assumption written out. Tao's statements are modulo `3^j` and say nothing about residues modulo `q`: a naming, not a lever.

Classical attribution, verified by web search on 2026-09-04 against the EuDML record (eudml.org/doc/290184): C. Böhm, G. Sontacchi, *On the existence of cycles of given length in integer sequences like `x_(n+1) = x_n/2` if `x_n` even, and `x_(n+1) = 3x_n + 1`*, Atti della Accademia Nazionale dei Lincei, Classe di Scienze Fisiche, Matematiche e Naturali, Rendiconti (8) 64 (1978), no. 3, 260–264; Zbl 0417.10008. The brief's version of the title carries a trailing "otherwise" that the EuDML record does not; the record's form is the one used in cycles.md 12.6.1.7. Lagarias 1985 (pinned in publication.md) surveys the cycle equation and lists the known cycles.

### 3.5 No lever, no sidestep

Nothing in §3.1–3.4 moves a front. The core laws are as stated; the digit budget's heuristic is unchanged and better delimited; the statistics half's location against the literature is corrected in one README clause and otherwise as publication.md has it; the cycle condition has a classical name and a proved-mixing neighbour at the wrong modulus. Further coordinate changes are not recommended: the reduced coordinates already expose the per-step laws exactly, and the two residual questions (equidistribution past the budget; `R_0 mod q`) are not coordinate questions.

## 4. What is not claimed

* No lever and no sidestep. Every front status is unchanged: cycles parked (cycles.md 12.8.5), AEH proof effort parked (README stopping rules), the Bridge open (bridge.md §16).
* The AEH verdict (publication.md; aeh.md 13.2, 13.3.3) is untouched on this branch. The Section 5 read's negative verdict leaves it as written; nothing here anticipates or extends that read.
* The delay-line reading of 11.8.7.7 changes no theorem and no status; it delimits the organizing heuristic. The consumption identity is proved; the heuristic remains a heuristic.
* Remark 12.6.1.7 excludes nothing and proposes no route to an exclusion. Tao's fine-scale mixing is modulo `3^j`; the parked condition is modulo `q`.
* The orbit statistics in §3.3 (TV `0.0125`, `0.018`) are descriptive spot measurements at one size and one horizon, not a calibration of AEH and not evidence about any individual orbit.
* The Böhm–Sontacchi attribution is verified bibliographically; their paper was not read on this branch, and the exact form of the cycle equation they state is not quoted.

## 5. Tao's statements as read (arXiv:1909.03562v7, from the PDF)

* **Remark 1.4, p.3.** An absolute-constant bound `Col_min(N) ≤ C_0` for almost all `N` "is likely to be almost as hard to settle as the full Collatz conjecture, and out of reach of the methods of this paper"; the paper's `C_δ` grows like `exp(δ^(−O(1)))`; replacing logarithmic by natural density is called "plausible".
* **Eq. 1.5, p.5.** `F_n(a) = Σ_(m=1)^(n) 3^(n−m) 2^(−a_[m,n])`, the `n`-Syracuse offset map, `Z[1/2]`-valued. **Eq. 1.7, p.5.** `Syr^n(N) = 3^n 2^(−|a^(n)(N)|) N + F_n(a^(n)(N))`.
* **Proposition 1.9, p.6.** If `N mod 2^(n')` is within `2^(−n')` of uniform on the odd residues for some `n' ≥ (2 + c_0) n`, then `d_TV(a^(n)(N), Geom(2)^n) ≪ 2^(−c_1 n)` (eqs. 1.11–1.12). Applied in Section 5 "not to the original logarithmic distribution … but to the variant `Log(2N+1 ∩ [y, y^α])`" (pp.6–7). **Remark 1.10, p.7.** The 2-adic Haar formalism (iid `Geom(2)` valuations under Haar on the odd 2-adics), "well known", not used in the paper.
* **Proposition 1.11, pp.8–9.** Stabilisation of first passage: for `y = x^α, x^(α²)` with `α = 1.001` (1.18), `P(T_x(N_y) = +∞) ≪ x^(−c)` (1.19) and `d_TV(Pass_x(N_(x^α)), Pass_x(N_(x^(α²)))) ≪ log^(−c) x` (1.20); "(1.19), (1.20) imply that the first passage map approximately maps the distribution `ν_(x^α)` … to the distribution `ν_x`, and one can then iterate this" (p.9).
* **Eqs. 1.21–1.23, pp.9–10.** `Syr^n(N) = F_n(a^(n)(N)) mod 3^k` for `k ≤ n`; `Syrac(Z/3^n) := F_n(Geom(2)^n) mod 3^n`; `Syrac(Z/3^n) mod 3^k = Syrac(Z/3^k)`. **Lemma 1.12, p.10.** The recursion; the printed values of `Syrac(Z/3)` (`0, 1/3, 2/3`) and `Syrac(Z/9)`. **Remark 1.13, p.11.** `Syrac(Z_3)` as the projective limit and as the stationary measure of `x ↦ (3x+1)/2^a` with transition probability `2^(−a)`; footnote 4, the ancient-iteration reading (the one aeh.md 13.6.5 cites).
* **Proposition 1.14, p.11.** For `1 ≤ m ≤ n`, `Osc_(m,n)(P(Syrac(Z/3^n) = Y mod 3^n)) ≪_A m^(−A)` (1.26), with the oscillation at 3-adic scale `3^(−m)` defined by (1.27); "approximately uniformly distributed in fine-scale or high-frequency cosets" (pp.11–12). **Remark 1.15, p.12.** The heuristic: `Geom(2)^n` has entropy `log 4`, the range has cardinality `3^n`, a random-map model predicts `exp(−cm)`, "which we do not attempt to establish here". **Remark 1.16, p.12.** Upgrading to natural density "seems necessary to strengthen Proposition 1.14 by establishing a suitable fine scale mixing property of the entire random affine map `Aff_(Geom(2)^n)`, as opposed to just the offset `F_n(Geom(2)^n)`" — "plausibly attainable", not pursued.
* **Proposition 1.17, p.12.** For `n ≥ 1` and `ξ ∈ Z/3^n` not divisible by `3`, `E e^(−2πi ξ Syrac(Z/3^n)/3^n) ≪_A n^(−A)` (1.28), the implied constant uniform in `n` and `ξ`. **Remark 1.18, p.12.** Propositions 1.14 and 1.17 are equivalent (triangle inequality).

The Section 5 mechanics (where Proposition 1.9 is applied, at his (5.4)) are the parallel read's; this file quotes only its verdict (§3.3).

## 6. The terminology question (pending)

The author has raised a terminology-alignment question for the statistics half in the light of §3.3. It is recorded here as pending and not decided; no page was changed on its account, and the README clause was rewritten only for consistency with publication.md's existing verdict. The main session's recommendation will be recorded in HANDOFF.md (open work item 4) when the author decides.

## 7. Where this lands in the record

* stage4.md 11.8.7.7 — the paragraph **Calibration (delay-line reading; 2026-09-04)**, finding 3.2 with its verification line.
* bridge.md 16.2 — one pointer sentence to that paragraph.
* cycles.md — **Remark 12.6.1.7 (the rotation numerator is Tao's `n`-Syracuse offset; one object, two moduli)**, finding 3.4 with the Böhm–Sontacchi attribution and the verification line.
* README.md, "Where the difficulty actually lives", item 1 — the clause replaced (finding 3.3).
* HANDOFF.md, open work item 4 — the pointer to this file and the four scripts, the Section 5 verdict, the pending terminology decision.
* index.md — unchanged; no page's "Current state" paragraph is made wrong by the above.
