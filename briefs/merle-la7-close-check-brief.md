# Brief: L-A7 closure check — Merle's round-10 acceptance + margin-proof numerics — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md`, `HANDOFF.md` item 1, `briefs/merle-la7-mu-check-findings.md` (our round-9 L-A7 record — the μ adjudication, the 372/440 crossings, the sensitivity table, the operational definitions of `R(n)`, best cell, word units), `briefs/merle-round8-coedit-findings.md` part A (the (B) constants: `c_gen = 0.0793186`, `c_strat = 0.2667875`, `α* = 0.3747344` — derivation and meaning).

## Provenance

Merle answered our round-9 reply with three letters (2026-07-25/26) and eleven shared-repo commits: shared repo `github.com/macindoe/one-obstruction-three-faces` HEAD moved `641a530 → 826970e`, `LEDGER.md` only (+114 lines), all his. The L-A7 blocks (commits `9c14824`, `203aeb4`, `fa4acb5`, `266f26b`, `bd16011`) claim:

1. **Acceptance of our four offer clauses verbatim** (Rhin 1987 / Simons–de Weger 2005 re-sourcing; headline `n ≈ 2233`; `C₀ ≈ 2.06`; repair bits `< 1.94`). The `≈ 550` crossing **withdrawn** — never computed; his re-derivation: per-scale `n = 372`, cumulative `N = 440`, "reproducing both Macindoe readings exactly."
2. **Volunteered honesty item:** his `C₀` is exhibited from data, not proved for all `n` — entry now conditional on the for-all-`n` margin inequality. Our offer to write that proof: accepted.
3. **South floor discharged with no new ingredient:** `ε_n = ⌈nL⌉ − nL`, `ε′_n = nL − ⌊nL⌋`, `ε_n + ε′_n = 1` identically; at most one shore small; the other `≥ 1/2` free; both-shore step ≤ 1 bit. Numerics: 0 violations all `n` tested; `n = 15601`: `ε = 2.6·10⁻⁵`, `ε′ = 0.999974`; `n = 190537`: min `9.3·10⁻⁸`.
4. **Margin inequality verified + route de-risked:** `margin(n) − c_gen·n ≥ 0` exact, `n ≤ 3000`, min slack `2.8414` at `n = 2` (our `2.84`). Entropy route (`C(m,k) ≤ 2^{m·H(k/m)}`, `m = n+S−2`, `k = n−1`) dominates `c_gen·n` to `n = 200,000` **but is tight**: route margin stays in `[1.66, 2.10]` bits, min `1.6647` at `n = 16266`, asymptotically constant; the gap between true margin and entropy bound tracks `(1/2)·log₂ n` (measured `3.92` at `n = 100`, `8.91` at `n = 10⁵`, vs `3.32`, `8.30`).
5. **Junction provenance:** the deficit lemma appears in his older Junction Theorem preprint §3 with constant `γ = 1 − h(1/log₂3)` and **`γ·log₂3 = c_gen` exactly (claimed error 0.0 at fifty digits)** (REQ-MATH-037).
6. **The margin inequality claimed PROVED at kernel** (`marginTarget`, `DeficitLemma.lean`, stack `b22fafc` in his Lean repo `ericmerle3789/one-obstruction-three-faces-lean`): rational binomial route `x = 12/7` near `x* = 1/(log₂3 − 1) = 1.7095`, statement `12^k · 7^(m−k) · C(m,k) ≤ 19^m`; asymptotic constant `0.0793165`, within `2.1·10⁻⁶` of `c_gen`; **proved constant `1/13 = 0.0769231`** (~3% below `c_gen`); `margin(n) ≥ n/13` for `n = 1..3000`, 0 failures, min slack `1.700` bits; integer target `C(K−2,n−1)^13·2^n ≤ 2^{13K}` for `n = 1..1200`, 0 failures, binomial route implying it with ≥ 22 bits spare; negative control `c = 2/25` fails at 241 scales. Assembly: window for `t/s` = `[5.727444, 5.747075]` (width `0.0196`), `s = 15, t = 86` smallest admissible, atoms holding with `0.088` and `0.327` bits spare; `key_core`: `2^{86(k+j+2)}·2^{15(k+1)}·7^{195k} ≤ 2^{562}·12^{195k}`. Two recorded Merle-side machine-caught errors (missing `/log₂3` proposing inadmissible `s = 1, t = 6`; `norm_num` failing on a 71-digit constant, replaced by `3^86 ≤ 4^86 = 2^172`).
7. **Thresholds recomputed under the proved constant** (REQ-MATH-043, same Rhin exponent): per-scale crossing `1596 → 1655`, cumulative-tail `1661 → 1722`.

This session verifies the NUMERICS AND ALGEBRA of all of the above in a clean room. The Lean statement-match is a **sibling session, not yours** (`merle-lean-r10-audit`); do not audit `.lean` files beyond pulling operational definitions if a ledger claim is otherwise ambiguous.

**Stopping-rule compliance:** replication of a correspondent's verified claims — not a proof effort on the open condition, not a cycle search. Cycles front stays PARKED.

## Queue

1. **Shared repo, read-only.** Fresh clone (scratchpad). Record HEAD (expected `826970e`; if moved, record and continue read-only at `826970e`). Record the five new L-A7 blocks verbatim in the findings. Read his committed artifacts (`test_REQ-MATH-035/036/039/040/042/043` scripts + outputs in the Lean repo's `experiments/`) for operational definitions ONLY; never run his code as verification.

2. **Replication, fresh code** (`experiments/merle_la7_close_check.py`; imports nothing from his repos or prior checks; exact integers for word counts and `q`; `mpmath` with stated guard digits for logs — every pass/fail decision robust to rounding, state how):
   - (a) **Crossings.** Re-derive per-scale 372 / cumulative 440 from our own chain (should match `briefs/merle-la7-mu-check-findings.md`; if our findings already state them, recompute anyway — this is the cross-check that his "reproducing both readings exactly" is true).
   - (b) **South floor.** Prove `ε + ε′ = 1` for irrational `nL` in one line (record it); verify the claimed values at `n = 15601` and `n = 190537` and scan all `n ≤ 200,000` for min/max; confirm "at most one shore < 1/2".
   - (c) **Margin + entropy route.** Reproduce min slack `2.8414` at `n = 2` (`n ≤ 3000`). Then the route: verify domination and tightness to `n = 200,000` (or the largest `n` you can do with honest precision — state the range you achieved); reproduce `[1.66, 2.10]`, min `1.6647` at `n = 16266`, and the `(1/2)log₂n` tracking pairs (3.92/3.32, 8.91/8.30).
   - (d) **The γ identity.** Verify `γ·log₂3 = c_gen` at ≥ 50 digits, AND attempt the symbolic derivation (both sides in closed form from the (B) derivation in round-8 part A) — if it is an exact identity, say why; if only numeric, say so flatly.
   - (e) **The rational route constants.** Derive the asymptotic constant of the `x = 12/7` bound yourself (from `C(m,k) ≤ (1+x)^m/x^k` and the `K`-vs-`n` relation `3^n ≤ 2^K < 2·3^n`); reproduce `0.0793165` and the `2.1·10⁻⁶` loss; confirm `x* = 1/(log₂3 − 1)` recovers `c_gen` exactly at the optimum.
   - (f) **Assembly arithmetic, exact integers.** Verify the window `[5.727444, 5.747075]` from its definition (re-derive what constraint puts `t/s` there — his artifacts state it; record the derivation), confirm `s = 15, t = 86` is the smallest admissible pair (exhaust `s = 1..14`), confirm the atom margins `0.088`/`0.327` bits, verify `key_core`'s inequality for a sweep of `(k, j)` in exact integers, and confirm the two recorded error-catches (the inadmissible `s = 1, t = 6` really is refuted by the exact check; `3^86 ≤ 4^86 = 2^172` is trivially true and sufficient where used).
   - (g) **Proved-constant claims.** `margin(n) ≥ n/13`, `n = 1..3000`, min slack `1.700` bits; integer target `n = 1..1200` and the ≥ 22-bit implication margin; negative control `c = 2/25` fails at exactly 241 scales in his stated range (record his range).
   - (h) **Thresholds.** Recompute the four figures 1596/1655/1661/1722 under Rhin 13.3 × {`c_gen`, `1/13`}; reconcile with our sensitivity table's `n ≈ 2233` headline (different quantities — state the definitions of each so the entry can never confuse them again).

3. **Record** (branch commits, per-item):
   - `experiments/merle_la7_close_check.py` + committed output (one commit; canaries printed first).
   - `briefs/merle-la7-close-check-findings.md` — verbatim blocks; every replication with match/mismatch stated flat; the γ-identity verdict; the key recommendation. Expected shape: L-A7's **two-keys standing is confirmed** (his acceptance satisfied our stated condition) and the question is whether the NEW margin-proof blocks are verified our side — recommend scoped co-edit language (our verification record for the additions; any discrepancies as offers). The `marginTarget` kernel claim itself is the sibling session's to adjudicate; your recommendation covers numerics/algebra only and says so.
   - `HANDOFF.md` item 1 — ONE scoped paragraph on this check's state; do not touch other lines (siblings `merle-lean-r10-audit` and `merle-la8-t1-check` edit item 1 in parallel).

## Rules

- Branch **`merle-la7-close-check`** from your worktree HEAD (verify it contains this brief; state the base SHA in the findings). Per-item commits; do NOT merge — the main session reviews (re-runs the script) and merges.
- Read-only everywhere outside this repo: no pushes, no shared-repo writes, no web access (all items are internal mathematics; the citations were adjudicated in round 9).
- Discrepancies recorded and flagged, never disputed in prose. Record obstructions; don't force analogies.
- No reply paragraphs; no key turns (recommendation only); no co-edit commits; stop after item 3.
