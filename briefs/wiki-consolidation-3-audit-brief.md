# Brief: wiki consolidation pass 3 — read-only audit

**Branch:** `wiki-consolidation-3-audit`, cut from `d09895c` (verify your worktree's merge-base against `main` before writing anything; if your worktree was cut elsewhere, rebase first — this has gone wrong before).
**Deliverable:** `briefs/wiki-consolidation-3-audit-findings.md`, committed on the branch. **That file is the only thing you create or edit.** No wiki page, no script, no output file, nothing in `paper/`, `sources/`, `experiments/`, `viz/`, no other brief.
**Register:** flat, calibrated prose. Findings state what is, with file:line evidence. No excitement, no advocacy. Where you are unsure, say so in a dedicated section rather than hedging inline.
**Read-only means read-only:** no network operations of any kind (no `ls-remote`, no `gh`, no clones). Repo-state facts about external repositories are recorded from the existing record with their as-of dates, not re-verified.
**Tools:** Edit/Write tools only for file content. Never PowerShell `Get-Content`/`Set-Content` (UTF-8 corruption; see AGENTS.md quirks). Run `python experiments/encoding_scan.py` before committing and record its verdict in the findings.

## Context (pre-verified by the main session 2026-08-12 — do not re-derive, do check current file contents against it)

This is the third consolidation pass; precedent is `wiki-consolidation` (2026-07-17, merge `0ca58ba`) and `wiki-consolidation-sweep`/`-reverse` (2026-07-22, merges `d654b53`/`bf775cd`). Read those two briefs (`briefs/wiki-consolidation-brief.md`, `briefs/wiki-consolidation-sweep-brief.md`) for the practice's shape: status surfaces compressed to the current-answer standard, compression-without-loss, history is git's job.

Ground facts, verified in-session:

- Working tree clean; every branch is merged into `main`; public wiki `main` = local `main` = `d09895c`.
- The staircase-arc branches HANDOFF items 4–10 describe as "awaiting review" are ALL merged: `e42d785`, `da5f06d`, `4538a20`, `b85be16`, `2b9e424`, `3a50eea`, `297f1fa`.
- Shared repo `macindoe/one-obstruction-three-faces` HEAD unmoved at `7c05458`; PR #1 and PR #2 both OPEN, zero reviews (checked 2026-08-12). The Merle arc is quiescent — awaiting his reviews, which are the second keys under the accepted PR medium.
- Page sizes: HANDOFF.md 132 KB (its charter says "current state only"; the 2026-07-22 pass got it to 7.4 KB), itinerary.md 139 KB, aeh.md 92 KB.
- Front-matter dates: program.md / spine.md / stage2.md / stage4.md 2026-07-22, stage1-synthesis.md 2026-07-12, ladder.md / anchor-digit-search.md 2026-07-23 — all pre-dating the staircase all-p closure (cycles.md 12.8.6, 2026-07-29) and paper 1 v3 (published 2026-08-03, DOI 10.5281/zenodo.21730505).

Decisions already made by the author (2026-08-12): full-repo scope; the seven stale printed-string `12.8.6.2` citations in `experiments/` are to be repointed and their committed outputs regenerated (production-phase work — your job is to enumerate them exactly).

## The audit's sections

Produce the findings file with exactly these sections.

### §1 HANDOFF.md de-narration spec

The rewrite target is the current-state standard: what a new session needs, nothing about how it got here. For the production delegate, specify:

(a) **The facts-to-preserve list** — every fact that must survive, quoted or pinned, each with its current HANDOFF line. At minimum, verify and list: the onboarding order, register norm, and author-role paragraphs; the State-of-the-fronts bullets (re-dated); the standing conventions (sending stays with the author; verbatim pastes; two-key protocol; the accepted §13 PR medium — one round per PR, second key = the approving review); the standing decisions block (credit, hosting pinned to v2, venue, Gersonides posture, gateway viz, credit-deflection on file); the ledger state L1–L-A9 with grades and key status, compressed to one block; the live conditions (PR #1/#2 open awaiting the second keys; the `[GRADE AT SIGNING…]` bracket must not survive into the signed note; the L-A9 grade line restates per whatever h1 becomes; round 13 runs under the new medium; the Zenodo metadata line on the frozen Version note deliberately unaddressed, the author's 2026-08-03 decision; ccchallenge's v1 pointer noted flat); the Merle credit language, verbatim; items 2 and 3 (KL–LP residual, longer-horizon items); the delegation pattern; the infrastructure quirks.

(b) **The drop-map** — for each narrative block to be dropped (the round 8–12 narration, the "Superseded" paragraphs, the closed-window reports), name where the dropped facts live: the specific `briefs/merle-*` or staircase findings file, or the merge SHA. This is the compression-without-loss invariant; the reviewer will spot-check it. Any fact that has NO home outside HANDOFF gets flagged — it must be preserved or given a home, not dropped.

(c) **Stale-label corrections** — every "awaiting review" / "not merged" / "NOT pushed" claim in HANDOFF that the ground facts above contradict, with line numbers.

### §2 Periodic status pass (AGENTS.md)

For every wiki page, diff its claims about *other* pages against those pages' own front matter and current state. Table: page, line, the claim as written, the owning page's current answer, proposed fix (one line). Suspects to check first (but sweep everything): program.md, spine.md, stage1.md (including the compact ledger 11.8.4.5), stage1-synthesis.md, stage2.md, stage3.md, stage4.md, ladder.md, anchor-digit-search.md, index.md (both the table and the status paragraph), README.md, TOUR.md, publication.md, open-problems.md (calibration notes), bridge.md, anchors.md, cycles.md, reverse.md, itinerary.md, aeh.md. The three big post-07-22 events any of them may be stale against: the staircase all-p closure with its scope (unconditional p ≥ 16, finite check 3 ≤ p ≤ 15, p ∈ {2,4} by exhibition, γ bracketed 3.683012–5.140212), v3 published (and v2 archived to `sources/paper/`), and the Merle arc's current standing. Do not propose editing any mathematical statement — status surfaces and cross-claims only.

### §3 Convention violations

Against AGENTS.md's "No change logs in tracked files" and the front-matter standard: running narration, "was X, now Y" prose, dated verification-record *appends* (the rule is one current line, overwritten), and front-matter `status:` fields that have grown past the short-state-word-plus-pointer standard (the 2026-07-17 pass set reverse.md's to ≤ 3 lines; aeh.md's current `status:` is a paragraph — assess all pages). List each with location and a proposed trimmed form. Wiki pages only — `briefs/` are records of their moment and are exempt.

### §4 Cross-reference gaps

Facts stated in one page that other pages should point to and don't, or pointers that now resolve to moved/renamed content. Include a check that every `12.8.6.x` citation across the wiki resolves to the *rewritten* §12.8.6 correctly (the numbers kept their roles at the rewrite, but check the claims made about them at each citing site).

### §5 itinerary.md and aeh.md: bloat assessment

139 KB and 92 KB. Assess against the conventions only: do they carry narration, duplicated status claims, superseded-formulation prose that belongs in `archive/`, or are they just large because the mathematics is large? Propose nothing unless a convention is actually violated; "big" is not a defect.

### §6 The seven printed-string citations

`briefs/record-consistency-sweep-findings.md` records six comment/docstring `12.8.6.2` citations repaired and seven left in printed strings because repointing changes committed output. Enumerate all seven exactly: script, line, the string, which committed output files regenerate, and the re-run command. Confirm the six repaired ones still resolve. The production phase will repoint and regenerate; spec the mechanics so it is one clean commit.

### §7 briefs/ supersession headers

Candidates only where a later reader would be actively misled (precedent: the header on `briefs/staircase-allp-findings.md`). List: file, the misleading claim, the one-line header proposed. Do not propose headers for files that are merely dated.

### §8 Proposed production split

Recommend the branch split (precedent: one HANDOFF branch, one sweep branch), application order, per-edit risk grade (mechanical / judgment / author-level), and a reviewer checklist. Flag any edit that must be its own commit (content vs structure separation).

### §9 Lower-confidence items

Anything you are not sure of, stated plainly, separate from the confident findings.

## Guard rails

- `12.8.5`, the PARKED cycle front, and the three README stopping rules: confirm by reading that no proposal touches them, and say so.
- The Merle credit language and standing decisions: verbatim preservation, never paraphrase.
- No mathematical statement is edited, ever, in this pass. Where a status-pass fix touches a sentence containing mathematics, the proposal quotes the exact before/after so the reviewer can see the mathematics is unmoved.
- Where this brief contradicts what you find in the files, the files win — record the discrepancy in §9 and follow the file (the round-10 lesson: where a brief contradicts a findings file, the findings file wins).
