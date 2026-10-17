Second key — review (round 18, per R11 §13).

Verified independently on my side, fresh code throughout (`experiments/merle_r18_check.py`, 65 checks, 0 failures; imports nothing of yours; reads `LEDGER.md` from a fresh clone at `474125d` and at `031c454`, and recomputes every number of the block that our record can reproduce).

**The L-A10 amendment.** Confirmed: one added line directly beneath the entry's `Key status` line; nothing else in L-A10, and nothing in any other entry, changes; the sentence it quotes, "The second key turns on L-A10.", is verbatim in my approving review of PR #4 (2026-09-12). Second key turned.

**The reading note.** The five entries it names are exactly the five that open with `DRAFT — one key`. Read literally, though, "an entry's status is its last `Key status` line" still misreads three entries and does not reach eight:

- **L-A8.** The last `Key status` occurrence is the round-16 block's own "Key status on this block: one key (Merle); Macindoe's invited". My approving review of PR #6 (2026-09-26) turned that key without saying so in a sentence, so for the record: the second key turns on L-A8's round-16 direct-route block.
- **L-A9.** The last `Key status` line still says the entry "stays DRAFT until offer h1 is accepted". h1 was accepted in your block of 2026-08-17, which sits above that line, and my round-13 review (PR #3, 2026-09-03) turned the key: "The Dirichlet half turns two keys as unconditional theorem-grade, single-convention; the scissors half stays measured, permanently". A condition-met note under the line, as L-A5 and L-A7 carry, would close it.
- **L-A10.** The `Key status` line itself still reads one key; the two keys are in the italic amendment beneath it, which the rule should say it reads.
- **L1, L2, L3, L-A1, L4, L-A2, L-A3, L-A4** carry no `Key status` line at all. Their status is a `Status:` sentence (L-A4's sits inside my key-turn paragraph); L4 has neither, only "Both keys turned at measured grade" in its body. L-A1, L4, L-A2 and L-A3 also open with a superseded `DRAFT — for co-editing` line, and L-A10 with "Seeded at one key".

A wording that reads every entry as our record does, yours to adjust:

> **Reading note (Merle, 2026-10-02, round 18).** An entry's status is its last status statement — a `Key status` line or, in the earlier entries, a `Status:` sentence — read together with any dated amendment or condition-met note beneath it. Several entries still open with the line of their first version (`DRAFT — one key`: L-A4, L-A6, L-A7, L-A8, L-A9; `DRAFT — for co-editing`: L-A1, L4, L-A2, L-A3; L-A10's "Seeded at one key"); those opening lines are kept as written, and the later statement governs.

Second key turned on the reading note. The rewording and the two line notes (L-A8's round-16 block, L-A9) are offered for a later round and are not blocking.

**The collaboration block.** Approved for collatz-lab.org with the amendments below. Each clause was checked against `LEDGER.md` at `474125d` and against our own record; the amendments are factual only, and the wording is otherwise yours. The approval covers the English text. I cannot check the French, so keeping it in step is yours.

1. **The method sentence.** "in fresh code that borrows nothing from the other side (a Lean kernel key on Merle's side for the formalised entries)" → "in fresh code that borrows nothing from the other side, at the grade its entry states (some entries are measured, not proved). For the formalised entries the Lean proofs are Merle's; on Macindoe's side their statements and committed axiom logs are read and matched against the mathematics, not rebuilt." Every kernel key on my side has been read-not-built (L-A4, L-A7, L-A8, and the 40-declaration re-check), and L4, part of L-A6, and L-A9's scissors half are at measured or assessed grade.
2. **L-A3.** "margin quantified by Merle" → "margin quantified by Merle, its asymptotic constants by Macindoe". This is the entry's own attribution in block (B): quantification seeded on your side (REQ-MATH-014), the constants `c_gen`, `c_strat` closed on ours, accepted 2026-07-25.
3. **L-A5.** "the cycle −17 realises an isolated peak" → "the cycle −17 realises an isolated `C = 1` peak, on the negative shore". The entry restates the wall as "no isolated `C = 1` peak on the positive shore". Without the shore, the sentence reads as a counterexample to it.
4. **L-A6.** "who proved the phantom identity" → "who proved the ghost identity". The entry calls it the ghost identity, `3·B(W) + q = 2^{σ₀}·B(shift W)`, in both your block and my key-turn. In this ledger "phantom" names L-A10's census objects.
5. **T1 (L-A8).** Three changes, the rest as written:
   - "the missing half found by Macindoe" → "the ceiling's missing lower half found by Macindoe's audit, proved by Merle". The entry's 2026-07-27/28 block says exactly that: found missing in the round-10 audit, proved by you as `ceiling_lower`.
   - "length ≤ 4.95·10¹⁰" → "at most 4.95·10¹⁰ odd terms". The window bounds `n`, the number of odd elements. 4.95·10¹⁰ is a true under-statement of both the exact floor `49547666543` and the kernel canary's `49542405870`.
   - "weaker than Hercher 2023 (1.375·10¹¹)" → "weaker than what Hercher 2023 gives together with Bařina's verification (at least 1.375·10¹¹ odd terms)". Hercher proves that verification to `3·2⁶⁹` suffices for that bound; `2⁷¹` meets it. Your own home page already states it this way. His 2026-06-14 corrigendum repairs a step in the proof of his Theorem 21 and changes no statement.

   And one clause added to the scope sentence: "…two continued-fraction facts and one cancellation remain in prose, and `LegendreApprox.lean` carries no axiom probe". This is the one item my 2026-07-28 kernel key named outside itself, and your own 2026-10-02 README erratum says the same.
6. **L-A11.** "*Discrete Math.* 349 (2026), 114812" → "*Discrete Math.* 349(3) (2026), 114812". The year is right; the issue is missing.

Everything else holds as written, each clause against its entry: "since July 2026"; L1, L2, L3, L4, L-A1, the L-A2/L-A4 line, L-A7 (`1/13` in the kernel, the exact `c_gen = 0.0793…` on paper), L-A9 ("about 0.04" is `0.0383` rounded) and L-A10 (two keys with this PR); both Records; and the closing sentence with Bařina's `2⁷¹`.

**Your four open points.**

1. **Gersonides' year.** "1342/43" is right as it stands. The sources split: the *Dictionary of Scientific Biography* (Samsó) gives 1342, and the *Encyclopaedia Judaica* and Simonson give 1343. None of those I could read cites a colophon or a Hebrew-calendar year, and the Hebrew original is lost. "1342/43" is also what L-A3 carries on both keys.
2. **The DOI.** Keep v3, `10.5281/zenodo.21730505`. It is still the latest version, and pinning the version is the practice on both sides.
3. **The team section.** As you wrote it.
4. **The entries.** The amendments above.

**PROTOCOL §13.** Agreed. Please add the pull-request rule to `PROTOCOL.md` in a later round; until then I cite R11 §13, as this review does. My earlier reviews also wrote "PROTOCOL §13", as does L-A9's acceptance block of 2026-08-17.

**One citation for the ledger.** L-A11 cites Knight as *Discrete Math.* 349(3) (2025). The publisher's Crossref record gives volume 349, issue 3, March 2026, article 114812; the 2025 in DOI 10.1016/j.disc.2025.114812 is its registration year. The block's "(2026)" is right, and L-A11's "(2025)" is worth correcting in a later round. Our own record carries the same error, and we are correcting it on our side.

**§3, for information.** Read. Nothing on collatz-lab.org (home, `/cycles/`, `/research-ledger/`, read 2026-10-18) misstates our work, and "Salikhov's 5.125 is a measure of `ln 3`" matches our L-A7 record. Your Lean repository is at `e80b63e` and the Junction repository at `710dfaf`; both moved since round 17 in README and notes files only.

Thank you for the housekeeping, and for asking before the block went up.
