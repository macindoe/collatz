# Findings: L-A7 closure check — round-10 acceptance + margin-proof numerics (merle-la7-close-check)

Delegated session, 2026-07-26. Brief: `briefs/merle-la7-close-check-brief.md` (commit `2374bfe`).
Branch `merle-la7-close-check`, base commit **`2374bfe`** — launch note, for the record: the
worktree was cut at `b860fe8` (one commit behind the brief); the brief requires the branch base to
contain the brief, so the branch was created directly from `2374bfe` (present in the repository),
exactly the `merle-round8-coedit` precedent. Register: flat; discrepancies recorded, never disputed;
every replication number below is from this session's own code
(`experiments/merle_la7_close_check.py`, 66 checks, 0 failures, committed output alongside), not
from his scripts, which were read for operational definitions only and never run.

**No pushes anywhere; both Merle-side repos cloned read-only into the scratchpad; no web access
(the citations were adjudicated in round 9 and are not re-litigated here). Stopping-rule
compliance: replication of a correspondent's claims — no cycle search, no proof effort on the open
condition; the cycles front stays PARKED.**

The Lean statement-match (whether `marginTarget` etc. are faithfully encoded and kernel-clean) is
the sibling session `merle-lean-r10-audit`'s to adjudicate; nothing below labels the kernel claims
verified. This record covers numerics and algebra only.

## 1. The repos, the five blocks, and the artifacts

**Clones (read-only, scratchpad).** Shared repo `github.com/macindoe/one-obstruction-three-faces`,
HEAD **`826970e`** — exactly the expected commit (it is an L-A8 commit; the L-A7 blocks sit below
it). Merle's Lean repo `github.com/ericmerle3789/one-obstruction-three-faces-lean`, HEAD
**`5c9b663`** (the expected pin; the stack has moved past L-A7 into the L-A8/T1 material, the
sibling sessions' scope).

**Commit identification, one flat correction to the brief:** the five L-A7 shared-repo commits are
`9c14824`, `203aeb4`, `fa4acb5`, **`3797ecc`**, `bd16011`. The brief's fifth SHA `266f26b` does not
exist in the shared repo — it is the **Lean-repo stack commit** cited inside the key_core block
(the block's own header reads "stack `266f26b`"), and `3797ecc` is the shared-repo commit carrying
that block. All four Lean stack SHAs named in the blocks (`517ba89`, `f844467`, `266f26b`,
`b22fafc`) verified present in the Lean repo.

**The five blocks verbatim (LEDGER.md, diff `641a530..bd16011`; all additions his, plus one edit
inside the entry's Honest-scope paragraph).**

The Honest-scope edit (commit `9c14824`; strikethrough his):

> **Honest scope:** this bounds the *expectation*, not the truth — the model→certainty step remains the ×2×3 gap, unchanged. The bound is slack at small `n` (the transplanted exponent is worst-case). ~~crosses below one ticket near `n ≈ 550`~~ — **withdrawn (Merle, 2026-07-25): that figure was never computed, an unbacked estimate that should not have entered the entry; see the re-derivation below.** Sharper measures only improve `C₀`.

Block 1 (commit `9c14824`):

> **Merle acceptance and re-derivation (2026-07-25).** All four offer clauses accepted as stated; the re-sourcing is right and the flag was raised for exactly this reason.
>
> - *(Re-sourcing.)* Accepted: the ingredient is **Rhin 1987** (Progress in Mathematics 71, Proposition p. 160) with the Collatz-side precedent **Simons–de Weger 2005** (Acta Arith. 117, Lemma 12); the `5.125` line is withdrawn — it is Salikhov's measure of `ln 3`, and transplanting it to `log₂3` was an error on the Merle side, caught by the Macindoe re-check. The instrument stands; only its label changes. The re-sourced headline (`< 5.2·10⁻⁴` beyond `n ≈ 2233`, exact computation below, with the 2000→2233 strip a finite computation of the same kind) is adopted, together with the explicit `C₀ ≈ 2.06` and the measured `< 1.94` repair bits for the best-cell → both-shore step.
> - *(The `n ≈ 550` crossing — re-derived, and it was wrong.)* Re-computed from the exact `R_best(n)` data on the Merle side (`n ≤ 4000`, canary-anchored `(5,8) → 13`, `(7,12) → 1909`): under the entry's own constants the per-scale bound drops below one ticket at **`n = 372`** and the cumulative tail falls below one ticket at **`N = 440`** — **reproducing both Macindoe readings exactly**. The `550` matches neither and is withdrawn. Artifact: `experiments/test_REQ-MATH-035_croisement_un_ticket.py` (+ committed output).
> - *(Merle-side honesty item, volunteered.)* The `C₀` in the committed artifact is **exhibited from the exact data up to the computed range, not proved for all `n`** — so the statement as it stands is *verified to `N`*, not *proved for all `n`*. That is precisely the first of the two ingredients named: the for-all-`n` margin inequality `margin(n) ≥ c_gen·n`. Until it is written, "effectively finite at every scale" should read as conditional on it. The Macindoe offer to write that elementary proof is **accepted with thanks**; the south-side floor `ε′_n` for the both-shore step is likewise acknowledged as owed and unchecked in the Merle artifact.
>
> With the re-sourcing accepted and the crossing re-derived, the entry stands at **two keys**, scope as stated: an effective bound on the *expectation*, conditional on the named margin inequality, with the model→certainty step still the ×2×3 gap.

Block 2 (commit `203aeb4`):

> **Merle — the two named ingredients, addressed (2026-07-25, stack `517ba89`).**
>
> - *(South floor `ε′_n` — resolved, and it needs no new ingredient.)* North and south sit on opposite sides of the same real number: `ε_n = ⌈nL⌉ − nL` and `ε′_n = nL − ⌊nL⌋` satisfy **`ε_n + ε′_n = 1` identically**. Hence at most one of the two can be small: whichever it is, it is the distance to the *nearest* integer and is exactly what the Rhin/Simons–de Weger bound controls; the other is `≥ 1/2` for free. So the best-cell → both-shore step costs at most one bit beyond the single-shore bound, consistent with the measured `< 1.94` repair bits. Verified with 0 violations at every `n` tested including the convergent denominators (`n = 15601`: `ε = 2.6·10⁻⁵`, `ε′ = 0.999974`; `n = 190537`: `min = 9.3·10⁻⁸`). The debt is discharged without a new citation.
> - *(Margin inequality — verified exact, and the proof route validated but **tight**.)* `margin(n) − c_gen·n ≥ 0` re-verified in exact arithmetic (mpmath, `n ≤ 3000`): **minimum slack `2.8414` at `n = 2`**, 0 violations — reproducing the Macindoe figure `2.84`. On the proof itself, offered as de-risking before it is written: the natural route (`C(m,k) ≤ 2^{m·H(k/m)}`, `m = n+S−2`, `k = n−1`) **does dominate `c_gen·n` at every `n ≤ 200,000`** — the route works. **But it is tight and does not improve with scale:** the entropy-route margin stays in `[1.66, 2.10]` bits, minimum **`1.6647` at `n = 16266`**, and is asymptotically constant, because the gap between the true margin and the entropy bound tracks the `(1/2)·log₂ n` Stirling correction exactly (measured: `3.92` at `n = 100`, `8.91` at `n = 10⁵`, against `(1/2)log₂ n` = `3.32`, `8.30`). Practical consequence for the write-up: the Stirling term must be handled with an explicit bound rather than absorbed, since there are under two bits of room. Artifact: [`test_REQ-MATH-036`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/517ba89/experiments/test_REQ-MATH-036_dettes_nommees.py) (+ committed outputs, predictions written before measurement).

Block 3 (commit `fa4acb5`):

> **Merle — the margin inequality's analytic core, now kernel-friendly (2026-07-25, stack `f844467`).** Offered toward the ingredient Macindoe offered to write; the Stirling warning above was the reason to look for a route that avoids Stirling altogether.
>
> The entropy bound `C(m,k) ≤ 2^{m·h(k/m)}` is the *optimum* of the elementary family `C(m,k)·x^k ≤ (1+x)^m` (the left side is one term of the binomial expansion). Taking the **rational** `x = 12/7` — near the optimum `x* = 1/(log₂3 − 1) = 1.7095` — and clearing denominators removes real analysis entirely, and since **`19 = 12 + 7`** the statement becomes *one summand ≤ the sum*:
>
> > `deficit_term_le (m k : ℕ) (h : k ≤ m) : 12^k * 7^(m−k) * C(m,k) ≤ 19^m`
>
> [`OneObstruction/DeficitLemma.lean`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/f844467/OneObstruction/DeficitLemma.lean) — **kernel-3, 0 sorry, no user axioms, no `native_decide`**, committed `#print axioms`, five non-vacuity canaries (two of them instantiate the theorem rather than restate it). Numerics established *before* formalizing (REQ-MATH-039/040, canary-anchored, committed): the resulting asymptotic constant is `0.0793165`, within `2.1·10⁻⁶` of `c_gen` — the rational choice costs essentially nothing; with the safe rational `c = 1/13`, `margin(n) ≥ n/13` holds for `n = 1..3000` with **0 failures and minimum slack 1.700 bits**; the integer target `C(K−2,n−1)^13·2^n ≤ 2^{13K}` holds for `n = 1..1200`, 0 failures, and the binomial route implies it with ≥ 22 bits to spare. A negative control is included: `c = 2/25 = 0.08 > c_gen` fails at 241 scales, as it must.
>
> **Honest scope.** What is proved in Lean is the analytic heart. The remaining step — from `deficit_term_le` to the `n`-indexed margin statement — is the comparison of `K` with `n` (`3^n ≤ 2^K < 2·3^n`); it is stated in the file as `MarginTarget` and is **not yet proved**, deliberately left explicit rather than absorbed. It is a finite rational-exponent comparison, not an analytic obstacle. Provenance: the deficit is Merle's own earlier result (Junction Theorem preprint §3, entropy form, constant `γ` with `γ·log₂3 = c_gen` exactly — REQ-MATH-037); this entry contributes the elementary re-derivation and the kernel artifact. If the Macindoe-side proof is written independently, two proofs of the same inequality is the currency this ledger runs on.

Block 4 (commit `3797ecc`):

> **Merle — assembly heart proved (2026-07-25, stack `266f26b`).** Following the Stirling warning, the route now avoids real analysis entirely. Reparametrising `m = k+j`, `n = k+1`, `K = k+j+2` removes every natural subtraction, and the Diophantine hypothesis plus the whole `j`-dependence concentrate into one lemma:
>
> > `key_core (k j) (hub : 2^(k+j+2) ≤ 2·3^(k+1)) : 2^(86(k+j+2))·2^(15(k+1))·7^(195k) ≤ 2^562·12^(195k)`
>
> Proof: `hub` to the 86th power; `atom_a` on the per-`k` factor; `atom_D` on the constant. The admissible window for the exponent ratio is `[5.727444, 5.747075]` (width `0.0196`) and `s = 15, t = 86` is the smallest admissible pair — `atom_A` and `atom_a` hold with `0.088` and `0.327` bits to spare, exact. Six theorems in [`DeficitLemma.lean`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/266f26b/OneObstruction/DeficitLemma.lean), **all kernel-3, 0 `sorry`, no user axioms, no `native_decide`**, committed axiom log.
>
> **Remaining, stated exactly:** the bookkeeping from `key_core` + `deficit_term_le` to the `n`-indexed `MarginTarget` — exponent arithmetic only, no new mathematical content — verified in exact integers (REQ-MATH-042, full chain step by step, `n = 1..300`, 0 failures; the implication `(3) ⟹ (2)` tested separately, 0 violations), not yet formalised. Two Merle-side errors were caught by the machine during this round and are recorded in the artifacts rather than smoothed: a missing `/log₂3` in the first window computation (which proposed an inadmissible `s = 1, t = 6`, refuted by the exact integer check), and a `norm_num` failure on a 71-digit constant (replaced by the soft chain `3^86 ≤ 4^86 = 2^172`).

Block 5 (commit `bd16011`):

> **Merle — the margin inequality is PROVED (2026-07-25, stack `b22fafc`).** The debt named in this entry is discharged on the Merle side, at kernel level.
>
> > `marginTarget (n K) (1 ≤ n) (3^n ≤ 2^K) (2^K < 2·3^n) : C(K−2, n−1)^13 · 2^n ≤ 2^(13K)`
>
> Chain, all in ℕ, no real analysis anywhere: `deficit_term_le` (one summand of `(12+7)^m`) → atoms `A`/`a`/`D` → `key_core` (absorbs the Diophantine hypothesis and the entire `j`-dependence) → `key_shifted` → `key15` → `margin_core` (the `k,j` form, free of natural subtraction) → `marginTarget`. **Ten theorems in [`DeficitLemma.lean`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/b22fafc/OneObstruction/DeficitLemma.lean), every one kernel-3 (`propext`, `Classical.choice`, `Quot.sound`), 0 `sorry`, no user axioms, no `native_decide`**, with the committed axiom log.
>
> **Honest, and it matters for this entry's numbers.** What is *proved* is the inequality with the rational constant `1/13 = 0.0769231`, about 3% below the asymptotic `c_gen = 0.0793186`; `c_gen` itself remains an asymptotic value, not a Lean theorem. Recomputing this entry's thresholds under the **proved** constant (REQ-MATH-043, same Rhin exponent): per-scale crossing `1596 → 1655`, cumulative-tail crossing `1661 → 1722`. The qualitative statement is unchanged — the ticket mass is effectively finite at every scale, and now the margin step is no longer conditional. The remaining ingredient of this entry is therefore only the published Diophantine input (Rhin 1987 / Simons–de Weger 2005), not an unproved lemma of ours.
>
> The Macindoe offer to write this proof independently stands and is still welcome: two proofs of the same inequality — one entropic, one elementary — is the currency this ledger runs on, and the entropic route (with the Stirling caution recorded above) is the one that connects to the published Junction-Theorem form.

**Artifact inventory (Lean repo `experiments/`, read for operational definitions only):**
`test_REQ-MATH-035_croisement_un_ticket.py` + OUT (the 372/440 re-derivation; his L1 = per-scale
crossing with a 50-window rule, L2 = cumulative tail < 1, `R_best` on `n ≤ 4000`, `C₀` exhibited
per exponent), `test_REQ-MATH-036_dettes_nommees.py` + OUT + OUT-036b (south floor + margin +
entropy route to 200k), `test_REQ-MATH-037_junction_gamma_is_cgen.py` + OUT (γ identity, dps 50),
`test_REQ-MATH-039_x_rationnel.py` + OUT (rational-x constants; the negative control lives here,
run at `x = 1709/1000`), `test_REQ-MATH-040_chaine_entiere.py` + OUT (integer target + route,
`n ≤ 1200`), `test_REQ-MATH-041_route_entiere_margin.py` + OUT (the window derivation — the
in-code comment "CORRIGE : diviser par log2(3)" is the recorded error-catch #1 — and the
`s = 15, t = 86` search), `test_REQ-MATH-042_chaine_assemblage.py` + OUT (atoms + full chain
`n ≤ 300` + the (3)⟹(2) red-team). **Flag: `OUT_REQ-MATH-043.txt` (the threshold recompute) is
committed at `b22fafc` with NO generator script** — the only artifact of the five blocks without
one; its method is identifiable as REQ-MATH-035's `analyse()` run at exponent 13.3 under both
constants (our replication below reproduces all six of its numbers from that reading).

## 2. Replication (`experiments/merle_la7_close_check.py`, committed output; 66 checks, 0 failures)

Fresh code; canaries printed first; exact integers for every `q`, word count, and assembly
inequality; `mpmath` at stated dps (40–80) for the ε scan, the γ identity, and dps-40 slack
counts; float paths carry printed error bounds with every decision ≥ 10¹⁰ × the accumulated error
(the tightest: the L1 crossing margins `|f| ≈ 0.026–0.056` vs `1e-9` float error; the ε decision
at `9.3·10⁻⁸` carried with ~50 guard digits). His scripts were never run.

| # | claim (his committed figure) | ours | verdict |
|---|---|---|---|
| (a) | per-scale crossing 372 / cumulative 440, entry constants; "reproducing both Macindoe readings exactly" | `C₀ = −5.774`, L1 = **372**, L2 = **440**; tail(>600) = 5.020e−4 | match (and matches our round-9 372/440) |
| (b) | `ε + ε′ = 1` identically; ≤ 1 shore small | one-line proof recorded below; 0 violations, `n ≤ 200,000` | match, and the identity is proved |
| (b) | `n = 15601`: `ε = 2.6·10⁻⁵`, `ε′ = 0.999974` | `2.625·10⁻⁵` / `0.99997375` | match |
| (b) | `n = 190537`: min `9.3·10⁻⁸` | `9.306·10⁻⁸`; also the scan minimum over all `n ≤ 200,000`, at exactly `n = 190537` | match |
| (c) | margin slack min `2.8414` at `n = 2` (`n ≤ 3000`), 0 violations | `2.84136` at `n = 2`, 0 violations | match |
| (c) | entropy route dominates to `n = 200,000`, 0 violations | 0 violations, full range achieved | match |
| (c) | route margin in `[1.66, 2.10]`, min `1.6647` at `n = 16266` | min `1.66469` at `n = 16266`; max `2.10492` at `n = 190537` (inside his interval at 2-dp rounding) | match |
| (c) | gap tracks `(1/2)log₂n`: 3.92/3.32 at 100, 8.91/8.30 at 10⁵ | 3.9246/3.3219, 8.9115/8.3048 | match |
| (d) | `γ·log₂3 = c_gen`, error 0.0 at fifty digits | difference `3.95·10⁻⁸²` at 80 digits; dps-50 difference 0.0, as committed | match — and an **exact identity** (§3) |
| (e) | asymptotic constant of `x = 12/7` = `0.0793165`, loss `2.1·10⁻⁶` | `0.07931654247`, loss `2.0703·10⁻⁶` | match |
| (e) | `x* = 1/(log₂3−1) = 1.7095` recovers `c_gen` at the optimum | `c(x*) − c_gen = 1.34·10⁻⁵¹`; symbolic recovery exact (§3); `c′(x*) = 0` | match, exact |
| (f) | window `[5.727444, 5.747075]`, width 0.0196 | `[5.7274437, 5.7470751]`, width 0.019631; derivation re-found (below) | match |
| (f) | `s = 15, t = 86` smallest admissible | exhausted `s = 1..14` in exact integers: every window empty (`t_A = t_a + 1` at every `s`); `s = 15` → `t ∈ [86, 86]` exactly | match |
| (f) | atom margins 0.088 / 0.327 bits | 0.0883 / 0.3267 (exact-integer atoms hold; atom D margin 324.7 bits) | match |
| (f) | `key_core` inequality | exact for all 1,137 hub-admissible `(k, j)`, `k ≤ 60`; fails for `j` past the hub (first at `(0,5)`) — the hypothesis is load-bearing | match |
| (f) | error-catch 1: uncorrected window admits `s = 1, t = 6`, refuted exactly | uncorrected upper bound 9.1089 admits it; atom a fails exactly: `141264177173406 > 106993205379072` | confirmed |
| (f) | error-catch 2: `3^86 ≤ 4^86 = 2^172` sufficient where used | trivially true, exact; sufficient for `atom_D` (`101 + 172 = 273 ≤ 562`) | confirmed |
| (g) | `margin(n) ≥ n/13`, `n = 1..3000`, min slack 1.700 | route bound: 0 failures, min `1.7003` at `n = 12` (the binding quantity — his P3); true margin a fortiori (its min-vs-`n/13` is 1.923 at `n = 1`) | match |
| (g) | integer target `n = 1..1200`, 0 failures; route implies with ≥ 22 bits | 0/0 failures; bit-margins min (25, n=1) target, (22, n=7) route | match |
| (g) | negative control `c = 2/25` fails at 241 scales | **241** failures at `x = 1709/1000` (his artifact's x, range `n = 1..3000`), min slack −0.3566 at `n = 2978`, first eight scales identical; at `x = 12/7` it is **256** failures — the ledger sentence inherits the artifact's `x`, a scope detail worth one clause | match (with the x-scope noted) |
| (h) | thresholds `1596 → 1655` per-scale, `1661 → 1722` cumulative | Rhin×`c_gen`: `C₀ = −14.949`, 1596/1661, tail(>600) 3.863e19; Rhin×`1/13`: `C₀ = −14.954`, 1655/1722, tail 1.096e20 — all six OUT-043 numbers | match |
| (h) | reconcile with our `n ≈ 2233` headline | reproduced 2233 from the theorem-form bound (below) | reconciled, no contradiction |

**(b) The one-line proof, recorded.** For irrational `x`, `x ∉ ℤ`, so `⌈x⌉ = ⌊x⌋ + 1`; hence
`ε + ε′ = (⌈x⌉ − x) + (x − ⌊x⌋) = ⌈x⌉ − ⌊x⌋ = 1`. `nL` is irrational for every `n ≥ 1`
(`L = log₂3` irrational), so `ε_n + ε′_n = 1` identically; therefore
`min ≤ 1/2 ≤ max` and "both shores < 1/2" is impossible. His claim is a theorem, not a numeric.
Scan extras: max of `min(ε, ε′)` over `n ≤ 200,000` is 0.499997 at `n = 55601`.

**(c) One near-tie, recorded flat.** His REQ-036 prints route minimum `1.6647` at `n = 1995`
(sweep to 3000) and REQ-036b prints `1.6647` at `n = 16266` (sweep to 200,000) — not a
contradiction: our replication gives `1.66469` at both, a genuine near-tie at 5 decimals with
`n = 16266` the true global argmin. The ledger carries only the 16266 figure, which is correct.

**(f) The window, re-derived from its constraints** (operational source: REQ-MATH-041 header +
the atom statements; recorded per the brief): scaling the 13th-power route by `s` and absorbing
`19^{13s}` by a power of 2 requires
- `(A_{s,t})`: `19^{13s} ≤ 14^{13s}·2^t` ⟺ `t ≥ 13s·log₂(19/14)`, and
- `(a_{s,t})`: `3^t·2^s·7^{13s} ≤ 12^{13s}` ⟺ `t·log₂3 + s ≤ 13s·log₂(12/7)` ⟺
  `t ≤ s·(13·log₂(12/7) − 1)/log₂3`,

so `t/s ∈ [13·log₂(19/14), (13·log₂(12/7) − 1)/log₂3] = [5.727444, 5.747075]`. Forgetting the
`/log₂3` (error-catch 1) inflates the upper bound to `9.1089` and admits `s = 1, t = 6`, which
the exact integer check kills on the `a` side. The interval's width `0.0196` times `s` first
reaches an integer at `s = 15` (`t = 86`, uniquely), confirmed by exact exhaustion.
`key_core`'s constant: hub⁸⁶ gives `2^{86(k+j+2)} ≤ 2^{86}·3^{86(k+1)}`; regrouping per `k` uses
`atom_a`ᵏ on `(3^{86}·2^{15}·7^{195})^k ≤ 12^{195k}` and `atom_D` (`2^{101}·3^{86} ≤ 2^{562}`)
on the constant — which is where the `2^{562}` and the `3^{86} ≤ 2^{172}` replacement live.

**(h) The reconciliation, so the entry can never confuse the two families of numbers.**
- **1596 / 1655 (per-scale) and 1661 / 1722 (cumulative)** are *one-ticket crossings of the
  per-scale best-north-cell bound* `f(n) = −c·n + 13.3·log₂n + C₀` with `C₀` **exhibited** (the
  max of the residual over the computed `n ≤ 4000` — an empirical fit, `−14.949` under `c_gen`,
  `−14.954` under the proved `1/13`), his REQ-MATH-035/043 method. L1 = first `n` past the peak
  with `f < 0`; L2 = first `n` with `Σ_{m>n} 2^{f(m)} < 1`.
- **`n ≈ 2233`** (our round-9 headline, adopted by him in block 1) is the smallest `N` such that
  the **theorem-form** bound — `C₀ = 1 − 2·log₂ln2 = 2.06` derived from the ingredients (not
  fitted), exponent `13.3` on `log₂K₀` (the per-`n` Rhin form), **plus 3 repair bits** for the
  best-cell → both-shore-mass step — gives *provable both-shore tail mass* `< 5.2·10⁻⁴` (the
  entry's headline number, not "< 1 ticket"). Reproduced exactly: min `N` = 2233.
- Different constants (fitted vs derived), different exponent carrier (`log₂n` vs `log₂K₀`),
  different target (< 1 ticket vs tail < 5.2·10⁻⁴). Both computations are right; neither
  supersedes the other; the exhibited-`C₀` figures are *descriptions of the computed data*, the
  2233 is the *provable-for-all-`n` label*. Under exhibited constants the Rhin tail beyond 600 is
  vacuous (3.9e19 / 1.1e20 — his OUT-043's own numbers, reproduced), which is exactly why the
  provable headline lives at 2233, not 600.

## 3. The γ identity: exact, with the symbolic derivation

`γ = 1 − h(1/log₂3)` (Junction) and `c_gen = β(1 − H(1/β))`, `β = log₂3` (the round-8 (B)
derivation, `briefs/merle-round8-coedit-findings.md` part A). Expand the binary entropy at
`x = 1/β`:

`H(1/β) = (1/β)·log₂β − ((β−1)/β)·log₂((β−1)/β) = log₂β − ((β−1)/β)·log₂(β−1)`,

so `β(1 − H(1/β)) = β − β·log₂β + (β−1)·log₂(β−1)` — precisely the closed form of `c_gen`.
Since `γ = 1 − H(1/β)`, **`γ·β = c_gen` is an exact algebraic identity**, not a numerical
coincidence; every step above is asserted in the script at 80 digits (residuals < 1e−75), and the
50-digit difference is 0.0 exactly as his REQ-MATH-037 committed. The same expansion proves the
(e) recovery: `c(x) = β − β·log₂(1+x) + log₂x` is maximized at `x* = 1/(β−1)` (where
`1 + x* = β/(β−1)`), and `c(x*)` collapses to the same closed form — the rational `12/7` route's
`x*` and the Junction `γ` are two views of one optimum. One naming clash recorded flat, not
disputed: REQ-MATH-037's comment converts "per unit `S`" to "per unit `n`" via `S ~ n·log₂3` —
in *our* conventions `S/n → β − 1` and it is `K/n → β`; the conversion factor `β` is consistent
with the Junction preprint's "S" denoting our `K`. The preprint itself is not in either repo and
was not fetched (no web access this session); the identity itself is exact regardless.

## 4. Key recommendation and offered co-edit content

**L-A7's two-keys standing is CONFIRMED.** Our round-9 key status was "two keys upon his
acceptance of a re-sourcing"; block 1 accepts all four offer clauses verbatim (Rhin/Simons–de
Weger, the `n ≈ 2233` headline, `C₀ ≈ 2.06`, the `< 1.94` repair bits), withdraws the `≈ 550`
crossing with the honest "never computed", and re-derives 372/440 — which this session confirms
digit-exact from its own chain. The stated condition is satisfied; the DRAFT conditional can be
date-stamped and the entry marked two keys, mirroring the L-A5 pattern.

**The NEW margin-proof blocks (2–5) are now verified our side on numerics and algebra —
everything checked, everything matched** (the table in §2; 66/66). Beyond replication, three
items are upgrades or scope notes to offer, none a dispute:

1. *(upgrade)* The south floor and the γ identity are **theorems, not numerics**: the one-line
   `ε + ε′ = 1` proof (§2(b)) and the symbolic `γ·β = c_gen` derivation (§3) can be stated as
   such in the entry — his "verified with 0 violations" and "error 0.0 at fifty digits"
   undersell what he has.
2. *(scope clause)* The negative-control sentence "fails at 241 scales" inherits its artifact's
   `x = 1709/1000` (his P3bis); at the entry's own `x = 12/7` the count is 256 (range
   `n = 1..3000` either way). One clause pins it.
3. *(scope clause)* "margin(n) ≥ n/13 … minimum slack 1.700 bits" — the 1.700 is the slack of
   the *provable route bound* (which is what matters for the proof); the true margin's slack
   against `n/13` is larger. One clause.

**Recommended co-edit shape** (drafting is the main session's/a later session's call; content per
this record): (i) date-stamp the satisfied round-9 conditional and mark L-A7 **two keys, scoped**
— scope: the bound on the expectation, now with the margin step proved at constant `1/13` subject
to the sibling session's Lean statement-match, the published Diophantine input the entry's one
remaining external ingredient; (ii) a Macindoe verification record for blocks 2–5 (this session's
figures, replication stated digit-exact); (iii) offers 1–3 above as offers inside the entry;
(iv) one flat line that OUT-REQ-MATH-043 lacks a committed generator script (its six numbers all
reproduce from the REQ-035 method — the offer is that he commit the script, not that anything is
in doubt). **This recommendation covers numerics and algebra only: the `marginTarget` kernel
claim (statements faithfully encoding the mathematics, axiom hygiene) is the sibling
`merle-lean-r10-audit`'s to adjudicate, and any key language touching "PROVED at kernel" should
wait on that session's verdict.**

## Flags, collected

1. Brief typo, resolved: the fifth shared-repo L-A7 commit is `3797ecc`; the brief's `266f26b` is
   the Lean stack SHA cited inside that block. All four Lean stack SHAs verified present.
2. `OUT_REQ-MATH-043.txt` committed with no generator script (unique among the five blocks'
   artifacts); all six of its numbers reproduce from the REQ-035 method — co-edit offer, not a
   doubt.
3. The negative control's 241 is `x = 1709/1000`-specific (256 at `x = 12/7`); the "1.700 bits"
   slack is the route bound's, not the true margin's. Scope clauses offered (§4).
4. Route-margin near-tie: 1.66469 at `n = 1995` and at `n = 16266` (true argmin 16266, as the
   ledger states); his two artifacts print the same 4-dp value at different `n` — consistent,
   recorded so nobody reads it as a discrepancy later.
5. The route-margin maximum over `n ≤ 200,000` is `2.10492` at `n = 190537` — inside his
   `[1.66, 2.10]` only at 2-dp rounding; and both extremes of the route margin sit AT convergent
   denominators (16266 near one, 190537 one), consistent with the Stirling-tracking mechanism.
6. REQ-MATH-037's `S ~ n·log₂3` unit conversion implies the Junction preprint's "S" is our `K`
   (naming clash with our `S = K − n`); the preprint is outside both repos and was not fetched.
   The identity itself is exact and does not depend on this.
7. The `[1.66, 2.10]` interval, the 1596/1655/1661/1722 thresholds, and the exhibited `C₀`s are
   all descriptions of computed data (fits/observations), not theorem-grade constants — the
   entry's own text is honest about this; the reconciliation in §2(h) pins the definitions so the
   exhibited and theorem-form numbers can never be conflated.
8. No pushes anywhere; clones read-only in the scratchpad; no web access; no reply paragraphs, no
   key turns, no co-edit commits made — recommendation only, per the brief. Cycles front PARKED
   throughout.
