# experiments/p22_passer.py
#
# Standalone verifier for the p = 22 resolution recorded in cycles.md
# 12.8.6 ("Obstruction (p = 22) -- resolved (2026-07-17)"). Fresh code:
# imports nothing from experiments/merle_pincer_check.py or
# experiments/staircase_allp.py. The rotation-sum formula below is
# re-derived directly from cycles.md Proposition 12.6.1, not copied from
# either of those scripts.
#
# Supports: cycles.md 12.8.6 (Obstruction paragraph, 12.8.6.4's extended
# record). Provenance of the two certificates: Eric Merle (correspondence
# 2026-07-16/17), verified by experiments/merle_pincer_check.py and
# recorded in briefs/merle-pincer-check-findings.md; this script is a
# THIRD independent implementation of Proposition 12.6.1 confirming both
# exactly, from the formula alone.
#
# What is checked, per instance:
#   n = sum(m_t), K = sum(s_t) + n, q = 2^K - 3^n > 0            (12.1.1)
#   R_r = sum_t 3^(M_t) * 2^(S_t) * (2^(s_t) - 1)  for every rotation r,
#     M_t = sum_{j>t} m_j, S_t = sum_{j<t} sigma_j,
#     sigma_j = s_j + m_{j+1 mod p}                              (12.6.1)
#   size-passer: q <= R_r for all p rotations
#   divisibility (bounded observation, no halt condition unless it hits
#     every rotation, which would mean a genuine cycle candidate): q | R_r
#   gamma = K - log2(q), via a bit-length-based log2 that never converts
#     the full (possibly ~40,000-bit) integer q to a float -- only its
#     top 60 bits are ever used for the fractional part, so this is exact
#     for the integer part and accurate to ~17 significant digits for the
#     fractional part regardless of how large q is.
#
# The p = 7 published staircase instance (cycles.md 12.8.3, gamma =
# 6.7438) is run first, as a sanity anchor: it fixes this script's gamma
# convention against the one published, trusted number before the p = 22
# certificates -- which are otherwise unverifiable by eye at this scale
# (q ~ 2^40000) -- are evaluated with it.
#
# Exact integer arithmetic for every pass/fail decision. Runnable in
# seconds: python experiments/p22_passer.py

import math


def log2_bigint(x):
    """log2 of a positive Python int, safe for arbitrary size. The
    integer part is exactly x.bit_length() - 1; the fractional part
    comes from a plain float log2 of the top 60 bits of x (obtained by
    an exact integer right-shift, never a full int-to-float cast), which
    gives about 17 significant decimal digits of accuracy independent of
    how many bits x has -- q reaches ~40,000-50,000 bits for the p = 22
    certificates below, far past the ~1024-bit range a naive float(x)
    conversion could even represent without overflowing."""
    assert x > 0
    bl = x.bit_length()
    if bl <= 60:
        return math.log2(x)
    shift = bl - 60
    top = x >> shift
    return math.log2(top) + shift


def R_all(ms, ss):
    """Independent implementation of cycles.md Proposition 12.6.1: given
    entry depths ms and exit valuations ss of a candidate period-p
    profile (both length p, read cyclically), return [R_0, ..., R_(p-1)]
    with

        R_r = sum_{t=0}^{p-1} 3^(M_t) * 2^(S_t) * (2^(s_t) - 1)

    where, reading indices in rotation order starting at r: M_t is the
    sum of the (rotated) entry depths strictly after position t, and
    S_t is the sum of sigma_j = s_j + m_{j+1 mod p} (rotated, cyclic)
    strictly before position t. This is the formula as stated in
    12.6.1, evaluated directly with exact Python integers -- no
    reuse of any other script's accumulator variables or loop order."""
    p = len(ms)
    assert len(ss) == p and p >= 1
    out = []
    for r in range(p):
        mm = ms[r:] + ms[:r]
        sss = ss[r:] + ss[:r]
        sigma = [sss[t] + mm[(t + 1) % p] for t in range(p)]

        M = [0] * p
        running = 0
        for t in range(p - 1, -1, -1):
            M[t] = running
            running += mm[t]

        S = [0] * p
        running = 0
        for t in range(p):
            S[t] = running
            running += sigma[t]

        R = sum((3 ** M[t]) * (1 << S[t]) * ((1 << sss[t]) - 1) for t in range(p))
        out.append(R)
    return out


def check_instance(label, ms, ss, expected_gamma=None, gamma_tol=5e-3,
                    interval=None):
    """Runs the full check on one (ms, ss) profile and prints a report.
    expected_gamma, if given, is cross-checked against the published
    figure (the p = 7 anchor). interval, if given as (lo, hi), asserts
    gamma/log2(p) falls inside it (12.8.6.4's recorded [1.828, 3.643])."""
    p = len(ms)
    n = sum(ms)
    K = sum(ss) + n
    q = (1 << K) - 3 ** n
    assert q > 0, f"{label}: q <= 0 -- not a valid candidate (12.1.1 needs 2^K > 3^n)"

    Rs = R_all(ms, ss)
    size_ok = [R >= q for R in Rs]
    n_pass = sum(size_ok)
    div_ok = [R % q == 0 for R in Rs]
    n_div = sum(div_ok)
    gamma = K - log2_bigint(q)
    ratio = gamma / math.log2(p) if p > 1 else float("nan")

    print(f"-- {label} --")
    print(f"  p={p}, n={n}, K={K}")
    print(f"  size-passer (q <= R_r), all {p} rotations: {n_pass}/{p} "
          f"({'PASS' if n_pass == p else 'FAIL'})")
    print(f"  divisibility (q | R_r): {n_div}/{p} pass "
          f"(bounded observation; a halt would require {p}/{p})")
    print(f"  gamma = K - log2(q) = {gamma:.4f}")
    if p > 1:
        print(f"  gamma/log2(p) = {ratio:.4f}")

    if expected_gamma is not None:
        ok = abs(gamma - expected_gamma) < gamma_tol
        print(f"  cross-check vs published gamma={expected_gamma}: "
              f"{'MATCH' if ok else 'MISMATCH'} (diff {gamma - expected_gamma:+.4f})")
        assert ok, f"{label}: gamma convention does not match the published anchor"

    if interval is not None:
        lo, hi = interval
        ok = lo <= ratio <= hi
        print(f"  gamma/log2(p) in 12.8.6.4's recorded [{lo}, {hi}]: "
              f"{'YES' if ok else 'NO'}")
        assert ok, f"{label}: gamma/log2(p) outside the recorded interval"

    if n_div == p:
        print("  !!! HALT: size AND divisibility both pass on every rotation "
              "-- this would be a genuine cycle candidate. Stop and escalate, "
              "do not continue.")
        raise SystemExit(1)

    assert n_pass == p, f"{label}: not a size-passer"
    print(f"  {label}: size-passer confirmed, divisibility fails as expected.")
    print()
    return dict(n=n, K=K, q=q, gamma=gamma, ratio=ratio, n_pass=n_pass, n_div=n_div)


def main():
    print("=" * 70)
    print("SANITY ANCHOR: published p = 7 staircase instance (cycles.md 12.8.3)")
    print("=" * 70)
    m7 = [4, 7, 9, 15, 23, 35, 1]
    n7 = sum(m7)
    K7 = (3 ** n7).bit_length()
    S7 = K7 - n7
    s7 = [1, 1, 1, 1, 1, 1, S7 - 6]
    check_instance("p=7 anchor (n=94)", m7, s7, expected_gamma=6.7438)

    interval = (1.828, 3.643)

    print("=" * 70)
    print("p = 22 CERTIFICATE 1: n = 25217 -- Merle's in-scale point")
    print("(construction 12.8.6.2 + 13 correction moves of 12.8.6.3;")
    print(" briefs/merle-pincer-check-findings.md item 2)")
    print("=" * 70)
    ms_a = [1, 1, 3, 3, 6, 10, 14, 24, 37, 59, 95, 149, 235, 372, 588,
            932, 1475, 2338, 3704, 5869, 9301, 1]
    ss_a = [1] * 21 + [14730]
    check_instance("p=22, n=25217", ms_a, ss_a, interval=interval)

    print("=" * 70)
    print("p = 22 CERTIFICATE 2: n = 31202 -- Merle's off-scale point")
    print("(construction 12.8.6.2 + 8 correction moves of 12.8.6.3;")
    print(" briefs/merle-pincer-check-findings.md item 2)")
    print("=" * 70)
    ms_b = [1, 2, 3, 4, 8, 11, 18, 29, 46, 73, 115, 182, 290, 460, 728,
            1152, 1826, 2893, 4584, 7264, 11512, 1]
    ss_b = [1] * 21 + [18231]
    check_instance("p=22, n=31202", ms_b, ss_b, interval=interval)

    print("=" * 70)
    print("RESULT: both p = 22 certificates verified from Proposition 12.6.1")
    print("alone (third independent implementation) -- PASS.")
    print("=" * 70)


if __name__ == "__main__":
    main()
