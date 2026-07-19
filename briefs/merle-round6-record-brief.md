# Brief: round-6 record + viz motivation captions (for a delegated session)

**Context required before starting (in order):** `HANDOFF.md` item 1 (through the round-5 shipped state), `briefs/merle-round5-check-findings.md` (frame paragraph + item 1), `cycles.md` 12.5–12.6.1.2 (the cycle equation frame), `viz/cycle_anchor_gateway.html` (intro paragraph, panel 1, panel 6 — the edit targets).

## Provenance

Eric Merle's sixth reply (pasted verbatim by the author, 2026-07-19). Largely closural — every round-5 item adopted. Transcription note for the record: the letter contains a Gmail redirect wrapper (`google.com/url?q=http://collatz-lab.org...`) around his site URL — a copy artifact, not content; the site is `collatz-lab.org`.

**Verified by the main session (2026-07-19, read-only GitHub API):** his commit `3b547c4` (`ericmerle3789/one-obstruction-three-faces-lean`, dated 2026-07-18T15:55:58Z; the thread-date/clock skew previously recorded stands, git order authoritative) touches only `experiments/test_REQ-MATH-011_pourquoi_le_signe.py`, +12/−10, message confirming: the multiplicative-vs-additive adjudication folded in, the `k ≥ 2` caveat with the `k = 1` sole tie, Gersonides 1343 with Mihailescu/Catalan not needed, and the act-C header comment fixed — exactly what his letter claims. Also confirmed by the main session: `main` was pushed to `origin` before the round-5 send, so the viz sentence in our letter was true when he read it.

## Queue

1. **HANDOFF item 1 — round-6 record** (one commit): sixth reply received (pasted verbatim; closural register). Adopted on his side: Gersonides posture ("Catalan retired to a footnote at most"), the anchor-correspondence references as the note's provenance, the Benford brick stated "with those neighbors named, and not one inch more," L-A2 and L-A3 both accepted (he edits from `ff379c4`), the sibling gateway to be built in his own voice for collatz-lab.org "in a few days" with his link dropped into our footer slot. His self-catch adjudication folded into his artifact and the stale header fixed — commit `3b547c4`, verified as above. **Credit deflection, recorded with no record change:** he takes the spent-stock credit "in the spirit it's given and no further," would rather the record read the packaging as "a small joint"; he requested no edit and none is made — Remark 12.6.1.2 already reads "packaging his, verification joint"; the note's credit language at drafting time is the author's call, with this preference on file. **State:** nothing owed from our side this round; pending his end — his LEDGER.md edits (verify at next touch) and his sibling-page link (then: fill the footer cross-link slot, push, done). Sending/acks stay with the author.

2. **Viz motivation captions** (one commit) — the author's review feedback: the page never says *why* near-misses of the two towers matter. Two additions, register flat and lay-readable, sense transcribed from cycles.md 12.5–12.6 / the findings' frame paragraph, no new claims:
   - **Intro or top of panel 1 (your placement call, 2–4 sentences):** the missing bridge. Sense to convey: a loop that returns after `k` steps has multiplied by 3-and-a-bit `k` times and halved `m` times; closing exactly forces the balance `x · q = R`, where `q = 2^m − 3^k` and `R` is an integer the step pattern determines. The towers never meet exactly (`q = 0` is impossible), so an exact collision is ruled out and no "perfect" loop exists; instead every loop must ride a *near-miss* — and must win the divisibility `q | R`. At `|q| = 1` that win is free (1 divides everything); otherwise it is a lottery. That is why the ladder is the page's first picture.
   - **Panel 6, one clause on the strip's intent:** the `k ≤ 10` exhaustion is a verification exhibit — the story confirmed completely for every `k ≤ 10` — not a proof method; `k` has no ceiling, and the unbounded statement is the open problem (keep consistent with the existing end-line; do not duplicate it).
   - Do not restructure anything; insert prose only. Keep the page's voice; symbols already introduced stay introduced once.

## Rules

- Branch **`merle-round6-record`**, two commits as itemized, do NOT merge — the main session reviews and merges.
- No mathematical claims beyond the named sources; no reply paragraphs (none owed this round); no scope expansion; stop after item 2.
