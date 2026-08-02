# Findings: Lemma `13.2.4`(a)'s tail term (v3 round 4, final pass)

**Branch.** `v3r4-review-round4`. Base `53975e2`; two commits added:

| commit | contents |
|---|---|
| `03207fe` | record: `aeh.md` `13.2.4`(a) and (c) and its Verified line, `open-problems.md` `11.12`, `experiments/aeh_word_shift.py` |
| `c964d7d` | Appendix A pin `132cb4d` → `03207fe`, rebuilt PDF |

No push, no merge, no rebase, no branch switch, no worktree. Every file written with the Write/Edit
tools; no PowerShell redirection touched any file; both edited pages re-checked byte-wise afterwards
(no BOM, no mojibake, `≤ − ₂ ⊗ ℓ δ θ τ 𝒢` all intact).

**The repaired bound holds, at every number measured.** `13.2.4`(a) now reads
`TV(Law(ℓ_0, …, ℓ_(n−1)), B^(⊗n)) ≤ 2^(J+2)/N + P_B(S_(n+1) ≥ J)`. §3 has the numbers.

---

## 1. Which word (a) is about, established from the definitions

Not from the brief and not from either previous delegate. The chain is four definitions long:

* **itinerary.md `14.15.1.1`** — `stratum(y) = (m, r)`, `m = v₂(y+1)`, `q = (y+1)/2^m`,
  `r = v₂(3^m q − 1)`; and **reverse.md `14.14.3.1`** — `G(y) = (3^m q − 1)/2^r`.
* **itinerary.md `14.15.1.2`** — `y` *follows* `W = ((m_0,r_0), …, (m_(n−1),r_(n−1)))` if, **writing
  `y_0 := y`**, `y_(i+1) := G(y_i)`, `stratum(y_i) = (m_i, r_i)` for `i = 0, …, n−1`. So the word
  `14.15.1.5` counts **starts at the sampled integer itself**.
* **aeh.md `13.2.4`**, its own printed sentence — `y_(−1) = x`, `y_n = G^(n+1)(x)`,
  `ℓ_n = stratum(y_n)`. Hence `ℓ_0 = stratum(G(x))`, and

```text
(ℓ_0, …, ℓ_(n−1))  =  (stratum(G(x)), stratum(G²(x)), …, stratum(G^n(x)))
                   =  the letter word of x with its FIRST letter deleted.
```

That is the answer: **(a)'s word is the length-`n` letter word of `G(x)`, not of `x`.** The letter
`14.15.1.5` charges for and (a) does not is `stratum(x)` itself. Equivalently, in the naming
`open-problems.md` `11.12` uses (`y_i = G^i(x)`), `13.2.4`'s letter `i` is `stratum(y_(i+1))` —
reading (B) — while `14.15.1.5`'s is `stratum(y_i)` — reading (A). The external reviewer's advice
that `S_n` is "the natural sharp form" is right about reading (A) and wrong about the reading
`13.2.4` prints.

**Why the shift costs a letter, exactly.** `x` has word-after-one-`G`-step equal to `W` iff `x`
follows the **extended** word `(u, W)` for its own leading letter `u = stratum(x)`. By `14.15.1.5`
applied to `(u, W)`, those `x` are one class mod `2^(|u|+S(W)+1)` — *not* mod `2^(S(W)+1)`. Summing
over `u` gives total mass `Σ_(m,r≥1) 2^(−(m+r))·2^(−S(W)) = 2^(−S(W))`, so the **conclusion** is
untouched; what moves is the **modulus**, hence the budget `J` the cylinder count needs, hence the
error term. Verified exhaustively over all odd `x < 2^18`: `495` `(u, W)` cells, each exactly one
class mod `2^(|u|+S(W)+1)`, `0` failures; and over all leading letters at once, the `28` words with
`S(W) ≤ 8` meet between `4` and `37` distinct classes mod `2^(S(W)+1)` — never one.

**Two supporting identities re-derived, not assumed**: `G = T^(v₂(y+1))` (reverse.md `14.14.7.1`) on
`2,000` random doors, `0` failures; and the clock identity `x_exit(k−1) = T_1^(S_k)(x)` run
literally under the one-division map at `2,000` `(start, k)` pairs, `0` failures — confirming that
`13.2.3`'s budget sum runs over reading (A)'s word, the collision `11.12` records.

## 2. The repair

**(a), the narrow repair, as authorized.** Tail term restored to `P_B(S_(n+1) ≥ J)`, plus the proof
clause naming the start's own letter. The proof now runs:

> the word begins one `G`-step past the start, so the word `14.15.1.2` reads at `x` is the extended
> word `ℓ^+ = (stratum(y_(−1)), ℓ_0, …, ℓ_(n−1))` of `n + 1` letters; `14.15.1.5` gives atom-by-atom
> agreement with `B^(⊗(n+1))` on `{S(ℓ^+) + 1 ≤ J}`, whose complement has `B`-mass
> `P_B(S_(n+1) ≥ J)`; and (a)'s word is a marginal of `ℓ^+`, whose total variation it cannot exceed.

Note `S_(n+1)` is used as a `B`-probability, where all `n + 1` letters are i.i.d., so it names the
same number as the extended word's own exponent. The alternative repair (moving the letter
definition to reading (A)) was not attempted: it is out of scope and breaks `13.2.4.1`.

**Nothing in (b), (d)–(g), Corollary `13.2.4.1` or Theorem `13.6.4` needs a word.** Checked against
the committed text, one by one, and the structural reason is that **the repair only enlarges the
bound**, so every statement that consumes (a) as an *upper* bound survives:

| item | status |
|---|---|
| (b) | The identity `P_B(S_n ≥ J) = P(Bin(J−1,1/2) < 2n)` is general in `n`, so it covers `n+1` as printed. "Both terms of (a) are `e^(−Θ(b))`" survives: `P(Bin(J−1,1/2) < 2(n+1))` and `P(Bin(J−1,1/2) < 2n)` differ by a factor polynomial in `b`, and `2(⌈θb⌉+1)/J → 2θ/(1−η)` is the same limit. |
| (d), (e) | Consume `δ_N` as an upper bound only; `δ_N` is now larger. |
| (f) | Scope statement, no index. |
| (g) | `P(S_(T_N) ≥ Λ_N) ≤ 2δ_N(τ)` still holds: `P ≤ P_B(S_(T_N) ≥ Λ_N) + TV ≤ P_B(S_(T_N+1) ≥ Λ_N) + δ_N(τ) ≤ 2δ_N(τ)`. The rate `I(θ, τ)` is the same at `n = T_N + 1` as at `T_N`. The offset parenthetical transfers the one-letter law "through (a) at `n = 1`", which the repaired (a) still does (at `n = 1` its tail is the two-letter mass). |
| `13.2.4.1` | Cites (g), (d), (e) — no index. |
| `13.6.4` | Index-free (bulk frequencies at every offset window). |
| `13.2` display at L61 | `TV(Law(letter word of x), B^(⊗n)) ≤ 2^(J+2)/N + P_B(S_n ≥ J)` — correct **as printed**, because it names the letter word *of `x`*, reading (A). It and (a) now differ by exactly one letter in both the word and the tail, consistently. Not touched. |

**(c), same repair.** §4.

## 3. The numerical proof

`experiments/aeh_word_shift.py` — **new file**, chosen over extending `aeh_budget_clause.py` because
it supports a different statement of `13.2.4` (the word of (a) and the altitude line of (c)) rather
than (g)'s budget clause, and because a fresh file makes "imports nothing" checkable at a glance. It
imports nothing from `experiments/`; `stratum`, `G`, `T`, `T_1`, the Bernoulli law and the tail law
are rebuilt from the record's definitions.

**Method.** For every odd `x` of `[2^b, 2^(b+1))` — *all* `2^(b−1)` of them, not a sample — iterate
`G` and record both readings' length-`n` words. Total variation against `B^(⊗n)` is computed
**exactly**: all masses put over a common power of two, integer arithmetic, and the `B`-mass of the
never-realized words added in full. This is the case (a) itself singles out (`N = 2^b`, `J = b`,
where (a)'s window term is `0`), so the bound under test is the bare tail term.

| `b` | `n` | true TV, `13.2.4`'s word | `n`-letter tail `P_B(S_n ≥ b)` | ratio | **`(n+1)`-letter tail `P_B(S_(n+1) ≥ b)`** | holds |
|---|---|---|---|---|---|---|
| 16 | 1 | `2279/2^20` = `2.173424e−3` | `1/2^11` = `4.883e−4` | **`4.45`** | `9/2^9` = `1.7578e−2` | **yes** |
| 20 | 1 | `685/2^21` = `3.266335e−4` | `5/2^17` = `3.815e−5` | **`8.56`** | `145/2^16` = `2.2125e−3` | **yes** |
| 24 | 1 | `2163/2^26` = `3.223121e−5` | `3/2^20` = `2.861e−6` | **`11.27`** | `1/2^12` = `2.4414e−4` | **yes** |
| 24 | 2 | `32261685/2^35` = `9.389386e−4` | `1/2^12` | `3.85` | `5569/2^20` = `5.3110e−3` | yes |
| 24 | 3 | `24942629851/2^41` = `1.134259e−2` | `5569/2^20` | `2.14` | `763/2^14` = `4.6570e−2` | yes |

`b = 24` is the larger scale (`8,388,608` starts, exact rationals throughout). The full sweep is
`b = 12, 16, 20` at `n ≤ 5` and `b = 24` at `n ≤ 3` — **`18` cells**:

* the repaired tail `P_B(S_(n+1) ≥ b)` holds in **all `18`**;
* the printed tail `P_B(S_n ≥ b)` is exceeded in **`15`** of them (`b = 12`: `n = 1,2,3`; `b = 16`:
  `n = 1..4`; `b = 20`: `n = 1..5`; `b = 24`: `n = 1..3`), with the factor at `n = 1` growing
  `2.82 → 4.45 → 8.56 → 11.27` in `b`;
* the proof's own chain `TV_B(n) ≤ TV(Law(ℓ^+), B^(⊗(n+1))) ≤ P_B(S_(n+1) ≥ b)` holds in all `18` —
  both the marginal step and the cylinder step, separately;
* the control, reading (A)'s word — the start's own — is inside `P_B(S_n ≥ b)` in all `18`, which is
  what `14.15.1.5` requires and what says the code is measuring the right thing;
* general (non-dyadic) windows `[N, 2N)` at `(N, J) = (1000003, 14)` and `(700001, 12)`, `n ≤ 3`:
  the full bound `2^(J+2)/N + tail` holds with either term (the window term dominates there, so
  these are supporting rather than discriminating);
* the tail identity `P_B(S_n ≥ J) = P(Bin(J−1,1/2) < 2n)` re-checked by exact rational convolution of
  the one-letter law `P(m + r = t) = (t−1)2^(−t)` at `16` `(n, J)` pairs, `0` mismatches — so the
  bound being compared against is not itself taken on trust.

**No cell violates the repaired bound.** The stop clause did not fire.

## 4. `13.2.4`(c) — verdict: the previous pass was right, and the line is now fixed

**The printed line was false.** `log₂(y_n + 1) > log₂ N − S_n` is proved by chaining
`y_(i+1) + 1 > (y_i + 1)(3/2)^(m_i)2^(−r_i)` from `y_0`; under `13.2.4`'s own indexing `y_0 = G(x)`,
so the chain starts one letter below `x` and the printed inequality is short by `stratum(x)`'s own
exponent. Measured: **`226` failures in `5,000` steps** (`200` uniform odd starts at `b = 400`,
`n ≤ 25`, seed `93003`).

**Fixed the same way**, inside (c) and nowhere else:

```text
log₂(y_n + 1)  >  log₂ N − (m_(−1) + r_(−1)) − S_n ,   (m_(−1), r_(−1)) = stratum(x) = stratum(y_(−1))
```

`0` failures in the same `5,000` steps. The subtracted quantity is the total exponent of exactly the
`n + 1` letters (a) now charges for, so (c)'s "off a set of starts of density `≤ δ_N`" reads with the
repaired `δ_N` and needs no other change — and the corrected line is now **term-for-term** `13.2.3`'s
altitude bound `log₂ x_exit(n−1) ≥ log₂ x − S_n` read in door coordinates, since `13.2.3`'s budget
count over `n + 1` blocks is exactly `(m_(−1) + r_(−1)) + S_n`. (c)'s own closing parenthetical
already says the two are independent derivations of the same thing; they now agree exactly rather
than by slack. **Nothing beyond (c) moved** — the conclusion, the `ω_+` clause and the `δ_N` bound
are as printed. `13.2.4`'s Verified line records `0` failures for (c) over `72,000` and `115,200`
steps; those runs test the **conclusion** (exits above `N^η`), which the printed altitude line
over-delivered on because `13.2.3` covers it with `(3/2)^(Σm)` of slack, and they are unaffected.

## 5. `11.12` as it now reads

Title, structure and the three-readings paragraph are unchanged. What changed:

* The **resolved defect is gone.** The sentence "(a)'s tail term is then one letter short, and the
  printed bound does not hold" is replaced by "(a)'s tail term has to run over `n + 1` letters, and
  `13.2.4`(a) and (c) are written that way", quoting the repaired bound and naming (c)'s explicit
  `stratum(x)`.
* The **measurements stay**, reframed as the price of the convention rather than as a defect: the
  same exact rationals at `b = 16, 20`, now with `b = 24` added, against both tail terms, plus
  reading (A)'s control values. The pointer now names `experiments/aeh_word_shift.py` alongside
  `briefs/v3r4-fix-findings.md` §3.3 and §8.
* "(c)–(f) read identically either way" → **"(d)–(f)"**, since (c) did move.
* The pricing sentence is past tense: keeping (B) "costs the extra letter now carried in
  `13.2.4`(a)'s tail term and `13.2.4`(c)'s altitude line … that price is paid, so what is open here
  is the convention and not a defect."
* The **open question is untouched**: three readings, one symbol collision, `(A)`'s cost (`13.2.1`'s
  letter, `13.6.3`(i)(a), `13.2.4.1`, reverse.md `14.14.6`'s seam sentence), `(C)` not a candidate,
  and the same closure test. **No cross-page tension remains**: no tracked page now says a printed
  bound of `13.2.4` fails.

## 6. The pin, and the build

`132cb4d` → **`03207fe`**, the record commit, in its own commit `c964d7d`, which touches the pin
string and the rebuilt PDF and nothing else (`git show --stat`: `2` files, `1` insertion,
`1` deletion in the `.tex`).

**Verified at `03207fe` by `git show`, never against the working tree.**

* **All ten named files present**: `aeh.md`, `cycles.md`, `itinerary.md`, `stage3.md`,
  `experiments/{period1,period2,period3}_cycles.py`, `one_step_propagation.py`,
  `anchor_increment.py`, `absorption_law.py`.
* **Every named anchor resolves**, matched on its own heading or numbered-result text: `aeh.md`
  §13.1, §13.2.3, Lemma 13.2.4 with item (g), Corollary 13.2.4.1, Proposition 13.2.5, §13.3.2, §13.4,
  §13.5, Lemma 13.6.3 with items (iii) and (v), Theorem 13.6.4, §13.6.5; `itinerary.md`
  Theorem 14.15.1.5; `stage3.md` §11.8.6.3; `cycles.md` §§12.2.3, 12.5.2, 12.5.3, 12.6.1, 12.6.2,
  12.7.4, 12.7.5, 12.8.6 — all eight.
* **Positively, on this round's change**: (a)'s `P_B(S_(n+1) ≥ J)`, the extended-word proof clause,
  (c)'s `log₂ N − (m_(−1) + r_(−1)) − S_n`, `experiments/aeh_word_shift.py` in the Verified line with
  its `2163/2^26` and seeds `93001`–`93003`, and `11.12`'s revised text and pointer — all at the pin.
* **Negatively**: `B^(⊗n)) ≤ 2^(J+2)/N + P_B(S_n ≥ J)` and `log₂(y_n + 1) > log₂ N − S_n` are gone
  from `aeh.md`; `the printed bound does not hold`, `(a)'s tail term is then one letter short` and
  `P_B(S_n ≥ J) becomes` are gone from `open-problems.md`; and the earlier rounds' removals —
  `The gap is exactly s_n − s_0`, `this page's own hypothesis`, any mention of the deferred `13.2.6` —
  are still absent, so no pointer dangles.
* **Earlier round-4 material still present at the pin**: (g)'s `m_0 + s_0` clause, the one-letter law
  `P_B(m + r ≥ t) = t·2^(1−t)`, `13.2.3`'s corrected gap and its `3 log₂ T_N` whole-letter maximum,
  `aeh_budget_clause.py` in the Verified line.
* The two historical pins in the published version-note text — `72ec88e` and `9d9d1ec`, both naming
  `cycles.md` §12.8.6 — are untouched, correctly: they record what a published version said.
* `13.3.2` is **byte-identical** across the record commit (compared section text at `53975e2` and
  `03207fe`); the heading list of `aeh.md` is identical, so no anchor was renumbered; `git diff` is
  three changed lines in `aeh.md` (the (a) line, the (c) line, the Verified line) and three in
  `open-problems.md`, plus the new script. Nothing pruned; the deferred prefix result is claimed
  nowhere; no change log or dated journal added to any tracked page.

**Build.** Clean rebuild in `paper/`, `.aux`/`.log`/`.out` deleted first:

| | |
|---|---|
| passes | 3 × `pdflatex -halt-on-error -interaction=nonstopmode`, all exit `0` |
| pages | **17** |
| overfull boxes | **0** |
| underfull boxes | **1** — `\hbox (badness 1067)` at L489–490, the `lagarias` bibitem inside `\thebibliography`. Pre-existing, identical badness to the previous builds. |
| unresolved references | **none**; the log contains no `LaTeX Warning` line of any kind, no undefined reference or citation, no rerun request |
| PDF | `434,266` bytes (previous build `434,156`) |

**Confirmed from the built artifact**, not from the source: `pdftotext -layout` finds
`cited at commit 03207fe` exactly once and `132cb4d` zero times, and diffing the new extraction
against the previously committed PDF's extraction returns **one changed line — the pin token**.

## 7. Found and not fixed

1. **(c)'s "off a set of starts of density `≤ δ_N`" is loose by a factor `2`.** The event is
   transferred through (a), so the honest constant is `2δ_N`, exactly as `13.2.4`(g) writes it for
   its own analogue (`P(S_(T_N) ≥ Λ_N) ≤ 2δ_N(τ)`). This looseness is **pre-existing and unchanged**
   by this pass — it is the same factor before and after the repair, and both sides are `e^(−Θ(b))`
   — so it was left alone rather than folded into an authorized one-line fix. Cheap to close if
   wanted: `δ_N` → `2δ_N` in (c), one token.
2. **`13.2` L61's display and `13.2.4`(a) now carry different tail indices** (`S_n` against
   `S_(n+1)`). Both are correct: the display is about the letter word *of `x`* and (a) is about the
   word one `G`-step on. A reader who does not notice that the two sentences name different words
   will read it as an inconsistency. Fixing it means fixing the convention — `11.12`, out of scope.
3. **The symbol collisions `11.12` records are unchanged** — `13.2.3`'s bare `m_i` is `13.2.4`'s
   `m_(i−1)`, and `13.2.1` carries the same collision between its `ℓ_n = (m_(+,n), s_(n+1))` and its
   `S_n = Σ_(i<n)(m_i + s_i)`. Both are true as written under their own readings; neither is fixable
   without choosing a convention. Recorded, not touched.
4. **`13.2.4` never names `ℓ_(−1)`.** (a)'s proof and (c) now both need the start's own letter, and
   both write it out (`stratum(y_(−1))`, `stratum(x) = (m_(−1), r_(−1))`) rather than extending the
   `ℓ` indexing to `−1`. Defining `ℓ_(−1)` once in the lemma's preamble would be tidier and is
   exactly the kind of change the standardization round should make, so it was not made here.
5. `briefs/v3r4-lemma-index-brief.md` and this file are left **uncommitted** in the working tree,
   following the pattern of the round's earlier passes, where the main session lands the briefs in
   its own `briefs:` commit.
