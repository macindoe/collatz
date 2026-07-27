# Findings: round-11 Lean re-audit — the ceiling repair (`ceiling_lower` / `ceiling_pinned`, `hceil` removal)

Delegated session, 2026-07-27. Brief: `briefs/merle-r11-ceiling-audit-brief.md`.
Branch `merle-r11-ceiling-audit`, base commit **`e938040`** — the worktree was
cut from the session-start HEAD `2225b68`, which does **not** contain the
brief; it was rebranched onto `e938040` (the brief commit, current `main`)
before any work began, as the launch instruction and the brief's Rules require.

Register: flat; statements recorded verbatim; discrepancies recorded, never
disputed in prose. No key is turned. No reply paragraphs, no ledger text.
Read-only clone in the scratchpad; no pushes; no fork, issue, star, watch or
comment on any of his repositories; no Lean toolchain installed or attempted.

**Trust boundary, stated plainly.** This is a **read-not-built** statement-match
audit, the precedent being `experiments/merle_lean_r10_audit.py`. What is
verified here: (1) the Lean *statements* say what the letter and the L-A8
ledger block say they say; (2) the *dependency structure* is what he describes
— specifically that `hceil` is gone from the four downstream signatures and is
re-derived internally from `ceiling_lower`, checked against every mechanism by
which a hypothesis can vanish from a printed signature and still be threaded;
(3) the committed axiom logs match the claimed axiom sets, and the 13 → 15
reconciliation is exact; (4) every statement, instantiated at exact-integer
points including edges and the real cycles, is *true as stated*. What is NOT
verified here: that the proofs compile and the kernel accepts them. The
kernel-3 / `[propext]` / no-axiom claims rest on his committed logs and his
four-way-hardened protocol — the same posture as the ContentDescent, L-A1 and
round-10 precedents.

**Stopping-rule compliance:** verification of a correspondent's artifacts; no
new computational front; the cycles front stays PARKED (the synthetic sweeps
are element multisets and `(n, K)` pairs, not orbit or period searches).

## Item 1 — the clone, the graph, the drift check

Fresh unauthenticated read-only clone (2026-07-27) of
`github.com/ericmerle3789/one-obstruction-three-faces-lean` into the scratchpad.

**HEAD = `c991430297b1e6e3e88f1c09c5f3c20b7dd6220b` (`c991430`)** — exactly the
expected pin, with `6c084c5` beneath it. **The graph `5c9b663 → HEAD` is
linear**: each commit has exactly one parent (`c991430`'s parent is `6c084c5`;
`6c084c5`'s parent is `5c9b663`), two commits, no merges, both authored
`Eric MERLE`, 2026-07-26 CEST (17:39:14 and 20:30:40 +0200).

| commit | date | what it changed |
|---|---|---|
| **`6c084c5`** | 2026-07-26 17:39 | "Round-10 repairs, all found by Macindoe's audit and confirmed here before fixing." 13 files, +376/−122. `T1Structure.lean`: adds `ceiling_lower`, `ceiling_pinned`, their canary and their two `#print axioms` probes; removes `hceil` from four signatures. `DeficitLemma.lean`: SCOPE header corrected in place, probes added for `key_shifted`/`key15`. Both axiom logs regenerated. `OUT_REQ-MATH-052/053`: crashed-run tracebacks removed, the δ factor-2 corrected in the P3 table, the indexing convention pinned to standard, the "exhaustive to `q₁₀ = 190537`" label corrected to `n < q₁₃ = 190537` and the sweep actually extended to `j = 12`. `OUT_REQ-MATH-043/055/056` gain reproduction verdicts; `OUT-056` gains the multiples clause. Three previously scriptless outputs gain their generator scripts (`test_REQ-MATH-043`, `-055`, `-056`). |
| **`c991430`** | 2026-07-26 20:30 | "Restore the permanent RETRACTED record for da2c8db, per Macindoe's round-10 flat note." `T1Structure.lean` only, +24/−0: the standalone RETRACTED block. |

**Drift check — NO DRIFT.** `git diff` against the previously audited SHAs is
empty for all four files:

- `ContentDescent.lean` — unchanged since `67c428a`.
- `ContentSeparation.lean` — unchanged since `905d75b`.
- `TransportRecurrence.lean` — unchanged since `7d3d44a`.
- **`LegendreApprox.lean` — unchanged since `da2c8db`, and byte-identical
  between `5c9b663` and HEAD.** (Recorded explicitly because it bears on the
  sibling session `junction-public-recon`: the file's *home* is still not
  confirmed, but the file itself has not moved.)

`README.md` and `experiments/README.md` are also unchanged.

**One incidental observation, flat.** The three `exponentiation.threshold`
warning lines that `DeficitLemma_axioms.txt` carried at `5c9b663` — which
embedded his local working path
`/Users/ericmerle/Documents/Collatz-Racine-Mur-2026-07-16/lean/DeficitLemma.lean`
— are removed at HEAD along with the log headers (item 6). Recorded because
the round-10 record cites that path; it is no longer in the tree.
