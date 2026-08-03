# Findings: the fix pass that closes the pruning round (v3 round 6)

**Branch.** `v3r6-prune`, worked in `c:\Users\Ace\Documents\Collatz`, no worktree, no branch switch,
no push, no merge, no rebase. Three commits on top of `0e50afb`:

| commit | what |
|---|---|
| `0a32136` | wiki: `aeh.md` L8 and 13.5, `README.md` L40, `bridge.md` L71 — D3 |
| `f9b07b1` | paper: D1, D2, D4–D9, D11 and one further regression found here |
| `eb3f4c4` | Appendix A record pin `881c92e` → `f9b07b1`, in its own commit |

**Headline.** All eleven defects disposed of; **one further compression casualty of the D1/D2 class was
found and repaired** (a scope word demoted to a participle in the one-limit paragraph). The paper is
**still 15 pages**, build clean at **zero overfull boxes and zero LaTeX warnings**. Every numbered
environment is byte-identical to the pre-prune paper `29ecb1b` except `rem:verify1`, the endorsed
Remark 3.6 narrowing. The pin verifies positively and negatively with `git show`. **D12 untouched.**

---

## 1. Disposition, D1–D11

### D1 — the Inselmann pair. FIXED as endorsed.

`paper` L400–406. The apply delegate's wording, endorsed by verify and by the main session, landed
verbatim:

> "…Inselmann's `\cite[Cor.~1.4, Thm.~1.10]{inselmann}`, cited in Related work, **are unconditional
> and run** to `$4.8188\ldots$` times the classical range at which this section's cylinder count stops,
> the two measured in the same units, **the second two-sided and uniform in the time**."

"Two-sided" and "uniform in the time" now attach to Thm. 1.10 alone; "unconditional" and the
`4.8188…` ratio to both, which is what `briefs/v3r3-inselmann-horizon-findings.md` §§1.3, 1.5 support.
The citation is left merged, as the endorsed text has it; what was restored is the split of the
*adjectives*, which is where the round's error was.

### D2 — the agent of "given mass 0". FIXED.

`paper` L275. `by $\pi^{(L)}_{k,D}$` restored; the paragraph is now word-for-word the `29ecb1b`
sentence. The target law gives `†` mass `0`; the empirical distribution does not, and the budget
clause's whole content is that `†`'s empirical *frequency* vanishes (L323–324, unchanged).

### D3 — four sites disagreeing on the calibration limits. FIXED, separate commit `0a32136`.

The paper is the most conservative document and was not touched. The three body sentences and the two
pointer pages were brought up to `aeh.md`'s front matter:

| site | now reads |
|---|---|
| `aeh.md` L8 (*Current state*) | "No residual discrepancy … within three limits …: block lengths `L ≤ 2`, pooled adjudicating runs (a consequence of 13.2.1, not its per-start form), and an altitude guard on the core that binds at finite size (13.5)." |
| `aeh.md` L151 (§13.5 *Status: resolved*) | the same three, spelled out, keeping its `13.6.4`(q1) pointer and adding `13.4` for the guard |
| `README.md` L40 | the same three |
| `bridge.md` L71 | points at `aeh.md` 13.5 instead of restating, per `AGENTS.md` L16 |

"Unqualified" goes with them: it survives nowhere as a calibration claim (`git grep` on tracked pages:
0 hits in that sense). The word remains at `aeh.md` L214 — "the identification with `13.6.3`(v)'s law
is exact and unqualified" — which is about a *proved identification*, not the campaign, and is
untouched. A **repo-wide sweep of tracked files** confirms the four sites verify named were the only
calibration restatements; no fifth page carries one.

No status changed, so no ledger or `open-problems.md` entry was due (`AGENTS.md` L24 governs status
changes; this was the L42 periodic-status-pass bug). `updated:` was already `2026-08-03`.

### D4 — "the exact window chain". FIXED, minimally.

`paper` L435: "transfer-operator analysis of **the chain of exact depth-`$k$` windows
(Theorem~`\ref{thm:onestep}`)**". Theorem 3.8 is where the paper defines *depth-`k` window*, so the
object is now one the paper names. Nothing was rewritten into a claim about a stationary law, per the
design pass's standing warning.

### D5 — the retired-route pointer. FIXED, after checking `cycles.md`.

Checked in the file, not recalled: `12.8.6.3` (L364–366) is the *profile-plus-correction recipe*; the
continued-fraction/semiconvergent route is at **`12.8.6.1`, *Superseded formulation*** (L329). The v2
note named both halves, so `paper` L231 now reads "at `\S12.8.6.1` and `\S12.8.6.3` there". The
release-description half of that sentence is D12 and was **not** touched. `cycles.md` has no commits
since `9d9d1ec` (`git log 9d9d1ec..HEAD -- cycles.md` empty), so the in-text URL is still current.

### D6 — "a stronger density notion". FIXED with a pointer.

`paper` L384: "…in step time and by a stronger density notion rather than a sharper count
**(`\texttt{aeh.md}` `\S13.3.2`)**." The `*`-density sentence is present at `13.3.2` in the pinned
tree (checked with `git show`), so the claim about a third party's technique now has an address like
every other wiki-backed claim in §5.

### D7 — Thm 1.6's content. FIXED with a half-clause, not a restoration.

`paper` L405: "His `\cite[Thm.~1.6]{inselmann}`, **a density statement about odd steps**, is what
carries his own passage from `$T$`-time to Syracuse time…". That is the minimum that makes the
following negative claim readable: a *one-letter* density against the *two-letter* statistic the
passage to block time needs. It matches `aeh.md` §13.3.2 ("Thm `1.6` bounds the density of the
one-letter pattern `1` and gives nothing about `10`") and the pre-prune paper's "odd steps occupy half
the schedule". Five words; the cut sentence was not reinstated.

### D8 — *bottom regime* introduced after use. FIXED by moving the gloss, at net zero words.

First use (`paper` L299, PDF p. 11) now carries the emphasis **and** the gloss: "far above the
`\emph{bottom regime}` of `\texttt{aeh.md}` \S13.1, **the fixed drainage basin of small integers**."
Second use (Calibration, L425, p. 13) drops the emphasis and the same seven words, keeping its
calibration-specific content ("where deviations reach `$z=41$` but reflect particular numbers rather
than a measure").

### D9 — the sentence said twice on p. 9. FIXED by the trim verify proposed.

`paper` L225 now ends "…by the witnesses exhibited above. The status paragraph below states what was
proved, where, and at what scope." The claim itself is made once, four lines below, in the paragraph
whose job it is.

### D10 — the `P(s=j)=2^{-j}` justification. NOT RESTORED, deliberately. Reason:

The cut parenthetical ("four of eight classes give `$s=1$`, two give `$s=2$`, and the lifting shells
are geometric") is a **derivation aid, not a scope word** — the class-by-class content is printed in
full in Theorem 3.3 (`thm:vlaw`) on p. 5, which lists exactly those four `$s=1$` classes and two
`$s=2$` classes and gives `$s = 2 + v_2(d-M(\w)) \ge 3$` on the lifting classes. Nothing the reader
needs is missing, and the surviving sentence states the marginal exactly, with its cap and tail cell.
Restoring it would re-expand the paper against the brief. The finding that stands is the **ledger
one**: C17's "no content removed, wording only" label was wrong for this item, and this file records
it so the round's own cut list is complete.

### D11 — the lost blank line. FIXED.

Blank line restored between the version note and `\subsection*{Author's note}`. Rendering is unchanged
(p. 2 verified), which is the point — it was source hygiene.

### D12 — NOT TOUCHED, as instructed.

Both sentences that point at the release description are exactly as the apply delegate left them,
including `paper` L231's "are in the release description", whose `\S`-pointer half is all that D5
changed. The release blocker and its two carry-forward consequences stand as verify recorded them.

---

## 2. The compression-casualty sweep

Method: every hunk of `git diff 29ecb1b..0e50afb -- paper/collatz-reduced-v3.tex` was classified as a
**deletion** or a **condensation**, and every condensation was read against its pre-prune original
clause by clause, asking only "which words carried scope, and are they still here?". Sixteen hunks;
eleven of them condensations. Result: **one new casualty, three near-misses cleared, the rest clean.**

### NEW — the one-limit paragraph lost the restriction to convergent orbits. FIXED.

`paper` L287–289 (PDF p. 11). At `29ecb1b`:

> "That is forced. **Along a fixed orbit no limiting procedure survives:** the unrestricted empirical
> distribution is false **on every convergent orbit**, whose tail sits at `$(1,1)$` forever; …"

as the round left it:

> "That is forced: along a fixed orbit **the unrestricted empirical distribution is false**, every
> convergent tail sitting at `$(1,1)$` forever, …"

The main clause became a universal statement about *every* fixed orbit, with its restriction demoted
to a participial absolute — exactly the D2 failure mode. It is not established for a divergent orbit
or a hypothetical nontrivial cycle, and `aeh.md` `13.2.1` ("No single-orbit form is available: above a
fixed cut **a convergent orbit** supplies finitely many qualifying visits…") argues it only for
convergent orbits, as the pre-prune paper did. **Repaired at net zero words**: "along a fixed
**convergent** orbit the unrestricted empirical distribution is false, **the** tail sitting at
`$(1,1)$` forever, while above a fixed cut **such an orbit** supplies only finitely many qualifying
visits…". Reported here rather than fixed silently, per the brief.

### Cleared after checking — three that read like casualties and are not

* **Abstract, "on the lifting classes"** replaced "whenever `$3^d\w \equiv 1 \pmod 8$`". Exactly
  equivalent, and *lifting* is defined at Theorem 3.3 — but the abstract now uses a term of art it
  does not define. Not a scope loss; **not fixed** (the abstract is protected territory for length,
  and the substitution is faithful).
* **"exact only away from the start"** (was "away from the segment's start"). The sentence opens "A
  sampled segment has no infinite past at its first block", so the referent is fixed by its own
  clause; and the segment does begin at the start. No loss.
* **"`\S13.5`'s standing rule"** lost its gloss ("fixed horizon, unweighted, per-visit sampling from
  uniform starts") — but unlike D6 it kept its **pointer**, and the rule is stated at `aeh.md` 13.5.
  Pointing rather than restating is the wiki's own rule. No repair.

### Checked and intact

The "past that range" passage (every clause preserved — vanishing `†` frequency, "not a bound on a sum
over its complement", full-weight budget-exhaustion block, unbounded letter, uncontrolled `o(T_N)`
tail, `→ 4` denial); the base-case tail (the Chernoff derivation went, the *rate* and the *vanishing
point* stayed, with `aeh.md` §13.2 supplied); the clock paragraph (the `4.8188…` factor and its
unit-independence survive at L328–333 and L400–406); Remark 3.6 (endorsed); the §5 opening; the
Calibration paragraph (which the round made *weaker*, correctly); the intro roadmap; the status
paragraph.

### One item reported, not fixed — the status paragraph's borrowed vocabulary

`paper` L231 says "below **the target arc's** length, so any 66 consecutive integers contain an
**admissible exponent** `$n$`". Neither term is defined in the paper; the pre-prune correction note
defined both inline (`⌈nL⌉ - nL ∈ [0.0415, 0.1169390665…]`). This reads as D4's class, but it is
materially different and is left alone: the whole paragraph is explicitly a *report of a result proved
elsewhere and not reproduced here*, and it carries its address (`cycles.md` §12.8.6, with the URL) in
the same sentence group. Defining the arc would re-expand a paragraph that exists to be short. Flagged
so a later pass can decide otherwise.

---

## 3. The six-claim sweep, re-run after editing

| # | prohibited claim | verdict | evidence, on the edited source |
|---|---|---|---|
| 1 | AEH supplies the mean exponent past the digit budget | **ABSENT** | `E_B[m+r]` at L310 (definition of *consistent*), L316 ("under `$B$` a block spends"), L375 (the clock, with "a conversion available here precisely because the word is exactly `$B$` here" in the same sentence). The denial is intact at L327: "`$T_N^{-1}\sum(m_n+r_n)\to4$` **does not follow there and can fail by any amount**", closed at L333 "not a consequence of the hypothesis above it". Untouched by this pass. |
| 2 | AEH converts a horizon into blocks per bit | **ABSENT** | one occurrence of "blocks per bit", L374, the clock's, with its scoping clause attached. The three surviving carriers of the block-time correction (Related work L58; the ledger paragraph, which this pass edited *around* the correction without touching it; the horizon paragraph L328–333) all still say the division is a theorem inside the budget and neither a theorem nor a consequence past it. |
| 3 | the finite bound is about a word beginning at the sampled start | **ABSENT** | the R5 passage is **byte-identical to `29ecb1b`** (393 chars, checked), as is the `gathered` display (270 chars, `$S_{n+1}$` on both lines). |
| 4 | bulk uniformity stands unqualified | **ABSENT** | `grep -c -i unqualified` on the `.tex` = **0**. And now absent from `aeh.md`, `README.md` and `bridge.md` as a calibration claim too (D3). |
| 5 | `13.6.4`'s union mass is exact | **ABSENT** | `13.6.4` occurs once, L278, as "a deterministic dictionary between letters and labelled window blocks". The only "union" left, L396–398, says the union over all scales **is not controlled**. |
| 6 | any conditional drift consequence | **ABSENT** | both denials present and unedited: L240 "no drift or contraction statement about orbits follows from it"; L400 "The descent consequence is **not stated here**". The D1 repair rewrote the *attribution* that follows that denial, not the denial. |

---

## 4. What must not have moved — re-verified against `29ecb1b`

Method: `\begin{env}…\end{env}` blocks matched by `\label` and compared **byte for byte** across
`29ecb1b`, `0e50afb` and the pinned `f9b07b1`/`eb3f4c4`.

* **23 environments before, 23 after.** Against `29ecb1b` the only differing block is **`rem:verify1`**
  (Remark 3.6, `1072 → 722` chars) — the endorsed narrowing, untouched by this pass. Against
  `0e50afb`, **every** environment is byte-identical: this pass changed no numbered environment at all.
* **Counts unchanged**: theorem 8, proposition 2, lemma 4, corollary 1, definition 2, hypothesis 1,
  heuristic 1, remark 3. **Nothing renumbered.**
* Byte-identical to `29ecb1b`: the round-5 `gathered` display (270), Hypothesis 5.1 (1616), the
  two-sided law with its `13.6.3`(iii)/`13.6.5` and `Remark 1.13, footnote 4 of arXiv v7` locators
  (603), the `W_{k,D}` display, "product names exactly two clauses" (370), the base-case statement
  (222), the R5 shifted-word passage (393), Theorem 4.4's proof outline (1049), **Related work and
  provenance** (4549), **the author's prefatory note** (1147), **the responsibility and verification
  protocol** (1287, pin normalised).

---

## 5. Build

Rebuilt from clean (`.aux`, `.log`, `.out` deleted), three `pdflatex -halt-on-error
-interaction=nonstopmode` passes, then rebuilt again after the pin edit.

| | result |
|---|---|
| passes | 3, exit `0` each, converged (`rerunfilecheck`: `.out` has not changed) |
| **page count** | **15** — unchanged; the six words D1/D7/D8 add and the sentence D9 removes cancel to within one line |
| overfull boxes | **0** |
| underfull boxes | 1 — `Underfull \hbox (badness 1067) … lines 462--463`, the `\bibitem{lagarias}` entry, page 15. Pre-existing, recorded before the round |
| `LaTeX Warning` | **0 of any kind** |
| undefined references / citations | **0**; 18 `\cite` keys against 18 `\bibitem`, none uncited, none missing |
| layout | pages 2, 9, 11–15 rendered at 110 dpi and inspected: no stranded heading, no split display, no widow. The p. 14/15 break moved by one bibliography entry (References now heads p. 14 with three entries under it); Lemma 5.2, the `gathered` display and all of §6/Appendix A remain whole on their pages |
| encoding | `aeh.md`, `README.md`, `bridge.md`, the `.tex`: UTF-8, no BOM, no `U+FFFD`, no mojibake |

---

## 6. The pin `f9b07b1` — verified with `git show`, never the working tree

The pin names the **paper commit**, whose tree contains both this round's wiki edits (via its parent
`0a32136`) and the repaired paper. The pin itself lands in the child commit `eb3f4c4`, the same
chicken-and-egg pattern as `6a9183a → c2d465a` and `881c92e` before it.

**Positive.** Extracted from the *pinned* paper, not from a list: **21 section pointers, 3 numbered
wiki objects, 10 files**. All 24 wiki anchors are *defined* at the pin by heading or bolded statement —
`stage3.md` 11.8.6.3; `cycles.md` 12.2.3, 12.5.2, 12.5.3, 12.6.1, 12.6.2, 12.7.4, 12.7.5, 12.8.6,
**12.8.6.1** (new this pass), 12.8.6.3; `aeh.md` 13.1, 13.2, 13.2.3, 13.2.4, 13.2.5, 13.3.2, 13.4,
13.5, 13.6.3, 13.6.4, 13.6.5, 13.6.6; `itinerary.md` 14.15.1.5 — and all six `experiments/*.py` plus
the four pages exist at the pin. A deliberately bogus anchor (`13.99.99`) is not found, so the search
is not matching everything. Every repair of this pass is inside the pinned tree (D1, D2, D4, D5, D6,
D7 probes all hit), as are the `*`-density sentence and the three-limit lines in `aeh.md`, `README.md`
and `bridge.md`.

**Negative.** At the superseded pin `881c92e`: the `aeh.md` 13.5 three-limit sentence — **0**; the
`UNQUALIFIED` sentence — **1**; `README` three limits — **0**; `README` unqualified — **1**;
`bridge.md`'s pointer form — **0**; the paper's split Inselmann attribution — **0**; the
`\S12.8.6.1 and \S12.8.6.3` pointer — **0**. The old pin could not have supported the repaired paper,
which is why the bump was necessary.

---

## 7. Found and not fixed

1. **The status paragraph's "target arc" / "admissible exponent"** (§2 above) — reported, left short by
   design, with its record address in the same sentence group.
2. **The abstract's "lifting classes"** — faithful but term-before-definition.
3. **D10's parenthetical** — not restored; reasoned above.
4. **`\label{prop:elim}` has no `\ref`** — five other labels are likewise unreferenced (`cor:size`,
   `lem:ceiling`, `lem:routing`, `rem:verify1`, `thm:smallp`); harmless, all six numbered and stated.
5. **Pre-existing, unchanged**: "door-letter alphabet" (L240) and "the door" (L431) are never defined
   in the paper; `$\pi_{k,D}$` is used in §1 and Related work before its §5 definition; `stage3.md`
   calls Remark 3.6's branch *resonant* where the paper calls it *boundary*; Theorem 3.7 and §5 both
   say flatly "`$a_+$` is a `$3$`-adic function of `$\w$`" three lines under the newly narrowed
   Remark 3.6.
6. **D12 and the release blocker** — untouched, and unresolved: v3 cannot be released until the
   release description exists, and the v2-era pin `72ec88e` with the six itemised repairs lives
   nowhere in the repository.

## 8. What I did not check

The primary sources (D1's verdict still rests entirely on `briefs/v3r3-inselmann-horizon-findings.md`,
and D7's phrasing on that brief plus `aeh.md` 13.3.2); the mathematics of `cycles.md` §12.8.6 beyond
locating `12.8.6.1`'s *Superseded formulation* and reading what it says; `aeh.md`'s own proofs; the
network (Zenodo DOIs, GitHub URLs, whether a v3 release description exists anywhere). No script in
`experiments/` was run. `open-problems.md` 11.12, the indexing standardization and the deferred prefix
result were not attempted, per the brief.
