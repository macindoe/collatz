# Findings: the v3 external-review corrections

**Branch:** `v3-external-review-corrections`.
**Base SHA actually cut from:** `e1c7d5f6d7ba0c0bb7d34df3fd44205ba8c4e7cb` — verified with `git rev-parse HEAD` before starting; the working tree was clean apart from the untracked brief.
**Pushed:** nothing. **Merged:** nothing. The branch is handed back checked out in the working directory.

**Tracked files edited:** `paper/collatz-reduced-v3.tex` and the rebuilt `paper/collatz-reduced-v3.pdf`, plus this file; and in round 2, the new `experiments/absorption_law.py` with its committed output (added under the author's ruling — see the round-2 section). No wiki page, no `sources/`, no `viz/`, no `README.md`/`index.md`/`publication.md`/`TOUR.md`/`HANDOFF.md` was touched.

**Diff, both rounds:** 36 insertions, 24 deletions in the `.tex` (round 2's two edits fell on lines round 1 had already touched, so the counts are unchanged); the PDF rebuilt; `experiments/absorption_law.py` and its output added in round 2.

**Encoding scan:** `python experiments/encoding_scan.py` → round 1 `369 tracked files … RESULT: CLEAN`; round 2, after the new script, `371 tracked files … RESULT: CLEAN` (0 non-UTF-8, 0 BOMs, 0 double-encoding signatures). Every edit was made with the file-editing tools; no `Get-Content`/`Set-Content` was used on a tracked file.

---

## The independent numerical re-verification

Fresh code, importing nothing from `experiments/`, exact integer (and `Fraction`) arithmetic at every decision. Run once, output quoted below verbatim in the relevant items. This script — the one that re-verified items 2, 3 and 4 — lives in the session scratchpad and is deliberately **not** added to `experiments/`: round 1's brief put `experiments/` out of scope. (Round 2 lifted that for one purpose only; the absorption-law check `experiments/absorption_law.py` is a *separate* and independently written file, and is committed. See R2-1.)

---

## Item 1 — §5's `π_k` depth clause. **Done.**

**Verified against the page, not the brief.** `aeh.md` §13.6.5 reads, in the page's own digits:

> the chain has `P(a=1) = 17/63`, `P(a ≥ 2) = 4/63`, `P(d=2) = 19/63` … against the exact bulk values `19/63`, `2/63`, `20/63`

and

> the depth histogram matches the exact law (`L1 ≤ 0.006` over `d ≤ 5`; `P(d=2) = 0.3192` vs `20/63 = 0.31746`) and rejects the chain law (`P(d=2)` off by `0.018`, `≈ 14` pooled standard errors)

and §13.6.4's qualifier **(q2)** (line 114) reads:

> Proposition `13.6.5` shows that chain's stationary law is **not** the exact bulk marginal — the exact one is the convolution law of `13.6.3`(v)

The brief's numbers all match the page. No discrepancy.

**Changed** (`paper/collatz-reduced-v3.tex` line 239): the depth clause of the `π_k` definition. It now names the exact renewal law of `13.6.3`(v) — `d_+ = m_+ + a_+` with `m_+` geometric(1/2) **independent** of `a_+` — quotes the marginal from `13.6.5` (`P(a_+=0)=2/3`, `P(a_+=1)=19/63`, `P(a_+≥2)=2/63`, `P(d=1)=1/3`, `P(d=2)=20/63`), and keeps the window chain in one clause as a `~1%`-accurate model, the resolution at which `13.4` recorded it. Three sentences plus two pointers; nothing else in §5 moved.

**Scope held.** `aeh.md` line 116 states the `ω`-residue/`s`-word component of `π_k` is exact and unqualified, so the `P(s=j) = 2^{-j}` ledger, the exact `1/3` 3-gain rate (from `lem:absorption`), and the drift sentence are untouched. AEH and its consequences were not rebuilt.

**Concluded on the abstract and §1:** neither needs adjustment. The abstract's "exactly computable product law" and §1's "an exact statement about an explicitly computable product law `π_k`" remain true — more exactly so now, since the depth marginal is a finite rational computation rather than a chain's stationary law.

---

## Item 2 — `thm:onestep` gains the stratum labels. **Done.** Counterexample re-verified.

**Fresh exact-integer output:**

```text
  (w,d) = (263,1):     A = 788    s = 2   C = 792    sigma = 3   a_+ = 2   m_+ = 1   w_+ = 11   d_+ = 3
  (w,d) = (2375,1):    A = 7124   s = 2   C = 7128   sigma = 3   a_+ = 4   m_+ = 1   w_+ = 11   d_+ = 5

  agreement at k = 1 (the window of thm:deltaM):
     w mod 2^(sigma+k+2) = w mod 64 :  7 , 7        equal
     d mod 2^(sigma+k)   = d mod 16 :  1 , 1        equal
     (s, sigma)                     : (2,3),(2,3)   equal
     a_+ mod 2^k                    :  0 , 0        equal
  outputs:
     a_+ : 2 vs 4     differ
     d_+ : 3 vs 5     differ
```

Both states sit in the third branch of `lem:absorption` (`s = 2` even, `h(2) = 1 + v_3(2) = 1`, `d = 1 = h(s)`), and the branch formula reproduces both values exactly:

```text
  (263,1):  d + v3(w + (2^s-1)3^(-d)) = 1 + v3(264)  = 1 + 1 = 2  = a_+
  (2375,1): d + v3(w + (2^s-1)3^(-d)) = 1 + v3(2376) = 1 + 3 = 4  = a_+
```

— a 3-adic function of `ω` that no 2-adic window sees at any `k`, which is `aeh.md` (q1) verbatim: *"`a_{+,n+1}` is not a function of any depth-`k` window at visit `n`, at any `k`."* The failure is not isolated: over `ω < 40000`, `d ≤ 16`, **121 of 4,774** depth-1 windows carry more than one `(a_+, d_+)`. With the labels `(s, σ, a_+)` present, all 283 label triples give a single `d_+`, since `d_+ = (σ−s)+a_+` identically.

**`thm:deltaM` is not contradicted, and stands unchanged.** `ΔM mod 2^k` agrees for the pair at `k = 1, 2, 3` (values `1,1` / `3,3` / `7,7`); from `k = 2` the `a_+` residues separate the two states, exactly as the theorem's data list requires.

**Changed:**
- line 160 — `thm:onestep` now opens by defining the depth-`k` window as the residues of `thm:deltaM` **together with the stratum labels `(s, σ, a_+)`**, matching `stage4.md` §11.8.7.6 in structure ("consists of the residues … together with the stratum labels `(s, σ, a_+)`"). Its proof already said `d_+` "is exact from the stratum data"; statement and proof now agree.
- line 152 — `thm:deltaM`'s trailing clause kept, with a qualifier.
- line 37 (abstract) — "A finite window of digits, **together with the step's stratum labels**, consequently decides each step…". One clause. The reviewer's "countable shell-indexed chart" framing was **not** adopted.

**Judgement call, made and justified.** I **kept** `thm:deltaM`'s clause "and the stratum data `(s,σ)` are determined by the same residues" and added the qualifier that it does not extend to `a_+`. I did **not** promote all three to labels there. Reason: `stage4.md` Theorem `11.8.7.3.1` makes the identical `(s, σ)` claim and lists `a_+ mod 2^k` as an *input residue*; promoting `a_+` to a label in `thm:deltaM` would contradict the record's own theorem and would weaken `thm:deltaM`, which the brief forbids. The three-label form belongs to the *window* (`11.8.7.6`), which is precisely where it now sits in the paper.

---

## Item 3 — `thm:vlaw`'s Baker bound at `d = 1`. **Done, with a discrepancy to record.**

**Fresh output:**

```text
  (w,d) = (3,1): Y = 3^d w = 9, Y mod 8 = 1 -> lifting = True
  s = v2(3^d w - 1) = v2(8) = 3
  RHS as printed:  C(w)*(log 1)^2 = 0     ->  the claim s <= 0 is FALSE
  w < 200, d = 1: 67 of 67 states have s > 0  (3w-1 is always even)
  largest s at d = 1 for w < 100000:  s = 17 at w = 43691
```

**Changed** (line 115): `s \le C(\w)(\log d)^2` → `s \le C(\w)\,(1 + \log d)^2`.

**DISCREPANCY — the brief's diagnosis is right about the paper but the record is not wrong.** `stage1-synthesis.md` Corollary `11.8.3.11.1` states the bound as

> `s(ω, d) <= C(ω) · (log d)^2      for all d >= 2`

i.e. the record *already carries a `d ≥ 2` guard*, and the paper dropped it when importing. The repair I made is a strengthening of that guard rather than a new claim: `(1+\log d)^2 > (\log d)^2` for every `d ≥ 1`, so the record's statement on `d ≥ 2` is implied, and the printed inequality is now finite and true at `d = 1` as well. Either repair would have been defensible; I chose the brief's because it removes the range restriction from the reader's path rather than adding one.

**Smaller wart NOT fixed (out of scope, and it is a record-level issue too):** the pinned constant `C(ω) = 208·log 9·log ω` (`stage1-synthesis.md` §11.8.3.11) is **zero at `ω = 1`**, so both the record's form and the paper's form degenerate on that single core. The paper writes only "an effective `C(ω)`", so it is not literally false; but if the pinned formula is ever printed, `ω = 1` needs a word. Author-side.

---

## Item 4 — `def:reduced` requires `ω > 0`. **Done.**

**Fresh output:**

```text
  (w,d) = (-1,1) satisfies every printed condition: w odd, 3 does not divide w, d >= 1
  A = 3^d w - 1 = -4 ;  s = v2(A) = 2 ;  C = A + 2^s = 0
  sigma = v2(0) : undefined ;  a_+ = v3(0) : undefined   ->  F undefined at (-1,1)
```

**Changed** (line 64): "a pair `(ω, d)` with `ω` odd **and positive**, `3∤ω`, `d ≥ 1`".

**Nothing downstream silently assumed it, and the addition is safe:** with `ω ≥ 1`, `d ≥ 1` we have `C = 3^d ω − 1 + 2^s ≥ 4`, and a sweep over `0 < ω < 20000`, `1 ≤ d < 25` returns `min C = 4` at `(1,1)`. `prop:block` already ranges over positive odd `x`; `thm:equiv`'s fixed point `(1,1)` and every cycle statement are unaffected.

**Beyond the brief:** `(-1,1)` is not the only degenerate state. Exhaustively over `−999 < ω < 0`, `d < 12`, the states with `C = 0` exactly are

```text
  (w, d, s) = (-455, 2, 12), (-341, 1, 10), (-85, 1, 8), (-7, 2, 6), (-5, 1, 4), (-1, 1, 2)
```

so the positivity condition closes a family, not a single point.

---

## Item 5 — `thm:uniform`'s `n_0(p)`. **Done.**

Imported verbatim in content from `cycles.md` Corollary `12.8.2` ("any period-`p` cycle has `n <= n_0(p)`, **the unique solution (in `n`) of**"):

```text
0.585·n / (1.585^p - 1)  =  log_2(p) + (p + 13.3·(0.46057 + log n)) / log 2
```

printed in the paper's own notation, `(\LL - 1)n / ((\LL)^p - 1)` on the left. The Rhin pin is imported as `12.8.2` takes it from `12.5.3`: `K log 2 − n log 3 > exp(−13.3·(0.46057 + log n))`. **Changed** at lines 210–213. The corollary's surrounding claims — the `n_0(p)` table, the `Λ`-conversion derivation, the crossover reading — are **not** restated.

One structural follow-up commit: the Rhin form inline overflowed the measure by 42.9pt inside the italic theorem body, so it is displayed. No wording change.

---

## Item 6 — `hyp:aeh`'s limit. **Done.**

`aeh.md` Theorem `13.6.4` reads:

> call a statistic's *bulk frequency* its empirical frequency over the visits with `x_exit > X`, in the limit orbit length `→ ∞` then `X → ∞` (exactly `13.2.1`'s regime)

**Changed** (line 242): the hypothesis now states the order explicitly — "the two limits taken in the order *orbit length → ∞ first, then X → ∞*" — and drops the muddled "for every `k` and `X`" quantifier in favour of "for every `k`", with `X` living in the limit.

**Changed** (line 245): one new sentence handles the reviewer's real sub-point, from `13.6.6`'s bottom-regime paragraph ("for them the unrestricted statement is not merely unproved but false on every convergent orbit … so the bulk cut is precisely what makes the integer question nondegenerate"): the cut is load-bearing, the unrestricted version is false on every convergent orbit, and **at a fixed cut a given orbit need not supply a growing qualifying set**.

**Deliberately not done:** `13.6.4`'s equivalence theorem was not imported, and the natural-density-of-starting-values quantifier of `13.2.1` was **kept**. `13.6.4` is orbit-by-orbit with no measure on starts, but `13.2.1` — not `13.6.4` — is the hypothesis the paper states, and the brief scoped this to the hypothesis statement.

---

## Item 7 — `prop:budget` becomes a heuristic. **Done.**

`stage4.md` §11.8.7.7: *"The consumption identity is proved; the conclusion drawn from it … is the organizing heuristic, not a formalized theorem."*

**Changed:** a `heuristic` environment sharing the `theorem` counter is declared (line 13), `prop:budget` uses it (line 167), and the three cross-references read "Heuristic~\ref{prop:budget}" (lines 53, 175, 246). Numbering is unchanged because the counter is shared; the label name `prop:budget` is kept so nothing else moves; no content is deleted. One sentence added inside it, in the record's own words, separating the proved consumption identity from the conclusion.

**Changed** (line 175): "…and a rigidity question for cycles (Section 4)**, and nothing else**" → "…**; we know of no residual content outside those two**".

---

## Item 8 — the v3 correction paragraph. **Done.**

**Scope sentence verified against `cycles.md` §12.8.6 and left alone — it matches.** The page's own Scope paragraph reads:

> unconditionally for every `p >= 16` (`12.8.6.1` → `12.8.6.2`), by finite check for `3 <= p <= 15`, and by direct exhibition at `p ∈ {2, 4}`, which lie outside `12.8.6.2`'s reach

and

> the constructed family's `γ` is bracketed between two absolute constants, `3.683012` and `5.140212` (`12.8.6.1`)

The paper's `3.683012`/`5.140212` and its three-part scope match to the digit.

**Changed** (line 235): one clause added after the "two halves compose to a proof" sentence — the proof "is established in the project record at the reference below and is *not reproduced in this paper*; Theorem `thm:staircase` and its hedge stand above exactly as written."

**Author's decision honoured:** `thm:staircase` and its hedge are untouched, §4 is not restructured, nothing else in §4 moved.

---

## Item 9 — `thm:smallp`'s pointers. **Done. One brief number was wrong.**

Every section number was resolved on `cycles.md` before printing:

| printed | resolves to |
|---|---|
| `12.2.3` | **Theorem 12.2.3** (period-1 classification) ✓ |
| `12.5.3` | **Theorem 12.5.3** (period-2 classification) ✓ |
| `12.7.5` | **Theorem 12.7.5** (period-3 classification, complete) ✓ |
| `12.5.2` | **Lemma 12.5.2** (size trim) ✓ |
| `12.7.4` | **Lemma 12.7.4** (period-3 trim) ✓ |
| `12.6.2` | **Lemma 12.6.2** (ceiling forcing) ✓ |

**THE BRIEF IS WRONG HERE.** It asked for "the trim lemmas at `12.6`/`12.7.4`". §12.6 is *"The General Elimination and the Ceiling Lemma"* and contains **no trim lemma** — it holds Proposition `12.6.1` (the general elimination) and Lemma `12.6.2` (ceiling forcing). The two trim lemmas the paper's proof outline actually invokes ("budget-trim lemmas … force `0 < K log2 − n log3 < 2^{c−n/5}` resp. `2^{3−0.115n}`") are **`12.5.2`** and **`12.7.4`**. I printed those, and cited `12.6.2` separately for the ceiling that supplies `K = ⌈n log_2 3⌉` (the outline's searches depend on it via `cycles.md`'s own K-completeness method note).

The theorem is **not** relabelled: its proof is already headed "Proof outline" and the statement already says the derivations, not the theorems, are the contribution.

---

## Item 10 — script filenames and one commit pin. **Partly done. One real obstruction.**

Every script was **opened and run** before its name was printed.

| script | run output | paper's figure | verdict |
|---|---|---|---|
| `one_step_propagation.py` | `k=4: 9986 steps, 9711 decided, 0 errors, 275 undecided, 0 violations` + `k=8: 11310, 11289, 0, 21, 0` | 21,296 steps / 21,000 decided / 0 errors / 296 flagged / 0 violations | **exact match** (9986+11310 = 21296; 9711+11289 = 21000; 275+21 = 296) |
| `period1_cycles.py` | `period-1 solutions for m <= 20000: [(1, 1, 0, 1)]`; direct search `{((1,1),)}` | "exact search kills `m ≤ 20,000`" | supports |
| `period2_cycles.py` | 19 open-window `n`; 11 exact size-passing checks, the only one degenerate; `nontrivial period-2 solutions: NONE` | "exact searches to `n = 20,000` find no solutions" | supports |
| `period3_cycles.py` | `76` values of `n`; `886` exact big-integer tests; `51` size-passers; `4798` audit cells, 0 violations; `NONE` | same | supports |
| `anchor_increment.py` | header + `stage4.md` §11.8.7.4 record | named for `thm:deltaM` | supports |

**Commit pin: `e1c7d5f`** — this branch's base, and the commit at which the DOI was stamped. It is the tree every section number and script name above was read from, so it is the pin that makes the citations checkable. No reason was found to prefer a different one. Added to Appendix A (line 263) without weakening it.

### OBSTRUCTION — `rem:verify1` has no runnable script, and one of its figures has no record at all

`rem:verify1` quotes three figures. Searching all 69 scripts in `experiments/` and every wiki page:

- **62,937 valid states, `ω < 3000`, `d < 64` (entry-depth law)** — recorded verbatim at `stage3.md` §11.8.6.3, "Numerical verification". **No script in `experiments/`.**
- **8,000 random states (valuation law)** — recorded in `stage3.md`'s status header ("8,000 random states re-checked 2026-07-06") and in `AGENTS.md`'s "Before marking anything proved". **No script in `experiments/`.**
- **60,000 random states including 341 boundary cases `d = h(s)` (absorption law)** — appears in **no wiki page anywhere**. It occurs only in `sources/paper/collatz-reduced-v1.tex`, `paper/collatz-reduced-v2.tex` and `paper/collatz-reduced-v3.tex`. It has been carried in the paper since v1 with nothing behind it in the record.

I therefore could not name a script here, and did not invent one. `"Scripts accompany the paper."` was replaced by the two pointers that do resolve (`stage3.md` §11.8.6.3 and that page's status header). **Appendix A was not weakened**, as instructed — which means that, for this one remark, Appendix A's *"every computational claim cites a runnable script"* is **not yet true as written**. This needs an author-side decision: either restore the draft-era verification code into `experiments/` (which would also give the 60,000/341 figure a record for the first time), or soften that clause of Appendix A. It is not fixable inside this brief's scope, since `experiments/` and Appendix A are both out of bounds.

---

## Item 11 — `M_t` versus `M(ω)`. **Done.**

**Checked `cycles.md` first, as instructed.** Proposition `12.6.1` uses exactly this symbol for exactly this object:

> `M_t = Σ_(j>t) m_j`

**Judgement call, made and justified: keep `M_t`, add a disambiguating parenthetical** (line 184). Renaming in the paper would desync the paper's central cycle identity from the page that carries its proof, the transport recurrence (`12.6.1.1`), the descent lemma (`12.6.1.4`) and every verified instance — a permanent cost, paid to avoid a collision the reader meets exactly once and which a clause dissolves. The parenthetical says `M_t` is a partial sum of entry depths, unrelated to the anchor `M(ω)` of §2, and that it is the record's notation, kept so paper and record read together.

---

## Item 12 — bibliography. **Done, with one flag.**

- **Yu I–III** split into properly citable form under the same key (so no `\cite` site moves): Acta Arith. 53 (1989), 107–186; Compositio Math. 74 (1990), 15–113; Compositio Math. 91 (1994), 241–276. This also removes an outright error: the entry said "Compositio Math. (1989–2007)", but part I is *Acta Arithmetica* and no part is from 2007.
  **FLAG:** these three volume/page numbers are **not** in this repository's record — the record has only "K. Yu, *Linear forms in p-adic logarithms*" (`publication.md` line 18). They are standard citations supplied from outside the repo and the author should confirm them before publication.
- **Rhin/Wu** completed from what the repo already knows: `cycles.md` §12.5.3 pins "Progr. Math. 71, Birkhäuser 1987, p. 160"; `briefs/merle-la7-rhin-check-findings.md` §2(a) pins the volume as *Séminaire de Théorie des Nombres, Paris 1985–86*, pp. 155–164, Proposition p. 160; the same file item 4 pins Wu as *On the linear independence measure of logarithms of rational numbers*, Math. Comp. **72** (2003), no. 242, 901–911.
- **`llmcollatz` (arXiv:2603.11066)** left exactly as it stands. The record has no authors for it either and none were invented. **Author-side lookup.**

---

## Item 13 — the build. **Done. Gate met.**

**Failure reproduced first** (sandbox temp dir, source copied out of the mount):

```text
pdflatex -interaction=nonstopmode -halt-on-error collatz-reduced-v3.tex   -> EXIT 1
! Missing $ inserted.
<inserted text> $
l.30
!  ==> Fatal error occurred, no output PDF file produced!
```

Line 30 is `\maketitle`; the cause is line 26's `\;` and `\cdot` in the `\date` argument, both math-mode-only. Confirmed that the committed PDF exists only because the build ran without `-halt-on-error`: the same source without that flag produces a PDF with 0 overfull boxes and 11 pages.

**Fix:** the separator is wrapped in `$…$`, chosen precisely so the rendered result is identical. Verified: `pdftotext` of the old and new title blocks are **byte-identical** on the date line (`v3, August 2026 \267 DOI: …`, octal dump compared).

**`\hypersetup` added** (line 29). `pdfinfo` before: `Title:` blank, `Author:` blank. After: `Title: Reduced coordinates for the Collatz map: exact per-step laws, anchor dynamics, and the limits of counting arguments for cycles`, `Author: Ben Macindoe`.

**Acceptance gate met:** from a clean directory, `pdflatex -interaction=nonstopmode -halt-on-error` exits **0 on two consecutive runs**. Second run: **0 overfull boxes** (matching the baseline), 0 undefined or multiply-defined references. The build was done in the scratchpad; only the PDF artifact was copied back into `paper/`.

**Regression checks:** no clipping and no overfull-box regression (baseline 0, now 0); the DOI target `https://doi.org/10.5281/zenodo.21730505` and both `cycles.md` permalinks (`72ec88e`, `9d9d1ec`) are unchanged in the annotation stream. Page count 11 → 12, from the added text.

---

## Hygiene

**The v3 Version-note entry was rewritten in place**, not appended to, and **no v4 entry was opened**. It keeps the published-document register — what this version changes relative to v2, no dated narrative, no change log. The v1 and v2 entries are untouched.

---

## What this brief got wrong

1. **Item 9's "trim lemmas at `12.6`".** §12.6 holds the general elimination and the ceiling lemma, not a trim lemma. The trim lemmas are `12.5.2` and `12.7.4`. Corrected before printing (see item 9).
2. **Item 3's framing of `thm:vlaw`.** The brief implies the record shares the defect. It does not: `stage1-synthesis.md` Corollary `11.8.3.11.1` already carries a `d ≥ 2` guard that the paper dropped. The verdict (the paper's printed bound is false at `d = 1`) is right; the attribution is not.
3. **Item 10 is not fully achievable.** `rem:verify1`'s three figures have no script in `experiments/`, and the absorption figure (60,000 states / 341 boundary cases) has no record anywhere in the wiki. See the obstruction under item 10.
4. **Item 2's abstract clause is not the only site.** §1 line 55 ("A finite window of state digits then decides the next step in a trichotomy that never errs") and the Contributions list, item (iv) ("an error-free finite-window trichotomy for the next step"), carry the same unqualified reading. The brief named only the abstract and said "one clause, minimal", so **I left both** rather than widen the edit unasked. They should get the same qualifier.

## What I deliberately did not do

- **Did not touch any wiki page.** `aeh.md`, `stage4.md`, `cycles.md` were read only.
- **Did not add a script to `experiments/`** to cover `rem:verify1`, though that is the natural repair — `experiments/` is out of scope.
- **Did not fix `2^{c-n/5}` in `thm:smallp`'s proof outline** (line 204). The `c` is undefined in the paper; `cycles.md` Lemma `12.5.2` gives the constant as `6` (`0 < K·log 2 − n·log 3 < 2^(6 − n/5)`). This is a typo in a proof outline and correcting it is a mathematical content change outside items 1–2, so it is recorded, not made. **It should be `6`.**
- **Did not widen item 2's qualifier** to §1 or the Contributions list (see above).
- **Did not adopt the reviewer's "countable shell-indexed chart" framing**, per the brief.
- **Did not rebuild AEH or its consequences** (item 1's load-bearing instruction).
- **Did not push or merge.**

## Internal consistency with `aeh.md` §13.6 and `stage4.md` §11.8.7.6

**In my reading, yes, on the two points named.** `thm:onestep`'s window is now `stage4.md` §11.8.7.6's window, label for label; `π_k`'s depth component is now `aeh.md` §13.6.3(v)'s law with §13.6.5's marginal, and the window chain is demoted to the `~1%` model that §13.6.5 says it is. `thm:deltaM` and `stage4.md` `11.8.7.3.1` now say the same thing with the same caveat.

### Remaining drift noticed, out of scope to fix

1. **§1 and the Contributions list** still assert unqualified finite-window determinism (item 2 above).
2. **`thm:onestep`'s undecided rate.** The paper says "under the product law of Section 5 the undecided rate is `≈ 2^{-(k+1)}`". `stage4.md`'s Remark (undecided rate) derives that figure "under the **uniformity heuristic**", `P(lifting)·2^{-(k-1)} ≈ (1/4)·2^{-(k-1)}` — i.e. from a *uniform* depth/class assumption, which item 1 has just established is **not** `π_k`'s depth marginal. The measured rates (`0.0275` at `k=4`, `0.0019` at `k=8`) are unaffected, and the figure is stated as an approximation, so nothing is false; but the attribution "under the product law of Section 5" is now the wrong provenance for a number derived under uniformity. Small, real, and a wiki-side question as much as a paper-side one.
3. **`hyp:aeh` and `aeh.md` `13.2.1` share a residual imprecision.** With the cut fixed, a convergent orbit supplies only finitely many qualifying visits, so the inner "orbit length → ∞" limit is degenerate on exactly the orbits the conjecture says are all of them. The paper now says this out loud (item 6); the wiki does not, and `13.6.4` has the same shape. Not a defect in either statement's intent — `13.6.6` is explicit that the cut is what makes the question nondegenerate — but the two pages would read better if `13.2.1`/`13.6.4` carried the same sentence the paper now carries.
4. **`rem:verify1`'s absorption figure has no provenance at all** (item 10 obstruction). This is the one item on this list I would raise first.

---

## Round 2 — the author's rulings

Same branch, same discipline: per-item commits, content separate from structure, nothing pushed, nothing merged.

### R2-1 — Appendix A made true by re-running the check. **Done.**

**New file: `experiments/absorption_law.py`**, with its committed output `experiments/absorption_law_output.txt`, following the neighbours' convention (`anchor_increment.py`, `one_step_propagation.py`, `margin_asymptote_output.txt`, …): a module docstring naming the page and result it supports, `[PASS]`/`[FAIL]` lines, a `TOTAL: N checks, M failures.` footer, and a nonzero exit on any failure.

**What it supports**, stated at the top of the file: `stage3.md` §11.8.6.2 (Proposition 11.8.6.2.1, the exact 3-adic law for `C`) together with its sub-law `h(s) = v_3(2^s − 1)`, and the paper's `lem:absorption`. Every state is checked against **both** forms — the record's three-case comparison of `d` against `h(s)`, and the paper's case split on the parity of `s` — plus the paper's "gains a factor of 3 exactly when `s` is even" trigger.

**Independence is structural, not merely asserted.** The truth value is `v_3(C)` obtained by trial division of `C` and by nothing else; the predicted value is evaluated from `(ω, d, s)` through the law's branches and never sees `C`. Neither path can compute the other. The file imports nothing from any other script in the repository. All arithmetic is exact integer; no floating point appears anywhere. Deterministic (seed `40101`); the run was repeated and the output is **byte-identical**.

**The boundary branch is constructed, not waited for.** `d = h(s)` forces `s` even, and `h(s) = 1 + v_3(s)`, so `d = 1` needs `3 ∤ s`, `d = 2` needs `v_3(s) = 1`, `d = 3` needs `v_3(s) = 2`. Solving `v_2(3^d ω − 1) = s` exactly pins `ω` to one residue class mod `2^{s+1}`, which the script walks. Every such `(d, s)` with `s ≤ 44` is built: `d = 1` at fifteen values of `s`, `d = 2` at five, `d = 3` at two. Branch (ii), `d < h(s)`, is rare under sampling for the same reason and is constructed the same way.

**The run, verbatim from `experiments/absorption_law_output.txt`:**

```text
Part 1 (sub-law h(s), exhaustive s = 1..600)      0 failures
Part 2 (exhaustive, w < 20000, 1 <= d <= 40)      266680 states, 0 discrepancies
         branch counts: (i) h<d = 264354,  (ii) h>d = 106,  (iii) h=d = 2220
Part 3 (random, w < 2^64, d <= 200, seed 40101)    60000 states, 0 discrepancies
         branch counts: (i) h<d = 59897,   (ii) h>d = 7,    (iii) h=d = 96
Part 4 (BOUNDARY d = h(s), constructed)              880 states, ALL in branch (iii)
         d = 1 at s in [2,4,8,10,14,16,20,22,26,28,32,34,38,40,44]
         d = 2 at s in [6,12,24,30,42]
         d = 3 at s in [18,36]
         v_3(w + beta) histogram: {0: 440, 1: 308, 2: 88, 3: 44}
Part 5 (branch (ii) d < h(s), constructed)           420 states, all in branch (ii)
Part 6 (canaries)                                  (263,1) a_+ = 2 ; (2375,1) a_+ = 4
Part 7 (negative controls)                         both bite

Summary
  states verified          : 327980
    branch (i)   h(s) < d  : 324251
    branch (ii)  h(s) > d  : 533     (420 constructed)
    branch (iii) h(s) = d  : 3196    (880 constructed)

TOTAL: 983954 checks, 0 failures.
```

**Boundary cases the run actually hit: 3,196**, of which **880 were constructed**, spread deliberately over `d ∈ {1, 2, 3}`; the remaining 2,316 arose in the two sweeps (2,220 exhaustive, 96 random).

**The negative controls matter more than they look.** Dropping the boundary branch — i.e. using `min(d, h(s))` everywhere — is wrong on **140 of 280** constructed boundary states, not all of them. That is the honest shape of the thing: on the boundary branch `a_+ = d + v_3(ω + β)`, and `v_3(ω + β) = 0` about half the time, in which case the truncated law coincides with the truth by accident. **So a sampler that merely lands on boundary cases has roughly even odds of missing the defect on each one** — which is precisely why the branch had to be constructed and counted rather than sampled and hoped for. It is also, exactly, why the `(263,1)`/`(2375,1)` pair could sit undetected behind Theorem 3.8.

**`rem:verify1` rewritten** (`paper/collatz-reduced-v3.tex` line 146) around the numbers this run produced, with the script named. The unsupported "`60,000` random states including `341` boundary cases `d = h(s)`" is **deleted**, not carried forward and not reproduced. The valuation-law (`8,000`) and entry-depth (`62,937`) figures are unchanged — those two do have a record — and the `stage3.md` §11.8.6.3 pointer is kept.

**One observation about the deleted figures, offered so the record is fair to them:** they were unreproducible, not demonstrably false. `341` boundary hits in `60,000` samples is `0.57%`, and my exhaustive small-depth sweep gives `2220/266680 = 0.83%` — the same order. My *random* sweep hit only `96` in `60,000`, but it samples `d ≤ 200`, which suppresses `d = 1` and hence the commonest boundary case. So the old figure is consistent with a small-`d` sampler. It still had to go: nothing in the repository could produce it, and Appendix A promises a runnable script.

**Appendix A was not weakened.** Every computational claim in the paper now cites either a runnable script or a record section that carries the check.

### R2-2 — `thm:smallp`'s undefined constant. **Done. `c = 6`.**

Verified against the page myself, three independent ways, all consistent:

- `cycles.md` **Lemma 12.5.2** states the trim as `0 < K·log 2 − n·log 3 < 2^(6 - n/5)` (line 101);
- **Theorem 12.5.3** quotes it back in the same form (line 106);
- the page's own arithmetic checks it: "the lemma's requirement is `< 2^(6 - 20001/5) = 2^(-3994.2)`" (line 114), and `6 − 20001/5 = −3994.2` exactly.

**Changed** (line 204): `2^{c-n/5}` → `2^{6-n/5}`. Kept to the constant. The period-3 companion `2^{3-0.115n}` already matches `cycles.md` Lemma 12.7.4 and is untouched.

**Small correction to the instruction, for the record:** the ruling says "`cycles.md` 12.5.3 gives `2^(6 - n/5)`". That is true as a *quotation site* — 12.5.3 does print it — but the lemma that *states* the trim is **12.5.2**, which is what the paper now cites for it (item 9, last round). No consequence; noting it only so the two citations are not later thought to disagree.

### R2-3 — §1 and Contributions (iv): left exactly as they are. **Recorded as known-open.**

Per the ruling, **not touched**. For the record, the two sites are:

- **line 55** (§1, prose summary): "A finite window of state digits then decides the next step in a trichotomy that never errs."
- **line 53** (Contributions, item (iv)): "an error-free finite-window trichotomy for the next step".

Both carry the unqualified reading that the abstract and `thm:onestep` now qualify: the deciding data is the residue window **together with the stratum labels `(s, σ, a_+)`**, and `a_+` is a 3-adic function of `ω` that no residue window determines at any `k` (`aeh.md` (q1); the `(263,1)`/`(2375,1)` pair). **Known-open, author's call, deliberately not made.**

### R2-4 — Does `stage3.md` owe a line? **In my reading, yes — and here it is, unmade.**

`AGENTS.md` is explicit on both halves. *"Before marking anything 'proved': run an independent numerical check (not the one quoted in the text — a fresh implementation), and record what was checked, the range, and the date in the page."* And, in Conventions: *"When a result is verified, record the current verification inline per the proved-claim workflow — what was checked, the range, the date, one line — and overwrite it next time rather than appending a new entry."*

§11.8.6.2 presently carries **no verification line at all** — the section runs from Proposition 11.8.6.2.1 through Corollaries 11.8.6.2.2–11.8.6.2.3 to the "Interpretation" paragraph and stops (the "Numerical verification" paragraph at line 611 belongs to §11.8.6.3, the entry-depth law). This round produced exactly the kind of check that rule asks for, so on my reading the section is owed one line. **I have not added it.**

The exact line I would add, immediately after the "Interpretation" paragraph closing §11.8.6.2 (i.e. at line 505, before the `#### 11.8.6.3.` heading at line 506) — a single current line, to be overwritten on re-verification rather than appended to:

> **Verified** (2026-08-01, `experiments/absorption_law.py`, fresh code importing nothing from any other script here; exact integer arithmetic, no floating point; deterministic, seed `31006`-style fixed, re-run byte-identical): `327,980` valid states — all `266,680` with `ω < 20,000`, `1 <= d <= 40`, plus `60,000` random with `ω < 2^64`, `d <= 200`, plus `1,300` constructed — each checked against this Proposition's three cases, against the paper's `lem:absorption` form, and against the `3`-gain trigger (`a_+ > 0` iff `s` even): `983,954` comparisons, `0` failures. The resonant branch `d = h(s)` is **constructed rather than sampled** — `3,196` states in all, `880` built explicitly at `d ∈ {1,2,3}` by solving `v_2(3^dω − 1) = s` exactly — as is the shallow branch `d < h(s)` (`533` states, `420` built); the sub-law `h(s)` is exhaustive for `s <= 600`. Two negative controls bite: dropping the resonant branch is wrong on `140` of `280` constructed boundary states (it coincides by accident whenever `v_3(ω + β) = 0`), and `h(s)` perturbed to `2 + v_3(s)` fails at all `99` even `s` tested.

(The seed is literally `40101`; substitute it when placing the line. I have written the sentence to the page's register rather than the paper's.)

**Not made — the author's call, and wiki pages are off-limits this round.**

### R2-5 — the `stage3.md` line, placed. **Done.** (Author-approved after R2-4.)

The one wiki edit authorised on this branch. `stage3.md` and nothing else in it.

**Where:** immediately after the "Interpretation" paragraph closing §11.8.6.2 ("…remains the next unresolved target."), before the `#### 11.8.6.3.` heading — exactly the position specified in R2-4. **Pure insertion: `git diff --stat stage3.md` reports `2 insertions(+)`, 0 deletions.** Front matter, the Current-state paragraph, and §11.8.6.3's existing "Numerical verification" paragraph are untouched.

**The placeholder is gone.** The drafted line carried "seed `31006`-style fixed" with a parenthetical telling the placer to substitute; the placed line reads `seed 40101` and carries no residue of that wording.

**Every figure re-checked against `experiments/absorption_law_output.txt` at placement**, one more time, as instructed — all eleven agree with the committed output:

| in the line | in the output |
|---|---|
| `327,980` states | `states verified : 327980` |
| `266,680` exhaustive, `ω < 20,000`, `1 <= d <= 40` | Part 2 header + `266680 valid states` |
| `60,000` random, `ω < 2^64`, `d <= 200`, seed `40101` | Part 3 header + `60000 random states` |
| `1,300` constructed | Part 4 `880` + Part 5 `420` |
| `983,954` checks, `0` failures | `TOTAL: 983954 checks, 0 failures.` |
| branch (iii) `d = h(s)`: `3,196`, `880` built | `branch (iii) h(s) = d : 3196 (the boundary; 880 of them constructed)` |
| built at `d ∈ {1,2,3}` | Part 4's three `[PASS] 4a` rows |
| branch (ii) `d < h(s)`: `533`, `420` built | `branch (ii) h(s) > d : 533`; `[PASS] 5a … 420` |
| `h(s)` exhaustive to `s <= 600` | Part 1 header + `[PASS] 1a … all 600 values` |
| control: `140` of `280` | `[PASS] 7a … WRONG on 140 of 280 constructed` |
| control: `99` of `99` even `s` | `[PASS] 7b … fails at 99 of 99 even s` |

**Reproducibility claimed no more strongly than it holds.** The placed line says "re-running it reproduces the committed output" — not "byte-identical". My own re-run was byte-identical (`diff -q`, LF both sides), but a re-run redirected through a shell that emits CRLF differs in line endings while reproducing the content, which is what the coordinator observed. The weaker phrasing is true in both cases.

**Register.** One current line, in the form `aeh.md` and `cycles.md` use (`**Verified** — script, conditions, date. …`), overwritable on re-verification rather than appended to. No change log, no dated narrative, no "was X, now Y". Every symbol it uses — `ω`, `d`, `s`, `h(s)`, `a_+`, `β` — is defined in §11.8.6.2 itself.

**One thing I did not do, deliberately:** the front matter's `updated: 2026-07-23` is now stale by this edit. `AGENTS.md`'s status-change workflow would ordinarily bump it, but the instruction was explicit that the front matter is not to be touched, and this is a verification record rather than a status change — the section's `status:` is unaffected. **Flagged, not made.** If the author wants it bumped to `2026-08-01` it is a one-field edit.

### Round-2 gates

- **Build:** rebuilt from clean. `pdflatex -interaction=nonstopmode -halt-on-error` exits **0 on two consecutive runs**; **0 overfull boxes**, 0 undefined or multiply-defined references. Title/author metadata still populated, DOI target and both `cycles.md` permalinks unchanged, 12 pages (unchanged from round 1). PDF rebuilt in the sandbox and copied back as the artifact only.
- **Encoding scan:** `python experiments/encoding_scan.py` → `371 tracked files … RESULT: CLEAN` (0 non-UTF-8, 0 BOMs, 0 double-encoding signatures). The new script is ASCII-only; all edits were made with the file-editing tools.
- **Scope:** files touched this round are `experiments/absorption_law.py` (new), `experiments/absorption_law_output.txt` (new), `paper/collatz-reduced-v3.tex`, `paper/collatz-reduced-v3.pdf`, and this file. No wiki page was edited.

### What I found wrong or worth flagging this round

1. **Nothing in the ruling was wrong on substance.** The one imprecision is the 12.5.2/12.5.3 attribution noted in R2-2.
2. **The boundary branch coincides with the truncated law about half the time** (140 of 280). This is the sharpest thing I learned this round and it is now on the record in both the script and `stage3.md`'s owed line: incidental sampling of the branch is *not* equivalent to testing it, because the branch only differs from `min(d, h(s))` when `v_3(ω + β) > 0`. Any future re-verification should construct, not sample.
3. **`stage3.md` §11.8.6.2 has never carried a verification line** (see R2-4). That is a pre-existing gap in the record, not something this round created — but this round is the first time there is a script to point it at.
