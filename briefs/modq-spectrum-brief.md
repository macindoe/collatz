# Brief: the mod-`q` spectrum of the rotation numerator — the joint law behind the parked condition — for a delegated session

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — the cycle front is PARKED; this brief does not reopen it and runs no search), `AGENTS.md` (house norms: fresh verification code, no change logs, every fact in one page), `HANDOFF.md` — the "Register norm" paragraph at the top and the "Known infrastructure quirks" section only, `cycles.md` 12.6.1 (the numerator `R_r` and `q`), 12.6.1.1 (transport recurrence; the `p` conditions are one condition), 12.6.1.5 (the margin heuristic — `2^(−margin)` as the expected count of divisible profiles), 12.6.1.6 (the prime-`7` mechanism: the `(2^s − 1)` orbit collapse; "bias decays with block count"), 12.6.1.7 (the numerator is Tao's offset; "modulo `q` the parked condition asks the same object not to concentrate at `0`"; the mod-`3^j` Fourier table there is the model for what this brief measures mod `q`), `briefs/prime-local-probe-brief.md` and `briefs/prime-local-probe-findings.md` (the local marginals `R_0 mod ℓ` are flat at every prime tested; the **ghost-hunt discipline** — every apparent signal was dissolved to an elementary pushforward cause; read both in full, this brief is their global sequel), `briefs/merle-la6-check-findings.md` §2(a) (the exact census of divisible words at `n ≤ 14`, both shores — a canary below). Read `experiments/prime_local_probe.py` for its conventions only (profile family, shores, seeding); import nothing from it.

## Provenance and purpose

The parked condition `q | R_0` has been probed from four directions and each came back flat or elementary-caused: the graded content `C(P)` (L-A5), the local marginals `R_0 mod ℓ` for each prime `ℓ | q` (prime-local probe), the prime-`7` bias (12.6.1.6), the divisible-word census against the lottery (L-A6). What no probe has measured is the **joint** law: two primes dividing `q` can each be uniform while the pair is correlated, and the condition needs every prime power of `q` to hit `0` together. The direct instrument is the characteristic function of `R_0` over the profile family at a fixed cell, the discrete Fourier transform of the residue distribution on `Z/q`:

```text
φ(ξ) = (1/N) · Σ_(profiles) exp(2πi · ξ · R_0 / |q|),     ξ ∈ Z/|q|.
```

Frequencies `ξ` that are multiples of `|q|/ℓ^a` (for a prime power `ℓ^a ‖ q`) are the characters of the marginal mod `ℓ^a` — they must reproduce the prime-local probe. Every other `ξ` is a cross-prime character, and that is the new information. Under the no-conspiracy heuristic of 12.6.1.5 every nonzero `|φ(ξ)|` sits at the sampling floor. A peak off the local frequencies and off the explained `5` and `7` lines is structure; flatness everywhere is a second verdict completing the local one. Either outcome is a calibration of the named open wall (12.6.1.6's "generic equidistribution of `R_0 mod q` along the family"), recorded as such, with no status change.

**Stopping-rule compliance:** no per-period cycle search is run, no exclusion is attempted, no proof effort on the equidistribution question. The pipeline histograms `R_0 mod |q|` over a whole profile family; the zero bin is the L-A6 census (used as a canary, not as a search). The `−17` cell is an instrument calibration on a known cycle. The front stays parked whatever comes out; the verdict is a calibration sentence at most.

## Definitions, fixed

- **Cell** `(n, K)`, `q = 2^K − 3^n`, `S = K − n`. Positive shore `K = ⌈n·log₂3⌉` (`q > 0`), negative shore `K = ⌊n·log₂3⌋` (`q < 0`); the modulus is `|q|` on both. `gcd(q, 6) = 1` always.
- **Profile family at a cell:** all ordered tuples `(m_t, s_t)_(t<p)` with entries `≥ 1`, `Σ m_t = n`, `Σ s_t = S`, over every `p` from `1` to `min(n, S)` (`p = 1` included). Count `Σ_p C(n−1,p−1)·C(S−1,p−1) = C(K−2, n−1)` (12.6.1.5). Rotations are distinct members (each ordered tuple once); say so in the findings, and note that a profile's `p` rotations carry residues related by units (12.6.1.1), so the pooled population mixes them.
- **Residue:** `R_0` per 12.6.1 (`M_t = Σ_(j>t) m_j`, `S_t = Σ_(j<t) σ_j`, `σ_j = s_j + m_(j+1)` cyclic — the shift is essential), reduced mod `|q|`. Exact integers throughout; floats only inside the spectra.
- **Cells to run** (pre-computed by the main session, from-scratch Pollard rho; `sympy` is not installed, `numpy 2.2.6` and `mpmath` are):

| n | shore | K | q | factorization | profiles |
|---|---|---|---|---|---|
| 5 | + | 8 | 13 | 13 | 15 |
| 5 | − | 7 | −115 | 5·23 | 5 |
| 7 | + | 12 | 1909 | 23·83 | 210 |
| 7 | − | 11 | −139 | 139 | 84 |
| 12 | + | 20 | 517135 | 5·59·1753 | 31,824 |
| 12 | − | 19 | −7153 | 23·311 | 12,376 |
| 17 | + | 27 | 5077565 | 5·71·14303 | 2,042,975 |
| 17 | − | 26 | −62031299 | 11·23·245183 | 735,471 |
| 22 | + | 35 | 2978678759 | 7·425525537 | 3.5·10^8 |
| 22 | − | 34 | −14201190425 | 5²·19·97·308219 | 1.3·10^8 |
| 29 | + | 46 | 1738366812781 | 39409·44110909 | 4.2·10^11 |
| 29 | − | 45 | −33446005276051 | 23·47·307·3191·31583 | 1.5·10^11 |
| 41 | + | 65 | 420491770248316829 | 19·29·17021·44835377399 | 9.4·10^16 |
| 41 | − | 64 | −18026252303461234787 | 23²·239·7237·19701228121 | 3.4·10^16 |

  Re-derive every entry with your own code before use (a factorization that does not reproduce is a finding, not a typo to fix). Cells with `≤ 2.1·10^6` profiles are **exact** (full enumeration); the rest are **sampled**: `N = 10^6` profiles drawn uniformly from the family (choose `p` with weight `C(n−1,p−1)·C(S−1,p−1)`, then a uniform composition of `n` and of `S` into `p` parts — prove the sampler uniform on an exact cell by comparing its histogram to the enumeration). Seed fixed and stated.

## Queue

1. **Instrument, then canaries — before any exploratory number.** Build the residue histogram `h(x) = #{profiles : R_0 ≡ x}` per cell. Canaries, printed first: (i) the `−17` cell `(7, −)`: the block profile `((4,1),(3,3))` has `R_0 = 139`, its rotation `((3,3),(4,1))` has `R_0 = 695 = 5·139`, both `≡ 0 (mod 139)` (main session, 2026-09-08); (ii) the zero bin at `(5, ±)`, `(7, ±)`, `(12, ±)` must equal the L-A6 census counts of divisible words at those cells (read them from `briefs/merle-la6-check-findings.md` §2(a); if the census is indexed differently, reconcile and state how); (iii) the uniform null: the same pipeline on `N` uniform random residues mod `|q|`; (iv) sampler calibration at `(17, +)`: `10^6` samples against the exact histogram at the selected frequencies of item 3, the discrepancy against `1/√N`.

2. **Full spectrum where feasible.** For `|q| ≤ 10^7` (`(5,±)`, `(7,±)`, `(12,±)`, `(17,+)`), compute `φ(ξ)` for **every** `ξ` by FFT of the histogram (numpy; length `|q|`). Report `|φ|` sorted: the top `20` frequencies with, for each, its **type** — local (`|q|/ℓ^a` divides `ξ`, which `ℓ^a`), monomial (`ξ ≡ ±2^a·3^b mod |q|` for small `a, b`, since `R_0` is a sum of such monomials times `(2^s − 1)`), or other — and the population floor: a uniformly random population of the same size `N` shows `E max_ξ |φ| ≈ √(ln|q| / N)`; state it next to every peak. Then the same **per period `p`** (the family split by block count): the `5`-line and `7`-line are known to shrink with `p` (12.6.1.6) — that is the instrument's canary — and anything that does not shrink with `p` is what this brief is for.

3. **Selected frequencies everywhere** (exact and sampled cells alike), six classes, `|φ(ξ)|` for each `ξ`: (a) low, `ξ = 1..2000`; (b) local, `ξ = j·|q|/ℓ^a` for each `ℓ^a ‖ q`, `j = 1..min(ℓ^a − 1, 300)`; (c) cross-prime, `ξ = j₁·|q|/ℓ₁^a + j₂·|q|/ℓ₂^b` for each pair of prime powers, `j_i = 1..min(·, 30)`; (d) monomial, `ξ ≡ 2^a·3^b (mod |q|)`, `0 ≤ a ≤ 64`, `0 ≤ b ≤ 40`; (e) random, `5,000` uniform draws from `1..|q|−1`; (f) the `⟨2,3⟩`-orbit of the top peak found in item 2 where available. For each class: the maximum `|φ|`, the `ξ` attaining it, the class's Rayleigh floor `√(ln(#ξ in class) / N)` and the unit `1/√N` (for exact cells `N` is the population size; the floor then says what a random population of that size would show). A class maximum above `3×` its floor is a **candidate** and enters the ghost-hunt of item 5 before it enters any table as a finding.

4. **The joint law directly, in the reading a non-specialist can check.** For each pair of prime powers `ℓ₁^a, ℓ₂^b ‖ q` with `ℓ₁^a·ℓ₂^b ≤ 10^6`: the joint table of `(R_0 mod ℓ₁^a, R_0 mod ℓ₂^b)`, its mutual information in bits, the null expectation `(k₁−1)(k₂−1)/(2·N·ln 2)` for independent uniform marginals, and a permutation control (shuffle one coordinate, recompute). Also the total-variation distance of the joint from the product of its marginals, against the same control. This is the cross-prime independence test stated without Fourier language; it must agree with item 3(c).

5. **Ghost-hunt discipline (mandatory for every candidate).** Before any peak is recorded as a finding, hunt its elementary cause in this order: the small-entry pushforward (a finite composition measure at small `p` or small entries concentrates residues — the prime-local probe's dissolved ghost; test by restricting to `p ≥ 3` and entries `≥ 2`), the `(2^s − 1)` orbit collapse (12.6.1.6; test whether the peak is a local character of `5` or `7`), rotation multiplicity (the `p` rotations of one tuple carry unit-related residues; test on one representative per rotation class), sampler artifacts (exact cell agreement), and float rounding in the spectrum (recompute the peak by exact rational arithmetic on the histogram with `mpmath` at high precision). A peak that survives all five is recorded with its evidence and labeled **unexplained**, not as a lever; a peak that dissolves is recorded with its cause, as the prime-local probe did.

6. **The deltas, three tables.** (a) The maximum off-local, off-monomial `|φ|` against its floor, per cell, along `n` — both shores side by side. (b) The same at fixed cell `(17, +)` and `(12, ±)` as a function of `p`. (c) The cross-prime mutual information against its null, per cell. Each table one line per row, the floor next to the value, no adjectives.

7. **Verdict, flat, one of two.** (i) *Global structurelessness at this scale:* every off-local class at its floor, the joint law at null, the `5`/`7` lines reproducing 12.6.1.6 and shrinking with `p` — the joint law is as flat as the marginals. (ii) *A surviving candidate:* stated precisely (cell, class, `ξ`, `|φ|`, floor, the five hunts and their outcomes), with its elementary cause if found. In either case the front stays parked.

8. **Wiki output, minimal.** Only if the verdict is clean either way: **one** calibration sentence, in its own commit, appended to cycles.md 12.6.1.7's "One object, two moduli" paragraph (after "`12.6.1.5`'s margin heuristic is the equidistribution-mod-`q` assumption written out"), stating what was measured (the joint law over the family at the listed cells, the classes, the floor), the verdict, the script and the date — one sentence, register of 12.6.1.6's *Calibration* line. Nothing else on any page; no `HANDOFF.md`, no `open-problems.md`, no `symbols.md`. If the verdict is (ii) with an unexplained survivor, write no wiki sentence — the findings carry it and the main session decides.

## Record

- `experiments/modq_spectrum.py` — fresh code (imports nothing from any existing script; Miller–Rabin, Pollard rho and the numerator reimplemented; numpy for histograms and FFT only), canaries printed first, seed fixed, runtime capped at `45` minutes for the committed run (state the time; if a cell would exceed the cap, reduce `N` for that cell and say so). Committed output `experiments/modq_spectrum_output.txt` — compact: canaries, per-cell class maxima with floors, the top-20 tables for the exact cells, the joint-law table, the three delta tables, totals.
- `briefs/modq-spectrum-findings.md` — the definitions as used, the cell table re-derived, the canaries, the tables (representative rows plus totals; full data in the output file), every candidate's ghost-hunt with outcome, the verdict in the form of item 7, the runtime, `RESULT: CLEAN` from the encoding scan, and a "left open" section that says flatly what was not covered (cells not run, classes not tested).
- The optional cycles.md sentence of item 8, in its own commit.

## Rules

- Branch **`modq-spectrum`** from your worktree HEAD. FIRST verify the worktree contains this brief (`briefs/modq-spectrum-brief.md`); worktrees are sometimes cut from a stale HEAD — if it is missing, `git merge main` before starting, and state your base SHA in the findings.
- No web access, no contact with anyone, no pushes, no edits outside this repository, no reading of any Merle repository (nothing here needs one).
- File edits via the Edit/Write tools only — never PowerShell `Get-Content`/`Set-Content` (see HANDOFF quirks; the repo's `—`/`≤`/`₃` are destroyed silently). Run `experiments/encoding_scan.py` before the final commit and record `RESULT: CLEAN`.
- Register: flat, calibrated prose. No excitement. "Excludes nothing" is true of every line here; say it once in the findings and do not hedge it further. A signal is a candidate until the ghost-hunt is done; a dissolved ghost is recorded with its cause, not deleted.
- Run scripts in the foreground and wait for them (timeouts up to `600000` ms per call; split the run into per-cell invocations if one call would exceed that, and commit the pieces). Do not stop until the commits exist.
- Do NOT merge — the main session reviews (re-runs the script, reads the tables) and merges. Stop after Record.
