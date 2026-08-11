# Findings: staircase-status-audit — what the all-`p` closure retires (2026-07-28)

> **Superseded as drafts.** The drafted texts here were applied with eleven deviations — the applied record is `briefs/staircase-status-apply-findings.md`; gates (P1)/(P2) are both discharged (`briefs/staircase-gamma-upper-findings.md`; the author's P2 call).

Brief: `briefs/staircase-status-audit-brief.md`. Branch `staircase-status-audit`.
**Base SHA `82f0523`** — the worktree was cut from `2225b68`, which does not
contain the brief; the branch was re-cut at `82f0523` before any work began.

**PROPOSALS ONLY.** No file in the repository is modified by this session except
this findings file and one scoped paragraph in `HANDOFF.md`. Every replacement
below is a draft for the main session and the author to weigh, quoted against
the current text. `cycles.md`, `README.md`, `index.md`, `open-problems.md`,
`program.md`, `spine.md`, `publication.md`, `TOUR.md`, `paper/` and `sources/`
are untouched.

**Sibling session.** `record-defects-repair` runs in parallel on §12.6.1's
undefined `σ` and the `p = 92` figure. It may edit `README.md`'s strategy
paragraph and `cycles.md` 12.8.5/12.8.2 for the numeric repair. Nothing proposed
here touches §12.6.1, and the only 12.8.5 proposal here is an optional pointer
clause that does not collide with a numeric repair — see §5 item 1 and §7.

---

## 0. What is actually proved, stated once, with its hypotheses and its holes

Everything downstream depends on getting this paragraph right, so it is stated
first and in full. Two theorems compose.

> **Theorem B** (`briefs/staircase-allp-construction-findings.md` §5). Let
> `p ≥ 2`, `n ≥ 1` be integers, `L = log₂3`, `K = ⌈nL⌉`, `S = K − n`,
> `q = 2^K − 3^n`, `γ = K − log₂q`, `η = −log₂(1 − 2^{−(S−p+1)})`. Assume
> **(H0)** `S ≥ p` and `(L−1)(n−p) + γ ≥ p + η`; **(H1)**
> `γ ≥ max(2 + η, Γ(p,n))`, with `Γ` the displayed closed form of that §5. Then
> Construction B returns a period-`p` profile with all entries `≥ 1`, `Σm_t = n`,
> `Σs_t + n = K`, **crash depth exactly 1**, satisfying `q ≤ R_r` at **every**
> rotation — **with no correction step**.

> **Lemma D** (`briefs/staircase-allp-diophantine-findings.md` §6.3). With
> `θ := 8 − 5L = 0.0751874964…`, stepping `n → n+5` decreases `{nL}` by exactly
> `θ`; the 15 points `N, N+5, …, N+70` lie `θ` apart along a full turn
> (`14θ = 1.0526 ≥ 1`), so any arc of length `> θ` contains one. Hence **among
> any 71 consecutive integers there is an `n` with `⌈nL⌉ − nL ≤ 0.116939`**.

> **Theorem D** (same file, §6.4). `sup` over `p = 6…2000` of
> `Γ(p, 1.05·1.585^p)` is `3.683012`, and `⌈nL⌉ − nL ≤ 0.116939` is exactly
> `γ ≥ 3.683013`; so every `n` in `[1.585^p, 1.05·1.585^p]` meeting Lemma D's
> condition satisfies (H1). That window holds `0.05·1.585^p` integers, which
> reaches 71 at `p = 16`. Hence **for every `p ≥ 16` the window contains an `n`
> satisfying Construction B's hypothesis, unconditionally.**

**The composed statement, at the strength it deserves:**

> For every period `p ≥ 16` there is an explicit integer `n` and an explicit
> period-`p` profile `(m_t, s_t)` — computed in exact integers, with no floating
> point anywhere — satisfying **every** rotation's exact size condition
> `q ≤ R_r`. The argument uses no hypothesis on the partial quotients of
> `log₂3`, no effective irrationality measure, no continued-fraction chain and
> no sign condition; the Diophantine input is one exact number, `8 − 5L`.

**Coverage below `p = 16`, honestly.**

* `3 ≤ p ≤ 15` — the same hypothesis (H1) is met at an explicit `n` in a
  widened window (`κ ≤ 2`), **checked directly**. This is a finite check, not
  the asymptotic argument.
* `p ∈ {2, 4}` — **outside Theorem B's reach**. `Γ`'s coefficient on `n` is
  `(L−1)/(L^{p−1} − 1)`, which is `O(L^{−p})` only once `L^{p−1} ≫ 1`; at those
  two periods the required quality outruns what integers at that scale supply.
  Both have exact size-passers by **direct exhibition**
  (`briefs/staircase-allp-construction-findings.md` §7 Part 1, §9). They are
  covered by exhibition, not by the theorem, and every restatement must say so.

**Three further holes that belong in the true statement.**

* **`Γ` is conservative by `0.6`–`0.9` bits** (NC-A). `(C_r)` keeps one term of
  `R_r` and discards `p−1` positive ones, so (H1) is sufficient and not
  necessary: some `n` with `γ < Γ` also work and are simply not certified. This
  narrows the *theorem's* reach relative to the empirical family; it weakens
  nothing that is proved.
* **The independent verification stops at `p ≈ 32`, on big-integer cost, not on
  mathematics.** `p = 32` means `n ≈ 2.5·10⁶` and `3^n` at `4·10⁶` bits. Nothing
  in Theorem B degrades with `p`. This is a limit on the *check*, not on the
  theorem — and `AGENTS.md`'s "before marking anything proved" rule asks for an
  independent numerical check, not for one covering every `p`, which is
  impossible for a for-all-`p` statement.
* **The independent checks that exist, named:**
  `experiments/staircase_allp_construction.py` (`p = 2…32`, exact big integers,
  importing nothing from `staircase_allp.py`/`p22_passer.py`/`uniform_trim.py`);
  `experiments/staircase_allp_diophantine.py` (a second, structurally different
  evaluator — Horner for `R_0`, then `12.6.1.1`'s transport recurrence for every
  other rotation — with Construction B transcribed from the statement, not the
  code, `p = 3…26`); and the main session's own third evaluator at review,
  `p = 16…28`, 0 failures. Lemma D was re-derived from scratch at review. The
  house norm is met.

### 0.1 The one thing that is asserted but not yet proved: the `γ` upper bound

**This is the single most important finding of this audit beyond the sweep, and
every proposal that says `γ = O(1)` is gated on it.**

Theorem B's hypothesis (H1) is `γ ≥ Γ`: **larger `γ` is easier**. Lemma D is
correspondingly one-sided — it delivers `δ := ⌈nL⌉ − nL ≤ 0.116939`, i.e.
`γ ≥ 3.6830`, and places **no upper bound on `γ` at all**. But the sharpness
claim needs `γ` *small*. So:

* **`Γ(p,n) = O(1)` is proved.** `Γ = 0.92714·κ + 2.70951 + η + O(p·L^{−p})`,
  `κ = n/L^p`; at `κ ≤ 1.05` it never exceeds `3.6831`, with no `p`-dependence.
  That is a closed-form computation on the displayed formula. It is a statement
  about the **demand**.
* **`γ = O(1)` at the constructed witness is asserted in both findings files and
  proved in neither.** The evidence offered is empirical: `γ ∈ [2.91, 17.06]`
  over `p = 2…32` with no upward trend (construction §6); `γ ≈ 2.2…3.0` where
  the sharpening pass ran to completion (diophantine §3); but `γ = 17.058` at
  the first good `n` at `p = 26` (diophantine §6.4 table). Nothing in the record
  bounds the achieved `γ` above.

**The repair is two lines and costs nothing, and I verified it.** Lemma D's
argument bounds an arc, so it works two-sidedly. The target arc
`{nL} ∈ [1 − 0.116939, 1 − 0.04]` has length `0.076939 > θ = 0.0751875`, so the
identical 71-integer argument gives, among any 71 consecutive integers, an `n`
with

```text
0.04  ≤  ⌈nL⌉ − nL  ≤  0.116939,     hence     3.6830 ≤ γ(n) ≤ 5.1926 .
```

Both ends are absolute constants, uniform in `p`; the lower end still satisfies
(H1) since `Γ ≤ 3.6831` on the window. The largest admissible lower cut is
`0.116939 − θ = 0.0417515`, so `0.04` sits inside with margin. Checked here at
60–80 digits, and brute-forced: over `n = 1…3·10⁵` the longest run of
consecutive integers failing the **two-sided** condition is **16**, against the
proved bound 70 (the one-sided condition's longest failing run is 11, matching
both delegates' independently observed worst offset).

**Consequence for the proposals.** No page may state `γ = O(1)` as proved until
this two-sided form of Lemma D is written down and re-derived by the main
session. It is the first item of the application order (§6). Until then the
honest statement is *"the demand `Γ` is `O(1)`, uniform in `p`; the achieved `γ`
is bounded by an absolute constant on a two-sided refinement of Lemma D"* — or,
if the main session prefers to hold the line, simply *"`γ` does not grow with
`p`"* with the measured tables cited as evidence. I flag this as my
lowest-confidence item not because I doubt the arithmetic — I checked it — but
because it is a *new* mathematical step introduced at audit, and this session is
supposed to propose status, not mathematics.

### 0.2 The status words, applied

| word | applies to | why |
|---|---|---|
| **proved** | existence of a size-passer at every `p ≥ 16` | Theorem D → Theorem B, both with written proofs and independent numerical checks by fresh code (`AGENTS.md`, "Before marking anything proved") |
| **proved (finite check)** | `3 ≤ p ≤ 15` | (H1) met at an explicit `n`, verified exactly; a finite check is a proof of a finite statement |
| **verified** | `p ∈ {2,4}` | exact size-passers exhibited; no theorem covers them |
| **proved**, pending §0.1 | `γ = O(1)` | licensed by the two-sided Lemma D, which is not yet in the record |
| **assessed** | *nothing here any more* | the word's canonical instance in `TOUR.md` is this claim; see §2 item 25 |
| **floor grade** | *nothing here any more* | 12.8.6 was its only instance in the tree; see §2 item 26 |
| **heuristic** | untouched | no heuristic-grade statement in this area moves |

---

## 1. The sweep table

Verdicts: **RETIRE** (the text states something now false and its content goes),
**UPDATE** (the text stays in role but its wording is wrong, stale or
understated), **UPGRADE** (correct but weaker than what is now proved),
**UNAFFECTED** (checked, no change).

Counts: **RETIRE 5 · UPDATE 17 · UPGRADE 3 · UNAFFECTED 21** across 12 tracked
files, plus 4 published locations analysed separately in §4.

### 1.1 `cycles.md` — the owning page

| # | location | current text (verbatim, elided with …) | verdict | why |
|---|---|---|---|---|
| 1 | front matter `status:` | `all-p sharpness ASSESSED not proved, floor grade (12.8.6)` | **RETIRE** | both status words are now wrong |
| 2 | front matter `updated:` | `2026-07-23` | UPDATE | mechanical, with the content edit |
| 3 | Current-state ¶ | `…is calibrated further at floor grade (12.8.6): an explicit per-period construction recipe plus a bounded correction algorithm produce verified instances for the full contiguous range p ∈ {2,...,23}…; the all-p claim remains assessed, not proved, with the Diophantine coverage bound of 12.8.6.1 the sole open gap.` | **RETIRE** | wrong three times: the grade, the machinery (the correction algorithm is removed from the argument), and the named gap |
| 4 | §12.8 preamble | `that degradation is assessed as **intrinsic** … (Remark 12.8.3; sharp at the verified instances, the all-p claim assessed, not proved, 12.8.6)` | UPDATE | "assessed" → proved; the parenthetical's scope clause changes |
| 5 | Remark 12.8.3, closing sentence | `The instance record is substantially extended, and the construction generalized to an explicit per-period recipe covering the full contiguous range p ∈ {2,...,23}, at 12.8.6; this Remark's own recorded instances are unchanged.` | UPDATE | the recipe named is superseded and the range is now every `p`; the Remark's own instances genuinely are unchanged and that clause survives |
| 6 | Remark 12.8.3, body (the `p = 7` and `p = 6` instances) | — | UNAFFECTED | reproduced and re-verified by both delegate evaluators at `γ = 6.744`; nothing moves |
| 7 | Remark 12.8.4 | (what the staircase means) | UNAFFECTED | strengthened, not changed; no status word |
| 8 | Consequence 12.8.5 | (strategy; the stopping rule fires) | **UNAFFECTED** | see §5 — confirmed by reading, not assumed. Optional pointer clause only |
| 9 | §12.8.6 heading | `Diophantine Input and the Explicit Staircase Recipe (floor grade)` | **RETIRE** | grade wrong; "Recipe" names the superseded object |
| 10 | §12.8.6 preamble ¶ | `This subsection attempts to upgrade … It reaches the **floor grade** … The primary theorem and both fallback gradations of the brief remain open` | **RETIRE** | the primary theorem does not remain open |
| 11 | Lemma 12.8.6.1 + its *Status of this lemma* ¶ | `…a fully general, closed-form bound on the multiplicative gap between consecutive correctly-signed runs … is not established; this is recorded as a gap … and it is the **sole remaining gap** of the floor-grade result below.` | **RETIRE** | the bound is not needed *and* the route is a characterized dead end; the requirement it served is proved |
| 12 | Construction 12.8.6.2 | `…round the geometric profile m_j ∝ L^j … by rounding the *partial sums* …` | UPDATE | replaced in role by Construction B; kept as the superseded profile, with NC-B's numbers attached |
| 13 | Algorithm 12.8.6.3 | `The base construction of 12.8.6.2 typically falls short … A deterministic, auditable local search closes this…` | UPDATE | **removed from the argument, not bounded**; demoted to the superseded block (recommendation and reasons at §3c) |
| 14 | Prop. 12.8.6.4, band | `p ∈ {2, 3, ..., 23}, with γ / log_2 p ∈ [1.828, 3.643]` | UPDATE | must be described as what the recipe produced from chain candidates, not as a property of the family (§3b) |
| 15 | Prop. 12.8.6.4, the two `p = 22` rows | `At p = 22, candidate availability — not combinatorial resistance — is the binding constraint: the candidate chain has a genuine hole at that scale…` | UPDATE | the diagnosis was right about the *chain* and wrong about `log₂3`; the "hole" is a property of the candidate list |
| 16 | Prop. 12.8.6.4, closing clause | `consistent with, but not a proof of, the assessed γ = O(log p) shape` | UPDATE | now a proof, and at a stronger shape |
| 17 | "Achieved grade: floor, substantially exceeded" ¶ | `…the sole remaining gap in this floor-grade result is the Diophantine coverage bound of 12.8.6.1 (still open, per its status paragraph above).` | **RETIRE** | wrong twice over (§3a) |
| 18 | 12.8.1, 12.8.2, 12.6.1.x, 12.7.x, §12.1–12.7 | — | UNAFFECTED | the new results *consume* `12.6.1`'s `R_r` and `12.8`'s `γ`; they change neither |

### 1.2 Other wiki pages

| # | file / location | current text | verdict | why |
|---|---|---|---|---|
| 19 | `index.md` line 33, `cycles.md` row | `staircase sharpness recipe at floor grade (12.8.6)` | UPDATE | grade + superseded object |
| 20 | `index.md` line 46, Current status | `the all-p staircase sharpness held at floor grade — verified instances for the full contiguous range p ∈ {2,...,23} (12.8.6), the Diophantine coverage bound its sole remaining gap` | **RETIRE** | wrong twice |
| 21 | `README.md` line 17, scoreboard | `an explicit family shows counting arguments cannot do substantially better — sharp at the verified instances, assessed at every period (cycles.md)` | UPDATE | "assessed at every period" is the exact clause that dies |
| 22 | `README.md` line 34, strategy ¶ | `with an explicit family of near-counterexamples (the *staircase*, §12.8.3) showing counting arguments cannot do substantially better` | **UPGRADE** (optional) | carries no status word, so not wrong; may gain one clause. **The sibling session edits this paragraph's `p = 92` figure** — see §7 |
| 23 | `README.md` line 36, stopping rules | (all three rules) | **UNAFFECTED** | confirmed by reading, §5 |
| 24 | `TOUR.md` line 14, paper→wiki map | `the post-publication attempt to prove the family at every period is **12.8.6** (floor grade; see below)` | UPDATE | no longer an attempt, no longer floor grade |
| 25 | `TOUR.md` line 22, correspondence section | `The attempt to close it is cycles.md **12.8.6**: a Diophantine lemma (semiconvergents of log₂3), an explicit profile, a bounded correction, and verified instances for the full contiguous range p ∈ {2,…,23}` | **RETIRE** | all three machinery items are superseded; this is the page external readers arrive on |
| 26 | `TOUR.md` line 23–24, pointers + code | `…are in briefs/staircase-allp-findings.md; …The verification code for all of it is experiments/staircase_allp.py` | UPDATE | two new findings files and two new scripts are now the current record |
| 27 | `TOUR.md` line 39, vocabulary | `**assessed** — … the paper's thm:staircase sharpness half is the canonical example.` | UPDATE | delicate: the *published* sentence is still assessed, the *wiki's* claim is not. Draft at §2 |
| 28 | `TOUR.md` line 42, vocabulary | `**floor grade** — a delegation outcome…` | UPDATE | 12.8.6 was the tree's only floor-grade instance; the entry becomes orphaned |
| 29 | `publication.md` line 38, hedge-status entry | `the published thm:staircase hedge … stands; the delegated attempt reached floor grade … not the all-p proof. **The hedge sentence is not upgradable**; better evidence, not a closure, is what v2 added.` | **RETIRE** | "not upgradable" was a statement of fact and is now a *decision* — and one that is not this page's to make |
| 30 | `publication.md` line 7, Current state | `its sharpness dichotomy … is the strongest candidate for a genuinely new theorem` | **UPGRADE** (optional) | still true, now more so |
| 31 | `HANDOFF.md` line 19, Cycles front | `staircase sharpness at floor grade, contiguous p ∈ {2,...,23}` | UPDATE | grade + range |
| 32 | `HANDOFF.md` lines 85–86, open items | two items **both numbered `4`**, both now delivered and merged | UPDATE | collapse into the front bullet; the duplicate numbering is a separate small defect, recorded not repaired |
| 33 | `bridge.md` line 79 | `the staircase family **proves** no size-counting argument does better (cycles.md 12.8.3)` | **UNAFFECTED** | notable: this page was ahead of the record and is now exactly right. Recorded, no change |
| 34 | `bridge.md` line 90, 16.4.6 | one-configuration-both-halves | UNAFFECTED | strengthened |
| 35 | `aeh.md` 13.3.3, 13.6.6, front-matter `source:` | staircase as AEH-exceptional set | UNAFFECTED | no status claim about sharpness |
| 36 | `stage4.md` lines 8, 96 | `the uniform trim is resolved, the crossover plan withdrawn` | UNAFFECTED | no grade stated |
| 37 | `program.md` line 99 | stopping-rules pointer | UNAFFECTED | pointer only |
| 38 | `open-problems.md` lines 179, 183 | 12.8.2's `n_0(p)`; the Rhin citation guard | UNAFFECTED | about the trim's effectivity, not the sharpness grade |
| 39 | `anchors.md` line 53, `itinerary.md` 577/612, `reverse.md`, `ladder.md`, `anchor-digit-search.md` line 18, `spine.md`, `stage1–3` | various pointers to 12.8.x | UNAFFECTED | checked individually; none states the sharpness grade |
| 40 | `viz/` (all files) | — | **UNAFFECTED** | grepped on `staircase\|12\.8\.6\|floor grade\|assessed` and on `12\.8\|uniform trim\|sharpness`: **zero matches in the whole directory.** `cycle_anchor_gateway.html` carries no status text about this claim |

### 1.3 `briefs/` and `experiments/`

| # | file | verdict | why |
|---|---|---|---|
| 41 | `briefs/staircase-allp-diophantine-findings.md` §5(a) | UPDATE (**internally stale**) | "Do not lift `thm:staircase`'s hedge … Nothing here proves the *construction* succeeds at any `p ≥ 24`" was written against the **old** interface and is superseded by that same file's §6. Under Construction B the construction *is* proved. Flagged, not repaired — a findings file is a dated record |
| 42 | `briefs/staircase-allp-diophantine-findings.md` §5(b) draft, last sentence | UPDATE (**stale as drafted**) | `What remains unproved is the construction half … for which no bound on the correction's move count is established` — Construction B removes the correction. Repaired draft at §2 |
| 43 | `briefs/staircase-allp-diophantine-findings.md` §5(c), second clause | UPDATE (**stale as drafted**) | `the "sole remaining gap" … should become the correction algorithm's move count` — same cause. Repaired draft at §2 |
| 44 | `briefs/staircase-allp-findings.md` item 4 + closing | UNAFFECTED (dated record) | `it remains open (now the sole remaining gap…)` is false as of today, but the file is a dated session record already carrying its own supersession section. Optional one-line header at §2 R11 |
| 45 | `briefs/jointnote-premise-ours-findings.md`, `briefs/merle-round11-*`, `briefs/p22-record-update-brief.md`, `briefs/paper1-v2-*` | UNAFFECTED (dated records) | they quote the wiki/paper text correctly *as of their dates*; the joint-note consequence is flagged for the author at §4.5 and is explicitly not this session's |
| 46 | `paper/collatz-reduced-v2-review.md` | UNAFFECTED (frozen-adjacent) | a dated review record of a published version; `paper/` is off-limits and it would be wrong to retrofit it anyway |
| 47 | `experiments/staircase_allp.py`, `p22_passer.py`, `uniform_trim.py` | UNAFFECTED | they support recorded instances that remain correct. The two new scripts are additive, already committed |

---

## 2. Drafted replacements, in full

Register target: `cycles.md`'s own — flat, backticked symbols, em-dashes,
`*Calibration.*` / `*Verified*` blocks, no narration of how the state was
reached (`AGENTS.md`: no change logs in tracked files).

**Structural recommendation for §12.8.6, first, because the drafts assume it.**
Keep all four section numbers and replace their *contents in place*, each number
keeping its role:

* `12.8.6.1` — Diophantine input → the **availability theorem** (same role: what
  supplies `n`), with the convergent-run framing recorded inside it as a named
  **superseded formulation**, since the published v2 note points at it.
* `12.8.6.2` — the explicit profile → **Construction B** (same role), with the
  pure-geometric rounding recorded as what it replaces and why.
* `12.8.6.3` — the correction algorithm → retitled and **demoted to the
  superseded block**, kept with the `Θ(p)` result that killed it.
* `12.8.6.4` — the instance record → recalibrated.
* the grade paragraph → replaced by a scope-and-holes paragraph.

This satisfies `AGENTS.md`'s "do not renumber" (nothing shifts) and its
rewrite-in-place model, and it keeps every external citation landing on an
object of the same kind. *Alternative, if the main session prefers:* add
`12.8.6.5`/`12.8.6.6` for the new results and demote `12.8.6.1`–`12.8.6.3`
wholesale. I recommend against it — it leaves the argument's main line at the
*end* of the subsection behind three superseded items, which is the reading
order `TOUR.md` sends external arrivals into. **One risk of in-place
replacement, recorded:** the correspondent cites `12.8.6.1` as "the Diophantine
coverage bound"; after the edit that number resolves to a different statement.
The superseded-formulation paragraph inside it is the mitigation and should not
be dropped.

### R1 — `cycles.md` front matter

Current:
```
status: periods 1–3 CLOSED; uniform trim RESOLVED (12.8); all-p sharpness ASSESSED not proved, floor grade (12.8.6); front PARKED per stopping rules
updated: 2026-07-23
```
Proposed:
```
status: periods 1–3 CLOSED; uniform trim RESOLVED (12.8); all-p sharpness PROVED (12.8.6 — unconditional for p ≥ 16, finite check below, p ∈ {2,4} by exhibition); front PARKED per stopping rules
updated: 2026-07-28
```

### R2 — `cycles.md` Current-state paragraph, the sharpness clause

Current:
> …but its constant degrades like `1.585^(-p)`, and the staircase family (12.8.3) shows size-counting can do no better at the two periods where it was originally checked. Whether that exponential weakness is intrinsic at *every* period (the published paper's `thm:staircase` hedge) is calibrated further at floor grade (12.8.6): an explicit per-period construction recipe plus a bounded correction algorithm produce verified instances for the full contiguous range `p ∈ {2,...,23}` (the two `p = 22` candidates credited to Eric Merle's pincer hypothesis); the all-`p` claim remains assessed, not proved, with the Diophantine coverage bound of `12.8.6.1` the sole open gap.

Proposed:
> …but its constant degrades like `1.585^(-p)`, and the staircase family (12.8.3) shows size-counting can do no better at the two periods where it was originally checked. That the exponential weakness is intrinsic at *every* period — the question the published paper's `thm:staircase` carries as assessed — is now **proved** (12.8.6): an availability theorem supplies a candidate `n` at every scale from one exact number, `8 − 5·log_2 3` (`12.8.6.1`), and an explicit integer construction turns it into a profile whose `p` size conditions hold **by construction, with no correction step** (`12.8.6.2`). Unconditional for every `p ≥ 16`; `3 ≤ p ≤ 15` by finite check; `p ∈ {2,4}` lie outside the construction's reach and are covered by direct exhibition. The quality consumed is a fixed density condition on `⌈n·log_2 3⌉ − n·log_2 3`, with no `p`-dependence at all.

*(If §0.1's two-sided Lemma D lands, append: `— so the family's γ is bounded by an absolute constant, stronger than the O(log p) the published theorem assesses.`)*

### R3 — `cycles.md` §12.8 preamble

Current:
> …and that degradation is assessed as **intrinsic** — an explicit family of configurations shows counting arguments cannot do substantially better (Remark `12.8.3`; sharp at the verified instances, the all-`p` claim assessed, not proved, `12.8.6`).

Proposed:
> …and that degradation is **intrinsic** — an explicit family of configurations shows counting arguments cannot do substantially better (Remark `12.8.3` for the family and its first instances; proved at every period in `12.8.6`, unconditionally for `p ≥ 16`).

### R4 — `cycles.md` Remark 12.8.3, closing sentence

Current:
> The instance record is substantially extended, and the construction generalized to an explicit per-period recipe covering the full contiguous range `p ∈ {2,...,23}`, at `12.8.6`; this Remark's own recorded instances are unchanged.

Proposed:
> The family is constructed at **every** period in `12.8.6`, from an explicit integer construction requiring no correction step; this Remark's own recorded instances are unchanged, and both are reproduced there as cross-checks.

### R5 — `cycles.md` §12.8.6 heading and preamble

Current heading:
> `## 12.8.6. Diophantine Input and the Explicit Staircase Recipe (floor grade)`

Proposed heading:
> `## 12.8.6. The Staircase at Every Period`

Current preamble:
> This subsection attempts to upgrade `12.8.3`'s sharpness assessment … It reaches the **floor grade**: a general per-period construction recipe and a verified instance record covering every period `p ∈ {2,...,23}` … The primary theorem and both fallback gradations of the brief remain open; `12.8.5`'s strategic conclusion is unaffected.

Proposed preamble:
> This subsection proves `12.8.3`'s sharpness assessment (`γ` small at *every* period, verified there only at `p ∈ {6, 7}`) — the same statement the published paper's Theorem `thm:staircase` carries as assessed. Two independent halves compose: an availability theorem for the exponent `n` (`12.8.6.1`) and an explicit integer construction whose size conditions hold by construction (`12.8.6.2`). Neither uses a hypothesis on the partial quotients of `log_2 3`, an effective irrationality measure, or a continued-fraction chain. The question was opened by an external suggestion (Eric Merle, correspondence 2026-07-16) and closed in two delegated attempts; stopping-rule compliance is recorded in their briefs (this is a negative structural result about the reach of size arguments — no cycle search, no divisibility-based exclusion attempt). Every configuration constructed here is a **size-passer only**: all were tested against the divisibility system `q | R_r` at all rotations and **all fail**, as `12.8.3`'s own instances do. `12.8.5`'s strategic conclusion is unaffected at any grade.

### R6 — `cycles.md` Lemma 12.8.6.1, replaced (this is §6.7's recommendation, carried out)

Proposed, in full:

> **Theorem 12.8.6.1 (availability, unconditional).** Let `L = log_2 3` and
> `θ := 8 − 5L = 0.0751874964…`. Since `5L = 8 − θ`, stepping `n → n+5`
> decreases the fractional part `{nL}` by exactly `θ`; the fifteen points
> `n = N, N+5, ..., N+70` therefore lie exactly `θ` apart along a full turn
> (`14θ = 1.0526 ≥ 1`), so any arc of length `> θ` contains one of them. Hence
> **among any 71 consecutive integers there is an `n` with**
>
> ```text
> ⌈nL⌉ − nL  ≤  0.116939 ,       equivalently       γ(n) ≥ 3.68302 .
> ```
>
> The window `[1.585^p, 1.05·1.585^p]` holds `0.05·1.585^p` integers, which
> reaches `71` at `p = 16`. Since `sup_p Γ(p, 1.05·1.585^p) = 3.683012`
> (`12.8.6.2`), **every period `p ≥ 16` therefore has an `n` in that window
> meeting Construction B's hypothesis, unconditionally.** For `3 ≤ p ≤ 15` the
> hypothesis is met at an explicit `n` in the widened window `κ ≤ 2`, by direct
> check; `p ∈ {2, 4}` lie outside the construction's reach (`12.8.6.2`) and are
> covered by exhibition.
>
> **Proof.** The sweep and the arc are the display above. The threshold
> `0.116939` is `⌈nL⌉ − nL` at `γ = 3.683013`, since
> `γ = −log_2(1 − 2^(−(K − nL)))` is strictly decreasing in `K − nL`. ∎
>
> *What is consumed.* A **fixed density condition** on `⌈nL⌉ − nL`, with no
> `p`-dependence: no convergent denominator, no semiconvergent, no
> continued-fraction structure, no sign condition on a run, no membership in any
> chain, no irrationality measure. One exact number, `8 − 5L`, and the fact that
> it is positive and below `0.117`.
>
> *Superseded formulation (kept: the published v2 note points at it).* This
> lemma previously routed availability through the continued fraction of `L` —
> correctly-signed convergent runs and their semiconvergents — and named as its
> open gap a closed-form bound on the multiplicative gap between consecutive
> such runs. That route is now closed **in the other direction**, as a
> characterized obstruction rather than an unfinished proof: the multiplicative
> gaps in the convergent chain *are* the partial quotients, so a uniform bound
> on them is exactly the assertion that `L` is badly approximable — open for
> every classical constant and, by Borel–Bernstein with the measured
> Gauss–Kuzmin behaviour of this expansion, almost certainly false. The
> semiconvergent repair fails there too: the correctly-signed run following
> `q₁₃ = 190537` has length `a₁₅ = 1`. The chain is a sparse, sign-restricted
> subset of the candidate supply, and the construction never needed it. Nobody
> should attempt that route again.
>
> *Verified* (`experiments/staircase_allp_diophantine.py`, fresh code, exact
> integer arithmetic at every pass/fail decision): the sweep and the arc bound;
> brute force over `n = 1…3,000,000`, where the longest run of consecutive
> integers *all* failing the condition is **11**, against the proved bound `70`;
> the first good `n` and its offset from the window's left edge at every
> `p = 2…40`, largest offset `10`; and a negative control that fails where it
> must — an arc of length `θ/2` placed between two sweep points contains no
> sweep point at `399/399` starting values. The convergent desert at
> `p = 27…35`, which motivated the superseded formulation, is unremarkable
> under this statement: the witnesses sit at offsets `0…6` and none is a
> convergent or semiconvergent denominator.

### R7 — `cycles.md` Construction 12.8.6.2, replaced

Proposed, in full:

> **Theorem 12.8.6.2 (explicit construction; no correction step).** Notation as
> in `12.8` and `12.6.1`; write `η := −log_2(1 − 2^(−(S−p+1)))`, `β := 1 + η`,
> and
>
> ```text
> Γ(p, n) := [ (n−1)(L−1)² + L^(p−1)·(1 + β(L−1)) − (p−2+β)(L−1) − L ]
>            / [ (L−1)·(L^(p−1) − 1) ] .
> ```
>
> Let `p ≥ 2`, `n ≥ 1` be integers, `K = ⌈nL⌉`, `S = K − n`, `q = 2^K − 3^n`,
> `γ = K − log_2 q`, and assume **(H0)** `S ≥ p` and `(L−1)(n−p) + γ ≥ p + η`
> — a scale side-condition, automatic once `n ≳ 2.71p`, hence at every `p ≥ 6`
> at `n ≈ L^p` — and **(H1)** `γ ≥ max(2 + η, Γ(p,n))`. Set `T_(−1) = 0`,
> `s_crash = S − (p−1)`, and for `r = 0, …, p−2`
>
> ```text
> X_r      = 3^(T_(r−1)) · 2^(n − T_(r−1) + p − 1 − r) · (2^(s_crash) − 1)
> cap_r    = max{ m ≥ 0 : q·2^m ≤ X_r }          ( = bitlength(⌊X_r/q⌋) − 1 )
> budget_r = n − 1 − T_(r−1) − (p − 2 − r)
> m_r      = min(cap_r, budget_r),      T_r = T_(r−1) + m_r
> ```
>
> with `m_(p−1) = n − T_(p−2)`, `s_j = 1` for `j ≤ p−2`, `s_(p−1) = s_crash`.
> Then the profile has all entries `≥ 1`, `Σ m_t = n`, `Σ s_t + n = K`, **crash
> depth exactly `1`**, and satisfies `q ≤ R_r` at **every** rotation. No
> floating point occurs anywhere in the construction or its verification
> (`K = ⌈nL⌉` is `bitlength(3^n)`, `L` being irrational).
>
> **Proof.** Five steps, in `briefs/staircase-allp-construction-findings.md` §5:
> well-definedness (the greedy cannot die once `γ ≥ 2 + η`), growth against the
> real recursion `A_r = L·A_(r−1) + γ − r − β`, the closed form of `A_r` — whose
> requirement `A_(p−2) ≥ n−1` is, after clearing denominators, *exactly*
> `γ ≥ Γ(p,n)` — the landing `T_(p−2) = n−1`, and the size conditions, where
> `m_r ≤ cap_r` **is** one term of `R_r` and every term is positive. ∎
>
> *The shape, and the constant that was missing.* This is `12.8.3`'s own shape —
> geometric climb at ratio `≈ L`, unit exits, one crash — with the additive
> offset the pure geometric profile lacks. Asking for a real profile whose
> deficit is constant in `r` forces `T_r = C·L^r + r/(L−1) + b`, i.e.
> `m_r = C(L−1)L^(r−1) + 1/(L−1)`: **geometric plus a fixed
> `1/(L−1) = 1.70951` per block.** The offset's meaning is mechanical — at the
> exchange rate `L−1 = log_2(3/2)`, `1/(L−1)` units of standing depth generate
> exactly one bit of credit per block, precisely the one unit of exit valuation
> each climb block spends. A pure geometric profile therefore runs a deficit of
> exactly one bit per block, i.e. `Θ(p)` overall, which is what the superseded
> route (`12.8.6.3`) was repairing by hand.
>
> *Scope, exactly.* `Γ → 0.92714·κ + 2.70951 + η` with `κ = n/L^p`, so the
> demand is `O(1)` — **no `p`-dependence at all**, `≤ 3.6831` for `κ ≤ 1.05`,
> against the `O(log p)` the published `thm:staircase` assesses. `Γ` is
> **conservative by `0.6`–`0.9` bits**, because `(C_r)` keeps one term of `R_r`
> and discards `p−1` positive ones: (H1) is sufficient, not necessary.
> `p ∈ {2, 4}` are **outside the theorem's reach** — `Γ`'s coefficient on `n` is
> `(L−1)/(L^(p−1) − 1)`, large enough at those two periods that the required
> quality outruns what integers at that scale supply — and are covered by
> exhibited size-passers instead.
>
> *Verified* (`experiments/staircase_allp_construction.py`, fresh code,
> importing nothing from `staircase_allp.py`, `p22_passer.py` or
> `uniform_trim.py`; exact big-integer comparison at every pass/fail decision;
> committed output `experiments/staircase_allp_construction_output.txt`):
> a theorem-certified `n` within `≤ 11` of `round(L^p)` (mean `3.6`) at every
> `p ∈ {2,…,30}` outside `{2,4}`, each re-verified through `R_r` computed from
> `12.6.1` at all `p` rotations; `p = 31` and `p = 32` beyond that; each proof
> step checked separately over a grid of `(p,n)`, zero violations; and four
> negative controls that bite — the quality hypothesis fails `78`–`94%` of `n`
> in a window while never producing a false pass; the rounding rule is the whole
> content (**greedy saturation `29/29` against the superseded partial-sum
> rounding's `6/29` at the same `n`**, the latter's six successes all at
> `p ≤ 8`, failing `24` of `30` rotations at `p = 30`); the crash depth's
> derived ceiling brackets the largest passing `c` at every period; and local
> perturbation breaks the exact test at `δ = 1` or `2` at all `102` blocks
> tested, so the caps are genuinely saturated. A second, structurally different
> evaluator reproduces the composition independently
> (`experiments/staircase_allp_diophantine.py`, `p = 3…26`, Construction B
> transcribed from the statement rather than the code).

### R8 — `cycles.md` 12.8.6.3, demoted

Proposed, in full (replacing the current Algorithm text):

> **12.8.6.3 (superseded: the bounded correction).** The construction that
> `12.8.6.2` replaces rounded a *pure* geometric climb and then repaired the
> shortfall by a deterministic local search — repeatedly locate the worst
> rotation, move one unit of climb depth from a donor to a recipient block
> (never the crash block), accept whichever single move most improves the worst
> margin, until every rotation passes or a move budget is exhausted
> (`experiments/staircase_allp.py` Part D). It is recorded because the published
> v2 note names it, and because the reason it had to go is a result in its own
> right: each move buys `O(1)` bits while the pure-geometric profile's shortfall
> is `Θ(p)` (`12.8.6.2`), so its move count is `Θ(p)` at fixed `γ` and **no
> `O(1)` or `O(log p)` bound on it exists to be proved**. The observed counts —
> `0` at small `p`, `8` at `p ∈ {18, 23, 24, 25}`, `13` at `p = 22` — are that
> linear law, partially masked by the larger `γ` the chain candidates carried.
> `briefs/staircase-allp-findings.md` item 5.3, which proposed proving such a
> bound, is **refuted as a target**, not merely unachieved. The right move was
> not to bound the algorithm but to remove the shortfall, which `12.8.6.2` does.

### R9 — `cycles.md` 12.8.6.4, recalibrated

Two edits inside the existing Proposition; the instance record itself stands.

(i) After the displayed band, replace
> — a contiguous range.

by
> — a contiguous range. **The band is a property of the recipe's candidate
> list, not of the family:** these `γ` are those of the chain candidate nearest
> `1.585^p`, and they are not the smallest at which a staircase closes. With
> candidates drawn from the whole scale window the same profile-and-correction
> procedure closes `p = 24…35` at `γ/log_2 p ≈ 0.46…0.65` — `γ` roughly
> *constant* in `p`, not logarithmic — and `12.8.6.2`'s certified witnesses have
> `γ/log_2 p` falling with `p` (`0.97` at `p = 10`, `0.82` at `p = 22`, `0.61`
> at `p = 31`).

(ii) Replace the closing clause
> no halt condition was triggered — consistent with, but not a proof of, the assessed `γ = O(log p)` shape (`12.8.3`, `thm:staircase`).

by
> no halt condition was triggered. These instances are now the finite record
> beneath a proof (`12.8.6.1`–`12.8.6.2`), not evidence in place of one.

(iii) In **The two `p = 22` rows**, replace
> At `p = 22`, candidate availability — not combinatorial resistance — is the binding constraint: the candidate chain has a genuine hole at that scale

by
> At `p = 22` the binding constraint was candidate availability *within the
> recipe's own continued-fraction chain*, which has a hole at that scale

and append to that paragraph:
> Under `12.8.6.1`'s statement the episode does not arise: from `p = 8` upward
> not one working witness is a convergent or semiconvergent denominator, so the
> hole was a property of the candidate list, not of `log_2 3`.

### R10 — `cycles.md`, the grade paragraph replaced

Current:
> **Achieved grade: floor, substantially exceeded.** … the sole remaining gap in this floor-grade result is the Diophantine coverage bound of `12.8.6.1` (still open, per its status paragraph above). `12.8.5`'s strategic conclusion … is unchanged, as recorded above.

Proposed:
> **Scope, and what is not covered.** The all-`p` sharpness claim is **proved**:
> unconditionally for every `p ≥ 16` (`12.8.6.1` → `12.8.6.2`), by finite check
> for `3 ≤ p ≤ 15`, and by direct exhibition at `p ∈ {2, 4}`, which lie outside
> `12.8.6.2`'s reach. Three limits are part of the true statement and are not
> softened: `Γ` is conservative by `0.6`–`0.9` bits, so the certified family is
> narrower than the empirical one; `p ∈ {2,4}` have exhibited size-passers but
> no theorem covering them; and the independent verification stops at `p ≈ 32`
> on big-integer cost (`n ≈ 2.5·10^6`, `3^n` at `4·10^6` bits) — a limit on the
> check, not on the theorem, nothing in which degrades with `p`. What the
> published `thm:staircase` assesses at `γ = O(log p)` is reached at a demand
> that does not grow with `p` at all. `12.8.5`'s strategic conclusion (the cycle
> front stays parked; the residual content of cycle exclusion is anchor-walk
> rigidity) is unchanged, as recorded above: this is sharper evidence that
> counting cannot do better, and no evidence at all about exclusion.

*(If §0.1 lands, the penultimate sentence may read: `…is reached, and exceeded:
the constructed family's γ is bounded by an absolute constant, uniformly in p.`)*

### R11 — the downstream pointer pages

**`index.md` row (line 33)** — replace `staircase sharpness recipe at floor grade (12.8.6)` with `the staircase constructed at every period (12.8.6)`; the row's Status cell `periods 1–3 closed; front PARKED` is unchanged.

**`index.md` Current status (line 46)** — replace
> and the all-`p` staircase sharpness held at floor grade — verified instances for the full contiguous range `p ∈ {2,...,23}` (12.8.6), the Diophantine coverage bound its sole remaining gap

by
> and the all-`p` staircase sharpness now proved (12.8.6) — unconditionally for every `p ≥ 16`, by finite check below, with `p ∈ {2,4}` covered by exhibition

**`README.md` scoreboard (line 17)** — replace
> an explicit family shows counting arguments cannot do substantially better — sharp at the verified instances, assessed at every period (cycles.md)

by
> an explicit family shows counting arguments cannot do substantially better, now constructed at every period rather than exhibited at two (cycles.md)

**`TOUR.md` map row (line 14)** — replace the trailing clause
> and the post-publication attempt to prove the family at every period is **12.8.6** (floor grade; see below)

by
> and the post-publication proof of the family at every period is **12.8.6** (see below — the paper's own hedge sentence is unchanged; the wiki carries the proof)

**`TOUR.md` correspondence section (line 22)** — replace
> The attempt to close it is `cycles.md` **12.8.6**: a Diophantine lemma (semiconvergents of `log₂3`), an explicit profile, a bounded correction, and verified instances for the full contiguous range `p ∈ {2,…,23}` — an initial obstruction at `p = 22` was resolved 2026-07-17 via a second exchange with the same correspondent. Grade and gaps are stated in the section itself.

by
> It is closed at `cycles.md` **12.8.6**, in two independent halves: an
> availability theorem resting on one exact number, `8 − 5·log₂3`, and an
> explicit integer construction whose size conditions hold with no correction
> step. Unconditional for `p ≥ 16`, finite check below, `p ∈ {2,4}` by
> exhibition; scope and limits are stated in the section itself. The earlier
> route — semiconvergents of `log₂3`, a rounded geometric profile, a bounded
> correction, and verified instances for `p ∈ {2,…,23}` with an obstruction at
> `p = 22` resolved 2026-07-17 through the same correspondent — is what the
> published v2 note describes, and is kept there as the superseded formulation.

**`TOUR.md` pointers (line 23)** — append: `The two sessions that closed it are recorded at briefs/staircase-allp-construction-findings.md (the construction) and briefs/staircase-allp-diophantine-findings.md (availability, and the γ budget); briefs/staircase-allp-findings.md is the superseded earlier attempt.`

**`TOUR.md` code (line 24)** — replace `The verification code for all of it is experiments/staircase_allp.py …` with `The verification code is experiments/staircase_allp_construction.py and experiments/staircase_allp_diophantine.py (two independent implementations, exact big integers throughout); experiments/staircase_allp.py is the earlier route's, and experiments/uniform_trim.py produced the original instances.`

**`TOUR.md` vocabulary, "assessed" (line 39)** — the delicate one. Replace
> **assessed** — a stated judgment with evidence, explicitly not proved; the paper's `thm:staircase` sharpness half is the canonical example.

by
> **assessed** — a stated judgment with evidence, explicitly not proved. The paper's `thm:staircase` sharpness half is the canonical example and remains stated that way *in print*; the wiki has since proved it (`cycles.md` 12.8.6), which is exactly the divergence this page exists to make visible.

**`TOUR.md` vocabulary, "floor grade" (line 42)** — the tree has no floor-grade instance left. Either keep the definition unattached (it is a live delegation outcome that will recur) or add `— no result currently in the wiki stands at this grade.` I lean to keeping it as-is and adding nothing; recorded as a judgment call, not a defect.

**`HANDOFF.md` Cycles bullet (line 19)** — replace `staircase sharpness at floor grade, contiguous p ∈ {2,...,23}` with `staircase sharpness proved at every period, 12.8.6`. And collapse the two items both numbered `4` (lines 85–86), now delivered and merged, into that bullet; the duplicate numbering is a separate small defect, recorded here and not repaired by this session.

**`briefs/staircase-allp-findings.md`** — *optional, low priority*: a one-line header `**Superseded (2026-07-28).** Both gaps this file records are closed; the current record is briefs/staircase-allp-construction-findings.md and briefs/staircase-allp-diophantine-findings.md.` The file already carries a supersession section, so the house style permits it; leaving it untouched is equally defensible since it is a dated record.

### R12 — `publication.md`, the hedge-status entry

Current:
> **Sharpness-hedge status:** the published `thm:staircase` hedge ("we assess … though not proved here for all `p`") stands; the delegated attempt reached floor grade — a general per-period construction recipe plus verified instances for the full contiguous range `p ∈ {2,...,23}` (`cycles.md` 12.8.6; the `p = 22` candidates from the correspondent's pincer hypothesis, `briefs/merle-pincer-check-findings.md`) — not the all-`p` proof. The hedge sentence is not upgradable; better evidence, not a closure, is what v2 added.

Proposed:
> **Sharpness-hedge status:** the assessed claim is now **proved** in the wiki (`cycles.md` 12.8.6 — unconditional for `p ≥ 16`, finite check below, `p ∈ {2,4}` by exhibition), at a `γ` demand that does not grow with `p`, which is stronger than the published `O(log p)`. The published sentences are not falsified by this: `thm:staircase`'s first sentence and its closing consequence are quantified over all configurations satisfying the size conditions and are simply now true at every period, and its hedge clause says "not proved *here*", which remains a true statement about the paper. **One published sentence is now wrong** — the v2 note's identification of the remaining gap (both halves: the bound is not needed, and the `p = 22` episode was a property of the candidate list, not of `log₂3`). Whether the hedge clause can be *restated* turns on a question that is the author's and is not decided here: whether Construction B is `thm:staircase`'s own "staircase family" better specified, or a different family — the case each way is laid out at `briefs/staircase-status-audit-findings.md` §4.4. Options for the published record, with costs, are at §4.3 of the same file; the standing recommendation is wiki-only now, an erratum correcting the v2 note's gap sentence once 12.8.6 is settled, and no v3 until the family question is answered.

### R13 — the v2 note's gap sentence (a **draft for an erratum**, not an edit)

`paper/` and `sources/` are frozen and untouched. This is the replacement text
for the erratum option at §4.3, built from
`briefs/staircase-allp-diophantine-findings.md` §5(b) **with its stale last
sentence repaired** — as drafted there, that sentence still says the
construction half is unproved and names the correction algorithm's move count,
which the sibling result removes from the argument entirely.

Current published text (v2 note, third-from-last sentence):
> The remaining gap is the one already named: no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs --- the bound that would certify no period is skipped --- and the $p = 22$ episode is a demonstration that this gap bites in practice, not only in principle.

Proposed replacement:
> *(Correction, 2026-07-28.)* The gap named in this note has since been closed,
> and closed by replacing the route rather than completing it. Candidate
> availability needs no continued-fraction input: among any 71 consecutive
> integers there is an `n` with `⌈n log₂3⌉ − n log₂3 ≤ 0.117`, because
> `8 − 5log₂3 = 0.07519…` is positive and smaller than that, and the scale
> window contains far more than 71 integers at every period from 16 onward.
> The bound on the multiplicative gap between correctly-signed runs is not
> needed, and as posed it is a dead end — a uniform bound on those gaps is
> exactly the assertion that `log₂3` is badly approximable. The `p = 22` episode
> was a property of the candidate list used, not of `log₂3`: at candidates drawn
> from the whole window the same construction closes every period tested. The
> construction half is closed independently: a corrected profile — the geometric
> climb with a fixed additive offset `1/(log₂3 − 1)` per block, absent from the
> profile described above — satisfies all `p` size conditions **by
> construction**, with no correction step, so the bounded correction is removed
> from the argument rather than bounded. The current record is `cycles.md`
> §12.8.6 of the project repository.

**Do not send this without a decision on §4.4.** As drafted it corrects only the
gap sentence and says nothing about the hedge — deliberately, since restating
the hedge requires the family judgment.

---

## 3. The three named recalibrations

### 3a. The "Achieved grade" paragraph — wrong twice over, and the obvious repair is wrong too

The sentence is *"the sole remaining gap in this floor-grade result is the
Diophantine coverage bound of `12.8.6.1`"*. Both nouns fail:

1. **"floor-grade result"** — the primary theorem the floor was measured against
   is now proved.
2. **"the Diophantine coverage bound … the sole remaining gap"** — that bound is
   not a remaining gap. It is not needed (Construction B consumes a fixed
   density condition, not a chain), and the route as posed is a *characterized
   obstruction*, not an unfinished proof.

**And the repair the sibling findings suggest is itself stale.**
`briefs/staircase-allp-diophantine-findings.md` §5(c) proposes that the sentence
*"should become the correction algorithm's move count"*. That was written
against the interface as it then stood; the construction session removed
Algorithm `12.8.6.3` from the argument altogether, so the move count is not a
remaining gap either — there is nothing left for the sentence to name. The
paragraph must be replaced rather than patched, which is what **R10** does. This
is the "wrong twice over" the brief flags, plus a third turn nobody had caught.

### 3b. 12.8.6.4's band `γ/log₂p ∈ [1.828, 3.643]`

The band is what the recipe produced **from candidates drawn out of the
continued-fraction chain**, at the chain member nearest `1.585^p`. It is not a
property of the staircase family and should not be read as one. Evidence:
window-wide candidates close `p = 24…28` at `γ/log₂p ≈ 0.46…0.65`, decreasing
(`briefs/staircase-allp-diophantine-findings.md` §3, the rows where the
sharpening pass ran to completion — the `p = 29…35` rows are capped-budget
upper bounds and must not be read as measurements); and `12.8.6.2`'s certified
witnesses have `γ/log₂p` falling monotonically in `p`. Drafted at **R9(i)**.

### 3c. Algorithm 12.8.6.3 — keep it, clearly marked superseded

**Recommendation: keep, demoted, in one paragraph under its own number, out of
the argument's main line.** Three reasons.

1. **The published v2 note names it** — "a bounded correction closes the last
   bits". A reader arriving from the paper must be able to find what that named.
   Deleting it makes the published note unresolvable against the wiki, which is
   the one thing `TOUR.md` exists to prevent.
2. **The negative result attached to it is load-bearing and worth keeping.** Its
   move count is `Θ(p)`, so `briefs/staircase-allp-findings.md` item 5.3's
   proposed `O(1)`/`O(log p)` bound *does not exist*. A future session that
   deletes the algorithm without that sentence will re-propose the bound.
3. **`AGENTS.md`'s own rule**: refuted and failed routes are kept with the
   evidence that killed them, not deleted.

*Counter-consideration, recorded honestly:* `AGENTS.md` also says a page states
the current answer and carries no change log, and §12.8.6 would end up with
three superseded objects (the chain framing inside `12.8.6.1`, the pure
geometric inside `12.8.6.2`, and `12.8.6.3` entire). The mitigation is that each
is kept as a *named object the published record points at*, consolidated into
one clause or paragraph rather than narrated, and never as "was X, now Y" prose.
If the main session judges that still too diary-like, the fallback is to keep
only `12.8.6.3`'s paragraph (the one the paper names) and move the other two
supersessions into this findings file by pointer. I prefer the version drafted,
but this is a close call and I flag it as such.

---

## 4. The published record

`paper/collatz-reduced-v2.tex` corresponds to a published artifact — v2, DOI
10.5281/zenodo.21421120 — and the PDFs and `sources/` are frozen. Nothing in
`paper/` or `sources/` was edited by this session.

### 4.1 Which published sentences are affected, quoted

**(i) `thm:staircase`, first sentence.**
> No trim uniform in $p$ can extend the small-period constants: there exist configurations satisfying every rotation's exact size condition $q \le R_r$ whose $\gamma$ falls far below any polynomial-in-$p$ extension of the constants of periods $2$--$3$.

**Understated, not wrong.** As printed it is an existence claim, and the wiki's
own adjudication already reads it as a theorem by exhibited witness (`p = 7`,
`n = 94`, `γ = 6.74`; `briefs/jointnote-premise-ours-findings.md`). It is now
true at *every* period. No erratum owed.

**(ii) `thm:staircase`, the hedge clause.**
> and we assess (supported by the verified instances, though not proved here for all $p$) that it passes all size conditions with $\gamma = O(\log p)$ for every $p$.

**Understated, not wrong — and not falsified.** "not proved *here*" is a
statement about the paper and remains exactly true: the paper contains no such
proof. A later proof elsewhere does not falsify it. It is understated in two
independent directions: the exponent `O(log p)` is more than the theorem's own
job needs (any `ρ^p` with `ρ < 1.585` suffices —
`briefs/staircase-allp-diophantine-findings.md` §1), and the constructed family
does better than `O(log p)`. Whether it can be *restated* depends on §4.4.

**(iii) The abstract's dichotomy sentence.**
> an explicit family of near-counterexamples (\emph{staircases}: geometric climbs closed by a single crash, precisely divergent-orbit profiles bent into loops) shows counting arguments cannot do substantially better, so uniform cycle exclusion requires arithmetic (divisibility) input, not sharper counting.

**Understated, not wrong.** It carries no status word and no for-all-`p`
quantifier; its conclusion is now better supported. No erratum owed.

**(iv) The v2 note's gap sentence.**
> The remaining gap is the one already named: no proved closed-form bound on the multiplicative gap between consecutive correctly-signed semiconvergent runs --- the bound that would certify no period is skipped --- and the $p = 22$ episode is a demonstration that this gap bites in practice, not only in principle.

**WRONG, on both halves, and it is the only wrong sentence in print.**
*Half 1:* the bound is not needed — the requirement it served ("no period is
skipped") is proved by a counting route with no chain, no sign condition and no
partial-quotient hypothesis. Worse, the bound as posed is a dead end: uniform
multiplicative gaps in the convergent chain *is* the badly-approximable
assertion for `log₂3`. *Half 2:* the `p = 22` episode was a property of the
candidate list — the recipe drew from the chain — not of `log₂3`; from `p = 8`
upward not one working witness is a convergent or semiconvergent denominator.

**Two mitigating facts, both real.** The note's own repository pointer is
**pinned to a frozen commit** (`…/blob/72ec88e/cycles.md`), so a reader who
follows the citation lands on the §12.8.6 text the note correctly describes, not
on the current one; the note is wrong about the mathematics, not internally
inconsistent with its own citation. And the note's closing sentence — "The hedge
sentence above is therefore unchanged: finite-range evidence supports the
assessed `γ = O(log p)` behaviour, but does not prove it for all `p`" — is a
statement about the paper and remains true.

**(v) Version note, Discussion, Related work.** `No theorem or universal claim is
strengthened; v2 adds a finite computational evidence record` is true of v2 as
published. `rigidity statements for closed anchor walks beyond the size level
(the only route past Theorem~\ref{thm:staircase})` and the `merle` related-work
clause are **UNAFFECTED** and better supported. No action.

### 4.2 Wrong versus understated, in one line

**One sentence is wrong: the v2 note's gap sentence.** Everything else in print
is understated. That asymmetry is the whole shape of the decision — an erratum
is the standard instrument for a false statement about what remains open; no
instrument at all is owed for an understatement.

### 4.3 Options, costs, and what a referee would expect

**Option 1 — leave the published record alone; carry the update in the wiki
only.**
*Cost:* effectively zero; it is the work §2 proposes anyway. *What a referee
expects:* nothing. No published claim is falsified, and a repository is the
correct home for post-publication development — this paper already points at it
by name and by pinned commit. *Risk:* the one wrong sentence stays in print, and
it is a sentence about an open problem, i.e. exactly the kind a referee or a
correspondent quotes. *Mitigation, and it is strong:* the pinned citation means
the paper is self-consistent, and a restated §12.8.6 that keeps the convergent-run
framing as a *named superseded formulation* corrects any reader in one hop. That
mitigation only exists if R6's superseded-formulation paragraph is kept.

**Option 2 — publish an erratum.**
*Cost:* low. One paragraph (drafted at **R13**), no re-typesetting of theorems,
no change to any proof. On Zenodo this is a new version record under the same
concept DOI; the v2 DOI keeps resolving. *What a referee expects:* an erratum is
the normal instrument here, and one that corrects a statement about an open gap
— rather than a claim — reads as good practice, not as a retraction. *Risk:* an
erratum that corrects the gap sentence invites "so is the hedge lifted?", which
forces §4.4 into print before the author has answered it. *Therefore:* if chosen,
the erratum should correct **only** the gap sentence and be silent on the hedge,
pointing at the repository for the current state. R13 is drafted that way.
*Sequencing:* do it **after** §12.8.6 is restated and merged, so the erratum
points at settled text.

**Option 3 — prepare a v3.**
*Cost:* high, and higher than it looks. It means a new mathematical subsection
carrying Theorem B's five steps and Lemma D (both short — this is not the
problem), plus: a second external referee pass, by the house's own record
("Both papers passed external referee cycles before publication"); a new DOI
version; an explicit scope statement for `p ∈ {2,4}`, `p ≤ 15`, and `Γ`'s
conservativeness; the §0.1 two-sided lemma if `γ = O(1)` is claimed; and — the
item that actually decides it — an answer to §4.4, because a v3 either restates
`thm:staircase` or adds a separate theorem beside it. It also reverses v2's own
Version note, which was careful to say "No theorem or universal claim is
strengthened". *What a referee expects of a v3:* the proof in full; the scope
holes stated rather than elided; and a clear statement of whether the family
proved is the family the v1/v2 theorem described.

**Recommendation.** *Option 1 now; Option 2 once §12.8.6 is restated and merged;
Option 3 not yet.* Reasoning: only one sentence is wrong and it is about an open
gap, not a claim; the wiki restatement is owed regardless and is the cheapest
complete fix; the erratum is worth making but should point at settled text; and
a v3 has two prerequisites (§4.4 and §0.1) neither of which is urgent. **One
sequencing note, flagged and not decided:** if the joint note with the
correspondent happens, that is the natural place for this proof to appear in
print first, which would make a v3 unnecessary. What goes to Merle is not this
session's.

### 4.4 The judgment that is the author's: same family, or a different one?

`thm:staircase`'s hedge attaches to a described construction:
> The construction --- block depths growing geometrically at ratio $\approx\LL$ with unit exit valuations, closed by a single block of unit depth and maximal exit valuation --- tracks the extremal configuration of the max-plus recursion in the proof of Theorem~\ref{thm:uniform}, and we assess … that it passes all size conditions with $\gamma = O(\log p)$ for every $p$.

Construction B is that shape with one addition: each climb depth carries a fixed
additive offset `1/(L−1) = 1.70951` on top of the geometric term. Is the family
the published sentence names therefore **the same family, better specified**, or
**a different family**? I lay out both and adjudicate neither.

**The case for *the same family, better specified*.**

1. **Every clause holds verbatim.** Ratio `≈ L`: `m_r/m_(r−1) → L` exactly,
   since the offset is a constant against a term growing like `L^r`. Unit exit
   valuations on the climb: `s_j = 1`. A single closing block: yes. **Of unit
   depth**: Theorem B *proves* crash depth is exactly `1` — tighter than the
   wiki's own recipe, which allowed `c ∈ {1,2}`. Maximal exit valuation:
   `s_(p−1) = S − (p−1)`.
2. **The published description is a shape, not a formula, and never specifies a
   rounding rule.** "Round the partial sums of the pure geometric" was the
   *wiki's* later choice (`12.8.6.2`), not the paper's. What failed is not
   something the paper said.
3. **The paper's own witnesses are members.** The `p = 7`, `n = 94` staircase
   `m = (4,7,9,15,23,35,1)` is reproduced and re-verified as a size-passer by
   both delegate evaluators at `γ = 6.744`. It is not a Construction B *output*
   — Construction B at `p = 7` returns `n = 29` — but 12.8.6.4 already records
   that the family is not unique at a given period, and 12.8.3 records 84
   size-passers at `p = 6` alone. A family with many members per period is not
   identified with one algorithm's output.
4. **The offset is bookkeeping the published sentence already implies.** At the
   exchange rate `L−1 = log₂(3/2)`, `1/(L−1)` units of standing depth generate
   exactly one bit of credit per block — precisely the one unit of exit
   valuation each climb block spends. The published sentence stipulates unit
   exits; the offset is what unit exits cost, made explicit.
5. **The published sentence's own extremality clause fits Construction B better
   than it fits the wiki recipe.** It says the construction "tracks the extremal
   configuration of the max-plus recursion". Construction B is defined by
   *saturating* the exact size condition at every block, and NC-D confirms it
   sits on the boundary — perturbing any block by `1` or `2` breaks the exact
   test at all `102` blocks tested. On this reading Construction B is the more
   faithful realization of what was printed.

**The case for *a different family*.**

1. **NC-B is the hard evidence.** At the *same* `n`, same shape, same crash
   depth, changing only the integer-rounding rule: greedy saturation passes
   `29/29`, the pure geometric `6/29`, and its six successes are all at
   `p ≤ 8`; at `p = 30` it fails `24` of `30` rotations. So the profiles
   satisfying the size conditions are a thin subset of "geometric at ratio `≈ L`
   with unit exits and one crash", and the offset is what selects it. **A family
   description that admits profiles failing at every large `p` is not the family
   with the asserted property.**
2. **The shortfall is `Θ(p)`, not a rounding detail.** A reader who builds the
   most natural profile from the published sentence is short by roughly one bit
   per block, growing linearly in `p`. That is a structural defect of the
   description.
3. **The paper exhibits no member of the constructed family.** Its `p = 7`
   witness is of the shape but is not a Construction B output. A restated
   theorem would be about a family the paper exhibits nothing from.
4. **The quantifier structure changes.** The proved statement carries (H0),
   (H1), the quality condition `⌈nL⌉ − nL ≤ 0.117`, a finite check below
   `p = 16`, and the exclusion of `p ∈ {2,4}`. "For every `p`" becomes "for
   every `p ≥ 16`, plus a finite check, minus two periods". A restatement that
   changes the quantifier is arguably a different statement, not a sharper one.
5. **Register.** The house norm claims a proof only for what was proved, and
   `AGENTS.md` requires math statements be edited conservatively. Stating the
   new result as a *new theorem* rather than as a lifted hedge is the
   conservative reading.

**What each answer implies.** *Same family better specified* → the hedge clause
can be restated (v3 or erratum) as proved-with-scope, and `12.8.3` can carry the
same. *Different family* → the published hedge stands as written and is not
restated; the wiki records a **new** result — sharpness proved at an explicit
sub-family — which *implies* the published theorem's headline dichotomy without
lifting its hedge sentence, and `cycles.md` gets a new statement rather than a
rewritten `12.8.3`.

**One structural fact that lowers the stakes either way, and it is worth having
before deciding.** The family question binds **only the hedge clause**.
`thm:staircase`'s first sentence and its closing consequence ("Uniform cycle
exclusion therefore requires the divisibility system --- equivalently, rigidity
of the closed anchor walk"), the abstract's dichotomy sentence, and the
Discussion's "the only route past Theorem~\ref{thm:staircase}" are all
quantified over *configurations satisfying the size conditions*, not over a
named family. Those are now true at every period regardless of how §4.4 is
answered, and need no decision at all.

### 4.5 One flag for the author, no proposal

The joint-note contribution sentence the correspondent asked for directly is
affected — `briefs/jointnote-premise-ours-findings.md` records that
"provably cannot close them uniformly" was *exactly half proved*, the all-`p`
half carrying the published hedge. That half is now proved in the wiki. This
changes what an honest contribution sentence can say. **Recorded only.** What
goes to Merle — ledger, note or reply — is a later decision and explicitly not
this session's; nothing here is drafted for any of them.

---

## 5. What does NOT change — confirmed by reading, not assumed

Each item below was read in full at its source in this session.

1. **Consequence 12.8.5's strategic conclusion — UNAFFECTED.** Read at
   `cycles.md` line 297. It rests on exactly two things: 12.8.2's search bound
   at `p = 92` being infeasible, and 12.8.3 showing no size-level lemma can
   lower it. The new results strengthen the second (from assessed at two periods
   to proved at every period) and touch the first not at all. Its own closing
   sentence — *"This conclusion is unchanged by `12.8.6` below, at any grade —
   that subsection only recalibrates the sharpness evidence of `12.8.3`; it
   settles nothing about exclusion."* — was written for precisely this case and
   is now doing that work. **No proposal in §2 alters it**; the only optional
   change is a pointer clause, and I recommend even that be skipped, because the
   sentence is already correct and the sibling session is editing the same
   sentence's `p = 92` figure.
2. **The cycle front stays PARKED — UNAFFECTED.** Both delegate sessions
   constructed **size-passers only**. Each touched the divisibility system
   solely to confirm that every constructed instance **fails** `q | R_r`:
   construction findings §7 (all `p ∈ {2,…,32}`, all rotations, zero divisible),
   diophantine findings §3 (an explicit HALT-and-exit guard that never fired).
   No per-period cycle search was run; no divisibility-based exclusion was
   attempted. The front's reopening condition — "a divisibility-aware
   (anchor-rigidity) idea, not more computation" — is untouched, and nothing
   proposed here supplies one or claims to.
3. **README's stopping rules — UNAFFECTED.** Read in full at line 36, all three:
   *(i)* "No per-period cycle search runs, period" — none was run, and none is
   proposed. *(ii)* "The cycle front reopens only with a divisibility-aware
   (anchor-rigidity) idea, not more computation" — unchanged; this result is
   explicitly *not* such an idea and says so. *(iii)* "The equidistribution
   question is treated as long-range" — untouched entirely. **No proposal in §2
   touches any of the three sentences.** The one README edit proposed (line 17,
   the scoreboard) is in a different section and states a grade, not a rule.
4. **README's strategy paragraph's logic — UNAFFECTED.** Line 34's chain
   ("explicit family → counting cannot do better → refutes the crossover plan")
   is strengthened at its middle link and unchanged at its conclusion. The
   crossover refutation was never contingent on the all-`p` grade.
5. **Remark 12.8.4 — UNAFFECTED.** The staircase as a divergent-orbit profile
   bent into a loop, and the two-halves-one-problem reading, are strengthened
   and unaltered.
6. **`bridge.md`, `aeh.md`, `stage4.md`, `program.md`, `open-problems.md`,
   `anchors.md`, `itinerary.md`, `ladder.md`, `reverse.md`, `spine.md`,
   `stage1–3` — UNAFFECTED.** None states the sharpness grade. Noted in passing:
   `bridge.md` line 79 already reads *"the staircase family **proves** no
   size-counting argument does better"* — a wording that was ahead of the record
   and is now exactly right. Recorded; no change proposed.
7. **`viz/` — UNAFFECTED, and checked rather than assumed.** Grepped over the
   whole directory on `staircase|12\.8\.6|floor grade|assessed` and on
   `12\.8|uniform trim|sharpness`: **zero matches.** No visualization carries a
   status statement about this claim, including `cycle_anchor_gateway.html`.
8. **Theorems 12.8.1, 12.8.2 and Proposition 12.6.1 — UNAFFECTED.** The new
   results *consume* `12.6.1`'s `R_r` and `12.8`'s `γ`; they modify neither, and
   nothing about the trim's own statement, constant or effectivity moves.
9. **AEH and the statistics front — UNAFFECTED.** No equidistribution work was
   touched by either session; `aeh.md` 13.3.3's "individual staircase tails not
   excluded" is unchanged and remains the correct scope statement.

---

## 6. Application order, risk, and what a reviewer should re-check

**Two prerequisites, neither of them an edit.**

* **P1 — the `γ = O(1)` gate (§0.1).** The main session re-derives the two-sided
  form of Lemma D and decides whether any page may state `γ = O(1)` as proved.
  Every drafted text above marks its `γ`-bound clause as conditional on this.
* **P2 — the family judgment (§4.4).** The author's. Gates R12
  (`publication.md`), R13 (the erratum draft), any restatement of the *published*
  claim, and any rewrite of `12.8.3` beyond its pointer sentence.

**Then, in this order.**

| step | edit | grade | what a reviewer re-checks |
|---|---|---|---|
| 1 | **`cycles.md` §12.8.6 rewritten** — R5, R6, R7, R8, R9, R10, in that internal order | **substantive** | that Theorem B's hypotheses (H0)/(H1) and `Γ` are transcribed exactly from `briefs/staircase-allp-construction-findings.md` §5 and not paraphrased; that Lemma D's `θ`, the `0.116939` threshold and the `p = 16` crossing are re-derived independently; that the `p ∈ {2,4}` and `p ≤ 15` scope clauses survive every draft; that no sentence claims a bound on `γ` unless P1 landed; that the divisibility-fails clause is present |
| 2 | `cycles.md` 12.8.3 pointer sentence (R4) and §12.8 preamble (R3) | **substantive** | that 12.8.3's own recorded instances are untouched, and that the preamble's new clause is quantified exactly as §12.8.6 is |
| 3 | `cycles.md` front matter + Current-state paragraph (R1, R2) | mechanical *given* 1–2 | that the status line's scope matches §12.8.6's own scope word for word |
| 4 | `index.md` row + Current status; `README.md` line 17; `TOUR.md` rows 14/22/23/24; `HANDOFF.md` line 19 (R11) | mechanical | that each is a *pointer* and restates no fact (`AGENTS.md`: every fact lives in exactly one page); that `TOUR.md`'s correspondence section still resolves the published note's vocabulary |
| 5 | `TOUR.md` vocabulary entries, "assessed" and "floor grade" (R11) | **substantive** | that "assessed" still describes the published sentence correctly — this is the one place the paper/wiki divergence is *defined* for external readers |
| 6 | `publication.md` hedge-status entry (R12) | **substantive; gated on P2** | that it decides nothing §4.4 leaves open, and that "not upgradable" is not replaced by an equally strong claim in the other direction |
| 7 | the published-record decision (§4.3), and R13 if Option 2 | author's | that the erratum corrects only the gap sentence and is silent on the hedge |

**Safe mechanical status changes:** steps 3 and 4 — but "mechanical" means the
*fact* is settled by step 1, not that no judgment is involved; each still
carries a status word.
**Substantive restatements needing their own review:** steps 1, 2, 5, 6.

---

## 7. Interaction with the sibling session, and things I am less than confident in

**Sibling (`record-defects-repair`).** It may edit `README.md`'s strategy
paragraph and `cycles.md` 12.8.5 or 12.8.2 for the `p = 92` figure, and
`cycles.md` §12.6.1 for the undefined `σ`. **No proposal here touches §12.6.1,
§12.8.1 or §12.8.2.** The only overlap is `cycles.md` 12.8.5 and `README.md`
line 34, and in both I propose *no change* (§5 items 1 and 4), precisely so the
sibling's numeric repair lands cleanly. `README.md` line 17 (the scoreboard) is
a different paragraph from line 34 (the strategy section) and does not collide.
`HANDOFF.md`: my paragraph is a single new block; I touch no line of the
sibling's.

**Less than confident, in order.**

1. **§0.1, the two-sided Lemma D.** I checked the arithmetic at 60–80 digits and
   brute-forced it, and I believe it. But it is *new mathematics introduced at
   audit* by a session briefed to propose status, not to prove things. It should
   be re-derived by the main session and, if it is to be stated in `cycles.md`,
   verified by fresh code like anything else. Until then no page should say
   `γ = O(1)` is proved. **This is the item most likely to be wrong in its
   consequences, not in its arithmetic** — specifically, I have not checked
   whether the two-sided condition interacts badly with (H0) at the smallest
   `p ≥ 16`, only that it holds at `κ ∈ [1, 1.05]` where `Γ ≤ 3.6831`.
2. **The in-place replacement of `12.8.6.1`–`12.8.6.3`** (§2, structural
   recommendation). Numbers keep their roles, which I think is right, but the
   correspondent cites `12.8.6.1` as "the Diophantine coverage bound" and after
   the edit that number resolves to a different statement. The
   superseded-formulation paragraph is the mitigation and must not be dropped.
   The alternative — new numbers `12.8.6.5`/`12.8.6.6` — is defensible and I may
   be wrong to have argued against it.
3. **§3c, keeping three superseded objects in §12.8.6.** It is the right call
   against `AGENTS.md`'s "keep failed routes" rule and the wrong call against its
   "no change logs" rule. I chose keep-and-demote; the fallback (keep only
   `12.8.6.3`, the one the paper names) is in §3c.
4. **`TOUR.md`'s "assessed" vocabulary entry (R11).** The draft makes the entry
   describe a paper/wiki divergence rather than a status word. That is honest but
   it changes what the entry is for, and a cleaner solution may be to pick a
   different canonical example. I could not find a better live one in the tree,
   which is itself worth knowing.
5. **`briefs/staircase-allp-diophantine-findings.md` §5(a).** I have recorded it
   as internally stale relative to its own §6 and proposed nothing. If the main
   session disagrees with my reading — that Construction B makes §5(a)'s "nothing
   here proves the construction succeeds" no longer the operative statement —
   then several of my "proved" verdicts weaken with it. This is the single
   reading on which the whole audit's status verdict rests, and it deserves an
   explicit yes/no at review.
