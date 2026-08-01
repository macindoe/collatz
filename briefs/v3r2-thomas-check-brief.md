# Brief: A. Thomas (2017) and the non-Haar 3-adic law — closing Tao's footnote (v3 round 2)

**Why this exists, and why it is the last one.** Tao's footnote in arXiv:1909.03562 names two prior works as possibly related to his `Syrac(Z_3)` process. One is Wirsching (LNM 1681), checked and cleared: `briefs/v3r2-wirsching-check-findings.md` shows his inverse branches are weighted uniformly, giving Haar, where ours and Tao's are weighted `2^{-a}`, giving `Syrac` — different objects for a stateable reason. The other is:

> **A. Thomas, _A non-uniform distribution property of most orbits, in case the 3x+1 conjecture is true_, Acta Arithmetica 178 (2017), 125–134.**

Nobody has opened it. It predates Tao by two years, and "non-uniform distribution" is the one phrase met this round that points at a **non-Haar `3`-adic law** — the genre our `ν` belongs to.

**This closes the footnote and the check sequence.** Wirsching and Thomas are the two names in it. Anything beyond these is a general novelty re-sweep, which is a separate decision and not this brief's business. Do not open one.

## Context you need

This round has already established, and you should not re-derive:

- `aeh.md` `13.6.5`'s absorption law **is** Tao's `Syrac(Z_3)` under `y_3 = Syrac(Z_3)/2` (`briefs/v3r2-syrac-identity-findings.md`, proved and verified at 363 residues). Attribution to Tao is owed and drafted.
- Wirsching does **not** predate Tao for it, and does not cover the product law (`briefs/v3r2-wirsching-check-findings.md`).
- The AEH section's remaining novel content is `aeh.md` `13.6.3`(v) (the joint product/renewal law), `13.6.4` (the orbit-by-orbit genericity equivalence), and the calibration record.

Read those two findings files, plus `aeh.md` `13.6.3`(v), `13.6.5`, and `publication.md`'s novelty sweep, before searching outward.

## The questions

1. **What does Thomas actually prove?** Exact statement from a primary source. The title conditions on the `3x+1` conjecture being true — establish what is assumed, what is concluded, and about what object.
2. **Is his non-uniform distribution law our `ν` / Tao's `Syrac`?** If the paper exhibits a specific non-Haar limiting law on `Z_3` (or on `Z_3^×`), compute or extract its low-level values and compare against `ν_1 = (0, 2/3, 1/3)` on residues `(0,1,2) mod 3` and against `13.6.5`'s `2/3, 19/63, 2/63`. A level-one disagreement settles it negatively; agreement at levels one **and** two is strong evidence of the same object and warrants going further.
3. **If it is the same law:** does Thomas predate Tao as the correct primary attribution for `13.6.5`? Draft the corrected attribution.
4. **Does it bear on `13.6.3`(v) or `13.6.4`?** The product/renewal structure and the genericity equivalence are what the paper still claims. Answer separately from question 2 — a paper can contain the law without containing the product structure, which is exactly what happened with Tao.
5. **Should it be cited regardless?** It is named in Tao's footnote; a referee who follows that footnote will find it. Draft a `\bibitem` and a related-work sentence if warranted.

## Sourcing

Acta Arithmetica 178 is a 10-page journal paper, not a monograph — this should be obtainable. Try the journal (impan.pl), arXiv, the author's page, and citing literature. If the full text is unreachable, a detailed review (zbMATH/MathSciNet) plus the abstract may settle question 2 on its own, since a level-one value is usually stated in an abstract or review.

**Mark every claim verified-primary, secondary-description, or unconfirmed.** "Could not establish" is an acceptable outcome; state what access would settle it.

## Deliverable

`briefs/v3r2-thomas-check-findings.md` — the only file you may write. Include Thomas's statement with its source, the comparison verdict for each question, any drop-in `\bibitem` and prose, and an explicit closing line stating whether Tao's footnote is now fully discharged.

## Constraints

- **Read-only on every tracked file.** No edits to `aeh.md`, `publication.md`, the `.tex`, or any wiki page. Nothing added to `experiments/`; scratch work in the scratchpad.
- No `git` write operations of any kind.
- Write with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`.
- Exact rational arithmetic in any comparison that decides the verdict.
- Do not state any theorem's form from memory. Three checks this round found something believed novel was already known; a fourth found the opposite. Report what the source supports, either way.
