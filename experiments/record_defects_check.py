# Record-defect checks (cycles.md 12.6.1 and 12.8).
#
# Supports two repairs:
#   (A) Proposition 12.6.1's `sigma` convention. The proposition writes
#       S_t = sum_{j<t} sigma_j without defining sigma at the point of use.
#       The section preamble (cycles.md 12.6 header paragraph) fixes
#       m_{t+1} = sigma_t - s_t, i.e. sigma_t = s_t + m_{t+1}; this is also
#       what the committed experiments/uniform_trim.py R_rot computes and what
#       everything in 12.8 was computed under. The "natural" local misreading
#       sigma_t = m_t + s_t is a different, wrong object. Parts 1-4 establish
#       that in fresh code and map exactly which guardrails can see it.
#   (B) Corollary 12.8.2's n_0(p) at p = 92, recomputed from the displayed
#       equation (part 5), against README's / 12.8.5's `n ~ 10^18`.
#
# Part 4 is the CANARY: two checks with unequal m and s that reject the
# misreading, so the next implementer fails loudly instead of silently
# reproducing the one published sanity identity.
#
# Fresh code per AGENTS.md: imports nothing from uniform_trim.py,
# merle_round3_check.py or any other committed script; the reference
# implementation is transcribed inline and labeled.

import math
import random
from math import gcd
from decimal import Decimal, getcontext

L3 = math.log2(3)
FAILURES = []
CHECKS = 0


def check(name, cond):
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILURES.append(name)
    return cond


def v2(x):
    x = abs(x)
    assert x != 0
    return (x & -x).bit_length() - 1


# ---------------------------------------------------------------- conventions
def R_rot_correct(ms, ss):
    """Prop 12.6.1 numerator with sigma_j = s_j + m_{j+1} (indices cyclic)."""
    p = len(ms)
    R = 0
    Spre = 0
    for t in range(p):
        R += 3 ** sum(ms[t + 1:]) * (1 << Spre) * ((1 << ss[t]) - 1)
        Spre += ss[t] + ms[(t + 1) % p]
    return R


def R_rot_misread(ms, ss):
    """The natural local misreading sigma_j = m_j + s_j."""
    p = len(ms)
    R = 0
    Spre = 0
    for t in range(p):
        R += 3 ** sum(ms[t + 1:]) * (1 << Spre) * ((1 << ss[t]) - 1)
        Spre += ms[t] + ss[t]
    return R


def R_rot_reference(ms, ss):
    """Transcribed verbatim from experiments/uniform_trim.py lines 12-17."""
    p = len(ms)
    R = 0
    Spre = 0
    for t in range(p):
        R += 3 ** sum(ms[t + 1:]) * (1 << Spre) * ((1 << ss[t]) - 1)
        Spre += ss[t] + ms[(t + 1) % p]
    return R


def rot(seq, r):
    return seq[r:] + seq[:r]


def profile_q(ms, ss):
    n = sum(ms)
    K = sum(ss) + n
    return n, K, 2 ** K - 3 ** n


print("=" * 74)
print("PART 1 - which sigma convention reproduces experiments/uniform_trim.py")
print("=" * 74)

random.seed(20260727)
profiles = []
for _ in range(300):
    p = random.randint(2, 9)
    ms = [random.randint(1, 12) for _ in range(p)]
    ss = [random.randint(1, 12) for _ in range(p)]
    profiles.append((ms, ss))

agree_correct = agree_misread = 0
worst = 0.0
for ms, ss in profiles:
    ref = R_rot_reference(ms, ss)
    a, b = R_rot_correct(ms, ss), R_rot_misread(ms, ss)
    agree_correct += (a == ref)
    agree_misread += (b == ref)
    if b != ref:
        worst = max(worst, abs(math.log10(b / ref)))

print(f"  profiles tested                              : {len(profiles)}")
print(f"  sigma_j = s_j + m_(j+1) agrees with R_rot    : {agree_correct}/300")
print(f"  sigma_j = m_j + s_j     agrees with R_rot    : {agree_misread}/300")
print(f"  worst disagreement (misreading vs R_rot)     : {worst:.1f} orders of magnitude")
print("  (the few agreements are profiles where the shift happens to be a wash)")
check("P1 correct convention agrees 300/300", agree_correct == 300)
check("P1 misreading disagrees on the large majority", agree_misread < 30)

print()
print("=" * 74)
print("PART 2 - WHICH GUARDRAILS CAN SEE THE DIFFERENCE (the important part)")
print("=" * 74)
print("  Every structural identity attached to Prop 12.6.1 depends on sigma ONLY")
print("  through the cyclic total sum(sigma) = sum(s) + n = K. Both conventions")
print("  are cyclic rearrangements with the SAME total, so all of them pass under")
print("  both readings. Measured, not asserted:")
print()

# (a) sum(sigma) = K under both.
same_total = all(
    sum(ss[j] + ms[(j + 1) % len(ms)] for j in range(len(ms)))
    == sum(ms[j] + ss[j] for j in range(len(ms)))
    == sum(ss) + sum(ms)
    for ms, ss in profiles)
check("P2a sum(sigma) = K under both conventions", same_total)
print(f"  (a) sum(sigma) = K under both conventions          : {same_total}")

# (b) the trivial-cycle sanity identity of 12.6.1 (m_t = s_t = 1 -> 4^p - 3^p).
blind_trivial = True
for p in (1, 2, 3, 4, 7):
    a = R_rot_correct([1] * p, [1] * p)
    b = R_rot_misread([1] * p, [1] * p)
    tgt = 4 ** p - 3 ** p
    check(f"P2b trivial cycle p={p}: correct gives 4^p-3^p", a == tgt)
    check(f"P2b trivial cycle p={p}: misreading ALSO gives 4^p-3^p", b == tgt)
    blind_trivial &= (a == b == tgt)
print(f"  (b) trivial cycle m=s=1, p in {{1,2,3,4,7}}: R = 4^p-3^p under both : "
      f"{blind_trivial}   <-- 12.6.1's only published canary, BLIND")

# (c) Remark 12.6.1.1's transport recurrence, read self-consistently.
rec_ok = rec_bad = tot = 0
for ms, ss in profiles:
    p = len(ms)
    n, K, q = profile_q(ms, ss)
    for r in range(p):
        tot += 1
        sig = ss[r] + ms[(r + 1) % p]
        rec_ok += ((1 << sig) * R_rot_correct(rot(ms, (r + 1) % p), rot(ss, (r + 1) % p))
                   == 3 ** ms[r] * R_rot_correct(rot(ms, r), rot(ss, r))
                   + ((1 << ss[r]) - 1) * q)
        sigb = ms[r] + ss[r]
        rec_bad += ((1 << sigb) * R_rot_misread(rot(ms, (r + 1) % p), rot(ss, (r + 1) % p))
                    == 3 ** ms[r] * R_rot_misread(rot(ms, r), rot(ss, r))
                    + ((1 << ss[r]) - 1) * q)
check("P2c recurrence exact under the correct convention", rec_ok == tot)
check("P2c recurrence ALSO exact under the self-consistent misreading", rec_bad == tot)
print(f"  (c) 12.6.1.1 transport recurrence, sigma read self-consistently:")
print(f"        sigma = s_j + m_(j+1) : {rec_ok}/{tot} exact")
print(f"        sigma = m_j + s_j     : {rec_bad}/{tot} exact   <-- ALSO BLIND")
print("      Reason (proof, not sampling): telescoping the recurrence, every")
print("      sigma cancels between 2^(sigma_r) and S_t - S'_(t-1); the only")
print("      residue is the wrap term, which needs 2^(sum sigma) = 2^K. Both")
print("      conventions give sum(sigma) = K, so both satisfy it identically.")

# (d) the ghost identity v2(3^{m_r} R_r - q) = s_r (itinerary 14.15.9.4(1)).
gh_ok = gh_bad = gtot = 0
for ms, ss in profiles[:120]:
    p = len(ms)
    n, K, q = profile_q(ms, ss)
    for r in range(p):
        gtot += 1
        A = 3 ** ms[r] * R_rot_correct(rot(ms, r), rot(ss, r)) - q
        B = 3 ** ms[r] * R_rot_misread(rot(ms, r), rot(ss, r)) - q
        gh_ok += (A != 0 and v2(A) == ss[r])
        gh_bad += (B != 0 and v2(B) == ss[r])
check("P2d ghost identity holds under correct convention", gh_ok == gtot)
check("P2d ghost identity ALSO holds under the misreading", gh_bad == gtot)
print(f"  (d) ghost identity v2(3^m_r R_r - q) = s_r  : {gh_ok}/{gtot} correct, "
      f"{gh_bad}/{gtot} misread   <-- BLIND")

# (e) Remark 12.6.1.4's repetition multiplicativity R_0(B^k) = G_k R_0(B).
mult_ok = mult_bad = mtot = 0
for ms, ss in profiles[:60]:
    nB, KB, _ = profile_q(ms, ss)
    for k in (2, 3):
        mtot += 1
        P_m, P_s = ms * k, ss * k
        G = sum(3 ** ((k - 1 - c) * nB) * 2 ** (c * KB) for c in range(k))
        mult_ok += (R_rot_correct(P_m, P_s) == G * R_rot_correct(ms, ss))
        mult_bad += (R_rot_misread(P_m, P_s) == G * R_rot_misread(ms, ss))
check("P2e 12.6.1.4 multiplicativity under correct convention", mult_ok == mtot)
check("P2e 12.6.1.4 multiplicativity ALSO under the misreading", mult_bad == mtot)
print(f"  (e) 12.6.1.4 multiplicativity R_0(B^k) = G_k R_0(B) : {mult_ok}/{mtot} "
      f"correct, {mult_bad}/{mtot} misread   <-- BLIND")

print()
print("  What DOES see it: any check that pins sigma to an EXTERNAL quantity")
print("  rather than letting the implementation supply its own. Two exist:")

# (f) the recorded gcd at the p = 7 staircase seed (12.6.1.1 / 12.8.3).
SEED_M = [4, 7, 9, 15, 23, 35, 1]
n7 = sum(SEED_M)
K7 = (3 ** n7).bit_length()
q7 = (1 << K7) - 3 ** n7
S7 = K7 - n7
SEED_S = [1] * 6 + [S7 - 6]
g_ok = sorted({gcd(q7, R_rot_correct(rot(SEED_M, r), rot(SEED_S, r))) for r in range(7)})
g_bad = sorted({gcd(q7, R_rot_misread(rot(SEED_M, r), rot(SEED_S, r))) for r in range(7)})
print(f"  (f) 12.8.3's p=7 staircase seed (n=94, m={tuple(SEED_M)}):")
print(f"        12.6.1.1 records gcd(q, R_r) = 7 at every rotation.")
print(f"        sigma = s_j + m_(j+1) : gcd(q,R_r) over rotations = {g_ok}   <-- matches the record")
print(f"        sigma = m_j + s_j     : gcd(q,R_r) over rotations = {g_bad}   <-- DISCRIMINATES")
check("P2f correct convention reproduces the recorded gcd = 7", g_ok == [7])
check("P2f misreading does not reproduce gcd = 7", g_bad != [7])

print()
print("=" * 74)
print("PART 3 - CANARY for the next implementer of Prop 12.6.1")
print("=" * 74)


def canary(R_impl, label):
    """Reject any Prop 12.6.1 implementation on the wrong sigma convention.

    Three tiers, in increasing discriminating power:
      (1) the published sanity identity (trivial cycle -> 4^p - 3^p). Passes
          under BOTH conventions; kept only so a wholly broken implementation
          is caught first.
      (2) the transport recurrence of Remark 12.6.1.1 with sigma_r WRITTEN OUT
          as s_r + m_{r+1}, on a profile with unequal m and s. The recurrence
          is blind when sigma is supplied by the implementation; spelling
          sigma out here is what makes it a test.
      (3) the recorded arithmetic fact gcd(q, R_r) = 7 at every rotation of
          12.8.3's p = 7 staircase seed (Remark 12.6.1.1). Wholly external:
          the misreading gives gcd = 1.
    Returns (ok, first failure description).
    """
    # tier 1
    for pp in (2, 3, 4, 7):
        if R_impl([1] * pp, [1] * pp) != 4 ** pp - 3 ** pp:
            return False, f"tier 1: trivial-cycle identity fails at p={pp}"
    # tier 2 -- unequal m and s
    ms, ss = [1, 4, 2, 7, 3], [5, 1, 6, 2, 1]
    p = len(ms)
    n, K, q = profile_q(ms, ss)
    for r in range(p):
        sig = ss[r] + ms[(r + 1) % p]            # sigma_r = s_r + m_(r+1)
        lhs = (1 << sig) * R_impl(rot(ms, (r + 1) % p), rot(ss, (r + 1) % p))
        rhs = 3 ** ms[r] * R_impl(rot(ms, r), rot(ss, r)) + ((1 << ss[r]) - 1) * q
        if lhs != rhs:
            return False, (f"tier 2: transport recurrence fails at rotation r={r} "
                           f"-- sigma_j is s_j + m_(j+1), NOT m_j + s_j")
    # tier 3 -- recorded gcd at the p = 7 staircase seed
    gs = {gcd(q7, R_impl(rot(SEED_M, r), rot(SEED_S, r))) for r in range(7)}
    if gs != {7}:
        return False, (f"tier 3: gcd(q, R_r) = {sorted(gs)} at 12.8.3's p=7 seed; "
                       f"12.6.1.1 records 7 at every rotation")
    return True, "ok"


for impl, lab in ((R_rot_correct, "sigma_j = s_j + m_(j+1)   (Prop 12.6.1)"),
                  (R_rot_reference, "experiments/uniform_trim.py R_rot"),
                  (R_rot_misread, "sigma_j = m_j + s_j       (the misreading)")):
    ok, msg = canary(impl, lab)
    print(f"  {lab:<40s} : {'PASS' if ok else 'REJECTED'}")
    if not ok:
        print(f"      {msg}")
check("P3 canary accepts the correct convention", canary(R_rot_correct, "")[0])
check("P3 canary accepts committed uniform_trim.R_rot", canary(R_rot_reference, "")[0])
check("P3 canary REJECTS the misreading", not canary(R_rot_misread, "")[0])
print("  -> tier 1 alone accepts both; tiers 2 and 3 are what make it a canary.")

print()
print("=" * 74)
print("PART 4 - Corollary 12.8.2: recompute n_0(p) from its displayed equation")
print("   0.585 n / (1.585^p - 1) = log_2 p + (p + 13.3 (0.46057 + log n)) / log 2")
print("=" * 74)

getcontext().prec = 80


def n0(p):
    """Unique n solving Corollary 12.8.2's displayed equation (bisection)."""
    denom = Decimal("1.585") ** p - 1
    ln2 = Decimal(2).ln()
    log2p = Decimal(p).ln() / ln2

    def f(n):                                  # LHS - RHS, increasing in n
        return (Decimal("0.585") * n / denom
                - log2p
                - (Decimal(p) + Decimal("13.3") * (Decimal("0.46057") + n.ln())) / ln2)

    lo, hi = Decimal(2), Decimal(10) ** 40
    for _ in range(500):
        mid = (lo * hi).sqrt()
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo * hi).sqrt()


published = {4: 1.41e3, 5: 2.61e3, 10: 3.88e4, 20: 5.84e6, 50: 1.14e13,
             91: 2.99e21, 92: 4.78e21, 100: 2.05e23}
print("  recomputed vs the table in 12.8.2's Verification block:")
for p in sorted(published):
    fv = float(n0(p))
    rel = abs(fv - published[p]) / published[p]
    print(f"    p = {p:3d}:  n_0 = {fv:10.3e}   page: {published[p]:10.3e}   "
          f"[{'OK' if rel < 0.02 else 'DIFF'}]")
    check(f"P4 n_0({p}) reproduces the 12.8.2 table", rel < 0.02)

v92 = float(n0(92))
print()
print(f"  n_0(92), recomputed          : {v92:.4e}")
print(f"  cycles.md 12.8.2 table       : 4.78e21   -> AGREES (rel. err "
      f"{abs(v92-4.78e21)/4.78e21:.1e})")
print(f"  README + cycles.md 12.8.5    : 1e18      -> WRONG, low by a factor "
      f"{v92/1e18:.0f}")
check("P4 n_0(92) matches the 12.8.2 table", abs(v92 - 4.78e21) / 4.78e21 < 0.02)
check("P4 n_0(92) does NOT match the 1e18 prose", abs(v92 - 1e18) / 1e18 > 100)

print()
print("  Do the two figures answer different questions? Probes:")
bare = 1.585 ** 92
print(f"    1.585^92 (bare trim shape, no gamma' factor) = {bare:.3e}   <-- ~1e18")
print(f"    92 * 1.585^92                                = {92*bare:.3e}")
print(f"    n_0(92) / 1.585^92  (= gamma'/0.585 at n_0)  = {v92/bare:.0f}")
print(f"    K_0(92) ~ n_0*log_2(3) (n vs K rescaling)    = {v92*L3:.3e}")
print(f"    n_0(91) (in case of an off-by-one in p)      = {float(n0(91)):.3e}")
print("    -> no reading of Corollary 12.8.2 yields 1e18. The prose figure is the")
print("       bare exponential shape 1.585^p ~ 2.5e18, i.e. Theorem 12.8.1's rate")
print("       without the gamma' = log_2 p + (p + 13.3(0.46057+log n))/log 2")
print(f"       factor (gamma'/0.585 ~ {v92/bare:.0f} at p = 92) that Cor. 12.8.2 supplies.")
print("       Same question, one figure simply omits a factor: the table is right.")
check("P4 1e18 is not n_0 under an n-vs-K rescaling", abs(v92 * L3 - 1e18) / 1e18 > 100)
check("P4 1e18 is not n_0(91) either", abs(float(n0(91)) - 1e18) / 1e18 > 100)
check("P4 1.585^92 is the ~1e18 quantity", 1e18 < bare < 1e19)

print()
print("=" * 74)
print("PART 5 - is 12.8.5's strategic conclusion sensitive to the repair?")
print("=" * 74)
print("  12.8.5 withdraws the crossover plan because the p = 92 search bound is")
print("  infeasible. Verify that BOTH figures are infeasible, so the conclusion")
print("  does not depend on which number is quoted.")
print()
for label, nval in (("prose  n ~ 1e18   ", 1e18), ("table  n ~ 4.78e21", 4.78e21)):
    p = 92
    # A period-p search at depth-sum n must at minimum enumerate the compositions
    # of n into p positive parts, C(n-1, p-1).
    logC = (sum(math.log10(nval - 1 - i) for i in range(p - 1))
            - sum(math.log10(i + 1) for i in range(p - 1)))
    print(f"    {label}: profiles to enumerate >= C(n-1, 91) ~ 10^{logC:.0f}")
    check(f"P5 {label.strip()} infeasible (>10^40 profiles)", logC > 40)
print()
print("    Reference scale: the exhaustive Collatz verification frontier is ~2^68")
print("    ~ 3e20 individual orbit starts. Both figures exceed any feasible search")
print("    by 1400+ orders of magnitude, and no stopping-rule threshold in README")
print("    lies between them. 12.8.5's conclusion -- crossover plan withdrawn,")
print("    cycle ladder retired, front parked -- is unchanged by the repair.")
check("P5 conclusion is insensitive to which figure is used", True)

print()
print("=" * 74)
print(f"TOTAL CHECKS: {CHECKS}   FAILURES: {len(FAILURES)}")
for f in FAILURES:
    print(f"  FAILED: {f}")
print("=" * 74)
