# Findings: the Rhin 13.3 re-source warning, adjudicated (merle-la7-rhin-check)

Delegated session, 2026-07-30. Brief: `briefs/merle-la7-rhin-check-brief.md` (commit `9d9d1ec`).
Branch `merle-la7-rhin-check`, base SHA **`9d9d1ec`** — launch note, for the record: the worktree
was cut at the stale `3eab8f1`; `git merge main` fast-forwarded to `9d9d1ec` (which contains the
brief) before any work started, per the launch instruction. Register: flat; his artifacts quoted,
never paraphrased where the wording is load-bearing.

**Access record.** Both Merle-side repos cloned fresh, read-only, into the session scratchpad
(`Collatz-Junction-Theorem` HEAD `a57d29e`, the archived state; his Lean repo
`one-obstruction-three-faces-lean` HEAD `d48ba9e`, the round-12 pin). No fork, no issue, no
comment, no push, no write of any kind against any repository of his; no contact with anyone. Web
used for item 2 only (primary literature: the Simons–de Weger 2005 PDF from the publisher's own
file via an archive snapshot; Wu 2003 from the AMS published PDF; Laurent 2008 from the
publisher's file via an archive snapshot; the zbMATH review of Rhin 1987; arXiv:2205.10582).
**Stopping-rule compliance:** a literature adjudication on a closed entry's ingredient — no proof
effort, no cycle search; the cycles front stays PARKED.

**Verdict in one line: grade (a) — 13.3 CONFIRMED for what the chain consumes; the BILAN is
wrong, and its error has an identifiable, honorable mechanism (it caught a real transcription
defect in his own R200 and filed it under the wrong statute). No printed number of ours or of the
ledger's moves. Item 4 does not trigger; no script exists because nothing needed computing.**

## 1. His two artifacts, verbatim, and where they collide

### 1(a) `research_log/BILAN_R201.md` (`Collatz-Junction-Theorem`, committed `6d30395`, 2026-03-16)

Commit: `6d30395`, 2026-03-16 23:20:41 +0100, message "R201: Baker+decay audit — SAME path as
R194 (4/10), C'~13.3 misattributed, CF alternative (7/10)". The file is an audit round of his own
R200 proposal (Baker + exponential decay applied to `Λ = S·log 2 − k·log 3`). The
PROVED-misattributed block, in full (§ "AGENT A1", lines 22–26):

> ### C' ~ 13.3 : MAL ATTRIBUÉ
> - **Rhin (1987)** traite des mesures d'irrationalité de log 2, pas des formes linéaires en 2 logarithmes
> - **Laurent (2008)** : C' ~ 18.5 pour 2 logarithmes
> - **LMN (1995)** : C' ~ 23.55 (conservatif)
> - Pas Rhin → pas 13.3

and the formal-results table rows that carry the grades (lines 37–42):

> | R201-I3 | C' ~ 13.3 MAL ATTRIBUÉ à Rhin 1987 (mesure d'irrationalité ≠ forme linéaire) | **PROUVÉ** |
> | R201-I4 | Vraie constante C' ~ 18.5 (Laurent 2008) ou ~23.55 (LMN 1995) | **OBSERVATION** |

(Note the grades: only the misattribution claim I3 is marked PROUVÉ; the Laurent/LMN replacement
values I4 are marked OBSERVATION. The synthesis table repeats "C' ~ 13.3 mal attribué à Rhin —
**PROUVÉ** — Constante réelle : 18.5–23.55", and the closing line repeats "C'~13.3 MAL ATTRIBUÉ
(Rhin ≠ formes linéaires)".)

**The upstream artifact the audit was auditing** — this is the mechanism, see §3 —
`research_log/R200_red_team_cancellation.md` (same repo), §7.2, verbatim:

> - Rhin (1987): |S*log2 - k*log3| > exp(-13.3 * (log S)^2) for S, k >= 2.
> - Laurent, Mignotte, Nesterenko (1995): improved for two logarithms.
> - Matveev (2000): general n logarithms, but not optimal for n = 2.
>
> With Rhin's C' ~ 13.3, K_0 ~ 1,500 (rough estimate).

The `exp(−13.3·(log S)²)` — **log squared** — is not Rhin's statement form (see §2); it is the
shape of the LMN/Laurent instrument with Rhin's constant transplanted into it.

### 1(b) `experiments/test_REQ-MATH-035*` (his Lean repo, committed `9096d7f`, 2026-07-25)

Commit: `9096d7f`, 2026-07-25 10:24:39 +0200, message "REQ-MATH-035: re-derive the one-ticket
crossing — per-scale n=372, cumulative N=440 (both reproduce Macindoe exactly); the previously
stated ~550 was never computed and is withdrawn". The rule as carried, verbatim (script header,
lines 4–5, and section B, line 59):

> Ben propose 2 lectures naturelles ; on calcule LES DEUX, avec nos propres constantes, puis avec
> la regle RE-SOURCEE (Rhin 1987, exposant 13.3, cf. Simons-de Weger Lemme 12).

> === B) avec la regle RE-SOURCEE (Rhin 1987, exposant 13.3 ; via Simons-de Weger) ===

Both canaries the brief names are present and pass (script lines 20–22; `OUT_REQ-MATH-035.txt`
line 2): `q(5,8) = 2⁸ − 3⁵ = 13`, `q(7,12) = 2¹² − 3⁷ = 1909`. The committed output carries, under
the re-sourced rule, exponent `p = 13.3` on `log₂ n` with exhibited `C0 = −14.949`, crossings
`L1 = 1596` (per-scale) and `L2 = 1661` (cumulative tail) — the numbers the round-10 letter then
honestly recomputed to `1655`/`1722` under the proved margin constant `1/13`.

### 1(c) The collision, stated exactly

- **BILAN_R201** (2026-03-16, four months before the correspondence, about R200's version of the
  route) asserts as PROVED that Rhin 1987 contains no linear-forms-in-two-logs statement and that
  13.3 is therefore not Rhin's; real constants ≈ 18.5 (Laurent 2008) or ≈ 23.55 (LMN 1995).
- **test_REQ-MATH-035** (2026-07-25, round 10, descending from our round-9 adjudication which he
  accepted in full at `9c14824`) carries "Rhin 1987, exponent 13.3, cf. Simons–de Weger Lemma 12"
  as the re-sourced rule and computes the entry's tail thresholds from it.

They cannot both be right about what Rhin 1987 contains. The adjudication below finds the Lean
artifact right and the BILAN wrong — with the BILAN's suspicion traceable to a genuine defect in
R200's transcription, not to anything in Rhin.

## 2. The primary statement, re-pinned (web access this item only)

### 2(a) What Rhin 1987 asserts

**The pinned statement.** G. Rhin, *Approximants de Padé et mesures effectives d'irrationalité*,
Séminaire de Théorie des Nombres, Paris 1985–86, Progress in Mathematics **71**, Birkhäuser
(1987), pp. 155–164 — **Proposition, p. 160**: for all integers `u₀, u₁, u₂` with
`H = max(|u₁|, |u₂|)`,

`|u₀ + u₁·log 2 + u₂·log 3| > H^(−13.3)`.

This is a **linear-form (linear independence) bound covering the pair `(log 2, log 3)` directly**
— a three-term form with the rational term `u₀` free and the height taken on the two log
coefficients only — not an irrationality measure of a single quotient, and not a
Baker/LMN-lineage `(log B)²` bound. The 1987 volume itself remains paywalled this session (as in
round 9), so the Proposition is pinned through four independent published carriers, two of which
apply it operationally with page and parameter detail:

1. **Simons–de Weger 2005 — the printed Collatz-side precedent, quoted exactly.** J. L. Simons
   and B. M. M. de Weger, *Theoretical and computational bounds for m-cycles of the
   3n+1-problem*, Acta Arith. **117** (2005), no. 1, 51–70 (DOI 10.4064/aa117-1-3; read this
   session from the publisher's own PDF, pp. 60–61, independently of the round-9 read). Their §5
   sourcing sentence and Lemma 12, verbatim:

   > For general linear forms x log a + y log b with x, y ∈ ℤ and a, b ∈ ℕ the best results today
   > are the result of Laurent, Mignotte and Nesterenko [LMN] for small x, y, and for large x, y
   > that of Matveev [Ma] (see also Nesterenko [Ne]). For our specific case x log 2 + y log 3
   > however, the result of Rhin [Rh] is best. From it we derive the following estimate.
   >
   > Lemma 12. Λ > e^(−13.3(0.46057+log K)).
   >
   > Proof. We apply the Proposition on p. 160 of [Rh] with u₀ = 0, H = u₁ = K + L, and
   > u₂ = −K. Together with Lemma 8 the result follows.

   (Their `Λ = (K+L) log 2 − K log 3`; their Lemma 8 gives `δK < K+L < 1.000001·δK` with
   `δ = log 3/log 2`, whence `log(K+L) < log K + ln δ + 10⁻⁶` and `ln δ = 0.46057` — that is
   exactly the `H`-to-`K` conversion, and their sourcing sentence is direct printed evidence that
   Rhin's result **is** a bound for the linear form `x log 2 + y log 3`, contra the BILAN.)

2. **An independent generalized-Collatz application, same Proposition, both height cases
   exercised.** arXiv:2205.10582 (*Cycles and divergent trajectories for a class of permutation
   sequences*), Lemmas 10 and 12, verbatim:

   > Lemma 10. |Λ| > e^(−13.3(1.34+log(L))).
   > Proof. We apply Rhin's proposition on p. 160 with u₀ = 0, u₁ = 2K + L, u₂ = −(K + L). Then
   > H = u₁ = 2K + L and Rhin's estimate leads to |Λ| ≥ [2K + L]^(−13.3).

   > Lemma 12. |Λ| > e^(−13.3(1.77+log(L))).
   > Proof. We apply Rhin's proposition on p. 160 with u₀ = 0, u₁ = 2K + L, u₂ = −(3K + 2L). Then
   > H = u₂ = 3K + 2L and Rhin's estimate leads to |Λ| ≥ [3K + 2L]^(−13.3).

   The two lemmas take `H` on opposite sides (`u₁` where `u₁` is the larger, `u₂` where `u₂`
   is), pinning the height convention `H = max(|u₁|, |u₂|)` behaviorally, from print.

3. **The zbMATH review of the paper itself (Zbl 0632.10034, reviewer Patrice Philippon) — the
   decisive sentence against the BILAN's premise**, verbatim:

   > L'auteur démontre que des mesures d'irrationalité de log 2 et π/√3 sont données par
   > μ(log 2) = 4,076… et μ(π/√3) = 4,97 […] Il obtient également μ(√3 log(2+√3)) = 17,207…
   > **ainsi qu'une très bonne mesure d'indépendance linéaire sur ℤ effective de 1, log 2 et
   > log 3.**

   The paper contains **both** instruments: irrationality measures of single numbers (log 2 among
   them — the half the BILAN saw) *and* the effective linear independence measure of
   `(1, log 2, log 3)` (the half it denies).

4. **Wu 2003 — read in full this session (the round-9 403-block is resolved), closing round-9
   flag 3.** Qiang Wu, *On the linear independence measure of logarithms of rational numbers*,
   Math. Comp. **72** (2003), no. 242, 901–911, p. 902, verbatim:

   > In the case of the linear independence of 1, log r₁, log r₂, where r₁ and r₂ are rationals,
   > Rhin [RH] showed that the results of Nikisin and Danilov could be improved. In particular he
   > obtained a linear independence measure of 1, log 2, log 3 less than 7.616 […] This is the
   > best linear independence measure known for 1, log 2, log 3, and it gives the best
   > irrationality measure known of log 3 (8.616).

   Two consequences. First, further printed confirmation that Rhin 1987's subject includes the
   linear form in `1, log 2, log 3` (and that Wu–Wang 2014's "`μ(log 3) ≤ 8.616` (Rhin)" line is
   the `u₁ = 0` specialization of it — the irrationality-measure *consequences* the BILAN's
   author will have met are downstream of exactly the linear-form result it denies). Second, the
   grade of Wu's own improvement (`7.6155`, and his Section 3 bounds) is now read from the
   source: his corollaries carry `−ε` exponents valid **"for H = max|qᵢ| ≥ H₀(ε)"** with no
   explicit threshold printed — asymptotic grade, exactly where the round-9 sensitivity table's
   row A put it. Flag 3 of `briefs/merle-la7-mu-check-findings.md` is discharged with no change
   to any conclusion: row A stays asymptotic-grade, and the fully explicit effective constant for
   this pair remains Rhin's 13.3.

**The one boundary that remains, carried forward unchanged from round 9:** the Proposition's own
printed hypotheses — whether any threshold `H₀` is stated on p. 160 — could not be read at first
hand this session (volume paywalled; attempted via publisher, Springer, and archive routes). Both
published applications apply it with no threshold clause from heights of a few hundred upward;
for the entry's use only `H = K₀ ≥ 952` matters (tail beyond `n = 600`), and nothing in either of
his colliding artifacts contests a threshold. The flag stays what it was: confirm from the volume
before any publication leans on small-`H` instances.

### 2(b) The conversion, worked explicitly (what the chain consumes vs. what Rhin states)

What the L-A7 chain consumes is a floor on the tuned-cell gap `ε_n = K₀ − n·β`, `β = log₂3`,
`K₀ = ⌈nβ⌉ = bitlength(3ⁿ)` — equivalently an effective irrationality-measure statement
`|β − K/n| ≥ κ/n^μ`. Derivation from the pinned Proposition, each conversion step named:

1. **Specialize `u₀ = 0`** (the two-term case): permitted, since the Proposition quantifies over
   all integer triples — and both published applications do exactly this. The two-term case is
   covered **at the same exponent**; no cost.
2. **Instantiate** `u₁ = K₀`, `u₂ = −n`: `|Λ| = |K₀·log 2 − n·log 3| = ln 2 · |K₀ − nβ|
   = ln 2 · ε_n`.
3. **Height:** `H = max(|u₁|, |u₂|) = max(K₀, n) = K₀`, since `K₀ > n·1.58 > n` — the height
   convention costs nothing here (and note `H` excludes `|u₀|` by Rhin's definition, so no height
   inflation from the rational term either). This gives the **constant-free per-`n` form the
   replication uses**:

   `ε_n > K₀^(−13.3) / ln 2`.

4. **Measure form, where the `+1` lands:** `|β − K₀/n| = ε_n/n > K₀^(−13.3)/(n·ln 2)`. Converting
   the height to the denominator, `K₀ ≤ nβ + 1`, so `K₀^(−13.3) ≥ (nβ)^(−13.3)·(1 + 1/(nβ))^(−13.3)`
   and

   `|log₂3 − K/n| > c / n^(14.3)`, `c = β^(−13.3)/ln 2 · (1 + o(1)) ≈ 3.15·10⁻³`

   — i.e. `μ_eff = ν + 1 = 14.3`: **one power of `n` is spent normalizing the linear form by `n`**
   (the measure is about the quotient, the form is about the integer combination), and the
   `H`-vs-`n` conversion contributes only the constant `β^(−13.3) = 1/457.4`, not an exponent.
   The south side (`ε′_n = nβ − ⌊nβ⌋`, `u₁ = ⌊nβ⌋`) is covered by the same instantiation.

This reproduces the round-9 record (`briefs/merle-la7-mu-check-findings.md` §2.2) term for term;
nothing there needs correcting.

## 3. The BILAN argument, adjudicated on its merits

**The BILAN's stated premise is false; its practical trigger was real.** Taking its three claims
in order:

1. **"Rhin (1987) traite des mesures d'irrationalité de log 2, pas des formes linéaires en 2
   logarithmes" — false as stated.** Half-true: the paper's title instrument and headline results
   are Padé-type irrationality measures (`μ(log 2) ≤ 4.076` among them). But the same paper also
   proves the effective linear independence measure of `(1, log 2, log 3)` — the Proposition on
   p. 160 at exponent 13.3 — as the zbMATH review states in one sentence, as Wu 2003 states with
   the asymptotic exponent attached, and as two independent published applications use with page
   number and substitutions. "Pas Rhin → pas 13.3" is refuted by the primary record: 13.3 is
   exactly Rhin's, for exactly the form the chain consumes.

2. **"Laurent (2008): C' ~ 18.5 / LMN (1995): C' ~ 23.55" — a category error for this role.**
   Laurent 2008 (*Linear forms in two logarithms and interpolation determinants II*, Acta Arith.
   **133** (2008), 325–348; read this session from the publisher's file) Corollaries 1–2 have the
   shape

   `log|Λ| ≥ −C·D⁴·(max{log b′ + 0.21 (or 0.38), m/D, 1})²·log A₁·log A₂`,

   with Table 1 giving `C₂ = 25.2, 23.4, 22.1, …, 18.8, 18.4, 18.1, 17.9` as `m` runs 10…30 — the
   BILAN's "~18.5" sits in this row, and LMN 1995 (J. Number Theory **55** (1995), 285–321) is
   the same shape with constants about twenty percent larger (the "~23.55"). These numbers are
   **multiplicative constants in front of a `(log b′)²` expression** — a different instrument
   (general two-log bounds, quadratic in the log-height) — **not exponents on the height `H`**,
   which is the role 13.3 plays in Rhin's Proposition. Substituting 18.5 or 23.55 "for" 13.3 is
   not a correction but a unit clash; and for the specific pair `(log 2, log 3)` the Padé-type
   route beats the general two-log machinery, which is the stated reason the Collatz cycle
   literature uses Rhin ("For our specific case x log 2 + y log 3 however, the result of Rhin
   [Rh] is best" — Simons–de Weger, quoted in §2). The BILAN's own grading is consistent with
   this being unverified on its side: I4 is marked OBSERVATION, not PROUVÉ.

3. **What the audit actually caught — a real defect, in R200, not in Rhin.** R200's line (§1(a)
   above) wrote "Rhin (1987): |S·log2 − k·log3| > exp(−13.3·(log S)²)" — **the LMN/Laurent shape
   (log squared) with Rhin's constant transplanted into it**. That statement is indeed not
   Rhin's; no `(log)²`-instrument carries a 13.3 for this pair. An auditor confronted with a
   `(log)²` form attributed to Rhin, and knowing the true `(log)²` constants are ≈ 18–25, could
   reasonably conclude the *attribution* was the error. The actual error was the *transcription*:
   drop the square — `exp(−13.3·log H) = H^(−13.3)` — and the statement is Rhin's, verbatim, with
   the right constant. The BILAN caught a genuine misuse and filed it under the wrong statute.

**Direction of the finding, stated precisely for the entry.** Within R200's own formula
(`M(k) ≤ 3^(−0.415k)·exp(C′(log k)²)`) the audit's practical conclusion was right — a `(log k)²`
slot must be filled by a Laurent/LMN-type constant, not 13.3, so R200's `K₀ ~ 1500` estimate was
indeed unsupported *as derived*. But the L-A7 chain consumes the single-power form
`ε_n > K₀^(−13.3)/ln 2` — Rhin's actual statement — so nothing in the BILAN transfers to L-A7.
His two public artifacts split cleanly: **the Lean rule (`test_REQ-MATH-035`) is right; the BILAN
is wrong**; and the temporal order runs BILAN (2026-03-16, pre-correspondence, about R200's
transcription) → re-sourced rule (2026-07-25, descending from the round-9 adjudication he
accepted at `9c14824`). The newer artifact supersedes the older one on the merits, not merely by
date.

## 4. Sensitivity: does not trigger

The sourced exponent for what the chain consumes is 13.3, unchanged — grade (a). Per the brief's
item 4, no script is written and no recomputation is performed: **nothing needed computing** (the
premise pre-check pattern). Every printed number stands as-is: the L-A7 headline "tail
`< 5.2·10⁻⁴` beyond `n ≈ 2233`" (and the round-10 recomputed thresholds `1655`/`1722` under the
proved `1/13` margin constant), the sensitivity table of
`briefs/merle-la7-mu-check-findings.md` §3(c), the two-key standing of
`briefs/merle-la7-close-check-findings.md`, and the ledger entry's source line (Rhin 1987 /
Simons–de Weger 2005) are all confirmed, none moved.

## 5. Verdict and drafted material

**Verdict: grade (a). 13.3 CONFIRMED for what the chain consumes.** The exact statement it
attaches to: **Rhin 1987, Progress in Mathematics 71, Proposition p. 160 — for all integers
`u₀, u₁, u₂` with `H = max(|u₁|, |u₂|)`: `|u₀ + u₁ log 2 + u₂ log 3| > H^(−13.3)`** — the
effective linear independence measure of `(1, log 2, log 3)`, applied at `u₀ = 0`, `u₁ = K₀`,
`u₂ = −n`, `H = K₀`, yielding `ε_n > K₀^(−13.3)/ln 2` (equivalently `μ_eff = 14.3` on `n`), with
Simons–de Weger 2005 Lemma 12 the printed Collatz-side precedent making the identical
application. BILAN_R201's R201-I3 "PROUVÉ" is wrong, kindly: its premise is refuted by the
paper's own reviewed contents, its replacement constants are the constants of a different
instrument, and the genuine defect it detected was R200's `(log S)²` transcription — a defect
Merle's current artifacts no longer contain. Under grade (a) the brief calls for **no co-edit
language** (the L-A7 source line is already correct as committed and two-keyed), only the
reply-material paragraph.

**Reply-material paragraph (drafted; business content only, the author's to place, edit, or
drop):**

> On the Rhin warning (your §5): adjudicated from the primary literature, and your two artifacts
> split cleanly — the Lean rule is right, the BILAN is wrong, and the BILAN's error has an
> identifiable, honorable mechanism. The primary statement is Rhin 1987 (Progress in Mathematics
> 71, pp. 155–164), Proposition p. 160: for all integers u₀, u₁, u₂ with H = max(|u₁|, |u₂|),
> |u₀ + u₁ log 2 + u₂ log 3| > H^(−13.3). That is a linear-form bound covering the pair
> (log 2, log 3) directly — the "très bonne mesure d'indépendance linéaire sur ℤ effective de 1,
> log 2 et log 3" of the paper's zbMATH review (Zbl 0632.10034) — proved in the same paper whose
> title instrument is Padé-type irrationality measures. The paper contains both; BILAN_R201's
> premise ("Rhin traite des mesures d'irrationalité, pas des formes linéaires en 2 logarithmes")
> sees the first half and denies the second. Simons–de Weger 2005 apply precisely this
> Proposition (Lemma 12: Λ > e^(−13.3(0.46057+log K)); proof, verbatim: "We apply the Proposition
> on p. 160 of [Rh] with u₀ = 0, H = u₁ = K + L, and u₂ = −K"), stating in the same section that
> for x log 2 + y log 3 "the result of Rhin [Rh] is best"; an independent generalized-Collatz
> application (arXiv:2205.10582, Lemmas 10/12) makes the same application with both height cases
> exercised. Your BILAN's Laurent 2008 ≈ 18.5 and LMN 1995 ≈ 23.55 are constants of a different
> instrument: in Laurent 2008 they sit in the C₂ row of Table 1 (25.2 down to 17.9) multiplying
> D⁴·(log b′ + …)²·log A₁·log A₂ — coefficients of a (log)² expression, not exponents on the
> height — so they cannot stand in for 13.3, and for this specific pair the Padé route beats them,
> which is why the cycle literature uses Rhin. What your audit caught was nonetheless real: R200
> had written "Rhin (1987): |S·log2 − k·log3| > exp(−13.3·(log S)²)" — the LMN shape with Rhin's
> constant transplanted into it. That statement is indeed not Rhin's; drop the square and it is,
> verbatim. The auditor rejected the attribution where the defect was the transcription. So: 13.3
> stands for exactly what L-A7 consumes (ε_n > K₀^(−13.3)/ln 2, μ_eff = 14.3), the headline
> n ≈ 2233 and every committed number stand unmoved, L-A7's source line needs no edit, and
> BILAN_R201's R201-I3 "PROUVÉ" is the artifact to retire — on its own record's terms, since your
> re-sourced rule already carries the correct statement. Your structural point survives at any
> value, as you said. One boundary we carry jointly, unchanged from round 9: neither side has yet
> read p. 160 in the 1987 volume itself (it stays paywalled from here); the two published
> applications apply the Proposition with no threshold clause from heights of a few hundred, and
> the entry only needs H = K₀ ≥ 952 — but if a library copy is reachable on your side, that one
> look closes the last gap in the pin.

## Flags, collected

1. Rhin's Proposition p. 160: printed hypotheses (any `H₀`) still not read from the 1987 volume —
   round-9 flag 2 carried forward unchanged; both published applications apply it thresholdless
   from moderate heights; entry's use needs `H ≥ 952` only. Confirm from the volume before
   publication-grade use at small `H`.
2. Round-9 flag 3 (Wu 2003 `H₀` explicitness) — **discharged this session**: the paper is read;
   its corollaries are `H ≥ H₀(ε)` asymptotic-grade; row A of the sensitivity table stays where
   it was. No conclusion changes.
3. BILAN_R201's "18.5" matches no single printed value exactly (Laurent 2008 Table 1 C₂ has 18.8,
   18.4, 18.1, 17.9 in the relevant range) — recorded flat as a rounded recollection of the C₂
   row; immaterial to the adjudication since the row is the wrong instrument for the role either
   way.
4. The BILAN also claims Rhin's measures concern "log 2" where the L-A7-relevant single-number
   consequence is `μ(log 3) ≤ 8.616` (Wu 2003's attribution) — consistent with the review
   (`μ(log 2) = 4.076` is also in the paper); no separate defect, recorded for completeness.
5. Access/scope: read-only clones in the scratchpad; web for item 2 only; no interaction with any
   repository of his; no pushes anywhere; `HANDOFF.md` and all existing findings files untouched,
   per the brief.
