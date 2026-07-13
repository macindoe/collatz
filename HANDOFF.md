# Handoff

Written 2026-07-11, ahead of the primary assistant's access ending. This document lets any capable model (or a future session of any model) continue the project without loss. It is a working document: update it whenever the project's state changes materially.

## Onboarding order for a new assistant

1. `README.md` — what this project is, the strategy, and the **binding stopping rules**.
2. `AGENTS.md` — the schema and verification protocol. Non-negotiable: nothing is labeled proved without independently written verification code; failures are recorded, not deleted; sources/ is immutable.
3. `index.md` — the resolver; then whichever pages the task touches.
4. This file — current state and open items.

**Register norm (author's explicit preference):** flat, calibrated prose. No excitement inflation — it degrades judgment and invites hallucination. Heuristics are labeled heuristics. Claims pass through verification before they pass into prose.

**The author's role:** Ben directs. Empirically, the project's load-bearing ideas — the coordinate system itself, the family diagram, the mirror front, the ladder, the dead-ends map — originated as his plain-language questions. Take his naive-sounding questions seriously and work them before defaulting to queued engineering.

## State of the fronts (2026-07-12)

- **Forward per-step theory** (spine, stages 1–4): closed per step; terminal open object is the anchor increment at unbounded depth ("the bridge", stage4.md 11.8.5.6).
- **Cycles** (cycles.md §12): periods 1–3 closed; uniform trim resolved with sharpness (staircase); front PARKED by stopping rule — reopens only with a divisibility-aware idea.
- **Statistics / AEH** (aeh.md §13): hypothesis formalized, calibration clean (four dissolved anomalies, methodology fixed); proof effort parked. A new **single-sequence** calibration axis was added (anchors.md §17.7), distinct from aeh.md's cross-sectional tests: a breadth battery (§17.7.1, 200 anchors × 4096 bits) and a 32×-deeper single-anchor probe (§17.7.2, one bulk anchor to 2^17 bits), both clean passes against the fair-coin null; plus a first **structural** screen (§17.7.3) showing M(ω) is not 2-automatic (⇔, by Christol, not algebraic over F_2(x)), which rules out the automatic/algebraic family of hidden order; plus three operation lenses (§17.7.4 — Berlekamp–Massey linear complexity, Walsh–Hadamard spectrum, LIL partial-sum walk), all clean. Governing frame now explicit: M(ω) is computable, hence not Martin-Löf random — §17.7 tests pseudo-randomness, which it passes. §17.7.2/§17.7.3 reproduced by delegated Sonnet sessions; §17.7.4 verified inline (author's discretion; delegate-then-verify convention resumes next session). Remaining un-run tool: TestU01/PractRand (blocked on Windows — no gcc/make; MSVC present but TestU01 needs a port; generator O(M²) also caps single-anchor bit volume). Proof effort still parked.
- **Reverse / mirror** (reverse.md §14): ACTIVE. Mirror machinery complete (14.1–14.4), dead ends mapped (14.5), rigorous density bound proved (14.6: X^0.3), dual per-step theory complete (14.7–14.10, delegated to Sonnet, reviewed, merged). **KL–LP refinement CLOSED (2026-07-11, delegated to Sonnet, reviewed + verification re-run, merged):** multi-door renewal gives a small but rigorous lift (14.6.5, c\* 0.3304 → 0.33515); the mod-3^k LP and exact-anchor-phase routes hit a structural obstruction — the collapse map is affine not multiplicative, so no residue or anchor propagates to the child without losing exactly d digits per step (14.13); the 0.43 bar was not reached and the brief closed per its own stop criterion.
- **Ladder** (ladder.md §15): closed as local law.
- **Papers**: BOTH PUBLISHED. Paper 1: Zenodo 10.5281/zenodo.21273548. Paper 2 (the mirror): Zenodo 10.5281/zenodo.21303918, linked via a Continues relation; two external referee cycles completed before publication. Sources at `paper/collatz-reduced-v1.tex`, `paper/collatz-mirror-v1.tex`.

## Open work items, in priority order

1. **The anchor question — author's active focus (2026-07-11).** Ben is turning attention to "pinning down the anchors." Framing settled this session: the anchor `N(ω)` is the **2-adic logarithm of the odd core** — the unique `N(ω) ∈ Z₂` with `9^N(ω) ≡ ω^(−1) (mod 2^k)` for all `k` (stage1-synthesis.md 11.8.3.6), and the global law `s = 3 + v₂(n − N(ω))` says one block is governed by the 2-adic displacement from it. "Pinning it down" splits into two genuinely different questions:
   - **(a) The increment question** — how the anchor moves under one `F`-step (stage4.md ΔM low-order law; the terminal open object is the increment at unbounded depth, "the bridge", 11.8.5.6). This is the direct heir of the 2023 seed question *"what does halving do to the Seed?"*
   - **(b) The equidistribution question** (AEH, aeh.md §13) — whether the anchor's digits behave like fair coins along orbits. Formalized and calibrated (bulk uniformity unqualified); this is the precise statistical half, and its proof is a question about digit-statistics of 2-adic logarithms, beyond current theory.
   The prime-factorization instinct (*"3x+1 only introduces factors of 3, all other primes preserved"*, the 2023 seed) is the **historical ancestor** of the anchor; the mature object deliberately trades the multiplicative factorization of `ω` for the 2-adic digits of a single logarithm, because the dynamics linearize in the log, not in the factorization. Next step: pick (a) or (b) and sharpen one concrete sub-question before any computation — AEH *proof* effort stays parked per the stopping rules, but conceptual/structural framing is open and is exactly the author's-naive-question work HANDOFF flags as load-bearing. **Update (2026-07-11):** the first concrete output of this focus is **§16 (bridge.md)** — consolidating the program's terminal open object (the anchor increment at unbounded depth, forward and reverse) and naming the **core-extraction deficit**: the two-sided per-step anchor precision loss (σ = v₂(C) digits forward, d = v₃(N) reverse, ≥1 always) that unifies the forward digit budget (11.8.7.7) with the reverse affine-collapse obstruction (14.13). Diagnostic, not a lever — it explains why no bounded method closes the bridge in either direction, but does not change what is provable. Verified in experiments/digit_duality.py.
2. **Eric Merle follow-up** (expected week of 2026-07-13): he has paper v1; kindred methodology; his δ8 lemma relates to our staircase theorem — a technical comparison note would be a natural collaboration seed.
3. **KL–LP residual** (low priority; CLOSED front, see State of the fronts). One well-defined sub-question survives in 14.13: whether a *size-threshold-coupled* version of the `(j,r)` DAG (coupling precision-loss to the renewal induction's accumulated-offset variable, rather than crediting exhaustion for free) recovers real gains from residues. Reopens only with an idea for that coupling, not with more computation.

**Standing note — community feedback (de-prioritized 2026-07-11):** outreach (r/Collatz, ccchallenge) is not materializing and is no longer a standing work item. If a substantive response ever does need handling: verify its claims against the wiki, send **one reply, no questions**, and record any found errors per house norms.

## The delegation pattern (proven)

One full case study exists: `briefs/mirror-queue-brief.md` → Sonnet session → branch `mirror-queue` → four theorems with per-commit discipline → independent re-verification in review (~50k checks re-run) → merge. The pattern: (i) written brief forcing AGENTS.md compliance and branch discipline; (ii) explicit "record obstructions, don't force analogies" instruction; (iii) reviewer re-runs all verification code before merging. Use it for items 1–3.

## Known infrastructure quirks

- The sandbox mount of the repo can serve stale reads mid-session (files appear truncated). The Windows-side files are authoritative; verify via PowerShell (`git status`, line counts) before "repairing" anything.
- LaTeX builds: the mount locks aux files; build in a sandbox temp dir and copy artifacts in.
- `\wp` and `\dp` are TeX primitives; the papers use `\wnext`, `\dnext`.
