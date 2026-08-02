# Brief: the exceptional set and the base-case lemma (v3 round 3, major finding)

**Round.** Third external review of the unpublished `paper/collatz-reduced-v3.tex`, reviewed at `dc61306` (= current `main`). You are Wave 2. Two Wave 1 delegates have reported and their results are **inputs you must use, not questions you may reopen**.

**This task has a proof in it.** Unlike the other delegates in this round, you are asked to establish something, not only to restate it. Read the whole brief before starting; the standard for "proved" in this repository is set in `AGENTS.md` and is quoted at the end.

## What is already settled, and binding on you

**The author has chosen Option 1.** AEH now quantifies over all finite block lengths, in letter coordinates. Read `briefs/v3r3-aeh-object-findings.md` §3 (definitions), §4 (Option 1) and §7 (drop-ins) before writing. The observable `W_{k,D}`, the cap `D`, the law `π_{k,D}`, **total variation**, the **two-sided** `B̂`, and §3.6's segment-boundary treatment are fixed. If your proof forces a change to any of them, report it loudly rather than diverging quietly.

**This raises your bar.** A's decisive argument for Option 1 (its §6 item 1) is that the record's own base case already proves the strengthened form, because `aeh.md` L34 bounds `TV(Law(W_n), B^{⊗n})` — the joint law of the whole length-`n` word, not a marginal. **You are the delegate who has to make that true in detail.** If it does not survive assembly, Option 1's principal justification fails and the author must be told.

**Delegate B has refuted the `1/β` support.** Read `briefs/v3r3-inselmann-horizon-findings.md` §0, §2.5 and §3. Its **S1** is an unconditional one-line argument that the bulk cut is non-binding for `θ < 1/4` — exponentially small bad density, proved in-house without Inselmann. That is your item (iv) below, most of the way done; verify it rather than reproving it, and credit it.

**The clock.** Horizons are moving to total-exponent (digits-spent) time, where Inselmann's step count, the repository's cylinder count and the digit budget are all the same unit; a parallel delegate (`briefs/v3r3-cut-weighting-brief.md`) owns that restatement. Your base case is *natively* in that clock already — `{S + 1 ≤ L}` is an exponent-budget event — which should make your statement simpler, not harder. Coordinate by reading that brief; do not duplicate its work on `θ`.

## Finding 1: the exceptional set is a triangular array (cheap, definite)

The reviewer:

> The bad sets form a triangular array depending on `N`. Vanishing bad density in each `[N, 2N)` does not make their unrestricted union density zero. Define the exceptional set using dyadic shells and evaluate each `x` at its canonical shell scale; then the natural-density conclusion follows.

The site is `aeh.md` L32: "Because the bad density vanishes at every scale, the union of the bad sets has natural density zero in the integers — so the statement does deliver 'almost every integer', for a finite-horizon property, with the exceptional set depending on `ε` and `θ`." The same claim is in the paper at L301–304 ("all but a set of starting values of natural density zero carry those frequencies along their first `⌈θ log₂ x⌉` bulk blocks").

Establish exactly what is true. Give the dyadic-shell formulation, prove the natural-density conclusion in that form, and state precisely what the unrestricted union does and does not satisfy. This is the cheapest repair in the round and should be airtight rather than clever.

## Finding 2: the base case is a sketch called a theorem

The reviewer:

> The `θ < 1/4` base case is convincing, but the paper currently sketches only the cylinder count. The literal theorem also needs: extension from dyadic blocks to general `[N, 2N)`; concentration of empirical pattern frequencies; removal of the initial past-boundary; treatment of the bulk cut. These look provable, but should be assembled as a lemma before the paper calls Hypothesis 5.1 a theorem in that range.

Both sites say "theorem" without qualification: `aeh.md` L34 ("**Hypothesis 13.2.1 is therefore a theorem for every `θ < 1/4`.**") and `paper` L288–289 ("Hypothesis~\ref{hyp:aeh} is a \emph{theorem} for every horizon rate `θ < 1/4`").

The four gaps, with what each actually involves:

**(i) Dyadic blocks to general `[N, 2N)`.** The cylinder argument runs for `x` uniform on `[2^L, 2^{L+1})`; the hypothesis samples uniformly from odd `x ∈ [N, 2N)` for arbitrary `N`. Close it or state the restriction.

**(ii) Concentration of empirical pattern frequencies.** A total-variation bound on the joint law is not yet a statement that empirical frequencies concentrate. Under Option 1 this must hold for every finite block length simultaneously, which is where A's justification lives. Note the letter alphabet is countable with geometric tails, so the truncation has to be handled rather than assumed.

**(iii) Removal of the initial past-boundary.** An integer orbit segment has no infinite past at its first visit, while the reconstruction of §13.6.3(iii) reads letters to the left. A's §3.6 answers what the boundary *is*; you must show the boundary's contribution to the empirical frequencies vanishes. Quantify it.

**(iv) Treatment of the bulk cut.** B's S1. Verify and cite.

**Assemble these as one numbered lemma**, stated so that "Hypothesis 13.2.1 is a theorem for every `θ < 1/4`" follows from it by a named implication rather than by assertion. If any of the four does not close, say which, and state what the honest claim is instead — "provable to `θ < 1/4` by this argument, modulo the boundary term" is a perfectly good outcome and far better than a theorem that is a sketch.

**Notation collision to fix.** `aeh.md` L34 uses `L` for the bit-length of the start (`x` uniform on `[2^L, 2^{L+1})`); Option 1 uses `L` for the block length. Choose a convention and apply it throughout your text.

## Deliverable

Write **only** `briefs/v3r3-basecase-density-findings.md`, containing:

1. the dyadic-shell formulation and its proof, with the precise statement of what the unrestricted union satisfies;
2. **the base-case lemma**, stated formally, with a complete proof or an explicit list of what remains open;
3. a verdict on whether A's Option 1 justification survives assembly — stated unhedged, because the author's decision rests on it;
4. **exact drop-in text** — Markdown for `aeh.md` L32 and L34; LaTeX for `paper` L279–299 and L301–304 — consistent with A's §7 and B's §5 drop-ins, and with the exponent-time clock;
5. an explicit note listing every place your text overlaps another delegate's, and which should win;
6. the numerical verification record (below);
7. anything you could not settle, named as an open question.

## Verification

`AGENTS.md`, "Before marking anything proved": *run an independent numerical check (not the one quoted in the text — a fresh implementation), and record what was checked, the range, and the date in the page.*

Your lemma is subject to this. Write fresh code — importing nothing from `aeh_calibration.py`, `aeh_symbolic.py` or `itinerary_coding.py` — and check at minimum: the exact-cylinder claim at the scale you use it; the concentration of at least one multi-letter pattern frequency; and the size of the boundary term you bound in (iii). Report what was checked, the ranges, the seeds, and the counts, in the form the wiki's other verification lines use.

**Write that code to the scratchpad, not the repository:**
`C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz\7ee86884-4e62-4eca-b73c-3d997568403a\scratchpad`
Include the full source in your findings file so the apply phase can promote it to `experiments/` if the lemma lands. Do not add any file to the repository.

## Constraints

- **Read-only on every tracked file.** The one file you may write in the repository is your findings file; scratch code goes to the scratchpad path above.
- No `git` write operations of any kind. You are working directly in `c:\Users\Ace\Documents\Collatz` on `main`.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`.
- Do not renumber any monolith anchor. Append new ones if needed.
- No change logs or dated journals in anything destined for a tracked page.
- Numbers, section numbers and quoted values must be verified against the files, not recalled.
- The paper is **unpublished**; statements may be restated in place. No erratum framing.
- **Do not attempt to prove AEH itself.** The base case at `θ < 1/4` is provable and is your scope; past the digit budget is the hypothesis, and proof effort there is parked per the README stopping rules. If you find yourself proving something past `1/4`, stop and report it as a finding — it would be a major result and must not be buried in a round-3 findings file.
