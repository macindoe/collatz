# Brief: record-consistency sweep — five small items left undone after the staircase arc — for a delegated session

**Context required before starting (in order):** `README.md`, `AGENTS.md` (every fact lives in exactly one page; no change logs in tracked files; conservative editing; `sources/` immutable), `cycles.md` §12.8.6 **as it now stands**, and `briefs/staircase-status-apply-findings.md` (which recorded four of these five and lists the sites).

Round 11 is closed on both sides and the staircase arc is applied. Five small record-consistency items were recorded and deliberately left; this window clears them. None is mathematical — do not change a claim, a constant or a status word anywhere.

## Queue

1. **The mis-resolving `experiments/` citations — the only one with a live consequence.** Six scripts cite "Construction `12.8.6.2`" meaning the **superseded pure-geometric profile with partial-sum rounding**. After the rewrite, `12.8.6.2` is **Construction B**, so every one of those citations now points at the wrong object. Sites recorded in the apply findings: `staircase_allp.py`, `staircase_allp_construction.py:250`, `staircase_allp_diophantine.py:1010`, `merle_pincer_check.py`, `merle_round3_check.py`, `p22_passer.py`, `prime_local_probe.py:939`.
   - **Verify each site before touching it** — read enough context to confirm which object the script actually means. Some may legitimately mean Construction B, or mean the *section* rather than the construction; those must be left alone. The recorded list is a starting point, not an instruction.
   - Repoint the genuine ones at **`12.8.6.3`**, which now carries the superseded route in place, and where necessary add three or four words naming which object is meant so the citation survives the next renumbering.
   - **Do not change any script's behaviour.** Comments and docstrings only; no code, no output. Confirm by re-running each edited script and checking its committed output is unchanged — or, where a script is expensive, by confirming the diff touches only comment lines.
2. **`TOUR.md`'s "floor grade" vocabulary entry** is now unattached — nothing in the wiki carries that grade since §12.8.6 was rewritten. Either repoint it at a live example or retire the entry. The status-apply session kept it and recorded that as a judgment call; make the call now, and if you retire it check no other page's status vocabulary depends on it.
3. **`HANDOFF.md` duplicate item numbering** — this session's paragraphs left the numbered items out of sequence. Renumber so the list reads correctly. Structure only; change no content, and do not consolidate or summarise any paragraph.
4. **`briefs/staircase-allp-findings.md`** — add a one-line header noting it is superseded, with pointers to the three findings files that replaced it. It records a floor-grade result whose target was later refuted, and a reader arriving cold should learn that in the first line. `AGENTS.md` keeps failed routes; this makes the route legible rather than removing it.
5. **`README.md` line 53** still calls the uniform trim "the open objective" in the repository-map row for `cycles.md`. That predates this arc by a long way and is simply stale — the uniform trim question was resolved before the correspondence began. Correct the row to describe what `cycles.md` is now. Do not expand it into a summary of §12.8.6; one clause.

## Record

`briefs/record-consistency-sweep-findings.md` — each item, what you found, what you changed, and anything you left alone with the reason (item 1 in particular will have sites that should not move). Plus ONE scoped `HANDOFF.md` paragraph, folded into the renumbering of item 3.

## Rules

- Branch **`record-consistency-sweep`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA in your launch instructions, and state the base SHA.
- One commit per item; structure separate from content.
- **Change no claim, constant, status word or piece of mathematics.** If an item seems to require one, stop and record why instead.
- Do not touch `paper/`, `sources/`, `cycles.md` §12.8.3 or §12.8.6, or any ledger/correspondence material. Nothing for the shared repo.
- No pushes.
- Encoding: Edit/Write tools only, never PowerShell `Get-Content`/`Set-Content`; run `experiments/encoding_scan.py` before your last commit.
- Stop after item 5.
