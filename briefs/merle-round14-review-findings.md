# Findings: round-14 review window — PR #4 verified (L-A10 keyed with fresh code, the two retractions read and confirmed, the three round-13 carries closed at their addresses), paperwork drafts

Brief: `briefs/merle-round14-review-brief.md`. Branch **`merle-round14-review`**.

**Base SHA: `6a908051c13efe990d0c0926d150dc73d9ed7d69`** ("briefs: the round-14
review brief ..."), local `main`'s tip at session start. The worktree
contained the brief at launch; no fast-forward was needed.

Register: flat, calibrated prose. Every number carries its named source or
this session's own derivation; every defect found in Merle's material is a
finding delivered kindly, in the register of his letters and of our round-13
review (`briefs/merle-round13-review-findings.md` §7.1). Nothing here turns a
key: the review is a draft (§9.1) and the posting is the author's decision.

---

## 1. State check (Queue 1)

**Fresh scratchpad clones, read-only** (`git clone`, no fork/issue/star/
watch/comment/push, no interaction with any repository beyond the clone and
`gh` reads):

| repo | expected | actual | status |
|---|---|---|---|
| `macindoe/one-obstruction-three-faces` `main` | `93c6ac4` | `93c6ac49886c3a2887fef282b00991f8357dce0b` | **MATCH** |
| — branch `round-14` (PR #4) | `2f7b865` | `2f7b865ba609364dd0535b48c691cca4a81d32ba` | **MATCH** |
| — branch `round-13` | `f336e57` | `f336e577c5b452985a44f5ebc572989e597c7804` | **MATCH** (merged) |
| — branch `note-v1-draft` | `96ccadf` | `96ccadf889e5466eba81dddab953fbf45de994d3` | **MATCH** (merged) |
| — branch `round-12` | `accda4b` | `accda4b47c407ea1b2dfdfc5c01b6ad79784ce9b` | **MATCH** (merged) |
| `ericmerle3789/one-obstruction-three-faces-lean` `main` | `db0e89d` | `db0e89de423f9208734b4a8a0ecfebc0c987a807` | **MATCH** |
| `ericmerle3789/Collatz-Junction-Theorem` `main` | `8bcee67` | `8bcee67ec278d2288f6fac35612931e1a4d4d254` | **MATCH** |
| — branch `proof-assembly-v1` | `77e3f07` | `77e3f071843fd48a8e386a7e5a41f1d035ec761d` | **MATCH** (the round-13 retraction commit) |
| — branch `syracuse-jepa-v2` | (new to our record) | `f6e1bff6954dad33c2049742dff1fa89410a5e3f` | recorded flat, not read |

Nothing has moved beyond the brief's Provenance. `grep "GRADE AT SIGNING"
NOTE-v1.md` on `main` returns nothing — the bracket patch is on `main` at
`93c6ac4`, as the Provenance says.

**PR #4** (`gh pr view 4 --json ...`, read-only): number 4, title "Round 14:
§96 settled at two lines, the p=3 question answered, two retractions", state
**OPEN**, opened `2026-09-03T18:14:43Z` by `ericmerle3789`, base `main`
(`baseRefOid 93c6ac4`), head `round-14` (`headRefOid 2f7b865`), **reviews:
none**, `reviewDecision` empty, `mergeable: MERGEABLE`. Files: `LEDGER.md`
`+38/−0`, `briefs/merle-breach-campaign-map.md` `+36/−17`,
`rounds/R14-merle.md` `+134/−0` (`git diff --stat 93c6ac4..2f7b865`: 3 files,
208 insertions, 17 deletions; one commit, `2f7b865` "Round 14: section 96
settled at two lines, and two retractions it forced."). `gh pr diff 4` is 256
lines, LF-only.

**PR #3**: state **MERGED**, `mergedAt 2026-09-03T17:00:46Z`, `mergedBy
ericmerle3789`, merge commit `95e721224a793c881e7b73784c11303f04ce8719`,
head `f336e57`; our review `macindoe APPROVED 2026-09-03T14:23:00Z`.

### 1.1 PR #4 body, verbatim

> Round 14. Answers the `p = 3` non-reproduction your round-13 review raised, and carries the two retractions it forced. Full letter: `rounds/R14-merle.md`.
>
> **Your `p = 3` finding was right, and your own operational note 1 named the cause.** Your figures reproduce exactly here. They land on a different object: the **accelerated** map with one canonical successor per residue, where §96 works on the **Terras half map** carrying **both** lifts from `ℤ/2^{k+1}` (`run_049` line 33, now public). Your graph keeps the `m = 0` branch of a relation with `2^v` branches, and the witness edge lives on the other one — at `p=3, k=8` your map sends `255 → 127` where ours has `255 → 255`. Both are checked side by side in `run_050` P4.
>
> **And the entry is better for having been asked.** `LEDGER.md` **L-A10**, seeded at one key with artifacts committed, as you proposed:
>
> > Since `p−2` is odd, put `r_p = −(p−2)^{−1} mod 2^{k+1}`, `u_p = r_p mod 2^k`. Then `r_p` is odd, and for **every** positive `x ≡ r_p (mod 2^{k+1})`: `x ≡ T(x) ≡ u_p (mod 2^k)` and `T(x) − x = ((p−2)x+1)/2 > 0`. Same residue ⇒ same `f` ⇒ `V(T(x)) > V(x)`.
>
> Two lines, one integer comparison `p > 2`. No Bellman–Ford, no linear program, no cycle enumeration, no census, no floating point. At `p=3`: `u_p = 2^k − 1`, and `511 → 767` at `k=8`. **Nothing in that mathematics is new** — the loop is §95's, the legitimacy of the constraint is §96's; this round adds only that the two already suffice on their own.
>
> **Two retractions, both mine.**
> 1. **The phantom census is withdrawn in full, including the "100 % at `p=7,k=8`" I sent you in round 13.** Preparing the artifacts, `run_048.py` turned out **not to run** — its own canary C3 fires and halts it — so that output was never produced; with the one-word bug fixed it fails its **own** control P5 (it emits `x = −6`, on no cycle); and it never tests `p = 7`. **Withdrawn, not corrected.** It is committed exactly as written, canary firing, nothing removed. Offer g's pattern turned on ourselves. The conclusion never depended on it — `run_049`'s own argument is that phantom-ness is beside the point.
> 2. **A formulation of mine:** the witness does *not* climb forever inside its class; it leaves at step 2. My own canary caught it. One step is all the argument ever needed.
>
> I have also disambiguated your own 100 %-phantom figure in the map: it is **yours, on your object**, and this side has not reproduced it — it must not be read as related to the withdrawn census.
>
> **Also in this round:** your peak replication accepted with your wording, both readings as you stated them (clustering a clean non-finding, spectral marginal) — the spectral mismatch is **my** defect and I withdraw `5.62× @ f=124` as a recoverable claim; your `θ` strengthening verified independently and adopted (at `p = 5, 7` there is no nontrivial positive root **at all**); the h4 provenance recorded on my side too — those three numbers are your script's output returned to you; and the Rhin locatability fixed (`8bcee67`, additive, 10 lines, nothing removed).
>
> Artifacts: `ericmerle3789/one-obstruction-three-faces-lean` at `db0e89d` — `run_050.py` (14 checks, 0 failures, integer arithmetic: 4000 `(p,k)` pairs, 2880 positive witnesses, the divergence diagnosis, a negative control at `p=1` so it cannot prove too much), `run_049.py`, and `run_048.py` with its retraction header.
>
> No schedule, ever. Whenever the governance consultation lets go.

### 1.2 PR #4 diff, verbatim (`gh pr diff 4`, 256 lines)

```diff
diff --git a/LEDGER.md b/LEDGER.md
index 8af722a..9d40d28 100644
--- a/LEDGER.md
+++ b/LEDGER.md
@@ -479,3 +479,41 @@ Offers, inside the entry per the co-edit style — his prose untouched, acceptan
 
 Artifact: `macindoe/collatz` `experiments/merle_la9_check.py` with committed output (commit `913f577`, on public `main`; 50 checks, 0 failures).
 
+
+---
+
+## L-A10 — No finite-quotient altitude decreases: the ascending fixed point (Merle, §95–§96, correspondence 2026-09-03)
+
+**Seeded at one key with artifacts committed, per your round-13 review** ("seed it as a ledger entry with the artifacts committed, we key it, and it enters v2 at two keys like everything else there"). Your `p = 3` question is what forced the entry into this shape, and it is the reason the entry is better than the offer was.
+
+**Claim.** Let `p ≥ 3` be odd and let `T` be the Terras half map — `T(x) = x/2` for `x` even, `T(x) = (px+1)/2` for `x` odd. Then for every fixed `k ≥ 1` and **every** function `f : ℤ/2^k → ℝ_{>0}`, the multiplicative altitude `V(x) = x · f(x mod 2^k)` fails to satisfy `V(T(x)) < V(x)` on all positive integers. No compression of `x` to its last `k` bits can carry a descent certificate.
+
+**Proof, in full.** Since `p − 2` is odd it is invertible mod `2^{k+1}`; put
+
+> `r_p = −(p−2)^{−1} mod 2^{k+1}`  and  `u_p = r_p mod 2^k`.
+
+`r_p` is odd (the inverse of an odd number is odd, and `2^{k+1} − odd` is odd), so the ascending branch applies, and by construction `(p·r_p + 1)/2 ≡ u_p (mod 2^k)`. Now take **any** positive integer `x ≡ r_p (mod 2^{k+1})`. Writing `x = r_p + m·2^{k+1}`, we get `(px+1)/2 = (p·r_p+1)/2 + pm·2^k`, so
+
+> `x ≡ u_p (mod 2^k)`,  `T(x) ≡ u_p (mod 2^k)`,  and  `T(x) − x = ((p−2)x + 1)/2 > 0`.
+
+The two points therefore carry **the same** value of `f`, and `V(T(x)) = T(x)·f(u_p) > x·f(u_p) = V(x)`. ∎
+
+**What this costs: nothing.** One integer comparison, `p > 2`. No Bellman–Ford, no linear program, no cycle enumeration, no phantom census, no floating point anywhere. For `p = 3` the witness is the plainest object in the problem: `u_p = 2^k − 1`, and the smallest positive witness at `k = 8` is `x = 511 → T(x) = 767`, both `≡ 255 (mod 256)`.
+
+**Provenance, stated exactly.** Nothing in the mathematics above is new to this round. The loop is **§95**'s — the fixed point of the ascending branch, `x = −1/(p−2)`, present for every odd `p` (25 cases). That the constraint is legitimate *whether or not integers close a cycle* is **§96**'s, established in `run_049` P1 (20,000 edges, all realised). This round contributes only the observation that those two results already suffice **on their own, in two lines**, and the exact-integer instrument that shows it.
+
+**Why `ℤ/2^k` cannot see it.** `ℤ/2^k` does not distinguish `2^k − 1` from `−1`, and `−1` is a genuine fixed point of `3x+1`. The finite quotient inherits, as a loop, the shadow of a real fixed point living on the part of `ℤ` where the altitude is not defined. This is the "one obstruction" seen from the digits face: not an accident of the modulus, but the price of forgetting the sign.
+
+**One formulation retracted, ours, before you have to catch it.** The trajectory does **not** stay in its residue class: `511 → 767 → 1151`, and `1151 ≡ 127 (mod 256)` — it leaves at step 2. The lift of `767` in `ℤ/2^{k+1}` is `255`, not `511`, so the next step takes the other branch. Any wording of this entry that says the witness "climbs forever inside one class" is false and is withdrawn. **One step is all the argument ever needed**, which is precisely §96's point restated: the constraint is on the *edge*, never on a closed trajectory — so the phantom/real question does not even arise here.
+
+**Your `p = 3` non-reproduction, resolved — and you had already named the cause.** Your reconstruction measured the **accelerated** map `x → (px+1)/2^v` on odd residues with **one canonical successor** per node. Ours is the Terras half map carrying **both lifts** from `ℤ/2^{k+1}` (`run_049` line 33) — the relation has `2^v` successors and yours keeps the `m = 0` branch. Verified both ways in `run_050` P4: your figures reproduce exactly on your object (`p=3`: none at `k=4..9`, one at `k=10`, one at `k=11`, two at `k=12`, none at `k=13..16`; `p=7,k=8`: three, at `(L,K) = (3,4), (4,8), (31,67)`), **and the witness edge `u → u` is absent from it** — at `p=3, k=8` your map sends `255` to `127`. Your operational note 1 identified this exactly; the measurement was right and the object was not ours. Your other three operational gaps — the tautological edge-realizability check, the choice of "phantom" criterion, and the bounded search — are recorded as **moot for this entry rather than answered**: the two-line argument needs no cycle, so it never asks whether one closes.
+
+**Two retractions carried into this entry, neither touching the claim.**
+- **The phantom census is withdrawn in full**, including the figure *"100 % of the faulty residue cycles are phantoms at `p = 7, k = 8`"* quoted in `rounds/R13-merle.md` §6 and in `briefs/merle-breach-campaign-map.md`. Re-running `run_048.py` for this delivery found that **it does not run**: its own canary C3 fires and halts it (its `rationnel` walks the word backwards where `run_049`'s walks it forwards), so its P3/P4/P5 were never produced. With that one-word bug fixed it then fails its **own** control P5, emitting `x = −6`, which lies on no cycle — it solves the word's linear equation without checking that the trajectory's parities follow the word. The file never tests `p = 7` at all. The figure is **withdrawn, not corrected**, and `run_048.py` is committed exactly as written with a retraction header and nothing removed. This is offer g's pattern turned on ourselves: a sentence in this correspondence that had no working artifact behind it.
+- What survives is the entire result: `run_049` is sound, and its argument never needed the census.
+
+**Honest scope.** This closes the family `V = x·f(x mod 2^k)` at *fixed* `k`. **It excludes no cycle**, and nothing here is formalised in Lean. The one escape — `k` growing with `x` — is argued sterile in prose (it stops compressing and falls back to the full parity vector, §75) and that argument is **not** verified in the artifacts; it is offered as prose, at that grade. `p = 1` is carried as a negative control (`run_050` P6): there `T` descends, the constraint is satisfiable, and the argument correctly declines to conclude — it does not prove too much.
+
+**Artifacts — Merle:** `ericmerle3789/one-obstruction-three-faces-lean` at commit `db0e89d`: `experiments/run_050.py` (the exact reprise — 14 checks, 0 failures, integer arithmetic throughout: 4000 `(p,k)` pairs `p = 3..201` odd, `k = 1..40`; 2880 positive witnesses; the divergence diagnosis; the negative control) with `run_050_output.txt`; `experiments/run_049.py` and its output (the standing §96 run, P1's 20,000 edges); `experiments/run_048.py` and its output, committed **with its canary firing**, as the record of the retraction.
+
+**Key status: one key (Merle).** Yours is invited on this entry as you proposed. Placement in the note, as you set it: the principle in one sentence in the body's 2-adic paragraph, the theorem itself in the marked apparatus section.
diff --git a/briefs/merle-breach-campaign-map.md b/briefs/merle-breach-campaign-map.md
index fab0fa6..c123025 100644
--- a/briefs/merle-breach-campaign-map.md
+++ b/briefs/merle-breach-campaign-map.md
@@ -22,29 +22,48 @@ for. Nothing here excludes a cycle.
 
 ## Two hard negatives (theorem-grade)
 
-**⊢ Finiteness of the quotient (§96).** No multiplicative altitude `V(x) = x·f(x mod 2^k)`,
-for any *fixed* `k`, can strictly decrease under the accelerated map on all integers — and
-the reason is not Collatz, it is that `ℤ/2^k` carries residue cycles `ℤ` does not. `g = log f`
-telescopes to 0 around every residue cycle, forcing `Σ(log3 − v·log2) < 0` there, but the
-finite quotient has cycles with `Σ ≥ 0` ("phantoms", 100% of the faulty cycles at `p=7,k=8`),
-each edge realised by a real integer (20,000 random edges, all realised) — so the constraint
-set is legitimately unsatisfiable. The only escape, `k` growing with `x`, is sterile (it stops
-compressing and falls back to the full parity vector, i.e. almost every integer). *This is the
-first failure reason I have that sits in the tool, not the problem — and it is what the note's
-2-adic / digits face is for.* Detailed in `rounds/R13-merle.md` §6.
+**⊢ Finiteness of the quotient (§95–§96).** No multiplicative altitude `V(x) = x·f(x mod 2^k)`,
+for any *fixed* `k`, can strictly decrease on the positive integers under the Terras half map
+`T` — and the reason is not Collatz, it is that a finite window on the last `k` bits cannot see
+the sign. **Two lines, one integer comparison.** Since `p − 2` is odd, set
+`r_p = −(p−2)^{−1} mod 2^{k+1}` and `u_p = r_p mod 2^k`; `r_p` is odd, so for every positive
+`x ≡ r_p (mod 2^{k+1})` we get `x ≡ T(x) ≡ u_p (mod 2^k)` with `T(x) > x` whenever `p > 2`.
+The two points carry the *same* `f`, so `V(T(x)) > V(x)`. For `p = 3`: `u_p = 2^k − 1`, and
+`511 → 767` at `k = 8`, both `≡ 255 (mod 256)`. `ℤ/2^k` does not distinguish `2^k − 1` from
+`−1`, and `−1` is a genuine fixed point of `3x+1` — the quotient inherits, as a loop, the
+shadow of a real fixed point living where the altitude is not defined. The only escape, `k`
+growing with `x`, is sterile — it stops compressing and falls back to the full parity vector,
+i.e. almost every integer — and that last clause is prose, not an artifact. *This is the first
+failure reason I have that sits in the tool, not the problem — and it is what the note's 2-adic
+/ digits face is for.* Full entry, artifacts and scope: `LEDGER.md` **L-A10**.
+
+> **Withdrawn (2026-09-03).** This paragraph previously ran the argument through a census of
+> "phantom" residue cycles and quoted *"100 % of the faulty cycles at `p = 7, k = 8`"*. **That
+> figure is withdrawn, not corrected**: re-running its artifact for the round-14 delivery showed
+> the script halts on its own canary and had never produced the census at all, that the census is
+> wrong again once the halting bug is fixed, and that the file never tests `p = 7`. It also said
+> "the accelerated map", which is not the map §96 works on. Nothing in the conclusion depended on
+> any of it — the standing run's own argument is that phantom-ness is *beside the point*, since
+> every edge is realised by real integers (20,000 checked). Kept visible rather than deleted, and
+> detailed in L-A10.
 
 **Cross-side, round 13 — what came back (2026-09-03).** Your review reconstructed the
-telescoping mechanism independently, and it reproduces exactly at `p=7, k=8` (4 residue cycles,
-3 faulty, 100% phantom under a bounded search) — confirmed a third time here, cycle for cycle,
-lengths and valuation sums identical. Carried alongside it, at the grade you set it: it **does
+telescoping mechanism independently, and it reproduces exactly at `p=7, k=8`: 4 residue cycles,
+3 faulty, at `(L,K) = (3,4), (4,8), (31,67)` — **that** much confirmed a third time here, cycle
+for cycle, lengths and valuation sums identical. Your accompanying bounded search found those
+three faulty cycles to be 100% phantom; **that figure is yours, on your object, and this side has
+not reproduced it** — it should not be read as related to the withdrawn census above, which was
+mine, on a different graph, and never computed at all. Carried alongside it, at the grade you set
+it: your reconstruction **does
 not reproduce for `p=3` at small `k`** — no faulty cycle for `k = 4..9`, one at `k = 10` and
 `k = 11`, two at `k = 12`, none again at `k = 13..16` — non-monotonic, reproduced here exactly.
 Your own operational note names the likely cause (the residue graph you had to specify keeps one
 successor per node, where the relation has `2^v`), and you are right that this is what the keying
-round must settle first. It is settled, and in your favour; but the argument is new material you
-have not read, so it does not travel under this round's approval — it is round 14, with the
-artifacts, for your key. Until then this ⊢ item stands at **`p = 7` verified cross-side, `p = 3`
-open**, and the four operational gaps your review records stand with it.
+round must settle first. **Settled in round 14, and in your favour**: your figures reproduce
+exactly on your object, and the cause is the one your own note named — the accelerated map with
+a single canonical successor keeps the `m = 0` branch, and the witness edge lives on the other
+one. Your measurement was right; the object was not ours. The resolution, the artifacts and the
+two retractions it forced are in `LEDGER.md` **L-A10**, seeded at one key for yours.
 
 **⊢ No metric descent of the excursion form (§80, §85).** The excursion is the maximum of a
 multiplicative walk (×3/2 or ×1/2, each with probability ½ under the §75 bijection). Its tail
diff --git a/rounds/R14-merle.md b/rounds/R14-merle.md
new file mode 100644
index 0000000..5745381
--- /dev/null
+++ b/rounds/R14-merle.md
@@ -0,0 +1,134 @@
+# Round 14 — Merle to Macindoe
+
+*Reply to your round-13 approving review of PR #3. Business paragraphs only; the personal
+half travels by mail, per the accepted split. This round is a pull request; the second key
+is the approving review, per PROTOCOL §13.*
+
+---
+
+## 1. Your `p = 3` non-reproduction: you were right, and you had already named the cause.
+
+You reconstructed §96 independently, reproduced it at `p = 7, k = 8`, and reported that it
+**does not reproduce for `p = 3` at small `k`** — none at `k = 4..9`, one at `k = 10` and
+`k = 11`, two at `k = 12`, none again at `k = 13..16`. I reproduced your figures exactly
+before doing anything else with them, cycle for cycle, lengths and valuation sums identical.
+
+The cause is the one your own operational note 1 flagged. You measured the **accelerated**
+map `x → (px+1)/2^v` on odd residues, with the **canonical representative** as the single
+successor. §96's object is the **Terras half map** `T` — `x/2` or `(px+1)/2` — on `ℤ/2^k`
+carrying **both** lifts from `ℤ/2^{k+1}` (`run_049` line 33, now public). Your graph keeps
+the `m = 0` branch of a relation with `2^v` branches, and **the witness edge lives on the
+other one**: at `p = 3, k = 8` your map sends `255 → 127`, where ours has `255 → 255`. Your
+measurement was right; the object was not ours. Both are now checked side by side in
+`run_050` P4.
+
+## 2. And the entry is better for it: §96 now costs two lines and one integer comparison.
+
+Being asked to defend it at every `k` is what stripped the argument down. `LEDGER.md`
+**L-A10**, seeded at one key with artifacts committed, as you proposed:
+
+> Since `p − 2` is odd, put `r_p = −(p−2)^{−1} mod 2^{k+1}` and `u_p = r_p mod 2^k`. Then
+> `r_p` is odd, so for **every** positive `x ≡ r_p (mod 2^{k+1})`:
+> `x ≡ T(x) ≡ u_p (mod 2^k)` and `T(x) − x = ((p−2)x + 1)/2 > 0`.
+> The two points carry the same `f`, hence `V(T(x)) > V(x)` — for every `f`, every `k`,
+> every odd `p ≥ 3`.
+
+No Bellman–Ford, no linear program, no cycle enumeration, no census, no floating point. For
+`p = 3`: `u_p = 2^k − 1`, and the smallest witness at `k = 8` is `511 → 767`, both
+`≡ 255 (mod 256)`. Verified over 4000 `(p,k)` pairs and 2880 positive witnesses in exact
+integers, with a negative control at `p = 1` so it cannot prove too much.
+
+**Provenance, stated exactly, because it matters more than the result.** Nothing in that
+mathematics is new. The loop is **§95**'s — the fixed point of the ascending branch,
+`x = −1/(p−2)`, present for every odd `p`. That the constraint is legitimate *whether or not
+integers close a cycle* is **§96**'s, established in `run_049` P1. This round contributes the
+observation that those two already suffice on their own, and the instrument that shows it.
+The interpretation the short form makes visible: `ℤ/2^k` cannot distinguish `2^k − 1` from
+`−1`, and `−1` is a genuine fixed point of `3x+1`. The quotient inherits, as a loop, the
+shadow of a real fixed point living on the part of `ℤ` where the altitude is not defined.
+
+## 3. Two retractions, both ours, and the second one is mine from this round.
+
+**(a) The phantom census is withdrawn in full — including the number I sent you.** Preparing
+the artifacts for this PR, I re-ran `run_048.py` and found that **it does not run**: its own
+canary C3 fires and the assert halts it, because its `rationnel` walks the word backwards
+where `run_049`'s walks it forwards. Its P3/P4/P5 outputs were **never produced**. With that
+one-word bug fixed it then fails its **own** control P5 — it emits `x = −6`, which lies on no
+cycle, because it solves the word's linear equation without checking that the trajectory's
+parities follow the word. And the file never tests `p = 7` at all.
+
+So *"100 % of the faulty residue cycles are phantoms at `p = 7, k = 8`"*, which I put in
+round 13 §6 and in the campaign map, **has no artifact behind it. It is withdrawn, not
+corrected.** This is offer g's pattern turned on ourselves, and the canary had said so all
+along — it was the report that did not listen. `run_048.py` is committed exactly as written,
+with a retraction header and nothing removed, so the record shows the canary firing.
+
+Nothing in the conclusion depended on it: `run_049`'s own argument is that phantom-ness is
+*beside the point*, since every edge is realised by real integers.
+
+**(b) A formulation of mine, retracted before you have to catch it.** The witness does **not**
+climb forever inside its residue class. `511 → 767 → 1151`, and `1151 ≡ 127 (mod 256)`: it
+leaves at step 2, because the lift of `767` in `ℤ/2^{k+1}` is `255`, not `511`. My own canary
+fired on this while I was writing the instrument. **One step is all the argument ever needed**
+— which is §96's point restated at its sharpest: the constraint is on the *edge*, never on a
+closed trajectory, so here the phantom question does not even arise.
+
+## 4. Your peak replication: accepted, and the defect is mine.
+
+Your P4 reproduces my figures exactly (250 peaks, mean gap 7.19, clustering 0.831) on
+independent continued-fraction code — that is the strong evidence, and it says the underlying
+sequence and bookkeeping are the same. **Your corrected null is the right instrument** and
+better than the one I asked for: six real constants on a common footing, with `e` excluded and
+kept as a **positive control** (`891×`, two orders of magnitude clear) and `√2, √3` excluded
+for bounded partial quotients. Recording the exclusions rather than dropping them silently is
+what makes the band mean anything.
+
+I adopt your wording as the record, both readings as you stated them: **clustering, a clean
+non-finding that survives the corrected footing** (rank 4 of 7, inside `[0.646, 1.221]`);
+**spectral, genuinely marginal and reported flat** (rank 1 of 7, one-sided `p ≈ 0.14`, nowhere
+near the positive control). Not forced either way, exactly as you wrote it.
+
+The spectral mismatch is **my defect, not your replication's**: "highest Fourier coefficient of
+the centred peak-indicator, in units of its variance" does not pin a normalisation or a search
+range, and your session is the second to say so. The honest disposition is that the exact
+figure `5.62× @ f=124` is not a recoverable claim and I withdraw it as one; what stands is the
+qualitative reading, on your estimator, consistently applied — which is what the corrected-null
+comparison actually needs.
+
+## 5. Your `θ = 1` strengthening: verified here, and accepted.
+
+Confirmed independently before accepting: `f(1) = (p+1)/2 − 2 = 0` exactly at `p = 3` as a
+`Fraction`; and at `p = 5, 7` there is **no nontrivial positive root at all** — `f'(0) =
+ln(p/4) > 0` there, so the convex function never returns below its trivial root (`+0.2231` at
+`p = 5`, `+0.5596` at `p = 7`; scan of `(0, 50]` finds no sign change). Your mean-log-step
+drift reading is the cleaner mechanism and I take it: `−0.1438` at `p = 3` (down, finite
+excursion), `+0.1116` at `p = 5` (up, infinite). The map's framing "`θ < 1` at `p = 5, 7`" is
+weaker than the truth and is replaced by yours. The scope you carried forward stands as you set
+it: the `R^{−θ}` tail under the §75 bijection rests on my local artifacts and is not
+independently checked.
+
+## 6. The three smaller items, closed.
+
+- **h5.** You were right; the acceptance sentence had been standing in for a discharge for a
+  round. Applied in `f336e57` before the merge, in your wording and your figures, with the
+  superseded drawn control kept visible and the gap itself recorded rather than tidied away.
+- **The h4 provenance.** Noted with thanks, and I record it on my side too: the chord `0.5001`,
+  the 30-bit floor `0.32` and the `μ > ~2.05` threshold are **your** `merle_la9_check.py`'s own
+  PART 3 output, returned to you through my co-edit — not independent verification of a fresh
+  claim. Your re-measurement stands on its own regardless, as you say.
+- **The Rhin locatability.** Fixed: `ericmerle3789/Collatz-Junction-Theorem` `main` at
+  [`8bcee67`](https://github.com/ericmerle3789/Collatz-Junction-Theorem) now carries the
+  retraction at the head of its README, additively — 10 lines added, nothing on that branch
+  edited or removed — so a reader following the archive notice meets it before citing
+  `BILAN_R201.md`. Good catch; it would have sat there for years.
+
+## 7. Placement, and no schedule.
+
+I take your placement decision as given: §96 goes in the marked apparatus section, with the
+principle in one sentence in the body's 2-adic paragraph — *every finite model of `ℤ` inherits
+what `ℤ` does not, so a finite-state descent certificate answers constraints the integers never
+pose*. The Zenodo metadata note is yours to write and I am not touching it.
+
+Seventy checks in the middle of a governance consultation was more than this round had any
+right to ask for. Nothing here is urgent: the problem has waited eighty-nine years, and it
+will wait for either of us to have a good month.
```

### 1.3 The two PR #3 commit messages, verbatim

**`95e7212`** (author `ericmerle3789 <ericmerle3789@gmail.com>`, `Thu Sep 3
19:00:46 2026 +0200`, parents `308d6bb` and `f336e57`):

> Merge pull request #3 from macindoe/round-13
>
> Round 13 — two keys. L-A9 offers h1-h5 applied (Dirichlet half unconditional theorem-grade), Rhin closed on the Merle side, peak-detector spec supplied, section-96 and the breach-campaign map offered.

**`f336e57`** (author `Eric MERLE <ericmerle3789@gmail.com>`, `Thu Sep 3
19:00:16 2026 +0200`, parent `ef1742d`; `LEDGER.md` `4 ++--`,
`briefs/merle-breach-campaign-map.md` `22 ++++++++++++++++++++--`):

> Round 13, pre-merge: apply offer h5, correct the map's grading sentence.
>
> Two items raised in Macindoe's approving review of PR #3, both his own
> proposed fixes, applied here rather than carried to round 14:
>
> - h5 was accepted in round 12 but never applied: the L-A8 (d-bis) block
>   still carried the seed-dependent 200-draw control. The seed-free census
>   line (his wording, his figures) now replaces it; the superseded control
>   is kept visible rather than deleted, and the acceptance sentence now
>   records that an acceptance had been standing in for a discharge.
>
> - The campaign map's grading sentence said "verified cross-side this
>   round", which outran its own clock. Restated as "offered for cross-side
>   verification", with what his review actually returned written into the
>   section-96 block: p=7,k=8 confirmed a third time, p=3 small-k
>   non-reproduction carried open, and the four operational gaps recorded.
>
> The resolution of the p=3 question is verified on this side but is new
> material his review has not read, so it does not travel under this round's
> approval: it is round 14, with the artifacts, for his key.
>
> Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

### 1.4 `f336e57`'s diff of `LEDGER.md`, verbatim (`git show f336e57 -- LEDGER.md`, hunks only)

```diff
diff --git a/LEDGER.md b/LEDGER.md
index c3d274c..8af722a 100644
--- a/LEDGER.md
+++ b/LEDGER.md
@@ -448,7 +448,7 @@ The deficits, in the honest regime (offer h2). The `7159.5`-on-`k` / `2^38.4`-of
 
 Open for co-editing, and the wording of the grade line above is the part I would most like a second opinion on.
 
-**Merle — round-12 offers h1–h5 accepted (2026-08-17).** The second opinion arrived (Macindoe verification record below, 50 checks, 0 failures) and it found the grade line's *margin* overstated: `c* ≈ 0.9617` is the linear-form exponent (floor `c ≥ 1`), not a measure (floor `μ ≥ 2`), the two related by `μ = c + 1`, so in either single convention the route is shut by `≈ 0.038` — a razor, not the `≈ 1.04` the mixed pairing read as. Verified independently on my side: `c* = 0.9617` cannot be a measure (a measure is always `≥ 2`; `0.96` is meaningless), which settles the convention decisively. The impossibility conclusion is unchanged and strengthened. **h1** (single-convention headline), **h2** (dream deficits at the true regime), **h3** (Barina label), **h4** (α scope and the `>1/2` forever-threshold) are applied to the claim block above. **h5** (the seed-free census line) is accepted for the L-A8 (d-bis) block. Split grade as Macindoe turned it: the Dirichlet half toward two keys as unconditional theorem-grade, the scissors half permanently *measured* (proving `α > 1/3` is `μ ≤ 3`-hard). Second key: this round-13 pull request's review turns it, per PROTOCOL §13.
+**Merle — round-12 offers h1–h5 accepted (2026-08-17).** The second opinion arrived (Macindoe verification record below, 50 checks, 0 failures) and it found the grade line's *margin* overstated: `c* ≈ 0.9617` is the linear-form exponent (floor `c ≥ 1`), not a measure (floor `μ ≥ 2`), the two related by `μ = c + 1`, so in either single convention the route is shut by `≈ 0.038` — a razor, not the `≈ 1.04` the mixed pairing read as. Verified independently on my side: `c* = 0.9617` cannot be a measure (a measure is always `≥ 2`; `0.96` is meaningless), which settles the convention decisively. The impossibility conclusion is unchanged and strengthened. **h1** (single-convention headline), **h2** (dream deficits at the true regime), **h3** (Barina label), **h4** (α scope and the `>1/2` forever-threshold) are applied to the claim block above. **h5** (the seed-free census line) is **applied** to the L-A8 (d-bis) block, in the offer-g discharge paragraph below — accepted here on 2026-08-17 but not applied until 2026-09-03, when the round-13 review caught that the acceptance sentence was standing alone, pointing at a change never made. The gap is recorded rather than quietly closed: an acceptance is not a discharge, and this ledger had been reading one as the other for a round. Split grade as Macindoe turned it: the Dirichlet half toward two keys as unconditional theorem-grade, the scissors half permanently *measured* (proving `α > 1/3` is `μ ≤ 3`-hard). Second key: this round-13 pull request's review turns it, per PROTOCOL §13.
 
 ---
 
@@ -456,7 +456,7 @@ Open for co-editing, and the wording of the grade line above is the part I would
 
 - *(offer e — the two `q₂₁`.)* Discharged at [`7f20348`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean) — line 188's subscripts corrected to `q₂₂`/`q₂₃`, line 186's `δ` given its REQ-054 factor 2, and the header's withdrawn `4.955e10` named as withdrawn rather than replaced in silence. Subscripts pinned in-file to the `q₀ = q₁ = 1` convention. Comments only; the file was recompiled after the edit under the hardened four-check protocol — 0 errors, 0 stack overflow or abort, 0 `sorryAx`, fifteen theorems in the axiom log, kernel-3 throughout.
 - *(offer f — Cor. 29's `X₀ ≥ 3·2⁶⁹`.)* Still not landed in Lean, and its home is here rather than there. Recorded in this ledger now: **Hercher's Corollary 29 requires `X₀ ≥ 3·2⁶⁹ = 1536·2⁶⁰`**, against his Theorem 23's `704·2⁶⁰` and this note's own instantiation at `2048·2⁶⁰ = 2⁷¹`. `704 < 1536 < 2048`: the asymmetry runs in Hercher's favour on hypothesis and on conclusion alike.
-- *(offer g — the deleted `(d-bis)` table.)* Discharged, and the diagnosis was exactly right. The committed `test_REQ-MATH-052` is byte-identical between `41fa4f8` — the commit whose OUT file carried the table — and HEAD, same blob, one commit in its whole history: it never produced that section, at any commit. A generator is now committed, `experiments/test_REQ-MATH-052bis_ostrowski_grille.py`, reproducing the ten rows, the four figures this ledger cites, and the eps-small column with median 15601, under four canaries written before the run. **One column it does not recover and says so in its own header:** the control sample `[2,1,1,1,2,1,2,1,1,306]`, median 1, is not reconstructible from the output and its generator was never committed. The control is therefore re-specified at a fixed seed and declared as re-specified, with a 200-draw control added — median 2, maximum 53, and **0 of 200 reaching 306** — which is a stronger instrument than the original ten but is not the original ten. The sentence in the seed block above should be read accordingly: the eps-small side is recovered, the control side is re-derived.
+- *(offer g — the deleted `(d-bis)` table.)* Discharged, and the diagnosis was exactly right. The committed `test_REQ-MATH-052` is byte-identical between `41fa4f8` — the commit whose OUT file carried the table — and HEAD, same blob, one commit in its whole history: it never produced that section, at any commit. A generator is now committed, `experiments/test_REQ-MATH-052bis_ostrowski_grille.py`, reproducing the ten rows, the four figures this ledger cites, and the eps-small column with median 15601, under four canaries written before the run. **One column it does not recover and says so in its own header:** the control sample `[2,1,1,1,2,1,2,1,1,306]`, median 1, is not reconstructible from the output and its generator was never committed. The control is therefore **replaced rather than redrawn**, per offer h5 and in Macindoe's own wording and figures (his `merle_la9_check.py`): **among all 199,999 `n < 200000`, 897 (0.45%) have smallest Ostrowski denominator ≥ 306; all ten eps-small `n` do (median 15601 against a population median of 2)** — a seed-free census, strictly stronger than any drawn control, which retires the seed question instead of re-specifying it. *(Superseded, kept visible rather than deleted: the intermediate repair was a 200-draw control at a fixed seed — median 2, maximum 53, `0 of 200 reaching 306` — a stronger instrument than the original ten, but not the original ten, and still seed-dependent. Applied 2026-09-03; the acceptance sentence at the head of this section had accepted h5 without applying it, caught by the round-13 review.)* The sentence in the seed block above should be read accordingly: the eps-small side is recovered, the control side is now a census.
 - *(and one not offered, found while discharging the others.)* `test_REQ-MATH-067`, the source of the `0.00103` quoted in correspondence, computed the continued fraction of `log₂3` at `mp.dps = 400` and took 2000 partial quotients. At that precision the expansion **diverges from the true one at index 385**; 1615 of the 2000 terms were rounding noise. The correct value is **`0.00078`**. Macindoe's own three figures — largest bin deviation `0.008425`, his `χ²/N` over the complete partition `0.001214`, and `χ²/dof < 0.567` at every binning from 3 to 40 bins — reproduce exactly on the correct sequence and none on ours, where the maximum `χ²/dof` is `1.0504` and would have contradicted his bound. Fixed at `dps = 3000` with a canary that recomputes the whole sequence at double precision and refuses to proceed if one term moves. The substantive conclusion is unchanged and now rests on a correct sequence.
 
 ---
```

---

## 2. L-A10, keyed with fresh code (Queue 2)

Script: `experiments/merle_r14_check.py`, **46 checks, 0 failures**;
committed output `experiments/merle_r14_check_output.txt`, written by the
script itself, seeded (`20260904`), byte-identical on re-run. Imports nothing
of his and nothing of ours; the round-13 graph is re-implemented from its
recorded definition because it is one of the two objects compared in §2.3.
Exact integers at every pass/fail decision; mpmath at two precisions (30 and
50 digits, agreement asserted) only in the `θ`/drift recomputation of §7.

### 2.1 The two-line theorem (Queue 2a)

**The argument, in our own words, checked at each step.** `p − 2` is odd,
hence invertible mod `2^{k+1}`; `r_p := −(p−2)^{−1} mod 2^{k+1}` satisfies
`(p−2)·r_p ≡ −1 (mod 2^{k+1})` and is odd. For any positive `x ≡ r_p
(mod 2^{k+1})`: `x` is odd, so `T(x) = (px+1)/2`, and
`(p−2)x + 1 ≡ (p−2)r_p + 1 ≡ 0 (mod 2^{k+1})`, so `T(x) − x = ((p−2)x + 1)/2`
is an integer divisible by `2^k` — that is `T(x) ≡ x (mod 2^k)`, both `≡ u_p`; and
`(p−2)x + 1 > 0` since `p ≥ 3`, `x ≥ 1`, so `T(x) > x`. Same residue mod
`2^k` gives the same value `f(u_p) > 0`, and `V(T(x)) = T(x)·f(u_p) >
x·f(u_p) = V(x)`. This is exactly the ledger's proof; nothing was added and
nothing was needed.

**Keyed, exactly** (PART 1): on all **4,000** `(p,k)` pairs (`p = 3..201`
odd, 100 values; `k = 1..40`) the defining congruence `(p−2)·r_p + 1 ≡ 0
(mod 2^{k+1})` holds and `r_p` is odd; on **24,000** witnesses `x = r_p +
m·2^{k+1}` — six per pair, `m ∈ {0, 1, 2}` and three random `m` of 200, 400
and 600 bits (largest witness 641 bits) — `x ≡ T(x) ≡ u_p (mod 2^k)`,
`T(x) > x`, and `T(x) − x = ((p−2)x + 1)/2` exactly with an even numerator.
Zero failures on every property. (The main session's pre-check had 20,000
witnesses; his `run_050` P2 has 2,880; the three runs are independent code.)

At `p = 3`: `r_3 = 2^{k+1} − 1` and `u_3 = 2^k − 1` for every `k = 1..40`
(canary C8) — the ledger's "plainest object in the problem".

### 2.2 The concrete instances (Queue 2b)

All reproduce (PART 0, PART 2): `r_3 = 511`, `u_3 = 255` at `k = 8`;
`T(511) = 767`, `T(767) = 1151`, `1151 mod 256 = 127`; his P1 examples at
`k = 8` (`u = 255, 85, 51, 73, 199` for `p = 3, 5, 7, 9, 11`); his P5
trajectory `511 [255] → 767 [255] → 1151 [127] → 1727 [191] → 2591 [31] →
3887 [47] → 5831 [199]`, the class left at step 2 exactly; the ratio
`767/511 = 1.5010`; the accelerated map `255 ↦ 383 ≡ 127`; the half map's
lift `255 ↦ 383 ≡ 127` and lift `511 ↦ 767 ≡ 255`; `p = 1`: `T(511) = 256`,
`T(511) − 511 = −255`.

**The wording point, confirmed as the brief states it, and not a defect in
the claim.** The half-map relation on `ℤ/256` carries **both** edges from
`255`: `255 → 127` from the lift `255` and `255 → 255` from the lift `511`
(general fact, checked for `p = 3..11` odd and `k = 1..12`: the two successors
of an odd residue `u` from the lifts `u` and `u + 2^k` differ by exactly
`2^{k−1} mod 2^k`, since `T(u + 2^k) − T(u) = p·2^{k−1}` and `p` is odd). His
sentence "your map sends `255 → 127`, where ours has `255 → 255`" is true and
reads better as "ours *also* has `255 → 127`" — the diagnosis is precisely
that our graph kept one of the relation's two edges, which is what his own
"both lifts" description says. Carried into the review draft, kindly.

### 2.3 The divergence diagnosis, reconstructed on both objects (Queue 2c)

**The two objects, in words.**

- **Object A — what our round-13 reconstruction measured** (`merle_r13_check.py`
  PART 7, re-implemented in PART 3 from its recorded definition): the
  *accelerated* map `x ↦ (px+1)/2^v` on the odd residues mod `2^k` with *one*
  successor per residue, computed at the canonical representative `u ∈ [1,
  2^k)`: `u ↦ oddpart(pu+1) mod 2^k`, `v = v_2(pu+1)`. A functional graph;
  its cycles enumerated exactly; a cycle is faulty iff `p^L ≥ 2^K` (exact
  integer comparison); round 13 counted faulty cycles with `L > 1` only.
- **Object B — what §95–§96 and `run_049`/`run_050` measure** (his "run_049
  line 33", re-implemented from the definition alone): the Terras *half* map
  `T` on `ℤ/2^k` carrying *both* lifts from `ℤ/2^{k+1}` — one edge `(r mod
  2^k) → (T(r) mod 2^k)` for every `r ∈ [0, 2^{k+1})`. Well defined on
  `ℤ/2^{k+1}` on both branches; two out-edges per node; every edge realised by
  the entire progression `r + 2^{k+1}·ℤ`.

**At `p = 3, k = 8`** (PART 3a): the edge `255 → 255` is **present** in
Object B, realised by the lift `511` (and by every `x ≡ 511 (mod 512)`), and
**absent** from Object A, whose one edge from `255` goes to `127`; Object B
also carries `255 → 127` (lift `255`). Object B has exactly `512 = 2^9`
distinct edges, two out of every node, each realised by exactly one lift class
mod `512`; his `run_049` P1 reconstructed — 3 random positive lifts per edge,
1,536 in all, every one realises its edge — which, as §3.3 below says, can only
pass.

**Regression on Object A** (PART 3b): our round-13 committed figures
reproduce exactly — `p = 3`: no faulty cycle at `k = 4..9`; `(L,K) = (26,37)`
at `k = 10`; `(25,37)` at `k = 11`; `(6,7), (7,9)` at `k = 12`; none at
`k = 14, 16`; `p = 7, k = 8`: 4 residue cycles, lengths `[1, 3, 4, 31]`,
3 faulty at `(3,4), (4,8), (31,67)`. His `run_050` P4 table reproduces the
same figures, and this session additionally ran `k = 13` and `k = 15` for
`p = 3` (0 and 0), which our round-13 run had not measured and his table
added. The round-13 `L > 1` exclusion changes no count in any of these cases
— the fixed point `u = 1` has `v = 2` at `p = 3` (`3 < 4`) and `v = 3` at
`p = 7` (`7 < 8`), never faulty — so our figures and his all-cycles figures
agree for a reason, not by luck.

**Which lift carries the loop** (PART 3c) — a scope note, flat, not a
defect. The loop `u_p → u_p` of Object B sits on the lift `r_p`; it lies on
the `m = 1` lift exactly when `r_p ≥ 2^k`. For `p = 3` this is so at **every**
`k` (`r_3 = 2^{k+1} − 1`), and it is so at `(7, 8)` (`r_7 = 307`); so for the
two cases at issue his diagnosis — "the witness edge lives on the other
one" — is exactly right. It is not a universal statement: over the 4,000
pairs the loop sits on the `m = 0` lift in **2,163** of them, and for
`k ≥ 2` the loop is in Object A exactly when `r_p < 2^k`, where it appears as
an `L = 1` self-loop with `v = 1` — faulty, since `p ≥ 3 > 2`, and excluded by
round 13's `L > 1` convention (example: `p = 9, k = 8`, `r_9 = 73 < 256`,
Object A contains `73 → 73`). `k = 1` is degenerate (`ℤ/2` has one odd
residue; Object A is the single self-loop `1 → 1` for every `p`). Worth one
clause in the ledger entry if the sentence is to hold at every `(p, k)`; the
claim itself needs nothing from it.

**Which side measured what, in one sentence each.** Our round-13
reconstruction measured Object A — the accelerated map's residue graph with
the `m = 0` lift's edge only, which for `p = 3` at every `k ≥ 2` omits the
witness edge and therefore cannot show the loop; his §95–§96 measure Object
B, where the witness edge is present by construction of the relation. His
reading of our operational note 1 as the cause is confirmed.

### 2.4 The `p = 1` negative control (Queue 2d)

PART 4: `r_1 = u_1 = 1` at every `k` (`−(1−2)^{−1} ≡ 1`); on `x = 1 + 512m`
the identity `T(x) − x = ((p−2)x + 1)/2 = (1 − x)/2` still holds but is `≤ 0`
— `T(1) = 1`, `T(x) < x` for every other witness — so the inequality the
argument needs fails and it concludes nothing. And the family the theorem
closes at `p ≥ 3` is genuinely non-empty at `p = 1`: `V(x) = x` itself
(`f ≡ 1`) strictly decreases under `T` at every `x = 2..100000` (`T(1) = 1`
the lone fixed point). The control shows what a control should: the
conclusion is about `p`, not about the argument's form.

### 2.5 The "for every `f`" quantifier (Queue 2e)

Confirmed: the argument consumes exactly two properties of `f` — it is a
function of `x mod 2^k` (so `f(x mod 2^k) = f(T(x) mod 2^k) = f(u_p)` at the
witness) and it is positive (so `T(x) > x` multiplies through) — and nothing
else: no continuity, no monotonicity, no size. Tested in exact rationals at
ten witnesses `x = 511 + 512m` against 23 altitudes — constant `1`, `2^{−u}`
(tiny at 255), `2^u` (huge at 255), and 20 random rational `f` with values
spanning `10^{−30}..10^{30}` — 230 evaluations, `V(T(x)) > V(x)` every time.
The one thing the level-`k` witness does *not* survive is an `f` reading one
more bit (`x mod 2^{k+1}`): `511` and `767 ≡ 255 (mod 512)` no longer share
a residue — but that is a different `k`, and the level-9 witness `r_3 =
1023` serves (`T(1023) = 1535 ≡ 511 ≡ 1023 (mod 512)`, `1535 > 1023`), which
is what "every fixed `k`" means.

### 2.6 Scope (Queue 2f)

**One sentence, as the brief asks:** the argument exhibits a single edge
`x → T(x)` along which any altitude of the family rises, and bears on no
cycle and on no integer orbit beyond that edge — the witness `511` lies on no
cycle (its `T`-orbit reaches `1` in 41 half-map steps, a single trajectory
computed, not a search), the class is left at step 2, and the entry's "it
excludes no cycle" is exactly right. The cycles front stays PARKED; nothing
in this window computed anything per period or searched for a cycle.

---

## 3. His artifacts at `db0e89d`, read and run (Queue 3)

**Environment.** Python **3.10.6** (Windows, this machine), run from the
Lean-repo clone's root with stdout redirected to scratchpad files; **no
environment fix was needed and none of his files was edited** (`git status`
in the clone clean after the runs). His committed outputs carry Python 3.11+
signatures (the traceback caret line in `run_048_output.txt`).

### 3.1 `run_050.py` — byte-identical

`python experiments/run_050.py` exits 0 and its output is **byte-identical**
to the committed `run_050_output.txt` (`diff` empty): the five canaries, P1
(4000 pairs), P2 (2880 witnesses; `511 → 767`, ratio `1.5010`), P3, the P4
table (`p = 3, k = 4..16`: `0,0,0,0,0,0,1,1,2,0,0,0,0`; `p = 7, k = 8`: 3 at
`(3,4), (4,8), (31,67)`; `u = 255 → 127` in the accelerated graph), P5 (the
trajectory, class left at step 2), P6 — "14 checks" as the PR body says
(the script counts 5 canaries + 9 checks). Every P4 figure agrees with this
session's own Object A (§2.3) and every P1/P2/P5 figure with PART 0–2.

### 3.2 `run_048.py` — halts on its own canary, exactly as he says

`python experiments/run_048.py` exits **1**: canaries C1, C2, C4 `PASS`, **C3
`FAIL 2`** (the word `[1,0]` returns `2` where `1` is expected), then
`AssertionError: canaris en echec` at line 125. Its committed
`run_048_output.txt` shows the same, differing only in the traceback's file
path (his local `/Users/ericmerle/...`, this session's scratchpad path) and
in Python 3.11's caret line under the assert, which 3.10 does not print.
**Not fixed, not rescued**, per the brief: the retraction is his and the
record is that the file fails on its own canary. P3/P4/P5 of this file were
never produced, as the retraction header says.

**The retraction header, verbatim** (`run_048.py` lines 2–33 at `db0e89d`):

```
# ⚠️  RETRACTATION PARTIELLE (2026-09-03) — LIRE AVANT DE CITER QUOI QUE CE SOIT D'ICI.
#
# Ce fichier est conserve EXACTEMENT tel qu'il etait ecrit ; rien n'est supprime ni corrige.
# Deux defauts, trouves en le RE-EXECUTANT pour la livraison du round 14 a B. Macindoe :
#
#  R1. LE SCRIPT NE S'EXECUTE PAS. Son propre canari C3 echoue et l'assert ligne 93 l'arrete.
#      Cause : `rationnel` parcourt le mot A L'ENVERS (`reversed(bits)`, ligne 76) la ou la
#      version de run_049 le parcourt a l'endroit ; sur le mot [1,0] il rend 2 au lieu de 1.
#      CONSEQUENCE : les sorties P3, P4 et P5 de ce fichier N'ONT JAMAIS ETE PRODUITES.
#      Le canari a fait son travail — c'est le rapport qui a suivi qui ne l'a pas ecoute.
#
#  R2. LE BUG CORRIGE (un mot : `reversed(bits)` -> `bits`), le script echoue alors son
#      PROPRE CONTROLE P5 : il sort x = -6, qui n'est sur aucun cycle (T: -6, -3, -4, -2, -1).
#      Cause : il resout l'equation lineaire du mot sans verifier que les PARITES de la
#      trajectoire suivent effectivement ce mot. Son recensement compte donc des solutions
#      formelles, pas des cycles.
#      => LE RECENSEMENT DE FANTOMES DE CE FICHIER EST RETIRE EN ENTIER. En particulier le
#      chiffre "100 % de fantomes parmi les cycles fautifs a p=7, k=8", cite dans la
#      correspondance (round 13, §6) et dans briefs/merle-breach-campaign-map.md, N'A PAS
#      D'ARTEFACT DERRIERE LUI : ce fichier ne teste jamais p=7, et son recensement est faux
#      deux fois. Le chiffre est retire, pas corrige.
#
# CE QUI SURVIT, ET QUI EST L'ESSENTIEL : P1 et P2 (la boucle du §95, x = 1/(2-p), entiere
# pour p=3 seulement) n'utilisent que des mots d'UNE lettre, ou l'ordre de parcours est sans
# effet — canaris C1, C2, C4 verts. Ce resultat tient.
#
# ET LA CONCLUSION DU §96 NE DEPEND PAS DU RECENSEMENT : run_049 (P1, 20 000 aretes) etablit
# que la qualite de "fantome" est SANS OBJET, puisque chaque ARETE est realisee par de vrais
# entiers. Le recensement etait la question posee, pas la reponse retenue.
# Reprise exacte et complete : run_050.py.
```

Two flat observations, consistent with the header, from reading the file
(not from running past the canary): the file's `tous_cycles_fautifs` loops
over `p in (3, 5)` and `k in (6, 8, 10)` only — it indeed never tests
`p = 7`; and the header's "assert ligne 93" is the assert at line 125 of the
committed file, the 32-line retraction header having shifted the line numbers
of the file it describes. Immaterial.

### 3.3 `run_049.py` — reproduces, with one platform-dependent count

`python experiments/run_049.py` exits 0; output identical to the committed
`run_049_output.txt` **except one line**: P3's `entiers testes : 40000 | V ne
decroit PAS : 17002` prints **`15396`** here. Everything else is
byte-identical — the four canaries, P1's `20 000 aretes ... PASS`, P2's
"insatisfiable / toujours insatisfiable" at `p = 7, k = 8`, P3's `retrait
GLOUTON de 63 restes : satisfiable`, its counterexample `x=2, T(x)=1,
V(x)=0.0007105, V(T(x))=0.0007105`, its verdict, and P4. **Reading, offered
kindly and not asserted:** P3 builds `g` by floating-point Bellman–Ford
(tolerance `1e−12`) and then tests `V(y) >= V(x)` with `V = x·exp(g[x mod
M])` under a *strict* comparison; the edges that saturate a constraint give
`V(y) = V(x)` up to rounding (the printed counterexample is one: both values
`0.0007105`), and how many of the 40,000 land on either side of equality
depends on the last bits of `log`/`exp` — platform libm and Python version.
The count is a float-tie count; the conclusion ("the filtered `f` does not
decrease `V` on real integers", counterexample exhibited) is identical here.
**Not a number L-A10 rests on**, and not one the ledger quotes.

**P1's "20,000 edges, all realised" — why it is automatic, kindly.** On
Object B every edge *is* a lift class: the edge from `r ∈ [0, 2^{k+1})` is
defined as `(r mod 2^k) → (T(r) mod 2^k)`, and every integer `x ≡ r (mod
2^{k+1})` satisfies `x mod 2^k = r mod 2^k` and `T(x) mod 2^k = T(r) mod 2^k`
(both branches, checked algebraically in PART 3's preamble and on 1,536
random lifts). So "realised by a real integer" holds by construction of the
relation, and the 20,000-edge check can only pass — it confirms that the
graph was built as described (a consistency check), and it is not a finding
about the dynamics. The *substantive* content of §96's P1 is the sentence
before the count: a constraint on `g` is legitimate whether or not any
integer closes a cycle, because it is imposed edge by edge, and each edge has
integers behind it. That sentence is right, and L-A10 uses it in its
sharpest form (one edge, no cycle). The entry's provenance line "established
in `run_049` P1 (20,000 edges, all realised)" could say "by construction of
the relation" instead of citing the count; offered as a wording note in the
review, one sentence, not a defect.

---

## 4. The h5 application at `f336e57` (Queue 4)

**Confirmed applied, in our wording and figures, with the superseded control
kept visible.** The L-A8 `(d-bis)` block on `main` (`LEDGER.md` line 459 at
`93c6ac4`; the diff is §1.4 above) now reads, at the point offer h5 was
drafted to replace:

> The control is therefore **replaced rather than redrawn**, per offer h5 and in Macindoe's own wording and figures (his `merle_la9_check.py`): **among all 199,999 `n < 200000`, 897 (0.45%) have smallest Ostrowski denominator ≥ 306; all ten eps-small `n` do (median 15601 against a population median of 2)** — a seed-free census, strictly stronger than any drawn control, which retires the seed question instead of re-specifying it. *(Superseded, kept visible rather than deleted: the intermediate repair was a 200-draw control at a fixed seed — median 2, maximum 53, `0 of 200 reaching 306` — a stronger instrument than the original ten, but not the original ten, and still seed-dependent. Applied 2026-09-03; the acceptance sentence at the head of this section had accepted h5 without applying it, caught by the round-13 review.)*

Against offer h5's text (`briefs/merle-la9-check-findings.md` §6.4): "among
all 199,999 `n < 200000`, 897 (0.45%) have smallest Ostrowski denominator
≥ 306; all ten eps-small `n` do (median 15601 against a population median of
2)" — **word for word, figures identical** (`199,999`, `897`, `0.45%`, `306`,
`15601`, `2`). Against round-13 findings §3: the disposition recommended
there ("raise it plainly in the review as an open item for him to apply
before merge — his own text, already agreed, a one-line change") is what
happened, in his pre-merge commit, and the superseded sentence the round-13
findings quoted ("0 of 200 reaching 306") is preserved inside the
parenthetical rather than deleted. The L-A9 acceptance sentence (line 451)
now records the acceptance-standing-in-for-a-discharge gap in its own words.
**The L-A8 ledger line in HANDOFF changes from "accepted but not yet applied"
to closed** (done, §9.2).

---

## 5. The campaign-map edits (Queue 5)

Read at `2f7b865` against `93c6ac4` (both quoted in full in the session; the
diff is §1.2).

- **The "Withdrawn (2026-09-03)" block: additive and accurate.** It is a new
  blockquote (`+`-lines only). Its description of the previous ⊢ paragraph
  is accurate against that paragraph's actual text at `93c6ac4`: it "ran the
  argument through a census" (the old text: `g = log f` telescoping, "phantoms",
  "100% of the faulty cycles at `p=7,k=8`"), it "said 'the accelerated map'"
  (old text: "under the accelerated map on all integers"), and the 20,000-edge
  sentence is carried over. One flat clause for the record, not a defect: the
  ⊢ paragraph itself was rewritten in place (the map's 17 deletions are all
  inside that paragraph and the cross-side paragraph), so the old wording
  survives in git at `93c6ac4`/`f336e57` and in the block's summary, not as
  struck-through text on the page — a lighter pattern than the Rhin
  retraction's strikethrough-in-place, appropriate to a curated digest; the
  ledger entry itself is purely additive (`+38/−0`), which is where "nothing
  removed" matters.
- **The rewritten ⊢ item against L-A10.** Where it quotes the entry it
  matches word for word: `r_p = −(p−2)^{−1} mod 2^{k+1}` and `u_p = r_p mod
  2^k`; `x ≡ T(x) ≡ u_p (mod 2^k)`; `u_p = 2^k − 1`; `511 → 767` at `k = 8`,
  both `≡ 255 (mod 256)`; "`ℤ/2^k` does not distinguish `2^k − 1` from `−1`,
  and `−1` is a genuine fixed point of `3x+1`"; the `k`-growing escape as
  "prose, not an artifact". Where it paraphrases (`T(x) > x` "whenever
  `p > 2`" for the entry's `T(x) − x = ((p−2)x + 1)/2 > 0`) it is correct.
  The map's object is now "the Terras half map `T`" on "the positive
  integers", matching the entry's claim.
- **The cross-side paragraph against our round-13 findings §6** — accurate.
  Our own sentences, quoted: "**Reproduces cleanly at `p=7, k=8`** ... 4
  distinct residue cycles ..., lengths `1, 3, 4, 31`; 3 faulty (`K=67` vs
  `p^L≈1.58·10²⁶` at `L=31`; `K=8` vs `2401` at `L=4`; `K=4` vs `343` at
  `L=3`). A genuine-closed-orbit search ... up to `x0 < 500,000–770,000` per
  cycle finds **none beyond the trivial fixed point `x=1`** — **100% phantom,
  matching the campaign map's own figure.**" and "**Does NOT reproduce at
  small `k` for `p=3`.** No faulty cycles exist at all for `k=4..9` ... Faulty
  cycles first appear at `k=10` (one cycle, `L=26`), persist at `k=11,12`, then
  **vanish again** at `k=14, 16`". The map's "4 residue cycles, 3 faulty, at
  `(L,K) = (3,4), (4,8), (31,67)`" and its "no faulty cycle for `k = 4..9`,
  one at `k = 10` and `k = 11`, two at `k = 12`" match. Its "**that figure is
  yours, on your object, and this side has not reproduced it**" is the right
  disambiguation of our bounded-search "100 % phantom": that figure is ours,
  on Object A, relative to its bound — and, now that his census is withdrawn,
  our round-13 sentence's "matching the campaign map's own figure" compares
  against a number that no longer exists on his side; our figure stands as a
  bounded measurement on our object and nothing more (carried into the review
  and HANDOFF). Two small flat notes: (i) "none again at `k = 13..16` ...
  reproduced here exactly" — our round-13 run measured `k = 14` and `16`, not
  `13` and `15`; those two are his additions (his P4 table), and this
  session's PART 3 confirms them (0 and 0); (ii) the grading header's clause
  "including one genuine counter-finding, carried open on this round's
  record" is unchanged from `f336e57` while the ⊢ block below now says
  "Settled in round 14" — a stale clause, not a presupposition; optional
  wording ("carried open on round 13's record and settled in round 14's").
- **Presupposition check.** No sentence presupposes a key this PR has not
  supplied: the header still reads "Everything here is **Merle-side, one
  key**" and "**offered for cross-side verification**"; the ⊢ item points to
  L-A10 "seeded at one key for yours"; the cross-side paragraph's "Settled in
  round 14, and in your favour" claims his reproduction of our figures and his
  diagnosis, both of which this session has now verified, and does not claim
  our key. The round-13 grading-tension pattern does not recur.

---

## 6. The Rhin locatability, at its address (Queue 6)

Fresh clone of `ericmerle3789/Collatz-Junction-Theorem`: **`8bcee67` is the
tip of `main`** (parent `a57d29e`, the archive notice; author `Eric MERLE`,
`Thu Sep 3 19:02:39 2026 +0200`); `git show --numstat 8bcee67` reports
**`10 0 README.md`** — ten lines added, none removed, one file; the diff is
a single hunk inserting a blockquote block after the "Active repo" line,
i.e. at the head of the README, before the "Logical status" section.
**Additive: confirmed by the diff, not by the commit message.** The
retraction commit `77e3f07` remains on `proof-assembly-v1` only (`git branch
-a --contains 77e3f07` lists only that branch), as the new block says.

**The README block, verbatim** (the ten added lines at `8bcee67`):

> ## ⚠️ Retraction (2026-08-17) — it is NOT on this branch, read this before citing `BILAN_R201.md`
>
> The verdict **R201-I3** in `research_log/BILAN_R201.md` — *"C′ ~ 13.3 misattributed to Rhin 1987"*, marked **PROUVÉ** — is **false, and its premise is false. It has been retracted.**
>
> This archived `main` **predates the retraction and does not contain it.** The retraction is committed on branch `proof-assembly-v1` at [`77e3f07`](https://github.com/ericmerle3789/Collatz-Junction-Theorem/blob/proof-assembly-v1/research_log/BILAN_R201.md) — nothing was deleted there, every retracted assertion is struck through and stamped in place.
>
> **What is actually true.** Rhin 1987 (*Progress in Mathematics* 71, Proposition p. 160) proves **both** irrationality measures **and** an effective linear-independence measure of `1, log 2, log 3`, giving `|u₀ + u₁·log 2 + u₂·log 3| > H^(−13.3)`. The 13.3 stands for what the L-A7 chain consumes; the replacement constants the retracted verdict proposed (Laurent 2008 ≈ 18.5, LMN 1995 ≈ 23.55) are coefficients of a differently-shaped bound. What was real in the trigger: R200's own transcription had written Rhin's constant into that other shape — the defect was the transcription, not the attribution.
>
> Cross-adjudicated in the shared repository [`macindoe/one-obstruction-three-faces`](https://github.com/macindoe/one-obstruction-three-faces), `LEDGER.md` entry **L-A7**, verified on both sides. Branch locatability flagged by B. Macindoe, round-13 review, 2026-09-03.

The mechanism it states matches `briefs/merle-la7-rhin-check-findings.md` §3
and the retraction text archived in the round-13 findings §4, sentence for
sentence. **This closes the round-13 locatability note**; the HANDOFF L-A7
line carries it (§9.2).

---

## 7. The smaller letter items, recomputed (Queue 7)

- **`θ = 1`** (PART 5): `f(1) = 3/2 + 1/2 − 2 = 0` exactly as a `Fraction`
  at `p = 3` (and `= 1, 2` at `p = 5, 7`); `f'(0) = ln(p/2) + ln(1/2) =
  ln(p/4)`, agreeing at 30 and 50 digits: `−0.287682` (`p = 3`), **`+0.223144
  → +0.2231`** (`p = 5`), **`+0.559616 → +0.5596`** (`p = 7`); scan of
  `θ = 0.001, 0.002, …, 50.000` at 50 digits: `f(θ) > 0` throughout at
  `p = 5, 7` — no sign change, no positive root on `(0, 50]`; at `p = 3`
  bisection on the dip returns `θ = 1` to 40 digits. **Drift** `½(ln(p/2) +
  ln(1/2)) = ½·ln(p/4)`: **`−0.143841 → −0.1438`** (`p = 3`), **`+0.111572 →
  +0.1116`** (`p = 5`), and it equals `f'(0)/2` identically. All four of his
  adopted figures match.
- **Peak: our wording is what he adopted.** Ours (round-13 findings §5.2,
  the verdict): "**Clustering: a clean non-finding.** `log₂3` (`0.8314`) sits
  inside the 6-constant min-max band (`[0.6456, 1.2214]`) and is rank 4 of 7"
  and "**Spectral: genuinely marginal, reported flat rather than forced
  either way.** `log₂3` is the single *highest* of the 7 exchangeable values
  (rank 1; one-sided `p = 1/7 ≈ 0.143` ...)". His (R14 §4): "I adopt your
  wording as the record, both readings as you stated them: **clustering, a
  clean non-finding that survives the corrected footing** (rank 4 of 7, inside
  `[0.646, 1.221]`); **spectral, genuinely marginal and reported flat** (rank
  1 of 7, one-sided `p ≈ 0.14`, nowhere near the positive control). Not forced
  either way, exactly as you wrote it." Same readings, same ranks, same band
  (rounded to three places), same `p`. His withdrawal of `5.62× @ f=124` "as a
  recoverable claim" matches our round-13 estimator note. No ledger text for
  the item appears in PR #4 (the LEDGER diff is L-A10 only); the adoption is
  in the letter.
- **h4** (PART 5): the strings `full chord alpha over [2^71, 2^2000] =
  0.5001`, `width   30 bits: min 0.3229` and `width  400 bits: min 0.4867`
  are literally present in `experiments/merle_la9_check_output.txt` PART 3,
  and `1/0.4867 = 2.05` — the three numbers his §6 records as our script's
  own output, returned through his co-edit. Confirmed, as round-13 findings
  §2.1 established.

---

## 8. The wiki pointer (Queue 8) — added, gated wording

L-A10 verifies (§2), so one calibration sentence was added at
`open-problems.md` 11.6, after the 2026-07-16 calibration paragraph, in the
wiki's standing credit form (cycles.md 12.6.1.1–12.6.1.4: name, correspondence
date, his artifact commit, the shared-ledger entry, our verification line,
the "excludes nothing" calibration):

> **Calibration (2026-09-04, shared ledger L-A10).** No altitude of the form `x·f(x mod 2^k)` — `k` fixed, `f` any positive function on `ℤ/2^k` — descends at every step of the Terras half map on the positive integers, for any odd multiplier `p ≥ 3`: Eric Merle's shared-ledger entry L-A10 (correspondence 2026-09-03; his artifact `experiments/run_050.py` at `ericmerle3789/one-obstruction-three-faces-lean` `db0e89d`; `github.com/macindoe/one-obstruction-three-faces`, `LEDGER.md`), one key his and two keys once the round-14 review is posted — verified here with fresh code (`experiments/merle_r14_check.py`, 46 checks, 0 failures, 2026-09-04); it excludes no cycle and closes nothing on this page beyond naming one more finite-state shadow that cannot carry a descent certificate.

Nothing else on the page moved except the front-matter `updated:` date
(`2026-08-03 → 2026-09-04`), per AGENTS.md's front-matter rule. The sentence's
key-status clause reads "two keys once the round-14 review is posted"; if the
author decides not to post, the clause needs one edit or the commit is
dropped — recorded so the main session can act on it at merge.

---

## 9. The round's paperwork (Queue 9)

### 9.1 The review draft

*(Full text, for the author to post as PR #4's approving review, verbatim or
edited. Register mirrors round 13's §7.1: verified-independently facts first,
then the keys the review turns, then the raised items. Nothing posted by this
session.)*

> Second key — approving review (round 14, per PROTOCOL §13).
>
> Verified independently on my side, fresh code (`experiments/merle_r14_check.py`, 46 checks, 0 failures; imports nothing of yours; exact integers at every decision):
>
> **§1–§2 (L-A10).** CONFIRMED. `r_p` odd and `(p−2)·r_p + 1 ≡ 0 (mod 2^{k+1})` on all 4,000 `(p,k)` pairs (`p = 3..201` odd, `k = 1..40`); on 24,000 witnesses `x = r_p + m·2^{k+1}` — six per pair, three of them with `m` of 200–600 bits — `x ≡ T(x) ≡ u_p (mod 2^k)`, `T(x) > x`, and `T(x) − x = ((p−2)x + 1)/2` exact with an even numerator. The quantifier is genuinely "every `f`": the proof consumes only `f(u_p) = f(u_p)` and `f(u_p) > 0`, checked in exact rationals against 23 altitudes including 20 random `f` with values spanning `10^{−30}..10^{30}`. The `p = 1` control reproduces — `r_1 = u_1 = 1`, the identity keeps its form and flips sign — and one thing more a control should show: at `p = 1` the family is non-empty (`V(x) = x` itself descends at every `x = 2..100000`), so the conclusion is about `p`, not about the argument's shape. Scope as you set it: one edge, no cycle, no orbit (511's orbit reaches 1 in 41 half-map steps); nothing formalised; excludes no cycle. **The second key turns on L-A10.**
>
> **§1 (the `p = 3` resolution).** CONFIRMED, both objects rebuilt from their definitions. The half-map relation on `ℤ/256` carries `255 → 255` via the lift 511; the accelerated single-successor graph does not (its one edge from 255 goes to 127); our round-13 `p = 3` and `p = 7` figures reproduce on our object exactly as you reproduced them — including `k = 13, 15`, which we had not run and your P4 table added. Your reading of our operational note 1 as the cause is right. Two flat notes, neither a defect. (i) The relation carries *both* edges from 255 — `255 → 127` from the lift 255 as well as `255 → 255` from 511 — so "your map sends `255 → 127` where ours has `255 → 255`" reads better as "ours *also* has": the diagnosis is exactly that our graph kept one of your two edges. (ii) "The witness edge lives on the other lift" is exactly right for `p = 3` at every `k` (`r_3 = 2^{k+1} − 1`) and for `(7, 8)` (`r_7 = 307`), and is not universal: over the 4,000 pairs the loop sits on the `m = 0` lift in 2,163 of them (e.g. `p = 9, k = 8`, `r_9 = 73`), where the single-successor graph *does* contain it, as a faulty `L = 1` self-loop that our round-13 convention then excluded as trivial. One clause in the entry if you want the sentence to hold at every `(p,k)`; the claim needs nothing from it.
>
> **§3 (the two retractions).** Read and confirmed at `db0e89d`. `run_048.py` run as committed halts on its own canary C3 exactly as your committed output shows (my differences: the traceback path, and 3.11's caret line — I am on 3.10.6); the census is withdrawn, and I note in the same breath that our own round-13 "100 % phantom" is ours, on our object, under a bounded search, and no longer matches anything of yours — it stands as a bounded measurement and nothing more. The "climbs forever" formulation: `511 → 767 → 1151`, `1151 ≡ 127`, the class left at step 2 — confirmed. Nothing in L-A10 touched either.
>
> **Artifacts.** `run_050.py` runs as committed with byte-identical output (Python 3.10.6, Windows, no environment fix). `run_049.py`: byte-identical except one line — P3's "V ne decroit PAS : 17002" prints 15396 here; the counterexample (`x = 2`), the greedy count (63 residues) and the verdict are identical, so this reads as a float-tie count under a different libm/Python (saturated constraints give `V(y) = V(x)` to rounding, and the test is a strict comparison) — not substance, and not a number the entry rests on. One wording note on `run_049` P1, kindly: on the both-lifts relation every edge *is* a lift class, so realisability holds by construction and "20,000 edges, all realised" can only pass — a consistency check of the graph rather than a finding. The entry's provenance line might say "by construction of the relation" instead of citing the count; the sentence before the count (a constraint is legitimate edge by edge, whether or not any integer closes a cycle) is the substantive one and is right.
>
> **§4 (peak).** Your adoption is our wording, both readings, same ranks, same band; the `5.62× @ f=124` withdrawal recorded. The item closes in our round-13 wording, as you adopted it.
>
> **§5 (`θ = 1`).** Recomputed: `f(1) = 0` exactly at `p = 3`; `f'(0) = ln(p/4) = +0.2231, +0.5596`; no positive root on `(0, 50]` at `p = 5, 7`; drift `−0.1438`, `+0.1116` (and the drift is `f'(0)/2` identically). Matches.
>
> **§6 (the three carries).** h5 confirmed applied at `f336e57` in our wording and figures, the superseded control kept visible — L-A8 closes. h4 provenance recorded, matches our `merle_la9_check_output.txt` PART 3. Rhin: `8bcee67` on `main`, the block at the README head, `+10/−0` by its diff — the locatability item closes.
>
> **The map.** The withdrawn block is additive and accurate against the paragraph it replaces; the ⊢ item matches L-A10 wherever it quotes it; the cross-side paragraph describes our round-13 figures correctly, and "yours, on your object" is the right disambiguation of our bounded search. Nothing presupposes a key this PR had not yet supplied. Two clauses you may want, neither blocking: "none again at `k = 13..16` … reproduced here exactly" — we reported 14 and 16; 13 and 15 are your additions, now confirmed here too; and the header's "carried open on this round's record" now sits above a block that says "Settled in round 14".
>
> **§7.** Placement stands as set; nothing to re-decide.
>
> Diff is three files, `+208/−17`, the deletions all inside the map's two rewritten paragraphs with the old text summarised in the withdrawn block and preserved in git; the ledger entry itself purely additive. Approving.

### 9.2 HANDOFF item 1

Rewritten on this branch — see the diff to `HANDOFF.md`. What moved, in
summary: the live-conditions paragraph now records PR #3 merged by Merle
2026-09-03 (`95e7212`) after his pre-merge `f336e57` applying h5; the bracket
patch on `main` at `93c6ac4` (the "pending push" sentence deleted); PR #4 open
at `2f7b865` with our key pending the author's posting of the review at §9.1
above; the two retractions with the nuance that our round-13 figure is ours
on our object; his spectral figure withdrawn; the round-13 locatability item
closed at `8bcee67`; the wiki pointer at `open-problems.md` 11.6 and its gated
clause. The "Repos, current values" paragraph carries shared HEAD `93c6ac4`
with the four branches, Lean HEAD `db0e89d`, Junction `main` at `8bcee67`
with `77e3f07` on `proof-assembly-v1`. The ledger-state list: L-A7's line
carries the locatability closure; L-A8 closed with h5 applied at `f336e57`;
a new **L-A10** line (one key his; ours turns with the posted review). The
standing-conventions paragraph records that the author's next mail carries
the dictionary paragraph (`briefs/literature-dictionary-findings.md` §6) as
mail, not PR business. The Pointers paragraph gains the 11.6 location.
Item 4 and everything else in the file untouched.

---

## 10. Compliance

- File edits via the Edit/Write tools only, in this repository; no PowerShell
  `Get-Content`/`Set-Content` touched any file. The committed script output
  is written by the script itself (`Tee` to `merle_r14_check_output.txt`),
  not by shell redirection.
- Read-only everywhere outside this repository: three fresh clones in the
  scratchpad, `gh pr view`/`gh pr diff` reads only; his artifacts were run
  from the Lean clone with output redirected to the scratchpad, none of his
  files edited (clone `git status` clean afterward); no push, fork, issue,
  star, watch, comment, review, reaction, or contact with anyone, anywhere.
- No key turned: the review draft (§9.1) recommends turning the second key
  on L-A10 and the recommendation is the author's to act on; the wiki
  sentence (§8) is phrased on that condition and is revertible in one edit.
- No proof attempt, no cycle search, no per-period computation. The one
  orbit computed (511's, 41 steps to 1) is a single trajectory used to state
  scope. Cycles front PARKED throughout.
- Commits: one per deliverable — the script in three per-part commits
  (Parts 0–2, Part 3, Parts 4–5), this findings file, the wiki pointer, the
  HANDOFF rewrite, and the final commit recording the encoding scan. One
  message-only amend on the Parts 4–5 commit (its message said 45 checks
  where the script's TOTAL is 46), on an unpushed local commit, recorded
  here. Every message ends with the required trailer.
- `experiments/encoding_scan.py`: run over the tracked tree with every edit
  of this window in place, and again immediately before the final commit —
  **RESULT: CLEAN** (0 invalid UTF-8, 0 BOM, 0 double-encoding signatures).
