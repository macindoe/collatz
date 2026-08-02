# Brief: does Inselmann's horizon convert to `1/β` reduced blocks? (v3 round 3, major finding)

**Round.** Third external review of the unpublished `paper/collatz-reduced-v3.tex`, reviewed at `dc61306` (= current `main`).

**This is a source-reading task.** You are checking claims *this repository makes about someone else's paper*. Produce a verdict and, if the claims are overstated, drop-in corrections. Change nothing in any tracked file.

## The claim under test

The repository asserts an exact correspondence between Inselmann's horizons and its own, and then leans on it twice — once for the cut's non-binding regime, once for the scope of what AEH adds. The reviewer challenges the conversion itself:

> The claimed threshold `θ < 1/β` needs care. Inselmann proves a natural-density-one trajectory envelope in Syracuse-step time, including the full classical descent horizon; he does not directly count the reduced `F`-blocks, which are renewal times inside that trajectory. Converting his horizon to `1/β` reduced blocks requires the very letter-frequency information under discussion. Inselmann's primary result therefore does not by itself establish that the cut is non-binding throughout the asserted block range.

If that is right, the repository has a circularity: the non-binding regime of AEH's own cut would be justified by a conversion that presupposes AEH's letter frequencies.

## Where the claim is made

Every site must be checked against the source, not against the other sites:

- `aeh.md` L32: "For `θ < 1/β`, `β = 2(2 − log₂3) = 0.8301…`, the cut binds on a vanishing density of starts, the tally denominator is the deterministic `⌈θ log₂ N⌉`, and `13.5`'s standing rule is satisfied as written."
- `aeh.md` L34: "for the *trajectory envelope* and for the ledger's *first moment* it has been crossed unconditionally at natural density `1`, out to exactly `1/β` (Inselmann; `13.3.2`), by a different technique."
- `aeh.md` L42 (§13.3.2), the full Inselmann paragraph: the envelope `(3/4)^k m^{1−ε} ≤ Syr^k(m) ≤ (3/4)^k m^{1+ε}` "simultaneously for all `k ≤ (log₂(4/3))^{-1} log₂ m`"; Corollary `1.4`; and the explicit identification **"His `α = (log 2)^{-1}` is `13.2.1`'s `θ = 1/4` and his `α = 2(log(4/3))^{-1}` is `θ = 1/β`; the classical frontier and its unconditional crossing are the same two numbers seen from the other side."**
- `paper/collatz-reduced-v3.tex` L273–277 (the `θ < 1/β` non-binding sentence), L296–299 (Inselmann "crosses it unconditionally for the trajectory envelope and the first moment"), L307–313 (Cor. 1.4, Thm 1.10, Thm 1.6 as cited consequences), L59 (Related work).
- `publication.md`, the Inselmann bullet under "The 2024–26 landscape" (item 4): "His two horizons are exactly aeh.md `13.2.1`'s own: `α = (log 2)^{-1}` is `θ = 1/4` block per bit (the digit budget) and `α = 2(log(4/3))^{-1}` is `θ = 1/β` (a full descent), ratio `4.8188` both ways." Also the AEH verdict bullet under "Verdicts, claim by claim".

## Why this needs doing now

Round 2 recorded, in its own verification pass (`briefs/v3r2-round-findings.md`, "Stated plainly: what I could not verify"):

> **The external mathematics.** I did not read Tao, Inselmann, Wirsching, Thomas, Korec, Terras or Everett. Every claim about them was checked only for *internal* consistency — paper against `publication.md` against the round's own findings documents. If those findings documents mis-read a source, that error passes through this verification untouched.

So the conversion has never been checked against the source. It was introduced by `briefs/v3r2-contraction-literature-findings.md`; read that document to see what argument was actually made, then check it.

## The task

**Part 1 — Inselmann, arXiv:2402.03276 (v3, Aug 2024).** Get the paper. Establish, quoting the source:

1. The exact statement of Thm 1.10, Thm 1.6, and Cor. 1.4 — hypotheses, conclusions, density notion, and the exact role of `α`.
2. **The time parameterization.** In what time is `k` counted — Syracuse steps (odd-to-odd), raw `T`-steps, or something else? State it exactly, with the source's own notation.
3. **The conversion.** Does `α = 2(log(4/3))^{-1}` in his time correspond to `θ = 1/β` reduced `F`-blocks per bit, and what does the correspondence require? The reduced blocks are renewal times inside the trajectory (`aeh.md` §13.6.3(i): one letter per `F`-block, letter `n` occupying exactly `m_n` raw `T`-steps, with `n^{-1}Σ m_i → E[m] = 2` **on a `B`-generic word**). That last clause is the reviewer's point: if the conversion runs through `E[m] = 2`, it runs through the letter statistics AEH asserts.
4. **The verdict on circularity.** Is the conversion (a) unconditional — Inselmann's own result already controls the block count; (b) conditional on letter frequencies, hence circular in this use; or (c) unconditional but only over a shorter range than `1/β`. If (b) or (c), say what *is* supportable and out to what horizon.
5. Separately: does Inselmann's result support "the cut binds on a vanishing density of starts" at all, or only the trajectory envelope from which the repository infers it? The cut is `x_exit > X_N` with `log X_N = o(log N)`; the inference is that a two-sided envelope keeps the orbit above the cut. Check whether the envelope's lower side actually delivers this, uniformly in the time, at the stated horizon.

**Part 2 — Tao, arXiv:1909.03562 (Forum Math. Pi 10 (2022) e12), Remark 1.13.** The same reviewer, on a different finding, writes: "Tao makes precisely this 'ancient iteration' interpretation when defining the stationary Syracuse random variable from arbitrarily remote negative time. Tao's Remark 1.13 supports the attribution and the need for this distinction." Establish:

1. What Remark 1.13 actually says, quoted.
2. Whether it supports defining the stationary law from an infinite past (the "ancient iteration" reading).
3. Whether the attribution currently paid at `aeh.md` L137 (§13.6.5, citing "Lemma 1.12 and Remark 1.13") is correct as to what each is being cited *for*, and whether a two-sided formulation would owe any further attribution beyond what is already there.
4. Confirm or refute the printed `Syrac(Z/9Z)` values the repository reads off at `aeh.md` L137: `0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63`, and that the mass `2/63` sits at residue `7 ≡ −2 (mod 9)`.

This part feeds a parallel delegate working on the two-sided probability space; report it cleanly and separately, not folded into Part 1.

## Deliverable

Write **only** `briefs/v3r3-inselmann-horizon-findings.md`, containing:

1. the verdict on the conversion, stated in one sentence at the top, unhedged;
2. the source statements quoted exactly, with locations;
3. the time-parameterization analysis;
4. if the claim is overstated: **drop-in replacement text** for every site listed above — Markdown for `aeh.md` L32/L34/L42 and `publication.md`, LaTeX for `paper` L273–277 / L296–299 / L307–313 — saying what *is* supportable;
5. Part 2's findings, separately;
6. what you could not obtain or verify, named plainly.

If the claim survives intact, say so as crisply as you would say the opposite, and record what the supporting argument actually is so the next round need not re-derive it.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file.
- No `git` write operations of any kind. You are working directly in `c:\Users\Ace\Documents\Collatz` on `main`.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`.
- You will need the network (`WebFetch` / `WebSearch`) to obtain both papers. Quote what you read; do not reconstruct a theorem statement from memory or from a secondary description. If you cannot obtain a source, say so and stop rather than inferring its contents.
- Every number and section reference in your findings must be verified against the file or the source, not recalled.
- Do not edit the bibliography or attempt the apply step; that is a later phase by a different delegate.
