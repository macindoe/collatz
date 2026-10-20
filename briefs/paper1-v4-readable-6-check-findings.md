# Findings: scope-drift check of paper 1 v4, readability round 6 (final polish)

**Branch and base.** Branch `paper1-v4-readable-6-check`, cut at **`73d51d4`** (the head of `paper1-v4-readable-6`: content commit `92881dd` plus the §7f record). The comparison base is round 5 on `main` at `56d6b3b`. Baseline: the claims ledger `paper/collatz-reduced-v4-claims.md`, identical at both commits. Method as in the round-5 check (`briefs/paper1-v4-readable-5-check-findings.md`). Every sentence that changed between `56d6b3b` and `73d51d4` is mapped to the ledger row(s) behind it, if it states a fact, a credit, a scope or a provenance claim. The scope is the abstract, the Symbols page, §§1–8 and the guided accounts of Appendices C–E. Done 2026-10-20. The `.tex` was not edited; nothing went outward.

**Verdict in one paragraph.**
- **The round-5 fixes.** The required §4 fix is in verbatim. All four optional notes are applied with at least their scope, and so are the two further notes (App C names `depth_law_reverify.py`; "the staircases of part (i)").
- **Changed sentences.** 78 changed; 4 are navigation. **Of the 74 counted, 71 keep their row's scope, 3 change it, and 0 have no row.**
  - Two of the three are the same gloss: "admissible" in the abstract and in §6 drops the protection clause's "all but a vanishing share of starts". Read literally, it fails at τ = 1.1 (§4).
  - The third is §5's "first proved by Brox". The ledger says only "Brox proved", and the record has Rozier 1991 (p. 8, Théorème) nine years earlier.
- **Unchanged material.** The 19 formal statement environments, the Technical summary, the front matter, the Version note and the Author's note are all identical to `56d6b3b`. From `\appendix` on, exactly three lines differ, one in each guided account, made of five declared phrase edits.
- **Worked numbers.** All recomputed in fresh code. **56 checks, 0 failures; 9 negative controls, all rejected.**

---

## 1. The round-5 check's fixes

| Item | Asked for | At `73d51d4` | Verdict |
|---|---|---|---|
| Required (A-9) | §4: the heuristic label governs "each decided step uses up binary digits … nothing restores them" | the check's sentence verbatim; "But each decided step uses up" is gone | applied verbatim |
| Optional (a) | §5: closeness depends on size | "only slightly larger than 3 to the power n, and by less the larger the cycle's numbers are" | applied, full scope (C-4.2) |
| Optional (b) | §5: size arguments tied to the size conditions | "use only this closeness, through the cycle's size conditions (Appendix D)" | applied, at least the note's scope (C-4.5(b), C-4.1(c)) |
| Optional (c) | "passing examples only" | verbatim; "without that range" is gone | applied verbatim |
| Optional (d) | §6 keeps the tolerance | "every finite pattern of letters and every tolerance … by more than the tolerance" | applied, full scope (C-5.1's `ε`) |
| Further | App C guided account names the script | "`ω = 1` included (`experiments/depth_law_reverify.py`)" | applied |
| Further | "the staircases of part (i)" | App D guided account, with "their n" | applied |

**Verdict: 1/1 required and 4/4 optional applied, none narrower than asked.**

## 2. Unchanged material (part B)

- **The 19 formal statement environments** (theorem, proposition, lemma, corollary, definition, hypothesis, heuristic) are identical to `56d6b3b`.
- **The Technical summary is identical** (3,540 characters), and so are the front matter, the Version note and the Author's note.
- **From `\appendix` on,** exactly three non-blank lines differ, each inside a guided account. Together they make exactly five declared phrase edits; applying them to `56d6b3b` reproduces `73d51d4`'s appendices exactly:
  - App C, "Checks": the script is named;
  - App D: "the staircases of part (i)" and "their n";
  - App E: the letter is written `m|s` with the bar's reason, and the running example's letters and `1|2` use that notation.
- **Control:** a one-character edit inside Theorem C.5 is caught.

**Verdict: the formal statements and the Technical summary are unchanged since `56d6b3b`.**

## 3. Sentence-by-sentence verdicts

"Same" means the sentence restates the named row(s) with the row's quantifiers and scope words, or with a gloss the row supports. The script splits the abstract, Symbols page, §§1–8 and the three guided accounts into sentences. It lists every sentence new at `73d51d4` and requires each to match exactly one entry below, and each entry to match exactly one sentence (78/78).

**Navigation (4, not counted).** All four resolve:
- §1 (ii) "(This is the exit rule of Section 4; Theorem C.3.)";
- §5 "The paper does three things here.";
- §7 "Three directions are open:";
- §8's pointer to Appendix F. Its glosses, "density results" and "3-adic comparisons", match Appendix F's paragraphs.

| # | Sentence (abridged) | Rows | Verdict |
|---|---|---|---|
| AB-1 | the map gives the same answers on whether every orbit "(the sequence of numbers a start visits)" reaches 1 and which cycles exist | C-Abs.1, C-2.3 | same |
| AB-2 | finitely many digits "with three numbers describing the step (Section 4)" decide each step, never wrong | C-Abs.6, C-3.8 | same |
| AB-3 | staircases pass every size test while the closeness "(how small the gap between the two powers is, compared with the larger one)" stays between two fixed numbers, from 3 on (16 by proof, 3–15 by check; 2 and 4 examples, no range) | C-Abs.11, C-4.cfg(a), N-19 | same (`γ = −log₂(q/2^K)`) |
| AB-4 | "they attain the optimum of Rozier's 1991 analysis — the best worst case over block depths allowed to be any real numbers — under every size test" | C-Abs.13, C-4.thr.6, C-4.6.minimax, C-RW.17, N-7 | same (§5 of this file) |
| AB-5 | the fair-coin assumption stated as a precise conjecture | C-Abs.15 | same |
| AB-6 | record each block's (entry depth, exit valuation) pair within a budget, over a horizon, both fixed multiples of the bit length | C-Abs.15, C-5.1 | same |
| **AB-7** | "… for every admissible choice of the two multiples (one that fits the record inside the halving budget on the model's average and keeps the orbit away from small numbers; Section 6)" | C-Abs.15, C-5.adm | **scope changed** (§4) |
| SY-1 | `n`: the sum of a cycle's entry depths | C-4.setup | same |
| SY-2 | `K`: `n` plus the sum of the exit valuations | C-4.setup | same |
| SY-3 | `γ`: the gap between `2^K` and `3^n` is `2^K / 2^γ` | C-4.cfg(a) | same |
| SY-4 | `m\|s`: a letter, a block's entry depth and exit valuation | C-5.1 | same |
| SY-5 | anchor (a fixed binary string running to the left, all zeros at `ω = 1`), lifting (1 mod 8 with `d` even, 3 mod 8 with `d` odd), absorption (factors of 3 picked up) | C-3.1, C-3.3(a), C-3.4 | same |
| I-1 | size arguments go no farther; the weakening cannot be avoided, from 3 blocks on | C-Int.2, C-Abs.10 | same |
| I-2 | the same with every number at least a given size, from an explicit threshold on | C-Int.2, C-Abs.12 | same |
| I-3 | orbits reach the state of 1 exactly when the original orbits reach 1; the trivial cycle corresponds to the state of 1, which `F` fixes; every other cycle corresponds to exactly one other cycle of states, and back | C-2.3(a)(b)(c) | same (the bijection of nontrivial cycles; `(1,1)` fixed with fibre `{1}`) |
| I-4 | the digits either predict the next step or say the next burst "is longer than those digits can determine" | C-3.8, C-Int.8 | same (`s₊ ≥ k + 2`) |
| I-5 | staircases from 3 on "(by proof from 16 on, by computer check for 3 to 15; for 2 and 4 blocks, examples only)" | C-4.6(i)a–c, N-4, N-19 | same |
| I-6 | "there it reaches the optimum of Rozier's analysis — the best worst case …" | C-Int.9, C-4.thr.6, C-RW.17, N-7 | same |
| I-7 | "It does not prove that no fixed, finite number of binary digits can decide an orbit's whole future" | N-1 | same |
| I-8 | "That is the paper's organizing heuristic" | N-1, C-3.9(e) | same |
| I-9 | for 2 and 4 blocks only passing examples, "with no claim about their closeness measure" | C-4.6(i)c, N-19 | same |
| I-10 | no statement that orbits drift downward "or shrink" follows | N-11, C-5.piledger | same |
| I-11 | does not state that almost every orbit falls below its start ("descent"); proved without it, more strongly, by Inselmann | C-5.descent, N-13, C-RW.2 | same |
| I-12 | starting values whose blocks "stray from the coin pattern" form a vanishing fraction; not the same as almost no orbits stray | C-5.exc, N-15 | same |
| B-1 | "(a number 2 more than a multiple of 4 is twice an odd number)" | C-2.2(i) | same (recomputed) |
| B-2 | `s` = the cascade's halvings "not counting its first" | C-2.1 | same |
| R-1 | after the `m − 1` rising steps, one more than the number is `2 · ω · 3^{d−1}` | C-2.2(i) | same (recomputed, odd `x < 200,001`) |
| R-2 | "The reason: x+1 had a factors of 3, and each of the m − 1 rising steps added one more, d − 1 in all." | C-2.2(i) | same (`a + m − 1 = d − 1`, recomputed) |
| R-3 | 13 → `(7,1)`, "a block of one odd number (m = 1)", 40 halves three times (`s = 2`) to 5 | C-2.1 (worked) | same (recomputed) |
| R-4 | 5 → `(1,2)`, "again a block of one odd number", 16 halves four times (`s = 3`) to 1 | C-2.1 (worked) | same (recomputed) |
| R-5 | the only number with state `(1,1)` is 1, "since 1 + 1 = 2 gives m = 1, a = 0 and ω = 1" | C-2.3(a), C-2.2(iii) | same. Optional note (d) |
| A-1 | eight kinds by `ω mod 8` "(which is 1, 3, 5 or 7, since ω is odd)" and parity of `d` | C-3.3 | same |
| A-2 | lifting kinds defined in words; `s ≥ 3`, 2 plus agreement with the anchor | C-3.3(a), C-3.1 | same (the words = `3^d ω ≡ 1 (mod 8)`, recomputed) |
| A-3 | the required fix (heuristic label on the premise) | C-3.9(a)(c)(e), C-Int.13, N-1 | same |
| A-4 | `(7,1)`: kind (7, odd), `s = 2`, "and s = 2 is even", so a factor of 3: 6 = 2·3 | C-3.3(b), C-3.4 | same (recomputed) |
| C-1 | a cycle multiplies by 3 `n` times "(n is the sum of the blocks' entry depths)" | C-4.setup | same |
| C-2 | `2^K` only slightly larger than `3^n`, "and by less the larger the cycle's numbers are" | C-4.1(a), C-4.2 | same |
| C-3 | "the gap between the two powers is 2^K divided by 2^γ, so a larger γ means a closer approach" | C-4.cfg(a) | same (`q = 2^{K−γ}` by definition; recomputed) |
| C-4 | size arguments "use only this closeness, through the cycle's size conditions (Appendix D)" | C-4.5(b), C-4.1(c) | same |
| C-5 | classically the uniform trim (Rozier 1991; SdW 2005) bounds `n` for `p` blocks; weakens exponentially | C-4.5(a), C-Abs.9, C-RW.14 | same |
| **C-6** | "Combined with Rhin's theorem — a classical limit on how close a power of 2 can come to a power of 3 — it leaves only finitely many possible cycles to check at each p (that there are only finitely many was first proved by Brox)." | C-4.5(c)(d), C-RW.15, C-4.5.cr | **scope changed** (§4). The Rhin gloss alone is same (C-4.5(d), C-4.4.p23) |
| C-7 | rederives the bound by another route | C-4.5.cr, P-16 | same |
| C-8 | rederives no cycles other than 1, 4, 2, 1 at one to three blocks | C-4.4, N-2 | same |
| C-9 | proves the weakening cannot be avoided by size arguments | C-Abs.10, C-4.6(i)d | same |
| C-10 | near-cycles: "lists of block depths and exit valuations shaped like a cycle and tested only by the size conditions" — the staircases | C-4.cfg(a), C-Abs.11 | same. Optional note (b) |
| C-11 | staircases pass every size test, every starting block, from 3 on (16 by proof, 3–15 by check, "passing examples only" at 2 and 4); and from an explicit threshold on | C-4.6(i)a–c, C-4.6(iii)a, N-4 | same |
| C-12 | "every staircase checked fails at least one of these divisibility conditions" | C-4.ver(c), C-4.6(iv), N-9 | same: "checked" keeps (iii)'s untested configurations out, and "at least one" is the weaker reading of "fail the conditions". On the printed instance `q ∣ R_r` at 0 of 7 rotations |
| C-13 | `n = 94`, "the sum of the entry depths", `K = 94 + 55 = 149` | C-4.6(iv) | same (recomputed) |
| C-14 | v3's instance, not of Theorem D.6(i)'s family (`γ` 3.68–5.14); this one's `γ` is 6.74 | C-4.6(iv), C-4.6(i)a | same (`γ = 6.743758`) |
| H-1 | a letter "written m\|s: its entry depth m and its exit valuation s", with a bar | C-5.1 | same |
| H-2 | Terras: the two parts as independent coin-toss counts | C-5.1, C-Int.16 | same |
| H-3 | stated as a precise conjecture (Hypothesis E.1) | C-Abs.15 | same |
| H-4 | draw a large odd start at random; record letters under two conditions | C-5.1 | same |
| H-5 | horizon: the record stops after a fixed multiple of the bit length in blocks | C-5.1 (`T_N`) | same |
| H-6 | budget: a letter is recorded only while fewer halvings than another fixed multiple have been done | C-5.1 (`S_n < Λ_N`) | same |
| **H-7** | "Call a choice of the two multiples admissible when the record fits inside the budget on the model's own average (four halvings per block) and the budget keeps the orbit away from the small numbers." | C-5.adm, C-5.cons | **scope changed** (§4). The consistency half is same |
| H-8 | for every admissible choice, every finite pattern and every tolerance, the share of starts deviating by more than the tolerance shrinks to zero | C-5.1 | same |
| H-9 | proved while fewer halvings than the start's bit length, "because the start's lowest binary digits fix its first blocks exactly (the starts with a given pattern of first blocks form one class of remainders on division by a power of 2)" | C-5.base, C-5.thm | same (§5 of this file) |
| H-10 | "the unconditional base case, the part proved without assuming anything (proof assembled in the project record, Appendix G)" | C-Abs.17, C-5.thm | same |
| H-11 | blocks 7, 11, 17; 13; 5; 1 have letters `3\|1, 1\|2, 1\|3, 1\|1` | worked (C-2.1) | same (recomputed by direct Syracuse steps) |
| H-12 | `1\|2` has chance ½ × ¼ = ⅛ | C-5.1 | same |
| O-1 | going beyond size: Theorem D.6 shows any uniform exclusion needs arithmetic statements beyond the size level | C-D.3, C-4.6.close | same |
| O-2 | one candidate: the anchors are rigid, returning round a cycle, changes adding to zero | C-D.3 | same |
| O-3 | following windows step by step: one exact window of Theorem C.8 leading to the next, as a chain (transfer operators) | C-D.3 | same |
| O-4 | the anchors' digits: "in standard terms, digits of 2-adic logarithms of whole numbers (Appendix C) — a problem this paper inherits rather than creates" | C-D.3, P-29, C-D.1 | same. Optional note (c) |
| P-1 | three terms "for objects of Sections 2–3": skeleton rows (Williams's name for the states), the representative fibre, the intra-block cascade | C-RW.22 | same. C-RW.22 credits Williams with the objects, and the provenance paragraph still says so ("The same states, with their representative fibre and intra-block cascade, appear independently as the skeleton rows … of Williams"). The ledger does not say whose the two terms are, and the sentence no longer says either |
| P-2 | "In Williams's picture a row is a pair: a skeleton λ (our odd core) and a depth k (our depth)." | C-RW.22 | same |
| P-3 | "When a trajectory leaves a row, Section 4's laws give the exit valuation and the entry position, and so the depth k of the row it lands in." | C-RW.23 | same (§5 of this file) |
| P-4 | "They give no law for the skeleton λ of that row: on that, F only restates Williams's Proposition 3.10." | C-RW.23 | same |
| GC-1 | App C "Checks": the 63,000 sentence names `experiments/depth_law_reverify.py` | C-3.6, C-3.5(a) | same |
| GD-1 | App D: "Apply it to the staircases of part (i), whose γ is at most about 5.14 while their n is at least 1.585… to the power p" | C-4.6(i)a, (i)d | same |
| GE-1 | App E: the letter "written m\|s: the block's entry depth and exit valuation (the bar keeps a letter from being mistaken for a state)" | C-5.1 | same |
| GE-2 | App E: running example's letters `3\|1, 1\|2, 1\|3, 1\|1` | worked | same |
| GE-3 | App E: `1\|2` has chance ⅛ | C-5.1 | same |

**Totals: 78 changed sentences. 4 are navigation; of the 74 counted, 71 are same, 3 scope changed, 0 unsupported.**

## 4. The three scope changes, with their fixes

### AB-7 and H-7: the "admissible" gloss drops the protection clause's quantifier

- **Ledger.** C-5.adm: "`τ` is protected when **all but a vanishing density of starts** keep every in-budget exit above any `X_N` with `log X_N = o(log N)`. `(τ, θ)` is consistent when `θ E_B[m + r] < τ`. Admissible means both." Hypothesis E.1's terms and App E's guided account both keep "all but a fraction of starts that shrinks to zero".
- **The two glosses.**
  - Abstract: "(one that fits the record inside the halving budget on the model's average and keeps the orbit away from small numbers; Section 6)".
  - §6: "Call a choice of the two multiples admissible when the record fits inside the budget on the model's own average (four halvings per block) and the budget keeps the orbit away from the small numbers."
  - The consistency half is exact: 4θ < τ, four halvings per block, `E[m] = E[s] = 2`.
  - The protection half states for "the orbit", without the exceptional set, what the row states for all but a vanishing share of starts.
- **Why it matters (a fresh witness).** Read for every start, protection fails as soon as the budget rate exceeds 1 by a little.
  - Take `x = (2^42 − 1)/3`, an odd start in `[2^40, 2^41)`. Then `3x + 1 = 2^42`, so its first block ends at 1 after 42 halvings.
  - That is inside the budget `⌈1.1 · 40⌉ = 44`.
  - So on the literal reading no `τ` much above 1 is admissible, and the conjecture shrinks to little more than its proved base case (`τ < 1`). The row makes every `τ < 4.8188…` protected (C-5.prot).
- **Fixes.**
  - Abstract: "… and keeps the orbit away from small numbers; Section~\ref{sec:aeh})" → "… and keeps **all but a vanishing share of orbits** away from small numbers; Section~\ref{sec:aeh})".
  - §6: "and the budget keeps the orbit away from the small numbers." → "and the budget keeps **all but a vanishing share of starts** away from the small numbers."

### C-6: "first proved by Brox"

- **Ledger.** C-RW.15: "Brox proved finiteness for each `p`." C-4.5(c) and C-4.5.cr credit the finiteness to Brox ("is Brox's"). No row makes a priority claim.
- **The record contradicts "first".** `briefs/ceiling-ccchallenge-sweep-findings.md` §0 quotes Rozier 1991, p. 8, Théorème, read from the page images: « Pour chaque entier n, il n'y a qu'un nombre fini de cycles alternant n séquences d'entiers impairs avec n séquences d'entiers pairs ». It notes that this "predates … Brox 2000 by 9" years. The paper's own App D guided account dates Rozier's bound 1991 and Brox's finiteness 2000.
- **Fix.** "(that there are only finitely many was first proved by Brox)" → "**(Brox proved that there are only finitely many)**". This is C-RW.15's own wording and makes no priority claim.
- **Flag for the coordinator (not a round-6 drift).** The ledger's own "finiteness at each `p` is Brox's" (C-4.5.cr) also sits uneasily with Rozier's p. 8 Théorème. It is printed after Theorem D.5 as "finiteness at each p is due to Brox". Bringing the ledger into line is a content decision, outside a scope check.

## 5. The particular-attention items

- **"Admissible"** (abstract, §6) against C-5.1/C-5.adm and Hypothesis E.1's two clauses. Consistency matches; protection loses its quantifier. **Scope changed** (§4).
- **Base case** (§6). C-5.base is "the odd integers whose first `n` blocks realize a prescribed itinerary form exactly one residue class modulo `2^{S+1}`"; C-5.thm puts the range at `τ < 1`.
  - "The start's lowest binary digits fix its first blocks exactly (the starts with a given pattern of first blocks form one class of remainders on division by a power of 2)" is that row in words.
  - "While the orbit has done fewer halvings than the start has binary digits" is `τ < 1`. **Same.**
  - Fresh check, with blocks computed by direct Syracuse steps and not from the state formulas:
    - every pattern of first blocks with `S + 1 ≤ 16`, counting the start's own block, is one residue class mod `2^{S+1}` (16,383 patterns, odd `x < 2^20`);
    - each such class occurs exactly `2^{20−S−1}` times, its coin share `2^{−S} = Π 2^{−(m+s)}`;
    - in three random windows of `2^16` consecutive integers, every such pattern occurs exactly in its coin share.
  - Control: "a full class mod `2^S`" is rejected.
- **Minimax gloss** ("the best worst case over block depths allowed to be any real numbers"). The rows:
  - C-4.6.minimax: "`ρ₀ ≥ κ_p n` … Rozier's minimax, valid for positive reals";
  - C-RW.17: "optimal over real run-length tuples, the extremal tuple growing geometrically at ratio `L`";
  - C-4.thr.6 and N-7: the minimax value is what is attained, not Lemme 4's inequality.

  The gloss is the minimax read in words: the minimum over real tuples of the maximum per-block term. **Same.** Fresh check, for `p = 3..8` and `n = 1000`:
  - the geometric tuple of ratio `L` attains `κ_p n` exactly;
  - 3,000 random real tuples per `p` all have worst case `≥ κ_p n`.

  Control: the ratio-2 tuple does not attain it.
- **§8, depth versus skeleton** (C-RW.23).
  - The row's "hence the row entered" is read as the row's depth. `briefs/williams-letter-findings.md` (Item A) confirms that reading: "Hence the row entered, `k′ = a′ + b′`, also has an exact law", with the entry position `(a′, b′) = (m₊, a₊)`.
  - So "the exit valuation and the entry position, and so the depth k" is exact in Williams's coordinates; the entry position already includes the absorption. **Same.**
  - Fresh check: `s` (Theorem C.3), `m₊` (Theorem C.5), `a₊` (Lemma C.4), and so `d₊ = m₊ + a₊`, agree with `F` on all 5,320 valid states with `ω < 400`, `d ≤ 40`. Equal `(s, m₊, a₊, d₊)` occur with different skeletons `ω₊`.
  - Control: the depth as `m₊` alone fails (447 mismatches on `ω < 200`, `d ≤ 20`).
- **§5's three statements.**
  - Brox: **scope changed** (§4).
  - Rhin's gloss, "a classical limit on how close a power of 2 can come to a power of 3": C-4.5(d) is a lower bound on `K log 2 − n log 3`. **Same.** On the printed staircase `Λ = 9.37·10⁻³` against the bound `1.25·10⁻²⁹`.
  - "Every staircase checked fails at least one": **same** (C-4.ver(c), C-4.6(iv)). On the printed instance, 7/7 size conditions hold and `q ∣ R_r` at 0/7 rotations. Control: "divisible at some rotation" is rejected.
- **§1's trivial-cycle correspondence** (C-2.3).
  - "The trivial cycle 1, 4, 2, 1 corresponds to the state of 1, which the reduced map sends to itself" is C-2.3(a): `(1,1)` is fixed, with fibre `{1}`.
  - "Every other cycle of numbers corresponds to exactly one other cycle of states, and back" is C-2.3(c): the bijection between nontrivial cycles. **Same.**
  - This also resolves cold read 4's item 15 ("exactly" against the excluded trivial cycle).

## 6. Optional wording notes (no scope change)

- **(a) Symbols page, opening paragraph.** "The appendices use many more symbols, among them q, γ, X₀ and p₁(X₀)…" still lists `γ`, which is now in the table and used in §5. Optional: drop "$\gamma$, " from that parenthesis.
- **(b) §5, C-10.** The near-cycle gloss "tested only by the size conditions" sits two sentences before "every staircase checked fails at least one of these divisibility conditions". So the staircases were tested for divisibility too. Optional: "required to meet only the size conditions".
- **(c) §7, O-4.** Round 5 read "digits of 2-adic logarithms of whole numbers, of which the anchors are instances". The bullet now names the anchors' digits and equates them with that class "in standard terms", and it has no main verb. Optional: "\emph{The anchors' digits.} Any progress on the digits of $2$-adic logarithms of whole numbers, of which the anchors are instances (Appendix~\ref{app:laws}), would bear on it --- a problem this paper inherits rather than creates."
- **(d) §3, R-5.** "The only number with that state is 1, since 1 + 1 = 2 gives m = 1, a = 0 and ω = 1": the reason shows that 1 has the state, not that it is the only one. The round-5 text had the same reason in a parenthesis. Optional: "… is $1$: a state of depth $1$ has exactly one number (Proposition~\ref{prop:block}(iii)), and $1 + 1 = 2$ gives $m = 1$, $a = 0$ and $\w = 1$."

## 7. Worked numbers (fresh code)

`experiments/paper1_v4_readable6_check.py` was written for this check from the paper's text: Definition C.1, Lemma C.4, Theorem C.5, Proposition D.1, Hypothesis E.1 and the main text. It imports nothing from the repository. It uses exact integers and Fractions for every integer decision. It reads the TeX, the ledger and the record file it quotes from git at pinned commits. One command, about five seconds:

    python experiments/paper1_v4_readable6_check.py

It writes `experiments/paper1_v4_readable6_check_output.txt` and exits 0. **56 checks, 0 failures; 9 negative controls, all rejected.**

**New worked numbers recomputed:**
- §2: "twice an odd number" (all `4j + 2 < 10^5`); 24 and 22 for `x = 7`.
- §3:
  - `y + 1 = 2ω·3^{d−1}` and `a + m − 1 = d − 1` after the rising steps (odd `x < 200,001`);
  - `13 → (7,1)` with `m = 1`, 40 halving three times; `5 → (1,2)` with `m = 1`, 16 halving four times;
  - the fibre of `(1,1)` is `{1}`.
- §4: the remainders 1, 3, 5, 7; lifting in words is exactly `3^d ω ≡ 1 (mod 8)` (`ω < 2000`, `d < 30`); `(7,1)` with `s = 2` even and `a₊ = 1`.
- §5:
  - `n = 94` as a sum, `K = 149`;
  - `q = 2^K / 2^γ`, with `γ = 6.743758`, outside `[3.683012, 5.140212]`; the trivial cycle has `γ = 2`;
  - 7/7 size conditions hold, 0/7 divisible;
  - Rhin's bound is respected; `Λ = −log(1 − 2^{−γ}) > 2^{−γ}`.
- §6 and App E: the letters `3|1, 1|2, 1|3, 1|1`, then `1|1`, by direct Syracuse steps; ⅛.
- The base-case coding fact, the admissibility witness, the minimax gloss and §8's depth law, as in §5 of this file.

**Text checks (parts A–C):**
- the required fix is verbatim; the four optional notes and two further notes are present;
- the ledger is unchanged between the two commits;
- 19 environments, the Technical summary and the front matter are identical;
- the appendices are reproduced by the five declared edits;
- 78/78 changed sentences match the inventory;
- every named ledger row exists;
- C-5.adm's quantifier, C-RW.15's wording and the record's Rozier quotation are present as cited.

**Controls rejected:**
- a one-character edit in Theorem C.5;
- "full class mod `2^S`";
- the letter `2|1` for `1|2`;
- `K = 148`;
- divisibility at some rotation;
- protection for every start at `τ = 1.1`;
- the ratio-2 tuple attaining `κ_p n`;
- the row depth as `m₊` alone;
- `γ` inside part (i)'s range.

## 8. Record

- Branch `paper1-v4-readable-6-check`, cut at `73d51d4`.
- Deliverables: `experiments/paper1_v4_readable6_check.py`, its output, and this file.
- Not edited: the `.tex`, the PDF, the ledger, and every wiki page. Nothing was pushed.
