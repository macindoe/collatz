# Findings: verify round 2 and close the stale pointers (v3 round 2, Phase 3)

Branch `v3r2-review-round2`, verified at `3511a0d` (three commits on `e4dac49`). Read-only
git throughout; nothing committed, nothing pushed, no branch/checkout/stash/merge. The
Part 1 repairs below are left as uncommitted working-tree changes for the main session.

## What the round changed

`81e41e1` briefs only: five design briefs and five findings documents
(`v3r2-aeh-formulation`, `v3r2-contraction-literature`, `v3r2-staircase-scope`,
`v3r2-syrac-identity`, `v3r2-thomas-check`, `v3r2-wirsching-check`, plus the two apply
briefs). No tracked page touched.

`c2d465a` content, six files:

- **`aeh.md`** — `13.2` rewritten: the depth cap `D_k` is given its own job, `π_k`'s depth
  component becomes the exact convolution `d = m + a`, `m` geometric(1/2), `m ⊥ a`, with the
  values delegated to `13.6.5`; `13.2.1` restated as the **ensemble form** (uniform starts in
  `[N,2N)`, horizon `⌈θ log₂ N⌉`, one limit `N → ∞`) with two new explanatory paragraphs
  ("Why the ensemble…", "Base case…", the `θ < 1/4` theorem). `13.3.1`/`13.3.2`/`13.3.3`
  rescoped to density-of-starting-values; `13.3.2` renamed and now carries an explicit
  argument that **no drift or contraction consequence follows**. `13.4` gains the
  per-orbit/standing-rule reconciliation and the `x_exit` vs `ω_+` cut note. `13.6.4` gains
  the visit-family formulation; its `(q2)` is rewritten from a qualifier into a forward
  reference. `13.6.5` gains the **Tao attribution** paragraph. `13.6.6`/`13.6.7` rescoped.
- **`publication.md`** — Wirsching and Thomas checks written into the pinned-citations bullet
  and the landscape; Inselmann added as neighbour 4; the AEH verdict rebuilt into six
  sub-bullets (consequences subsumed, depth law attributed to Tao, residue unfound).
- **`itinerary.md`** — `14.15.3`(d) Wirsching sentence corrected (he `3`-adically completes
  the *root* of the predecessor tree and averages **predecessor**-counting functions).
- **`README.md`**, **`bridge.md`** — AEH's scope line brought to "ledger + 1/3 rate, density-zero
  set of starting values, finite horizon, no drift or contraction consequence".
- **`paper/collatz-reduced-v3.tex`** (+ PDF) — version note rewritten (eight repairs, correctly
  counted); Related work gains the unconditional-density-line paragraph (Terras, Everett,
  Korec, Inselmann, Tao) and the Wirsching/Thomas paragraph; `thm:staircase`'s assessment
  clause moved out of the theorem environment into `\paragraph{Sharpness evidence and
  assessment}`; §5 rebuilt (Tao attribution, joint labelled law, ensemble Hypothesis 5.1,
  the `θ < 1/4` base case, the reframed consequences paragraph); six new `\bibitem`s;
  digit-budget "proved identity" sentence removed.

`3511a0d` Appendix A pin `6a9183a → c2d465a` and the PDF rebuild. Nothing else in the tex.

---

## Part 1 — the stale pointers, applied

All five sites repaired; the matched pair edited together. Minimal, pointer-level wording
only; no numerical value touched, no anchor renumbered. `updated:` bumped to `2026-08-02`
on the three pages that carry front matter and did not already have it (`anchors.md`,
`index.md`, `reverse.md`); `itinerary.md` and `aeh.md` already read `2026-08-02`; `TOUR.md`
carries no front matter.

| site | before | after |
|---|---|---|
| `anchors.md` L59 | "bulk-form hypothesis (13.2.1)" | "ensemble-form hypothesis (13.2.1)" |
| `index.md` L26 | "precise bulk formulation (13.2)" | "precise ensemble formulation (13.2)" |
| `reverse.md` L62 | "AEH: orbit equidistribution (§13)" | "AEH: ensemble equidistribution (§13)" |
| `TOUR.md` L26 | "the bulk hypothesis conditions on a size cut and cannot see individual tails by construction" | "the hypothesis is a statement about uniformly sampled starting values over a prescribed finite horizon, so no individual orbit's tail is in its reach by construction" |
| `itinerary.md` L73 | "π_k (13.2) quantifies **along actual orbits**; AEH is … that **actual orbits' stratum words** equidistribute against the cylinder measure" | "π_k (13.2) quantifies; AEH is … that **the stratum words of the bulk segments of uniformly sampled starting values** (aeh.md `13.2.1`) equidistribute against the cylinder measure" |
| `aeh.md` L36 | "AEH is precisely the statement that **actual orbits' stratum words** equidistribute against the itinerary cylinder measure" | "AEH is precisely the statement that **the stratum words of the bulk segments of uniformly sampled starting values** (`13.2.1`) equidistribute against the itinerary cylinder measure" |

Notes on the edits:

- `index.md` keeps the pointer at `13.2` rather than `13.2.1`: the table cell lists §13's
  subsections in order (13.2, 13.3, 13.4, 13.5, 13.6) and changing one entry to a
  sub-subsection would break the pattern. Only the adjective changed.
- `anchors.md`'s trailing clause "AEH ⟺ bulk Bernoulli-genericity of the door letter word"
  was **left alone**: that is `13.6.6`'s own current wording ("bulk `B`-genericity of the
  integers' letter words") and is not retired.
- `reverse.md` §14.5.3 was not touched. Confirmed read-only: its "measured stationary depth
  distribution" sits beside "the depth law `2·3^(−d)`" and Theorem `14.5.1`'s mortality —
  the **backward tree's** depth law, not the forward window chain. Only L62 was edited.
- No `Get-Content | Set-Content` and no PowerShell redirection was used; all edits went
  through the Edit tool. Re-checked afterwards: `≤ — ε π ω ⊥ → ⇔ ≥ ℓ β θ ν` all decode
  correctly in every edited file, no `U+00C3`/`U+00E2 U+0080`/`U+00C2` mojibake and no
  `U+FFFD` anywhere.

**Does Part 1 invalidate the Appendix A pin?** No. The paper names `aeh.md` §13.1, §13.4,
§13.5, §13.6.3(v), §13.6.5 and `itinerary.md` §14.15.1.5. The `aeh.md` edit is inside §13.2
and the `itinerary.md` edit inside §14.15.2 — neither is a section the paper cites. The paper
names no section of `anchors.md`, `index.md`, `reverse.md` or `TOUR.md` at all. `c2d465a`
remains a correct pin after these repairs are committed.

---

## Part 2 — verification

### A. The Appendix A pin resolves — **PASS**

Every `\texttt{}` wiki section and every script named in `paper/collatz-reduced-v3.tex`
was extracted and resolved against `git show c2d465a:<file>`. Nothing missing.

Wiki sections (18 citations, 16 distinct anchors):

| file | anchor | resolves at `c2d465a` as |
|---|---|---|
| `stage3.md` | 11.8.6.3 | `#### 11.8.6.3. The target-shift lemma and the entry-depth law` |
| `cycles.md` | 12.2.3 | `**Theorem 12.2.3 (period-1 classification)**` |
| `cycles.md` | 12.5.2 | `**Lemma 12.5.2 (size trim)**` |
| `cycles.md` | 12.5.3 | `**Theorem 12.5.3 (period-2 classification)**` |
| `cycles.md` | 12.6.1 | `**Proposition 12.6.1 (period-p elimination)**` |
| `cycles.md` | 12.6.2 | `**Lemma 12.6.2 (ceiling forcing)**` |
| `cycles.md` | 12.7.4 | `**Lemma 12.7.4 (period-3 trim)**` |
| `cycles.md` | 12.7.5 | `**Theorem 12.7.5 (period-3 classification, complete)**` |
| `cycles.md` | 12.8.6 (×2) | `## 12.8.6. The Staircase at Every Period` |
| `aeh.md` | 13.1 | `## 13.1. Two regimes, one lesson` |
| `aeh.md` | 13.4 (×2) | `## 13.4. Calibration record (2026-07-08)` |
| `aeh.md` | 13.5 (×2) | `## 13.5. The (1 mod 8, d = 1) anomaly` |
| `aeh.md` | 13.6.3(v) | `**Lemma 13.6.3**` part (v), the renewal/product law |
| `aeh.md` | 13.6.5 (×2) | `**Proposition 13.6.5 (the depth marginal, exactly)**` |
| `itinerary.md` | 14.15.1.5 | `**Theorem 14.15.1.5 (the finite-itinerary cylinder theorem)**` |

Scripts (6, all present at `c2d465a`): `absorption_law.py`, `one_step_propagation.py`,
`anchor_increment.py`, `period1_cycles.py`, `period2_cycles.py`, `period3_cycles.py`.
All six are also present at `HEAD`.

Content spot-checks, not just existence: `stage3.md`'s status header does carry the
verification record `rem:verify1` cites ("62,937 states in the note; 8,000 random states
re-checked 2026-07-06"); `aeh.md` `13.4` does record the chain reproducing the orbit `d`-law
"to `~1%`", which is the resolution both the paper and `13.6.5` attribute to it;
`aeh.md` `13.5` does carry the standing rule in the exact words the paper quotes
("fixed-horizon, unweighted, per-visit sampling from uniform starts").

The two **URL** pins inside the v2 Note and its Correction also resolve, and contain what
they claim:

- `72ec88e` (v2 Note) — `cycles.md` §12.8.6 there is the *superseded* state:
  "all-p sharpness ASSESSED not proved… contiguous range `p ∈ {2,…,23}`… the Diophantine
  coverage bound of `12.8.6.1` now the sole open gap". Correct for what the Note describes.
- `9d9d1ec` (Correction) — `cycles.md` §12.8.6 there is the *proved* state:
  "all-p sharpness PROVED (12.8.6 — unconditional for p ≥ 16, finite check for 3 ≤ p ≤ 15,
  p ∈ {2,4} by exhibition)". Correct for what the Correction describes.

The pin points at `c2d465a` (the content commit) rather than at `3511a0d` (the commit
carrying the pin). That is the correct pattern and the one `643e864` established — a pin can
never name the commit that contains it. `3511a0d`'s diff to the tex is the pin string and
nothing else; the committed PDF carries `c2d465a` on p. 14, so PDF and tex are in sync.

### B. Paper and record agree — **PASS**, with one flagged sentence (item G3)

**What AEH is.** Paper Hypothesis 5.1 and `aeh.md` `13.2.1` are the same statement,
clause by clause: same sample space (`x` uniform among the odd integers of `[N, 2N)`), same
horizon (`T = ⌈θ log₂ N⌉`, `θ > 0` fixed), same cut family (`X_N → ∞`, `log X_N = o(log N)`),
same bulk restriction (`x_exit > X_N`), same weighting ("each qualifying visit counted once,
no per-orbit reweighting"), **one** limit (`N → ∞`), same quantifier tail ("for every
admissible `θ` and `(X_N)`"). The paper writes the density as `(2/N)·#{…}`, the correct
normaliser for the odd integers of `[N,2N)`.

One definitional difference, non-blocking: `aeh.md` `13.2` builds a **depth cap** `D_k` into
the window state (`(ω mod 2^(k+2), min(d, D_k))`, "the cap does one job, keeping the window
alphabet finite"); the paper's "depth-`k` window" is `thm:onestep`'s object (the residues of
`thm:deltaM` together with the labels `(s,σ,a_+)`) and carries no cap. Total variation is
still well defined without the cap, and the uncapped assertion implies the capped one, so the
paper is not claiming *less* than the record — but the two pages do not define "window"
identically and a reader crossing between them will notice.

**What it buys.** Paper's reframed consequences paragraph vs `aeh.md` §13.3: both give
(i) the ledger with error `O(2^{-k})` via the trichotomy, in density-of-starting-values form
over `⌈θ log₂ x⌉` bulk blocks; (ii) the exact `1/3` rate; (iii) explicit non-iteration, in
Tao's own terms; (iv) explicit non-exclusion of individual staircase tails; (v) explicit
statement that the exceptional set is a density-zero set of *starting values at a finite
horizon*, not a null set of orbits and not a tail statement. Neither states a descent or
contraction consequence of the hypothesis; both hand descent to Inselmann Cor. 1.4 / Thm 1.10
and the ledger's first moment to Inselmann Thm 1.6. `README.md` and `bridge.md` were brought
to the same line. **One residual sentence is flagged at G3 below.**

**`π_k`'s depth component.** Paper: `d_+ = m_+ + a_+`, `m_+` geometric(1/2), `m_+ ⊥ a_+`,
"so that it is the distribution of the depth, and not that of the absorption, which is the
convolution of the two" — the convolution now attaches to `d`, which was review finding (2).
`aeh.md` `13.2` states the same shape and explicitly delegates: "its depth marginal is
computed in closed form at `13.6.5`, which is where the values live." Inside the wiki the
values live in exactly one place (`13.6.5`); `13.2` and `13.6.4`(q2) point at it. The paper,
being a standalone artifact, restates the five values and points at `13.6.5` — appropriate.

**`13.6.5`'s Tao attribution.** Present in both, in the same form (`y_3 = Syrac(Z_3)/2`, the
`2^{-1}` unit explained by the renewal at exponents `≥ 2`, `a_+ = v_3(Syrac(Z_3)+2)`, values
read off Tao's printed `Syrac(Z/9Z)`, Lemma 1.12 and Remark 1.13). **Values unchanged and
identical in both:** `P(a_+=0)=2/3`, `P(a_+=1)=19/63`, `P(a_+≥2)=2/63`, `P(d=1)=1/3`,
`P(d=2)=20/63`. Verified in the committed PDF as well.

**The staircase scope.** Paper's Correction against `cycles.md` §12.8.6, item by item — all
match: `θ = 8 − 5·log₂3 = 0.0751874964…`; arc `[0.0415, 0.1169390665…]`; "any 66 consecutive
integers"; window `0.05·L^p`, "79 at `p = 16`", "`p = 16` is the first period supplying 66";
γ bracket `3.683012`–`5.140212`, both absolute constants; proof for every `p ≥ 16`;
`3 ≤ p ≤ 15` by finite check; `p ∈ {2,4}` outside the construction's reach, by direct
exhibition; the additive offset `1/(log₂3 − 1) = 1.70951` per block with no correction step;
"from `p = 8` upward not one working witness is a convergent or semiconvergent denominator";
"end to end at `p ∈ {3,…,26}`" (= `staircase_allp_diophantine.py`'s range) and "the
construction itself verified through `p = 32`" (= `cycles.md`'s "`p = 31` and `p = 32`
beyond that"). No numerical divergence found.

Two smaller cross-checks against the round's own findings documents also hold: the Thomas
sentence (`1/6 + 0.0215`, `N^{0.9999}`, "some class to frequency at least `2/9`") matches
`briefs/v3r2-thomas-check-findings.md` including the `2/9 > 1129/6000` pigeonhole; the
Wirsching sentence (`[0,1] × Z_3^×`, equal-weight inverse branches, Haar limit, `(2/3,1/3)`
where Haar gives `(1/2,1/2)`) matches `briefs/v3r2-wirsching-check-findings.md` §2.4.

### C. AGENTS.md compliance on every page touched — **PASS**

- No change log, no dated journal, no branch narration added to any tracked page. The only
  new dates are `updated:` front matter (schema-sanctioned) and two inline verification
  stamps in the "current verification, overwritten not appended" form the schema requires
  (`aeh.md` `13.6.5`: "Verified to precision `3^5` in exact rational arithmetic (2026-08-02,
  `briefs/v3r2-syrac-identity-findings.md`)"; `publication.md`: "confirmed in exact
  arithmetic (2026-08-02, …)").
- The round **removed** two pieces of "was X, now Y" prose rather than adding any:
  `13.6.5`'s "The chain **was, and remains**, a `~1%`-accurate model" became "The chain **is**
  a `~1%`-accurate model", and `13.6.4`(q2) stopped narrating a correction.
- `status:` lines are state phrases plus pointers, not diaries. `aeh.md`'s is long but every
  clause is a state, not an event. `publication.md`'s new "targeted checks ongoing" is a
  state.
- **The retired window-chain depth law is nowhere presented as `π_k`'s definition.** Grepped
  every tracked non-`briefs/`, non-`sources/` `.md`. The only surviving mentions are in
  `aeh.md` `13.2` ("a *different object*: a `~1%`-accurate model of this marginal"),
  `13.6.4`(q2) ("**not** this law … a model object internal to this record") and `13.6.5`
  (the explicit contrast, with the exact rationals). The one other hit is
  `paper/collatz-reduced-v2-review.md`, which is the archived v2 review text, not a live claim.
- **`13.6.4`(q2) no longer asks the reader to retroactively reinterpret `13.2`.** It now reads
  "forward reference, not a qualifier … Nothing here reinterprets a definition given
  elsewhere", and the header above it was corrected from "two qualifiers" to "one qualifier
  and one pointer". Confirmed.

Two minor AGENTS.md observations, neither blocking:

- `publication.md` L43 — "Attribution owed and given at aeh.md `13.6.5`; **every value there
  is unchanged** and was computed correctly." "is unchanged" is a statement about a diff, not
  a current fact. Harmless but it is the genre the schema discourages.
- `publication.md` L21 — "whose size coordinate carries the invariant density
  `φ' = (9/2)φ(3·)`". Per `briefs/v3r2-wirsching-check-findings.md` §2.3, the invariant
  density is `φ`; `φ'(x) = (9/2)φ(3x)` is the relation `φ` satisfies, and only on `[0, 2/3]`.
  A precision slip in the phrasing, not a wrong number.

### D. No anchor renumbered — **PASS**

Extracted the full set of `**Theorem|Lemma|Proposition|Corollary|Definition|Remark|Hypothesis|
Consequence N.N.N**` statements and `#`-headings from every page the round changed, at
`e4dac49` and at `HEAD`, and diffed. **Identical anchor sets on all five pages**
(`aeh.md`, `bridge.md`, `itinerary.md`, `publication.md`, `README.md`). `cycles.md`,
`stage3.md`, `spine.md`, `stage1.md`–`stage4.md`, `reverse.md` were not touched by the round.

The named anchors resolve to the same objects as at `e4dac49`:
`13.2.1` = the AEH statement (restated in place, same number, same role);
`13.6.4` = the genericity-form theorem (generalized from "one orbit" to "a visit family",
same object); `13.6.5` = the depth marginal (unchanged, with an attribution paragraph
inserted); `14.15.1.5` = the cylinder theorem (untouched); `12.8.6` = the staircase at every
period (untouched). Part 1 renumbered nothing.

Paper side: all `\ref` targets resolve to a `\label`, all `\cite` keys resolve to a
`\bibitem`, no bibitem is uncited, no duplicate keys — checked programmatically. Theorem
numbers are unchanged (Def 2.1, Thm 3.3, Thm 3.7, Thm 3.8, Heuristic 3.9, Prop 4.1, Thm 4.5,
Thm 4.6, Hyp 5.1). *Reference* numbers did shift — six bibitems were inserted at positions
2–7, so e.g. Steiner moved from `[2]` to `[8]`. Normal for a revision, and no in-text
numeric citation is hard-coded; recorded only so nobody is surprised.

### E. Encoding — **PASS**

`grep` for the three mojibake signatures (`U+00C3`, `U+00E2 U+0080`, `U+00C2`) across **every
tracked `.md`** (including `sources/`): zero hits.
Additionally decoded every page the round or Part 1 touched as UTF-8 and confirmed
`≤ — ε π ω ⊥ → ⇔ ≥ ℓ β θ ν` all present and correct, with no `U+FFFD`. The `.tex` compiles
to a 15-page PDF whose extracted text carries the round's new passages verbatim (ensemble
form, `Syrac(Z_3)`, `19/63`, Wirsching, Thomas, Inselmann, the `c2d465a` pin), so the
committed PDF is built from the committed tex.

### F. The five review findings — **all addressed**

1. **Hypothesis 5.1's sample space.** Addressed. The hypothesis is now over uniformly sampled
   odd starts in `[N,2N)` with a single limit `N → ∞`, and the paper spends a paragraph on
   *why* no single-orbit form survives (a convergent orbit's tail sits at `(1,1)`; above a
   fixed cut it supplies finitely many qualifying visits and eventually none, "in whichever
   order it is taken"). `aeh.md` `13.2.1` matches word for word in substance, and `13.6.6`
   was rewritten to say the same thing ("The bulk cut is **not** that restriction… What makes
   the integer question nondegenerate is the ensemble").
2. **`π_k`'s joint labelled law including `a_+`, and the convolution attaching to `d = m + a`.**
   Addressed, and this is the sharpest of the five. §5 now says the convolution is the
   *depth's* distribution and not the absorption's, and adds the joint labelled clause: the
   `ω`-residues Haar-uniform among odd residues and independent of the depth, carried on the
   residues **together with** the stratum labels `(s,σ,a_+)` that `thm:onestep` reads,
   `a_+` being a `3`-adic function of `ω` the `2`-adic window does not determine
   (`aeh.md` `13.6.3`(v)). `aeh.md` `13.2` was rebuilt to the same shape.
3. **`aeh.md` no longer defining `π_k` by the refuted stationary law.** Addressed. `13.2`'s
   old parenthetical ("depth distributed by the stationary law of the exact window chain,
   computed at depth 12: 0.333, 0.302, …") is gone; `π_k`'s depth is the convolution, the
   chain is demoted in the same paragraph to "a different object … internal to this record",
   and the depth-12 numbers moved to `13.6.5` where the contrast lives. Verified by grep that
   no page anywhere still defines `π_k` by the chain.
4. **Staircase status versus the version note's no-strengthening claim.** Addressed, and
   carefully. The old note said "No theorem or universal claim is strengthened" while v3
   reports a *proved* all-`p` result; the new note reads "No **numbered theorem's** claim is
   strengthened, weakened, or renumbered, and nothing new is proved here; v3 reports a
   stronger result established in the project record and not reproduced in this paper."
   The mechanism is the move of the assessment clause out of the theorem environment into
   `\paragraph{Sharpness evidence and assessment}`, disclosed in the note. This is
   internally consistent *given* the note's stated reading that a clause labelled "we assess
   … though not proved here" was never part of the theorem's claim — the paragraph now says
   exactly that ("This assessment is evidence for Theorem 4.6 and no part of it"). Also
   fixed in passing: the note's repair count, which said "four defects and three statements"
   (= 7) over a list of 8, now correctly says "eight repairs" over the same 8 items. I
   verified all eight are actually present in the tex.
5. **The digit budget's removed proved-identity claim.** Addressed. The sentence "The
   consumption identity of the first two sentences is proved; only the conclusion drawn from
   it is the organizing heuristic" is deleted; the environment is `\begin{heuristic}` and the
   note says "no part of it is now claimed as proved". Note the record is *stronger* here:
   `stage4.md`'s current-state paragraph still says "The digit-budget accounting (`11.8.7.7`)
   **proves** that each decided step consumes anchor digits nothing regenerates". The paper
   being the more conservative of the two is not a defect, but the two no longer say the
   same thing and someone may want them reconciled.

### G. Anything the round broke

**G1 (real, cross-page). `cycles.md` now describes the paper's structure as it was before
this round.** Three sentences say the assessment lives *inside* `thm:staircase`:

- L8 (Current state): "the question the published paper's `thm:staircase` **carries as
  assessed**"
- L301: "the same statement the published paper's Theorem `thm:staircase` **carries as
  assessed**"
- L360: "against the `O(log p)` the published `thm:staircase` **assesses**"

After the round, `thm:staircase` carries no assessment; `\paragraph{Sharpness evidence and
assessment}` does. `cycles.md` was not touched this round, so nothing was updated.
**Mitigating:** each sentence says *"the published paper"*, and in v1/v2 — the versions
actually published — the theorem did carry the clause. So these are true today and become
false the moment v3 is uploaded. They are a publication-time to-do, not a present error.
Same caveat applies to `publication.md` L39's "the hedge clause says 'not proved *here*'".

**G2 (real, in the tex — reported, not fixed).** Two descriptors in the v2 Note now point at
material that has left the theorem:

- L232 "Prompted by correspondence with Eric Merle concerning **this theorem's sharpness
  hedge**…"
- L232 "…we attempted a single period-parametrized construction procedure toward **the
  assessed claim of Theorem~\ref{thm:staircase}**"

Both were accurate while the clause sat inside the theorem. They are now loose. This is the
same defect family as the already-known "the hedge sentence above" at L234, which now
resolves to the `\paragraph` rather than the theorem — but it is two further instances, both
introduced by this round, and worth listing beside the known one. **No tex edit made.**

**G3 (real, in the tex — reported, not fixed). §5 still ends its unconditional list with
"and the classical negative drift follows".** The sentence is *true of the measure*
(`E_{π_k}[Δ log x] = 2 log 3 − 4 log 2 < 0`, since `E[m_+] = E[s] = 2`), and it sits before
the hypothesis is stated, so the version note's claim ("Section 5 no longer states a descent
or contraction consequence of Hypothesis 5.1") is technically correct. But it is immediately
followed by "the empirical question is only whether the orbits of typical starting values
follow `π_k`" — which invites exactly the inference `aeh.md` `13.3.2` now spends a paragraph
ruling out (equidistribution at each fixed `k` gives Fatou `liminf` bounds but no `limsup` on
`m_+`; the drift needs a uniform-integrability input equidistribution does not supply).
`aeh.md` `13.2`'s parallel "Supporting exact facts (unconditional)" list deliberately omits
drift. **This is the one place where the paper and §13.3 do not read the same**, and it is the
sentence a referee would pick. Recommended (for a future tex round, not this one): delete the
clause, or make it "and the classical negative drift is the mean of `π_k`", which is what it
means. **No tex edit made** — the PDF is committed and pinned.

**G4 (pre-existing, on a page the round touched). `publication.md` L39 still records the
superseded publication plan.** "The standing recommendation for the published record is
unchanged and remains the author's: wiki-only now; an erratum correcting only the v2 note's
gap sentence, **silent on the hedge**, once 12.8.6 is settled; **no v3 yet**." The repo now
contains a complete v3 with a stamped DOI (`10.5281/zenodo.21730505`), a full Correction that
is *not* silent on the hedge, and a rebuilt PDF. This was already stale at `e4dac49`, so the
round did not break it — but the round rewrote other bullets on the same page and left this
one, and it is the page that is supposed to own publication state. Also note the `status:`
line still reads "both papers published (paper 1 v2 DOI …21421120)".

**G5 (borderline, not repaired — outside the brief's five).** `anchor-digit-search.md` L37 and
L78 use "the bulk hypothesis" as a name for AEH ("not counterevidence to the bulk hypothesis";
"says nothing about the bulk hypothesis"). Both sentences are about the bulk/bottom split,
which survives the restatement intact, so they are not false — but they are the retired name.
`bridge.md` L48 likewise says AEH is needed "for **typical orbits**" where the round moved
everything else to "typical starting values". Neither site was on the brief's list and I did
not touch them; flagging for the main session's call.

### Already-known open items, confirmed still open

- **Abstract singular vs Contributions plural.** Abstract: "**Our main new theorem** is a sharp
  dichotomy for counting arguments". Contributions (v): "and --- **the main new theorems** ---
  a uniform trim … together with a sharpness family". Both present at HEAD, in the PDF.
- **The v2 note's "hedge sentence above"** now names a `\paragraph` rather than a clause of
  the theorem. Confirmed (L234). See G2 for the two further instances.
- **Length.** The committed PDF is **15 pages** against the reviewer's 12-page request.
  The round added roughly a page and a half net (the Related-work density paragraph, the
  Wirsching/Thomas paragraph, the rebuilt §5, six bibitems), partly offset by `\small` on the
  bibliography. Moving further from the target, not toward it.

### Stated plainly: what I could not verify

- **The external mathematics.** I did not read Tao, Inselmann, Wirsching, Thomas, Korec,
  Terras or Everett. Every claim about them was checked only for *internal* consistency —
  paper against `publication.md` against the round's own findings documents. If those
  findings documents mis-read a source, that error passes through this verification
  untouched. The one caveat the findings themselves record and `publication.md` does not
  surface: `briefs/v3r2-wirsching-check-findings.md` L126 flags an unresolved `[?]` — whether
  Lagarias's phrasing attaches `φ` to `Z_3^×` where Wirsching's (5.1) puts plain Haar there.
  The brief argues §2.4's exact tiling settles it either way; `publication.md` states the Haar
  verdict without the caveat.
- **I did not re-run any experiment.** Scripts were checked for existence at `c2d465a` and at
  `HEAD`, not executed. No numerical result in `aeh.md`, `cycles.md` or the paper was
  independently recomputed; the arithmetic I did check by hand is limited to the identities
  that close on themselves (`β = 2(2−log₂3) = 0.8301…`, `1/β = 1.2047…`, `4/β = 4.8188`,
  `1 − β/4 = log₂3/2 = log₄3 = 0.79248…` exactly, `E[σ] = E[s] + E[m_+] = 2 + 2 = 4`,
  `2/9 > 1129/6000`).
- **The PDF's typesetting** was verified only through `pdftotext`: page count, the pin string,
  and that the round's new passages are present. I did not inspect the rendered layout, so
  overfull boxes, a bad page break at the new `\paragraph`, or a widow in the rebuilt §5 would
  not have been caught.
- **`HANDOFF.md`** (124 KB) was grepped for AEH scope language and the retired names and came
  back clean, but it was not read end to end.
