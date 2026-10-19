# Brief: align the wiki with the ceiling's settled credit chain and 12.8.7 — publication.md, index.md, TOUR.md, README.md, cycles.md 12.7.3 / 12.8.1–12.8.2, HANDOFF — for a delegated session

**Why.** Five windows merged 2026-10-18/19 changed the standing of paper 1's ceiling: the trim is Rozier 1991 / Simons–de Weger 2005 / Brox 2000; the sharpness is partially anticipated (Rozier 1991 p. 11 real extremal; SdW 2005 p. 69 belief; Halbeisen–Hungerbühler 1997 in the length parameter); `m = p` (cycles.md 12.4, corrected); the sharpness now holds at SdW's threshold (cycles.md 12.8.7, new); the `(ω, d)` states are independently Williams 2026; F answers Williams's open problem (1) in part. The pages that state the old standing have not been updated — AGENTS.md's status-change workflow and "every fact in one page" rule apply.

**Context required before starting:** `README.md`, `AGENTS.md` (the workflows, esp. "When a result's status changes" and the periodic status pass), `briefs/ceiling-novelty-refresh-findings.md` §5 (proposed wordings), `briefs/ceiling-ccchallenge-sweep-findings.md` §6 (proposed wordings, Williams lines calibrated to "in part"), `briefs/cycles-12-4-recheck-findings.md` (affected-sentence list), `briefs/staircase-x0-threshold-findings.md` (its "pages left for the main session" list), `briefs/williams-letter-findings.md`, `briefs/paper1-v4-items-findings.md` (the TOUR.md line-22 note).

## Items

1. `publication.md`: the 12.8 line and the Reduced-blocks line, at their current standing (the findings' proposed wordings, adjusted for 12.8.7 and the "in part" calibration); the status line and Current-state paragraph; one dated verification line, no change-log prose.
2. `cycles.md`: 12.8.1–12.8.2 carry the attribution (Rozier 1991, SdW 2005 Lemma 7 / Lemma 14 / Thm 3(d), Brox 2000), conservatively — credit only, no proof change; the Current-state paragraph mentions 12.8.7; 12.7.3's "`p ≤ 68` remain subsumed by Simons–de Weger" brought to Hercher's `m ≤ 91` (which the same paragraph cites) via `m = p`.
3. `index.md`: the cycles.md row and status summary; the resolver gains 12.8.7 (no renumbering).
4. `TOUR.md`: the uniform-trim dictionary row (it says "no literature name" — now it has one); the threshold "elements" gloss note; the line-22 claim that paper 1 names the one-division map "in words only" (inaccurate — v3 line 405 uses `T`); the `(ω, d)` row gains Williams 2026.
5. `README.md`: the strategy paragraph's account of the uniform-trim resolution — the trim is classical, the sharpness at both thresholds is the record's; stopping rules unchanged.
6. `experiments/williams_coordinate_check.py`: docstring statement numbers to the published Prop 2.2 / Thm 2.3 (comment only; re-run and confirm the output is unchanged).
7. HANDOFF.md: a short current-state entry for the paper 1 v4 work (in progress; what is decided; where the checklist and draft live) — present tense, no journal.
8. A periodic status pass limited to these claims: grep every tracked page for "uniform trim", "staircase", "dichotomy", "main new theorem", "Simons", "Rozier", "Williams", "12.4", "deep-entry" and list any remaining statement that contradicts the new standing; fix it if it is on a page this window owns, else list it.

## Rules and deliverables

Conservative edits: credit and standing only, no proof changes, no renumbering. Do not edit `paper/` (a separate window drafts v4) or anything in the shared Merle repo. Nothing outward; if a command is denied, stop and report. Edit/Write only; encoding scan before the last commit. Content and structure in separate commits. Foreground until committed. Branch `ceiling-wiki-alignment` from current `main` (`git merge --ff-only main` first if behind; record the base SHA). Findings `briefs/ceiling-wiki-alignment-findings.md`: every edit with its source, the status-pass list, anything left for the main session.
