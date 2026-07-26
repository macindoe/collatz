# Brief: round-10 Lean statement-match audit — DeficitLemma + T1Structure (read-not-built) — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `HANDOFF.md` item 1, `briefs/merle-la5-closure-findings.md` (the ContentDescent statement-match precedent — this session repeats that pattern on two new files), `briefs/merle-la7-mu-check-findings.md` (operational definitions: `R(n)`, best cell, `q = 2^K − 3^n`, word counts).

## Provenance

Merle's Lean repo `ericmerle3789/one-obstruction-three-faces-lean` moved `97b57d7 → 5c9b663` (~20 commits). Two new proof files carry the round's claims:

- **`OneObstruction/DeficitLemma.lean`** (stacks `f844467 → 9521b16 → 266f26b → b22fafc`): **ten theorems claimed kernel-3, 0 sorry, no user axioms, no `native_decide`**, ending in
  `marginTarget (n K) (1 ≤ n) (3^n ≤ 2^K) (2^K < 2·3^n) : C(K−2, n−1)^13 · 2^n ≤ 2^(13K)`
  via `deficit_term_le (m k) (k ≤ m) : 12^k · 7^(m−k) · C(m,k) ≤ 19^m`, atoms `A`/`a`/`D`, `key_core`, `key_shifted`, `key15`, `margin_core`.
- **`OneObstruction/T1Structure.lean`** (stacks `41fa4f8 → 81054ea → 89d9efc → dac39a3 → da2c8db → 7d46474 (RETRACTION) → 4856058 → 5c9b663`): **thirteen theorems claimed kernel-3, 0 sorry, no `native_decide`, no user axioms**; chain `cycle_prod_identity → survivor_bound → seam_bound → log_gap_gen → quotient_is_convergent_gen`, plus `ceiling_upper`, `seam_gap_at_barina`, `ratio_bound_at_barina`, `log_gap_at_barina`, and the finite discharge `discharge_all` (claimed axioms **`[propext]` only**; `convPairs_length = 22` claimed **no axioms at all**).
- **`OneObstruction/LegendreApprox.lean`** — imported from his separate "Junction" repository; claimed 0 sorry / 0 axioms / 0 native_decide, wrapping Mathlib's Legendre criterion; entry point `abs_sub_ge_of_not_convergent`.
- **A retraction on record:** commit `da2c8db` claimed the Legendre step kernel-3; it was false (stack overflow read as "0 errors"; `sorryAx` at workable recursion depths). Withdrawn at `7d46474` with a RETRACTED note; his verification protocol hardened to four checks (error lines AND overflow/abort AND `sorryAx` AND presence in the theorem's own `#print axioms` probe).

We have no Lean toolchain here: this is a **read-not-built statement-match audit**, precedent `experiments/merle_contentdescent_check.py` (4,541 exact checks). Trust boundary stated plainly in the findings: we verify that the *statements* say what the ledger claims they say and that the committed axiom logs match; we do not re-run the kernel.

**Stopping-rule compliance:** verification of a correspondent's artifacts, no new computational front, cycles front stays PARKED.

## Queue

1. **Lean repo, read-only.** Fresh clone (scratchpad). Record HEAD (expected `5c9b663`; if moved, record and continue read-only at `5c9b663`). Verify the commit graph from `97b57d7` is linear and record it. Diff `ContentDescent.lean`, `ContentSeparation.lean`, `TransportRecurrence.lean` against the previously audited SHAs — expected unchanged; flag any drift.

2. **DeficitLemma.lean statement match.**
   - Record all ten theorem statements verbatim (findings). For each, state in one line the mathematical claim it encodes and whether hypotheses/conclusion match the ledger's prose.
   - **The load-bearing question:** does `marginTarget` actually encode `margin(n) ≥ n/13`? Unfold: taking `log₂`, the conclusion reads `13·log₂C(K−2,n−1) + n ≤ 13K`, i.e. `K − log₂C(K−2,n−1) ≥ n/13`. Match `C(K−2,n−1)` against OUR operational word count at the best cell (from the la7 findings) and `K` against `log₂` of the ticket denominator — is `margin(n)` as the L-A7 entry uses it exactly `K − log₂ #words`? If there is any gap (e.g. words counted by compositions vs binomial, north vs both shores, the `K` range `3^n ≤ 2^K < 2·3^n` covering exactly the cells the entry needs — what about the south shore / `2^K < 3^n` cells?), state it exactly; that is the audit's product.
   - Statement-level canaries in fresh Python, exact integers: instantiate `deficit_term_le` and `marginTarget` at ~200 `(m,k)` / `(n,K)` points including edges (`k = 0`, `k = m`, `n = 1`, both `K` values per `n`); confirm the inequalities hold as stated (a false statement would be caught here even without a kernel).
   - Axiom log: `experiments/DeficitLemma_axioms.txt` — verify all ten theorems appear, each with exactly `{propext, Classical.choice, Quot.sound}`; flag anything extra or missing.
3. **T1Structure.lean statement match.**
   - Record all thirteen theorem statements verbatim; same one-line-per-theorem match against the L-A8 ledger blocks.
   - **Load-bearing questions:** (i) does `cycle_prod_identity` quantify over genuine cycles (rotation/Fin, all elements odd positive) as the entry claims; (ii) `ceiling_upper`'s hypothesis — the entry states `2(p+1) < 3X` with all elements `≥ X`; letter says `2n < 3·x_min` — same thing? record precisely; (iii) `quotient_is_convergent_gen` — is the window hypothesis exactly `4000·n² ≤ 2079·X` and the conclusion "`K/n` is a convergent of `log₂3`" in Mathlib's sense; (iv) `discharge_all` — record the `convPairs` list verbatim (all 22 pairs `(q_j, q_{j+1})`) and the criterion `2000·q·(q+q′) ≤ 2079·2^71`; independently compute the convergent denominators of `log₂3` in fresh Python (high-precision continued fraction, ≥ 60 guard digits, stability check at two precisions) and confirm the list is exactly the denominators in the window — this is one of the two glue facts he names as unproved, so OUR independent confirmation is the value here; (v) trace the implication direction: `θ_j > 1/(q_j+q_{j+1})` (classical) + criterion `2000·q·(q+q′) ≤ 2079·2^71` ⟹ the seam constraint `‖nL‖ < nδ` FAILS at `n = q_j` — write the two-line derivation out and confirm the inequality directions and the constants 2000/2079 (vs the exact `3·ln2/4`), including why the integer form is conservative.
   - Verify the RETRACTED note is present in the file as described, and that no theorem in the current file depends on the retracted one.
   - Axiom log(s) for T1: all thirteen theorems present; `discharge_all` with `[propext]` only; `convPairs_length` with `[]`; the rest kernel-3; flag deviations.
4. **LegendreApprox.lean.** Record its statements and claimed axioms; confirm `abs_sub_ge_of_not_convergent` states Legendre's criterion contrapositive (`|L − K/n| < 1/(2n²)` ⟹ `K/n` convergent — record the exact form and any hypotheses, e.g. coprimality/positivity, and whether `quotient_is_convergent_gen` discharges them). Note its provenance (Junction repo) — do NOT audit the Junction repo itself; that is a later, separate item.

5. **Record** (branch commits, per-item):
   - `experiments/merle_lean_r10_audit.py` + committed output (the canary instantiations + the independent convergent computation; one commit).
   - `briefs/merle-lean-r10-audit-findings.md` — verbatim statements; per-theorem match table; the marginTarget-encodes-margin verdict with the unfolding written out; the convPairs independent confirmation; the direction-trace; the axiom-log audit; the trust boundary stated; key recommendation scoped to what a read-not-built audit can support (precedent: the ContentDescent language).
   - `HANDOFF.md` item 1 — ONE scoped paragraph on this audit's state; siblings `merle-la7-close-check` and `merle-la8-t1-check` edit item 1 in parallel — keep your edit to your own lines.

## Rules

- Branch **`merle-lean-r10-audit`** from your worktree HEAD (verify it contains this brief; state the base SHA in the findings). Per-item commits; do NOT merge — the main session reviews and merges.
- Read-only everywhere outside this repo; no pushes; no web access; no Lean toolchain installs (read-not-built is the protocol, not a limitation to work around).
- Discrepancies recorded and flagged, never disputed in prose. A statement that does not match its ledger prose is a finding delivered kindly, exactly like the μ re-source.
- No reply paragraphs; no key turns (recommendation only); no co-edit commits; stop after item 5.
