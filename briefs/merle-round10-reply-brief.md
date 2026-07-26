# Brief: round-10 reply draft (business paragraphs) — for a delegated session

**Context required before starting (in order):** `README.md`, `AGENTS.md`, `HANDOFF.md` item 1 (all round-10 paragraphs), then the five round-10 records — `briefs/merle-la7-close-check-findings.md`, `briefs/merle-lean-r10-audit-findings.md`, `briefs/merle-la8-t1-check-findings.md`, `briefs/margin-inequality-proof-findings.md`, `briefs/junction-repo-recon-findings.md`. Read `briefs/merle-round9-reply-draft.md` for the established register and shape.

## What this is

Merle sent **three letters** in one round (2026-07-25/26). The reply covers the business of all three. **Business paragraphs only** — the personal opening and closing, and anything answering his personal paragraphs, are the author's own and are not drafted here. Leave them as clearly marked placeholders.

**Every number, SHA and citation must be verified at its named place in the findings files before it goes in the draft.** That verification is part of the job, not a formality: this round contains several figures that are right only for a particular constant or a particular definition.

## The personal frame — read before drafting

His first letter told us who he is: a lycée electricity teacher, no doctorate, no mathematical training beyond his subject, who came to Collatz as a test of what these machines could do and got caught. He described a year of "joy, despair, and — many times — the electric certainty of having found the thing," every one dissolving on contact with verification, and said the protocol was "born out of those failures, one rule per wound."

**Do not answer any of that** — it is the author's to answer. But let it set the register: this round he withdrew an unbacked figure of his own with its cause stated, volunteered an honesty item nobody asked about, retracted a false kernel claim, and audited his own older repository into a weaker and truer headline. The draft's job is to match that standard, not to praise it. No warmth that the author has not chosen; no grading of his work.

## What the reply must carry

1. **L-A7 closed at two keys.** His acceptance satisfied our stated condition. Report our verification of the new blocks as digit-exact, and hand back the two upgrades — his south floor and `γ` identity are **theorems**, and our findings carry the one-line and symbolic proofs; his own reporting of them ("0 violations", "error 0.0 at fifty digits") undersells them.

2. **Our margin proof — the centrepiece, stated exactly and no stronger.** Theorem A for all `n ≥ 1` at the true `c_gen`, elementary, citing nothing; Theorem B′ the Robbins refinement; Theorem A′ the cell scope covering the whole south shore, which closes half the coverage gap our audit found against his `marginTarget`. **Include the honest part, prominently: our Stirling warning was based on a wrong premise.** A constant surplus is not a shortage — the constant is provably positive and uniform, so the crude entropy bound closes on its own, and concavity gives the perturbation step with no remainder. He restructured his whole route to avoid Stirling *on the strength of that warning*, and got a good proof out of it; his rational-`x` device is his own and stands as a genuinely independent second proof. Say this plainly rather than letting the credit sit ambiguously. Add the closed-form upgrade of his `[1.66, 2.10]` interval and the flat 7-digit-decimal correction (his figures are right for the constant he used).

3. **L-A8 key turned on the mathematics, kernel claims deferred.** Every link confirmed in the clean room. Both discrepancies resolved *without fault*: the two window figures are the exact and integral windows and both are right; the `q₂₁` collision is an indexing convention, substance right in both stacks. The Hercher observation **survives with a correction** — the coincidence is real and the frame-prediction point genuinely supported, but his bound is conditional (Cor. 29, `X₀ ≥ 3·2^69`) and the "3.9× further" comparison needs restating. **[CORRECTED AT REVIEW, 2026-07-26: this brief originally said that comparison "is not apples-to-apples". That is backwards, and the error is the main session's. Per `briefs/merle-la8-t1-check-findings.md` (Hercher adjudication item 3), the comparison IS apples-to-apples on both axes, with the asymmetry running in *Hercher's* favour — weaker hypothesis and further conclusion — so the phrase understates his advantage. The reply session caught the divergence against the findings, followed the findings rather than this brief, and flagged it; that was the right call and is why the draft is correct.]**

4. **The one substantive mismatch, delivered kindly:** `ceiling_upper` proves the upper half only, while the entry, docstring and commit all state both bounds; the lower half is threaded downstream as an unproved elementary hypothesis. One-lemma repair or restatement, his choice. Mention the axiom-log coverage (8 of 10) and `LegendreApprox`'s absence from the log its header names as hygiene, not as findings of substance.

5. **The Junction repository — ask, do not imply.** We could not confirm his self-audit because **the repository is not publicly reachable**: his handle shows three public repos, none containing `AUDIT_V9`. Nothing we found contradicts his account, and the reply must not suggest otherwise — a set-aside preprint repo may simply be private or unpushed, and he plainly assumed we could see it. Ask where it lives, in one sentence, without hedging and without insinuation. Note that we settled the `S`-vs-`K` unit question from his committed artifacts alone (the preprint's `S` is our `K`), so the deficit-lemma provenance is not blocked on access. **His `LegendreApprox.lean` is imported by the T1 chain and its home is unconfirmed** — worth one clause, because it bears on what the T1 formalization rests on.

6. **The retraction.** He reported it himself before we could find it. Acknowledge it once, factually, and note that our own audit confirmed the record is clean: the RETRACTED note is present, and nothing at HEAD depends on the withdrawn theorem. **No praise, no moral.** One or two sentences.

7. **The joint note.** He said yes and added that the account must be as honest about what it does not do as about what it does. Confirm agreement with that framing and with no schedule. Do **not** draft an outline or propose sections — that is the next arc and is the author's to open.

8. **The map:** where everything lives — the co-edit commit SHA (a parallel session prepares it; carry an explicit `[PENDING: shared-repo push — SHA to be filled at send time]` placeholder and do **not** claim that session's work), the wiki `main` pin, and our artifact paths.

## Queue

1. Draft to `briefs/merle-round10-reply-draft.md`. Business paragraphs only; personal opening/closing as clearly marked placeholders for the author.
2. Verify every number, SHA, section reference and citation against the findings files at drafting; state in the draft's own header that this was done and note anything that could not be verified.
3. One scoped paragraph in `HANDOFF.md` item 1.

## Rules

- Branch **`merle-round10-reply`** from your worktree HEAD; **verify the base against current `main` and rebase if stale** (worktrees are cut from session-start HEAD). State the base SHA.
- **Draft only. Nothing is sent, and nothing is pushed** — sending is the author's, always. No shared-repo writes, no Gmail, no contact of any kind.
- No ledger text (parallel session). Do not claim the co-edit session's work as your own.
- Register: flat, calibrated, no excitement inflation. Where the news is good, state the result and let it stand on its own.
