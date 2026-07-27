# Brief: round-11 co-edit — the L-A8 kernel key, his proposed "K pinned" wording, and the round's offers — PREPARE LOCAL-ONLY — for a delegated session

**Context required before starting (in order):** `README.md`, `AGENTS.md`, `HANDOFF.md` item 1, and this round's five findings files, which are the authority for every number and verdict you will write: `briefs/merle-r11-ceiling-audit-findings.md`, `briefs/junction-public-recon-findings.md`, `briefs/merle-r11-hygiene-check-findings.md`, `briefs/jointnote-premise-ours-findings.md`, `briefs/jointnote-premise-external-findings.md`. Also `briefs/merle-round10-coedit-findings.md` for the house pattern (prepared blocks verbatim, offers inside entries, patch archived).

**Where a brief and a findings file disagree, the findings file wins.** That rule exists because it was broken once (round 10, the Hercher "apples-to-apples" clause) and again in a milder form this round.

## The state you are working from

- Shared repo `github.com/macindoe/one-obstruction-three-faces`, HEAD **`c966875`** — our own round-10 co-edit push. **Verified unmoved by the main session on 2026-07-28** (`ls-remote`: `c96687544fd387fd8bcff1df2c04056a2be99f3a`). Nothing of his has landed since round 10. **Re-verify it yourself at the start and again immediately before you finish**, and record both checks.
- His Lean repo HEAD **`c991430`** over `6c084c5` over `5c9b663`.
- Round 11's four verification windows are all reviewed and merged on our `main`.

## What this session does, and does not

**Prepare one shared-repo commit, LOCAL-ONLY, and do not push.** The push is the author's decision, and this round it is additionally gated (see "Pre-push condition"). You work in a **scratchpad clone**, on a local branch, and you archive a portable patch back into this repository.

`LEDGER.md` only. **His prose is untouched everywhere** — corrections are offered *inside* the entries, never applied to his sentences. Offers are offers; his acceptance is his.

**Not in this commit:** anything about the Junction repositories (reply material, as at round 10); the joint note and its contribution sentence (the author's); any new entry for a claim of *his* that has no entry yet (see item 6).

## Queue

1. **L-A8 — turn the Macindoe kernel key, scoped.** Round 10 turned our key on the mathematics of every link and deferred every kernel claim to the Lean audit. That deferral is now discharged: `briefs/merle-r11-ceiling-audit-findings.md` is the record — 190 exact checks, 0 failures, the `hceil` removal verified rather than taken, the axiom logs reconciling 13 → 15 exactly, `sorryAx` absent, the RETRACTED block standalone.
   - Write the key-turn block in the **ContentDescent language** (the precedent that worked twice): statement match, dependency structure, committed axiom logs, the instantiation checks, our own derivation of the repair — with **read-not-built in the same sentence**, and explicitly outside the key: the two continued-fraction glue facts (independently confirmed, not kernel-proved) and `LegendreApprox.lean`'s absent axiom-log entry.
   - **Do not write, and do not imply, that T1's chain is machine-checked end to end.** The findings' key recommendation says so in terms.
   - Pin the artifacts. Every record in this commit pins one, per the round-10 consistency call.

2. **The "K pinned" wording — take his proposal.** He wrote, and it is his own proposal about his own claim:

   > My proposal, and it is only a proposal: the entry says the ceiling is pinned, cites `ceiling_pinned`, and notes that the lower half was found missing in your round-10 audit and proved afterwards. Your key on the kernel side belongs wherever you judge it belongs.

   He deliberately left `LEDGER.md` untouched rather than restate his own claim after we caught it. **Write it as he proposed**, citing `ceiling_pinned` and `ceiling_lower`, with the round-10 finding and the round-11 repair both named factually and without moral. Record in the findings that the wording is his proposal adopted, so the history is unambiguous.

3. **The one-sidedness sharpening — offered as a gift, not a correction.** Because `ceiling_lower` is now a theorem, a positive cycle is confined to convergents *above* `log₂3`. `p₂₂/q₂₂` falls below (`−1.016·10⁻²²`) and `p₂₃/q₂₃` above (`+9.427·10⁻²⁴`), so the first admissible north-shore scale is `q₂₃ = 137,528,045,312` — **exactly Hercher's underlying threshold**. This tightens our own la8 §(f) sentence, not anything of his, and it makes his own frame-prediction point land harder than he claimed it. State it that way.

4. **The round's offers, all minor, all his call** (sources: the ceiling-audit findings' five hygiene offers, and the hygiene-check findings):
   - axiom-log headers / raw probe output restored (the deleted headers took the four-way claim out of the artifact);
   - `#print axioms` probes for `mul_pow_succ_le` and `pow_succ_lt_two_mul_pow`;
   - a probe and log entry for `LegendreApprox`'s two theorems;
   - the `1.700 bits` clause pinned to the route-implied bound (already offered at round 10, still open);
   - **the two `q₂₁` in `T1Structure.lean`** (line 188 the shifted `6.547·10¹⁰`, line 433 the correct `6586818670`) and the pre-054 `δ` in the same docstring — his sweep reached the Python and not the Lean comments;
   - **Cor. 29's `X₀ ≥ 3·2⁶⁹`, promised in his letter and not landed** in the Lean repo — recorded as promised-not-yet-landed, with no complaint;
   - **the deleted `OUT-052` `(d-bis)` section.** This one is different in kind and should be marked as such: the ledger's own **L-A8 seed block cites its `median 15601 vs control 1` and `14936 = 22·665 + 306`**, and the repaired script no longer produces them, so a sentence already in the shared ledger has no committed artifact behind it. Offer the remedy he himself used for 043/055/056 — commit the generator. Flat, and framed as the same good habit, not as a lapse.

5. **The verification record for the hygiene pass.** Everything reconciled; nothing failed. Include, because it is his own work checking out: all five scripts run here and reproducing their committed outputs; the numbers independently recomputed; **`5.17× at j = 21` confirmed CORRECT** (we queried it, we were wrong, and the record should say so plainly); and the `053` monotonicity argument **exhibited** — valid, needing no hypothesis, but yielding `≥ 22` rather than `= 22`, with the equality a separate computation at a margin of only `2.0039×`. He ran it. Say so.

6. **The theorem hand-back — the third face made exact.** Verified on all four real cycles both shores:
   `Σᵢ log₂(1 ± 1/(3xᵢ)) = K − n·log₂3` **exactly** — the seam identity written one step at a time. His "third face of the same wall" is right and stronger than he states it.
   Two corrections inside the same offer, both flat: "summed around a cycle that is exactly `n·δ`" is **not** an identity but a sharp upper bound `Σ D(xᵢ) ≤ n·D(x_min)`, equality only when every element sits at the minimum (on `−17`: `0.188` against `0.396`); and what *is* exact is **`D(x_min) = δ·(1 + 1/(27x_min²))`** — `δ` is the per-step north–south drift at the minimum element and sits strictly *below* it. **Check that direction character by character before you write it.** It was written backwards once this round, in a findings summary, and corrected at merge; the body of `briefs/merle-r11-hygiene-check-findings.md` has it right in three places. Add the `x = 1` corollary as ours.

7. **Our own bookkeeping, since we are in the file.** `L-A3 (B)` still reads "two keys once Merle's acceptance of the asymptote lands"; our record has that acceptance in his round-9 letter. Date-stamp it as met, exactly as round 10 date-stamped the L-A7 conditional. Our line, our fix — but still a single-line pure-append modification, and count it in the diff stat.

8. **What you must NOT do about Face I.** `briefs/jointnote-premise-external-findings.md` records that his δ8 impossibility — Face I's Merle half — has **no ledger entry at all**, against `NOTE.md`'s own rule that every claim enters via a turned entry. **Do not create an entry for his claim.** That is his to seed, and the observation is reply material. Record in your findings that you deliberately left it alone.

9. **Prepare, verify, archive.**
   - One commit on a local branch of a scratchpad clone over `c966875`. Record: SHA, tree hash, files touched, exact insertion/deletion counts, and a one-line justification for every "deletion" (they should all be pure-append single-line modifications, as at rounds 9 and 10).
   - Generate the patch, verify it applies clean on a **pristine** `c966875` and yields a **tree-identical** result, and archive it at `briefs/merle-round11-coedit-patches/`.
   - Re-verify the remote unmoved immediately before finishing.

10. **Pre-push condition — state it prominently, at the top of your findings.** Every artifact this commit pins lives in commits on our wiki `main` that exist **only locally** (round 11's merges: `3aeecbc`, `185d44b`, `185c622`, `836735b`, `b782e59`, and whatever this branch adds). Public `main` is behind. **List every pin you write and check each against the public remote**, then state plainly: the author must push wiki `main` before or with the shared-repo push, or the pins do not resolve. That check is not optional — it is the round-9 and round-10 pattern and it caught a real problem both times.

11. **Record** (branch commits, per item):
    - `briefs/merle-round11-coedit-findings.md` — every prepared block **verbatim**, the diff stat with each deletion justified, the pin list with its resolve check, the remote-unmoved checks with times, the Face-I abstention, and the statement that his prose is untouched.
    - `briefs/merle-round11-coedit-patches/0001-*.patch`.
    - `HANDOFF.md` item 1 — ONE scoped paragraph. A sibling session (`merle-round11-reply`) edits item 1 in parallel; keep to your own lines.

## Rules

- Branch **`merle-round11-coedit`**. Verify your worktree HEAD contains this brief; if not, rebase onto the `main` SHA given in your launch instructions, and state the base SHA in the findings.
- **NOT PUSHED. Nothing leaves this machine.** No push to the shared repo, no push to our own remote, no interaction with his repositories.
- Per-item commits on our branch. Do **not** merge — the main session reviews and merges.
- Register: flat, calibrated, no excitement inflation. Corrections are offered, never applied to his sentences. A finding delivered kindly is still the finding.
- Encoding: use the Edit/Write tools, never PowerShell `Get-Content`/`Set-Content`; run `experiments/encoding_scan.py` before your last commit.
- Stop after item 11.
