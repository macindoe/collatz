# Findings: L-A5 closure + kernel-key check (merle-la5-closure)

Delegated session, 2026-07-25. Brief: `briefs/merle-la5-closure-check-brief.md`
(committed at `34296e8`). Branch `merle-la5-closure`, base commit `34296e8` —
the brief commit itself was the worktree HEAD at launch, so the branch was
created directly from it; no rebase needed, base condition satisfied exactly.
Register: findings only; confirmations and flags separated; where observation
and claim differ, both are recorded, nothing is disputed in prose.
Verification code: `experiments/merle_contentdescent_check.py` (fresh code,
imports nothing from any Merle repository and nothing from prior Merle-check
scripts; conventions re-implemented from cycles.md 12.6.1 / 12.6.1.1 /
12.6.1.4 only; exact integer arithmetic at every pass/fail decision; canaries
hand-computed and printed before sweeps); committed output alongside as
`experiments/merle_contentdescent_check_output.txt`. **4,541 exact checks, 0
failures.** No pushes, no shared-repo or Lean-repo writes; both clones fresh,
unauthenticated, read-only, in the scratchpad; `ls-remote` checked before
cloning. No Lean file or Merle script was run (and no build was possible —
below). **Handbacks: none.**

## Item 1 — shared repo, read-only

Live `ls-remote` then fresh clone (2026-07-25): `refs/heads/main` =
`81431c754c634b66c057fb784c0f25d844288c71` (`81431c7`) — **exactly as the
letter and the brief expected; not moved again.** Six commits above our
`e53630f`, all authored Eric MERLE, 2026-07-24 CEST, in order: `6b9f2b1`
(17:29) → `49351e5` (17:48) → `92a6edb` → `08dc3d5` (18:21) → `fb5e8fc` →
`81431c7`. The L-A6 (`92a6edb`, `fb5e8fc`) and L-A7 (`81431c7`) seeds are
separate briefs' scope; noted here only as present, inserted as new entries
*after* the L-A5 entry.

- **`49351e5` touches `LEDGER.md` only, 2 insertions / 4 deletions — exactly
  as expected.** The 4 deletions are the old one-key status line (1) and the
  old closing gloss (3); the 2 insertions are the new two-keys status line and
  the restated gloss (item 2).
- **`6b9f2b1` touches what its message says:** `LEDGER.md` 1 line (the L-A5
  artifacts sentence gains the `905d75b` `#print axioms` link and the
  unreduced-modulus-note clause) + `NOTE.md` 1 line (the §6 rewrite, item 3).
  2 insertions / 2 deletions total.
- **`08dc3d5` touches `LEDGER.md` only, 4 insertions, 0 deletions** — the
  "Lean key on the structured half" block, inserted at the end of the L-A4
  entry (after our two offers), before the L-A5 header (item 4).
- **No drift.** The cumulative diff `e53630f..81431c7` on `LEDGER.md` (37
  insertions, 5 deletions) is exhausted by exactly: the `08dc3d5` block, the
  `49351e5` status line + gloss replacement, the `6b9f2b1` citation line, and
  the appended L-A6/L-A7 entries. Every deletion is accounted for by the
  status line, the gloss, and the citation line. Separately, our appended
  block — the Macindoe verification record, the `−17` exhibit, offers (a) and
  (b), and the Key-status paragraph — was byte-compared programmatically
  against the verbatim quote in `briefs/merle-la5-coedit-findings.md`:
  **identical, every non-empty line.** Our record has not drifted.

## Item 2 — the restatement adjudication

**The compared texts.** Offer (a)'s long form as pushed at `e53630f` (the
findings §(d) language, verbatim in `briefs/merle-la5-coedit-findings.md`) is
the reference. His `49351e5` replacement for the entry's final two sentences,
verbatim:

> So content towers have no shoulders in the exact sense the lemma proves:
> **no word is connected to a `C = 1` word by one-unit adjacent transfers**
> (adjacency separation, T1/T2), and repetition merely *approaches* `C = 1`,
> reaching it only from a cycle [L-A4]. What the lemma does not exclude — and
> what NOTE §6's residual gap now names exactly — is an **isolated** aperiodic
> peak at `C = 1`, unreachable by transfer: the `−17` cycle is precisely such
> a peak, realized on the negative shore (primitive, `q = −139`, `C = 1`,
> shared content 1 with all six neighbours, forced by the corollary
> `gcd(139, 3³ − 2³) = gcd(139, 19) = 1`). The wall, restated: no isolated
> `C = 1` peak on the positive shore. (Domain: `C` is defined for `|q| > 1`;
> on the spent-stock `|q| = 1` words it is `0/0` — offer (b), accepted.)

And the new key-status line, verbatim:

> **Two keys (Merle: Lean kernel + independent scripts; Macindoe: clean-room
> re-derivation, 2026-07-25). Closing gloss restated per Macindoe offer (a) —
> adjacency separation, not the wall; `|q| > 1` domain per offer (b).**

**Claim-identity test, clause by clause** (his own wording, per our offer; the
test is claim identity, not textual identity):

| Required by the offer/findings | His restated text | Match |
|---|---|---|
| Adjacency separation only: no word *connected to* `C = 1` by one-unit transfers | "no word is connected to a `C = 1` word by one-unit adjacent transfers (adjacency separation, T1/T2)" | **Yes** — our offered phrase, claim-identical |
| Repetition approaches `C = 1`, reaches it only from a cycle | "repetition merely *approaches* `C = 1`, reaching it only from a cycle [L-A4]" | **Yes** — the exact (b2) law; drops our "for every base" rider, which only strengthened the sterile-ness reading; no overreach |
| Must NOT claim the wall | The wall appears once, as a named restated target ("The wall, restated: …"), directly after "What the lemma does not exclude … is …"; commit message: "adjacency separation …, NOT the wall" | **Yes** — named, not claimed (one precision observation below) |
| Isolated aperiodic peak named as the open residual (NOTE §6) | "What the lemma does not exclude — and what NOTE §6's residual gap now names exactly — is an **isolated** aperiodic peak at `C = 1`" | **Yes** |
| `−17` exhibit stated correctly (primitive, `q = −139`, `C = 1` exact, totally isolated, negative shore) | "realized on the negative shore (primitive, `q = −139`, `C = 1`, shared content 1 with all six neighbours, forced by the corollary `gcd(139, 3³ − 2³) = gcd(139, 19) = 1`)" | **Yes** — all five elements; the arithmetic re-checked (`3³ − 2³ = 19`, `gcd(139, 19) = 1`, six neighbours per our findings) |
| Offer (b) domain clause (`|q| > 1`, `0/0` at spent stock) | "(Domain: `C` is defined for `|q| > 1`; on the spent-stock `|q| = 1` words it is `0/0` — offer (b), accepted.)" | **Yes** — landed verbatim in substance |
| Key-status: exactly two keys, both sides' grounds truthful | Two keys; Merle grounds = Lean kernel + independent scripts (verified our side at statement level, kernel log now committed — item 4); Macindoe grounds = clean-room re-derivation, 2026-07-25 (our pushed record's date) | **Yes** |

Every claim the restated text makes is one our checks verified; nothing new is
claimed.

**Verdict: CLEAN — the two-keys marking is honest on our record.** The gloss
now claims adjacency separation, the repetition law, and the exhibit — all
verified (`merle_la5_check.py`, ~10,372 decisions; re-confirmed on the descent
side this session) — and names the isolated-peak existence as the open
residual rather than claiming it closed.

Two observations, flat, neither a key blocker:

1. **The wall rider's elided qualifier.** Standalone, "no isolated `C = 1`
   peak on the positive shore" lacks "aperiodic/primitive": the forced powers
   of the `+1` cycle sit at `C = 1` on the positive shore and are totally
   isolated in the lemma's own sense (the trivial square `((1,1),(1,1))` has
   `q = R_0 = 7`, `C = 1`, and unit seams `3¹ − 2¹ = 2¹ − 1 = 1`, so shared
   content 1 with every neighbour — canary C2 of this session's script). Read
   in place the sentence is anaphoric — "such a peak" two lines up is the
   *isolated aperiodic* peak, and the paragraph's own repetition clause
   already places powers-of-cycles at `C = 1` — so the elliptical reading is
   the only self-consistent one. Minor co-edit candidate for a future round
   ("no isolated *primitive* `C = 1` peak…"), not rewritten by us, not a flag
   against the key.
2. **A satisfied conditional left standing.** Our appended Key-status
   paragraph (unchanged, correctly) still ends "Status stays **DRAFT** with
   this stated until then"; the header above it now says two keys. The stated
   condition — acceptance of a restatement — is met by `49351e5`, so the
   paragraph reads as a satisfied conditional, but a reader meets "DRAFT" and
   "Two keys" in one entry. Date-stamping the paragraph is a natural co-edit,
   the author's call.

## Item 3 — `6b9f2b1` review

**NOTE §6, the changed sentence** (one paragraph, 1 insertion / 1 deletion;
the margin sentence and "No promise past the calculations" untouched). The
rewrite inserts, into the residual-hypothesis sentence, the parenthetical:

> (the *arithmetic* distribution of the seam residues across profiles — to be
> kept terminologically distinct from the ergodic/statistical equidistribution
> of AEH orbits, `aeh.md 13.6.7`; note that `R_r mod ℓ` is in fact non-uniform
> at every prime yet unconfined, structural bias strongest at `7 = 2³−1`,
> consistent with the prime-local probe's *no-coset-confinement* verdict; the
> structured refuge is closed by descent [L-A4])

Adjudicated against our round-8 record (12.6.1.6; part-A table in
`briefs/merle-round8-coedit-findings.md`):

- **The disambiguation itself is exactly ours:** arithmetic-family vs
  AEH-ergodic, with the correct pointer `aeh.md 13.6.7` (the remark written
  for precisely this distinction, cited from 12.6.1.5's calibration). Accurate.
- **"Structural bias strongest at `7 = 2³−1`"** matches 12.6.1.6's provable
  content (unique minimal 3-element orbit of `2^s − 1` mod 7, the maximal
  collapse; largest and most robustly detectable bias, not an exclusive one)
  and replaces his letter-era "solitary 7" — the refinement absorbed, not
  overstated.
- **"Non-uniform at every prime yet unconfined"** does not overstate our
  part-A finding — it goes *further than our measured record* but on his own
  new committed artifact: our record shows mod 5 also crossing his
  significance bar at `N = 30,000` (TV `0.0128` vs 7's `0.0151`), single-term
  distributions far from uniform at every prime, and family-level bias
  measured only for small-orbit primes (decaying with block count to the
  sampling floor). The at-every-prime claim rests on REQ-MATH-021/021b
  (committed in `905d75b`, same commit as the axioms log): his chi²/df-growth
  criterion vs `N` (30k/120k/480k) reports STRUCTUREL for all of
  `ℓ ∈ {5, 7, 11, 13, 31, 127}`, with the header conclusion "7's uniqueness
  is the mechanism (`2³−1`), not detectability" — the same direction as our
  refinement, extended by his measurement. **Read, not re-run** (his script,
  per the standing rule); recorded as his artifact's claim, consistent with
  and unrefuted by everything our side measured. "Unconfined" and the
  no-coset-confinement pointer match the prime-local probe verdict recorded
  in 12.6.1.1 / NOTE §4 (`briefs/prime-local-probe-findings.md`). No
  resolution-dependence clause survives in his sentence, but under the
  structural (chi²-growth) framing none is needed — the claim is no longer a
  detectability claim.
- **The L-A5 citation additions point at real artifacts** (verified item 4):
  the `#print axioms` link resolves at `905d75b` to
  `experiments/ContentSeparation_axioms.txt` with kernel-3 for all five
  theorems, and the unreduced-modulus note is really in
  `ContentSeparation.lean`'s header as of `905d75b` (statements about the raw
  `q = 2^K − 3^n`, never `q/gcd`; the `p = 7` seed named as where they
  differ; `q_divisor_coprime` stated with no reduction assumed). One flat
  pin note: the entry's *file* link for `ContentSeparation.lean` still points
  at blob/`e297d9d`, whose header predates the note — the note is visible
  from `905d75b` onward. Same benign pattern as the earlier REQ-018 pin;
  recorded, not a mismatch of substance.

## Item 4 — Lean repo, read-only

Fresh clone; `main` = `97b57d719e30d0967ab6129ad13d17289202d700` (`97b57d7`),
as the letter said. **The graph `017288f → 97b57d7` is linear** (each commit
the sole parent of the next), all authored 2026-07-24 CEST:

`017288f` (12:38, REQ-013..017) → `3ed1ef4` (14:38, REQ-018) → `9932f3f`
(14:56, REQ-019) → `e297d9d` (15:12, ContentSeparation.lean + REQ-020) →
**`905d75b`** (17:29, review hardening: unreduced-modulus header note +
committed `ContentSeparation_axioms.txt` + REQ-021/021b) → `ae1edba` (18:05,
REQ-022/023) → **`67c428a`** (18:21, ContentDescent.lean + committed
`ContentDescent_axioms.txt` + REQ-024) → `8b3a7d3` (REQ-025) → `7e4b005` →
`a9ae7bb` → `1648a6c` → `f550147` (REQ-029) → `6679e2a` → `d873bbc` →
`97b57d7` (22:30, REQ-034). Both cited commits exist on `main`, where the
letter and ledger place them.

### The `905d75b` reconciliation — the graph answers it: added later, not missed

- At `e297d9d` (the HEAD our la5-check recorded, 15:12 +0200), `git ls-tree`
  shows **no** `*_axioms.txt` anywhere in the tree — re-verified this session.
  Our check's observation "`#print axioms` output not committed anywhere in
  the repo" was **correct at the commit it examined**.
- `905d75b` is the direct child of `e297d9d`, committed 17:29 +0200 — about
  2h17m later — and it is the commit that adds
  `experiments/ContentSeparation_axioms.txt` (its own header stamps the
  capture at 2026-07-24T15:25Z = 17:25 +0200). Our clone recorded `main` at
  `e297d9d`, so the clone predates the push of `905d75b`.
- **Reconciliation, flat:** both records are right with times attached. The
  letter's "has been in the stack" is true from 17:29 +0200 on 2026-07-24;
  our "not committed" was true of the stack at `e297d9d`, the HEAD at check
  time. We did not miss it; it was added after our check — quite possibly in
  response to the invitation our findings carried ("an OUT file would close
  it"), which the pushed co-edit block also stated. No discrepancy of fact.
- **`ContentSeparation_axioms.txt` contents:** kernel-3 (`propext`,
  `Classical.choice`, `Quot.sound`) for **all five** ContentSeparation
  theorems (`T1`, `T2`, `separation_T1`, `separation_T2`,
  `q_divisor_coprime`) — exactly what the entry's citation claims. The
  header also claims a clean compile (`lake env lean`, 0 errors) — his log,
  read not reproduced. This closes the la5-check flag (iii) at the level of
  a committed record: the kernel-3 claim now rests on a committed log rather
  than header prose. It remains his log, not our build (below).

### `ContentDescent.lean` at `67c428a` — statement-level review, clause by clause

The file works in `namespace ContentDescent` over `List (ℕ × ℕ)` with
`msum l = Σ m`, `mssum l = Σ (m + s)` (= `K`), the fold
`W0 [] = 0; W0 ((m,s)::rest) = 3^(msum rest)·2^m·(2^s − 1) + 2^(m+s)·W0 rest`
(the same fold as ContentSeparation.lean), `rep l k` = k-fold concatenation,
and the recursive cofactor `geom l 0 = 0; geom l (k+1) = 3^(k·msum l) +
2^(mssum l)·geom l k` (with `geom_nonneg`/`geom_pos` lemmas). Header states
scope (unreduced modulus throughout) and the exact statement list. Against the
`08dc3d5` LEDGER block AND our verified forms:

| `08dc3d5` block clause | Lean statement (as read) | vs our verified form | Match |
|---|---|---|---|
| cocycle `W0(l1 ++ l2) = 3^(msum l2)·W0(l1) + 2^(mssum l1)·W0(l2)` | `lemma W0_append`, identical, arbitrary lists | the la5-check prefix lemma is its `msum`-matched special case; verified exhaustively + random this session | **Exact** |
| `power_mult`: `W0(B^k) = G_k·W0(B)` | `theorem power_mult : W0 (rep l k) = geom l k * W0 l` (all `k ≥ 0`) | `R_0(B^k) = R_0(B)·G_k` (12.6.1.4) times the common `2^{m_0}` | **Exact** |
| `q_pow_factor`: `q(B^k) = G_k·q(B)` | `theorem q_pow_factor : 2^(k·mssum l) − 3^(k·msum l) = geom l k · (2^(mssum l) − 3^(msum l))` | `q_P = q_B·G_k` (12.6.1.4) | **Exact** |
| `cycle_iff` both directions, `k ≥ 1` | `theorem cycle_iff (hk : 1 ≤ k) : q(B^k) ∣ W0(B^k) ↔ q(B) ∣ W0(B)` (proof cancels `geom_pos`) | the L-A4 biconditional, untuned, both signs (round-8: 12,888 checks) | **Exact** |
| `gcd_climb`: `gcd(q(B^k), W0(B^k)) = G_k·gcd(q(B), W0(B))` | `theorem gcd_climb : Int.gcd … = (geom l k).natAbs * Int.gcd …` (all `k ≥ 0`) | the L-A2 law one level up, 12.6.1.4(b) | **Exact** (`natAbs` is cosmetic: `geom ≥ 0` by `geom_nonneg`) |

**`G_k` definition check:** unrolling the file's recursion gives
`geom l k = Σ_{c<k} 2^(c·mssum l)·3^((k−1−c)·msum l)` — with `mssum = K_B`,
`msum = n_B`, **exactly 12.6.1.4's `G_k = Σ_{c<k} 3^((k−1−c)·n_B)·2^(c·K_B)`,
the cofactor our identity produces** (`q_P/q_B`). Verified recursive = closed
= `q`-cofactor at all 540 grid pairs this session (item 5), plus hand values
(`G_1 = 1`, `G_2 = 3^{n_B} + 2^{K_B}`; trivial word 7; `−17` word 4,235).

Statement-scope observations, flat: (1) letters live in `ℕ²` with zeros
allowed and `k = 0` is included where stated — a superset of the wiki's
entries-`≥ 1` convention, strictly more general, harmless (same posture as
ContentSeparation). (2) `q` appears as the expression `2^(mssum l) − 3^(msum l)`
rather than a named def — matches the block's `q(l)` gloss. (3) The block's
"kernel-certified end to end" is scoped by its own words to the *structured
half* (repetition/descent/climb); no wall claim anywhere in block or file.
(4) `67c428a` also carries REQ-MATH-024 (transfer-path content measurements),
outside the block's citation; noted only.

**Checks by read:** 0 occurrences of `sorry`, 0 of `native_decide`, no `axiom`
declarations, single `import Mathlib`; two non-vacuity canaries proved by
`norm_num` (trivial word: `W0(B²) = 7·W0(B)`; the trivial square is a cycle,
`7 ∣ 14`) — both re-derived by hand this session and used as script canaries;
five `#print axioms` commands, and **`experiments/ContentDescent_axioms.txt`
is committed in the same commit**: kernel-3 for all five (`W0_append`,
`power_mult`, `q_pow_factor`, `cycle_iff`, `gcd_climb`), header claiming a
clean compile. So this file's axioms log was committed from the start — the
ContentSeparation gap did not recur.

**Build status, honestly: read, not built.** No Lean toolchain on this machine
(`lake`/`elan` absent), so the ~15-minute build window could not be attempted —
same posture as the la5-check and L-A1 precedents. The kernel-3 claims rest on
his committed logs; the mathematical content is independently confirmed by
this session's clean-room check regardless (item 5), so nothing downstream
hangs on the build.

## Item 5 — clean-room statement check

`experiments/merle_contentdescent_check.py`, run 2026-07-25; committed output
alongside. `W0 := 2^{m_0}·R_0` implemented from cycles.md 12.6.1's `R_0` only
(the wrap term never enters `R_0` on a linear word, noted in-file);
`W0([]) := 0`. Canaries hand-computed and printed before any sweep: the
trivial word (`R_0 = 1`, `W0 = 2`, `q = 1`), the trivial square (`R_0 = 7`,
`W0 = 14`, `q = 7` — both Lean canaries reproduced), a hand-computed cocycle
instance (`86 = 86`), the `−17` word (`q = −139`, `R_0 = 139`, `W0 = 2,224`,
`G_2 = 4,235`, `q(B²) = −588,665 = −139·4,235`), hand values of `geom`, and
one `cycle_iff` instance each direction (trivial word = cycle base; `((1,2))`
= non-cycle base, `5 ∤ 6` and `55 ∤ 66`). All passed before any sweep.

- **Cocycle (`W0_append`):** exhaustive over all ordered pairs of words of
  length ≤ 2 with entries in `{1,2}` (21 × 21 = 441) + 300 random pairs
  (lengths 0–4, entries 1–9; concatenated `q > 0` in 265, `q < 0` in 29) —
  **741/741 exact**.
- **Power laws:** grid of 540 `(B, k)` pairs (exhaustive: 90 bases of length
  1–2, entries `{1,2,3}`, `k ∈ {1..4}`; random: 60 bases of length 3–6,
  entries 1–8, `k ∈ {2,3,4}`; 49 negative-`q` bases, 16 divisible-base pairs
  all inheriting upward). At every pair, seven exact checks: `geom` recursive
  = closed form, `geom` = `q`-cofactor (`q_pow_factor`), `power_mult` in `W0`,
  the 12.6.1.4 identity in `R_0`, `gcd_climb`, `gcd(q, W0) = gcd(q, R_0)`
  (`q` odd), and the `cycle_iff` biconditional — **3,780/3,780 exact**.
- **Total: 4,541 exact checks, 0 failures.** The Lean statements as read are
  the same laws as 12.6.1.4's descent identity, its `q`-factorization, and
  the L-A2 gcd law one level up, plus the cocycle they hang on — this largely
  re-confirms round 8 (12,888 checks), which is the point: the formalization
  matches the verified mathematics, clause for clause.

## Adjudication summary

| Claim | Status |
|---|---|
| `49351e5` lands offers (a) + (b); two-keys marking honest | **CLEAN — confirmed.** Claim-identical to the offered restatement on every required clause; `−17` exhibit correct; domain clause landed; key grounds truthful. Two observations (wall rider's elided "aperiodic/primitive"; the satisfied DRAFT conditional left standing) — co-edit candidates, not key blockers |
| `6b9f2b1` NOTE §6 disambiguation | **Confirmed accurate** — the arithmetic-vs-AEH split with the right pointer (13.6.7); "strongest at 7 by the `2³−1` mechanism" is 12.6.1.6's content; "non-uniform at every prime" rests on his committed REQ-MATH-021 (read, not re-run), consistent with our part-A refinement and going beyond it only on his own artifact |
| `6b9f2b1` L-A5 citation additions | **Confirmed real** — `905d75b` axioms file resolves (kernel-3, all five theorems); unreduced-modulus header note present at `905d75b`; flat pin note: the Lean-file link itself still points at `e297d9d`, which predates the note |
| The letter's `905d75b` "has been in the stack" vs our "not committed" | **Reconciled by the graph, no discrepancy:** the file entered at `905d75b` (17:29 +0200), the direct child of `e297d9d` (15:12), which was `main` when our check cloned. Added after our check; not missed by it |
| `08dc3d5` ContentDescent kernel block | **Confirmed at statement level, read-not-built** — all five statements match the block and our verified 12.6.1.4/L-A2 forms exactly; `G_k` is our cofactor; 0 sorry / no `native_decide` / no user axioms by read; axioms log committed in the same commit, kernel-3 all five; no toolchain here, build not attempted |
| Clean-room re-confirmation | **4,541 exact checks, 0 failures** (`merle_contentdescent_check.py`) |

**Flags, collected:** none blocking. Observations for the reply/co-edit
rounds, flat: (i) the wall rider in the restated gloss reads standalone
without "aperiodic/primitive" — forced powers of `+1` are literal
positive-shore isolated `C = 1` words — while the in-context anaphora is
unambiguous; a two-word precision would close it. (ii) Our appended
Key-status paragraph's "DRAFT until then" conditional is now satisfied but
still reads as pending; date-stamping is the author's call. (iii) The entry's
`ContentSeparation.lean` link pin (`e297d9d`) predates the header note the
same sentence cites (`905d75b`). (iv) Kernel-3 rests on committed logs, not
an our-side build (no toolchain; established read-not-built practice). **No
discrepancies of digits, hashes, or texts anywhere this round. Handbacks:
none.**
