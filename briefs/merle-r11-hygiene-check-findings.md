# Findings: round-11 hygiene verification + the four negative measurements

Delegated session, 2026-07-27/28. Brief: `briefs/merle-r11-hygiene-check-brief.md`.
Branch `merle-r11-hygiene-check`, **base commit `e938040`** — launch note, for the
record: the worktree was cut at the session-start HEAD `2225b68`, which does not
contain the brief; it was rebased onto `e938040` (the brief commit, current
`main`) before any work started, exactly as the rules require.

Register: flat. Discrepancies are recorded with each value and its provenance,
never disputed in prose. No key is turned, no ledger text is written, no reply
paragraph is drafted. No pushes anywhere; both Merle-side repositories cloned
read-only into the scratchpad; no interaction of any kind with them (no fork,
issue, star, watch or comment).

Verification code: **one script**, `experiments/merle_r11_hygiene_check.py`
(committed output alongside), covering **both halves** — the brief allowed one
or two and asked which; it is one. Fresh code: it imports nothing from either
Merle repository and nothing from any earlier `merle_*` check in this
repository. Fixed-point big-integer logarithms are built in-house from the
`atanh` series at **two working precisions** with agreement asserted between
them (130 and 210 digits for half 1; 2600 and 3000 for the continued-fraction
work of half 2; 160 digits of `mpmath` for section L, where the quantities
compared differ at the 45th decimal). Every decision that can be an exact
integer is an exact integer. `mpmath` is used only for π's continued fraction
and for section L. **115 recorded checks, 0 failures.**

Stopping-rule compliance: this verifies a correspondent's artifacts and checks a
small number of exact identities. No new computational front is opened; **the
cycles front stays PARKED**. Item 3 of his negatives (the neighbours) was
explicitly *not* turned into a cycle search over other `a` — see §4.3, where the
want is recorded and stopped.

---

## 1. The repositories, read-only, and the artifact/script pairing

Fresh unauthenticated clones into the scratchpad (2026-07-27), no writes:

| repo | HEAD | note |
|---|---|---|
| `ericmerle3789/one-obstruction-three-faces-lean` | **`c991430`** | two commits over the round-10 pin `5c9b663`: `6c084c5` (the hygiene pass + the ceiling repair) and `c991430` (the restored standalone RETRACTED block) |
| `macindoe/one-obstruction-three-faces` (shared) | **`c966875`** | unmoved — this is *our own* round-10 co-edit push. **Nothing of the round-11 hygiene pass has reached the shared LEDGER**; it is all artifact-side. |

That second row is load-bearing for item 7 below: every "correction accepted"
that lives in ledger prose is by construction *not yet landed*, because the
ledger has not moved. What can have landed is what lives in his Lean repository.

### 1.1 Do the three orphan outputs now have generator scripts?

Yes, all three, added in `6c084c5`:

- `test_REQ-MATH-043_seuils_constante_prouvee.py` (90 lines, new)
- `test_REQ-MATH-055_fenetre_entiere.py` (66 lines, new)
- `test_REQ-MATH-056_decharge_entiere.py` (80 lines, new)

Each carries a header saying it was written retroactively on 2026-07-26 because
the output had been deposited without it, and each names our audit as the
finder. Each ends with a self-check that compares its own computed values
against the committed figures and exits non-zero on a mismatch.

### 1.2 Executed, not merely read

The brief said "where you can execute, execute". All five relevant scripts
(043, 055, 056, and the repaired 052, 053) are plain Python + `mpmath` and were
**run here**, in the scratchpad clone, and their output diffed against the
committed `OUT_REQ-MATH-*.txt`:

| script | exit | diff against committed OUT |
|---|---|---|
| `test_REQ-MATH-043` | 0 | **byte-identical** |
| `test_REQ-MATH-055` | 0 | **byte-identical** |
| `test_REQ-MATH-056` | 0 | identical except one em-dash rendered as `?` by this machine's cp1252 console — a local artefact of our redirect, not a difference in the file |
| `test_REQ-MATH-052` | 0 | **byte-identical** |
| `test_REQ-MATH-053` | 0 | identical except the same one em-dash |

So the pairing claim is confirmed at the strongest available grade: the
committed outputs are exactly what the committed scripts produce, today, on a
different machine. (Running his scripts is the *pairing* check only; every
number below is independently recomputed in our own code, which never imports
his.)

---

## 2. Half 1 — the hygiene claims, per claim

All "ours" values are from `experiments/merle_r11_hygiene_check.py`.

### 2.0 The main-session pre-check, re-derived independently

Under the pinned convention `q₀ = q₁ = 1` **both counted** (our continued
fraction built from scratch, partial quotients identical at both precisions
through all 60 terms used):

`q = 1, 1, 2, 5, 12, 41, 53, 306, 665, 15601, 31867, 79335, 111202, 190537, 10590737, 10781274, 53715833, 171928773, 225644606, 397573379, 6189245291, 6586818670, 65470613321, 137528045312, 753110839881, …`

| pre-check | ours | verdict |
|---|---|---|
| `q₁₃ = 190537` | 190537 | **confirmed** |
| `q₂₁ = 6586818670` | 6586818670 | **confirmed** |
| `q₂₂ = 65470613321` | 65470613321 | **confirmed** |
| `q₂₃ = 137528045312` | 137528045312 | **confirmed** |

Cited as the main session's pre-check and re-derived here independently. Every
index in his hygiene list is correct on that convention. Cross-checks: the
project's known scales `5, 12, 41, 53, 306, 665, 15601, 190537` all appear; the
convergent sides alternate (even `j` below `log₂3`, odd `j` above) by exact
integer comparison `2^{p_j}` vs `3^{q_j}`; and the classical sandwich
`1/(q_j+q_{j+1}) < θ_j < 1/q_{j+1}` holds for `j = 1..27`.

### 2.1 The per-claim table

| # | his claim (committed figure) | ours, independently | verdict |
|---|---|---|---|
| 1 | `C₀ = −14.949` under `c_gen` | `−14.9487` | **match** |
| 2 | `C₀ = −14.954` under `1/13` | `−14.9535` | **match** |
| 3 | per-scale crossing `1596` / `1655` | `1596` / `1655` | **match** |
| 4 | cumulative crossing `1661` / `1722` | `1661` / `1722` | **match** |
| 5 | tails `3.863·10¹⁹` / `1.096·10²⁰` | `3.8626·10¹⁹` / `1.0959·10²⁰` | **match** |
| 6 | exact window `3.5035491·10¹⁰` | `35035491004` (both precisions) | **match** |
| 7 | integral window `3.503177115·10¹⁰` | `35031771147` (exact integers, tight both sides) | **match** |
| 8 | loss `0.01062 %` | `0.010617 %` | **match** |
| 9 | 22 convergents in the window | 22, `j = 0..21`; the same 22 under the exact window and under his rounder Lean threshold `34 900 000 000` | **match** |
| 10 | tightest margin **`5.17×` at `j = 21`** | `5.1713×` at `j = 21`, `q = 6586818670`; LHS `949258476701148143940000`, RHS `2079·2⁷¹ = 4908899958942996199636992` — both digit-exact | **match; the index is correct — see §2.2** |
| 11 | exact test `5.443×` | `5.4433×`, also at `j = 21`; the integer form is `≤` the exact test at all 22 | **match** |
| 12 | non-vacuity at the next convergent | `q₂₂` fails the integer criterion and *is* admissible under the exact seam test (`0.2495`) | **match** |
| 13 | `δ = 4.0734·10⁻²²` | `4.073367·10⁻²²` | **match** |
| 14 | first admissible scale `j = 22`, `q = 65470613321`, under both deltas | confirmed under both — see §3 | **match** |
| 15 | exhaustive best approximation to `n < q₁₃ = 190537`, 0 failures | confirmed in fresh code, all 190 536 values of `n` | **match** |
| 16 | ratio to Hercher `2.10×` | `1.375·10¹¹ / 65470613321 = 2.1002` | **match** |

Nothing in the hygiene list has moved since round 10, and nothing failed to
reconcile. The one figure that *looks* like it moved is the window loss: round
10's records carry `0.011 %` and the new script prints `0.01062 %`. These are
the same number (`0.010617 %`) at two roundings; recorded so it is never read
as a change.

### 2.2 Item 4 of the queue — "tightest margin 5.17× at j = 21": the index question

The brief flagged this as exactly where a stale index would hide. It is not
stale. Recomputing the discharge margin at **every one of the 22** convergents
under the pinned `q₀ = q₁ = 1` convention, the tightest is at **`j = 21`**,
`q = 6586818670`, margin `5.1713×` — and the exact test is tightest at the same
`j`, `5.4433×`.

This is consistent with our own round-10 record (`briefs/merle-la8-t1-check-findings.md`
flag 2), which found stack `89d9efc`'s `q₂₁ = 6.587·10⁹` **correctly** labelled
and only stack `0905b00`'s two subscripts off by one. `5.17× at j = 21` belongs
to the correct family. **Flat finding, and a small one: there is nothing to fix
here.**

Where the stale index *did* survive is a different file — see §5.2.

### 2.3 Item 3 of the queue — which `C₀` is which

Our record carries three numbers all called `C₀`. They are three objects, and
two of them are the same construction at two different exponents. Established
before comparing anything, and reproduced here:

| object | construction | exponent | value | reproduced here |
|---|---|---|---|---|
| (i) | **exhibited** fit: `C₀ = max_n (R_best(n) + c·n − p·log₂n)` | `p = 4.125` (`μ−1` with Salikhov's `μ = 5.125`, since withdrawn) | **`−5.774`** | `−5.7737`, with crossings `372` / `440` and tail(>600) `5.0203·10⁻⁴` — the la7 record exactly |
| (ii) | the **same** construction | `p = 13.3` (Rhin 1987 via Simons–de Weger Lemma 12) | **`−14.949` / `−14.954`** | `−14.9487` / `−14.9535` — **this is REQ-043's object** |
| (iii) | **derived**, not fitted: `1 − 2·log₂(ln 2)` | — | **`≈ 2.06`** | `2.057533` |

So: (i) and (ii) are one construction at two exponents — the re-sourcing from
Salikhov to Rhin moves the exponent from `4.125` to `13.3` and the exhibited
constant from `−5.774` to `−14.95`. (iii) is a different construction entirely
(the theorem-form constant behind the `n ≈ 2233` headline). **REQ-043 means
(ii).** No reconciliation of (ii) with (i) or (iii) is possible or wanted: they
are not the same quantity, and `briefs/merle-la7-close-check-findings.md` §2(h)
already pins the definitions so they cannot be conflated. The operational
reading of the exponent (`μ−1 = 4.125`, not `μ = 5.125`) was taken from his
REQ-MATH-035 header, read for definitions only.

---

## 3. Item 5 — the `053` "no result changed" argument, exhibited

### 3.1 The bug he found himself — confirmed from the diff

The committed pre-repair script had `for j in range(6,20)`: the admissibility
loop ran to `j = 19`. The first admissible convergent is `j = 22`. So `first`
stayed `None`, and the *next* line — unconditional — evaluated
`1.375e11/first`, which is the `TypeError` in the committed `OUT_REQ-MATH-053.txt`.
Confirmed against `5c9b663..6c084c5`. (The line immediately above it was
guarded by a conditional expression and would not have raised; the crash is
one line later. Immaterial, recorded because it is the only place the two
readings differ.)

The same commit fixed the second defect: the script still carried
`delta = 1/(3·X·ln2)`, the **pre-REQ-054** constant, missing the factor 2.

### 3.2 Both deltas, reproduced

| | ours | his committed figure |
|---|---|---|
| `δ_new = 2/(3·2⁷¹·ln2)` | `4.073367·10⁻²²` | `4.0734e-22` |
| `δ_old = 1/(3·2⁷¹·ln2)` | `2.036684·10⁻²²` | `2.037e-22` (still printed at HEAD in `OUT_REQ-MATH-052.txt`, correctly, as that block's own figure) |
| ratio | exactly `2` | — |

And the withdrawn window is the `√2` artefact of the same slip:
`√(1/(2δ_old)) = 49547666543 = 4.9548·10¹⁰`, which is `√2 ×` the corrected
`35035491004`. (This re-confirms round 10's finding independently.)

### 3.3 The first admissible scale under each delta

Admissibility is `θ_j ≤ q_j·δ`, decided here as an exact integer comparison
(`θ_j·3·2⁷¹·ln2 ≤ c·q_j`, `c ∈ {1,2}`, with `ln2` as a fixed-point integer at
two precisions).

- under **`δ_new`**: first admissible `j = 22`, `q = 65470613321`
- under **`δ_old`**: first admissible `j = 22`, `q = 65470613321`

**His result claim is confirmed.**

### 3.4 The monotonicity argument — exhibited, not taken

His sentence: *"the old delta was twice too small and hence strictly more
demanding, so it could only push the answer later, never earlier."*

**(i) The direction is valid, and needs no hypothesis.** Write the test as
`P_d(j) := [θ_j ≤ q_j·d]`. For fixed `j` the right-hand side is strictly
increasing in `d`, so `d′ < d ⟹ (P_{d′}(j) ⟹ P_d(j))`. Hence
`{j : P_{d′}} ⊆ {j : P_d}` and therefore `min{j : P_{d′}} ≥ min{j : P_d}`.
Nothing about how `θ_j` or `q_j` behave in `j` is used. Verified as a set
inclusion over every computed `j`.

**(ii) What the direction does not give.** It gives `≥ 22`, not `= 22`. The
equality needs one further fact, which is a *computation* and not an argument:
that `j = 22` is admissible under the **old** delta as well. It is:

> `θ₂₂ / (q₂₂·δ_old) = 0.499018 < 1`

so `q₂₂` clears the old, stricter test — but only by a factor `2.0039`. Had the
factor-2 slip been a factor-3 slip, the answer *would* have moved. So the
equality genuinely had to be checked; the monotonicity sentence alone does not
establish it. **He did check it** (his RED-TEAM run, named as such in the commit
message), and the check is correct. Recorded exactly this way: the reasoning is
sound as a *direction*, the *equality* is a checked computation, and both hold.

**(iii) A stronger fact, not needed, but it makes the sentence general.** The
admissible set is an **up-set** in `j`: the ratio `q_j·δ/θ_j` is strictly
increasing in `j`, because `θ_j ≍ 1/q_{j+1}` and `q_j·q_{j+1}` is strictly
increasing. Both verified (`j = 1..29`). With (iii), "first admissible" is
well defined under any `δ` and moves rightward monotonically as `δ` shrinks —
which is the general form of his sentence, and it is true.

**Verdict on the claim "no result changed; only the reasoning became correct":
CONFIRMED**, with the small precision that the reasoning as stated proves the
inequality and the computation supplies the equality.

### 3.5 Item 5(v) — the citation search, our side

He adds: *"none of the altered `θ_j`/`δ` figures is cited in the ledger or in
our correspondence."* That is a search we can run on our own side and he cannot.

The figures the repair altered are: the printed `delta` (`2.0367e-22` →
`4.0734e-22`), the whole `θ_j/δ` column of the P3 table (every entry halved:
`1.479e19`, `7.241e18`, …, `7.497e11`, `7.171e10`, `3.267e10`, …), the
"`rapport à Hercher : 0.48x`" line, the shifted-index `q₂₀…q₂₅` list, and the
"`PREMIER j admissible : j=21`" line. The `θ_j` values themselves did not
change.

**Searched:** every `briefs/merle-*` record and every tracked `.md`/`.py`/`.txt`
in this repository, plus `LEDGER.md`, `NOTE.md` and `PROTOCOL.md` in the shared
repository at `c966875`.

**Result: CONFIRMED — no altered `θ_j`/`δ` figure is cited anywhere**, in the
shared ledger or in any of our correspondence records. The only hits on those
denominators (`397573379`, `753110839881`, …) are our *own* independently
computed convergent lists in `experiments/merle_lean_r10_audit.py` and
`briefs/merle-la8-t1-check-findings.md`, not citations of his table.

Two adjacent observations, recorded flat because they sit in the same repair
and are not covered by his sentence:

**(a) The `OUT-052` grid evidence is now uncited-by-artifact.** The hygiene pass
also cleaned `OUT_REQ-MATH-052.txt`, and in doing so removed its `(d-bis)`
section — the Ostrowski table with "`mediane eps-petits : 15601 | mediane
controle : 1`" and the expansion `14936 = 22·665 + 306`. The committed
`test_REQ-MATH-052_chaine_T1.py` **does not produce that section** (it ends at
`tous ancres sur la grille ?`), so the section came from an uncommitted script —
the same "two runs stitched together" pattern he identified in OUT-053, in the
other file. Confirmed by running the committed script here: its output is now
byte-identical to the cleaned OUT.

The shared LEDGER's L-A8 seed block (`be8869f`) cites exactly those numbers:
*"the grid half is script-verified: the Ostrowski expansion of every ε-small `n`
uses only large convergent denominators (median lowest denominator 15601,
against 1 for controls; e.g. `14936 = 22·665 + 306` …)"*. **At HEAD that
sentence has no committed artifact behind it.** No figure is disputed and
nothing about the grid half is called into question — the claim may well be
exactly right; the observation is that the artifact which supported it was
removed rather than restored. The clean remedy is the same service the 043 /
055 / 056 pass just performed: commit the script that produced the `(d-bis)`
table.

A related, smaller note in the same file: the *committed* 052 script's own
coarse grid test prints `tous ancres sur la grille ? False` (its `near_grid`
helper only tries single-denominator anchoring, so `14936`, `47468`, `94936`
come back `None`). The deleted `(d-bis)` table, which used the full Ostrowski
expansion, is the stronger test and the one the ledger sentence rests on. No
contradiction in substance; recorded so the `False` is never read as one.

**(b) Our own la8 record quotes the old file's *structure*.** `briefs/merle-la8-t1-check-findings.md`
(operational-observations list) cites OUT-053's "two tables with indexings
differing by one" and its line "`Hercher publie : n > 1.375e11 = q_23
exactement (True)`" as the evidence for the Discrepancy-2 diagnosis. Both are
gone at HEAD — the file is one clean run now. That record pins `5c9b663` and
remains accurate as of its pin; noted only so nobody re-reads it against `c991430`
and concludes we were wrong. Nothing in it needs changing.

---

## 4. Item 6 — the rewritten sweep sentence

**The sentence.** "best approximation verified exhaustively to `q₁₀ = 190537`"
(wrong twice, as round 10 said: the sweep stopped at `n < 31867`, and `190537`
is `q₁₃`) is now **"exhaustive to `n < q₁₃ = 190537`"**, and — this is the part
worth naming — he did not relabel, he *extended the sweep* so the sentence is
true as written. The committed script now runs `for j in range(2,14)`.

**Re-derived here, in fresh code.**

- `q₁₃ = 190537` on the pinned convention: **confirmed** (§2.0).
- The best-approximation property, re-verified exhaustively for **every** `n`
  from 1 to 190 536: for each `j ≤ 12`, `min_{1 ≤ n < q_{j+1}} ‖n·log₂3‖` is
  attained at `n = q_j` and equals `θ_j`. **0 failures.** Fixed-point at 40
  digits, no float in any decision.
- Cross-citation: our round-10 record already verified this property to
  `n < 190537` (`briefs/merle-la8-t1-check-findings.md` §(e)) — so the fact
  stood before his extension; what has changed is that his committed artifact
  now supports his own sentence. Both citations on record, as the brief asked.

**The in-file indexing pin — present, but in one file only.** The pin
(`q_0 = q_1 = 1, tous deux comptes ; c'est celle des OUT-054/056`) appears in
`test_REQ-MATH-053_grille_seam_bound.py` and its output. Searching the whole
Lean repository, that is the **only** place it appears. The pin is consistent
with the convention actually used in 053, 054, 055 and 056 — all four scripts
index from `conv = [1]` built from `a₀`, i.e. `q₀ = q₁ = 1` — so there is no
inconsistency *between* the scripts. See §5.2 for the one file that is
inconsistent with itself.

---

## 5. Item 7 — the accepted corrections: landed, or letter-only?

Reminder from §1: the shared LEDGER has not moved, so anything whose home is
ledger prose is letter-only by construction. What follows is about his Lean
repository, where the artifacts live.

| correction | landed? | where |
|---|---|---|
| the `q₂₃` label / printed-vs-underlying `1.375·10¹¹` | **LANDED** | `test_REQ-MATH-053` + `OUT-053` now print `Hercher (dedie, publie) : n > 1.375e11 = q_23 (seuil sous-jacent)` — "underlying threshold" is our offer (c) wording, adopted |
| Cor. 29's `X₀ ≥ 3·2⁶⁹` named rather than assumed | **NOT LANDED — promised** | no occurrence of `3·2⁶⁹` / `1536·2⁶⁰` / the Cor.-29 condition anywhere in the Lean repository (the only `Cor. 29` mentions are in the old REQ-001/004 headers, without the condition). Recorded as promised-not-yet-landed, without complaint — its natural home is ledger prose, and the ledger has not moved |
| the exact-vs-integral window naming clause | **LANDED, partially** | the new `test_REQ-MATH-055` header states both definitions and the direction of the loss explicitly ("la fenetre entiere est strictement INTERIEURE a l'exacte : perte du bon cote"), and `T1Structure.lean`'s §Legendre-invocation comment says the integral window is "within 0.011 % of the exact window". What no single place says is that the two four-digit roundings `3.5035·10¹⁰` and `3.5032·10¹⁰` *are the same object under two definitions* — which was the substance of the offer |
| the `q₂₁` subscripts | **LANDED in the scripts, NOT in the Lean source** | see §5.2 |
| the multiples tightening, in the discharge script's own conclusion | **LANDED** | `test_REQ-MATH-056` conclusion now reads: "n dans la fenetre => n = q_j (ou un MULTIPLE — cf. Macindoe r10 : si n = t·q_m alors \|K−nL\| = t·θ_m et n·δ = t·q_m·δ, le t se simplifie, donc les memes 22 tests tuent tous les multiples)", with attribution. Verified independently here (`\|m·q_j·L − m·p_j\| = m·θ_j` at three instances) |

### 5.2 One stale index survives, in `T1Structure.lean`

The brief predicted that a surviving `j` label would be where a stale index
hides. It is not in the discharge (§2.2) — it is in the Lean source comments:

- **line 188–189**, the `seam_bound` docstring: *"…yields `n ≥ q₂₁ = 6.547·10¹⁰`
  for `X ≥ 2⁷¹` — one convergent step below Hercher's dedicated
  `q₂₂ = 1.375·10¹¹`."* Both subscripts are off by one under the pinned
  convention: the true labels are `q₂₂ = 65470613321` and `q₂₃ = 137528045312`.
  This is verbatim the text of ledger stack `0905b00`, the block round 10
  flagged.
- **line 433**, the discharge docstring: *"tightest margin 5.17× at
  `q₂₁ = 6586818670`"* — **correct** under the same convention.

So `T1Structure.lean` at `c991430` contains **two different `q₂₁`** 245 lines
apart. The Python artifacts were repaired and the pin added; the Lean source
comments were not swept.

Two smaller stale figures in the same file, same character:

- **line 186**, in the same `seam_bound` docstring: *"Large `X` forces
  `‖n·log₂3‖ ≤ n/(3X·ln2)`"* — that is the **pre-REQ-054 δ**, missing the
  factor 2. The corrected constant is `2/(3X·ln2)`. Everything downstream in
  the file uses the corrected one; this is one comment line.
- **line 14**, the file header: *"Legendre window 4.955e10"* — the withdrawn
  figure. Defensible as a record of what REQ-052 computed at the time, and
  `OUT-052` still prints it too; recorded flat, at the lowest grade, because
  the header presents it as a current machine-verified fact rather than as
  history.

None of this touches a theorem statement, a proof, or any number that enters
the discharge. It is comment hygiene in the one file that did not get the
sweep the scripts got — and it is exactly the class of thing this pass was for,
which is why it is recorded rather than let go.

---

## Half 2 — the four negative measurements

They are offered freely and claim nothing. They are verified in the same
register.

## 6. Item 8 — the cheap reproductions

### 6.1 The four lag-1 autocorrelations, and which statistic they are

Continued fractions built here from scratch at two precisions (2600 and 3000
digits; π from `mpmath` at two precisions), with the number of *stable* partial
quotients asserted before any statistic is computed: 2100 for `log₂3`, 1600
each for π, `log₂5`, `log₂7` — all well above the 1500 used.

| constant | his | ours, on `log a_i` | ours, on raw `a_i` |
|---|---|---|---|
| `log₂3` | `−0.070` | **`−0.0700`** | `−0.0055` |
| π | `−0.063` | **`−0.0631`** | `−0.0012` |
| `log₂5` | `−0.104` | **`−0.1035`** | `−0.0039` |
| `log₂7` | `−0.103` | **`−0.1032`** | `−0.0088` |

**All four reproduce**, to three decimals, **once the statistic is read as the
lag-1 Pearson correlation of `log a_i`.** On the raw partial quotients the same
four series give an order of magnitude less, and essentially noise — because
under Gauss–Kuzmin `a_i` has infinite mean and infinite variance, so a raw
Pearson is dominated by its single largest term (here `max a_i = 20776`, in π).
Taking logs first is the right choice and is evidently what he did. It is worth
**one scope clause** because the letter says "autocorrelation of the partial
quotients", and a reader reproducing it literally will get `−0.006` and think
something is wrong. For completeness: the rank (Spearman) version gives
`−0.086 / −0.083 / −0.127 / −0.114` — same sign, same ordering, same
conclusion, so nothing depends on the choice.

**His retraction is CONFIRMED.** `log₂3`'s `−0.070` sits *inside* the range of
the three control constants (`[−0.1035, −0.0631]`), and is the *second smallest*
in magnitude of the four. Against real continued fractions on a common footing
there is no anomaly to explain. Confirming a correspondent's own self-correction
is exactly what the two-key protocol is for, and it confirms.

### 6.2 Gauss–Kuzmin over 2000 partial quotients, and **the chi-squared question**

The fit itself: over the 2000 stable partial quotients of `log₂3`, the largest
deviation of any bin probability from Gauss–Kuzmin is `|p_obs − p_exp| =
0.008425`, and the statistic is well below its degrees of freedom at every
binning tried (`max χ²/dof = 0.5666` over binnings from 3 to 40 bins). **The
substantive claim — that `log₂3` is statistically ordinary — survives every
reading, unqualified.**

**The number `0.00103` itself does not.** The brief asked us to establish
whether it is a statistic, a p-value, or a normalised distance, and to give the
value under each reading. Answering flatly:

| reading | value over binnings 3…40 bins | verdict |
|---|---|---|
| chi-squared **statistic** | `1.079` … `22.10` | not `0.00103`; a statistic that small over 2000 draws would be a fit far too good to be random, not a good fit |
| **p-value** | `0.9997` … `0.9982` (the fit is excellent, so the p-value is near 1) | `0.00103` as a p-value would mean **rejection** at the 0.1 % level — the opposite of what the letter says |
| **normalised distance** `χ²/N` | `0.000540` … `0.011048` | right order of magnitude; **brackets** `0.00103` |
| KL divergence | `0.000273` … `0.005947` | right order of magnitude |
| squared Hellinger | `0.000137` … `0.003466` | right order of magnitude |

So: **it is a normalised distance, not a statistic and not a p-value.** Which
normalisation and which binning is not recoverable from the letter — the
readings that land in the right decade span a factor of twenty across natural
binnings, i.e. the quantity is binning-dependent at exactly the scale of the
number quoted. The closest single reading found is `χ²/N` at bins
`{1},…,{9},{≥10}`, which gives `0.001214`. **This is a question, not a dispute:
one clause naming the normalisation and the binning would settle it, and
nothing in the conclusion depends on the answer.**

### 6.3 The denominator-ratio range, against φ

| claim | ours | verdict |
|---|---|---|
| ratios run **1.02 to 55.6** | min `1.01799`, max `55.5836` | **match** |
| the max | `q₁₄/q₁₃ = 10590737/190537`, the partial quotient `55` | confirmed |
| the min | `q₁₅/q₁₄ = 10781274/10590737`, a partial quotient `1` | confirmed |
| window-independence | the same min and max for *every* window `j = 1..h` with `h ≥ 16` — so the range does not depend on where he stopped | recorded |
| φ's denominators are the Fibonacci numbers | exact for the first 30 | confirmed |
| φ's ratios are the constant `1.618` | `[1.617978, 1.618056]` beyond `j = 10`; every partial quotient is `1` | confirmed |
| `log₂3` is therefore not of golden type | its ratio range is ~54 wide against φ's ~1e−4 | confirmed |

**His own scoping is correct and worth endorsing rather than merely recording.**
Statistical ordinariness closes arguments that need `log₂3` to be *peculiar*;
it does not touch arguments resting on **effective diophantine input**, because
an effective irrationality exponent is perfectly compatible with a
Gauss–Kuzmin-typical continued fraction. Our own L-A7 chain is the live example:
it consumes Rhin 1987's *effective* exponent `13.3` and would consume it
identically whatever the partial quotients looked like. He says exactly this,
and it is right.

## 7. Item 9 — the neighbours: the structural claim, verified; the empirics, his

### 7.1 The structural claim, derived in our own coordinates

Let `a` be **odd** and let `T_a(x) = (a·x + 1)/2^v` be the odd-to-odd map,
`v = v₂(a·x+1) ≥ 1` (`a·x+1` is even because both `a` and `x` are odd). One
step, in `log₂`:

> `log₂ T_a(x) − log₂ x = log₂(a + 1/x) − v`.

**The averaging convention, stated precisely — this is where such claims
usually fail.** Two things are averaged and they are averaged differently:

1. the `1/x` term is **dropped**; it is `O(1/x)`, its total along an orbit is
   dominated by a convergent series once the orbit is above any fixed bound, and
   it can therefore change no drift *sign*;
2. `v` is averaged under the standard 2-adic model `P(v = k) = 2^{−k}` on
   `k ≥ 1`, whose mean is `Σ k·2^{−k} = 2` **exactly**.

Both are **per-step arithmetic means over odd steps** — not time averages along
a single orbit, and not size-weighted. That is the convention under which the
statement is true, and it is the convention in which the program's own drift
statements (aeh.md §13; `README`'s "1/3 rate, drift — almost-everywhere
statements only") are phrased.

Then the per-step drift is `D_a = log₂ a − 2`, and

> `D_a < 0 ⟺ log₂ a < 2 ⟺ a < 4`.

Among odd `a` in `3..31`, exactly one has negative drift, and it is `a = 3`
(`−0.415037`; `a = 5` gives `+0.321928`, `a = 7` gives `+0.807355`). The
equivalence `log₂a < 2 ⟺ a < 4` is exact for every integer `a`.

**Verdict: the structural claim is CORRECT, and it is exact arithmetic rather
than a measurement** — it is structural exactly as he says. It is also standard
(it is the textbook `5x+1`-divergence heuristic), and his own REQ-MATH-050 says
so in as many words; nothing here is claimed as new by anyone.

One boundary worth stating, because the sentence sits next to a table of cycle
counts: a negative drift is a statement about the *average step*, and cycle
existence is not a drift question. The structural claim explains why `a = 3` is
the interesting `a`; it does not bear on how many cycles any `a` has.

### 7.2 His empirics — recorded as his, unreplicated

Recorded here without replication, with his own caveat carried as he states it:

- correlation between cycle count and approximation quality of `log₂ a`:
  **`+0.22`** (Markov constant), **`−0.29`** (largest partial quotient) —
  nothing; **drift gives `−0.57`**;
- worst-protected neighbour `a = 17` (partial quotient 215) has **no** cycles;
  best-protected in range `a = 21` has **none either**;
- his caveat, verbatim in substance: for large `a` the orbits leave his search
  window, so those zeros mean **"not found here"**, and the drift statement does
  not depend on the search.

### 7.3 The stopping rule, biting — recorded

Replicating the three correlations would require recomputing cycle counts for
`ax+1` over odd `a = 3..31`, i.e. **a cycle search over other `a`**. The brief
and `README`'s binding stopping rules forbid it, and the main session's launch
instructions named this item specifically. **The want is recorded and the search
is not run.** What that costs is stated plainly: `+0.22`, `−0.29` and `−0.57`
stand entirely on his side of the two-key protocol and should be described that
way anywhere they are used. What it does not cost is anything structural — the
only non-empirical statement in item 3 is verified above, exactly, and it needs
no search at all.

## 8. Item 10 — the drift from the inside

This is the substantive one and the effort went here.

### 8.1 `D(x)` and its asymptotic — confirmed, with the next term

`D(x) := log₂(3 + 1/x) − log₂(3 − 1/x) = log₂((3x+1)/(3x−1))` — the two forms
are identical (verified at five values, to 50 digits).

Writing `u = 1/(3x)`, `D(x) = (2/ln2)·artanh(u)`, whose series has **all
positive** higher terms, so:

> `D(x) = 2/(3x·ln2) · (1 + 1/(27x²) + O(x⁻⁴))`, and `D(x) > 2/(3x·ln2)` strictly.

Confirmed numerically at 160 digits: at `x = 2⁷¹` the relative excess of `D`
over its asymptote is `6.64319·10⁻⁴⁵`, and `1/(27x²) = 6.64319·10⁻⁴⁵` — agreeing
to every printed digit. So his asymptotic `2/(3x·ln2)` is right, and the
direction of the approximation is now pinned (`D` is *above* it, by a relative
`1/(27x²)`).

### 8.2 "Summed around a cycle that is exactly `n·δ`" — adjudicated

**What is exact.** Split `D` into its two halves,
`D⁺(x) := log₂(1 + 1/(3x))` (north) and `D⁻(x) := log₂(1 − 1/(3x))` (south), so
`D = D⁺ − D⁻`. Then, for a cycle:

> **Identity.** For a positive cycle of `n` odd elements with `K = Σ v_i`,
> `Σ_i log₂(1 + 1/(3x_i)) = K − n·log₂3` **exactly**;
> for a negative cycle (elements `y_i = |x_i|`),
> `Σ_i log₂(1 − 1/(3y_i)) = K − n·log₂3` **exactly**.

*Derivation, three lines, ours.* Each step is `3x_i + 1 = 2^{v_i}·x_{i+1}`, so
`3 + 1/x_i = 2^{v_i}·x_{i+1}/x_i`. Multiplying around the cycle the `x`'s
telescope and `Σ v_i = K`, giving `∏(3 + 1/x_i) = 2^K`, i.e.
`Σ log₂(3 + 1/x_i) = K`. Subtract `n·log₂3`. The south shore is the same
computation with `3y_i − 1 = 2^{v_i} y_{i+1}`. ∎

Verified on **all four real cycles, both shores** (`+1`, `−1`, `−5`, `−17`),
agreeing with `K − n·log₂3` to 45 digits in every case.

**This identity *is* the seam identity, written per step.** Its right-hand side
is `log₂(2^K/3^n)` — precisely the quantity T1's chain bounds (la8 §(c):
`0 < K·ln2 − n·ln3 = ln(1 + q/3^n)`). So the "third face" claim is **correct**,
and in fact stronger than he states it: the per-step drift does not merely
*bound* the seam gap, it **sums to it exactly**.

**What is not exact.** The sum of the *full* `D` around a cycle is not `n·δ`.
`D` is strictly decreasing, so for a cycle with all elements `≥ X`:

> `Σ_i D(x_i) ≤ n·D(X) = n·δ·(1 + 1/(27X²))`,  `δ := 2/(3X·ln2)`,

with **equality if and only if every `x_i` equals `X`** — which no cycle
achieves (exhibited: on the `−17` cycle `Σ D = 0.18834` against
`n·D(x_min) = 0.39608`). So the statement is a **sharp upper bound whose
equality case is the extremal one**, not an identity. At `X = 2⁷¹` the two sides
agree to 44 decimal places, which is presumably why it reads as exact.

**But the constant identification is exact enough to be structural, and it is
the real content.** `δ`, the constant that makes T1's window finite, satisfies

> `D(x_min) / δ = 1 + 6.64·10⁻⁴⁵` at `x_min = 2⁷¹`

— i.e. **`δ` is the per-step north–south drift evaluated at the minimum
element**, to a relative `1/(27x_min²)`. And the factor 2 in `δ` is *exactly*
the two-shore doubling: `log₂(1+u) − log₂(1−u) = 2u/ln2 + O(u³)`.

That last point deserves one flat sentence, because it is a reframing rather
than a confirmation. In the la8 derivation the factor 2 in `δ` arrives from a
**crude step** — the two-bound `(m+1)^n < 2m^n` used to control the difference
of powers. In the drift reading it arrives from a **symmetry** — north and
south contributing one unit each. Two different mechanisms landing on the same
`2`. The drift reading is the one that explains the constant as structure
rather than as slack, and that is a genuine gain in understanding even though
no number moves.

### 8.3 `x* = 7/3` — exact, unique, and what the two objects are

- `(3x+1)/(3x−1)` at `x = 7/3` is `8/6 = 4/3` in exact rationals; his form
  `(3 + 3/7)/(3 − 3/7) = 24/18 = 4/3` likewise. **Confirmed.**
- `log₂(4/3) = 2 − log₂3` **identically** (`log₂4 − log₂3`). Confirmed to 50
  digits — but note that this identity is a *tautology*; it carries the claim,
  it is not the claim.
- **Uniqueness, and it is exact:** `D(x) = log₂(4/3) ⟺ 3(3x+1) = 4(3x−1) ⟺
  9x + 3 = 12x − 4 ⟺ 3x = 7 ⟺ x = 7/3`. One linear equation, one root. `D` is
  strictly decreasing, so `D(x) > 2 − log₂3` below `7/3` and
  `D(x) < 2 − log₂3` above.
- At `x = 2⁷¹`: `D(x)/(2 − log₂3) = 9.81446·10⁻²²`. **His `9.8·10⁻²²`
  confirmed.**

**What "the sign information" is, as a quantity.** The two objects being
compared are `D(x)` — the per-step cost of the `±` choice, which is what the
sign of the `1` in `3x ± 1` is worth — and the constant `2 − log₂3 =
0.4150374992788…`, which is "the drift" in exactly the sense item 3 uses (item
3's drift is `log₂a − 2`; at `a = 3` its magnitude is `2 − log₂3`). The
brief's candidate — our `|q| ≥ 1` seam input — is **not** the right
identification in general, and saying so is the point of the check. The
constant has three exact descriptions, all of the same number:

- (a) the mean per-odd-step contraction of the Collatz map, `2 − E[v] + …`,
  i.e. minus item 3's drift at `a = 3`;
- (b) `D⁺(1) = log₂(1 + 1/3)`, the **north** per-step drift at `x = 1`;
- (c) `K − n·log₂3` for the trivial cycle (`n = 1`, `K = 2`) — i.e. the
  log-seam gap of the `|q| = 1` instance **at `n = 1` and only there**. In
  general the seam input is `log₂(2^K/3^n) ≥ log₂(1 + 1/3^n)`, which is not a
  constant.

All three verified equal, exactly. So "the sign information equals the drift at
`x* = 7/3`" **is** a statement about two well-defined objects and not a
coincidence of two expressions — with the qualification that the identity
quoted to justify it is trivial, and the content is the root.

**One corollary, ours, which sharpens it into something with integer teeth:**

> Since `D` is strictly decreasing and `7/3` lies strictly between the odd
> integers `1` and `3`, **`x = 1` is the only odd positive integer at which the
> sign information exceeds the drift** (`D(1) = 1` exactly, against
> `2 − log₂3 = 0.415`; `D(3) = log₂(5/4) = 0.322` is already below it, and it
> falls from there).

Verified for every odd `x ≤ 199` and true by monotonicity beyond. That is the
form in which his observation says something: *the `±1` matters more than the
drift at exactly one odd integer, and that integer is the trivial cycle.*
Everywhere else — "the terrain is grey", in his words — and at `2⁷¹` the sign
is worth `10⁻²¹` of the drift.

### 8.4 Verdict — theorem or measurement

Of the four negatives:

**Items 1, 2 and 3 are empirical records to be logged as his.** Item 1 (the
golden ratio) and item 2 (the rhythm of the peaks) reproduce here, with two
scope clauses (§6.1, §6.2) and no dispute; item 3's *empirics* are unreplicated
by the stopping rule (§7.3). Item 3 does contain one exact statement — the
drift dichotomy `log₂a < 2 ⟺ a < 4` — but it is standard and he says so, so it
is a confirmation, not a hand-back.

**Item 4 contains an exact statement worth restating as a theorem — but it is
not the one he names.** The precedent is the two upgrades we already handed
back (`ε + ε′ = 1`, and `γ·log₂3 = c_gen` with its symbolic derivation), where
his numerics undersold what he had. The same thing has happened again:

> **Hand back as a theorem.** For a cycle of the odd map with `n` odd elements
> and `K = Σ v₂(3x_i ± 1)`, the summed per-step drift equals the log-seam gap
> **exactly**, on both shores:
> `Σ_i log₂(1 + 1/(3x_i)) = K − n·log₂3` (north) and
> `Σ_i log₂(1 − 1/(3y_i)) = K − n·log₂3` (south).
> **Corollary.** With `X = x_min`, `Σ_i D(x_i) ≤ n·D(X)` with equality only in
> the extremal case, and `D(X) = δ·(1 + 1/(27X²))` where `δ = 2/(3X·ln2)` is
> T1's constant. The factor 2 in `δ` is the two-shore symmetry.

That is the "third face of the same wall" made exact, and it is a **structural
statement for the joint note, not a measurement** — the drift is not a new
object, it is the seam identity read one step at a time, and now with an
identity rather than an approximation.

**Two things in item 4 are correct but should not be restated as theorems.**
"Summed around a cycle that is exactly `n·δ`" is a sharp bound with an extremal
equality case, not an identity (§8.2) — handing it back as an identity would be
handing back something false at the 45th decimal, and the honest restatement is
the one above. And `x* = 7/3` is exact and unique, but the identity carrying it
is a tautology; what is worth a sentence is the **corollary** in §8.3 — `x = 1`
is the only odd integer where the sign outweighs the drift — which is his
observation with integer teeth, and which he can have.

---

## 9. Flags, collected

1. **`j = 21` is correct** — the surviving index label in the discharge is not
   stale. Recomputed at all 22 convergents (§2.2).
2. **The `053` no-result-changed claim holds**, with the precision that the
   monotonicity sentence proves `≥ 22` and a separate computation supplies
   `= 22`, at a margin of `2.0039×` (§3.4).
3. **The citation claim (v) is confirmed** on our side (§3.5). Two adjacent
   items recorded flat: the deleted `OUT-052` `(d-bis)` section whose figures
   the ledger's L-A8 seed block cites; and our own la8 record's citation of the
   old `OUT-053` structure, accurate as of its pin.
4. **`T1Structure.lean` carries two different `q₂₁`** at `c991430` (lines 188
   and 433), plus the pre-054 `δ` in the `seam_bound` docstring and the
   withdrawn `4.955e10` in the file header (§5.2).
5. **Cor. 29's `X₀ ≥ 3·2⁶⁹` is promised, not landed** — absent from the entire
   Lean repository; its natural home is ledger prose, and the shared ledger has
   not moved (§5).
6. **The autocorrelation statistic is on `log a_i`**, not the raw partial
   quotients; the letter's phrasing is one clause away from reproducible
   (§6.1).
7. **`0.00103` is a normalised distance**, not a statistic and not a p-value;
   which normalisation and which binning is not recoverable, and the natural
   readings span a factor of twenty around it (§6.2).
8. Item 3's empirics are **his and unreplicated**; the stopping rule was
   applied and the want recorded (§7.3).
9. No pushes, no forks, issues, stars, watches or comments; clones read-only in
   the scratchpad; no key turned, no ledger text, no reply paragraph. Cycles
   front PARKED throughout.

## 10. Recommendation (recommendation only — no key is turned here)

**What belongs in the reply.**

1. That the hygiene pass is verified, at the strongest grade available: the
   three generator scripts exist, and all five relevant scripts were **run**
   here and reproduce their committed outputs byte-identically. Every number
   independently recomputed, 115 checks, 0 failures.
2. That `5.17× at j = 21` is **correct** — worth saying explicitly, because he
   had just changed conventions and the natural worry is that a label went
   stale; it did not.
3. The `053` argument accepted, with the one precision stated as a compliment
   to his own red team rather than a correction: the monotonicity gives `≥`,
   the equality is a computation, the margin was `2.0039×`, and he ran it.
4. Three flat artifact notes, in descending order of size: (a) `T1Structure.lean`'s
   two surviving `q₂₁`/`q₂₂` subscripts and the pre-054 `δ` in the same
   docstring — the sweep reached the Python and not the Lean comments; (b) the
   deleted `OUT-052` `(d-bis)` section whose median-15601 figures the ledger
   cites, with the offer that he commit the script that produced it, exactly as
   he did for 043/055/056; (c) Cor. 29's condition recorded as promised.
5. The four negatives reproduced, with the two scope clauses (`log a_i`; the
   chi-squared reading) put as questions, and his own retraction confirmed on a
   common footing.
6. **The theorem hand-back** of §8.4 — the per-step drift identity on both
   shores, with `δ = D(x_min)(1 + 1/(27x_min²))` and the factor 2 named as the
   two-shore symmetry — offered as the third-face claim made exact, with the
   flat note that "exactly `n·δ`" is a sharp bound rather than an identity, and
   the `x = 1` corollary handed back as his.

**What belongs in a ledger entry: nothing yet.** The shared ledger has not
moved since our own round-10 push, and the entire hygiene pass is artifact-side
— it repairs the evidence under claims already recorded, and changes no claim.
If anything eventually belongs in L-A8, it is one clause of the §8.4 theorem as
the third face; that is a co-edit decision, gated on the author's go-ahead, and
it is not drafted here.

**Owed next:** main-session review (re-run `experiments/merle_r11_hygiene_check.py`)
and merge. Nothing else is owed by this session.
