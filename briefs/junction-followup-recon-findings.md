# Junction follow-up recon — his §§1–2 repairs, verified read-only

Brief: `briefs/junction-followup-recon-brief.md`. Branch `junction-followup-recon`,
base **`9d9d1ecfe3434b514b10238c1d622194c8a7543f`** (the worktree was cut at the
stale `3eab8f1`, which does not contain the brief; it was fast-forwarded to
`9d9d1ec` by `git merge main` before any work started, per the launch instruction).

This session closes out the three NOT-FOUND verdicts of
`briefs/junction-public-recon-findings.md` against the repairs described in
`briefs/merle-round12-letter.md` Part 2 §§1–2. Recon only: nothing mathematical,
no key turned, no ledger or reply text beyond the one deliverable paragraph.

## Interaction record — none occurred

All access was by **unauthenticated read-only `git clone`** into the session
scratchpad plus read-only `gh api` calls against public endpoints (the repository
activity endpoint, which is GitHub's own log of ref updates). There was **no fork,
no issue, no pull request, no comment, no star, no watch, no follow, no push, no
write of any kind** against any repository of his, and no contact with anyone.

## Outcome in one line

**All three round-11 NOT-FOUND verdicts move to CONFIRMED.** The files exist where
he said, at the commits he named, with the content he described; the marker count
comes back at his eighteen by our own grep; the byte-identity claim holds at the
committed-tree level, one step stronger than the working-copy diff he ran; and the
push structure is visible in GitHub's activity log and is consistent with his
account, with one flat refinement recorded at item 5. This is the case the round-11
posture sentence was written to allow: **the account was true and the copies were
simply not public.**

---

## Item 1 — clones and refs

Fresh unauthenticated clones, 2026-07-30, all remote heads fetched.

| Repository | Refs fetched | Tip | Tip date |
|---|---|---|---|
| `Collatz-Junction-Theorem` | `main`, `proof-assembly-v1`, `syracuse-jepa-v2` | `main` = `a57d29e7c062e6c614ebca4dc0875f70065561a9` (2026-04-22, unchanged since round 11); **`proof-assembly-v1` = `8ff1010`** (2026-07-29 14:10:14 +0200); `syracuse-jepa-v2` = `f6e1bff` (2026-03-17) | — |
| `collatz-cycles-lean` | `main` (its only branch) | **`main` = `b38758dd1474d2b84ba9b6743a8ae48bfb5be6a3`** (2026-07-29 14:10:11 +0200) | — |

Round 11's HEADs were `a57d29e` and `1d77168`. The movement since is exactly the
six commits his letter names, plus nothing else.

---

## Item 2 — AUDIT_V9: **CONFIRMED**

**The file exists publicly, at the named path, branch, commit and date.**
`audits/AUDIT_V9_PORTEE_2026-07-25.md` in `Collatz-Junction-Theorem`, branch
`proof-assembly-v1`, added at commit `98b2de697c3548584acdbd3a2ff1d9a2a4870a87`,
author and committer date both **2026-07-25 11:30:01 +0200** — every particular as
described. The commit touches exactly two files: the audit file (46 insertions) and
`README.md` (25 insertions, 4 deletions).

**Parent and position.** `98b2de6`'s sole parent is `3caaa11` (2026-03-18, *"Honest
status: research doesn't converge, publish what's proved"*). The branch graph is
linear: `3caaa11 → 98b2de6 → 6de1743 → ff27436 → 8ff1010` (tip). `98b2de6` is
reachable from `origin/proof-assembly-v1` only — it is on no other ref.

**When it became publicly reachable.** GitHub's repository activity endpoint — an
exposed ref log — records every push to `proof-assembly-v1`: the branch tip was
`3caaa11` from **2026-03-18T18:54:09Z** until **2026-07-29T07:20:12Z**, when a push
moved it `3caaa11 → 6de1743`, carrying `98b2de6` with it. So at the round-11 recon
(2026-07-28) the public tip of the branch was `3caaa11`, and `98b2de6`'s parent *is*
`3caaa11` — his "exactly one commit ahead of `origin/proof-assembly-v1` at your
look, never pushed" is confirmed in every publicly checkable half: the origin tip
he names is the tip the log shows, and the commit sits exactly one ahead of it.

**What cannot be established read-only, stated plainly and without implication
either way:** that the commit existed, with that content, before its push. Commit
timestamps are author-set; the earliest platform-side attestation of `98b2de6` is
the 2026-07-29T07:20:12Z push. Nothing visible contradicts the 2026-07-25 date and
nothing outside his machine can attest it.

**The file's own verdict lines, and how V9 relates to V8.** The round-11 recon
found the public series stopped at V8 (*"l'abstract suraffirme"*) and recorded his
shop-window sentence as "not a repository artifact." It now is one. AUDIT_V9's own
verdict, verbatim:

> `**Le fond du dépôt était juste ; sa vitrine dépassait son fond.** C'est la vitrine qui a été corrigée.`

— the French original of *"the mathematics inside was sound; the shop window was
ahead of the shop."* Its §1 table marks `PROOF_ASSEMBLY.md` §2, the preprint's
Hypothesis-(H) clause and `AUDIT_V8_RESULTS.md` 1.3a/1.3b all *"✅ honnête"*, and the
pre-correction `README.md` *"❌ surclamait"* / `STATUS.md` *"❌ ambigu"* — so V9 cites
V8 and continues its series rather than repeating it: V8 (2026-03-07) graded the
paper, V9 (2026-07-25) grades the repository's own internal consistency, crediting
the trigger as *"relecture externe déclenchée par la collaboration Macindoe."* Its
§2 records an independent check run before writing (`corrSum` canary; `range/d`
measured 6–372 over all compositions, so the short README phrasing was misleading,
not the mathematics), its §4 carries forward four *still-unfixed* corrections
inherited from the March STATUS.md, and its §5 states what the repository actually
contributes (the entropy deficit `γ` with `γ·log₂3 = c_gen` exactly — the L-A7
brick). `audits/` on the branch now holds V1–V4, V8, V9.

**Corroboration of what V9 says it corrected:** the README on `proof-assembly-v1`
at `3caaa11` (pre-V9) did carry, verbatim, *"**Theorem (Unconditional).** For every
integer $k \geq 3$, there is no non-trivial positive cycle of length $k$"* — and at
`98b2de6` the same README's table marks `k = 201..10000` *"MACHINE-CHECKED, not
kernel-proved"*, `k > 50000` **OPEN**, and states *"This repository does not prove
the Collatz cycle conjecture."* One reconciliation for our own record: round 11's
sentence that the Junction README *"has said 'Conditional on GRH' since its first
substantive version"* was about `main` and remains true of `main`; the overclaiming
README was this branch's, which round 11 did not quote — the two statements are
about different files and both stand.

One flat placement note, not a defect: AUDIT_V9 and STATUS.md are public on the
non-default branch (`proof-assembly-v1` is where the file always lived, per his
account, and `main` is the archived state); a reader landing on `main` still sees
the audit series stop at V8.

---

## Item 3 — STATUS.md: **CONFIRMED**

**Committed** at `6de1743` (2026-07-29 09:19:51 +0200, *"Publish STATUS.md, and
carry the PROOF_ASSEMBLY.md retraction into this tree"*), 90 lines, blob unchanged
through `ff27436` and `8ff1010`. First and only ref ever to carry it — confirming
round 11's "never committed in any ref" and his explanation at once.

**The `.gitignore` line: gone, with the reason recorded in its place.** At
`98b2de6`, `.gitignore` line 52 — exactly the line number he named — reads
`STATUS.md`, under the heading `# Internal project management (not for
publication)`. The diff at `6de1743` replaces that one line with, verbatim:

> `# STATUS.md removed from this list 2026-07-29: it is not internal project management.`
> `# It is the repository's scope statement — it marks what the Junction Theorem is not,`
> `# and states plainly that this repository does not prove the Collatz conjecture.`
> `# It was cited to a correspondent as public evidence while being excluded here.`

**Content matches his three-point description, each point verbatim in the file:**

1. Scope — non-existence proved for `3 ≤ k ≤ 200` only:
   > `**Non-existence des cycles : PROUVÉE pour 3 ≤ k ≤ 200 seulement** ; au-delà, deux programmes asymptotiques avec gaps nommés`
2. The preprint's Hypothesis (H) for `k ≥ 69`, quoted:
   > `Le préprint l'écrit lui-même : *« the complete exclusion of cycles further requires Hypothesis (H) for k ≥ 69 »* (Remark \`junction-scope\`)`
3. The plain does-not-prove sentence:
   > `**Ce dépôt ne prouve pas la conjecture de Collatz.**`

All three sit in one warning box (*"⚠️ CE QUE CE THÉORÈME N'EST PAS"*) under the
main-result heading — the box AUDIT_V9 §3.2 says was added in the same day's
mise-en-cohérence. The rest of the file is the March 2026 state it claims to be
(*"Dernière mise à jour : 7 mars 2026"*), including the four pre-submission
corrections that AUDIT_V9 §4 carries forward as still open.

**One flat observation, same shape as the original finding:** STATUS.md's audit
table lists `audits/AUDIT_V5_APEX1.md`, `AUDIT_V6_DEEP_DIVE.md` and
`AUDIT_V7_PHASE23_REVIEW.md`, and none of the three exists in any public ref of
either repository (the committed series is V1–V4, V8, V9); its *"Projet frère"* and
*"Lien Artin"* sections point at `SISTER_PROJECT.md` and `research_protocol/`,
both still on the `.gitignore` list. Recorded flat — the file is an honest copy of
an internal document whose neighbours are still internal — and not adjudicated.

---

## Item 4 — PROOF_ASSEMBLY.md at `b38758d`: **CONFIRMED**, eighteen against eighteen

**Our own marker count: 18.** Pattern stated per the brief: case-sensitive grep for
`RETRACTED` over `docs/PROOF_ASSEMBLY.md` at `b38758d`, excluding the retraction
block's own heading (line 11) and the block's prose. The eighteen in-place markers
sit at lines **2, 7, 73, 158, 220, 243, 247, 249, 273, 304, 317, 329, 339, 356,
357, 358, 360, 375**. His count of eighteen at `b38758d` is **exact**.

**His named lines verified in the pre-retraction file** (`1d77168`, blob unchanged
since the file was added at `8fdfb20`): line 7 (`**Status:** **COMPLETE.** …
unconditionally for all $k \geq 3$`), 113, 175, 202, 272, the §10.6 heading at 294
(`GAP CLOSED`), and 315 (`No gap remains…`) — all seven exactly where he put them —
and §6's heading (`## 6. The Asymptotic Gap — **RESOLVED**`) at line 198, the one
his third pass caught. The current line numbers are the old ones shifted by the
inserted block.

**The sequence, counted under one convention.** His finding is the sequence
7 → 14 → 18; the brief says record it as his, and it is. Counting the same pattern
at each pass: `d7dbb7a` has **7** in-place markers (his seven), `995c98c` has
**15**, `b38758d` has **18** (second pass added 8, third added the 3 he names —
§6's heading at 243, the §4 Path-A paragraph at 249, the finite-bridge line at
375). So under our single convention the middle number is 15, not 14 — and the
Junction carry-commit `ff27436`'s own message says *"sixteen markers"*, which
matches 15 plus the block heading. Three stated counts, three conventions. This is
recorded flat, not as a correction: it is a fourth instance of his own finding, and
the block's remedy already covers it — *"No count is given here on purpose, and
none should be trusted."* Our 18-against-18 agreement at `b38758d` holds because
at the final state every convention lands on the same markers.

**The RETRACTED block tops both copies with all five stated elements.** At
`b38758d` (and byte-identically at `8ff1010`), the block `## ⚠️ RETRACTED —
PERMANENT RECORD, DO NOT REMOVE` carries, as its five bullets: **what was claimed**
(Path A establishes `N₀(d(k)) = 0` unconditionally for all `k ≥ 3`, `k ≠ 4`);
**why it is false** (the Range Exclusion module computes the wrong function — its
`corrSum` is not the quantity the argument requires, so both halves of Path A apply
to a different object); **where the current record is** (`VERIFICATION.md`,
`README.md`, `lean/range-exclusion/WARNING.md`, `docs/AUDIT_CORRSUM.md`, all in
`collatz-cycles-lean`, with a locator sentence for readers of the Junction copy);
**what survives** (none of the unconditional claim; Path B untouched and
independently establishing `k ∈ {3,…,200}`, the enumeration table rows left PROVED
for that reason; the reusable asset `γ·log₂3 = c_gen`); and
**"This repository does not prove the Collatz conjecture."**

**Nothing deleted — with two mechanical variants recorded flat.** The cumulative
diff `1d77168 → b38758d` is the block insertion plus exactly 18 line-level edits,
one per marker. Sixteen of the eighteen keep the original sentence intact on its
line with the marker appended (or, at line 220, prepended). The two variants: the
Status line's original sentence was *replaced* by the RETRACTED pointer, its claim
restated in the block's "What was claimed" bullet in near-identical words; and the
three §10.6 table rows read `**RETRACTED** (was PROVED)`, replacing the cell while
recording what it was. Every assertion remains visible or explicitly restated;
no content line of the document was removed.

**The byte-identical claim: CONFIRMED at the committed trees, which pair we
compared stated.** His diff was Junction-`98b2de6`-tree against the
`collatz-cycles-lean` *working copy* of 2026-07-29; the working copy cannot be
established read-only, so we compared committed blobs. `docs/PROOF_ASSEMBLY.md`
has the identical git blob in both repositories at **every** corresponding stage:

| Stage | cycles-lean commit | Junction commit | blob |
|---|---|---|---|
| pre-retraction / inside `98b2de6` | `8fdfb20` = `1d77168` | `3caaa11` = `98b2de6` | `a8bd7df` |
| pass 1 | `d7dbb7a` | `6de1743` | `d2210d5` |
| pass 2 | `995c98c` | `ff27436` | `9005895` |
| pass 3 | `b38758d` | `8ff1010` | `6d57ed7` |

The first row is the pair his claim is about: the file inside `98b2de6`'s tree is
byte-identical to the file at `1d77168` — the public `collatz-cycles-lean` HEAD of
that moment, unchanged since the file's addition. So his no-output diff is
confirmed for the committed state on both sides, and his §2 consequence with it:
pushing `98b2de6` alone would have published the retraction's trigger beside an
unmarked copy of every assertion.

**One flat date note.** The block's closing line says the README and
`VERIFICATION.md` *"were corrected on 2026-04-25"*; the visible corrections are
`1a56828` (2026-03-26) and the archive banner `1d77168` (2026-04-22), and no
2026-04-25 commit exists in `collatz-cycles-lean` (2026-04-25 is
`collatz-nocycle-lean4`'s last push date). Recorded flat; nothing turns on it.

Junction placement, for completeness: `docs/PROOF_ASSEMBLY.md` exists on
`proof-assembly-v1` only (`main` and `syracuse-jepa-v2` have no copy), so "both
copies" is exactly two files, and both are marked. His §1 self-correction also
checks: the file's header says `**Branch:** proof-assembly-v1` while the round-11
copy lived in `collatz-cycles-lean`, whose only branch is `main`.

---

## Item 5 — the push structure: consistent, with one flat refinement

GitHub's activity log for both repositories, 2026-07-29 (UTC):

| Time | Repository | Ref update |
|---|---|---|
| 07:20:02Z | `collatz-cycles-lean` `main` | `1d77168 → d7dbb7a` (pass 1) |
| 07:20:12Z | Junction `proof-assembly-v1` | `3caaa11 → 6de1743` (**carries `98b2de6`**, STATUS.md, pass 1) |
| 07:51:25Z | `collatz-cycles-lean` `main` | `d7dbb7a → 995c98c` (pass 2) |
| 07:51:26Z | Junction `proof-assembly-v1` | `6de1743 → ff27436` (pass 2) |
| 12:10:13Z | `collatz-cycles-lean` `main` | `995c98c → b38758d` (pass 3) |
| 12:10:15Z | Junction `proof-assembly-v1` | `ff27436 → 8ff1010` (pass 3) |

These are the only pushes to either repository after 2026-04-25. Commit timestamps
precede their pushes by seconds throughout, cycles-lean first and Junction seconds
behind, both repos in step at each pass.

Consistency with his account, recorded flat with no adjudication of intent: three
retraction commits per repo — confirmed, the six commits he names and no others;
the push carried `98b2de6` with it — confirmed, and it was the **first** push of
the day (07:20:12Z) that did, alongside pass 1. The one refinement: his sentence
*"three passes … and only then the push"* reads as commits-then-one-push, while the
log shows **three paired pushes, one per pass**, each made within seconds of its
commits. The property his ordering exists to protect holds regardless and is the
thing worth stating: **at no moment was `98b2de6` publicly reachable from a tree
whose `PROOF_ASSEMBLY.md` carried no marker** — the push that published AUDIT_V9
also published STATUS.md and the first-pass retraction in the same ref update.

---

## Item 6 — the three round-11 verdicts, moved

The round-11 posture sentence is carried forward explicitly: **absence of a public
copy is not evidence against his account.** It was written for exactly this
resolution, and here it resolves: the account was true and the copies were simply
not public — one unpushed (AUDIT_V9), one self-gitignored (STATUS.md), one
unfinished at our look and since finished three times over (the markers).

| Round-11 verdict | New state | Where |
|---|---|---|
| `AUDIT_V9` NOT FOUND in any ref of any of the four | **CONFIRMED** — public at `audits/AUDIT_V9_PORTEE_2026-07-25.md`, `Collatz-Junction-Theorem` `proof-assembly-v1`, commit `98b2de6` (2026-07-25 11:30:01 +0200), parent = the then-public tip `3caaa11`, first reachable 2026-07-29T07:20:12Z. Residue not establishable read-only: the commit's existence before its push (timestamps are author-set); stated without implication either way | Item 2 |
| `STATUS.md` NOT FOUND in any ref | **CONFIRMED** — committed at `6de1743`; `.gitignore` line 52 gone, four-line reason in its place; all three described content points verbatim | Item 3 |
| `PROOF_ASSEMBLY.md` §10.6 still closing *"No gap remains"* at HEAD (`k > 50000` PROVED, not OPEN) | **CONFIRMED repaired** — permanent RETRACTED block atop both copies with all five elements; eighteen in-place markers counted independently, 18 = 18; the §10.6 closing line and all three PROVED rows marked; nothing deleted; both copies byte-identical at every pass; on the branch README `k > 50000` now reads **OPEN** | Items 4–5 |

---

## Reply material — one paragraph

We re-cloned both repositories and checked §§1–2 point by point, and all three of
round 11's not-found verdicts are closed, at full weight: AUDIT_V9 is public at
`audits/` on `proof-assembly-v1` at `98b2de6` with the date you named, and its
parent is the commit that GitHub's own push log shows as origin's tip from 18 March
until 29 July — so "exactly one commit ahead, never pushed" is what the graph
says, not just what you say; STATUS.md is committed with line 52 replaced by its
reason, and the three things you said it says, it says verbatim; and we counted the
PROOF_ASSEMBLY.md markers ourselves at `b38758d` and got eighteen, your named lines
where you named them, nothing deleted, and the two copies byte-identical at every
one of the six commits — we compared the committed blobs, one step stronger than
the working-copy diff you ran, and they agree at every stage. Round 11's posture
sentence — absence of a public copy is not evidence against the account — resolves
here exactly the way it was written to allow. One count of ours for your sequence:
under a single convention (in-place markers, the block's own heading excluded) we
get 7 → 15 → 18 rather than 7 → 14 → 18, and your carry-commit says sixteen — three
stated counts, three conventions, converging only at the end. That is not a
correction of the finding; it is a fourth instance of it, and your remedy sentence
already covers all four: the pattern and the range, never the tally.

---

## Closing

Access record, restated: read-only clones and read-only public API calls only. No
fork, no issue, no pull request, no comment, no star, no watch, no follow, no push,
no write of any kind, and no contact with anyone. `Projet_Collatz` untouched,
unrequested, unreached. No verification script was warranted: every count here is a
stated-pattern grep over cloned refs, recorded above with its pattern and lines.
