# Round-11 reply — business paragraphs (DRAFT)

Drafted per `briefs/merle-round11-reply-brief.md`, 2026-07-28.
Branch `merle-round11-reply`, base: main **`9fdaa0f`** (the worktree was cut at the stale
session-start HEAD `2225b68`, which does not contain the brief; it was rebranched onto
`9fdaa0f` — the brief commit, current `main`, carrying all five round-11 findings files —
before anything below was written).

Conventions as rounds 7–10. **Business paragraphs only:** the personal opening and closing,
and anything answering his personal paragraphs — his training, the retraction, the "not a
debt" symmetry, his own two false alarms in one week — are the author's own and are not
drafted here, nor glossed anywhere below. They are marked as placeholders, for the author to
write, fold in, reorder or cut. Sending stays with the author; nothing here has been sent
and nothing has been pushed.

**Two things this draft deliberately does not contain**, both by instruction and both
because they are the author's:

1. **The joint note's contribution sentence.** He asked the author directly and framed it as
   the thing that decides whether the note should exist. This draft carries the *facts* the
   premise check established and stops at a marked placeholder. No wording for that sentence
   is proposed anywhere, in any form.
2. **Any outline, spine, section list or genre for the note.** Round 10 proposed none; this
   round carries the premise-check results, which is a different thing. Nothing below
   recommends a shape.

**Verification.** Every number, SHA, section reference and citation below was checked at its
named place in the five round-11 records as it was drafted —
`briefs/merle-r11-ceiling-audit-findings.md`, `briefs/junction-public-recon-findings.md`,
`briefs/merle-r11-hygiene-check-findings.md`, `briefs/jointnote-premise-ours-findings.md`,
`briefs/jointnote-premise-external-findings.md` — and the load-bearing arithmetic was
additionally recomputed from scratch in this session before it was written down: the
continued fraction of `log₂3` and its denominators `q₀…q₂₅` on the pinned `q₀ = q₁ = 1`
convention, the sides of `q₂₂` and `q₂₃` against `log₂3`, `δ = 2/(3·2⁷¹·ln2)`, the exact and
integral Legendre windows, the discharge criterion at all 22 convergents and its tightest
margin, `θ₂₂/(q₂₂·δ_old)`, the seam identity on all four real cycles both shores, the `−17`
drift sums, `D(x_min)/δ − 1` against `1/(27x_min²)`, `D(1)` and `D(3)` against `2 − log₂3`,
`γ`, `c_gen`, `1 + log₂β`, `S(k) = ⌈k log₂3⌉` over `k = 1..400`, the deficit inequality read
without `ε(k)`, and the `704 / 1536 / 2048` verification comparison. All agreed with the
findings except the one item flagged at (1) below.

**Four things flagged here rather than buried:**

1. *One constant in our own record does not reproduce, and the correction is ours.*
   `briefs/junction-public-recon-findings.md` §4.3(b) gives the limiting gap between his
   `binom(S−1,k−1)` and our `binom(K−2,n−1)` as `log₂(log₂3 / (log₂3 − 1)) ≈ 1.43823` bits.
   Recomputed at 60 digits, that closed form is **`1.43803265928…`**. The findings' two
   finite checkpoints reproduce exactly (`1.34792` at `k = 18`, `1.43752` at `k = 2000`), and
   the finite sequence converges to `1.43803` (`1.43802` at `k = 200 000`), so only the
   printed limit is wrong, by `2·10⁻⁴` bits. Nothing depends on it. The draft writes the
   closed form and `1.438`, and this is worth one line back to that findings file — ours,
   named as ours, in the same spirit as round 10's `35 031 770 966` and the recon's
   spring-2025 dating slip.
2. *Kernel claims remain read-not-built.* There is no Lean toolchain on this side and none
   was installed. The round-11 audit verifies statements, dependency structure, committed
   axiom logs and the truth of every statement as instantiated; kernel-3 / `[propext]` /
   no-user-axiom claims rest on his logs and his four-way-hardened protocol. The draft says
   so in the same sentence as the key language.
3. *`AUDIT_V9` and `STATUS.md` could not be found, and that is a negative, not a denial.*
   The round-10 posture carries over verbatim and is stated in the reply itself: absence of
   a public copy was never evidence against his account and is not now. The V8 audit's
   resemblance to what he described is written **as a resemblance** and nowhere as an
   identification.
4. *The negative-slack count at (b) of flag 6 is a sampling figure.* The findings record
   **8** negative-slack instances over their sampled `k`; sweeping every `k ∈ [18, 500]`
   here gives 19. Same phenomenon, different sample; the worst case is identical
   (`−4.4848` at `k = 306`) and the draft says "at sampled `k`".

**Two bracketed fields, both to be resolved at send time:**

- The round-11 co-edit is a **parallel session's** work and is not claimed here. Its
  shared-repo push SHA is carried as
  `[PENDING: shared-repo push — SHA to be filled at send time]`.
- The wiki-`main` pin is **`9fdaa0f`** at drafting and is marked **CHECK AT SEND TIME**.
  Public `main` is behind; it must be pushed first or none of the artifact pins in the
  co-edit resolve. That check caught a real problem at rounds 9 and 10.

**Placeholders left in the draft, in order:** personal opening; his personal paragraphs; the
joint note's contribution sentence and the answer to his three proposals; personal closing.
Nothing is written inside any of them.

---

> **[PLACEHOLDER — personal opening: the author's own.]**

> **[PLACEHOLDER — anything answering his personal paragraphs: the author's own. Nothing
> below touches them, and nothing below glosses them.]**

---

## The ceiling repair — checked, not accepted

**It is closed, and closed further than we offered.** We asked for either a one-lemma
`ceiling_lower` or a restatement; you removed `hceil` from the four downstream signatures
rather than discharging it at the call sites, which is the stronger of the two repairs. What
follows is what we actually checked, because a repair reported in good faith and still wrong
is the failure mode worth spending effort on.

Lean HEAD `c991430` over `6c084c5` over `5c9b663`, linear, both commits yours, both
2026-07-26. No drift in `ContentDescent.lean`, `ContentSeparation.lean`,
`TransportRecurrence.lean` or `LegendreApprox.lean` — the last recorded explicitly because it
bears on the repository question below.

`ceiling_lower` is **unconditional and entirely in ℕ**: `hstep`, `hK`, `hX : 0 < X`,
`hmin : ∀ i, X ≤ x i`, and nothing else. No `hpX`, no `2^71`, no window, no real-number
hypothesis anywhere in the statement or the proof, whose only inputs are `cycle_prod_identity`
and Mathlib's `Finset` product lemmas. That is the fact that licenses the downstream removal:
had the lemma carried any of those, discharging `hceil` at a call site would have smuggled the
condition back in. And `∏x > 0` is **proved in the file**, not assumed — `0 < xᵢ` from
`0 < X ≤ xᵢ`, then `Finset.prod_pos`. `ceiling_pinned` conjoins exactly the ledger block's two
bounds, `3^(p+1) < 2^K ∧ 2^K < 2·3^(p+1)`, same direction, same strictness, same exponent, with
`hpX` inherited from the upper half alone — which is right, since the lower half needs no size
condition and the upper one does.

**On the removal itself we checked every route by which a hypothesis can leave a printed
signature and still travel.** All four signatures are recorded verbatim at `5c9b663` and at
HEAD; in each pair the entire delta is the deletion of `(hceil : 3 ^ (p+1) < 2 ^ K)` and
nothing else. It is not renamed and not weakened — no hypothesis of any name is added to any
of the four, and the binder lists shrink by exactly one. It is not a structure or class field
— no structure or class is declared. And it is not **hoisted**, which was the route worth
checking hardest: `T1Structure.lean` declares no `variable`, `include`, `omit`, `section`,
`structure`, `class`, `instance`, `attribute` or `local` anywhere in its 482 lines, the only
two structural lines in the file being `namespace T1Structure` and `end T1Structure`. There is
therefore no mechanism by which anything could be threaded into those theorems without
appearing in their own binders. It is genuinely re-derived, by `have hceil := ceiling_lower …`
at two located call sites inside `ratio_bound_at_barina` and `log_gap_gen`, and inherited
transitively by the other two, each of which simply passes one fewer argument. Nothing
unrelated rode along with the repair: the window constants, `2000`/`2079`,
`4000·(p+1)² ≤ 2079·X`, the `2^71` numerals and every conclusion are character-identical
across the diff.

The rest, briefly, because it all reconciled. The T1 axiom log is **13 → 15 exact** — exactly
`ceiling_lower` and `ceiling_pinned` added at the top, nothing removed, renamed or
re-axiomatised, the thirteen pre-existing lines byte-identical including `discharge_all`'s
`[propext]` and `convPairs_length`'s no-axioms line. The `DeficitLemma` log is **10 of 10**,
with `key_shifted` and `key15` now carrying their own probes. `sorryAx` is **absent** from the
whole tree but for two prose lines inside the RETRACTED block, which is present, standalone,
marked DO NOT REMOVE, at lines 312–334, and states all five of the things you list; nothing at
HEAD depends on the retracted result — the non-general `quotient_is_convergent` does not exist
as a declaration anywhere in the tree. The SCOPE header now matches the file it heads, and the
chain it names, `key_shifted → key15 → margin_core → marginTarget`, is exactly the sequence of
declarations at lines 187, 213, 224 and 231.

We also re-derived the repair itself in our own words before reading your proof term: the
product identity, then `3x < 3x+1` per factor with positivity making the product inequality
strict, then right-cancellation of `∏x`. Exact-integer throughout, no analytic input, and
`n = p+1` is the same `n` the rest of the chain uses — no index shift. It agrees with your
one-line summary exactly, and it confirms the round-10 characterisation: the gap was a
formalization gap, not a mathematical one.

**190 exact checks, 0 failures**, in fresh code importing nothing of yours and nothing from
our own round-10 scripts. **No handbacks anywhere this round on the Lean side** — no
discrepancy of digits, hashes, statements or list contents was found.

Five small offers, all hygiene and all your call, carried in the co-edit rather than argued
here: a one-line header on each axiom log saying what it is and how it was produced (the
deleted headers took the four-way claim out of the artifact along with the stale
`LegendreApprox` reference); `#print axioms` probes for `mul_pow_succ_le` and
`pow_succ_lt_two_mul_pow`, the last two declarations in either file that check 4 does not
reach directly; a probe and log entry for `LegendreApprox`'s two theorems; the `1.700 bits`
clause in the `DeficitLemma` header pinned to the route-implied bound (already offered at
round 10, simply still open); and the sharpening below.

## The one-sidedness sharpening — ours, and it tightens our sentence, not yours

Because `ceiling_lower` is now a **theorem** rather than a threaded hypothesis, the log gap's
positivity is a theorem too: `K > n·log₂3` unconditionally for a genuine positive cycle.
Combined with the Legendre step's `n = t·q_m`, `K = t·p_m`, that gives
`K − nL = −t·(q_m L − p_m)`, so a positive cycle can sit only on a convergent lying **above**
`log₂3` — the odd-indexed ones.

Our own `briefs/merle-la8-t1-check-findings.md` §(f) records the first scale the seam chain
cannot exclude as `q₂₂ = 65 470 613 321`, which is the answer to the *two-sided* test
`‖nL‖ < nδ`. But `p₂₂/q₂₂` sits **below** `log₂3` (by `−1.016·10⁻²²`), so that scale can host
only a south-shore configuration. `p₂₃/q₂₃` sits above (by `+9.427·10⁻²⁴`), so the first
admissible **north-shore** scale is `q₂₃ = 137 528 045 312` — exactly Hercher's underlying
threshold.

That is our sentence to fix, not yours; your blocks never stated the two-sided figure. It is
worth a paragraph anyway, because it makes your own frame-prediction point land harder than
you claimed it: the first scale a positive cycle can occupy at all, and the scale the
published record's own threshold sits on, are the same convergent. Verified at both working
precisions, and the convergent sides confirmed to alternate at every `j ≤ 25`.

## The repositories

Thank you for making them public. Your reason is the right one and it is the whole of the
matter — a formalisation nobody can open is a claim, not a contribution — and it converted a
recon we had recorded as *not found* into one we could actually run. The completed recon
follows, and we ran it read-only throughout: unauthenticated clones and public API reads
only, no fork, issue, pull request, comment, star, watch, follow or push against anything of
yours, and no contact with anyone. `Projet_Collatz` stays private by your decision; it was
not requested, not reached, and its absence is treated as a gap in nothing.

**What confirmed, several of it word for word.** The README that claimed an unconditional
no-cycles result for all `k` is there, verbatim — *"For every k ≥ 1, the accelerated Collatz
map … admits no nontrivial positive cycle of length k"* — and so is its rewrite, seven hours
later the same day, commit `1a56828`, whose own message reads *"reduce claim to what is
actually proved"*. The two asymptotic programs with a named unclosed gap each beyond
`k = 200` are `docs/PROOF_ASSEMBLY.md` §2, verbatim, one gap per path. The preprint states in
its own text that complete cycle exclusion for `k ≥ 69` needs the additional Hypothesis (H)
(`rem:junction-scope`), immediately after saying that nonsurjectivity alone does not exclude
cycles. The scope banners go **further** than you described — they tell readers by name not to
cite the broken module. Simons–de Weger appears as a genuine `axiom` declaration, which is the
item round 10 could only record as not verifiable. And the licence account checks out in every
particular, including which repository had none: `collatz-audit-2026`, MIT added at the flip
in `eb237b3`, 2026-07-26 21:25:49 +0200, message *"Add MIT licence before making the
repository public."* — the only commit anywhere in the four dated later than 2026-04-25. "Last
pushed 22 April" for the Junction repository is correct to the second.

One flat observation on the shape rather than the substance: the material is distributed
across two repositories rather than one. The overclaim, the rewrite and the status page live
in `collatz-cycles-lean`; the `k ≥ 69` clause is in the Junction preprint; the plain-words
"does not prove the Collatz conjecture" is in `collatz-nocycle-lean4` only. **Your self-audit's
substance stands.**

**Three things did not match, and here is the posture first, because it is the same one we
took at round 10 and nothing has happened to change it: absence of a public copy was never
evidence against your account, and it is not now.**

- **No `AUDIT_V9`** in any ref of any of the four — searched by working-tree find, by
  `--diff-filter=A` over all history, and by pickaxe. The public series stops at **V8**,
  `AUDIT_V8_RESULTS.md`, added 2026-03-07, whose verdict is *"LE SQUELETTE STRUCTURAL
  TIENT … L'ABSTRACT SURAFFIRME"*. We record that **as a resemblance and not as an
  identification**: it is the same shape of verdict as the one you described, three months
  earlier, and it is not the file you named. Whether `AUDIT_V9` is somewhere we have not
  looked and are not going to look is not settled by anything public, and we do not settle it.
- **No `STATUS.md`** by that name anywhere in the four. The document that does the job is
  `collatz-cycles-lean/VERIFICATION.md`, rewritten in the same commit as the README, and it
  does the job well: it marks its own headline module **INVALID** by name, marks its own
  asymptotic argument INVALID, and leaves the general claim OPEN.
- **One straggler from the rewrite, and it is the one with practical consequence.**
  `docs/PROOF_ASSEMBLY.md` was added earlier the same day and has never been modified since.
  At HEAD it still closes §10.6 with *"No gap remains. The proof is unconditional for all
  `k ≥ 3`."*, and marks `k > 50000` **PROVED** — about the Range Exclusion module the README,
  `VERIFICATION.md`, `WARNING.md` and `AUDIT_CORRSUM.md` all mark as computing the wrong
  function. So a reader who opens `docs/` before `VERIFICATION.md` meets the withdrawn claim
  first. That is a one-file loose end from an otherwise thorough retraction; it is small, and
  it is the only reason it is mentioned at all.

**`LegendreApprox.lean`: home confirmed, and the diff we had recorded as NOT PERFORMED is now
performed.** The Junction copy is at `lean/skeleton/LegendreApprox.lean`, blob `a4fae1f`,
entered at `09f481b` on 2026-02-26 and byte-identical to HEAD — **upstream by five months**,
and byte-identical to the `collatz-cycles-lean` copy. Against the T1-chain copy (blob
`b55095a`, unchanged at `da2c8db`, `5c9b663` and current `c991430`) it is **not** byte-identical
— and the entire difference is a two-line reordering of `open Real` relative to the namespace
line. Same 3,175 bytes; not one character of any statement, hypothesis, binder, docstring or
tactic differs; the three declarations are identical in both. Nothing in T1 turns on it, and
your `da2c8db` commit message is accurate as to origin. The build contexts differ (v4.29.0-rc2
against v4.27.0) without bearing on T1, which compiles its own copy.

**Flag 6 is upgraded from settled-by-units to settled-on-the-definition.** The preprint
*defines* `S = S(k) = ⌈k log₂3⌉` with `k` the number of odd steps — which is our `K` with our
`n`, same formula, different letter — so there is no correction to the round-10 settlement,
and the naming clash with our own `S = K − n` is real and is yours, not ours. Checked in exact
integers: `S(k) = ⌈k·log₂3⌉` for every `k = 1..400`, 0 mismatches, with `S(3) = 5`, `S(5) = 8`,
`S(100) = 159` reproducing the preprint's own printed values.

Two flat differences newly visible now that the preprint can be read, neither knowable from the
committed scripts, and both recorded so a joint note cannot let the two forms be read as one:

- **The preprint's statement carries an error term and ours does not.** The proposition is
  `log₂ d − log₂ C ≥ (S−1)·γ − ε(k)` with `ε(k) = O(log k)`; your own transcription in
  `test_REQ-MATH-037_junction_gamma_is_cgen.py` drops the `− ε(k)`. Harmless for the identity
  that script tests, which is a statement about constants — but read literally without it the
  printed inequality **fails**: negative slack at sampled `k`, worst `−4.485` at `k = 306`,
  and `−2.451` at `k = 200`, every failure sitting at or near a convergent denominator, which
  is exactly where `log₂ d` falls furthest below `S` and exactly what `ε(k)` exists to absorb.
  Our own margin uses `K` where the preprint uses `log₂ d`, so it carries no error term at all.
- **The binomial index differs by one.** The preprint counts `C = binom(S−1, k−1)`; our L-A7
  word count is `binom(K−2, n−1)`. Yours is the larger, by `1.348` bits at `k = 18` and by
  `log₂(log₂3/(log₂3 − 1)) = 1.438` bits in the limit. Otherwise the two forms are term for
  term the same statement.

For what it is worth on the reading question the preprint answers: its own version of the
lemma is exhibited on `k ∈ [18, 500]` plus an asymptotic argument in which `c` and `ε(k)` are
never made explicit. That is the idea and the constant, which is what our record needed to
know it supplies, and it is not an effective inequality. No comparison of merit is drawn from
that and none is needed — our Theorem A supplies the effective form for the `K`-form
elementarily, and your rational-binomial `marginTarget` route supplies it at `1/13` in the
kernel.

## Prior art of yours, which we would rather say first

`collatz-cycles-lean/docs/PROOF_ASSEMBLY.md` **§10.5, dated 17 March 2026** in the document
header and committed 2026-03-26, reads:

> **Consequence:** The "dangerous" `k` values (where `{kα}` is smallest) are confined to
> convergent denominators `q_n` of the continued fraction of `α`. No other `k` can approach 0
> more closely. This regularizes the problem: we only need to check that the Baker bound holds
> at convergent denominators.

That is the L-A8/T1 frame-prediction point — thresholds live on the convergent grid — written
down on your side four months before these rounds began, in a document you have not cited for
it. §10.2 of the same file gives the continued fraction of `log₂3` to 10,000 terms, and §10.4
tabulates the irrationality measures, including the same Rhin 1987 / Salikhov 2007 /
Wu–Wang 2014 list the L-A7 re-sourcing adjudicated. We are saying this because you have not,
and because a date and a document are easier to record now than to reconstruct later. No
priority is being adjudicated in either direction, and nothing of ours is displaced by it.

Two further comparisons, recorded flat and now, so the two records can never be conflated
later:

- **Your Range Exclusion is our uniform-trim geometry in other coordinates.** Ours derives
  from the rotation size conditions that a cycle forces `2^K` close to `3^n`; yours confines
  `corrSum` to an interval of width `3^r − 1` around `3^k` and asks whether `d = 2^S − 3^k`
  can divide anything in it. Same geometry, different coordinates, and the closeness is the
  whole content on both sides. Your §3.1 "Forced Flatness Theorem" has no counterpart in our
  record at all.
- **Your `3^(−0.415k)` is *not* our `1.585^(−p)`, and the proximity is a coincidence of two
  constants.** `3^0.415 = 1.5777…` is `3^(2 − log₂3)`; our `1.585` is `log₂3 = 1.58496…`; and
  your exponent counts odd steps `k` where ours counts blocks `p`. Two different quantities
  that happen to print alike. Relatedly: there is no counterpart anywhere in the four to the
  staircase family or to any statement that counting arguments cannot do substantially better;
  the word *escalier* does occur in the Junction research log, for the lattice path traced by
  `2^a 3^b`, which is a different object.

Nothing found in any of the four would change a claim of ours.

## The hygiene pass

Everything reconciled and nothing failed. **115 checks, 0 failures**, and at the strongest
grade available rather than by reading: the three previously orphaned outputs now have their
generator scripts, and all five relevant scripts — 043, 055, 056 and the repaired 052, 053 —
were **run here**, on a different machine, and reproduce their committed outputs
byte-identically (two of the five differ only in an em-dash mangled by our own console's
codepage on redirect, which is our artefact and not a difference in your files). Every number
was then independently recomputed in code that imports none of yours: the six thresholds under
both constants, both windows and the `0.010617 %` loss — the same number round 10 rounded to
`0.011 %` — the 22 convergents, `5.1713×` against the exact `5.4433×`,
`δ = 4.073367·10⁻²²`, and the best-approximation property re-verified over all 190,536 values
of `n < q₁₃ = 190537`.

**`5.17× at j = 21` is correct.** We queried the index and we were wrong; the tightest
discharge margin really is at `j = 21`, `q = 6 586 818 670`, recomputed at all 22 convergents
under the pinned `q₀ = q₁ = 1` convention, and the exact test is tightest at the same `j`.

The stale index did survive, but in a different file: `T1Structure.lean` at `c991430` carries
**two different `q₂₁`** 245 lines apart — line 188, the `seam_bound` docstring, has the shifted
`6.547·10¹⁰` and calls Hercher's threshold `q₂₂`, while line 433, the discharge docstring, has
the correct `6586818670`. The same docstring at line 186 still carries the **pre-054 `δ`**,
`‖n·log₂3‖ ≤ n/(3X·ln2)`, missing the factor 2, and the file header at line 14 still prints the
withdrawn `4.955e10` as a current fact. None of it touches a theorem, a proof, or any number
entering the discharge; the sweep reached the Python and not the Lean comments.

**The `053` argument holds, and the precision worth adding is a compliment.** The monotonicity
direction is valid and needs no hypothesis at all: writing the test as `P_d(j) := [θ_j ≤ q_j·d]`,
the right side is strictly increasing in `d` for fixed `j`, so a smaller `d` gives a subset of
admissible `j` and therefore a first admissible `j` that is no earlier. Nothing about how `θ_j`
or `q_j` behave in `j` is used. What that gives is `≥ 22`, not `= 22`. The equality is a
separate computation — that `j = 22` clears the *old*, stricter test as well — and it clears it
by a factor of only **`2.0039×`** (`θ₂₂/(q₂₂·δ_old) = 0.499018`). Had the slip been a factor of
three rather than two, the answer would have moved. You ran that check, and it is right; so
"no result changed, only the reasoning became correct" holds, with the reasoning supplying the
inequality and the computation supplying the equality. One fact makes your sentence general
rather than instance-bound: the admissible set is an **up-set in `j`**, because `q_j·δ/θ_j` is
strictly increasing (`θ_j ≍ 1/q_{j+1}` and `q_j q_{j+1}` increasing), so "first admissible" is
well defined under any `δ` and moves rightward monotonically as `δ` shrinks. Both verified over
`j = 1..29`.

**Your citation claim confirmed**, on the side where only we can check it: no altered `θ_j` or
`δ` figure — the printed `δ`, the whole halved `θ_j/δ` column, the `0.48×` Hercher line, the
shifted `q₂₀…q₂₅` list, the `PREMIER j admissible : j=21` line — is cited anywhere in the shared
`LEDGER.md`, `NOTE.md` or `PROTOCOL.md`, or in any of our `briefs/merle-*` correspondence
records. The only hits on those denominators are our own independently computed convergent
lists.

Three flat artifact notes, in descending order of size. The `q₂₁`/`q₂₂` subscripts and the
pre-054 `δ` above are the first. The second is the one with a live consequence:

**The `OUT-052` `(d-bis)` deletion.** The same pass that cleaned `OUT_REQ-MATH-052.txt` removed
its `(d-bis)` Ostrowski section — the table carrying *"mediane eps-petits : 15601 | mediane
controle : 1"* and the expansion `14936 = 22·665 + 306`. The committed
`test_REQ-MATH-052_chaine_T1.py` does not produce that section (we ran it; its output is now
byte-identical to the cleaned file), so it came from an uncommitted script — the same
two-runs-stitched-together pattern you identified in 053, in the other file. The consequence is
that the shared ledger's own **L-A8 seed block cites exactly those numbers** — *"median lowest
denominator 15601, against 1 for controls; e.g. `14936 = 22·665 + 306`"* — and at HEAD that
sentence has no committed artifact behind it. No figure is disputed and nothing about the grid
half is in question; the observation is only that the supporting artifact was removed rather
than restored. The clean remedy is the one you just applied yourself to 043, 055 and 056:
commit the script that produced the table. (A smaller note in the same file so the reading is
never mistaken for a contradiction: the committed 052 script's own coarse grid test prints
`tous ancres sur la grille ? False`, because its `near_grid` helper tries single-denominator
anchoring only. The deleted `(d-bis)` table, using the full Ostrowski expansion, is the stronger
test and the one the ledger sentence rests on.)

Third and smallest: **Cor. 29's `X₀ ≥ 3·2⁶⁹` is promised and not landed** — no occurrence of
`3·2⁶⁹`, `1536·2⁶⁰` or the Corollary-29 condition anywhere in the Lean repository. Its natural
home is ledger prose and the ledger has not moved, so this is a note, not a complaint.

## The four negatives

Received as offered — flat, claiming nothing, verified in the same register.

**Your retraction is confirmed, on a common footing.** All four lag-1 autocorrelations
reproduce, to three decimals, **once the statistic is read as the lag-1 correlation of
`log aᵢ`**: `log₂3` `−0.0700`, π `−0.0631`, `log₂5` `−0.1035`, `log₂7` `−0.1032`, against your
`−0.070 / −0.063 / −0.104 / −0.103`, over continued fractions built here from scratch at two
precisions with the number of *stable* partial quotients asserted before any statistic was
computed. One scope clause and not a correction: on the **raw** partial quotients the same four
series give an order of magnitude less and essentially noise (`−0.0055 / −0.0012 / −0.0039 /
−0.0088`), because under Gauss–Kuzmin `aᵢ` has infinite mean and infinite variance, so a raw
Pearson is dominated by its single largest term — here `max aᵢ = 20776`, in π. Taking logs
first is the right choice; the letter says "autocorrelation of the partial quotients", and a
reader reproducing it literally will get `−0.006` and think something is wrong. The rank version
gives `−0.086 / −0.083 / −0.127 / −0.114` — same sign, same ordering, same conclusion, so
nothing depends on the choice. And the retraction stands on the numbers: `log₂3`'s `−0.070`
sits *inside* the range of the three controls and is the second smallest in magnitude of the
four.

**One question, and it is a question and not a dispute: `0.00103`.** The substantive claim —
that `log₂3` is statistically ordinary — survives every reading unqualified: the largest bin
deviation from Gauss–Kuzmin over 2000 partial quotients is `0.008425`, and `χ²/dof` stays below
`0.567` at every binning from 3 to 40 bins. The number itself we could not place. As a
chi-squared **statistic** it should read between `1.079` and `22.10` across those binnings — and
a statistic of `0.00103` over 2000 draws would be a fit far too good to be random rather than a
good one. As a **p-value** the readings are `0.9997` down to `0.9982`, so `0.00103` would mean
**rejection** at the 0.1 % level, which is the opposite of what your letter concludes. As a
**normalised distance** it is in the right decade under three natural readings — `χ²/N` gives
`0.000540`–`0.011048`, KL `0.000273`–`0.005947`, squared Hellinger `0.000137`–`0.003466` — and
the closest single reading we found is `χ²/N` at bins `{1},…,{9},{≥10}`, which gives `0.001214`.
So it is a normalised distance; which normalisation and which binning is not recoverable from
the letter, and the readings that land in the right decade span a factor of twenty. One clause
naming the two would settle it, and nothing in the conclusion depends on the answer.

The rest of item 1 reproduces exactly: denominator ratios `1.01799` to `55.5836` (the max at
`q₁₄/q₁₃`, the partial quotient 55; the min at `q₁₅/q₁₄`, a partial quotient 1), and the same
min and max for every window `j = 1..h` with `h ≥ 16`, so the range does not depend on where you
stopped; φ's denominators exactly the Fibonacci numbers for the first 30, its ratios inside
`[1.617978, 1.618056]` beyond `j = 10`.

**Your scoping of that result we accept as you wrote it, and it is worth endorsing rather than
merely recording.** Statistical ordinariness closes arguments that need `log₂3` to be
*peculiar*; it does not touch arguments resting on **effective diophantine input**, because an
effective irrationality exponent is perfectly compatible with a Gauss–Kuzmin-typical continued
fraction. Our own L-A7 chain is the live example — it consumes Rhin 1987's effective exponent
`13.3` and would consume it identically whatever the partial quotients looked like. That
distinction is right, and our use of Rhin depends on it.

Item 3's structural claim is exact and we verified it as such: with the `1/x` term dropped and
`v` averaged under `P(v = k) = 2^{−k}`, mean exactly 2 — both per-step arithmetic means over
odd steps, which is the convention in which such claims are usually lost — the per-step drift
is `D_a = log₂a − 2`, so `D_a < 0 ⟺ log₂a < 2 ⟺ a < 4`, exactly, for every integer `a`. Among
odd `a` in `3..31`, `a = 3` alone is negative. Your empirics we have recorded as yours and
unreplicated: replicating `+0.22`, `−0.29` and `−0.57` would mean recomputing cycle counts for
`ax+1` over odd `a`, which is a cycle search, and our own stopping rules forbid it. So those
three numbers stand entirely on your side of the two-key protocol and we will describe them
that way wherever they are used. Nothing structural is lost by that; the only non-empirical
statement in item 3 needs no search at all.

## Item 4 — one theorem to hand back, and it is not the one you name

This is the substantive one, and it is stronger than you stated it.

> **The identity.** For a cycle of the odd map with `n` odd elements and `K = Σ vᵢ`, the
> summed per-step drift equals the log-seam gap **exactly**, on both shores:
> `Σᵢ log₂(1 + 1/(3xᵢ)) = K − n·log₂3` (north) and
> `Σᵢ log₂(1 − 1/(3yᵢ)) = K − n·log₂3` (south).

Three lines: each step gives `3 + 1/xᵢ = 2^{vᵢ}·x_{i+1}/xᵢ`, the `x`'s telescope around the
cycle, `Σvᵢ = K`, so `∏(3 + 1/xᵢ) = 2^K` and `Σ log₂(3 + 1/xᵢ) = K`; subtract `n·log₂3`. The
south shore is the same computation on `3yᵢ − 1 = 2^{vᵢ}y_{i+1}`. Verified on **all four real
cycles, both shores**, agreeing to 45 digits in every case.

Its right-hand side is `log₂(2^K/3^n)` — precisely the quantity T1's chain bounds. So "a third
face of the same wall" is right, and the drift does not merely *bound* the seam gap: **it sums
to it exactly**. That is a structural statement, not a measurement, and it is the seam identity
written one step at a time.

Two corrections inside the same hand-back, both flat.

**"Summed around a cycle that is exactly `n·δ`" is a sharp bound, not an identity.** `D` is
strictly decreasing, so for a cycle with all elements `≥ X`, `Σᵢ D(xᵢ) ≤ n·D(X)`, with
equality **if and only if every element sits at `X`** — which no cycle achieves. On `−17` the
sum is `0.18834` against `n·D(x_min) = 0.39608`. At `X = 2⁷¹` the two sides agree to 44 decimal
places, which is presumably why it reads as exact.

**What is exact is the constant identification, and it is the real content:**

> `D(x_min) = δ · (1 + 1/(27·x_min²))`,  `δ = 2/(3·x_min·ln2)`

— that is, **`δ` is the per-step north–south drift evaluated at the minimum element, and it
sits strictly *below* that drift**, by a relative `1/(27x_min²) = 6.643·10⁻⁴⁵` at `2⁷¹`. (`D`'s
series in `u = 1/(3x)` has all positive higher terms, so `D(x) > 2/(3x·ln2)` strictly; the two
figures agree to every printed digit at `2⁷¹`.) And the factor 2 in `δ` is *exactly* the
two-shore doubling, `log₂(1+u) − log₂(1−u) = 2u/ln2 + O(u³)`. That last point is a reframing
rather than a confirmation, and it is the gain: in our own la8 derivation that factor 2 arrives
from a **crude step**, the two-bound `(m+1)^n < 2m^n` used to control a difference of powers.
In the drift reading it arrives from a **symmetry** — north and south contributing one unit
each. Two mechanisms landing on the same 2, and the drift reading is the one that explains the
constant as structure rather than as slack. No number moves.

`x* = 7/3` is exact and unique, and the uniqueness is where the content sits:
`D(x) = log₂(4/3) ⟺ 3(3x+1) = 4(3x−1) ⟺ 3x = 7`, one linear equation, one root, with `D`
strictly decreasing on either side. Your `9.8·10⁻²²` at `2⁷¹` we reproduce as `9.8145·10⁻²²`.
The one gentle note: the identity quoted to justify it, `log₂(4/3) = 2 − log₂3`, is a
tautology — it carries the claim rather than being it. **The corollary with integer teeth is
yours to have:** since `7/3` lies strictly between the odd integers 1 and 3 and `D` is strictly
decreasing, `x = 1` is the **only odd positive integer** at which the sign information exceeds
the drift (`D(1) = 1` exactly, against `2 − log₂3 = 0.415`; `D(3) = log₂(5/4) = 0.322` is
already below it, and it falls from there). Which is to say: the `±1` outweighs the drift at
exactly one odd integer, and that integer is the trivial cycle. Everywhere else the terrain is
grey, in your words, and at `2⁷¹` the sign is worth `10⁻²¹` of the drift.

## The joint note — what we checked, and then it is yours

You asked one question before any structure, and made three proposals. Here is what we
established, and nothing beyond it.

**"Already published": yes, and verified in the frozen PDFs rather than from our own planning
page.** Both halves are paper 1 **v1**, DOI 10.5281/zenodo.21273548, §4, printed as **Theorem
4.5** (uniform trim) and **Theorem 4.6** (sharpness: the staircase), and unchanged in **v2**,
DOI 10.5281/zenodo.21421120. The mirror paper (10.5281/zenodo.21303918) carries no part of it —
its own `thm:dich` is the 3-adic one-step predecessor window, a different theorem about a
different object, so a sentence citing the mirror paper for this would be wrong. No load-bearing
half is wiki-only. The `p ∈ {2,…,23}` contiguous evidence is v2 only, and §12.8.6's machinery is
wiki-only while everything it *claims* is in the v2 note.

**The phrase is yours.** "Counting dichotomy" has zero occurrences in the wiki, in `paper/`, in
`sources/`, or in either PDF. What it contracts are two phrases in our own **published**
abstract and Related-work paragraph — *"a sharp dichotomy for counting arguments"* and *"the
counting-limit dichotomy developed here"*, under a title ending *"…and the limits of counting
arguments for cycles"*. So the mathematics and the word are ours and the two-word contraction is
yours, and it is a faithful one. Worth telling you plainly, since you are proposing to put it in
a referee's mouth.

**Two places where the fit is looser than the sentence implies, and they are the two a referee
would find.**

- *"Counting closes every period"* overstates what we published. What Theorem 4.5 and Corollary
  12.8.2 give is **effective finiteness** at every period — the candidate set is finite and
  explicitly bounded — which is not the period being closed. Closing one means running the
  finite computation, and our own stopping rules forbid running it past `p = 3`. Our published
  wording is careful about exactly this and says "giving effective finiteness at every period",
  never "closes".
- *"Provably cannot close them uniformly"* is **exactly half proved**, and our own paper marks
  the seam. The no-extension statement is a theorem by exhibited witness: no trim uniform in `p`
  can extend the small-period constants, with the `p = 7` staircase (`n = 94`, `γ = 6.74`) as
  the witness. The all-`p` claim carries our own published hedge, *"we assess (supported by the
  verified instances, though not proved here for all `p`)"* — present verbatim in v1 and
  **unchanged in v2**, and not upgradable; better evidence, not a closure, is what v2 added. The
  word "provably" attaches to the first sentence and not to the second.

**"Three independent directions" — information, not a veto.** The three faces are your
architecture: the shared repository's name, and `NOTE.md`'s §2 size / §3 digits / §4 seam. Our
own record does not carry a "three directions" object at all; where it counts the faces of the
difficulty it counts **two** — "cleanly in two, and only two, places", in README, in
`stage4.md` 11.8.7.7, and in the published sentence after Prop. 3.9. "Three" survives this
round's finding, because the drift was never one of the three: the finding removes a candidate
*fourth*, it does not disturb the count. What our record does not establish is *independent*,
and its characteristic move runs the other way — `cycles.md` 12.8.4 says the cycle half and the
divergence half "are the same problem", and `aeh.md` 13.6.7 says the two equidistributions are
"two faces of one missing genre of theorem". Being the same wall is what makes something a face
and what makes it not independent. That is a fact about our files, offered so the word can be
chosen with it in view.

Related, and the same kind of fact: our record has no single object called "the obstruction".
It has four statements at four grades — the consumption identity is **proved** (11.8.7.7,
published Prop. 3.9); the conclusion drawn from it is, in our own published words, *"the
organizing heuristic, not a formalized theorem"*; the two-way split is *"the paper's organizing
negative observation"*; and the only **theorem**-grade statement of what the obstruction *is*
is Theorem 4.6's closing sentence, that uniform exclusion requires the divisibility system /
anchor-walk rigidity. `cycles.md` 12.6.1.3 explicitly disclaims being a lever, and the `×2×3`
gap is not ours at all — it is the shared naming of 2026-07-24, recorded at `aeh.md` 13.6.7.

**`NOTE.md` as it currently stands** (shared HEAD `c966875`, unmoved — our own round-10 push,
so nothing of yours has landed there since round 10 and your proposals are proposals): the word
"dichotomy" does not occur in it; there is no abstract for a position paragraph to sit in, the
opening being §0, the Gersonides porch; and the mapping-and-instruments register is already
partly present at §7, "Method (the actual novelty for many readers)", and in the shared
README's own "technical-comparison note". Structurally the file is still the 19 July skeleton —
`git diff f496abe..HEAD` is 2 insertions and 2 deletions, one line of §4 and one of §6, both
rewritten by you on 2026-07-24 absorbing our two pins; everything else, including the header,
is byte-identical.

**Face I's missing ledger entry**, raised only because your own header rule requires it.
`NOTE.md` opens "Every numbered claim enters via LEDGER.md first (all entries below have their
keys turned)". Faces II and III are clean on that rule — L-A1 and L-A2 at two keys with a
kernel key on top, L3 and L-A4 at two keys with the ContentDescent kernel key on the structured
half. Face I's Merle half, the δ8 impossibility, **has no ledger entry at all**: `LEDGER.md` at
`c966875` has zero occurrences of "Product", "δ8" or "scissors", though the claim is in the
shared README and in `NOTE.md` §2 and §6. And the entry §2 does cite, L1, carries the status
word `corrected`, not `two keys` — it is a strong entry and it refuted a claim on each side,
but a reader checking the header rule against it will find a different word. **This is yours to
seed and we have not touched it**; the co-edit deliberately creates no entry for a claim of
yours. One adjacent fact in the same neighbourhood: **L-A5 through L-A8 are cited nowhere in
`NOTE.md`**, including L-A8/T1 — which is the very thing any machine-checked-fragment clause
would rest on.

**`ccchallenge.org`: all four of your numbers are the site's current numbers**, checked
2026-07-28 — 371 entries, 1 formalised, 4 being formalised, 5 "Ready to be audited" — so there
is no drift to record. (The `371`/`363` pair is database size against formalisation goal:
`353 + 4 + 5 + 0 + 1 = 363`.) Steiner (three entries), Simons–de Weger and Hercher are all
listed, all ☆ Wishlist, all **Formalisations (0)**. And the fact your correction turns on is
confirmed: `Eliahou1993`, *"New Lower Bounds on Nontrivial Cycle Lengths"*, carries one `lean4`
formalisation at **"Ready to be audited"**, disclosed AI-assisted (aristotle). **The register
supports your self-correction twice over**, in fact: the single *accepted* formalisation in the
whole register, `BohmSontacchi1978`, is itself a cycle-existence paper — *"On the existence of
cycles of given length…"* — and it is not merely awaiting audit but audited and accepted; and
`Knight2026`, *"Collatz high cycles do not exist"*, is currently being formalised. So on that
register machine-checked work on the cycle literature is not first, not sole, and not confined
to the awaiting-audit bucket.

**Hercher.** `m ≥ 92` is confirmed — Theorem 23, and the abstract's own symbol, with `m`
defined there as **the number of local minima**. Flat note on the pairing rather than a
correction: `m` and `K` measure different things — `K` counts odd members — and only `K` is on
the same axis as the note's own exclusions. Your "strictly weaker verification hypothesis"
clause is right in direction, agrees with our own la8 adjudication, and is now established for
**both** your numbers rather than only Corollary 29. In units of `2^60`: Theorem 23 needs
**704** (his Definition 4, citing Barina), Corollary 29 needs **1536** `= 3·2⁶⁹`, and the note's
own exclusion instantiates **2048** `= 2⁷¹`. `704 < 1536 < 2048`, so the asymmetry runs in
Hercher's favour on hypothesis and on conclusion alike (`q₂₃/35 031 771 147 = 3.9258`). He is
formalised nowhere we can see — ccchallenge 0, no counterpart in any of your repositories,
nothing of ours.

One item there is ours to fix and it is mentioned once: `Macindoe2026` is catalogued on the
register from the **v1** DOI, `10.5281/zenodo.21273548`, while our own hosting decision pins v2,
`10.5281/zenodo.21421120`. Anyone following the register's link lands on v1.

> **[PLACEHOLDER — THE AUTHOR'S: the joint note's contribution sentence, and the answer to the
> three proposals. Nothing is drafted here, and no wording for that sentence is proposed
> anywhere in this reply.]**

## Where everything lives

Wiki `main` stands at **`9fdaa0f`** — **CHECK AT SEND TIME**; it must be public before or with
the shared-repo push or none of the co-edit's artifact pins resolve.

The five round-11 records are `briefs/merle-r11-ceiling-audit-findings.md` (the ceiling repair,
the `hceil` removal, the axiom logs and the RETRACTED block),
`briefs/junction-public-recon-findings.md` (the completed recon, the `LegendreApprox` diff, flag
6 at first hand, and the prior-art comparison), `briefs/merle-r11-hygiene-check-findings.md`
(the hygiene pass and the four negatives), and the two joint-note premise pre-checks,
`briefs/jointnote-premise-ours-findings.md` and
`briefs/jointnote-premise-external-findings.md`. The last two carry no verification script,
because nothing in them needed computing and inventing one would have verified nothing; they say
so in their own text.

The fresh verification code is `experiments/merle_r11_ceiling_audit.py` (**190 checks, 0
failures**), `experiments/junction_public_recon_deficit_check.py` (**465 checks, 0 failures**)
and `experiments/merle_r11_hygiene_check.py` (**115 checks, 0 failures**), each with its output
committed alongside. Each imports nothing from your repositories and nothing from the earlier
`merle_*` checks in ours.

The round-11 co-edit — the L-A8 kernel key turned and scoped in the ContentDescent language, the
"K pinned" wording written as you proposed it, the one-sidedness sharpening, the round's hygiene
offers, and our own L-A3 (B) date-stamp — is at
`[PENDING: shared-repo push — SHA to be filled at send time]`, over `c966875`, `LEDGER.md` only,
your prose untouched throughout.

No new claims ride along with any of this. Everything cited above sits at its named place in the
five findings records, and the two bracketed fields are the only values not yet on file.

---

> **[PLACEHOLDER — personal closing: the author's own.]**
