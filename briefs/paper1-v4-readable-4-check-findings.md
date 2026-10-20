# Findings: scope-drift check of paper 1 v4, readability round 4

**Branch and base.** Branch `paper1-v4-readable-4-check`, cut at **`190b6af`** (round 4's record commit; its content commit is `60522a7`). The comparison base is round 3 at `cbcc8b8`. Baseline: the claims ledger `paper/collatz-reduced-v4-claims.md` at `190b6af`. It is byte-identical to the ledger at `cbcc8b8` (last changed in `03fdf7b`). Method as in the round-3 check (`904dcc6:briefs/paper1-v4-readable-3-check-findings.md`): every sentence of the plain abstract, the Symbols page and §§1–8 that changed between `cbcc8b8` and `190b6af` (`git diff --word-diff`) and states a fact, a credit, a scope or a provenance claim is mapped to the ledger row(s) behind it. Done 2026-10-20. The `.tex` was not edited; nothing went outward.

**Verdict in one paragraph.**
- **All 12 of the round-3 check's fixes are applied with at least their scope.** Each is applied in the check's own wording, and each old wording is gone. The four navigation notes and the optional one are done too.
- **96 changed sentences checked: 92 keep their row's scope, 4 change it, 0 have no row.** None of the four makes a claim stronger than the lock:
  - one adds an ordering the lock does not make ("weaker than");
  - one attaches "older and broader" to the anchors instead of to 2-adic logarithms;
  - one drops the comparand of the Lemme 4 comparison;
  - one adds a mechanism to the calibration ("which the sharper control set aside").
- **One record-level discrepancy** surfaced because round 4 brought Remark C.6's counts into §4. "All 62,937 valid states with ω below 3000 and d below 64" does not match the arithmetic: there are 63,000 such states, and 62,937 is the count without `ω = 1`. The ledger row (C-3.6) and `stage3.md` say the same thing, so this is not round-4 drift. The author should look at it.
- **Unchanged text.** Appendices B–E, the Technical summary and Appendices A, F, G and H are identical, character for character, between `cbcc8b8` and `190b6af`. So are the Version note and the Author's note. Appendix I differs by one word (after → before).
- **Worked numbers.** All recomputed in fresh code: **71 checks, 0 failures; 11 negative controls, all rejected.**

---

## 1. The round-3 check's 12 fixes

Part A of `experiments/paper1_v4_readable4_check.py` requires each new wording in the `190b6af` main text and each old wording to be absent.

| Fix | Round-3 wording asked for | At `190b6af` | Verdict |
|---|---|---|---|
| 1 (Ab10) | abstract: "no cycles other than 1, 4, 2, 1 made of one, two or three blocks" | verbatim; "no cycles made of one" gone | applied, full scope |
| 1/7 (I15) | §1 (v): "no cycles other than 1, 4, 2, 1 with one, two or three blocks" | verbatim | applied |
| 2 (Ab11) | "how many odd steps (multiplications by 3)" | verbatim; "rising steps" gone | applied |
| 3 (Ab14) | "with their measure of closeness exceeding the classical bound's own exponent by at most a fixed amount" | verbatim | applied |
| 4 (Ab16) | "ruling out cycles of every length at once needs divisibility" | verbatim | applied |
| 5 (Ab17) | "the record's length, itself a fixed multiple of the start's number of binary digits" | verbatim | applied |
| 6 (Ab19) | "shows that the fair-coin conjecture holds outright … (the proof is assembled in the project record)" | verbatim | applied |
| 8 (A30) | the trichotomy "run along real orbits", not "so were" | "(Remark C.6). The three outcomes were run along real orbits, 21,296 steps, with zero errors (Remark C.10)." The step count is C-3.10's | applied, full scope (the "independently written code" clause no longer reaches the trichotomy) |
| 9 (C22) | "the more multiplications by 3 a cycle has (the larger n)" | verbatim | applied |
| 10 (C30) | "at seven blocks the requirement must be weaker than at three. (That it must weaken exponentially … is part (i) below.)" | verbatim; old clause gone | applied |
| 11 (C50) | "The staircases pass every size condition, and every one tested fails the divisibility conditions." | verbatim | applied |
| 12 (A11) | "The law describes a step; it is not offered as a faster way to compute one." | verbatim; "shortcut", "costs about as much" and the `briefs/` pointer are gone | applied; no `.md` or `briefs/` pointer remains anywhere in §§1–8 |

Navigation notes, all done:
- the `p`-adic / `m`-cycle sentence on the symbols page (its claim holds: `p` appears only in "`$p$-adic'" in the Author's note, and `m` only in "`$m$-cycle'" in §5; the abstract and §1 contain no lettered math);
- "runs through Sections 2–4, and its blocks return in Section 6" (holds: §6's letters are the orbit of 7's);
- Appendix I "before Section 1";
- the §8 cascade gloss;
- H25 "the proportion of its steps that are odd".

**Verdict: 12/12 applied, none narrower than asked.**

## 2. Unchanged text (part B)

- **Version note and Author's note:** identical.
- **From `\appendix` to `\section{Symbol index}`:** identical, 83,080 characters. This span holds the Technical summary and Appendices A–H, so B–E (63,660 characters) are untouched. No text moved into B–E in round 4.
- **Appendix I:** exactly one token differs, `after` → `before` (navigation note 3).
- **Control:** a one-character edit inside B–E is detected.

**Verdict: B–E unchanged since `cbcc8b8`; no moved text this round.**

## 3. Sentence-by-sentence verdicts

"Same" means the sentence restates the named row(s) with the row's quantifiers and scope words, or with a gloss the row supports. Navigation sentences (pointers, reading instructions) are checked but not counted: every pointer resolves. The pointers are:
- "the dictionary paragraph" → *The dictionary with m-cycles*;
- "The uniform trim" → *The uniform trim: a short history*;
- "The unconditional base case" and "What the hypothesis implies" → the Appendix E subsections of those names;
- "Appendix G" → *Verification index*, whose last paragraph lists the statements proved in the record.

### 3.1 Plain abstract (9)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| Ab-1 | the new map "loses nothing: it gives the same answers as the original rule to whether every orbit reaches 1 and to which loops (cycles) exist" | C-Abs.1, C-2.3(b)(c) | same |
| Ab-2 | "exact laws for four things: …" | C-Abs.3–5, C-3.4 | same |
| Ab-3 | the identity "rewrites a cycle as whole-number conditions of two kinds: size conditions (about how close a power of 2 must come to a power of 3) and divisibility conditions" | C-Abs.8, C-4.1(b)(c) | same (the size gloss is §5's own definition of size arguments) |
| Ab-4 | derivations: no cycles other than 1, 4, 2, 1 at 1–3 blocks; Rozier/SdW bound on odd steps, fading exponentially | C-Abs.8, C-Abs.9, C-RW.14, C-4.4 | same (fixes 1, 2) |
| Ab-5 | "with their measure of closeness exceeding the classical bound's own exponent by at most a fixed amount" | C-Abs.12, C-4.6(iii)a | same (fix 3) |
| Ab-6 | "attain the best value of Rozier's 1991 real-number optimum (the minimax value of his extremal profile) under every size test" | C-Abs.13, C-RW.17, C-4.thr.6 | same. Optional wording note: "the best value of … optimum" says "best" twice; "attain Rozier's 1991 real-number optimum" says the same thing. |
| Ab-7 | "of every length at once" | C-Abs.14 | same (fix 4) |
| Ab-8 | the conjecture, "the record's length, itself a fixed multiple of the start's number of binary digits" | C-Abs.15, C-5.1, C-5.adm | same (fix 5) |
| Ab-9 | "shows that the fair-coin conjecture holds outright … (the proof is assembled in the project record)" | C-Abs.16–18, C-5.thm | same (fix 6) |

### 3.2 Symbols at a glance (1)

| # | Sentence | Rows | Verdict |
|---|---|---|---|
| S-1 | "Simons and de Weger's `m-cycle', which this paper calls a p-cycle" | C-4.dict(c) | same |

### 3.3 Section 1 (10)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| I-1 | "they bound how many odd steps a cycle can have, but the bound weakens exponentially as the number of blocks in the cycle grows" | C-Int.2, C-RW.14, C-Abs.9 | same |
| I-2 | "size arguments go no farther — that this exponential weakening cannot be avoided: for every number of blocks from 3 on; and … from an explicit threshold on" | C-Int.2, C-Abs.10 | same |
| I-3 | "an odd number plus 1 is even), so at least one halving always follows" | C-Int.1 | same (elementary) |
| I-4 | "its orbits reach the state of the number 1 exactly when the original orbits reach 1" | C-2.3(b) | same |
| I-5 | (ii) eight kinds by two remainders; six fixed; two "read off by comparing the state's depth, digit by digit, with a fixed binary pattern belonging to the state. (The valuation law.)" | C-Int.6, C-3.3 | same ("global" dropped from the label; "for the other two it is read off" still covers every such state) |
| I-6 | (iv) "three numbers describing the step (how far it falls, how deep the next block enters, and how many factors of 3 it picks up)" | C-Int.8, C-3.8 | same (`(s, m₊, a₊)` ≡ the ledger's `(s, σ, a₊)`, since `σ = s + m₊`) |
| I-7 | (iv) "a heuristic — a reasoned estimate, not a proof" | C-Int.8, N-1 | same |
| I-8 | (v) the identity "(stated in Section 5)"; "no cycles other than 1, 4, 2, 1 with one, two or three blocks" | C-Int.9, C-4.4 | same (fix 1) |
| I-9 | not claimed: "So is the uniform bound on cycles that Section 5 calls the trim (Rozier 1991; SdW)" | N-3, C-Abs.9 | same |
| **I-10** | not claimed: "form a fraction of all starting values that shrinks to zero as the starting size grows; **that is weaker than saying that almost no orbits misbehave**" | N-15, C-5.exc | **scope changed** (§4 item 1) |

### 3.4 Section 2 (1)

| # | Sentence | Rows | Verdict |
|---|---|---|---|
| B-1 | rising steps: "3x+1 can be halved only once, and half of 3x+1 is more than x, so the result is larger than where it started" | C-2.2(i) | same (checked for all `x ≡ 3 (mod 4)` below 200,001) |

### 3.5 Section 3 (4)

| # | Sentence | Rows | Verdict |
|---|---|---|---|
| R-1 | after the `m − 1` rising steps, one more than the number is "2 times ω times 3 to the power d − 1: the a factors … plus one more for each of the m − 1 rising steps" | C-2.2(i) | same (checked for odd `x` below 100,001) |
| R-2 | numbers sharing a state exit at the same place; "call them the state's representatives" | C-2.2(ii)(iii) | same |
| R-3 | "Put together: an odd number reaches 1 exactly when its states reach (1,1) (by the first two facts), and every valid state belongs to some odd number (the third)" | C-2.3(a)(b) | same |
| R-4 | Williams found the states "with their representatives and the forced run of steps" | C-RW.22, P-22 | same (the forced run is §8's gloss of the intra-block cascade) |

### 3.6 Section 4 (24)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| A-1 | the rule depends first on which of eight kinds; sort by `ω mod 8` and the parity of `d` | C-3.3 | same |
| A-2 | "On the six kinds marked with a number, s is that number" | C-3.3(b) | same (the printed table checked on 40,000 states) |
| A-3 | lifting: `s ≥ 3`, "set by a fixed binary pattern that belongs to ω, running on to the left without end: s is 2 plus the number of lowest binary digits on which d agrees with that pattern" | C-3.3(a), C-3.1 | same. §7d flagged it. `M(ω)` depends on `ω` only, is an element of Z₂, and `v₂(d − M(ω))` is exactly the number of agreeing low digits. Checked on all 10,000 lifting states with `ω < 3001`, `d ≤ 40`, anchor mod 2⁶⁴. |
| A-4 | "For ω = 1 the pattern is all zeros", `s` = 2 + trailing zeros of `d`, and the table d = 2, 4, 6, 8 → s = 3, 4, 3, 5 | C-3.3(d) (the `ω = 1` case) | same (recomputed) |
| A-5 | "(1,2) … is the first row: 3·5 + 1 = 16 halves four times, the first halving plus s = 3 more" | C-3.3, C-2.2 | same |
| A-6 | the other example states are not lifting; kinds and `s` | C-3.3(b) | same |
| A-7 | "Why the table holds. The cascade begins at the number 2 × (3^dω − 1) …, so s is the number of times 2 divides 3^dω − 1; … 26 = 2·13" | C-2.1, C-2.2(ii) | same |
| A-8 | powers of 3 mod 8; lifting → remainder 1 → `s ≥ 3`; else 3, 5, 7 → 2, 4, 6 → `s` = 1 or 2 | C-3.3(a)(b) | same. This explains the fixed cells and `s ≥ 3`, not the anchor rule, and it does not claim to. |
| A-9 | "The pattern is called the anchor of ω; Definition C.1 defines it" | C-3.1 | same (def) |
| A-10 | "The law describes a step; it is not offered as a faster way to compute one" | — | holds: no claim (fix 12) |
| A-11 | "One more than the exit, multiplied by 2^s, is the number 3^dω + 2^s − 1, so the next state's factors of 3 are those of this number" | C-2.1 | same (identity checked for `ω < 601`, `d ≤ 20`) |
| A-12 | first part a multiple of 3; `2^s − 1` a multiple of 3 iff `s` even; so a factor of 3 iff `s` even | C-3.4 | same |
| A-13 | example: (7,1), `s = 2`, exit 5, "(5 + 1) × 4 = 24 = 21 + 3", next state (1,2) with `a = 1` | C-2.1, C-3.4 | same (recomputed) |
| A-14 | "in one boundary case it depends on the remainders of ω on division by powers of 3" | C-3.4 | same (the 3-adic digits, glossed) |
| A-15 | next entry depth "by an exact formula in s and in how d compares with the anchor (Theorem C.5); the formula can never give less than 1" | C-3.5(a)–(c) | same. §7d flagged it. On both lifting components the displacement is `(d − M(ω))/2`, because `2N(3ω) = M(ω) − 1`. Off them the formula uses `d − M(ω)` and `(d − 1) − M(ω)`. |
| A-16 | "The anchor never ends, but one step needs only finitely many of its digits: s depends only on how many of its lowest digits agree with d" | C-3.3, C-3.7 | same |
| A-17 | the digits "do not determine the absorption, which depends on the remainders of ω on division by powers of 3; so the absorption has to be supplied separately, as a label of the step" | C-3.7, C-5.joint, C-3.8 | same (C-5.joint: `a₊` "the finite 2-adic residue window does not determine") |
| A-18 | the window, and its depth = "the number of anchor digits it tracks" | C-3.8 | same (def) |
| A-19 | the rate under the model "(whose cut-off, the cap, is taken at least the window's depth plus 2)" | C-3.8.rate | same |
| A-20 | "So, by this count — about the window's depth plus 6 digits per step on average — a window … can decide at most a number of steps proportional to its length" | C-3.9(a)(b)(d) | same (inside the heuristic paragraph; `k + E[s] + E[m₊] + 2 = k + 6` under the model, recomputed) |
| A-21 | the three laws checked by independent code: valuation on 8,000 random states, entry depth "on all 62,937 valid states with ω below 3000 and d below 64", absorption on 327,980 states | C-3.6 | same as the ledger. **But see §4 item 5:** the count does not match its own description. |
| A-22 | "The three outcomes were run along real orbits, 21,296 steps, with zero errors" | C-3.10 | same (fix 8) |
| A-23 | every quantity but the absorption "obeys an exact law in how d compares with the anchor", the absorption "its own exact law" | C-Int.11 | same ("3-adic" now said two paragraphs earlier, as the remainders on division by powers of 3) |
| A-24 | "the difficulty of the problem sits in one place" | C-Int.14 | same ("not diffuse") |

### 3.7 Section 5 (23)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| C-1 | the size conditions are met "at the scale the classical bound allows. (That bound is called the trim …)" | C-4.6.close | same |
| C-2 | "a p-cycle in Simons and de Weger's sense (their `m-cycle', with their m equal to our p, not to an entry depth)" | C-4.dict(c) | same |
| C-3 | Hercher rules out every nontrivial cycle of F "(every cycle other than 1, 4, 2, 1)" with at most 91 blocks | C-4.dict(d) | same |
| C-4 | "Multiplying by 3^n and dividing by 2^K alone would have to land back on the start; with the extra 1s pushing up, the halvings must win slightly" | C-4.1(a), C-4.2 | same (the reason for `q > 0`) |
| C-5 | "the more multiplications by 3 a cycle has (the larger n), the closer …; … weakens exponentially" | C-4.5(a) | same (fix 9) |
| C-6 | "The proof uses only the size conditions, so the bound holds for every size-passer, not only for cycles" | C-4.5(b) | same |
| C-7 | "How this leaves finitely many candidates at each number of blocks, in three steps (Theorem D.5, second part)" | C-4.5(c)(d) | same |
| C-8 | (a) by the trim, at a given `p`, a large `n` needs a large `γ` | C-4.5(a) | same |
| C-9 | (b) "By Rhin's theorem, a power of 2 cannot come too close to a power of 3: γ can grow at most like a fixed multiple of the logarithm of n" | C-4.5(d) (Rhin's display) | same. §7d flagged it. Rhin's display `Λ > exp(−13.3(0.46057 + log n))` and `Λ ≤ 2·2^{−γ}` for `γ ≥ 1` give `γ < 1 + (13.3/ln 2)(0.46057 + ln n)`, a fixed multiple of `log n` plus a constant. Checked at every `n ≤ 20,000` and at the convergent denominators up to `Q₆₉`; the largest `γ`/bound ratio is 0.203. |
| C-10 | (c) linear beats logarithmic; "n is bounded — at most of the order of p times (1.585… raised to the power p) — and only finitely many configurations remain" | C-4.5(c)(d) | same (`n₀(p)/(pL^p)` falls from 63.5 at `p = 2` to 21.9 at `p = 60`; without the factor `p` it is unbounded, control) |
| C-11 | the three-block bound "demands that γ exceed 0.1157 times n, minus 2: about 8.9 at n = 94" | C-4.6(iv) | same (8.8758) |
| C-12 | "at seven blocks the requirement must be weaker than at three. (That it must weaken exponentially … is part (i) below.)" | C-4.6(iv), C-4.6(i)d | same (fix 10) |
| C-13 | the 84 size-passers: "none of them falls below that three-block threshold (each clears it by at least 0.698)" | C-4.6(iv) | same. Optional: "threshold" is also the paper's word for `X₀` and `p₁`; "bound" would avoid the clash. |
| C-14 | "in this one configuration, the cycle side and the ever-growing side of the problem meet" | C-4.7 | same |
| C-15 | `n` "is at least 1.585…^p and at most 1.05 times that" | C-4.6(i)a | same |
| C-16 | "Take the base-2 logarithm of that smallest number: it lies within about the base-2 logarithm of p of γ" | C-4.6(ii)a | same |
| C-17 | `p₁` "computed from the best whole-number fractions approximating 1.585… (its continued fraction)" | C-4.6.pf.iii, C-4.thr.1 | same |
| C-18 | "It never decreases as X₀ grows" | C-4.thr.1 (monotonicity, proved here) | same (nondecreasing on 802 grid points `X₀ = 2^{e/4}`, `e ≤ 800`, plus `5·2⁶⁰`) |
| C-19 | the sample values 10, 22, 36, 98, 110, 309 | C-4.thr.1 | same (recomputed) |
| C-20 | "(These are samples, not a complete table; the record computes p₁(X₀) at every power of 2 up to 2^200.)" | C-4.ver(a), C-4.thr.1 (verification) | same. §7d flagged it. The record's `x0_threshold_independent_check_output.txt` reads "X0 = 2^j, j = 0..200". Recomputed here at every `j ≤ 200`: range `[2.7839895, 10.629477]`, inside the ledger's `[2.783, 10.630]`. |
| **C-21** | "not the inequality of his Lemma 4 (…`Lemme 4'), **whose extra term, 2 to the power p, is larger throughout this range**" | C-4.thr.6 | **scope changed** (§4 item 3) |
| C-22 | "That multiplier currently depends on p; whether it can be made a constant, independent of p, is left open, as SdW leave it" | C-4.thr.5, N-6 | same. §7d flagged it. The multiplier is SdW's prefactor `p c_p`, which carries an explicit `p`. "Can be made a constant" is C-4.thr.5's "lowered to a constant": a multiplier that grows with `p` becomes constant only by being lowered. |
| C-23 | "The staircases pass every size condition, and every one tested fails the divisibility conditions." | C-4.ver(c), N-9 | same (fix 11) |

### 3.8 Section 6 (17)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| H-1 | "(Appendix E also states it as a law for finite pieces of the state)" | C-Int.16 | same |
| H-2 | the factor-of-3 part of the model "is not new here: it is a law Tao introduced, his `Syracuse random variable', rescaled to the present setting" | C-5.syrac, P-28 | same (the block law is `Syrac(Z₃)/2`, a rescaling by the 3-adic unit `2^{−1}`) |
| H-3 | "entry depths and exit valuations have no upper limit, and a few very long blocks can dominate an average" | C-5.piledger, N-11 | same |
| H-4 | "The usual list of these facts (the folklore `ledger') is thus true of the model" | C-5.piledger | same |
| H-5 | protected: "while the budget lasts, the orbit has not yet fallen among the small numbers. Precisely, all but a fraction of starts that shrinks to zero keep every recorded block's exit (the odd number the block ends at) above any level …" | C-5.adm | same |
| H-6 | the base case "(Appendix E, …; proof assembled in the project record, Appendix G)" | C-5.thm, C-Abs.17 | same |
| H-7 | a pattern with fewer than ten halvings "is a class of remainders on division by 2 to a power of at most 10, and any run of 1024 consecutive integers contains each such class equally often" | C-5.base | same. §7d flagged it. Each pattern is one class mod `2^{S+1}`, with `S + 1 ≤ 10`. Checked on all odd `x < 2¹⁵`: 255 patterns, one class each. |
| H-8 | "among the odd numbers of any run of 1024 consecutive integers, each such pattern occurs in exactly its fair-coin share" | C-5.base | same (7 runs, including unaligned ones and one at `2⁴⁰ + 3`; all 255 patterns exact; fails at `S = 10`, control) |
| H-9 | longer patterns and sampling "explicitly bounded (Appendix E); the rest of the proof, which shows that frequencies concentrate, is in the project record" | C-5.TV, C-5.thm | same. Optional: C-5.thm's assembly also removes the segment's initial past-boundary. "which shows, among other things, that frequencies concentrate" would be exact. |
| H-10 | the quarter-block frontier is where "Terras's counting argument (the classical count of which starts follow which pattern) stops", and Korec's exponent | C-5.Korec | same |
| H-11 | "a limit of this technique, not of the problem"; Inselmann goes beyond it: range and proportion of odd steps; single steps; a stronger "almost all" | C-5.Korec, C-RW.4 | same |
| H-12 | the failing starts have density zero, "below any large bound, their share of the odd numbers shrinks to zero (given the hypothesis; …; proof assembled in the project record, Appendix G)" | C-5.dyadic | same (natural density zero, glossed) |
| **H-13** | "The hypothesis's real content is a question about the digits of the anchors of Section 4 (Appendix C names them precisely), **and that question is older and broader than the Collatz problem**" | C-5.exc | **scope changed** (§4 item 2) |
| **H-14** | "(2) correlations between neighbouring blocks — both artifacts of including small starting values, **which the sharper control set aside**" | C-5.cal | **scope changed** (§4 item 4) |
| H-15 | "41 standard deviations (a standard deviation measures how far a count strays from what chance predicts)" | C-5.cal | same (a gloss of `z`) |
| H-16 | "the earlier method — averaging, orbit by orbit, ratios of counts — had picked up as a bias" | C-5.cal, C-5.ratio | same |
| H-17 | "the filter … looks at the next state's odd core rather than at the block itself, and does remove some visits" | C-5.limits (3), N-16 | same (`ω₊` is the next state's odd core) |

### 3.9 Sections 7 and 8 (7)

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| O-1 | "one fixed pattern per state, the anchor, governs the step, apart from the factor-of-3 absorption" | C-D.1 | same |
| O-2 | "one difficulty, seen from two sides": statistical (Hyp E.1), arithmetic (divisibility of Prop D.1, which "by Theorem D.6, size alone cannot decide") | C-D.2 | same |
| O-3 | the staircase "is a single configuration that belongs to both sides" | C-D.2, C-4.7 | same |
| O-4 | "statements that a cycle's anchors are rigid: going once round a cycle, the anchors return to where they started, so their changes add up to zero" | C-D.3 | same |
| O-5 | "treated as a chain (the method of transfer operators)" | C-D.3 | same |
| O-6 | "the digits of the anchors — in the usual terms, the digits of 2-adic logarithms of whole numbers (Appendix C) — a problem this paper inherits rather than creates" | C-D.3, P-29 | same (the lock's own identification, as in round 1's "a `2-adic logarithm'") |
| P-1 | §8: "the intra-block cascade is the forced run inside a block (…; elsewhere in this paper `cascade' means only the block's final burst of halvings)" | C-RW.22 | same |

**Totals: 96 sentences. 92 same, 4 scope changed, 0 unsupported.**

## 4. Scope changes, with exact fixes; one record-level discrepancy

1. **I-10, §1 not-claimed bullet 5: "that is weaker than saying that almost no orbits misbehave."**
   - **Ledger:** N-15 and C-5.exc say the exceptional set is "a set of starting values of vanishing density at a prescribed finite horizon — not a null set of orbits, and not a statement about any orbit's infinite tail". Round 3 had "that is not the same as a negligible set of orbits".
   - **Problem:** "weaker than" asserts an ordering: that "almost no orbits misbehave" would imply the density statement. The lock asserts only that the two differ. They concern different events (frequencies at a finite horizon tied to a sampling scale, against the behaviour of orbits), and neither implies the other in general.
   - **Fix:** "that is not the same as saying that almost no orbits misbehave."
2. **H-13, §6 "What it would not give", last sentence: "and that question is older and broader than the Collatz problem".**
   - **Ledger:** C-5.exc says "Its content is a question about digits of 2-adic logarithms, older and broader than the Collatz problem". C-D.3 and P-29 say the same of "digits of 2-adic logarithms of integers".
   - **Problem:** round 4 replaced "digits of 2-adic logarithms of whole numbers" with "the digits of the anchors of Section 4". "That question is older" now attaches to objects this paper defines. What is older is the question about 2-adic logarithms, of which the anchors are instances. §7's third direction makes the link ("in the usual terms"); §6 does not.
   - **Fix:** "a question about the digits of the anchors of Section~\ref{sec:anchor} --- in the usual terms, digits of $2$-adic logarithms of whole numbers (Appendix~\ref{app:laws} names them precisely) --- and questions of that kind are older and broader than the Collatz problem."
   - **Alternative without the term:** "… (Appendix~\ref{app:laws} names them precisely); the anchors are numbers of a classical kind, and questions about their digits are older and broader than the Collatz problem."
3. **C-21, §5 "What is attained": "whose extra term, 2 to the power p, is larger throughout this range".**
   - **Ledger:** C-4.thr.6 says "not the inequality of his Lemme 4, whose additive term `2^p` exceeds `2^{κ_p n}` throughout this range" (the comparison is proved in the record).
   - **Problem:** the comparand is gone. "Larger" than what? The reader cannot recover the claim.
   - **Fix:** "… whose extra term, $2$ to the power $p$, is larger throughout this range than $2$ to the power ($n$ times the shrinking factor)."
   - **Witness:** at every `X₀ = 2^j`, `j ≤ 200`, `p₁(X₀) > g + 1 − λ₀ ≥ κ_p n` (smallest margin 6.62). So the ledger's comparison holds on the whole range.
4. **H-14, §6 calibration item (2): "both artifacts of including small starting values, which the sharper control set aside".**
   - **Ledger:** C-5.cal says "each dissolved by a sharper control: (1) an `s = 3` marginal excess and (2) pair correlations, both artifacts of small starting values". Appendix E says the same. Neither names the control. §7d flagged the clause.
   - **Problem:** the added clause says that one control, the exclusion of small starts, dissolved both. The record names different controls: `aeh.md` §13.4 says the three early discoveries "each dissolved under better controls (larger starts, per-orbit statistics, bulk/bottom separation)". Read in order, that names per-orbit statistics, not setting small starts aside, for the pair correlations.
   - **Fix:** drop the clause: "(2) correlations between neighbouring blocks --- both artifacts of including small starting values;". The list's lead-in already says each anomaly "dissolved under a sharper control".
5. **Record-level, not round-4 drift. A-21 (and Remark C.6, C-3.6, `stage3.md` §11.8.6.3): "the entry-depth law on all 62,937 valid states with ω below 3000 and d below 64".**
   - **The arithmetic:** the valid states with `ω < 3000` (odd, positive, prime to 3) and `1 ≤ d < 64` number **63,000**: 1,000 cores × 63 depths. 62,937 is exactly that count without `ω = 1` (63 states). Witness in part D.
   - **Status:** the sentence matches the lock word for word, so its verdict is "same". The discrepancy predates the readable rewrite. Round 4 is where it first enters the main text. `briefs/v3-external-review-corrections-findings.md` notes that no script for this count exists in `experiments/`.
   - **Suggested action (author's call, through the ledger):** either state the range the record actually checked (if `ω = 1` was excluded: "all 62,937 valid states with $1 < \w < 3000$ and $d$ below $64$"), or re-run the entry-depth law over the stated range and quote the new count. Remark C.6 and C-3.6 would then change with it. This check does not change either.

## 5. Worked numbers (fresh code)

`experiments/paper1_v4_readable4_check.py` was written for this check from the paper's text, and nothing in it is imported from the repository's other scripts. It uses exact integers and Fractions for integer decisions, `mpmath` at 400 digits for `γ`, `p₁` and the constants, and 60 digits for the `γ` sweep over `n ≤ 20,000`. It reads the TeX, the ledger, `aeh.md` and the record's `p₁` output from git at pinned commits. One command, a few seconds:

    python experiments/paper1_v4_readable4_check.py

It writes `experiments/paper1_v4_readable4_check_output.txt` and exits 0. **71 checks, 0 failures; 11 negative controls, all rejected.**

| Part | Checks | What |
|---|---|---|
| A | 19 | the 12 fixes, the navigation notes, no out-of-paper pointers in §§1–8, the ledger unchanged since `cbcc8b8` |
| B | 4 | Version and Author's notes; `\appendix` to the Symbol index; B–E; Appendix I one token |
| C §2–3 | 5 | rising steps halve once and rise (`x ≡ 3 (4)`, `< 200,001`); `24`, `22 → 11`; `x_{m−1} + 1 = 2·ω·3^{d−1}` (odd `x < 100,001`); `18 = 2·3²`; "put together" (odd `x < 20,001`) |
| C §4 | 23 | the printed table (40,000 states); powers of 3 mod 8 and the remainders; `26 = 2·13`; the anchor rule as digit agreement (10,000 lifting states, anchor mod 2⁶⁴); `M(1) = 0`; the `ω = 1` table and `3^d − 1 = 8, 80, 728, 6560`; `16` halves four times; the example kinds; `(exit + 1)·2^s = 3^dω + 2^s − 1`, its threes `= a₊`, gain iff `s` even (`ω < 601`, `d ≤ 20`); powers of 2 mod 3; `(5 + 1) × 4 = 24 = 21 + 3`, `(1,2)`, `a = 1`; no gain at `s = 1, 3`; next depth 2; `m₊ ≥ 1`; `k + 6`; the counts 8,000, 62,937, 327,980 and 21,296 and the range `ω < 3000`, `d < 64` equal to the ledger's |
| C §5 | 10 | `0.1157·94 − 2 = 8.8758`; Rhin in `γ` terms (`n ≤ 20,000` and the convergent denominators to `Q₆₉`, max ratio 0.203); `n₀(p)/(pL^p)` bounded and decreasing, 63.5 → 21.9 over `p = 2…60`; `p₁` = 10 at `X₀ = 1, 2, 10, 16`, 22 at `2^8 … 2^12`, 36, 98, 110 and 309; never decreasing (802 points); every `2^j`, `j ≤ 200`, range `[2.7839895, 10.629477]`; the record's output covers `j ≤ 200`; `2^{−(λ₀+1.5)} = 0.0540518` |
| C §6 | 3 | the 1024-integer example in 7 runs (255 patterns, exact shares); one class mod `2^{S+1} ≤ 2^{10}` per pattern (odd `x < 2¹⁵`); the letters `(3,1), (1,2), (1,3), (1,1)` |
| D | 7 | witnesses for §4 items 1–5 (63,000 vs 62,937; the Lemme 4 comparand with margin 6.62; the calibration clause absent from Appendix E and the ledger; `aeh.md`'s list of controls; the §6 anchors sentence; "weaker than" against "not a null set of orbits") |

**Controls rejected:**
- the `ω = 1` row `d = 6 → s = 4`;
- the table cell `(5, even) → 1`;
- the exit of 13 given as 7, and `(5 + 1)·4 = 25`;
- `p₁(2^{20}) = 35`;
- a decreasing sequence passing the monotonicity test;
- `γ < 1 + ln n` (multiplier 1) at `n = 41`, where `γ = 6.455`;
- `n₀(p)` of order `L^p` without the factor `p`;
- an exact fair-coin share at `S = 10`;
- 62,937 as the full count;
- a comparand that fails (`p₁ > log₂X₀ + 200`);
- a one-character edit in B–E.

## 6. Record

- Branch `paper1-v4-readable-4-check`, cut at `190b6af`.
- Deliverables: `experiments/paper1_v4_readable4_check.py`, its output, and this file.
- Not edited: the `.tex`, the PDF, the ledger, and every wiki page. Nothing was pushed.
- Out of scope, not re-read sentence by sentence: the Version note and the Author's note (identical to `cbcc8b8`, part B) and the Technical summary (identical, part B).
