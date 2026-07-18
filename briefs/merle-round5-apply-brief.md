# Brief: round-5 apply — Remark 12.6.1.2, ledger entries L-A2/L-A3, HANDOFF record (for a delegated session)

**Context required before starting (in order):** `AGENTS.md`, `HANDOFF.md` item 1, `briefs/merle-round5-check-findings.md` (entire — the source of every applied line), `briefs/merle-round5-check-brief.md` (Appendix A, the letter), `cycles.md` 12.6.1–12.6.1.1 (placement target), `briefs/merle-round3-apply-brief.md` (the apply-round pattern this follows).

## Author decisions, recorded (2026-07-19)

1. **L-A2: agreed.** The repeated-word gcd law becomes a ledger entry (his proposal), both sides' keys attached.
2. **Gateway-viz plan change: accepted.** Each side builds its own cycle-side gateway and cross-links (replaces the round-4 plan where we build the only one). Our viz is being built in a parallel delegation (branch `cycle-gateway-viz`); this brief does not touch `viz/`.
3. **Note bricks: in, credited to Merle.** The spent-stock framing and the Benford side-asymmetry enter the joint note as his packaging ("it's his"); the Gersonides-not-Mihailescu citation posture adopted (author follows the findings' recommendation); his 50/50 self-catch stays visible per protocol; the k = 1 tie and the citation posture ride along from our verification.
4. **Stale header: mention.** One friendly line in the eventual reply (reply is NOT this brief's deliverable).
5. **L-A3: create.** The anchored-loops/spent-stock/Benford entry, per the findings' draft.

## Queue, in order

1. **Apply Remark 12.6.1.2 to `cycles.md`**, placed directly after Remark 12.6.1.1. Use the findings item 6(i) draft verbatim except: resolve the `[credit phrasing per the author]` placeholder to flat text implementing decision 3 — the spent-stock packaging is Merle's (round-5 correspondence, his commit `a67970f`, scripts REQ-MATH-010/011); the verification is joint (`experiments/merle_round5_check.py`, 211,047 checks, 0 failures, 2026-07-19); the `k = 1` exact tie and the Gersonides citation posture arose in our verification. Transcription only — no number, range, or claim may differ from the findings file. Check `index.md` for staleness against the new remark (expect: not stale — remark-level addition; state the judgment).

2. **Seed L-A2 and L-A3 into the shared repo's `LEDGER.md`** (`github.com/macindoe/one-obstruction-three-faces`) — author-authorized push, same pattern as the L1–L3/L-A1/L4 seeding (`briefs/merle-ledger-seed-brief.md` round). Use the findings item 6(ii) drafts, resolving the bracketed keys lines: L-A2 keys — his `a67970f` scripts + our `experiments/prime_local_probe.py` and `experiments/merle_round5_check.py`; L-A3 keys — his `a67970f` (REQ-MATH-010/011) + our `experiments/merle_round5_check.py`. Mark both entries **draft, for co-editing**, matching the existing seeded entries' header convention (read the live LEDGER.md first and match its format exactly). Constraints: one additive commit, `LEDGER.md` only, no other file touched, no force-push; then **audit via the GitHub API** (compare the pushed diff against your intended text verbatim) and record the commit SHA, line delta, and audit verdict in the findings-record section of your report and in HANDOFF.

3. **HANDOFF item 1 update** (round-5 record): fifth reply received (pasted verbatim; personal register on the JAR reframing; venue convergence now three independent readers; hosting settled — he DOI-pins to v2 and hosts the pair; viz accepted, each-side-builds-one plan proposed and accepted); the check delegated, verified, merged (`briefs/merle-round5-check-findings.md`: anchor table exact, |q|=1 lock 14th-century — Gersonides not Mihailescu, envelope proved, Benford side-asymmetry confirmed with the k = 1 tie refinement, k ≤ 10 map replicated exactly — 250,952 profiles, cycles exactly the four known, his commit `a67970f` found and read, one stale 50/50 header noted); the five author decisions as listed above; applied outcomes (Remark 12.6.1.2; L-A2/L-A3 seeded, SHA); state: our cycle-gateway viz in flight (parallel branch), the reply drafted **after** both artifact rounds land so it can point at shipped objects, sending stays with the author.

## Rules (non-negotiable)

- Branch **`merle-round5-apply`**, one commit per queue item, do NOT merge — the main session reviews and merges.
- Transcription discipline: every mathematical statement in applied text is copied from the findings file, not re-derived, not re-worded beyond the resolved placeholders. If a findings number and any wiki number appear to conflict, stop and record the conflict; do not harmonize.
- The shared-repo push is the ONLY action outside this repo; it is additive, LEDGER.md-only, and audited. No PROTOCOL.md edits, no issues, no comments.
- Register flat. No reply paragraphs — the reply is a later round.
- No scope expansion; stop after item 3.

## Definition of done

Remark 12.6.1.2 applied with the credit placeholder resolved per decision 3; index.md staleness judged; L-A2/L-A3 live in the shared LEDGER.md as draft-for-co-editing with the push audited via API and the SHA recorded; HANDOFF item 1 carries the full round-5 record including the decisions and the in-flight viz; three clean commits on `merle-round5-apply`.
