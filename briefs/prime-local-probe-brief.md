# Brief: prime-local structure of the divisibility residue — pinning probe and gcd spectrum (for a delegated session)

**Context required before starting (in order):** `README.md` (binding stopping rules — this brief lives right at their edge; see compliance below), `AGENTS.md`, `cycles.md` 12.6.1 + Remark 12.6.1.1 + 12.8.6 (the instance record 12.8.6.4), `reverse.md` 14.15.9 section (a) entire (the ε-law, Lemma 14.15.9.2(3), is item 1's model) and section (d) (the composed unit `g_P`, `ord_q` machinery — the shelf item 1 builds on), `briefs/merle-round3-check-findings.md` (item 2's dictionary; the Compliance section's off-brief observation (i) — the p = 7 seed's `gcd = 7` — is item 2's seed), `experiments/transport_recurrence_vectors.json` (+ its generator, your data baseline), `experiments/merle_round3_check.py` and `experiments/staircase_allp.py` (conventions; instance regeneration).

## Provenance and purpose

Main-session assessment (2026-07-18), author-approved for probing: the round-3 additions reshape periodic cycle exclusion into **one rotation-invariant condition** — `q | R_0`, `q = 2^K − 3^n` unreduced — which **factors prime-locally by CRT**: `q | R_0` iff `R_0 ≡ 0 (mod ℓ^e)` for every prime power `ℓ^e ∥ q`, each factor a property of the word, each living in a cyclic unit orbit (the transport recurrence's mod-`q` rotation). Two measurement probes follow. Their purpose is to **surface or kill candidate local structure** in the residue `R_0 mod ℓ` — not to exclude anything.

**The hard constraint, kept in view throughout:** the classical negative cycles are *full-divisibility witnesses* — the `−17` word (`m = (4,3)`, `s = (1,3)`) has `q = −139` and `gcd(q, R_r) = 139` at every rotation. No finite-place condition can exclude positive cycles by itself (full-shift freeness, reverse.md 14.15.2; the three-faces sign clause). Therefore: any regularity you find must be run on **both sectors** before being described; a candidate constraint that does not discriminate sectors is not obstruction-shaped and must be recorded as such. Conversely, the ghost-identity lesson (round 3): a regularity true of *every* profile carries no information — when you find a pattern, look for its elementary algebraic cause before recording it as signal.

**Stopping-rule compliance:** these are measurements in the AEH/calibration spirit, run on algebraic profile scans (the 14.15.7 precedent: letter scans are pure algebra, not cycle searches) and on the already-recorded instance data. Explicitly NOT in scope: any divisibility-based exclusion attempt; any cycle search; any proof development beyond identifying the elementary cause of an observed regularity (one-line algebra yes, argument-building no). The cycle front stays parked; if a probe surfaces a genuine reopen candidate, that is a *finding to record*, and the reopen decision is the author's.

## Item 1: the prime-local pinning probe

**The model.** At the prime 3, the residue of every rotated fixed point is pinned by one letter: `ε_{i+1} = y*_{i+1} mod 3` depends only on `r_i`'s parity (Lemma 14.15.9.2(3)), because `v₃(α_i) = m_i ≥ 1` kills the history. At primes `ℓ ∤ 6` no valuation vanishes, so *that* mechanism is unavailable — the question is what, if anything, replaces it.

**The measurements** (fresh code, `experiments/prime_local_probe.py`, no imports from committed scripts except — permitted and stated — `merle_round3_check.py` or the vector generator for cross-validation of `R_r`/`N_r` values; exact integer arithmetic everywhere; every statistical claim labeled with its test and sample size; fixed stated seed):

1. **Exhaustive small-case scan (exact).** All profiles with `p ≤ 3`, entries `m, s ≤ 4` (and as far beyond as runtime sanely allows — state the range you achieved). For each, factor `q` (these are small), and for each prime `ℓ | q`, `ℓ ∤ 6`, record `R_0 mod ℓ` (equivalently `y* mod ℓ` — note `R_0 mod ℓ` and `N_0 mod ℓ` are interchangeable through the seam identity; pick one and say so). Questions, answered from the data: (a) does `R_0 mod ℓ` depend on the letters through any visible law (tabulate against per-letter data, letter parities, `K mod ord_ℓ(2)`, `n mod ord_ℓ(3)`)? (b) which residues are *attained* — does `R_0 mod ℓ` range over all of `Z/ℓ`, or is it confined (e.g. to a coset of the subgroup `⟨2, 3⟩ ≤ (Z/ℓ)*`, the natural candidate given the unit orbit)? (c) in particular, how often is `R_0 ≡ 0 (mod ℓ)` against the naive `1/ℓ` baseline?
2. **Fixed-`q` families.** Profiles sharing `(n, K)` share `q`. For several `(n, K)` with `q` having a usable prime factorization (include both signs of `q`), scan many profiles (exhaustive where feasible, seeded-random where not) and measure the distribution of `R_0 mod ℓ` *within* the fixed-`q` family — this isolates residue behavior from `q`-variation. Test uniformity (or uniformity-on-the-attained-set) per prime; report per-prime `z`/χ² with counts.
3. **The sector comparison (mandatory).** Every measurement above, run on both signs of `q`. Report whether any observed regularity or non-uniformity discriminates the sectors. The `−17` and `−5` words and the trivial-cycle profiles are your calibration anchors — the full-divisibility branch must show up where it is known to live, and nowhere else.

**Verdict wanted, flat:** one of — (i) a candidate pinning law at some class of primes, stated precisely with its evidence and (if found) its elementary cause; (ii) local structurelessness: `R_0 mod ℓ` equidistributes on its attained set at every prime tested, both sectors, in which case say so with the numbers — that verdict is valuable (it says the `1/q` heuristic has no local leak and the residual difficulty is genuinely global/archimedean, consistent with the parking rationale); or (iii) something between, described exactly.

## Item 2: the gcd spectrum

**The seed observation** (round-3, off-brief, undeveloped): our own recorded p = 7 staircase seed has `gcd(q, R_r) = 7` — partial divisibility, at a prime equal to the period. One instance; could be noise; nobody has looked.

**The measurements** (same script or a clearly-separated section):

1. **The instance record.** Regenerate the 12.8.6.4 staircase passers (`p ∈ {2,...,23}`, via the committed construction in `staircase_allp.py` at the recorded parameters — regeneration, not search; the two p = 22 instances' profiles are printed in `briefs/merle-pincer-check-findings.md`) and compute `gcd(q, R_0)` for each. Tabulate: the gcd's prime factorization, against `p`, the letters, `K`, `n`, sector.
2. **The `ℓ = p` hypothesis, tested explicitly.** Is "the period divides the gcd" (as at p = 7) a pattern or a coincidence? Check across the instance record and across the scans below; if a pattern, look for the elementary cause (a plausible one exists: profiles with internal rotational symmetry force structure on the `R_r` — check whether symmetry, not the period per se, is the operative variable; the constant-pair word `m=(1,1), s=(2,2)` with `gcd = 11` at `p = 2` is a first data point *against* the naive `ℓ = p` form).
3. **Baseline scans.** `gcd(q, R_0)` over the 60 vector-file profiles and a fresh seeded scan (state size); frequency of each prime `ℓ | q` appearing in the gcd, against the `1/ℓ` baseline; both sectors; the full-divisibility anchors (`−17`, `−5`, trivial) confirmed present and correctly classified.

**Verdict wanted:** the spectrum described flatly — which primes divide the gcd how often, whether anything beats its baseline, whether symmetry or period or sector predicts anything, each claim with its counts and either its elementary cause or its explicit lack of one.

## Record

`briefs/prime-local-probe-findings.md`: both probes' data tables (compact — representative rows plus totals, full data printed by the script), the two verdicts in the forms requested, the sector comparisons, any elementary causes identified, and — only if a genuine candidate law emerged — a drafted-but-NOT-applied proposal line for the owning wiki page, clearly marked as a reopen candidate for the author's decision. No wiki page touched. Off-brief observations logged and stopped.

## Rules and stop

- Branch **`prime-local-probe`**, commit per item, do NOT merge — main session reviews and re-runs before merging.
- Fresh code as specified; exact arithmetic for every pass/fail and every residue; floats only in labeled statistics columns. Seeds, ranges, dates inline.
- Register flat. A uniform histogram is a finding, not a disappointment; a pattern is a candidate, not a breakthrough.
- Runtime sanity: this is a bounded measurement session, not a campaign — if a scan looks like it will exceed ~10 minutes, cut its range and state the cut.
- **Stop** after the findings file. Explicitly forbidden: exclusion attempts, cycle searches, proof development beyond one-line causes, PractRand-scale statistics, touching the shared repository, any Lean work.

## Definition of done

Both probes measured at the stated scales with both-sector coverage; the two verdicts stated in the requested forms with their evidence; calibration anchors confirmed; the findings file complete; clean per-item commits on `prime-local-probe` with `experiments/prime_local_probe.py` running clean end-to-end.
