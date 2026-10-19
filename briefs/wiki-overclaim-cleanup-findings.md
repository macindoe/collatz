# Findings: wiki overclaim cleanup — cycles.md Remark 12.8.4 and aeh.md §13.5

Brief: `briefs/wiki-overclaim-cleanup-brief.md`. Branch `wiki-overclaim-cleanup`, base `46e7464`. Wording only; no statement's proof touched.

## 1. Is the anchor-walk equivalence proved anywhere in the record?

No. The places the record points to give only the necessary direction:

- `spine.md` 9.8.4, Remark (anchor form): a nontrivial cycle *is* a periodic anchor-increment sequence, a closed walk whose `ΔM_t` sum to `0`. That is cycle ⇒ closed walk. It does not show that a closed walk (`Σ ΔM_t = 0`) meets the divisibility conditions `q | R_r` of `cycles.md` 12.6.1, and it does not show the converse.
- `bridge.md` 16.4.4 restates the same target ("a nontrivial cycle is a finite closed anchor walk with `Σ ΔM_t = 0`") with no equivalence proof.
- `stage2.md` 11.8.5.6 has the increment identity `ΔM = N((ω_+/ω)²)`. It does not connect to `R_r`.

This matches the fix pass's U6 source column (`briefs/paper1-v4-fixpass-findings.md`). So the sentence is weakened to what is proved, and no citation could stand in for the equivalence.

## 2. Edits

| Page | Old | New | Source |
|---|---|---|---|
| `cycles.md` Remark 12.8.4 | "What *must* kill the staircase is the `p`-fold divisibility system — equivalently, in anchor coordinates, the rigidity of closed anchor walks (`11.8.5.6`, `9.8.4` anchor form)." | "What *must* kill the staircase is the `p`-fold divisibility system — the conditions `q \| R_r` of `12.6.1` — not size alone. In anchor coordinates the arithmetic input shows up, for example, as the closed anchor walk: a cycle's anchors return and its increments satisfy `Σ_t ΔM_t = 0` (`11.8.5.6`, `9.8.4` anchor form). That is a necessary condition; its equivalence with the divisibility system is not proved." | Paper v4 U6 (Thm 4.6's closing sentence: "requires the divisibility conditions `q ∣ R_r` of Proposition 4.1, not size alone"; the anchor walk kept as an example: "a cycle's anchors return and its increments satisfy `Σ_t ΔM_t = 0`"). Necessary direction: `spine.md` 9.8.4 anchor form. |
| `aeh.md` §13.5, "The artifact mechanism" | "This also explains the cell-specificity: `(1,1)` is the unique class with a deterministic self-loop channel." | "This also explains the cell-specificity: the bias is aimed at the class `(1,1)`, whose residue `1` returns to it deterministically (a self-loop channel, Lemma `13.5.1`)." | Paper v4 U17 ("the class `[1,1]`, whose residue 1 returns to it deterministically (a self-loop channel)"). Lemma 13.5.1 proves the routing from `(1,1)` only. It says nothing about other classes, so the uniqueness claim is dropped, not proved. |
| `aeh.md` front matter | `updated: 2026-09-04` | `updated: 2026-10-19` | — |

`cycles.md` already carries `updated: 2026-10-19`. Neither page's `status` changes: no result's standing moved.

## 3. Other places with the phrasings (not edited)

- **No other wiki page repeats either sentence.** I ran a `git grep` over all tracked files, excluding `sources/` and `paper/`, for "unique class", "self-loop channel", "equivalently, in anchor coordinates" and "equivalently … anchor walk". It found no other wiki-page hits. The `stage1-synthesis.md` hits for "unique class" are unrelated congruence-class uniqueness statements.
- **Briefs (historical records; not edited).** These quote the published v1–v3 sentence or the record's: `briefs/jointnote-premise-ours-findings.md:328`, `briefs/jointnote-v1-draft-brief.md:31`, `briefs/jointnote-v1-draft-findings.md:117`, `briefs/jointnote-v1-draft-patches/0001-…patch:45`, `briefs/merle-round19-pr-patches/0001-…patch:47`, `briefs/paper1-content-lock-findings.md:66,77`, `briefs/paper1-v4-items-findings.md:66`, `briefs/v3r6-prune-design-findings.md:625`. The joint-note patches quote the published Theorem 4.6 of v3 verbatim, which is accurate as a quotation of v3. Whether the joint note should quote v4's wording instead is the author's call.
- **Related framing, kept.** Several pages say cycle exclusion's residual content "is anchor-walk rigidity": `cycles.md` Current state, 12.8.5 and the 12.8.6 scope paragraph; `index.md:49`; `stage4.md:96`; `stage1.md:637`; `spine.md` 9.8.4 anchor form ("Cycle exclusion is thus an exact-rigidity statement about such closed walks"); `bridge.md` 16.4.4. These name the open front and the strategic bet. They do not assert an equivalence with the divisibility system, so they were left alone. A future status pass could decide whether "residual content is anchor-walk rigidity" should become "the divisibility conditions, of which anchor-walk rigidity is one reading".
