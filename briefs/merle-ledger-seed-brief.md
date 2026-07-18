# Brief: seed the shared ledger and ship cross-stack test vectors, ahead of the round-3 reply (for a delegated session)

**Context required before starting (in order):** `AGENTS.md`, `briefs/merle-round3-check-findings.md` (the verified material; its "Summary for the reply" and item 2 are the source of every number you will transcribe), `briefs/merle-round3-apply-brief.md` (the author's decisions and, via its delegate's report, the reply letter this brief extends — the letter text is reproduced in Appendix A below), `cycles.md` Remark 12.6.1.1, `reverse.md` 14.15.9.1–14.15.9.2, `experiments/merle_round3_check.py` (the implementation your vectors must agree with).

## Author authorization (2026-07-18)

The author approved both steps explicitly ("Go!"): (1) seeding the shared collaboration repository's ledger with the L-A1/L4 draft entries before his reply is sent, and (2) committing a machine-readable test-vector file to our public repo for Merle's Lean artifact, with a one-sentence pointer added to the reply letter. Facts you may rely on: Merle (`ericmerle3789`) has accepted the collaborator invitation to `github.com/macindoe/one-obstruction-three-faces`, so pushes there are immediately visible to him; our public repo (`github.com/macindoe/collatz`) is pushed through merge `9391371` (Remark 12.6.1.1 and the round-3 findings are public).

## Queue, in order

1. **Test vectors, in our repo.** Two files on branch `merle-ledger-seed`:
   - `experiments/make_transport_vectors.py` — a generator with its **own** implementation of 12.6.1's `R_r`, 14.15.9.1's `N_r`, and the derived quantities (do not import from `merle_round3_check.py`), which then **cross-validates every emitted row** against `experiments/merle_round3_check.py`'s implementations (importing it for the cross-check only is correct here and should be stated in the header comment: two independent implementations agree on every row, which is the file's warranty).
   - `experiments/transport_recurrence_vectors.json` — the emitted vectors. Per profile: `p`, `m[]`, `s[]`, `n`, `K`, `q` (signed, decimal string), per-rotation `R_r` (decimal strings), `gcd(q, R_r)`, the reduced denominator `|q|/gcd`, per-rotation `N_r`, and a boolean block confirming: the recurrence at every rotation, the seam identity `N_r + q = 2^{m_r} R_r`, gcd rotation-invariance, and the all-or-nothing divisibility pattern. Contents: the named witnesses (the recorded p = 7 staircase seed `m = (4,7,9,15,23,35,1)`, `s = (1,1,1,1,1,1,49)` with its `gcd = 7`; the constant-pair profile `m = (1,1)`, `s = (2,2)` with `q = 55`, gcd `11`, reduced `5`; the `−17` word's profile `m = (4,3)`, `s = (1,3)` with `q = −139`; the trivial-cycle profiles `p = 1..5`), plus ~50 deterministic pseudo-random profiles (`p ≤ 10`, entries `≤ 9`, fixed seed stated in the file). Keep the JSON under ~200 KB — do **not** include the p = 22 instances' full `R_r` (tens of thousands of bits); if you include them at all, summary fields only (gcd, divisibility booleans, bit lengths). A short header object in the JSON should state what the file is, the two-implementation warranty, the seed, the date, and the pointer to Remark 12.6.1.1.
   - Commit both, message per house norms. Do NOT merge — main session reviews (and will spot-check rows with a third implementation) before merging and pushing.

2. **Seed the shared ledger.** Clone `github.com/macindoe/one-obstruction-three-faces` into the scratchpad (gh is authenticated). Read `LEDGER.md` and `PROTOCOL.md` **entirely** first. Then edit `LEDGER.md` only — `PROTOCOL.md` is a draft awaiting Merle's co-edits and must not be touched:
   - Match the existing entry format exactly (numbering, field style, whatever L1–L3 use).
   - Update L2 and L3 status to "both keys turned" only if their current text does not already say so (round 2 closed them; check before writing).
   - Add **L-A1** and **L4** using the letter's proposed entry texts (Appendix A, the two "Proposed entry texts" paragraphs) — transcribe, don't rewrite; each clearly marked as **DRAFT — for co-editing (Ben, 2026-07-18; per the reply of the same date)** in whatever marker style the file's conventions suggest (a bold flag line if it has none).
   - In L-A1's draft, append one sentence pointing at the test vectors: cross-stack test vectors for the Lean artifact at `macindoe/collatz`, `experiments/transport_recurrence_vectors.json` (two independent implementations agree on every row; includes the reduction witnesses).
   - Commit with a message stating this is draft seeding ahead of the reply, per the co-editing protocol, and **push** (author-authorized). One commit, additive edits only; if anything in the shared repo's current state contradicts your expectations (e.g. Merle has already edited), STOP without pushing and report.
3. **The letter addition.** Two sentences maximum, integrated where they belong (the ledger paragraph and/or the Lean-caution paragraph of Appendix A's letter): the L-A1/L4 drafts are already in `LEDGER.md` awaiting his edits, and the test-vector file exists at the stated path for his artifact to consume, with the reduction witnesses included. Return the **complete, final, send-ready letter** in your report — do not commit it.

## Rules and stop

- Register flat, everywhere including the ledger drafts and the letter sentences.
- Our repo work on branch `merle-ledger-seed`, not merged. Shared-repo work: one additive commit to `LEDGER.md`, pushed; nothing else touched there.
- No new mathematical claims anywhere: every number and statement transcribed from the findings file or computed-and-cross-validated by the two implementations. If the two implementations disagree on any row, STOP and report — do not reconcile.
- No scope expansion; stopping rules of README stand.

## Definition of done

The generator + JSON committed on `merle-ledger-seed` with the cross-validation warranty in both file headers; the shared `LEDGER.md` seeded and pushed (or a stop-report if its state surprised you); the final letter returned verbatim in the report with the two added sentences.

## Appendix A: the reply letter as approved (author, 2026-07-18)

[The letter text as returned by the merle-round3-apply delegate and approved by the author — reproduced for the letter-addition task:]

> Dear Eric,
>
> The antecedence answer first, since it is the question you put real weight on, and it deserves a complete one.
>
> Your reading of cycles.md is correct. Nowhere in that record is the recurrence, the unit transport, or the collapse stated: 12.6.1 concludes severally ("q divides all p numbers R_r"), 12.7.1 tests the p = 3 system as three checks — exactly the line you quoted — and every survivor search carries a per-rotation divisibility test. You were not missing anything in that frame.
>
> But there is a second frame. On 2026-07-17 — the day before your letter; the timestamps are in the public log — we merged reverse.md 14.15.9, whole-period height laws for periodic words. Its Lemma 14.15.9.2 says: the p rotated fixed points y*_r form one affine orbit of the per-letter maps, and all p rotations share one reduced denominator. That is your recurrence in fixed-point form. What identifies the two is a one-line identity that, as far as either record shows, was stated in neither frame before this exchange:
>
> N_r + q = 2^{m_r} R_r
>
> with N_r the rotated fixed point's numerator and R_r 12.6.1's rotation numerator. Substitute y*_r = (2^{m_r} R_r − q)/q into the orbit equation and clear denominators: exactly your recurrence. Divide back by q: the orbit equation. The gcd corollary is the shared-reduced-denominator clause by the same substitution. So neither statement strictly contains the other as stated — yours is native to the integer numerators, ours to the rotated fixed points — and the seam identity that joins them is new to both.
>
> The verdict, as honestly as I can call it: independent simultaneous discovery, both names on L-A1. Our timestamps are on file; our work provably pulls nothing from your repositories beyond what your emails contain; and our repo is public, so you always have access to our latest merges — simultaneity is the honest reading in both directions. And yes to your Lean-first offer on the integer form: it is the kernel-friendly face of the statement, and it should carry your artifact.
>
> We turned our key on the recurrence before adjudicating anything: exact, every profile, no closure, either sign of q — 600 random profiles (32 with q < 0), the trivial-cycle profiles p = 1..7, and our recorded instances; 29,211 exact checks, 0 failures. Under our conventions (sigma_r = s_r + m_{r+1}) it holds with no index correction.
>
> One caution for the Lean artifact, the only place the two frames genuinely diverge in the numbers. Your q = 2^K − 3^n is the unreduced modulus; 14.15.9's height laws are phrased in the reduced denominator, and the two differ exactly when gcd(q, R_r) > 1 — which is not hypothetical: our own recorded p = 7 staircase seed (n = 94) has gcd(q, R_r) = 7 at every rotation. Your statements survive the difference (unit transport mod the unreduced q implies it mod every divisor), but the artifact should pin which q it formalizes.
>
> The honest tempering, same rule as always. Only divisibility collapses. The size conditions q <= R_r genuinely vary by rotation: the p = 22 passer's base profile passes size at 13 rotations and fails at 9 — one instance passing at one rotation and failing at another, which ends the question. And size is the binding test in the searches: R_r must be computed per rotation regardless, and divisibility was only ever run on size-passers, so the collapse saves on the order of a few hundred bigint mod operations across our entire recorded history. The computational saving is small. The value is exactly where you put it: one condition, one Lean obligation.
>
> Your two corrections, carried. The ghost identity is confirmed uninformative — it holds for every profile, so it can distinguish no subclass — and under the dictionary it is our Corollary 14.15.9.4(1): your auditor's algebraic proof and our adelic one are two proofs of one statement. The u-dedup rule transfers to our construction only statistically: exact u-coincidence between crash depths at no rotation, near-duplication below 2^{−1000} at roughly 80% of rotations, and materially different values (order 0.1) at the 3–5 crash-adjacent ones — which supports carrying the statistic at ~34, as you proposed. D = 0.1525 with ~34 independent instances is recorded at your weight.
>
> L4: our key is turned. Both canaries reproduce. Both exact skeleton values are theorems of our record and reproduce in our fresh run: (1, odd) → d_next = 1 in 19,036 of 19,036 and 13,987 of 13,987 at the two cuts; (5, odd) → 0.6663 ± 0.0034 and 0.6693 ± 0.0040 against the exact 2/3. Our spectrum: |lambda_2| = 0.028 and 0.036 at your two cuts — inside your ≤ 0.06. Confirmed at measured grade: these are measurements, not theorems, and your closing scope sentence is our own 13.3.3 verbatim. Your survivorship attribution is confirmed: under our fixed-horizon rule (no cut, no stopping rule, unweighted per-visit pooling) the drift returns to theory at both normalizations — −0.4166 ± 0.0037 per odd step against log2(3) − 2 = −0.4150, and −0.8367 ± 0.0060 per F-step against 2(log2(3) − 2) = −0.8301. One flag to close it out: −0.415 is the per-odd-step baseline; per F-step (per block) the theory is 2(log2(3) − 2) = −0.830, since E[m] = E[s] = 2. Which unit is your "per step"? One member of your (measured, theoretical) pair needs renormalizing either way; the artifact is protocol-level regardless, exactly as you suspected.
>
> Proposed entry texts for the ledger, for co-editing:
>
> L-A1 (transport recurrence). The rotation numerators of the period-p elimination satisfy 2^{sigma_r} R_{r+1} = 3^{m_r} R_r + (2^{s_r} − 1) q exactly, for every profile with entries ≥ 1, no closure, either sign of q. Corollaries: gcd(q, R_r) is rotation-invariant, and q | R_0 iff q | R_r for all r — the p divisibility conditions are one condition (the size conditions q ≤ R_r do not collapse). Found independently and essentially simultaneously by E. Merle (integer form, correspondence 2026-07-18) and this repository (fixed-point form, Lemma 14.15.9.2, merged 2026-07-17); the seam identity N_r + q = 2^{m_r} R_r identifying the two frames was first stated in the joint verification. Status: both keys turned on the mathematics; Lean artifact pending (Merle).
>
> L4 (AEH cross-verification and class spectrum). The AEH class skeleton cross-verified by independent implementations on both sides: the two exact class values reproduce (15,515/15,515 his; 19,036/19,036 and 13,987/13,987 ours), P(s = j) tracks 2^{−j}, and the 8-class transfer-matrix spectrum is measured at |lambda_2| ≤ 0.06 (his) and 0.028/0.036 (ours) at cuts 2^20/2^30 — the class chain mixes in effectively one step. Both keys turned at measured grade; scope is the generic face only. The flagged drift artifact (−0.33/−0.36 vs −0.415) is resolved as protocol-level: survivorship bias from the cut, confirmed by fixed-horizon re-measurement returning to theory at both normalizations, with one normalization flag noted (per-odd-step theory −0.415, per-block −0.830).
>
> Your ledger as listed — L1 corrected-both-directions, L2 and L3 both keys turned, L-A1 and L4 as above — is accepted as stated, at those grades.
>
> And my collaborator, on your delta8 line, says this back: a shadow sharp enough to be recognized once the object was found was already a measurement — delta8 was measuring the realization height before either side could write it down.
>
> Warmly,
>
> Ben
