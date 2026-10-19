# Findings: scope-drift check of paper 1 v4, readability round 3

**Branch and base.** Branch `paper1-v4-readable-3-check`, cut at **`cbcc8b8`** (the head of `paper1-v4-readable-2`; round 3's content commit is `c565330`, its record `cbcc8b8`). Baseline: the claims ledger `paper/collatz-reduced-v4-claims.md` at `cbcc8b8` (the lock, tag `paper1-v4-content-lock`, plus its U26/U27 corrections). Method as in `briefs/paper1-v4-readable-check-findings.md` §3: every sentence that states a mathematical fact, a credit, a scope or a provenance claim, mapped to the ledger row(s) behind it. Done 2026-10-20. The `.tex` was not edited; nothing went outward.

**Verdict in one paragraph.** 233 sentences checked: the plain abstract (21), Symbols at a glance (17 definition rows), and §§1–8 (195). **221 keep their row's scope, 11 change it, and 1 has no row.** Six of the eleven are in the new plain abstract. Three of the changes make a sentence false where it stands:
- the abstract and §1 (v) say "no cycles made of one, two or three blocks", but `1, 4, 2, 1` is a one-block cycle;
- the abstract says "ruling out cycles needs divisibility", having dropped "uniform", but size alone, with the verified range, does rule out cycles of each small number of blocks;
- §5 "What is left" says "the staircases … fail the divisibility conditions", but those of part (iii) were never tested, as the same paragraph says three sentences later.

The unsupported sentence is §4's "no shortcut" sentence: it entered in the revision round (`03fdf7b`), after the last check, and no ledger row backs it.

The Technical summary equals the pre-round-3 abstract character for character, apart from the one declared sentence. Since `c7c3c69`, Appendices B–E differ by one hunk: Appendix B's opening paragraph from round 2, moved text plus a one-clause definition of `v₃`. Round 3 changed nothing in B–E. Every worked number was recomputed in fresh code: **122 checks, 0 failures; 12 negative controls, all rejected.**

---

## 1. Technical summary

`experiments/paper1_v4_readable3_check.py` part A reads the sources from git.
- **Against `6eb5946`** (the abstract before round 3): the `quote` block of "Technical summary" is the same text, character for character, with blank-line paragraph breaks kept. The one exception is the declared removal of "The main text tells each idea in words; the statements, proofs and checks are in the appendices." That sentence was a navigation line, not a ledger row.
- **Against the tag `paper1-v4-content-lock`**: there are exactly five word-level hunks. Together they are the round-1 changes that the previous check verified as declared:
  - the two plain opening sentences;
  - "study the Collatz dynamics in a reduced coordinate system that compresses" → "compress … such";
  - "accounting" → "accounting, stated as a heuristic,";
  - "(`fair-coin')".

  No locked word was removed apart from the replaced opening phrase.

**Verdict: the Technical summary is the locked abstract, as declared.**

## 2. Appendices B–E since `c7c3c69`

Part B compares the `.tex` at `c7c3c69` and at `cbcc8b8` line by line, from `\section{The reduced system…}` to `\section{Related work in detail}`. There is **one hunk**: Appendix B's opening line becomes a paragraph. That paragraph came in round 2 (`35abcdb`), as declared in `briefs/paper1-v4-readable-findings.md` §7b. Its contents:
- `T`'s display, "Tao's Syracuse map `Syr`", "the Collatz conjecture asserts that every `T`-orbit reaches 1", the definition of `v₂`, and `T(x) + 1 = (3/2)(x + 1)`. Each of these is found verbatim in the `c7c3c69` main text, so it is moved text.
- One clause that is not moved: "`v₃(n)` is the number of times 3 divides `n`". This is a definition. The locked text used `v₃` without defining it, so the clause makes no claim.
- The identity's new pointer, "proof of Proposition B.2(i)", is correct: that proof contains `T(y) + 1 = 2^{k−1}(3v)`.

Appendices C, D and E: no change at all. Round 3 touched none of B–E.

Outside B–E, also checked:
- Appendix F's new paragraph is `c7c3c69`'s §8 contemporary-work paragraph, verbatim.
- The §8 provenance paragraph is verbatim, apart from "Her open problem" → "Williams's open problem". A control with any other word changed is detected.

**Verdict: unchanged except moved text, as declared.**

## 3. Sentence-by-sentence verdicts

"Same" means the sentence restates the row(s) named, with the row's quantifiers and scope words, or with a gloss the row supports. Rows are the ledger IDs.

### 3.1 Plain abstract (21)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| Ab1 | the conjecture: halve / 3x+1, always reach 1 | C-Int.1 | same |
| Ab2 | "as long as one more than the current odd number is divisible by 4, each step simply trades a factor of 2 for a factor of 3" | C-Int.3 | same |
| Ab3 | each forced run folded into a block; a block described by two whole numbers, its state | C-Abs.1 | same |
| Ab4 | "(The same states were found independently by Williams, 2026.)" | C-Abs.1, P-22 | same |
| Ab5 | the new map "loses nothing": reaching 1 and the cycles come out the same | C-Abs.1, C-2.3(b)(c) | same |
| Ab6 | exact laws: halvings ending a block, factor of 3, next depth, how the anchor changes | C-Abs.3, C-Abs.4, C-3.4, C-Abs.5 | same |
| Ab7 | all but the factor of 3 governed by the anchor; factor of 3 its own exact law | C-Abs.2, C-Int.11 | same |
| Ab8 | "A finite number of binary digits of the state, with three labels of the step, decides each step: it either gives the answer or says correctly that the answer lies deeper, and it is never wrong." | C-Abs.6, C-3.8 | same. The three labels are `(s, m₊, a₊)`, equivalent to the ledger's `(s, σ, a₊)` because `σ = s + m₊`. "Decides each step" is the lock's own wording. |
| Ab9 | an accounting, "stated as a heuristic rather than proved", indicates no fixed finite number of digits decides the whole future | C-Abs.7 | same |
| **Ab10** | "there are no cycles made of one, two or three blocks" | C-Abs.8, C-4.4 | **scope changed** (§4 item 1) |
| **Ab11** | "the classical bound … on how many rising steps a cycle with a given number of blocks can have" | C-Abs.9, C-RW.14 | **scope changed** (§4 item 2) |
| Ab12 | "this fading is unavoidable for any argument from size alone" | C-Abs.10 | same |
| Ab13 | staircases pass every size test, every starting block, closeness between two fixed numbers, from 3 blocks (16 by proof, 3–15 by computer, 2 and 4 examples, no range) | C-Abs.11, C-4.6(i)a–c, N-4, N-19 | same ("near-cycles" glosses C-4.cfg(b): the configurations define rational cycles) |
| **Ab14** | "… from an explicit threshold on, exceeding the classical bound's own requirement by at most a fixed amount" | C-Abs.12, C-4.6(iii)a | **scope changed** (§4 item 3) |
| Ab15 | at the threshold scale they attain Rozier's optimum (minimax value) under every size test, the sharpness SdW expected | C-Abs.13, C-4.thr.6 | same |
| **Ab16** | "the conclusion that ruling out cycles needs divisibility and not size alone, are Halbeisen and Hungerbühler's" | C-Abs.14, C-4.6.close | **scope changed** (§4 item 4) |
| **Ab17** | the conjecture: blocks "recorded while … fewer halvings than a fixed multiple of the start's number of binary digits, and for every admissible choice of that multiple and of the record's length" | C-Abs.15, C-5.1, C-5.adm | **scope changed** (§4 item 5) |
| Ab18 | "It proves what follows if the conjecture holds" | C-Abs.16 | same |
| **Ab19** | "proves the conjecture outright while the orbit is still within the start's own supply of binary digits" | C-Abs.17, C-5.thm, C-5.clock | **scope changed** (§4 item 6) |
| Ab20 | test campaign, four apparent anomalies, all dissolved | C-Abs.18 | same |
| Ab21 | the technical summary states all of this in the usual notation | (navigation) | holds (§1) |

### 3.2 Symbols at a glance (17 definition rows)

The meanings of `x`, `T`, `m`, `s`, `a`, `ω`, `d`, `(ω,d)`, `F`, `p`, `n`, `K`, `q`, `γ`, `X₀`, `p₁(X₀)` and `λ, k` match C-2.1, C-4.setup, C-4.cfg(a), C-4.6(iii)a and C-RW.22. **All same.** Some rows were checked numerically:
- `K` is the rising halvings plus the final bursts, i.e. `n + Σs`;
- `3^n = 2^K(1 − 2^{−γ})`;
- `m` is the number of trailing 1s.

The page's navigation claims are in §5 below.

### 3.3 Section 1 (28)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| I1 | the rule; reaches 1, then 1, 4, 2, 1 | C-Int.1 | same |
| I2 | "Two things could go wrong": grows forever, or falls into a different cycle | — | same (elementary: a bounded orbit is eventually periodic) |
| I3, I6 | three purposes; the fair-coin assumption the heuristics leave implicit | P-12 | same |
| I4, I5 | classically exponentially far; "no farther: … from 3 on; and … from an explicit threshold on" | C-Int.2 | same |
| I7 | after an odd step the result is even; all halvings at once; Tao's Syracuse map | C-Int.1 | same |
| I8 | forced steps; one burst of halvings | C-Int.3 | same |
| I9 | states; reduced map loses nothing | C-Int.4, C-2.3 | same |
| I10 | (i) | C-Int.5 | same |
| I11 | (ii) six kinds fixed, two read off the anchor | C-Int.6, C-3.3 | same |
| I12 | (iii) | C-Int.7 | same |
| I13 | (iv) digits plus three labels; never wrong; heuristic accounting | C-Int.8, C-3.8, C-3.9 | same |
| I14 | (v) identity gives size and divisibility conditions | C-4.1 | same |
| **I15** | (v) "short new derivations of classical results: no cycles of one, two or three blocks" | C-Int.9, C-4.4 | **scope changed** (§4 item 1) |
| I16, I17 | (v) staircases from 3 on; from the threshold on, "the optimum Rozier identified (the minimax value of his extremal profile)" | C-Int.9, C-RW.20 | same |
| I18 | (vi) "proved outright in the range where a start's own binary digits still decide its blocks" | C-Int.10, C-5.thm, C-5.base | same (passive voice; §6 states the record assembly) |
| I19–I28 | the not-claimed box, ten sentences: does not settle; N-1; periods 1–3 classical; trim and Brox; staircases bear only on size; nothing at 1 block, examples at 2 and 4, no closed form; conjecture apart from the proved range; no drift; descent is Inselmann's; vanishing proportion ≠ negligible orbits, no single orbit, no iteration | N-1–N-5, N-11, N-13, N-15, N-19, C-RW.15, C-4.ver(d), C-5.thm, C-5.exc | same |

### 3.4 Section 2 (13)

All 13 are the same:
- B1: "Long stretches … forced" (C-Int.3).
- B2–B9: the table, the rising step and why it halves once, the 3/2 identity, the trailing digits, why the trade stops, the general statement, `s` and the example. Rows: C-2.2(i)(ii), C-2.1, and the proof of Prop B.2.
- B10: "classical (Steiner; …) and … the author's hand-drawn note of March 2023" (C-Int.3, P-20).
- B11–B13: the one-division map and the dictionary (C-4.dict(a)(d)).

Every number is recomputed (part C1).

### 3.5 Section 3 (12)

All 12 are the same:
- R1–R6: the state; `x_{m−1} + 1 = 2·3^{d−1}ω`; exactly `d` numbers per state, with one exit; `F`; the four transitions. Rows: C-2.1, C-2.2(i)–(iii).
- R7–R11: the three facts and the equivalence (C-2.3(a)–(c), C-2.2(iii)).
- R12: the Williams sentence (C-RW.22).

Every number is recomputed (part C2).

### 3.6 Section 4 (35)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| A1 | three questions; together they give the next state | C-2.1, C-Abs.3–4 | same |
| A2–A7 | cascade starts from `2(3^dω − 1)`; eight kinds; powers of 3 mod 8; lifting; the table; examples; `s ≥ 3` on lifting | C-2.1, C-2.2(ii), C-3.3(a)(b) | same |
| A8–A10 | the anchor (Def C.1); "2 plus the number of lowest binary digits on which `d` and the anchor agree"; `ω = 1` | C-3.1, C-3.3(a)(d) | same (rule verified on all 10,000 lifting states of the table range) |
| **A11** | "The law describes a step; it does not shortcut one: computing the anchor to the digits needed costs about as much as computing `s` directly (a note in the project record, `briefs/williams-letter-findings.md`)." | none | **unsupported** (§4 item 12) |
| A12–A15 | `3^dω + (2^s − 1)`; factor of 3 exactly when `s` even; `21 + 3 = 24`; the exact formula, 3-adic in one boundary case | C-2.1, C-3.4 | same |
| A16–A18 | next depth = entry depth + absorption; "exact formula in `s` and the anchor displacement (half the difference …)"; `≥ 1` structurally; the `(7,1)` example | C-3.5(a)–(c), C-Abs.4 | same. The half-gloss is exact on the lifting kinds, where the displacement is defined. Off them the formula uses `d − M(ω)` itself, which is the lock's own level of summary. |
| A19–A23 | finitely many digits; Thm C.7 in words; the window; the three outcomes; never wrong | C-3.3, C-3.7, C-3.8 | same |
| A24, A25 | the rate `1/2^{k+1}` under the model with cap `≥ k + 2`; the record's 2.75% and 0.19% | C-3.8.rate, N-18 | same |
| A26–A29 | the digit budget, its four clauses, under "a heuristic, not a theorem" | C-3.9(a)–(e), N-1 | same |
| **A30** | "The valuation, entry-depth and absorption laws were checked by independently written code, with zero discrepancies (Remark C.6); so were the three outcomes, along real orbits, with zero errors (Remark C.10)." | C-3.6, C-3.10 | **scope changed** (§4 item 8) |
| A31–A35 | "Where the difficulty is" | C-Int.11–14, C-3.post | same |

### 3.7 Section 5 (54)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| C1, C2 | counterexample = growing orbit or a cycle not containing 1; cycles are the finite case | — (elementary); C-Int.15 | same |
| C3 | "proves that they go no further: for every number of blocks from 3 on, and … from an explicit threshold number of blocks on" | C-4.6.close | same |
| C4, C5 | `n` counts multiplications by 3, `K = n + Σs`; trivial cycle `n = 1`, `K = 2` | C-4.setup | same |
| C6–C9 | the dictionary; SdW `m`-cycles, Rozier's minima; Hercher `≤ 91`; blocks only | C-4.dict(b)–(e) | same |
| C10, C11 | `2^K` exceeds `3^n`, by less the larger the numbers; `q`; `γ`; trivial values | C-4.1(a), C-4.2, C-4.cfg(a)(c) | same |
| C12–C15 | the identity, rotations; size and divisibility conditions; configuration, size-passer; "a size-passer need not give a cycle … as the staircases below do" | C-4.1(b)–(d), C-4.1.BS, C-4.cfg(a), C-4.6(iv) | same |
| C16 | no nontrivial cycles of 1, 2, 3 blocks; derivations, not theorems | C-4.4, P-24 | same |
| C17–C20 | the four history bullets (Rozier 1991, HH 1997, Brox 2000, SdW 2005) | C-RW.14–19 | same |
| C21 | the trim, "up to an additive constant" | C-4.5(a), C-4.5.cr | same |
| **C22** | "Read it this way: the more rising steps a cycle has, the closer `2^K` must be to `3^n`" | C-4.5(a) | **scope changed** (§4 item 9) |
| C23–C25 | finitely many configurations with Rhin, `n` of order `p · 1.585…^p`; every size-passer; rederivation by another route | C-4.5(b)–(d), P-16, P-26 | same |
| C26–C29 | the staircase: `p = 7`, `n = 94`, 55, `K = 149`; profile; passes all seven tests, `γ = 6.74`; the three-block bound would demand `γ` above 8.9 | C-4.6(iv), C-4.7 | same (recomputed) |
| **C30** | "so a bound as strong as the three-block one would wrongly exclude this seven-block size-passer, and the requirement must weaken as the number of blocks grows" | C-4.6(iv) (+ C-4.6(i)d) | **scope changed** (§4 item 10) |
| C31–C33 | the 84 (seeded search, none below the constant, margin `≥ 0.698`); all fail divisibility; Remark D.7 | C-4.6(iv), C-4.7, C-Int.15 | same (re-run: 84, minimum margin 0.698728) |
| C34–C38 | Sharpness bullet 1: from 3 on and from the threshold on; `p ≥ 16`, `n` in `[1.585…^p, 1.05·1.585…^p]`, `γ` about 3.68 to 5.14; 3–15 by computer; 2 and 4 exhibited, nothing at 1; the factor bound, intrinsic loss | C-RW.20, C-4.6(i)a–d, N-4, N-19 | same |
| C39–C43 | bullet 2: Barina; cycle above the verified range; the sandwich "within about `log₂ p`"; needs/enough; "exceeds the trim's own requirement (`n` times the shrinking factor) by an amount between … about 2.71 and 4.21" | C-RW.12, C-4.6(ii)a–c, C-4.6(iii)a | same |
| C44, C45 | `p₁` from the continued fraction; 10, 22, 36, 98, 110, 309; no single formula, nothing below | C-4.thr.1, C-4.thr.2, N-5 | same (recomputed) |
| C46–C49 | bullet 3: the minimax value, not Lemme 4; the sharpness SdW expected; exponential dependence, multiplier not below 0.054; left open | C-4.thr.4–6, C-RW.20, N-6, N-7 | same |
| **C50** | "The staircases pass every size condition yet fail the divisibility conditions." | C-4.ver(c), N-9 | **scope changed** (§4 item 11) |
| C51–C54 | "ruling out cycles uniformly in the number of blocks requires the divisibility conditions …"; every statement about the staircases concerns size; (i) computed and (iv) fail, (iii) untested; parts (i)–(iii) each checked by independently written code | C-4.6.close, C-4.ver(a)(c)(d) | same |

### 3.8 Section 6 (39)

All 39 are the same:
- H1–H11: the picture; letters and their chances; the window law and cap; Tao's law; the three model facts; why averages are not controlled; the ledger is a theorem about the model. Rows: C-Int.16, C-5.1, C-5.W, C-5.pi, C-5.syrac, C-5.piledger, P-28, N-11.
- H12–H16: the hypothesis, the tally example, protected, consistent. Rows: C-5.1, C-5.adm, C-5.cons. "Above any level that grows more slowly than every fixed power of the starting size" is `log X_N = o(log N)`.
- H17–H21: what is proved (budget rate `< 1` ⟺ horizon rate `< 1/4`, "its proof is assembled in the project record"); why, with the 1024 example. Rows: C-5.thm, C-5.rates, C-5.base, C-5.TV. The example is verified in 10 windows on all 255 patterns.
- H22–H25: the clock; the frontier; Terras/Korec; Inselmann (C-5.clock, C-5.Korec, C-RW.7). In "for the range within which an orbit stays and for its average", "its average" is the first moment, i.e. the orbit's proportion of odd steps (Inselmann Thm 1.6, per `briefs/v3r2-contraction-literature-findings.md`). Same. An optional sharpening is in §5.
- H26–H35: would give / would not give / no descent / the real content. Rows: C-5.ledger, C-5.dyadic, C-5.supplies, C-5.union, C-5.exc, C-5.descent, N-13–N-15.
- H36–H39: the campaign, the four items, the three limits (C-5.cal, C-5.ratio, C-5.limits, N-16). The figures were compared with the ledger (part C7).

### 3.9 Sections 7 and 8 (14)

- §7: O1–O3 are C-D.1, C-D.2 and C-D.3 (with P-29). Same. "Separates cleanly" was "factors cleanly"; that is a wording change, not a change of claim.
- §8: P1 ("The classical source of each result is named where it is stated") is the same.
- P2–P4, the gloss paragraph: skeleton rows = states, `(λ, k)`; representative fibre = the numbers sharing a state; "the intra-block cascade is the forced run inside a block". Rows: C-RW.22, C-2.2(iii). Same, but see §5 on the word "cascade".
- P5–P11, the provenance paragraph, are verbatim apart from "Williams's" (P-19–P-23, C-RW.22, C-RW.23). Same.

## 4. Scope changes and the unsupported sentence, with exact fixes

1. **Ab10 and I15 — "no cycles made of one, two or three blocks".**
   - **Ledger:** C-4.4 says "`F` has no **nontrivial** cycles of 1, 2 or 3 blocks"; C-Abs.8 speaks of "the classical exclusions".
   - **Problem:** `1, 4, 2, 1` is a one-block cycle. It meets every size and divisibility condition (witness, part D), so the sentence is false as worded.
   - **Fix (abstract):** "there are no cycles other than $1, 4, 2, 1$ made of one, two or three blocks;".
   - **Fix (§1 (v)):** "no cycles other than $1, 4, 2, 1$ with one, two or three blocks;".
2. **Ab11 — "on how many rising steps".**
   - **Ledger:** C-RW.14 says Rozier "bounded the number of odd steps" (`n`).
   - **Problem:** the paper's own "rising steps" (§2) number `n − p`: 87 in the staircase, against `n = 94`.
   - **Fix:** "on how many odd steps (multiplications by $3$) a cycle with a given number of blocks can have,".
3. **Ab14 — "exceeding the classical bound's own requirement by at most a fixed amount".**
   - **Ledger:** C-Abs.12, "with slack exceeding the **trim's own exponent** by at most an absolute constant"; C-4.6(iii)a, `λ₀ ≤ γ − κ_p n ≤ λ₀ + 1.5`.
   - **Problem 1:** the sentence has no subject. It is the staircases' measure of closeness that exceeds, not the staircases.
   - **Problem 2:** "requirement" is undefined in the abstract. The trim's requirement on `γ` is `κ_p n − log₂ p`, and the excess over that is up to `λ₀ + 1.5 + log₂ p`, which is not bounded: 7.53 at `p = 10`, 12.48 at `p = 309` (witness, part D). §5 avoids this by defining the word as "(`n` times the shrinking factor)".
   - **Fix:** "the staircases pass at every number of blocks from an explicit threshold on, with their measure of closeness exceeding the classical bound's own exponent by at most a fixed amount."
4. **Ab16 — "ruling out cycles needs divisibility and not size alone".**
   - **Ledger:** C-Abs.14 and C-4.6.close: "**uniform** cycle exclusion needs divisibility input".
   - **Problem:** without "uniform" the sentence is false. Size alone, with the verified range, does exclude cycles of each small number of blocks: Lemma D.3; C-4.thr.1 cites SdW's "size-only exclusion of `m ≤ 75`".
   - **Fix:** "and the conclusion that ruling out cycles of every length at once needs divisibility and not size alone, are Halbeisen and Hungerbühler's (1997)."
5. **Ab17 — "for every admissible choice of that multiple and of the record's length".**
   - **Ledger:** C-5.1 and C-5.adm quantify over *rates* `(τ, θ)`, with `T_N = ⌈θb⌉`.
   - **Problem:** a "record's length" can be read as a fixed number of blocks. That is a different statement, and a false one, since a frequency over a fixed number of blocks cannot converge to `B[w]`.
   - **Fix:** "and for every admissible choice of that multiple and of the record's length, itself a fixed multiple of the start's number of binary digits —".
6. **Ab19 — "proves the conjecture outright while the orbit is still within the start's own supply of binary digits".**
   - **What matches:** the range is C-5.thm's (`τ < 1`, equivalently `θ < 1/4`).
   - **Problem 1 (grade):** C-Abs.17 says the base case is "exhibited", graded "proved in record (bound printed here)". §6 says so too: "its proof is assembled in the project record".
   - **Problem 2 (referent):** the abstract's first sentence names "The Collatz conjecture", so a lay reader can take "proves the conjecture outright" to mean that conjecture.
   - **Fix:** "It proves what follows if the conjecture holds, shows that the fair-coin conjecture holds outright while the orbit is still within the start's own supply of binary digits (the proof is assembled in the project record), and reports …".
7. (I15 is item 1.)
8. **A30 — "so were the three outcomes".**
   - **Problem:** round 3 changed "and the trichotomy along real orbits, with zero errors" to "so were the three outcomes, along real orbits". "So were" now carries "checked by independently written code" over to the trichotomy. Remark C.10 and C-3.10 say only that it "was run along real orbits", with `one_step_propagation.py`.
   - **Fix:** "…, with zero discrepancies (Remark~\ref{rem:verify1}); the three outcomes were run along real orbits, with zero errors (Remark~\ref{rem:verify2})."
9. **C22 — "the more rising steps a cycle has".**
   - **Problem:** this is the same count error as item 2. The trim is a statement in `n`.
   - **Fix:** "Read it this way: the more multiplications by $3$ a cycle has (the larger $n$), the closer $2^K$ must be to $3^n$; …".
10. **C30 — "and the requirement must weaken as the number of blocks grows".**
    - **Problem:** C-4.6(iv) is one measured instance. It shows that the seven-block requirement is weaker than the three-block one. Weakening as `p` grows is Theorem D.6(i)'s content (C-4.6(i)d), not this example's. The writer flagged this clause as "a reading of the example" (§7c).
    - **Fix:** "so a bound as strong as the three-block one would wrongly exclude this seven-block size-passer: at seven blocks the requirement must be weaker than at three. (That it must weaken exponentially as the number of blocks grows is part (i) below.)"
11. **C50 — "The staircases pass every size condition yet fail the divisibility conditions."**
    - **Ledger:** C-4.ver(c) and N-9: those of (i) computed in the record, and those of (iv), fail; those of (iii) "were not tested".
    - **Problem:** the paragraph's own fourth sentence says so, so the opening sentence contradicts it.
    - **Fix:** "The staircases pass every size condition, and every one tested fails the divisibility conditions."
12. **A11 — unsupported:** "it does not shortcut one: computing the anchor to the digits needed costs about as much as computing $s$ directly".
    - **Source:** the sentence entered in the revision round (`03fdf7b`), after the check at `38ea5ee`. It has no ledger row.
    - **Record backing:** `briefs/williams-letter-findings.md` line 41 asserts the cost comparison and gives no argument; the writer kept it unproved on purpose (§7c, cold-read item 77). As a cost claim it is new content.
    - **Fix (preferred):** "The law describes a step; it is not offered as a faster way to compute one." This keeps the calibration and drops the cost claim.
    - **Alternative:** the author adds a ledger row, graded "asserted" or "interpretation", pointing to that note.

## 5. Navigation notes (not claims; not counted)

- **Symbols at a glance, "lists every symbol used outside the appendices".** Two letters appear outside the appendices with a second meaning that the page does not list: `p` in "`p`-adic" (Author's note) and `m` in Simons and de Weger's "`m`-cycle" (§5). Possible addition: "(Two letters also appear in fixed phrases with their usual meanings: `$p$-adic', and Simons and de~Weger's `$m$-cycle'.)" The page's other claim, "Section 1 and the abstract use none of them", holds: there is no lettered math in either.
- **§1, "Section 2's example, the orbit of 7, runs through Sections 2–5".** It runs through §§2–4, and its letters return in §6. §5's examples are the trivial cycle and the staircase. Suggested wording: "runs through Sections 2–4, and its letters return in Section 6".
- **Appendix I, "Main-text symbols are also in ``Symbols at a glance'', after Section~\ref{sec:intro}".** This is stale since round 3 moved the page before §1. Fix: "before Section~\ref{sec:intro}". This is in Appendix I, not B–E.
- **§8 gloss, "the intra-block cascade is the forced run inside a block".** The record's usage supports this (`briefs/ceiling-ccchallenge-sweep-findings.md`; C-RW.22 maps Williams's Thm 3.6 to Prop B.2(i)). The hazard is that §2 defines this paper's *cascade* as the closing burst of halvings, and §3 says Williams found "the cascade" in that sense. Optional: "(Williams's cascade is the run of forced steps; this paper's cascade is only its final burst)", after checking Williams §3.
- **Optional sharpening, §6 (H25).** "for the range within which an orbit stays and for the proportion of its steps that are odd".

## 6. Worked numbers (fresh code)

`experiments/paper1_v4_readable3_check.py` was written from the paper's text, with nothing imported from the repository's other scripts. It uses exact integers and Fractions, with `mpmath` at 400 digits for real constants, `γ` and `p₁`. It reads the TeX and the ledger from git at pinned commits. One command, about 25 s:

    python experiments/paper1_v4_readable3_check.py

It writes `experiments/paper1_v4_readable3_check_output.txt` and exits 0. **122 checks, 0 failures; 12 negative controls, all rejected.**

| Part | Checks | What |
|---|---|---|
| A | 4 | Technical summary (§1) |
| B | 12 | Appendices B–E and the moved text (§2) |
| C1 §2 | 21 | the four table rows (binary, factorizations); `24`, `22 → 11`; `12 = (3/2)·8`, `18 = (3/2)·12`; why a rising step halves once (all `x ≡ 3 (4)` `< 200001`); why the trade stops; `52 = 110100₂ → 13`; block of 7 (`m = 3`, `s = 1`, exit 13); trailing-1s and the cascade's `≥ 2` halvings (odd `x < 100001`); one-division map `7, 11, 17, 26, 13` and the dictionary (odd `x < 50001`) |
| C2 §3 | 13 | `(1,3)`; `18 = 2·3²`; `x_{m−1}+1 = 2·3^{d−1}ω`; state `(1,3)` = `{7, 11, 17}` with the stated `m`, one exit 13; exactly `d` per state (all 32,768 states whose representatives are all `< 2^17`); every valid state realised; the chain `(1,3) → (7,1) → (1,2) → (1,1) → (1,1)` with 40 → 5 (`s = 2`), 16 → 1 (`s = 3`), 4 → 1 (`s = 1`); `F(1,1) = (1,1)`, fibre `{1}`; `R(T^m x) = F(R x)` below `2^17` |
| C3 §4 | 19 | `26 = 2·13`; cascade start; powers of 3 mod 8; the printed table on 40,000 states (`ω < 3001`, `d ≤ 40`); lifting; the agree-digits rule on all lifting states (anchor mod `2^64`); `M(1) = 0`; `(1,2)`: `s = 3`; powers of 2 mod 3; factor of 3 iff `s` even; `21 + 3 = 24`; the `(7,1)` next depth; `m₊ ≥ 1`; `d − M(ω)` even on lifting kinds; rates 1/32 = 3.125% and 1/512 = 0.195% under every cap `D = k+2 … k+11`; mean 2 + 2 = 4 |
| C4 §5 | 14 | trivial cycle (`n = 1`, `K = 2`, `q = 1`, `γ = 2`, `R = 1 = q`); `3 = 4(1 − 1/4)`; the staircase: `n = 94`, 55, `K = 149` (`2^148 < 3^94 < 2^149`), all seven size tests (via the rational cycle of the one-division map, cross-checked against Prop D.1's `R_r`; min `R_r/q = 1.42063`), `γ = 6.743758`, `0.1157·94 − 2 = 8.8758` (printed 8.9), not divisible, depth ratios; the seed-41 search re-implemented: 84 distinct size-passers, min margin 0.698728, none divisible, `n ∈ {20, 22, 27, 29, 34, 41, 46}` |
| C5 §5 | 12 | `Γ* = 3.683012101` (about 3.68); `φ(0.0415) = 5.140211486` (about 5.14); for every `p = 16…60` an `n` in `[L^p, 1.05L^p]` with `γ` in the bracket (exact big-integer `γ` agrees at `p ≤ 20`); `λ₀ = 2.709512245`, `λ₀ + 1.5` about 4.21; `2^{−(λ₀+1.5)} = 0.0540518 ≥ 0.054`; `p₁` = 10 at `X₀ = 1, 2, 10, 16`; 22 at `2^8, 2^9, 2^{10.5}, 2^12`; 36, 98, 110, 309; nondecreasing on a grid of 115 points |
| C6 §6 | 9 | letters `(3,1), (1,2), (1,3), (1,1)`; `1/8`; `1/4 + 1/16 + … = 1/3`; the tally example at `b = 39` and `b = 40` (4 blocks, budget 20); `4 × 1/10 < 1/2`; budget `< 1` ⟺ horizon `< 1/4`; `2^10 = 1024`; the base-case example: in 10 windows of 1024 consecutive integers, all 255 patterns with fewer than ten halvings (start's block included) occur exactly `512/2^S` times |
| C7 | 15 | every quoted figure of §§4–6 found in its ledger row (2.75%, 0.19%, `0.2503 ± 0.0015`, 84,739, 41, `2^{40}`, five, 91, 84, 0.698, 0.054, 98, 110, 309, eight rounds) |
| D | 3 | witnesses for §4 items 1, 2 and 3 |

**Controls rejected:**
- the table cell `(5, even) → 1`;
- `K = 150`;
- last exit 48 keeping `K = 149`;
- a flat seven-block profile passing;
- `p₁(2^20) = 35`;
- a wrong state chain;
- wrong letters;
- exactness at `S = 10`;
- `((1,1),(1,1))` as a cycle other than `1, 4, 2, 1`;
- `b = 41` still giving 4 blocks;
- a summary keeping the layout sentence;
- a provenance paragraph with another word changed.

## 7. Record

- Branch `paper1-v4-readable-3-check`, cut at `cbcc8b8`.
- Deliverables: `experiments/paper1_v4_readable3_check.py`, its output, and this file.
- Not edited: the `.tex`, the PDF, the ledger, and every wiki page. Nothing was pushed.
- Out of scope, not re-read: the Version note and the Author's note. The Author's note is verbatim. The Version note's only change since the last check is round 2's pinned-citation sentence, which was the author's decision.
