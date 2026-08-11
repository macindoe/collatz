# Brief: the printed-string `12.8.6.2` repoint + output regeneration

**Branch:** `experiments-12862-repoint`. Verify your worktree contains merge `049bda3` (the audit merge) before writing anything; rebase onto current `main` if not.
**Authority:** `briefs/wiki-consolidation-3-audit-findings.md` §6 (the site table, the mechanics paragraph) and §9 items 1–3. The author's decision (2026-08-12) is on record: repoint and regenerate. Verify every site against the current file by quoted string, not line number.
**Deliverable:** ONE commit — scripts and regenerated outputs together, message naming every site — plus `briefs/experiments-12862-repoint-findings.md` (the per-site before/after strings, the output diffs summarized, the encoding-scan verdict, run times).
**Register:** flat, calibrated. **Tools:** Read/Edit/Write for file content; never PowerShell Get-/Set-Content. **Output regeneration must not go through PowerShell `>`** (BOM-stamps the file — this exact fault is in the record); run the scripts from Git Bash redirection or write output Python-side. `python experiments/encoding_scan.py` before committing.

## The sites (audit §6 table + two reviewer additions)

Sites 1–7 per the audit's table. Additions, both approved at review:

- **Site 8** — `experiments/merle_pincer_check.py` f-string ("Correction runs (algorithm 12.8.6.3 via Section 1's instrumented copy): … base construction 12.8.6.2."): **confirmed live by main-session trace** — `print(item2c_correction_runs())` at line 755 — so it joins the commit. No committed output exists for this script; no regeneration needed for it.
- **Site 9** — `experiments/staircase_allp_diophantine.py:6`, the "floor-grade result at cycles.md 12.8.6" docstring clause: comment-only repair (12.8.6 is now proved with scope), no output change.

**The double-citation subtlety — read cycles.md §12.8.6 as it now stands before editing these:** sites 1–2 (`p22_passer.py`: "construction 12.8.6.2 + N correction moves of 12.8.6.3") and site 7 (`staircase_allp_diophantine.py`: "Recipe of 12.8.6.2 + 12.8.6.3") cite BOTH old numbers — the old `12.8.6.2` (the pure-geometric profile, now `12.8.6.3`) and the old `12.8.6.3` (the correction algorithm). A bare number-swap would produce "12.8.6.3 + … of 12.8.6.3". Confirm from the current cycles.md where each object now lives and write the object names into the strings (audit mechanics: "the superseded pure-geometric recipe/profile" / "the correction algorithm", with the section numbers as they now resolve). Record the mapping you used in your findings.

## Regeneration and verification

- `staircase_allp_construction.py` → replaces `staircase_allp_construction_output.txt` (~400 s). Diff against the committed predecessor: only the repointed strings and wall-clock columns may differ; every check count and 0-failures line byte-identical. If anything else moves, STOP and record — do not commit.
- `staircase_allp_diophantine.py` Part 3 → replaces `staircase_allp_diophantine_part3.out` only (the committed `.out` set is a documented concatenation; `staircase_allp_diophantine_note.txt` explains the split — regenerate Part 3 per its documented invocation, nothing else). Same diff rule. This is the expensive run (per-period cost ~`n^1.585`); budget accordingly and record the run time.
- Scripts with no committed output (sites 1–3, 8): run or trace enough to confirm the edited strings render, record the check in the findings (no output file committed).

No network operations. No file outside `experiments/` and your findings file is touched. Commit message ends with:

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
