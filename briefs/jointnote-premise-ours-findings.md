# Joint-note premise pre-check, half A — what is actually ours, and actually published

**Branch** `jointnote-premise-ours`. **Base SHA `d945556`** (the worktree was cut at
the stale `2225b68`, which does not contain this brief; rebased onto `d945556`
before any work).

**Scope.** A records audit of our own published and wiki material, run against
Merle's proposed one-sentence statement of the joint note's contribution. Facts
only. No sentence is drafted here, no wording is proposed, no opinion is offered
on whether the note should be written — the sentence is the author's, and Merle
asked him directly.

**Stopping rules.** No new computational front; no new mathematics; cycles front
stays PARKED (`cycles.md` 12.8.5). Nothing below reopens it.

**Nothing needed computing.** Every question in the queue is answered by reading
the record — the phrase search, the statement comparison, the PDF check, the
dates, the status words. No verification script was written, because inventing
one would have verified nothing. The only tooling used was a throwaway text
extractor over the two frozen PDFs, run from the scratchpad and not committed.

The sentence under audit, verbatim:

> Taking Macindoe's counting dichotomy as given, the note locates the obstruction
> that dichotomy identifies, exhibits it from three independent directions, and
> contributes a machine-checked fragment of the cycle literature.

And his stated reason for that shape, verbatim:

> I have written it that way deliberately. The dichotomy is already yours and
> already published; the note should present it, not appear to prove it for the
> first time. What would be new is the located obstruction, jointly, and the
> formalisation, mine. If we cannot write a sentence of that shape honestly, we
> should not write the note.

---

## Verdict table

| # | Premise, as he states it | What our record says | Verdict |
|---|---|---|---|
| 1 | the phrase **"counting dichotomy"** | Not in our record in that form. Our published abstract has **"a sharp dichotomy for counting arguments"** and our published Related-work paragraph has **"the counting-limit dichotomy developed here"**. The two-word compression is his. | **Supported with qualification** — the phrase is a faithful contraction of our own published words, but it is his contraction, not a term of ours |
| 2 | it names a **dichotomy** | The two halves are our published Theorem 4.5 (uniform trim) and Theorem 4.6 (sharpness: the staircase). "Dichotomy" is our own published word for exactly this pair. The *fit* is loose in two named places (§2.3 below). | **Supported with qualification** |
| 3 | it is **already published** | Both halves are in paper 1 v1, DOI 10.5281/zenodo.21273548, §4, as Theorems 4.5 and 4.6, and unchanged in v2, DOI 10.5281/zenodo.21421120. Verified in the frozen PDFs, not from `publication.md`. | **Supported** |
| 4 | it is **already yours** | 12.8 was written 2026-07-08 (`b5f367d`), drafted into the paper 2026-07-09, published July 2026. The Merle correspondence begins 2026-07-16. Nothing in 12.8.1–12.8.5 rests on it. One thing does not carry over cleanly: 12.8.6/the v2 note. And our own published paper already names a kindred impossibility lemma of his. | **Supported** for the published pair; **qualified** for the v2 evidence note (§4) |
| 5 | "**locates the obstruction** that dichotomy identifies" | Our record's answer to *what the obstruction is* is split across four status grades, one of which is an explicitly labelled **organizing heuristic, not a formalized theorem**. | **Not supported as a single object** — see §5.1; the strength varies by which item is meant |
| 6 | "**three independent directions**" | Our record does not carry a "three directions" object at all under that name. Three different triples exist, none of them the note's. *Independent* survives the hygiene finding only because the drift was never one of the three. | **Not supported from our record** — the three faces are the shared repo's structure, not ours; see §5.2 |
| 7 | "a machine-checked fragment of the cycle literature", **his** | Outside this session's scope (sibling brief). What our record carries is recorded flat in §5.3. | Not adjudicated here |

---

## 1. Does "counting dichotomy" name anything in our record?

**Exact phrase `counting dichotomy`: three hits in the repository, all of them
ours quoting him.**

- `HANDOFF.md` line 63 — the window-D description, which itself quotes his letter
  ("whether *Macindoe's counting dichotomy* names an already-published result of
  ours").
- `briefs/jointnote-premise-ours-brief.md` lines 9, 21, 23, 32 — this brief.
- `briefs/jointnote-premise-external-brief.md` line 40 — the sibling brief.

There is **no hit anywhere in the wiki pages, in `paper/`, in `sources/`, or in
either published PDF.** The phrase, in those two words, is his.

**But the words are ours, one clause apart.** The near variants are the load-bearing
finding here, and they are in the *published abstract*:

- **Paper 1 v1** (DOI 10.5281/zenodo.21273548), abstract, verbatim from the frozen
  PDF `sources/paper/collatz-reduced-v1.pdf`:

  > Our main new theorem is **a sharp dichotomy for counting arguments**: a trim
  > uniform in the number of blocks `p` exists, giving effective finiteness at
  > every period, but its constant necessarily degrades like `(log₂3)^(−p)` — an
  > explicit family of near-counterexamples (*staircases*: geometric climbs closed
  > by a single crash, precisely divergent-orbit profiles bent into loops) shows
  > counting arguments cannot do substantially better, so uniform cycle exclusion
  > requires arithmetic (divisibility) input, not sharper counting.

- **Same paper**, Related work and provenance, verbatim:

  > neither contains the anchor machinery, exact per-step laws, or **the
  > counting-limit dichotomy** developed here.

- **Same paper**, title: *Reduced coordinates for the Collatz map: exact per-step
  laws, anchor dynamics, and **the limits of counting arguments for cycles***.

- **Paper 1 v2** (DOI 10.5281/zenodo.21421120): both sentences byte-for-byte the
  same, verified in `paper/collatz-reduced-v2.pdf`. v2's own Version note says
  "No theorem or universal claim is strengthened."

- `publication.md` (wiki, not published) uses "dichotomy" for the same object
  twice: *"its sharpness dichotomy (uniform trim capped at `1.585^(-p)`, staircase
  witness)"* (current-state paragraph) and *"feature the uniform-trim/staircase
  dichotomy as the main new theorem"* (framing recommendation).

**Where "dichotomy" does *not* appear: `cycles.md`.** The page that carries the
mathematics uses the word zero times. Every other `dichotomy` in the repository
names a different object and must not be confused with this one:

| Location | Object | Not this |
|---|---|---|
| `ladder.md` Theorem 15.1.1, `reverse.md` Theorem 14.10.1 | "ladder dichotomy" — one Collatz step off-spike vs an affine kick at spikes | different theorem |
| `reverse.md` §14.9, `paper/collatz-mirror-v1.tex` `thm:dich` | "the one-step dichotomy (not a trichotomy)" — the 3-adic reverse window | different theorem, different paper |
| `itinerary.md` (front matter, 14.15.9) | the `q`-dichotomy / capped-vs-escaping | different theorem |
| `stage1.md` 11.8.1.7.4, `archive/appendix-a.md`, drafts v068–v078 | the *refuted* regular/irregular tower dichotomy, explicitly **dissolved** | a dead claim |
| `bridge.md` line 50 | "the forward trichotomy collapsing to a reverse dichotomy" | mirror asymmetry note |

**Plain statement.** "Counting dichotomy" is **his coinage**, and it is a faithful
two-word contraction of our own published phrases "a sharp dichotomy for counting
arguments" and "the counting-limit dichotomy". The mathematics it points at is
ours; the label in that exact form is not a term this project has ever used.

---

## 2. Which result is it pointing at, and does "dichotomy" fit?

### 2.1 The two halves, as the wiki carries them

`cycles.md` §12.8, front matter status line: *"uniform trim RESOLVED (12.8);
all-p sharpness ASSESSED not proved, floor grade (12.8.6); front PARKED per
stopping rules."*

**Half A — counting reaches every period.**

- **Theorem 12.8.1 (uniform trim, all `p`)** — status word: **Theorem**, with a
  proof in place. Every nontrivial period-`p` cycle of `F` satisfies
  `γ + log₂p > 0.585·n/(1.585^p − 1)`, where `γ = K − log₂q`.
- **Corollary 12.8.2 (uniform effective finiteness)** — status word: **Corollary**.
  Combined with Rhin's effective bound (pinned at 12.5.3), `n ≤ n₀(p)` explicitly
  for every period. Its closing sentence: *"Cycle exclusion at every single period
  is therefore a finite, explicitly bounded computation — uniformly in `p`."*

**Half B — counting cannot reach them uniformly.**

- **Remark 12.8.3 (sharpness: the staircase family)** — status word in the wiki:
  **Remark**. The exhibited instance at `p = 7`, `n = 94`, `γ = 6.74` against the
  period-3 constant's demand of `8.9`; `84` further size-passers at `p = 6`. All
  fail the divisibility conditions `q | R_r` — none is a cycle.
- **§12.8.6, achieved grade: floor.** A per-period recipe plus a bounded correction
  algorithm produce a size-passer at every `p ∈ {2,…,23}` with
  `γ/log₂p ∈ [1.828, 3.643]`. Its own closing words: *"the all-`p` sharpness claim
  in `thm:staircase` is calibrated further … but **not proved**; the sole remaining
  gap in this floor-grade result is the Diophantine coverage bound of `12.8.6.1`."*

**Remark 12.8.4** states what the pair means: the staircase is a divergent-orbit
profile bent into a loop, so *"the two halves of the conjecture's residual
difficulty (statistics for orbits, rigidity for cycles) meet in this one
configuration, which is strong evidence they are the same problem."*
**Consequence 12.8.5** is the stopping rule firing: crossover plan withdrawn,
cycle front parked, residual content of cycle exclusion identified as anchor-walk
rigidity.

### 2.2 Does "dichotomy" fit?

**Yes, and it is our own word for it.** The published abstract calls exactly this
pair "a sharp dichotomy for counting arguments" and the Related-work paragraph
calls it "the counting-limit dichotomy". A referee reading the paper meets the
word before he meets the theorems.

The clean statement of the pair, in our own published words (abstract): *a trim
uniform in `p` exists, giving effective finiteness at every period, but its
constant necessarily degrades like `(log₂3)^(−p)` … so uniform cycle exclusion
requires arithmetic (divisibility) input, not sharper counting.*

### 2.3 Where the fit is loose — two places, both nameable

**(a) "Counting closes every period" overstates 12.8.2.** What is proved is
*effective finiteness*: the candidate set at each period is finite and explicitly
bounded, `n ≤ n₀(p) = O(p·(log₂3)^p)`. That is not the same as the period being
closed. Closing a period requires *running* the finite computation, and the wiki
records that it has not been run past `p = 3` and will not be: `n₀(92) ~ 10^18`
(12.8.5, README), and the stopping rules forbid further per-period searches. Our
own published wording is careful about this and says **"giving effective finiteness
at every period"**, never "closes". The periods actually closed in our record are
`p = 1, 2, 3` (12.2.3, 12.5.3, 12.7.5), and our published Theorem 4.4 states those
are *rederivations* of Steiner / Simons–de Weger / Hercher: *"These statements are
contained in the classical results; the derivations, not the theorems, are the
contribution."*

**(b) "Provably cannot close them uniformly" is exactly half proved.** The published
Theorem 4.6 has two sentences with different strengths, and the paper marks the
seam itself:

- *Proved, by exhibited witness*: **"No trim uniform in `p` can extend the
  small-period constants: there exist configurations satisfying every rotation's
  exact size condition `q ≤ R_r` whose `γ` falls far below any polynomial-in-`p`
  extension of the constants of periods 2–3."** The `p = 7` staircase is the
  witness; this half is a theorem and needs nothing further.
- *Assessed, not proved*: **"we assess (supported by the verified instances, though
  not proved here for all `p`) that it passes all size conditions with
  `γ = O(log p)` for every `p`."** This hedge is present verbatim in the v1 PDF and
  **unchanged in the v2 PDF**; `publication.md` records that "The hedge sentence is
  not upgradable; better evidence, not a closure, is what v2 added."

So the honest form of half B is: *counting provably cannot be extended by the
small-period constants* (theorem), and *the exponential weakness is assessed to be
intrinsic at every period, on floor-grade evidence over `p ∈ {2,…,23}`* (assessed,
not proved). The word "provably" attaches to the first and not to the second.

**(c) A third, smaller looseness.** The wiki calls half B a **Remark** (12.8.3);
the published paper calls it a **Theorem** (4.6). This is a wiki-vs-published
*status-word* difference in the direction that favours the published form. Recorded,
not corrected — `sources/` is immutable and the published PDF is frozen.

---

## 3. "Already published" — verified against the frozen artifacts

Checked by extracting text from the committed PDFs, not from `publication.md`.

### 3.1 Which artifact carries which half

| Half | Published artifact | Printed as |
|---|---|---|
| A: uniform trim + effective finiteness | **paper 1 v1**, DOI 10.5281/zenodo.21273548, `sources/paper/collatz-reduced-v1.pdf` §4 | **Theorem 4.5 (uniform trim)** |
| B: sharpness / counting can do no better | **paper 1 v1**, same, §4 | **Theorem 4.6 (sharpness: the staircase)** |
| The pair, named as a dichotomy | **paper 1 v1**, abstract and Related work | "a sharp dichotomy for counting arguments"; "the counting-limit dichotomy" |
| Both halves again, unchanged | **paper 1 v2**, DOI 10.5281/zenodo.21421120, `paper/collatz-reduced-v2.pdf` | same numbers, Theorem 4.5 / Theorem 4.6 |
| The contiguous `p ∈ {2,…,23}` evidence | **paper 1 v2 only**, "Note added in v2 (July 2026)" | `γ/log₂p ∈ [1.828, 3.643]` |

The **mirror paper** (DOI 10.5281/zenodo.21303918, `paper/collatz-mirror-v1.pdf`)
carries **no part of this result**. Its only "dichotomy" is `thm:dich`, the 3-adic
one-step predecessor window — a different theorem about a different object. If a
sentence cites the mirror paper for the counting dichotomy it is wrong.

### 3.2 Published vs wiki — the gap, stated in both directions

**No load-bearing half is wiki-only.** Both halves of the dichotomy are in the
frozen v1 PDF, at full strength, with the same hypotheses and the same scope as the
wiki's current 12.8.1 and 12.8.3. Four differences exist and none of them moves a
half out of the published record:

1. **Status word.** Wiki: *Remark* 12.8.3. Published: *Theorem* 4.6. The published
   form is the stronger label; the mathematical content and the hedge are identical.
2. **§12.8.6 is in the wiki at greater length than in print.** The wiki carries
   Lemma 12.8.6.1 (with its open Diophantine coverage bound), Construction 12.8.6.2,
   Algorithm 12.8.6.3, Proposition 12.8.6.4 and the two `p = 22` rows. The published
   v2 note compresses all of it to one paragraph. Everything *claimed* in the wiki
   version is claimed in print; the machinery is not.
3. **The hedge is identical in both.** v1 PDF and v2 PDF both read "though not
   proved here for all `p`". Wiki front matter says "ASSESSED not proved, floor
   grade". No drift.
4. **Corollary 12.8.2's numeric table** (`n₀(p)` for `p = 4…100`) is wiki-only. The
   published Theorem 4.5 states only the shape `n₀(p) = O(p (log₂3)^p)`. A
   referee-facing sentence should not cite a specific `n₀` value as published.

One cross-page inconsistency inside our own record, recorded and not corrected:
README's strategy paragraph says the crossover search bound at `p = 92` is
`n ~ 10^18`, and `cycles.md` 12.8.5 says the same; `cycles.md` 12.8.2's own
verification table gives `n₀(92) ~ 4.78·10^21`. Both are ours, both are wiki, and
neither is in the published paper. Flagged because a referee-facing sentence must
not reach for either number.

---

## 4. "Already yours" — the attribution as our own record states it

**The published pair is unambiguously ours as of its publication date.** Dates from
our own git log and front matter:

| Date | Event | Commit / artifact |
|---|---|---|
| 2026-07-08 | §12.8 written: 12.8.1 uniform trim, 12.8.2 effective finiteness, 12.8.3 staircase sharpness, 12.8.4, 12.8.5 | `b5f367d` |
| 2026-07-09 | First complete paper draft | `6d121e7` |
| 2026-07-09 | Merle's *published Zenodo preprint* read as prior-art due diligence and cited | `f2f084e` |
| July 2026 | **Paper 1 v1 published**, DOI 10.5281/zenodo.21273548 | `sources/paper/collatz-reduced-v1.pdf` |
| 2026-07-16 | **The Merle correspondence begins** | `0129680`, `2c54669` (12.8.6) |
| July 2026 | Paper 1 v2 published, DOI 10.5281/zenodo.21421120 | `paper/collatz-reduced-v2.pdf` |

Nothing in 12.8.1–12.8.5 rests on Merle's contributions, on the correspondence
rounds, or on jointly verified material. The correspondence starts **eight days
after** 12.8 was written and **after** v1 was drafted.

**Two things that do not carry over cleanly, both recorded by our own pages:**

**(a) §12.8.6 / the v2 note is partly his, and our published paper says so.**
`cycles.md` 12.8.6 opens: *"The attempt packages an external suggestion (Eric
Merle, correspondence 2026-07-16)."* The two `p = 22` closing candidates
(`n = 25217`, `n = 31202`) are credited to his "Diophantine pincer" hypothesis
(12.8.6.4, the "two `p = 22` rows"). The published v2 note says the same in print:
*"correspondence with Eric Merle identified the cause as a gap in that chain's
coverage at the required scale."* So the **strengthened sharpness evidence** —
the contiguous `p ∈ {2,…,23}` range — is **not** wholly ours. The **dichotomy
itself** is, because v1 carries both halves at full strength without it.

**(b) Our own published paper already names a kindred lemma of his.** Related work,
v1 and v2, verbatim: *"a Lean 4 formalization [11] proves cycle exclusion
conditionally on Baker-type and verification hypotheses, **including an
impossibility lemma for measure-based uniform bounds kindred to our Theorem 4.6**;
neither contains the anchor machinery, exact per-step laws, or the counting-limit
dichotomy developed here."* Citation `[11]` = E. Merle, *On the non-existence of
non-trivial Collatz cycles: a conditional formal proof in Lean 4*, Zenodo DOI
10.5281/zenodo.19790406 (2026). `publication.md` records the same reading: "δ8
lemma kindred to our staircase theorem; cited in paper" (`f2f084e`, 2026-07-09).

This is not a priority contest and nothing here adjudicates one. It is recorded
because a sentence saying "already yours" about Theorem 4.6 will be read by a
referee who can also read our own Related-work paragraph, and that paragraph
already concedes a kindred antecedent on his side while claiming the *dichotomy*
— the pairing of trim with sharpness — as ours. The distinction our published text
draws is between his impossibility lemma and our dichotomy; it does not claim the
impossibility direction as ours alone.

---

## 5. The sentence's other two clauses, against our record only

The external half of this — `ccchallenge.org`, Hercher's numbers, the shared
repo's `NOTE.md` — is the sibling session's (`briefs/jointnote-premise-external-brief.md`)
and is not duplicated here.

### 5.1 "locates the obstruction that dichotomy identifies"

Our record does **not** carry one object called "the obstruction". It carries four
statements at four different grades, and the failure mode this brief names — calling
a heuristic a located obstruction — is live, because the single statement our own
README calls "the program's most important negative statement" is the one explicitly
labelled a heuristic.

**Status words, carried exactly:**

| # | Statement | Where | Status word, verbatim from the page |
|---|---|---|---|
| a | Deciding one step at depth `k` consumes the state's 2-adic data to depth `σ + k + 2`, and nothing regenerates it | `stage4.md` 11.8.7.7; published as Prop. 3.9 | **"The consumption identity is proved"** |
| b | Therefore bounded-window determinism cannot decide unbounded horizons | same sentence, same paragraph | **"the organizing heuristic, not a formalized theorem (the published paper's own register, adopted here)"** |
| c | The residual difficulty splits in two and only two places: statistics for typical orbits, rigidity for cycles | `README.md`; `stage4.md` 11.8.7.7; published as the sentence after Prop. 3.9 | published: **"the paper's organizing negative observation"**; README: **"an organizing observation, and we treat it as load-bearing"** |
| d | Uniform cycle exclusion requires the divisibility system — equivalently, rigidity of the closed anchor walk `Σ_t ΔM_t = 0` | `cycles.md` 12.8.4; published inside Theorem 4.6 | **Theorem** (the closing sentence of Thm 4.6); wiki carries it as **Remark 12.8.4** |
| e | The spent unit stock (`q = ±1`) is the rational-anchor instance of the digit-match ceiling — linear closure demand against (poly)logarithmic tracking capacity | `cycles.md` 12.6.1.3 | **Remark**; its own Calibration paragraph: *"this is a unification note, not a lever, and nothing about cycle exclusion, the Bridge, or `q` dividing `R_0` moves"* |
| f | The `×2×3` gap | `aeh.md` 13.6.7 | Not a result of ours. Named there as the thing **both** equidistribution statements sit on: *"which is exactly the kind of independence nobody can currently prove"*; the two are *"two faces of one missing genre of theorem, not … one statement in two notations"* |

**What this means for the clause, stated flat.**

- The **only** item at theorem grade that says what the obstruction *is*, is (d) — and
  (d) is a statement about what uniform cycle exclusion *requires* (divisibility /
  anchor-walk rigidity), not a proof that the requirement cannot be met. It locates,
  it does not obstruct.
- The item usually reached for as "where the difficulty lives" — README's own heading,
  which is (b)+(c) — is at **heuristic** and **observation** grade, not theorem. README
  says so in the same sentence it makes the claim: *"which strongly suggests — as the
  organizing heuristic, not a formalized theorem — that no bounded amount of digit
  information can decide an orbit's behavior forever."*
- (e) explicitly disclaims being a lever.
- (f) is not our result at all; `aeh.md` 13.6.7 records it as the shared naming from
  the correspondence of 2026-07-24, and uses it to say that *neither* equidistribution
  statement implies the other.

**Verdict.** "Locates the obstruction" is supported only if "the obstruction" means
(d): *what uniform cycle exclusion requires instead of counting*. Under that reading
it is a published theorem sentence and the clause is honest. Under the reading a
referee is at least as likely to take — the digit-budget localization, README's "where
the difficulty actually lives" — the clause would be attaching a theorem-shaped verb
to a statement our own record and our own published paper both label an organizing
heuristic. Both readings are available from our record; the record does not choose
between them.

One further constraint, from `cycles.md` 12.8.4 itself: *"both are rare-event
arithmetic questions, not counting questions."* The obstruction the dichotomy
identifies is, by our own text, the *absence* of a tool (arithmetic/rigidity input),
not the presence of a proved barrier.

### 5.2 "exhibits it from three independent directions"

**There is no "three directions" object in our record.** The phrase belongs to the
shared repository, whose name is `one-obstruction-three-faces` and whose `NOTE.md`
skeleton (Merle, 2026-07-19, recorded at `briefs/merle-round7-check-findings.md`
§(iv)) has the working title *"One obstruction, three faces: the Collatz cycle problem
between size, digits, and the local–global seam"* with §2 **Face I size [L1]**, §3
**Face II digits [L-A1, L-A2]**, §4 **Face III the seam [L3]**. That is his
architecture. Their current ledger status is the sibling session's item, not this one's.

**Our record has three *different* triples, and none of them is that one.** They must
not be conflated:

1. **The three faces of the target-shift mechanism** — boundary-shell localization and
   forced carry (`stage3.md` 11.8.6.3, Interpretation), the entry-depth targets
   `1 − 2^s` (11.8.6.3.3), the ladder targets `3^(−k)` (`ladder.md` 15.5). `cycles.md`
   12.6.1.3(d) adds the target family `c = −q` as a **fourth** face. This is about one
   lemma, not about the cycle obstruction.
2. **"Three directions have defined success criteria"** — published paper, Discussion,
   verbatim: *"rigidity statements for closed anchor walks beyond the size level (the
   only route past Theorem 4.6); transfer-operator analysis of the exact window chain;
   and any progress on digits of 2-adic logarithms of integers."* These are three
   *research directions*, not three exhibitions of an obstruction.
3. **Two, not three** — README, `stage4.md` 11.8.7.7, and the published sentence after
   Prop. 3.9 all say the residual difficulty splits *"cleanly in two, and only two,
   places"*: statistics and rigidity. Our record's own count of the faces of the
   difficulty is **two**.

**Does "independent" survive the round-11 finding?**

The finding, from `briefs/merle-r11-hygiene-check-findings.md` §8.2 and item 4, in its
own words:

> So the "third face" claim is **correct**, and in fact stronger than he states it:
> the per-step drift does not merely *bound* the seam gap, it **sums to it exactly**.

and

> the drift is **not a new object, it is the seam identity read one step at a time**,
> and now with an identity rather than an approximation.

Two things follow, and they point opposite ways, so both are recorded:

- **The drift is not an additional independent direction.** It is the seam identity
  (Face III) re-expressed per step. Whatever the count of independent faces is, the
  drift does not raise it.
- **The finding calls the "third face" claim correct** — correct precisely *because*
  the drift is a face of the *same* wall. Being the same wall is what makes it a face
  and what makes it not independent. The two statements are consistent; the word doing
  the work is "same".

**Terminology discrepancy, recorded and not adjudicated.** His round-11 letter calls
the drift *"a third face of the same wall"* (that is the phrase the hygiene findings
quote and answer). This brief calls it *"a fourth face"*. Our record contains only the
former wording; where the count "third" or "fourth" comes from is not settled by
anything in our files, because his letter is counting faces of T1's wall and the note
is counting faces of the obstruction, and those are two different lists.

**Verdict.** "Three" survives the round-11 finding, because the drift was never one of
the three — the finding removes a *candidate fourth*, it does not disturb the count.
But "three independent directions" is **not supported from our record**, for a
different reason: our record does not have three directions. It has his three faces
(size / digits / seam, his architecture, ledger-backed on his side), and separately its
own count of **two** (statistics / rigidity). And our own record supplies a positive
reason to be careful with *independent* in this exact neighbourhood: `aeh.md` 13.6.7
records two objects that both wear the word "equidistribution" and are *"two faces of
one missing genre of theorem"*, and `cycles.md` 12.8.4 records that the cycle half and
the divergence half *"are the same problem"*. Our record's characteristic move on this
material is to show that apparently separate things are the same thing. A referee-facing
claim of *independence* runs against that grain, and nothing in our files establishes
the independence of the note's three.

### 5.3 "a machine-checked fragment of the cycle literature" — what our record carries

Not adjudicated here (his half, and the artifacts are his). Recorded flat, from
`HANDOFF.md` item 1, so that the author has our side of it in one place: every kernel
claim we have keyed is keyed **read-not-built** — no Lean toolchain exists in this
workspace, and the trust boundary is stated in each findings file. The statement-match
audits are ours; the machine-checking is his.

---

## 6. The prior-art item found this round, stated flat

From `briefs/junction-public-recon-findings.md` §5.2(iv), recorded here without
adjudication:

`collatz-cycles-lean/docs/PROOF_ASSEMBLY.md` §10.5, **dated 17 March 2026** in the
document header and **committed 2026-03-26**, verbatim:

> **Consequence:** The "dangerous" `k` values (where `{kα}` is smallest) are confined
> to convergent denominators `q_n` of the continued fraction of `α`. No other `k` can
> approach 0 more closely. This regularizes the problem: we only need to check that
> the Baker bound holds at convergent denominators.

**What it bears on.** This is the same observation as the L-A8/T1 frame-prediction
point — thresholds live on the convergent grid — and as the tightening our round-10
L-A8 check contributed (that an in-window `n` is a priori a *multiple* of a convergent
denominator, `cycles.md` 12.8.6.1's neighbourhood). **It is his, and it predates the
correspondence on his side by four months** (correspondence begins 2026-07-16). It
belongs in the note's credit language.

**What it does not bear on.** It does not touch either half of the counting dichotomy.
The recon records, in the same section: our `1.585^(−p)` degradation and his
`3^(−0.415k)` are **different constants over different counters** (`3^0.415 = 1.5777…`
is `3^(2−log₂3)`; our `1.585` is `log₂3 = 1.58496…`; his `k` counts odd steps, our `p`
counts blocks) and *"the numerical proximity is a coincidence of two different
constants"*; and there is **no counterpart anywhere in his four repositories** to the
staircase family or to any statement that counting arguments cannot do substantially
better (§5.2(iii); the word *escalier* occurs for a different object and is recorded
so it cannot later be mistaken for a shared one). The recon's own bottom line:
**"Nothing found would change a claim of ours."**

No priority is adjudicated here. Dates and documents are recorded so the author can.

---

## 7. What a referee would find in our published record that the sentence must survive

One short list. Every item is ours, published or in the wiki a published paper points
at, and every one constrains what the note may claim.

1. **The program disclaims a path to the conjecture.** `README.md`, closing paragraph,
   verbatim: *"**What this program does not claim:** a path to the conjecture. Its
   honest product is the conversion of folklore into exact statements — a faithful
   reformulation, exact per-step laws, a precise localization of the difficulty, and
   cycle results with unusually little machinery."*

2. **The sharpness hedge is published and is not upgradable.** Theorem 4.6, v1 and v2:
   *"we assess (supported by the verified instances, though not proved here for all
   `p`)."* `publication.md`: *"The hedge sentence is not upgradable; better evidence,
   not a closure, is what v2 added."* v2's own Version note: *"No theorem or universal
   claim is strengthened."*

3. **Periods 1–3 are rederivations and priority is disclaimed.** Published Theorem 4.4,
   verbatim: *"These statements are contained in the classical results [Steiner,
   Simons–de Weger, Hercher]; the derivations, not the theorems, are the contribution."*
   `publication.md`: *"**Cycles, periods 1–3** — *subsumed*… Never claim priority."*

4. **The digit budget's conclusion is a heuristic, in print.** Published Prop. 3.9:
   *"we treat it as the organizing heuristic, not a formalized theorem."*
   `publication.md` records the same for the budget's conclusion.

5. **Our own published Related-work paragraph names a kindred lemma of his** (§4(b)
   above), and the same paragraph is where a referee would check the dichotomy's
   novelty claim.

6. **The cycle front is parked and the ladder retired.** `README.md` stopping rules:
   *"No per-period cycle search runs, period."* `cycles.md` 12.8.5. A note that implied
   the counting result is a step on an active cycle programme would contradict our own
   published and wiki strategy.

7. **AEH's scope is almost-everywhere only, and the paper says the budget blocks
   reaching it.** Published, after Hypothesis 5.1: AEH *"does not exclude individual
   staircase tails … and by Proposition 3.9 it cannot be reached by finite-window
   computation. Its content is a question about digits of 2-adic logarithms, older and
   broader than the Collatz problem."*

8. **One internal number a referee could catch.** README and `cycles.md` 12.8.5 give
   the `p = 92` search bound as `n ~ 10^18`; `cycles.md` 12.8.2's own verification
   table gives `n₀(92) ~ 4.78·10^21`. Both wiki, neither published. Recorded, not
   corrected (this session does not edit wiki pages). A referee-facing sentence should
   cite neither.

9. **`publication.md` is not a published artifact.** It is a wiki planning page that
   summarises the papers, and it uses the word "dichotomy" in wordings ("its sharpness
   dichotomy", "the uniform-trim/staircase dichotomy") that are *not* the published
   ones. The published wordings are "a sharp dichotomy for counting arguments" and
   "the counting-limit dichotomy". Anything quoted to a referee should come from the
   PDF.
