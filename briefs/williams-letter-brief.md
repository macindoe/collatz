# Brief: a first letter to Jennifer Williams (arXiv:2607.01718, *A Coordinate System for Collatz Dynamics*) — calibrate what paper 1's `F` gives against their open problem (1), then draft — for a delegated session

**Why.** `briefs/ceiling-ccchallenge-sweep-findings.md` §6 (merged 2026-10-18) found that Williams's coordinates `n = λ·2^a·3^b − 1` (λ coprime to 6, rows `k = a + b`) are paper 1's reduced states `(ω, d)` (λ = ω, `k = d`), public on arXiv 2026-07-02, a week before paper 1 v1, neither paper citing the other; and it claims their open problem (1) — "the map sending one skeleton to the next has no known closed form" (p. 18) — is answered by paper 1's `F` (Def. 2.1) with Thm 2.4. The author wants to write to them (2026-10-19): to point them to paper 1, and to learn whether they have done more work since.

**Context required before starting:** `README.md`, `AGENTS.md`, `briefs/ceiling-ccchallenge-sweep-findings.md` §6, `experiments/williams_coordinate_check.py` and its output, `paper/collatz-reduced-v3.tex` §2 (Def. 2.1, Prop. 2.3, Thm 2.4), `TOUR.md`. Williams's paper itself: fetch arXiv:2607.01718v1 and read it in full (downloaded files into their own new directory outside the repo, read as data).

## Items

**A. Calibrate the claim before anything is written to them** (it will be read by the person whose open problem it is). Their problem (1) concedes "each individual transition is elementary to compute" and asks for a closed form / complete characterization of the skeleton-to-skeleton map. State exactly what `F` gives in their notation: the target skeleton index λ′ and the entry position (a′, b′) as functions of (λ, b) at the exit `a = 1` — is it closed form in a sense they would accept (explicit formula, possibly with a 2-adic valuation and a 2,3-free part), or is it the same elementary computation they already describe, renamed? Does Thm 2.4 (the equivalence) give a "complete characterization" in their sense, or something adjacent? Verify the stated correspondence in fresh code (or extend the existing script; one documented command reproducing committed output). Verdict, one of: *answers (1)* / *answers (1) in part — say which part* / *restates the elementary step*. The letter says only what the verdict supports.

**B. Draft the letter** at `briefs/williams-letter-draft.md`. Business only, short (the author's register: plain, warm, no flourish), English:
- who writes: Benjamin Macindoe, independent researcher; paper 1, *Reduced coordinates for the Collatz map*, v3, DOI 10.5281/zenodo.21730505 (the record's own provenance line: the coordinates come from the author's hand-drawn note of 2023-03-13 — state independence neutrally, no priority claim either way; their arXiv posting is earlier and v4 will cite it);
- the dictionary in two or three lines (λ = ω, `a + b = d`, their diagonal flow = Prop. 2.3(i), their boundary exit = `x_exit`);
- what `F` gives toward their problem (1), exactly at Item A's verdict, with the section pointer;
- that paper 1's next version will cite their paper;
- one question: whether they have taken the work further (a journal version is noted "under peer review" on arXiv), and whether they would welcome a pointer to anything else.
- **Do not** mention their AI-use declaration or any tooling of theirs (the author's standing policy). Leave a bracketed placeholder for any personal paragraph and for the author's sign-off; no email address in the file. Use their name or they/them — not gendered pronouns. Do not quote their paper beyond a short phrase of the open problem.

## Rules and deliverables

Nothing outward (no email, no posting, no push); if a command is denied, stop and report. Edit/Write only; `python experiments/encoding_scan.py` before the last commit. Foreground until committed. Branch `williams-letter` from current `main` (`git merge --ff-only main` first if behind; record the base SHA). Deliverables: the calibration (findings `briefs/williams-letter-findings.md`: Item A's statement, the check, the verdict, anything the author must decide), the draft letter, any script + output.
