# Brief: gateway footer cross-link (for a delegated session)

**Context required before starting (in order):** `HANDOFF.md` item 1 (round-7 state), `briefs/merle-round7-check-findings.md` item 1 (the verified sibling-page facts — on branch `merle-round7-check` if not yet merged to main), `viz/cycle_anchor_gateway.html` (footer, lines ~169–172 — the edit target).

## Provenance

Round-7: Eric Merle's sibling gateway page is live and verified (2026-07-23) — `https://collatz-lab.org/cycles/`, "Collatz cycles: two towers, four harbours", bilingual FR/EN, back-linking our gateway at `https://macindoe.github.io/collatz/viz/cycle_anchor_gateway.html` (verified resolving) and citing the v2 and mirror DOIs digit-exact. The footer slot in our gateway has carried a TODO placeholder since round 6; this brief fills it.

## Queue

1. **Fill the footer slot** (one commit). In `viz/cycle_anchor_gateway.html`, replace the placeholder line — the `href="#"` anchor with the TODO title and the `TODO` badge — with the live link:
   - `href="https://collatz-lab.org/cycles/"` (the real URL; no Gmail wrapper, no trailing garbage).
   - Anchor/label sense, in the page's existing footer voice: Eric Merle's cycle-side narrator page, *"Two towers, four harbours"* (collatz-lab.org) — his letter's own framing is operate ↔ narrate, each side pointing at the other; one clause of that sense may carry into the line, flat register, no praise.
   - Remove the TODO badge and the "placeholder, link to follow" text entirely. Keep the surrounding footer structure, styles, and the "the two pages cross-link" sense (now true — state it as fact, not future).
   - Nothing else on the page changes.

## Rules

- Branch **`gateway-footer`**, one commit, do NOT merge and do NOT push — the main session reviews, merges, and pushes (the push is what makes the cross-link live on GitHub Pages).
- Do not edit `HANDOFF.md` (the round-7 branch owns that file this session; the owed-item tick happens at merge).
- No other files; no scope expansion; stop after item 1.
