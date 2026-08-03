# Findings: the pruning plan (v3 round 6, design)

**Round.** Design delegate for the fifth external review's pruning assessment. Base: `main` at
`29ecb1b`, `paper/collatz-reduced-v3.tex` (71,774 chars, 506 lines), PDF 18 pages.
**Read-only on every tracked file; this findings file is the only write.** No `git` write of any kind
was performed, no branch, no commit. All candidate builds were assembled and compiled in the session
scratchpad from an unmodified copy of the source.

**Headline.** The reviewer's plan is sound and every one of its five items is safe. Executed
faithfully it takes the paper from **18 pages to 16**. A second pass over the same material — the
abstract, the introduction's roadmap, `Remark 3.6`, and §5's discursive layer — takes it to **15**,
and that is the floor for content cuts that leave the corrections and the protected material intact.
**12–13 pages is reachable, but the last two to three pages come from the type size, not from
content**: the same 15-page manuscript sets to **13 pages at 10pt** and **12 pages at 10pt with 1in
margins**. All four numbers are measured, not estimated (§6).

---

## 1. The current page budget, measured

### 1.1 Method

Page-fraction estimates from character counts are unreliable here (displays, theorem environments,
`\small` abstract, inline fractions). Instead each passage boundary was measured directly:

* the source was truncated at the boundary and given a **zero-height marker**
  (`\par\nointerlineskip\vbox to 0pt{\vss\hbox{QQZZMARKQQ}}`), so the marker cannot itself displace
  material or force a page break;
* the file was compiled with `\nofiles` against a copy of the repository's own `.aux`, so every
  `\ref`, `\cite` and `\bibitem` number resolves exactly as in the full document and line breaking is
  unchanged;
* the marker's `(page, y)` was read from the PDF text matrix, and cumulative height taken as
  `(page-1)·633.6 + (712.8 - y)` pt — `633.6 pt = 8.8 in` is `\textheight` for
  `margin=1.1in` on US Letter, and `712.8 pt` is the text-block top (first baseline `701.8` plus
  `\topskip = 11 pt`).

Baseline sanity: the scratchpad rebuild of the untouched source reproduces **18 pages** and the
repository PDF's pagination exactly. The document is set `\raggedbottom` and carries no floats, so
accumulated page-break slack is near zero: total material measures **10,808.6 pt = 17.06 page
equivalents**, laid out in 18 pages with essentially all the slack (596 pt) on the near-empty final
bibliography page. **Consequence: physical pages ≈ ceil(material / 633.6).** That is what makes the
projections in §6 checkable.

Units below: `pt`, `lines` (at `\baselineskip = 13.6 pt`), `pages` (at 633.6 pt).

### 1.2 By section

| block | pt | lines | pages | span in PDF |
|---|---:|---:|---:|---|
| title block + `\maketitle` | 184.6 | 13.6 | 0.29 | p1 |
| Abstract | 360.8 | 26.5 | 0.57 | p1 |
| **Version note** | **684.5** | **50.3** | **1.08** | p1–p2 |
| Author's note | 220.3 | 16.2 | 0.35 | p3 |
| §1 Introduction | 586.8 | 43.1 | 0.93 | p3–p4 |
| Related work and provenance | 618.9 | 45.5 | 0.98 | p4–p5 |
| §2 The reduced system | 561.3 | 41.3 | 0.89 | p5 |
| §3 Anchor dynamics | 1588.3 | 116.8 | 2.51 | p6–p8 |
| §4 Cycles | 1896.6 | 139.5 | 2.99 | p8–p11 |
| **§5 AEH** | **3076.9** | **226.2** | **4.86** | p11–p16 |
| §6 Discussion | 165.0 | 12.1 | 0.26 | p16 |
| Appendix A | 220.3 | 16.2 | 0.35 | p16–p17 |
| Bibliography | 644.3 | 47.4 | 1.02 | p17–p18 |
| **total** | **10,808.6** | | **17.06** | |

### 1.3 Inside §4 and §5, at passage resolution

§4 (1896.6 pt):

| passage | pt | lines |
|---|---:|---:|
| Prop 4.1 (elimination identity) + proof | 263.3 | 19.4 |
| Cor 4.2 + Lemma 4.3 (ceiling) | 111.7 | 8.2 |
| Thm 4.4 (periods 1–3) + proof outline | 195.0 | 14.3 |
| Thm 4.5 (uniform trim) + proof | 326.9 | 24.0 |
| Thm 4.6 (staircase) | 118.0 | 8.7 |
| *Sharpness evidence and assessment* | 127.1 | 9.3 |
| Remark 4.7 | 63.2 | 4.6 |
| **Note added in v2 (July 2026)** | **311.7** | **22.9** |
| **(Correction, 2026-08-01.)** | **379.5** | **27.9** |

§5 (3076.9 pt):

| passage | pt | lines |
|---|---:|---:|
| opening paragraph (comparison object → "folklore ledger") | 724.9 | 53.3 |
| — null-model motivation | 153.0 | 11.2 |
| — Tao `Syrac(Z_3)` identification | 81.9 | 6.0 |
| — the `P(a_+ = ·)`, `P(d = ·)` values | 26.5 | 1.9 |
| — joint labelled law | 57.9 | 4.3 |
| — `W_{k,D}` display + alphabet + "not Thm 3.8's window" | 118.9 | 8.8 |
| — `π_{k,D}` + two-sided + Tao footnote 4 | 83.0 | 6.1 |
| — "product" scoping | 40.6 | 3.0 |
| — window-chain `~1%` caveat | 40.6 | 3.0 |
| — class skeleton | 28.1 | 2.1 |
| — `π_{k,D}` marginals (`2^{-j}`, `1/3`) | 39.0 | 2.9 |
| — drift denial | 41.3 | 3.0 |
| — folklore-ledger sentence | 14.1 | 1.0 |
| Hypothesis 5.1 | 212.5 | 15.6 |
| equivalence paragraph | 132.8 | 9.8 |
| "one limit" paragraph | 92.1 | 6.8 |
| horizon / budget / admissibility paragraph | 426.1 | 31.3 |
| base case paragraph (incl. `gathered` display 67.3) | 349.6 | 25.7 |
| "natural clock" paragraph | 271.0 | 19.9 |
| "AEH implies the ledger" paragraph | 459.9 | 33.8 |
| Calibration + Lemma 5.2 + ratio-estimator paragraph | 407.6 | 30.0 |

Two structural facts confirmed by measurement:

* **the last bibliography page is free.** The bibliography ends 596 pt into page 18's 633.6 pt, so
  any body reduction over ~40 pt removes page 18 outright.
* **the round-5 `gathered` display measures 67.3 pt** and is left byte-identical in every proposal
  below. It is not re-tightened, not re-flowed, and not moved.

---

## 2. The cut list

Notation: **[W]** = the passage is a summary of wiki text and survives there (source given);
**[P]** = paper-only, needs landing or must stay; **[D]** = duplicated inside the paper, one copy
kept. Savings are measured deltas from the baseline table unless marked *(est.)*.

### 2.1 Front matter

**C1. Version note → one short paragraph.** Save **~545 pt (0.86 pages)** — 684.5 → ~140.
**[W]/[D]** The version note *narrates* repairs; it asserts nothing the body does not already carry.
Every item it lists is realised in the text it describes: `\w > 0` in Definition 2.1;
`C(\w)(1+\log d)^2` in Theorem 3.3; the stratum labels in Theorem 3.8; `n_0(p)` in Theorem 4.5; the
`heuristic` environment on 3.9; `\sigma_j = s_j + m_{j+1}` and the `M_t`-vs-anchor note in
Proposition 4.1; the capped window, `\pi_{k,D}`, the ensemble hypothesis, the exponent budget, the
base case and its rate, the shell-scale density, the two attributions and the two campaign ceilings
in §5. **Nothing vanishes from the paper**; the narration moves to the release description (§5 of
this file supplies it as plain text). Drop-in at §3.1.

**C2. Abstract → shorter.** Save **~50 pt** — 360.8 → ~311. **[D]** with §1 (Contributions and the
roadmap carry the same six items with pointers). Drop-in at §3.2. The compression is deliberately
conservative: the exit-valuation law, the depth closure, and the *graded-residue* form of the
anchor-increment law are kept verbatim, because a shorter paraphrase I first drafted misstated
Theorem 3.7 (it is determined by graded residues of `(\w, d, a_+)`, **not** by the anchor
displacement). Recorded as a near-miss.

### 2.2 §1 and Related work

**C3. Introduction roadmap paragraph → compressed.** Save **~30 pt** *(est.; measured together with
C2 below the noise floor)*. **[D]** with `Contributions` (i)–(vi) and with §6 Discussion, which
states the same "one question, two costumes" framing. Drop-in at §3.3.

**C4. Related work — recommend against cutting.** See §7.1.

### 2.3 §3

**C5. Remark 3.6 (verification notes) → condensed.** Save **~60 pt** *(est.)* — 143 → ~80.
**[W]** `stage3.md` §11.8.6.3 (already the paper's own pointer) carries every count verbatim:
"`327,980` valid states — all `266,680` with `ω < 20,000`, `1 <= d <= 40`, plus `60,000` random with
`ω < 2^64`, `d <= 200`, plus `1,300` constructed … `983,954` checks, `0` failures"; and
"`62,937` states covering all six residue-parity classes — with zero discrepancies"; the `8,000`
random states are in the same page's status line. The script name
`experiments/absorption_law.py` and the `stage3.md` §11.8.6.3 pointer are **kept**, so v3's
"verification pointers and script names are concrete throughout" is not touched. Drop-in at §3.4.

### 2.4 §4 — the staircase note and its correction

**C6. `Note added in v2` + `(Correction, 2026-08-01.)` → one status paragraph.**
Save **~530 pt (0.84 pages)** — 691.2 → ~160.

**[W], completely.** Every claim in both blocks is in `cycles.md` §12.8.6, which the correction
already cites at commit `9d9d1ec`:

| paper claim | `cycles.md` location |
|---|---|
| `8 − 5·log_2 3 = 0.0751874964…`, arc `[0.0415, 0.1169390665…]`, "any 66 consecutive integers" | Thm `12.8.6.1` statement + proof ("**66 consecutive integers suffice and 61 do not**") |
| window `[L^p, 1.05·L^p]` holds `0.05·L^p` integers, `79` at `p = 16`, first period supplying 66 | `12.8.6.1` proof ("exactly `50` at `p = 15` and `79` at `p = 16`") |
| partial quotients / badly-approximable dead end | `12.8.6.1`, *Superseded formulation* |
| additive offset `1/(L−1) = 1.70951` per block, no correction step | Thm `12.8.6.2` + *The shape, and the constant that was missing* |
| `p ≥ 16` unconditional, `3 ≤ p ≤ 15` finite check, `p ∈ {2,4}` by exhibition | `12.8.6.1` and *Scope, and what is not covered* |
| `γ ∈ [3.683012, 5.140212]`, no `p`-dependence | `12.8.6.1` display |
| end to end at `p ∈ {3,…,26}`; construction verified through `p = 32` | `12.8.6.2` *Verified* |
| "from `p = 8` upward not one working witness is a convergent or semiconvergent denominator" | `12.8.6.4`, *The two `p = 22` rows* |
| v2 route: semiconvergents, rounded geometric profile, bounded correction | `12.8.6.3` (kept in the record precisely because the published v2 note names it) |
| v2 range `p ∈ {2,…,23}`, `γ/log_2 p ∈ [1.828, 3.643]`; `p = 22` at `n = 25217`, `n = 31202`, `13` and `8` moves | Prop `12.8.6.4` and *The two `p = 22` rows* |
| every configuration a size-passer only, all fail `q \| R_r` | `12.8.6`, `12.8.6.2` *Verified*, `12.8.6.4` |

The status paragraph keeps the numbers a reader needs to judge the claim (the one exact number, the
66, the offset, the scope split, the `γ` bracket, the size-passer-only finding) and retires the
narrative of how the route changed to the release description. The **current-record URL
`…/blob/9d9d1ec/cycles.md` is preserved**; the v2-era URL `…/blob/72ec88e/…` goes to the history.
**The Appendix A pin (`1663d30`) is not touched.** Drop-in at §3.5.

**C6b. One consequential edit outside the replaced block.** The *Sharpness evidence and assessment*
paragraph currently ends "…the Note added in v2 and its correction below state what was proved,
where, and at what scope." That cross-reference must become "…the status paragraph below states what
was proved, where, and at what scope." Save 13 pt. Exact edit at §3.6. Theorem 4.6's statement,
Remark 4.7, and the rest of the *Sharpness* paragraph are untouched.

### 2.5 §5 — every item with its correction analysis

The four rounds' corrections that §5 carries are, in the order they were made:

* **(R2)** AEH is an *ensemble* statement; `π_{k,D}`'s depth component is the exact convolution, not
  the window chain's stationary law; "product" names exactly two clauses; the Tao attributions.
* **(R3)** AEH does not supply `E_B[m+r] = 4` or the empirical exponent mean past the digit budget;
  the budget's protection is a deterministic identity; Inselmann's envelope is in the one-division
  unit, "nothing converted".
* **(R4)** the block-time conversion is not claimed for the hypothesis anywhere in the document.
* **(R5)** the finite bound is about the **extended `(n+1)`-letter word**, not the word beginning at
  the sampled start.

Each item below states which of these it touches.

**C7. Window-chain `~1%` caveat — cut.** Save **40.6 pt**.
Text: *"The stationary law of the exact window chain is a `~1%`-accurate model of the depth marginal
of `π_{k,D}` rather than the marginal itself — the resolution at which `aeh.md` §13.4 recorded it —
and the two differ by exactly computed rationals (`aeh.md` §13.6.5)."*
**[W]** `aeh.md` §13.2 final sentence of the `π_{k,D}` paragraph ("The stationary law of the exact
window chain is a different object: a `~1%`-accurate model of this marginal, internal to this record,
whose exact discrepancy from it is recorded at `13.6.5`") and §13.6.5's own paragraph
(`17/63` vs `19/63`, `4/63` vs `2/63`, `19/63` vs `20/63`).
**Correction touched: (R2), the depth component.** *Why it survives:* the correction is carried by
the **definition**, not by this caveat. After the cut the paper still says (a) `π_{k,D}` is *the law
of `W_{k,D}` under the two-sided Bernoulli measure `\hat B`*, and (b) the depth's law is
`d_+ = m_+ + a_+` with `m_+` geometric(1/2) `⊥ a_+` and `a_+`'s law identified as
`v_3(Syrac(Z_3)+2)`. There is no second candidate law left in the paper for a reader to confuse it
with, because the window chain's stationary law is never otherwise mentioned. `aeh.md` §13.6.4(q2)
records the same judgement: the discrepancy "concerns a model object internal to this record and
qualifies nothing above."
*Checkpoint for the applying delegate:* §6 Discussion still proposes "transfer-operator analysis of
the exact window chain". After this cut that phrase reads as the chain of Theorem 3.8's exact
windows, which the paper does define. No edit is required, but do not let it be rewritten into a
claim about a stationary law.

**C8. Class-skeleton sentence — cut.** Save **28.1 pt**.
Text: *"The class skeleton of the chain is computable exactly: the transition from
`(ω ≡ 1 (8), d odd)` cited above holds because `m_+ = 1` and `a_+ = 0` there, and from
`(ω ≡ 5 (8), d odd)`, `P(d_+ even) = 2/3` exactly."*
**[W]** `aeh.md` §13.2, "Supporting exact facts": "The class process under `π_{k,D}` is an explicit
finite Markov chain with computable entries (e.g., from class `(1 mod 8, d odd)` the next depth is
exactly `1`; from `(5 mod 8, d odd)`, `P(d_+ even) = 2/3` exactly)."
**Corrections touched: none.** The sentence is illustrative. The `(1 mod 8, d odd)` transition it
explains is **kept** where it does work — as the example proving the process is not independent
across time, which is an (R2) clause.

**C9. The `P(d = 1) = 1/3`, `P(d = 2) = 20/63` values — cut; the `a_+` values kept.**
Save **~15 pt** *(est.)*.
**[W]** `aeh.md` Proposition 13.6.5's exact-values box carries all four `a` values and all four `d`
values. The paper keeps `P(a_+ = 0) = 2/3`, `P(a_+ = 1) = 19/63`, `P(a_+ ≥ 2) = 2/63` because those
are what is *read off Tao's printed `Syrac(Z/9Z)`* and therefore carry the attribution; the depth
values are one convolution step further and are pointed at instead.
**Correction touched: (R2).** The convolution claim is stated, not deleted; only its two evaluated
entries move to the pointer.

**C10. Chernoff-tilt clause — cut.** Save **~18 pt** *(est.)*.
Text: *"…, since the optimal Chernoff tilt is `e^λ = 2(1−2θ)` and needs `λ > 0`."*
**[W]** `aeh.md` §13.2 "Base case, and where the content is": "positive for every `θ < 1/4`
(`0.0201` at `θ = 0.20`, `0.00080` at `θ = 0.24`) and **exactly `0` at `θ = 1/4`**, the optimal
Chernoff tilt `e^λ = 2(1 − 2θ)` requiring `λ > 0`", and `13.2.4`(b)/(f)/(g).
**Corrections touched: (R2), (R3).** The version note's promise is that the base case is "given with
the exact rate at which it holds and the exact horizon at which that rate vanishes". Both survive:
the rate `log 2 − H(2θ)` per bit and the vanishing at `θ = 1/4` are kept verbatim; only the
*derivation* of why it vanishes there goes, with a pointer to `aeh.md` §13.2. This is the one place
the reviewer's phrase "Chernoff algebra" bites, and it is worth exactly 1.3 lines.

**C11. `O(2^{-k})` disclaimer — cut.** Save **27.1 pt**.
Text: *"The error `O(2^{-k})` of Theorem 3.8 prices a different statement — predicting the next exit
valuation from a window — which the hypothesis does not use."*
**[W]** `aeh.md` §13.3.1, same sentence: "The error `O(2^-k)` prices a different statement —
*predicting* the next exit valuation from a window, the one-step trichotomy of `11.8.7.6.1` … —
which the hypothesis does not use."
**Corrections touched: none.** It is a defensive clarification against a confusion the paper already
forecloses two paragraphs earlier, where `W_{k,D}` is distinguished from Theorem 3.8's window and
declared to decide nothing.

**C12. The clock paragraph's restatement of the block-time scope — cut.** Save **~67 pt**.
Text: *"His horizons are in step time: he starts from the classical range of `log_2 m` steps of `T`
and extends it by the factor `(1−log_2√3)^{-1} = 4.8188…`. That factor is `(1/β)/(1/4)` — the
identity `4/β = 2/(2−log_2 3)` — and is the same number in any time units; the endpoints read as
`1/4` and `1/β` blocks per bit only after dividing by the mean exponent per block, which is a theorem
where the cylinder count runs (`aeh.md` Lemma 13.2.4(g)) and, past it, is neither a theorem nor a
consequence of Hypothesis 5.1 (`aeh.md` §13.2.3)."*
**[W]** `aeh.md` §13.2.3 (the two-line `4θ < τ < 1` / `4θ < τ < 4.8188…` box and the paragraph after
it) and §13.3.2 (the whole Inselmann time-change analysis).
**[D] — and this is why it is the safest large §5 cut.** The **same** (R3)/(R4) correction is stated
**three times** in the paper:
1. Related work: "All of these horizons are counted in steps, and their reading in the reduced blocks
   of Section 5 is not free: it divides by a mean number of steps per block which is a theorem of the
   cylinder count inside the digit budget and, past it, neither a theorem nor a consequence of
   Hypothesis 5.1."
2. this clock passage;
3. the ledger paragraph: "The further passage to block time needs the frequency with which a Syracuse
   step ends a block, a two-letter statistic of the parity word that neither theorem supplies and that
   `π_{k,D}` does; … inside the digit budget it is a theorem of the cylinder count (`aeh.md`
   Lemma 13.2.4(g)), and past it neither a theorem nor a consequence of the hypothesis
   (`aeh.md` §13.2.3)."
**Corrections touched: (R3), (R4) — the two that must never come back.** *Why they survive:* copies
1 and 3 are both kept, unchanged in substance. Copy 3 is the strongest of the three (it names *why*
— the two-letter statistic) and copy 1 scopes the whole literature paragraph. The clock paragraph
retains "it reads as `1/4` blocks per bit only through the mean exponent per block,
`E_B[m+r] = 4`, a conversion available here **precisely because the word is exactly `B` here**",
which is the scoping clause itself. **Do not apply C12 without verifying copies 1 and 3 are present
in the file being edited.**

**C13. Inselmann recitation in the ledger paragraph — compressed to a pointer.**
Save **~80 pt** *(est.)*.
**[W]** `aeh.md` §13.3.2. **[D]** with Related work, which already states Thm 1.10's envelope, its
horizon, and its density.
**Corrections touched: (R3), and the standing prohibition on a conditional drift consequence.**
*Why they survive:* the sentence that does the work — "The descent consequence is not stated here,
because it is a theorem without the hypothesis **and a stronger one**" — is kept and strengthened;
`Cor. 1.4`, `Thm. 1.10` and `Thm. 1.6` keep their citations; the "`4.8188…` times the classical
range … the two measured in the same units" clause is kept; and the two-letter-statistic clause
(copy 3 above) is kept in full. What goes is the restatement of the theorem contents, which Related
work already gives.

**C14. `*`-density parenthetical — cut, but ONLY after landing it in `aeh.md`.**
Save **~30 pt** *(est.)*.
Text: *"(`*`-density: every initial segment carries all but `O(N^{-δ})` of its mass for some
`δ > 0`, which sets of natural density one need not do)"*.
**[P] — PAPER-ONLY.** Swept the whole repository: `*`-density appears in
`briefs/v3r3-basecase-density-findings.md`, `briefs/v3r3-inselmann-horizon-findings.md` and
`briefs/v3r3-paper-apply-findings.md` — round-3 working documents — and **nowhere in the wiki**.
`aeh.md` §13.3.2 and `publication.md` describe Inselmann's results but not the density notion his
argument buys. Drop-in Markdown for `aeh.md` §13.3.2 is at §4. **If the wiki edit is not made, keep
the parenthetical**; the 30 pt is not worth an unrecorded deletion.

**C15. Bottom-regime gloss — one of two copies cut.** Save **~20 pt** *(est.)*.
The gloss "the fixed drainage basin of small integers, whose window statistics are the digits of
particular numbers rather than samples from a measure" appears in the horizon paragraph and again,
almost verbatim, in the Calibration paragraph. **[W]** `aeh.md` §13.1. **[D]** — the Calibration copy
is kept (it is where `z = 41` needs it); the horizon copy becomes a pointer to `aeh.md` §13.1, which
the sentence already carries.
**Corrections touched: none.**

**C16. "Uniformity stands unqualified" → the reviewer's replacement, with the three limits kept.**
Save **~10 pt**; the point of this item is accuracy, not length.
Current: *"Uniformity stands unqualified at every tested depth and cell, within two ceilings the
campaign does not reach past."* — followed immediately by **three** qualifications (block length
`L ≤ 2`; pooled adjudicating runs; the altitude guard that binds).
Replacement: *"No residual discrepancy was detected at any tested depth or cell, under the stated
protocol and within three limits the campaign does not reach past: …"* — and the three limits stay,
each in full, only tightened in wording.
**[W]** `aeh.md` §13.5 *Status: resolved* ("at block lengths `L ≤ 2` — the campaign tests `L = 1` and
`L = 2` and is silent above (`13.6.4`(q1))"), §13.4 (pooling: "the pooled runs test a consequence of
the hypothesis rather than the quenched statement itself. The quenched form would be tested by the
distribution across orbits of `‖ν(x) − π_{k,D}‖`, which no run currently reports") and §13.4's
protocol-gap paragraph (the core cut: "removes `4,191` of `158,580` visits (`2.6 %`)").
**Correction touched: (R4)'s narrowing of the calibration claim.** *Why it survives:* the
replacement is strictly weaker than the current sentence and names the same three limits; it also
fixes an internal inconsistency, since the current sentence says "two ceilings" and then lists three.
Note for the record: `aeh.md`'s own status line still reads "bulk uniformity confirmed **UNQUALIFIED**
at every tested depth and cell, at block lengths `L <= 2`". After this change the paper is more
conservative than the wiki. That divergence is flagged, not resolved — see §8.

**C17. Remaining §5 compressions (no content removed, wording only).** Save **~150 pt** *(est.)*
across: the "not the window of Theorem 3.8" clause; the "one limit" paragraph; the segment-boundary
sentence; the "predictable / standing rule" sentence; the "past that range" sentence; the
`θ < 1/4` / `θ < 1/β` arithmetic; the Calibration campaign narrative. Every clause that carries a
correction is preserved; the drop-in at §3.7 is the exact text.

### 2.6 What is deliberately left alone in §5

Hypothesis 5.1 (byte-identical), the `W_{k,D}` display (byte-identical), the `gathered` display
(byte-identical, on its two deliberate lines), Lemma 5.2 (byte-identical), the two-sided `\hat B`
definition with its `13.6.3`(iii)/`13.6.5` pointer, both Tao attributions including the
`footnote 4 of arXiv v7` locator, the "product names exactly two clauses" scoping, the extended
`(n+1)`-letter-word passage (R5), the drift denial, the protected/consistent/admissible definitions,
the "same unit, nothing converted" clause, the `13.2.4(g)` scoping, the "past that range the
hypothesis supplies less" passage, the shell-scale/triangular-array pair, and the closing scope
paragraph.

---

## 3. Drop-in LaTeX

All replacements below were applied to a scratchpad copy and compiled. The build is clean: **no new
overfull or underfull boxes** (the single `Underfull \hbox (badness 1067)` in the log is
pre-existing, in the `lagarias` bibliography entry, and is present in the repository's own log).

### 3.1 Version note — replaces lines 41–42 in full

```latex
\subsection*{Version note}
v1, July 2026 (original publication). v2, July 2026 (v2-specific Zenodo DOI: 10.5281/zenodo.21421120): the subtitle of the \texttt{merle} citation restored, and a note added evidencing the sharpness hedge of Theorem~\ref{thm:staircase}, prompted by correspondence with Eric Merle. v3, August 2026 (drafted; the version-specific DOI on the title page is reserved and this version is not yet published): after external review, each definition, statement and scope word is brought back into line with the project record; the sharpness assessment of Section~\ref{sec:cycles} is reported as proved there; and Section~\ref{sec:aeh} is restated around one object and one hypothesis in ensemble form. No numbered theorem's claim is strengthened, weakened, or renumbered in either revision, and nothing new is proved in this paper; v3 reports two results established in the project record and not reproduced here. The repair history, item by item, is in this version's release description.
```

*Note on the last sentence.* The brief is explicit that the release description is the author's and
cannot be landed here. If the author would rather not commit the paper to a document that does not
yet exist, the alternative ending is: *"The repair history, item by item, is in the project record's
release notes for this version."* Either is one line; **the applying delegate should not choose
between them without the author.**

### 3.2 Abstract — replaces line 38 in full

```latex
We study the Collatz dynamics in a reduced coordinate system that compresses each deterministic valuation run into a single block, producing a self-map $F$ on states $(\w,d)$ --- an odd core prime to $3$ and a depth --- whose convergence problem and cycle set are exactly those of the Collatz map. In these coordinates the local arithmetic admits exact laws, all governed by one $2$-adic quantity, the \emph{anchor} $M(\w) = -2\log\w/\log 9 \in \Z_2$: the exit valuation obeys the global law $s = 2 + \vt{d - M(\w)}$ on the lifting classes and is constant on the rest; the depth evolution closes exactly in the anchor displacement together with a stated $3$-adic absorption law; and the anchor increment obeys an exact law modulo any power of $2$, computable from graded residues of the state. A finite window of digits and stratum labels consequently decides each step in an error-free trichotomy, while a digit-budget accounting indicates that no bounded window can decide infinite horizons --- localizing the difficulty in the digit supply of the anchors. On the cycle side, a one-line elimination identity yields short rederivations of the classical exclusions at one, two and three blocks, and our main new theorem is a sharp dichotomy for counting arguments: a trim uniform in the number of blocks $p$ gives effective finiteness at every period, but its constant necessarily degrades like $(\LL)^{-p}$, and an explicit family of near-counterexamples (\emph{staircases}: divergent-orbit profiles bent into loops) shows counting cannot do substantially better, so uniform cycle exclusion requires arithmetic (divisibility) input, not sharper counting. Finally we state the equidistribution hypothesis implicit in the classical heuristics as a precise conjecture --- that the block letters of uniformly sampled large starts carry, at every finite block length, the frequencies of an exactly computable Bernoulli law --- prove its consequences conditionally, exhibit an unconditional base case inside the digit budget, and report a calibration campaign whose four apparent anomalies all dissolved under controls.
```

### 3.3 Introduction roadmap — replaces line 56 in full

```latex
Section~\ref{sec:anchor} is the technical heart: every quantity above obeys an exact law in the anchor displacement $d - M(\w)$, a finite window of digits and stratum labels then decides the next step in a trichotomy that never errs, and an elementary accounting argument shows each decision \emph{consumes} digits irreversibly. In these coordinates the difficulty of the problem is not diffuse: it is the question of where the digits of the anchors come from. Section~\ref{sec:cycles} tests the one regime where finite data can beat unbounded depth --- cycles --- and, since the staircase is precisely a divergent-orbit profile closed into a loop, the cycle half and the divergence half of the residual difficulty are, in a concrete sense, one object. Section~\ref{sec:aeh} formalizes the statistical half: the folklore ``fair-coin'' heuristics (Terras \cite{terras}) become an exact statement about the block letters of typical orbits, equivalently about an explicitly computable window law $\pi_{k,D}$, whose ledger consequences are unconditional theorems \emph{about} $\pi_{k,D}$.
```

### 3.4 Remark 3.6 body — replaces line 146 in full

```latex
Each law above was checked by independently written code, with zero discrepancies: the valuation law on $8{,}000$ random states across both lifting components, the entry-depth law exhaustively on all $62{,}937$ valid states with $\w < 3000$, $d < 64$, and the absorption law on $327{,}980$ states ($983{,}954$ comparisons against both this Lemma and its form in the record), with the two branches on which $a_+$ is a $3$-adic function of $\w$ constructed rather than sampled. The records are \texttt{stage3.md} \S11.8.6.3 and that page's status header; the code is \texttt{experiments/absorption\_law.py}.
```

### 3.5 Staircase status paragraph — replaces lines 231–237 in full (heading, v2 note, `\medskip`, correction)

```latex
\paragraph{Status of the assessment (August 2026).} Prompted by correspondence with Eric Merle concerning this theorem's sharpness hedge (his related formal work is cited in \cite{merle}), the assessment above has since been \emph{proved} in the project record, at a scope and a shape stronger than it claims, and is not reproduced here; Theorem~\ref{thm:staircase} stands above exactly as written. A passing size-condition witness is constructed at every period, and the whole Diophantine input is one exact number: $8 - 5\LL = 0.0751874964\ldots$ is positive and below the target arc's length, so any $66$ consecutive integers contain an admissible exponent $n$, and the scale window at period $p$ holds $0.05\,(\LL)^{p}$ integers --- $79$ already at $p = 16$ --- while a corrected profile, the geometric climb with a fixed additive offset $1/(\LL - 1) = 1.70951$ per block, satisfies all $p$ size conditions by construction, with no correction step. The two halves compose to a proof for every $p \ge 16$, at $\gamma$ between the absolute constants $3.683012$ and $5.140212$ --- no $p$-dependence at all --- with $3 \le p \le 15$ meeting the same bracket by finite check and $p \in \{2,4\}$, outside the construction's reach, covered by direct exhibition. Every constructed configuration remains a size-passer only and fails the divisibility conditions $q \mid R_r$, as the instances above do: sharper evidence that counting cannot do better, and no evidence about exclusion. The record is \texttt{cycles.md} \S12.8.6 (\url{https://github.com/macindoe/collatz/blob/9d9d1ec/cycles.md}); the note added in v2 and the continued-fraction route it named are in the release description and at \S12.8.6.3 there.
```

### 3.6 Sharpness paragraph cross-reference — exact edit inside line 225

Replace

```
the Note added in v2 and its correction below state what was proved, where, and at what scope.
```

with

```
the status paragraph below states what was proved, where, and at what scope.
```

Nothing else in line 225 changes.

### 3.7 §5 — replaces lines 239–465 in full

```latex
\section{The equidistribution hypothesis, made exact}\label{sec:aeh}

What is the right comparison object? By Theorem~\ref{thm:onestep} every dynamical decision at horizon one is a function of the depth-$k$ window, so the null model is a measure on windows, and the structure forces the choice: the $\w$-residues carry the anchor digits, for which Haar measure is the canonical reference (this is where the classical $2$-adic shift-conjugacy heuristics live), while the depth is \emph{dynamical} --- it is produced by Theorem~\ref{thm:depth} --- and receives instead its own exact renewal law, $\dnext = m_+ + a_+$ with $m_+$ geometric$(1/2)$ and \emph{independent} of the absorption $a_+$, so that it is the distribution of the depth, and not that of the absorption, which is the convolution of the two. The stationary $3$-adic law governing $a_+$ (\texttt{aeh.md} \S13.6.5) is not new here: it is Tao's Syracuse random variable $\mathrm{Syrac}(\Z_3)$ \cite[Lemma~1.12 and Remark~1.13]{tao}, in the present normalisation. Precisely, the $3$-adic past-limit of the block coordinate has the law of $\mathrm{Syrac}(\Z_3)/2$ --- the two differ by the $3$-adic unit $2^{-1}$ because one block here is a run of Syracuse steps terminated by the first exponent $\ge 2$, so that the block chain sees the Syracuse chain conditioned on that event --- and hence $a_+ = \vth{\mathrm{Syrac}(\Z_3) + 2}$, with $P(a_+ = 0) = \tfrac23$, $P(a_+ = 1) = \tfrac{19}{63}$ and $P(a_+ \ge 2) = \tfrac{2}{63}$ read off the nine values of $\mathrm{Syrac}(\Z/9\Z)$ that Tao computes. What the present coordinates add is the \emph{joint labelled} law (\texttt{aeh.md} \S13.6.3(v)): the $\w$-residues are Haar-uniform among odd residues and independent of the depth, the whole carried on the residues \emph{together with} the stratum labels $(s,\sigma,a_+)$ --- $a_+$ being a $3$-adic function of $\w$ (Lemma~\ref{lem:absorption}) which the finite $2$-adic residue window does not determine. Two integers fix the observable: a depth $k$ and a \emph{cap} $D$, chosen together and quantified over. The \emph{capped depth-$k$ window} at a visit is
\[
  W_{k,D} \;=\; \bigl(\, \w \bmod 2^{k+2},\; d \wedge D,\; s \wedge D,\;
  \sigma \wedge D,\; a_+ \wedge D \,\bigr), \qquad u \wedge D := \min(u,D),
\]
a finite alphabet of at most $2^{k+1}D^3(D+1)$ letters; the cap is what bounds it, and it must cap the labels as well as the depth, since $\sigma$ and $a_+$ are unbounded. It is not the window of Theorem~\ref{thm:onestep}, whose alphabet is countably infinite and which decides the next step: $W_{k,D}$ decides nothing, and no statement in this section asks it to. Let $\pi_{k,D}$ denote the law of $W_{k,D}$ under the two-sided Bernoulli measure $\hat B = \bigotimes_{i \in \Z}(\mathrm{geom}(\tfrac12) \times \mathrm{geom}(\tfrac12))$ on the door-letter alphabet --- two-sided because the absorption $a_+$ is a function of the orbit's $3$-adic past and has no realisation on the one-sided $2$-adic side (\texttt{aeh.md} \S13.6.3(iii), \S13.6.5); reading the stationary Syracuse variable as the outcome of an iteration extending to arbitrarily large negative times is Tao's own alternative to his positive-time indexing \cite[Remark~1.13, footnote~4 of arXiv~v7]{tao}. ``Product'' names exactly two clauses of $\pi_{k,D}$ --- residue $\perp$ depth, and $m_+ \perp a_+$ --- and no others: $\pi_{k,D}$ is not a product across its coordinates ($s$ is an exact function of the full state), and the process $(W_{k,D}(n))_n$ is stationary but not independent across time (e.g.\ from $(\w \equiv 1\ (8),\ d$ odd$)$ the next depth is exactly $1$). Under $\pi_{k,D}$, unconditionally: $P(s = j) = 2^{-j}$ at every $j < D$, the mass beyond the cap sitting in one tail cell; the $3$-gain rate is $\sum_{j\,\mathrm{even}} 2^{-j} = \tfrac13$ by Lemma~\ref{lem:absorption}, exact up to that same cell, whose parity split the cap hides; and the classical negative drift is a property of $\pi_{k,D}$ --- but only of $\pi_{k,D}$: window equidistribution at each fixed $(k,D)$ does not control the means of the unbounded $m_+$ and $s$, so no drift or contraction statement about orbits follows from it (\texttt{aeh.md} \S13.3.2). The folklore ``ledger'' is thus a theorem \emph{about} $\pi_{k,D}$; the empirical question is only whether the orbits of typical starting values follow $\pi_{k,D}$.

\begin{hypothesis}[AEH, ensemble form]\label{hyp:aeh}
Fix a \emph{budget rate} $\tau > 0$ and a \emph{block horizon rate} $\theta > 0$;
for each $N$ put $b = \lfloor\log_2 N\rfloor$, $\Lambda_N = \lceil \tau b\rceil$
and $T_N = \lceil \theta b\rceil$. Draw $x$ uniformly from the odd integers of
$[N, 2N)$; put $(\w_0,d_0) = R(x)$ and $(\w_{n+1},d_{n+1}) = F(\w_n,d_n)$; let the
\emph{letter} at block $n$ be $\ell_n = (m_{+,n},\,s_{n+1})$, and let
$S_n = \sum_{i<n}(m_i + s_i)$ be the \emph{exponent spent} before block $n$ ---
the number of $2$'s divided out from $x$ to $x_{\mathrm{exit}}(n-1)$. Tally block
$n$ at the symbol
\[
  \tilde\ell_n \;=\; \ell_n \ \text{ if } S_n < \Lambda_N, \qquad
  \tilde\ell_n \;=\; \dagger \ \text{ otherwise.}
\]
For a finite word $w = (w_1,\dots,w_L)$ of letters, let $f_N(w,x)$ be the
frequency of $w$ among the $T_N - L + 1$ blocks
$(\tilde\ell_n,\dots,\tilde\ell_{n+L-1})$, $0 \le n \le T_N - L$: every
block counted exactly once, at weight $1/(T_N-L+1)$ --- the same number for
every block of every orbit, so no block is reweighted by the orbit it came from
and no denominator is random. Then for every finite word $w$ and every
$\varepsilon > 0$,
\[
  \frac{2}{N}\,\#\bigl\{\, x \text{ odd},\ N \le x < 2N \;:\;
  \bigl| f_N(w,x) - B[w] \bigr| > \varepsilon \,\bigr\}
  \;\longrightarrow\; 0 \qquad (N \to \infty),
\]
where, writing $w_i = (m_i, r_i)$ for the components of the $i$-th letter of $w$,
$B[w] = \prod_{i} 2^{-(m_i + r_i)}$, and $B[w] = 0$ for any $w$ containing
$\dagger$, for every admissible pair $(\tau,\theta)$ in the sense defined below.
\end{hypothesis}

Equivalently, and this is the form the calibration measures: for every $k$, $D$
and $L$, the empirical distribution of the $L$-blocks of consecutive capped
windows $W_{k,D}$ over the same tallied blocks, with $\dagger$ carried through
and given mass $0$, converges in total variation on the finite window alphabet,
off a vanishing density of starts, to $\pi^{(L)}_{k,D}$, the $L$-block law of the
stationary process under $\hat B$. The equivalence is Theorem 13.6.4 of
\texttt{aeh.md}, a deterministic dictionary between letters and labelled window
blocks; the case $L = 1$ recovers $\pi_{k,D}$, and
$\pi^{(L)}_{k,D} \neq \pi_{k,D}^{\otimes L}$. A sampled segment has no infinite
past at its first block, so the reconstruction of $W_{k,D}$ from letters is exact
only away from the start; the deviation occupies $O(1)$ blocks of a horizon
$T_N \to \infty$ and contributes $O(1/T_N)$ to every frequency above.

There is one limit here, $N \to \infty$, and the sample grows because the sampling
scale grows rather than because any one orbit is run forever. That is forced: along
a fixed orbit the unrestricted empirical distribution is false, every convergent
tail sitting at $(1,1)$ forever, while above a fixed cut a convergent orbit
supplies only finitely many qualifying visits and none at all once the cut exceeds
its maximum, so a limit in orbit length is empty rather than merely delicate, in
whichever order it is taken (\texttt{aeh.md} \S13.6.6).

The horizon does the job a bulk cut would do, and does it without one. A step of
the one-division map $y \mapsto y/2$ or $(3y+1)/2$ never lowers $\log_2$ by more
than $1$, so $\log_2 x_{\mathrm{exit}}(n-1) \ge \log_2 x - S_n$ for every start and
every $n$, with no exceptional set; inside a budget $\tau < 1$ of the start's own
bits every tallied exit therefore exceeds $N^{1-\tau}$, far above the
\emph{bottom regime} of \texttt{aeh.md} \S13.1. That matters because any altitude
threshold is a selection on the observable itself --- a cut on
$x_{\mathrm{exit}} = (3^{d}\w - 1)/2^{s}$ censors large $s$, and a cut on the core
$\wnext$ censors large $s$, $m_+$ and $a_+$ together --- whereas the budget clause
$S_n < \Lambda_N$ is \emph{predictable}, decided by blocks strictly earlier than
the one it admits, and the tally denominator is the deterministic $T_N$ that
\texttt{aeh.md} \S13.5's standing rule was written to secure. Call $\tau$
\emph{protected} when all but a vanishing density of starts keep every in-budget
exit above any $X_N$ with $\log X_N = o(\log N)$, and $(\tau,\theta)$
\emph{consistent} when $\theta\,\mathbb{E}_B[m+r] < \tau$; \emph{admissible} means
both. Every $\tau < 1$ is protected outright by the bound above, and every
$\tau < (1-\log_2\sqrt3)^{-1} = 4.8188\ldots$ is protected at natural density one
by Inselmann \cite[Thm.~1.1]{inselmann}, whose two-sided envelope is stated for
the one-division map --- the same unit, nothing converted.
Consistency is compatibility with the target law rather than a claim about
orbits: under $B$ a block spends $\mathbb{E}_B[m+r] = 4$ of exponent, so
$4\theta < \tau$ says exactly that $B$ itself predicts no out-of-budget block,
which is what $\pi_{k,D}$'s giving $\dagger$ no mass requires. Where the cylinder
count runs it is more, and unconditionally: for $\tau < 1$ no block of the horizon
leaves the budget and the empirical exponent mean converges to $4$
(\texttt{aeh.md} Lemma 13.2.4(g), whose two error terms are, on that range,
precisely the two clauses of admissibility). Past that range the hypothesis
supplies less, and only about frequencies: a vanishing frequency of $\dagger$ says
all but $o(T_N)$ of the first $T_N$ blocks are within budget, and is not a bound on
a sum over its complement --- the block at which the budget is exhausted is tallied
at full weight and its letter is unbounded, and the $o(T_N)$ blocks past it are
uncontrolled, so $T_N^{-1}\sum_{n<T_N}(m_n+r_n) \to 4$ does not follow there and
can fail by any amount. Hence $4\theta < \tau < 1$ is $\theta < 1/4$ and
$4\theta < \tau < 4.8188\ldots$ is $\theta < 1/\beta = 1.2047\ldots$, where
$\beta = 2(2-\LL) = 0.8301\ldots$ is the classical per-block contraction rate and
$4/\beta = (1-\log_2\sqrt3)^{-1}$ an identity --- arithmetic on the definition of
consistency, with the divisor in either block reading the mean of the target law:
a theorem about orbits below the budget, and not a consequence of the hypothesis
above it.

The hypothesis has an unconditional base case, and it is Heuristic~\ref{prop:budget}
with a number on it. The classical coding fact --- the odd integers whose first $n$
blocks realize a prescribed itinerary form exactly one residue class modulo
$2^{S+1}$, $S$ the itinerary's total exponent (Terras \cite{terras}; in the present
coordinates \texttt{itinerary.md} \S14.15.1.5) --- makes the first $n$ blocks of a
start drawn uniformly from \emph{any} window of $2^{J}$ consecutive integers
exactly product-distributed on the event $S + 1 \le J$: the event that the itinerary
has not outspent the start's supply of binary digits. That fact is about the word
beginning at $x$ itself, while $\ell_0$ is the letter of the block \emph{after} the
start's own; it is applied here to the \emph{extended} $(n+1)$-letter word --- the
start's own letter followed by $\ell_0,\dots,\ell_{n-1}$, of total exponent exactly
$S_{n+1}$, the divisions from $x$ down to $x_{\mathrm{exit}}(n)$ --- of whose law
the one displayed is a marginal. Writing
$b = \lfloor\log_2 N\rfloor$, this gives, for every $J \ge 2$,
\[
  \begin{gathered}
    \bigl\lVert \mathrm{Law}(\ell_0,\dots,\ell_{n-1}) - B^{\otimes n}
      \bigr\rVert_{\mathrm{TV}}
    \;\le\; \frac{2^{J+2}}{N} + P_B(S_{n+1} \ge J), \\[2pt]
    P_B(S_{n+1} \ge J) = P\bigl(\mathrm{Bin}(J-1,\tfrac12) < 2(n+1)\bigr),
  \end{gathered}
\]
the second identity because $S_{n+1}$ is the waiting time for the $2(n+1)$-th
head in a fair coin sequence. The first term is the price of a general window
$[N,2N)$ over a dyadic one and is negligible for $J \le (1-\eta)b$; the second
decays at the exact rate $\log 2 - H(2\theta)$ per bit at $n = \lceil\theta b\rceil$,
$H$ the binary entropy --- positive for every $\theta < 1/4$ and \emph{zero} at
$\theta = 1/4$ (\texttt{aeh.md} \S13.2). The bound is on the joint law of the whole
length-$n$ word, so it controls every finite block length at once, and with the
concentration of empirical pattern frequencies, the removal of the segment's initial
past-boundary and the altitude bound above --- which makes the budget its own
protection --- it yields the hypothesis outright:
Hypothesis~\ref{hyp:aeh} is a \emph{theorem} for every admissible $(\tau,\theta)$
with $\tau < 1$, equivalently for every horizon rate $\theta < 1/4$, at every
block length. The assembly is Lemma 13.2.4 of \texttt{aeh.md}.

The natural clock here is total exponent, not blocks: the frontier is one unit of
exponent per bit of start --- the start's own digit supply, with no estimate in it
--- and it reads as $1/4$ blocks per bit only through the mean exponent per block,
$\mathbb{E}_B[m+r] = 4$, a conversion available here precisely because the word is
exactly $B$ here. Hypothesis~\ref{hyp:aeh} is the assertion that the law still
describes the orbit after the start's digits have been spent; the digit budget
locates the frontier, and this is the statistical statement on the far side of it.
That frontier is the classical one --- the same $\theta < 1/4$ is where Terras's
count stops, and $1 - \beta/4 = \log_4 3$ is exactly the exponent Korec
\cite{korec} obtains by exhausting it --- and it is a frontier of this technique
and not of the problem, Inselmann \cite{inselmann} crossing it unconditionally for
the trajectory envelope and the first moment, in step time and by a stronger
density notion rather than a sharper count.

AEH implies the ledger, in the form the hypothesis has: $s$ is a coordinate of
the observable, so $P(s = j) = 2^{-j}$ is a marginal of $\pi_{k,D}$ rather than a
deduction, exactly at every $j < D$ and up to the cap's single tail cell above;
and for every $\varepsilon$ and every horizon rate, all but a vanishing density of
the odd starting values of each size carry those frequencies along their first
$T_N$ blocks, all but $o(T_N)$ of them within the budget --- and all of them when
$\tau < 1$. Evaluating each odd $x$ once, at its own dyadic scale
$2^{\lfloor \log_2 x\rfloor}$, turns that array of statements into a single one:
the odd integers that fail at their own scale have natural density zero
(\texttt{aeh.md} Proposition 13.2.5). The union over \emph{all} sampling scales is
a different and larger object and is not controlled --- the bad sets form a
triangular array, each testing a horizon and a budget that move with the scale, and
vanishing density in every window does not thin their unrestricted union. The
descent consequence is not stated here, because it is a theorem without the
hypothesis and a stronger one: Inselmann's \cite[Cor.~1.4, Thm.~1.10]{inselmann},
cited in Related work, is two-sided, uniform in the time, unconditional, and runs
to $4.8188\ldots$ times the classical range at which this section's cylinder count
stops, the two measured in the same units. His \cite[Thm.~1.6]{inselmann} is what
carries his own passage from $T$-time to Syracuse time; the further passage to
block time needs the frequency with which a Syracuse step ends a block, a
two-letter statistic of the parity word that neither theorem supplies and that
$\pi_{k,D}$ does, so it is not available to underwrite the hypothesis: inside the
digit budget it is a theorem of the cylinder count (\texttt{aeh.md}
Lemma 13.2.4(g)), and past it neither a theorem nor a consequence of the hypothesis
(\texttt{aeh.md} \S13.2.3). What the hypothesis supplies beyond these is
distributional and is the whole of its content: the full $2^{-j}$ marginal at every
$j$ below the cap, the exact $\tfrac13$ rate of Lemma~\ref{lem:absorption}, and the
depth law, at every finite depth and past the budget at which the classical count
stops. Its exceptional set is a set of \emph{starting values} of vanishing density
at a prescribed finite horizon --- not a null set of orbits, and not a statement
about any orbit's infinite tail. It does not exclude individual staircase tails
(Remark~\ref{rem:staircase}); it does not iterate --- the image of a density-one
set of starts need not be density-one at the next scale, an obstruction Tao states
in the same terms \cite{tao}; and by Heuristic~\ref{prop:budget} it cannot be
reached by finite-window computation. Its content is a question about digits of
$2$-adic logarithms, older and broader than the Collatz problem.

\paragraph{Calibration.} An eight-round campaign (per-orbit statistics over each cell's own conditional counts, $1{,}600$--$2{,}600$ independent orbits per cell, under an altitude cut on the core) produced four apparent violations of $\pi_{k,D}$-uniformity, each dissolved by a sharper control: an $s{=}3$ marginal excess and pair correlations (artifacts of small starting values); digit biases (contamination by the \emph{bottom regime}, the fixed drainage basin of small integers, where deviations reach $z=41$ but reflect particular numbers rather than a measure); and a $5\sigma$ digit bias in one cell surviving a $2^{40}$ cut. The last dissolved under fixed-horizon unweighted sampling ($0.2503\pm0.0015$ against null $0.25$ over $84{,}739$ visits) and was explained exactly:

\begin{lemma}[deterministic routing]\label{lem:routing}
For $\w \equiv 1 \pmod 8$, $d = 1$: here $s = 1$, $C = 3\w + 1$, $\vt{C} = 2$, $a_+ = 0$, so $\wnext = (3\w+1)/4$ and $\dnext = 1$; the residue $\w \bmod 32$ determines the next class exactly: $1 \mapsto (1,1)$ (immediate self-return), $9 \mapsto (7,1)$, $17 \mapsto (5,1)$, $25 \mapsto (3,1)$, the lifting class.
\end{lemma}

Ratio estimators over correlated visit sequences inherit this routing (residue $25$ leads into deep descent, hence fewer qualifying visits, hence inflated per-orbit weight), manufacturing a bias aimed at one residue of the unique class with a self-loop channel. No residual discrepancy was detected at any tested depth or cell, under the stated protocol and within three limits the campaign does not reach past: it tests block lengths $L = 1$ and $L = 2$ only and is silent above; its adjudicating runs pool per visit across orbits, so they measure the across-orbit average of the per-start frequencies --- a consequence of Hypothesis~\ref{hyp:aeh} rather than the per-start statement itself, which would be tested by the distribution across orbits of $\lVert\nu - \pi_{k,D}\rVert_{\mathrm{TV}}$ and is not among the runs reported; and its altitude guard cuts on the core $\wnext$ rather than the door, censoring $s$, $m_+$ and $a_+$ at once, and does bind at finite size, removing $2.6\%$ of visits in the adjudicating run and moving the reported statistics at the third decimal (\texttt{aeh.md} \S13.4, \S13.5). Hypothesis~\ref{hyp:aeh} carries no cut of any kind; it tallies within the exponent budget, which bounds every tallied exit from below without selecting on the letter being tallied.
```

**The calibration sentence, isolated** (in case the applying delegate prefers a surgical edit to
line 465 rather than the whole-section replacement). Replace

```
Uniformity stands unqualified at every tested depth and cell, within two ceilings the campaign does not reach past. It tests block lengths $L = 1$ and $L = 2$ --- single cells and consecutive-pair cells, and no longer pattern than that --- and is silent above; and its adjudicating runs pool per visit across orbits,
```

with

```
No residual discrepancy was detected at any tested depth or cell, under the stated protocol and within three limits the campaign does not reach past: it tests block lengths $L = 1$ and $L = 2$ only and is silent above; its adjudicating runs pool per visit across orbits,
```

---

## 4. Drop-in Markdown — the one item that must land in `aeh.md` first

**Target:** `aeh.md` §13.3.2, immediately after the sentence ending *"…improving Tao's
logarithmic-density theorem to natural density for these thresholds."* (currently line 124 of
`aeh.md`). Insert as a new sentence in that same paragraph:

```markdown
What buys the iteration invariance his argument needs is not a sharper count but a stronger notion of density: `*`-density, under which every initial segment of the set carries all but `O(N^(−δ))` of its mass for some `δ > 0` — a property that sets of natural density one need not have. That is the mechanism the published paper names when it says the `θ < 1/4` frontier is a frontier of the cylinder-count technique and not of the problem.
```

**Why this is required.** A repository-wide sweep found `*`-density only in
`briefs/v3r3-basecase-density-findings.md` (§5.5), `briefs/v3r3-inselmann-horizon-findings.md`
(§5.5) and `briefs/v3r3-paper-apply-findings.md` — all round-3 working documents — and **nowhere in
the wiki**. It entered the paper in round 3 and was never landed in `aeh.md`. Under the brief's
rule, C14 may not be applied until this sentence (or the author's own wording of it) is in
`aeh.md`; otherwise the parenthetical stays in the paper.

**No other cut in this plan requires a wiki landing.** Every other passage removed above was checked
against `aeh.md` §13.1–§13.6.6, `cycles.md` §12.8.6, `stage3.md` §11.8.6.3 and
`itinerary.md` §14.15.1.5 and found present there, with the exact locations recorded in §2.

**Two further paper-only items that this plan therefore KEEPS** (recorded so a later pass does not
remove them without noticing):

* the identity `1 − β/4 = log_4 3` tying the frontier to Korec's exponent. Present in
  `briefs/v3r2-contraction-literature-findings.md` and `briefs/v3r2-round-findings.md`; **not in the
  wiki**. Kept in the paper.
* the Wirsching "siblings in shape" comparison in Related work (what Wirsching needs is a
  Collatz-generated object unbiased in `3`-adic coordinates; AEH is that one is unbiased in `2`-adic
  coordinates). Present in `briefs/v3r2-wirsching-check-findings.md`; **not in the wiki**. Kept — see
  §7.1.

---

## 5. The repair history, as plain text for the author

Not landed anywhere. This is the content the version note currently carries, restated for a release
description, plus the two rounds the version note does not narrate as rounds. Every item is taken
from the current version note, the round briefs and the commit log at `main` = `29ecb1b`; nothing is
added.

```
RELEASE NOTES — "Reduced coordinates for the Collatz map", v3 (August 2026)

v1 — July 2026. Original publication.

v2 — July 2026. Zenodo DOI 10.5281/zenodo.21421120.
  - Restored the subtitle of the `merle` citation.
  - Added a Note evidencing the sharpness hedge of Theorem 4.6 (the staircase),
    prompted by correspondence with Eric Merle: a single period-parametrized
    construction procedure — semiconvergents of log_2 3 select the exponent n, a
    rounded geometric profile builds the climb, a bounded correction closes the
    last bits — verified by exact big-integer arithmetic to produce a passing
    size-condition witness at every period p in {2,...,23}, with
    gamma / log_2 p in [1.828, 3.643]. The recipe's own candidate chain initially
    left p = 22 unresolved; correspondence with Eric Merle identified the cause as
    a gap in that chain's coverage at the required scale, not a failure of the
    correction step, and candidates outside the chain (n = 25217, n = 31202)
    resolved it with 13 and 8 correction moves. The note named its remaining gap:
    no proved closed-form bound on the multiplicative gap between consecutive
    correctly-signed semiconvergent runs.
  - No theorem or universal claim strengthened. v2 adds a finite computational
    evidence record.
  - Record of the v2 note: cycles.md 12.8.6 at commit 72ec88e.

v3 — August 2026 (drafted; version-specific Zenodo DOI 10.5281/zenodo.21730505
     reserved; not yet published). Five rounds of external review.

  THE STAIRCASE (Section 4).
  - The gap named in the v2 note has been closed, and closed by replacing the
    route rather than completing it. Candidate availability needs no
    continued-fraction input: 8 - 5*log_2 3 = 0.0751874964... is positive and
    below the target arc's length, so any 66 consecutive integers contain an n
    whose ceil(n*log_2 3) - n*log_2 3 lies in [0.0415, 0.1169390665...], and the
    scale window at period p holds 0.05*(log_2 3)^p integers — 79 at p = 16 — so
    p = 16 is the first period supplying 66 consecutive integers.
  - The bound the v2 note asked for is not needed and, as posed, is a dead end:
    those gaps are the partial quotients of log_2 3, so a uniform bound on them is
    exactly the assertion that log_2 3 is badly approximable.
  - The p = 22 episode was a property of the candidate list used, not of log_2 3:
    under the availability statement it does not arise — from p = 8 upward not one
    working witness is a convergent or semiconvergent denominator.
  - The construction half is closed independently: a corrected profile — the
    geometric climb with a fixed additive offset 1/(log_2 3 - 1) = 1.70951 per
    block, absent from the v2 profile — satisfies all p size conditions by
    construction, with no correction step. The bounded correction is removed from
    the argument rather than bounded.
  - The two halves compose to a proof for every period p >= 16, at gamma between
    the absolute constants 3.683012 and 5.140212 — no p-dependence at all — with
    3 <= p <= 15 meeting the same bracket by finite check, and p in {2,4}, outside
    the construction's reach, covered by direct exhibition. End to end verified at
    p in {3,...,26}; the construction itself verified through p = 32.
  - The proof is established in the project record and is NOT reproduced in the
    paper. Theorem 4.6 stands exactly as written in v1 and v2. Every constructed
    configuration remains a size-passer only and fails the divisibility conditions
    q | R_r: sharper evidence that counting cannot do better, and no evidence
    about exclusion.
  - Current record: cycles.md 12.8.6 at commit 9d9d1ec.
  - Presentational: the sharpness assessment, previously Theorem 4.6's closing
    clause, is set out beside the theorem under "Sharpness evidence and
    assessment", so the theorem environment carries only what the paper proves.

  DEFINITIONS AND STATEMENTS BROUGHT BACK INTO LINE WITH THE RECORD.
  - Definition 2.1 requires omega > 0, without which (-1, 1) leaves F undefined.
  - Theorem 3.3's unconditional bound reads C(omega)(1 + log d)^2; the printed
    (log d)^2 was vacuous at d = 1.
  - Theorem 3.8 states its depth-k window as the residues of Theorem 3.7 TOGETHER
    WITH the stratum labels (s, sigma, a_+), matching its own proof. Theorem 3.7
    is unchanged.
  - Theorem 4.5's n_0(p) is defined.
  - The digit budget is labelled a heuristic, as its own text always said; no part
    of it is claimed as proved.
  - Proposition 4.1 defines sigma_j at its point of use (sigma_j = s_j + m_{j+1},
    as in Definition 2.1) and distinguishes M_t, a partial sum of entry depths,
    from the anchor M(omega).

  SECTION 5 — ONE OBJECT, ONE CLOCK, ONE HYPOTHESIS.
  - The section now carries one object where it previously carried several. The
    observable is the capped window W_{k,D}, at a depth k and a cap D quantified
    together, the cap bounding the stratum labels as well as the depth.
  - The comparison law pi_{k,D} is the law of that window under the two-sided
    Bernoulli measure, its depth component the exact convolution rather than the
    window chain's stationary law. "Product" names its two proved clauses and no
    others — in particular the window process is stationary but not independent
    across time.
  - Hypothesis 5.1 is stated in ensemble form — uniformly sampled starts, a
    horizon linked to the sampling scale, every block counted once, a single limit
    — in letter coordinates and at every finite block length. This retires both
    the single-orbit reading, which is empty on every convergent orbit, and the
    single-visit reading, which is strictly weaker. The distance is total
    variation on the finite window alphabet, named where it is used.
  - The bulk cut is replaced by an exponent budget whose admissibility is defined
    and whose protection is a deterministic identity rather than an assumption.
  - The section states NO descent or contraction consequence of Hypothesis 5.1:
    that conclusion is a theorem without the hypothesis, and stronger, so the
    section is framed onto what the hypothesis alone supplies, which is
    distributional.
  - The unconditional base case is given with the exact rate at which it holds and
    the exact horizon at which that rate vanishes. It is about the EXTENDED
    (n+1)-letter word — the start's own letter followed by the n sampled letters —
    and not about a word beginning at the sampled start; the displayed bound is a
    marginal of that word's law.
  - The density conclusion is stated at dyadic-shell scale, where it is exact; the
    union over all sampling scales is a triangular array that no per-scale
    statement controls.
  - Section 5 does not claim that Hypothesis 5.1 supplies E_B[m + r] = 4, or the
    empirical exponent mean, past the digit budget; and the reading of any
    step-time horizon in reduced blocks is a theorem of the cylinder count inside
    the digit budget and, past it, neither a theorem nor a consequence of the
    hypothesis.

  ATTRIBUTIONS PAID.
  - The stationary 3-adic law governing the absorption is Tao's Syracuse random
    variable (Forum Math. Pi 10 (2022) e12, Lemma 1.12 and Remark 1.13), in the
    present normalisation; the block coordinate's 3-adic past-limit has the law of
    Syrac(Z_3)/2.
  - Its negative-time reading is Tao's own alternative to his positive-time
    indexing, at Remark 1.13, footnote 4 of arXiv v7.
  - The unconditional density line the hypothesis does not add to — Terras,
    Everett, Korec, Inselmann, Tao — is cited in Related work, with the horizons
    given in the step units in which they are proved.
  - The two further 3-adic studies a reader of Tao's footnote will reach
    (Wirsching, Thomas) are cited and distinguished from the object appearing
    here.

  CALIBRATION.
  - The record is reported with the limits it does not reach past: block length
    L <= 2, pooled adjudicating estimates, and an altitude guard on the core that
    binds at finite size (2.6% of visits in the adjudicating run, moving the
    reported statistics at the third decimal).

  SCOPE OF v3.
  - No numbered theorem's claim is strengthened, weakened, or renumbered, and
    nothing new is proved in the paper. v3 reports two results established in the
    project record and not reproduced there: the sharpness construction of
    Section 4 and the base-case assembly of Section 5.
  - Verification pointers and script names are concrete throughout. The complete
    record is public at https://github.com/macindoe/collatz; Appendix A pins the
    commit at which every wiki section and script named in the paper is cited.
```

---

## 6. Projected page count — measured, not estimated

Every row below is a real `pdflatex` build of the full manuscript in the scratchpad, from an
unmodified copy of `paper/collatz-reduced-v3.tex` with the drop-ins of §3 applied.

| build | content changes | type | **pages** | material (pt) |
|---|---|---|---:|---:|
| baseline | none | 11pt / 1.1in | **18** | 10,808.6 |
| **Plan A** | C1, C2, C3, C5, C6, C6b, C7–C11, C15 (the reviewer's five items, executed) | 11pt / 1.1in | **16** | 9,663.9 |
| **Plan B** | Plan A + C12, C13, C14, C16, C17 (the full cut list) | 11pt / 1.1in | **15** | 9,382.1 |
| Plan B | + bibliography at `\footnotesize` | 11pt / 1.1in | 15 | — |
| Plan B | — | 11pt / **1in** | 15 | — |
| Plan B | — | **10pt** / 1.1in | **13** | — |
| Plan B | — | **10pt** / **1in** | **12** | — |
| baseline | none | 10pt / 1.1in | 15 | — |
| baseline | none | 10pt / 1in | 14 | — |

**Confidence: high, for the 15.** It is a compiled artifact of the exact drop-in text in §3, not a
projection. The only source of drift when a delegate applies this is whitespace and paragraph
boundaries; the plan touches no float, no display, and no theorem environment, and introduces no new
over/underfull box.

**Confidence: high, for "12–13 is not reachable by content cuts."** The arithmetic is forced.
`\raggedbottom` with no floats makes physical pages ≈ `ceil(material / 633.6)`, so 13 pages needs
material ≤ 8,237 pt and 12 needs ≤ 7,603 pt. Plan B leaves 9,382 pt. What remains in the document at
that point is: §2+§3+§4's theorem statements and proofs (4,046 pt before Plan B's small trims), §5's
untouchable core (Hypothesis 5.1, both displays, Lemma 5.2, the definitions of `W_{k,D}` and
`\pi_{k,D}`, and the clauses carrying (R2)–(R5), ~950 pt), the bibliography (644 pt), Appendix A
(220 pt), the author's note (220 pt), the title block (185 pt), the Discussion (165 pt), §1 (585 pt)
and Related work (619 pt). Those sum to roughly 7,600 pt of material that is either explicitly
protected by the brief, is a theorem or its proof, or is a correction. **There is no 1,145 pt of
discardable prose left.**

**The reviewer's target is reachable — by type size.** Plan B at 10pt is **13 pages**; at 10pt with
1in margins it is **12 pages**. That is a decision for the author about how the paper is set, not a
content cut, and it is offered here only because it is the honest answer to "can it be 12–13": yes,
and this is where the last three pages actually are. Note also that the baseline alone at 10pt is 15
pages — i.e. the type size is worth more than the reviewer's entire content plan. Recommend the
author decide the type size first, then apply the content plan, since the two compose.

---

## 7. What I recommend against

### 7.1 Cutting anything from Related work

The reviewer does not propose it; I looked because the plan is short of pages, and I am recommending
against it. Measured contents: the classical line 74 pt; Terras/Everett/Korec/Inselmann/Tao 84 pt;
the horizons-in-steps clause 40 pt; the "what AEH asserts" clause 28 pt; **Wirsching 107 pt**;
**Thomas 42 pt**; the cycle literature and the verified range 40 pt; the contemporary human–AI work
and Rackl 81 pt; **the provenance and division-of-labor statement 123 pt**.

* Three of these are attributions paid in round 2 (Inselmann's horizon in its own unit, Wirsching,
  Thomas). Shortening them is exactly the kind of edit that loses a distinction someone worked to
  establish — Wirsching's Haar limit versus the `2^{-a}`-weighted law, `(2/3, 1/3)` against
  `(1/2, 1/2)`; Thomas's `N^{0.9999}` counting function against a constructed limiting measure.
* The Wirsching "siblings in shape" sentence is **paper-only** (see §4). Cutting it costs 28 pt and
  buys an unrecorded deletion or a second wiki landing. Not worth it.
* The Rackl sentence is prior-art clearance from the novelty sweep. Deleting a negative prior-art
  finding to save two lines is a bad trade.
* The provenance statement carries the priority claim (the coordinate system is the author's
  invention, hand-drawn note of 13 March 2023, predating the collaboration). It overlaps the author's
  note and Appendix A in tone but not in content, and both of those are protected.

### 7.2 Cutting Theorem 4.4's proof outline

195 pt, and it looks like a candidate because "Full details are in the project record". But
Theorem 4.4's own statement says "the derivations, not the theorems, are the contribution", so the
outline *is* the contribution's exhibit. Measured saving from a sensible compression: ~30 pt. Not
worth the risk of the sketch ceasing to be checkable.

### 7.3 Re-tightening the round-5 display

Not proposed, and not done. It is left byte-identical, on its two `gathered` lines. Recorded here so
the applying delegate has it in writing.

### 7.4 The reviewer's phrasing of the calibration sentence, taken literally

"No residual discrepancy was detected within the tested `L ≤ 2` cells under the stated protocol"
folds three qualifications into one clause and leans on "the stated protocol" to carry the pooling
and the altitude guard. If the three qualifications are then trimmed as redundant — which is the
natural next step for someone cutting length — the (R4) narrowing is gone. §3.7's version keeps the
reviewer's improvement (no "unqualified") and keeps all three limits explicit and named. Saving from
the reviewer's shorter form over mine: about 45 pt. I recommend against taking it.

### 7.5 Bibliography at `\footnotesize`

Measured: it does not change the page count (still 15). It only makes the references harder to read.
Recommend against.

---

## 8. What I could not settle

1. **Where the repair history goes.** The brief is right that the release description is the
   author's. §3.1's version note ends by pointing at it. If the author decides otherwise — a
   `HISTORY.md` in the repo, the Zenodo description, an appendix — that last sentence changes. **The
   applying delegate must not pick.**

2. **`aeh.md`'s own status line.** It reads "bulk uniformity confirmed **UNQUALIFIED** at every
   tested depth and cell, at block lengths `L <= 2`", and §13.5 *Status: resolved* repeats
   "**unqualified** … at block lengths `L ≤ 2`". After C16 the paper is strictly more conservative
   than the wiki on the same finding. That is not a defect in either — the wiki qualifies in the same
   sentence — but the divergence is real and this is a paper-only design pass. **Handed back, not
   changed.**

3. **The v2 note's status as a published artifact.** v2 is published, with a DOI, and it contains a
   Note. v3 replacing that Note with a current-status paragraph is normal errata practice, and §3.5's
   paragraph names the v2 note and says where it went. But whether the author wants the v2 text
   *reproduced* somewhere permanent (the release description, or `cycles.md` §12.8.6.3, which already
   keeps the superseded recipe "because the published v2 note points at it") is an editorial call I
   cannot make. The plain-text history at §5 reproduces its substance so the option is open.

4. **Whether `\S12.8.6.3` is the right pointer for the retired route.** §3.5's status paragraph sends
   a reader chasing the v2 route to `cycles.md` §12.8.6.3. That subsection does carry the superseded
   recipe, and §12.8.6.4 carries the `p = 22` episode and the instance record. I split the pointer
   between the release description and §12.8.6.3 rather than naming both subsections, to save a line.
   If the author prefers precision over the line, name `\S12.8.6.3--\S12.8.6.4`.

5. **The exact saving of C3, C5, C9, C10, C14, C15, C17.** These were measured in aggregate (Plan A →
   Plan B is 281.8 pt) rather than individually; the per-item numbers marked *(est.)* are line-count
   estimates. Nothing in the plan depends on them individually — the two page counts that matter, 16
   and 15, are measured builds.

6. **`open-problems.md` 11.12 (the indexing standardization) and the deferred prefix result** were
   not attempted and are not touched anywhere in this plan, per the brief.

---

## 9. Application order for the delegate who applies this

1. Land the `aeh.md` sentence at §4 **first**, or drop C14 and keep the `*`-density parenthetical.
2. Apply §3.1 (version note), §3.2 (abstract), §3.3 (roadmap), §3.4 (Remark 3.6).
3. Apply §3.6 (the one-clause cross-reference edit inside line 225) **before** §3.5, so the
   replacement of lines 231–237 does not orphan the reference.
4. Apply §3.5 (status paragraph, replacing lines 231–237 including the `\subsection*` heading, the
   v2 note, the `\medskip`, and the correction).
5. Apply §3.7 (§5, replacing lines 239–465).
6. Rebuild. Expected: **15 pages**, one pre-existing underfull hbox in the `lagarias` bibliography
   entry, no other over/underfull boxes, no undefined references.
7. Do **not** change the Appendix A pin, the `\documentclass` options, or the `geometry` margins
   without the author's decision (see §6).
