# Brief: verify round 3 (v3 round 3, Wave 4)

**Branch.** `v3r3-review-round3`, at `fa07929`. `main` is `dc61306`. Work directly in `c:\Users\Ace\Documents\Collatz` on the branch. **Do not create a worktree.**

**You are the last gate before a merge decision.** Six delegates have run: four design, two apply. Your job is to find what they got wrong — not to agree with them. A verify pass that reports "all clean" without having independently reproduced anything is worthless, and round 2's verify pass is the cautionary example: it stated plainly that it had read no external source, re-run no experiment, and inspected no rendered page. **You are expected to do all three.**

**Read-only on every tracked file** except your own findings file. You may run code and rebuild the PDF.

## Read

`git log dc61306..HEAD` and the full diff. The four design findings (`v3r3-aeh-object`, `v3r3-inselmann-horizon`, `v3r3-cut-weighting`, `v3r3-basecase-density`) and the two apply findings (`v3r3-record-apply`, `v3r3-paper-apply`). The author chose **Option 1** — AEH strengthened to all finite block lengths.

## What this round claims to have established

Check each against the files and, where it is a computation or a reading of a source, against reality:

1. **The equivalence overclaim is gone.** Nine sites asserted AEH *is* Bernoulli genericity while (q1) said the converse was obstructed. Under Option 1 those sites should now be true where they stand. Verify the count and that no site still contradicts (q1).
2. **The Inselmann conversion is circular.** The claim that his descent horizon is `1/β` reduced blocks per bit needs a pair statistic of the parity word he never counts. **Obtain arXiv:2402.03276 and check the theorem statements yourself.** Also check that the surviving claims (the `4.8188` ratio, the `θ = 1/4` end) are stated correctly wherever they now appear.
3. **The bulk cut binds.** `2.64 %` of visits, `15.5 %` of orbits in the flagship run. **Re-run it.** The independent check that needs no code: each orbit contributes exactly 30 visits when nothing is dropped, and `154,389` is not a multiple of 30.
4. **The density inference was false.** Check the counterexample and that the dyadic-shell replacement (`13.2.5`) is correctly stated and correctly used wherever the record now leans on it.
5. **The base case proves the strengthened form below `θ < 1/4`,** and `1/4` is the exact entropy barrier of the method. **Re-run `experiments/aeh_basecase.py`.** Check the rate identity `log 2 − H(2θ)` and the tail identity `P(S_n ≥ J) = P(Bin(J−1,½) < 2n)` yourself, in exact or high-precision arithmetic.
6. **The depth marginal did not move** under the two-sided space. `2/3`, `19/63`, `2/63` and the derived values. Recompute in exact rational arithmetic; do not accept the claim from a findings file.

## Four specific things to attack

**(a) The unbriefed proof edit.** The record delegate added a parenthetical inside Theorem `13.6.4`'s (⇐) proof — that each letter is read off once `D` exceeds its components, the definition quantifying over every `D`. `AGENTS.md` forbids improving a proof during organizational work, so this edit needs an independent reading. Is the parenthetical true? Is the proof correct with it? **Was it necessary** — i.e. was the sentence actually false without it? Say so plainly either way.

**(b) The rendered PDF.** Rebuild from clean (`pdflatex -halt-on-error`, three passes). Then **render pages to images and look at them.** Round 2 checked only extracted text and therefore could not have caught a bad page break, a widow, or a broken display. §5 grew by 1.8× and the paper by two pages; the new material is where damage would be. Report layout defects with page numbers.

**(c) The Appendix A pin.** It reads `b278e5a`, which contains the record but not the paper commit that cites it. Earlier rounds needed a follow-up commit for exactly this (`3511a0d`, `643e864`). Adjudicate: is the pin honest as it stands, or does it need a follow-up? State which commit it should name.

**(d) The two apply deviations lists.** Each apply delegate listed ~10 changes no design delegate specified. Read both lists and check each change against the files. These are the least-reviewed edits in the round.

## Cross-page consistency

`AGENTS.md`'s periodic status pass: diff every page's claims about *other* pages against those pages' own front matter. The round touched `aeh.md`, `itinerary.md`, `bridge.md`, `anchor-digit-search.md`, `publication.md`, two scripts and the paper. Any mismatch is a bug. Check in particular that no page still describes AEH in the retired single-visit terms, and that the two calibration ceilings (block length `L ≤ 2`; the pooled-versus-per-start scope) are stated consistently wherever the campaign is characterized.

Also verify: `≤`, `—`, `ε` render correctly in every edited page (PS 5.1 double-encoding is the known failure mode); no monolith anchor was renumbered beyond the three new ones; no change log, dated journal or "was X, now Y" prose entered a tracked page; and `experiments/aeh_symbolic.py`'s behaviour is byte-identical apart from its docstring.

## The biased-number list

The record delegate produced a list of measured values standing under a protocol whose bias is known but unquantified — including all of `13.6.5`'s orbit adjudication. **Check the list is complete and correct**: are there measured values it missed, and are any of the ones it names actually cut-free? This list is going to the author as a decision, so its accuracy matters more than its length.

Where you can cheaply bound the effect, do — a value whose bias is demonstrably below its quoted precision can come off the list.

## Deliverable

Write **only** `briefs/v3r3-verify-findings.md`:

1. **A defect list, most severe first.** For each: what is wrong, where, and what it would take to fix. If the round is sound, say so — but only after the checks above are actually done, and list what you ran.
2. What you independently reproduced, with the numbers you got, versus what was claimed.
3. The rendered-layout report, with page numbers.
4. The verdicts on (a) the proof edit, (c) the pin, and the biased-number list.
5. **A merge recommendation**: merge as-is, merge after named fixes, or do not merge — with reasons.
6. What you could not check, named plainly. This section is mandatory and must not be empty unless you genuinely checked everything.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file. You may write scratch code to the scratchpad: `C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\7ee86884-4e62-4eca-b73c-3d997568403a\scratchpad`
- Rebuilding the PDF will modify `paper/*.aux`, `*.log`, `*.pdf` in the working tree. That is expected; **do not commit them**, and report whether the rebuilt PDF is byte-identical to the committed one.
- No `git` write operations of any kind: no commit, no branch, no checkout, no push, no merge.
- Never `Get-Content | Set-Content` or PowerShell redirection.
- Every number you report must be one you read or computed, not one you recalled.
- Do not fix anything. Report it. A fix applied by the verifier is a fix nobody verified.
