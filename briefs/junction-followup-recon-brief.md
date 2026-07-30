# Brief: Junction follow-up recon — his §§1–2 repairs, verified read-only — for a delegated session

**Context required before starting (in order):** `README.md`, `AGENTS.md`, `HANDOFF.md` item 1 (the round-10 Junction recon paragraph and the round-11 public recon paragraph — the posture sentence in them is binding here too), `briefs/junction-public-recon-findings.md` (the three NOT-FOUND verdicts this window closes out), `briefs/merle-round12-letter.md` Part 2 §§1–2.

## Provenance

Our round-11 recon recorded three points of his account NOT FOUND in any public ref: no `AUDIT_V9`, no `STATUS.md`, and `PROOF_ASSEMBLY.md` §10.6 still closing "No gap remains" — with the posture sentence that absence of a public copy is not evidence against his account. His round-12 §§1–2 now explain and repair all three, and the explanations are specific enough to verify:

1. **AUDIT_V9** (`AUDIT_V9_PORTEE_2026-07-25.md`): existed at `audits/` in `Collatz-Junction-Theorem`, branch `proof-assembly-v1`, commit `98b2de6` (2026-07-25 11:30:01 +0200) — at our recon time exactly one commit ahead of `origin/proof-assembly-v1`, never pushed. Now pushed; "AUDIT_V9 is public."
2. **STATUS.md**: never committed in any ref because it sat on line 52 of his own `.gitignore` under "Internal project management (not for publication)". Now committed, the `.gitignore` line gone with the reason recorded in its place; content per his description: the scope statement — non-existence proved for `3 ≤ k ≤ 200` only, the preprint's Hypothesis (H) for `k ≥ 69` quoted, and the plain does-not-prove sentence.
3. **PROOF_ASSEMBLY.md**: the withdrawn claim was not one line but **eighteen markers'** worth at `b38758d` (his count moved 7 → 14 → 18 across three passes — the sequence is his finding, record it as such); a permanent RETRACTED block now tops **both** copies (the `collatz-cycles-lean` copy and the Junction copy), stating what was claimed, why it is false, where the current record is, what survives, and the does-not-prove sentence, with nothing deleted. Commits: `collatz-cycles-lean` `d7dbb7a`, `995c98c`, `b38758d`; `Collatz-Junction-Theorem` `6de1743`, `ff27436`, `8ff1010`; the push carried `98b2de6` with it. He also claims the file inside `98b2de6`'s tree is byte-identical to the `collatz-cycles-lean` working copy of that moment (his diff, no output).

**Stopping-rule compliance:** read-only external recon; nothing mathematical.

## Queue

1. Fresh read-only clones (scratchpad) of `Collatz-Junction-Theorem` and `collatz-cycles-lean` (all branches). Record HEADs and the refs you fetched.
2. **AUDIT_V9:** confirm the file exists publicly at the named path/branch; confirm commit `98b2de6` and its date; record the commit's parent/position (his "one commit ahead of origin at your look" is unverifiable from outside — record what IS visible: when the commit became reachable from a public ref, i.e. which push carried it, from ref logs if exposed or from the commit graph; state plainly what cannot be established read-only, without implication either way). Record the file's own verdict line(s) — the round-11 recon found the public series stopped at V8 ("l'abstract suraffirme"); record how V9 relates.
3. **STATUS.md:** confirm committed; confirm the `.gitignore` no longer carries it and that a reason is recorded in its place (quote it); confirm content matches his three-point description (quote the load-bearing lines).
4. **PROOF_ASSEMBLY.md:** at `b38758d`, count the markers yourself against his eighteen (list line numbers; his named lines 7, 113, 175, 202, 272, the §10.6 heading at 294, 315, and §6's heading among them); confirm the RETRACTED block tops both copies with all five stated elements; confirm nothing was deleted (the markers annotate, the assertions remain visible); verify his byte-identical claim between the two copies at the commits he names (`git cat-file` both blobs, compare hashes — his diff was against a working copy, yours is against the committed trees; state which pair you compared).
5. **The push structure:** confirm the three-passes-then-push order he describes is consistent with the commit graph and dates (three retraction commits per repo, then the push carrying `98b2de6`); record flat, no adjudication of intent.
6. **Deliverable:** each of the three round-11 NOT-FOUND verdicts moved to its new state (CONFIRMED / PARTIALLY CONFIRMED / still not establishable, item by item), with the round-11 posture sentence carried forward explicitly — and its resolution noted where it resolves: this is the case where the account was true and the copy was simply not public. One paragraph of reply material: what we verified, flat and kind, in the register of the round-11 repositories-thanked-for paragraph.

## Record

- `briefs/junction-followup-recon-findings.md` — the record. No verification script is needed unless you find yourself computing something (marker counts by grep are recorded as counts with the pattern stated); if a script does become warranted, `experiments/junction_followup_recon_check.py` + output.
- Do NOT edit `HANDOFF.md` or `briefs/junction-public-recon-findings.md` (supersession is recorded at merge by the main session). Five windows run in parallel this round.

## Rules

- Branch **`junction-followup-recon`** from your worktree HEAD. FIRST verify the worktree contains this brief; if missing, merge/rebase onto local `main` first; state your base SHA in the findings.
- Read-only everywhere: clones and public API reads only; **no interaction of any kind** with his repositories (no fork, issue, PR, comment, star, watch, follow); no web beyond GitHub.
- File edits via Edit/Write tools only; run `experiments/encoding_scan.py` before your final commit and record RESULT: CLEAN.
- The standing posture is binding: what cannot be established read-only is recorded as such, plainly and without implication. Where his account is confirmed, say so at full weight — the round-11 verdicts were NOT FOUND, not disbelieved, and the difference matters to how this is written.
- No reply paragraphs beyond the one deliverable paragraph; do NOT merge. Stop after Record.
