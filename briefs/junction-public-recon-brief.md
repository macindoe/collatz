# Brief: the Junction stack, now public — completing the recon that could not be done — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `HANDOFF.md` item 1, `briefs/junction-repo-recon-brief.md` and `briefs/junction-repo-recon-findings.md` (this session completes that one — every entry it recorded as NOT FOUND is now answerable), `briefs/merle-la7-close-check-findings.md` flag 6 (the `S`-is-`K` settlement, made from committed artifacts alone and now checkable at first hand), `briefs/merle-lean-r10-audit-findings.md` item on `LegendreApprox.lean` (the diff verdict recorded as NOT PERFORMED).

## Provenance

Round 10's recon recorded, correctly and carefully: **the repository his letter describes is not publicly reachable**, so his self-audit could be neither confirmed nor denied; every described point was logged NOT FOUND (repository inaccessible); the posture was stated explicitly — *absence of a public copy is not evidence against his account.*

His round-11 letters change that. The first names the repository and offers read-only invitations; the second, sent an hour later, supersedes it:

> Between writing that letter and sending it, I made the Collatz stack public. […] you do not need an invitation, and neither does anyone else.

Now public:

- `github.com/ericmerle3789/Collatz-Junction-Theorem` (MIT code, CC-BY 4.0 paper) — last pushed 22 April per his first letter; `AUDIT_V9` and `STATUS.md` live here; `LegendreApprox.lean` at **`lean/skeleton/LegendreApprox.lean`**
- `github.com/ericmerle3789/collatz-nocycle-lean4` (MIT)
- `github.com/ericmerle3789/collatz-cycles-lean` (MIT code, CC-BY 4.0 paper)
- `github.com/ericmerle3789/collatz-audit-2026` (MIT, added before publishing)

He states his reason — a formalisation nobody can open is a claim, not a contribution — and that he checked all four for credentials before flipping, and added MIT to one that had no licence at all.

**`Projet_Collatz` remains private and is OFF LIMITS.** Do not request access, do not accept an invitation, do not attempt to reach it by any route, and do not treat its absence as a gap in this recon. The author's standing decision: leave it be. Eight hundred files of process material bearing on no claim either side makes.

**Stopping-rule compliance:** recon and provenance settlement on a correspondent's now-public artifacts. No new computational front; cycles front stays PARKED. In particular, nothing here licenses a cycle search of any kind.

## Interaction discipline (unchanged from the round-10 recon, and binding)

Read-only clones only. **No fork, no issue, no pull request, no comment, no star, no watch, no follow** — no interaction of any kind that appears in his notifications or event stream. Record explicitly in the findings that none occurred.

## Queue

1. **Public status and licences.** For each of the four: confirm public, record HEAD SHA and date, default branch, branch/tag count, and the licence file present. Verify his licence account: MIT on code, CC-BY 4.0 on papers where he says so, and **which repository had no licence** — check whether the licence commit is dated at the flip. Record `Collatz-Junction-Theorem`'s last-push date against his "22 April". Flat statements of fact; no inference about motive anywhere.

2. **`Collatz-Junction-Theorem` — the self-audit.** This is the recon's headline.
   - Record `AUDIT_V9` and `STATUS.md` in full (quote the load-bearing parts verbatim in the findings).
   - His round-10 self-report: the README **overclaimed an unconditional no-cycles result** and was rewritten to match its own technical documents. Verify at first hand — find the overclaiming version in the history and the rewrite commit, record both texts, and state whether the current README's claims match what the technical documents in the same repository actually support. Where they do, say so; where they do not, that is a finding, recorded flat and delivered kindly.
   - Check the repository as we check any artifact: counts of `sorry`, `axiom`, `native_decide` by read; what is claimed proved versus claimed conditional; which external results are hypotheses (Simons–de Weger, Barina) and how they enter.
   - Resolve **each** NOT FOUND entry in `briefs/junction-repo-recon-findings.md` one by one, in a table: what round 10 could not find, what is there now, verdict.

3. **`LegendreApprox.lean` — perform the diff.** Recorded NOT PERFORMED because no counterpart existed to diff against.
   - Byte-compare `lean/skeleton/LegendreApprox.lean` (Junction) against the copy in `one-obstruction-three-faces-lean` (round 10: byte-identical since `da2c8db`). Record the verdict, the hashes, and which is upstream by commit date.
   - If they differ: record the diff in full — this file is imported by the T1 chain, so any divergence is material and belongs in the reply.
   - Either way, record the Junction copy's own `sorry` / `axiom` / `native_decide` counts by read, its imports, and whether its build context (Mathlib pin, lakefile) differs in a way that bears on the T1 chain's kernel claims.
   - A sibling session (`merle-r11-ceiling-audit`) is checking whether this file drifted in his Lean repo since `5c9b663`. If you find drift on the Junction side, say so in your findings and leave the reconciliation to the main session.

4. **The deficit lemma's provenance, at first hand.** Round 10 recorded it at second hand from the `DeficitLemma.lean` header ("Junction Theorem preprint 2026, §3") and his REQ-MATH-037 output; from those artifacts alone we settled flag 6 — **the preprint's `S` is our `K`** — on the units argument (`γ·log₂3 = c_gen` exactly, versus `γ·(log₂3 − 1) = 0.02928`). The preprint is now readable. Open §3: confirm or correct the settlement at first hand, confirm the deficit lemma is there and states what the header says it states, and record whether the preprint's own version is proved, conditional, or exhibited.

5. **The other three repositories — light recon, prior art the point.**
   - For `collatz-nocycle-lean4`, `collatz-cycles-lean`, `collatz-audit-2026`: what each claims, in its own status words; size and shape; `sorry`/`axiom`/`native_decide` by read; what is formalised versus asserted; what `collatz-audit-2026` audits.
   - **Overlap with our own record, stated flat.** `collatz-cycles-lean` and `collatz-nocycle-lean4` are exactly where a counterpart to our periods 1–3, the uniform trim (cycles.md §12.8.1), the `1.585^(−p)` degradation, or the staircase (§12.8.3) would live. Record any counterpart precisely: what he has, what we have, which is more general, and the dates. This is prior-art hygiene for a joint note, **not** a priority contest — no adjudication of credit, and no comparative adjectives.
   - Record anything that would change a claim of ours if true. That is the only thing here that is urgent.

6. **Our own record.** `HANDOFF.md` item 1 currently states that the repository "is not publicly reachable" and carries the NOT FOUND verdicts. Replace those lines with the settled state — the recon's posture paragraph (absence was not evidence) stays on record as written, without retroactive comment in either direction. One scoped paragraph.

7. **Record** (branch commits, per item):
   - `briefs/junction-public-recon-findings.md` — the NOT FOUND resolution table; `AUDIT_V9`/`STATUS.md` quoted; the README overclaim-and-rewrite verdict; the `LegendreApprox.lean` diff verdict with hashes; the flag-6 first-hand confirmation or correction; the three-repo recon with any prior-art counterpart stated flat; the licence facts; and the explicit statement that no interaction of any kind occurred.
   - Any verification script this required, plus its committed output, under `experiments/` (name it `junction_public_recon_*.py`). If nothing needed computing, say so rather than inventing a script.
   - `HANDOFF.md` item 1 — ONE scoped paragraph, per item 6. Two siblings edit item 1 in parallel (`merle-r11-ceiling-audit`, `merle-r11-hygiene-check`); keep to your own lines.

## Rules

- Branch **`junction-public-recon`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA given in your launch instructions, and state the base SHA in the findings.
- Per-item commits. Do **not** merge — the main session reviews and merges.
- No pushes anywhere. No writes outside this repository.
- `Projet_Collatz`: not touched, not requested, not discussed beyond recording that it stays private by his choice and ours.
- Findings only. No reply paragraphs, no ledger text, no key turns, no co-edit commits. Stop after item 7.
