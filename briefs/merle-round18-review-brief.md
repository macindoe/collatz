# Brief: round 18 review window — verify PR #8 (two ledger lines brought up to the record; the collaboration block proposed for collatz-lab.org; a truthfulness pass on his side, for information), settle the Gersonides year, bring HANDOFF item 1 current, prepare the review — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `HANDOFF.md` item 1 (STALE: it still has PR #6 and PR #7 open — this brief's Provenance is current; rewriting it is Item F), `briefs/merle-round16-17-review-brief.md` and `briefs/merle-round16-17-review-findings.md` (the previous window; §8 is the register of the posted reviews), `briefs/merle-round14-review-findings.md` §9.1 (the posted PR #4 review that L-A10's amendment quotes), `briefs/merle-round15-review-findings.md` (our Knight 2025 re-verification and its citation), `publication.md` (DOIs; the Gersonides citation posture), `paper/collatz-reduced-version-history.md` (which version is the latest released one).

## Provenance (current state, 2026-10-18, verified read-only via `gh` by the main session)

- **PR #6 (round 16) and PR #7 (round 17) are MERGED**, both by Merle on 2026-10-02 (06:48 UTC), after a pre-merge commit `2dbb364` on `round-16` applying the two notes of our round-16 review. His letter names the merge commits `bb1510e` and `474125d` — confirm from your own clone; do not take them from the letter.
- **PR #8 (round 18) is OPEN**, opened 2026-10-02 15:00 UTC by `ericmerle3789`, branch `round-18` at **`031c454`** (one commit), base `main`, `+136/−0` over three files: `LEDGER.md` (+3: a reading note at the head; an amendment line under L-A10's `Key status`), `briefs/merle-site-collaboration-block.md` (+72, the proposed public text), `rounds/R18-merle.md` (+61, the letter). Zero reviews, zero comments. The main session has not checked whether his Lean or Junction repos moved since `8cb8a98` / `8bcee67` — check, and record flat.
- **What he asks:** the second key on the two ledger amendments; approval, with amendments, of the collaboration block (it goes online only with our approving review); answers to the block's four open points. §3 of the letter (collatz-lab.org v0.9.0 erratum; six repositories with errata) is for information. One aside: "PROTOCOL §13" does not exist — the PR rule was proposed in R11 §13 and accepted — and he offers to add it to `PROTOCOL.md` in a later round.
- **Any mail of his is the author's.** Do not retrieve email; do not draft a letter.

## The author's decisions (2026-10-18) — carry into the review as given

1. **Gersonides' year:** the author does not hold it; Item C looks it up, and the review answers with what the sources support.
2. **DOI:** pin **v3**, `10.5281/zenodo.21730505` (the reference is static; pinning is the consistent practice). Check that v3 is still the latest released version; if a later one exists, flag it rather than choose.
3. **Naming:** as Merle wrote it is fine. Verify only that the paper's title as he gives it (*Reduced coordinates for the Collatz map*) matches the released v3 exactly; a mismatch is a correction, not a preference.
4. **Entries:** the author is skimming them; the review's entry-by-entry amendments come from Item B, factual only.

## Items

**A. The two ledger amendments.**
1. L-A10: confirm the quoted sentence "The second key turns on L-A10." appears verbatim in our posted PR #4 review (`gh pr view 4 --json reviews`), and that the amendment changes nothing else in the entry.
2. The reading note: at his `main` after the round-16/17 merges, list every entry's first and last `Key status` (or `DRAFT — one key`) line. Confirm the five entries he names (L-A4, L-A6, L-A7, L-A8, L-A9) are exactly the set that opens with a superseded one-key line, and that under the rule "last `Key status` line governs" every entry reads what our record says it is. Any entry he missed, or any entry whose last line misstates its standing, is a finding.

**B. The collaboration block, line by line.** It is public text naming the author; every clause is checked against `LEDGER.md` at his `main` (record the SHA) and against our own record. Build a table: clause → source → verdict (holds / amend / flag) → proposed wording if amended. Checks the main session already knows to be needed (not exhaustive):
- **Knight's citation.** The block says *Discrete Math.* 349 (**2026**), 114812; our L-A11 record says 349(3) (**2025**). Settle volume, issue, year and article number at the publisher's page / DOI. If our own record is the one wrong, that is a correction to our own pages too — flag it for the main session rather than editing in this window, unless it sits in a file this window owns.
- **T1 (L-A8):** "length ≤ 4.95·10¹⁰" against the floor `49547666543`; "weaker than Hercher 2023 (1.375·10¹¹)" against Hercher's stated bound (and its June-2026 corrigendum, on record from round 16); "two continued-fraction facts and one cancellation remain in prose" against our round-16 record (a third unformalized glue fact was named there — check it is the same thing).
- **L-A9:** "a margin of about 0.04" against `0.0383`.
- **L-A7:** the Lean constant `1/13` and "on paper with the exact constant".
- **L-A5:** "the cycle −17 realises an isolated peak".
- **"Bařina's verification to 2⁷¹"**, **"Since July 2026"**, and every per-entry attribution (who proposed, who closed, who corrected) against the entry's own header and our findings files.
- The block's description of method ("fresh code that borrows nothing from the other side") — calibrate against our record; where it overstates (e.g. kernel statements read, not built), say what the record supports.
- The site will show it "in English and French, same content". Our approval can only cover the English; say so in the review.

**C. Gersonides' year.** Look it up. *De numeris harmonicis* (written for Philippe de Vitry): find what the standard secondary sources give for its date and on what evidence — e.g. Carlebach's 1910 edition, Chemla & Pahaut (1992) on Gersonides' mathematical works, Simonson's papers on Gersonides' mathematics, and any primary-source dating (colophon, Hebrew-calendar year). Record each source, what it says, and whether you held it or are relying on a citation of it. Recommend: a single year, or "1342/43" with the reason the sources split. Our own record already disagrees with itself (`briefs/jointnote-*` say "1342/43", `briefs/cycle-gateway-viz-brief.md` says "1343") — list every occurrence in tracked files; fix nothing in this window, flag them for the main session.

**D. His §3 (for information).** No key is asked. Light check only: that nothing on collatz-lab.org's current pages misstates our work (read the pages if reachable; record the date read), and that the attribution "Salikhov's 5.125 is a measure of `ln 3` (your catch, L-A7)" matches our L-A7 record. The rest of his errata (his April theorem, his repositories) are his; do not adjudicate them.

**E. PROTOCOL §13.** The review accepts his offer to add the PR rule to `PROTOCOL.md` in a later round, citing R11 §13 until then — unless our own record shows we cited it differently somewhere that matters; list where we wrote "PROTOCOL §13" in tracked files and flag those for the main session.

**F. HANDOFF item 1.** Bring it current, in place, present tense, no change-log prose (AGENTS.md): PRs #6 and #7 merged with their merge commits; the shared repo's `main` HEAD; PR #8 open at `031c454` with our review prepared, not posted; the ledger-state bullets for L-A8 and L-A10 no longer "not yet on `main`"; repo current values. Leave every gated clause ("review posted", "two keys once posted") in its pre-posting form — the main session flips them after posting.

**G. The review.** Draft the approving review in the register of `briefs/merle-round16-17-review-findings.md` §8: second key on the two ledger amendments (if Item A holds); approval of the collaboration block **with** the amendments of Item B and the answers to his four points (Gersonides per Item C; DOI v3 pinned; naming as written; the entry amendments); PROTOCOL §13 per Item E. Business only — no personal paragraph, no thanks beyond one line. Put it as a section of the findings and stage the body as a standalone UTF-8 (no BOM) file at `briefs/merle-round18-review-body.md`. **Do not post it.**

## Verification

Fresh code, `experiments/merle_r18_check.py`, importing nothing of his: it reads `LEDGER.md` at a pinned SHA of his `main` and at `031c454` (from a fresh clone, `git show <sha>:LEDGER.md`), enumerates the `Key status` lines per entry (Item A.2), checks the L-A10 quote against the PR #4 review text, and recomputes every number the block quotes that our record can reproduce (the T1 floor and its rounding, the L-A9 margin, etc.). **One documented command reproduces the committed output** (`python experiments/merle_r18_check.py > experiments/merle_r18_check_output.txt`); record checks/failures and the date in the findings. Literature items (Knight, Hercher, Gersonides) are recorded as read-at-source or not, with URL/DOI and date.

## Conventions (binding)

- **Do not record a correspondent's tooling.** His PR body carries a tool footer; it does not enter any tracked file, the findings, or the review.
- Credit lines: name and date. No email address in any tracked file. His letter is paraphrased in our files, not quoted at length; short quotes of ledger text are fine.
- A label is not a cause; a reviewer's correction is still a claim — every amendment you propose carries its source.
- Nothing outward: no `gh pr review`, no comment, no push, no email. If any command is denied, stop and hand it back; do not re-route.
- Edit files with the Edit/Write tools only, never PowerShell `Set-Content`; run `python experiments/encoding_scan.py` before the last commit and record the RESULT line.
- Work in the foreground; do not stop until the commits exist.

## Deliverables

Branch `merle-round18-review`, cut from current `main` (**first** `git merge --ff-only main` if your worktree started behind — this brief is committed on `main`; record the base SHA). Commits, content separate from structure:
- `experiments/merle_r18_check.py` + `experiments/merle_r18_check_output.txt`
- `briefs/merle-round18-review-findings.md` — Provenance as verified; Items A–E with tables; the Gersonides source record; the review draft (§ "The review"); "For the main session at merge" (corrections to our own pages, the flipped clauses after posting, anything the author must decide).
- `briefs/merle-round18-review-body.md` — the review body, verbatim-ready.
- `HANDOFF.md` item 1 (Item F), its own commit.
