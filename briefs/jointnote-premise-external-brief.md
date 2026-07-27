# Brief: joint-note premise pre-check, half B — **the external facts** — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `HANDOFF.md` item 1, `briefs/merle-la8-t1-check-findings.md` (the Hercher adjudication — item 3 is the authority), `briefs/junction-public-recon-findings.md` (the newly public repositories and what they contain).

## Why this exists

Merle's round-11 letter proposes a shape for the joint note and, in doing so, states a number of checkable external facts. Two of them he volunteered as corrections to himself, which is precisely why they should be checked rather than assumed. **The note's framing depends on them, and every one is verifiable in minutes.**

His statements, verbatim where they matter:

> There is an organised effort — ccchallenge.org, "Formalising the Collatz literature, one paper at a time" — with 371 entries, and at the time I looked one formalised, four in progress and five awaiting audit. Steiner, Simons-de Weger and Hercher are listed and none is formalised. Your Macindoe2026 is catalogued there too, with an empty "Add formalisation".

> But I very nearly wrote "the first machine-checked fragment of the cycle literature", and that would have been false and checkable in one click: Eliahou 1993, "New Lower Bounds on Nontrivial Cycle Lengths", already carries a formalisation awaiting audit. So the honest form is "a fragment", not "the first".

And, for the abstract's position paragraph:

> The note's exclusions are weaker than the published record (Hercher m >= 92, K > 1.375e11, and on a strictly weaker verification hypothesis than ours).

**This session establishes facts. It does not write note prose, does not propose the contribution sentence, and does not recommend a framing** — the sentence is the author's, and half A of this pre-check (`briefs/jointnote-premise-ours-brief.md`, a sibling session) covers our own record. Do not duplicate half A.

**Stopping-rule compliance:** an external records check. No new computational front; cycles front stays PARKED.

## Queue

1. **`ccchallenge.org`, checked directly.** Record, with the date and time of the check and the URL of each page consulted:
   - The site's stated purpose and scope, in its own words.
   - **The entry count** (he says 371) and **the status breakdown** (he says, at the time he looked: one formalised, four in progress, five awaiting audit). Record the current numbers. A drift since he looked is not a discrepancy — record both readings and say which is which.
   - Whether **Steiner**, **Simons–de Weger** and **Hercher** are listed, and each one's formalisation status.
   - Whether **`Macindoe2026`** is catalogued, exactly how it is catalogued (which paper, which DOI, what metadata, whose entry it appears to be), and whether its formalisation slot is empty. Record the entry verbatim. **Do not create, claim, edit or submit anything** — this is a read-only look at a public register.
   - Whether **Eliahou 1993, "New Lower Bounds on Nontrivial Cycle Lengths"** is listed and whether it carries a formalisation awaiting audit, as he says. This is the fact that turned his "the first" into "a", so it is the one most worth confirming.
   - Any submission/contribution process the site documents, recorded as fact only — whether we ever use it is the author's call and not this session's business.

2. **Hercher's published numbers.** Our own round-10 adjudication (`briefs/merle-la8-t1-check-findings.md` item 3) is the authority and already establishes: the bound is `K > 1.375·10^11` (Cor. 29), conditional on `X₀ ≥ 3·2^69`, met by Barina's `2^71`; the underlying threshold is exactly `q₂₃ = 137,528,045,312`; and the comparison with T1 **is** apples-to-apples on both axes, with the one asymmetry running in **Hercher's** favour on hypothesis and conclusion alike.
   - Check his letter's `m >= 92` against the paper and against our record. Is `m` his cycle-length parameter, and is 92 the right figure and the right symbol? Record the citation precisely (theorem/corollary number, statement as printed).
   - Check the clause **"on a strictly weaker verification hypothesis than ours"**. Weaker *for whom*, and in which direction? Our record says his corollary needs strictly *less* verified range than T1 instantiates — i.e. the asymmetry favours him. Confirm the clause as he wrote it says the same thing our record says, or record precisely how it differs. This is a sentence destined for an abstract, so the direction must be unambiguous.
   - Record whether Hercher's paper is formalised anywhere we can see (this connects to item 1).

3. **The shared repository's `NOTE.md`.** He refers to "the NOTE.md skeleton from 19 July" and proposes three changes to it. Take a fresh read-only clone of `github.com/macindoe/one-obstruction-three-faces` and record:
   - Current HEAD (our record expects **`c966875`**, our own round-10 co-edit push) and whether it has moved since. If it has moved, record the new commits and who made them — that is material to the whole round.
   - `NOTE.md` as it currently stands: its section structure, and specifically what §6 ("what remains") and the abstract-or-opening currently say, since his three proposals are (i) make the counting dichotomy the load-bearing result and the three faces its instances, (ii) state the position once, early, in the abstract, (iii) treat the genre as mapping-and-instruments rather than announcing a result.
   - Whether a 19 July skeleton is what is actually there, or whether it has been revised since (our record notes he rewrote §4 and §6 on 2026-07-24). Record the discrepancy if the date does not match — flatly; a misremembered date in a letter is not a finding of substance, but the note's shape should be discussed against the file that exists.

4. **The three faces, as the note would present them.** From `NOTE.md` and our own record, list the three faces the note currently names, with the ledger entry or wiki section each rests on and its two-key status. Then record, as a plain fact and without recommendation, which of them are at two keys today and which are not. (Half A checks the *independence* of the three; you check their *status*.)

5. **Anything external that would embarrass the note.** One short list, facts only: results in the published cycle literature that the note's exclusions do not reach, any formalisation of the same territory by a third party, and — relevant since this round — the fact from `briefs/junction-public-recon-findings.md` that `PROOF_ASSEMBLY.md` at HEAD still carries an unconditional claim about a module the same repository marks INVALID, which matters if the note cites that repository.

6. **Record** (branch commits, per item):
   - `briefs/jointnote-premise-external-findings.md` — a per-fact table (his statement / what the source says / verdict / date checked / URL or citation), the `ccchallenge` entry for `Macindoe2026` verbatim, the Hercher citation with its exact statement, the current `NOTE.md` structure, and the three-faces status list.
   - A script only if something needed computing; otherwise say so.
   - `HANDOFF.md` item 1 — ONE scoped paragraph. A sibling session (`jointnote-premise-ours`) edits item 1 in parallel; keep to your own lines.

## Rules

- Branch **`jointnote-premise-external`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA given in your launch instructions, and state the base SHA in the findings.
- Per-item commits. Do **not** merge — the main session reviews and merges.
- **Read-only everywhere.** No pushes to any repository including the shared one; no forks, issues, stars, watches, comments or follows; **no submission, edit, account creation or claim of any kind on `ccchallenge.org`**. Record what is there; touch nothing.
- **Facts only.** No draft of the contribution sentence, no note prose, no framing recommendation. Where his statement and the source differ, record both and let the difference stand.
- Stop after item 6.
