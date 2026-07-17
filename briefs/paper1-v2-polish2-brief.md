# Brief: paper 1 v2, final wording round — two verified external-review edits (for a delegated session)

**Context required before starting:** `paper/collatz-reduced-v2.tex` and `paper/collatz-reduced-v2-review.md` on main, `briefs/paper1-v2-p22-brief.md` (its constraints all still bind), `cycles.md` 12.8.6 (Resolution paragraph — the wording model for edit 1).

## Provenance

Third external review pass (ChatGPT, 2026-07-17), verdict "ready after two very small edits." Both verified by the main session against main before delegation:

1. **The note says "the same recipe resolves it" at candidates outside the chain** — mildly self-contradictory, since the note defines "the recipe" as three stages *including* semiconvergent candidate selection, which is exactly the stage that failed. cycles.md's own Resolution paragraph phrases it correctly ("Construction 12.8.6.2 plus Algorithm 12.8.6.3 resolve…"). Verified present in the tex.
2. **The review bundle reintroduced the rejected declaration** "No mathematical claim in the paper changes strength anywhere in this diff" (line ~18) — a regression against the formulation agreed in the first revision round. Verified present in the bundle.

## Queue (branch `paper1-v2-polish2` from main)

1. **One tex edit (one commit):** in the "Note added in v2", replace `the same recipe resolves it ($13$ and $8$ correction moves), closing the range above` with `the same profile-and-correction procedure resolves it ($13$ and $8$ correction moves), closing the range above`. Nothing else in the tex changes; the `thm:staircase` environment stays byte-identical to v1 (re-checked at review).
2. **Rebuild the PDF (one commit):** same temp-dir procedure and known toolchain signature; confirm page count and probe the changed phrase in extracted text.
3. **Bundle fix (one commit):** replace the regressed declaration sentence-pair with the agreed formulation, extended per the reviewer's suggestion: `No theorem or universal claim is strengthened; v2 adds and updates a finite computational evidence record.` Regenerate the bundle's v1→v2 diff (it changes by one word) and re-run the fidelity transcript (hedge byte-identity; numbers verbatim in cycles.md §12.8.6; the five register greps; add one: "the same recipe resolves" → 0 occurrences).

## Rules

All prior rounds' constraints bind: no new content, register norms, sources/paper 2/wiki untouched, no push, no merge — the main session reviews. Off-brief findings to `briefs/paper1-v2-findings.md`.

## Definition of done

The one-word-scale tex edit; rebuilt PDF; bundle with the agreed declaration and refreshed diff/transcript; clean commits on `paper1-v2-polish2`.
