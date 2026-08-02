# Findings: applying round 3 to the record (v3 round 3, Wave 3, record delegate)

**Task:** `briefs/v3r3-record-apply-brief.md`. Edit round, not a design round.
**Branch:** `v3r3-review-round3`, base `2423f5c`. Three commits landed: `9d160d8` (experiments),
`a1e1701` (the record), `957f6cb` (`publication.md`). No push, no merge, no rebase, no worktree.
**Applied in order A → B → C → D**, with the later delegates superseding the earlier ones exactly where
their own reconciliation sections say so (`briefs/v3r3-cut-weighting-findings.md` §9,
`briefs/v3r3-basecase-density-findings.md` §6.2).

---

## 1. Site-by-site

### `aeh.md`

| Site (pre-edit line) | Whose text | Deviation, and why |
|---|---|---|
| L2 `status:` | A §7.6 | **+ one clause**: `unconditional base case PROVED at 13.2.4 … with the exceptional set at shell scale (13.2.5)`. AGENTS.md's proved-claim workflow requires the front matter to record a status change; A wrote §7.6 before D's lemma existed. Flagged in §5. |
| L8 Current state | A §7.6 (the two substitutions + the added clause) | **+ three touches**: the opening clause restated to the letter-primary form (Option 1a), `unqualified` gained `at block lengths L ≤ 2` (A §4.4 item 3, "must be printed"), and the ledger clause dropped "with explicit error bounds" (A §9 item 1 retires that error) and gained the `13.2.5` pointer (D §2). |
| L20–28 (the `13.2` preamble) | A §7.4 | Verbatim. `D_k` → free cap `D`; "validity data" retired. |
| L30 Hypothesis `13.2.1` | **C §8.1** (supersedes A §7.4's version) | Notation only: C's `L = ⌊log₂ N⌋` → `b`, and C's `ℓ` for word length → `L`. Forced by D §1, which fixes `b` = bit scale and `L` = block length, and by A's fixed `π^(L)_{k,D}`. |
| after `13.2.1` | C §8.1's following paragraph ("The budget clause is predictable…") | Verbatim. |
| Hypothesis `13.2.2` | **C §8.2** (amends A §7.4's) | Same `ℓ` → `L` substitution. |
| the segment boundary | A §7.4 | Verbatim; `T` → `T_N` for consistency with C's symbols. |
| L32 "Why the ensemble…" | **C §8.4**, final sentence replaced by **D §5.1** | Collision 1, see §2. D's `(k, D, ℓ)` → `(k, D, L)`. |
| L34 base case | **D §5.2 opening paragraph**, then **C §8.5**, then **B §5.2** + the closing "What has not been carried past it…" sentence | D §6.2 items 4–7. D's own second paragraph dropped, as D instructs. In B's clause, "`T`-steps per bit" → "divisions per bit (`T_1`-steps, `13.2.3`)": C §3(d) forbids bare "`T`-steps", three maps having worn the letter. |
| new anchor `13.2.3` | C §8.3 | **+ one clause** at the end of the clock paragraph reconciling the two exponent counts `Σ(m_i+s_i)` and `Σ(m_i+r_i)` — D §6.1 asked the apply phase to "pick one and say which", and both now appear on the page. |
| new anchors `13.2.4`, `13.2.4.1`, Verified line, `13.2.5`, Scope | D §5.3 | `T` → `T_N` throughout. Corollary `13.2.4.1`'s "every admissible `(X_N)`" → "every `θ < 1/4` — equivalently … every admissible `(τ, θ)` with `τ < 1` — and every cut sequence `(X_N)`", because "admissible" is now C's two-clause predicate on `(τ, θ)`. Lemma (c)'s parenthetical dropped its "delegate B's S1" cross-reference (a brief-internal name must not land in a tracked page). |
| L36 supporting facts | A §7.4's token substitutions | **+ two touches**: the `s`-marginal gained "at every `j < D`, with the cap's single tail cell above" (A §9 items 1–2), and "bulk segments" → "in-budget blocks" (C §5.1). |
| `13.3.1` | A §9 item 1 + C §10 item 6 | Restated: the ledger is a marginal of `π_{k,D}`, the `O(2^-k)` retired to `11.8.7.6.1`'s prediction statement, "bulk blocks" → "blocks, all of them within budget", `13.2.5` pointer, and the `L = 1` annotation A §6 item 5 asks for. |
| `13.3.2` opening | A §9 item 2 + C §10 item 7 | Same shape; cap error `O(2^{-D})` printed. |
| `13.3.2` Inselmann sentence | **B §5.3** + B's two precision fixes | **+ two touches**: "simultaneously for all `k`" gained "(`k` in **Syracuse** steps)" and "at exactly the horizon `θ = 1/β` that `13.2.1` names as a full descent" became "out to the descent horizon whose block-time image is `13.2.1`'s admissible ceiling `θ = 1/β` (`13.2.3`)" — B §5.8 prescribes exactly this pair of fixes for the same sentence in `publication.md`, and the clause conflates the two times. **+ one clause** naming Inselmann's `T` as `13.2.3`'s `T_1`. |
| L48 `13.4` reconciliation and cut note | C §8.6 | Verbatim. |
| `13.5` standing rule | C §8.11 | Verbatim. |
| `13.5` "Status: resolved" | A §4.4 item 3 | "unqualified at all tested depths and cells" gained "at block lengths `L ≤ 2` — the campaign tests `L = 1` and `L = 2` and is silent above". Not a named drop-in; A says it must be printed. |
| `13.6` opening, `13.4` bullet 3, `13.6.5` closing | A §7.4 token substitution | `π_k` → `π_{k,D}` (4 sites). |
| `13.6.3`(i)(a) | C §10 item 14 | "The bulk cut is literally the same on both sides" → the door-coordinate reason. |
| `13.6.3`(iii) | A §3.1, §3.5 | `D_k` → `D`; "the reading of `13.2`'s 'validity data'" replaced by the capped labels of `W_{k,D}`; **+ one clause** recording that under `B̂` the exceptional event has probability zero (A §3.5 reason 2, which the `13.2` preamble already states and this site contradicted). |
| `13.6.3`(v) | A §9 item 5 | Restated on `B̂`, with A's reason (the absorption is not a function on odd `Z_2`) and A's two consequences (`m_n ⊥ a_{n+1}` exact, no exceptional event). No drop-in existed; the brief lists the site, and I kept to A's §3.5/§9 wording. |
| `13.6.4` statement | A §7.5 + C §10 item 11 | Verbatim, plus "together with a bulk cut" → "together with a rule selecting which blocks are tallied" and "bulk segments" → "in-budget blocks". |
| `13.6.4` proof (⇐) | — | **+ one parenthetical**: each letter is read off once `D` exceeds its components, the definition quantifying over every `D`. See §4 item 1. |
| `13.6.4` (q1) | A §7.5 | Verbatim. |
| `13.6.5` "Under `B`" | A §9 item 10 | → "Under `B̂`", with the one-clause reason. |
| `13.6.5` attribution | **B §6.3** | **+ the footnote-4 citation**, owed because the author chose Option 1 and the page now constructs the law from an infinite past. Conditional in B's text on exactly that choice. |
| `13.6.5` orbit adjudication | C §10 item 15 | Protocol relabelled (`core cut ω_+ > 2^30 — which binds, 13.4`), and C's qualifier printed on the `a_+ = 0` cell. **No measured value touched.** |
| `13.6.6` | C §5.1, §10 item 13 | "the cut keeps the narrower job" → the budget of `13.2.3` keeps it; "bulk segments" → "in-budget blocks". |
| `13.6.7` | C §5.1 | "the bulk visits of uniformly sampled large starts" → "the in-budget blocks". |

### Other pages

| Site | Whose text | Deviation |
|---|---|---|
| `itinerary.md` L73 | A §7.7 verbatim (including the `2^{-S}` normalization fix of A's footnote) | "bulk segments" → "in-budget blocks", for consistency with `aeh.md`. |
| `bridge.md` L69 | A §7.8 (`π_k → π_{k,D}`) | Reworded to "in its precise ensemble form, equivalently against the stationary window law `π_{k,D}` (aeh.md 13.2.1, 13.2.2)", because under Option 1a `13.2.1` is the letter form and `π_{k,D}` is `13.2.2`'s object. |
| `bridge.md` L48 (**G5**) | — | "for typical orbits" → "for typical starting values". |
| `HANDOFF.md` L20 | A §7.8 | **No edit** — A: "substantively unchanged under Option 1". |
| `anchor-digit-search.md` L37, L78 (**G5**) | — | "the bulk hypothesis" → "AEH (aeh.md `13.2.1`)" and "AEH". |
| `publication.md` `status:` (**G4**) | — | Records paper 1 at v2 and the mirror paper published; v3 DRAFTED and UNPUBLISHED, DOI `10.5281/zenodo.21730505` reserved. |
| `publication.md` landscape item 4 | B §5.7 verbatim | — |
| `publication.md` AEH descent bullet | B §5.8, all three amendments | — |
| `publication.md` L45 Tao motive | B §6.5 | — |
| `publication.md` staircase bullet (**G4**) | — | The superseded plan sentence ("wiki-only now… no v3 yet") replaced by the current state. No "was X, now Y". |
| `publication.md` L26, L46 | A §7.4 token substitution | `π_k` → `π_{k,D}` (the L46 phrase became "the joint labelled law `π_{k,D}` with its two product clauses", since "exact product law" is the misreading A's round exists to remove). |

### `experiments/`

| Site | What |
|---|---|
| `experiments/aeh_basecase.py` (new) | D §8 promoted verbatim, minus the unused `import sys`, plus the repo's `Run: … (date: …)` header line. Header already names the page and results it supports (AGENTS.md, Layers 3). Smoke-run here: C0 `0` failures at `300` starts; C3 exact at two `(n,J)`; C1 at `J = 14` gives `4,095` words `= 2^{J−2} − 1`, `0` failures; C7 at `b = 200` gives `0`/`0` failures; `I(0.20, 0.24, 0.25) = 0.020136, 0.00080, 0`. Every one matches D's §7 table. The full campaign (`J = 22` exhaustive, `6000`-bit starts) was not re-run. |
| `experiments/aeh_symbolic.py` L541–544 | Docstring only. The false "never binds" replaced by the measured rates, with an explicit note that the behaviour is left as it is because `13.6.5`'s recorded values were produced by it. **No code path touched.** |

---

## 2. The two collisions, resolved

**Collision 1 — the defective density sentence.** C's §8.4 rewrites `aeh.md` L32 as a whole paragraph and
reproduces the old inference ("the union of the bad sets has natural density zero") verbatim, changing
only the dependence list. D's §5.1 is the substitute tail and says so. **Applied: C's §8.4 block with its
final sentence replaced by D's §5.1**, and D's `(k, D, ℓ)` re-lettered to `(k, D, L)`. The page now carries
the triangular-array diagnosis, the `Bad_N = [N, N(1 + 1/log N))` counterexample, and a pointer to
`13.2.5`, which is the repair. Nothing on the page still asserts the false implication.

*Handover to the paper delegate:* the identical defect sits at `paper/collatz-reduced-v3.tex` L301–304,
where **A's §7.3 reproduces it uncorrected**. **D's §5.5 is the merged block** (A's ledger/cap clause plus
the shell repair) and is the one to apply — D §6.2 item 15. I did not touch `paper/`.

**Collision 2 — the anchor number.** C claimed `13.2.3`; D yielded (D §6.1: C's anchor is cited from
inside the hypothesis statements, D's only from prose). **Applied as they now stand: C's `13.2.3` (the
clock and "admissible"), D's `13.2.4` / `13.2.4.1` / `13.2.5`.** Section order in `13.2` is A's
`13.2.1`, A's `13.2.2`, the boundary paragraph, the L32 paragraph, the L34 paragraph, `13.2.3`, `13.2.4`,
`13.2.4.1`, `13.2.5` — D §6.2 item 8. **No existing anchor was renumbered.**

---

## 3. Measured values now standing under a protocol whose bias is known but unquantified

C established that the core cut `ω_+ > X` biases the ledger's own statistic and measured the effect for
the flagship run only (`briefs/v3r3-cut-weighting-findings.md` §4, §12 item 4). **Nothing below was
re-derived, adjusted or re-worded.** This list is for the author's decision; no caveat beyond the two
C-specified ones (`13.4`'s protocol-gap paragraph, `13.6.5`'s `a_+ = 0` cell) went onto a tracked page.

**A. Under the core cut `ω_+ > X` (the coordinate C shows is the wrong one).**

| Where | Values | Protocol |
|---|---|---|
| `13.4` bullet 1 | `P(bits 3–4 \| class (1,2)) = 0.2533` (`0.8σ`); `(7,1)` cell `0.5017` (`0.4σ`); `(s,s') = (4,3)` cell `0.1277` vs `0.128` (`−0.1σ`); and the unquantified claim that "the `s`-marginals, `d`-law, and class-transition structure all match the exact chain" | `aeh_calibration.py` L350–372, `CUT = 2^24`, `big = w > CUT`; per-orbit ratios gated `h[cell][0] >= 2` |
| `13.4` bullet 2 | bottom-regime deviations "up to `z = 41`" | same run, the **complement** `ω ≤ 2^24` — the same selection, read from the other side |
| `13.4` bullet 4 | Merle's `\|λ₂\| ≤ 0.06`; our re-run `0.028 / 0.036` | `merle_aeh_key_check.py` `skeleton_and_spectrum(orbits, cut)`, cuts `2^20` and `2^30`, "transition counted while the source exit exceeds the cut" — an **altitude** (door-side) cut, not the core one, so C's measured direction is the milder of the two |
| `13.5` opening | `0.2677` vs `0.25`, `z = 5.0`, `2,610` orbits, "surviving a `2^40` cut" | `aeh_calibration.py` L394–409, `w > CUT` with `CUT = 2^40`, per-orbit ratio gated `den >= 2`. Already recorded on the page as an artifact of the ratio estimator; the cut coordinate is a second, independent defect in the same run |
| `13.6.5` orbit adjudication | `154,389` tallied visits; `L1 ≤ 0.006` over `d ≤ 5`; `P(d=2) = 0.3192` vs `20/63`; the chain-law rejection `0.018`, `≈ 14` pooled SE; `P(ω_+ ≡ 1 mod 3 \| a_+ = 0) = 0.6662 ± 0.0015`, `0.3σ` from `2/3`, `112σ` from `1/2` | `aeh_symbolic.py` `check_orbit_texture`, `CUT = 2^30` on `w1` (the core), seed `31005`. This is the run C replicated: `2.64 %` of visits and `15.5 %` of orbits removed |

**B. Verified *not* under any cut** (read in the code this round, so the list above is not longer than it
has to be):

* the drift `−0.4166 ± 0.0037` per odd step and `−0.8367 ± 0.0060` per block (`13.3.2`, `13.4` bullet 4) —
  `merle_aeh_key_check.py` `drift_fixed_horizon`, whose docstring reads "no stopping rule, **no cut**",
  confirmed by reading the function: it takes `trans[:horizon]` unconditionally;
* `13.5`'s decisive test, `0.2503 ± 0.0015` pooled over `84,739` visits — `experiments/aeh_anomaly.py`
  applies no cut anywhere in the file;
* `13.6.2`'s and `13.6.5`'s verification blocks — exhaustive counts and
  `check_two_sided_reconstruction` (`4,368` visits, `1` exceptional, seed `31003`), no cut in either.

**C. A different protocol question, flagged because it surfaced while checking B.** `13.3.2`'s measured
`3`-gain rate `0.3352` comes from `aeh_calibration.py` L61–84 (`pair2_s`), which runs **whole orbits**
from `40`-bit starts with `break` at `(1,1)` and **no bulk/bottom separation and no cut at all**. So it is
not touched by C's finding, but it is the one number in `13.3` measured under a protocol that `13.1` and
`13.5` both say is the wrong one. Not in this round's scope; recorded so it is not lost.

**What re-running would settle.** C §12 item 4 and item 6 name the two runs: the eight
`aeh_calibration.py` rounds under the door cut, and `13.6.5`'s `a_+ = 0` cell under the door cut or the
budget. Both are one-run items and both are out of scope here.

---

## 4. Asserted but not verified against the files

1. **`13.6.4`(⇐) at a fixed cap.** A §9 item 8 says the proof "survives verbatim", and A §3.1 says the
   capped labels are what the `(⇐)` direction reads letters off. At a *fixed* `D` the recovery
   `letter n = (σ_n − s_n, s_{n+1})` fails whenever a component reaches the cap, so "letters are *exact*
   functions of consecutive labeled window states" is true only once `D` exceeds those components. Since
   "bulk-equidistributed" quantifies over every `D`, the equivalence goes through; but A's drop-in does
   not say so, and the printed proof read as false at fixed `D`. **I added one parenthetical** rather than
   leave it. This is the one place I edited a proof, and it is flagged for review.
2. **A's open question 3** — that `13.6.3`(iv)'s `2·(0.93)^j` bound is unaffected under `B̂` — is used by
   D's `13.2.4`(e) and by `13.6.4`'s `(⇒)`. A flagged a one-paragraph re-derivation as an apply-phase
   item; **I did not do it.** Nothing on the page changed as a result: the bound is printed as it was, and
   its proof text is untouched. Still open.
3. **A's open question 4** — the composite five-coordinate labelled reconstruction is still not run as one
   test. D's C8 covers `(min(s,3), min(d,3))` only. Still open; the `13.6` verification block still
   describes the two-coordinate test it actually runs.
4. **C's full campaign was not re-run.** C's §4 numbers (`4,191`, `1,538`, `1.9871`, …) are quoted from
   C's replication, which reproduced `154,389` exactly. I did not re-run it. I did re-run the fast checks
   of D's promoted code (§1, `experiments/`), which reproduced D's own results.
5. **D's `1,376,253` distinct words** in the `13.2.4` verification line is `65,535 + 262,143 + 1,048,575`,
   which is consistent, and my `J = 14` run gave `4,095 = 2^{J−2} − 1` on the same formula. The `J = 22`
   exhaustive run itself was not repeated.
6. **Inselmann and Tao were not re-read.** B's transcriptions are taken as read.

---

## 5. Changes no delegate specified (every entry is a flag for review)

1. **`aeh.md` L2 gained the `13.2.4` / `13.2.5` clause.** AGENTS.md's proved-claim workflow; A's §7.6 was
   written before D's lemma existed.
2. **`aeh.md` L8's opening clause was restated to the letter-primary form** and its ledger clause dropped
   "with explicit error bounds". Both follow from A's Option 1a and A §9 item 1; neither is A's literal
   text.
3. **`13.3.1` and `13.3.2` were restated**, not merely re-worded. C §10 items 6–7 specify the "bulk
   blocks" → "within budget" change; A §9 items 1–2 specify the marginal/cap-error change but give
   drop-in text only for the paper (§7.3). The `aeh.md` wording is mine, tracking A's paper text.
4. **`13.6.3`(v)'s restatement is mine**, following A §3.5 and §9 item 5. The brief lists the site; A
   supplied no drop-in for it.
5. **`13.6.3`(iii) and `13.5`'s closing line** were touched to remove `D_k`, "validity data", and the
   now-narrowed "unqualified at all tested depths". A requires all three; none is a drop-in.
6. **Notation harmonisation across C and D:** `b` for bit scale, `L` for block length, `T_N` for the block
   horizon, `ℓ_n` for the letter. C's `L = ⌊log₂ N⌋` collided with A's and D's `L`; D §1 settles it and D
   is the later delegate. Nothing mathematical moves.
7. **`13.2.3` gained a clause reconciling `Σ(m_i+s_i)` with `Σ(m_i+r_i)`.** D §6.1 asked for exactly this;
   the wording is mine.
8. **`13.6.4`'s (⇐) parenthetical** — §4 item 1.
9. **B's "`T`-steps per bit" was disambiguated to "divisions per bit (`T_1`-steps, `13.2.3`)"** in the
   `13.2` base-case paragraph, and Inselmann's `T` was named as `13.2.3`'s `T_1` in `13.3.2`. C §3(d)
   forbids bare "`T`-steps" on this page; B wrote before `13.2.3` existed.
10. **`13.3.2`'s "at exactly the horizon `θ = 1/β`" clause** was replaced, applying B §5.8's prescription
    for the same sentence in `publication.md` to its `aeh.md` twin. B did not name this clause.
11. **`import sys` removed** from the promoted verification script (unused).

---

## 6. Left alone deliberately

* **`paper/` — untouched**, including the version note, the Appendix A commit pin `c2d465a` (which A and C
  both flag as dying on any `aeh.md` edit — it has now died), and the `.pdf`.
* **`HANDOFF.md`** — A §7.8 says L20 is substantively unchanged, so it is unchanged. Its "Papers — both
  published" bullet restates DOIs that `publication.md` owns; it is now less complete than
  `publication.md` (no v3 line). Out of G4's stated scope, so not edited; flagged.
* **Every measured value in `13.4` and `13.6.5`** — §3.
* **`13.4`'s and `13.5`'s historical narrative** of the dissolved discoveries — untouched.
* **Round 2's parked items** (2, 3, 4) and A's, C's and D's open questions — untouched.
