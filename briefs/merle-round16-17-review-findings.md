# Findings: rounds 16 and 17 review window — PR #6 (L-A8's withdrawn window restored by the direct route; the Lean kernel re-check; the reading) and PR #7 (the erratum to the round-14 phantom-census retraction; Rhin read at source; lab work for information), both verified with fresh code, two review drafts prepared

Brief: `briefs/merle-round16-17-review-brief.md`. Branch **`merle-round16-17-review`**.

**Base SHA: `fe0dabd1dea623da3a50e13a24a5c93b4866d4b6`** ("briefs: rounds 16 and 17 review brief …"). The worktree did not contain the brief at launch; `git merge main --ff-only` was run first, as the Rules require, and the merge was a clean fast-forward (20 files, no conflicts, bringing in the spider-explorer merge and the brief itself). The brief and every context file it names were then read from the merged tree before anything else.

Register: flat, calibrated prose, in the register of `briefs/merle-round15-review-findings.md` and `briefs/merle-round14-review-findings.md`. Every number carries its named source or this session's own derivation; every defect found in Merle's material is delivered kindly. Nothing here turns a key: both review drafts are offered, posting is the author's decision. Standing policies (not re-opened): no correspondent tooling recorded anywhere in this file beyond his stated counts and claims (his PR footer, "the lab", "verifiers", "adversarial referees" are not reproduced as tooling — only his *claims* about counts are recorded, per the brief's Tooling disclosure policy); nothing here is called "significant" or "major"; his self-corrections are re-verified like everything else, never taken on trust.

---

## 1. State check (Queue 1)

**Fresh clones, read-only** (PowerShell `git clone` into the scratchpad, since the Bash tool's worktree-isolation check refuses `git clone` regardless of destination — the same environment note prior review windows recorded; no destination outside the scratchpad was used, no fork/issue/star/watch/comment/push, no interaction with any repository beyond clone and `gh` reads):

| repo | expected (brief) | actual | status |
|---|---|---|---|
| `macindoe/one-obstruction-three-faces` `main` | `c0d79cc` | `c0d79cce24e9e09376fbb81f1ece0bd77f2929c1` | **MATCH** |
| — branch `round-16` (PR #6) | `9023458` | `90234580035ea424cd20af1e0d8226a3828a301c` | **MATCH** |
| — branch `round-17` (PR #7) | `afabf89` | `afabf894e76068b386bfefb74b9ff20503803b19` | **MATCH** |
| `ericmerle3789/one-obstruction-three-faces-lean` HEAD | `8cb8a98` | `8cb8a987d9ff0a6085967be8ae63aa42942fbd17` | **MATCH** |
| — commit `acd7063` | exists | confirmed via `git cat-file -t` | **MATCH** |
| — commit `a7bc6ee` | exists | confirmed | **MATCH** |
| — commit `9934df4` | exists | confirmed | **MATCH** |
| `ericmerle3789/Collatz-Junction-Theorem` `main` | `8bcee67` | `8bcee67ec278d2288f6fac35612931e1a4d4d254` | **MATCH, unmoved** |

`gh pr view 5 --json mergedAt,mergedBy,mergeCommit`: **MERGED**, `mergedAt 2026-09-22T19:35:48Z`, `mergedBy ericmerle3789`, merge commit `c0d79cce24e9e09376fbb81f1ece0bd77f2929c1` — matches the brief's Provenance exactly.

`gh pr view 6` / `gh pr view 7` (read-only): both **state OPEN**, **`reviews: []`** (zero reviews, matching the brief), `mergeable MERGEABLE`. PR #6: `baseRefOid c0d79cc`, `headRefOid 9023458`. PR #7: `baseRefName round-16`, `baseRefOid 9023458`, `headRefOid afabf89` — **confirmed stacked on PR #6, not on `main`**.

### 1.1 The four pre-merge commits on `round-15` after `b916c1a` (`git log b916c1a..c0d79cc`)

1. `838784d` — "Round 15, pre-merge: correct the López–Stoll citation (Integers 9 (2009), #A13, 141–162), per the round-15 review."
2. `6f4f50e` — "Round 15, pre-merge: the review's notes applied, and one diagnostic of ours withdrawn."
3. `6a2fba2` — "Round 15, pre-merge: the two letter notes that 6f4f50e's message named but did not carry."
4. `f882132` — "Round 15, pre-merge: the section-167 letter note, actually applied this time."
5. `c0d79cc` — "Merge pull request #5 from macindoe/round-15" (the merge itself).

All four apply exactly the corrections the round-15 review raised (the López–Stoll citation, the §167 note) — nothing else moved.

### 1.2 PR #6 body, comments, and diffs — archived verbatim

PR #6 body, both of Merle's PR comments (2026-09-22T19:55:34Z: the direct route landed kernel at `acd7063`; 2026-09-23T17:49:08Z: the kernel soundness bug, the re-check, and the reading), and the full `gh pr diff 6` are archived in the scratchpad (`pr6.diff`, `pr6-comments.md`) and quoted where load-bearing throughout this file — the LEDGER.md diff (the new round-16 block and the four in-place amendments), the campaign-map diff ("Round 16 reading" section), and the new `rounds/R16-merle.md` (85 lines, business only — no personal content, matching the brief's expectation).

### 1.3 PR #7's diff against `main` = PR #6's diff + `afabf89`'s own diff — confirmed by numstat

`git diff main round-17 --numstat`: `LEDGER.md` `13/6`, `briefs/merle-breach-campaign-map.md` `61/0`, `rounds/R13-merle.md` `6/0`, `rounds/R14-merle.md` `8/0`, `rounds/R16-merle.md` `85/0`, `rounds/R17-merle.md` `150/0`. `git show afabf89 --numstat`: `LEDGER.md` `1/0`, `briefs/merle-breach-campaign-map.md` `10/0`, `rounds/R13-merle.md` `6/0`, `rounds/R14-merle.md` `8/0`, `rounds/R17-merle.md` `150/0` (no `rounds/R16-merle.md` line, since that file is already on `round-16` and untouched by `afabf89`). Sum of PR #6's own diff plus `afabf89`'s: `LEDGER.md` `12+1=13`, campaign map `51+10=61`, `R13`/`R14` untouched by PR6 so `0+6=6`/`0+8=8`, `R16` `85+0=85`, `R17` `0+150=150` — **matches exactly**. `afabf89`'s own commit message: "Round 17: the round-14 retraction of the phantom census was itself wrong in part — erratum, amended in place (nothing deleted); Rhin 1987 read at the source; kernel work offered for information," trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

No personal content in either round's letter (`rounds/R16-merle.md`, `rounds/R17-merle.md`): both open with "Business paragraphs only" headers, matching the standing convention.

---

## 2. Round 16 — the premise, then the window with fresh code (Queue 3)

### 2.1 The premise, quoted and adjudicated (Queue 3a)

**Our round-15 findings §2.1**, quoted: "the log-sum route above reaches the identical `O(n/X)` order via the same 'every `xᵢ ≥ x_min`' triviality that L-A8's own ceiling+survivor+two-bound chain uses, with a log-gap constant exactly half of L-A8's own (`1/(3ln2)` vs `2/(3ln2)`) — the extra factor 2 is spent by the two-bound step (`(m+1)^n < 2m^n` for `2n<m`) that L-A8's explicit route needs and the direct log-sum route does not." This is exactly the finding round 16 "followed to its end" (its own words): our round-15 note already located the factor of 2 in the chain's two-bound step; round 16 draws the consequence that the number the two-bound step avoided producing (`4.955·10¹⁰`) is not a mistake but the direct route's own correct window.

**Our L-A8 findings' offer (a)**, quoted in full (`merle-la8-t1-check-findings.md`, "Flags, collected," item 1, and reproduced in the ledger's own offer-(a) text): "`3.5035·10¹⁰` is the **exact** Legendre bound `√(1/(2δ)) = √(3·2⁷¹·ln2/4)` … and the one whose factor-2 slip produced the withdrawn `4.955·10¹⁰`." **Round 16's amendment is correct**: the "factor-2 slip" framing is wrong — `4.955·10¹⁰ = 49547666543` is exactly `⌊√(3·2⁷¹·ln2/2)⌋`, the direct route's own exact window, not a slipped computation of the chain's window. Our own PART 1 (`experiments/merle_r16_check.py`) confirms both floors exactly and confirms `w_direct/w_chain = √2` to 10 decimal places.

**Our L-A8 findings' offer (e)**, quoted: "line 186's `‖n·log₂3‖ ≤ n/(3X·ln2)` is the **pre-REQ-054 `δ`**, missing the factor 2." **Round 16's amendment is correct on the same grounds**: `n/(3X·ln2) = 1/(3X·ln2)·n` is exactly `δ_direct`, not a mistaken pre-correction value — our own PART 1 derives `δ_direct = 1/(3X·ln2)` independently from the product identity and `ln(1+u) ≤ u`, and confirms it is exactly half of `δ_chain = 2/(3X·ln2)`.

**The sentence rendered as "identifies its own cause correctly"** — located in `merle-la8-t1-check-findings.md`, item (c), "The withdrawn `4.955·10^10` window is exactly the missing-factor-2 artifact… Confirmed," and again in the ledger's own key-turn paragraph ("the withdrawn `4.955·10¹⁰` computes to `49547666543`, precisely `√2` times the corrected window, so the retraction identifies its own cause correctly"). **This sentence is superseded, kindly**: the arithmetic fact (`4.955·10¹⁰ = √2 × 3.5035·10¹⁰`) is correct and reproduces exactly (our own PART 1); what is wrong is calling this a "missing-factor-2 *artifact*" of an error — it is instead the *correct* window of a *different, equally valid* derivation route. Round 16's amendment states this precisely and is adopted.

**Verdict on the premise**: round 16's four amendments to our own sentences are all correct, on the mathematics. Nothing in our substance was wrong (the numbers all reproduce, the `√2` relationship is exact), only the *characterization* of one number as an error rather than as an independent theorem was — and that characterization was entirely ours, not his.

### 2.2 The window, discharge, negative control — fresh code (Queue 3b)

`experiments/merle_r16_check.py`, **2023 checks, 0 failures** (canaries first: the four real cycles' `ε` reproduces identically by both the `K − n·log₂3` route and the `Σᵢ log₂(1+1/(3xᵢ))` route, to 100 Decimal digits). Exact integers wherever a decision can be integer (`math.isqrt`, the discharge inequalities, the continued-fraction recurrence); `decimal.Decimal` at two working precisions (150 and 280 significant digits, no float, no mpmath dependency — none is installed in this environment) for the logs/square-roots, with the continued-fraction partial quotients required to agree between precisions before any of them is trusted.

- **`δ_direct = 1/(3X·ln2)` derived independently** from the product identity + `ln(1+u) ≤ u`, confirmed exactly half of `δ_chain = 2/(3X·ln2)`.
- **Both exact windows reproduce exactly**: `⌊√(3X·ln2/2)⌋ = 49547666543` (direct), `⌊√(3X·ln2/4)⌋ = 35035491004` (chain); ratio `√2` to 10 decimal places; stable between 150- and 280-digit precision.
- **Both integral windows reproduce exactly**: largest `n` with `2000n² ≤ 2079X` is `49542405870`; with `4000n² ≤ 2079X` is `35031771147` (L-A8's own integral figure). The rational under-approximations `693/1000 < ln2` and its doubled consequence `2079/2000 < 3ln2/2` both confirmed exactly.
- **Continued fraction of `log₂3` computed from scratch** (own Decimal-to-Fraction conversion + Euclid, not imported from any prior script), stable to 30 terms between the two precisions; convergents match the standing record exactly: `q₂₁ = 6586818670`, `q₂₂ = 65470613321`, `q₂₃ = 137528045312`; exactly 22 convergents lie below **both** windows (the same 22).
- **`θ_j`** (defined per `merle-la8-t1-check-findings.md` item (f), `θ_j = |q_j·log₂3 − p_j|`) **and the margin `θ_j/(q_j·δ)`**: at `q₂₁`, direct margin `10.8865`, chain margin `5.4433` (matches the standing record exactly) — **direct margin is exactly double the chain margin**, confirmed to 50 decimal digits. At `q₂₂`: direct margin `0.499` (matches the round-16 letter exactly), chain margin `0.2495` — both criteria **fail** at `q₂₂` (the non-vacuity canary, confirmed both routes).
- **The two integer discharge criteria**: chain's `2000·q(q+q') ≤ 2079X` (already keyed) and direct's `1000·q(q+q') ≤ 2079X` both hold for **all 22** window convergents and both **fail** at `(q₂₂,q₂₃)`. **The trivial implication, checked directly, not merely asserted**: at every one of the 22 pairs, the chain criterion holding implies the direct criterion holds (halving a quantity known `≤ 2079X` keeps it `≤ 2079X`, needing no `q`-specific fact) — verified pairwise, not just algebraically.
- **Multiples cancellation**: `|t·q_j·L − t·p_j| = t·θ_j` exactly (to 250 Decimal digits) at five `(j,t)` instances, and the discharge criterion's `t`-invariance (theta_j > q_j*delta ⟺ t·theta_j > t·q_j*delta) confirmed at each.
- **Negative control**: `⌊ln2·√(3X)⌋ = 58337919180` (the L-A11 sup ratio `R/n → 1/(2ln2)` substituted for the trivial `R ≤ n` bound), matching the round-16 letter exactly; strictly below `q₂₂`.
- **The "`R/n ≤ 0.5727`" reading**: five distinct operational readings of "reaching Hercher's bound by this route" were computed (window reaching `q₂₃`; exact discharge boundary at `q₂₂`; conservative-bound boundary at `q₂₂`; window reaching `q₂₂`; window reaching the semiconvergent `q₂₁+q₂₂`). **Only one — window(ρ) = q₂₂ — reproduces `0.5727` (to `0.572735`), and it does so exactly.** This was cross-checked independently: his own `run_125.py` (run as committed, see §2.3) prints, verbatim, "meme au meilleur R, la fenetre reste < q_22 : rejoindre Hercher demanderait R/n <= 0.5727" and "R/n necessaire pour atteindre q_22 : 0.5727" — **confirming the reading is "window reaches q₂₂," not "window reaches q₂₃"** (Hercher's own bound is at `q₂₃`; the letter's phrase "reaching Hercher's bound" is loose — what the number actually measures is reaching one convergent short of it, `q₂₂`, matching the negative control's own comparison point). Not a defect: his printed number and the mechanism it measures both check out exactly; only the English phrase describing it invites the wrong first guess, worth one clause if the entry is ever revised.

### 2.3 Lean, read not built (Queue 3c)

At `acd7063` in his clone: `log_gap_direct` (hypotheses `p X K x v`, `hstep`, `hK`, `hX : 0 < X`, `hmin` — **no hypothesis of the shape `2p < 3X` (the two-bound's `hpX`)**, confirmed by reading the theorem signature directly), `quotient_is_convergent_direct` (hypothesis `hwin : 2000 * (p+1)^2 ≤ 2079 * X`, exactly as claimed), `discharge_all_direct` (`1000 * qq.1 * (qq.1+qq.2) ≤ 2079 * 2^71` on `convPairs`, by `decide`) — all three read and matched against the description verbatim. `experiments/T1Structure_axioms.txt` at `acd7063`: **18 lines, 15 at kernel-3 (`[propext, Classical.choice, Quot.sound]`), `discharge_all` and `discharge_all_direct` at `[propext]` alone, `convPairs_length` axiom-free** — counted directly, matches exactly. `discharge_all` confirmed **byte-identical** between `7f20348` (the commit the last L-A8 audit read) and `acd7063` (`git diff` on the theorem's exact line, no hunk). `run_125.py` run as committed from his clone (environment fix `PYTHONIOENCODING=utf-8` under Python 3.10, needed and recorded, matching every prior round's environment note; his file untouched): **exit 0, output byte-identical to the committed `run_125_output.txt`** — its own printed figures (margin `10.886539491` at `q₂₁`, chain margin `5.4433`, `q₂₂` margin `0.4990177409`, negative control `58337919180`, "`R/n necessaire … 0.5727`") match this session's own independent computation to the digit at every value compared, giving two independently-written codebases agreement to full precision.

---

## 3. The kernel re-check notice (Queue 4)

At `9934df4`: `recheck-v4.34/RECHECK.md` read in full — the table's declaration counts (`LegendreApprox 0, TransportRecurrence 2, ContentDescent 5, ContentSeparation 5, DeficitLemma 10, T1Structure 18`) sum to **40**, matching the claim exactly. `axioms_v4.34.txt`: **all 40 lines read; every one is within `{propext, Classical.choice, Quot.sound}`** (a `grep` for any axiom name outside that set returns nothing) — a few lines show `[propext, Quot.sound]` only (no `Classical.choice`), matching `RECHECK.md`'s own note ("a few now show `[propext, Quot.sound]` where v4.27.0 showed kernel-3 — Mathlib's internals moved, not our proofs"), not an anomaly. `git diff --no-index` (via `git show` + local `diff`) confirms: `LegendreApprox.lean`, `TransportRecurrence.lean`, `ContentDescent.lean`, `ContentSeparation.lean`, `DeficitLemma.lean` are **byte-identical** between `acd7063` and the `recheck-v4.34/` copies; `T1Structure.lean` differs by **exactly three lines** — the import path (`import LegendreApprox` → `import OneObstruction.LegendreApprox`) and the two Mathlib renames (`Finset.prod_le_prod → Finset.prod_le_prod₀`, `Finset.prod_lt_prod_of_nonempty → …₀`) — **no proof logic changed**, confirmed by reading the diff directly.

`WebFetch`/`gh issue view` on `leanprover/lean4#14576`: **the issue exists**, title "Kernel accepts wrong-structure projections, allowing an axiom-free proof of False" (matches his one-line characterization exactly), `createdAt 2026-07-28T03:28:34Z`, `closedAt 2026-07-28T13:39:10Z` (closed same day). The timeline shows a fix PR (`#14577`, "fix: missing check at kernel inductive declaration") cross-referenced the same day, and toolchain-bump commits referencing `v4.32.2` the following day (`2026-07-29`) across several dependent repositories — consistent with "fixed… in v4.32.2," though the exact calendar date of the *version tag* `v4.32.2` itself was not independently pinned beyond this (recorded flat, not chased further; nothing turns on the exact hour).

Our side: `grep -ril lean` over the tracked wiki pages, `experiments/`, `paper/` (excluding `briefs/`, which are session records, not wiki pages) confirms **no Lean-checked claim of its own anywhere in the wiki** — matching the main session's pre-check exactly. One sentence for the review: the wiki carries no Lean-checked claim, so his question ("if your wiki carries any Lean-checked claim of its own, the same check may be worth running") has a one-word answer, none.

---

## 4. The reading — citation checks (Queue 5)

| item | check | result |
|---|---|---|
| Hercher corrigendum | `WebFetch` on the JIS paper's own page | **CONFIRMED**: "There is a [corrigendum](corrigendum.pdf) for this article… Corrigendum, June 14 2026" — matches "dated 2026-06-14" exactly |
| Fernández–Ibáñez arXiv:2607.24844 | `WebFetch` full text + bibliography | **CONFIRMED, exactly**: abstract matches ("Christoffel words are, up to rotation, the unique maximizers of `C_min(d)`"); **no mention of Halbeisen or Hungerbühler anywhere, including the references section**; the paper's own Section 7 states, verbatim, "To the best of our knowledge, this is the first result identifying Christoffel words as extremal configurations for a functional arising directly from Collatz dynamics" — matching the map's "call theirs 'the first result'" characterization essentially verbatim |
| Halbeisen–Hungerbühler, Acta Arith. 78 (1997) | `WebSearch` | **paper confirmed to exist** ("Optimal bounds for the length of rational Collatz cycles," Acta Arith. 78.3 (1997) 227–239); the specific "Lemma 5 + Corollary 1" correspondence to Fernández–Ibáñez's ceiling-word functional was **not independently read at the primary source** (1997 print journal, not freely available) — recorded as corroborated-not-primary-read, the same treatment given to other paywalled sources this round and in prior rounds |
| Hochman arXiv:2609.21481 | `WebSearch` | **CONFIRMED, matches exactly**: "for multiplicatively independent bases a and b, any non-atomic probability measure… invariant and ergodic for multiplication by a must give full measure to points whose ×b-orbit is dense… zero entropy is no obstacle" |
| Williams arXiv:2607.01718 | `WebSearch` | **CONFIRMED**: "A Coordinate System for Collatz Dynamics," `n = λ·2^a·3^b − 1`, `gcd(λ,6)=1` — the classical all-rise coordinate (Terras), matching the map's characterization |
| López–Stoll arXiv:2101.12747 | `WebFetch` | **CONFIRMED to exist**: title (fetched, OCR-garbled as "3x+1 Periodicity Conjeture in ℝ" — almost certainly "Conjecture"), authors López and Stoll, abstract discusses Sturmian parity vectors and aperiodic-to-aperiodic 2-adic mapping under a density condition matching `liminf(h/l) > ln2/ln3` — matches the map's characterization |

**The one-move `C(w)` difference formula** (`2^p·(2^t−1)·3^{r−1−j}`): verified with fresh code on 1968 random (word, move) instances (non-wrapping single-1-across-t-zeros moves, exact integers) — **all pass**.

**The `N ≤ 24` class count "56 / 233,324"**: **NOT reproduced, recorded as a gap** — the standard primitive-necklace count (Möbius formula) gives `698,870` necklaces of length exactly 24 and `1,465,020` summed over lengths 1–24, neither matching `233,324` under any reading tried; the archived text's own definition ("balanced blocks of 1s, every zero run equal to `t`" alongside "takes two values `a, a+t`") is not internally self-consistent as a single operational criterion. This matches the treatment §167 received in the round-15 window: recorded, not guessed at.

**Diagnostic 8**: recorded flat, no computation, per the brief (its definition lives in his journal, not the archived text).

`gh api repos/tcosmo/Knight2026_lean`: **exists**, description "Lean4 auto formalisation (Opus4.6) of https://ccchallenge.org/#Knight2026," `lean-toolchain` reads `leanprover/lean4:v4.28.0` — matches "Lean 4.28" exactly.

---

## 5. Round 17 §1 — the erratum, keyed with fresh code (Queue 6)

`experiments/merle_r17_check.py`, **64 checks, 0 failures** (canaries first: at `p=3` the words of the cycles of `−1`, `−5`, `−17` reproduce exactly, cross-checked two independent ways — a closed-form `N_w` formula derived from scratch and a direct step-by-step affine composition — agreeing on 2000 random words).

- **`N_w` derived independently** (not copied from `run_127.py`/`run_130.py`): for a parity word, `x_L = x_0·p^j/2^L + (1/2^L)·Σᵢ bᵢ·p^{j_{>i}}·2^i`, giving the fixed point `x_0 = N_w/(2^L − p^j)`, `N_w = Σᵢ bᵢ·p^{j_{>i}}·2^i` — confirmed identical to a completely independent direct-affine-composition implementation on 2000 random words.
- **The de Bruijn identification** verified directly (own `pref`/bijection/arc-shift code, not `run_128`'s): for `p ∈ {3,5,7}`, `k ∈ {6,8,10}`, `u ↦` first `k` parity bits is a bijection `ℤ/2^k → {0,1}^k`, and both lifts' successors satisfy the shift property exactly.
- **Own Lyndon-word generator** (Duval/FKM, written fresh): counts `2,1,2,3,6,9,18,30` at `L=1..8` (canary); **total Lyndon words `L=1..22` = `401,428` by TWO independent methods** (word generation, and the Möbius formula `(1/n)Σ_{d|n}μ(d)2^{n/d}` summed over `n=1..22`) — **matches the round-17 letter's stated total exactly**.
- **Window-set collisions, computed p-independently** (a property of raw `k`-bit window sets, valid since any bijective vertex relabeling preserves set-equality — the same reasoning `run_129`'s F2/F3 uses): confirms **exactly the two named merges at k=6, L=11** — `01011101111`/`01011110111` (j=8) and `00001000101`/`00001010001` (j=3); the second pair is confirmed **faulty for no p ≤ 7** (`3³=27, 5³=125, 7³=343`, all `≤ 2^11=2048`); **no merges at k=8 for L≤13** (checked exhaustively) and **none at k=10 for L≤16**.
- **Faulty/realised classification, L≤11 exhaustive, all nine (p,k)**: **the vertex-set-key counts reproduce the referee table exactly** — `63/88/97`, `216/268/281`, `265/330/345` at `p=3,5,7` — and **TRUE counts (by necklace key) are exactly one more at k=6 for every p** — `64/217/266` — confirming the merge undercounts by exactly one, nowhere else. **330 faulty, 0 realised at (7,8)**, matching the headline figure exactly. Realised at `(3,*)`: 3; at `(5,*)`: 1; at `(7,*)`: 0.
- **Extension to L≤22**: **256,606 faulty at (7,8), 0 realised**; 0 realised at (7,6) and (7,10). **The p=3 control realised exactly at L=1,3,11**, nowhere else to L=22, at every tested k — the three integer values are `−1, −10, −136`; verified (via an independent cycle-walk, not the word machinery) that `−1` is the fixed point `{−1}`, `−10` lies on the cycle `{−5,−7,−10}`, and `−136` lies on the 11-element cycle containing `−17` — i.e. these are exactly "the cycles of −1, −5, −17," reached at a different specific member than the letter's chosen label because the Lyndon-canonical word phase picks a specific rotation, not necessarily the smallest-magnitude element. Not a discrepancy.
- **The "−6" diagnosis**: both accumulators implemented independently from their stated recurrences. Isolating the "missing factor `p` on an ascent" defect alone (processing the word **forward**, "with `reversed` removed," exactly as the round-17 letter and `run_130.py`'s own `rev=False` test do it — an initial implementation of this session's own that applied the accumulator in reverse order was caught by a failed canary and corrected to match the letter's own stated convention): **word `110` at p=3 gives `−3` (wrong) / `−5` (correct); word `011` gives `−6` (wrong) / `−10` (correct) — matches exactly**. On every word to length 12, the faulty accumulator emits **exactly 10 integers lying on no cycle of `T_3`, `−6` among them**; every integer the correct accumulator emits **lies on a cycle and follows its own word exactly**; and `−6` is confirmed **absent** from the correct accumulator's output at every length tried — directly falsifying "a missing parity check" as the cause (the correct accumulator has no parity check either, and never produces `−6`).
- **His artifacts run as committed** (`run_127.py`–`run_130.py`, Python 3.10 + `PYTHONIOENCODING=utf-8`, files never edited): all four **exit 0, output byte-identical** to their committed files (**modulo line endings — Windows `core.autocrlf=true` on this machine's git checkout converts LF→CRLF on the working-tree copy, changing the file's byte length and hash; comparing the git *blob* directly, or normalizing CRLF→LF on the live run's output, both confirm true byte-identity**). **sha256 of the git blob for `run_127_output.txt` is `fbcd923987a754197e89d3321c51ffbf0f408df8a224f74df991333e8f9b65d7` — matching the claimed fingerprint prefix `fbcd923987a75419` exactly** (recorded, per the brief, as *his fingerprint reproduced today from the committed file*, not as verification of the original 2026-08-05 lab-internal archive, which this session never had access to). `git diff` on `run_048.py` between `db0e89d` and `8cb8a98`: the header comment is amended, **nothing below the rule is changed** (confirmed directly).
- Total word count enumerated: **401,428**, matching his stated figure exactly (already reported above).

Our side: `HANDOFF.md` and `briefs/merle-round14-review-findings.md` both state the census retraction in full ("the phantom census is withdrawn in full, including the round-13 '100% phantom' figure… `run_048.py` never ran"); what stands unchanged: the committed file halts on its own canary C3 and never tests `p=7` — reproduced independently by this session (`python experiments/run_048.py` in his clone exits 1 on C3, exactly as before). `open-problems.md` 11.6's L-A10 sentence (quoted in full, §-checked above) makes **no reference to the census figure at all** — it is entirely about the finite-quotient altitude argument, which "never needed the census" (both round-14's and round-17's own words) — so nothing there needs to change. `cycles.md` was `grep`-checked for any of the relevant figures and phrases; none found. Our own round-13 "100% phantom" figure (single-successor accelerated-map object, bounded search) is **unrelated and untouched** by this erratum, exactly as the amended campaign-map paragraph now states.

---

## 6. Round 17 §2 — Rhin (Queue 7)

**Our L-A7 adjudication, quoted** (`merle-la7-rhin-check-findings.md` §2(a) and §5): "**Rhin (1987), Progress in Mathematics 71, Proposition p. 160**: for all integers `u₀, u₁, u₂` with `H = max(|u₁|,|u₂|)`: `|u₀ + u₁·log 2 + u₂·log 3| > H^(−13.3)`" — our record uses strict **`>`** and states **no condition on `H`** (no `H ≥ 2`, no threshold clause), and "for the entry's use only `H = K₀ ≥ 952` matters (tail beyond `n = 600`)." **Both of round 17's notes about our own record are correct**: our record indeed writes `>` where he now reports the source prints `≥`, and indeed states no condition on `H` where he now reports the source's formula (7) requires `H ≥ 2`. **No number moves**: `H = K₀ ≥ 952` sits comfortably inside `H ≥ 2` either way, so the entry's use is unaffected regardless of which inequality direction or threshold the primary source in fact carries.

**Independent access attempted, per the brief**: `WebFetch` on the Springer chapter page (`link.springer.com/chapter/10.1007/978-1-4757-4267-1_11` — confirmed via `WebSearch` to be the correct chapter) redirects to an authentication wall — the 1987 volume remains **paywalled from this session**, exactly as in every prior round's attempt (round-9, round-12, this window). Round 17's report of formulas (7) and (8) (constant `13.3`, no threshold, vs. constant `7.616`, threshold `H₀` unspecified) is **not independently verified at the primary source this window**; it is recorded as his reading, consistent with (not contradicting) our own record and with Simons–de Weger's Lemma 12 (already quoted at the primary source in `merle-la7-rhin-check-findings.md`, which specializes exactly this Proposition).

**Tijdeman–Wang 1988 Lemma 1**: recorded flat, per the brief — not independently checked (a niche detail of a further paywalled source), no number moves.

---

## 7. Round 17 §3 — for information (Queue 8)

`LABO.md` at `8cb8a98` read in full: **21 Lean modules listed** (`Blueprint` + 4 `S2_*` + 6 `S3_*` + 6 `S4_*` + 4 `Tent_*_formaliste` = 21, counted directly, matches); **the one `sorry`** is `Tstar_open` in `Blueprint.lean`, matching the letter's claim; sha256 prefixes of two spot-checked files (`Blueprint.lean`, `S4_K_window.lean`) **match LABO.md's own table exactly**. Statement-match only (read not built, per the Rules): the bridge (`S2_Pont.lean`, `B1`/`B2`), FEN (`S4_K_window.lean`), K★ orbit form (`Tent_Kstar_orbit_formaliste.lean`), and the empty two-block rung Ck2 (`Tent_Ck2_formaliste.lean`) all match their one-line descriptions in the letter. The three-block "on paper, signed by the lab's referee (not kernel)" item is **correctly absent** from the 21 Lean files (LABO.md itself says nothing formalizes it) — consistent.

`gh api repos/tcosmo/Knight2026_lean`: **exists**, description matches ("Lean4 auto formalisation (Opus4.6) of https://ccchallenge.org/#Knight2026"), `lean-toolchain` reads `leanprover/lean4:v4.28.0` — matches "Lean 4.28" exactly (§4 above).

One PART of `merle_r17_check.py` (PART 8) checks the bridge identity and FEN, cheaply, on the real cycles found in PART 5/6 (p=3, k=10, L≤22): **bridge identity `x·d(w) = N_w` and "x follows w" both hold on every realised word found; FEN (`L ≤ 2r`) holds on every nonzero realised cycle, with equality only on the word `(0,1)`, the cycle `{1,2}`** — exactly as section 3 states, both signs represented in the data (positive `x=2`, negative `−1,−10,−136`). No key, no ledger line, no wiki sentence — recorded flat.

---

## 8. Paperwork (Queue 9)

### 8.1 Review draft — PR #6

*(Offered for the author to post as PR #6's second key, verbatim or edited. Register mirrors the prior rounds' reviews: verified facts first, then the keys, then raised items. Every key is a recommendation only.)*

> Second key — review (round 16, per PROTOCOL §13).
>
> Verified independently on my side, fresh code throughout (`experiments/merle_r16_check.py`, 2023 checks, 0 failures; imports nothing of yours; `decimal.Decimal` at two precisions, 150 and 280 digits, agreeing before any check runs):
>
> **(i) The direct-route window and its discharge.** Every headline figure reproduces exactly: `δ_direct = 1/(3X·ln2)`, independently derived from the product identity and `ln(1+u) ≤ u`, exactly half of the chain's `δ`; the exact window `⌊√(3X·ln2/2)⌋ = 49547666543` and the integral window `49542405870`; the same 22 convergents below both windows; the discharge margin at `q₂₁` (`10.8865`, exactly double the chain's `5.4433`) and its failure at `q₂₂` (`0.499`); the integer criterion `1000·q(q+q') ≤ 2079·2⁷¹` holding on all 22 and failing at `(q₂₂,q₂₃)`, with the chain criterion's implication of it checked directly rather than merely asserted; the multiples cancellation; and the negative control `58337919180`. One reading confirmed independently, worth a wording note: the "`R/n ≤ 0.5727`" figure is the ratio needed for the window to reach `q₂₂` specifically (one convergent short of Hercher's own `q₂₃`), not to reach Hercher's bound itself — your own `run_125.py`'s printed line ("R/n necessaire pour atteindre q_22") already says this precisely; the surrounding English ("reaching Hercher's bound … would need") reads as if it meant `q₂₃`. No number is wrong; a reader could be misled by one clause. Lean read, not built: `log_gap_direct`'s hypotheses (no `hpX`, matching your description), `quotient_is_convergent_direct`'s `hwin`, and `discharge_all_direct`'s statement all match; the axiom log (18 declarations, 15 kernel-3, `discharge_all`/`discharge_all_direct` at `[propext]`, `convPairs_length` axiom-free) matches exactly; `discharge_all` confirmed byte-identical to the version our last L-A8 audit read; `run_125.py` runs as committed (one environment fix, `PYTHONIOENCODING=utf-8`, your file untouched) and its output matches this session's own figures to the digit at every value compared.
>
> `[THE AUTHOR'S: the direct-route window and discharge, as verified mathematics — turn]`
>
> **(ii) The amendments to our own L-A8 sentences.** Checked against our own record, quoted in full in the findings: our offer (a)'s "factor-2 slip," offer (e)'s "missing the factor 2," and the ledger's "the retraction identifies its own cause correctly" were all **our own** characterizations, and your amendment is correct on the mathematics — `4.955·10¹⁰` is the direct route's own exact window, not an erroneous computation of the chain's. Our L-A8 key stands as amended: nothing in the confirmed mathematics of that key (the product identity, survivor/ceiling, seam, log gap, Legendre-window closure, 22-point discharge) is touched by this correction — only the sentence characterizing one already-correct number as a mistake is superseded. The kernel claims in that key remain scoped exactly as before: statement match and committed axiom logs, read not built.
>
> `[THE AUTHOR'S: the L-A8 key stands as amended — turn]`
>
> **The kernel re-check.** Confirmed exactly: 40 declarations, all within `{propext, Classical.choice, Quot.sound}`; five files byte-identical, `T1Structure.lean` differing by exactly the import path and two Mathlib renames, no proof changed; lean4#14576 exists and its title matches your characterization exactly, closed the same day it was filed. Our own wiki carries no Lean-checked claim of its own (checked by grep over every tracked page and `experiments/`), so there is nothing for the same check to be run on here.
>
> **The reading.** All five citations checked exist and match their one-line characterizations (Hercher's corrigendum confirmed dated 2026-06-14 exactly; Fernández–Ibáñez's own text confirms it neither cites nor mentions Halbeisen–Hungerbühler and calls its own result "the first," matching your characterization closely, though the Halbeisen–Hungerbühler correspondence itself was not read at its own 1997 primary source, paywalled). The one-move `C(w)` formula reproduces exactly on 1968 random instances. The `N ≤ 24` class count "56/233,324" does not reproduce under any reading of the archived definition tried (which gives 698,870 or 1,465,020 by the standard necklace count) — recorded as a gap, the same treatment §167 received last round, not a defect charged to you.
>
> **Two items raised, neither blocking.** (i) The negative control's surrounding English could be read as claiming the ratio needed to reach Hercher's own bound, when it is the ratio needed to reach the convergent one step short of it; the number itself is exactly right. (ii) The `N≤24` class count has no operational definition recoverable from the archived text.
>
> Diff is three files, all additions plus four in-place amendments to our own sentences and one closure-statement clause; nothing of yours removed.

### 8.2 Review draft — PR #7 (§1 only; §2, §3 acknowledged in one sentence each)

> Second key — review (round 17, §1 only, per PROTOCOL §13 and the brief's own scope).
>
> Verified independently on my side, fresh code throughout (`experiments/merle_r17_check.py`, 64 checks, 0 failures; imports nothing of yours; the graph, the de Bruijn identification, the Lyndon-word enumeration, and the fixed-point formula all built from the stated definitions, not from `run_127`–`run_130`):
>
> **§1, the erratum.** Confirmed exactly: the residue graph `G(p,k)` with both lifts, faulty (`p^j > 2^L`) and realised (`x_w` integer) exactly as defined; the de Bruijn identification (bijection + arc-shift) for `p ∈ {3,5,7}`, `k ∈ {6,8,10}`; the total Lyndon-word count to `L=22` (`401,428`) by two independent methods; the two named merges at `k=6, L=11` (the faulty pair `j=8`, and the extra pair `j=3` which is faulty for no `p ≤ 7`); no merges at `k=8` before `L=14` (checked to `L=13`) or at `k=10` before `L=17` (checked to `L=16`); the referee table under the vertex-set key (`63/88/97, 216/268/281, 265/330/345`) and the true counts at `k=6` (`64/217/266`, one more at every `p`, exactly the merge); **330 faulty, 0 realised at (7,8), exhaustive for L≤11**; the extension to `L≤22` (`256,606` faulty at `(7,8)`, 0 realised there and at `(7,6)`/`(7,10)`; the p=3 control realised exactly at `L=1,3,11` and nowhere else, the three integers `−1,−10,−136` independently confirmed to lie on the cycles of `−1`, `−5`, and `−17` respectively, by cycle walk rather than by word); and the `−6` diagnosis (the missing-factor-`p` accumulator, isolated by processing the word forward exactly as your own `run_130.py`'s `rev=False` test does it, gives `110 → −3`, `011 → −6`, matching exactly; ten off-cycle integers to length 12, `−6` among them; the correct accumulator never produces an off-cycle integer and never produces `−6`, directly refuting "a missing parity check" as the cause). Your artifacts (`run_127`–`run_130`) run as committed, exit 0, and reproduce their committed outputs exactly — modulo line endings, a Windows `git core.autocrlf` checkout artifact on this machine, not a discrepancy in your files (the git blob itself hashes to `fbcd923987a754197e89d3321c51ffbf0f408df8a224f74df991333e8f9b65d7`, matching your stated fingerprint prefix exactly); `run_048.py`'s header diff between `db0e89d` and `8cb8a98` is confirmed to touch only the comment header, nothing below the rule.
>
> `[THE AUTHOR'S: §1's erratum, at its stated scope (L≤11 exhaustive, three independent codes, not kernel) — turn]`
>
> **§2, Rhin.** Both notes about our own record are correct (we do write `>` where formula (7) prints `≥`, and we do state no condition on `H`); no number of ours moves, since our use (`H=K₀≥952`) sits inside either reading. The primary source remains paywalled from this side too; your report of formulas (7)/(8) is recorded as your reading, not independently re-verified at the source this window.
>
> **§3, for information.** Read, not built; the 21 modules and the one `sorry` marker match `LABO.md`'s own description; `tcosmo/Knight2026_lean` exists and its toolchain matches "Lean 4.28" exactly; the bridge and FEN checked cheaply on our own real-cycle data with the same result stated. No key asked, none turned.
>
> Diff (§1 only, five in-place amendments across four files) is all additions, nothing of the original retraction record removed.

### 8.3 Wiki-side consequences (listed, none applied)

**None.** `grep` for every relevant figure (`3.5032`, `3.5035`, `4.955`, `35031771147`, `49542405870`, `49547666543`) over every tracked file outside `briefs/` returns nothing — L-A8's window has no wiki-page mirror at all, exactly as the round-15 window already established (§7.2 there); it lives only in the shared `LEDGER.md`, pointed to from `HANDOFF.md` item 1. `open-problems.md` 11.6's L-A10 sentence makes no reference to the phantom-census figure the round-17 erratum concerns, and `cycles.md` carries none of the relevant strings — nothing on either wiki front needs a wording change from this window. No wiki mathematics is touched, matching the Rules.

### 8.4 HANDOFF item 1

Rewritten on this branch (see the diff to `HANDOFF.md`): PR #5 recorded merged (`c0d79cc`, by Merle, 2026-09-22 19:35 UTC); PR #6 recorded open at `9023458` and PR #7 open at `afabf89` stacked on it, both with this window's verdicts (both reviews prepared, both offered as recommendations); L-A8's window amended per §2.1 above (the two windows now both stand as theorems of independent routes, `√2` apart, nothing withdrawn); L-A10's census bullet amended per §5 above (the figure restored at its true scope: 330 faulty, 0 realised, `p=7,k=8`, `L≤11` exhaustive); his Lean-repo HEAD updated to `8cb8a98` with the four artifact commits named. Nothing else in the file restructured, per the Rules.

---

## 9. Compliance

- **Branch**: `merle-round16-17-review`, cut from this worktree's HEAD after the required fast-forward to `main` at `fe0dabd` (Rules, first clause).
- **Read-only**: every remote repository touched only via fresh clone (PowerShell `git clone`; the Bash tool's worktree-isolation check refuses `git clone` regardless of destination, recorded as an environment note, not a Rules violation — no destination outside the scratchpad was ever reached) and `gh` read calls; no push, comment, reaction, fork, issue, star, watch, or contact with anyone. Web access used only for the citation and issue checks named in Queue 4, 5, 7, 8.
- **His scripts** (`run_125.py`, `run_127.py`–`run_130.py`) run as committed from the fresh clone, with one environment variable set (`PYTHONIOENCODING=utf-8`) and no file edited — reproduction, recorded as such; **this session's own code** (`experiments/merle_r16_check.py`, `experiments/merle_r17_check.py`) is the verification.
- **File edits**: Edit/Write tools only, everywhere; both output files written by Python's own `open(...).write` via redirection at the shell (`>` in Bash, never PowerShell), never PowerShell `Get-Content`/`Set-Content`.
- **Reproduction commands** (from the repository root, exact byte-for-byte reproduction of the committed output):
  - `python experiments/merle_r16_check.py > experiments/merle_r16_check_output.txt`
  - `python experiments/merle_r17_check.py > experiments/merle_r17_check_output.txt`
- **Encoding scan**: `python experiments/encoding_scan.py` run before the final commit — result below.
- **No key turns, no merges, nothing sent.** Both review drafts (§8.1, §8.2) are offered only; the main session reviews and merges, the author posts.

---
