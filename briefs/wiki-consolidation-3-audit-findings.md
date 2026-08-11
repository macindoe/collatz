# Findings: wiki-consolidation-3-audit — the pass-3 read-only audit (2026-08-12)

Brief: `briefs/wiki-consolidation-3-audit-brief.md`. Branch `wiki-consolidation-3-audit`.
**Base SHA `7b6ef15`** (the brief commit) — the worktree was cut from `d09895c`, one
commit behind; the branch was fast-forwarded onto `7b6ef15` before any work began.

Read-only throughout: this file is the only thing created or edited. No network
operation of any kind was performed; every repo-state fact below is from the local
tree and log. `python experiments/encoding_scan.py`: **CLEAN** (447 tracked files,
0 invalid, 0 BOM, 0 double-encoding), run before this commit.

Ground facts re-verified in-tree: all seven staircase-arc merges are ancestors of
`main` — `e42d785` (staircase-allp-construction), `da5f06d` (staircase-allp-diophantine),
`b85be16` (staircase-status-audit), `4538a20` (record-defects-repair), `2b9e424`
(staircase-gamma-upper), `3a50eea` (staircase-status-apply), `297f1fa`
(record-consistency-sweep). Line numbers below are from this tree at `7b6ef15`;
locate by quoted text at production time, since edits shift lines.

**Guard rails, confirmed by reading (not assumed):** `cycles.md` 12.8.5 (line 297,
including its closing "unchanged by 12.8.6 below, at any grade" sentence), the
PARKED front (cycles.md front matter line 2, 12.8.5, 12.8.6's own preamble), and
the three README stopping rules (README.md lines 32–38: the ladder retired /
reopen only on a divisibility-aware idea / equidistribution proof effort waits on
an idea) were each read in full. **No proposal in this file touches any of them.**
The one proposal nearest to them (§2 item 6, program.md line 99) aligns a stale
paraphrase *with* those rules and changes nothing about them.

---

## §1 HANDOFF.md de-narration spec

HANDOFF.md is 121 lines, 132 KB; the whole excess is item 1 (lines 27–93, the
Merle arc, ~110 KB) plus items 4–10 (lines 99–108, the staircase arc, ~25 KB).
Lines 1–25 and 110–121 are already at the current-state standard. The file's own
charter (line 3: "it carries the current state only") is the rewrite's warrant.
One structural fact worth the rewriter's attention: the round-11 CLOSURE
paragraph (line 63) sits *before* the round-11 working paragraphs (lines 67–70,
74, 78) — the chronology is scrambled by parallel appends, so a reader cannot
recover current state by reading forward. Target size on the 2026-07-22
precedent: ≈ 8–10 KB.

### (a) Facts-to-preserve (each pinned to its current line)

Structure and norms — keep verbatim in substance:

1. Charter sentence (line 3), onboarding order 1–4 (lines 7–10).
2. Register norm (line 12) and the author's-role paragraph (line 14) — keep both
   verbatim; they are the author's explicit preferences.
3. Delegation pattern (lines 110–112).
4. Infrastructure quirks, all five (lines 116–120): stale sandbox reads;
   the PowerShell Get-/Set-Content UTF-8 hazard with the `encoding_scan.py`
   instruction and the no-mojibake-sample rule; the Gmail numeral garbling;
   LaTeX aux locking; `\wp`/`\dp` primitives. Keep in full — these are
   load-bearing operational rules, not narration.

State of the fronts (lines 18–23) — keep all six bullets, re-dated (the block
currently carries no as-of date). Verified current against the owning pages,
with one internal exception noted in (c) item 9. The papers bullet (line 23)
carries the only wiki-wide statement of the v3 headline set (v3 DOI
10.5281/zenodo.21730505, published 2026-08-03, 15 pages; v1 10.5281/zenodo.21273548,
v2 10.5281/zenodo.21421120, mirror 10.5281/zenodo.21303918; repair history at
`paper/collatz-reduced-version-history.md`) — preserve exactly.

Item 1 (Merle), the facts that must survive:

5. **Standing conventions** (line 29): sending/acks stay with the author;
   verbatim pastes of Merle's replies (Gmail garbles numerals); two-key/three-repo
   protocol. Plus the **accepted §13 PR medium** (line 83, decision 2; enacted
   lines 89/91): the technical half moves in PRs, one round per PR, the second
   key = the approving review; mail keeps everything that is not a claim.
6. **Repo facts, at their CURRENT values** (the frozen values inside line 31 are
   stale — see (c) item 9): shared repo `github.com/macindoe/one-obstruction-three-faces`,
   **public** (flipped by the author 2026-07-24), HEAD **`7c05458`** (line 83),
   with PR #1 branch `round-12` pushed at `accda4b`, tree `8e9b1eb` (line 89) and
   PR #2 branch `note-v1-draft` pushed at `96ccadf`, tree `d374546` (line 91);
   contents PROTOCOL.md (§7 acceptance in-file), LEDGER.md, NOTE.md; his handle
   `ericmerle3789`; his Lean repo `ericmerle3789/one-obstruction-three-faces-lean`,
   HEAD **`d48ba9e`** (line 83), `rounds/R11-merle.md` at `d48ba9e`.
7. **Ledger state, one line per entry with key status** (from lines 31, 35, 37,
   39, 43, 45, 47, 59, 61, 63, 70, 83, 85, 89): L1 (corrected, both directions);
   L2 (two keys); L3 (corrected by him 2026-07-24, accepted into the two-key
   record at `c40aa58`); L4 (AEH replication, our key turned); L-A1 (transport
   recurrence — two keys + kernel; **credit: independent simultaneous discovery,
   both names**); L-A2 (repeated-word gcd law, two keys, `ec4f229`); L-A3
   (two keys, the (B) margin-quantification additions, conditional date-stamped);
   L-A4 (descent, two keys + the ContentDescent kernel key on the structured
   half, `08dc3d5`/`67c428a`); L-A5 (adelic content invariant, **two keys via
   `49351e5`**, closure-verified); L-A6 (calibrated lottery, two keys scoped,
   pushed `641a530`); L-A7 (torsion ruler, **two keys** — the Rhin 1987 /
   Simons–de Weger 2005 re-sourcing accepted, headline `n ≈ 2233`; the margin
   inequality now **proved on both sides**, ours at the true `c_gen` with
   uniform surplus `1 + log₂β`); L-A8 (T1/no-hair, **two keys on the
   mathematics**, kernel claims scoped to the read-not-built audits, the
   ceiling repair verified, entry in his own proposed wording via `1d7907c`);
   L-A9 (δ8 impossibility, **seeded one key his at `78f80f0`**; our
   turn prepared **split-grade, conditional on offer h1**, carried in PR #1).
8. **Standing decisions block (line 33) — VERBATIM, never paraphrase**: L-A1
   credit (independent simultaneous discovery, both names); hosting on
   collatz-lab.org approved, **DOI-pinned to v2** (10.5281/zenodo.21421120),
   mirror-paper pair offered; venue for the joint note number-theory-shaped,
   formalization as supporting artifact; citation posture Gersonides 1342/43,
   not Mihailescu; gateway visualization each side builds its own and
   cross-links (ours `viz/cycle_anchor_gateway.html`); his credit-deflection
   preference on file with no record change (Remark 12.6.1.2 reads packaging
   his / verification joint); the note's credit language at drafting time is
   the author's call. Note: the hosting pin (v2) and the round-12 canonical-
   citation guidance (v3, line 87) coexist; both must survive — see §9 item 8.
9. **The Merle credit language** — HANDOFF carries it via the standing-decisions
   block and the pointers line; the owning wiki text is cycles.md 12.6.1.1 /
   12.6.1.2 / 12.6.1.4 / 12.8.6.1 (rotation reformulation, both names) /
   12.8.6.4 (pincer credit) and aeh.md 13.4's external-replication line.
   Verbatim preservation everywhere; the rewrite keeps the pointer set (line 93).
10. **Live conditions** (lines 89, 91) — the block that must lead the rewritten
    item 1: **PR #1 OPEN** (`.../one-obstruction-three-faces/pull/1`; his
    approving review is the round's second key — offers h1–h5, the regime
    column, the L-A8 corrections); **PR #2 OPEN** (pull/2; the note's second
    key; subtitle/Gersonides/file-name/credit open to his edit); the
    **`[GRADE AT SIGNING…]` bracket must not survive into the merged, signed
    note** — it resolves when the Macindoe L-A9 key turns (PR #1's review);
    the **L-A9 grade line restates per whatever h1 becomes**; **round 13 runs
    under the new medium**; the **Zenodo metadata line on the frozen
    Version-note clause is deliberately unaddressed** (the author's 2026-08-03
    decision; the version-history file carries the defect; if Merle asks, the
    answer is the changed decision stated plainly); **ccchallenge's v1 pointer
    noted flat** with canonical citation = the v3 DOI (line 87).
11. **The author's five round-12 decisions** (line 83, dated 2026-07-30): cost
    answer his; §13 accepted; smallest-object accepted in principle (pen taken,
    line 89); erratum-before-reply (discharged by v3); regime column accepted.
    Preserve at least as a compressed decision list — see (b) on homes.
12. **v3 facts** (line 87): full revision, not the prepared erratum; six-round
    external-review arc (94 commits, `briefs/v3r*`, version-history file); v2
    archived to `sources/paper/`; Zenodo file hash-identical to
    `paper/collatz-reduced-v3.pdf`; the frozen Version-note self-description
    defect (recorded in the version-history file); the paper's Status paragraph
    pins `cycles.md` at `9d9d1ec` and Appendix A at `6285485`, both resolving
    on public `main`; citation guidance v3-for-dichotomy-phrases /
    v2-for-the-contiguous-evidence-note.
13. **Items 2 and 3** (lines 95, 97): the KL–LP residual (idea-gated, closed
    front) and the longer-horizon items (anchor-pinning thread paused at the
    Bridge; AEH long-range per stopping rules; outreach de-prioritized) —
    keep both as they stand; they are already current-state.

### (b) The drop-map

Every narrative block below is recoverable at the named home; the rewrite keeps
one pointer sentence per arc (the existing pointers line 93 already names the
`briefs/merle-*` family as the round-by-round record).

| dropped block (lines) | where the facts live |
|---|---|
| Round-8 narration and key turns (31, 35) | `briefs/merle-round8-check-findings.md`, `briefs/merle-round8-coedit-findings.md`, merge `55f23cb`; patches `briefs/merle-round8-coedit-patches/` |
| L-A5 arc (35, 39) | `briefs/merle-la5-check-findings.md`, `-closure-findings.md`, `-coedit-findings.md`; patch `briefs/merle-la5-coedit-patches/` |
| L-A6 / L-A7 checks (35, 37, 47) | `briefs/merle-la6-check-findings.md` (merge `08b1547`), `briefs/merle-la7-mu-check-findings.md` (merge `13ba557`), `briefs/merle-la7-close-check-findings.md` |
| Round-9 co-edit + reply (39, 41) | `briefs/merle-round9-coedit-findings.md` (+ patches), `briefs/merle-round9-reply-draft.md`; shared-repo commit `641a530` |
| Round-10 letter, audits, recon, margin proof (43, 45, 47, 49, 51, 55, 57, 59, 61, 72, 76) | `briefs/merle-lean-r10-audit-findings.md` (merge `30d0d89`), `briefs/merle-la8-t1-check-findings.md`, `briefs/junction-repo-recon-findings.md` (merge `ece0162`), `briefs/margin-inequality-proof-findings.md` (merge `5c1faf4`), `briefs/merle-round10-coedit-findings.md` (+ patches; shared `c966875`), `briefs/merle-round10-reply-draft.md`; the `0816878` record repair |
| Round-11 audits, hygiene, recon, co-edit, reply, closure (53, 63, 65, 67, 68, 70, 74, 78) | `briefs/merle-r11-ceiling-audit-findings.md` (merge `3aeecbc`), `briefs/merle-r11-hygiene-check-findings.md` (merge `185c622`), `briefs/junction-public-recon-findings.md` (merge `185d44b`), `briefs/merle-round11-coedit-findings.md` (+ patches; shared `1d7907c`), `briefs/merle-round11-reply-draft.md`, `briefs/merle-round11-reply-adjust-findings.md`; wiki push `3eab8f1` |
| Window D premise pre-checks (80, 81) | `briefs/jointnote-premise-ours-findings.md` (merge `836735b`), `briefs/jointnote-premise-external-findings.md` (merge `b782e59`) |
| Round-12 letter, five windows, decisions enacted (83, 85) | `briefs/merle-round12-letter.md`; `briefs/junction-followup-recon-findings.md` (`6c1fc97`), `briefs/erratum-v3-prep-findings.md` (`332f67e`), `briefs/merle-la7-rhin-check-findings.md` (`c8a4bb1`), `briefs/merle-r12-drift-check-findings.md` (`87483c5`, addenda `c13f48c`), `briefs/merle-la9-check-findings.md` (`913f577`) |
| v3 publication arc (87) | `paper/collatz-reduced-version-history.md`; `briefs/v3r*` findings; publication.md line 39 |
| PR #1 package narration (89) | `briefs/merle-round12-pr-findings.md` (merge `887e324`; its §6 the review edits, §7 the author's paragraphs); patches `briefs/merle-round12-pr-patches/` |
| PR #2 / joint-note draft narration (91) | `briefs/jointnote-v1-draft-findings.md` (merge `f968060`); `NOTE-v1.md` on the shared branch |
| Staircase-arc items 4–10 (99–108) | the seven findings files named in each item + merges `e42d785`, `da5f06d`, `b85be16`, `4538a20`, `2b9e424`, `3a50eea`, `297f1fa`; the arc's consolidated current state is cycles.md §12.8.6 itself |

**Facts with no verified home outside HANDOFF — preserve, or give a home before
dropping** (flagged, not assumed): (i) the author's five round-12 decisions as a
*decision list* (line 83 — the enactments are in the briefs, but the decisions'
statement as the author's, dated, may exist only here); (ii) the deliberate
non-decision on the Zenodo metadata line with its if-Merle-asks answer (line 91);
(iii) Merle's personal-background sentence (line 45: lycée electricity teacher,
no doctorate, a year in — the letter it summarizes is not in `briefs/`, only the
round-12 cover is); (iv) the L-A9 bracket-resolution rule (line 91 — likely also
in `briefs/jointnote-v1-draft-findings.md`, not verified line-by-line here);
(v) the spend-limit symmetry anecdote (line 85) — sent in PR #1, so
`briefs/merle-round12-pr-findings.md` §7 should carry it; verify before dropping.

### (c) Stale-label corrections (ground facts contradict the text)

1. Line 99, item 4: "DELIVERED on branch `staircase-allp-construction`,
   **awaiting review**" — merged, `e42d785`. (Line 100 itself already says
   "merged `e42d785`" — an internal contradiction.)
2. Line 100, item 5: "CLOSED, **awaiting main-session review** … both
   delegate-side and unmerged" — merged, `da5f06d`.
3. Line 101, item 6: "PROPOSALS DELIVERED … **awaiting review**" — merged,
   `b85be16`.
4. Line 103, item 7: "REPAIRED … **awaiting review**" — merged, `4538a20`.
5. Line 105, item 8: "CLOSED … **awaiting review**" — merged, `2b9e424`.
6. Line 107, item 9: "APPLIED … **awaiting review** … nothing merged and
   nothing pushed" — merged, `3a50eea`.
7. Line 108, item 10: "CLEARED … **awaiting review** … nothing merged or
   pushed" — merged, `297f1fa`.
8. Line 63, the repo-hygiene list ("six `experiments/` scripts cite … TOUR.md's
   now-unattached floor grade … this file's duplicate item numbering … an
   optional supersession header … README line 53") — all five were discharged
   by `record-consistency-sweep` (`297f1fa`), except the printed-string half of
   the citations, which is §6's production decision. The same line's "the
   erratum … drafted, not issued" is superseded by v3 (line 87).
9. Line 31, the repos-and-ledger paragraph pins shared HEAD **`81431c7`** and
   Lean HEAD **`97b57d7`** — both frozen at round 9. Current per lines 83/89/91:
   shared `7c05458` (+ the two PR branches), Lean `d48ba9e`. The same paragraph's
   "L-A6 … check in flight" / "L-A7 … check in flight" are superseded by lines
   35/37 (both done, merged, keys settled).
10. Line 35 tail: "the L-A7 check … is the remaining in-flight item" —
    superseded by line 37.
11. Lines 39/41: round-9 "Owed now: sending only" — round 9 closed (reply sent,
    established line 35's SENT clause and line 63).
12. Lines 57/59/61: round-10 owed-lists — closed by lines 61/63.
13. Line 65: "Still to come … window D … then the co-edit and the round-11
    reply" — all done (lines 67–70, 80–81); the three merges it names are
    correct and current.
14. Line 72: "*(Round 10, closed.)* Owed next … SENDING ONLY" — closed-window
    report, drop whole.
15. Line 76: "*(Superseded, kept for the shape of the round.)*" — self-labeled;
    drop whole.
16. Line 83: "five windows briefed and launched" + its owed-list — superseded by
    lines 85/87/89.
17. Line 85: "Owed next, in order: (1) the author — wiki `main` pushed public …
    the σ decision, the Zenodo v3 upload …" — superseded by line 87 (v3
    published) and line 89 (PR #1 sent).
18. Line 87: "Amended owed-next … (2) the co-edit + round-12 reply as the first
    PR …" — superseded by line 89 (PR #1 open).
19. Line 89: "Owed by us this week … the joint-note first draft as its own PR" —
    superseded by line 91 (PR #2 open, four days inside the promise).

No "NOT pushed" claim survives that is currently false: the two co-edit
paragraphs carrying "PREPARED LOCAL-ONLY, NOT PUSHED" headers (lines 59, 70) are
each followed by their own PUSHED paragraphs (lines 61, 63) — stale headers on
superseded paragraphs, covered by the drop-map rather than by correction.

---

## §2 Periodic status pass

Sweep coverage: every wiki page listed in the brief was read in full or to the
depth its cross-claims required (front matter + Current state + every line that
names another page; spine.md and stage1-synthesis.md carry almost no cross-page
claims — spine.md's one pointer block, line 1481, is current). Findings, in
priority order:

| # | page:line | claim as written | owning page's current answer | proposed fix (one line) |
|---|---|---|---|---|
| 1 | index.md:46 | "Both papers are published … with paper 1's **v2 uploaded** (DOI 10.5281/zenodo.21421120, publication.md)" | publication.md:2/39 — **v3 published 2026-08-03**, DOI 10.5281/zenodo.21730505; v2 archived to `sources/paper/` | "…paper 1 at v3 (DOI 10.5281/zenodo.21730505; v1 10.5281/zenodo.21273548, v2 10.5281/zenodo.21421120, publication.md)"; refresh `updated:` |
| 2 | cycles.md:171 (12.6.1.4(a)) | "Ledger status, honestly **as of this writing**: our key turn on L-A4 is **prepared and pending** the author's review of the shared-repo push" | HANDOFF:31/35 — L-A4 pushed 2026-07-25 (`cb765be`), stands at **two keys**, plus the ContentDescent kernel key (`08dc3d5`) | "Shared-ledger status: L-A4 at two keys (2026-07-25), with the kernel key on the structured half." — own commit; adjacent credit prose untouched (before/after quoted at production per the brief's math-adjacency rule) |
| 3 | program.md:99 | "the cycle ladder (§12) is not climbed per period; **work there serves only the uniform trim lemma**" | cycles.md 12.8/12.8.5 + README:36 — the trim is **resolved**, the ladder retired, the front parked; reopens only on a divisibility-aware idea | "…the cycle ladder (§12) is retired and the front parked (12.8.5); it reopens only under README's stopping rule." |
| 4 | stage1.md:650–673 (11.8.4.5 tail) | "the conversion … is only partially complete: … **still open: control of `C`, laws for `d_+`**, eventual refinement of `ω_+`" | stage3.md front matter — closed at the valuation level, all residue classes; contradicted by the ledger block 20 lines above it | restate the checkpoint tail at the current answer: completed = parity of `s`, 3-gain, `d_+` (11.8.6); open = the odd core `ω_+` ⟺ anchor increment (stage4.md, bridge.md §16) — quote before/after, no formula touched |
| 5 | publication.md:2, 7 | "targeted checks **ongoing**" / "targeted checks continuing **as the paper is finalized**" | both papers published; v3 out 2026-08-03 | drop the "as the paper is finalized" clause; date the assessment as a snapshot ("as of 2026-08-03") — this page's staleness is a known failure mode (it reads as live while being dated) |
| 6 | index.md:25 (Pages table) | publication.md row status "**sweep complete**" | publication.md's own status: "novelty verdicts per claim below, targeted checks ongoing…" | align the two (suggest both read "novelty assessment (dated snapshot); papers published at v3") |
| 7 | publication.md:59 | "Pre-submission checklist, **still open**: sweep Lagarias's bibliographies…; **choose and state one concrete irrationality measure**" | the measure is chosen, pinned and published (Rhin 1987 at cycles.md 12.5.3/12.7.5/12.8.2, stage1-synthesis.md 11.8.3.11; v3 out) | mark the measure item discharged with its pin sites; the Lagarias-sweep half is unverified — see §9 item 5 |
| 8 | TOUR.md:22 | "…is what **the published v2 note** describes, and is kept there as the superseded formulation" (and :14 "the paper's own hedge sentence is unchanged") | v3 replaced the v2 note with the *Status of the assessment* paragraph (verified in `paper/collatz-reduced-v3.tex`: the hedge sentence itself **survives** in the "Sharpness evidence and assessment" paragraph; the Status paragraph reports the proof and pins `cycles.md` at `9d9d1ec`) | one-line update per row: name v3's Status paragraph as the current print-side pointer; keep the v2-note sentence as historical ("the v2 release note described…") |
| 9 | TOUR.md:39 (status vocabulary, "assessed") | "remains stated that way *in print*" | still true of v3 (the assess sentence survives) but the divergence the entry describes has narrowed: v3 itself reports the proof | optional one-clause update ("v3 additionally reports the proof's existence; the wiki carries it") — judgment grade |
| 10 | README.md:40 (statistics door) | describes AEH formalized/calibrated with conditional theorems; **no mention of the unconditional base case** | aeh.md 13.2.4 / front matter and index.md:46 both headline the base case (every θ < 1/4, every block length, shell-scale density) | add one clause pointing at 13.2.4 — author-level edit (README is the author's map page) |
| 11 | index.md:26 (Pages table, aeh row) | contents list ends at "genericity form (13.6)" | aeh.md now also carries 13.2.4/13.2.5 (base case) as a headline | optional: append "unconditional base case (13.2.4)" to the row — low priority, the status paragraph already carries it |

Checked and found current (no fix proposed): stage4.md's cycles claims (line 8,
96 — parked/withdrawn/resolved all match cycles.md); stage2.md; stage3.md;
ladder.md's status surfaces; anchors.md (hedge at line 37 matches the published
register); bridge.md (its `n_0(91) ~ 3·10^21` at 16.4.4 matches cycles.md
12.8.2's table `2.99·10^21`; its 12.8.3 citations resolve one-hop to 12.8.6 via
12.8.3's own pointer sentence); open-problems.md (11.8's discharge record and
n₀ figure match; calibration notes current); reverse.md and itinerary.md front
matter; aeh.md's cross-claims (13.3.3 → 12.8.4, 16.4.6); index.md's resolver
line; HANDOFF's State-of-the-fronts bullets (modulo §1(c) item 9); TOUR.md's
12.8.6 rows (all four resolve to the rewritten section correctly, scope wording
matching cycles.md's own).

---

## §3 Convention violations

Wiki pages only; `briefs/` exempt. Against "no change logs in tracked files",
the one-current-line verification rule, and the short-`status:` standard (the
2026-07-17 pass set reverse.md's to ≤ 3 lines).

1. **aeh.md:2 — `status:` is a full paragraph** (~1,400 characters: formalized /
   base case / calibrated with three limits / anomaly resolved / depth marginal /
   parked). The Current-state callout (line 8) already carries all of it.
   Proposed trimmed form:
   `status: hypothesis FORMALIZED (13.2.1); unconditional base case PROVED (13.2.4, every θ < 1/4); calibrated clean within three stated limits (13.4–13.5); genericity form proved (13.6); proof effort parked per stopping rules`
2. **publication.md:2 — `status:` is two long clauses** (verdict summary + both
   papers' DOI history). Proposed:
   `status: novelty assessment, dated snapshot (2026-08-03); papers published — paper 1 v3 DOI 10.5281/zenodo.21730505, mirror DOI 10.5281/zenodo.21303918`
3. **anchor-digit-search.md:2 — `status:` enumerates all five batteries.**
   Proposed: `status: executed search, clean at every endpoint (17.7.1–17.7.5; M(ω) not 2-automatic)` — borderline; keep if the reviewer prefers.
4. **cycles.md:171 — "honestly as of this writing"** — session-status prose
   inside a wiki page (same site as §2 item 2; one fix covers both).
5. **reverse.md:370 — provenance stamp in a theorem header**: "*(Added
   2026-07-15, branch `block-map`, per `briefs/block-map-brief.md`, item 3 — a
   strengthening…)*". Branch-and-brief narration of exactly the kind the
   2026-07-22 pass removed elsewhere. Proposed: keep only the mathematical
   clause ("a strengthening of 14.14.5.1–.3: one law covering both cases…"),
   drop the date/branch/brief provenance.
6. **itinerary.md:219 — "review addition, 2026-07-16"** inside a remark title.
   Proposed: drop the stamp, keep the remark ("Remark (liveness is not assumed
   at intermediate doors).").
7. **anchor-digit-search.md:131/141 — §17.8 "Search plan (scoped 2026-07-12;
   executed — results in §17.7.1)" and §17.9 likewise** — plan sections retained
   after execution, i.e. superseded-formulation prose at section grade.
   Candidate only (when in doubt keep): either collapse each to a two-line
   pointer at the section number (numbers are immovable) or retitle "(executed;
   kept as the search's specification)". Judgment grade.
8. **Not violations, recorded as assessed**: itinerary.md/cycles.md one-line but
   long `status:` fields (within tolerance); aeh.md's dated §13.4 heading
   "(2026-07-08)" — the campaign's identity, kept (see §9 item 7); the many
   dated verification lines across pages — each is the single current line the
   workflow prescribes, none is an append-chain; correspondence dates in
   cycles.md 12.6.1.x — facts of the credit record, keep verbatim.

---

## §4 Cross-reference gaps

1. **ladder.md:56 — mis-homed pointer**: "raw material for the fiber-to-orbit
   bridge (**stage4.md**, `11.8.5.6`)". §11.8.5.6 lives on stage2.md per the
   resolver; bridge.md §16 is the consolidation. Proposed: "(stage2.md
   `11.8.5.6`; consolidated as the Bridge, bridge.md §16)".
2. **The 12.8.6.x citation check — every wiki citing site resolves correctly.**
   Sites outside cycles.md that cite `12.8.6` or a sub-number: README.md:53
   (section cite, correct); index.md:33/46 (scope wording matches cycles.md's
   own); TOUR.md:14/22/23/39/42 (correct, including 12.8.6.1/12.8.6.3 named as
   the superseded route's home); publication.md:39 (correct, same); HANDOFF
   (multiple, current); aeh.md/bridge.md cite 12.8.3/12.8.4 (one-hop correct —
   12.8.3's pointer sentence lands on 12.8.6). No wiki page cites `12.8.6.2`
   in the pre-rewrite sense. The mis-resolving citations are confined to
   `experiments/` printed strings (§6) and to pre-rewrite `briefs/` (§7).
3. **index.md:46 v2/v3** — the one stale pointer found in the resolver/status
   layer (already §2 item 1).
4. No dangling section numbers found: §11.9/§11.10 disambiguation intact
   (index.md:42, open-problems.md:3); §14.15 → itinerary.md and §17.7–17.10 →
   anchor-digit-search.md resolve; spine.md 9.8.4's outbound pointers (cycles.md
   §12, bridge.md 16.4.4) current.
5. Cross-reference *additions* considered and not proposed: cycles.md 12.6.1.4's
   ledger-status sentence should point nowhere new once corrected (HANDOFF is
   the ledger-state surface); README →13.2.4 is §2 item 10.

---

## §5 itinerary.md and aeh.md: bloat assessment

**Verdict: both are large because the mathematics is large. No structural
proposal.**

- itinerary.md (139 KB, 615 lines): ten numbered blocks (14.15.1–14.15.10),
  each theorem/proof/verification. The per-block "Accounting and closing
  status" subsections (lines 199, 272, 368, 567) repeat the Bridge-unchanged
  sentence, but each is that block's own scope statement — the register norm's
  requirement, not duplicated status (the Bridge's status itself is stated
  once, at bridge.md). Verification lines are one-per-result, dated, current.
  The only convention item found is the provenance stamp at line 219 (§3
  item 6). No superseded-formulation prose found: 14.15.7/14.15.8 are already
  the collapsed stubs the 2026-07-22 reverse pass left, carrying the
  closed-form laws verbatim.
- aeh.md (92 KB, 232 lines): 13.2 (hypothesis + base case) and 13.6 (genericity
  form) are the mass; both are current mathematics. 13.4's campaign paragraphs
  record dissolved discoveries as methodology — deliberate, calibration-grade
  content, not narration; the protocol-gap paragraph (line 132) states a
  current measured fact. The one violation is the front-matter `status:`
  paragraph (§3 item 1). The single-visit/block distinction, the three limits,
  and the standing rule each appear in both the front matter and the body —
  trimming the front matter (§3) removes the duplication without touching the
  body.

---

## §6 The seven printed-string citations (and one more)

Recorded in `briefs/record-consistency-sweep-findings.md` §1.2 at their
2026-07-29 line numbers; enumerated here at current lines, each with the exact
string, the committed output it prints into, and the re-run command. In every
case the correct referent is the **superseded pure-geometric recipe/profile,
now `12.8.6.3`** (in `12.8.6.2`'s old pre-rewrite sense); `12.8.6.2` now names
Construction B.

| # | script:line | printed string (verbatim core) | committed output that regenerates | re-run |
|---|---|---|---|---|
| 1 | `experiments/p22_passer.py:170` | `"(construction 12.8.6.2 + 13 correction moves of 12.8.6.3;"` | none committed | `python experiments/p22_passer.py` (visual check only) |
| 2 | `experiments/p22_passer.py:180` | `"(construction 12.8.6.2 + 8 correction moves of 12.8.6.3;"` | none committed | same run as #1 |
| 3 | `experiments/prime_local_probe.py:939` | `"…the staircase recipe (12.8.6.2) always uses K = ceil(n log2 3)…"` (f-string, lines 936–942) | none committed | `python experiments/prime_local_probe.py` (long; visual check only) |
| 4 | `experiments/staircase_allp_construction.py:498` | `"   unit of exit valuation each climb block spends.  12.8.6.2's PURE"` | `staircase_allp_construction_output.txt:73` | `python experiments/staircase_allp_construction.py > experiments/staircase_allp_construction_output.txt` (~400 s; expect wall-clock columns to differ, nothing else — precedent in the sweep findings §1.5) |
| 5 | `experiments/staircase_allp_construction.py:520` | `hdr("PART 2.  Shortfall of the base construction 12.8.6.2 at the SAME n")` | `staircase_allp_construction_output.txt:92` | same run as #4 |
| 6 | `experiments/staircase_allp_construction.py:797` | `"     partialsum  : round the partial sums of the PURE geometric  [12.8.6.2]"` | `staircase_allp_construction_output.txt:242` | same run as #4 |
| 7 | `experiments/staircase_allp_diophantine.py:1010` | `"  Recipe of 12.8.6.2 + 12.8.6.3, reimplemented independently; candidate"` | `staircase_allp_diophantine_part3.out:4` — **not** `_note.txt` as the sweep findings state; see §9 item 2 | Part 3 only; the committed `.out` set is a documented concatenation of several invocations (`staircase_allp_diophantine_note.txt` explains the split — Part 3's per-period cost grows like `n^1.585`, `n ~ 1.585^p`, so regenerating `_part3.out` is the expensive step) |

**An eighth printed-string site the sweep record does not list**:
`experiments/merle_pincer_check.py:518–520`, the f-string
`"Correction runs (algorithm 12.8.6.3 via Section 1's instrumented copy): …
crash_depth=1, base construction 12.8.6.2."` — "base construction" is the
superseded profile, so this printed citation mis-resolves in exactly the same
way. No committed output file exists for this script, so repointing it costs
nothing beyond the edit; whether to fold it into the same commit is the
production session's call (§9 item 3).

**The repaired comment/docstring sites still resolve** — confirmed by reading
each in context: `merle_pincer_check.py:21` and `:381` (both name `12.8.6.2` as
Construction B and the pure profile as `12.8.6.3`, with the
name-is-an-identifier clause), `merle_round3_check.py:425` (same),
`staircase_allp_construction.py:255` (negative control named), and the Part-2
banner `staircase_allp_construction.py:511–516` (redirects the printed text of
that Part). The current tree has five literal `12.8.6.2` comment/docstring
sites against the record's "six" — a counting artifact of the repair's
rewording, not a missing repair (§9 item 1). One adjacent stale comment,
recorded for the production session's option: `staircase_allp_diophantine.py:6`
still says "the **floor-grade** result at cycles.md 12.8.6" (the sweep left it
as a status word; 12.8.6 is now proved) — comment-only, no output change.

**Mechanics for one clean commit** (the author's decided production step):
edit the eight (or seven) strings `12.8.6.2` → `12.8.6.3` with the object named
where the sentence allows ("the superseded pure-geometric recipe, 12.8.6.3");
re-run `staircase_allp_construction.py` and the diophantine Part 3, replacing
`staircase_allp_construction_output.txt` and `staircase_allp_diophantine_part3.out`;
diff each regenerated output against its committed predecessor and confirm the
only changes are the repointed strings and wall-clock columns; run
`experiments/encoding_scan.py` (regeneration must not go through PowerShell
`>`, which BOM-stamps output files — the scan has caught exactly this before;
use Git Bash redirection or Python-side writing); one commit, scripts +
outputs together, message naming the seven-plus-one sites.

---

## §7 briefs/ supersession headers

Precedent: the header on `briefs/staircase-allp-findings.md` (present, correct,
including its pre-rewrite sub-number warning). Candidates where a later reader
would be actively misled — each gets one line under the title, nothing else:

1. **`briefs/staircase-allp-construction-findings.md`** — cycles.md 12.8.6.2's
   proof cites this file's §5 as its full record, but the file's own uses of
   "Construction `12.8.6.2`" (§2 heading at line 113, lines 127, 153, 176, 446,
   480) carry the **pre-rewrite** meaning (the pure-geometric profile, now
   12.8.6.3), and what this file calls "Construction B" is now numbered
   12.8.6.2. Proposed header: "Sub-numbers here are pre-rewrite: '12.8.6.2' in
   this file is the pure-geometric profile, now `cycles.md` 12.8.6.3; the
   Construction B it proves is now numbered 12.8.6.2 (applied with deviations —
   see `briefs/staircase-status-apply-findings.md`)."
2. **`briefs/staircase-status-audit-findings.md`** — carries drafted replacement
   texts for §12.8.6 and both gates as open; the texts were applied **with
   eleven deviations** (the load-bearing one: the sharp `maxgap` criterion
   replacing the span argument) and both gates are discharged (P1 by
   `staircase-gamma-upper`, P2 by the author). A reader quoting its drafts as
   the current record would be wrong in eleven places. Proposed header: "The
   drafted texts here were applied with eleven deviations — the applied record
   is `briefs/staircase-status-apply-findings.md`; gates (P1)/(P2) are both
   discharged (`briefs/staircase-gamma-upper-findings.md`; author's P2 call)."
3. **`briefs/junction-repo-recon-findings.md`** — every NOT FOUND /
   NOT CONFIRMED / NOT PERFORMED verdict is superseded: reachability by
   `briefs/junction-public-recon-findings.md` (four repos made public;
   `LegendreApprox` home CONFIRMED, diff PERFORMED) and the self-audit by
   `briefs/junction-followup-recon-findings.md` (all three round-11 NOT-FOUNDs
   CONFIRMED at full weight — the account was true, the copies not public).
   Proposed header: one line naming both successors and stating the posture
   sentence stands.
4. **`briefs/staircase-allp-diophantine-findings.md`** — one pre-rewrite
   sub-number use (line 371, "recipe of `12.8.6.2`–`12.8.6.3`") plus its (i)/(ii)
   results are re-stated at the sharper `maxgap`/two-sided form in the applied
   record. Weaker case than #1 (the availability theorem it proves is still the
   one cited); proposed only if the reviewer wants symmetry with #1 — a
   one-line pre-rewrite-numbering warning.

Considered and **not** proposed: `briefs/merle-lean-r10-audit-findings.md`
(its item (iv) figure was corrected in place at review — lines 279–281 carry
the correction; the one remaining over-inclusion in a verbatim lemma list is
named in the r11 ceiling findings and does not mislead about any verdict);
`briefs/jointnote-premise-ours-findings.md` (its "recorded and not corrected"
`n₀(92)` clause is superseded by the record-defects repair, but the file
explicitly frames itself as a dated fact base and HANDOFF item 7 records the
supersession — borderline; escalate only if it feeds the joint note again);
`briefs/merle-la7-mu-check-findings.md` (its re-sourcing recommendation was
*accepted*, not superseded); reply drafts and letters (records of their
moment, exempt).

---

## §8 Proposed production split

Three branches, in this order (precedent: pass 2's one-HANDOFF-branch /
one-sweep-branch split, plus the separately-decided experiments repair):

**Branch 1 — `wiki-consolidation-3-sweep`** (pages first, so HANDOFF's rewrite
can point at corrected surfaces). Commits, content separate from structure:

- Commit A (mechanical): index.md v2→v3 + table row (§2 items 1, 6, 11);
  publication.md status-surface clauses (§2 items 5, 7 measure-half);
  ladder.md pointer (§4 item 1). Risk: mechanical.
- Commit B (judgment): program.md:99 (§2 item 3); stage1.md checkpoint tail
  (§2 item 4, before/after quoted in the commit message); TOUR.md v3 rows
  (§2 items 8–9). Risk: judgment — each edit touches a sentence adjacent to
  mathematics or to the published record; quote before/after.
- Commit C (convention trims): aeh.md / publication.md / (optionally)
  anchor-digit-search.md `status:` fields (§3 items 1–3); reverse.md:370 and
  itinerary.md:219 provenance stamps (§3 items 5–6). Risk: mechanical, but
  reverse.md:370 sits in a theorem header — quote before/after.
- Commit D (its own commit, correspondence-adjacent): cycles.md:171 L-A4
  ledger-status sentence (§2 item 2 / §3 item 4). Risk: **judgment** — inside
  Remark 12.6.1.4, five lines from credit language that must not move;
  reviewer diffs the whole remark.
- Commit E (candidates, only on reviewer approval): README.md:40 base-case
  clause (§2 item 10 — **author-level**, README is the author's page);
  anchor-digit-search.md §17.8/17.9 retitle (§3 item 7).

**Branch 2 — `wiki-consolidation-3-handoff`**: the HANDOFF rewrite per §1, one
commit. Risk: judgment throughout; the verbatim blocks (§1(a) items 2, 8, 9,
10) must be byte-identical, and the five no-home facts (§1(b)) must survive.

**Branch 3 — `experiments-12862-repoint`**: §6's one clean commit (scripts +
regenerated outputs). Independent of branches 1–2; can run in parallel. Risk:
mechanical edit, expensive regeneration; the eighth site and the `_note.txt`
vs `_part3.out` discrepancy need the production session's explicit line in its
findings.

**Reviewer checklist** (all three branches):

1. `python experiments/encoding_scan.py` clean on every branch before merge.
2. Branch 1: `git diff` read in full; every §2 edit checked against the owning
   page's line quoted in this file; no edit touches cycles.md §12.8.5, the
   PARKED wording, README lines 32–38, or any displayed formula; commit D's
   remark diffed whole with the credit sentences confirmed byte-identical.
3. Branch 2: every dropped HANDOFF block matched to its drop-map row
   (spot-check at least the round-10 and round-12 rows); the standing-decisions
   block, register norm, author's-role paragraph, credit language, and quirks
   confirmed verbatim; the five §1(b) no-home facts located in the rewrite;
   the two PR-open live conditions and the bracket rule present; fronts block
   re-dated.
4. Branch 3: regenerated outputs diffed against predecessors — only repointed
   strings and wall-clock columns may differ; no BOM (scan catches it); the
   re-run's check counts and 0-failures lines byte-identical.
5. Merge order 1 → 2 → 3 (3 may land any time); no pushes — the author reviews
   and pushes per standing conventions.

---

## §9 Lower-confidence items

1. **"Six" repaired comment sites vs five found.** The sweep findings' §1.1
   heading says 3 sites, its table has 5 rows spanning 7 line numbers, and its
   text says "all six". Today's tree has five literal `12.8.6.2`
   comment/docstring occurrences, all resolving correctly. I believe the
   repair reworded some docstrings so the literal string no longer appears
   (e.g. old `merle_pincer_check.py:473`), and nothing is missing — but I did
   not reconstruct the pre-repair file to prove the count.
2. **The sweep findings mis-name one committed output.** §1.2 says repointing
   would regenerate `staircase_allp_construction_output.txt` and
   `staircase_allp_diophantine_note.txt`; the stale string actually prints
   into `staircase_allp_diophantine_part3.out:4`, and `_note.txt` is a
   provenance note containing no citation. Per the files-win rule this file
   records the discrepancy and follows the tree (§6 table).
3. **The eighth printed site** (`merle_pincer_check.py:518–520`) is my reading
   of an f-string built into a report the script emits; I did not run the
   script (240 s correction-run deadlines). If the `out` list is never
   printed, the site is inert — the production session should confirm with a
   cheap trace before deciding whether it joins the commit.
4. **Homes for §1(b)'s five flagged facts.** I verified the *arcs* have homes;
   I did not verify line-by-line that the author's five decisions, the
   Zenodo-metadata non-decision, and Merle's personal-background sentence
   appear verbatim in any findings file. The rewrite should preserve them
   until someone checks.
5. **publication.md's Lagarias-sweep checklist item.** I could not determine
   from the tree whether the bibliographies sweep happened (the measure item
   is demonstrably discharged). Left as "verify before marking discharged".
6. **TOUR.md v3 items are judgment calls**, not corrections of falsehoods: the
   v2-era sentences remain true of the frozen v2 at its DOI; what changed is
   which version a new reader holds. Proposed wording should preserve the
   v2 facts as historical rather than delete them.
7. **aeh.md §13.4's dated heading** and campaign-methodology paragraphs were
   deliberately not proposed for trimming — they read to me as the register
   norm's own genre (dissolved discoveries recorded as calibration), but a
   stricter reading of "no change logs" could disagree. Flagged for the
   reviewer rather than proposed.
8. **The hosting-pin/canonical-citation tension.** The standing decision says
   hosting is DOI-pinned to **v2**; round 12's citation guidance says canonical
   citation = the **v3** DOI (v2 for the contiguous-evidence note). These are
   different objects (a hosting pin vs a citation recommendation) and both are
   preserved in §1(a) verbatim, but the rewritten HANDOFF should keep them
   adjacent so the difference stays visible; whether the hosting pin should
   move to v3 is the author's decision, not proposed here.
9. **stage1.md's checkpoint tail (§2 item 4)** may be intentionally retained
   monolith prose ("read only as a checkpoint"). I read it as a stale status
   surface because it contradicts the ledger block directly above it in the
   same subsection; if the author wants it kept as historical framing, the
   minimal fix is one introductory clause dating it.
10. **Brief-vs-files discrepancies found: none material.** The brief's ground
    facts all verified (seven merges, page sizes, front-matter dates, public
    `main` = `d09895c` at cut time — my worktree was cut there and moved to
    `7b6ef15` per its own instruction). The only corrections this audit makes
    to prior *records* are items 1–2 above, both against
    `briefs/record-consistency-sweep-findings.md`, both in the direction the
    tree dictates.
