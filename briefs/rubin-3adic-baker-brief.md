# Brief: the 3-adic Baker cap on the mirror side (Rubin correspondence, 2026-09-05) — for a delegated session

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules**), `AGENTS.md` (house norms: nothing is labeled proved without independently written verification code; no change logs in tracked files; every fact lives in exactly one page), `HANDOFF.md` item 1 (register norm; the personal-email rule under "Known infrastructure quirks" applies to every correspondent, not only Merle), `stage1-synthesis.md` 11.8.3.11 (the 2-adic pin this brief mirrors — read it twice: its structure is the template for the new remark), `reverse.md` 14.1–14.3 (the predecessor characterization, the mirror isometry 14.2.1, the backward anchor 14.2.2–14.2.3, the backward valuation law 14.2.4, the duality table 14.3), `paper/collatz-mirror-v1.tex` (the published statement of the law; the paper stays at v1 — do not touch `paper/`), `anchors.md` 17.4 and `cycles.md` 12.6.1.3(c) (how the 2-adic pin is cited elsewhere; pointers only), `symbols.md` (registry conventions), `index.md` (resolver granularity).

## Provenance

On 2026-09-05 Brett Rubin — an independent worker, empirical rather than formal, on the problem since 2022 — wrote to the author after reading paper 1 at v3. Paraphrased (his letter is private correspondence: **do not quote it verbatim and do not write his email address into any file**; the credit line is his name and the date):

1. His `columnCenter` law, `v₂(base·3^c − 1) = 2 + v₂(c − columnCenter)` for `base ≡ 1, 3 (mod 8)`, is paper 1's Theorem 3.3 (the lifting clause) under renaming. He checked agreement mod `2^16` for every such base coprime to `3` below `300`.
2. With the primes swapped: for odd `e` with `3 ∤ e` there is a unique 3-adic `D` with `e·2^((e mod 3) + 2D) = −1`, and `v₃(e·2^((e mod 3) + 2k) + 1) = v₃(k − D) + 1` for every `k ≥ 0`. At `e = 1` it degenerates to `D = −1/2` and lifting-the-exponent. He believed this was not in the record.
3. For fixed `e`, a small `k` can carry a deep valuation whenever `D` opens with a run of zero digits (`e = 5` reaches `4` at `k = 1`; `e = 41` reaches `6` at `k = 13`), so "the analogue of Theorem 3.3's unconditional clause has to bound the constant rather than the growth". He has not done that work and does not hold the Yu / Bugeaud–Laurent references.

**Pre-checked by the main session, 2026-09-07, fresh code in the scratchpad, nothing filed:** both laws reproduce (his 3-adic law against the 14.2.4 form, `96,824` decidable `(e, k)` cases at `e < 400`, `0` failures; his forward law on the `50` lifting-class bases below `300` at the `2^16` window, `37,472` cases, `0` failures); his two valuations reproduce; `D` is `M₃` under an affine change of variable — with `s = (e mod 3) + 2k` one has `s − M₃(e) = 2(k − D)`, so `v₃(k − D) = v₃(s − M₃(e))` and his law **is** Theorem 14.2.4; his `e = 1` degeneration is Lemma 14.2.1 / Proposition 14.2.3. Point 2 is therefore a correct independent rediscovery of the mirror paper's central law (he had not seen the mirror paper; the author's reply points him at it).

**Point 3 names a real gap.** The 2-adic side carries an unconditional cap, `s ≤ C(ω)·(log d)²` (11.8.3.11, Bugeaud–Laurent Corollaire 2, pinned 2026-07-12). The mirror side — `reverse.md` and the mirror paper alike — carries **no** cap on `d` as a function of `s`. This brief fills it, as a transplant of the existing pin, with the credit clause "flagged by Brett Rubin (correspondence 2026-09-05)".

**Stopping-rule compliance:** a structural remark about the formalism on the mirror side, mirroring a pin the record already carries. No cycle search, no proof effort on the equidistribution question, no front reopened; the reverse front is ACTIVE and this is a small addition to 14.2. The cap is asymptotic bookkeeping — it excludes nothing and changes no status.

## Queue

1. **The mathematics, written out before any computation.** Reduce the mirror law to a two-logarithm form in *principal* 3-adic units, mirroring the squaring step paper 1 uses on the 2-adic side (Lemma 3.2 there; 11.8.3.11's "`g = 1`, automatic at `p = 2`" is what squaring buys here). For `s` of the admissible parity, `v₃(2^s y + 1) ≥ 1`, hence `v₃(2^s y − 1) = 0` (the two differ by `2`), hence

   ```text
   d = v₃(2^s y + 1) = v₃(4^s·y² − 1) = v₃(α₁^(b₁) − α₂^(b₂)),   α₁ = 4, α₂ = y^(−2), b₁ = s, b₂ = 1,
   ```

   with `α₁ ≡ α₂ ≡ 1 (mod 3)` (both principal units), both rational (`D = 1` in the source's notation), and multiplicatively independent exactly when `|y| ≠ 1` (`y` odd). The excluded case `y = ±1` is exact by Lemma 14.2.1 — this is precisely Rubin's `e = 1` degeneration, `D = −1/2` — and needs no Baker input; record it as the excluded case in the statement.

2. **The constant, from the primary source.** Obtain the statement of Bugeaud–Laurent's Corollaire 2 (*Minoration effective de la distance p-adique entre puissances de nombres algébriques*, J. Number Theory 61 (1996), 311–342 — Elsevier's open archive serves it; failing that, a secondary source that restates it in full, e.g. Bugeaud's 2018 monograph *Linear forms in logarithms and applications*) and record the **general-`p` statement verbatim** in the findings (it is a published theorem; quoting it is fine). Then specialize `p = 3`, `D = 1`, `α₁ = 4`, `α₂ = y^(−2)`, `b₁ = s`, `b₂ = 1` and write the explicit inequality `d ≤ C₃(y)·(max{…})²`, naming `C₃(y)` in closed form as 11.8.3.11 names `C(ω) = 208·log 9·log ω`. Check that the specialization at `p = 2`, `α₁ = 9`, `α₂ = ω^(−1)` reproduces 11.8.3.11's displayed constant — that is your control that you have read the statement correctly; if it does not reproduce, stop and record the discrepancy (11.8.3.11 may be the one in error; do not silently "fix" either). **If the primary statement cannot be obtained, do not invent a constant:** state the bound with `C₃(y)` named as effectively computable from Corollaire 2 at `p = 3`, the exponent `2` pinned by the same argument as 11.8.3.11's, and say in the page and the findings that the numerical constant is not pinned and why.

3. **Rubin's point about the constant, stated correctly.** The cap bounds `d` by `(log s)²` times a constant that is astronomically large, so for small `s` the exact law (digit-lifting of `M₃`) is the only information, and deep `d` at small `s` happen exactly when the anchor's leading 3-adic digits vanish. Verify his two instances with fresh code and record the digits: at `e = 5`, `D ≡ 1 (mod 3)` followed by two zero digits gives `d = 4` at `k = 1`; at `e = 41`, `D ≡ 13 (mod 243)` gives `d = 6` at `k = 13`. Add a bounded texture record — `max_(s ≤ S) d(y, s)` for a handful of `y` and `S`, against the cap's value at the same `S` — the mirror of 11.8.3.11's "large but finite and slow-growing" sanity check and 12.6.1.3's texture line. The cap is nowhere near binding; say so flatly.

4. **Fresh verification code — `experiments/mirror_baker_cap.py`, committed with its output.** Imports nothing from any existing script (the main session's scratchpad check is not to be copied either); exact integer arithmetic at every pass/fail decision; canaries printed first. Contents: (a) the squaring reduction `v₃(2^s y + 1) = v₃(4^s y² − 1)` on a grid of `(y, s)` at admissible parity; (b) the law 14.2.4 with a fresh digit-lifting of `M₃` (note: the condition mod `3^(j+2)` fixes digit `j` of the exponent, since `v₃(2^(2u) − 1) = 1 + v₃(u)`); (c) Rubin's parametrization — `s = (e mod 3) + 2k`, `D = (M₃(e) − (e mod 3))/2` — and the identity `v₃(k − D) = v₃(s − M₃(e))` on the grid; (d) his two quoted valuations; (e) the `y = ±1` exact case via lifting-the-exponent; (f) the numeric cap at the specialized constant (if pinned) against the observed maxima of (3); (g) the `p = 2` control of item 2 if the constant is pinned. Record counts, ranges, date.

5. **Wiki edits — conservative; content and structure in separate commits.**
   - `reverse.md`: a new **Remark 14.2.5 (effective bound: contact with 3-adic Baker theory)** after 14.2.4's verification paragraph, mirroring 11.8.3.11 in structure and register: the two-logarithm form, the pinned source and specialization (or the honest unpinned form), the imported bound, a corollary in the 11.8.3.11.1/11.8.3.11.2 shape (unconditional cap on entry depth; effective 3-adic irrationality measure for `M₃(y)`, i.e. an integer of size `s` matches at most `O((log s)²)` leading 3-adic digits of the anchor), the excluded `y = ±1` case, the "constants are and are not good for" remark, the verification line inline (what, range, date — one line, per AGENTS.md), and the credit clause. One row added to the 14.3 duality table: `cap s ≤ C(ω)(log d)² (11.8.3.11)` | `cap d ≤ C₃(y)(log s)² (14.2.5)`. Front matter `updated`; the Current-state paragraph gains at most one clause naming 14.2.5.
   - `stage1-synthesis.md` 11.8.3.11 and `anchors.md` 17.4: one pointer sentence each to 14.2.5 as the 3-adic twin — pointers, nothing restated.
   - `symbols.md`: an entry for `C₃(y)` mirroring whatever the registry carries for `C(ω)`; check the collision index for `D` (Rubin's symbol is not the record's; do not introduce it into the registry — the findings may mention it as his name for the reparametrized anchor).
   - `index.md`: add 14.2.5 to the resolver only if the resolver lists at the granularity of 14.2.4; otherwise leave it.
   - `briefs/rubin-3adic-baker-findings.md`: the provenance (paraphrased, no verbatim letter, no address), the derivation written out, the source statement verbatim, the specialization and the `p = 2` control, the verification record, the texture table, and a short section *For the author's reply* — anything that should correct the drafted sentence "It transplants directly" (the squaring step; the `y = ±1` exclusion; the constant's status).
   - **Do not edit** `HANDOFF.md` (the main session records at merge), `publication.md`, `paper/`, `TOUR.md` (his names are not literature), or anything under `sources/`.

6. **Compliance.** Run `experiments/encoding_scan.py` before the final commit and record `RESULT: CLEAN` in the findings.

## Record

- `experiments/mirror_baker_cap.py` + committed output (canaries first; per-item commits).
- `reverse.md` 14.2.5 and the 14.3 row; the two pointer sentences; the `symbols.md` entry; the resolver line if applicable.
- `briefs/rubin-3adic-baker-findings.md` as specified.

## Rules

- Branch **`rubin-3adic-baker`** from your worktree HEAD. FIRST verify the worktree contains this brief (`briefs/rubin-3adic-baker-brief.md`); worktrees are sometimes cut from a stale HEAD — if it is missing, merge or rebase onto local `main` before starting, and state your base SHA in the findings.
- Web access only for the Bugeaud–Laurent statement (and the secondary source if needed); no contact with anyone; no pushes; no edits outside this repository.
- File edits via the Edit/Write tools only — never PowerShell `Get-Content`/`Set-Content` (see HANDOFF quirks; the repo's `—`/`≤`/`₃` are destroyed silently).
- Register: flat, calibrated prose. The cap excludes nothing; say so. Heuristics labeled heuristics; nothing labeled proved without the fresh code of item 4.
- Run scripts in the foreground and wait for them; do not stop until the commits exist.
- Do NOT merge — the main session reviews (re-runs the script, checks the specialization against the source) and merges. Stop after Record.
