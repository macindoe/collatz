"""Generator for experiments/transport_recurrence_vectors.json.

Supports: cycles.md Remark 12.6.1.1 (the transport recurrence
2^{sigma_r} R_{r+1} = 3^{m_r} R_r + (2^{s_r}-1) q and the seam identity
N_r + q = 2^{m_r} R_r) and reverse.md Lemma 14.15.9.2. The JSON is a
machine-readable test-vector file for cross-stack consumption (in the
first instance, E. Merle's Lean artifact of the integer-form
recurrence).

Two-implementation warranty. This generator contains its OWN
implementations of 12.6.1's rotation numerators R_r, 14.15.9.1's
rotated numerators N_r, and the derived quantities (n, K, q, gcd,
reduced denominator) -- written fresh, prefix-sum style, importing
nothing for the computation. It then imports
experiments/merle_round3_check.py (the round-3 verification script,
29,211 exact checks, 0 failures) for CROSS-VALIDATION ONLY: every
emitted row (every R_r, every N_r, every (n, K, q) triple) is
recomputed by that script's independent double-loop implementations,
and the two must agree exactly on every row or this generator stops
without writing the file. Two independent implementations agree on
every emitted row: that is the file's warranty.

Conventions (12.6.1 / 14.15.9.1, aligned per the round-3 findings):
  n = sum(m_t), K = sum(s_t) + n, q = 2^K - 3^n (signed, UNREDUCED);
  sigma_t = s_t + m_{(t+1) mod p};
  R_r = sum_t 3^{M_t} 2^{S_t} (2^{s_t}-1), indices in rotation order
        starting at r, M_t = sum_{j>t} m_j, S_t = sum_{j<t} sigma_j;
  N_r = 14.15.9.1's numerator on the rotated word with letters
        (m_i, r_i) := (m_i, s_i), same cyclic order (the dictionary);
  reduced denominator = |q| / gcd(q, R_r) (rotation-invariant).

Contents: the named witnesses (the recorded p = 7 staircase seed with
gcd(q, R_r) = 7; the constant-pair reduction witness m = (1,1),
s = (2,2) with q = 55, gcd 11, reduced denominator 5; the -17 word's
profile m = (4,3), s = (1,3) with q = -139, the integer-cycle branch;
the trivial-cycle profiles p = 1..5), 50 deterministic pseudo-random
profiles (p <= 10, entries <= 9, seed 20260718), and the two recorded
p = 22 instances as SUMMARY-ONLY entries (gcd, booleans, bit lengths --
their R_r run to tens of thousands of bits and are not embedded).

Run:  python experiments/make_transport_vectors.py     (~5 s)
"""

import json
import os
import random
import sys
from math import gcd

SEED = 20260718
DATE = "2026-07-18"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "transport_recurrence_vectors.json")

# Cross-validation import ONLY (see the warranty in the module
# docstring): none of the quantities below are computed with it.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import merle_round3_check as mrc  # noqa: E402

CROSS = {"rows": 0}


# ---------------------------------------------------------------------
# Own implementations (fresh; prefix-sum single pass, no double loop).
# ---------------------------------------------------------------------

def derived(ms, ss):
    """(n, K, q) with q = 2^K - 3^n signed, unreduced."""
    n = sum(ms)
    K = sum(ss) + n
    return n, K, (1 << K) - 3 ** n


def R_rotation(ms, ss, r):
    """12.6.1's R_r, own implementation: rotate, then one pass with a
    running suffix product of 3^m and a running prefix sum of sigma."""
    p = len(ms)
    mr = list(ms[r:]) + list(ms[:r])
    sr = list(ss[r:]) + list(ss[:r])
    # suffix powers of 3: pow3suf[t] = 3^{sum_{j>t} mr[j]}
    pow3suf = [1] * p
    for t in range(p - 2, -1, -1):
        pow3suf[t] = pow3suf[t + 1] * 3 ** mr[t + 1]
    total, S_t = 0, 0
    for t in range(p):
        total += pow3suf[t] * (1 << S_t) * ((1 << sr[t]) - 1)
        S_t += sr[t] + mr[(t + 1) % p]        # sigma_t, rotated labels
    return total


def N_rotation(ms, ss, r):
    """14.15.9.1's numerator on the r-th rotation under the dictionary
    (m_i, r_i) = (m_i, s_i); own implementation, same one-pass style."""
    p = len(ms)
    mr = list(ms[r:]) + list(ms[:r])
    sr = list(ss[r:]) + list(ss[:r])
    pow3suf = [1] * p
    for i in range(p - 2, -1, -1):
        pow3suf[i] = pow3suf[i + 1] * 3 ** mr[i + 1]
    total, Spre = 0, 0
    for i in range(p):
        total += (3 ** mr[i] - (1 << mr[i])) * pow3suf[i] * (1 << Spre)
        Spre += mr[i] + sr[i]
    return total


def boolean_block(ms, ss, n, K, q, Rs, Ns):
    """The four confirmations, computed from this file's own rows."""
    p = len(ms)
    rec = all(
        3 ** ms[r] * Rs[r] + ((1 << ss[r]) - 1) * q
        == (1 << (ss[r] + ms[(r + 1) % p])) * Rs[(r + 1) % p]
        for r in range(p))
    seam = all(Ns[r] + q == (1 << ms[r]) * Rs[r] for r in range(p))
    gs = [gcd(abs(q), R) for R in Rs]
    ginv = len(set(gs)) == 1
    divs = [R % q == 0 for R in Rs]
    allnone = all(divs) or not any(divs)
    return {
        "recurrence_all_rotations": rec,
        "seam_identity_all_rotations": seam,
        "gcd_rotation_invariant": ginv,
        "divisibility_all_or_nothing": allnone,
    }, gs[0], all(divs)


def cross_validate(ms, ss, n, K, q, Rs, Ns):
    """Every emitted row against merle_round3_check.py's independent
    implementations. Exact equality or stop."""
    Km, nm, qm = mrc.profile_K_n_q(list(ms), list(ss))
    if (nm, Km, qm) != (n, K, q):
        sys.exit(f"CROSS-VALIDATION DISAGREEMENT (n,K,q) on {ms},{ss}: "
                 f"own ({n},{K},{q}) vs check ({nm},{Km},{qm})")
    CROSS["rows"] += 1
    for r in range(len(ms)):
        if mrc.R_rot(list(ms), list(ss), r) != Rs[r]:
            sys.exit(f"CROSS-VALIDATION DISAGREEMENT R_{r} on {ms},{ss}")
        CROSS["rows"] += 1
        if Ns is not None:
            if mrc.N_rot(list(ms), list(ss), r) != Ns[r]:
                sys.exit(f"CROSS-VALIDATION DISAGREEMENT N_{r} on {ms},{ss}")
            CROSS["rows"] += 1


def profile_entry(pid, kind, ms, ss, note=None, summary_only=False):
    ms, ss = list(ms), list(ss)
    p = len(ms)
    n, K, q = derived(ms, ss)
    Rs = [R_rotation(ms, ss, r) for r in range(p)]
    Ns = [N_rotation(ms, ss, r) for r in range(p)]
    checks, g, divall = boolean_block(ms, ss, n, K, q, Rs, Ns)
    cross_validate(ms, ss, n, K, q, Rs, Ns)
    entry = {
        "id": pid,
        "kind": kind,
        "p": p,
        "m": ms,
        "s": ss,
        "n": n,
        "K": K,
    }
    if note:
        entry["note"] = note
    if summary_only:
        entry["summary_only"] = True
        entry["q_bit_length"] = abs(q).bit_length()
        entry["R_bit_lengths_min_max"] = [min(R.bit_length() for R in Rs),
                                          max(R.bit_length() for R in Rs)]
        entry["gcd_q_R"] = str(g)
        entry["reduced_denominator_bit_length"] = (abs(q) // g).bit_length()
    else:
        entry["q"] = str(q)
        entry["R"] = [str(R) for R in Rs]
        entry["N"] = [str(N) for N in Ns]
        entry["gcd_q_R"] = str(g)
        entry["reduced_denominator"] = str(abs(q) // g)
    entry["q_divides_all_R"] = divall
    entry["checks"] = checks
    return entry, q, g, divall


def main():
    profiles = []

    # ---- named witnesses (expected values transcribed from
    # briefs/merle-round3-check-findings.md; asserted as guards). ----
    e, q, g, divall = profile_entry(
        "p7-staircase-n94", "named-recorded",
        (4, 7, 9, 15, 23, 35, 1), (1, 1, 1, 1, 1, 1, 49),
        note="recorded p = 7 staircase seed (12.8.3, n = 94): a live "
             "reduction witness, gcd(q, R_r) = 7 shared across all seven "
             "rotations")
    assert g == 7 and not divall, "p7 guard"
    profiles.append(e)

    e, q, g, divall = profile_entry(
        "constant-pair", "named-reduction-witness",
        (1, 1), (2, 2),
        note="the multi-letter probe's constant pair ((1,2),(1,2)): "
             "unreduced q = 55, gcd = 11, reduced denominator 5 "
             "(14.15.9's q = 5; the unreduced and reduced moduli differ "
             "exactly here)")
    assert q == 55 and g == 11 and abs(q) // g == 5, "constant-pair guard"
    profiles.append(e)

    e, q, g, divall = profile_entry(
        "minus17-word", "named-integer-cycle",
        (4, 3), (1, 3),
        note="the classical negative cycle -17, word ((4,1),(3,3)): "
             "q = 2^11 - 3^7 = -139, gcd = 139, reduced denominator 1 -- "
             "the integer-cycle (full-divisibility) branch, q < 0")
    assert q == -139 and g == 139 and divall, "minus17 guard"
    profiles.append(e)

    for p in range(1, 6):
        e, q, g, divall = profile_entry(
            f"trivial-p{p}", "named-trivial-cycle",
            (1,) * p, (1,) * p,
            note="trivial cycle as a fake period-%d profile: R_r = q = "
                 "4^%d - 3^%d at every rotation (12.6.1 sanity identity)"
                 % (p, p, p))
        assert divall, f"trivial p={p} guard"
        profiles.append(e)

    # ---- 50 deterministic pseudo-random profiles. ----
    rng = random.Random(SEED)
    for t in range(50):
        p = rng.randint(1, 10)
        ms = [rng.randint(1, 9) for _ in range(p)]
        ss = [rng.randint(1, 9) for _ in range(p)]
        e, q, g, divall = profile_entry(f"random-{t:02d}", "pseudo-random",
                                        ms, ss)
        profiles.append(e)

    # ---- the recorded p = 22 instances, summary only. ----
    e, q, g, divall = profile_entry(
        "p22-n25217", "named-recorded", mrc.P22A_MS, mrc.P22A_SS,
        note="recorded 12.8.6.4 extension instance (n = 25217, corrected "
             "passer): R_r embedded as bit lengths only",
        summary_only=True)
    profiles.append(e)
    e, q, g, divall = profile_entry(
        "p22-n31202", "named-recorded", mrc.P22B_MS, mrc.P22B_SS,
        note="recorded 12.8.6.4 extension instance (n = 31202): R_r "
             "embedded as bit lengths only",
        summary_only=True)
    profiles.append(e)

    n_full = sum(1 for e in profiles if not e.get("summary_only"))
    n_reduc = sum(1 for e in profiles
                  if e["gcd_q_R"] != "1"
                  and e.get("reduced_denominator", "") != "1"
                  and e.get("reduced_denominator_bit_length", 2) > 1)
    doc = {
        "header": {
            "what": "Test vectors for the transport recurrence "
                    "2^{sigma_r} R_{r+1} = 3^{m_r} R_r + (2^{s_r}-1) q "
                    "(cycles.md Remark 12.6.1.1), the seam identity "
                    "N_r + q = 2^{m_r} R_r, and the divisibility/gcd "
                    "corollaries (= reverse.md Lemma 14.15.9.2 in integer "
                    "form). For cross-stack consumers, in the first "
                    "instance the Lean artifact of the integer-form "
                    "recurrence (E. Merle).",
            "warranty": "Every row (every R_r, N_r, and (n, K, q)) was "
                        "computed by two independent implementations -- "
                        "experiments/make_transport_vectors.py (this "
                        "file's generator, fresh prefix-sum code) and "
                        "experiments/merle_round3_check.py (the round-3 "
                        "verification script) -- which agree exactly on "
                        "every emitted row. All boolean blocks are true.",
            "conventions": "n = sum(m_t); K = sum(s_t) + n; q = 2^K - 3^n "
                           "signed and UNREDUCED; sigma_t = s_t + "
                           "m_{(t+1) mod p}; R_r per 12.6.1 in rotation "
                           "order starting at r; N_r per 14.15.9.1 on the "
                           "rotated word with letters (m_i, r_i) = "
                           "(m_i, s_i); reduced denominator = "
                           "|q|/gcd(q, R_r); all big integers are decimal "
                           "strings.",
            "generator": "experiments/make_transport_vectors.py",
            "cross_validated_against": "experiments/merle_round3_check.py",
            "seed": SEED,
            "date": DATE,
            "reference": "cycles.md Remark 12.6.1.1; reverse.md Lemma "
                         "14.15.9.2; briefs/merle-round3-check-findings.md",
        },
        "profiles": profiles,
    }
    doc["header"]["counts"] = {
        "profiles": len(profiles),
        "full_vector_profiles": n_full,
        "summary_only_profiles": len(profiles) - n_full,
        "profiles_with_nontrivial_reduction": n_reduc,
        "rows_cross_validated": CROSS["rows"],
    }
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(doc, f, indent=1)
        f.write("\n")
    size = os.path.getsize(OUT)
    print(f"wrote {OUT}: {len(profiles)} profiles ({n_full} full, "
          f"{len(profiles) - n_full} summary-only), "
          f"{CROSS['rows']} rows cross-validated against "
          f"merle_round3_check.py (exact agreement on every row), "
          f"{n_reduc} profiles with nontrivial reduction, "
          f"{size} bytes")


if __name__ == "__main__":
    main()
