# Findings: L-A6 verify (merle-la6-check)

Delegated session, 2026-07-25. Brief: `briefs/merle-la6-check-brief.md`.
Branch `merle-la6-check`, base commit `34296e8` (the brief commit; the worktree
HEAD was already at `34296e8`, no rebase needed).
Register: findings only; the three grade strata (exact-confirmed /
model-replicated / assessed-heuristic) kept visibly separate throughout;
nothing here disputes the entry's text — where observation and claim differ,
both are recorded. Verification code: `experiments/merle_la6_check.py` (fresh
code, imports nothing from any Merle repository and nothing from prior
Merle-check scripts; conventions re-implemented from cycles.md 12.6.1/12.6.1.1
and the operational definitions recorded below; exact integer/rational
arithmetic at every pass/fail decision, floats only in the λ/P(0)/tail
readouts, labeled; predictions block written and printed before any sweep;
canaries — the four known cycles' words — hand-computed and printed first).
Full run output committed alongside as `experiments/merle_la6_check_output.txt`.
**424 recorded checks (the census's 816,870 frame-agreement words counted once
each), 0 failures.** No pushes, no shared-repo or Merle-repo writes; both
clones unauthenticated and read-only into the scratchpad. **Handbacks: none.**

## Item 1 — the shared repo and the artifacts, read-only

### (i) Shared repo state

Unauthenticated clone of `github.com/macindoe/one-obstruction-three-faces`
(2026-07-25). **HEAD `81431c754c634b66c057fb784c0f25d844288c71` (`81431c7`) —
exactly the brief's expected pin.** The L-A6 entry entered in two commits, both
Eric MERLE:

- `92a6edb` (2026-07-24 18:05:51 +0200) — seed, `LEDGER.md` +14 lines;
- `fb5e8fc` (2026-07-24 18:46:29 +0200) — realizability-filter addendum,
  `LEDGER.md` +2 lines.

Repo movement since `e53630f`, observed at clone and recorded flat (all his,
2026-07-24, in order): `6b9f2b1` review polish; `49351e5` L-A5 → two keys
(offers (a)+(b) accepted); `08dc3d5` ContentDescent.lean kernel block; the two
L-A6 commits; `81431c7` L-A7 seed (torsion ruler; his µ-source flagged by
himself for re-check). This cross-checks consistent with the round-9 part-1
record (`briefs/merle-la5-closure-findings.md`, which verified `49351e5` and
`08dc3d5` directly); the L-A7 seed is out of this brief's scope and already
briefed separately (`briefs/merle-la7-mu-check-brief.md`).

### (ii) L-A6 entry text, verbatim (current state = seed + addendum)

> ## L-A6 — The calibrated lottery: the two shores' cycle census equals their necklace budget (Merle, correspondence 2026-07-24)
>
> **DRAFT — one key (Merle, measured/assessed grade); Macindoe key invited.**
>
> In the letter alphabet (classical frame, numerator `B` built from the letter constants `β_m = 3^m − 2^m`; frame-agreement `q | B ⟺ q | R_0` checked on every hit), the **complete `C = 1` census at `n ≤ 14`, both shores,** is exactly: the Gersonides freebies (`|q| = 1`: `+1`, `−1`, `−5` — deterministic, outside any lottery), the `−17` orbit at `(n, K) = (7, 11)` (primitive, `q = −139`, the words `(4,3|1,3)` and `(3,4|3,1)` realizing `−17` and `−41`), and the L-A4-forced powers. Nothing else — predictions written before measurement, canaries = the four real cycles' words hand-computed first.
>
> **The lottery, in necklace units** (the necklace is the independent trial — `gcd(q, R_r)` is rotation-invariant by L-A1): south `n ≤ 14`: `λ = 1.12`, primitive necklace-hits **1** (the `−17` — the unique *paid-lock* cycle in existence); north: `λ = 2.64`, primitive hits **0** (`P(0) ≈ 7%`, larger still after the realizability filter — all 18 formal hits observed do realize as true cycles/powers, so the filter only shrinks `λ`). The tail `Σ_{n>14}` decays geometrically at the capacity–demand rate (the (B) constants): south `+0.16`, north `+0.33` through `n = 200`, vanishing beyond; the dominant future cells sit on convergent anchors (`27/17` north, `84/53` south). Cross-checked against the verified range, the north's residual budget — cells whose realizable elements could exceed verification — is `≈ 5·10⁻³` formal cycles.
>
> **Filter closed (Merle, 2026-07-24, REQ-MATH-025).** A formal hit IS a real cycle: all 18 census hits realize exactly (true-map orbit, parity, sigma pattern, return), and the mechanism is the 2-adic ghost identity — the fixed point `x = B/q` follows the word's itinerary automatically (300/300 random words, classical frame; parity of `x` forced by `v_2(ghost) = 0`). So no realizability correction applies: the budgets above are directly real-cycle expectations.
>
> **Reading, at assessed grade and no higher:** the mirror shore *calibrates* the uniform-residue model — its winnings equal its budget — and under the calibrated model the positive shore's remaining expectation is `~0.005`. The wall's exact role is unchanged and now has odds attached: replace this Poisson statement by rigidity (NOTE §6's gap). Falsifier: any second paid-lock cycle, either shore, breaks the calibration.
>
> **Artifacts — Merle (2026-07-24):** `experiments/test_REQ-MATH-022_miroir_rive_sud.py` (exhaustive census), `experiments/test_REQ-MATH-023_loterie_calibree.py` (necklace correction + tails), outputs committed alongside. Joins L-A3's spent-stock and (B)-margin bricks; census consistent with the known ×3−1 cycle list. Open for co-editing.

One pin note, flat: the entry's artifact line names REQ-022 and REQ-023 only;
the filter paragraph names REQ-MATH-025. All three exist with committed
outputs in `ericmerle3789/one-obstruction-three-faces-lean` (REQ-022/023 at his
`ae1edba`, REQ-025 at `8b3a7d3`; that repo's `main` has since moved to
`97b57d7` with exploratory scripts REQ-026..034, read-not-relied-on here; his
REQ-027 commit message itself flags two display caveats of REQ-022 — the
`n ≥ 2` freebie undercount and the power-listing — consistent with our
observations below).

### (iii) Operational definitions, recorded from the scripts (read, never run)

- **Word** = pair of compositions `(m_0..m_{p−1})`, `(s_0..s_{p−1})` of
  `(n, S)` into `p ≥ 1` parts each, entries `≥ 1` ("canonical alphabet
  `s ≥ 1`"), `p ∈ [1, min(n, S)]`; `K = n + S`, `q = 2^K − 3^n`. The `−1`
  cycle's word is the `s = 0` pure-climb, outside the alphabet — his REQ-022
  header P1 notes this explicitly.
- **Census domain (REQ-022):** `n ∈ [2, 14]`, `S ∈ [1, min(9, 2n)]` — an
  `SMAX = 9` window, stated in the code, **not stated in the entry**. His
  sweep also starts at `n = 2`, so of the three freebies only `−5`'s word is
  in-domain (his output: "mots |q|=1 … : 1 — realisations x : [−5]").
- **Hit ("C = 1")** = `|q| > 1` and `|q|` divides the classical numerator
  `B = Σ_t 3^{M_after(t)} 2^{Kpre(t)} β(m_t)`, `β_m = 3^m − 2^m`,
  `Kpre(t) = Σ_{u<t}(m_u + s_u)`; realization `x = B/q`; frame-agreement bit
  = (`R_0 mod |q| = 0`) recorded per hit (`R_0` = cycles.md 12.6.1's rotation
  numerator, his `sigma_t = s_t + m_{(t+1) mod p}` — the 12.6.1 convention).
- **"18 hits"** = **words** (not necklaces), both shores, powers included,
  freebies excluded, in the REQ-022 domain. REQ-025 hardcodes the list:
  trivial^j `j = 2..9`, `(−5)`-word^j `j = 2..7`, the `−17` orbit's two words,
  its square's two words.
- **Necklace** (REQ-023) = rotation class of the letter word (canonical form =
  min over simultaneous rotations); cell budget = `#necklaces/|q|`; shore
  `λ` = sum over that shore's `|q| > 1` cells in the same domain;
  `P(0) = e^{−λ}` (Poisson at the necklace-trial level, uniform-residue
  probability `1/|q|` per trial). Note, flat: his `P(0 primitif)` uses the
  **total** necklace budget (including forced-power and freebie-cell mass),
  compared against **primitive** hit counts.
- **Tail (REQ-023):** `n = 15..200`, `S ∈ [1, int(0.5849625·n) + 3]` (the
  near-tuned band — again not stated in the entry), necklace counts
  approximated as `Σ_p (#words_p / p) / |q|` via base-2 logs with a `−60`
  cutoff; tranches `[15,30], [31,60], [61,120], [121,200]`; dominant cells
  `λ > 0.02`.
- **Residual `≈ 5·10⁻³`:** the committed script computes **no element-size or
  verification-bound criterion**; the only reproduction of the number in his
  artifacts is the sum of the last two tranches, i.e. the **cut `n ≥ 61`**
  (his OUT-023: `0.0049 + 0.0001`). The entry's gloss "cells whose realizable
  elements could exceed verification" is not implemented in the committed
  code; recorded flat (the letter is with the author).
- **Realizability (REQ-025):** true map `x → (3x+1)/2^{v_2(3x+1)}` on odd
  integers of either sign (negatives carry the south = the ×3−1 mirror);
  prescribed itinerary of letter `(m, s)` = `(m−1)` steps of valuation 1 then
  one step of valuation `s + 1`; hit test = σ-sequence equal, return exact,
  `x` odd. Ghost test = `x = B·q^{−1} mod 2^{Bits}`, `Bits = K + 64 + n`,
  orbit run mod a shrinking margin, 300 random words `p ≤ 5`, entries `≤ 6`,
  seed 20260724.

## Item 2 — independent verification (`experiments/merle_la6_check.py`)

Predictions block printed first (expected census word-by-word, budgets,
tranches, realizability, paid-lock verdict — all as stated in the output);
canaries hand-computed before coding and printed before any sweep: the four
known cycles' words (`+1`: `q = 1, B = 1, x = 1`; `−1`: `σ = (1)^n`,
`B = 3^n − 2^n = −q`, `x = −1`, outside the alphabet; `−5`: `q = −1, B = 5`;
`−17`: `B(4,3|1,3) = 27·65 + 32·19 = 2363 = 17·139`, `x = −17`, `R_0 = 139`,
and the rotation `B(3,4|3,1) = 5699 = 41·139`, `x = −41`, `R_0 = 695 = 5·139`),
the hand ghost instance on `−5`, the hand true-orbit of `−17`
(σ `1,1,1,2,1,1,4`), and the `(7,11)` necklace count by hand-Burnside
(`1 + 9 + 15 + 5 = 30`). All passed before any sweep.

### (a) Census — CONFIRMED EXACT, and completed to all `S`

- **His domain, exhaustive: 816,871 words over 108 cells.** Hits (`|q| > 1`):
  **exactly the predicted 18 words, nothing else** — trivial^j at `(j, 2j)`
  `j = 2..9` (north, `x = 1`), `(−5)`-powers at `(2j, 3j)` `j = 2..7` (south,
  `x = −5`), the `−17` orbit at `(7,11)` (`q = −139`; `(4,3|1,3) → −17`,
  `(3,4|3,1) → −41`), its square at `(14,22)` (`q = −588665`). Freebie stock
  in-domain: exactly 1 word (`([2],[1])` at `(2,3)`, `x = −5`). Primitive
  hits: exactly the `−17` orbit's 2 words = 1 necklace, south; north 0.
- **Frame agreement `q | B ⟺ q | R_0`: 816,870/816,870 words, both
  directions** (every `|q| > 1` word, not only hits). Stronger probe, an
  observation beyond the entry's claim: `gcd(|q|, B) = gcd(|q|, R_0)` at
  **every** word — the two frames agree at full gcd level, not only at
  divisibility.
- **`n = 1` (below his `n ≥ 2` start), closed analytically:** all `n = 1`
  words have `B = 1`; `|q| = 1` only at `S = 1` (the `+1` freebie); no hits.
- **Census completion to ALL `S ≥ 1` at `n ≤ 14` (our extension, exact):**
  using the ghost lemma (below) + the cycle product identity
  `2^K = Π_t (3 + 1/x_t)`: a south hit forces `2^K < 3^n` (`|x_t| ≥ 3`), i.e.
  `S ≤ 8` for `n ≤ 14` — every possible south hit was already inside his
  window; a north extension hit (`S ≥ 10`) forces
  `x_min ≤ 1/(2^{K/n} − 3)`, a tiny bound (`< 1` for `S > 2n`, impossible),
  enumerated exactly: the only candidates are `x = 1` at `(j, 2j)`,
  `j = 10..14` — the trivial powers, each verified `B = q` directly. **The
  complete all-`S` census at `n ≤ 14` is 23 words** (13 trivial powers + 6
  `(−5)`-powers + 2 + 2), and the entry's qualitative claim — freebies + `−17`
  orbit + L-A4-forced powers, **nothing else** — holds *unconditionally* at
  `n ≤ 14`, stronger than his sweep verified. The count "18" is the
  `S ≤ 9` window count (domain note, not a discrepancy). Consistent with
  12.6.1.2's exhaustive `k ≤ 10` two-sector replication.
- **L-A4 cross-check:** all 16 non-primitive hits decompose as `base^k` with
  base a hit (or the `−5` freebie), and the 12.6.1.4 identities
  `R_0(B^k) = R_0(B)·G_k`, `q_{B^k} = q_B·G_k` hold exactly at every
  instance (48/48).
- **Interest cells replicated (word level, REQ-022):** `(5,8)`: 15 words,
  `λ = 1.154`, 0 hits; `(7,11)`: 84 words, 2 hits; `(12,19)`: 12,376 words,
  `λ = 1.730`, 0 hits — all digit-exact against his output.

### (b) Necklace budgets — REPLICATED EXACT (model computation)

Exact necklace counts per cell, two independent methods (canonical-form count
and Burnside), agreeing on all 108 cells; primitive-word counts cross-checked
by Möbius on every cell. Budgets as exact `Fraction`s, floats only at the
readout:

- **South `λ = 1.1175` (his 1.12), north `λ = 2.6447` (his 2.64)** —
  digit-exact at his printed precision. `P(0) = e^{−λ}`: south `0.3271`
  (his 0.327), north `0.0710` (his 0.071, the entry's "≈ 7%"). Necklace hits
  8/8, primitive 1 south / 0 north — matches (a)'s census with powers and
  freebies excluded per the definitions.
- Word-level replication of REQ-022: budgets `3.41 / 6.17`, word hits
  `10 / 8` — digit-exact.
- The Poisson step is stated as **model** (uniform residue `1/|q|` per
  necklace trial, independence across cells), per the brief.
- Flat observation, quantified: his `P(0)` uses the **total** budget while
  the hits it prices are the **primitive** ones; the primitive-only budgets
  are `λ_prim = 1.0502` south / `2.4282` north (`P(0)` 0.350 / 0.088). Same
  qualitative story; the entry's 7% would read 8.8% in primitive-only units.
  Co-edit candidate, minor.

### (c) Tail — REPLICATED, both his approximation and an exact upgrade

- **Exact Burnside necklace counts** per cell over his recorded window
  (`n = 15..200`, `S ≤ int(0.5849625·n)+3`): tranches
  `0.1043/0.2648`, `0.0519/0.0583`, `0.0034/0.0049`, `0.0000/0.0001`
  (south/north) — **identical to his OUT-023 at all four decimals** (his
  words/`p` approximation is that accurate here; separately replicated his
  formula, same numbers). Totals **south 0.1596, north 0.3280** — the entry's
  `+0.16 / +0.33`.
- **North residual:** `n ≥ 61` sum = **0.0050** — the entry's `≈ 5·10⁻³`,
  under the cut identified in item 1(iii). The cut's provenance ("the
  verified range") is not in the committed artifacts; recorded flat.
- **Dominant cells (exact):** max `(17,27)` north `λ = 0.062`; then `(24,38)`
  south `0.034`, `(53,84)` south `0.028`, `(15,24)` north `0.022`, `(29,46)`
  north `0.022`, `(19,30)` south `0.021` — matching his list cell for cell.
  The `27/17` / `84/53` anchor claim: both cells confirmed as stated. Two
  flat notes: `84/53` is a principal convergent of `log₂ 3`, `27/17` a
  semiconvergent (mediant of `8/5` and `19/12`) — "convergent anchors" covers
  both loosely; and the top **south** cell by budget is `(24,38)` (the
  doubled `19/12` convergent), with `(53,84)` second — the entry names
  `84/53` for the south.
- **Decay rate vs the (B) constant:** effective rates from the exact tranche
  sums (midpoint spacing): `0.0758`, `0.0830`, `0.0863` bits/n — geometric
  decay confirmed, rates bracketing `c_gen = 0.0793` (round-8 part A /
  12.6.1.5). Model-replication readout, labeled.
- **Window note, flat (operational-definition observation):** beyond the
  near-tuned band the uniform-residue budget is size-degenerate — a hit
  `q | B` with `0 < B < q` is impossible, which is REQ-016's recorded 94–98%
  size artifact — while the *formal* per-cell budget does **not** decay with
  `K` (illustrated at `n = 17`: `#words/q ≈ 0.032–0.035` for `K = 29..34`,
  against realizable-size bounds collapsing below 4). The `S`-window is
  therefore a load-bearing, principled part of the model's definition; the
  entry states the census count, the budgets, and `Σ_{n>14}` without stating
  it. Co-edit candidate (one clause naming the band).

### (d) Realizability and the ghost identity — CONFIRMED, and upgraded to EXACT

- **All census hits realize: 23/23** (his 18 + the 5 extension powers):
  exact integer true-map orbit follows the word's σ-itinerary step for step,
  returns exactly, `x` odd — his 18/18 reproduced and extended.
- **Fresh 2-adic ghost draws (our seed, our code): 350/350** (47 south / 303
  north), exceeding his 300/300.
- **The load-bearing lemma is EXACT, not merely empirical.** Derivation
  (this session, checked by machine): in the per-odd-step frame
  `B(W) = Σ_{j<n} 3^{n−1−j} 2^{σ_0+…+σ_{j−1}}` (equal to the letter-frame `B`
  via `β_m = Σ_{j<m} 3^{m−1−j}2^j`; cross-checked 300/300), the **telescoping
  identity**

  ```text
  3·B(W) + q = 2^{σ_0} · B(shift W),    q = 2^K − 3^n,
  ```

  holds for every σ-word with entries `≥ 1`: the `j = 0` term `3^n` cancels
  `q`'s `−3^n`, factoring `2^{σ_0}` from the remainder reindexes it to the
  shifted word, and `q`'s `2^K` supplies the shifted word's last term. `B(W)`
  is **odd** for every word (its `j = 0` term is the unique odd term) — this
  is exactly his "`v_2(ghost) = 0`". Hence for `x = B(W)/q ∈ Z_2` (`q` odd):
  `3x + 1 = 2^{σ_0}·(B(shift W)/q)` with the second factor an odd 2-adic
  unit, so `v_2(3x+1) = σ_0` is **forced** at every step; the true-map orbit
  of the ghost follows the word's itinerary automatically and returns after
  `n` steps (`shift^n = id`). Verified exhaustively (all σ-words with entries
  `≤ 4`, lengths `≤ 5`: 1,364/1,364, every rotation position, oddness, and
  full-period return) and on 400 random words (lengths 6–40, 200 south / 200
  north): 0 failures. Consequence, exact: **a formal hit IS a real cycle** —
  `q | B` makes `x = B/q` an odd integer whose true-map orbit realizes the
  word (sign of `x` = shore; powers traverse their base cycle). No
  realizability correction applies to the budgets, exactly as the addendum
  claims — and the identity is the odd-step refinement of 12.6.1.1's
  transport recurrence (same telescoping mechanism, per-step instead of
  per-block). **Grade: exact-confirmed** — his empirical 18/18 + 300/300 is
  upgraded to a proved two-line identity on our side.

### (e) "The unique paid-lock cycle in existence"

Checked on the known census (cycles.md 12.6.1.2 anchors): `+1 (q = 1)`,
`−1 (q = −1)`, `−5 (q = −1)`, `−17 (q = −139)` — **exactly one paid lock
(`|q| > 1`) among the four knowns: the `−17`.** TRUE on the knowns. The
phrase's ground, per the entry itself, is "census consistent with the known
×3−1 cycle list" — the classical known list (Lagarias 1985, pinned at
14.15.6(d)(iv)/12.6.1.2). Its universality — no further paid-lock cycle on
either shore — is exactly the parked open condition `q | R_0` (south: the
open ×3−1 cycles question beyond verified ranges), and the entry's own
falsifier sentence ("any second paid-lock cycle, either shore, breaks the
calibration") carries this honestly. Not an overreach as phrased in context;
a scope clause ("known") would make the sentence self-contained. Minor
co-edit candidate.

## Adjudication summary (one line per entry claim, grade-stratified)

| Entry claim | Status / grade |
|---|---|
| 1. Census (freebies + `−17` orbit + L-A4-forced powers, nothing else, `n ≤ 14`; frame agreement; predictions-first) | **EXACT-CONFIRMED** — 18/18 word-exact in his domain (816,871 words swept); frame biconditional 816,870/816,870 plus gcd-level equality; completed our side to ALL `S`: the qualitative claim holds unconditionally (23 words), "18" being the unstated `S ≤ 9` window count |
| 2. Necklace budgets (south `λ = 1.12`, 1 primitive hit; north `λ = 2.64`, 0, `P(0) ≈ 7%`) | **MODEL-REPLICATED, exact as computations** — 1.1175/2.6447 from exact necklace counts (two methods agreeing on every cell); hits and primitives match census; Poisson/uniform-residue is model, stated so; flat note: `P(0)` priced on total budget vs primitive hits (`λ_prim` 1.0502/2.4282) |
| 3. Tail (geometric at the (B) rate; `+0.16/+0.33` to `n = 200`; anchors `27/17`, `84/53`; residual `≈ 5·10⁻³`) | **MODEL-REPLICATED** — his numbers reproduced to all printed decimals, and upgraded to exact necklace counts (identical at 4dp); decay rates 0.076–0.086 bits/n bracket `c_gen = 0.0793`; dominant cells confirmed (notes: `27/17` is a semiconvergent; top south cell is `(24,38)`); residual = the `n ≥ 61` cut, provenance of "verified range" not in the committed artifacts |
| 4. Realizability filter = 1 (18/18; ghost identity; `v_2(ghost) = 0`) | **EXACT-CONFIRMED AND UPGRADED** — 23/23 orbits exact; 350/350 fresh draws; the ghost identity derived as a proved telescoping identity (`3B + q = 2^{σ_0}B'`, `B` always odd), so "formal hit IS a real cycle" is a theorem, not a measurement; budgets are real-cycle expectations exactly as claimed |
| 5. Reading (south calibrates the model; north residual ~0.005; falsifier) | **ASSESSED-GRADE HEURISTIC, left exactly there** — he labels it so himself ("at assessed grade and no higher"); nothing in our verification raises or lowers it; the falsifier is well-posed given (e) |
| 6. "Unique paid-lock cycle in existence" | **TRUE ON THE KNOWNS** (exact check); "in existence" grounded on the known ×3−1 list per the entry's own artifact line; universality = the open condition, carried by his falsifier sentence; scope clause a minor co-edit candidate |

## Flags, collected (recorded, not disputed)

1. **Domain/window not stated in the entry** (the round's main co-edit item,
   minor in substance): the census "18" is the `S ≤ 9` window count and the
   `n ≥ 2` start sees only the `−5` freebie (his own REQ-027 later flags
   this); the budgets and tail live on the near-tuned band
   `S ≤ int(0.5849625·n)+3`, which is *load-bearing* (outside it the formal
   budget does not decay while realizable size collapses — the REQ-016 size
   artifact). One clause naming the band, plus "known" before "in existence",
   would close all of it. Our side supplies a *strengthening* to offer: the
   census claim is true unconditionally at `n ≤ 14` (all `S`), by the ghost
   lemma + the product-identity size argument, 23 words.
2. **The residual's cut:** `≈ 5·10⁻³` = the north tail for `n ≥ 61`; the
   committed script computes no verification-bound criterion, so "beyond the
   verified range" rests on the letter, not the artifact. Co-edit candidate:
   pin the cut in the entry.
3. **`P(0)` prices primitive hits with the total budget** (forced-power and
   freebie-cell mass included): `λ_prim = 1.0502/2.4282` would give
   0.350/0.088. Same story, cleaner units; minor.
4. **Anchor wording:** `27/17` is a semiconvergent (mediant), not a principal
   convergent; the top south cell is `(24,38)` (doubled `19/12`), `84/53`
   second. Substance replicates; wording loose. Minor.
5. **Repo movement, flat:** L-A5 is now **two keys** (his `49351e5` accepted
   offers (a) and (b) — the restatement is faithful to our findings' language);
   `08dc3d5` adds a kernel L-A4/L-A2 artifact with committed axioms;
   **L-A7 is seeded** (out of scope here; its own µ-source flag is his).
   These belong to the main session's ledger state, not to this round's key.

No discrepancies of digits, hashes, or texts anywhere this round: every
number the entry and his outputs state was reproduced exactly at its stated
precision. **Handbacks: none.**

## Key recommendation (recommendation only; no key is turned here)

**Turn, with offers** — the key's scope stated exactly:

- **Turns on:** the census (exact, both frames, with our all-`S` completion
  recorded as a strengthening), the realizability filter (exact — the ghost
  identity proved, upgrading his empirical grade), and the budget/tail
  numbers **as replicated model computations** (exact necklace counts our
  side, matching his approximation at all printed decimals).
- **Explicitly left at his own assessed grade:** the calibration reading
  (south winnings = budget; north residual ~0.005 as "odds attached to the
  wall") — our key must not grade it higher, and his entry already labels it
  correctly.
- **Offers to carry (acceptance his call):** (a) domain clauses — the
  `S ≤ 9` census window / `n ≥ 2` start and the near-tuned tail band named
  in the entry, with the all-`S` completion at `n ≤ 14` offered as the
  closure (23 words; ghost + product-identity argument); (b) the ghost
  identity as a stated exact lemma (`3B(W) + q = 2^{σ_0}B(shift W)`, `B`
  odd), replacing "300/300 random words" as the entry's mechanism sentence;
  (c) pin the residual's `n ≥ 61` cut; (d, minor) "known" before "in
  existence", `λ_prim` units, and the semiconvergent wording.

Stopping-rule compliance, recorded: bounded-range census re-verification and
model replication only; no cycle search beyond the recorded domains, no
exclusion attempt, no equidistribution proof effort; the wall touched only
descriptively (the falsifier and the reading, both left at their stated
grades). The cycles front stays PARKED.
