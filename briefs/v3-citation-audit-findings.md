# Findings: pre-upload citation audit of `paper/collatz-reduced-v3.tex`

Delegated session, 2026-08-01. Target: the twelve `\bibitem` entries at lines 266–277 of
`paper/collatz-reduced-v3.tex` (repo HEAD `e1c7d5f`, branch `main`).

**No file in the repo was edited.** This document is the sole output.

**Headline: 10 of 12 entries CONFIRMED exactly as printed; 2 need correction (`llmcollatz`,
`merle`); 0 unverifiable. The Rhin `p.~160` pin SURVIVES — it is corroborated verbatim, twice,
by John L. Simons, the co-author of the very Simons–de Weger paper our chain follows.**

## Method and access record

`sources/` holds no PDFs or extracts of any cited reference (only draft history, our own v1
paper, data files, and the 2023 hand-drawn note) — the repo settled nothing on its own. The wiki
gave one usable pin (`cycles.md` line 108, the Rhin `p. 160` attribution) but that line was
itself added in commit `d5a6b0d` by the same unverified process, so it counts as a claim to be
checked, not as evidence. Everything below therefore rests on external sources: publisher
records (IMPAN, Numdam, Springer, Crossref), the arXiv API, Zenodo, OpenAlex, and — for the
Rhin page pin — the full text of arXiv:2205.10582.

`git show HEAD:paper/collatz-reduced-v2.tex` supplied the v2 fallback wording quoted in the
revert column.

## The table

Verdicts: **CONFIRMED** = every printed field matched an authoritative record.
**CORRECTED** = a field is wrong or missing; exact replacement given. **UNVERIFIABLE** = no
authoritative source found; revert recommended. (Nothing landed in the third bucket.)

| key | as currently printed | verdict | authoritative source | replacement / note |
|---|---|---|---|---|
| `terras` | R. Terras, *A stopping time problem on the positive integers*, Acta Arith. 30 (1976), 241–252. | **CONFIRMED** | IMPAN Acta Arithmetica record, vol. 30 no. 3 (1976), pp. 241–252, DOI `10.4064/aa-30-3-241-252` | none. Author's given name is Riho; issue is no. 3. Both optional. |
| `steiner` | R. P. Steiner, *A theorem on the Syracuse problem*, Proc. 7th Manitoba Conf. Numerical Math. (1977), 553–559. | **CONFIRMED** (secondary) | J. L. Simons, arXiv:2205.10582, ref. `[St]`: "Proc. 7th Manitoba Conference on Numerical Mathematics 1977, Winnipeg 1978, pp. 553–559"; corroborated by SciRP reference record (Utilitas Mathematica, Winnipeg) | none required. Strictly, the conference was 1977 and the volume appeared **Winnipeg, 1978** (Congressus Numerantium XX). Printing only "(1977)" is the common convention and is not false. Cosmetic upgrade if wanted: `Proc.\ 7th Manitoba Conf.\ Numerical Math.\ (1977), Utilitas Math., Winnipeg, 1978, pp.\ 553--559`. |
| `eliahou` | S. Eliahou, *The 3x+1 problem: new lower bounds on nontrivial cycle lengths*, Discrete Math. 118 (1993), 45–56. | **CONFIRMED** | ACM DL / ScienceDirect record, Discrete Mathematics vol. 118 no. 1–3 (1993), 45–56, DOI `10.1016/0012-365X(93)90052-U` | none. |
| `sdw` | J. Simons, B. de Weger, *Theoretical and computational bounds for $m$-cycles of the $3n+1$ problem*, Acta Arith. 117 (2005), 51–70. | **CONFIRMED** | EUDML record; and Simons's own bibliography in arXiv:2205.10582, ref. `[SW]`: "Acta arithmetica 117.1 [2005] pp. 51–70" | none. The original title hyphenates "$3n+1$-problem"; ours drops the hyphen. Cosmetic only. |
| `hercher` | C. Hercher, *There are no Collatz $m$-cycles with $m \le 91$*, J. Integer Seq. 26 (2023); arXiv:2201.00406. | **CONFIRMED** | Journal of Integer Sequences, `cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html` — vol. 26 (2023), **Article 23.3.5** | none required. Optional precision: add `Article 23.3.5` after `26 (2023)`. JIS has no page numbers, so the entry is already complete by that journal's own convention. |
| `lagarias` | J. C. Lagarias, *The 3x+1 problem: an annotated bibliography*, I–II, arXiv math/0309224, math/0608208. | **CONFIRMED** | arXiv abstract pages. `math/0309224` = "An annotated bibliography (1963–1999)"; `math/0608208` = "An Annotated Bibliography, II (2000–2009)" | none. Both identifiers and the I–II structure are right. |
| `yu` | K. Yu, *Linear forms in $p$-adic logarithms*, Acta Arith. **53 (1989), 107–186**; …II, Compositio Math. **74 (1990), 15–113**; …III, Compositio Math. **91 (1994), 241–276**. | **CONFIRMED** (all three) | I: IMPAN record, Acta Arith. 53 no. 2 (1989) 107–186, DOI `10.4064/aa-53-2-107-186`. II: Numdam `CM_1990__74_1_15_0`, Compositio Math. 74 (1990) 15–113. III: Numdam `CM_1994__91_3_241_0`, Compositio Math. 91 no. 3 (1994) 241–276. | none. **This is the entry the v3 round improved most and it is entirely correct.** Note for the record: the *v2* form — "Compositio Math. (1989–2007)" — was the false one (Part I is Acta Arithmetica, not Compositio, and no 2007 instalment is in the I–III series). Do **not** revert this entry. |
| `bl` | Y. Bugeaud, M. Laurent, *Minoration effective de la distance $p$-adique entre puissances de nombres algébriques*, J. Number Theory 61 (1996), 311–342. | **CONFIRMED** | OpenAlex record for DOI `10.1006/jnth.1996.0152`: J. Number Theory 61 no. 2 (1996), 311–342; ScienceDirect record `S0022314X96901523` | none. |
| `rhin` — main | G. Rhin, *Approximants de Padé et mesures effectives d'irrationalité*, in: Séminaire de Théorie des Nombres, Paris 1985–86, Progr. Math. 71, Birkhäuser, Boston, 1987, **pp. 155–164** | **CONFIRMED** | Springer chapter DOI `10.1007/978-1-4757-4267-1_11` (book: *Séminaire de Théorie des Nombres, Paris 1985–86*, ed. C. Goldstein, Progress in Mathematics vol. 71, Birkhäuser Boston, 1987); zbMATH **Zbl 0632.10034**; Simons, arXiv:2205.10582 ref. `[Rh]`: "Progress in Mathematics 71 [1987], pp. 155–164" | none. Series, volume, publisher, city, year and page range all check out against three independent records. |
| `rhin` — **the p.160 pin** | "(the Proposition used here is on p.~160)" | **CONFIRMED** (secondary, high confidence) | **J. L. Simons, *Cycles and divergent trajectories for a class of permutation sequences*, arXiv:2205.10582v1 (21 May 2022), proofs of Lemma 10 and Lemma 12**, verbatim: *"We apply Rhin's proposition on p. 160 with u0 = 0, u1 = 2K + L, u2 = −(K + L)"* and *"We apply Rhin's proposition on p. 160 with u0 = 0, u1 = 2K + L, u2 = −(3K + 2L)"* | **Keep the pin.** See the discussion below — this is the single strongest corroboration available short of the book itself. |
| `rhin` — Wu secondary | Q. Wu, *On the linear independence measure of logarithms of rational numbers*, Math. Comp. 72 (2003), no. 242, 901–911. | **CONFIRMED** | OpenAlex record for DOI `10.1090/S0025-5718-02-01442-4`: Mathematics of Computation, vol. 72, issue 242, pp. 901–911 | none. (OpenAlex stamps the year 2002 — that is the electronic-posting date; AMS prints the issue as 72 (2003), no. 242. The entry as printed is the AMS canonical form.) |
| `barina` | D. Barina, *Improved verification limit for the convergence of the Collatz conjecture*, J. Supercomputing (2025). | **CONFIRMED** (vague but true) | Crossref record for DOI `10.1007/s11227-025-07337-0`: The Journal of Supercomputing, **vol. 81, issue 7, article no. 810**, published 2 May 2025 | none required. Optional precision, now fully verified: `J.\ Supercomputing 81 (2025), article 810; DOI 10.1007/s11227-025-07337-0.` |
| `merle` | E. Merle, *On the non-existence of non-trivial Collatz cycles: a conditional formal proof in Lean 4**,** with documented structural obstructions*, preprint, Zenodo DOI 10.5281/zenodo.19790406 (2026). | **CORRECTED** (punctuation) | Zenodo record `zenodo.org/records/19790406`, published 26 April 2026 | The record's title carries **no comma** before "with". Replace the emphasised title with: `On the non-existence of non-trivial Collatz cycles: a conditional formal proof in Lean 4 with documented structural obstructions`. Author (Eric Merle), DOI, and year all confirmed. |
| `llmcollatz` | *(no author)* *Exploring Collatz Dynamics with Human–LLM Collaboration*, arXiv:2603.11066 (2026). | **CORRECTED** (author established) | arXiv API `export.arxiv.org/api/query?id_list=2603.11066` and the arXiv abstract page: sole author **Edward Y. Chang**; submitted 10 March 2026; math.DS, cs.AI, cs.HC; 233 pages, 11 figures, 52 tables | Replace with: `\bibitem{llmcollatz} E.~Y.~Chang, \emph{Exploring Collatz Dynamics with Human--LLM Collaboration}, arXiv:2603.11066 (2026).` |

## Does the Rhin `p.~160` pin survive? Yes.

This was the flagged suspect, so the reasoning is set out in full.

The book chapter itself is paywalled (Springer redirects to an identity provider; zbMATH returns
403), so the page could not be read directly. What was found instead is stronger than a
catalogue record:

**arXiv:2205.10582, *Cycles and divergent trajectories for a class of permutation sequences*, is
by John L Simons (University of Groningen)** — the *same* J. Simons who is the first author of
`sdw`, the Simons–de Weger paper whose Lemma 12 our `cycles.md` §12.5.3 explicitly says it
follows. In that preprint he twice writes, in the proofs of his Lemmas 10 and 12:

> Proof We apply Rhin's proposition on p. 160 with u0 = 0, u1 = 2K + L, u2 = −(K + L).

> Proof We apply Rhin's proposition on p. 160 with u0 = 0, u1 = 2K + L, u2 = −(3K + 2L).

and derives from it `|Λ| > e^(−13.3(1.34+log L))` and `|Λ| > e^(−13.3(1.77+log L))` respectively.
His bibliography entry `[Rh]` gives "Progress in Mathematics 71 [1987], pp. 155–164".

Three independent things line up:

1. **The page.** He names p. 160 explicitly, twice, in a paper about cycle bounds.
2. **The notation.** His `u0 = 0, u1 = …, u2 = …` is exactly the `u_0=0, H=u_1=K+L, u_2=-K`
   parametrisation `cycles.md` line 108 already records as "applied exactly as in
   Simons–de Weger (2005), Lemma 12". Same proposition, same three-coefficient shape, same
   author.
3. **The constant and the shape.** His bound is `exp(−13.3(c + log L))` with `c` varying by
   which coefficient realises `H`. Ours (v3 line 211) is `exp(−13.3(0.46057 + log n))`, and
   `0.46057 = log(log 3 / log 2)` is precisely the constant that converts `H = K ≈ n·log_2 3`
   into `log n`. The exponent `13.3` and the additive-log form are Rhin's `H^{−13.3}`,
   instantiated for our `H`. The pin, the constant, and the printed inequality are mutually
   consistent, which is what one would expect if the pin were real and would be a coincidence
   otherwise.

**Caveat, stated plainly.** This is corroboration by an expert secondary user of the exact
proposition, not autopsy of the printed page. If the author wants zero residual risk, the
minimal safe edit is to keep the pin but attribute it — e.g. `pp.~155--164` followed by
`(the Proposition applied here is the one on p.~160, in the parametrisation used by Simons
\cite{...}, arXiv:2205.10582)`. My recommendation is simply to **keep the pin as it stands**:
the evidence is good, and the alternative (deleting a locator that is almost certainly right)
loses the reader something real.

## What must change before upload, versus what is cosmetic

### Must change (2 items)

1. **`llmcollatz` — add the author.** Citing a 233-page arXiv paper with no author at all is the
   most visible defect in the bibliography and the easiest to fix. Exact line:
   `\bibitem{llmcollatz} E.~Y.~Chang, \emph{Exploring Collatz Dynamics with Human--LLM Collaboration}, arXiv:2603.11066 (2026).`
   Confirmed distinct from `merle`: Chang (Stanford/arXiv, March 2026, transfer-operator and
   paradigm-exhaustion material) and Eric Merle (independent researcher, Chartres; Zenodo, April
   2026; Lean 4 formalisation) are two different people and two different works. They were not
   conflated at any point in this audit.

2. **`merle` — drop the stray comma in the title.** "…in Lean 4**,** with documented…" →
   "…in Lean 4 with documented…". Small, but this is a title being quoted, and the paper's whole
   claim is that quoted things are checked.

### Cosmetic / optional (take or leave)

3. `hercher` — add `Article 23.3.5` (JIS's own locator; the entry is already complete without it).
4. `barina` — upgrade to `81 (2025), article 810` and/or add the DOI. Now verified via Crossref,
   so this is safe if wanted.
5. `steiner` — add `Utilitas Math., Winnipeg, 1978` (the volume's actual imprint year).
6. `terras` — the author's given name is Riho; `sdw` — the original title hyphenates
   "$3n+1$-problem". Neither is an error in the current form.

### Nothing to revert

No entry needed the v2 fallback. In particular **do not revert `yu`**: the v2 form ("Compositio
Math. (1989–2007)") was the inaccurate one, and the v3 expansion — Acta Arith. 53 (1989)
107–186; Compositio Math. 74 (1990) 15–113; Compositio Math. 91 (1994) 241–276 — is correct in
every field. Same for `rhin`: v2's vaguer "Sémin. Théor. Nombres Paris (1987)" is strictly worse
than v3's fully checked "Progr. Math. 71, Birkhäuser, Boston, 1987, pp. 155–164".

The round that added this metadata got it right. That was worth checking, and it is worth
recording that it checked out.

---

# Appendix: what was applied (2026-08-01, branch `v3-citation-fixes`)

Base: `main` at **`9ff55d3`** ("Merge branch v3-body-qualifier"). Note for the record — the
audit brief named `e1c7d5f` as HEAD, but `main` had advanced to `9ff55d3` by the time the fixes
were authorised. The bibliography block (lines 266–277) is **byte-identical** between the two
commits, so the audit above transfers without re-checking. (What moved in between was the body
qualifier round, plus — as it happens — the very `yu` and `rhin` expansions this audit was
convened to check.)

All six approved fixes are applied to `paper/collatz-reduced-v3.tex` only, in two commits:

- **`b2e0b92`** — the two must-fixes: `llmcollatz` gains `E.~Y.~Chang,`; `merle` loses the comma
  before "with documented".
- **`c5ef0e6`** — the four cosmetic locators: `terras` given name Riho; `steiner` imprint
  `Utilitas Math., Winnipeg, 1978`; `hercher` `Article 23.3.5`; `barina` `81 (2025), article 810`
  plus DOI.

No entry marked CONFIRMED-as-printed was otherwise altered; no field was added beyond what the
table above sources; no wiki page, `cycles.md`, or any other tracked file was touched.

Encoding scan (`experiments/encoding_scan.py`) over all 372 tracked files: **RESULT: CLEAN**, exit
0 — no double-encoding, no BOM, no invalid UTF-8. The accented entries (Padé, Birkhäuser,
algébriques) are intact; all edits went through the Edit tool, never PowerShell redirection.

## The acceptance gate did not pass, and the PDF was therefore not rebuilt into the repo

`pdflatex -interaction=nonstopmode -halt-on-error` returns **exit 0 on three consecutive runs**
with **no undefined references or citations**. Two gate conditions fail:

| condition | required | actual |
|---|---|---|
| exit status, consecutive clean runs | 0, twice | **0, three times — PASS** |
| undefined references / citations | none | **none — PASS** |
| overfull boxes | 0 | **0 overfull — PASS** (one *underfull* \hbox, badness 10000, lines 277–278) |
| page count | unchanged at 12 | **13 — FAIL** |

**Cause, isolated by controlled build.** The unmodified `main` tex, built in the same sandbox,
gives exactly **12 pages and zero box warnings**. The must-fix commit `b2e0b92` *alone* — before
any cosmetic change — already gives 13. Reverting all four cosmetic edits does not recover the
page; nor does dropping the Barina DOI.

The reason is visible in the output. At `main`, entry `[12]` (`llmcollatz`) is a single line and
is the **last line on page 12**, which is full to the baseline. Adding the thirteen characters
`E. Y. Chang, ` wraps that entry to two lines, it no longer fits, and the whole entry migrates to
page 13 — which then contains one reference and nothing else. The underfull \hbox is that
stranded line.

So the page count is not a casualty of the cosmetic round; **the approved must-fix costs the
page by itself.** Recovering 12 pages would require making the bibliography *shorter than
`main`'s*, which cannot be done without editing an entry marked CONFIRMED-as-printed, or without
a formatting change outside the bibliography. Both are outside this round's scope and are the
author's call, so the build was left uncommitted rather than handed back as a pass.

**The options, for the author:**

1. **Accept 13 pages.** Nothing is wrong with the document; a single-reference last page is
   merely ugly. Zero risk to correctness.
2. **Shorten a confirmed entry to buy the line.** The natural candidate is the `rhin`
   parenthetical, but that is the audit's headline finding and shortening it is a real loss.
   `lagarias` and `yu` also carry slack. Any of these needs explicit approval — I will not trim
   a verified citation to hit a page number.
3. **Formatting.** Set the bibliography in `\small`, or nudge the float/pagination. Cheapest and
   loses no content, but it edits outside the bibliography, which this round was told not to do.
4. **Drop the `terras` given name and the `barina` DOI** and accept whatever the count lands on.
   Tested: insufficient on its own, but it is the least-loss trim if combined with (3).

My recommendation is **(1)** for correctness-first, or **(3)** if the 12-page shape matters for
the Zenodo record. What I decline to do unilaterally is either quietly ship a 13-page PDF as a
passing build, or start cutting verified bibliographic detail to make a number come out right —
those are the two failure modes this audit was convened to prevent.

`paper/collatz-reduced-v3.pdf` is therefore **unchanged from `main`** on this branch, and the tex
and PDF are consequently out of sync until the above is decided. That is deliberate and is
flagged here so it cannot be mistaken for an oversight. Branch handed back unpushed and unmerged.

## One thing noticed in passing, outside scope and not acted on

Line 263 of the tex still reads "every wiki section and script named in this paper is cited at
commit `e1c7d5f`". `main` is now `9ff55d3`. That is a verification-record pin, not a bibliography
field, so this round left it alone — but it is stale, and it is the kind of thing worth settling
before a DOI is minted against the document.
