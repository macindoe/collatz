# Brief: wiki consolidation pass — status surfaces compressed to current-state (for a delegated session)

**Context required before starting (in order):** `README.md`, `AGENTS.md` (the one-fact-one-page and current-answer norms this pass enforces), `index.md`, `HANDOFF.md`, `reverse.md` front matter + Current-state callout only, `TOUR.md`, `open-problems.md`, `cycles.md` front matter + Current-state callout only.

## Provenance and principle

After a dense week (door seam, block map, itinerary language, 14.15.4–14.15.6, the 12.8.6 resolution, paper v2), the wiki's **status surfaces** have accreted narration: index.md's "Current status (one paragraph)" is now several pages; reverse.md's front-matter `status:` field is itself a paragraph; HANDOFF's "State of the fronts" is headed 2026-07-12 and its bullets carry per-delegation process history (who was delegated, which brief, review choreography) that git log and briefs/ already record permanently. The repository convention is that tracked files state the **current answer**, with history in git. This pass compresses the status surfaces back to that standard.

**The invariant: compression without loss of facts.** Every mathematical fact, status, grade, and open item currently on these surfaces must remain either (a) stated, or (b) reachable via an explicit pointer to the page/brief/log that owns it. Nothing mathematical is rephrased in substance; no section numbering changes; no page other than the five named below is touched.

## Two frozen clauses (do not alter meaning)

1. `HANDOFF.md` item 2's current facts: Merle's second reply received and verified; the pincer check merged; **the reply to him is pending (drafted, not sent)**. Compress the prose freely; do not change these facts or mark the reply sent.
2. `publication.md` is **out of scope entirely** this pass (its upload-pending status changes only when the author uploads).

## Queue, in order

1. **index.md.** Rewrite "Current status (one paragraph)" to be an actual paragraph (target: one-third of a screen): per-step theory formal (pointers), cycle front parked with the 12.8.6 record at floor grade (contiguous `{2,…,23}`, sole gap the Diophantine coverage bound), AEH formalized/calibrated/parked with §17.7 at its endpoint, mirror front's 14.14–14.15.6 arc summarized in two sentences (seam; itinerary full shift; two-sided coding with the completed three-way diagonal characterization, signed extension; Bridge unchanged throughout), papers published with v2 prepared, terminal object = the Bridge. Every dropped detail must already live on its owning page — verify each as you cut, and keep the pointer set complete (a reader must be able to reach every fact in ≤ 2 hops). Update the pages table's reverse.md and cycles.md rows if they lag.
2. **reverse.md front matter.** Compress the `status:` field to ≤ 3 lines (grades + pointers; the Current-state callout below it keeps the fuller summary — trim that callout only where it duplicates itself, not where it carries facts).
3. **cycles.md front matter.** Same treatment if warranted (it is shorter; touch only if it fails the current-answer test).
4. **HANDOFF.md "State of the fronts".** Re-head with the current date. Compress each front bullet to: current state + grade + owning pointers + what reopens it. Move the per-delegation choreography (brief names, who reviewed what, per-commit notes) out: it survives in git log and briefs/ — where a bullet loses a detail, ensure the pointer it keeps reaches that detail. Item 2's frozen facts per above; the "Open work items" list should reflect reality: (1) Merle reply pending + protocol co-draft next, (2) Zenodo v2 upload pending (author), (3) the KL–LP residual (idea-gated), (4) the wiki's own longer-horizon items unchanged.
5. **TOUR.md and open-problems.md — verify only.** Confirm TOUR's pointers all resolve post-12.8.6-resolution and post-14.15.6 (fix any that don't, minimally); confirm open-problems.md's 11.6 entry reflects 14.15.2's closure (the prior sweep claimed this — verify, fix only if false). Report findings either way.

## Rules (non-negotiable)

- Compression only: no new claims, no substantive rephrasing of mathematical statements, no renumbering, no page beyond the five named.
- Every cut fact verified reachable at its owning location before it is cut (spot-check by grep, note the method).
- Register norm: flat; the compressed text must not read as a victory lap.
- Work on branch **`wiki-consolidation`**, one commit per queue item, do NOT merge — the main session reviews (including diff-reading every removal) before merging.
- No scope expansion; off-brief findings to `briefs/wiki-consolidation-findings.md`.

## Definition of done

index.md's status genuinely one paragraph with a complete pointer set; reverse.md status ≤ 3 lines; HANDOFF current-dated, compressed, with the two frozen clauses intact; TOUR/open-problems verified; clean per-item commits on `wiki-consolidation`.
