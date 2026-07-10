# Handoff

Written 2026-07-11, ahead of the primary assistant's access ending. This document lets any capable model (or a future session of any model) continue the project without loss. It is a working document: update it whenever the project's state changes materially.

## Onboarding order for a new assistant

1. `README.md` — what this project is, the strategy, and the **binding stopping rules**.
2. `AGENTS.md` — the schema and verification protocol. Non-negotiable: nothing is labeled proved without independently written verification code; failures are recorded, not deleted; sources/ is immutable.
3. `index.md` — the resolver; then whichever pages the task touches.
4. This file — current state and open items.

**Register norm (author's explicit preference):** flat, calibrated prose. No excitement inflation — it degrades judgment and invites hallucination. Heuristics are labeled heuristics. Claims pass through verification before they pass into prose.

**The author's role:** Ben directs. Empirically, the project's load-bearing ideas — the coordinate system itself, the family diagram, the mirror front, the ladder, the dead-ends map — originated as his plain-language questions. Take his naive-sounding questions seriously and work them before defaulting to queued engineering.

## State of the fronts (2026-07-11)

- **Forward per-step theory** (spine, stages 1–4): closed per step; terminal open object is the anchor increment at unbounded depth ("the bridge", stage4.md 11.8.5.6).
- **Cycles** (cycles.md §12): periods 1–3 closed; uniform trim resolved with sharpness (staircase); front PARKED by stopping rule — reopens only with a divisibility-aware idea.
- **Statistics / AEH** (aeh.md §13): hypothesis formalized, calibration clean (four dissolved anomalies, methodology fixed); proof effort parked.
- **Reverse / mirror** (reverse.md §14): ACTIVE. Mirror machinery complete (14.1–14.4), dead ends mapped (14.5), rigorous density bound proved (14.6: X^0.3), dual per-step theory complete (14.7–14.10, delegated to Sonnet, reviewed, merged).
- **Ladder** (ladder.md §15): closed as local law.
- **Papers**: v1 published (Zenodo 10.5281/zenodo.21273548, cited by repo README). Paper 2 drafted at `paper/collatz-mirror.tex` (7 pp., compiles clean) — **draft only, not yet refereed**.

## Open work items, in priority order

1. **Paper 2 referee passes.** First external skeptical pass (ChatGPT, 2026-07-11) received and fully implemented in revision 2 (commit 132851c): exponent group formalized, M₃(1) language corrected, all Section-5 theorems given in-paper proofs, verification counts moved to an appendix table, density proof rewritten as five lemmas (constant corrected to 2^(−3.6)), steering law simplified to M(pred) ≡ d mod 2^(s−2) with explicit threshold, KL comparison softened. Remaining: send revision 2 back for the referee's re-read (especially the density lemmas); Ben's author's note (his words); then Zenodo as a separate DOI.
2. **Back-port to the wiki:** the steering laws (paper 2, Theorem 7.1 — depth control / 2-adic freeze / anchor placement `M(pred) = −d·M(3) mod 2^(s−2)`) were verified in-session (2,025 checks + freeze data) but never paged. Add as reverse.md 14.12 with a verification script in experiments/ (currently the checks live only in the chat record; re-derive from the laws — they are four lines each).
3. **The KL–LP refinement program** (the front's defined open theorem): reinstate doors, residue types mod 3^k, and anchor phases into the density core; optimize the branch inventory (linear programming, mirroring Krasikov–Lagarias arXiv:math/0205002). Needs its own brief before anyone starts; the brief should set an explicit success/stop criterion (e.g., beat c = 0.43 rigorously or record the obstruction).
4. **Community feedback processing.** Outreach (r/Collatz, ccchallenge) is in the author's hands. Any model can process responses: verify claims against the wiki, draft replies in the author's calibrated register, record any found errors per house norms.
5. **Eric Merle follow-up** (expected week of 2026-07-13): he has paper v1; kindred methodology; his δ8 lemma relates to our staircase theorem — a technical comparison note would be a natural collaboration seed.

## The delegation pattern (proven)

One full case study exists: `briefs/mirror-queue-brief.md` → Sonnet session → branch `mirror-queue` → four theorems with per-commit discipline → independent re-verification in review (~50k checks re-run) → merge. The pattern: (i) written brief forcing AGENTS.md compliance and branch discipline; (ii) explicit "record obstructions, don't force analogies" instruction; (iii) reviewer re-runs all verification code before merging. Use it for items 1–3.

## Known infrastructure quirks

- The sandbox mount of the repo can serve stale reads mid-session (files appear truncated). The Windows-side files are authoritative; verify via PowerShell (`git status`, line counts) before "repairing" anything.
- LaTeX builds: the mount locks aux files; build in a sandbox temp dir and copy artifacts in.
- `\wp` and `\dp` are TeX primitives; the papers use `\wnext`, `\dnext`.
