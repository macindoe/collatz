"""
Single-sequence digit-structure search on the anchor M(omega).

Brief: briefs/anchor-digit-search-brief.md. Scope: anchors.md S17.7-17.9.
This file covers S17.8 item 1 (single-sequence statistics) and item 4's
cross-string correlate sweep. Compressibility/NIST battery is a separate
file (anchor_compressibility.py) per the brief's "each result gets fresh,
independently-written code" rule -- though both share nothing but the
generator, which both need and which is therefore duplicated rather than
imported, to keep each file independently runnable and self-contained.

Question under test: does a SINGLE M(omega), read as one bit string, show
internal structure -- run-length bias, autocorrelation, non-uniform
overlapping-window statistics? This is new territory: everything else in
the wiki (aeh.md S13) is a CROSS-SECTIONAL statistic averaged over many
different states/orbits. Nothing before this file has looked at one
anchor's own bit string as a standalone object.

Null model, stated precisely: M(omega)'s bits are modeled as an i.i.d.
fair-coin sequence (independent, P(bit=1)=1/2). This is the null every
test below is computed against; a rejection at a stated significance
level is evidence against this specific null, not proof of anything about
AEH (which is a cross-sectional, not single-sequence, hypothesis -- see
anchors.md S17.7's scope note).

Fresh implementation: the M(omega) generator computes the 2-adic
logarithm directly from its convergent series (stage1.md, remark after
Theorem 11.8.3.6.6) via 9^N(w) = w^-1, M(w) = N(w^2). It imports nothing
from digit_duality.py, anchor_increment.py, or any other script in this
repo (AGENTS.md house norm: fresh code per claim). Validated against the
independently-recorded worked-example table in anchors.md S17.7 (12
values, first 24 bits, lsb-first) -- see validate_against_reference().
"""
import random
import math
from scipy import stats

# ---------------------------------------------------------------------
# M(omega) generator: 2-adic log via its convergent power series.
# ---------------------------------------------------------------------

def v2(x):
    """2-adic valuation of a positive integer; None for x == 0."""
    if x == 0:
        return None
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def log2adic(x, M):
    """2-adic log(1+x) mod 2^M, for x with v2(x) >= 1, via the series
    sum_{i>=1} (-1)^(i+1) x^i / i (stage1.md, remark after 11.8.3.6.6).
    Division by i's odd part uses a modular inverse mod 2^M; division by
    i's power-of-2 part is a right shift, valid because v2(x^i) = i*v2(x)
    grows linearly in i while v2(i) grows only logarithmically, so
    v2(x^i) > v2(i) for every i >= 1 whenever v2(x) >= 1. Terms are
    dropped once their valuation certainly exceeds M (i*v2(x) >= M)."""
    mask = (1 << M) - 1
    x &= mask
    if x == 0:
        return 0
    vx = v2(x)
    total = 0
    xi = 1
    i = 0
    while True:
        i += 1
        xi = (xi * x) & mask
        if i * vx >= M:
            break
        e = v2(i) if i % 2 == 0 else 0
        j = i >> e
        term = ((xi >> e) * pow(j, -1, 1 << M)) & mask
        total = (total + term if i % 2 == 1 else total - term) & mask
    return total & mask


_log9_cache = {}


def _log9(M):
    if M not in _log9_cache:
        _log9_cache[M] = log2adic(8, M)
    return _log9_cache[M]


def compute_M_omega(omega, target_bits, margin=160):
    """Return M(omega) mod 2^target_bits as a nonnegative Python int
    (bit i of the return value is bit i of the 2-adic integer, lsb
    first). margin is extra working precision absorbed by the division
    by log(9) (which has valuation exactly 3) and by early series
    truncation; 160 bits of margin is far more than the <=3 bits any
    single division step can cost, kept generous for safety."""
    M = target_bits + 3 + margin
    mask = (1 << M) - 1
    y = (omega * omega) & mask
    x = (y - 1) & mask
    if x == 0:
        return 0  # omega == 1 (mod 2^M): the fixed point, M(omega) = 0 exactly
    Ly = log2adic(x, M)
    L9 = _log9(M)
    assert v2(L9) == 3, "log(9) must have 2-adic valuation exactly 3"
    ey = v2(Ly) if Ly != 0 else M
    assert ey >= 3, f"v2(log(omega^2)) = {ey} < 3 for omega={omega} (should be impossible for odd omega)"
    prec = M - 3
    pmask = (1 << prec) - 1
    u9 = (L9 >> 3) & pmask
    inv_u9 = pow(u9, -1, 1 << prec)
    Ly_shift = (Ly >> 3) & pmask
    N = (-(Ly_shift * inv_u9)) & pmask
    return N & ((1 << target_bits) - 1)


def bits_lsb_first(n, k):
    return [(n >> i) & 1 for i in range(k)]


def validate_against_reference():
    """Cross-check against the independently-recorded worked example in
    anchors.md S17.7 (computed in a prior session, first 24 bits,
    lsb-first as text strings of 0/1)."""
    reference = {
        1: "000000000000000000000000",
        3: "111111111111111111111111",
        5: "101011110100001111101100",
        7: "010010101101111111001101",
        11: "100110111000001010010011",
        13: "110111011010100100010110",
        17: "001100100100010001101100",
        19: "110000011010111111001110",
        23: "011001111111100000001110",
        29: "111011010111011110110011",
        31: "000101001100101110110001",
        37: "101101110100011110111111",
    }
    for omega, ref in reference.items():
        got = "".join(str(b) for b in bits_lsb_first(compute_M_omega(omega, 24), 24))
        assert got == ref, f"omega={omega}: got {got}, expected {ref}"
    return True


# ---------------------------------------------------------------------
# Sample generation
# ---------------------------------------------------------------------

def sample_omegas(n, seed, lo, hi):
    """n odd integers in [lo, hi), coprime to 3, drawn independently at
    random. 3 | omega is excluded because those omega are algebraically
    degenerate for this test by construction (omega a power of 3 times a
    unit makes M(omega) rational/eventually-periodic -- exactly the
    omega=3 case already flagged in anchors.md S17.7 as M(3)=-1 because
    3^2=9 is the log's own base; omega=9,15,21,... inherit related
    algebraic relations). This mirrors stage1.md's own restriction to
    3-nmid-omega families and keeps the sample in the genuinely-open
    'generic omega' regime the search is about, not in a family whose
    non-randomness is already explained. lo is kept well above the
    'bottom' regime (aeh.md S13.1's small-number drainage basin) so the
    sample targets typical, not degenerate, omega."""
    rng = random.Random(seed)
    out = []
    seen = set()
    while len(out) < n:
        w = rng.randrange(lo, hi) | 1
        if w % 3 == 0 or w in seen:
            continue
        seen.add(w)
        out.append(w)
    return out


# ---------------------------------------------------------------------
# Meta-analysis across many independent sequences (standard NIST SP
# 800-22 usage pattern: proportion-passing + p-value uniformity), used
# for every per-sequence test below so a single-sequence fluke can't be
# mistaken for a real finding.
# ---------------------------------------------------------------------

def meta_check(pvalues, alpha=0.01):
    n = len(pvalues)
    passed = sum(1 for p in pvalues if p >= alpha)
    p_hat = 1 - alpha
    se = math.sqrt(p_hat * (1 - p_hat) / n)
    ci = (p_hat - 3 * se, p_hat + 3 * se)
    prop = passed / n
    prop_ok = ci[0] <= prop <= ci[1]

    nbins = 10
    edges = [i / nbins for i in range(nbins + 1)]
    counts = [0] * nbins
    for p in pvalues:
        idx = min(int(p * nbins), nbins - 1)
        counts[idx] += 1
    expected = n / nbins
    chi2_stat = sum((c - expected) ** 2 / expected for c in counts)
    unif_p = stats.chi2.sf(chi2_stat, nbins - 1)
    unif_ok = unif_p >= 0.0001

    return dict(n=n, proportion_passing=prop, expected_ci=ci, proportion_ok=prop_ok,
                uniformity_chi2=chi2_stat, uniformity_pvalue=unif_p, uniformity_ok=unif_ok)


# ---------------------------------------------------------------------
# Test A: run-length distribution vs Geometric(1/2)
# ---------------------------------------------------------------------

def run_lengths(bits):
    runs = []
    cur = bits[0]
    length = 1
    for b in bits[1:]:
        if b == cur:
            length += 1
        else:
            runs.append(length)
            cur = b
            length = 1
    runs.append(length)
    return runs


def runlength_pooled_test(sequences, cap=14):
    """Pool run lengths across ALL sequences (0-runs and 1-runs together
    -- both are Geometric(1/2) under the null by symmetry) into one
    chi-squared goodness-of-fit test. Categories 1..cap-1 individually,
    cap+ as a tail bucket, chosen so every expected count is >= 5."""
    all_runs = []
    for bits in sequences:
        all_runs.extend(run_lengths(bits))
    total = len(all_runs)
    observed = [0] * cap
    for L in all_runs:
        observed[min(L, cap) - 1] += 1
    expected = [total * (0.5 ** l) for l in range(1, cap)]
    expected.append(total * (0.5 ** (cap - 1)))  # P(L >= cap) = 0.5^(cap-1)
    chi2_stat = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    df = cap - 1
    pval = stats.chi2.sf(chi2_stat, df)
    return dict(total_runs=total, chi2=chi2_stat, df=df, pvalue=pval,
                observed=observed, expected=expected)


def runlength_per_sequence_pvalues(sequences, cap=10):
    pvals = []
    for bits in sequences:
        runs = run_lengths(bits)
        total = len(runs)
        observed = [0] * cap
        for L in runs:
            observed[min(L, cap) - 1] += 1
        expected = [total * (0.5 ** l) for l in range(1, cap)]
        expected.append(total * (0.5 ** (cap - 1)))
        chi2_stat = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
        pvals.append(stats.chi2.sf(chi2_stat, cap - 1))
    return pvals


# ---------------------------------------------------------------------
# Test B: autocorrelation at lags 1..64
# ---------------------------------------------------------------------

def autocorr_pooled_test(sequences, max_lag=64):
    """For each lag k, pool A(k) = sum b_i*b_{i+k} (bits mapped to +-1)
    across all sequences; under the null E[A(k)]=0, Var[A(k)]=n-k per
    sequence, independent across sequences, so pooled_z(k) =
    sum_seq A(k) / sqrt(sum_seq (n_seq - k)) ~ N(0,1). Combine lags into
    one chi-squared statistic sum_k pooled_z(k)^2 ~ chi2(max_lag)
    (approximate: adjacent lags share bits and are not exactly
    independent, so this p-value is a standard approximation, not exact
    -- flagged here per the brief's rigor requirement, and cross-checked
    by the per-sequence meta-test and by the NIST DFT/spectral test in a
    separate stage)."""
    pm_sequences = [[1 if b else -1 for b in bits] for bits in sequences]
    n = len(pm_sequences[0])
    pooled_z = {}
    for k in range(1, max_lag + 1):
        total_A = 0
        total_var = 0
        for pm in pm_sequences:
            A = sum(pm[i] * pm[i + k] for i in range(n - k))
            total_A += A
            total_var += (n - k)
        pooled_z[k] = total_A / math.sqrt(total_var)
    chi2_stat = sum(z * z for z in pooled_z.values())
    pval = stats.chi2.sf(chi2_stat, max_lag)
    max_abs_z = max(abs(z) for z in pooled_z.values())
    bonferroni_z = stats.norm.ppf(1 - 0.05 / (2 * max_lag))
    return dict(chi2=chi2_stat, df=max_lag, pvalue=pval, pooled_z=pooled_z,
                max_abs_z=max_abs_z, bonferroni_threshold=bonferroni_z,
                any_lag_significant=max_abs_z > bonferroni_z)


def autocorr_per_sequence_pvalues(sequences, max_lag=64):
    pvals = []
    for bits in sequences:
        pm = [1 if b else -1 for b in bits]
        n = len(pm)
        chi2_stat = 0.0
        for k in range(1, max_lag + 1):
            A = sum(pm[i] * pm[i + k] for i in range(n - k))
            z = A / math.sqrt(n - k)
            chi2_stat += z * z
        pvals.append(stats.chi2.sf(chi2_stat, max_lag))
    return pvals


# ---------------------------------------------------------------------
# Test C: chi-squared on overlapping w-bit windows, w = 3, 4, 5
# ---------------------------------------------------------------------

def window_counts(bits, w):
    n = len(bits)
    counts = [0] * (1 << w)
    pat = 0
    for i in range(w):
        pat = (pat << 1) | bits[i % n]
    counts[pat] += 1
    for i in range(1, n):
        nb = bits[(i + w - 1) % n]
        pat = ((pat << 1) | nb) & ((1 << w) - 1)
        counts[pat] += 1
    return counts


def window_pooled_test(sequences, w):
    """Pool overlapping w-bit window counts (cyclic wrap, NIST Serial
    Test convention) across all sequences into one chi-squared test
    against the uniform null, df = 2^w - 1. Note: overlapping windows
    within a sequence are correlated (each bit appears in w windows), so
    this per-w chi-squared is the standard approximate form, not exact;
    it is cross-validated against nistrng's proper (overlap-corrected)
    Serial test in the compressibility-stage battery."""
    ncat = 1 << w
    total_counts = [0] * ncat
    total_n = 0
    for bits in sequences:
        c = window_counts(bits, w)
        for i in range(ncat):
            total_counts[i] += c[i]
        total_n += len(bits)
    expected = total_n / ncat
    chi2_stat = sum((c - expected) ** 2 / expected for c in total_counts)
    df = ncat - 1
    pval = stats.chi2.sf(chi2_stat, df)
    return dict(w=w, chi2=chi2_stat, df=df, pvalue=pval, total_n=total_n)


def window_per_sequence_pvalues(sequences, w):
    ncat = 1 << w
    pvals = []
    for bits in sequences:
        c = window_counts(bits, w)
        n = len(bits)
        expected = n / ncat
        chi2_stat = sum((x - expected) ** 2 / expected for x in c)
        pvals.append(stats.chi2.sf(chi2_stat, ncat - 1))
    return pvals


# ---------------------------------------------------------------------
# Simple monobit check (overall 1-density), reported alongside the above
# as a baseline sanity figure (matches stage1.md 11.8.4.2's density
# statistic, but computed fresh here, on the new sample).
# ---------------------------------------------------------------------

def monobit(sequences):
    total_ones = sum(sum(bits) for bits in sequences)
    total_bits = sum(len(bits) for bits in sequences)
    density = total_ones / total_bits
    z = (total_ones - total_bits / 2) / math.sqrt(total_bits / 4)
    pval = 2 * stats.norm.sf(abs(z))
    return dict(density=density, z=z, pvalue=pval, total_bits=total_bits)


# ---------------------------------------------------------------------
# Cross-string correlate sweep (S17.8 item 4): cheap candidate correlates
# beyond the already-refuted omega mod 3 (archive/appendix-a.md A.4.6).
# ---------------------------------------------------------------------

def correlate_sweep(omegas, sequences, bit_offset=0, width=24):
    """For each candidate residue class of omega, compare mean digit-sum
    of a `width`-bit window of M(omega) starting at `bit_offset` between
    classes, same methodology as the already-closed omega-mod-3 audit
    (A.4.6) applied to new candidates: omega mod 16, omega mod 32, digit
    sum of omega.

    IMPORTANT: omega mod 16/32 is a candidate correlate for the LEADING
    bits (bit_offset=0) only in the trivial, already-proven sense --
    M(omega)'s low-order bits are a deterministic function of a bounded
    number of omega's low-order bits (the digit-determinacy lemmas,
    stage4.md 11.8.7.2.1-3; the anchor being computable via a convergent
    series is exactly this). A dependence found at bit_offset=0 is a
    known law, not a discovery. The genuinely open test (per the brief,
    S17.8 item 4: "test the residual high-order digits ... beyond what
    the proved low-order law already accounts for") is the same sweep
    run at a bit_offset deep enough that no bounded window of omega
    could plausibly pin it (the digit-budget theorem, stage4.md
    11.8.7.7, says no FIXED window ever does, for any offset) -- callers
    should run this at bit_offset=0 for a known-positive control and
    again at a large bit_offset for the real test."""
    max_z_per_class_count = {}

    def zscores_for(groups, overall, se):
        return {r: (sum(v) / len(v) - overall) / (se / math.sqrt(len(v)))
                for r, v in groups.items() if len(v) >= 5}

    results = {}
    digitsums = [sum(bits[bit_offset:bit_offset + width]) for bits in sequences]
    overall = sum(digitsums) / len(digitsums)
    overall_var = sum((d - overall) ** 2 for d in digitsums) / (len(digitsums) - 1)
    se = math.sqrt(overall_var)

    for modulus in (16, 32):
        groups = {}
        for w, d in zip(omegas, digitsums):
            groups.setdefault(w % modulus, []).append(d)
        zscores = zscores_for(groups, overall, se)
        n_classes = len(zscores)
        max_z_per_class_count[f"omega_mod_{modulus}"] = n_classes
        results[f"omega_mod_{modulus}"] = dict(zscores=zscores, n_classes=n_classes,
                                                 max_abs_z=max(abs(z) for z in zscores.values()))

    def digitsum_omega(w):
        return bin(w).count("1")

    ds_groups = {}
    for w, d in zip(omegas, digitsums):
        ds_groups.setdefault(digitsum_omega(w) % 2, []).append(d)
    zscores = zscores_for(ds_groups, overall, se)
    results["omega_digitsum_parity"] = dict(zscores=zscores, n_classes=len(zscores),
                                             max_abs_z=max(abs(z) for z in zscores.values()))

    # attach Bonferroni thresholds so max|z| is judged against the right
    # number of simultaneous comparisons, not eyeballed against 1.96/2/3
    for name, res in results.items():
        k = res["n_classes"]
        res["bonferroni_threshold"] = stats.norm.ppf(1 - 0.05 / (2 * k))
        res["significant_after_correction"] = res["max_abs_z"] > res["bonferroni_threshold"]
    return results


# ---------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------

def main():
    print("Validating generator against anchors.md S17.7 worked example...")
    validate_against_reference()
    print("  OK: 12/12 reference values match.\n")

    N = 200
    BITS = 4096
    SEED = 20260712
    LO, HI = 1 << 20, 1 << 64
    print(f"Generating {N} independent omega in [{LO}, {HI}), coprime to 3, seed={SEED}...")
    omegas = sample_omegas(N, SEED, LO, HI)
    print(f"Computing M(omega) to {BITS} bits for each (fresh 2-adic-log series)...")
    sequences = [bits_lsb_first(compute_M_omega(w, BITS), BITS) for w in omegas]
    print("  done.\n")

    print("=== Monobit (overall digit density) ===")
    mb = monobit(sequences)
    print(f"  density={mb['density']:.5f}  z={mb['z']:.3f}  p={mb['pvalue']:.4f}  (n_bits={mb['total_bits']})\n")

    print("=== Test A: run-length distribution vs Geometric(1/2) ===")
    rl_pooled = runlength_pooled_test(sequences)
    print(f"  pooled: total_runs={rl_pooled['total_runs']}  chi2={rl_pooled['chi2']:.3f}  "
          f"df={rl_pooled['df']}  p={rl_pooled['pvalue']:.4f}")
    rl_pvals = runlength_per_sequence_pvalues(sequences)
    rl_meta = meta_check(rl_pvals)
    print(f"  meta (N={rl_meta['n']} sequences): proportion_passing={rl_meta['proportion_passing']:.4f} "
          f"(expect in {rl_meta['expected_ci']}, ok={rl_meta['proportion_ok']}); "
          f"uniformity p={rl_meta['uniformity_pvalue']:.4f} (ok={rl_meta['uniformity_ok']})\n")

    print("=== Test B: autocorrelation, lags 1..64 ===")
    ac_pooled = autocorr_pooled_test(sequences)
    print(f"  pooled: chi2={ac_pooled['chi2']:.3f}  df={ac_pooled['df']}  p={ac_pooled['pvalue']:.4f}  "
          f"max|z|={ac_pooled['max_abs_z']:.3f}  bonferroni_thresh={ac_pooled['bonferroni_threshold']:.3f}  "
          f"any_lag_significant={ac_pooled['any_lag_significant']}")
    ac_pvals = autocorr_per_sequence_pvalues(sequences)
    ac_meta = meta_check(ac_pvals)
    print(f"  meta (N={ac_meta['n']} sequences): proportion_passing={ac_meta['proportion_passing']:.4f} "
          f"(expect in {ac_meta['expected_ci']}, ok={ac_meta['proportion_ok']}); "
          f"uniformity p={ac_meta['uniformity_pvalue']:.4f} (ok={ac_meta['uniformity_ok']})\n")

    print("=== Test C: overlapping w-bit window chi-squared, w=3,4,5 ===")
    print("    (overlapping windows share bits, so consecutive window-pattern draws are")
    print("    correlated and the naive df=2^w-1 chi-squared null is only approximate --")
    print("    flagged in window_pooled_test's docstring before this was run. Confirmed below")
    print("    by running the identical test on a matched true-random control: if the control")
    print("    fails the same way M(omega) does, the failure is this test's own approximation,")
    print("    not a property of M(omega).)")
    control_rng = random.Random(SEED + 99)
    controls = [[control_rng.randint(0, 1) for _ in range(BITS)] for _ in range(N)]
    for w in (3, 4, 5):
        wp = window_pooled_test(sequences, w)
        wpv = window_per_sequence_pvalues(sequences, w)
        wm = meta_check(wpv)
        wpv_c = window_per_sequence_pvalues(controls, w)
        wm_c = meta_check(wpv_c)
        artifact = not (wm_c["proportion_ok"] and wm_c["uniformity_ok"])
        flag = "ARTIFACT (control fails identically)" if artifact else (
            "OK" if (wm["proportion_ok"] and wm["uniformity_ok"]) else "REVIEW -- control passes, M(omega) does not")
        print(f"  w={w}: pooled chi2={wp['chi2']:.3f} df={wp['df']} p={wp['pvalue']:.4f}")
        print(f"        M(omega): prop_passing={wm['proportion_passing']:.4f} unif_p={wm['uniformity_pvalue']:.4f} | "
              f"control: prop_passing={wm_c['proportion_passing']:.4f} unif_p={wm_c['uniformity_pvalue']:.4f}  [{flag}]")
    print()

    print("=== Cross-string correlate sweep (S17.8 item 4) ===")
    print("  -- shallow window (bits 0-24): known-law control, dependence here is EXPECTED --")
    cs_shallow = correlate_sweep(omegas, sequences, bit_offset=0, width=24)
    for name, res in cs_shallow.items():
        print(f"  {name}: max|z|={res['max_abs_z']:.3f}  bonferroni_thresh={res['bonferroni_threshold']:.3f} "
              f"(k={res['n_classes']} classes)  significant={res['significant_after_correction']}")
    print("  -- deep window (bits 2000-2024): genuinely-open region, per brief S17.8 item 4 --")
    cs_deep = correlate_sweep(omegas, sequences, bit_offset=2000, width=24)
    for name, res in cs_deep.items():
        print(f"  {name}: max|z|={res['max_abs_z']:.3f}  bonferroni_thresh={res['bonferroni_threshold']:.3f} "
              f"(k={res['n_classes']} classes)  significant={res['significant_after_correction']}")
    print()

    return dict(omegas=omegas, sequences=sequences, monobit=mb, runlength_pooled=rl_pooled,
                runlength_meta=rl_meta, autocorr_pooled=ac_pooled, autocorr_meta=ac_meta,
                correlate_shallow=cs_shallow, correlate_deep=cs_deep)


if __name__ == "__main__":
    main()
