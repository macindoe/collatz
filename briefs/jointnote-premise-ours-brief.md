# Brief: joint-note premise pre-check, half A — **what is actually ours, and actually published** — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `HANDOFF.md` item 1, `publication.md`, `cycles.md` §12.8 (the uniform trim, the `1.585^(−p)` degradation, the staircase), `briefs/junction-public-recon-findings.md` §5.2 (the prior-art comparison completed this round).

## Why this exists

Merle's round-11 letter opens the joint note by asking for one thing before any structure is agreed: the note's contribution in one sentence a referee could repeat back. His own proposal, verbatim:

> Taking Macindoe's counting dichotomy as given, the note locates the obstruction that dichotomy identifies, exhibits it from three independent directions, and contributes a machine-checked fragment of the cycle literature.

And his reasoning for that shape, verbatim:

> I have written it that way deliberately. The dichotomy is already yours and already published; the note should present it, not appear to prove it for the first time. What would be new is the located obstruction, jointly, and the formalisation, mine. If we cannot write a sentence of that shape honestly, we should not write the note.

**The sentence itself is the author's to write. This session does not write it, does not propose wordings, and does not draft note prose.** What it produces is the factual ground the author needs in order to write it — because the sentence's load-bearing premise is a claim about *our* record, and a sentence of that shape is honest only if the premise is true as stated.

**Stopping-rule compliance:** a records audit of our own published and wiki material. No new computational front, no new mathematics, cycles front stays PARKED.

## Queue

1. **Does "counting dichotomy" name anything in our record?** Search the whole repository — the wiki pages, `paper/`, `sources/`, the published PDFs — for the phrase and for every near variant (`dichotomy`, `counting argument`, `counting bound`, `trichotomy`). Record every hit with its location and its exact wording. **State plainly whether the phrase is ours, his, or neither.** If it is his coinage for a result of ours, say that — it changes nothing about the mathematics and everything about how the sentence should read.

2. **Identify the result the phrase is evidently pointing at**, on the mathematics rather than the label. The candidate is the pair in `cycles.md` §12.8: the uniform trim exists and gives effective finiteness at every period (§12.8.1–12.8.2), *and* its constant provably degrades like `1.585^(−p)`, with the staircase family (§12.8.3) showing counting arguments cannot do substantially better. Record the exact statements, their section numbers, and their status words as the page carries them. If the two halves together are fairly described as a dichotomy — counting closes every period but provably cannot close them uniformly — say so in our own words; if the fit is loose, say exactly where it is loose. **This is the audit's product.**

3. **"Already published" — verify, do not assume.** For whichever result item 2 identifies:
   - Is it in paper 1 (DOI 10.5281/zenodo.21273548), paper 1 v2 (10.5281/zenodo.21421120), or the mirror paper (10.5281/zenodo.21303918)? Check the actual PDFs/sources in `paper/` and `sources/`, not `publication.md`'s summary of them.
   - Record the section number and the statement **as printed in the published artifact**, and whether the published form carries the same strength, the same hypotheses and the same scope as the wiki's current form. Wiki pages are rewritten in place; the published PDF is frozen. Any gap between them is exactly the kind of thing that makes a referee-facing sentence wrong.
   - If a load-bearing half is in the wiki but *not* in any published paper, say so explicitly and identify which half.
4. **"Already yours" — check the attribution as our own record states it.** Does anything in the identified result rest on Merle's contributions, on the correspondence rounds, or on jointly verified material? The two-key protocol means several things in the ledger are joint; the point here is only to establish whether *this* result is unambiguously ours as of its publication date. Record dates. No credit adjudication beyond what our own record already says.

5. **The other two clauses of his sentence, checked against our record only** (the external half is a sibling session's, `briefs/jointnote-premise-external-brief.md` — do not duplicate it):
   - *"locates the obstruction that dichotomy identifies"* — what does our record actually say the obstruction is? `README.md`'s "where the difficulty actually lives", `stage4.md` §11.8.7.7 (the digit-consumption observation, and note its status word — organizing heuristic, not theorem), `cycles.md` 12.6.1.3, and the `×2×3` gap he names. Record the status words precisely: which of these are theorems, which are calibrated observations, and which are heuristics. A sentence that calls a heuristic a located obstruction is the failure mode to protect against.
   - *"exhibits it from three independent directions"* — identify the three faces as our record has them, and check the word *independent* against what we can support. His round-11 letter also proposes a fourth face (the drift), which the hygiene check found to be the seam identity re-expressed rather than an independent direction (`briefs/merle-r11-hygiene-check-findings.md`). Record whether "independent" survives that, and at what count.

6. **The prior-art item found this round, stated flat.** `briefs/junction-public-recon-findings.md` §5.2(iv): his `PROOF_ASSEMBLY.md` §10.5, dated 17 March 2026, already confines the dangerous `k` to convergent denominators of `log₂3` — the L-A8/T1 frame-prediction point, months before our rounds. Record what that does and does not bear on: it is his, it predates the correspondence, and it belongs in the note's credit language. Do **not** adjudicate priority; record dates and documents so the author can.

7. **Anything in our published record that a referee would find and that the sentence would then have to survive.** Read `publication.md` and the papers' own scope/limitations language, and record any statement of ours that constrains what the note may claim — in particular anything about what the program does *not* claim (`README.md`'s closing paragraph is explicit). One short list.

8. **Record** (branch commits, per item):
   - `briefs/jointnote-premise-ours-findings.md` — a per-premise verdict table (premise as he states it / what our record says / verdict: supported, supported-with-qualification, or not supported), with every section number and DOI pinned, the published-vs-wiki gap stated where one exists, and the status words carried exactly.
   - A verification script only if something needed computing; if nothing did, say so rather than inventing one.
   - `HANDOFF.md` item 1 — ONE scoped paragraph. A sibling session (`jointnote-premise-external`) edits item 1 in parallel; keep to your own lines.

## Rules

- Branch **`jointnote-premise-ours`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA given in your launch instructions, and state the base SHA in the findings.
- Per-item commits. Do **not** merge — the main session reviews and merges.
- **Facts only.** No draft of the contribution sentence, no alternative wordings, no note prose, no opinion on whether the note should be written. If a premise is not supported, the finding is the fact that establishes it, not a recommendation about what to say instead.
- Read-only outside this repo; no pushes; no interaction with his repositories.
- Where the wiki and a published paper differ, both are recorded; neither is "corrected" in passing. `sources/` is immutable.
- Stop after item 8.
