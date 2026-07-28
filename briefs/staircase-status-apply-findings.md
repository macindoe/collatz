# Findings: staircase-status-apply — the status edits, applied (2026-07-29)

Brief: `briefs/staircase-status-apply-brief.md`. Branch `staircase-status-apply`.
**Base SHA `bbd65aa`** — the worktree was cut from `2225b68`, which does not
contain the brief; the branch was re-cut at `bbd65aa` before any work began.

Six per-item commits, content separate from structure. **Not merged** — the main
session reviews and merges. Nothing pushed. `paper/`, `sources/`, `experiments/`
and `viz/` are untouched; the erratum in §5 is **drafted, not applied**.

`python experiments/encoding_scan.py`: **CLEAN** (345 tracked files, 0 invalid
UTF-8, 0 BOMs, 0 double-encoding signatures). Every edit was made with the
Edit/Write tools; PowerShell touched no tracked file.

---

## 1. What was applied, where

| commit | file(s) | what |
|---|---|---|
| `bbedf91` | `cycles.md` §12.8.6 | the subsection rewritten; all four sub-numbers keep their roles, nothing renumbered |
| `178acb9` | `cycles.md` | Remark `12.8.3`'s closing sentence; the §12.8 preamble |
| `34d98ef` | `cycles.md` | front matter `status`/`updated`; the Current-state paragraph |
| `31553bf` | `index.md`, `README.md`, `TOUR.md` | the pointer pages |
| `7be2583` | `publication.md` | the sharpness-hedge entry, with P2 decided |
| (this commit) | `briefs/`, `HANDOFF.md` | this record; the Cycles bullet; one scoped paragraph |

Exactly six locations in `cycles.md` changed: lines `2`, `4`, `8`, `232`, `293`
and the block `299`–`378`. Nothing else in the file moved — confirmed by
`git diff -U0 bbd65aa`, not by assumption.

### 1.1 `cycles.md` §12.8.6, object by object

* **Heading** — `Diophantine Input and the Explicit Staircase Recipe (floor
  grade)` → `The Staircase at Every Period`. Both retired words go: the grade,
  and "Recipe", which named the superseded object.
* **Preamble** — proves rather than attempts; names the two halves and says
  `12.8.6.2` carries hypotheses; keeps the size-passer-only clause, the
  stopping-rule clause, and `12.8.5` unaffected at any grade.
* **`12.8.6.1`** — now **Theorem (availability, unconditional)**, stated
  **two-sidedly**: the arc `[δ_lo, δ_hi] = [0.0415, 0.1169390665…]`, Lemma G's
  sharp sweep criterion, the window count, (H0), and the resulting bracket
  `3.683012 ≤ γ ≤ 5.140212`. Carries a *What is consumed* clause, the
  **superseded formulation** paragraph, and a *Verified* record.
* **`12.8.6.2`** — now **Theorem (explicit construction; no correction step)**:
  `Γ(p,n)` displayed, (H0) and (H1) as an explicit two-item list, Construction B
  in exact integers, the five-step proof, the additive-offset paragraph, a scope
  paragraph, and a *Verified* record.
* **`12.8.6.3`** — **demoted in place**, marked *(superseded: the
  profile-plus-correction recipe)*, carrying both parts of the old route and the
  `Θ(p)` result that killed it. Not deleted, not narrated.
* **`12.8.6.4`** — instance record intact; the band recalibrated as a property of
  the recipe's candidate list; the closing clause no longer offers the instances
  as evidence in place of a proof; the `p = 22` diagnosis restated.
* **Grade paragraph** — replaced by **Scope, and what is not covered**.

### 1.2 Status words, and the scope they carry

"Proved" appears only with its scope attached, in all five places it appears
(`cycles.md` front matter, Current state, §12.8 preamble, the Scope paragraph;
`index.md` Current status; `publication.md`). In each: **unconditional for
`p ≥ 16`**, **a finite check for `3 ≤ p ≤ 15`**, **`p ∈ {2,4}` by exhibition**.
No page writes `O(1)` bare where the bracket is meant; every statement of the
achieved `γ` gives `3.683012 ≤ γ ≤ 5.140212`. The Scope paragraph says in words
that "at every period" here means *every period, two of them by exhibition*, and
that the proof is a composition of **two theorems with hypotheses** — (H0) and
(H1) — not an unconditional identity.

---

## 2. Every deviation from the audit's drafts, with its reason

The brief's first instruction was to re-verify before writing. A fresh script
(mpmath at 60 dps plus exact `Fraction`/big-integer arithmetic, importing nothing
from `experiments/`) re-derived every constant. Eleven drafted items did not
survive that check unchanged.

**1. Lemma D's covering argument, restated at the sharp criterion (R6).** The
audit's draft — and every text it inherited — argued *"`14θ = 1.0526 ≥ 1`, so the
15 points lie around a full turn, so any arc longer than `θ` contains one"*. That
is a *sufficient-span* condition and it is not the one that governs. The
governing condition is `maxgap{jθ mod 1 : 0 ≤ j ≤ J} ≤ ℓ`, and it is an **iff**.
Recomputed here:

```text
theta        = 0.0751874963942...        two-sided arc length = 0.0754390665090...
maxgap(11)   = 0.1729375396635...        (fails both arcs)
maxgap(12)   = 0.0977500432693...        (one-sided OK -> 61 integers; two-sided fails)
maxgap(13)   = 0.0751874963942... = theta (two-sided OK -> 66 integers)
```

So the minimal sweep is `J = 13` (**66** consecutive integers) two-sided and
`J = 12` (**61**) one-sided. The record's "71" is valid but neither minimal nor
derived, and it is **not printed**. `12.8.6.1`'s proof states the criterion, its
two-line justification, both minimal `J`, and the failing `J = 11`.

**2. The brute-force comparison (R6).** The draft said the longest failing run of
`11` is "against the proved bound `70`". At the sharp criterion the proved bounds
are `60` (one-sided) and `65` (two-sided). Corrected; both runs are given
(`11` and `16`), each against its own bound. Reproduced here independently over
`n = 1…3·10⁵` (`11` and `16`, identical to the committed `3·10⁶` figures).

**3. `sup Γ` (R6).** The draft cited `sup` over `p = 6…2000` of
`Γ(p, 1.05·1.585^p)` — a tabulation. The proved statement is stronger and is what
`12.8.6.1` now carries: `Γ(p,n) < Γ*` for **every** `p ≥ 2` and every
`n ≤ 1.05·L^p`, because `η` enters `Γ` with coefficient exactly `1` and the
bracket `B(p)` is negative at `p = 2` and decreasing. Verified: `B(2) =
−0.6114616914…`; `Γ(p, 1.05L^p) < Γ*` at `p ∈ {2,6,16,20,30,60,200}` and equal to
`Γ*` at 60 dps by `p = 2000`, which is exactly why the strictness must come from
`B(p)` and not from a table.

**4. The `γ` bracket's upper end.** The audit's §0.1 gives `5.1926` at
`δ_lo = 0.04`. The gate-P1 result optimises to `δ_lo = 0.0415`, giving
`5.140212`. Recomputed: `−log₂(1 − 2^{−0.0415}) = 5.1402114860725…`, and
`δ_hi − θ = 0.0417515701148…`, so `0.0415` sits inside with margin
`0.000251570114…`. The brief's constants are used throughout.

**5. `12.8.6.4`'s recalibrated band (R9(i)).** The draft says window-wide
candidates close `p = 24…35` at `γ/log₂p ≈ 0.46…0.65`. **Wrong**: only
`p = 24…28` ran the sharpening pass to completion; `p = 29…35` ran under a 60 s
cap and their `γ ≈ 15.5…17.9` are *upper bounds*, not measurements
(`briefs/staircase-allp-diophantine-findings.md` §3, "Reading the table,
honestly"). The audit's own §3b has this right and its R9 draft does not.
Corrected, with the capped rows named as capped.

**6. `12.8.6.4`'s band, second half (R9(i)).** The draft's supporting figures
(`γ/log₂p` = `0.97` at `p = 10`, `0.82` at `p = 22`, `0.61` at `p = 31`) are
first-passer values from the **one-sided** search and are superseded by the
bracket. Replaced by the derived statement: the certified witnesses have
`γ ≤ 5.140212` at every `p ≥ 16`, so `γ/log₂p → 0`.

**7. `12.8.6.3`'s move count (R8).** The draft says *"its move count is `Θ(p)` at
fixed `γ`"* and calls the observed counts "that linear law". Both overstate the
source. `briefs/staircase-allp-construction-findings.md` §9 states it precisely:
the `Θ(p)` shortfall is an obstruction to any `O(1)`/`O(log p)` **upper** bound,
and there is **no proved lower bound** on the algorithm's own move count.
Rewritten to that statement. The draft's recorded counts also omit `p = 20`'s
`12` moves (`briefs/staircase-allp-findings.md` lines 48–57); all of them are now
listed, and they are explicitly *not* offered as a measurement of the law.

**8. Printed decimals in the wrong direction.** `briefs/staircase-gamma-upper-findings.md`
prints `Γ* ≤ 3.683012100721` and `θ ≤ 0.075187496394`. Both are **truncations**,
so both inequalities are false as written (`Γ* = 3.68301210072111…`,
`θ = 0.07518749639421…`); the file's own discipline is to truncate, which yields a
lower bound, not the upper bound the `≤` claims. No page reproduces those forms.
`cycles.md` gives values with an ellipsis and prints a rounded bound only where
the rounding is true in the claimed direction — `γ ≥ 3.683012` (truncated down),
`γ ≤ 5.140212` (rounded up), `δ_hi ≥ 0.116939` (truncated down, hence a
conservative threshold). *This is a flat note about the findings file, not a
defect in the mathematics: every underlying inequality is certified there as an
exact rational, and the margins are real.*

**9. Two internal cross-references the audit did not flag.** After the rewrite,
`12.8.6.4`'s opening *"By the recipe of `12.8.6.1`–`12.8.6.3`"* and the `p = 22`
paragraph's *"The recipe (`12.8.6.2`–`12.8.6.3`, unmodified)"* both resolved to
statements that had changed meaning — `12.8.6.1` is now availability and
`12.8.6.2` is now Construction B. Both now point at `12.8.6.3`, which was written
to carry the **whole** superseded route (profile *and* correction) precisely so
that they can.

**10. The superseded-formulation paragraph, extended (R6).** Kept, as the brief
requires — Merle cites `12.8.6.1` as "the Diophantine coverage bound" and that
number now resolves to a different statement. It additionally carries the
concrete instances the old lemma exhibited (`n = 41`, `n = 306` convergent
denominators; `n = 94 = 53 + 41` and `n = 971 = 665 + 306` the first
semiconvergents following `53` and `665`), re-derived here from the continued
fraction of `L`: `q₅ = 41`, `q₆ = 53`, `q₇ = 306`, `q₈ = 665`, `q₁₃ = 190537`,
`a₁₅ = 1`. Without them a reader arriving at the number from the v2 note or from
`experiments/merle_pincer_check.py` loses the grid the note describes.

**11. The number of delegated sessions (R5).** The draft says "closed in two
delegated attempts"; there were three (construction, diophantine, gamma-upper).
The preamble now names the three findings files rather than a count, which is a
pointer and not session narration.

### 2.1 Two figures recomputed that differ from the record, neither printed

`briefs/staircase-gamma-upper-findings.md` §5's finite-tail table gives
`Γ(5,17) = 3.750` and `Γ(6,17) = 3.256`. Recomputed from the displayed `Γ` with
the same `η` (`Γ = Γ₀ + η` exactly, since `β`'s coefficient in the numerator is
the denominator): `3.7414` and `3.2396`. `p = 3` and every row from `p = 7`
upward reproduce exactly. The verdicts are untouched — `γ` is `4.724` at both
rows, far above either figure — and neither number enters `cycles.md`. Recorded
for the main session; it is a third-decimal discrepancy in a table, not a claim.

---

## 3. Cross-reference sweep

Grepped the whole tree on `12.8.6`, each sub-number, `12.8.3`, `12.8.5`,
`floor grade`, `floor-grade`, `assessed`, `staircase`.

**Clean.** `bridge.md` (79, 90), `aeh.md` (13.3.3, 13.6.6), `stage4.md`,
`program.md`, `open-problems.md` (179, 183 — 12.8.2's `n₀(p)` only, and its
`n₀(91) ~ 3·10²¹` matches 12.8.2's own table), `anchors.md` (53),
`itinerary.md` (577, 612), `reverse.md`, `ladder.md`, `spine.md`,
`stage1`–`stage3`, `anchor-digit-search.md`: none states the sharpness grade and
none cites a sub-number whose statement changed. `viz/`: zero matches on
`staircase|12\.8\.6|floor grade|assessed`, re-checked rather than inherited.
`bridge.md` 79 — *"the staircase family **proves** no size-counting argument does
better"* — was ahead of the record and is now exactly right; no change.

**One item flagged and deliberately not repaired.** Six scripts carry section
citations in comments and printed output, and after the rewrite one of them
mis-resolves:

* `Construction 12.8.6.2` — now resolves to **Construction B**, where the comment
  means the superseded pure-geometric profile. In
  `experiments/staircase_allp.py` (header), `staircase_allp_construction.py:250`,
  `staircase_allp_diophantine.py:1010`, `merle_pincer_check.py:374,473,513`,
  `merle_round3_check.py:421,424`, `p22_passer.py:170,180`,
  `prime_local_probe.py:939`. The one-word repair is `12.8.6.2` → `12.8.6.3` at
  each site.
* `algorithm 12.8.6.3` still resolves correctly (`p22_passer.py`,
  `merle_pincer_check.py:501`, `staircase_allp_construction.py:552`).
* `lemma 12.8.6.1`'s sign-filtered grid (`merle_pincer_check.py:81,214,664,681`)
  resolves in one hop, via the superseded-formulation paragraph.

Not repaired here because `experiments/` is outside the audit's inventory (its
item 47) and the brief scopes this window to what the audit inventoried; the
repair is mechanical and belongs in its own structural commit.

**One pre-existing defect recorded, unrelated to this result.** `README.md`
line 53's repository-map row reads *"`cycles.md` | §12: … the uniform trim lemma
is the open objective"*. The trim was resolved at `12.8` before this arc began,
so that cell was already stale; nothing here made it so, and it is not in the
audit's inventory. Recorded, not repaired.

---

## 4. What did not move — confirmed by reading and by diff, not assumed

Each was read in full at its source, and `git diff -U0 bbd65aa` confirms no line
of any of them is in the diff.

1. **Consequence `12.8.5`** — untouched, line for line, including its own
   *"This conclusion is unchanged by `12.8.6` below, at any grade"* and the
   `n₀ ~ 4.78·10²¹` figure a sibling session repaired. The new Scope paragraph
   restates its conclusion as a pointer only, adding the brief's own sentence:
   sharper evidence that counting cannot do better, **no evidence at all about
   exclusion**.
2. **The parked cycle front** — untouched. All three sessions behind this result
   built **size-passers only** and touched the divisibility system solely to
   confirm that every constructed instance **fails** `q | R_r` at every rotation.
   No per-period cycle search was run; no divisibility-based exclusion was
   attempted; the front's reopening condition (a divisibility-aware,
   anchor-rigidity idea, not more computation) is untouched and nothing here
   supplies one or claims to.
3. **All three README stopping rules** (line 36) — untouched, all three. The only
   README edit is line 17, the scoreboard, a different section that states a
   grade and not a rule.
4. **README line 34, the strategy paragraph** — untouched, including the
   `n ~ 4.8·10²¹` figure. Its chain (explicit family → counting cannot do better
   → the crossover plan is refuted) is strengthened at its middle link and
   unchanged at its conclusion.
5. **Theorem `12.8.1`, Corollary `12.8.2`** (statements, proofs, and the `n₀(p)`
   table), **Remark `12.8.4`**, and **Proposition `12.6.1`** including the
   sibling's `σ` repair — untouched. The new results *consume* `12.6.1`'s `R_r`
   and `12.8`'s `γ`; they modify neither.
6. **Remark `12.8.3`'s body** — its `p = 7` (`n = 94`, `γ = 6.744`) and `p = 6`
   instances are untouched. Only its closing pointer sentence changed.
7. **`paper/`, `sources/`, `experiments/`, `viz/`, `archive/`** — untouched.

---

## 5. The erratum — DRAFTED, NOT APPLIED

`paper/` and `sources/` are frozen and were not opened for writing. This is the
audit's R13 carried forward, updated for P1's exact constants and for P2 as the
author decided it. It corrects **only** the v2 note's gap sentence and is silent
on the hedge. Sending it is a decision for the author, not for this session.

Current published text (v2 note, third-from-last sentence):

> The remaining gap is the one already named: no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs --- the bound that would certify no period is skipped --- and the $p = 22$ episode is a demonstration that this gap bites in practice, not only in principle.

Proposed replacement:

> *(Correction, 2026-07-29.)* The gap named in this note has since been closed,
> and closed by replacing the route rather than completing it. Candidate
> availability needs no continued-fraction input: because `8 − 5log₂3 =
> 0.0751874964…` is positive and smaller than the target arc, any `66`
> consecutive integers contain an `n` whose `⌈n log₂3⌉ − n log₂3` lies in
> `[0.0415, 0.1169390665…]`, and the scale window contains far more than `66`
> integers at every period from `16` onward. The bound on the multiplicative gap
> between correctly-signed runs is not needed, and as posed it is a dead end — a
> uniform bound on those gaps is exactly the assertion that `log₂3` is badly
> approximable. The `p = 22` episode was a property of the candidate list used,
> not of `log₂3`: with candidates drawn from the whole window the same
> construction closes every period tested. The construction half is closed
> independently: a corrected profile — the geometric climb with a fixed additive
> offset `1/(log₂3 − 1) = 1.70951` per block, absent from the profile described
> above — satisfies all `p` size conditions **by construction**, with no
> correction step, so the bounded correction is removed from the argument rather
> than bounded. The two halves compose to a proof for every period `p ≥ 16`, with
> `3 ≤ p ≤ 15` by finite check and `p ∈ {2,4}` outside the construction's reach
> and covered by exhibition, at `γ` between the absolute constants `3.683012` and
> `5.140212` — no `p`-dependence at all. The current record is `cycles.md` §12.8.6
> of the project repository.

Two notes on the draft. It is deliberately silent on the hedge clause, whose
"not proved *here*" remains a true statement about the paper. And it should point
at settled text: it is worth sending only **after** §12.8.6 is reviewed and
merged. The note's own repository pointer is pinned to a frozen commit
(`…/blob/72ec88e/cycles.md`), so until then the paper stays self-consistent
against its own citation.

---

## 6. Left undone, and things a reviewer should re-check

**Left undone, deliberately.**

* The `experiments/` section-citation repair (§3). Mechanical; its own commit.
* `TOUR.md`'s **floor grade** vocabulary entry, left exactly as written. `12.8.6`
  was the tree's only instance, so the entry is now unattached; a "nothing
  currently stands at this grade" note would be a change log. The audit leaned
  the same way. Recorded as a judgment call.
* `briefs/staircase-allp-findings.md`'s optional supersession header (audit R11,
  "optional, low priority"). It is a dated session record already carrying its own
  supersession section, and `TOUR.md` now identifies it as the earlier route's.
* `HANDOFF.md`'s duplicate item numbering (two `4`s and two `5`s at lines 85–91).
  Recorded by the audit and by this session; not repaired, being unrelated to the
  result.
* `publication.md`'s Current-state sentence (audit R30, "UPGRADE, optional"). It
  is still true and reads no differently; not touched.
* Anything for the ledger, the shared repo, or the reply. The reply is the next
  window and explicitly not this one's.

**What a reviewer should re-check.**

1. That `12.8.6.1`'s proof reads at the **maxgap** criterion and never at the
   span condition, and that "71" appears nowhere.
2. That `Γ(p,n)`, (H0), (H1) and Construction B in `12.8.6.2` are transcribed
   character for character from `briefs/staircase-allp-construction-findings.md`
   §4–§5 and not paraphrased.
3. That every "proved" carries `p ≥ 16` / finite check / `p ∈ {2,4}` with it, and
   that no sentence lets "at every period" absorb the two excluded ones.
4. That `12.8.6.3` is present, marked superseded, with its reason — and that no
   "was X, now Y" narration was written around it or around the superseded
   formulation inside `12.8.6.1`.
5. §2 item 8: that no inequality in `cycles.md` is printed in a direction its
   decimal does not support.
6. The re-verification script is not committed — it is scratch, and the committed
   verifier for every constant in the page is
   `experiments/staircase_gamma_upper.py` (45 checks, 0 failures), which the main
   session has already re-run byte-identically at the P1 review.
