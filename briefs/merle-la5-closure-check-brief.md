# Brief: L-A5 closure + kernel-key check (round 9, part 1) — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `HANDOFF.md` item 1 (through the L-A5 co-edit pushed state, shared HEAD `e53630f`), `briefs/merle-la5-check-findings.md` (esp. §(d), the exact corrected co-edit language), `briefs/merle-la5-coedit-findings.md` (the offer texts as pushed), `briefs/merle-round8-check-findings.md` (L-A4 verification, 12,888 checks — the laws the new Lean file formalizes), `cycles.md` 12.6.1.4 (descent identity).

## Provenance

Merle's round 9 arrived as a letter (2026-07-25, on file with the author; business content mirrored in shared-repo pushes) plus six shared-repo commits moving `main` from our `e53630f` to `81431c7`:

- `6b9f2b1` — "Review polish (Gemini pts 2-3)": NOTE §6 equidistribution disambiguation + L-A5 `#print axioms` citation and unreduced-modulus note.
- `49351e5` — L-A5 gloss restated per our offers (a) and (b); entry marked **two keys**.
- `92a6edb`, `fb5e8fc` — L-A6 seed + realizability filter (SEPARATE brief; not this session's scope).
- `08dc3d5` — new LEDGER block: Lean kernel key on the structured half (`ContentDescent.lean`, stack `67c428a`).
- `81431c7` — L-A7 seed (SEPARATE brief; not this session's scope).

His Lean repo `ericmerle3789/one-obstruction-three-faces-lean` has moved from `e297d9d` to `97b57d7`; the letter also cites a commit `905d75b` (committed `#print axioms` output for ContentSeparation) which he says has been in the stack and which our round-8/la5 checks recorded as absent — adjudicate that.

**This session's scope:** the L-A5 closure (does `49351e5` land what we offered, so that the two-keys marking is honest on our record?) and the ContentDescent kernel-key block (`08dc3d5`), plus the small `6b9f2b1` polish. Nothing else.

**Stopping-rule compliance:** record-verification of a correspondent's edits against our own offered texts, plus statement-level review of a formalization of laws we have already verified numerically (round 8: 12,888 checks, 0 failures). No cycle search, no new proof effort. Cycles front stays PARKED. Discrepancies are recorded flatly, never disputed in prose.

## Queue

1. **Shared repo, read-only.** Fresh clone (scratchpad). Record HEAD (expected `81431c7`; if moved again, record and continue read-only). Verify `49351e5` touches `LEDGER.md` only (2 insertions / 4 deletions expected) and `6b9f2b1` touches what its message says. Diff-verify that outside the restated gloss, the two-keys status line, and the `08dc3d5` block, the L-A5 entry (including our pushed verification record, the −17 exhibit, and both offer texts) is byte-identical to what we pushed at `e53630f` — our record must not have drifted.

2. **The restatement adjudication.** Compare `49351e5`'s new closing-gloss text word-by-word against (i) offer (a)'s long form as pushed at `e53630f` (in `briefs/merle-la5-coedit-findings.md` verbatim) and (ii) the findings §(d) language it came from. His own wording is equally welcome per our offer — the test is not textual identity but claim identity: the restated gloss must claim adjacency separation only (no word connected to `C = 1` by one-unit transfers), must NOT claim the wall, must name the isolated aperiodic peak as the open residual (NOTE §6), and must state the −17 exhibit correctly (primitive, `q = −139`, `C = 1` exact, totally isolated, negative shore). Verify the offer-(b) domain clause (`|q| > 1`, `0/0` at spent stock) is landed. Verify the key-status line now claims exactly two keys with both sides' grounds stated truthfully. Any claim the restated text makes that our checks did not verify is a flag, not a fix. Record verdict: CLEAN (two keys honest) or FLAGGED (with the exact clause).

3. **`6b9f2b1` review.** Diff NOTE.md: the §6 disambiguation should match our round-8 solitary-7 refinement (all primes structurally biased / non-uniform-but-unconfined, 7 strongest by the 2³−1 mechanism, resolution-dependence acknowledged) — verify it does not overstate what our part-A finding showed (mod 5 also crosses the significance bar at N = 30,000). Verify the L-A5 citation additions (the `905d75b` axioms link, the unreduced-modulus header note) point at real artifacts (next item).

4. **Lean repo, read-only.** Fresh clone. Record the commit graph from `017288f` through `97b57d7`; verify `905d75b` and `67c428a` exist and where they sit. At `905d75b`: `experiments/ContentSeparation_axioms.txt` — record contents; expected kernel-3 (`propext`, `Classical.choice`, `Quot.sound`) for all five ContentSeparation theorems; reconcile with our earlier "not committed" observation (was it added later than our check, or did we miss it? — the graph answers this; record which, flatly). At `67c428a`: read `OneObstruction/ContentDescent.lean` — record the exact statements of `cocycle` (`W0(l1 ++ l2) = 3^(msum l2)·W0(l1) + 2^(mssum l1)·W0(l2)`), `power_mult` (`W0(B^k) = G_k·W0(B)`), `q_pow_factor` (`q(B^k) = G_k·q(B)`), `cycle_iff` (both directions, `k ≥ 1`), `gcd_climb` (`gcd(q(B^k), W0(B^k)) = G_k·gcd(q(B), W0(B))`) and match them clause-by-clause against the `08dc3d5` LEDGER block AND against our verified forms (round-8 findings: the descent identity `R_0(B^k) = R_0(B)·(q_P/q_B)`, untuned, both signs; the L-A2 gcd law). Record the definition of `G_k` used in-file and check it equals the cofactor our identity produces. Check by read: 0 `sorry`, no `native_decide`, no user axioms; `experiments/ContentDescent_axioms.txt` contents. Attempt `lake build` ONLY if a toolchain + Mathlib cache is already present and completes inside ~15 minutes; otherwise record "read, not built" (established practice).

5. **Clean-room statement check, small.** Fresh script `experiments/merle_contentdescent_check.py` (imports nothing from his repos or prior checks; exact integer arithmetic): implement `W0` from our own conventions (12.6.1.1 / la5-check findings), verify the cocycle identity exhaustively on small word pairs plus random draws (both signs), verify `power_mult`/`q_pow_factor`/`gcd_climb` against 12.6.1.4's identity on a grid (this largely re-confirms round 8 — the point is that the *Lean statements as read* are the same laws; a few hundred exact checks suffice, canaries hand-computed and printed first, including one `cycle_iff` instance each direction: the trivial word and a non-cycle base).

6. **Record** (branch commits, per-item):
   - `experiments/merle_contentdescent_check.py` + committed output (one commit).
   - `briefs/merle-la5-closure-findings.md` — restatement verdict with the compared texts; the `6b9f2b1` review; the `905d75b` reconciliation (with the graph fact); ContentDescent statement-match clause-by-clause, built-or-read status; the small-check results; flags separated from confirmations.
   - `HANDOFF.md` item 1 update — repos-and-ledger facts to the new HEADs (`81431c7`, `97b57d7`, stacks `67c428a`/`905d75b`); L-A5 two keys CONFIRMED (or flagged, per verdict); the ContentDescent kernel block recorded; L-A6/L-A7 listed as seeded, checks in flight (separate briefs). Do not touch other items.

## Rules

- Branch **`merle-la5-closure`** from your worktree HEAD (verify it contains this brief, i.e. is `e71e81e` + the briefs commit or a descendant; state the base SHA in the findings). Per-item commits; do NOT merge — the main session reviews (re-runs the script) and merges.
- Read-only everywhere outside this repo: no pushes, no shared-repo or Lean-repo writes, no web actions beyond GitHub clones/reads of the two named repos. Any push impulse = stop and hand back.
- His scripts and Lean files are read, never run as verification (a build attempt per item 4 is the sole exception).
- Discrepancies recorded and flagged, never silently reconciled. If the restated gloss overreaches again, that is a finding for the reply — not something you rewrite.
- No reply paragraphs; no key turns beyond recording the verdict; no co-edit commits; stop after item 6.
