# A reader's trailhead

For external readers arriving from the papers or from correspondence: this page tells you where things live and how to check a claim yourself. It contains pointers only — every fact lives in exactly one wiki page, and this page restates none of them. The plain-language overview is `README.md`; the maintenance rules (what "proved" is allowed to mean here) are `AGENTS.md`.

## How this repository works, in four sentences

The wiki pages (`spine.md`, `stage1.md`–`stage4.md`, `cycles.md`, `aeh.md`, `reverse.md`, `bridge.md`, `anchors.md`, …) are the live document; each carries its current status in front matter, and history lives in git, not in the pages. `sources/` is the immutable draft archive (v000–v078); nothing there is ever edited. `experiments/` holds runnable verification code: every computational claim in the wiki names its script, and nothing is labeled *proved* on the strength of the code that suggested it — an independently written check is required first. Refuted and failed claims are kept, with their refutation data, not deleted (`archive/`, `briefs/*-findings.md`).

## If you are coming from the papers

| Paper | Wiki home |
|---|---|
| Paper 1, the reduced system and per-step laws (§2–3) | `spine.md` §9 (the reduced map, faithfulness), `stage1.md`–`stage4.md` (the four per-step laws), `stage1-synthesis.md` (the anchor) |
| Paper 1, cycles: periods 1–3, uniform trim, staircase (§4) | `cycles.md` §12 — the trim is 12.8.1, the staircase family 12.8.3, and the post-publication proof of the family at every period is **12.8.6** (see below — the paper's own hedge sentence survives in v3, whose *Status of the assessment* paragraph reports the proof; the wiki carries it) |
| Paper 1, AEH (§5) | `aeh.md` §13 (the hypothesis, the calibration campaign, the routing lemma); `anchor-digit-search.md` §17.7 (the single-sequence statistical battery) |
| Paper 1, Appendix A (methodology) | `AGENTS.md`, `HANDOFF.md` (the internal working conventions those paragraphs describe) |
| Paper 2, the 3-adic mirror | `reverse.md` §14.1–14.14 (canonical proofs; the door/exit seam is 14.14), `itinerary.md` §14.15 (the itinerary language) |
| Both papers' "where the difficulty lives" | `bridge.md` §16 (the terminal open object: the anchor increment at unbounded depth) |

## Dictionary: this record's terms against the literature

**Map symbols (the convention, stated once).** This record's `T` is the odd-to-odd map `x ↦ (3x+1)/2^{v₂(3x+1)}` on positive odd integers (spine.md §9.8), which is Tao's `Syr`; the literature's `T` — Terras 1976 and Lagarias 1985: one division per step, `x ↦ x/2` or `(3x+1)/2`, Tao's `Col₂` — is this record's `T₁` (aeh.md 13.2.3); the raw map `x ↦ x/2`, `3x+1` is `Col`, Tao's symbol (spine.md §3.1); and `T_N` is a block horizon (aeh.md 13.2.1), not a map. Both published papers use the odd-to-odd `T`: paper 1 defines it in its first sentence and names the one-division map in words only (its §5), and paper 2 fixes the same `T` in its introduction, with `T₃` for its mirror map on cores — so a reader arriving from the PDFs has seen this record's convention, not the literature's. The shared repository with Eric Merle (`macindoe/one-obstruction-three-faces`: `PROTOCOL.md`, `LEDGER.md`, `NOTE.md`, `NOTE-v1.md`) uses none of these map symbols — its `T1` is the label of a theorem — and cites this wiki by section number only in cycles.md §12.1, §12.6.1, §12.8, itinerary.md §14.15 and aeh.md 13.6.7. `symbols.md`'s registry and collision index carry the same mapping and point here.

| This record | Literature | Defined at |
|---|---|---|
| `Col` (raw map); `T` (odd-to-odd); `T₁` (one-division); `T_N` (block horizon) | Tao 2019: `Col`, `Syr`, `Col₂`; Terras 1976 / Lagarias 1985: `T` for the one-division map; no counterpart for `T_N` | the note above; spine.md §3.1, §9.8; aeh.md 13.2.1, 13.2.3 |
| reduced map `F`; block; reduced state `(ω, d)`; odd core `ω`; depth `d` | the Syracuse map with each rising run (`m − 1` odd steps from `2^m u − 1`, then one cascade) taken as a single step; no literature name for the state (publication.md: new packaging of known material) | spine.md §3.2–3.7, §5.6 |
| anchor `N(ω)`, `M(ω)`; the valuation law `s = 2 + v₂(d − M(ω))` | a normalized 2-adic logarithm, `N(ω) = −log ω / log 9`; the law is the isometry of the 2-adic logarithm, i.e. lifting-the-exponent; no literature name for the anchor as a dynamical coordinate (publication.md's verdict) | stage1-synthesis.md 11.8.3.6; stage2.md 11.8.5.6.1; anchors.md 17.1 |
| exit valuation `s`; entry depth `m`; letter `(m, r)`; stratum word; itinerary language | the parity vector (Terras 1976, Everett 1977; Lagarias 1985), equivalently Tao's `n`-Syracuse valuation `a^{(n)}(N)`, recoded at the renewal times where an exponent is `≥ 2`: a letter `(m, r)` is the exponent word `(1, …, 1, 1 + r)` of `m` entries | itinerary.md 14.15.1; aeh.md 13.6.5 (the dictionary) |
| digit budget; window trichotomy | Terras's cylinder count (each parity vector of length `n` on one residue class mod `2^n`); Tao 2019 Proposition 1.9; the 2-adic shift conjugacy (Lagarias 1985; Bernstein–Lagarias 1996) | stage4.md 11.8.7.6–11.8.7.7; aeh.md 13.2.4 |
| AEH (the Anchor Equidistribution Hypothesis); its genericity form | Tao 2019 Heuristic 1.8, the valuation heuristic (`a^{(n)}(N)` behaves like `Geom(2)^n`; its 2-adic Haar justification is his Remark 1.10), stated in ensemble form with a budget; the stochastic models classical since Terras 1976, surveyed in Lagarias 1985 | aeh.md 13.2, 13.6 |
| the depth law; the 3-adic past-limit `y₃` | Tao's Syracuse random variable `Syrac(Z₃)`: `y₃ = Syrac(Z₃)/2` in distribution | aeh.md 13.6.5; itinerary.md 14.15.3.3 |
| the 3-adic anchor `M₃(y)` | a 3-adic discrete logarithm base 2, affine (`2^{M₃(y)} = −1/y`); no literature name pinned in this record | reverse.md 14.2 |
| rotation numerator `R_r`; cycle product equation; seam gap `q = 2^K − 3^n` | Tao's `n`-Syracuse offset `F_n(a)`, via `2^{m₀} R₀ = 2^K F_n(a) + q`; the linear cycle equation of Böhm–Sontacchi 1978, surveyed in Lagarias 1985 | cycles.md 12.1, 12.6.1, 12.6.1.7 |
| the near-miss anchors; the spent `\|q\| = 1` stock | the `\|2^a − 3^b\| = 1` classification, Gersonides 1342/43 (the citation posture of this record and the shared ledger) | cycles.md 12.6.1.2 |
| period-1, period-2 exclusions | Steiner 1977 (circuits); Simons–de Weger 2005 (`m`-cycles); the current record Hercher 2022/23 | cycles.md 12.2, 12.4, 12.5 |
| digit-match ceiling | Baker-type `p`-adic bounds: Bugeaud–Laurent 1996, Yu | stage1-synthesis.md 11.8.3.11; anchors.md 17.4 |
| the density bound of the door tree | the Krasikov–Lagarias program (2002/03), after Crandall 1978 and Krasikov 1989 | reverse.md 14.6 |
| exit map `G`; block map; door; live and dead doors; Gardens of Eden | `G` is Tao's `Syr` observed at the renewal times above (the variable-return-time block map); "door" is this record's; Gardens of Eden is a cellular-automata term for states with no preimage, used here for the reduced map | reverse.md 14.14.3, 14.14.7; 14.14.1; 14.5 |
| top door; side doors; top-door lineage | no literature name pinned in this record; the nearest object is the `a = 0` branch of the Syracuse preimage tree, read as its own coordinate (the author's proposal, 2026-09-10) | reverse.md 14.8.4 |
| peak; comb; cascade edge; door edge; peak distance `λ`, reduced distance `η` | the classical Collatz inverse tree — the "Collatz graph" of Lagarias 1985 §2, equivalently the Syracuse (odd-to-odd) preimage tree — with each block's odd rising run contracted to its reduced state and the halvings of a cascade taken in pairs (the two preimages `2z` and `(z−1)/3` of the graph become the cascade edge and the door edge); the peak is the block's `3x+1` maximum halved once, which the graph carries as an ordinary even vertex, and no literature name was found for it as a coordinate or for the two-distance split (checked against the record's `sources/` — the drafts, the two papers, the residue data — and the citations on this page; the density literature of the row above counts odd integers or `T`-preimages, never the even maximum). Closest object seen: the level structure of the inverse tree by total stopping time, which is `λ` with cascade halvings counted singly and rising runs uncontracted — a different distance | comb.md §18 |
| capped window `W_{k,D}`; the law `π_{k,D}` | the cylinder measure of the parity-vector coding in Bernoulli form (aeh.md 13.6.2); no literature name for the capped window | aeh.md 13.2 |
| uniform trim; staircase; seam; Bridge; core-extraction deficit; ladder, spike, braid | no literature name (this record's) | cycles.md 12.8.1, 12.8.3; reverse.md 14.14; bridge.md §16, 16.2; ladder.md §15 |
| transport recurrence; spent stock; margin; capacity–demand | no literature name; joint with Eric Merle where the shared ledger says so (L-A1, L-A3) | cycles.md 12.6.1.1–12.6.1.5 |
| realization height `H_{p,q}`; diagonal compatibility locus; signed diagonal | no literature name; the 2-adic side is the classical coding above, and the two-sided `Z₂ × Z₃` object was not found (itinerary.md 14.15.3(d); publication.md) | itinerary.md 14.15.3–14.15.6 |

## If you are coming from the July 2026 correspondence (staircase / δ8)

- The `thm:staircase` hedge — sharpness assessed, not proved, for all `p` — is exactly `cycles.md` 12.8.3 (a *Remark* there, deliberately). It is closed at `cycles.md` **12.8.6**, in two independent halves: an availability theorem resting on one exact number, `8 − 5·log₂3`, and an explicit integer construction whose size conditions hold with no correction step. Unconditional for `p ≥ 16`, a finite check for `3 ≤ p ≤ 15`, `p ∈ {2,4}` by exhibition; scope and limits are stated in the section itself. The earlier route — semiconvergents of `log₂3`, a rounded geometric profile, a bounded correction, and verified instances for `p ∈ {2,…,23}` with an obstruction at `p = 22` resolved 2026-07-17 through the same correspondent — is what the v2 release note described, kept as the superseded formulation at v2's frozen DOI; v3 (2026-08-03) replaces that note with the *Status of the assessment* paragraph, which reports the proof and is the current print-side pointer.
- The diagnostic detail behind the (now resolved) `p = 22` obstruction and the three untried construction variants are in `briefs/staircase-allp-findings.md`, the superseded earlier attempt; the resolution's own diagnosis and independent re-verification are in `briefs/merle-pincer-check-findings.md`. The delegation briefs that scoped the two attempts are `briefs/staircase-allp-brief.md` and `briefs/merle-pincer-check-brief.md`. The sessions that closed it are recorded at `briefs/staircase-allp-construction-findings.md` (the construction), `briefs/staircase-allp-diophantine-findings.md` (availability) and `briefs/staircase-gamma-upper-findings.md` (the `γ` bracket).
- The verification code is `experiments/staircase_allp_construction.py`, `experiments/staircase_allp_diophantine.py` and `experiments/staircase_gamma_upper.py` — three independent implementations, exact big integers throughout; `experiments/staircase_allp.py` is the earlier route's, and `experiments/uniform_trim.py` produced the original instances.
- The closed anchor walk (`Σ ΔM_t = 0`) and its rigidity — the divisibility structure the size arguments cannot reach — live at `stage4.md` (the increment law) and `bridge.md` §16 (why the deficit is two-sided); the cycle-side statement of what remains is `cycles.md` 12.8.4–12.8.5.
- AEH calibration and its four dissolved anomalies: `aeh.md` §13. None was staircase-shaped; the hypothesis is a statement about uniformly sampled starting values over a prescribed finite horizon, so no individual orbit's tail is in its reach by construction.

## Visualizations

Interactive, self-contained single-file HTML lives in `viz/` (the README's repository map lists each one); `viz/cycle_anchor_gateway.html` is the cycle-side gateway.

## How to check a claim

Find the claim's verification line in its wiki section (what was checked, the range, the date, the script name), then run the script: `python experiments/<name>.py`. Scripts are self-contained, use exact big-integer arithmetic wherever a pass/fail decision is made, and print what they verify. If a script's output and its wiki section ever disagree, the section is wrong — that is a bug worth reporting.

## Status vocabulary

- **proved** — has a written proof *and* an independent numerical check by fresh code (not the code that found it).
- **assessed** — a stated judgment with evidence, explicitly not proved. The paper's `thm:staircase` sharpness half is the canonical example and remains stated that way *in print* (the assess sentence survives in v3, which additionally reports the proof's existence); the wiki has since proved it (`cycles.md` 12.8.6), which is exactly the divergence this page exists to make visible.
- **calibrated** — an empirical program executed with controls; says what survived, not what is true.
- **formulation grade** — a definition and its easy direction, recorded to name an open object precisely.
- **floor grade** — a delegation outcome: the attempt's minimum deliverable (extended evidence plus a documented obstruction), reached when the theorem itself was not. No wiki section stands at this grade; it grades the superseded earlier staircase attempt (`briefs/staircase-allp-findings.md`), which is the outcome the published v2 note reports, and which `cycles.md` 12.8.6 replaced with a proof.
- **parked** — closed by a binding stopping rule (`README.md`), not by resolution; reopens only under the rule's own condition.
