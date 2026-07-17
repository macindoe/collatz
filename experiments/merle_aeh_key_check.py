"""Merle round 3, item 5: our key on his L4 (AEH cross-verification).

Supports: briefs/merle-round3-check-findings.md (queue item 5 of
briefs/merle-round3-check-brief.md), 2026-07-18.

Fresh code per AGENTS.md: imports nothing from aeh_calibration.py,
aeh_anomaly.py, or any other committed script. The reduced map F is
implemented directly from spine.md section 9's laws (Proposition 9.1.1:
A = 3^d w - 1, s = v2(A), x_exit = A / 2^s; projection R: x + 1 =
2^m 3^a w). All dynamics are exact integer arithmetic; floats appear
only in the measurement layer (log2 drifts, frequencies, and the
class-level transfer-matrix spectrum), which is a MEASUREMENT, not a
proof -- labeled as such throughout, per the brief.

Protocol (his, at his scale, no bigger): 3000 orbits, odd uniform
starts in [2^55, 2^56), fixed seed 20260718; bottom-regime cut at
x_exit > 2^20 and a 2^30 control. Then our own calibration methodology
(aeh.md 13.5's decisive-test protocol: fixed horizon, unweighted, no
stopping rule) on the same orbit population, as the test of his
survivorship-bias attribution for the drift artifact.

Measured objects:
  (a) canaries: F(1,1) = (1,1); the block of 7 exits at 13.
  (c) class skeleton: (1 mod 8, d odd) -> d_next = 1 (exact theorem,
      paper sec:aeh / aeh.md 13.2); (5 mod 8, d odd) -> P(d_next even)
      vs exact 2/3; P(s = j) vs 2^-j; the 8-class transfer matrix
      (w mod 8 in {1,3,5,7} x d parity) and |lambda_2| at both cuts.
  (d) drift per step under his cut protocol -- five estimator
      variants: per F-step / per odd step, each crossing-included and
      censored-both-ends (per-transition conditioning), plus the
      survivor-averaged altitude slope (per-orbit-survival
      conditioning, the estimator family his survivorship-bias
      attribution names) -- vs the fixed-horizon protocol (pooled
      per-visit, no ratio-over-correlated-visits estimators, per
      aeh.md 13.5's standing rule), on the same orbit population and
      on an altitude-control population (starts 2^80, same seed
      construction). Theoretical identities under pi_k: per odd
      (T-)step log2(3) - 2 = -0.4150 (E[v2(3x+1)] = 2, the ledger
      P(s=j) = 2^-j, aeh.md 13.2/13.3.2); per F-step (per block)
      E[m] log2(3) - E[m] - E[s] = 2(log2(3) - 2) = -0.8301
      (E[m] = E[s] = 2 under pi_k).

Run:  python experiments/merle_aeh_key_check.py     (~20 s)
"""

import math
import random

import numpy as np  # measurement layer only (transfer-matrix spectrum)

SEED = 20260718
N_ORBITS = 3000
START_LO, START_HI = 1 << 55, 1 << 56
CUTS = (1 << 20, 1 << 30)
FLOOR = 4                # record transitions until x <= 4 (whole descent)
HORIZON = 15             # fixed-horizon protocol: exactly 15 F-steps
CTRL_LO, CTRL_HI = 1 << 80, 1 << 81   # altitude-control starts
CTRL_HORIZON = 25
LOG2_3 = math.log2(3.0)

CHECKS = {"count": 0, "fail": 0}


def check(cond, label):
    CHECKS["count"] += 1
    if not cond:
        CHECKS["fail"] += 1
        print(f"FAIL: {label}")
    return cond


def v2(x):
    return (x & -x).bit_length() - 1


def v3(x):
    a = 0
    while x % 3 == 0:
        x //= 3
        a += 1
    return a


def R_state(x):
    """Projection R (spine.md 9 / paper eq. defs): x + 1 = 2^m 3^a w,
    3 not| w; R(x) = (w, m + a)."""
    m = v2(x + 1)
    u = (x + 1) >> m
    a = v3(u)
    return u // 3 ** a, m + a


def F_exit(w, d):
    """One reduced step from state (w, d): A = 3^d w - 1, s = v2(A),
    x_exit = A / 2^s (Proposition 9.1.1)."""
    A = 3 ** d * w - 1
    s = v2(A)
    return A >> s, s


def canaries():
    print("=" * 72)
    print("(a) Canaries (his two, against direct computation)")
    print("=" * 72)
    x, s = F_exit(1, 1)
    check((x, s) == (1, 1) and R_state(x) == (1, 1), "F(1,1) = (1,1)")
    print(f"F(1,1): A = 3*1-1 = 2, s = {s}, x_exit = {x}, "
          f"R(x_exit) = {R_state(x)}  -> (1,1) confirmed")
    w7, d7 = R_state(7)
    x7, s7 = F_exit(w7, d7)
    check((w7, d7) == (1, 3), "R(7) = (1,3)")
    check(x7 == 13, "block of 7 exits at 13")
    print(f"7: R(7) = {(w7, d7)} (7+1 = 2^3), block exit = "
          f"(3^3*1 - 1)/2^{s7} = {x7}  -> exits at 13 confirmed")


# ---------------------------------------------------------------------
# Orbit generation: one pass, transitions recorded exactly.
# ---------------------------------------------------------------------

def generate_orbits(lo=START_LO, hi=START_HI, n=N_ORBITS):
    """Per orbit: list of transitions (x_prev, x_next, m, s, cls_prev,
    cls_next, d_next), where m = v2(x_prev + 1) = odd (T-)steps spent
    in the block, cls = (w mod 8, d mod 2). Exact integers."""
    rng = random.Random(SEED)
    orbits = []
    for _ in range(n):
        x = rng.randrange(lo | 1, hi, 2)
        w, d = R_state(x)
        trans = []
        while x > FLOOR:
            cls = (w % 8, d % 2)
            m = v2(x + 1)
            x2, s = F_exit(w, d)
            w2, d2 = R_state(x2)
            trans.append((x, x2, m, s, cls, (w2 % 8, d2 % 2), d2))
            x, w, d = x2, w2, d2
        orbits.append(trans)
    return orbits


# ---------------------------------------------------------------------
# (c) class skeleton + transfer-matrix spectrum, per cut.
# ---------------------------------------------------------------------

CLASSES = [(w, par) for w in (1, 3, 5, 7) for par in (1, 0)]
CIDX = {c: i for i, c in enumerate(CLASSES)}


def skeleton_and_spectrum(orbits, cut):
    print("-" * 72)
    print(f"Bulk protocol, cut x_exit > 2^{cut.bit_length()-1} "
          f"(transition counted while the source exit exceeds the cut)")
    print("-" * 72)
    n_trans = 0
    c1_tot = c1_hit = 0      # (1 mod 8, d odd) -> d_next = 1
    c5_tot = c5_even = 0     # (5 mod 8, d odd) -> d_next even
    s_hist = {}
    M = np.zeros((8, 8))
    per_orbit_c5 = []
    for trans in orbits:
        o5t = o5e = 0
        for (x, x2, m, s, cls, cls2, d2) in trans:
            if x <= cut:
                continue
            n_trans += 1
            s_hist[s] = s_hist.get(s, 0) + 1
            M[CIDX[cls], CIDX[cls2]] += 1
            if cls == (1, 1):
                c1_tot += 1
                c1_hit += d2 == 1
            elif cls == (5, 1):
                c5_tot += 1
                c5_even += d2 % 2 == 0
                o5t += 1
                o5e += d2 % 2 == 0
        if o5t:
            per_orbit_c5.append(o5e / o5t)
    print(f"transitions counted: {n_trans} over {len(orbits)} orbits")
    check(c1_hit == c1_tot and c1_tot > 0,
          f"(1 mod 8, d odd) -> d_next = 1, {c1_hit}/{c1_tot}")
    print(f"(1 mod 8, d odd) -> d_next = 1: {c1_hit} of {c1_tot} "
          f"(exact theorem; his 15,515 of 15,515)")
    p5 = c5_even / c5_tot
    se_pool = math.sqrt(p5 * (1 - p5) / c5_tot)
    po = np.array(per_orbit_c5)
    se_orbit = po.std(ddof=1) / math.sqrt(len(po))
    print(f"(5 mod 8, d odd) -> P(d_next even) = {p5:.4f} "
          f"+/- {se_pool:.4f} (pooled binomial SE; per-orbit-mean SE "
          f"{se_orbit:.4f}) vs exact 2/3 = {2/3:.4f}  "
          f"[his 0.6626 +/- 0.0074]; n = {c5_tot}")
    check(abs(p5 - 2 / 3) < 4 * se_pool, "(5,odd) P(even) within 4 SE of 2/3")
    print("P(s = j) vs 2^-j (pooled frequencies; float display):")
    for j in range(1, 9):
        f = s_hist.get(j, 0) / n_trans
        exp = 2.0 ** -j
        z = (f - exp) / math.sqrt(exp * (1 - exp) / n_trans)
        print(f"  s = {j}: {f:.5f} vs {exp:.5f}   z = {z:+.1f}")
    # Transfer matrix and spectrum (MEASUREMENT, floats, labeled).
    rows = M.sum(axis=1)
    P = M / rows[:, None]
    ev = np.linalg.eigvals(P)
    mags = sorted(np.abs(ev), reverse=True)
    print(f"class transfer matrix (8 classes = w mod 8 x d parity), "
          f"row counts {rows.astype(int).tolist()}")
    print(f"eigenvalue moduli (float measurement, not a proof): "
          f"{[f'{v:.4f}' for v in mags]}")
    print(f"|lambda_2| = {mags[1]:.4f}   spectral gap 1 - |lambda_2| = "
          f"{1 - mags[1]:.4f}   [his: |lambda_2| <= 0.06 at both cuts]")
    check(abs(mags[0] - 1.0) < 1e-9, "lambda_1 = 1 (row-stochastic)")
    return mags[1]


# ---------------------------------------------------------------------
# (d) drift: his cut protocol (4 variants) vs our fixed-horizon rule.
# ---------------------------------------------------------------------

def drift_cut_transition_variants(orbits, cut):
    """Per-transition conditioning on the cut, pooled per-visit means.
    SEs from per-orbit sums (orbits independent; cluster-robust).
    These are deliberately biased estimators -- they replicate the
    artifact space, they are not the page's methodology."""
    res = {}
    for censored in (False, True):
        sums = []  # per orbit: (dl_sum, n_f, m_sum)
        for trans in orbits:
            dl = nf = mm = 0
            for (x, x2, m, s, cls, cls2, d2) in trans:
                if x <= cut or (censored and x2 <= cut):
                    continue
                dl += math.log2(x2) - math.log2(x)
                nf += 1
                mm += m
            if nf:
                sums.append((dl, nf, mm))
        a = np.array(sums)
        for name, den in (("per F-step", a[:, 1]), ("per odd step", a[:, 2])):
            mean = a[:, 0].sum() / den.sum()
            # cluster SE via per-orbit residuals of the pooled ratio
            resid = a[:, 0] - mean * den
            se = math.sqrt((resid ** 2).sum()) / den.sum()
            res[(censored, name)] = (mean, se)
    return res


def drift_survivor_slope(orbits, cut, min_survivors=100):
    """Survivor-averaged altitude slope: A(t) = mean log2 x_t over the
    orbits still above the cut at step t; least-squares slope of A(t)
    over the t-range with >= min_survivors survivors. This conditions
    on per-orbit survival -- the estimator family the survivorship-bias
    attribution names. Per F-step; the per-odd-step version divides by
    the pooled E[m] among counted visits."""
    A, t = [], 0
    while True:
        vals = [math.log2(tr[t][0]) for tr in orbits
                if t < len(tr) and tr[t][0] > cut]
        if len(vals) < min_survivors:
            break
        A.append(sum(vals) / len(vals))
        t += 1
    ts = np.arange(len(A))
    slope = np.polyfit(ts, A, 1)[0]
    msum = sum(m for tr in orbits for (x, x2, m, *_) in tr if x > cut)
    nsum = sum(1 for tr in orbits for (x, x2, m, *_) in tr if x > cut)
    return slope, slope / (msum / nsum), len(A), msum / nsum


def drift_fixed_horizon(orbits, horizon, label):
    """aeh.md 13.5's decisive-test protocol: fixed horizon (exactly
    `horizon` F-steps from the start), unweighted, per-visit pooling,
    no stopping rule, no cut. No per-orbit ratio estimators (13.5's
    standing rule): pooled means with cluster SEs from per-orbit sums;
    the per-odd-step figure is the pooled ratio sum(dlog2)/sum(m),
    reported with its two pooled components."""
    sums = []
    min_alt = None
    for trans in orbits:
        seg = trans[:horizon]
        check(len(seg) == horizon, f"{label}: orbit covers the horizon")
        dl = sum(math.log2(x2) - math.log2(x) for (x, x2, *_) in seg)
        mm = sum(m for (_, _, m, *_) in seg)
        ss = sum(s for (_, _, _, s, *_) in seg)
        sums.append((dl, mm, ss))
        alt = min(x2 for (_, x2, *_) in seg)
        min_alt = alt if min_alt is None else min(min_alt, alt)
    a = np.array(sums)
    n_orb = len(a)
    n_vis = n_orb * horizon
    mf = a[:, 0].sum() / n_vis
    sef = a[:, 0].std(ddof=1) / horizon / math.sqrt(n_orb)
    Em = a[:, 1].sum() / n_vis
    Es = a[:, 2].sum() / n_vis
    mo = a[:, 0].sum() / a[:, 1].sum()
    resid = a[:, 0] - mo * a[:, 1]
    seo = math.sqrt((resid ** 2).sum()) / a[:, 1].sum()
    return mf, sef, mo, seo, Em, Es, min_alt


def drift_report(orbits):
    print("=" * 72)
    print("(d) The drift artifact: his cut protocol vs our calibration "
          "methodology")
    print("=" * 72)
    th_odd = LOG2_3 - 2
    th_f = 2 * (LOG2_3 - 2)
    print(f"theoretical identities under pi_k: per odd (T-)step "
          f"log2(3) - 2 = {th_odd:.4f} (E[v2(3x+1)] = 2, the ledger "
          f"P(s=j) = 2^-j; aeh.md 13.2/13.3.2, paper sec:aeh); per "
          f"F-step (per block) E[m]log2(3) - E[m] - E[s] = "
          f"2(log2(3) - 2) = {th_f:.4f} (E[m] = E[s] = 2 under pi_k)")
    print(f"[his artifact numbers: -0.33/-0.36 'drift-per-step' at the "
          f"two cuts, against a stated theoretical -0.415]")
    for cut in CUTS:
        res = drift_cut_transition_variants(orbits, cut)
        print(f"-- cut x_exit > 2^{cut.bit_length()-1} (all cut-protocol "
              f"estimators are biased by construction; measurement) --")
        for censored in (False, True):
            lbl = ("censored (both endpoints above cut)" if censored
                   else "crossing-included (source above cut)")
            for name in ("per F-step", "per odd step"):
                mean, se = res[(censored, name)]
                print(f"  {lbl:44s} {name:13s}: {mean:+.4f} +/- {se:.4f}")
        sl_f, sl_odd, Tlen, Em = drift_survivor_slope(orbits, cut)
        print(f"  {'survivor-averaged altitude slope':44s} "
              f"{'per F-step':13s}: {sl_f:+.4f}   (LSQ over {Tlen} steps, "
              f">=100 survivors; pooled E[m] = {Em:.3f})")
        print(f"  {'survivor-averaged altitude slope':44s} "
              f"{'per odd step':13s}: {sl_odd:+.4f}")
    print(f"-- fixed-horizon protocol (aeh.md 13.5 standing rule): "
          f"T = {HORIZON} F-steps, unweighted, per-visit pooling, no "
          f"stopping rule, no cut --")
    mf, sef, mo, seo, Em, Es, min_alt = drift_fixed_horizon(
        orbits, HORIZON, "main")
    print(f"  same population (starts 2^55..2^56): minimum altitude "
          f"visited 2^{math.log2(min_alt):.1f}")
    print(f"  {'fixed horizon':44s} {'per F-step':13s}: {mf:+.4f} +/- "
          f"{sef:.4f}   (theory {th_f:.4f}, z = {(mf-th_f)/sef:+.1f})")
    print(f"  {'fixed horizon':44s} {'per odd step':13s}: {mo:+.4f} +/- "
          f"{seo:.4f}   (theory {th_odd:.4f}, z = {(mo-th_odd)/seo:+.1f})")
    print(f"  pooled E[m] = {Em:.4f}, E[s] = {Es:.4f}  (theory 2, 2)")
    check(abs(mf - th_f) < 4 * sef,
          "fixed-horizon per-F-step drift within 4 SE of 2(log2(3) - 2)")
    check(abs(mo - th_odd) < 4 * seo,
          "fixed-horizon per-odd-step drift within 4 SE of log2(3) - 2")
    print(f"  altitude control (starts 2^80..2^81, T = {CTRL_HORIZON}, "
          f"same seed construction):")
    ctrl = generate_orbits(CTRL_LO, CTRL_HI, N_ORBITS)
    mf2, sef2, mo2, seo2, Em2, Es2, min2 = drift_fixed_horizon(
        ctrl, CTRL_HORIZON, "control")
    print(f"  {'fixed horizon (control)':44s} {'per F-step':13s}: "
          f"{mf2:+.4f} +/- {sef2:.4f}   (z = {(mf2-th_f)/sef2:+.1f}; "
          f"min altitude 2^{math.log2(min2):.1f})")
    print(f"  {'fixed horizon (control)':44s} {'per odd step':13s}: "
          f"{mo2:+.4f} +/- {seo2:.4f}   (z = {(mo2-th_odd)/seo2:+.1f})")
    print(f"  pooled E[m] = {Em2:.4f}, E[s] = {Es2:.4f}")
    check(abs(mf2 - th_f) < 4 * sef2,
          "control per-F-step drift within 4 SE of 2(log2(3) - 2)")
    check(abs(mo2 - th_odd) < 4 * seo2,
          "control per-odd-step drift within 4 SE of log2(3) - 2)")


if __name__ == "__main__":
    import time
    t0 = time.time()
    canaries()
    print()
    print(f"protocol: {N_ORBITS} orbits, odd uniform starts in "
          f"[2^55, 2^56), seed {SEED}, transitions recorded for the "
          f"whole descent (until x <= {FLOOR}); cuts 2^20 and 2^30")
    orbits = generate_orbits()
    n_tot = sum(len(t) for t in orbits)
    print(f"orbits generated: {len(orbits)}, total transitions {n_tot}")
    lam = {}
    for cut in CUTS:
        lam[cut] = skeleton_and_spectrum(orbits, cut)
    drift_report(orbits)
    dt = time.time() - t0
    print("=" * 72)
    print(f"TOTAL: {CHECKS['count']} checks, {CHECKS['fail']} failures, "
          f"{dt:.1f} s  (2026-07-18, seed {SEED}; spectrum and drift "
          f"columns are float measurements, labeled; all dynamics exact "
          f"integers)")
