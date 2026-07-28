# Findings: two record defects repaired — the undefined `σ` in Prop 12.6.1, and the `p = 92` bound

Brief: `briefs/record-defects-repair-brief.md`. Branch `record-defects-repair`, base `82f0523`
(the worktree was cut at the stale `2225b68` and was rebranched onto `82f0523` before any work).
Verification: `experiments/record_defects_check.py`, **40 checks, 0 failures**, output committed at
`experiments/record_defects_check_output.txt` (2026-07-27). Fresh code per AGENTS.md: nothing is
imported from `uniform_trim.py`, `merle_round3_check.py` or any other committed script; the
reference implementation is transcribed inline and labeled as such.

---

## Defect 1 — `σ` undefined at its point of use in Proposition 12.6.1

### The convention, established independently

`σ_j = s_j + m_(j+1)`, indices cyclic. Three independent confirmations:

1. **The page's own preamble.** `cycles.md` line 12 (the §12 header paragraph) gives
   `σ_t = v_2(C_t)` and `m_(t+1) = σ_t - s_t`. Rearranged, that *is* `σ_t = s_t + m_(t+1)`. It is
   112 lines above Proposition 12.6.1 and states the relation only in the `m`-solved direction.
2. **The committed reference implementation.** `experiments/uniform_trim.py`'s `R_rot` accumulates
   `Spre += ss[t] + ms[(t+1) % p]`. Over 300 random profiles (`p ∈ [2,9]`, entries `∈ [1,12]`):
   `σ_j = s_j + m_(j+1)` agrees **300/300**; the natural local misreading `σ_j = m_j + s_j` agrees
   **2/300** and is wrong by up to **3.3 orders of magnitude**. (The main session measured 6/300 on
   its own draw; the difference is the draw, not the fact — the agreements are profiles where the
   shift happens to be a wash.)
3. **A recorded arithmetic fact.** Remark 12.6.1.1 records `gcd(q, R_r) = 7` at every rotation of
   `12.8.3`'s `p = 7` staircase seed (`n = 94`, `m = (4,7,9,15,23,35,1)`). The correct convention
   gives `{7}`; the misreading gives `{1}`.

### Why the guardrails do not catch it — stronger than the brief supposed

The brief expected the transport recurrence of Remark 12.6.1.1 to fail under the misreading. **It
does not.** Measured, `1685/1685` exact under *both* conventions, and the reason is a proof, not a
sampling accident:

> Telescoping `2^(σ_r) R_(r+1) = 3^(m_r) R_r + (2^(s_r) − 1)q`, the terms `t = 1..p−1` of the two
> sides match term by term with **every `σ` cancelling** between the prefactor `2^(σ_r)` and the
> difference `S_t − S'_(t−1)`. The sole residue is the wrap term, which requires exactly
> `2^(Σσ) = 2^K`. Both conventions are cyclic rearrangements of the same multiset `{m_j} ∪ {s_j}`,
> so both give `Σσ = Σs + n = K`, and both satisfy the recurrence identically.

The same argument makes **every** structural identity attached to 12.6.1 blind, because each
depends on `σ` only through `Σσ`. All four measured:

| guardrail | correct | misread | verdict |
|---|---|---|---|
| trivial cycle `m_t = s_t = 1` → `R = 4^p − 3^p` (12.6.1's own sanity identity), `p ∈ {1,2,3,4,7}` | passes | passes | **BLIND** |
| `K = Σ s_t + n` (a cyclic sum) | invariant | invariant | **BLIND** |
| transport recurrence, 12.6.1.1, `σ` read self-consistently | 1685/1685 | 1685/1685 | **BLIND** |
| ghost identity `v_2(3^(m_r) R_r − q) = s_r` (itinerary 14.15.9.4(1)) | 668/668 | 668/668 | **BLIND** |
| repetition multiplicativity `R_0(B^k) = G_k·R_0(B)` (12.6.1.4) | 120/120 | 120/120 | **BLIND** |
| recorded `gcd(q, R_r) = 7` at 12.8.3's `p = 7` seed | `{7}` | `{1}` | **DISCRIMINATES** |

So a reader implementing from the prose gets a silently wrong object that reproduces not merely the
one published canary but the whole structural apparatus of §12.6.1. What discriminates is any check
that pins `σ` to a quantity the implementation does not itself supply: the recorded `gcd`, or the
recurrence with `σ_r` **written out** as `s_r + m_(r+1)` rather than taken from the implementation.

### The repair

One clause added to Proposition 12.6.1 (`cycles.md`), commit `33af16d`. Nothing renumbered, no
mathematics restated, the proof untouched. Exact text added, in place, after `S_t = Σ_(j<t) σ_j`:

> `, with `σ_j = s_j + m_(j+1)` the step's `2`-valuation `v_2(C_j)` of the section preamble, indices
> cyclic — the shift is essential, `m_(j+1)` and not `m_j`.`

`experiments/uniform_trim.py`'s `R_rot` (correct as committed; not a behaviour change) gains a
docstring naming the convention and pointing at the canary.

### The canary

`experiments/record_defects_check.py` part 3, function `canary(R_impl, label)` — a rejector for any
candidate implementation of Prop 12.6.1, three tiers:

1. the published sanity identity, trivial cycle `m = s = 1` → `4^p − 3^p` at `p ∈ {2,3,4,7}`. Kept
   only to catch a wholly broken implementation first; **accepts both conventions**.
2. the transport recurrence of 12.6.1.1 at every rotation of the profile
   `m = (1,4,2,7,3)`, `s = (5,1,6,2,1)` — **unequal `m` and `s`** — with `σ_r` spelled out in the
   assertion as `s_r + m_(r+1)`. Spelling `σ` out is what makes it a test; the misreading fails
   here at `r = 0`.
3. the recorded `gcd(q, R_r) = 7` at every rotation of 12.8.3's `p = 7` staircase seed. Wholly
   external to the implementation; the misreading gives `1`.

Measured: accepts `σ_j = s_j + m_(j+1)`, accepts the committed `uniform_trim.R_rot`, **rejects**
`σ_j = m_j + s_j` with a message naming the convention. Tier 1 alone accepts both — that is the
point of the record.

### Sweep — where else `σ` is used undefined

Read-only; `paper/` and `sources/` recorded, **not edited**.

**Still open in the live wiki (recorded, deliberately not repaired here — outside the brief's
edit permissions or its scope):**

| file | line | use | verdict |
|---|---|---|---|
| `cycles.md` | 136 | Remark 12.6.1.1, `2^(σ_r) R_(r+1) = 3^(m_r) R_r + (2^(s_r) − 1)q` | **UNDEFINED at use**, and structurally worse than 12.6.1 was: the remark quantifies over "every profile `(m_t, s_t)`", i.e. outside the cycle setting where the preamble's `σ_t = v_2(C_t)` even has a referent. Now covered by proximity — the repaired 12.6.1 sits six lines above and gives the combinatorial form, which is the one this remark needs. |
| `cycles.md` | 132 | proof of 12.6.1, `ω_p · 2^(Σσ) 3^(Σa) = …` | undefined at use; only `Σσ` is needed, which is convention-independent |
| `HANDOFF.md` | 35, 39 | ghost identity `3B(W) + q = 2^(σ₀)·B(shift W)` | **UNDEFINED**; `σ₀` unexplained. Pinned in `briefs/merle-la6-check-findings.md` line 231. Item 1 of HANDOFF is a sibling session's territory this window — recorded only. |
| `aeh.md` | 109, 127 | letter `n = (σ_n − s_n, s_(n+1))`, letter `= (σ−s, s_+)` | defined only by the line-86 pointer to stage4.md, not at use; same shift-sensitive index. Mild. |

**Frozen / published artifacts — recorded, not edited:**

| file | line | use | verdict |
|---|---|---|---|
| `paper/collatz-reduced-v2.tex` | 178 | Prop `prop:elim`, `S_t = \sum_{j<t}\sigma_j` | **UNDEFINED at use.** The indexed `σ_t` is never introduced; the nearest is `def:reduced` at line 60, 118 lines earlier, where `σ` is *unindexed* (`σ = v_2(C)`, `m_+ = σ − s`) so the index alignment must still be inferred. **One mitigation the wiki lacked:** the proof at line 182 cites `Definition~\ref{def:reduced}` explicitly. |
| `sources/paper/collatz-reduced-v1.tex` | 175 (proof 179, def 57) | same statement | same verdict; immutable |
| `paper/collatz-mirror-v1.tex` | 49 | `σ = v_2 C` | DEFINED at use; single-step only. The mirror paper carries no cycle-profile `σ_t`, no `R_r`, no elimination statement — nothing to flag. |
| `sources/drafts/*.md` (`v001`–`v078`, 73 files) | — | — | **zero occurrences of `σ`/`sigma`**, and none of `R_r`, `12.6.1`, "period-`p` elimination", "transport recurrence". §12 is post-monolith (cycles.md front matter says so), so the drafts never carried the statement. Uniformly clean; no per-file enumeration needed. |

**Clean, checked:**

- **`itinerary.md` Lemma 14.15.9.2** — the brief named this as the mirror-frame statement to check.
  It contains **no `σ` at all**: it is stated in `α_i, β_i, y*_i, q, r_i`, and its integer-form note
  (line 449) uses the seam identity `N_r + q = 2^(m_r) R_r` with `q = 2^(S_P) − 3^(M_P)`. Nothing
  to repair. *All 24* of `itinerary.md`'s `σ` occurrences are the **sector sign** `σ ∈ {+1,−1}`
  (Definition 14.15.6.8, line 333) — a different symbol.
- `spine.md`, `stage3.md`, `index.md`, `ladder.md`, `publication.md`, `TOUR.md`,
  `stage1-synthesis.md`, `anchor-digit-search.md`, `archive/appendix-a.md`: **zero `σ`**.
- `stage4.md` (lines 40, 44: "Throughout, `σ = v_2(C) = s + m_+`"), `reverse.md` (270–273, 411, 414),
  `bridge.md` (28): the same quantity, one step rather than indexed, and **defined at use** — in
  fact more explicitly than cycles.md 12.6.1 was.
- Different symbol, checked and excluded: `README.md` line 40 and most of `aeh.md` (statistical
  sigma; also the shift map at aeh.md 71 and σ-algebras at 72), `open-problems.md` line 191 (sector
  sign), `anchors.md` 35 / `stage1.md` 611 / `stage2.md` 245 / `program.md` 87 (adjectival
  "`σ`-graded modulus", each carrying a stage4.md pointer).

---

## Defect 2 — the `p = 92` search bound

### Verdict: the `12.8.2` table is right; both prose figures were wrong

`n_0(p)` recomputed in exact `Decimal` (80 digits, bisection in log-space) from Corollary 12.8.2's
own displayed equation `0.585n/(1.585^p − 1) = log_2 p + (p + 13.3(0.46057 + log n))/log 2`. The
solver reproduces **all eight rows** of 12.8.2's Verification table to within 0.4%, so it is the
same object the table records:

```text
p =   4: 1.415e3 (page 1.41e3)   p =  50: 1.138e13 (page 1.14e13)
p =   5: 2.605e3 (page 2.61e3)   p =  91: 2.986e21 (page 2.99e21)
p =  10: 3.884e4 (page 3.88e4)   p =  92: 4.778e21 (page 4.78e21)
p =  20: 5.835e6 (page 5.84e6)   p = 100: 2.047e23 (page 2.05e23)
```

`n_0(92) = 4.778·10^21`. The `10^18` in `README.md` and `cycles.md` 12.8.5 was low by a factor
**4,778**.

### They are not answering different questions

Checked rather than assumed, since the brief warned against presuming the table authoritative:

- `n` versus `K` rescaling: `n_0(92)·log_2 3 = 7.57·10^21` — not `10^18`.
- an off-by-one in `p`: `n_0(91) = 2.99·10^21` — not `10^18`.
- `92·1.585^92 = 2.33·10^20` — not `10^18`.
- **`1.585^92 = 2.53·10^18`** — the only `10^18`-scale quantity in sight. The prose figure is
  Theorem 12.8.1's bare exponential rate with the `γ'/0.585 ≈ 1890` factor that Corollary 12.8.2
  supplies simply omitted.

No reading of the corollary yields `10^18`. Same question, one figure dropped a factor — so the
repair is the number alone and no scope clause is needed.

### The repair

Commit `56666f7`, its own commit. `README.md` strategy section: `n ~ 10^18` → `n ~ 4.8·10^21`, with
a pointer to §12.8.2 (which owns the fact, per AGENTS.md "every fact lives in exactly one page").
`cycles.md` 12.8.5: `n_0 ~ 10^18` → `n_0 ~ 4.78·10^21` (its table). 12.8.2's table itself is
unchanged — it was already right. §12.8.3 and §12.8.6 untouched (sibling's territory), `paper/` and
`sources/` untouched.

Cross-checked for the same figure elsewhere: `bridge.md` 78 and `open-problems.md` 179 both quote
`n_0(91) ~ 3·10^21`, already consistent with the table. `stage1.md` 579's `10^18` is unrelated
(orbit seed scale). `HANDOFF.md` 76 records the defect as "not corrected" — now stale, but it sits
inside item 1, a sibling session's lines this window; flagged, not edited.

### 12.8.5's conclusion — verified unchanged, not asserted

12.8.5 withdraws the crossover plan because the `p = 92` bound is infeasible. A period-`p` search at
depth-sum `n` must at minimum enumerate the compositions of `n` into `p` positive parts,
`C(n−1, p−1)`:

```text
n ~ 1e18    (old prose) : >= C(n-1, 91) ~ 10^1498 profiles
n ~ 4.78e21 (correct)   : >= C(n-1, 91) ~ 10^1833 profiles
```

Against an exhaustive-verification frontier of `~2^68 ~ 3·10^20` individual orbit starts, both
exceed feasibility by more than 1,400 orders of magnitude, and no stopping-rule threshold in README
lies between them. The conclusion — crossover plan withdrawn, cycle ladder retired, front parked —
is unchanged, and so are 12.8.4 and the "unaffected by 12.8.6" clause.

---

## Failures and negatives, recorded

- The brief's expectation that the transport recurrence "fails under the misreading" is **wrong as
  stated**, and the first run of the check script recorded it as a failing assertion before the
  script was rewritten around the true fact. Read self-consistently the recurrence is blind; it
  discriminates only once `σ_r` is written out. This *strengthens* the case for the repair and is
  what dictated the canary's tier-3 design.
- No `10^18`-yielding reading of Corollary 12.8.2 was found under any of the four probes above; the
  "different questions" hypothesis is not supported.
- Nothing here touches the all-`p` staircase result, the ledger, the note, or the reply.
