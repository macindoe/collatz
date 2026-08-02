# Findings: the letter indexing (v3 round 4, closing pass)

**Branch.** `v3r4-review-round4`. Base `2ec9702`; two commits added:

| commit | contents |
|---|---|
| `132cb4d` | record: `aeh.md` `13.2.3`'s gap identity, `open-problems.md` `11.12` |
| `0352bf9` | Appendix A pin `a1f2ac3` → `132cb4d`, rebuilt PDF |

No push, no merge, no rebase, no branch switch, no worktree. Every file written with the Write/Edit
tools; no PowerShell redirection touched a tracked file; both edited pages re-checked byte-wise for
mojibake after editing (`≤`, `−`, `₂`, `·`, `≥`, `δ`, `θ`, `τ` all intact, no BOM).

**One statement was repaired; the second is handed back.** The fix delegate's report on statement 2
("harmless to every conclusion") does not survive checking: the off-by-one makes `13.2.4`(a) **false
as printed**, not merely inelegant, and every repair for it moves either (a)'s own bound or Corollary
`13.2.4.1`. Per the brief's stop clause that is outside this pass's scope. §3 and §7 below.

---

## 1. The indexing, traced from the definitions

Traced from `13.2.1`, `13.2.4`, `13.6.3`(i), reverse.md `14.14.6`, spine.md's `R`, itinerary.md
`14.15.1.1`–`14.15.1.5`, and reverse.md `14.14.7.1` — not from any findings file. Every step below was
then re-derived numerically from those definitions in fresh code (scratchpad only; nothing added to
`experiments/`, since nothing new is claimed on a tracked page beyond what `13.2.4`'s Verified line
already records).

### 1.1 The chain

Write `y_i := G^i(x)` for an odd start `x`, so `y_0 = x`.

* `R(x) = (ω_0, d_0)` is spine.md's `R`: `x + 1 = 2^m·3^a·Ω`, `(ω_0, d_0) = (Ω, m + a)`.
* Edge `n` is the `F`-step `(ω_n, d_n) → (ω_(n+1), d_(n+1))`; its exit is
  `x_exit(n) = (3^(d_n)ω_n − 1)/2^(s_n)`, `s_n = v_2(3^(d_n)ω_n − 1)`.
* **`x_exit(n) = y_(n+1)`.** Direct from `14.14.7.1`: `G(y) = T^(v_2(y+1))(y) = (3^m q − 1)/2^r`, and
  at `y = x` that is `(3^(d_0)ω_0 − 1)/2^(s_0)` exactly. So `13.2.4`'s `y_(−1) = x`, `y_n = G^(n+1)(x)`
  is this chain shifted by one, and `state(y_(n+1)) = (ω_(n+2), d_(n+2))` — `13.6.3`(i)(a)'s alignment.
* **`stratum(y_i) = (m_i, s_i)`**, where `m_i = v_2(y_i + 1)` is the number of `T`-steps in block `i`
  and `s_i` is block `i`'s own exit valuation. This is reverse.md `14.14.6`'s seam identification read
  at the door `y_i`: the `m`-label is the `m_+` of the edge whose exit is `y_i`, the `r`-label is the
  `s` of the edge `y_i`'s state emits. Equivalently `stratum(y_n) = (m_(+,n−1), s_n)`.

### 1.2 The three readings, and which statement uses which

* **(A) `letter i = stratum(y_i)`** — the letter word of `x` itself, which is the word itinerary.md
  Theorem `14.15.1.5` is stated about (Definition `14.15.1.2`: `y` *follows* `W` with `y_0 := y`).
  **`13.2.1`'s and `13.2.3`'s budget sum `S_n = Σ_(i<n)(m_i + s_i)` is (A)'s word**, and that is
  exactly what makes the clock identity `x_exit(n−1) = T_1^(S_n)(x)` hold: block `i` costs
  `m_i + s_i` divisions, by `14.14.7.1`'s valuation word `(1, …, 1, r+1)`.
* **(B) `letter i = stratum(y_(i+1)) = stratum(x_exit(i)) = (m_(+,i), s_(i+1))`** — what `13.2.1`
  names as *the letter*, what `13.2.4` defines (`ℓ_n = stratum(G^(n+1)(x))`), and what `13.6.3`(i)(a)
  fixes. `13.2.4`'s `S_n = Σ_(i<n)(m_i + r_i)` is (B)'s word.
* **(C) `letter i = (m_i, s_(i+1))`** — block `i`'s own `m` with block `i+1`'s `s`. Not a door
  stratum, defined on no page. It is the pairing `13.2.3`'s clause "`r_i = s_(i+1)`" reads as if left
  on its own, and it is the *only* reading under which the printed `s_n − s_0` is right.

**The symbol collision.** Under (A), `m_i = v_2(y_i + 1)`; under (B), `m_i = v_2(y_(i+1) + 1)`. So
`13.2.3`'s bare `m_i` in `Σ_(i<n)(m_i + s_i)` is `13.2.4`'s `m_(i−1)`, and `13.2.3` uses `m` in both
senses in one paragraph — "a letter occupying `m_n` of its steps" is (B), the budget sum is (A). This
is the root of the whole business and is what `11.12` now records.

### 1.3 The gap, exactly

`S^bud_n` (budget, (A)'s word, letters `y_0 … y_(n−1)`) against `S^let_n` (`13.2.4`, (B)'s word,
letters `y_1 … y_n`) — the same `n` letters shifted by one, so

```text
S^let_n − S^bud_n  =  (exponent of stratum(y_n))  −  (exponent of stratum(y_0))
                   =  (m_n + s_n) − (m_0 + s_0).
```

The printed `s_n − s_0` drops both `m` terms. They cancel only under (C).

### 1.4 Verified numerically, from the definitions

Fresh code, seed `70701`, `300` uniform odd starts at `b = 300`, `n = 40`, big-integer arithmetic
throughout:

| check | result |
|---|---|
| `x_exit(i) = G^(i+1)(x)` at every `i ≤ n+1` | `0` failures |
| `stratum(G^i(x)) = (m_i, s_i)` at every `i ≤ n+1` | `0` failures |
| `x_exit(k−1) = T_1^(S^bud_k)(x)`, run literally, every `k ≤ n` | `0` failures |
| gap `= (m_n + s_n) − (m_0 + s_0)` | **`300`/`300`** |
| gap `= s_n − s_0` (as printed) | `87`/`300` |
| `m_0 = m_n` | `87`/`300` — the same `87` starts |

The corrected identity held again on `500` further starts, `200` each at `b = 400` (`T = 80`) and
`b = 800` (`T = 160`) and `100` at `b = 1600` (`T = 320`), seed `90211`: `500`/`500`.

**The fix delegate was right about statement 1**, including the `87`/`300` figure, which reproduced
exactly. The direction is (letter − budget), matching the printed sentence's own sign.

---

## 2. Statement 1 — the repair chosen, and why

**Chosen: fix the identity in `13.2.3`, in `13.2.3`'s own notation.** Not the definition, and not a
convention-independent restatement.

*Why.* The sentence's own first clause already says the two counts "differ by **one letter at each
end**". `(m_n + s_n) − (m_0 + s_0)` is that clause written out; `s_n − s_0` is one *component* of one
letter at each end. So the repair makes the sentence agree with itself, changes one formula and its
supporting bound, and touches no definition and no other page. It is also the reading `13.2.4`(g)
already uses — (g) says the budget count exceeds the letter count "by at most the total exponent
`m_0 + s_0` of the start's own block", which is `(m_0 + s_0) − (m_n + s_n) ≤ m_0 + s_0` exactly. After
the repair `13.2.3` and (g) agree term for term instead of by luck.

Fixing the *definition* instead was rejected: `13.2.3`'s indexing is (A) and `13.2.4`'s is (B), and
moving either is the standardization round the brief forbids (§7).

**The negligibility clause follows the correction.** A whole letter's total exponent, not one
component, has to be bounded, so the clause now uses the one-letter law `13.2.4`(g) already carries:

```text
P_B(m + r >= t) = t*2^(1-t)   =>   max_(n <= T_N) (m_n + s_n) <= 3 log2 T_N
                                   off B-mass  (T_N+1)*t*2^(1-t) <= 12 log2 T_N / T_N^2.
```

Arithmetic, checked: `t·2^(1−t)` is decreasing for `t ≥ 2` (so the ceiling on `t = 3log₂T_N` only
helps), and `(T_N + 1)/T_N³ ≤ 2/T_N²` for `T_N ≥ 1`. Evaluated at `T_N = 10, 20, 40, 80, 160, 320,
640` the union bound is `2.15e−1, 6.67e−2, 2.00e−2, 5.87e−3, 1.69e−3, 4.78e−4, 1.34e−4` against
`3.99e−1, 1.30e−1, 3.99e−2, 1.19e−2, 3.43e−3, 9.75e−4, 2.73e−4` — a factor of two of slack in every
row. On real starts the maximum exceeded `3 log₂ T_N` on `1`/`200` at `(b, T) = (400, 80)` and `0` at
`(800, 160)` and `(1600, 320)`, against the bounds `0.0119`, `0.0034`, `0.0010`. The one-letter law
itself was re-checked by exact rational convolution of two geometric(1/2) at every `t ≤ 20`: `0`
mismatches. `3 log₂ T_N` at `T_N = ⌈θ log₂ N⌉` is still `O(log log N)` against a budget of
`Θ(log N)`, so the clause's conclusion is unchanged.

No number in `13.2.4`'s Verified line moves: the one-letter law is already recorded there, and the
new bound is arithmetic on it, not a measurement.

---

## 3. Statement 2 — verified, and **not** as reported

**The off-by-one is real.** `13.2.4` sets `ℓ_n = stratum(y_n) = stratum(G^(n+1)(x))`, so
`(ℓ_0, …, ℓ_(n−1))` is the letter word of `x` with its **first** letter deleted. (a)'s proof invokes
`14.15.1.5`, whose Definition `14.15.1.2` starts the word at `stratum(y)` for the sampled `y` itself.
Confirmed against both statements as printed.

**It is not harmless.** The followers of a word `W` are one class mod `2^(S(W)+1)` — but the starts
whose word *after* deleting the first letter is `W` are a countable union, one class
mod `2^(m+r+S(W)+1)` per leading letter `(m, r)`, by `14.15.1.3`(ii)'s affine level shift. Their total
Haar mass is still `2^(−S(W))`, so nothing is wrong with the *conclusion*; what is wrong is the
**error term**, which has to charge for the leading letter's own exponent. So (a)'s tail term is one
letter short.

**Measured, exactly, at the case the page itself singles out.** (a) says "For `N = 2^b` and `J = b`
the first term is `0`", i.e. `TV(Law(ℓ_0, …, ℓ_(n−1)), B^(⊗n)) ≤ P_B(S_n ≥ b)` when `x` ranges over
*every* odd integer of `[2^b, 2^(b+1))`. Total variation computed exactly, in rationals, over all
`2^(b−1)` starts:

| `b` | `n` | TV under (A) | TV under (B), as `13.2.4` defines | printed bound `P_B(S_n ≥ b)` | (B)/bound |
|---|---|---|---|---|---|
| 16 | 1 | `743/2^21` = `3.543e−4` | `2279/2^20` = `2.173e−3` | `1/2^11` = `4.883e−4` | **`4.45`** |
| 20 | 1 | `227/2^23` = `2.706e−5` | `685/2^21` = `3.266e−4` | `5/2^17` = `3.815e−5` | **`8.56`** |

Reading (A) is inside the printed bound at every `(b, n)` tested — `b = 12, 16, 20` and every
`n ≤ 5, 7, 9` respectively, `21` cells, `0` violations. Reading (B) violates it at every small `n`
(`n = 1, 2, 3` at `b = 12`; `n = 1 … 4` at `b = 16`; `n = 1 … 5` at `b = 20`) and satisfies
`P_B(S_(n+1) ≥ b)` in all `21`. That is the signature of exactly one missing letter.

**So `13.2.4`(a) is false as printed**, by a factor `2.82` at `b = 12`, `4.45` at `b = 16` and `8.56`
at `b = 20` — growing with `b`. The honest tail term is `P_B(S_(n+1) ≥ J)`.

**No conclusion of `13.2.4` is at stake**, which is why this was invisible: (b)'s identity is general
in `n`; `(g)`'s rate `I(θ, τ) = τ(log 2 − H(2θ/τ))` is the same limit at `n = T_N + 1` as at `T_N`;
`δ_N` is still `e^(−Θ(b))`; (c)–(f), Corollary `13.2.4.1` and Theorem `13.6.4` read identically. What
is wrong is one printed index in one printed bound.

**Why it was not fixed.** Both available repairs move something the brief put out of scope:

1. **Move the definition to (A)** (`y_n = G^n(x)`). (a) then becomes exactly `14.15.1.5` with *no
   change to (a)'s printed text*, (c)'s `log₂(y_n + 1) > log₂ N − S_n` becomes exact from `y_0 = x`,
   and `13.2.3`'s gap collapses to `0`. But `13.2.4`'s word is then `13.2.1`'s shifted by one, so
   Corollary `13.2.4.1`'s "`13.2.1`'s tallied word **is** the letter word of `13.2.4`(d)" stops being
   an identity — `13.2.4.1` moves.
2. **Keep (B) and repair (a)'s bound**: `P_B(S_n ≥ J)` → `P_B(S_(n+1) ≥ J)`, plus one clause in (a)'s
   proof naming the start's own letter. Nothing else in `13.2.4`, `13.2.4.1` or `13.6.4` needs a word
   changed — I checked each. But (a) itself moves.

The brief's instruction is explicit: *"If any of them moves, STOP and report; that would be outside
the authorized scope."* The authorization rested on the finding that statement 2 is harmless, and it
is not. **Stopped, reported, and landed as the open item.** Repair 2 is the smaller of the two and is
what `11.12` names as the cost of keeping (B).

---

## 4. Nothing downstream moved

Checked against the committed text, not from memory.

| item | status after the `13.2.3` edit |
|---|---|
| `13.2.4`(g), offset clause | **Unaffected, and now in exact agreement.** (g) bounds budget − letter by `m_0 + s_0`; the corrected gap gives budget − letter `= (m_0 + s_0) − (m_n + s_n)`, and `m_n + s_n ≥ 2 > 0`. Under (A) the excess is `0 ≤ m_0 + s_0`; under (C) it is `s_0 ≤ m_0 + s_0`. Still true under all three readings, as designed. |
| `13.2.4`(g), rate clause and second bullet | Not touched, no dependence on the gap formula. |
| `13.2.4`(a)–(f) | Not touched. (a)'s independent defect is §3, present before this pass and unchanged by it. |
| Corollary `13.2.4.1` | Not touched; cites (g)'s density conclusion only. |
| Theorem `13.6.4` | Not touched; the equivalence is index-free (bulk frequencies at every offset window). |
| `13.6.3`(i)(a) | Not touched. Its "fixed one-index offset" is still what `13.2.3`'s closing sentence points at, and is now the *only* offset claim on the page. |
| `13.3.2` | Byte-identical. Verified: `git diff 2ec9702 132cb4d -- aeh.md` is one hunk, in `13.2.3`. |
| `13.2.1`, `13.2.2`, `13.2.5`, `13.3.1`, `13.3.3`, `13.4`–`13.6` | Not touched. |
| Every other tracked page | `git grep` at `132cb4d` over all tracked `.md` (excluding `briefs/`, `archive/`, `sources/`) for `s_n − s_0`, `one letter at each end` and `one-index offset` returns `aeh.md` L69 and L178 only — `s_n − s_0` now nowhere at all. L178 is `13.6.3`(i)(a)'s own phrase and is unchanged. No page restates the gap. |
| the paper | No prose change beyond the pin token; `pdftotext` of the two builds differs on exactly one line. The paper never states the gap formula. Its Section 5 claims rest on `13.2.4`(g)'s in-budget conclusion and on `13.2.3`'s admissibility clause, neither of which moved. |

`aeh.md` front matter: `updated:` was already `2026-08-03`; no `status:` field changed; no anchor
renumbered; nothing pruned; the deferred prefix result is claimed nowhere; `13.2.6` appears in no
tracked page.

---

## 5. The open item, as landed

`open-problems.md` **`11.12`. Which door-letter indexing the record standardizes on** — one item, one
question, closure checkable in either direction, pointing at `briefs/v3r4-fix-findings.md` §3.3 and §8
for the measurements. It names the three readings and where each is used; records that the budget
sum's `m_i` is `13.2.4`'s `m_(i−1)`, so one symbol carries two meanings inside `13.2.3`; records §3's
counterexample to (a) as printed with the exact rationals; and prices both directions — (A) costs
restating `13.2.1`'s letter, `13.6.3`(i)(a), `13.2.4.1` and the seam sentence at reverse.md `14.14.6`;
(B) costs one index in `13.2.4`(a). Front-matter `scope:` extended to name `11.12`; `updated:` was
already `2026-08-03`.

**One tension, flagged deliberately.** `11.12` now records on a tracked page that `13.2.4`(a)'s
printed bound does not hold, while `13.2.4` itself still prints it. That is a cross-page mismatch of
the kind `AGENTS.md`'s periodic status pass is meant to catch, and it is the honest state of the
record until the standardization round runs: the alternative was to leave a demonstrably false bound
with no tracked trace of it anywhere. `aeh.md`'s "base case PROVED at 13.2.4" is *not* overturned —
every conclusion of the lemma survives repair 2 verbatim — but a reader of `11.12` should not be left
to discover the mismatch.

---

## 6. The pin, and the build

`a1f2ac3` → **`132cb4d`**, the record commit, in its own commit `0352bf9`, which touches the pin
string and the rebuilt PDF and nothing else.

**Verified at `132cb4d`**, by resolving every wiki section and script the `.tex` names against
`git show 132cb4d:<path>` — never against the working tree.

* **All ten named files present**: `aeh.md`, `cycles.md`, `itinerary.md`, `stage3.md`, and
  `experiments/{period1,period2,period3}_cycles.py`, `one_step_propagation.py`,
  `anchor_increment.py`, `absorption_law.py`.
* **Every named anchor resolves**, matched on its own heading or numbered-result text rather than on
  the bare number: `aeh.md` §13.1, §13.2.3, Lemma 13.2.4 with item (g), Corollary 13.2.4.1,
  Proposition 13.2.5, §13.3.2, §13.4, §13.5, Lemma 13.6.3 with items (iii) and (v), Theorem 13.6.4,
  Proposition 13.6.5; `itinerary.md` Theorem 14.15.1.5; `stage3.md` §11.8.6.3; `cycles.md` §§12.2.3,
  12.5.2, 12.5.3, 12.6.1, 12.6.2, 12.7.4, 12.7.5, 12.8.6 — all eight.
* **Positively on this round's change**: `13.2.3`'s corrected gap, the "two of the budget sum's own
  summands" clause, the whole-letter maximum `3 log₂ T_N` and its `B`-mass are all at the pin, as are
  `11.12` and its pointer to `briefs/v3r4-fix-findings.md`.
* **Negatively**: `The gap is exactly s_n − s_0`, `max_(n ≤ T_N) s_n ≤ 2 log₂ T_N` and `a difference
  of two geometric letters` are gone; and the earlier rounds' removals — `this page's own hypothesis`,
  `positive precisely for`, `which δ_N absorbs`, and any mention of the deferred `13.2.6` — are still
  absent, so no pointer dangles.
* **Round 4's earlier material still present at the pin**: (g)'s `m_0 + s_0` clause, the one-letter
  law, `aeh_budget_clause.py` in the Verified line, `13.3.2`'s restated attribution, and
  `publication.md`'s corrected clause.
* The two historical pins in the published version-note text — `72ec88e` and `9d9d1ec`, both naming
  `cycles.md` §12.8.6 — are untouched, correctly: they record what a published version said.

**Build.** Clean rebuild in `paper/`, `.aux`/`.log`/`.out` deleted first:

| | |
|---|---|
| passes | 3 `pdflatex -halt-on-error -interaction=nonstopmode`, all exit `0` |
| pages | **17** |
| overfull boxes | **0** |
| underfull boxes | **1** — `\hbox (badness 1067)` at L489–490, the `lagarias` bibitem inside `\thebibliography`. Pre-existing, identical badness to the previous two builds. |
| unresolved references | **none**; the log contains no `LaTeX Warning` line of any kind, no undefined reference or citation, no rerun request |
| PDF | `434,156` bytes (previous build `434,144`) |

**Confirmed from the built artifact**, not from the source: `pdftotext -layout` finds `cited at commit
132cb4d` exactly once and `a1f2ac3` zero times, and diffing the new extraction against the previously
committed PDF's extraction returns **one changed line — the pin token**. No prose change beyond it.

---

## 7. Found and not fixed

1. **`13.2.4`(a) is false as printed** — §3, with exact counterexamples. Handed back per the brief's
   stop clause; both repairs are priced in `11.12`. The smaller is
   `P_B(S_n ≥ J)` → `P_B(S_(n+1) ≥ J)` in (a), plus one clause in its proof.
2. **`13.2.4`(c) is short by the same letter under (B).** `log₂(y_n + 1) > log₂ N − S_n` is proved by
   chaining `y_(i+1) + 1 > (y_i + 1)(3/2)^(m_i)2^(−r_i)` from `y_0`; under (B), `y_0 = G(x)` and the
   chain starts one letter down from `x`, so the printed inequality needs `S_n` plus the start's own
   letter. The *conclusion* (`0` failures over `72,000` and `115,200` steps, per the Verified line) is
   unaffected — the altitude bound of `13.2.3` is a second, independent derivation with
   `(3/2)^(Σm)` of slack — and under (A) the printed line is exact. Not fixed, same reason as 1;
   folded into `11.12`'s (A)-side accounting.
3. **`13.2.3` uses `m` in two senses in one paragraph** (§1.2). Not fixable without choosing a
   convention. Recorded in `11.12`; the corrected gap clause is worded so that its `m` is
   unambiguously the budget sum's own (`a difference of two of the budget sum's own summands`).
4. **`13.2.1` has the same collision**, between its `ℓ_n = (m_(+,n), s_(n+1))` and its
   `S_n = Σ_(i<n)(m_i + s_i)`. The two are correct as written — the clock identity holds exactly with
   the second reading, `0` failures — but the bare `m_i` is not the `m_+` two clauses earlier.
   Recorded in `11.12`.
5. **Reading (C) is defined nowhere** and was reachable only through `13.2.3`'s printed identity,
   which is now gone. Nothing else in the record depends on it; the `git grep` of §4 confirms it.
6. **`13.2.3`'s `max` clause supports its own claim only.** After the repair it bounds the whole
   letter, which is what the corrected gap needs. `13.2.4`(g) does not use it — (g) bounds
   `m_0 + s_0` directly through the one-letter law — so the two passages no longer look like they
   should match and do not need to.
7. **Not pruned; no anchor renumbered; nothing in `13.3.2` touched; the deferred prefix result is
   claimed nowhere; no change log or dated journal added to any tracked page.** Re-checked at the pin.
