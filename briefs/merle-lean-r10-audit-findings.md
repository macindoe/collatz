# Findings: round-10 Lean statement-match audit — DeficitLemma + T1Structure (merle-lean-r10-audit)

Delegated session, 2026-07-26. Brief: `briefs/merle-lean-r10-audit-brief.md`.
Branch `merle-lean-r10-audit`, base commit **`2374bfe`** (the brief commit; the
worktree was cut at `b860fe8` and fast-forwarded to `2374bfe` before branching,
so the base contains the brief — condition satisfied).
Register: flat; statements recorded verbatim; mismatches recorded, never
disputed in prose. Verification code: `experiments/merle_lean_r10_audit.py`
(fresh code, imports nothing from any Merle repository, runs none of his
scripts; every inequality decision in exact integer arithmetic; the convergent
computation at two Decimal precisions, 150 and 250 digits, with a stability
assertion) — **15,930 exact checks, 0 failures**, committed output alongside.
No pushes anywhere; both clones read-only in the scratchpad; no web access
beyond the two read-only `git clone`s; no Lean toolchain installed.

**Trust boundary, stated plainly.** This is a **read-not-built** audit. What is
verified here: (1) the Lean *statements* say what the ledger says they say;
(2) the committed axiom logs match the ledger's axiom claims; (3) every
statement, instantiated at hundreds to thousands of exact-integer points
including edges, is *true as stated* (a false statement would have been caught
without a kernel); (4) the one genuinely finite ingredient — the `convPairs`
list — is independently recomputed and confirmed. What is NOT verified here:
that the proofs compile and the kernel accepts them. The kernel-3 /
`[propext]` / no-axioms claims rest on his committed logs and his (now
four-way-hardened) verification protocol — the same posture as the
ContentDescent and L-A1 precedents (`briefs/merle-la5-closure-findings.md`).

## Item 1 — Lean repo, read-only

Fresh clone (2026-07-26): `main` = **`5c9b663`**
(`5c9b66392a157ce63c34f765e18e05723d870ddf`) — exactly the expected HEAD; not
moved. **The graph `97b57d7 → 5c9b663` is linear** (each commit the sole parent
of the next), 20 commits, all authored 2026-07-25 CEST:

`97b57d7` → `9096d7f` (REQ-035: the ≈550 crossing withdrawn, 372/440 reproduced)
→ `517ba89` (REQ-036: south floor ε+ε′=1; margin route tight) → `a163c8c`
(REQ-037: γ·log₂3 = c_gen) → **`f844467`** (DeficitLemma.lean: deficit_term_le)
→ **`9521b16`** (atoms, s=15/t=86) → **`266f26b`** (key_core) → **`b22fafc`**
(marginTarget PROVED) → `6d8beb9` → `f2b9e5b` → `69d9cf6` → `1b06a99` →
`4cedbff` (REQ-044..051, exploratory, not this audit's scope) → **`41fa4f8`**
(T1Structure.lean: ceiling half) → **`81054ea`** (seam_bound) → **`89d9efc`**
(seam_gap_at_barina) → **`dac39a3`** (analytic bridge) → **`da2c8db`** (Legendre
step claimed — later retracted) → **`7d46474`** (RETRACTION of da2c8db) →
**`4856058`** (Legendre step proved, second attempt, threshold abstract) →
**`5c9b663`** (discharge_all). Both claimed stacks match the brief exactly.

**Drift check — no drift.** `git diff` against the previously audited SHAs is
empty for all three files: `ContentDescent.lean` unchanged since `67c428a`,
`ContentSeparation.lean` unchanged since `905d75b`, `TransportRecurrence.lean`
unchanged since `7d3d44a` (the L-A1 artifact commit). `LegendreApprox.lean`
entered at `da2c8db` (the retracted commit) and is byte-unchanged since — the
retraction was of a theorem *using* it, not of the file.

## Item 2 — DeficitLemma.lean statement match

### The ten theorems, verbatim (file at `5c9b663`, namespace `DeficitLemma`)

1. `theorem deficit_term_le (m k : ℕ) (h : k ≤ m) : 12 ^ k * 7 ^ (m - k) * (m.choose k) ≤ 19 ^ m`
2. `theorem deficit_choose_le (m k : ℕ) (h : k ≤ m) : (m.choose k) * (12 ^ k * 7 ^ (m - k)) ≤ 19 ^ m`
3. `theorem atom_A : (19 : ℕ) ^ 195 ≤ 14 ^ 195 * 2 ^ 86`
4. `theorem atom_a : (3 : ℕ) ^ 86 * 2 ^ 15 * 7 ^ 195 ≤ 12 ^ 195`
5. `theorem atom_D : (2 : ℕ) ^ 101 * 3 ^ 86 ≤ 2 ^ 562`
6. `theorem key_core (k j : ℕ) (hub : (2:ℕ) ^ (k + j + 2) ≤ 2 * 3 ^ (k + 1)) : 2 ^ (86 * (k + j + 2)) * 2 ^ (15 * (k + 1)) * 7 ^ (195 * k) ≤ 2 ^ 562 * 12 ^ (195 * k)`
7. `theorem key_shifted (k j : ℕ) (hub : …same…) : 2 ^ (86 * (k + j)) * 2 ^ (15 * (k + 1)) * 7 ^ (195 * k) ≤ 2 ^ 390 * 12 ^ (195 * k)`
8. `theorem key15 (k j : ℕ) (hub : …same…) : 19 ^ (195 * (k + j)) * 2 ^ (15 * (k + 1)) ≤ 2 ^ (195 * (k + j + 2)) * (12 ^ (195 * k) * 7 ^ (195 * j))`
9. `theorem margin_core (k j : ℕ) (hub : …same…) : ((k + j).choose k) ^ 13 * 2 ^ (k + 1) ≤ 2 ^ (13 * (k + j + 2))`
10. `theorem marginTarget (n K : ℕ) (hn : 1 ≤ n) (hlb : 3 ^ n ≤ 2 ^ K) (hub : 2 ^ K < 2 * 3 ^ n) : ((K - 2).choose (n - 1)) ^ 13 * 2 ^ n ≤ 2 ^ (13 * K)`

Plus five `example` canaries (three of which — 1, 4, 5 — instantiate
`deficit_term_le`; the ledger says "two of them instantiate the theorem", a
trivially conservative count). Checks by read: **0 `sorry`, 0 `native_decide`,
no `axiom` declarations, single `import Mathlib`.**

### Per-theorem match vs the ledger prose (L-A7 addenda, LEDGER.md at `826970e`)

| Ledger claim | Lean statement | Match |
|---|---|---|
| `deficit_term_le (m k) (k ≤ m) : 12^k·7^(m−k)·C(m,k) ≤ 19^m` (quoted verbatim in the entry) | statement 1 | **Exact** — verbatim |
| one summand of `(12+7)^m`; canary-instantiated | proof is `Finset.single_le_sum` after `19 = 12+7`; canaries present | **Exact** |
| `key_core (hub : 2^(k+j+2) ≤ 2·3^(k+1)) : 2^(86(k+j+2))·2^(15(k+1))·7^(195k) ≤ 2^562·12^(195k)` (quoted verbatim) | statement 6 | **Exact** — verbatim |
| atoms with margins 0.088 / 0.327 / ≈325 bits; window `[5.727444, 5.747075]`, `s=15,t=86` smallest | statements 3–5; margins recomputed this session: **0.088 / 0.327 / 324.693 bits** | **Exact** (window endpoints are REQ-041's computation, read not re-derived) |
| `marginTarget (n K) (1 ≤ n) (3^n ≤ 2^K) (2^K < 2·3^n) : C(K−2, n−1)^13 · 2^n ≤ 2^(13K)` (quoted verbatim) | statement 10 | **Exact** — verbatim |
| chain `deficit_term_le → atoms A/a/D → key_core → key_shifted → key15 → margin_core → marginTarget` | file order and proof dependencies as read | **Exact** |
| "Ten theorems, every one kernel-3, committed axiom log" | ten theorems ✓; log covers **8 of 10** (below) | **Partial — see axiom-log flag** |

### The load-bearing question: does `marginTarget` encode `margin(n) ≥ n/13`?

**Verdict: YES — exactly, at the tuned north cell, with the two gaps below
stated.** The unfolding, written out:

Taking `log₂` of the conclusion `C(K−2, n−1)^13 · 2^n ≤ 2^(13K)`:

  `13·log₂ C(K−2, n−1) + n ≤ 13K`  ⟺  `K − log₂ C(K−2, n−1) ≥ n/13`.

- **`C(K−2, n−1)` is OUR word count, exactly.** The L-A7 operational definition
  (la7 findings §1) counts words of the general family at cell `(n, S)`,
  `K = n + S`, as `C(n+S−2, n−1)` — the Vandermonde closed form of the
  sum-over-letter-counts `Σ_r C(n−1, r−1)·C(S−1, r−1)`. Verified exactly at all
  144 cells `n, S ≤ 12` this session: the summed composition count equals
  `C(K−2, n−1)` — no compositions-vs-binomial gap. The formula is
  shore-independent (it counts words at a cell; the shore is the sign of `q`).
- **`K` is the cell's capacity exponent, and `margin(n) = K − log₂ #words` is
  exactly the quantity the L-A7 entry consumes** (la7 findings §3(a) step 2:
  `log₂ #words = K₀ − margin(n) ≤ K₀ − c·n`). `K` is *not* `log₂ q` — the
  entry's `R(n)` uses `log₂ q`, which the derivation lower-bounds separately
  via the Diophantine floor (step 1). `marginTarget` is ingredient (ii) of the
  la7 findings — the counting half — and only that.
- **The `K`-range covers exactly the tuned north cell, and nothing else.**
  `3^n ≤ 2^K < 2·3^n` ⟺ `K = ⌈n·log₂3⌉ = K₀`: verified this session that the
  hypothesis admits **exactly one** `K` per `n` (n = 1..300, uniqueness checked
  against `K₀ ± 1`), equal to `bitlength(3^n)`, the tuned north `K₀`. The
  conclusion instantiated at every one in exact integers: holds. Outside the
  range it can genuinely fail — at `(n, K) = (100, 200)` (which violates
  `2^K < 2·3^n`) the conclusion is **false** — so the hypotheses are
  load-bearing, not decorative.

**The two gaps, stated exactly (the audit's product):**

1. **Constant:** the proved constant is `1/13 = 0.0769231`, 3.0% below the
   asymptotic `c_gen = 0.0793186`. His own block states this and recomputes the
   L-A7 thresholds under the proved constant (REQ-MATH-043: per-scale crossing
   `1596 → 1655`, cumulative `1661 → 1722`) — honest as written. `c_gen` itself
   remains an asymptotic value, not a Lean theorem.
2. **Coverage:** `marginTarget` bounds the word count at the **tuned north cell
   only**. The south shore (`2^K < 3^n`) and the above-tuned north cells
   (`2^K ≥ 2·3^n`) are outside its hypothesis range. Those cells are handled in
   the L-A7 accounting by the best-cell → both-shore repair (la7 findings
   §3(a)(iii): `|q| ≥ 3^n` above tuned, geometric decay + the south floor
   `ε′_n` south — now his `ε + ε′ = 1` observation at stack `517ba89`), **not
   by this theorem**. Within its scope the theorem is complete: for every
   `n ≥ 1` it covers the one cell the margin inequality is about. (At `n = 1`
   the tuned cell is the spent-stock `q = 1` cell, excluded from the L-A7 cell
   domain; `marginTarget` includes it anyway — a harmless superset.)

So: the L-A7 entry's "the margin step is no longer conditional" is accurate
**at the proved constant `1/13`**, for the tuned-cell margin inequality; the
best-cell → both-shore step and the Diophantine ingredient remain exactly where
the ledger says they are.

**One slack-figure reconciliation, flat (not a discrepancy of substance):** the
entry and file header say "minimum slack 1.700 bits at n = 12". The *true*
margin slack `margin(n) − n/13` has its minimum at `n = 1` (1.923 bits; 2.85 at
`n = 2`). His 1.700 figure is the slack of the **route-implied** bound
(`deficit_term_le` ⟹ `log₂C ≤ m·log₂19 − k·log₂12 − (m−k)·log₂7`) over `n/13`
— reproduced this session **digit-exact: min 1.700 bits at n = 12** (n ≤ 3000).
Same number, different (and for the proof, the right) quantity; the prose does
not say which. Recorded only so the next reader doesn't re-derive the mismatch.

**Stale header comment, flat:** the file's SCOPE header (lines 25–30, written
at `f844467`/`266f26b`) still says "What remains outside Lean is pure exponent
bookkeeping from `key_core` + `deficit_term_le` to the `n`-indexed statement
`MarginTarget`" — but `marginTarget` **is proved in the same file** (line 229,
added at `b22fafc`). The header was not updated when the debt was discharged.
The ledger's own later block (stack `b22fafc`) states the current truth
correctly; only the file header lags. Co-edit candidate, one sentence.

### Canaries (fresh Python, exact integers)

`deficit_term_le`: 399 instances (exhaustive `m ≤ 25` all `k`, including
`k = 0` and `k = m`; 40 random to `m = 400`; forced edges at `m = 50..400`) —
all hold. Atoms: exact, margins as above. `key_core`/`key_shifted`/`key15`: all
hub-valid `(k, j)` for `k ≤ 12` (60 each); `margin_core`: all hub-valid pairs
for `k ≤ 40` (524) — all hold; `key15` genuinely **fails** just outside `hub`
(first at `(k, j) = (0, 5)`), so the Diophantine hypothesis is load-bearing.
`marginTarget`: n = 1..300 at the unique admissible `K` (edge `n = 1`
included) — all hold. **0 failures anywhere.**

### Axiom log — `experiments/DeficitLemma_axioms.txt`

Header claims "10 theorems, all kernel-3". The log body records **8** theorems,
each with exactly `[propext, Classical.choice, Quot.sound]`:
`deficit_term_le`, `deficit_choose_le`, `atom_A`, `atom_a`, `atom_D`,
`key_core`, `margin_core`, `marginTarget`. **`key_shifted` and `key15` have no
`#print axioms` probe in the file and no line in the log** — the file's probes
(lines 75–76, 143–146, 242–243) cover only the 8. Flat: the two missing
theorems are intermediate steps of `margin_core`, whose own probe transitively
bounds their axioms, so nothing mathematical hangs on it — but the log as
committed does not cover all ten, and his hardened protocol's fourth check
("presence in the theorem's own `#print axioms` probe") is not met for those
two. Nothing extra in the log; three benign `exponentiation.threshold` warnings
(not errors). **Flag, minor: 8-of-10 probe coverage vs the "all ten, committed
log" prose.**

## Item 3 — T1Structure.lean statement match

### The thirteen probed theorems, verbatim (file at `5c9b663`, namespace `T1Structure`; hypotheses shared by several statements abbreviated after first appearance)

1. `theorem cycle_prod_identity (p : ℕ) (x v : Fin (p+1) → ℕ) (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1)) : ∏ i, (3 * x i + 1) = 2 ^ (∑ i, v i) * ∏ i, x i`
2. `lemma pow_succ_lt_two_mul_pow (m n : ℕ) (hm : 0 < m) (h : 2 * n < m) : (m+1) ^ n < 2 * m ^ n`
3. `theorem survivor_bound (p X K : ℕ) (x v : Fin (p+1) → ℕ) (hstep) (hK : K = ∑ i, v i) (hX : 0 < X) (hmin : ∀ i, X ≤ x i) : 2 ^ K * (3 * X) ^ (p+1) ≤ 3 ^ (p+1) * (3 * X + 1) ^ (p+1)`
4. `theorem ceiling_upper (p X K : ℕ) (x v) (hstep) (hK) (hX) (hmin) (hpX : 2 * (p+1) < 3 * X) : 2 ^ K < 2 * 3 ^ (p+1)`
5. `lemma succ_pow_le_pow_add (b : ℕ) : ∀ n, (b+1) ^ (n+1) ≤ b ^ (n+1) + (n+1) * (b+1) ^ n`
6. `theorem seam_bound (p X K : ℕ) (x v) (hstep) (hK) (hX) (hmin) (hpX : 2 * p < 3 * X) : 2 ^ K * (3 * X) < 3 ^ (p+1) * (3 * X + 2 * (p+1))`
7. `theorem seam_gap_at_barina (p K : ℕ) (x v) (hstep) (hK) (hmin : ∀ i, 2 ^ 71 ≤ x i) (hpX : 2 * p < 3 * 2 ^ 71) : 2 ^ K * (3 * 2 ^ 71) < 3 ^ (p+1) * (3 * 2 ^ 71) + 3 ^ (p+1) * (2 * (p+1))`
8. `theorem ratio_bound_at_barina (… as 7 …) (hceil : 3 ^ (p+1) < 2 ^ K) : 1 < (2:ℝ) ^ K / 3 ^ (p+1) ∧ (2:ℝ) ^ K / 3 ^ (p+1) < 1 + 2 * (p+1) / (3 * 2 ^ 71)`
9. `theorem log_gap_at_barina (… as 8 …) : 0 < (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 ∧ (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 < 2 * (p+1) / (3 * 2 ^ 71)`
10. `lemma log_two_gt : (693:ℝ)/1000 < Real.log 2`
11. `theorem log_gap_gen (p X K : ℕ) (x v) (hstep) (hK) (hX : 0 < X) (hmin : ∀ i, X ≤ x i) (hpX : 2 * p < 3 * X) (hceil : 3 ^ (p+1) < 2 ^ K) : 0 < (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 ∧ (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 < 2 * ((p:ℝ)+1) / (3 * X)`
12. `theorem quotient_is_convergent_gen (… as 11 …) (hwin : 4000 * (p+1) ^ 2 ≤ 2079 * X) : ∃ m, Rat.divInt (K : ℤ) ((p+1 : ℕ) : ℤ) = (Real.log 3 / Real.log 2).convergent m`
13. `theorem discharge_all : ∀ qq ∈ convPairs, 2000 * qq.1 * (qq.1 + qq.2) ≤ 2079 * 2 ^ 71` (by `decide`), and `theorem convPairs_length : convPairs.length = 22` (by `decide`).

(13 probed = the eleven above numbered 1–12 minus none, plus `discharge_all`
and `convPairs_length`; two further helper lemmas, `mul_pow_succ_le` and the
canaries, are unprobed — see the axiom-log paragraph.) Checks by read: **0
`sorry`, 0 `native_decide`, no `axiom` declarations**, imports `Mathlib` and
`LegendreApprox`. Four `example` canaries (trivial-cycle instantiations of
`ceiling_upper` and `seam_bound`, the Barina non-vacuity example, the
tightest-case and next-convergent discharge canaries — all reproduced exactly
in this session's script).

### The brief's load-bearing questions

**(i) Does `cycle_prod_identity` quantify over genuine cycles?** Rotation: yes
— `x, v : Fin (p+1) → ℕ` with `x (i + 1)` using `Fin` addition, which wraps
(the last element steps to the first); the proof's `Equiv.addRight 1` is the
rotation. Oddness/positivity: **the Lean statement requires neither.** `hstep`
alone forces every `x i ≥ 1` (since `3x_i + 1 ≥ 1` and `2^v·0 = 0`), so
positivity is implicit; oddness is *not* required (the statement admits e.g.
even `x_i` with `v_i = 0`). The ledger's "positive cycle with p+1 odd elements"
describes the intended instances; the Lean theorem is **strictly more
general** — hypotheses weaker, conclusion identical. Same posture as
ContentDescent's zeros-allowed generality: harmless, recorded.

**(ii) `ceiling_upper`'s hypothesis.** Lean: `hmin : ∀ i, X ≤ x i` with
`hX : 0 < X` and `hpX : 2*(p+1) < 3*X` — the entry's "all elements ≥ X … with
2(p+1) < 3X" verbatim. The letter's "2n < 3·x_min" (n = p+1) is the same
statement: `X` is any positive lower bound, and taking `X = x_min` makes the
two forms interderivable (if `2n < 3·x_min`, instantiate at `X = x_min`;
conversely `x_min ≥ X`). **Same thing, recorded precisely.**

**But — one statement/prose mismatch, the round's main one:** the ledger block
(and the file's own docstring and the `41fa4f8` commit message) state
`ceiling_upper` as concluding **`3^(p+1) < 2^K < 2·3^(p+1)`**. The Lean theorem
concludes **only the upper half, `2^K < 2·3^(p+1)`**. The lower half
`3^(p+1) < 2^K` is *nowhere proved in the file* — it enters downstream
(`ratio_bound_at_barina`, `log_gap_gen`, `quotient_is_convergent_gen`) as the
**hypothesis** `hceil : 3^(p+1) < 2^K`. Mathematically the lower half is one
line from `cycle_prod_identity` (`∏(3xᵢ+1) > ∏3xᵢ` gives `2^K·∏x > 3^(p+1)·∏x`
for positive elements), so this is a formalization gap, not a mathematical one
— but as committed, "K pinned to ⌈(p+1)·log₂3⌉" is **half a kernel theorem plus
an unproved (elementary) hypothesis threaded through the rest of the chain**.
Recorded flat; a one-lemma repair (`ceiling_lower`) would close it and
discharge `hceil` everywhere it appears.

**(iii) `quotient_is_convergent_gen`.** Window hypothesis: exactly
`4000·(p+1)² ≤ 2079·X` — the entry's `4000·n² ≤ 2079·X` with `n = p+1` ✓.
Conclusion: `∃ m, Rat.divInt K (p+1) = (Real.log 3 / Real.log 2).convergent m`
— `log₂3` spelled `log 3 / log 2`, and `.convergent` is **Mathlib's**
`Real.convergent` (Mathlib.NumberTheory.DiophantineApproximation, the
continued-fraction convergents used by `Real.exists_rat_eq_convergent`,
Mathlib's Legendre criterion) ✓. One precision to carry: `Rat.divInt K (p+1)`
is the **reduced** rational — the conclusion says the reduced `K/n` equals some
convergent `p_m/q_m`, i.e. `q_m | n`, not that `n` itself is a convergent
denominator. See the direction trace for why the discharge still covers
`n = t·q_m` (the `t` cancels), and the glue paragraph below. Additional
hypotheses beyond the entry's phrasing: `hceil` (see (ii)) and `hpX : 2p < 3X`
(implied by the window for any `X ≥ 3`; both are stated in the file, the ledger
block's one-line form omits them — summary-level, not a mismatch of substance).

**(iv) `convPairs` — recorded verbatim and independently confirmed.** The list,
verbatim from the file:

```
[(1,1), (1,2), (2,5), (5,12), (12,41), (41,53), (53,306), (306,665), (665,15601),
 (15601,31867), (31867,79335), (79335,111202), (111202,190537), (190537,10590737),
 (10590737,10781274), (10781274,53715833), (53715833,171928773), (171928773,225644606),
 (225644606,397573379), (397573379,6189245291), (6189245291,6586818670),
 (6586818670,65470613321)]
```

Independent computation this session (continued fraction of `log₂3` via
`Decimal` at 150 and 250 digits — ≥ 60 guard digits beyond anything used —
identical terms at both precisions; CF terms
`[1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1, 15, 1, 9, …]`):
**the 22 pairs are exactly `(q_j, q_{j+1})` for `j = 0..21`** of the convergent
denominators `1, 1, 2, 5, 12, 41, 53, 306, 665, 15601, 31867, 79335, 111202,
190537, 10590737, 10781274, 53715833, 171928773, 225644606, 397573379,
6189245291, 6586818670`, correctly successor-paired and chained; and the
denominators `≤` the integral window `⌊√(2079·2^71/4000)⌋ = 35 031 770 966`
are **exactly these 22** — the next, `q₂₂ = 65 470 613 321`, lies outside both
windows and is the file's non-vacuity canary (with `q₂₃ = 137 528 045 312`,
Hercher's, as its successor). **This is one of the two glue facts he names as
unproved; it is now independently confirmed on our side.** The criterion
itself: all 22 pass `2000·q·(q+q′) ≤ 2079·2^71` in exact integers, tightest
margin **5.17×** at `q = 6586818670` (his figure exactly); the exact test
(true `θ_j` at 150 digits) gives **5.44×** at the same `q` (his figure
exactly); and the criterion **fails** at `(q₂₂, q₂₃)` — window ends where it
should.

Window figures reconciled, flat: `3.5035·10¹⁰` (at `89d9efc`/REQ-054) is the
**exact** Legendre window `√(3·2^71·ln2/4) = 3.503549·10¹⁰`; `3.5032·10¹⁰` (at
`4856058`/REQ-055) is the **integral** window `⌊√(2079·2^71/4000)⌋ =
3.503177·10¹⁰`. Two different windows, both figures correct, ratio 1.000106
(his "within 0.011%" ✓). Labeling, flat: `89d9efc` calls 6586818670 "q₂₁"
(consistent with the standard `q₀ = 1` indexing used above), while `81054ea`
calls 65470613321 "q₂₁" and 1.375·10¹¹ "q₂₂" — a one-off indexing shift between
his own messages; the numbers themselves are correct denominators in both.

**(v) The implication direction, written out.** Let `L = log₂3`,
`δ = 2/(3X·ln 2)`, `X = 2^71`, and suppose a surviving positive cycle of length
`n = q_j` in the window.

1. `log_gap_gen` gives `0 < K·ln2 − n·ln3 < 2n/(3X)`; dividing by `ln 2`:
   `0 < K − nL < nδ`, hence `‖nL‖ ≤ |K − nL| < n·δ` — the seam constraint a
   surviving cycle **must** satisfy.
2. Classical convergent bound: `θ_j := ‖q_j·L‖ > 1/(q_j + q_{j+1})` (verified
   numerically for all `j ≤ 22` this session: `1/(q_j+q_{j+1}) < θ_j <
   1/q_{j+1}` throughout). The criterion `2000·q_j·(q_j+q_{j+1}) ≤ 2079·X`
   gives `1/(q_j+q_{j+1}) ≥ 2000·q_j/(2079·X)`, and since
   `2000/2079 = 2/(2.079) > 2/(3·ln 2)` (because `2.079 = 3·(693/1000) <
   3·ln 2 = 2.07944…` — exactly the `log_two_gt` floor), this yields
   `θ_j > 2·q_j/(3X·ln 2) = q_j·δ = n·δ`. **Contradiction with step 1** — the
   seam constraint FAILS at `n = q_j`. ∎

   Conservativity: the integer criterion `q(q+q′) ≤ (2079/2000)·X = 1.0395·X`
   is *strictly stronger* than the exact requirement `q(q+q′) ≤ (3·ln2/2)·X =
   1.039721·X`, because `693/1000 < ln 2`. So passing the integer test implies
   the exact one — conservative by design, as the commit says (and as the
   5.17× vs 5.44× margins show; verified `θ_j > q_j·δ` directly at 150 digits
   for all 22). The multiple case: if `n = t·q_m ≤ window` with reduced
   `K/n = p_m/q_m` (which is all `quotient_is_convergent_gen` guarantees), then
   `|K − nL| = t·|p_m − q_m·L| = t·θ_m` and `nδ = t·q_m·δ`, so the `t` cancels
   and the same `q_m`-level inequality kills it — the discharge at the 22
   denominators covers all `n` in the window. This one-line `t`-cancellation
   sits inside the second named glue fact (the classical bound's application),
   is standard, and is *not* separately named in the ledger's "two glue facts"
   sentence — noted flat for completeness, not as a gap of substance.

### Per-theorem match vs the L-A8 ledger blocks (LEDGER.md at `826970e`)

| Ledger block (stack) | Lean statement | Match |
|---|---|---|
| `ceiling_upper`: "all ≥ X, 2(p+1) < 3X, has **3^(p+1) < 2^K** < 2·3^(p+1), K forced" (`be8869f`) | concludes `2^K < 2·3^(p+1)` **only**; lower half is hypothesis `hceil` downstream | **MISMATCH — upper half only** (see (ii); elementary repair) |
| cycle product identity `∏(3xᵢ+1) = 2^K·∏xᵢ`, telescoping/rotation (`be8869f`) | statement 1 | **Exact** (odd/positive not required — strictly more general) |
| survivor bound `2^K(3X)^{p+1} ≤ 3^{p+1}(3X+1)^{p+1}`, per-factor `(3x+1)(3X) ≤ 3x(3X+1) ⟺ X ≤ x` (`be8869f`) | statement 3; per-factor iff verified on a 1,600-point grid | **Exact** |
| strict two-bound `(m+1)^n < 2m^n` for `2n < m` (`be8869f`) | statement 2 | **Exact** |
| `seam_bound`: "with 2p < 3X: 2^K·3X < 3^(p+1)·(3X + 2(p+1))" (`0905b00`) | statement 6 | **Exact** — verbatim |
| `seam_gap_at_barina` "subtraction-free, at X = 2⁷¹" (`9428663`) | statement 7 | **Exact** |
| `ratio_bound_at_barina` / `log_gap_at_barina` (`a37743f`, quoted forms) | statements 8, 9 | **Exact** (block omits the `hceil` hypothesis; present in file) |
| `quotient_is_convergent_gen`: "length n = p+1 with 4000·n² ≤ 2079·X has K/n a convergent of log₂3" (`5773bd0`) | statement 12 | **Exact** (conclusion is the *reduced* `K/n`; see (iii)) |
| `discharge_all`: "every convergent denominator in the Barina window satisfies 2000·q·(q+q′) ≤ 2079·2⁷¹" (`826970e`) | statement 13; "every denominator in the window" = the fixed list `convPairs`, whose identification with the actual denominators is glue fact 1 — **independently confirmed here** | **Exact** (given the confirmed list) |
| "Thirteen theorems, 0 sorry, no native_decide, no user axioms" (`826970e`) | 13 probed declarations, 0/0/0 by read | **Exact** (two unprobed helper lemmas besides — below) |
| "remaining glue = two standard CF facts: convPairs is the in-window denominator list; θ_j > 1/(q_j+q_{j+1})" (`826970e`) | both named, neither in the file | **Exact** — and both now independently verified our side (list exact; classical bound numerically at all 22) |
| retraction recorded "in the artifact with a RETRACTED note" (`5773bd0`) | see next paragraph | **Partial — note superseded at HEAD** |

### The retraction record

At **`7d46474`** the file carried the full standalone note — verbatim beginning:
"**RETRACTED (2026-07-25).** A `quotient_is_convergent` theorem was drafted
here and pushed in commit `da2c8db` claiming kernel-3 status. That claim was
FALSE: the file did not compile — `lake env lean` printed no `error:` line but
aborted with a stack overflow (`maxRecDepth 40000`), and at workable depths the
proof carries `sorryAx`. … It is withdrawn until proved, **and this note stays
as the record**" — exactly as the provenance describes. At **`4856058`** (the
successful second attempt) that block was **replaced** by the new section
header, which retains a one-line reference: "The first attempt (commit
`da2c8db`, retracted) let the literal `2^71` reach `nlinarith` and the
elaborator blew the stack." So at HEAD the retraction is on record in the git
history and referenced in the file, but the standalone note (whose own text
said it "stays as the record") no longer is. Flat observation — the honest
sequence is fully preserved in the history and the ledger block (`5773bd0`
addendum) tells it straight; only the in-file permanence promise lapsed when
the theorem was actually proved. **No theorem at HEAD depends on the retracted
one:** `quotient_is_convergent` (non-gen) does not exist in the file at
`5c9b663`; `quotient_is_convergent_gen` is a fresh proof with the threshold
abstracted, and nothing references the old name.

### T1 axiom log — `experiments/T1Structure_axioms.txt`

All 13 probed theorems present, matching the in-file probes one-to-one:
**`discharge_all` → `[propext]` only ✓; `convPairs_length` → "does not depend
on any axioms" ✓;** the remaining 11 each exactly
`[propext, Classical.choice, Quot.sound]` ✓. Nothing extra, nothing missing
relative to the probes; header records the four-way verification claim. The
helper lemmas `mul_pow_succ_le` (used by `pow_succ_lt_two_mul_pow`) and the
`example` canaries are unprobed — transitively covered by their consumers'
probes; same minor pattern as DeficitLemma, listed once in the flags.

## Item 4 — LegendreApprox.lean

Provenance: imported from his separate "Junction" repository (per the ledger
and commit `da2c8db`); entered this repo at `da2c8db`, byte-unchanged since.
The Junction repo itself is NOT audited here (later, separate item). Imports:
`Mathlib.NumberTheory.DiophantineApproximation.Basic`, `Mathlib.Data.Rat.Lemmas`.
Statements, verbatim:

- `theorem abs_sub_ge_of_not_convergent (ξ : ℝ) (q : ℚ) (hnc : ∀ n, q ≠ ξ.convergent n) : 1 / (2 * (q.den : ℝ) ^ 2) ≤ |ξ - ↑q|`
- `lemma divInt_den_dvd_nat (S k : ℕ) (_hk : 0 < k) : (Rat.divInt (↑S) (↑k)).den ∣ k`
- `theorem abs_sub_ge_nat_div (ξ : ℝ) (S k : ℕ) (hk : 0 < k) (hnc : ∀ n, Rat.divInt (↑S) (↑k) ≠ ξ.convergent n) : 1 / (2 * (k : ℝ) ^ 2) ≤ |ξ - (S : ℝ) / k|`

`abs_sub_ge_of_not_convergent` is exactly Legendre's criterion in contrapositive
form — "not a convergent ⟹ `|ξ − q| ≥ 1/(2·den(q)²)`", equivalently
"`|ξ − q| < 1/(2·den(q)²)` ⟹ `q` is a convergent" — proved directly from
Mathlib's `Real.exists_rat_eq_convergent`. **Hypotheses: none beyond `q : ℚ`**
— no coprimality (the denominator is the *reduced* one, `q.den`, so coprimality
is built into ℚ), no positivity, no irrationality side condition.
`abs_sub_ge_nat_div` specializes to `S/k` with `k` only a *bound* on the
denominator (`den | k`, so `1/(2k²) ≤ 1/(2·den²)` — a sound weakening, verified
on examples with `gcd(S,k) > 1`). `quotient_is_convergent_gen` discharges its
hypotheses fully: `hk` from `omega`, `hnc` from the contradiction assumption —
nothing is left dangling. Statement canary this session: exhaustive over
`q ≤ 200`, every rational within `1/(2q²)` of `log₂3` is a convergent (5 hits,
all convergents).

Checks by read: 0 `sorry`, 0 `native_decide`, no `axiom` declarations. **Flat
pin on the claimed axioms:** the ledger's recurring "0 sorry, 0 axioms,
0 native_decide" for this file — if "0 axioms" is read as *kernel* axioms — is
not evidenced by any committed log: `T1Structure_axioms.txt`'s header says
"T1Structure + LegendreApprox" but contains **no LegendreApprox entries**, and
the file itself has no `#print axioms` probes. Read as "0 *user* axioms" (the
established usage in every other block) it is consistent with the file as read;
its two theorems use `Real`/ℚ machinery and would be expected kernel-3, like
everything else. Recorded as: claim consistent by read, log coverage absent.

## Adjudication summary

| Brief question | Answer |
|---|---|
| `marginTarget` encodes `margin(n) ≥ n/13`? | **YES — exactly**, at the tuned north cell: hypotheses pin `K = ⌈n·log₂3⌉` uniquely; `C(K−2,n−1)` is the L-A7 word count (Vandermonde-verified); unfolding is `K − log₂#words ≥ n/13`. Gaps: constant `1/13` vs `c_gen` (3.0%, honestly ledgered); tuned-north-cell coverage only (south / above-tuned cells belong to the (iii) repair, not this theorem) |
| `convPairs` = the in-window convergent denominators? | **CONFIRMED independently** — 22 pairs `(q_j, q_{j+1})`, `j = 0..21`, exactly the denominators `≤ ⌊√(2079·2^71/4000)⌋`; criterion passes all 22 (5.17× / 5.44×), fails at `q₂₂` |
| Axiom logs match the claims? | **T1: exact** (13/13, `discharge_all` `[propext]`, `convPairs_length` `[]`). **DeficitLemma: 8 of 10** (`key_shifted`, `key15` unprobed/unlogged; transitively covered). **LegendreApprox: no log entries at all** despite the log header naming it |
| Statement/prose mismatches? | **One of substance: `ceiling_upper` proves the upper half only** — the ledger/docstring state both bounds; the lower `3^(p+1) < 2^K` is an unproved (elementary) hypothesis `hceil` threaded through the chain. Others flat/minor: retracted-note text superseded at `4856058`; stale DeficitLemma header scope note; reduced-`K/n` nuance in the convergent conclusion (covered by the `t`-cancellation); `q₂₁` indexing shift between `81054ea` and `89d9efc`; 3.5032/3.5035 = integral vs exact window, both correct; "slack 1.700" is the route-implied quantity |
| Retraction | Full note present at `7d46474` as described; replaced at `4856058` by a one-line reference; no dependence on the retracted theorem at HEAD |

**Flags, collected:** (1) `ceiling_upper` upper-half-only vs the ledger's
two-sided statement — the round's one substantive statement/prose mismatch;
one-lemma repair, co-edit/reply material. (2) DeficitLemma axiom log covers 8
of the stated 10 (probes absent for `key_shifted`, `key15`); his own hardened
protocol's probe-presence check is unmet for those two. (3) No LegendreApprox
entries in any committed axiom log despite the log header naming the file;
"0 axioms" untraceable to a log (consistent as "0 user axioms" by read).
(4) Stale DeficitLemma SCOPE header says `MarginTarget` is unproved; it is
proved 200 lines below in the same file. (5) The in-file RETRACTED note (which
promised to stay) was superseded by the successful proof's section comment;
history preserves it. (6) `quotient_is_convergent_gen` concludes about the
*reduced* `K/n`; the discharge still covers multiples by `t`-cancellation —
standard, unstated. (7) Read-not-built: kernel-3/`[propext]`/no-axiom claims
rest on his committed logs, not an our-side build. **No discrepancies of
digits, hashes, or list contents anywhere. Handbacks: none.**

**Key recommendation** (recommendation only — no key is turned here, per the
brief): scoped to what a read-not-built audit supports — the statements are
confirmed to say what the ledger says they say (with the `ceiling_upper`
exception stated), every statement is true as instantiated (15,930 exact
checks, 0 failures), the convPairs glue fact is now two-key at the level of
independent computation, and the axiom logs match their claims where they
exist. A Macindoe statement-match key on **DeficitLemma/marginTarget** can turn
as scoped (statement-level + canaries + log, read-not-built stated), ideally
with the 8-of-10 log completion offered; for **T1Structure**, turn-with-offer:
the `ceiling_upper` two-sided prose should either gain the one-lemma
`ceiling_lower` companion or be restated as upper-half-plus-hypothesis before
the L-A8 block's "K pinned" sentence carries a two-key marking.
