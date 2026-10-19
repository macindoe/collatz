# Findings: the wiki aligned with the ceiling's settled credit chain and 12.8.7

**Task:** `briefs/ceiling-wiki-alignment-brief.md`. Branch `ceiling-wiki-alignment`, base **`85f42d3`** (the worktree was cut at `946e0d8` and fast-forwarded to `85f42d3` before any work). Credit and standing only: no proof changed, nothing renumbered, `paper/` and the shared Merle repository untouched, nothing outward.

**Commits.**
- `0a53b8d`: content (publication.md, cycles.md, TOUR.md, README.md, HANDOFF.md bodies).
- `375a6be`: structure (front matter of publication.md and cycles.md; index.md; the Williams script's docstring).
- This findings file (encoding scan run before it).

## 1. Every edit, with its source

| # | Page, place | Edit | Source |
|---|---|---|---|
| 1.1 | publication.md, Current state | the cycle clause now says the trim is subsumed (Rozier 1991; SdW 2005 Lemma 7), the sharpness is partially anticipated (Rozier p. 11, SdW p. 69, HH 1997), and the integer realization at every period and at `X₀` (12.8.6–12.8.7) is the strongest remaining candidate; one clause on Williams for `(ω, d)`; the snapshot sentence says the cycle and coordinate verdicts were re-checked 2026-10-18/19 | NR §5.1 (proposed Current-state clause); CS §0, §6; X0 §10 |
| 1.2 | publication.md, 12.8 verdict | the verdict sentences replaced: trim first in Rozier 1991 (Théorème p. 8, Lemme 4 p. 11), explicit in SdW 2005 (Lemma 7, 12, 14, Thm 3(d)), Brox 2000; `m = p` (12.4); present as a rederivation; sharpness partially anticipated (Rozier's real-tuple minimax, SdW's belief, HH's length-parameter proof); the residue is Rozier's extremal realized in integers at every period and at SdW's threshold `X₀` (12.8.7, `Λ ≥ 0.0541·2^{−ε_p n}`); SdW's "to a constant" left open; one dated re-check line. The sharpness-hedge status and v2/v3 sentences after it are untouched | NR §5.1 wording, adjusted per CS §6 (Rozier first) and X0 §7, §9 (threshold form, what not to say) |
| 1.3 | publication.md, Reduced-blocks verdict | the "not found in this exact form" sentence replaced: the cascade is classical (Steiner, Rozier 1990, LaDue 2018); the state is Williams's skeleton row `(λ, k = a + b)`, one week before v1; `F` and the 9.8 equivalence are not in Williams; paper 1 answers her open problem (1) **in part** (where the trajectory lands, not which skeleton); one dated check line naming both Williams scripts | CS §5, §6 wording, calibrated by `briefs/williams-letter-findings.md` (verdict "in part") |
| 1.4 | publication.md, Provenance | "the human layer has no found neighbor" removed (false since Williams); the 2023 note stated as authorship, not priority; contemporary overlap named in both layers | CS §6 "Collateral"; paper1-v4-items 1.13–1.14 |
| 1.5 | publication.md, Framing recommendation | "feature the uniform-trim/staircase dichotomy as the main new theorem" replaced by the staircase sharpness with the trim attributed and rederived | NR §5.1 closing paragraph |
| 1.6 | publication.md, front matter | status notes the re-check and v4 in drafting; `updated: 2026-10-19` | Item 1 |
| 2.1 | cycles.md, Current state | the trim and finiteness labelled classical (Rozier 1991; SdW 2005 Lemma 7, 14; Brox 2000), pointer to the attribution; one sentence on 12.8.7 | X0 §10 (Current-state clause); NR §4.1; CS §3.1 |
| 2.2 | cycles.md, 12.8 intro; Theorem 12.8.1 and Corollary 12.8.2 headers | attribution parentheticals (header text only; numbers unchanged) | NR §3, §4.1 |
| 2.3 | cycles.md, new paragraph "Attribution (12.8.1–12.8.2)" after 12.8.2's verification, before Remark 12.8.3 | the dictionary (`m = p`, their `K` our `n`), Rozier Lemme 4, SdW Lemma 7 up to the additive constant, Lemma 14 / Thm 3(d) with the same Rhin measure, `K₁(m)/(m·δ^m) → 15.107…` as the counterpart of the table's ratio (no limit claimed for the record's table), Brox; claims neither as new | NR §4.1; CS §3.1 |
| 2.4 | cycles.md, Remark 12.7.3 | "all `p <= 68` remain subsumed by Simons–de Weger" → "all `p <= 91` are subsumed by the `m`-cycle record (Simons–de Weger to `68`/`76`, Hercher to `91`; publication.md's pin)", via `m = p` | 12.4 recheck findings §3 (first bullet) |
| 2.5 | cycles.md, front matter | status names the trim as classical | Item 2 |
| 3.1 | index.md, cycles.md row | `m = p` at 12.4; trim classical, rederived; 12.8.7 added; status "sharpness proved (12.8.6, 12.8.7)" | X0 §10; 12.4 recheck |
| 3.2 | index.md, publication.md row | status matched to its new front matter | periodic status pass |
| 3.3 | index.md, resolver | "§12 (post-monolith; through 12.8.7) → `cycles.md`" (the resolver maps by section prefix, so this records 12.8.7's home; no renumbering) | Item 3 |
| 3.4 | index.md, status summary; front matter | attribution and the 12.8.7 clause; `updated: 2026-10-19` | Item 3 |
| 4.1 | TOUR.md, paper-to-wiki row (cycles) | trim classical with pointer to the attribution; 12.8.7 named | Item 4 |
| 4.2 | TOUR.md, map-symbols note (line 22) | "names the one-division map in words only (its §5)" corrected: in words in §5, except one sentence writing "`T`-time" for it (v3 source line 406), recorded for v4 | paper1-v4-items §7 item 3, row 1.25; checked against `paper/collatz-reduced-v3.tex` (lines 295, 314 say "one-division map"; line 406 says `$T$-time`) |
| 4.3 | TOUR.md, `(ω, d)` row | Williams's skeleton row named with the dictionary (`λ = ω`, `k = d`); the cascade classical (Steiner 1977; LaDue 2018); `F` not in Williams | CS §5 items 1, 4–5 |
| 4.4 | TOUR.md, `m`-cycle row | "`m` = the number of blocks `p` exactly" | 12.4 recheck |
| 4.5 | TOUR.md, new row: block start / `a_r` / threshold `X₀` | `x_r = 2^{m_r}R_r/q − 1` is the local minimum; `a_r = R_r/q` is SdW's `a_i`, not an element; "every element `≥ X₀`" is `x_min ≥ X₀`, not `X₀ q ≤ R_r` | X0 §1.2, §10 (the TOUR item) |
| 4.6 | TOUR.md, the "uniform trim; staircase; …" row | split in three: the uniform trim now has its literature names (Rozier Lemme 4; SdW Lemma 7, 14, Thm 3(d); Brox); the staircase keeps "no literature name" with its anticipations (Rozier p. 11, SdW p. 69, HH 1997); the remaining terms unchanged | NR §5.2 (wiki-side proposal), CS §6 |
| 5.1 | README.md, strategy paragraph | the trim and finiteness are classical (Rozier 1991; SdW 2005, `m`-cycles = `p`-block cycles), rederived; the record's contribution is the sharpness at every period and at `X₀`, anticipated by Rozier's remark and SdW's expectation. Stopping rules untouched | Item 5; NR §5.2; X0 §10 |
| 5.2 | README.md, scoreboard sentence; map row for cycles.md | "(classical … rederived)"; "and at Simons–de Weger's size threshold `X₀`" | X0 §10 (the optional scoreboard item) |
| 6.1 | experiments/williams_coordinate_check.py, docstring | "Proposition 2.3" → "Proposition 2.2" (three places); a note that the printed label of check 3 still reads "Prop 2.3(i)" so the committed output stays byte-identical. Re-run 2026-10-19: output byte-identical to the committed file, ALL CHECKS PASS | williams-letter findings "Numbering correction"; paper1-v4-items §7 item 4 |
| 7.1 | HANDOFF.md, State of the fronts, Cycles | the trim's attribution, 12.8.7, and `m = p` | Item 7 context |
| 7.2 | HANDOFF.md, State of the fronts, Papers | a present-tense entry: paper 1 v4 in drafting, not published, no DOI; what is decided (D1–D15 in substance); where the checklist (`briefs/paper1-v4-items-findings.md`), decisions (`briefs/paper1-v4-draft-brief.md`) and draft (branch `paper1-v4-draft`) live; minting and register requests the author's | Item 7; `briefs/paper1-v4-draft-brief.md` |
| 7.3 | HANDOFF.md, "The paper at v3", citation guidance | "v3 for the dichotomy phrases and the Theorem 4.6 obstruction sentence" → v3 for the Theorem 4.6 sharpness and obstruction sentence, not for the trim (Rozier / SdW), the obstruction's cycle-length form credited to HH 1997 | status pass (paper1-v4-items row 2.11 names this line; its full replacement waits for v4 publication) |

Sources abbreviated: NR = `briefs/ceiling-novelty-refresh-findings.md`; CS = `briefs/ceiling-ccchallenge-sweep-findings.md`; X0 = `briefs/staircase-x0-threshold-findings.md`; 12.4 recheck = `briefs/cycles-12-4-recheck-findings.md`; HH = Halbeisen–Hungerbühler 1997; SdW = Simons–de Weger 2005.

**Calibrations applied while writing.**
- Williams: "answers open problem (1) in part" everywhere (the CS "answered by `F`" line is not carried).
- Residue: Rozier's extremal realized in integers (CS §3.2), not "settling SdW's expectation" (NR's earlier framing).
- Not said anywhere: that Rozier's Lemme 4 inequality is attained, that SdW's "at best a constant" is settled, that the unit-block staircase works at the threshold scale, or anything about exclusion (X0 §9's list).
- The trim's attribution says "up to the additive constant" and gives SdW's `15.107…` limit as theirs. The record's own `n_0(p)` table still claims no limiting constant.

## 2. The periodic status pass (Item 8)

**Grep.** Every tracked page (`*.md` at the root and `archive/`; `briefs/`, `sources/` and `paper/` excluded) was searched for "uniform trim", "uniform-trim", "staircase", "dichotomy", "main new theorem", "Simons", "Rozier", "Williams", "12.4", "deep-entry". After both commits, a second grep found no "main new theorem" claim, "counting-limit", "genuinely new theorem", "best candidate", "no found neighbor", "`p <= 68`" or "deep-entry" on any page; the one hit is HANDOFF's own sentence that v4 drops the phrase.

**Fixed** (pages this window owns):
- publication.md, Current state "sharpness dichotomy … strongest candidate for a genuinely new theorem" (1.1).
- publication.md, 12.8 verdict "best candidate for a genuinely new result … not found in the literature" (1.2).
- publication.md, Reduced-blocks "not found in this exact form" (1.3).
- publication.md, Provenance "the human layer has no found neighbor" (1.4).
- publication.md, Framing "the uniform-trim/staircase dichotomy as the main new theorem" (1.5).
- cycles.md 12.7.3 "`p <= 68`" (2.4).
- TOUR.md, the trim row "no literature name" (4.6), the `(ω, d)` row "no literature name for the state" (4.3), and line 22's "in words only" (4.2).
- HANDOFF.md, the v3 citation guidance "dichotomy phrases" (7.3).

**Checked and consistent, no edit:**
- `deep-entry`: no page carries the struck 12.4 clause (12.4 itself was rewritten on its own branch).
- publication.md line 14 "crossover threshold `p > 91` correctly calibrated"; open-problems.md's calibration note: both stand under `m = p` (12.4 recheck §3).
- index.md "m-cycle translation (12.4)"; cycles.md 12.5.3's SdW dictionary; 12.2.3: stand.
- The "dichotomy" hits in ladder.md, reverse.md, itinerary.md, stage1.md, bridge.md and archive/ are unrelated ladder, mirror or tower dichotomies.
- The "Simons" hits in stage1-synthesis.md 11.8.3.11, open-problems.md (lines 163, 174, 181, 187), bridge.md "The constants, pinned" and symbols.md: Rhin-via-SdW-Lemma-12 pins and cycle-length lower bounds, no novelty claim.
- "staircase" hits in aeh.md (`13.3.3`, the staircase as AEH-exceptional tails) and bridge.md 16.4.6 ("One configuration, both halves"): the staircase–divergence reading, which the literature search did not find; they stand.

**Left (not owned by this window, or the author's call), listed:**
1. bridge.md line 79 (the counting-limit bullet): "A trim uniform in `p` exists … the staircase family proves no size-counting argument does better (cycles.md 12.8.1–2, 12.8.3)". It does not contradict the new standing, since it claims no novelty, but it carries no attribution. A pointer "(classical: Rozier 1991, SdW 2005)" would align it. bridge.md is outside this window.
2. stage4.md (Current state and the `11.8.7` done-note): "the uniform trim resolved". Consistent; no attribution. Outside this window.
3. README.md, "What this program does not claim": "Realistic wins from here: the uniform cycle theorem, a crossover record, and a publishable spine." This predates the resolution (the crossover plan is withdrawn and the trim is classical). It is in README's strategy register and is the author's wording. Left, flagged.
4. spine.md line 38, "The fourth layer is the novel step of the framework" (line 38). Outside the grep terms. It is a framing sentence about the quotient, which Williams's states now partly anticipate. Left, flagged.
5. `experiments/williams_coordinate_check_output.txt` and the script's print label still say "Prop 2.3(i)". Changing them would change the committed output, so they were left (6.1).
6. `briefs/ceiling-ccchallenge-sweep-findings.md`: its gendered pronoun for Williams (williams-letter findings item 5). This is a brief, not a page, and out of scope.
7. `open-problems.md`: no entry posed the threshold question, so no closure note is owed. The optional new entry on SdW's "`m c_m` to a constant" (the `log₂ p` gap, X0 §10) is the author's call under the stopping rules. Not added.
8. HANDOFF.md, "The hosting pin (v2) …" and the v3 paragraph: they describe v3 as current, which it is until v4 is minted. Their v4 replacement is a main-session edit at publication (paper1-v4-items rows 2.11, 6.3–6.6).
9. README.md line 3: the paper 1 DOI is the v1 DOI (paper1-v4-items row 6.3). Left for the v4 publication edit.

## 3. For the main session

- **Merge order.** This branch touches HANDOFF.md, publication.md, cycles.md and README.md. The `paper1-v4-draft` and `merle-round19-pr` windows were told not to edit wiki pages, so no overlap is expected. Check before merging that neither did.
- **HANDOFF's v4 entry names the branch `paper1-v4-draft` and its findings file.** If that window's deliverables land under other names, adjust the one sentence.
- **"One dated verification line."** publication.md carries one per verified verdict, the 12.8 line and the Reduced-blocks line, inline per AGENTS.md. Neither is a change log.
- Items 3 and 4 of §2 (README's "realistic wins", spine.md's "novel step") are wording the author may want to revisit. Neither is wrong on the mathematics.
- The encoding scan (`python experiments/encoding_scan.py`) was run before the findings commit.
