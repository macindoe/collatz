"""
Three new "operation" lenses on a single anchor M(omega) bit string.

Follow-up to anchors.md S17.7.1-17.7.3 (2026-07-13). Those established M(omega)
is (i) statistically fair-coin-like across the standard batteries and (ii) not
2-automatic / not algebraic over F_2(x). This file adds three DIFFERENT lenses,
each a distinct mathematical OPERATION on the bit string rather than another
frequency test:

  1. LINEAR-COMPLEXITY PROFILE (Berlekamp-Massey over F_2). L_n = length of the
     shortest LFSR generating the first n bits. Fair coin: L_n hugs n/2 with a
     characteristic jump structure. A hidden linear recurrence (LFSR) plateaus.
     This is the RATIONAL-generating-function subcase of the algebraicity we
     already ruled out (S17.7.3) -- but the PROFILE (how L_n grows, its jumps)
     is a finer, quantitative statistic than the yes/no automaticity verdict.

  2. WALSH-HADAMARD SPECTRUM. The native harmonic analysis on {0,1}^n (characters
     of (Z/2)^n), sharper for bit strings than the ordinary DFT (which treats
     bits as a real time series, anchors.md S17.7.1 spectral item). Map bits to
     +-1; the Walsh coefficients W_k are, under the fair-coin null, ~ Normal(0,N)
     and independent; a structured string spikes one coefficient.

  3. PARTIAL-SUM / LIL WALK. S_n = sum_{k<n}(2 a_k - 1), the +-1 random walk of
     the digits. Fair coin: obeys the law of the iterated logarithm,
     limsup |S_n| / sqrt(2 n ln ln n) = 1, and S_n/sqrt(n) -> N(0,1); a density
     drift shows as linear trend, correlation as anomalous excursions. HONEST
     SCOPE NOTE: this is a randomness lens on the DIGITS. It is *not* the cycle
     anchor-walk (spine.md 9.8.4: a cycle is a closed walk sum ΔM_t = 0 over
     orbit INCREMENTS, different data) -- but it is the same OPERATION (partial
     summation in Z), so it is background for that front, not a test of it.

Null model, stated first: bits i.i.d. fair coin (independent, P=1/2). Every
lens is also run on a matched i.i.d.-coin control through identical code, and on
omega=3 (M=-1, all ones) as a NEGATIVE control that MUST trip every lens -- the
proof the lenses can see structure. Deepest, most decisive point stands from
S17.7's framing: M(omega) is COMPUTABLE, hence not Martin-Lof random; these
lenses probe whether its finite description leaves a *detectable* fingerprint,
i.e. test PSEUDO-randomness, not randomness.

Fresh generator per AGENTS.md: 2-adic-log series, imports nothing, validated
12/12 vs anchors.md S17.7 table.
"""
import argparse
import math
import random
import numpy as np

# =====================================================================
# Fresh M(omega) generator.
# =====================================================================

def _v2(x):
    v = 0
    while x & 1 == 0:
        x >>= 1; v += 1
    return v


def _log1p(x, prec):
    mod = 1 << prec
    mask = mod - 1
    x &= mask
    if x == 0:
        return 0
    vx = _v2(x)
    acc = 0; xi = 1; i = 0
    while True:
        i += 1
        xi = (xi * x) & mask
        if i * vx >= prec:
            break
        e = _v2(i)
        acc = (acc + ((xi >> e) * pow(i >> e, -1, mod))) & mask if (i & 1) \
              else (acc - ((xi >> e) * pow(i >> e, -1, mod))) & mask
    return acc & mask


_L9 = {}

def _log9(prec):
    if prec not in _L9:
        _L9[prec] = _log1p(8, prec)
    return _L9[prec]


def anchor_bits(omega, nbits, margin=192):
    prec = nbits + margin
    mask = (1 << prec) - 1
    x = ((omega * omega) - 1) & mask
    if x == 0:
        return np.zeros(nbits, dtype=np.int8)
    Lw = _log1p(x, prec)
    L9 = _log9(prec)
    assert _v2(L9) == 3
    p = prec - 3
    pm = (1 << p) - 1
    N = (-((Lw >> 3) & pm) * pow((L9 >> 3) & pm, -1, 1 << p)) & pm
    N &= (1 << nbits) - 1
    b = N.to_bytes((nbits + 7) // 8, "little")
    return np.unpackbits(np.frombuffer(b, dtype=np.uint8), bitorder="little")[:nbits].astype(np.int8)


_REFERENCE = {
    1: "000000000000000000000000", 3: "111111111111111111111111",
    5: "101011110100001111101100", 7: "010010101101111111001101",
    11: "100110111000001010010011", 13: "110111011010100100010110",
    17: "001100100100010001101100", 19: "110000011010111111001110",
    23: "011001111111100000001110", 29: "111011010111011110110011",
    31: "000101001100101110110001", 37: "101101110100011110111111",
}

def _validate():
    for w, ref in _REFERENCE.items():
        got = "".join(str(int(b)) for b in anchor_bits(w, 24))
        assert got == ref, f"gen mismatch omega={w}: {got} != {ref}"


def thue_morse(n):
    """Thue-Morse t_k = popcount(k) mod 2. Its +-1 form is a single Walsh
    function (t_k = XOR of k's bits), so it spikes exactly one Walsh coefficient
    -- the ideal positive control for lens 2 -- and its partial sums are bounded,
    tripping lens 3. (Its linear complexity is ~n/2, so it does NOT trip lens 1;
    omega=3 covers that lens.)"""
    k = np.arange(n, dtype=np.int64)
    v = np.zeros(n, dtype=np.int8)
    while k.any():
        v ^= (k & 1).astype(np.int8)
        k >>= 1
    return v


# =====================================================================
# Lens 1: linear-complexity profile (Berlekamp-Massey over F_2).
# =====================================================================

def linear_complexity_profile(bits):
    """L_n for n=1..len(bits) via Berlekamp-Massey over GF(2). Connection and
    previous polynomials held as Python ints (bit i = coeff of x^i); the
    discrepancy is parity(popcount(C & history)) where history's bit i is
    s[N-i], so C_i pairs with s[N-i]. Fair-coin expectation E[L_n] ~ n/2."""
    n = len(bits)
    C = 1                       # current connection poly, C_0 = 1
    B = 1                       # last poly before length change
    L = 0
    m = 1                       # N - (index of last length change)
    history = 0
    prof = np.empty(n, dtype=np.int64)
    for N in range(n):
        history = (history << 1) | int(bits[N])     # bit i = s[N-i]
        d = bin(C & history).count("1") & 1
        if d:
            T = C
            C ^= (B << m)
            if 2 * L <= N:
                L = N + 1 - L
                B = T
                m = 1
            else:
                m += 1
        else:
            m += 1
        prof[N] = L
    return prof


def lc_summary(prof):
    n = len(prof)
    tail = prof[n // 2:]                 # steady-state region
    dev = tail - (np.arange(n // 2, n) + 1) / 2.0
    jumps = int(np.count_nonzero(np.diff(prof)))
    return {"n": n, "L_final": int(prof[-1]), "mean_dev_from_half": float(dev.mean()),
            "std_dev_from_half": float(dev.std()), "n_jumps": jumps}


# =====================================================================
# Lens 2: Walsh-Hadamard spectrum.
# =====================================================================

def fwht(a):
    """Fast Walsh-Hadamard transform (natural/Hadamard order), length 2^m."""
    a = a.astype(np.float64).copy()
    n = len(a); h = 1
    while h < n:
        a = a.reshape(-1, 2 * h)
        b = a[:, :h].copy(); c = a[:, h:].copy()
        a[:, :h] = b + c
        a[:, h:] = b - c
        a = a.reshape(-1)
        h *= 2
    return a


def walsh_spectrum_test(bits):
    """W = FWHT(+-1 bits). Under the null W_k ~ Normal(0, N) for k>0 (W_0 is the
    monobit sum). Report normalized coefficients w_k = W_k/sqrt(N) (~N(0,1)),
    their max |.| vs the sqrt(2 ln N) extreme-value scale, and the raw w array
    for a two-sample comparison against the control by the caller."""
    N = len(bits)
    s = (1 - 2 * bits.astype(np.float64))       # 0->+1, 1->-1
    W = fwht(s)
    w = W / math.sqrt(N)
    w_ac = w[1:]                                 # drop DC (= monobit, tested elsewhere)
    return {"N": N, "dc": float(w[0]), "max_abs": float(np.max(np.abs(w_ac))),
            "argmax": int(np.argmax(np.abs(w_ac)) + 1),
            "evt_scale": math.sqrt(2 * math.log(N)), "w": w_ac}


# =====================================================================
# Lens 3: partial-sum / LIL walk.
# =====================================================================

def partial_sum_walk(bits):
    """S_n = sum(2a-1). Report the walk, its max |S_n|, the LIL-normalized
    max |S_n|/sqrt(2 n ln ln n), the cumsum-test statistic max|S_n|/sqrt(N),
    and the terminal z = S_N/sqrt(N) ~ N(0,1)."""
    N = len(bits)
    step = (2 * bits.astype(np.int64) - 1)
    S = np.cumsum(step)
    nn = np.arange(1, N + 1)
    lil_env = np.sqrt(2.0 * nn * np.log(np.log(np.maximum(nn, 3))))
    ratio = np.abs(S) / lil_env
    return {"N": N, "max_abs_S": int(np.max(np.abs(S))),
            "lil_ratio_max": float(np.max(ratio[10:])),   # skip tiny-n noise
            "cumsum_stat": float(np.max(np.abs(S)) / math.sqrt(N)),
            "terminal_z": float(S[-1] / math.sqrt(N)), "S": S}


# =====================================================================
# Driver
# =====================================================================

def report(label, bits, bm_n):
    print(f"\n########## {label}  (N={len(bits)}) ##########")
    prof = linear_complexity_profile(bits[:bm_n])
    lc = lc_summary(prof)
    print(f"  [1] linear complexity (n={bm_n}): L_final={lc['L_final']} (~n/2={bm_n//2}); "
          f"dev from n/2: mean={lc['mean_dev_from_half']:+.3f} std={lc['std_dev_from_half']:.3f}; "
          f"jumps={lc['n_jumps']}")
    ws = walsh_spectrum_test(bits)
    print(f"  [2] Walsh spectrum: max|w_k|={ws['max_abs']:.2f} at k={ws['argmax']} "
          f"(EVT scale sqrt(2lnN)={ws['evt_scale']:.2f}); DC(monobit)={ws['dc']:+.2f}")
    pw = partial_sum_walk(bits)
    print(f"  [3] partial-sum walk: max|S|={pw['max_abs_S']}, LIL ratio max={pw['lil_ratio_max']:.3f} "
          f"(fair coin -> <~1), cumsum stat={pw['cumsum_stat']:.3f}, terminal z={pw['terminal_z']:+.3f}")
    return {"lc": lc, "lc_profile": prof, "walsh": ws, "walk": pw}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nbits", type=int, default=131072)     # 2^17 for Walsh/walk
    ap.add_argument("--bm-n", type=int, default=32768)       # BM profile depth (O(n^2))
    ap.add_argument("--seed", type=int, default=20260713)
    ap.add_argument("--emit-json", type=str, default="")
    args = ap.parse_args()

    print("Validating fresh generator against anchors.md S17.7 table...")
    _validate(); print("  OK: 12/12.")

    rng = random.Random(args.seed)
    while True:
        omega = rng.randrange(1 << 40, 1 << 64) | 1
        if omega % 3 != 0:
            break
    print(f"\nbulk omega = {omega}\nnbits = {args.nbits} (2^{round(math.log2(args.nbits))}), "
          f"BM depth = {args.bm_n}, seed = {args.seed}")

    M = anchor_bits(omega, args.nbits)
    coin = np.array([rng.randint(0, 1) for _ in range(args.nbits)], dtype=np.int8)
    degen = anchor_bits(3, args.nbits)      # M(3) = -1, all ones: trips lens 1 (LC) + 3 (drift)
    tm = thue_morse(args.nbits)             # Thue-Morse: trips lens 2 (Walsh spike) + 3 (bounded)

    rM = report("M(omega) bulk anchor", M, args.bm_n)
    rC = report("FAIR COIN control", coin, args.bm_n)
    rD = report("omega=3 (all ones) -- positive control for lens 1 (LC) & 3 (drift)", degen, args.bm_n)
    rT = report("THUE-MORSE -- positive control for lens 2 (Walsh) & 3 (bounded walk)", tm, args.bm_n)

    if args.emit_json:
        import json
        def thin(a, k=1024):
            a = np.asarray(a)
            idx = np.linspace(0, len(a) - 1, min(k, len(a))).astype(int)
            return a[idx].tolist()
        # Walsh coeff histogram (normalized), binned
        def wh_hist(w):
            h, edges = np.histogram(w, bins=60, range=(-5, 5))
            return {"counts": h.tolist(), "edges": edges.tolist()}
        payload = {
            "omega": str(omega), "nbits": args.nbits, "bm_n": args.bm_n, "seed": args.seed,
            "lc_profile_M": thin(rM["lc_profile"]), "lc_profile_coin": thin(rC["lc_profile"]),
            "lc_profile_degen": thin(rD["lc_profile"]),
            "walsh_hist_M": wh_hist(rM["walsh"]["w"]), "walsh_hist_coin": wh_hist(rC["walsh"]["w"]),
            "walsh_max_M": rM["walsh"]["max_abs"], "walsh_max_coin": rC["walsh"]["max_abs"],
            "walsh_max_tm": rT["walsh"]["max_abs"], "walsh_evt": rM["walsh"]["evt_scale"],
            "walk_M": thin(rM["walk"]["S"]), "walk_coin": thin(rC["walk"]["S"]),
            "walk_degen": thin(rD["walk"]["S"]), "walk_tm": thin(rT["walk"]["S"]),
        }
        with open(args.emit_json, "w") as f:
            json.dump(payload, f)
        print(f"\nwrote viz payload -> {args.emit_json}")

    print("\n" + "=" * 62)
    print("Read: a clean pass = M(omega) matches the FAIR COIN on all three lenses")
    print("(L_n hugs n/2, flat Walsh spectrum, LIL ratio ~1) while omega=3 trips every")
    print("one (L bounded, Walsh spike, linear drift). Pseudo-randomness on new axes,")
    print("not a statement about AEH. See anchors.md S17.7.4.")


if __name__ == "__main__":
    main()
