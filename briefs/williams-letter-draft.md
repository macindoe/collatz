# Draft: first letter to Jennifer Williams (unsent)

Calibration: `briefs/williams-letter-findings.md` (verdict: answers (1) in part). The letter claims no more than that.

---

**Subject:** Your skeleton coordinates (arXiv:2607.01718) and a paper built on the same coordinates

Dear Jennifer Williams,

My name is Benjamin Macindoe. I'm an independent researcher, and I'm writing because I recently found your paper *A Coordinate System for Collatz Dynamics*. My own paper, *Reduced coordinates for the Collatz map* (v3, DOI 10.5281/zenodo.21730505), is built on the same coordinates. In my case they go back to a hand-drawn note of March 2023. I hadn't seen your paper when I published, and your arXiv posting came a week before my first version.

The dictionary is short. My state (ω, d) is your row: ω = λ and d = a + b = k. Your diagonal flow is my Proposition 2.2(i), and your boundary exit is my x_exit (Proposition 2.2(ii)).

On your open problem (1), I should say plainly that I don't have a closed form for which skeleton is entered. In your notation, at the exit (1, b) of row k = b + 1, put s = v₂(λ·3^k − 1). The entered position is then given by λ′·2^(a′+s)·3^(b′) = λ·3^k − 1 + 2^s, which is your Proposition 3.10 rearranged. What the paper adds is partial:

- It treats the transition as a self-map F on rows (λ, k) (Definition 2.1). It then proves that the Collatz conjecture, and the question of nontrivial cycles, are each exactly equivalent to a statement about F (Theorem 2.3).
- Section 3 gives exact laws for the rest of the transition, everything except λ′ itself. When λ·3^k ≡ 1 (mod 8), the boundary valuation is s = 2 + v₂(k − M(λ)), where M(λ) = −2 log λ / log 9 is a 2-adic logarithm fixed by the skeleton. Otherwise s ∈ {1, 2} is fixed by λ mod 8 and k mod 2 (Theorem 3.3). The entry position (a′, b′), and so the row entered, has laws of the same kind (Theorem 3.5, Lemma 3.4).

So where the trajectory lands in the next skeleton is characterized, but which skeleton it lands in is not. I checked all of this directly in your coordinates (53,360 rows, no discrepancies) and am happy to send the script.

The next version of my paper will cite yours.

I'd be glad to know whether you have taken the work further since July. I saw that a version is under peer review. I'd also like to know whether you would welcome a pointer to anything else in this direction.

[PERSONAL PARAGRAPH: author's choice, or omit]

[SIGN-OFF: author]
