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
