# Brief: round-11 Lean re-audit — the ceiling repair (`ceiling_lower` / `ceiling_pinned`, `hceil` removal) — read-not-built — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `HANDOFF.md` item 1, `briefs/merle-lean-r10-audit-brief.md` and `briefs/merle-lean-r10-audit-findings.md` (this session is the direct sequel — the mismatch it found is what he has now repaired), `briefs/merle-la8-t1-check-findings.md` (our clean-room derivation of every link in the T1 chain, and the cycle data).

## Provenance

Our round-10 audit found one substantive mismatch: `ceiling_upper` proved the **upper half only** (`2^K < 2·3^(p+1)`), while the L-A8 ledger block stated both bounds; the lower half `3^(p+1) < 2^K` travelled downstream as an unproved elementary hypothesis `hceil` through `ratio_bound_at_barina`, `log_gap_at_barina`, `log_gap_gen` and `quotient_is_convergent_gen`. We offered a one-lemma repair or a restatement, his choice.

His round-11 letter (2026-07-27) reports the repair, and reports it going further than we offered:

- **`ceiling_lower` is now kernel-3**, derived in one line from `cycle_prod_identity`: every factor `3x+1` strictly exceeds `3x`, so `3^(p+1)·Px < 2^K·Px`, and `Px > 0` cancels.
- **`ceiling_pinned`** gives both bounds in one statement.
- **`hceil` is REMOVED from all four downstream signatures** rather than merely satisfied — "derived internally now, so it cannot travel as an assumption again."
- **Fifteen theorems** (round 10 audited thirteen), 0 `sorry`, no `native_decide`, no user axioms, all four hardened checks clean.
- Incidental, volunteered: when he first placed the lemma *after* its own uses, Lean's error recovery inserted `sorryAx` into the downstream proofs, and check 3 of the hardened protocol caught it in the same run.
- **DeficitLemma axiom log now covers 10 of 10** — `key_shifted` and `key15` have their own probes, so check 4 is met for them directly and not only transitively (round 10 recorded 8 of 10).
- **The stale DeficitLemma SCOPE header** — which still said `MarginTarget` was outside Lean, two hundred lines above its proof — corrected in place, with the finder named.
- **The standalone RETRACTED block is back** in `T1Structure.lean` at **`c991430`**, marked DO NOT REMOVE, stating what was claimed, why it was false, the real obstruction, the fix, and the four-way hardening; our observation is named in it. (Round 10 recorded the full note at `7d46474`, superseded at `4856058` by a one-line reference — his point is that a record requiring `git log` to find is not a record.)

Stack: **`6c084c5`** and **`c991430`**, over `5c9b663`.

We have no Lean toolchain here. This is a **read-not-built statement-match audit**, precedent `experiments/merle_lean_r10_audit.py`. State the trust boundary plainly in the findings: we verify that the statements say what the ledger and letter claim they say, that the dependency structure is what he describes, and that the committed axiom logs match; we do not re-run the kernel.

**Stopping-rule compliance:** verification of a correspondent's artifacts, no new computational front, cycles front stays PARKED.

## Queue

1. **Clone and graph.** Fresh read-only clone of `ericmerle3789/one-obstruction-three-faces-lean` into the scratchpad. Record HEAD (expected `c991430`, with `6c084c5` beneath it). Verify the graph from `5c9b663` is linear and record it commit by commit with one line each on what that commit changed. Diff `ContentDescent.lean`, `ContentSeparation.lean`, `TransportRecurrence.lean`, `LegendreApprox.lean` against their previously audited SHAs — expected unchanged; **any drift is a finding**, and drift in `LegendreApprox.lean` is a finding that bears on a sibling session (see `briefs/junction-public-recon-brief.md`).

2. **`ceiling_lower` and `ceiling_pinned` — statement match.**
   - Record both statements verbatim. State in your own words what each encodes.
   - Do the hypotheses match `cycle_prod_identity`'s — i.e. is the lemma proved for the *same* notion of genuine cycle (rotation/`Fin`, all elements odd and positive), or does it carry extra hypotheses that the ledger's "the ceiling is pinned" does not mention?
   - Is `Px > 0` proved in-file or assumed? The cancellation is the whole argument; if positivity enters as a hypothesis rather than a consequence of the cycle's elements being positive, say so.
   - **Unconditionality is load-bearing:** confirm `ceiling_lower` needs no Barina input, no `x_min ≥ 2^71`, no window hypothesis. That is what makes it kernel and what permits the downstream removal. If it does depend on any of them, that is the audit's headline finding.
   - Does `ceiling_pinned` conjoin exactly the two bounds the L-A8 block states, in the block's own direction and strictness (`3^(p+1) < 2^K < 2·3^(p+1)`)? Record any strictness or index drift exactly.

3. **The `hceil` removal — verify it, do not take it.** This is the item most easily reported in good faith and still wrong.
   - Record all four signatures (`ratio_bound_at_barina`, `log_gap_at_barina`, `log_gap_gen`, `quotient_is_convergent_gen`) **verbatim at `5c9b663` and verbatim at HEAD**, side by side in the findings.
   - Confirm the hypothesis is *gone*, not: renamed; weakened to a differently-named hypothesis carrying the same content; absorbed into a `structure`/`class` field; or — the real trap — hoisted into a section `variable`, `include`, or `omit` declaration, where it vanishes from the printed signature while still being threaded. Check the enclosing section headers, not only the theorem lines.
   - Confirm it is genuinely *derived internally*: locate the call site of `ceiling_lower`/`ceiling_pinned` inside each of the four proofs and record it.
   - Anything else that changed in those four statements (window constants, `2000`/`2079`, the `4000·n² ≤ 2079·X` form, the convergent conclusion) must be recorded — a repair is a good moment for an unrelated drift to ride along unnoticed.

4. **Re-derive the repair ourselves, in our own words, independently.** Do not paraphrase his line. From the product identity for a genuine cycle, `∏(3x_i + 1) = 2^K ∏ x_i`; for positive integers `3x + 1 > 3x`, hence `3^n ∏x_i < ∏(3x_i+1) = 2^K ∏x_i`, and `∏x_i > 0` cancels to `3^n < 2^K`. Write out which index convention makes `n` equal his `p+1`, and confirm against `briefs/merle-la8-t1-check-findings.md` that this is the same `n` the rest of the chain uses. Confirm the argument is exact-integer and needs no analytic input.

5. **Canaries, fresh code, exact integers.** Write `experiments/merle_r11_ceiling_audit.py` from scratch (you may re-derive the cycle data, but do not import the old script):
   - Instantiate `ceiling_lower`, `ceiling_pinned` and the four repaired downstream statements at the four real cycles (both shores) and the trivial cycle; confirm each holds as stated, or is out of scope exactly where the hypotheses say.
   - Negative controls: exhibit a non-cycle tuple where `ceiling_lower`'s conclusion fails, confirming the hypotheses are load-bearing rather than decorative.
   - Statement-level canaries for the two new theorems at a few hundred synthetic `(n, K)` points including edges, in the manner of the round-10 audit.
   - Re-confirm the round-10 facts that the repair could have disturbed: the 22 in-window convergents, the discharge criterion, `δ = 4.0734·10⁻²²`.

6. **Axiom logs and the `sorryAx` claim.**
   - All **fifteen** theorems present in the committed T1 axiom log, each with its expected set; `discharge_all` `[propext]`; `convPairs_length` `[]`; the rest kernel-3. Reconcile 13 → 15: exactly `ceiling_lower` and `ceiling_pinned` added, nothing silently removed or renamed. If the count is not 13 + 2, say what else moved.
   - `sorryAx` absent everywhere in the current logs and files.
   - DeficitLemma axiom log: verify it now covers **10 of 10**, with `key_shifted` and `key15` carrying their own probes.
   - The corrected SCOPE header: record the new text and confirm it now matches the file it heads.

7. **The RETRACTED block at `c991430`.** Verify present in `T1Structure.lean`, standalone (not a one-line pointer), marked DO NOT REMOVE, and that it states all five things he lists. Record it verbatim in the findings. Re-confirm that no theorem at HEAD depends on the retracted result. Record flat, with no commentary on his conduct — the fact that it is there is the whole of it.

8. **Record** (branch commits, per item):
   - `experiments/merle_r11_ceiling_audit.py` + its committed output.
   - `briefs/merle-r11-ceiling-audit-findings.md` — verbatim statements; the four before/after signature pairs; the `hceil`-removal verdict with the section-variable check stated explicitly; our own derivation of the repair; the axiom-log audit and the 13 → 15 reconciliation; the RETRACTED block verbatim; the trust boundary; and a **key recommendation** on whether L-A8's kernel claims can now be keyed, scoped to what read-not-built supports (precedent: the ContentDescent language). Do not turn the key.
   - `HANDOFF.md` item 1 — ONE scoped paragraph. Two sibling sessions are editing item 1 in parallel (`junction-public-recon`, `merle-r11-hygiene-check`); keep your edit to your own lines.

## Rules

- Branch **`merle-r11-ceiling-audit`**. Verify your worktree HEAD contains this brief; if it does not, rebase onto the `main` SHA given in your launch instructions before starting, and state the base SHA in the findings.
- Per-item commits. Do **not** merge — the main session reviews (re-runs the script) and merges.
- Read-only outside this repo; no pushes; no forks, issues, stars, watches or comments on his repositories; no Lean toolchain installs — read-not-built is the protocol, not a limitation to route around.
- Discrepancies recorded and flagged, never disputed in prose. He repaired this because we found it; a second finding here is delivered exactly as flatly as the first.
- No reply paragraphs, no key turns, no co-edit commits, no ledger text. Stop after item 8.
