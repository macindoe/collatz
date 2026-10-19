# Brief: draft paper 1 v4 from the checklist — corrected attribution, the sharpness stated and proved (12.8.6, 12.8.7), every v3 note absorbed — source and PDF, not published — for a delegated session

**Why.** The author decided (2026-10-18) on a proper v4 rather than further notes on v3, and (2026-10-19) to proceed on the main session's recommendations. Everything v4 must carry is in `briefs/paper1-v4-items-findings.md` (the checklist, rows with sources, decisions D1–D15) and its three placeholders are now resolved: `[[12.4]]` → `briefs/cycles-12-4-recheck-findings.md` (`m = p`); `[[F]]` → `briefs/williams-letter-findings.md` (F answers Williams's open problem (1) **in part**: where the trajectory lands, not which skeleton); `[[X0]]` → `briefs/staircase-x0-threshold-findings.md` §9 and `cycles.md` 12.8.7 (including its list of what v4 must **not** say).

**Context required before starting:** `README.md`, `AGENTS.md`, `paper/collatz-reduced-v3.tex` (all), `paper/collatz-reduced-version-history.md`, the four findings files above, `briefs/ceiling-novelty-refresh-findings.md`, `briefs/ceiling-ccchallenge-sweep-findings.md` (its Williams lines are calibrated to "in part"), `cycles.md` 12.4, 12.8 (all, incl. 12.8.6, 12.8.7), `publication.md`, HANDOFF.md's LaTeX quirks (build in a sandbox temp dir; the mount locks aux files; `\wp`/`\dp` are primitives — the paper uses `\wnext`, `\dnext`).

## Decisions (the author's, 2026-10-19 — apply as given)

- **D1:** Theorem 4.5 keeps its number; its header carries the attribution (Rozier 1991; Simons–de Weger 2005; Brox 2000 for finiteness per `m`), and the text calls ours a rederivation by another route with `m = p`.
- **D2:** state the all-period sharpness with its proof (12.8.6: the `γ` bracket `[3.683012, 5.140212]`, the scope words — unconditional `p ≥ 16`, finite check `3 ≤ p ≤ 15`, exhibition at `p ∈ {2,4}`); retire "nothing new is proved in this paper". Proofs may be condensed with pointers to the record for the finite checks, but every stated claim must be proved in the paper or cited to a pinned record location.
- **D3:** include the `X₀`-threshold form (12.8.7) — necessity, the deep-crash construction, availability for `p ≥ p₁(X₀)`, `Λ ≥ 0.054·2^{−ε_p n}` — and the crash-depth-1 obstruction as a remark; the ordinary-scale family's Corollary-5-only status as one sentence or omitted (drafter's judgment, flagged).
- **D4:** drop "Our main new theorem"; the abstract states the sharpness plainly with its credit chain ("realizes Rozier's 1991 extremal, which Simons–de Weger expected in 2005"; the `p = n`-parameter analogue and the divisibility moral are Halbeisen–Hungerbühler 1997).
- **D5:** provenance — keep the authorship sentence (the 2023-03-13 note) true as authorship; **delete** "any overlap with contemporary work lies in that layer, not in the coordinate system"; cite the cascade's classical sources (Steiner 1977; LaDue 2018; Rozier 1990) and Williams 2026 as independent and earlier public for the states; say F/§3 answer Williams's open problem (1) in part, in one sentence, exactly at the calibration.
- **D6:** the Author's note stays in the author's voice: leave v3's text in place with a `% AUTHOR:` comment marking every sentence the findings make wrong; do not rewrite it.
- **D7:** cite Rozier 1990, LaDue 2018, Böhm–Sontacchi 1978 (only after checking its statement at a primary or reliable secondary source — record which); not Steiner 1981.
- **D8:** no contact needed before v4 (Williams is being written to separately).
- **D9:** keep `T`; fix line 405's clash.
- **D10:** cite Merle's paper at a pinned version.
- **D11:** the v4 version note: one paragraph, a `% DOI:` placeholder for the minted DOI.
- **D12:** out of scope here (register requests are the author's after minting).
- **D13:** re-pin Appendix A's and the Status paragraph's commit references with a `% PIN-AT-BUILD` marker (the wiki's `main` is not yet pushed; do not cite unreachable commits as reachable).
- **D14:** Thm 3.3's Baker clause scoped to `ω ≠ 1`, the `ω = 1` case by the isometry (`s = 2 + v₂(d)`), per the wiki's fix `d2cd6c6`.
- **D15:** the joint note cites Thm 4.6 by number — D1 keeps it valid.

## Rules and deliverables

Do not upload, mint, or touch Zenodo/ccchallenge; nothing outward; if a command is denied, stop and report. Do not edit wiki pages (a separate window is aligning them). Edit/Write only; encoding scan before the last commit. Foreground until committed; the LaTeX build runs in a temp dir and must succeed with no undefined references. Branch `paper1-v4-draft` from current `main` (`git merge --ff-only main` first if behind; record the base SHA). Deliverables:
- `paper/collatz-reduced-v4.tex` and the built `paper/collatz-reduced-v4.pdf`;
- a draft v4 section for `paper/collatz-reduced-version-history.md` (what changed from v3, per its genre);
- the Zenodo description text for v4 (with the abstract — v3's record lacked one, which is why ccchallenge kept v1's) at `briefs/paper1-v4-zenodo-description.md`;
- `briefs/paper1-v4-draft-findings.md`: checklist row → v4 location → done / changed / deferred, the `% AUTHOR:` and `% PIN-AT-BUILD` markers listed, a sentence-level sweep of the v4 abstract, related work and version note against the findings (no "new" for anything subsumed), and the author's remaining decisions.
