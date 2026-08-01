# Findings: staircase status versus the declared no-strengthening scope (v3 round 2, finding 4)

Brief: `briefs/v3r2-staircase-scope-brief.md`. Audited at `e4dac49` (= `main` at
session start), working tree clean.

**Audit only. Nothing in the repository is modified by this session except this
file.** `paper/collatz-reduced-v3.tex`, `cycles.md`, and every wiki page were
opened read-only. No git write operation of any kind was performed. Every
constant, period range, section number and line number below was read out of the
file it is attributed to; none is recalled.

**Recommendation in one line: take the MINIMAL option.** Six sentence-level
edits, one file, no renumbering, abstract untouched. The reasoning is §3; the
cost of rejecting the full option is stated fairly at §3.4; the full option's own
site list is §5, so the decision can be reversed cheaply.

---

## 1. Scope table

### 1.1 What `cycles.md` §12.8.6 actually proves

The claim at issue, stated once so the rest of the table can be read against it:
*for a given period `p`, there exists a period-`p` configuration `(m_t, s_t)`
satisfying every rotation's exact size condition `q ≤ R_r`, at a `γ` far below
any polynomial-in-`p` extension of the period-2/3 constants.* This is an
existence claim at each `p`; "all-`p` sharpness" is that claim quantified over
`p`.

| period range | what is established | by what means | where | achieved `γ` |
|---|---|---|---|---|
| **`p ≥ 16`** | existence, unconditionally | **proof.** `12.8.6.1` (availability) supplies an `n` in `[L^p, 1.05·L^p]` with `δ(n) ∈ [0.0415, 0.1169390665…]`, which meets `12.8.6.2`'s (H0) and (H1); `12.8.6.2` (explicit integer construction, no correction step) turns it into a profile passing all `p` rotations | `cycles.md` 12.8.6.1 → 12.8.6.2 | `3.683012 ≤ γ ≤ 5.140212`, **both ends absolute constants, no `p` in either** |
| **`p ∈ {3, 5, 6, …, 15}`** | existence | **finite check.** An explicit `n` meeting the same bracket, exhibited at a widened scale (`κ := n/L^p` up to `1.70`); `12.8.6.1` states this is a check and not the window argument | `cycles.md` 12.8.6.1 | same bracket |
| **`p ∈ {2, 4}`** | existence | **direct exhibition only.** Both lie *outside* `12.8.6.2`'s reach: `Γ(2,n) = n + η` and `Γ(4,n) = 0.196191·n + 1.507147 + η`, so a bounded `γ` caps `n` at `5` and `18`, and the canonical windows `[2.512, 2.638]` and `[6.311, 6.626]` contain no integer at all | `cycles.md` 12.8.3, 12.8.6.4 | **no bracket claim.** Witnesses come from the superseded recipe's record, band `γ/log₂p ∈ [1.828, 3.643]` |
| every `p` above | every constructed configuration **fails** the divisibility system `q \| R_r` at every rotation | exact integer check | 12.8.6.1–12.8.6.4, and `12.8.6`'s preamble | — |

**Four limits that are part of the true statement**, all stated by the record's
own *Scope, and what is not covered* paragraph (`cycles.md` L378) and none of
them softened here:

1. The proof is a **composition of two theorems with hypotheses**, (H0) and
   (H1) — not an unconditional identity. `12.8.6.1`'s job is exactly to supply
   an `n` meeting them.
2. `Γ` is **conservative by 0.6–0.9 bits** (the step-(e) bound keeps one term of
   `R_r` and discards `p−1` positive ones), so the certified family is narrower
   than the empirical one; (H1) is sufficient, not necessary.
3. `p ∈ {2, 4}` have exhibited size-passers but **no theorem covering them**.
   "At every period" means *every period, two of them by exhibition*.
4. Independent numerical verification stops at `p ≈ 32` (`n ≈ 2.5·10⁶`, `3ⁿ` at
   `4·10⁶` bits) — a limit on the check, not on the theorem, nothing in which
   degrades with `p`.

**Does exhibition at `p ∈ {2,4}` genuinely close the family?** Yes, for the claim
as stated. The claim at a fixed `p` is an existence claim, and an exhibited
witness closes an existence claim outright — this is the same instrument the
paper itself uses at `p = 7`. What exhibition does *not* do is place those two
periods inside the uniform bracket `[3.683012, 5.140212]`; the record makes no
bracket claim there, and neither should the paper. So the universal statement
("at every period there is a size-passer with small `γ`") is closed; the
*uniform-constant* statement has two named exceptions carrying explicit finite
values.

**One precision item on the record side, flagged not repaired.** `12.8.6.1` says
the finite check covers `3 ≤ p ≤ 15` and, in the next sentence, that
`p ∈ {2,4}` lie outside `12.8.6.2`'s reach. Since the finite check *uses*
`12.8.6.2` at a widened scale, `p = 4` cannot be in both. The honest partition is
`{3, 5, 6, …, 15}` by finite check and `{2, 4}` by exhibition, which is what
`experiments/staircase_allp_construction.py`'s own coverage (`p ∈ {2,…,30}`
outside `{2,4}`) reflects. The paper's correction (L235) mirrors the record's
wording exactly, so **no paper edit is proposed for this** — the paper should not
be more precise than the record it cites. If the record's sentence is repaired,
the paper's should follow in the same round.

### 1.2 What the paper claims, site by site

Verdicts: **KEEP** (accurate, no edit), **FIX** (inaccurate or becomes
inaccurate under the recommendation), **MOVE** (accurate but in the wrong
environment).

| line | site | current claim (elided with …) | status against `cycles.md` §12.8.6 | verdict |
|---|---|---|---|---|
| 38 | abstract | `Our main new theorem is a sharp dichotomy for counting arguments: … an explicit family of near-counterexamples (staircases…) shows counting arguments cannot do substantially better, so uniform cycle exclusion requires arithmetic (divisibility) input…` | carries **no status word and no all-`p` quantifier**; the claim is proved in-paper by the exhibited `p=7` witness and is now better supported by the record | **KEEP** |
| 41–42 | version note, v2 block | `No theorem or universal claim is strengthened; v2 adds a finite computational evidence record.` | true **of v2's own delta**; v2 added evidence and no claim | **FIX (2 words)** — scope it to v2 so it does not read as a standing policy the closing sentence then contradicts |
| 42 | version note, v3 block | `The original sentence stays in place, and Theorem~\ref{thm:staircase} with its hedge is unchanged.` | true today; **becomes false** the moment the hedge is lifted out | **FIX** |
| 42 | version note, v3 closing | `No theorem or universal claim is strengthened.` | **inaccurate.** v3's own appended correction reports a universal claim proved at every period, at `γ` between two absolute constants — stronger than the `O(log p)` the paper assesses. The reviewer is right | **FIX** |
| 46 | Author's note | `a uniform trim that caps what size-counting can achieve against cycles` | no status claim about the staircase | **KEEP** |
| 50 | Introduction | `(answer: exponentially far in the number of blocks, and provably no farther)` | "provably" is carried by Theorem 4.6's exhibited witnesses | **KEEP** |
| 54 | Contributions (v) | `--- the main new theorems --- a uniform trim … together with a sharpness family showing the exponential loss is intrinsic to size-counting` | both remain numbered theorems under the recommendation; the sharpness family is proved in-paper by exhibition | **KEEP** |
| 56 | Introduction | `proves both what counting can do there … and that it can do no more (the staircase family)` | same | **KEEP** |
| 59 | Related work | `an impossibility lemma … kindred to our Theorem~\ref{thm:staircase}` | `\ref` intact under the recommendation | **KEEP** |
| 221–222 | Theorem 4.6, opening + witnesses + divisibility + closing consequence | `No trim uniform in $p$ can extend the small-period constants: there exist configurations … Explicitly, at $p=7$, $n=94$ … $\gamma = 6.74$ … $84$ further verified instances … All such configurations fail … Uniform cycle exclusion therefore requires the divisibility system …` | **already proved, in the paper, by the exhibited witness.** A single witness at `p = 7` defeats any uniform-in-`p` extension of the `p = 2,3` constants; the theorem carries no `\begin{proof}` because the witness *is* the proof. Now proved at every period in the record as well | **KEEP, unchanged** |
| 222 | Theorem 4.6, the construction-and-assessment clause | `The construction --- block depths growing geometrically … --- tracks the extremal configuration …, and we assess (supported by the verified instances, though not proved here for all $p$) that it passes all size conditions with $\gamma = O(\log p)$ for every $p$.` | true as a statement about the paper ("not proved **here**"), and understated twice over: the record proves it, and at a shape (`γ` bounded by absolute constants) stronger than `O(log p)`. But it is an **unproved assessment inside a `theorem` environment** | **MOVE** |
| 225–227 | Remark 4.7 | what the staircase means | no status word; number unchanged under the recommendation | **KEEP** |
| 229–232 | Note added in v2 | the v2 evidence record and the gap it named | a dated v2 record, superseded by the appended correction rather than rewritten — the established convention, restated by the version note itself (`The original sentence stays in place`). Its closing `The hedge sentence above is therefore unchanged` still resolves: the assessment passage sits above it | **KEEP** |
| 235 | Correction, 2026-08-01 | every scope statement — `every period $p \ge 16$`, `$3 \le p \le 15$ … by finite check`, `$p \in \{2,4\}$ … by direct exhibition`, `\gamma` between `3.683012` and `5.140212`, `66` consecutive integers, `0.05(\LL)^p` integers, `79` at `p=16`, `1/(\LL-1) = 1.70951`, `13` and `8` correction moves, `p \in \{3,\dots,26\}` end to end, construction verified through `p = 32`, `from $p = 8$ upward not one working witness is a convergent or semiconvergent denominator` | **all verified accurate** against `cycles.md` 12.8.6.1–12.8.6.4 (see §6) | **KEEP** |
| 235 | Correction, final clause | `Theorem~\ref{thm:staircase} and its hedge stand above exactly as written.` | **becomes false** once the hedge leaves the theorem | **FIX** |
| 247 | AEH | `it does not exclude individual staircase tails (Remark~\ref{rem:staircase})` | no status claim; number unchanged | **KEEP** |
| 259 | Discussion | `for cycles, whether closed anchor walks are rigid (Theorem~\ref{thm:staircase} --- arithmetic)` and `rigidity statements … (the only route past Theorem~\ref{thm:staircase})` | both `\ref`s resolve to a theorem that **retains its anchor-walk closing consequence** under the recommendation | **KEEP** |

---

## 2. The four adjudications the brief asks for

### 2.1 Is Theorem 4.6's *opening* claim now proved outright by 12.8.6, rather than assessed?

**No — and the premise needs correcting, in the paper's favour.** The opening
claim was never assessed. It reads:

> No trim uniform in $p$ can extend the small-period constants: there exist
> configurations satisfying every rotation's exact size condition $q \le R_r$
> whose $\gamma$ falls far below any polynomial-in-$p$ extension of the constants
> of periods $2$--$3$.

That is an existence claim, and the theorem exhibits its witness in the very next
sentence: `p = 7`, `n = 94`, `m = (4,7,9,15,23,35,1)`, `γ = 6.74` against a
period-3 demand of `8.9`, plus `84` further instances at `p = 6`. One witness
defeats a *uniform-in-`p`* extension. The theorem environment carries no
`\begin{proof}` precisely because the witness is the proof. `cycles.md` 12.8.3
records the same instances at the same numbers, and the earlier round's audit
(`briefs/staircase-status-audit-findings.md` §4.1(i)) reached the same verdict:
"understated, not wrong". §12.8.6 does not change this sentence's status; it
strengthens what stands behind it, from two periods to all of them.

So the sharper form of the reviewer's objection is the one that survives, and it
does survive: **the hedge attaches to a different and stronger claim than the
theorem's opening**, namely `γ = O(log p)` for *every* `p`. That clause is (a) an
unproved assessment sitting inside a `theorem` environment, which is a register
defect independent of anything the record did, and (b) now stale, since the
record proves it at a stronger shape. Both are repaired by moving it out, which
is exactly the minimal option's core move.

There is a second consequence, and it points the opposite way from the reviewer's
first bullet: once the assessment leaves, **everything remaining inside Theorem
4.6 is proved**. A theorem that is entirely proved is not a candidate for
demotion to an unnumbered assessment passage.

### 2.2 Renumbering: what it actually costs

**Internally it is one number. Externally it is the worst kind of break.**

The preamble declares `\newtheorem{theorem}{Theorem}[section]`, so the counter
**resets at every section** and every other environment shares it via
`[theorem]`. Section 4 runs: Proposition 4.1 (`prop:elim`), Corollary 4.2
(`cor:size`), Lemma 4.3 (`lem:ceiling`), Theorem 4.4 (`thm:smallp`), Theorem 4.5
(`thm:uniform`), Theorem 4.6 (`thm:staircase`), Remark 4.7 (`rem:staircase`).
Nothing else in Section 4 follows. Section 5 begins its own count at Hypothesis
5.1 and Lemma 5.2.

So the brief's premise that the full option "renumbers everything after 4.6" is
false: it renumbers **exactly one printed number, Remark 4.7 → Remark 4.6.**
Section 5 does not move.

That makes the renumbering cost worse, not better. The number `4.6` is not
retired — it is **reused, for a different object of a different kind.** And `4.6`
is live:

* **v1** (DOI `10.5281/zenodo.21273548`) and **v2** (DOI
  `10.5281/zenodo.21421120`) both print **Theorem 4.6 = sharpness: the
  staircase**, confirmed at `briefs/jointnote-premise-ours-findings.md` L216–219
  ("same numbers, Theorem 4.5 / Theorem 4.6").
* `briefs/jointnote-premise-ours-findings.md` uses **Theorem 4.6** as the
  identifier for claim B of the contribution table (L43, L182, L217, L290, L328,
  L382, L490).
* `briefs/merle-round11-reply-draft.md` L703, L765 — **text already sent** —
  cites Theorem 4.5 and Theorem 4.6 by number, and identifies Theorem 4.6's
  closing sentence as the theorem-grade obstruction.
* **Merle's round-12 reply, received 2026-07-30** (`briefs/merle-round12-letter.md`
  L808): *"of which only Theorem 4.6's closing sentence is theorem-grade. A note
  titled for one obstruction has to say which of the four it means, and I think
  it should mean that sentence."*

That last one is decisive on its own. A joint note is being titled around
Theorem 4.6's closing sentence. The full option deletes the number that sentence
lives at, keeps the sentence but strips its theorem grade, and hands `4.6` to a
remark. Anyone resolving "Theorem 4.6" against v3 finds no such theorem and a
Remark 4.6 sitting where it used to be — a silent mis-resolution rather than a
loud one.

v3 being unpublished makes renumbering *possible*. It does not make it free.

### 2.3 Does the abstract's claim survive the minimal option honestly?

**Yes, and it is more accurate now than when it was written.** The sentence is:

> Our main new theorem is a sharp dichotomy for counting arguments: a trim
> uniform in the number of blocks $p$ exists, giving effective finiteness at
> every period, but its constant necessarily degrades like $(\LL)^{-p}$ --- an
> explicit family of near-counterexamples (\emph{staircases}: …) shows counting
> arguments cannot do substantially better, so uniform cycle exclusion requires
> arithmetic (divisibility) input, not sharper counting.

Three checks. (i) It carries **no status word** — no "assess", no "conjecture",
no "not proved". (ii) It carries **no all-`p` quantifier** on the sharpness half;
it says an explicit family shows counting cannot do substantially better, which
the in-paper `p = 7` witness establishes. (iii) The word doing the work,
**"sharp"**, is now better earned than in v1: the record shows the family closes
at every period at a `γ` that does not grow at all.

Both halves of the dichotomy remain numbered theorems under the minimal option
(4.5 and 4.6), so "dichotomy" continues to name a pair of theorems, which is what
`briefs/jointnote-premise-ours-findings.md` L43 records it as. **No edit.**

*One observation, explicitly not a proposal:* the abstract says "main new
theorem" (singular) for a pair, while Contributions (v) says "the main new
theorems" (plural). Pre-existing, cosmetic, and outside this round's finding.

### 2.4 Reporting the record result at its true scope without claiming it

The paper already does this well, and the credit belongs to the round-1
correction. L235 states: the two halves compose to a proof for every `p ≥ 16`, at
`γ` between `3.683012` and `5.140212` with no `p`-dependence; `3 ≤ p ≤ 15` by
finite check; `p ∈ {2,4}` outside the construction's reach and covered by direct
exhibition; every constructed configuration is a size-passer that fails
`q \| R_r`; and — the load-bearing clause — *"That proof is established in the
project record at the reference below and is **not reproduced in this paper**."*
I verified every one of those figures against `cycles.md` §12.8.6 (§6 below);
they are faithful.

So the wording problem is not "how do we report it" — that is solved — but that
the correction's **last clause** anchors itself to a hedge that is about to move.
That is the only sentence at L235 that changes.

The forward pointer belongs in the new assessment passage, not a second full
scope statement: stating the scope twice in one section invites the two copies to
drift.

---

## 3. Recommendation

### 3.1 Take the MINIMAL option.

Theorem 4.6 keeps its number and its statement. Its construction-and-assessment
clause is lifted into a labelled `\paragraph{Sharpness evidence and assessment.}`
placed immediately after the theorem. The correction's closing clause is
re-anchored. The version note gets three sentence-level repairs, including the
replacement the reviewer asked for. The abstract, Contributions, the
Introduction, the Discussion, Remark 4.7 and the Note added in v2 are untouched.
Nothing is renumbered.

**Six sentence-level edits, all in `paper/collatz-reduced-v3.tex`**, at lines
42 (three), 222 (one deletion), an insertion after 223, and 235 (one clause).
Plus the PDF rebuild the repo's own convention requires (`6a9183a`, "build: PDF
rebuilt from the audited tex"). No other tracked file changes.

### 3.2 Why

The reviewer's diagnosis is right and his prescription overshoots on one bullet
out of four.

He is right that a `theorem` environment must not contain "we assess … though not
proved here", and right that "No theorem or universal claim is strengthened" no
longer describes v3. Both are repaired by the minimal option, which adopts his
bullets 2, 3 and 4 essentially as written.

He is wrong on bullet 1 — "present only the uniform trim as the in-paper main
theorem" — because it rests on reading the staircase as an assessment. It is not.
Strip the hedge and what is left is a proved existence theorem with its witness
printed inline and a proved consequence attached (§2.1). Demoting a proved
theorem to an unnumbered "assessment" passage is a **false demotion**: it would
make the paper understate its own content, and it would do so at the exact moment
the supporting record got stronger. The paper would move away from accuracy in
both directions at once — the hedge lifted (correct) and the theorem downgraded
(incorrect).

Three further facts, each verified, each pointing the same way:

1. **The demoted content is the paper's novelty, and the promoted content is
   the part with the most classical company.** `publication.md` L38's own
   claim-by-claim verdict: the cycle layer's results are *subsumed* except that
   "an explicit theorem that size-counting cycle exclusion is capped at
   exponential-in-`p`, with a constructive sharpness family, was not found in the
   literature" — the sharpness dichotomy is "the strongest candidate for a
   genuinely new theorem". Theorem 4.5 alone is an effective-finiteness result in
   the Baker/Eliahou line the paper itself cites. The full option would headline
   the derivative half and unnumber the novel one.
2. **It would strand the live correspondence** (§2.2). Merle's round-12 letter
   proposes titling the joint note around Theorem 4.6's closing sentence, which
   the full option strips of theorem grade while reusing the number for a remark.
3. **The family question was already adjudicated, and it was adjudicated toward
   strength.** `publication.md` L38 records the decision: *"The construction
   proved is `thm:staircase`'s own family better specified, not a different one …
   What was mis-specified was the generator, never the family."* Under that
   ruling the record proves *this theorem's* assessment. A paper whose assessment
   has been proved does not respond by demoting the theorem the assessment sat
   under.

The minimal option also leaves Theorem 4.6 strictly cleaner than it is today:
every sentence inside the environment is proved, and the anchor-walk consequence
— the one statement in this area everyone external cites — stays inside a
numbered theorem where it belongs.

### 3.3 What the minimal option deliberately does *not* do

It does not import any part of the proof. It does not claim the all-period result
for the paper. It does not restate Theorem 4.6's claim to cover all `p`. It does
not touch the Note added in v2, whose gap sentence stays wrong-and-superseded
behind an appended correction, exactly as the round-1 decision left it and as the
version note describes.

### 3.4 The cost of the option I am rejecting, stated fairly

The full option is not unreasonable, and it buys three real things.

* **A cleaner theorem/evidence boundary at the section level.** With only one
  numbered theorem in the cycle section's climax, no reader can mistake evidence
  for theorem — a stronger guarantee than the minimal option's, which relies on
  the reader noticing where the theorem environment ends.
* **Maximum conservatism.** If the family judgment at `publication.md` L38 were
  ever reversed — if Construction B were later held to be a *different* family
  from the printed description — the full option's paper would already be making
  the weaker claim and would need no further retreat. The minimal option would
  then need a second pass. That risk is real but small: the ruling is recorded,
  reasoned, and turns on the published sentence describing a shape and specifying
  no rounding rule.
* **It answers the reviewer literally**, which has value when the same reviewer
  reads v3 again.

Against that: it renumbers a live, externally-cited number onto a different
object (§2.2); it rewrites the abstract's headline away from the paper's most
distinctive claim (§2.3); it strips theorem grade from the sentence a joint note
is being built around; it breaks all seven `\ref{thm:staircase}` sites, each
needing a prose replacement written by hand; and it understates the paper at the
one moment the record can support strengthening. The first and last of those are
not recoverable by careful wording.

I do not think the balance is close, and I am not leaving it open: **minimal.**

---

## 4. Drop-in text for the recommended option

All six edits are in `paper/collatz-reduced-v3.tex`. Each is given as an exact
`old` → `new` pair for a string-match edit. **Apply with the Edit tool. Never
`Get-Content | Set-Content` or PowerShell redirection** — this file contains
`---`, `≤`-class math and accented bibliography entries that PS 5.1
double-encodes.

Three of the six land on **line 42**, which the sibling round-2 delegate is also
likely to edit (see §7). All three are given as sentence-level anchors, not
line replacements, so the two sets compose in either order.

### Edit 1 — Theorem 4.6 (line 222): remove the assessment sentence

**old** (one sentence, mid-paragraph; the leading space before `The construction`
and the trailing space after `every $p$.` are inside the match so no double space
is left behind):

```latex
 The construction --- block depths growing geometrically at ratio $\approx\LL$ with unit exit valuations, closed by a single block of unit depth and maximal exit valuation --- tracks the extremal configuration of the max-plus recursion in the proof of Theorem~\ref{thm:uniform}, and we assess (supported by the verified instances, though not proved here for all $p$) that it passes all size conditions with $\gamma = O(\log p)$ for every $p$.
```

**new**: (empty — delete the matched text)

The theorem then reads, in full:

```latex
\begin{theorem}[sharpness: the staircase]\label{thm:staircase}
No trim uniform in $p$ can extend the small-period constants: there exist configurations satisfying every rotation's exact size condition $q \le R_r$ whose $\gamma$ falls far below any polynomial-in-$p$ extension of the constants of periods $2$--$3$. Explicitly, at $p=7$, $n=94$, the staircase $m = (4,7,9,15,23,35,1)$ with $s = (1,\dots,1,\,S-6)$ passes all seven size tests with $\gamma = 6.74$, where the period-$3$ constant would demand $\gamma > 8.9$; $84$ further verified instances occur at $p=6$ alone. All such configurations fail the divisibility conditions $q \mid R_r$. Uniform cycle exclusion therefore requires the divisibility system --- equivalently, rigidity of the closed anchor walk $\sum_t \Delta M_t = 0$.
\end{theorem}
```

Every sentence remaining is closed by the witnesses printed in the second
sentence.

### Edit 2 — insert the labelled passage after line 223 (`\end{theorem}`)

Insert as a new paragraph between `\end{theorem}` (223) and
`\begin{remark}\label{rem:staircase}` (225), keeping the blank lines either side:

```latex
\paragraph{Sharpness evidence and assessment.} The construction behind these witnesses --- block depths growing geometrically at ratio $\approx\LL$ with unit exit valuations, closed by a single block of unit depth and maximal exit valuation --- tracks the extremal configuration of the max-plus recursion in the proof of Theorem~\ref{thm:uniform}. Supported by the verified instances, though not proved here for all $p$, we assess that it passes all size conditions with $\gamma = O(\log p)$ for every $p$. This assessment is evidence for Theorem~\ref{thm:staircase} and no part of it: the theorem is closed at $p = 6, 7$ by the witnesses exhibited above. The assessment has since been proved in the project record, at a scope and a shape stronger than assessed here; the Note added in v2 and its correction below state what was proved, where, and at what scope.
```

Register notes: `\paragraph{...}` matches `\paragraph{Contributions.}` (L54) and
`\paragraph{Calibration.}` (L249) — mid-section, unnumbered, no table-of-contents
entry. The assessment's own wording is carried over unchanged in substance so
that nothing the reader had in v2 is lost. The scope of the record result is
*not* restated here; it lives once, at L235, and is pointed at.

### Edit 3 — the correction's final clause (line 235)

**old:**

```latex
That proof is established in the project record at the reference below and is \emph{not reproduced in this paper}; Theorem~\ref{thm:staircase} and its hedge stand above exactly as written.
```

**new:**

```latex
That proof is established in the project record at the reference below and is \emph{not reproduced in this paper}; Theorem~\ref{thm:staircase} stands above exactly as written, and what is proved in the record is the assessment stated above under \emph{Sharpness evidence and assessment}, at a stronger shape than that assessment claims.
```

### Edit 4 — version note, v2 block (line 42): scope the first occurrence

**old:**

```latex
No theorem or universal claim is strengthened; v2 adds a finite computational evidence record.
```

**new:**

```latex
No theorem or universal claim is strengthened in v2, which adds a finite computational evidence record.
```

This occurrence is *accurate* — it describes v2's own delta, and v2 genuinely
strengthened nothing. Two words fix the only defect it has, which is that a
reader meets the identical sentence twice and is entitled to read the first as a
standing policy that the second then contradicts.

### Edit 5 — version note, v3 block (line 42): the description of what v3 does

**old:**

```latex
The original sentence stays in place, and Theorem~\ref{thm:staircase} with its hedge is unchanged.
```

**new:**

```latex
The original sentence stays in place and Theorem~\ref{thm:staircase}'s statement is unchanged; its sharpness assessment, previously the theorem's closing clause, is now set out beside it under \emph{Sharpness evidence and assessment}, so that the theorem environment carries only what the paper proves.
```

### Edit 6 — version note, v3 closing (line 42): the sentence the reviewer flagged

**old:**

```latex
Verification pointers and script names are made concrete throughout. No theorem or universal claim is strengthened. v3-specific Zenodo DOI: 10.5281/zenodo.21730505.
```

**new:**

```latex
Verification pointers and script names are made concrete throughout. No numbered theorem's claim is strengthened, weakened, or renumbered, and nothing new is proved here; v3 reports a stronger result established in the project record and not reproduced in this paper. v3-specific Zenodo DOI: 10.5281/zenodo.21730505.
```

**Why not the reviewer's sentence verbatim.** He proposes *"No numbered theorem
is restated; v3 reports a stronger result established in the project record."*
The second half is exactly right and is kept. The first half is not quite true
under this recommendation: Theorem 4.6's printed text **does** change — it loses
a sentence. What is invariant is the theorem's *claim*, and its number. The
drop-in says that, and adds "and not reproduced in this paper", which is the fact
that keeps a reader from inferring the paper contains the proof.

*Fallback, if the shorter form is preferred:* `No numbered theorem's claim is
strengthened; v3 reports a stronger result established in the project record and
not reproduced here.`

### 4.1 Sites confirmed to need no edit under this option

Checked by reading, not assumed: **L38** (abstract), **L46** (Author's note),
**L50**, **L54** (Contributions (v)), **L56**, **L59** (Related work), **L177**
(section title), **L221** and the rest of **L222** (theorem opening, witnesses,
divisibility clause, closing consequence), **L225–227** (Remark 4.7),
**L229–232** (Note added in v2), the whole of **L235** except its final clause,
**L247** (AEH), **L259** (Discussion, both `\ref`s). Reasons per row in §1.2.

`cycles.md`, `TOUR.md`, `publication.md`, `index.md`, `README.md`, `HANDOFF.md`:
**no change.** They already carry the record result at the scope §1.1 verifies,
and `TOUR.md` L39's "assessed" vocabulary entry — *"the paper's `thm:staircase`
sharpness half is the canonical example and remains stated that way in print"* —
stays true, since the assessment remains in print, one paragraph further down.

---

## 5. Site list for the rejected option, if this is overruled

Everything the **full** option touches, so it can be executed without a second
audit. Edits 3–6 of §4 are needed under full as well, with Edit 5 extended to
record the demotion and the renumbering.

| # | site | change required |
|---|---|---|
| 1 | **L38, abstract** | `Our main new theorem is a sharp dichotomy for counting arguments:` must go. The trim alone becomes the headline; the staircase clause is recast as evidence. Note the knock-on: "dichotomy" is the paper's own word for the pair (Related work L59, `briefs/jointnote-premise-ours-findings.md` L43), and Merle's round-12 letter treats "counting dichotomy" as a contraction of it — dropping it from the abstract needs a decision about that correspondence too |
| 2 | **L54, Contributions (v)** | `--- the main new theorems ---` → singular; `together with a sharpness family showing the exponential loss is intrinsic to size-counting` recast as evidence rather than a theorem |
| 3 | **L221–223** | `\begin{theorem}[sharpness: the staircase]\label{thm:staircase} … \end{theorem}` → an unnumbered passage. The `\label` cannot survive: an unnumbered passage has no number to `\ref` |
| 4 | **L225, Remark 4.7 → Remark 4.6** | the *only* renumbering; `\newtheorem{theorem}{Theorem}[section]` resets per section, so Section 5's 5.1/5.2 do not move. The number `4.6` is reused for a different object of a different kind |
| 5 | **seven `\ref{thm:staircase}` sites break** | L42 (×2), L59, L230, L235, L259 (×2). Each needs a hand-written prose replacement — e.g. "the sharpness passage of Section~\ref{sec:cycles}". L230 sits inside the Note added in v2, which the round-1 decision froze; rewriting a reference inside it reopens that decision |
| 6 | **L247** | `\ref{rem:staircase}` still compiles; it silently resolves to 4.6 instead of 4.7. No edit, but it is the mechanism by which the number is reused |
| 7 | **L259, Discussion** | `(the only route past Theorem~\ref{thm:staircase})` loses its referent. This is the sentence Merle's round-12 letter identifies as the only theorem-grade statement of the four; recasting it needs its own decision |
| 8 | **version note** | Edits 4 and 6 of §4 as written; Edit 5 rewritten to record the demotion and the renumbering explicitly, since a renumbering is exactly the kind of change a version note exists to declare |
| 9 | **outside the tex** | `briefs/jointnote-premise-ours-findings.md` (L43, L182, L216–219, L245, L290, L328, L382, L490) and `briefs/merle-round11-reply-draft.md` (L703, L723, L765) cite Theorem 4.5/4.6 by number against v1 and v2. They are dated records and should not be retrofitted — but any *future* letter must then carry a v1/v2-versus-v3 numbering note, and the joint note's title question (round-12 letter, L808) has to be reopened |

Roughly: full is ~15 edit sites across 3+ files plus a correspondence decision,
against minimal's 6 sentence-level edits in 1 file.

---

## 6. Verification log

Every figure quoted above was read from the file named. Nothing is recalled.

**From `cycles.md` §12.8.6** (L299–378): `L = log_2 3`; `θ = 8 − 5L =
0.0751874964…`; `Γ* = 1.05·L(L−1) + 1/(L−1) + 1 + η = 3.6830121007…`; `δ_hi =
0.1169390665…`; `δ_lo = 0.0415`, with `δ_hi − θ = 0.0417515701…`; the bracket
`3.683012 ≤ γ ≤ 5.140212`; the sweep criterion `maxgap{jθ mod 1 : 0 ≤ j ≤ J} ≤ ℓ`
with minimal `J = 13` two-sided (**66** consecutive integers) and `J = 12`
one-sided (**61**), `maxgap(11) = 0.1729375397…` failing both; the window
`[L^p, 1.05·L^p]` holding `0.05·L^p` integers, **50 at `p = 15`** and **79 at
`p = 16`**; `B(2) = −0.6114616914…`; (H0)'s margins `911.75` and `906.07` at
`p = 16`; `Γ(2,n) = n + η`, `Γ(4,n) = 0.196191·n + 1.507147 + η`, caps `5` and
`18`, windows `[2.512, 2.638]` and `[6.311, 6.626]`; `κ` up to `1.70` for
`3 ≤ p ≤ 15`; `1/(L−1) = 1.70951`; `Γ` conservative by `0.6`–`0.9` bits;
verification ceiling `p ≈ 32`, `n ≈ 2.5·10⁶`, `3ⁿ` at `4·10⁶` bits;
`p = 22` rows `n = 25217` (`γ = 11.186`, `13` moves) and `n = 31202`
(`γ = 14.746`, `8` moves); band `γ/log₂p ∈ [1.828, 3.643]` over `p ∈ {2,…,23}`.

**From `cycles.md` 12.8.3** (L293): `p = 7`, `n = 94`, `m = (4,7,9,15,23,35,1)`,
`γ = 6.74`, period-3 constant `0.1157n − 2 = 8.9`, `84` further size-passers at
`p = 6`. Matches the paper's Theorem 4.6 exactly.

**Cross-check of the paper's correction (L235) against the record:** every figure
in it — `8 − 5\LL = 0.0751874964…`, the arc `[0.0415, 0.1169390665…]`, `66`
consecutive integers, `0.05(\LL)^p` integers with `79` at `p = 16`, `p = 16` the
first such period, `1/(\LL−1) = 1.70951`, `p ∈ {3,\dots,26\}` end to end,
construction verified through `p = 32`, `13` and `8` correction moves at
`p = 22`, "from `p = 8` upward not one working witness is a convergent or
semiconvergent denominator", the bracket `3.683012`/`5.140212` — **reproduces the
record.** No discrepancy found. The correction is sound and needs no repair
beyond its final clause.

**Structural facts checked in the tex:** `\newtheorem{theorem}{Theorem}[section]`
(L7) with all other environments sharing the counter via `[theorem]` (L8–15);
Section 4's sequence 4.1–4.7 with `rem:staircase` the only item after
`thm:staircase`; Section 5 starting at 5.1; Theorem 4.6 carrying **no
`\begin{proof}`**; `\ref{thm:staircase}` occurring at L42 (×2), L59, L230, L235,
L259 (×2) — seven references, one `\label` at L221.

**Family judgment, not re-litigated:** `publication.md` L38 records it as decided
— *"`thm:staircase`'s own family better specified, not a different one … What was
mis-specified was the generator, never the family."* Everything in §3.2 item 3
rests on that ruling standing; if it is reversed, revisit §3.

---

## 7. Coordination, and things I am less than confident in

**Collision risk on line 42, and how to avoid it.** The sibling round-2 delegate
works `briefs/v3r2-aeh-formulation-brief.md`, which reformulates
Hypothesis~\ref{hyp:aeh}. The version note's v3 block contains the clause
*"Hypothesis~\ref{hyp:aeh} states the order of its two limits"*, which that work
will falsify. So **both round-2 findings will propose edits to line 42.** All
three of my line-42 drop-ins are anchored on complete sentences that the AEH work
has no reason to touch, so they compose in either order — but they must be
applied as string-match edits, not as a line replacement, and whichever is
applied second must re-read the line first.

**Less than confident, in order.**

1. **The `p = 4` double-listing** (§1.1). I am confident the record's `3 ≤ p ≤ 15`
   and `p ∈ {2,4}` clauses overlap and that `{3,5,…,15}` / `{2,4}` is the honest
   partition, but I have not re-derived whether `p = 4` is genuinely outside
   `12.8.6.2`'s reach at the *widened* scale `κ ≤ 1.70`: that window is
   `[6.31, 10.7]`, which does contain integers, and `Γ(4,n) = 0.196191n +
   1.507147 + η` is under `5.14` for `n ≤ 18`. The record says `p = 4` is outside
   reach and I have taken it at its word. If it is not, the scope sentence in
   both the record and the paper is more conservative than it needs to be — which
   is the safe direction, but it should be checked before anyone quotes it in a
   letter.
2. **Placement of the new passage before rather than after Remark 4.7.** I put it
   immediately after the theorem so the reader loses nothing where the hedge used
   to be. Putting it after Remark 4.7 would sit it adjacent to the Note added in
   v2 that discusses it. Both defensible; I chose adjacency to the theorem and
   flag it as a judgment call, not a finding.
3. **Whether the Note added in v2 should acknowledge the move.** Its closing
   sentence *"The hedge sentence above is therefore unchanged"* still resolves —
   the assessment passage is above it — but the phrase "hedge sentence" now names
   a sentence in a `\paragraph` rather than in a theorem. I propose no edit,
   because the round-1 decision and the version note both treat the v2 note as
   appendable and not rewritable, and because reopening it for a wording nicety
   is a worse trade than the small awkwardness it leaves. Recorded as a close
   call.
4. **An unrelated count I could not reconcile, recorded not repaired.** The
   version note says v3 *"repairs four defects and brings three statements back
   into line with the project record"* — seven items — and then lists eight
   (`def:reduced`'s `\w > 0`; `thm:vlaw`'s `(1+\log d)^2`; `thm:onestep`'s
   window; `\pi_k`'s depth component; `hyp:aeh`'s limit order; `thm:uniform`'s
   `n_0(p)`; the digit budget's heuristic label; `prop:elim`'s `\sigma_j` and
   `M_t`). Either the count is off by one or two items are meant to group.
   Pre-existing, unrelated to this finding, on the same line as three of my
   drop-ins — worth routing to whoever applies line 42.
