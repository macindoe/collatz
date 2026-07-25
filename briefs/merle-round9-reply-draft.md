# Round-9 reply — business paragraphs (DRAFT)

Drafted per `briefs/merle-round9-reply-brief.md` (commit `69eebdd`), 2026-07-25.
Branch `merle-round9-reply`, base: main `69eebdd` (wiki main HEAD at drafting time).
Conventions as rounds 7–8, and one more this round: the personal opening and closing
are the author's own, and nothing here answers his personal paragraphs — these are the
business paragraphs only, for the author to fold in, reorder, or cut. Every number,
SHA, and citation below is verified at its named place in
`briefs/merle-la5-closure-findings.md`, `briefs/merle-la6-check-findings.md`, and
`briefs/merle-la7-mu-check-findings.md` (round-9 pointers back to
`briefs/merle-la5-check-findings.md`). Placeholder convention: the bracketed
`[PENDING: …]` field is filled by the author at send time; nothing bracketed is
guessed here. Sending stays with the author.

---

Your closures all check out, and briefly, because they were clean. `49351e5` was read
clause against clause with our offer (a): the restatement is claim-identical on every
required clause, the `−17` exhibit is correct down to `gcd(139, 19) = 1`, and the
`|q| > 1` domain clause landed with it — the two-keys marking is honest on our record,
and L-A5 is closed. On `905d75b`: both records are right, with times attached — your
axioms log entered the stack at 17:29 on the 24th, about two hours after our check
read the tree at `e297d9d` (15:12) — so nothing was mispointed on either side; the
commit graph settles it, and there is no discrepancy of fact.

ContentDescent is acknowledged as the kernel key on the structured half. All five
statements — the cocycle, `power_mult`, `q_pow_factor`, `cycle_iff` in both
directions, `gcd_climb` — were matched clause-by-clause against our 12.6.1.4 descent
identity and the L-A2 gcd law one level up, and your recursive `geom` unrolls to
exactly our `G_k` cofactor, the `q_P/q_B` factor our identity produces. Re-confirmed
clean-room our side: 4,541 exact checks, 0 failures
(`experiments/merle_contentdescent_check.py`). Honest status as before: read, not
built — no Lean toolchain on this side — with the kernel-3 claim resting on your
committed logs, which this time entered in the same commit as the file, so the
earlier gap did not recur.

L-A6: our key turns. The verification report, in brief. The census is exact-confirmed
in your domain — 816,871 words swept, your 18 hits reproduced word-exact, nothing
else, and the frame agreement `q | B ⟺ q | R_0` held at every word, in fact at full
gcd level. One window named, kindly, because your code applies it and the entry does
not state it: the sweep runs `S ≤ 9` from `n = 2`, and "18" is that window's count.
We completed the census to all `S` at `n ≤ 14`: 23 words, and your qualitative claim —
freebies, the `−17` orbit, the forced powers, nothing else — holds *unconditionally*
there, stronger than the sweep verified. The budgets and tail are digit-exact:
`λ = 1.1175` south / `2.6447` north from exact necklace counts against your
1.12/2.64, and the four tail tranches identical at all four decimals.

And your last bolt is not empirical — the ghost identity is a theorem. In the
per-odd-step frame, for every word,

`3·B(W) + q = 2^{σ₀}·B(shift W)`,  with `q = 2^K − 3^n` and `B` always odd;

so for `x = B/q` the valuation `v_2(3x + 1) = σ₀` is *forced* at every step, the
orbit follows the word's itinerary automatically, and a formal hit IS a real cycle —
exactly, not statistically. It is the odd-step refinement of the transport
recurrence's telescope (12.6.1.1 — the same mechanism, per step instead of per
block). Your 18/18 and 300/300 become exact: 23/23 census orbits realized, 350/350
fresh draws on our own seed, and the two-line proof carries the rest, so the budgets
are real-cycle expectations with no correction owed, exactly as your addendum claims.
The calibration reading itself stays at your own assessed grade — our key does not
raise it, and your entry already labels it correctly. Offers, compactly, acceptance
yours: (a) the domain clauses (census window, near-tuned tail band) with the all-`S`
completion as their closure; (b) the ghost lemma as the entry's mechanism sentence in
place of "300/300 random words"; (c) the residual's `n ≥ 61` cut pinned in the entry;
(d) minor wording — "known" before "in existence", primitive-`λ` units, the
semiconvergent note.

L-A7 is the re-check you asked for, and you were right to flag it. Flat: `5.125` is
real and is Salikhov's — but it is the irrationality measure of `ln 3` (Dokl. Math.
76 (2007), 955–957; Wu–Wang 2014 have since given `5.1163051`, again for `ln 3`),
and no measure of that strength exists in print for `log₂ 3`; the two numbers
transfer in neither direction. The construction does not fall. The citable effective
ingredient is Rhin 1987 (Proposition, p. 160:
`|u₀ + u₁·ln 2 + u₂·ln 3| > H^{−13.3}`) — exactly the chain Simons–de Weger 2005 use
on this very problem (their Lemma 12) — and under it the kiosk still provably closes:
corrected headline, total ticket mass beyond `n ≈ 2233` provably `< 5.2·10⁻⁴`, with
`n ≤ 2000` already exact computation on both sides and the computed picture unchanged
(`3.4·10⁻¹⁴` beyond 600). "Effectively finite at every scale" is true under every
sourced row, down to the guaranteed Gouillon floor. The sentence-sized version: the
instrument is right; the ruler's label is wrong; the sourced ruler moves one line and
changes nothing computed. The replication is digit-exact — `C₀ = −5.774` at `n = 2`,
ingredient slack `14.483`, headline cut `N = 600` exact. One number we could not
reproduce: the `≈ 550` crossing — our two natural readings give 372 (per-scale) and
440 (cumulative tail); yours to re-derive or drop. And two further ingredients, named
without ceremony: the for-all-`n` margin inequality `margin(n) ≥ c_gen·n` is verified
to 2000 (minimum slack 2.84, at `n = 2`) but not yet written as a proof — it is
elementary and worth writing down, and we offer to do that our side; and the
best-cell→both-shore step needs the south floor `ε′_n`, unchecked in your artifact —
our slack reads 70.1 at `n = 3`, so it passes, but it belongs in the record. Key
status: ours turns with the re-sourcing — your own wording equally welcome.

Where everything lives: wiki main stands at `69eebdd` as of drafting; the three
findings records are `briefs/merle-la5-closure-findings.md`,
`briefs/merle-la6-check-findings.md`, and `briefs/merle-la7-mu-check-findings.md`,
with the fresh verification code at `experiments/merle_contentdescent_check.py`,
`experiments/merle_la6_check.py`, and `experiments/merle_la7_check.py` (the `−17`
record began in `briefs/merle-la5-check-findings.md`). The round-9 co-edit — the
L-A6 key turn with its offers, the L-A7 verification record with the re-source
offer, and the L-A5 minor items — is prepared and pending push:
[PENDING: shared-repo push — SHA to be filled at send time].

> **[OPTIONAL — the author's call, drop freely]**
>
> One proposal, with no clock on it. "The floor is poured; only the open sky stays
> open" — taken at its word, that is a table of contents: the structured half
> kernel-certified, the lottery calibrated on the one shore where it can be tested,
> the tail effectively finite by published constants. That is a complete and honest
> account of everything short of the wall, and it may be time to write it down
> together — the standing frame is the one already on file, a number-theory-shaped
> note with the formalization as supporting artifact. An invitation, not a schedule.
>
> **[/OPTIONAL]**

No new claims ride along with any of this; everything cited above sits at its named
place in the findings records, and the bracketed field is the only value not yet on
file.
