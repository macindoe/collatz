# Handoff

This document lets any capable model (or a future session of any model) continue the project without loss. It is a working document: it carries the current state only; how the state got here is the git log and the `briefs/` record.

## Onboarding order for a new assistant

1. `README.md` — what this project is, the strategy, and the **binding stopping rules**.
2. `AGENTS.md` — the schema and verification protocol. Non-negotiable: nothing is labeled proved without independently written verification code; failures are recorded, not deleted; sources/ is immutable.
3. `index.md` — the resolver; then whichever pages the task touches.
4. This file — current state and open items.

**Register norm (author's explicit preference):** flat, calibrated prose. No excitement inflation — it degrades judgment and invites hallucination. Heuristics are labeled heuristics. Claims pass through verification before they pass into prose.

**The author's role:** Ben directs. Empirically, the project's load-bearing ideas — the coordinate system itself, the family diagram, the mirror front, the ladder, the dead-ends map — originated as his plain-language questions. Take his naive-sounding questions seriously and work them before defaulting to queued engineering.

## State of the fronts

- **Forward per-step theory** — closed per step → spine.md §9, stage1.md–stage4.md; terminal open object consolidated as the Bridge → bridge.md §16.
- **Cycles** — PARKED → cycles.md §12 (periods 1–3 closed; uniform trim resolved; staircase sharpness at floor grade, contiguous `p ∈ {2,...,23}`; the divisibility system one rotation-invariant condition, 12.6.1.1; the spent `|q| = 1` stock identified as the rational-anchor instance of the digit-match ceiling, 12.6.1.3). Reopens only with a divisibility-aware (anchor-rigidity) idea, per the stopping rules.
- **Statistics / AEH** — formalized, calibrated clean; proof effort parked → aeh.md §13; the single-sequence structural axis is at its endpoint → anchor-digit-search.md §17.7; the symbolic form is now a named, proved equivalence (the genericity form, aeh.md 13.6), with the depth marginal exactified (13.6.5).
- **Reverse / mirror** — ACTIVE → reverse.md §14.1–14.14 (duality 14.1–14.12; door/exit seam 14.14; KL–LP closed on a structural obstruction, 14.13/14.6.5); the itinerary language → itinerary.md §14.15 (whole-period height laws 14.15.9; the door-word ↔ near-miss-anchor dictionary 14.15.10).
- **Ladder** — closed as local law → ladder.md §15; at the valuation level identified as the third face of stage3's target-shift mechanism (15.5).
- **Papers** — both published → publication.md (paper 1 DOI 10.5281/zenodo.21273548, v2 DOI 10.5281/zenodo.21421120; mirror paper DOI 10.5281/zenodo.21303918).

## Open work items, in priority order

1. **Eric Merle collaboration — current state.**

   **Standing conventions.** Sending and acknowledgements stay with the author. The author pastes Merle's replies verbatim (Gmail retrieval garbles numerals; see quirks below). Two-key/three-repo protocol: claims are verified on both sides before they pass into prose or the shared ledger.

   **Repos and ledger facts.** Shared repo `github.com/macindoe/one-obstruction-three-faces` — **public** (flipped by the author himself, 2026-07-24; historical flag on record: not public at the 2026-07-23 check, his letter's "public per §7" having recorded the accepted in-file state, which only the owner could execute — adjudication and unauthenticated verification in `briefs/merle-round7-check-findings.md`, addendum; shared-repo HEAD at verification `61d2cf3`). Contents: `PROTOCOL.md` (§7 provides for the flip, acceptance recorded in-file), `LEDGER.md`, `NOTE.md` (his architecture skeleton, 2026-07-19 — eight sections, every claim entering via a turned ledger entry; the realization-height reference deliberately unpinned, "pin on co-edit"). His handle `ericmerle3789`; his Lean repo `ericmerle3789/one-obstruction-three-faces-lean` (Lean 4 / Mathlib v4.27.0, kernel-verified L-A1 artifact with an honest scope header). Ledger entries: L1–L3 — the seed entries (L1 recorded "corrected, both directions"); L4 — his AEH class-skeleton replication, our key turned (aeh.md 13.4); L-A1 — the transport recurrence (cycles.md 12.6.1.1), both keys plus the kernel; L-A2 — the repeated-word gcd law (his proposal), **two keys**: his clean-room re-derivation verified against the entry, 2,400/2,400 checks each clause, artifact `ec4f229`; L-A3 — the anchored-loops/spent-stock/Benford entry, **co-edited, two keys**, coherent with cycles.md 12.6.1.2/12.6.1.3, his one precision pinning the adjudicated artifact `3b547c4`.

   **Standing decisions.** L-A1 credit: independent simultaneous discovery, both names. Hosting on collatz-lab.org: approved, DOI-pinned to v2 (10.5281/zenodo.21421120), the mirror-paper pair offered. Venue for the joint note: number-theory-shaped, with the formalization as supporting artifact. Citation posture: Gersonides 1342/43, not Mihailescu. Gateway visualization: each side builds its own cycle-side gateway and cross-links — ours is `viz/cycle_anchor_gateway.html`. His credit-deflection preference is on file with no record change (Remark 12.6.1.2 already reads packaging his / verification joint); the note's credit language at drafting time is the author's call.

   **Pending.** Round 7 received (pasted verbatim, 2026-07-23; closural register). Both round-6 waits landed: the sibling-page link — `https://collatz-lab.org/cycles/` ("Two towers, four harbours") live, back-linking `https://macindoe.github.io/collatz/viz/cycle_anchor_gateway.html` (verified resolving to our gateway), v2 and mirror DOIs digit-exact — and his LEDGER.md edits, verified 2026-07-24 by unauthenticated clone after the author's own public flip (L-A2 two keys, L-A3 co-edited; PROTOCOL.md §7 and NOTE.md also verified; `briefs/merle-round7-check-findings.md`, addendum). Owed our side: (a) ~~footer cross-link~~ **done** — merged and pushed (main merge `2f24b56`, gateway commit `002c189`); (b) ~~NOTE.md pin~~ **done** — pushed to the shared repo 2026-07-24 on the author's explicit A+B go-ahead (pin commit `430c00c` → target **itinerary.md 14.15.5(b), Corollary 14.15.5.4**, the combined characterization, 14.15.5(c) for its wrong-sign clause — the earlier 14.15.9(c) call is revised in the findings; plus the separable one-word "odd" precision `d2407b9`, now the shared repo's HEAD); (c) reply — draft on file at `briefs/merle-round7-reply-draft.md` (merged `4eb28d7`; citations reviewed against itinerary.md 14.15.5–14.15.6), sending stays with the author. Nothing else owed either side once the reply goes out.

   **Pointers.** cycles.md 12.6.1.1/12.6.1.2; aeh.md §13.4 (external-replication line); itinerary.md 14.15.9(a); `experiments/transport_recurrence_vectors.json`; the `briefs/merle-*` files are the round-by-round record.

2. **KL–LP residual** (low priority; CLOSED front, see State of the fronts). One well-defined sub-question survives in 14.13: whether a *size-threshold-coupled* version of the `(j,r)` DAG (coupling precision-loss to the renewal induction's accumulated-offset variable, rather than crediting exhaustion for free) recovers real gains from residues. Reopens only with an idea for that coupling, not with more computation.

3. **The wiki's own longer-horizon items.** The anchor-pinning framing thread (README's 2023 seed question) has run its course through the door/exit seam, block-map layer, and itinerary language: the Bridge's remaining content is exactly the stratum word at unbounded length, proved free at every finite level (full shift, itinerary.md 14.15.2), with a symbolic name (the diagonal compatibility locus, 14.15.3(c)) — paused until a further step can engage the word at unbounded length directly, which is the Bridge itself. The equidistribution question (AEH, aeh.md §13) stays long-range per the stopping rules: proof effort waits on an idea. Community outreach (r/Collatz, ccchallenge) is de-prioritized, not a standing item; a substantive response would be verified against the wiki and answered with one reply, no questions.

## The delegation pattern (proven)

One full case study exists: `briefs/mirror-queue-brief.md` → Sonnet session → branch `mirror-queue` → four theorems with per-commit discipline → independent re-verification in review (~50k checks re-run) → merge. The pattern: (i) written brief forcing AGENTS.md compliance and branch discipline; (ii) explicit "record obstructions, don't force analogies" instruction; (iii) reviewer re-runs all verification code before merging. Use it for the delegatable items above (Merle follow-up, KL–LP, the long-horizon items) — not author-only publication steps.

## Known infrastructure quirks

- The sandbox mount of the repo can serve stale reads mid-session (files appear truncated). The Windows-side files are authoritative; verify via PowerShell (`git status`, line counts) before "repairing" anything.
- The Gmail retrieval pipeline can silently garble numerals in correspondence (observed 2026-07-17: several two-digit groups rendered as single glyphs in a Merle email that displayed cleanly in the author's own client; a reconstructed guess then produced a spurious "disagreement," dissolved once the author read the true value — `briefs/merle-pincer-check-findings.md`, Correction). Before verifying or disputing any number quoted from email, have the author confirm the digits from his own client.
- LaTeX builds: the mount locks aux files; build in a sandbox temp dir and copy artifacts in.
- `\wp` and `\dp` are TeX primitives; the papers use `\wnext`, `\dnext`.
