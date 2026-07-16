# Brief: the signed diagonal — 14.15.3–14.15.5 over the nonzero odd integers (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules**), `AGENTS.md` (binding house norms), `reverse.md` §14.14.3–14.14.4, §14.15 entire — especially 14.15.3 (the two-sided coding), 14.15.4 (unique predecessor, realization height, equivalence), 14.15.5 (admissibility-class lemma, the converse, the `−5` reconciliation) — and `briefs/diagonal-converse-findings.md` (the off-brief finding this brief executes, authorized by the author 2026-07-16), bridge.md §16 (charter: pointers only), cycles.md §12.1 (for the periodic reconciliation), spine.md §9.8 (the positive-domain convention).

## Provenance and pre-check

This brief executes the scope decision recorded in `briefs/diagonal-converse-findings.md`: the 14.15.3–14.15.5 apparatus is plausibly sign-independent, with positivity entering only as a hypothesis location (14.15.4.1's "quotient of two positive numbers"), not as structure. Author authorized 2026-07-16. Pre-checked with fresh throwaway code (main session, 2026-07-16; script deliberately not provided):

- **Sign sectors are dynamically disconnected.** The letter-prescribed predecessor of a nonzero odd `z` (formula of `14.15.4.1`, applied verbatim) exists iff `3^m | 2^r z + 1`, is unique, lands on stratum exactly `(m,r)`, has the **same sign as `z`**, and is **never `−1`** (`2^r z + 1 = 0` has no odd integer solution): `2,975` existing predecessors over `30,000` signed draws, `0` failures. Forward: `G` maps negative odd integers (≠ `−1`) to negative odd integers coprime to `3`: `10,000` checks, `0` failures.
- **`−1` is the unique singular point, and it is one-sided.** `stratum`/`G` are undefined at `y = −1` (`v₂(0) = ∞`); `−1` is unreachable backward (above) but reachable forward — `G(−3) = −1` exactly — so the negative sector has genuine **forward mortality** that the positive sector provably lacks (`14.14.3.2`(3) totality). A door following an infinite word forward never hits `−1` (its stratum is defined at every step), so the diagonal criterion excludes `−1` automatically: every `y₂(W)` has `v₂(y₂+1) = m₀ < ∞`.
- **The admissibility-class lemma is sign-blind.** Among *negative* odd `z`, the depth-`n` admissible set is exactly one residue class mod `3^{M_n}`, equal to `B_n mod 3^{M_n}`: `200` words, `0` class failures, `0` `B_n` mismatches. (The congruence `z ≡ B_n` is sign-blind; one class among **all** nonzero odd integers, each sign infinitely represented.)
- **The negative sector realizes every finite word tried.** Random length-3 words all have live *negative* followers (`60/60`) — the cylinder class mod `2^{S+1}` contains infinitely many live members of each sign.
- **The classical negative cycles land exactly.** `((2,1))^∞ ↔ y* = −5` (already in `14.15.5`(c)); and the period-`7` accelerated cycle `{−17,−25,−37,−55,−41,−61,−91}` is the **`G`-period-2** word `((4,1),(3,3))`: `stratum(−17) = (4,1)`, `G(−17) = −41`, `stratum(−41) = (3,3)`, `G(−41) = −17`, composed fixed point `y* = −17` exactly, block lengths `4 + 3 = 7` matching `14.14.7.1`'s return times.

Your job is to prove the signed statements at house standard, with fresh verification code.

## The framing mandate

This layer **relocates a hypothesis, it does not move the Bridge.** The signed characterization — a bi-infinite word is integrally realized by a nonzero odd integer iff `y₂(W) = y₃(W)` at such an integer — absorbs `14.15.5`(c)'s boundary exception (the classical negative cycles) into the theorem as ordinary periodic points, and shows the positive-domain restriction of the classical conjecture sits in the coding as a **sector choice**, not a structural asymmetry (the one genuine asymmetry is `−1`'s forward mortality, negative sector only). Deciding which words lie on the signed diagonal is exactly as hard as before — the positive sector's non-trivial periodic points are cycle exclusion, its typical words are equidistribution, both parked. Any prose implying the sign extension gives leverage on either is a register violation.

## Queue, in order

1. **The signed domain, the singular point, and sign preservation.** New subsection **14.15.6** (14.15.1–14.15.5 merged and closed; never renumber existing anchors). Define the signed door space (nonzero odd integers, `y ≠ −1`; *live* still means `3 ∤ y`). Prove, citing the sign-independent arguments rather than re-deriving: (i) `stratum`/`G` are defined on all of it, with `G`'s image live of the same sign — except `G` may output `−1` (forward mortality, negative sector only; instance `G(−3) = −1`, recorded as the one genuine sector asymmetry against `14.14.3.2`(3)); (ii) the signed unique-predecessor lemma — `14.15.4.1`'s statement with "positive" replaced by "same sign as `z`, never `−1`", the only changed step being the sign of `q = (2^r z + 1)/3^m`.

2. **The signed admissibility-class lemma and the two-sector bicylinder.** Same subsection. (i) `14.15.5.1` with "among positive odd integers" relaxed to "among nonzero odd integers": one class mod `3^{M_n}`, namely `B_n` — the proof is unchanged (note where its one positivity citation dissolves, per item 1(ii)). (ii) The bicylinder corollary holds **per sector**: every finite two-sided window is realized by a live integer segment of *each* sign (the class mod `2^{S+1}` meets each sign in infinitely many live members; the negative chain's construction otherwise identical to `14.15.4.2`).

3. **The signed characterization.** Same subsection. Define signed integral realization (as `14.15.3.5`, doors from the signed space; note liveness and `−1`-avoidance are automatic exactly as in `14.15.5.3`'s proof). Prove: `W` is integrally realized by a nonzero odd integer `y₀` ⟺ `y₂(W) = y₃(W) = y₀ ∈` the nonzero odd integers (`−1` impossible automatically — state why in one sentence). The positive case is `14.15.3.6` + `14.15.5.3`, cited not re-proved; the negative case runs the identical argument through items 1–2. For the height: treat sectors separately — the negative-sector height `H⁻_{p,q}(W) := min |y₀|` over negative members of the signed `R`-set — and state the per-sector equivalence (bounded ⟺ realized in that sector), with the monotone-net argument cited from `14.15.4.4`–`14.15.4.5` (it is sign-blind once `|·|` replaces the positive minimum; if any step genuinely fails to transfer, record it precisely instead of forcing it).

4. **Reconciliations, flat.** (i) `14.15.5`(c)'s `−5` instance upgrades from boundary exception to ordinary point: the word `((2,1))^∞` **is** integrally realized in the signed sense, by `−5` — one sentence, cross-referencing, not editing, `14.15.5`(c). (ii) The period-7 cycle as the `G`-period-2 word `((4,1),(3,3))`, `y* = −17`, verified exactly (pre-check above; your own fresh code). (iii) The `{−1}` classical cycle is **genuinely outside the coding** — its would-be door is the singular point itself — recorded as the honest boundary of the signed picture, not smoothed over. (iv) The known-cycle census, one flat sentence: the known `G`-periodic integer diagonal points are exactly `y=1` (word `((1,1))`), `y=−5` (word `((2,1))`), and `{−17,−41}` (word `((4,1),(3,3))`); whether the positive sector has any beyond `y=1` is precisely cycle exclusion (cycles.md §12, parked) — not a new lever, and the classical fact that these are the only known `3x+1` cycles is cited to the standard survey literature (pin a citation in publication.md's register style, or record its absence honestly).

5. **Accounting and closing status.** The Bridge (bridge.md §16) is unchanged; the sign boundary in `14.15.3`–`14.15.5` was a hypothesis location, now placed where it belongs (the sector choice, plus `−1`'s one-sided mortality); nothing about deciding diagonal membership changed in either sector. Extend the mandatory accounting sentence accordingly.

## Success / stop criteria

- **Floor:** items 1–2.
- **Primary (expected, given the pre-check):** items 3–5.
- **Stop:** after item 5, stop. Explicitly forbidden, whatever the results suggest: any search for further negative (or positive) cycles or enumeration beyond the three known instances named above; any attempt to decide `y₂ = y₃` for word families beyond those named periodic instances; any growth study of any height variant; any cycle-exclusion attempt; any equidistribution proof attempt; any extension of the domain further (e.g. `2`-adic or rational doors) beyond one recorded observation if one arises. Off-brief findings go to `briefs/signed-diagonal-findings.md`; log them and stop anyway.

## Placement and numbering

- `reverse.md`: new subsection **14.15.6** holding items 1–5. Never renumber or edit existing anchors; `14.15.5`(c) stays as written (item 4(i) cross-references it).
- `bridge.md` §16.4.5: one clause extension **iff** item 3 lands; update the `updated:` field.
- Cross-page status sweep per AGENTS.md when done: index.md (reverse.md row + status paragraph), HANDOFF.md one-liner (mark it pending main-session review, honestly), publication.md one sentence at most (the negative cycles are classical facts — Lagarias's surveys list them; the signed reading is bookkeeping, claim nothing).

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code, not the pre-check's constructions; record what was checked, the range, seeds, and the date, inline in the owning section.
- Verification code goes in `experiments/signed_diagonal.py`, imports nothing from `diagonal_converse.py`, `realization_height.py`, `itinerary_coding.py`, `block_map.py`, or `door_seam.py`, states which results it supports, stays runnable. Exact integer/`Fraction` arithmetic wherever a pass/fail decision is made.
- Failures and obstructions are recorded, not deleted. If the per-sector height transfer (item 3) hits a real snag, that is a finding, not a defect to hide.
- Register norm: flat, calibrated prose. This layer completes a reconciliation and relocates a hypothesis; the Bridge is unmoved; the known-cycle census is classical fact under new coordinates, not a discovery.
- Work on branch **`signed-diagonal`**, commit per item with verification in the same commit, and **do not merge to main** — the main session reviews and re-runs all verification code before merging.
- No scope expansion.

## Definition of done

Items 1–3 as proved, verified statements in a new reverse.md §14.15.6 (with the one-sided mortality asymmetry and the `−1` boundary recorded precisely); item 4's four reconciliations flat and exact; item 5's closing status stating plainly what changed (the negative cycles are ordinary periodic diagonal points; the sign restriction is a sector choice; `{−1}` alone stays outside) and what did not (the Bridge, both sectors); clean per-item commits on `signed-diagonal` with `experiments/signed_diagonal.py` committed and passing.
