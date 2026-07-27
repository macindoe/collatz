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
