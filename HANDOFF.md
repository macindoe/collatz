# Handoff

This document lets any capable model (or a future session of any model) continue the project without loss. It is a working document: it carries the current state only; how the state got here is the git log and the `briefs/` record.

## Onboarding order for a new assistant

1. `README.md` — what this project is, the strategy, and the **binding stopping rules**.
2. `AGENTS.md` — the schema and verification protocol. Non-negotiable: nothing is labeled proved without independently written verification code; failures are recorded, not deleted; sources/ is immutable.
3. `index.md` — the resolver; then whichever pages the task touches.
4. This file — current state and open items.

**Register norm (author's explicit preference):** flat, calibrated prose. No excitement inflation — it degrades judgment and invites hallucination. Heuristics are labeled heuristics. Claims pass through verification before they pass into prose.

**The author's role:** Ben directs. Empirically, the project's load-bearing ideas — the coordinate system itself, the family diagram, the mirror front, the ladder, the dead-ends map — originated as his plain-language questions. Take his naive-sounding questions seriously and work them before defaulting to queued engineering.

## State of the fronts (as of 2026-08-12)

- **Forward per-step theory** — closed per step → spine.md §9, stage1.md–stage4.md; terminal open object consolidated as the Bridge → bridge.md §16.
- **Cycles** — PARKED → cycles.md §12 (periods 1–3 closed; uniform trim resolved; staircase sharpness **proved at every period**, 12.8.6 — unconditional for `p ≥ 16`, finite check for `3 ≤ p ≤ 15`, `p ∈ {2,4}` by exhibition; the divisibility system one rotation-invariant condition, 12.6.1.1; the spent `|q| = 1` stock identified as the rational-anchor instance of the digit-match ceiling, 12.6.1.3). Reopens only with a divisibility-aware (anchor-rigidity) idea, per the stopping rules. The all-`p` staircase arc's record is its seven findings files in `briefs/` (`staircase-allp-construction`, `staircase-allp-diophantine`, `staircase-status-audit`, `record-defects-repair`, `staircase-gamma-upper`, `staircase-status-apply`, `record-consistency-sweep`); the consolidated state is 12.8.6 itself.
- **Statistics / AEH** — formalized, calibrated clean; proof effort parked → aeh.md §13; the single-sequence structural axis is at its endpoint → anchor-digit-search.md §17.7; the symbolic form is now a named, proved equivalence (the genericity form, aeh.md 13.6), with the depth marginal exactified (13.6.5).
- **Reverse / mirror** — ACTIVE → reverse.md §14.1–14.14 (duality 14.1–14.12; door/exit seam 14.14; KL–LP closed on a structural obstruction, 14.13/14.6.5); the itinerary language → itinerary.md §14.15 (whole-period height laws 14.15.9; the door-word ↔ near-miss-anchor dictionary 14.15.10).
- **Ladder** — closed as local law → ladder.md §15; at the valuation level identified as the third face of stage3's target-shift mechanism (15.5).
- **Papers** — both published → publication.md (paper 1 at **v3**, DOI 10.5281/zenodo.21730505, published 2026-08-03 — a full revision after external review, 15 pages, repair history at `paper/collatz-reduced-version-history.md`; v1 DOI 10.5281/zenodo.21273548, v2 DOI 10.5281/zenodo.21421120; mirror paper DOI 10.5281/zenodo.21303918).

## Open work items, in priority order

1. **Eric Merle collaboration — current state.**

   **Live conditions.** **PR #1 is OPEN** — `github.com/macindoe/one-obstruction-three-faces/pull/1`, the round-12 package: the L-A9 split-grade key turn conditional on offer h1 with offers h1–h5, the regime column into `PROTOCOL.md`, the two L-A8 corrections accepted as ours, and the `cycles.md` 12.8.6.1 rotation block under both names. **His approving review is the round's second key.** **PR #2 is OPEN** — `pull/2`, the joint note's first draft (`NOTE-v1.md`, sent 2026-08-03, four days inside the letter's this-week promise); his review is the note's second key; subtitle, Gersonides porch, file name and credit language open to his edit. The **`[GRADE AT SIGNING…]` bracket must not survive into the merged, signed note** — it resolves when the Macindoe L-A9 key actually turns (PR #1's review) — and the **L-A9 grade line restates per whatever h1 becomes**. **Round 13 runs under the new medium** (accepted §13, below). The **Zenodo metadata line on the frozen Version-note clause is deliberately unaddressed** — the author's decision, 2026-08-03; the version-history file carries the defect; if Merle asks, the answer is the changed decision stated plainly. **ccchallenge's `Macindoe2026` entry points at v1** — noted flat; canonical citation = the v3 DOI.

   **Standing conventions.** Sending and acknowledgements stay with the author. The author pastes Merle's replies verbatim (Gmail retrieval garbles numerals; see quirks below). Two-key/three-repo protocol: claims are verified on both sides before they pass into prose or the shared ledger. Under the accepted §13 medium the technical half moves in PRs — one round per PR, the second key = the approving review; mail keeps everything that is not a claim. Personal background, on record from his round-10 letter: he is a lycée electricity teacher, no doctorate, a year in — personal paragraphs are always the author's to answer.

   **Repos, current values.** Shared repo `github.com/macindoe/one-obstruction-three-faces` — **public** (flipped by the author himself, 2026-07-24). HEAD **`7c05458`**, with PR #1 branch `round-12` pushed at `accda4b` (tree `8e9b1eb`) and PR #2 branch `note-v1-draft` pushed at `96ccadf` (tree `d374546`). Contents: `PROTOCOL.md` (§7 acceptance recorded in-file), `LEDGER.md`, `NOTE.md`. His handle `ericmerle3789`; his Lean repo `ericmerle3789/one-obstruction-three-faces-lean`, HEAD **`d48ba9e`**, with his round-12 technical body `rounds/R11-merle.md`.

   **Ledger state.**
   - L1 — corrected, both directions.
   - L2 — two keys.
   - L3 — corrected by him 2026-07-24; accepted into the two-key record at `c40aa58`.
   - L4 — AEH replication; our key turned.
   - L-A1 — transport recurrence; two keys plus kernel. Credit: independent simultaneous discovery, both names.
   - L-A2 — repeated-word gcd law; two keys (`ec4f229`).
   - L-A3 — anchored-loops/spent-stock/Benford; two keys, with the (B) margin-quantification additions, the conditional date-stamped.
   - L-A4 — descent; two keys, plus the ContentDescent kernel key on the structured half (`08dc3d5`/`67c428a`).
   - L-A5 — adelic content invariant; two keys via `49351e5`, closure-verified.
   - L-A6 — calibrated lottery; two keys, scoped; pushed `641a530`.
   - L-A7 — torsion ruler; two keys — the Rhin 1987 / Simons–de Weger 2005 re-sourcing accepted, headline `n ≈ 2233`; the margin inequality now proved on both sides, ours at the true `c_gen` with uniform surplus `1 + log₂β`.
   - L-A8 — T1/no-hair; two keys on the mathematics, kernel claims scoped to the read-not-built audits, the ceiling repair verified; entry in his own proposed wording via `1d7907c`.
   - L-A9 — δ8 impossibility; seeded one key (his) at `78f80f0`; our turn prepared split-grade, conditional on offer h1, carried in PR #1.

   **Standing decisions.** L-A1 credit: independent simultaneous discovery, both names. Hosting on collatz-lab.org: approved, DOI-pinned to v2 (10.5281/zenodo.21421120), the mirror-paper pair offered. Venue for the joint note: number-theory-shaped, with the formalization as supporting artifact. Citation posture: Gersonides 1342/43, not Mihailescu. Gateway visualization: each side builds its own cycle-side gateway and cross-links — ours is `viz/cycle_anchor_gateway.html`. His credit-deflection preference is on file with no record change (Remark 12.6.1.2 already reads packaging his / verification joint); the note's credit language at drafting time is the author's call.

   The hosting pin (v2) and the round-12 canonical-citation guidance (v3) are different objects and coexist; whether the hosting pin moves to v3 is the author's open decision.

   **The paper at v3.** Published 2026-08-03, DOI 10.5281/zenodo.21730505 — a full revision, not the erratum round 12 prepared: a six-round external-review arc rebuilt the paper (94 commits; record in `briefs/v3r*` and `paper/collatz-reduced-version-history.md`, not here). v2 is archived to `sources/paper/`. The Zenodo file is hash-identical to `paper/collatz-reduced-v3.pdf`. One recorded defect (ours): the published PDF's Version note still carries its drafting-time "not yet published" self-description, frozen into the immutable file — recorded in the version-history file. The paper's Status paragraph pins `cycles.md` at `9d9d1ec` and Appendix A at `6285485`, both resolving on public `main`. Citation guidance: v3 for the dichotomy phrases and the Theorem 4.6 obstruction sentence; v2 for the contiguous `p ∈ {2,…,23}` evidence note.

   **The author's round-12 decisions (2026-07-30).** (1) The cost answer is his to write — and it noted the spend-limit symmetry: the L-A9 delegate was cut off once by the monthly spend limit mid-run — Merle's own failure mode exactly — and resumed cleanly. (2) §13 accepted — the PR medium above. (3) Smallest-object accepted in principle; the pen taken (the note promised in PR #1, delivered as PR #2). (4) Erratum before the reply — discharged by v3. (5) The regime-column protocol accepted — carried in PR #1.

   **Pointers.** The Merle credit language (verbatim preservation everywhere): cycles.md 12.6.1.1 / 12.6.1.2 / 12.6.1.4 / 12.8.6.1 (rotation reformulation, both names) / 12.8.6.4 (pincer credit); aeh.md §13.4's external-replication line. Also itinerary.md 14.15.9(a); `experiments/transport_recurrence_vectors.json`. The `briefs/merle-*` and `briefs/jointnote-*` files are the round-by-round record.

2. **KL–LP residual** (low priority; CLOSED front, see State of the fronts). One well-defined sub-question survives in 14.13: whether a *size-threshold-coupled* version of the `(j,r)` DAG (coupling precision-loss to the renewal induction's accumulated-offset variable, rather than crediting exhaustion for free) recovers real gains from residues. Reopens only with an idea for that coupling, not with more computation.

3. **The wiki's own longer-horizon items.** The anchor-pinning framing thread (README's 2023 seed question) has run its course through the door/exit seam, block-map layer, and itinerary language: the Bridge's remaining content is exactly the stratum word at unbounded length, proved free at every finite level (full shift, itinerary.md 14.15.2), with a symbolic name (the diagonal compatibility locus, 14.15.3(c)) — paused until a further step can engage the word at unbounded length directly, which is the Bridge itself. The equidistribution question (AEH, aeh.md §13) stays long-range per the stopping rules: proof effort waits on an idea. Community outreach (r/Collatz, ccchallenge) is de-prioritized, not a standing item; a substantive response would be verified against the wiki and answered with one reply, no questions.

## The delegation pattern (proven)

One full case study exists: `briefs/mirror-queue-brief.md` → Sonnet session → branch `mirror-queue` → four theorems with per-commit discipline → independent re-verification in review (~50k checks re-run) → merge. The pattern: (i) written brief forcing AGENTS.md compliance and branch discipline; (ii) explicit "record obstructions, don't force analogies" instruction; (iii) reviewer re-runs all verification code before merging. Use it for the delegatable items above (Merle follow-up, KL–LP, the long-horizon items) — not author-only publication steps.

## Known infrastructure quirks

- The sandbox mount of the repo can serve stale reads mid-session (files appear truncated). The Windows-side files are authoritative; verify via PowerShell (`git status`, line counts) before "repairing" anything.
- **Never edit a tracked file with PowerShell 5.1 `Get-Content`/`Set-Content`.** `Get-Content` decodes UTF-8 as ANSI and `Set-Content -Encoding utf8` re-encodes the result as UTF-8, double-encoding every non-ASCII character and adding a BOM. These pages are full of `—`, `≤`, `⌈⌉`, `ε`, `β`, so the damage is total and silent — it survives commits, rebases and merges, and `git diff --stat` shows only the lines you meant to touch. Observed 2026-07-26 resolving a rebase conflict in `HANDOFF.md`: 125 mangled sequences, repaired by restoring the file from the last clean commit (`0378ee4`) and re-applying the wanted change from its own uncorrupted commit rather than attempting byte surgery. Use the Edit/Write tools for file content; if PowerShell is unavoidable, use `[System.IO.File]::ReadAllText/WriteAllLines` with an explicit `UTF8Encoding($false)`. **Check with `experiments/encoding_scan.py`** (run it over the tracked tree before committing anything PowerShell has touched): it reports files that are not valid UTF-8, files carrying a BOM, and files containing the double-encoding signatures of the characters these pages actually use. The same script found and fixed two older instances of the *inverse* fault — `merle_la6_check_output.txt` had been written in cp1252 (a `0x97` em-dash byte, from a round-9 delegate session) and five committed script outputs carried BOMs from PowerShell `>` redirection, which is what caused the "output identical modulo a BOM" friction at earlier reviews. Do not paste a literal mojibake sample into any tracked file — it makes the file itself a permanent false positive.
- The Gmail retrieval pipeline can silently garble numerals in correspondence (observed 2026-07-17: several two-digit groups rendered as single glyphs in a Merle email that displayed cleanly in the author's own client; a reconstructed guess then produced a spurious "disagreement," dissolved once the author read the true value — `briefs/merle-pincer-check-findings.md`, Correction). Before verifying or disputing any number quoted from email, have the author confirm the digits from his own client.
- LaTeX builds: the mount locks aux files; build in a sandbox temp dir and copy artifacts in.
- `\wp` and `\dp` are TeX primitives; the papers use `\wnext`, `\dnext`.
