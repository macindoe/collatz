# Findings: symbols-registry (2026-08-15)

Delegated session, branch `symbols-registry`, brief `briefs/symbols-registry-brief.md`. Deliverables: `symbols.md` (new) and one pages-table row in `index.md`, committed separately. This file records the sweep, the verification method, and everything ambiguous or off-brief — record, not fix.

## Files covered

In queue order: `spine.md` §3–§5; `stage3.md` (11.8.6), `stage4.md` (11.8.7.1–11.8.7.3), `anchors.md` (all, pointers followed to homes), `ladder.md` (15.5), `stage1-synthesis.md` (11.8.3.6, 11.8.3.11), `stage1.md` (11.8.1.6, 11.8.4.1, 11.8.4.4), `stage2.md` (11.8.5.6), `reverse.md` (14.1–14.3, 14.14); `cycles.md` (§12 preamble, 12.1–12.2, 12.5–12.6, §12.8 preamble, 12.8.2); `itinerary.md` (14.15.1, 14.15.3–14.15.6, 14.15.7–14.15.10); `aeh.md` (13.1–13.3, 13.6). `bridge.md`, `open-problems.md`, `program.md`, `anchor-digit-search.md`, `stage1-synthesis.md` beyond the cited sections: consulted only where a pointer led there; they introduce no recurring notation of their own that the frames above do not already own.

## Verification method

Every defining pointer in `symbols.md` was verified in-session by opening the cited section and confirming the glyph is defined there (not merely used): spine §3/§4 read in full; each stage/cycles/itinerary/aeh definition read at its statement. No line-number citations anywhere. No pointer failed to resolve; no drifted definition site was found.

## Seeded collisions: verification results

- **`σ` ×4** — four registry rows confirmed (stage digit cost; cycles per-step `σ_t`; sector sign; shift map). Precision: rows 1 and 2 are the **same quantity** (`v₂(C)`, per-step) read in two frames, so distinct *meanings* number three, distinct rows four. The audit's "four meanings" is accurate at row granularity; recorded here so nobody later "corrects" the index in either direction.
- **`q` ×3+** — found **×4**: the seeded three (seam gap `2^K − 3^n`; fixed-point denominator `a/q`; window `(p,q)`) plus the door odd part `q(y) = (y+1)/2^{m(y)}` (reverse.md 14.14.3.1, itinerary.md 14.15.1.1), which the stratum definition uses throughout §14.14–§14.15.
- **`m`, `r`, `n`, `K`, `M`, `S`, `R`, `a`, `k`** — all verified as real collisions with the definition sites given in the index. Notes: the sharpest `m`/`K` hazard is the odd-step frame of cycles.md 12.6.1.2/12.6.1.3, where `m` means total halvings (this wiki's `K`) — the registry carries it as an explicit warning row. `r` and `k` each also serve as the wiki's default truncation-precision parameters (bound variables); those do not get rows and are flagged as such in the index.
- **Constants `0.585`** — the seed describes two quantities, drift `log₂3 − 1` vs side-asymmetry density `log₂(3/2)`. Precisely read, these are **algebraically equal** (`log₂3 − 1 = log₂3 − log₂2 = log₂(3/2) = 0.58496…`): one real number in two unrelated roles, not two values sharing a numeral. The registry's constants entry is worded accordingly ("cite the section, not the number"); the seed's phrasing is the only inaccuracy found in the brief, and nothing was forced into the page.

## Sweep discoveries beyond the seed

Sixteen additional multi-row glyphs, all now in the collision index with verified sites: `T` (spine raw map vs aeh odd-to-odd map, with `T₁`/`T_N` kept apart in-page at aeh 13.2.3), `F` (reduced map vs `F_i`), `G` (exit map vs `G_k`), `A` (step numerator vs `A_n`/`A_P` vs arc), `B` (affine offsets vs Bernoulli measure), `C` (carry vs Baker constant `C(ω)` vs signature coset), `D` (state depth vs unreduced denominator vs cap), `N` (anchor vs fixed-point numerator vs sampling scale), `H` (heights vs inline binary entropy), `W` (word vs `W_{k,D}` vs past-window depth), `L` (`log₂3` vs block length), `Λ` (Baker form vs budget), `β` (affine offset vs cycles-local `log₂3` vs aeh `2(2 − log₂3)`), `ε` (`ε_t` vs signature residue), `c` (target family vs `c_σ` vs margin constants), `p` (period vs past-window length).

One in-page collision worth naming: aeh.md's `S_n` carries two readings **inside one page** — budget count `Σ(m_i+s_i)` (13.2.1) vs letter count `Σ(m_i+r_i)` (13.2.4) — which the page itself keeps apart at 13.2.3. Not an inconsistency; recorded because it is the only place a glyph collides with itself within a single file.

## Ambiguities and judgment calls (recorded, not fixed)

1. **`α_i`, `β_i` glyph naming.** The affine coefficients are proved at reverse.md Theorem 14.14.4.1, but the theorem does not name them; the glyphs are first attached in Theorem 14.14.8.2's *proof* ("Write `α_i = …, β_i = …`") and re-fixed at itinerary.md 14.15.9's setup (`g_j(u) = α_j u + β_j`, citing 14.14.4.1). The row cites 14.14.4.1 as the defining site with the naming sites in parentheses. If a future edit wants the glyphs in 14.14.4.1's statement proper, that is a content decision for reverse.md's owner, not this registry.
2. **The door's definition is distributed.** "Door" is introduced across reverse.md 14.1.1 (exit construction), 14.6.5.1 (recovery), and 14.14.1 (edge parameterization, where the term and the `(y,s)` coordinates are fixed). The row cites 14.14.1 with the two sources in parentheses.
3. **`v₂`, `v₃` have no definition site.** The p-adic valuations are used from spine.md §3 onward as standard notation and are never defined anywhere in the wiki. No row was given (the rule "the glyph is actually defined there" cannot be satisfied); if a definition line is ever wanted, spine.md §3/§4 is the natural home. Same status: `⌈·⌉`/`⌊·⌋`, `ord_q(·)`, `gcd`, Iverson brackets `[·]` (used at itinerary.md 14.15.9.6 without ceremony).
4. **`Λ`'s defining site is a proof.** `Λ = K log 2 − n log 3` is named inside cycles.md 12.8.2's proof (as "Rhin's linear form, 12.5.3") and quoted by anchors.md 17.5; it has no definition-numbered home. Cited as "cycles.md 12.8.2 (proof)".
5. **Frame-2 file list vs anchor homes.** The brief's frame-2 file list (`stage3`, `stage4`, `reverse`, `anchors`, `ladder`) does not include `stage1-synthesis.md`/`stage1.md`/`stage2.md`, but the anchor family (`N`, `M`, `ΔM`, `n = d/2`, `C(ω)`) is defined there and recurs wiki-wide (anchors.md is pointers-only and defines nothing). The registry homes those rows in frame 2 with pointers to their true sites — the alternative (no rows for the anchors) would fail the page's charter.
6. **Frame-3 additions from §12.8.** `γ`/`γ'`, `w(A)`, `n₀(p)`, `Λ`, `c_gen`/`c_strat` sit in §12.8/12.6.1.5, outside the brief's §12.5–§12.6 window but recurring (README and anchors.md quote `n₀(p)`; the status header quotes `γ`). Included under "sweep for others that recur"; flagged here in case the reviewer wants frame 3 held strictly to its window.
7. **Size.** `symbols.md` is ~26 KB against the brief's 10–20 KB guidance. The overshoot is the collision index (27 glyph entries against the seeded 11) plus the door/itinerary frame's breadth; per the brief, fidelity won. Nothing in the page restates a theorem; every meaning is one line.
8. **`Ω` vs `ω`** (state core vs reduced core at the seam, reverse.md 14.14.1.1 proves `ω₊ = Ω`) was judged a near-collision of distinct glyphs, not a collision: one row (`state(y) = (Ω,D)`), no index entry. Likewise `E` vs `E₃` vs expectation `E[·]`, and `Q_n` vs the proof-internal `Q_t` (aeh.md 13.6.3(iv)): distinct glyphs or bound variables, no entries.

## Row counts (as committed)

Frame 1: 16 rows · Frame 2: 15 · Frame 3: 16 + 2 (odd-step sub-block) · Frame 4: 28 · Frame 5: 12 · Frame 6: 15 · Collision index: 27 glyph entries + 1 constants entry.
