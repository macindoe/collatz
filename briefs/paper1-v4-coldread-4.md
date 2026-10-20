# Cold read 4 of paper 1 v4 (Option A, round 5) — main text, pages 1–11 (Haiku, non-specialist persona, 2026-10-20)

Scope note: read pages 1–11 of v4-r5.pdf. The page-11 image showed the first lines of the "Technical summary" under its heading; I did not read on and used none of it for these verdicts.

## 1. NUMBERED LOG (reading order)

Page numbers are the printed page numbers (the PDF page numbers match).

1. p.1, Abstract, "whether every orbit reaches 1" — UNDEFINED (orbit used before Section 1 defines it). Fix: gloss "orbit" at first use: "the sequence of numbers a starting number visits".
2. p.1, Abstract, "with three labels of the step, decides each step" — UNDEFINED/REREAD ("labels" never said). Fix: "with three numbers describing the step (Section 4)".
3. p.1, Abstract, "its anchor, changes from one state to the next" — GAP. The anchor is the central object (Section 4, Section 7) but the main text never says how it is computed from ω; only ω = 1 is shown. Fix: one plain sentence on what the anchor is and how ω fixes it.
4. p.1, Abstract, "the shapes of the successive blocks" — REREAD/UNDEFINED ("shapes" is replaced by "letters" in Section 6; "admissible" undefined; packs four clauses). Fix: say "the (entry depth, exit valuation) pairs of the first blocks", split into two sentences, define "admissible".
5. p.1, Abstract, "a measure of closeness" — UNDEFINED. No words for what it measures anywhere in the main text. Fix: one sentence in Section 5 saying what it measures, before the abstract uses it.
6. p.1, Abstract, "At that threshold scale they attain the best value of Rozier's 1991 real-number optimum (the minimax value of his extremal profile)" — JARGON, not explained in plain words; LOST here. Fix: "(minimax: the best achievable worst case)" and drop "real-number optimum".
7. p.1, footnote and p.1 header, "DOI: [v4 version DOI]" — GAP (unfilled placeholder, repeated on p.2 "DOI [v4 version DOI]"). Fix: insert the real DOI.
8. p.2, Author's note, "into the states (ω,d)" — UNDEFINED (ω and d appear before the Symbols page and before Section 3). Fix: "states (ω,d) (Section 3)".
9. p.2, Author's note, "p-adic valuations were completely new to me as a formal concept" — JARGON, unexplained; acceptable in an aside. Fix: add "(a way of measuring divisibility by a prime)".
10. p.2, Version note, "the classical and contemporary sources of the reduced coordinates' objects and of the elimination identity" and "Theorem C.3's unconditional bound at the odd core 1" — JARGON/UNDEFINED. Skippable version history in the main text. Fix: move the version note to the back matter or after Appendix H.
11. p.3, Symbols table, anchor row missing — GAP: "every symbol the main text uses" is claimed, but the central term "anchor" (and "lifting kind", "absorption") is not listed. Fix: add a short line for the anchor and the lifting kinds, or point to Section 4.
12. p.3, Symbols table, "n — a cycle's total entry depth: how many times it multiplies by 3" — GAP: the table never says n is the sum of the blocks' entry depths, which Section 5's n = 94 relies on. Fix: "the sum of its blocks' entry depths".
13. p.3, Symbols table, "K — one in each rising step, plus each block's final burst" — REREAD: Section 5 describes the same K as "each block halves once per step, n times in all, plus exit valuations". Two descriptions, not reconciled. Fix: state K = n + (sum of exit valuations) once, in the table.
14. p.3, Section 1, "for every number of blocks from 3 on; and, when every number in the cycle must be at least a given size, for every number of blocks from an explicit threshold on (the threshold depends on the size)" — REREAD (nested quantifiers in one sentence). Fix: split into two sentences.
15. p.4, Section 1, item (3) "its cycles are exactly the original cycles" — CONTRADICTION with Section 3 (p.8), where the trivial cycle 1,4,2,1 is excluded and only nontrivial cycles correspond one to one. Fix: "its nontrivial cycles correspond one to one with the original nontrivial cycles".
16. p.4, What is new (ii), "(The valuation law. Section 4; Theorem C.3.)" — JARGON stray label, not explained. Fix: "This is the exit rule of Section 4 (Theorem C.3)".
17. p.4, What is new (iv), "the next burst of halvings is longer than those digits can resolve" — UNDEFINED ("resolve") and REREAD. Fix: "longer than the digits given can tell apart".
18. p.4, What is new (v), "(the minimax value of his extremal profile)" — JARGON, repeated from p.1 without gloss. Fix: same gloss as item 6.
19. p.4, What is new (v), "meets every size condition, for every choice of starting block, at every number of blocks from 3 on" — the claim is stronger than the text in Section 5 (proof from 16 on, computer check 3–15). Fix: add "(by proof from 16 on, by computer check for 3 to 15)".
20. p.5, "What this paper does not claim", bullet 2: "That no fixed, finite number of binary digits can decide an orbit's whole future (Section 4) is the paper's organizing heuristic" — REREAD: as written it reads as a claim the paper makes. Fix: "It does not prove that no fixed, finite number of binary digits can decide..."
21. p.5, bullet 3, "Brox proved that finitely many cycles can have any given number of blocks" — GAP: Section 5 (p.9) credits finiteness to "Rhin's theorem" and never mentions Brox. Fix: say which result gives finiteness in Section 5 and how Brox relates.
22. p.5, bullet 4, "without the range claimed elsewhere" — REREAD (which range?). Fix: "shown with no claim about other numbers of blocks".
23. p.5, bullet 5, "the descent of almost every orbit" and "drift downward or contract" — JARGON/UNDEFINED ("descent" and "contract" never glossed). Fix: "the fact that almost every orbit's numbers tend to shrink over time".
24. p.5, bullet 5, "The starting values it allows to misbehave" — UNDEFINED ("misbehave"; the paragraph also switches to "fraction... shrinks to zero" with no gloss). Fix: "starting values whose letters do not follow the coin pattern".
25. p.6, Section 2, "Here is why it halves only once... 3x+1 is that number minus 2, so it is 2 more than a multiple of 4 and can be halved only once" — GAP: the last step (a number 2 more than a multiple of 4 has exactly one factor of 2) is not given. Fix: "(4k+2 = 2(2k+1), and 2k+1 is odd)".
26. p.6, Section 2, "Write s for the number of the cascade's halvings beyond the first" — REREAD ("beyond the first" not said to be the first halving of the cascade). Fix: "not counting the cascade's first halving".
27. p.7, Section 3, "After the m−1 rising steps, one more than the current number is 2 times ω times 3 to the power d−1: the a factors of 3 that x+1 had, plus one more for each of the m−1 rising steps, d−1 of them in all" — REREAD (three ideas in one sentence). Fix: split into a formula sentence and a counting sentence.
28. p.7, reduced-map bullets, "5 + 1 = 6 is 2 · 3, so the next state is (1, 2): one step" — REREAD ("one step" means the block has one odd number, m = 1; not said). Fix: "(m = 1: a block of one odd number)".
29. p.8, Section 3, "the only number with that state is 1 (one more than it, 2, has m = 1, a = 0 and ω = 1)" — REREAD (muddled parenthesis). Fix: "the only number with that state is 1, since 1+1 = 2 has m = 1, a = 0, ω = 1".
30. p.8, Section 4, "sort the states into eight kinds by the remainder of ω on division by 8" — GAP: the reader is not told ω is always odd (so remainders are 1, 3, 5, 7) or how eight is counted. Fix: add "(ω is odd, so its remainder is 1, 3, 5 or 7)".
31. p.8, Section 4, "On the other two, the lifting kinds, s is at least 3, and it is 2 plus the number of lowest binary digits on which d agrees with a fixed binary pattern belonging to ω" — LOST here. "lifting" is undefined; "a fixed binary pattern belonging to ω" is the anchor again, not yet explained (item 3). Fix: define "lifting" in words and say the pattern is the anchor of item 3.
32. p.8, Section 4 worked example, "The state (7, 1) is of kind (7, odd), so s = 2; that is even, so the next state gains a factor of 3" — REREAD ("that is even" could refer to the kind). Fix: "s = 2 is even, so the next state gains a factor of 3".
33. p.9, Section 5, "with Rhin's theorem it leaves only finitely many candidates at each p" — UNDEFINED/JARGON (Rhin's theorem, "candidates", "uniform trim" never glossed). Fix: one clause: "Rhin's theorem, a classical limit on how close powers of 2 and 3 can get".
34. p.9, Section 5, "The paper rederives that bound by another route, rederives the classical facts that there are no cycles..., and proves that the exponential weakening cannot be avoided" — REREAD (three claims, two "rederives"). Fix: three sentences.
35. p.9, Section 5, "an explicit family of near-cycles, the staircases" — UNDEFINED ("near-cycle" glossed nowhere; "size test" not defined here). Fix: "a near-cycle: a loop that passes the size test without closing up".
36. p.9, Section 5, "The staircases pass every size test, and every one tested fails these divisibility conditions" — REREAD ("every one tested" ambiguous). Fix: "every staircase checked fails at least one divisibility condition".
37. p.9, Section 5 worked example, "Then n = 94" — GAP: no statement that n is the sum of the entry depths (see item 12). Fix: "Then n = 94, the sum of the entry depths".
38. p.9, Section 5 worked example, "(This instance is v3's ... not a member of the family of part (i), whose closeness measure lies between about 3.68 and 5.14 — this one's is 6.74.)" — UNDEFINED: the "closeness measure" has no words or formula in the main text, so 6.74 cannot be checked; "part (i)" has no referent on this page. Fix: state the measure in one sentence and name the theorem part.
39. p.9, Section 6, Hypothesis sentence "for large starting values drawn at random, the letters of their first blocks — recorded while the orbit has done fewer halvings than the start's number of binary digits, over a number of blocks itself a fixed multiple ..., and for every admissible choice of the two multiples —" — LOST here. One sentence carries four nested conditions; "admissible" and "the record's length" undefined. Fix: split into three sentences; define the admissible choices.
40. p.10, Section 6, "in all but a vanishing proportion of starts as the size grows" — JARGON. Fix: "for all but a fraction of starts that shrinks to zero as the size grows".
41. p.10, Section 6, "the start's own digits fix its first blocks exactly (the unconditional base case; proof assembled in the project record, Appendix G)" — GAP (no reason given why the digits fix the blocks) and JARGON ("unconditional base case"). Fix: one sentence pointing back to the representatives of Section 3.
42. p.10, Section 6 worked example, "The running example's letters are (3, 1), (1, 2), (1, 3), (1, 1)" — CLASH: (1, 2) and (1, 3) are also states in Section 3 with a different meaning, and the letters are never tied to their blocks. Fix: write letters as ⟨m, s⟩ or name them "letter of the block 7, 11, 17", and keep states as (ω, d).
43. p.10, Section 7, "Three directions are open: ... that a cycle's anchors are rigid ... the exact windows of Theorem C.8 ... (the method of transfer operators) ... 2-adic logarithms" — LOST here. "rigid", "exact windows", "transfer operators", "2-adic logarithms" are all unglossed. Fix: a plain clause for each, or move the three open problems to Section 7 as a list with one sentence each.
44. p.10, Section 8, "the 3-adic comparisons" and "density results" — JARGON, unexplained. Fix: one gloss each.
45. p.10, Section 8, "Three terms in it come from Williams's paper: ... the representative fibre of a state ... and the intra-block cascade" — REREAD: it is unclear whether the representative fibre is Williams's term or the author's; "cascade" here is a different thing from the Section 2 cascade (the paper flags this in brackets). Fix: say which of the three are Williams's and which are the author's.
46. p.11, Section 8, "It gives exact laws for where a trajectory leaving a row lands the exit valuation and the entry position, and hence which row is entered. It gives no law for which skeleton is entered" — CONTRADICTION within one paragraph (first sentence says the laws give which row is entered; the next says there is no law for it). Stop point. Fix: say that Section 4 gives the exit and entry depth, and that the next row is fixed by F only as a restatement of Williams's Proposition 3.10.

Total: 46 items.

## 2. ARITHMETIC CHECKED

Checked by hand, all correct unless noted:
- 7 to 22 to 11 (22 = 24 − 2, halves once to 11); 3·8 = 24.
- 11+1 = 12 = (3/2)·8; 17+1 = 18 = (3/2)·12.
- 3·17+1 = 52 = 110100 in binary; 52 → 26 → 13 (two halvings, s = 1).
- Binary column: 7 = 111, 11 = 1011, 17 = 10001, 13 = 1101; x+1: 1000, 1100, 10010, 1110. Factorisations 8 = 2^3, 12 = 2^2·3, 18 = 2·3^2, 14 = 2·7. All correct.
- Trailing-zero and trailing-one counts in the rising-step sentence: correct.
- Reduced map of 7: (1,3), (7,1), (1,2), (1,1). 13+1 = 14 = 2·7; 3·13+1 = 40 = 2^3·5, so s = 2 and exit 5; 5+1 = 6 = 2·3; 3·5+1 = 16, four halvings, s = 3; 1+1 = 2; 3·1+1 = 4, two halvings, s = 1. Correct.
- Representatives of (1,3): 7 (m = 3), 11 (12 = 4·3, m = 2), 17 (18 = 2·9, m = 1). Correct.
- Section 4 example: d = 2 = "10", one trailing zero, s = 2+1 = 3; 16 takes four halvings (first plus three). Correct.
- Section 4 example: 5+1 = 6 = 2·3 after the (7,1) block with s = 2 (even, so factor 3 gained). Correct.
- Section 5 example: entry depths 4+7+9+15+23+35+1 = 94; exit valuations 1·6 + 49 = 55; K = 94 + 55 = 149. Correct. Consistency check: 94·log2(3) ≈ 148.99, so 2^149 is about 0.9% above 3^94, matching "slightly larger". The closeness measure (6.74) could not be checked: no definition in the main text.
- Section 6: 1/4 + 1/16 + ... = 1/3 (correct); letter (1,2) chance 1/2 × 1/4 = 1/8 (correct).
- Section 6 letters (3,1), (1,2), (1,3), (1,1) agree with the orbit of 7 (blocks 7–17, 13, 5, 1).
- One-division map example: 7, 11, 17, then 26, then 13. Correct.

No arithmetic errors found.

## 3. SUMMARY: THREE WORST PROBLEMS

1. Contradiction on the central Williams link (p.11, item 46): the same paragraph says the laws give "which row is entered" and then that "there is no law for which skeleton is entered". Also p.4 (item 15) says the cycles are "exactly" the original cycles while p.8 excludes the trivial cycle. A reader cannot tell what is claimed.
2. Notation clash between states and letters (p.10, item 42): (1,2) and (1,3) are states in Section 3 and letters in Section 6 with different meanings, both in the same running example. Compounded by "anchor" being used from p.1 onward without any plain statement of how it is computed (items 3, 11, 31).
3. Dense, unglossed vocabulary at the points where the argument gets hard: the Hypothesis sentence (p.9, item 39), Section 5 (Rhin's theorem, "near-cycle", "closeness measure" with an unverifiable 6.74), and the open-directions paragraph (p.10, item 43: "transfer operators", "2-adic logarithms", "rigid", "exact windows"). A curious reader is stopped in the three most important sections.

## 4. VERDICT PER SECTION

- Front matter (abstract p.1; Version and Author's notes p.2): HARD. Stop point: abstract, "minimax value of his extremal profile" (item 6). The Version note is skippable.
- Symbols at a glance (p.3): READABLE. Stop point: none. Gaps are the missing anchor row and the n and K descriptions (items 11–13).
- 1 What this paper is about (p.3–5): HARD. Stop point: "What is new (v)" on p.4, "minimax" and "staircases" (items 18, 19). The "does not claim" list is clear apart from items 20–24.
- 2 One rising run (p.6): READABLE. Stop point: none. One GAP (item 25); the worked numbers are clean.
- 3 Blocks become states (p.7–8): READABLE with effort. Stop point: "Nothing is lost" on p.8 (item 29). The reduced-map walk-through is the best part of the paper for this reader.
- 4 Exact laws of one step (p.8): HARD. Stop point: "On the other two, the lifting kinds" (item 31). The "anchor" has not been explained.
- 5 Cycles (p.9): HARD. Stop point: "Rhin's theorem" (item 33) and the unverifiable closeness value (item 38).
- 6 Fair-coin hypothesis (p.9–10): LOST at the Hypothesis sentence (item 39). The "Why it matters" and worked example paragraphs are readable once the letters clash is fixed.
- 7 What remains open (p.10): LOST at "Three directions are open" (item 43).
- 8 Credit and provenance (p.10–11): LOST at the contradictory paragraph about rows (item 46).

## 5. FINISH

Could I read the main text to the end? Yes, through the page-11 heading, but only by pushing past a stop point in sections 4 through 8. Not smoothly.

(a) What the paper claims: yes, in outline. I came away knowing that a Collatz run folds into a block and a two-number state, that each step has exact laws, that counting arguments can only go so far against cycles, and that there is a precise fair-coin conjecture. The anchor's role stayed vague.

(b) Why it matters: yes. The "Why it matters" paragraphs in Sections 4–6 gave the stakes in plain words.

(c) What it does not claim: yes, clearly. Section 1's "What this paper does not claim" is the best-written part of the main text. Its wording on items 20 and 23 needs fixing.

Overall for a curious non-specialist: the first three sections work. Sections 4 to 8 would stop most readers, mainly from unglossed jargon and two internal contradictions.
