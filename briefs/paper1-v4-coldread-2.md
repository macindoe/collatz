# Cold read 2 of paper 1 v4 (readable, round 3) — main text, pages 1–17 (Haiku, non-specialist persona, 2026-10-20; input PDF at cbcc8b8)

COLD READ: v4-r3.pdf, pages 1-17 (main text, stopped at the "Technical summary" heading). Persona: EE/music engineer, not a mathematician. Note: the rendered page 17 showed the Technical summary body beneath its heading; I did not read or use it.

NUMBERED LOG (reading order; page, section, quote, rule, fix)

Front matter and abstract
1. p1, Abstract: "a new map that loses nothing ... come out exactly the same" | REREAD | Split into two sentences; say "same answers" once.
2. p1, Abstract: "how a single fixed binary string attached to each state, its anchor, changes from one state to the next" | REREAD (4 ideas in one sentence) | Break into a list of the four laws, one per line.
3. p1, Abstract: "a one-line identity gives short new derivations of two classical facts ... whose strength fades exponentially as the number of blocks grows" | REREAD (5+ ideas), UNDEFINED ("one-line identity" not named or stated until p10; "blocks" not defined until p4; "size" not defined) | Say in one sentence what a cycle is and what "size" means; name the identity forward-reference.
4. p1, Abstract: "passes every size test" | UNDEFINED | Gloss "size test" in the abstract.
5. p1, Abstract: "the minimax value of his extremal profile" | JARGON, not explained | Delete from abstract or gloss as "the best possible value".
6. p2, Author's note: "(p-adic valuations were completely new to me)" | JARGON, not explained | Gloss in a clause or drop the parenthetical.
7. p2, Author's note: "We cleaned my idea up into the states (omega, d)" | UNDEFINED (symbols used before any explanation or the Symbols page) | Say "two whole numbers, called omega and d, defined in Section 3".
8. p2, Version note: "its statements are therefore renumbered" and the DOI/version chain | REREAD (packs 4 version numbers, DOIs, Theorem numbers) | Move the version chain out of the front matter, keep one line.
9. p2-3, Symbols at a glance: 17-row table | READABLE; the table is a usable key. Note "λ, k: Williams's names for ω and d (Section 8 only)" is fine.

Section 1
10. p3, §1: "exponentially far in the number of blocks that a cycle has" | REREAD / JARGON ("exponentially far" is not plain) | "The classical answer: the number of cycles with a given number of blocks must be astronomically small (roughly 2 to the power of the block count)" or similar; say what "far" measures.
11. p3, §1: "The paper proves they go no farther: for every number of blocks from 3 on" | GAP ("they" = counting arguments; the reader has not been told what the argument gives) | One sentence: "counting arguments give a bound; this bound stops giving anything useful at X".
12. p3, §1 "Three levels", item (1): "So the paper does all the halvings at once and looks only at odd numbers" | GAP (the "so" needs "because the result is always even, you can halve in one go") | Add the because-clause.
13. p3, §1 item (3): "its orbits reach the state of 1" | REREAD (state (1,1) vs number 1 ambiguous) | Write "reach the state (1,1)".
14. p4, §1 "What is new" (ii): "For six of the eight kinds of state it is a fixed number" | UNDEFINED ("eight kinds" not defined until p8) | Forward-reference with "(Section 4 sorts states into eight kinds)".
15. p4, §1 (ii): "the global anchor law for the exit valuation" | JARGON (anchor not yet explained beyond the abstract; "law" vague) | Say "the rule that uses the anchor".
16. p4, §1 (iv): "Finitely many binary digits of the state, with three labels of the step" | UNDEFINED ("three labels" defined only on p9) | Forward gloss: "(three numbers describing the step, defined in Section 4)".
17. p4, §1 (iv): "How fast those digits are used up is estimated by an accounting stated as a heuristic, not proved." | READABLE but the "heuristic" is not glossed | Add "a guessed count, not a proof".
18. p5, §1 "What this paper does not claim": "So is the uniform bound against cycles, the trim (Rozier 1991; Simons-de Weger)" | UNDEFINED ("the trim" not defined until p11) | "the trim (a bound on cycles, explained in Section 5)".
19. p5, §1 "does not claim" bullet 4: "The starting values it allows to misbehave are a vanishing proportion of all starting values; that is not the same as a negligible set of orbits." | JARGON ("vanishing proportion", "negligible set", "descent") | Say: "a fraction that shrinks to zero as the size grows, which is weaker than saying almost no orbits misbehave".
20. p5, §1 "(v)" "A one-line identity turns a cycle into conditions of two kinds" | UNDEFINED / forward (identity not stated until p10) | Forward gloss: "(stated in Section 5)".
21. p5, §1 "How to read this paper": "formulas are in the appendices" | INCONSISTENT: main text uses formulas (3^d omega - 1, 3^n = 2^K(1-1/2^gamma) on p10, etc.) | Change to "heavier formulas are in the appendices".

Section 2
22. p6, §2, table: "2^3 ... 2^2*3 ... 2*3^2 ... 2*7" | ARITHMETIC OK. x+1 = 8, 12, 18, 14 factor correctly; binary 111, 1011, 10001, 1101 and x+1 binaries 1000, 1100, 10010, 1110 are correct.
23. p6, §2: "3x+1 is that number minus 2, so it is 2 more than a multiple of 4 and can be halved only once" | READABLE. Good.
24. p6, §2: "The steps from 7 to 11 and from 11 to 17 are rising steps: the result is larger than where it started, because 3x+1 can be halved only once." | GAP (the "because" is only half a reason; "larger" needs x > 1) | Add: "halving once gives (3x+1)/2, which is bigger than x when x > 1".
25. p6, §2: "The trade stops when only one factor of 2 is left in x+1, as at 17" | READABLE.
26. p6, §2: "The whole run — m odd numbers, m−1 rising steps and one cascade — is a block, and m is its entry depth." | READABLE; good.
27. p6, §2 one-division map paragraph: "a block of entry depth m and exit valuation s is exactly m odd numbers followed by s even ones" | READABLE; checked 7, 11, 17, then 26, then 13: correct.
28. p6, §2: "(Appendix D, 'The dictionary with m-cycles')" | JARGON, pointer; "m-cycles" uses m for a different quantity (see 48).

Section 3
29. p7, §3 "Why the state is enough": "one more than the current number is 2 times omega times a power of 3" | READABLE with a stumble (the "power of 3" exponent d−1 is not said here). Add "3 to the power d−1".
30. p7, §3 "Nothing is lost": "Hence the Collatz conjecture holds if and only if every F-orbit from a valid state reaches (1,1)." | GAP ("Hence" with no visible reason between the three facts and the iff) | One sentence linking the three facts to the equivalence.
31. p7, §3: "representative" / "the numbers that share them" | UNDEFINED term for the set of numbers sharing a state (named "representative fibre" only in §8, p16) | Define "the set of numbers with a given state" here.

Section 4 (the stop-point)
32. p8, §4 "The valuation law": "The cascade starts from twice (3 to the power d, times omega, minus 1) (Appendix B), so s is the number of times 2 divides 3^d omega − 1" | REREAD (the "twice (...)" is grammatically ambiguous; it reads as "2 times (3^d omega - 1)", which is not what is meant) | "The cascade starts from the number 3^d·omega − 1; s is how many times 2 divides it."
33. p8, §4: "its anchor: an infinite binary string, running on forever to the left (a '2-adic logarithm'; Definition C.1)" | UNDEFINED / JARGON. The anchor is the single most load-bearing object in the paper and is introduced by a label alone. "2-adic logarithm" is never explained in words. | Give one plain paragraph: what the string is, how the digits are produced, why it is called a logarithm, with the omega=1 case (all zeros).
34. p8, §4: "One fixed number attached to omega, its anchor" vs "an infinite binary string" | REREAD / contradiction in type ("fixed number" vs "infinite string") | Say "one fixed infinite binary string".
35. p8, §4: "s is 2 plus the number of lowest binary digits on which d and the anchor agree, counted from the right up to the first disagreement" | READABLE, and it checks: omega=1, d=2 gives s=3.
36. p8, §4 "The factor of 3": "So the next state gains a factor of 3 exactly when s is even" followed by "in one boundary case it depends on omega ... (its '3-adic' digits)" | REREAD (two "exactly" claims in one paragraph; "3-adic" undefined) | Separate "whether" from "how many"; gloss "3-adic".
37. p8, §4 example: "the number is 21+3=24, a multiple of 3, and the next state (1,2) indeed has a=1" | REREAD (the number 24 is not explained; the next number in the example is 5, and the reader has been told that) | Say what 24 is: "the number whose factor of 3 counts the absorption".
38. p8, §4 "The next depth (Theorem C.5)": "anchor displacement (half the difference between d and the anchor, taken in the same infinite binary arithmetic)" | UNDEFINED ("infinite binary arithmetic") and REREAD (packs three ideas) | Say "computed digit by digit from the right, like ordinary binary subtraction, but never stopping".
39. p8, §4: "the formula makes it at least 1 structurally" | JARGON ("structurally") | "the formula can never give less than 1".
40. p9, §4 "How many digits one step needs (Theorem C.7)": "together with the lowest digits of the absorption" | REREAD / GAP (the absorption was said to depend on omega's 3-adic digits, which the window does not contain) | Say which digits are used, or add one line on how the absorption's low digits are known.
41. p9, §4 "Three outcomes, never wrong (Theorem C.8)": "Call that finite data — the digits, together with the step's three labels (s, the next entry depth and the absorption) — a window, and the number of anchor digits it tracks its depth." | REREAD (dense; "its depth" has no antecedent) | Two sentences: define "window", then "depth".
42. p9, §4: "exactly 1 time in 2 raised to the window's depth plus 1: 1 in 32 (3.125%) at window depth 4, and 1 in 512 (0.195%) at depth 8" | ARITHMETIC OK (1/32 = 3.125%, 1/512 = 0.195%). REREAD: "under the fair-coin model ... with its cut-off, the cap, at least the window's depth plus 2" packs the model, cap and depth in one clause; "the cap" is not defined as a number until p13.
43. p9, §4 "Checks": "were checked by independently written code, with zero discrepancies (Remark C.6)" | GAP (no range, sample size or date given in the main text; the wiki's own rule requires them inline) | Add "over N cases, date" in one line.
44. p9, §4 "The digit budget": "So a window of finitely many digits can decide at most a number of steps proportional to its length." | GAP (proportionality not shown; the claim is only "strongly suggested" elsewhere) | Say "the heuristic suggests" and give the one-line count: about (depth + 6) digits per step.
45. p9, §4 "Where the difficulty is": "So in these coordinates the difficulty of the problem is not spread out: it is the question of where the digits of the anchors come from." | READABLE; good summary, but "not spread out" is a metaphor the reader has to decode.

Section 5 (hard)
46. p10, §5: "the classical bound, the trim, allows" | UNDEFINED at this point (trim first named on p5, not explained until p11). Forward-reference.
47. p10, §5 "A cycle as numbers": "A block of entry depth m multiplies by 3 exactly m times ... and halves m plus s times" | READABLE; checked: m + s halvings per block (m−1 rising, 1+s cascade).
48. p10, §5 "Known exclusions carry over": "Simons and de Weger call an m-cycle, with their m equal to p" | REREAD / clash: m is the block entry depth in §2–§4; here m-cycle means p | Rename: "a p-cycle (their m-cycle)".
49. p10, §5: "Hercher's theorem [20] rules out every nontrivial cycle of F with at most 91 blocks." | READABLE. "Nontrivial" not glossed in §5 (it is defined on p7 as other than 1,4,2,1; a pointer would help).
50. p10, §5 "Size": "Returning to the start therefore forces 2 to the power K to exceed 3 to the power n" | GAP (the reader needs one line: "each +1 pushes the total up, so 2^K must end up slightly above 3^n") | Add the reason.
51. p10, §5 "Size and divisibility (Proposition D.1)": "A positive whole multiple of q is at least q, so q is at most each of these p numbers" | READABLE; good.

Section 5 (cont.)
52. p11, §5 "The uniform trim: a short history", bullet 1: "the best real depths grow geometrically, by a factor of 1.585 ... (the base-2 logarithm of 3)" | ARITHMETIC OK (log2 3 = 1.58496).
53. p11, §5 "In this paper's notation ... (Theorem D.5): in every nontrivial cycle with p blocks" then "so the bound holds for every size-passer" | GAP (the domain widens from cycles to size-passers with no sentence saying so) | Say: "the proof uses only size conditions, so it holds for size-passers too".
54. p11, §5: "the more rising steps a cycle has, the closer 2^K must be to 3^n" | REREAD / IMPRECISE (n counts all multiplications by 3, not "rising steps") | "the larger n, the closer 2^K must be to 3^n".
55. p11, §5: "Combined with Rhin's lower bound on how close a power of 2 can come to a power of 3 [24], it leaves, for each number of blocks, only finitely many configurations to check, with n at most of the order of p times (1.585...)^p" | GAP (the single most important step of the cycle argument is one clause; no reader can follow how Rhin's bound and the trim give a finite list) | Give 3 lines: the trim bounds n in terms of p; Rhin bounds K given n; together they finitely bound every case.
56. p11, §5 "The staircase, as a picture": "Take seven blocks with entry depths 4, 7, 9, 15, 23, 35 and 1, and exit valuations 1, 1, 1, 1, 1, 1 and 49." | ARITHMETIC OK: depths total 94; exits total 55; K = 94 + 55 = 149 (correct). Gamma: 3^94 = 2^149 (1 − 2^−γ) gives 2^−γ ≈ 0.00933, so γ ≈ 6.74 (correct).
57. p11, §5: "The bound known for three-block cycles (Theorem D.6(iv) states it) would demand γ above 8.9 at this n" | NOT CHECKABLE from the page (no formula given in main text) | State the formula in a footnote or give the three-block bound's value.
58. p11, §5: "none of them falls below that three-block constant (each clears it by at least 0.698)" | UNDEFINED ("that three-block constant" was never named) | "the three-block bound's threshold".

Section 5 (cont., p12)
59. p12, §5 "Sharpness", bullet 1: "whose n lies between 1.585 ... to the power p and 5% more than that" | REREAD (ambiguous: does "between" mean "between X and 1.05X"?) | "whose n is at least 1.585^p and at most 1.05 times that".
60. p12, §5: "For 3 to 15 blocks, size-passers with gamma in the same range are found by a computer check of a finite list." | READABLE. Note that the range is checked, not proved.
61. p12, §5: "A configuration's smallest number is tied to gamma: its base-2 logarithm lies within about the base-2 logarithm of p of gamma" | JARGON / REREAD (packs three ideas) | Split and say "within about log2 p of gamma".
62. p12, §5 threshold list: "10 when X0 is at most 16; 22 when X0 is between 2^8 and 2^12; 36 at 2^20; 98 at ... 5 times 2^60; 110 at 2^71; 309 at 2^200" | ARITHMETIC/COVERAGE: values are monotone, but no value is given for X0 between 16 and 2^8, or between 2^12 and 2^20; the list reads as complete but is not. | State the gap explicitly or add the missing ranges.
63. p12, §5 threshold: "computed from the best fraction approximations to 1.585 ... (its continued fraction)" | JARGON, not explained ("continued fraction" never glossed) | One clause: "from the best whole-number fractions that approximate 1.585".
64. p12, §5 "What is attained": "the minimax value of his extremal profile ... his Lemme 4" | JARGON; "Lemme 4" is an untranslated French label | Gloss or delete.
65. p12, §5 "What is attained": "the multiplier in front of the exponential ... cannot be lowered below 0.054. Whether it can be lowered to a constant, independent of p, is left open" | REREAD / CONFUSING (0.054 is itself a constant; the reader cannot tell what is open) | State the open question as "whether the multiplier can be made to not depend on p".
66. p13, §5 "What is left": "The staircases pass every size condition yet fail the divisibility conditions." and p12 "All of these configurations fail the divisibility conditions, so none of them is a cycle." | INCONSISTENT / OVERREACH: the same paragraph says part (iii) staircases "were not tested for divisibility" | Limit the claim to the parts actually tested.
67. p13, §5: "the two remaining halves of the problem, cycles and ever-growing orbits, meet in one configuration, and are in that concrete sense one object" | OVERREACH / JARGON (one example is offered as proof of "one object") | Cut or qualify as an analogy.

Section 6 (hard/lost)
68. p13, §6: "equivalently, about an explicitly computable law for finite pieces of the state" | GAP ("equivalently" not shown) | One sentence of reason, or drop "equivalently".
69. p13, §6 "Letters and the model": "toss a fair coin until it lands tails, and count the tosses" | READABLE, very good. Checked: P(1,2) = 1/2 × 1/4 = 1/8 (correct).
70. p13, §6: "Its 3-adic part, the long-run law of the absorption, is not new here: it is Tao's Syracuse random variable [4], in the present normalisation." | JARGON (3-adic, Syracuse random variable, normalisation, all unexplained) | Replace with "the 3-part of each step follows a known law, due to Tao".
71. p13, §6: "a factor of 3 is gained with chance 1/3, up to the cap: ... exactly when the exit valuation is even, which has chance 1/4 + 1/16 + 1/64 + ... = 1/3" | ARITHMETIC OK (geometric series 1/4 / (1 − 1/4) = 1/3). READABLE.
72. p13, §6: "the classical negative drift holds" | JARGON ("negative drift" not glossed; it is the claim "numbers shrink on average") | Gloss in words.
73. p13, §6: "those values have no upper limit, and a few very long blocks can dominate an average" | REREAD (referent of "those values" unclear) | Name the quantity: "the exit valuations have no upper limit".
74. p13, §6: "The folklore 'ledger' of these facts is thus a theorem about the model" | JARGON ("folklore", "ledger") | Plain: "the usual list of facts is true of the model, not yet of orbits".
75. p14, §6 Hypothesis: "a horizon rate of 1/10 follows 4 blocks, and a budget rate of 1/2 records letters while fewer than 20 halvings have been done" | ARITHMETIC OK (40 digits: 1/10 gives 4 blocks; 1/2 gives 20 halvings).
76. p14, §6 Hypothesis, bullet "The budget is protected": "keep every recorded block's exit above any level that grows more slowly than every fixed power of the starting size" | REREAD / JARGON (packs "vanishing proportion", "fixed power", "level") | "the exit valuations stay below any growing limit, all but a vanishing fraction of starts".
77. p14, §6 "consistent": "4 × 1/10 is below 1/2" | ARITHMETIC OK (0.4 < 0.5). Also "each part of a letter averages 2, so a block uses 4 halvings on average" is correct (2 + 2).
78. p14, §6 "Why the base case holds": "each pattern of first blocks that uses fewer than ten halvings in all ... occurs in exactly its fair-coin share" | GAP (exactness claimed over 1024 integers, 512 of them odd; the reader is not shown why counts are exact) | One line: "the odd numbers mod 1024 are equally spread, so counts are exact".
79. p14, §6 "Why the base case holds": "The errors from longer patterns, and from the sampling, are explicitly bounded (Appendix E), and estimates of how closely frequencies concentrate finish the proof." | GAP (the proof is said to be "finished" by an appendix and "estimates"; the reader cannot see one) | Say that the proof is in Appendix E and is not reproduced here.
80. p14, §6: "The frontier is the classical one: one quarter of a block per digit ... Inselmann goes beyond it without any hypothesis — for the range within which an orbit stays and for its average, measured in single steps rather than blocks, and using a stronger notion of 'almost all' rather than a sharper count." | REREAD (four ideas in one sentence) | Split into a list.
81. p14, §6 "Korec's exponent [3]" and "Terras's counting argument" | JARGON, names only, no gloss | Gloss: "a classical counting limit".
82. p15, §6 "What it would give": "Checking each odd start once, at its own size ... the starts that fail form a set of density zero ... (a theorem of the record, given the hypothesis: aeh.md Proposition 13.2.5)" | JARGON ("density zero") and OUT-OF-PAPER POINTER (a file in the project record, not in the paper) | Gloss density; drop the file pointer from the main text or state it is not included here.
83. p14, §6 "Why the base case holds" and "The hypothesis is the assertion ..." pointer "aeh.md Lemma 13.2.4" | OUT-OF-PAPER: the base-case proof, called "unconditional" and "finished", points to a project file the reader cannot open | Put the proof in the paper or mark the status plainly as "proof in the project record".
84. p15, §6 "How it was tested": "(1) an excess of exit valuation 3, and" | GAP: item (1) gives no reason for its dissolution; the sentence says "each dissolved under a sharper control" | Name the control for item (1).
85. p15, §6 (3): "biases in the binary digits of up to 41 standard deviations" | READABLE; a non-specialist knows "standard deviations" only roughly. Gloss in a clause.
86. p15, §6 (4): "the earlier ratio-of-counts method had picked up as a bias" | JARGON / UNDEFINED ("ratio-of-counts method" is never described) | One clause on what the earlier method computed.
87. p15, §6 (4): "(0.2503 ± 0.0015 measured, against 0.25 expected, over 84,739 visits)" | ARITHMETIC OK (difference 0.0003, inside 0.0015).
88. p15, §6 limits: "the cut it used to keep orbits away from small numbers acts on the next odd core rather than on the block itself" | JARGON, REREAD ("the cut", "odd core", "deciding runs") | Plain version: "the filter that drops small numbers acts on the next number, not the block".

Section 7
89. p16, §7: "What remains is a single question wearing two costumes." | REREAD / GAP (one metaphor, then "three directions are open" in the next paragraph; "single question" is never shown) | Drop the metaphor, or say in one line why the three directions are one question.
90. p16, §7 bullet 1: "rigidity of the closed walk the anchors make around a cycle" | JARGON ("rigidity", "closed walk") | Plain: "the anchors must return to their start after a full cycle".
91. p16, §7 bullet 2: "by transfer operators" | JARGON, unexplained.
92. p16, §7 vs p11: divisibility is cited as "Proposition D.1" on p11 and "Theorem D.6 — arithmetic" on p16 | INCONSISTENT pointer (which result is the divisibility statement) | Check and fix the reference.

Section 8
93. p16, §8: "the representative fibre and intra-block cascade" | UNDEFINED ("representative fibre" never defined in words) | Gloss as "the set of numbers that share a state".
94. p16, §8: "(λ, k) with λ for the odd core omega and k for the depth d" | READABLE.
95. p16, §8: "Williams's open problem (1) [15, p. 18] asks for the map sending one skeleton to the next, and Section 4 answers it in part ... but none for which skeleton is entered, where F restates Williams's Proposition 3.10" | REREAD / CONTRADICTION-LOOKING ("none for which skeleton is entered" then "F restates ...", which is the entry rule) | Say which part is answered and which is only restated.
96. p16, §8: "the anchor formulation, the cycle apparatus, the equidistribution formalization" | JARGON, unexplained ("equidistribution")
97. p16, §8: "The reduced coordinate itself ... was worked out by the author by hand in December 2025 ..." | REREAD (history sentence packs 5 facts) | Split; keep "by hand in December 2025" and the tool names in one line.

ARITHMETIC CHECKED BY HAND (all correct unless flagged above)
- Orbit of 7: 7, 11, 17, 13 with x+1 = 8, 12, 18, 14 and factorizations 2^3, 2^2·3, 2·3^2, 2·7; binaries correct.
- Cascade 52 = 110100 halves to 13 (two halvings, s = 1); block 7,11,17 exits at 13.
- Reduced map chain: (1,3) -> (7,1) [40 = 8·5, three halvings, s=2] -> (1,2) [16 = 2^4, four halvings, s=3] -> (1,1) [4, two halvings, s=1]: all correct.
- Mod-8 table for the valuation law: all 8 cells correct; lifting kinds correct.
- (1,3): 3^3−1 = 26 = 2·13, s = 1: correct. (1,2): s = 2 + v2(2) = 3: correct.
- 24 = 21 + 3: correct.
- Trivial cycle: 4 − 3 = 1 = q, gamma = 2 (3 = 4·3/4): correct.
- Staircase: 4+7+9+15+23+35+1 = 94; 1·6 + 49 = 55; K = 149: correct. gamma ≈ 6.74: correct.
- Fair-coin tail: 1/32 = 3.125%, 1/512 = 0.195%: correct. 1/4+1/16+... = 1/3: correct.
- Words of depth: 4·(1/10) < 1/2: correct; 1/4 block per digit from 4 halvings per block: correct.
- Heuristic average of s + next entry depth = 2 + 2 = 4: correct.
- Threshold list: monotone but incomplete (see 62).
- Empirical 0.2503 ± 0.0015 vs 0.25: consistent.
- Not checkable from the page: 8.9, 0.698, 0.054, 2.71/4.21, 3.68/5.14, 84 found, 84,739 visits, 91 blocks, 41 SD, 5 SD.

SUMMARY: THREE WORST REMAINING PROBLEMS
1. The anchor (the one object the whole argument turns on) is introduced in §4 only as "an infinite binary string ... (a '2-adic logarithm'; Definition C.1)", with the type called "a fixed number" in §4 and "a string" elsewhere, "2-adic" and "infinite binary arithmetic" never explained, and no worked digits. A reader cannot compute s without the appendix. (Items 33, 34, 38.)
2. The cycle argument's key step, Rhin's bound plus the trim giving finitely many cases, is one clause (item 55). Combined with the overreach in §5 ("all of these configurations fail the divisibility conditions" and "pass every size condition yet fail the divisibility conditions" while part (iii) was not tested for divisibility) and "one object" (items 66, 67), the claim the reader is asked to take on trust is larger than what the page shows.
3. Forward references and undefined names pile up in §1 and §4-§8: "the trim" (p5 before p11), "eight kinds" (p4 before p8), "three labels" (p4 before p9), "one-line identity" (p1, p5 before p10), "representative fibre" (p16 only), "m-cycle" (overloads m). Several proof-status claims also point to project files outside the paper ("aeh.md Lemma 13.2.4", "aeh.md Proposition 13.2.5", "briefs/williams-letter-findings.md"), which the reader cannot check.

Also: the p3 claim "Section 2's example, the orbit of 7, runs through Sections 2–5" is contradicted by §5 itself, which uses the trivial cycle and a staircase, not the orbit of 7 (item noted under p3; treat as a bug in the page's cross-reference).

VERDICT PER SECTION
- Abstract and front matter (pp1-2): HARD. Stopped at the author's note's "(omega, d)" and the version-note chain (items 7, 8). Abstract sentence 3 (one-line identity) is the first real stop.
- Symbols at a glance (pp2-3): READABLE. Table is usable; no stop.
- §1 What this paper is about (pp3-5): HARD. First lost point: p4 (ii), "For six of the eight kinds of state" (item 14), with the "global anchor law" (item 15) confirming it.
- §2 One rising run (p6): READABLE. Best section; the worked example checks out. No stop.
- §3 Blocks become states (p7): READABLE. Minor stumble at "Hence ... if and only if" (item 30).
- §4 Exact laws of one step (pp8-9): LOST. First lost point: p8, "its anchor: an infinite binary string ... (a '2-adic logarithm'; Definition C.1)" (item 33). Stop would be there, because every later law depends on it.
- §5 Cycles (pp10-13): HARD. First lost point: p11, "Combined with Rhin's lower bound ..." (item 55). Earlier stop-point candidate: p10 "Known exclusions carry over" (m-cycle clash, item 48).
- §6 Fair-coin hypothesis (pp13-15): HARD, close to LOST. First lost point: p14, "Why the base case holds" (items 78, 79), where the exact 1024-integer count is asserted without the reason.
- §7 What remains open (p16): HARD. First lost point: "a single question wearing two costumes" (item 89).
- §8 Credit and provenance (pp16-17): HARD. First lost point: "representative fibre" (item 93), and "Williams's open problem" (item 95).

Caveat: I did not read the Technical summary or appendices, and I used no other file or web source. Claims marked "not checkable from the page" are only unverified, not wrong.
