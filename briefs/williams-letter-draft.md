# First letter to Jennifer Williams (sent 2026-10-19 by the author, from his own client; the text below is as sent)

Calibration: `briefs/williams-letter-findings.md` (verdict: answers (1) in part). The letter claims less than that: the Section 3 laws (M(λ)) are left out by the author's decision, 2026-10-19 — exact, but not a lever.

---

**Subject:** Your skeleton coordinates (arXiv:2607.01718) and a paper built on the same coordinates

Dear Jennifer Williams,

My name is Benjamin Macindoe. I'm an independent researcher, and I'm writing because I recently found your paper *A Coordinate System for Collatz Dynamics*. My own paper, Reduced coordinates for the Collatz map (v3, DOI 10.5281/zenodo.21730505), is built on the same coordinates, arrived at independently; your arXiv posting came a week before my first version.

The dictionary is short. My state (ω, d) is your row: ω = λ and d = a + b = k. Your diagonal flow is my Proposition 2.2(i), and your boundary exit is my x_exit (Proposition 2.2(ii)).

On your open problem (1), I should say plainly that I don't have a closed form for which skeleton is entered. In your notation, at the exit (1, b) of row k = b + 1, put s = v₂(λ·3^k − 1). The entered position is then given by λ′·2^(a′+s)·3^(b′) = λ·3^k − 1 + 2^s, which is your Proposition 3.10 rearranged. What my paper adds is the framing around that step: it treats the transition as a self-map F on rows (λ, k) (Definition 2.1), and proves that the Collatz conjecture, and the question of nontrivial cycles, are each exactly equivalent to a statement about F (Theorem 2.3).

I checked the dictionary and the transition directly in your coordinates (53,360 rows, no discrepancies) and am happy to send the script.

The next version of my paper will cite yours.

I'm curious whether you have taken the work further since July. I saw that a version is under peer review. I'd also like to know if you would welcome a pointer to anything else in this direction.

For context: the starting point was a note I scribbled in 2023 on the factoring mechanism. I worked out the coordinates themselves by hand last December, and built them out properly with AI from there; the next version of my paper describes how. You got there first in print. I only connected your paper to my own work this week, which is why I'm writing now.

Best regards,
Ben Macindoe
