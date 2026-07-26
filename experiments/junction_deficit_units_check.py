#!/usr/bin/env python3
"""Settle flag 6 of briefs/merle-la7-close-check-findings.md: is the Junction
Theorem preprint's `S` our `K`?

Supports: briefs/junction-repo-recon-findings.md, item 3.

The Junction §3 statement, as Merle transcribes it in his own committed script
`experiments/test_REQ-MATH-037_junction_gamma_is_cgen.py`
(ericmerle3789/one-obstruction-three-faces-lean @ 5c9b663):

    Junction: log2 d - log2 C >= (S-1)*gamma,  gamma = 1 - h(1/log2 3)  [per unit of S]
    L-A7    : margin(n) >= c_gen*n                                      [per unit of n]
    conversion comment: S ~ n*log2 3

with margin(n) = K - log2 C(K-2, n-1), K = ceil(n*log2 3).

Two readings are on the table: S = K, or S = K - n (the count of even steps).
This script shows the INEQUALITY does not discriminate between them -- the
S = K - n form is strictly weaker and also holds -- so the settlement rests on
the UNITS: the per-n constant implied by each reading. Only S = K reproduces
c_gen; S = K - n would give gamma*(log2 3 - 1) = 0.02928.

Run: python experiments/junction_deficit_units_check.py
"""

from mpmath import mp, mpf, log, binomial

mp.dps = 40

L = log(3) / log(2)                      # log2 3


def h(x):
    """Binary entropy, in bits."""
    return -x * log(x) / log(2) - (1 - x) * log(1 - x) / log(2)


gamma = 1 - h(1 / L)
c_gen = L - L * log(L) / log(2) + (L - 1) * log(L - 1) / log(2)

print("gamma   = 1 - h(1/log2 3)      =", mp.nstr(gamma, 12))
print("c_gen   = L - L log2 L + (L-1) log2(L-1) =", mp.nstr(c_gen, 12))
print("gamma*L =", mp.nstr(gamma * L, 12),
      "  |gamma*L - c_gen| =", mp.nstr(abs(gamma * L - c_gen), 6))
assert abs(gamma * L - c_gen) < mpf('1e-30'), "canary: the gamma identity"
print()

# --- the inequality under each reading of S ------------------------------
bad_A = bad_B = 0
min_A = min_B = mpf('1e9')
for n in range(2, 2001):
    K = int(mp.ceil(n * L))
    margin = K - log(binomial(K - 2, n - 1)) / log(2)
    for S, tag in ((mpf(K), 'A'), (mpf(K - n), 'B')):
        slack = margin - (S - 1) * gamma
        if tag == 'A':
            bad_A += slack < 0
            min_A = min(min_A, slack)
        else:
            bad_B += slack < 0
            min_B = min(min_B, slack)

print("margin(n) >= (S-1)*gamma, n = 2..2000")
print("  reading A, S = K    : failures", bad_A, " min slack", mp.nstr(min_A, 8), "bits")
print("  reading B, S = K-n  : failures", bad_B, " min slack", mp.nstr(min_B, 8), "bits")
print("  -> the inequality does NOT discriminate (B is the weaker statement)")
print()

# --- the units DO discriminate -------------------------------------------
n = 2000
K = int(mp.ceil(n * L))
print("per-unit ratios at n = 2000:")
print("  K/n      =", mp.nstr(mpf(K) / n, 10))
print("  (K-n)/n  =", mp.nstr(mpf(K - n) / n, 10))
print("  log2 3   =", mp.nstr(L, 10), " <- the conversion factor he uses (S ~ n*log2 3)")
print()
print("implied per-n constant:")
print("  reading A, S = K   : gamma*log2 3       =", mp.nstr(gamma * L, 12),
      "= c_gen  MATCH")
print("  reading B, S = K-n : gamma*(log2 3 - 1) =", mp.nstr(gamma * (L - 1), 12),
      "!= c_gen")
print()
print("VERDICT: S = K. The preprint's S is our K (log2 d = S, d = 2^K).")
