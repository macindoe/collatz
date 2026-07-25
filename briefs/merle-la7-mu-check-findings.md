# Findings: L-A7 μ-source check + replication (merle-la7-mu-check)

Delegated session, 2026-07-25. Brief: `briefs/merle-la7-mu-check-brief.md` (commit `34296e8`).
Branch `merle-la7-mu-check`, base commit `34296e8` (the brief commit; worktree cut from it directly).
Register: flat; discrepancies recorded, not disputed; every replication number below is from this
session's own code (`experiments/merle_la7_check.py`), not from his script, which was read for
operational definitions only and never run.

**No pushes anywhere; shared repo and Merle's repo cloned read-only into the scratchpad; web access
used for item 2 (μ-source literature) only.**

## 1. The entry, the artifact, and the operational definitions

**Clones (read-only).** Shared repo `github.com/macindoe/one-obstruction-three-faces`, HEAD
**`81431c7`** — exactly the expected commit ("Seed L-A7 draft: the torsion ruler …"). Merle's
repo `github.com/ericmerle3789/one-obstruction-three-faces-lean`, HEAD `97b57d7` (his stack has
moved past the L-A7 artifact: REQ-MATH-030..034 exist, out of this session's scope); the L-A7
artifact `experiments/test_REQ-MATH-029_regle_de_torsion.py` + `experiments/OUT_REQ-MATH-029.txt`
entered at his commit **`f550147`** and are byte-unchanged at his HEAD (single commit in their
`git log`).

**The ledger entry, verbatim (LEDGER.md at `81431c7`, entry L-A7 in full):**

> ## L-A7 — The torsion ruler: the lottery's total ticket mass is effectively finite, at every scale (Merle, correspondence 2026-07-24)
>
> **DRAFT — one key (Merle; theorem-grade modulo two published ingredients); Macindoe key invited.**
>
> The instrument fuses the two rulers this program already owns: the **(B) counting constant** `c_gen = 0.0793186` (crowd-side, finite places) and the **effective irrationality measure of `log₂3`** (exponent `μ = 5.125`, Salikhov as documented in the Merle v2 corpus §5 — *primary source to be re-checked before any publication*). The second is an **individual-grade** Diophantine statement — true for *every* `n`, no averaging — i.e. exactly the archimedean component of the "individual resolver" that NOTE §6's residual gap calls for, wired to the counting for the first time in this frame.
>
> **Statement (verified `n ≤ 2000`, canary-anchored):** for the best north cell at scale `n`, `R(n) = log₂(#words) − log₂ q ≤ −c_gen·n + (μ−1)·log₂ n + C₀`, with `C₀ = −5.77` exhibited (max at `n = 2`); the ingredient inequality has enormous slack (`min_n ε_n·n^{μ−1} ≈ 14.5`). Canaries: anchors `(5,8) → q = 13`, `(7,12) → q = 1909`; the `n ≤ 14` word-budgets reproduce the census exactly (`6.17` north / `3.41` south). **Consequence, effective and scale-free:** the tickets' total mass beyond `n = 600` is provably `< 5.2·10⁻⁴` (both shores; word units, which upper-bound necklace units), and everything below `n = 600` is exact finite computation. **The kiosk provably closes:** L-A6's tail is no longer "computed to `n = 200`" but bounded for all `n` by two published constants and elementary algebra.
>
> **Honest scope:** this bounds the *expectation*, not the truth — the model→certainty step remains the ×2×3 gap, unchanged. The bound is slack at small `n` (Salikhov's exponent is worst-case) and crosses below one ticket near `n ≈ 550`; sharper measures only improve `C₀`.
>
> **Artifacts — Merle (2026-07-24):** `experiments/test_REQ-MATH-029_regle_de_torsion.py` (+ committed output), predictions written before measurement. Open for co-editing.

**Operational definitions, read from the script (`f550147`), recorded — the script was never run:**

- **Cell:** a pair `(n, S)`, `K = n + S`, `q = 2^K − 3^n`, cells with `|q| ≤ 1` excluded. Shore =
  sign of `q` (north `q > 0`, south `q < 0`).
- **`#words` per cell:** the general-family profile count `C(n+S−2, n−1)` (the Vandermonde closed
  form of 12.6.1.5's general family — entries `≥ 1`, `Σm = n`, `Σs = S`), computed in his script
  via `lgamma` floats.
- **Ticket log-mass of a cell:** `R(n,S) = log₂(#words) − log₂|q|`; the cell's *word-unit* mass is
  `2^R = #words/|q|` — the uniform-residue expectation with each **word** (not necklace) as one
  trial of probability `1/|q|`. "Word units upper-bound necklace units" because `gcd(q, R_r)` is
  rotation-invariant (L-A1), so the necklace is the independent trial and the word count over-counts
  each necklace by its orbit size (≥ 1).
- **"Best north cell":** `R(n) = max over S of R(n,S)` restricted to `q > 0`, `S` ranging over
  `1 .. ⌊0.5849625·n⌋ + 3` (i.e. `K ≤ ⌊(β−1)n⌋ + 3 + n`, `β = log₂3` — cells up to ~3 bits past
  tuned; beyond this cap `q ≥ ~8·3^n` and the fixed point `R₀/q` drops below 1, the REQ-MATH-016
  "size artifact" region — the cap is the realizable-ticket domain, inherited from that entry, not
  re-derived in this script).
- **`ε_n`:** `K₀ − n·log₂3` with `K₀ = ⌊n·log₂3⌋ + 1` — the gap from `n·log₂3` up to the tuned
  (north) integer `K`. The "ingredient-inequality slack" is `min_{n ≤ 2000} ε_n · n^{μ−1}`,
  i.e. the factor by which the *actual* gap beats the floor `1/n^{μ−1}` that a measure
  `|log₂3 − K/n| ≥ 1/n^μ` (with `c = 1`) would guarantee. His committed value: `1.45e+01` at
  `n = 2`.
- **Where μ enters:** only in the bound line `−c_gen·n + (μ−1)·log₂n + C₀` and in the slack
  diagnostic; `C₀` is *defined* in the script as the exhibited maximum over `n ≤ 2000` of
  `Δ(n) = R_best(n) + c_gen·n − (μ−1)·log₂n` (committed: `−5.774` at `n = 2`) — it is measured,
  not derived from the source's constant `c`.
- **What the tail sums:** per scale `n`, `mass(n) = Σ_S #words/|q|` over the capped `S` range,
  **both shores**; "exact mass beyond N" = `Σ_{n>N} mass(n)` (computed to `n = 2000`); "provable
  bound beyond N" = `Σ_{n=N+1}^{2000} 2^{−c_gen·n + (μ−1)log₂n + C₀}` plus the analytic
  continuation `2^{bound(2000)}/(c_gen·ln 2)` for `n > 2000`. Committed values: beyond
  `n = 600` exact `3.414e−14`, bound `5.020e−04` (the entry's `< 5.2·10⁻⁴`).
- **Canaries (his):** `(n,K) = (5,8) → q = 13`, `(7,12) → q = 1909` (convergent-adjacent anchor
  cells); `n ≤ 14` word budgets with `S ≤ min(9, 2n)` (the REQ-MATH-022 census domain):
  north `6.17`, south `3.41`.

**Reading of the entry's logical structure, recorded for §3:** the *stated theorem* is a bound on
the **best north cell only**; the *consequence* (total both-shore mass) is the per-`n` bound applied
to `mass(n)`, which his script justifies **numerically on `n ≤ 2000`** (`bd ≥ ex` at seven cut
points), not by the two ingredients alone — the gap between "best cell ≤ bound" and "sum of ~1.17·n
cells over two shores ≤ same bound" is an elementary counting factor but it is not written out in
the entry or the script. See §3(a) for the repair and its cost (≈ `log₂ n` bits, absorbable).
