# A reader's trailhead

For external readers arriving from the papers or from correspondence: this page tells you where things live and how to check a claim yourself. It contains pointers only — every fact lives in exactly one wiki page, and this page restates none of them. The plain-language overview is `README.md`; the maintenance rules (what "proved" is allowed to mean here) are `AGENTS.md`.

## How this repository works, in four sentences

The wiki pages (`spine.md`, `stage1.md`–`stage4.md`, `cycles.md`, `aeh.md`, `reverse.md`, `bridge.md`, `anchors.md`, …) are the live document; each carries its current status in front matter, and history lives in git, not in the pages. `sources/` is the immutable draft archive (v000–v078); nothing there is ever edited. `experiments/` holds runnable verification code: every computational claim in the wiki names its script, and nothing is labeled *proved* on the strength of the code that suggested it — an independently written check is required first. Refuted and failed claims are kept, with their refutation data, not deleted (`archive/`, `briefs/*-findings.md`).

## If you are coming from the papers

| Paper | Wiki home |
|---|---|
| Paper 1, the reduced system and per-step laws (§2–3) | `spine.md` §9 (the reduced map, faithfulness), `stage1.md`–`stage4.md` (the four per-step laws), `stage1-synthesis.md` (the anchor) |
| Paper 1, cycles: periods 1–3, uniform trim, staircase (§4) | `cycles.md` §12 — the trim is 12.8.1, the staircase family 12.8.3, and the post-publication attempt to prove the family at every period is **12.8.6** (floor grade; see below) |
| Paper 1, AEH (§5) | `aeh.md` §13 (the hypothesis, the calibration campaign, the routing lemma); `anchor-digit-search.md` §17.7 (the single-sequence statistical battery) |
| Paper 1, Appendix A (methodology) | `AGENTS.md`, `HANDOFF.md` (the internal working conventions those paragraphs describe) |
| Paper 2, the 3-adic mirror | `reverse.md` §14.1–14.14 (canonical proofs; the door/exit seam is 14.14), `itinerary.md` §14.15 (the itinerary language) |
| Both papers' "where the difficulty lives" | `bridge.md` §16 (the terminal open object: the anchor increment at unbounded depth) |

## If you are coming from the July 2026 correspondence (staircase / δ8)

- The `thm:staircase` hedge — sharpness assessed, not proved, for all `p` — is exactly `cycles.md` 12.8.3 (a *Remark* there, deliberately). The attempt to close it is `cycles.md` **12.8.6**: a Diophantine lemma (semiconvergents of `log₂3`), an explicit profile, a bounded correction, and verified instances for the full contiguous range `p ∈ {2,…,23}` — an initial obstruction at `p = 22` was resolved 2026-07-17 via a second exchange with the same correspondent. Grade and gaps are stated in the section itself.
- The diagnostic detail behind the (now resolved) `p = 22` obstruction and the three untried construction variants are in `briefs/staircase-allp-findings.md`; the resolution's own diagnosis and independent re-verification are in `briefs/merle-pincer-check-findings.md`. The delegation briefs that scoped the two attempts are `briefs/staircase-allp-brief.md` and `briefs/merle-pincer-check-brief.md`.
- The verification code for all of it is `experiments/staircase_allp.py` (fresh implementation, independent of `experiments/uniform_trim.py`, which produced the original instances).
- The closed anchor walk (`Σ ΔM_t = 0`) and its rigidity — the divisibility structure the size arguments cannot reach — live at `stage4.md` (the increment law) and `bridge.md` §16 (why the deficit is two-sided); the cycle-side statement of what remains is `cycles.md` 12.8.4–12.8.5.
- AEH calibration and its four dissolved anomalies: `aeh.md` §13. None was staircase-shaped; the bulk hypothesis conditions on a size cut and cannot see individual tails by construction.

## Visualizations

Interactive, self-contained single-file HTML lives in `viz/` (the README's repository map lists each one); `viz/cycle_anchor_gateway.html` is the cycle-side gateway.

## How to check a claim

Find the claim's verification line in its wiki section (what was checked, the range, the date, the script name), then run the script: `python experiments/<name>.py`. Scripts are self-contained, use exact big-integer arithmetic wherever a pass/fail decision is made, and print what they verify. If a script's output and its wiki section ever disagree, the section is wrong — that is a bug worth reporting.

## Status vocabulary

- **proved** — has a written proof *and* an independent numerical check by fresh code (not the code that found it).
- **assessed** — a stated judgment with evidence, explicitly not proved; the paper's `thm:staircase` sharpness half is the canonical example.
- **calibrated** — an empirical program executed with controls; says what survived, not what is true.
- **formulation grade** — a definition and its easy direction, recorded to name an open object precisely.
- **floor grade** — a delegation outcome: the attempt's minimum deliverable (extended evidence plus a documented obstruction), reached when the theorem itself was not.
- **parked** — closed by a binding stopping rule (`README.md`), not by resolution; reopens only under the rule's own condition.
