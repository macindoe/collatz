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

   **Repos and ledger facts.** Shared repo `github.com/macindoe/one-obstruction-three-faces` — **public** (flipped by the author himself, 2026-07-24; historical flag on record in `briefs/merle-round7-check-findings.md`, addendum). **HEAD `b8842bb`** (Merle, 2026-07-24; verified by unauthenticated clone, `briefs/merle-round8-check-findings.md`). Contents: `PROTOCOL.md` (§7 acceptance recorded in-file), `LEDGER.md`, `NOTE.md` (his architecture skeleton — eight sections, every claim entering via a turned ledger entry; **§4 and §6 rewritten by him 2026-07-24** to the no-Hasse-gap/local-obstruction and equidistribution framing, our pin `430c00c` and "positive odd integer" precision `d2407b9` both preserved in his rewrite). His handle `ericmerle3789`; his Lean repo `ericmerle3789/one-obstruction-three-faces-lean` (kernel-verified L-A1 artifact; **scripts stack now `017288f`** — five scripts REQ-MATH-013..017 with outputs: stratum-rigidity negative, capacity-demand margin, Weyl/structure, size-artifact + descent, mod-7 local obstruction). Ledger entries: L1–L2 as before; **L3 — corrected by him 2026-07-24** (the session-2 "purely global" reading retracted: a linear divisibility has no Hasse gap, the p = 7 instance fails already in ℤ₇ with `v_7(q) = 3 > v_7(R_r) = 1` — verified independently our side; the correction is pure-additive, the original two-key data untouched, diff-verified); L4 — AEH replication, our key turned; L-A1 — transport recurrence, both keys plus kernel; L-A2 — repeated-word gcd law, **two keys** (`ec4f229`); L-A3 — anchored-loops/spent-stock/Benford, **two keys**, plus his round-8 "Additions accepted": (A) our signed characterization (Thm 14.15.6.7) as the two-shore frame, (B) the digit-match-ceiling identification (cycles.md 12.6.1.3) with his margin quantification ≈ 0.27·n stratum / 0.08·n general (REQ-MATH-014; replicated digit-exact our side; the entry states values without the operational definition — co-edit item); **L-A4 — new, seeded one-key (Merle)**: descent/no-new-cycle-in-structured-families, `q_P | R_0(P) ⟺ q_B | R_0(B)`, his 3,600/3,600 — clean-room re-derived and verified our side (12,888 checks, 0 failures; the identity `R_0(B^k) = R_0(B)·(q_P/q_B)` holds untuned, both signs — scope note in the findings).

   **Standing decisions.** L-A1 credit: independent simultaneous discovery, both names. Hosting on collatz-lab.org: approved, DOI-pinned to v2 (10.5281/zenodo.21421120), the mirror-paper pair offered. Venue for the joint note: number-theory-shaped, with the formalization as supporting artifact. Citation posture: Gersonides 1342/43, not Mihailescu. Gateway visualization: each side builds its own cycle-side gateway and cross-links — ours is `viz/cycle_anchor_gateway.html`. His credit-deflection preference is on file with no record change (Remark 12.6.1.2 already reads packaging his / verification joint); the note's credit language at drafting time is the author's call.

   **Pending.** Round 8 received (pasted verbatim, 2026-07-24). Round 7 is closed by his opening (round-7 reply received; the cross-link and the visibility record both accepted). Round-8 verification complete: every letter claim **confirmed** or **consistent-at-reduced-scale**, zero digit/hash/text discrepancies (`briefs/merle-round8-check-findings.md`; `experiments/merle_round8_check.py` + committed output, 12,888 checks, 0 failures — L-A4 clean-room derivation written out in the findings as the co-edit substance; L3's p = 7 local obstruction verified exactly; margin replicated digit-exact). Owed our side: (a) **L-A4 co-edit + our key turn in the shared LEDGER** — separate delegate; co-edit materials ready in the findings (the untuned-scope widening, the identity form, the margin-definition pin for L-A3, and the optional signed-frame sentence for NOTE §4, all his call); **push only on the author's explicit go-ahead**; (b) **our key on the corrected L3** — same gate; (c) reply — drafted after (a)–(b) settle; sending stays with the author.

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
