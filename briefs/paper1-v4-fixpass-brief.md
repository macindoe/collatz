# Brief: v4 fix pass before the content lock is tagged — tighten the 19 loose sentences (U1–U19), settle the author items, re-cut the claims ledger — for a delegated session

**Why.** `briefs/paper1-content-lock-findings.md` §3 lists 19 places (U1–U19) where v4's prose says more than the statement behind it, or carries no support in v4. The author decided (2026-10-19) to fix them before the lock is tagged, so the readability rewrite does not faithfully preserve them. The rewrite that follows will renumber freely and print a concordance; v3 stays the pinned citation for Merle's work, so nothing outside breaks.

**Read first:** `README.md`, `AGENTS.md`, `paper/collatz-reduced-v4.tex`, `paper/collatz-reduced-v4-claims.md`, `briefs/paper1-content-lock-findings.md`, `briefs/paper1-v4-draft-findings.md`, HANDOFF.md's LaTeX quirks.

## Items

1. **U1–U19.** For each: tighten the sentence to exactly what the statement behind it supports (or what the record proves, with a pointer), or add the missing support (a script pointer in the verification index, the Rackl bibliography entry, the proof or a pinned pointer for each unproved display). Never strengthen a theorem to match loose prose; always weaken the prose to match the theorem. Each fix gets a row in the findings: U-id → v4 location → old text (short) → new text → source.
2. **Author's decisions (2026-10-19), apply as given:**
   - **A-4 keep:** Appendix A's "the AI collaborators carried out the mathematical development" stands for both phases — the author explored the seed by hand and the project has outgrown hand work; the hand computations are already named. Remove any `% AUTHOR:` flag on it.
   - **A-5 cut:** the canonical-scale sentence (D3) at the end of "The threshold, explicitly".
   - **A-6 cut:** keep the optional items out (gcd rotation-invariance, the Tao p. 2 / Prop 1.11 refinement, the Knight clause).
   - **A-7:** check the Sós 1958 entry (and the Świerczkowski 1958 entry beside it) at a source — publisher page, zbMATH, or MathSciNet-mirroring record — and correct it if needed; record held/cited.
   - **A-2:** delete the line-61 `% AUTHOR:` comment (that sentence is accurate).
   - **A-1 propose, do not apply:** draft one replacement for the Author's note's second item (the uniform-trim sentence, wrong since the trim is Rozier's and Simons–de Weger's), in the author's plain first-person voice, as a `% AUTHOR-PROPOSED:` comment beside the current text, which stays until the author approves.
3. **Re-cut the claims ledger** to the fixed v4 (same IDs where the claim is unchanged; changed rows marked), and record the counts.
4. Rebuild the PDF (temp dir; 0 undefined references), encoding scan, commit (content and structure separate).

## Rules and deliverables

Change no theorem's mathematics. Nothing outward; if a command is denied, stop and report. Edit/Write only. Foreground until committed. Do not edit wiki pages. Branch `paper1-v4-fixpass` from current `main` (`git merge --ff-only main` first if behind; record the base SHA). Deliverables: the fixed `.tex` and PDF, the re-cut ledger, `briefs/paper1-v4-fixpass-findings.md` (the U table, the author-item outcomes, the Sós/Świerczkowski check, the proposed A-1 wording verbatim, anything left for the author).
