# Findings: applying round 3 to the paper (v3 round 3, Wave 3, paper delegate)

**Task:** `briefs/v3r3-paper-apply-brief.md`. Edit round, not a design round.
**Branch:** `v3r3-review-round3`, base `b278e5a` (the record delegate's last commit). One commit landed.
No push, no merge, no rebase, no worktree, no branch switch. **Only `paper/` was touched.**
**Applied in order A → B → C → D**, later superseding earlier where the findings say so
(`briefs/v3r3-cut-weighting-findings.md` §9, `briefs/v3r3-basecase-density-findings.md` §6.2), with the
**landed record winning every disagreement** (§3 below).

Line numbers in the table are **pre-edit**, i.e. against `HEAD:paper/collatz-reduced-v3.tex` at `b278e5a`.

---

## 1. Site-by-site

| Pre-edit line | Whose text | Deviation, and why |
|---|---|---|
| L38 abstract | — | **No drop-in exists.** "a precise conjecture about an exactly computable product law" is the misreading A §11 says the round exists to remove, and after A §7.1 the paper states in terms that "product" names two clauses of `π_{k,D}` and no others. Restated as the letter-genericity conjecture, with the base case named. See §5 item 1. |
| L42 version note | — | Rewritten to describe the paper **as it now stands** (v3 unpublished, so no erratum framing). v1/v2 text and both DOIs kept verbatim; the v3 DOI now reads "Zenodo DOI (reserved)" and the v3 sentence opens "drafted; … not yet published". "makes eight repairs" dropped (the count would now be wrong); the repair list keeps the five that still describe the paper and hands the `π_k`/hypothesis items to a new §5 description. §5 item 2. |
| L56 Introduction | A §7.4 token substitution | `π_k → π_{k,D}` (×2); "an explicitly computable product law" → "the block letters of typical orbits --- equivalently … an explicitly computable window law `π_{k,D}`". Same reason as L38. |
| L59 Related work | B §1.5, §2.2, §3 (S3) | **No drop-in exists for this site**; the brief names it. Inselmann's Thm 1.10 horizon `(log₂ 4/3)^{-1} log₂ m` now carries its unit ("Syracuse steps, the full descent horizon in that unit"), and one sentence added: all of the cited horizons are counted in steps, and their reading in reduced blocks divides by a mean that is itself part of `hyp:aeh`. `π_k → π_{k,D}`. |
| L160 `thm:onestep` | — | **Referent rename only**, forced: the theorem closed on "under the product law of Section~\ref{sec:aeh}", and §5 no longer names any object "the product law". Now "under the law $\pi_{k,D}$ of Section~\ref{sec:aeh}". The claim is byte-identical otherwise (§4). |
| L149–157 `thm:deltaM` | — | **Untouched**, per A §3.7 and A §9 item 18. |
| L241 `\pi_k` paragraph | **A §7.1**, verbatim | **+ one clause** paying B §6.3's footnote-4 attribution (§5 item 3); **+ four record-driven touches** in the paragraph's tail, which A's §7.1 does not reach: `π_k → π_{k,D}` throughout, `P(s=j) = 2^{-j}` gained "at every $j < D$" and the `1/3` rate gained the cap's tail cell (A §9 items 1–2, as the landed `13.3.1`/`13.3.2` print them), "at each fixed $k$" → "at each fixed $(k,D)$", and the class-skeleton sentence rewritten to refer back to A's example rather than restate it (§5 item 4). |
| L243–257 `hypothesis` | **C §8.7** (supersedes A §7.2's environment) | Re-lettered to the record: C's `L = ⌊log₂ N⌋` → `b`, C's `ℓ` for word length → `L` (§3 item D4). **+ two clauses**: `w_i = (m_i, r_i)` defined (§5 item 5) and "in the sense defined below" on *admissible* (§5 item 6). |
| after the environment | **A §7.2**'s second paragraph + C §8.7's two substitutions | "over the same bulk blocks" → "over the same tallied blocks, with $\dagger$ carried through and given mass $0$ by $\pi^{(L)}_{k,D}$"; `T → T_N`, `O(1/T) → O(1/T_N)`. |
| L259–265 | — | **Verbatim.** The one-limit paragraph down to "…in whichever order it is taken." |
| L265–277 | **C §8.8** (supersedes B §5.4) | Cut point moved: C §9 item 17 says "L259–270 survives verbatim", but the surviving sentence ("The bulk cut survives with a smaller and different job…") contradicts C §8.8's own opening. The landed `aeh.md` L56 deletes exactly that sentence. Record wins; the bottom-regime gloss it carried is folded into C §8.8's text so nothing is lost. §3 item D3. |
| L279–299 base case | **D §5.4** (which reproduces B §5.5 at its tail and supersedes C §8.9) | **+ D §6.2 item 12's own amendment** ("equivalently, for every admissible $(\tau,\theta)$ with $\tau < 1$"). `$O(N^{-D})$` re-lettered to `$O(N^{-\delta})$` — `D` is now A's cap (§3 item D5). "the product law still describes the orbit" → "the law still describes the orbit". |
| L301–304 ledger + density | **D §5.5** (the merged block: A §7.3 + the shell repair) | **+ C §8.10's clause**: D's "along their first `⌈θ log₂ x⌉` bulk blocks" → "along their first $T_N$ blocks, all of them within the budget", matching the landed `13.3.1`. §3 item D2. `⌈θ log₂ N⌉` written as `T_N`, the symbol the hypothesis defines (§3 item D9). |
| L307–313 Inselmann descent | **B §5.6**, verbatim | — |
| L313–324 what AEH supplies | — | **No drop-in**; the brief names the site. "the full $2^{-j}$ marginal at every $j$" → "at every $j$ below the cap" (A §9 items 1–2); "a density-zero set of *starting values*" → "a set of *starting values* of vanishing density", so the sentence does not re-assert per-scale what D §5.5 has just restricted to shell scale two sentences earlier. §5 item 7. |
| L326 Calibration opening | A §7.4 token substitution | `π_k`-uniformity → `π_{k,D}`-uniformity. |
| L332 Calibration close | A §4.4 item 3 + C §1.2/§8.6, as the landed `13.5` and `13.4` print them | "Bulk uniformity stands unqualified at all tested depths." replaced by what the campaign tested: unqualified at every tested depth and cell, **within two ceilings** — block lengths `L = 1` and `L = 2` and no longer pattern (landed `13.5` "Status: resolved"), and the pooled-versus-per-start scope, the adjudicating runs measuring the across-orbit average of the per-start frequencies rather than the per-start statement, whose test (`‖ν − π_{k,D}‖_TV` across orbits) no run reports (landed `13.4`). |
| L339 Appendix A pin | — | `c2d465a` → **`b278e5a`**. See §6. |

**Not edited, deliberately:** `paper/collatz-reduced-v2.tex`, `collatz-reduced-v2.pdf`,
`collatz-mirror-v1.*`, `collatz-reduced-v2-review.md`. The title block's DOI line (L27) is left as it
stands — the brief says keep the DOIs, and the "reserved" qualification belongs in the version note.

---

## 2. Build report

Three `pdflatex -halt-on-error -interaction=nonstopmode` passes, MiKTeX, run before and after.

| | before (`b278e5a`) | after |
|---|---|---|
| pass 1 / 2 / 3 | exit `0` / `0` / `0` | exit `0` / `0` / `0` |
| **pages** | **15** | **17** |
| overfull boxes | `0` | `0` |
| underfull boxes | `1` | `1` |
| undefined references / citations | `0` | `0` |
| `LaTeX Warning` lines | `0` | `0` |

The single underfull `\hbox` (badness `1067`) is the **pre-existing** one in the `rhin` bibliography
entry — `collatz-reduced-v3.log` L392, at tex lines `363--364` before and `470--471` after. Same box,
same badness, moved only by the line-number shift.

**One overfull box was introduced and removed.** The first build after D §5.4 landed gave
`Overfull \hbox (4.43764pt too wide) detected at line 345` — the two-part display carrying the TV bound
and the binomial tail identity. Fixed by tightening the display's internal spacing (`\qquad → \quad`,
and one `\;=\;` → `=` in the second half). No symbol, number or claim changed. Re-verified: `0` overfull
after.

### Page-count delta: `+2`, and where it went

Measured from the extracted text of the committed PDF against the extracted text of `HEAD`'s PDF
(`pdftotext`, characters per block):

| block | before | after | delta |
|---|---:|---:|---:|
| Version note | `3,118` | `4,630` | **`+1,512`** |
| Author's note | `1,104` | `1,100` | `−4` |
| §1 Introduction | `3,391` | `3,459` | `+68` |
| Related work and provenance | `3,829` | `4,102` | `+273` |
| §2 The reduced system | `2,500` | `2,506` | `+6` |
| §3 Anchor dynamics | `7,787` | `7,782` | `−5` |
| §4 Cycles | `10,081` | `10,078` | `−3` |
| **§5 The equidistribution hypothesis** | `9,499` | `17,243` | **`+7,744`** |
| §6 Discussion | `818` | `818` | `0` |
| Appendix A | `3,997` | `3,997` | `0` |
| **total** | `46,124` | `55,715` | **`+9,591`** |

**All of the `+2` pages are inside §5.** §4 begins on page `8` and §5 on page `11` in *both* PDFs;
§6 moves from page `13` to page `15` and Appendix A from `14` to `16`. §5 is `1.8 ×` its former length —
the round replaced almost every paragraph of it and added the base case's display, the admissibility
definition and the two calibration ceilings. The version note's `+1,512` characters and Related work's
`+273` are absorbed by reflow before §4 and cost nothing in pages.

No content was cut to reach a target; the author set no reduction mandate.

### PDF-text verification

`pdftotext` on the committed PDF, `30` distinctive strings from this round's new passages checked in the
extracted text: **`30 / 30` present**, including the capped window and its cap-the-labels clause, the
"not the window of Theorem 3.8" separation, the two-sided `B̂` clause and its footnote-4 cite, the budget
rate / block horizon rate / exponent spent / cemetery symbol, "is instead predictable", "admissible means
both", the `Bin(J−1,½)` tail, the Chernoff-tilt clause, "at every block length", `Lemma 13.2.4`,
`Proposition 13.2.5`, the dyadic-shell sentence, "triangular array", the two-letter-statistic sentence,
"Syracuse steps", "block lengths L = 1 and L = 2", the pooled-versus-per-start ceiling, `b278e5a`,
"Zenodo DOI (reserved)" and "No numbered theorem". Six retired strings checked **absent**:
`unqualified at all tested depths`, `c2d465a`, `bulk visits`, `bulk blocks`, `product law`,
`qualifying visit counted once`.

The source is ASCII throughout (checked: no byte outside `0x20–0x7E` plus tab/newline). Every edit was
made with the Edit/Write tools; no `Get-Content | Set-Content`, no PowerShell redirection.

---

## 3. Where the paper's drop-ins and the landed record disagreed

The record won every one. None of these was fixed by editing a wiki page; nothing outside `paper/`
was touched.

**D1 — the brief's G3 is stale, and the fix already landed.** The brief and
`briefs/v3r2-round-findings.md` G3 both say §5 "still ends its unconditional list with *and the classical
negative drift follows*" and that "No tex edit made". **It was made.** Commit `3213f0d` ("verify:
pointers moved to the ensemble form, and the drift clause aligned"), merged into `main` at `dc61306`,
replaced that clause with "the classical negative drift is a property of `π_k` --- but only of `π_k`:
window equidistribution at each fixed `k` does not control the means of the unbounded `m_+` and `s`, so
no drift or contraction statement about orbits follows from it (`aeh.md` §13.3.2)", which is exactly what
G3 recommended and exactly what the landed `13.3.2` says. **Nothing was left to fix.** I applied only the
round-3 token substitutions (`π_k → π_{k,D}`, "each fixed `k`" → "each fixed `(k,D)`"). Reported rather
than re-fixed, per the brief's own rule.

**D2 — D §5.5 reproduces "bulk blocks", which C §8.10 and the record retire.** D §5.5 is the merged
block the brief names, and it writes "along their first `⌈θ log₂ N⌉` **bulk** blocks". C §8.10 amends
exactly that clause of A §7.3 to "blocks, all of them within the budget", and the landed `aeh.md`
`13.3.1` reads "along their first `⌈θ log₂ N⌉` blocks, all of them within budget". **Record wins**;
C's clause applied inside D's block. Independent reason: after C §8.7 the paper's hypothesis has no
bulk cut, so "bulk blocks" would name nothing.

**D3 — C §9 item 17's line accounting contradicts C §8.8's own text.** §9 says "`paper` L259–270
survives verbatim"; the sentence at L265–270 is "The bulk cut survives with a smaller and different job:
it excises the bottom regime … for those sampled orbits that reach it inside the horizon", and C §8.8's
replacement opens "The horizon does the job a bulk cut would do, and does it without one." Both cannot
stand. The landed `aeh.md` L56 deletes the first and prints the second. **Record wins**: the replacement
starts at "The bulk cut survives…", and C §8.8's text was given the bottom-regime gloss the deleted
sentence carried, so no content is lost.

**D4 — C's letters collide with A's and D's.** C §8.7 writes `L = ⌊log₂ N⌋` (bit scale), `ℓ` for word
length, `π^{(ℓ)}_{k,D}`. D §1 and the landed record fix **`b`** = bit scale, **`L`** = block/word length,
**`ℓ_n`** = the letter; A §7.2 already used `L` for word length. **Record wins**, applied throughout the
hypothesis and its window paragraph. Nothing mathematical moves. (This is the same substitution the
record delegate reports at its §1 and §5 item 6.)

**D5 — `D` is used for two things.** B §5.5, reproduced inside D §5.4, glosses `*`-density as "every
initial segment carries all but `O(N^{-D})` of its mass". `D` is A's window cap in this section.
Re-lettered to `O(N^{-δ})` "for some `δ > 0`", which is Inselmann's Definition 2.6 as B transcribes it
(`0 < D ≤ 1`, existentially quantified in "`*`-dense"). No claim moves.

**D6 — `thm:onestep`'s "the product law of Section 5" loses its referent.** A §7.1 makes §5 say that
"product" names two clauses of `π_{k,D}` and no others, so no object in §5 is called "the product law"
any more. Renamed in place to "the law `π_{k,D}` of Section~\ref{sec:aeh}". Claim untouched (§4).

**D7 — `r_i` is never defined in the paper.** A §7.2 and C §8.7 both write `B[w] = Π 2^{-(m_i + r_i)}`;
`aeh.md` has the letter `(m, r)` from `13.6.1`, the paper does not. Added "writing `w_i = (m_i, r_i)` for
the components of the `i`-th letter of `w`".

**D8 — "admissible" is used three paragraphs before it is defined.** `aeh.md` `13.2.1` forward-points
("in the sense of `13.2.3`"); C §8.7's paper version does not. Added "in the sense defined below".

**D9 — two spellings of the tally denominator.** The hypothesis defines `T_N = ⌈θb⌉` with
`b = ⌊log₂ N⌋`; C §8.8 and D §5.5 then write `⌈θ log₂ N⌉`. The record carries both spellings
(`13.2.1` has `⌈θb⌉`, the L32 paragraph and `13.3.1` have `⌈θ log₂ N⌉`); in a single paper that reads as
a redefinition. Both sites now write `T_N`, the symbol the hypothesis defines. Nothing moves.

**D10 — A §7.1's closing parenthetical duplicates a sentence already in L241.** A's new sentence ends
"(e.g.\ from `(ω ≡ 1 (8), d odd)` the next depth is exactly `1`)", and the class-skeleton sentence two
later opened with the same example. A's drop-in kept verbatim; the later sentence now refers back
("the transition from `(ω ≡ 1 (8), d odd)` cited above holds because `m_+ = 1` and `a_+ = 0` there")
instead of restating it. Both facts survive; the repetition does not.

**Everything else agreed.** The paper's `hyp:aeh`, its consequences, its base case, its Inselmann
paragraph and its calibration paragraph now read the same as `aeh.md` `13.2.1`, `13.2.2`, `13.2.3`,
`13.2.4`, `13.2.5`, `13.3.1`, `13.3.2`, `13.4` and `13.5`, clause by clause, at the level of what is
asserted.

---

## 4. No numbered theorem's claim changed — what I checked

1. **Every numbered environment extracted and compared, old against new.** Script:
   `scratchpad/envdiff.py`, over `theorem`, `proposition`, `lemma`, `corollary`, `definition`,
   `hypothesis`, `heuristic`, `remark`, matched on `\label`, whitespace-normalised.
   **`22` environments before, `22` after, same labels in the same order** — nothing added, removed,
   renamed or reordered.
2. **`20` of the `22` are byte-identical:** `def:reduced`, `prop:block`, `thm:equiv`, the unlabelled
   anchor definition, `lem:squaring`, `thm:vlaw`, `lem:absorption`, `thm:depth`, `rem:verify1`,
   **`thm:deltaM`**, `prop:budget`, the unlabelled Heuristic-adjacent remark, `prop:elim`, `cor:size`,
   `lem:ceiling`, `thm:smallp`, `thm:uniform`, **`thm:staircase`**, `rem:staircase`, `lem:routing`.
3. **`thm:onestep` differs in one phrase and nothing else**, verified by direct diff of the environment:
   "under the product law of Section~\ref{sec:aeh}" → "under the law $\pi_{k,D}$ of
   Section~\ref{sec:aeh}". The depth-`k` window's definition (residues of `thm:deltaM` **together with**
   the stratum labels `(s, σ, a_+)`), the three outputs, the never-errs clause and the
   `≈ 2^{-(k+1)}` undecided rate are character-for-character unchanged. This is a rename of the referent
   forced by D6, not a change of claim.
4. **`hyp:aeh` is restated** — the one environment the round is authorised to move, by the author's
   decision (A Option 1a, C §8.7). It is a hypothesis, not a theorem.
5. **Printed numbers compared in the built PDFs.** The set of `Theorem/Lemma/Proposition/Corollary/
   Definition/Hypothesis/Heuristic/Remark N.M` strings is identical before and after, except for three
   **external** pointers this round adds to `aeh.md` (`Lemma 13.2.4`, `Proposition 13.2.5`,
   `Theorem 13.6.4`). The paper's own numbering is unchanged end to end: Definition 2.1, Proposition 2.2,
   Theorem 2.3, Definition 3.1, Lemma 3.2, Theorem 3.3, Lemma 3.4, Theorem 3.5, Remark 3.6, Theorem 3.7,
   **Theorem 3.8**, Heuristic 3.9, Remark 3.10, Proposition 4.1, Corollary 4.2, Lemma 4.3, Theorem 4.4,
   Theorem 4.5, **Theorem 4.6**, Remark 4.7, **Hypothesis 5.1**, Lemma 5.2.
6. **Cross-reference integrity:** `0` undefined references and `0` undefined citations across three
   passes, so no `\ref` in the paper now points at a moved or missing label.
7. The version note's closing sentence — "No numbered theorem's claim is strengthened, weakened, or
   renumbered" — is therefore true of the paper as it now stands, and is kept.

---

## 5. Changes no delegate specified (every entry is a flag for review)

1. **The abstract's "an exactly computable product law" was replaced.** No delegate names the abstract.
   But A §11 is that "product law" is the misreading the round exists to remove, and A §7.1 makes §5 say
   so explicitly; leaving the abstract would have left the paper contradicting itself on its first page.
   Now: "a precise conjecture --- that the block letters of uniformly sampled large starts carry, at
   every finite block length, the frequencies of an exactly computable Bernoulli law --- … exhibit an
   unconditional base case inside the digit budget". The added base-case clause is the one substantive
   addition; it reports what §5 now states and `aeh.md` `13.2.4` proves.
2. **The version note is mine.** The brief prescribes the *task* (describe the paper as it now stands,
   not an erratum, keep v2 material and the DOIs, the v3 DOI reserved) and no delegate supplies text.
   v1 and v2 sentences and both DOIs are verbatim. The v3 sentences now describe: the Section-5 repair
   as a whole (one object; the capped window; `π_{k,D}` on the two-sided measure; "product" naming two
   clauses; the hypothesis in letter coordinates at every finite block length with both weaker readings
   retired; total variation named; the bulk cut replaced by an exponent budget with admissibility
   defined), the base case with its exact rate and horizon, the shell-scale density conclusion, the
   step-time reading of the cited horizons, and the two calibration ceilings. It is a description, not a
   change log: no "was X, now Y", no round numbers, no dates beyond the version dates.
3. **The footnote-4 attribution is paid in the paper.** B §6.3 says the attribution is owed *if* the
   two-sided construction is written up as "the law defined from an infinite past". A §7.1's paper text
   does exactly that. The record delegate paid it at `13.6.5` (its §1, `13.6.5` attribution row); I paid
   it at the paper's `\hat B` sentence, as `\cite[Remark~1.13, footnote~4]{tao}`. Same footnote, same
   reason.
4. **The class-skeleton sentence at L241 was rewritten to refer back.** D10 above.
5. **`w_i = (m_i, r_i)` defined.** D7 above.
6. **"in the sense defined below" on *admissible*.** D8 above.
7. **Two precision touches in the "what the hypothesis supplies" sentences (L313–324):** "the full
   `2^{-j}` marginal at every `j`" gained "below the cap" (A §9 items 1–2), and "a density-zero set of
   *starting values*" became "a set of *starting values* of vanishing density", so that the paragraph
   does not re-assert unrestricted density zero two sentences after D §5.5 has confined it to shell
   scale. The brief names L301–324 as one site; no drop-in covers these two clauses.
8. **§5's opening question.** "Why is a product law the right comparison object?" → "What is the right
   comparison object?" Same reason as item 1; the paragraph's own answer is unchanged.
9. **The display-spacing fix** that removed the overfull box (§2). No symbol or number moved.
10. **Appendix A's pin.** §6.

---

## 6. The Appendix A commit pin

Set to **`b278e5a`**, and I believe that is the honest pin. Reasons, in order:

* Appendix A's claim is "every wiki section and script named in this paper is cited at commit
  `\texttt{...}`". The sections this round newly names — `aeh.md` `13.2.3`, `13.2.4`, `13.2.5`, `13.6.4`
  — and the script `experiments/aeh_basecase.py` exist only from the record delegate's commits
  (`9d160d8`, `a1e1701`). `b278e5a` is the tip that contains all four record commits, so it is the
  earliest commit at which the claim is true of *this* text.
* `a1e1701` would also satisfy the `aeh.md` half but predates nothing needed and postdates
  `9d160d8`; `b278e5a` additionally contains `publication.md`'s round-3 state, which the paper does not
  cite but which the record's own front matter now depends on. Pinning the tip is the repository's
  established practice (`3511a0d`, `643e864`).
* **Caveat, stated plainly:** `b278e5a` does *not* contain this commit, which changes only `paper/`.
  The paper cites no `paper/` path, so the claim as worded remains true; but if the author wants the pin
  to be a commit that also contains the paper naming those sections, the pin has to be advanced after
  this commit lands, exactly as `3511a0d` and `643e864` did for earlier rounds. **I did not create that
  follow-up commit** — the brief authorises one commit's worth of paper edits, not a self-referential
  second pass, and A §12 item 8 records that this repository has already spent a round on the mechanic.

---

## 7. Asserted but not verified here

1. **Every number, section reference and cross-reference in the drop-ins was checked against the source
   or the landed record, not recalled** — the `aeh.md` anchors (`13.1`, `13.2.3`, `13.2.4`, `13.2.5`,
   `13.3.2`, `13.4`, `13.5`, `13.6.3`, `13.6.4`, `13.6.5`), the constants
   `(1 − log₂√3)^{-1} = 4.8188…`, `1/β = 1.2047…`, `β = 2(2 − log₂3) = 0.8301…`, `E_B[m+r] = 4`,
   `log₄3`, the alphabet bound `2^{k+1}D³(D+1)`, and Inselmann's Thm 1.6 / Thm 1.10 / Cor. 1.4 locators.
   All were read from the landed `aeh.md` or from B's and D's transcriptions in this round's findings
   files. **I did not re-read Inselmann or Tao**; B's page-by-page transcriptions are taken as read, as
   the record delegate also did.
2. **No experiment was re-run.** The calibration numbers printed in the paper (`0.2503 ± 0.0015`,
   `84,739` visits, `z = 41`, `1,600`–`2,600` orbits per cell) are untouched and were not re-derived.
3. **C's measured protocol gap is not in the paper.** The landed `13.4` records that the core cut binds
   (`4,191` of `158,580` visits, `15.5 %` of orbits) and that the two cut rules differ. No delegate
   assigns a paper site for it, and the paper's calibration paragraph asserts nothing about a cut not
   binding, so nothing in the paper is false. **Flagged:** a reader comparing the two will find the
   record more qualified than the paper on this one point.
4. **A's open questions 3 and 4** (the `2·(0.93)^j` bound under `B̂`; the composite five-coordinate
   labelled reconstruction as one test) are untouched, as they were by the record delegate. Neither is
   asserted in the paper.
5. **The `.aux`, `.log` and `.out` are gitignored** (`paper/.gitignore`) and were not committed; the
   `.tex` and the rebuilt `.pdf` were.
