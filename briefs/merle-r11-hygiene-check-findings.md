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
