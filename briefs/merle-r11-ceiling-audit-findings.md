# Findings: round-11 Lean re-audit — the ceiling repair (`ceiling_lower` / `ceiling_pinned`, `hceil` removal)

Delegated session, 2026-07-27. Brief: `briefs/merle-r11-ceiling-audit-brief.md`.
Branch `merle-r11-ceiling-audit`, base commit **`e938040`** — the worktree was
cut from the session-start HEAD `2225b68`, which does **not** contain the
brief; it was rebranched onto `e938040` (the brief commit, current `main`)
before any work began, as the launch instruction and the brief's Rules require.

Register: flat; statements recorded verbatim; discrepancies recorded, never
disputed in prose. No key is turned. No reply paragraphs, no ledger text.
Read-only clone in the scratchpad; no pushes; no fork, issue, star, watch or
comment on any of his repositories; no Lean toolchain installed or attempted.

**Trust boundary, stated plainly.** This is a **read-not-built** statement-match
audit, the precedent being `experiments/merle_lean_r10_audit.py`. What is
verified here: (1) the Lean *statements* say what the letter and the L-A8
ledger block say they say; (2) the *dependency structure* is what he describes
— specifically that `hceil` is gone from the four downstream signatures and is
re-derived internally from `ceiling_lower`, checked against every mechanism by
which a hypothesis can vanish from a printed signature and still be threaded;
(3) the committed axiom logs match the claimed axiom sets, and the 13 → 15
reconciliation is exact; (4) every statement, instantiated at exact-integer
points including edges and the real cycles, is *true as stated*. What is NOT
verified here: that the proofs compile and the kernel accepts them. The
kernel-3 / `[propext]` / no-axiom claims rest on his committed logs and his
four-way-hardened protocol — the same posture as the ContentDescent, L-A1 and
round-10 precedents.

**Stopping-rule compliance:** verification of a correspondent's artifacts; no
new computational front; the cycles front stays PARKED (the synthetic sweeps
are element multisets and `(n, K)` pairs, not orbit or period searches).

## Item 1 — the clone, the graph, the drift check

Fresh unauthenticated read-only clone (2026-07-27) of
`github.com/ericmerle3789/one-obstruction-three-faces-lean` into the scratchpad.

**HEAD = `c991430297b1e6e3e88f1c09c5f3c20b7dd6220b` (`c991430`)** — exactly the
expected pin, with `6c084c5` beneath it. **The graph `5c9b663 → HEAD` is
linear**: each commit has exactly one parent (`c991430`'s parent is `6c084c5`;
`6c084c5`'s parent is `5c9b663`), two commits, no merges, both authored
`Eric MERLE`, 2026-07-26 CEST (17:39:14 and 20:30:40 +0200).

| commit | date | what it changed |
|---|---|---|
| **`6c084c5`** | 2026-07-26 17:39 | "Round-10 repairs, all found by Macindoe's audit and confirmed here before fixing." 13 files, +376/−122. `T1Structure.lean`: adds `ceiling_lower`, `ceiling_pinned`, their canary and their two `#print axioms` probes; removes `hceil` from four signatures. `DeficitLemma.lean`: SCOPE header corrected in place, probes added for `key_shifted`/`key15`. Both axiom logs regenerated. `OUT_REQ-MATH-052/053`: crashed-run tracebacks removed, the δ factor-2 corrected in the P3 table, the indexing convention pinned to standard, the "exhaustive to `q₁₀ = 190537`" label corrected to `n < q₁₃ = 190537` and the sweep actually extended to `j = 12`. `OUT_REQ-MATH-043/055/056` gain reproduction verdicts; `OUT-056` gains the multiples clause. Three previously scriptless outputs gain their generator scripts (`test_REQ-MATH-043`, `-055`, `-056`). |
| **`c991430`** | 2026-07-26 20:30 | "Restore the permanent RETRACTED record for da2c8db, per Macindoe's round-10 flat note." `T1Structure.lean` only, +24/−0: the standalone RETRACTED block. |

**Drift check — NO DRIFT.** `git diff` against the previously audited SHAs is
empty for all four files:

- `ContentDescent.lean` — unchanged since `67c428a`.
- `ContentSeparation.lean` — unchanged since `905d75b`.
- `TransportRecurrence.lean` — unchanged since `7d3d44a`.
- **`LegendreApprox.lean` — unchanged since `da2c8db`, and byte-identical
  between `5c9b663` and HEAD.** (Recorded explicitly because it bears on the
  sibling session `junction-public-recon`: the file's *home* is still not
  confirmed, but the file itself has not moved.)

`README.md` and `experiments/README.md` are also unchanged.

**One incidental observation, flat.** The three `exponentiation.threshold`
warning lines that `DeficitLemma_axioms.txt` carried at `5c9b663` — which
embedded his local working path
`/Users/ericmerle/Documents/Collatz-Racine-Mur-2026-07-16/lean/DeficitLemma.lean`
— are removed at HEAD along with the log headers (item 6). Recorded because
the round-10 record cites that path; it is no longer in the tree.

## Item 2 — `ceiling_lower` and `ceiling_pinned`, statement match

### Verbatim, `OneObstruction/T1Structure.lean` at `c991430` (lines 123–155)

```lean
/-- **The ceiling, lower half (REQ-MATH-066).** Found missing by Macindoe's round-10 audit:
`ceiling_upper` proves only `2^K < 2*3^(p+1)`; the companion bound `3^(p+1) < 2^K` was
threaded downstream as the hypothesis `hceil` and proved nowhere. One line from the product
identity: every factor `3*x i + 1` strictly exceeds `3*x i`, so
`3^(p+1) * ∏x < ∏(3x+1) = 2^K * ∏x`, and `∏x > 0` cancels. -/
theorem ceiling_lower (p X K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hX : 0 < X) (hmin : ∀ i, X ≤ x i) :
    3 ^ (p+1) < 2 ^ K := by
  have hxpos : ∀ i, 0 < x i := fun i => lt_of_lt_of_le hX (hmin i)
  have hprodpos : 0 < ∏ i, x i := Finset.prod_pos (fun i _ => hxpos i)
  have hid : ∏ i, (3 * x i + 1) = 2 ^ K * ∏ i, x i := by
    rw [hK]; exact cycle_prod_identity p x v hstep
  have hL : ∏ i, (3 * x i) = 3 ^ (p+1) * ∏ i, x i := by
    rw [Finset.prod_mul_distrib, Finset.prod_const, Finset.card_univ, Fintype.card_fin]
  have hlt : ∏ i, (3 * x i) < ∏ i, (3 * x i + 1) := by
    refine Finset.prod_lt_prod_of_nonempty (fun i _ => ?_) (fun i _ => ?_) Finset.univ_nonempty
    · have := hxpos i; omega
    · omega
  rw [hL, hid] at hlt
  exact lt_of_mul_lt_mul_right hlt (Nat.zero_le _)

/-- **The ceiling, both halves.** `K` is pinned: `3^(p+1) < 2^K < 2*3^(p+1)`. -/
theorem ceiling_pinned (p X K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hX : 0 < X) (hmin : ∀ i, X ≤ x i)
    (hpX : 2 * (p+1) < 3 * X) :
    3 ^ (p+1) < 2 ^ K ∧ 2 ^ K < 2 * 3 ^ (p+1) :=
  ⟨ceiling_lower p X K x v hstep hK hX hmin,
   ceiling_upper p X K x v hstep hK hX hmin hpX⟩

/-- Canary: `ceiling_pinned` on the trivial cycle gives `3 < 4 < 6`. -/
example : (3:ℕ) ^ 1 < 2 ^ 2 ∧ (2:ℕ) ^ 2 < 2 * 3 ^ 1 := by norm_num
```

### What each encodes, in our own words

- **`ceiling_lower`.** Given `p+1` positive naturals arranged in a cycle by the
  odd-Collatz step relation `3xᵢ + 1 = 2^{vᵢ}·x_{i+1}` (indices in `Fin (p+1)`,
  so the last wraps to the first) with `K` the total exit valuation `Σvᵢ`, the
  total halving `2^K` strictly exceeds the total tripling `3^{p+1}`. In the
  seam language: `q = 2^K − 3^n > 0`, i.e. **a genuine positive cycle lies on
  the north shore**, unconditionally. No size threshold, no window, no
  Barina input.
- **`ceiling_pinned`.** The same cycle, plus the elementary size condition
  `2(p+1) < 3X`, satisfies `3^{p+1} < 2^K < 2·3^{p+1}` — i.e. `2^K` sits in
  the half-open dyadic block immediately above `3^{p+1}`, which forces
  `K = ⌈(p+1)·log₂3⌉ = bitlength(3^{p+1})` and nothing else. One degree of
  freedom removed, in pure integers, no logarithm in the statement.

### The brief's four questions

**(a) Same notion of genuine cycle as `cycle_prod_identity`? — YES, with the
hypotheses *weaker*, not stronger.** `cycle_prod_identity` takes
`(p : ℕ) (x v : Fin (p+1) → ℕ) (hstep)`. `ceiling_lower` takes exactly that
plus `hK : K = ∑ i, v i` (a definition of `K`, not a restriction),
`hX : 0 < X` and `hmin : ∀ i, X ≤ x i`. Rotation is `Fin` addition, the same
wrap-around; `X` is any positive lower bound, exactly as in `ceiling_upper`
and `survivor_bound`. **No extra hypothesis** beyond the positivity bound
that the ledger's "the ceiling is pinned" does not mention; in particular no
oddness requirement — the Lean statement is, as at round 10, strictly more
general than the ledger's "positive cycle with `p+1` odd elements" prose
(hypotheses weaker, conclusion identical; harmless, recorded for the third
round running). The `X`/`hX`/`hmin` triple is used only to obtain
`0 < xᵢ`; `hstep` alone already forces `xᵢ ≥ 1` (from `3xᵢ+1 ≥ 1` and
`2^v·0 = 0`), so `ceiling_lower` could be stated with `hstep` and `hK` alone.
It is not — and that is the right call for the repair, because carrying the
same `X`, `hX`, `hmin` as `ceiling_upper` is what lets `ceiling_pinned`
apply both halves to one hypothesis set and what lets the downstream
call sites pass their existing arguments straight through. **Flat, not a
flag.**

**(b) Is `Px > 0` proved in-file or assumed? — PROVED IN-FILE, in two lines.**
```lean
  have hxpos : ∀ i, 0 < x i := fun i => lt_of_lt_of_le hX (hmin i)
  have hprodpos : 0 < ∏ i, x i := Finset.prod_pos (fun i _ => hxpos i)
```
`0 < xᵢ` is derived from `hX` and `hmin` (`0 < X ≤ xᵢ`); the product's
positivity is then `Finset.prod_pos`. Positivity of the elements enters as a
consequence of the cycle's stated lower bound, exactly as the letter says — it
is **not** a hypothesis of the form `0 < ∏x`. The cancellation itself is
`lt_of_mul_lt_mul_right hlt (Nat.zero_le _)` applied after rewriting both
sides into the form `(·) * ∏x`; note that on ℕ the right-cancellation lemma
needs only `0 ≤ ∏x`, so `hprodpos` is in fact carried but not consumed at the
final step — the positivity that matters is the strictness of `hlt`, which
comes from `Finset.prod_lt_prod_of_nonempty` with `0 < 3·xᵢ` (i.e. from
`hxpos`) and `3xᵢ < 3xᵢ+1`. Recorded precisely because the brief asks where
positivity enters: it enters through `hxpos`, derived, and it is genuinely
load-bearing — with `xᵢ = 0` allowed, `∏(3xᵢ) = 0 < ∏(3xᵢ+1)` still holds but
the strict-product lemma's hypothesis fails and the identity's right-hand
side collapses.

**(c) Unconditionality — CONFIRMED. `ceiling_lower` needs no Barina input, no
`x_min ≥ 2^71`, no window hypothesis.** Its full hypothesis list is
`p X K : ℕ`, `x v : Fin (p+1) → ℕ`, `hstep`, `hK`, `hX : 0 < X`,
`hmin : ∀ i, X ≤ x i`. There is no `hpX`, no numeral `2^71`, no `hwin`, no
`4000·n² ≤ 2079·X`, and no real-number hypothesis of any kind — the statement
and proof are entirely in ℕ. The proof's only inputs are
`cycle_prod_identity` (kernel, same file) and Mathlib's `Finset` product
lemmas. **This is what makes the downstream removal legitimate**, and it is
the load-bearing fact the brief flagged: had `ceiling_lower` carried any of
those, discharging `hceil` at the call sites would have smuggled the
condition in. It does not.

**(d) Does `ceiling_pinned` conjoin exactly the L-A8 block's two bounds? —
YES, exactly; no strictness or index drift.**

| L-A8 block (`be8869f`, quoted in `briefs/merle-la8-t1-check-findings.md`) | `ceiling_pinned` conclusion |
|---|---|
| `3^(p+1) < 2^K < 2·3^(p+1)` | `3 ^ (p+1) < 2 ^ K ∧ 2 ^ K < 2 * 3 ^ (p+1)` |

Both inequalities strict, both in the block's own direction, the same exponent
`p+1` on both sides, the same factor 2 on the upper bound. The hypothesis set
is the block's verbatim "all elements `≥ X`, with `2(p+1) < 3X`" — `hpX` is
`2 * (p+1) < 3 * X`, matching `ceiling_upper`'s and the block's `2(p+1) < 3X`
(and the letter's `2n < 3·x_min` under `X = x_min`, interderivable as recorded
at round 10). **The round-10 mismatch is closed at the statement level: the
ledger's two-sided sentence is now a single kernel theorem, not half a theorem
plus a hypothesis.**

`ceiling_pinned` is a term-mode conjunction of the two halves with no
additional proof content — it introduces no new obligation and cannot
introduce a hidden one.

## Item 3 — the `hceil` removal: verified, not taken

### The four signatures, verbatim, before and after

Copied from `OneObstruction/T1Structure.lean` at each SHA; the single
difference in each pair is marked. Conclusions included in full, so that any
drift in them would be visible here too.

**1. `ratio_bound_at_barina` — at `5c9b663`:**

```lean
theorem ratio_bound_at_barina (p K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hmin : ∀ i, 2 ^ 71 ≤ x i)
    (hpX : 2 * p < 3 * 2 ^ 71) (hceil : 3 ^ (p+1) < 2 ^ K) :
    1 < (2:ℝ) ^ K / 3 ^ (p+1) ∧
      (2:ℝ) ^ K / 3 ^ (p+1) < 1 + 2 * (p+1) / (3 * 2 ^ 71)
```

**at `c991430` (HEAD):**

```lean
theorem ratio_bound_at_barina (p K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hmin : ∀ i, 2 ^ 71 ≤ x i)
    (hpX : 2 * p < 3 * 2 ^ 71) :
    1 < (2:ℝ) ^ K / 3 ^ (p+1) ∧
      (2:ℝ) ^ K / 3 ^ (p+1) < 1 + 2 * (p+1) / (3 * 2 ^ 71)
```

Delta: `(hceil : 3 ^ (p+1) < 2 ^ K)` deleted. Nothing else.

**2. `log_gap_at_barina` — at `5c9b663`:**

```lean
theorem log_gap_at_barina (p K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hmin : ∀ i, 2 ^ 71 ≤ x i)
    (hpX : 2 * p < 3 * 2 ^ 71) (hceil : 3 ^ (p+1) < 2 ^ K) :
    0 < (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 ∧
      (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 < 2 * (p+1) / (3 * 2 ^ 71)
```

**at `c991430` (HEAD):**

```lean
theorem log_gap_at_barina (p K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hmin : ∀ i, 2 ^ 71 ≤ x i)
    (hpX : 2 * p < 3 * 2 ^ 71) :
    0 < (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 ∧
      (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 < 2 * (p+1) / (3 * 2 ^ 71)
```

Delta: `(hceil : ...)` deleted; in the body, the call becomes
`ratio_bound_at_barina p K x v hstep hK hmin hpX` (trailing `hceil` argument
dropped). Nothing else.

**3. `log_gap_gen` — at `5c9b663`:**

```lean
theorem log_gap_gen (p X K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hX : 0 < X) (hmin : ∀ i, X ≤ x i)
    (hpX : 2 * p < 3 * X) (hceil : 3 ^ (p+1) < 2 ^ K) :
    0 < (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 ∧
      (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 < 2 * ((p:ℝ)+1) / (3 * X)
```

**at `c991430` (HEAD):**

```lean
theorem log_gap_gen (p X K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hX : 0 < X) (hmin : ∀ i, X ≤ x i)
    (hpX : 2 * p < 3 * X) :
    0 < (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 ∧
      (K:ℝ) * Real.log 2 - (p+1) * Real.log 3 < 2 * ((p:ℝ)+1) / (3 * X)
```

Delta: `(hceil : ...)` deleted. Nothing else.

**4. `quotient_is_convergent_gen` — at `5c9b663`:**

```lean
theorem quotient_is_convergent_gen (p X K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hX : 0 < X) (hmin : ∀ i, X ≤ x i)
    (hpX : 2 * p < 3 * X) (hceil : 3 ^ (p+1) < 2 ^ K)
    (hwin : 4000 * (p+1) ^ 2 ≤ 2079 * X) :
    ∃ m, Rat.divInt (K : ℤ) ((p+1 : ℕ) : ℤ) = (Real.log 3 / Real.log 2).convergent m
```

**at `c991430` (HEAD):**

```lean
theorem quotient_is_convergent_gen (p X K : ℕ) (x v : Fin (p+1) → ℕ)
    (hstep : ∀ i, 3 * x i + 1 = 2 ^ v i * x (i + 1))
    (hK : K = ∑ i, v i) (hX : 0 < X) (hmin : ∀ i, X ≤ x i)
    (hpX : 2 * p < 3 * X)
    (hwin : 4000 * (p+1) ^ 2 ≤ 2079 * X) :
    ∃ m, Rat.divInt (K : ℤ) ((p+1 : ℕ) : ℤ) = (Real.log 3 / Real.log 2).convergent m
```

Delta: `(hceil : ...)` deleted; in the body, the call becomes
`log_gap_gen p X K x v hstep hK hX hmin hpX`. `hwin` is untouched and stays
last. Nothing else.

### Verdict: the hypothesis is GONE, not threaded. Every route checked.

**Route 1 — renamed or weakened to a differently-named hypothesis?** No.
`git diff 5c9b663 HEAD -- OneObstruction/T1Structure.lean` is 66 added lines
and 6 removed, and the *entire* signature delta is the four deletions above.
No hypothesis of any name is added to any of the four; the binder lists shrink
by exactly one and change in no other respect.

**Route 2 — hoisted into a section `variable`, `include` or `omit`?** No — and
this is the check the brief singles out. Grepping `T1Structure.lean` at HEAD
for every line-initial structural keyword
(`variable|variables|include|omit|section|structure|class|instance|open|namespace|end|attribute|local`)
returns **exactly two lines in the whole 482-line file**:

```
21:namespace T1Structure
482:end T1Structure
```

There is **no `variable` command, no `include`, no `omit`, no `section`, no
`structure`, no `class`, no `instance`, no `attribute`, no `local` anywhere in
the file.** There is therefore no mechanism by which any hypothesis — `hceil`
or otherwise — could be threaded into these four theorems without appearing in
their own binder lists. Every argument each theorem takes is printed in the
signatures above. (This also settles the `structure`/`class`-field variant: no
structure or class is declared in the file, and the four conclusions mention
none.)

**Route 3 — is it genuinely derived internally?** Yes; the call sites,
recorded:

- **`ratio_bound_at_barina`**, line 264–265 — a local `have`, immediately
  after `hB`:
  ```lean
    have hceil : 3 ^ (p+1) < 2 ^ K :=
      ceiling_lower p _ K x v hstep hK (by positivity) hmin
  ```
  The `_` for `ceiling_lower`'s `X` unifies with `2 ^ 71` from this theorem's
  own `hmin : ∀ i, 2 ^ 71 ≤ x i`; the `hX : 0 < X` slot is discharged by
  `positivity` on `0 < 2 ^ 71`. The name `hceil` survives only as a local
  hypothesis label inside the proof — the next line, `hlow`, is unchanged from
  `5c9b663`, which is why the rest of the proof body is byte-identical.
- **`log_gap_gen`**, line 358–359 — the same two lines, inserted after `hXR`:
  ```lean
    have hceil : 3 ^ (p+1) < 2 ^ K :=
      ceiling_lower p _ K x v hstep hK (by positivity) hmin
  ```
  Here the `_` unifies with this theorem's own `X` (from
  `hmin : ∀ i, X ≤ x i`), and the `hX : 0 < X` slot is discharged from the
  theorem's *own* `hX : 0 < X`, which is still in its binder list — Mathlib's
  `positivity` falls back to the local context for atoms. Flat note, since it
  is the one place the read cannot be fully mechanical: this is a genuine
  dependence on `hX`, and `hX` is still a stated hypothesis of `log_gap_gen`,
  so nothing is hidden; but whether `positivity` closes `0 < X` for a variable
  `X : ℕ` from the ambient `hX` is a compile-time fact, and this audit does not
  compile. His four-way protocol reports it clean.
- **`log_gap_at_barina`** and **`quotient_is_convergent_gen`** do not call
  `ceiling_lower` themselves: each simply passes one fewer argument to its
  predecessor (`ratio_bound_at_barina p K x v hstep hK hmin hpX` and
  `log_gap_gen p X K x v hstep hK hX hmin hpX` respectively — the trailing
  `hceil` argument deleted in both). They inherit the derivation transitively,
  which is the correct structure.

`grep -n hceil OneObstruction/*.lean` at HEAD returns **five lines total**: one
inside `ceiling_lower`'s docstring (narrating the round-10 finding), and the
two `have hceil`/`exact_mod_cast hceil` pairs above. No signature anywhere in
the repository contains it.

**Route 4 — anything else riding along in those four statements?** No. Checked
item by item against the diff: the window constants are untouched
(`hwin : 4000 * (p+1) ^ 2 ≤ 2079 * X` character-for-character identical;
`2000`/`2079` appear only in `discharge_all` and `convPairs`, both unchanged);
the Barina numeral `2 ^ 71` is unchanged in all three places it occurs; the
`hpX` forms (`2 * p < 3 * 2 ^ 71`, `2 * p < 3 * X`) are unchanged; both
conclusion pairs of `ratio_bound_at_barina` and the two `log_gap` theorems are
unchanged including the `2 * (p+1) / (3 * 2 ^ 71)` and
`2 * ((p:ℝ)+1) / (3 * X)` right-hand sides; and
`quotient_is_convergent_gen`'s conclusion is still
`∃ m, Rat.divInt (K : ℤ) ((p+1 : ℕ) : ℤ) = (Real.log 3 / Real.log 2).convergent m`
— the same reduced-`K/n` form, with the same Mathlib `Real.convergent`, so the
round-10 `t`-cancellation note continues to apply verbatim (and he has now
written that cancellation into `OUT_REQ-MATH-056.txt` himself, crediting it).
**No drift rode along with the repair.**

**Verdict: the removal is real.** `hceil` is not renamed, not weakened, not
absorbed into a structure field, and — the trap the brief named — not hoisted
into a section `variable`, `include` or `omit`, because the file declares none.
The lower bound is now derived inside `ratio_bound_at_barina` and
`log_gap_gen` from the kernel theorem `ceiling_lower`, and inherited by the
other two. His sentence "derived internally now, so it cannot travel as an
assumption again" is accurate as committed.
