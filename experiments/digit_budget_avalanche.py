#!/usr/bin/env python3
"""digit_budget_avalanche.py -- avalanche test of the digit-budget picture: flip
ONE bit j of a B-bit starting core and watch which later quantities move.

Supports: stage4.md 11.8.7.7 (the calibration paragraph: the delay-line
reading of the digit budget); pointed to from bridge.md 16.2. Filed from the
fresh-eyes assessment of 2026-09-04 (briefs/fresh-eyes-assessment-findings.md,
finding 2).

Fresh code: imports nothing from any other script here. Every pass/fail
decision is an exact integer comparison; the probabilities printed are
descriptive statistics over the sampled starts. Deterministic (seed 4); a
re-run from the repo root reproduces experiments/digit_budget_avalanche_output.txt
byte for byte.

Three quantities are tracked at every block t after flipping bit j of w_0:
  core    w_t mod 2^k          the reduced state's odd core
  exit    x_exit(t) mod 2^k    the odd integer leaving block t,
                               x_exit(t) = (3^{d_t} w_t - 1) / 2^{s_t}
  letter  s_t                  the exit valuation (the block's letter)

What the consumption identity of 11.8.7.7 says, made exact for a bit flip:
the underlying integer X_t = 3^{d_t} w_t agrees between the two runs modulo
2^{j - sum_{i<t} sigma_i} (as long as j > sum_{i<t} sigma_i), so the exit's
low k bits and the letter s_t cannot move once j >= sum_{i<t} sigma_i + k + s_t.
PART 3 checks that bound sharply, per sample. The core w_t = X_t / 3^{d_t} is
NOT local in that sense: at a resonant step (stage3.md 11.8.6.2.1 case 3,
d = h(s) with h(s) = v_3(2^s - 1), where a_+ = d + v_3(w + beta)) a high bit of
w can change v_3(w + beta) and move one factor of 3 between w and d, changing
w mod 2^k while X mod 2^k and every letter stay put. PART 3 diagnoses every
such event.

  PART 1  change probabilities per block (core / exit / letter), the budget
          line sum sigma, the never-spent statistic for bits 1..8
  PART 2  first block at which the letter differs, against j/4
  PART 3  locality: the sharp per-sample bound, the smallest uniform c per
          block, and the resonant-step diagnosis of the high-j core changes
  PART 4  the decorrelation value: P(s_16 changed | a low bit flipped)
          against 2/3 = 1 - sum_j 2^{-2j} (two independent ledger draws differ)
"""

import os
import random
import sys

DATE = "2026-09-04"          # assessment date; fixed so that re-runs are byte-identical
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "digit_budget_avalanche_output.txt")
LINES = []
CHECKS = 0
FAILS = []


def say(s=""):
    print(s)
    LINES.append(s)


def check(label, ok, detail=""):
    global CHECKS
    CHECKS += 1
    if not ok:
        FAILS.append(label)
    say("  [%s] %s%s" % ("PASS" if ok else "FAIL", label,
                         ("  (" + detail + ")") if detail else ""))


def v2(x):
    return (x & -x).bit_length() - 1


def v3(x):
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def h(s):
    """Resonance threshold of stage3.md 11.8.6.2.1: h(s) = v_3(2^s - 1)."""
    return v3((1 << s) - 1)


def step(w, d):
    """One reduced block: returns (w_+, d_+, s, sigma, a_+, x_exit)."""
    A = 3 ** d * w - 1
    s = v2(A)
    xexit = A >> s
    C = A + (1 << s)
    sig = v2(C)
    u = C >> sig
    a = v3(u)
    return u // 3 ** a, sig - s + a, s, sig, a, xexit


def trace(w, d, n):
    """n blocks from (w, d). W, D: states 0..n. S, SIG, AG, X: blocks 0..n-1.
    CUM[t] = sum_{i<t} sigma_i, entries 0..n."""
    W, D, S, SIG, AG, X, CUM = [w], [d], [], [], [], [], [0]
    for _ in range(n):
        w, d, s, sig, a, xexit = step(W[-1], D[-1])
        W.append(w)
        D.append(d)
        S.append(s)
        SIG.append(sig)
        AG.append(a)
        X.append(xexit)
        CUM.append(CUM[-1] + sig)
        if (w, d) == (1, 1):
            break
    return W, D, S, SIG, AG, X, CUM


def main():
    say("digit_budget_avalanche.py -- assessment date %s" % DATE)
    random.seed(4)
    B, T, k, NS = 256, 40, 8, 250
    NTR = T + 1                     # trace one block past T so that s_T and x_exit(T) exist
    MASK = (1 << k) - 1
    say("starts: %d draws of a %d-bit odd core (top bit set, 3 not dividing), d_0 uniform in 1..4; k = %d; T = %d blocks" % (NS, B, k, T))
    say("per start, every bit j = 1..%d is flipped once (flips making 3 | w_0 are skipped)" % (B - 1))
    say()

    core_chg = [[0] * B for _ in range(T + 1)]
    exit_chg = [[0] * B for _ in range(T + 1)]
    let_chg = [[0] * B for _ in range(T + 1)]
    ham = [[0.0] * B for _ in range(T + 1)]
    cnt = [0] * B
    budget = [0] * (T + 1)
    nb = 0
    firstdiv = [[] for _ in range(B)]
    c_exit = [None] * (T + 1)       # smallest c such that no exit change at j >= CUM[t] + k + c
    c_let = [None] * (T + 1)        # same for the letter
    s_max = [0] * (T + 1)
    viol_exit = viol_let = 0
    late_pairs = late_letter = 0    # (start, j >= 200) pairs; those whose letter word moves within T blocks
    highj = []                      # core changes at j >= CUM[t] + k + s_t, with their diagnosis

    for _ in range(NS):
        w0 = random.getrandbits(B) | 1 | (1 << (B - 1))
        if w0 % 3 == 0:
            continue
        d0 = random.randrange(1, 5)
        W, D, S, SIG, AG, X, CUM = trace(w0, d0, NTR)
        if len(S) < NTR:
            continue
        nb += 1
        for t in range(T + 1):
            budget[t] += CUM[t]
            s_max[t] = max(s_max[t], S[t])
        for j in range(1, B):
            w1 = w0 ^ (1 << j)
            if w1 % 3 == 0:
                continue
            W1, D1, S1, SIG1, AG1, X1, CUM1 = trace(w1, d0, NTR)
            if len(S1) < NTR:
                continue
            cnt[j] += 1
            fd = None
            for t in range(T + 1):
                core_moved = ((W[t] ^ W1[t]) & MASK) != 0
                exit_moved = ((X[t] ^ X1[t]) & MASK) != 0
                let_moved = S[t] != S1[t]
                if core_moved:
                    core_chg[t][j] += 1
                if exit_moved:
                    exit_chg[t][j] += 1
                if let_moved:
                    let_chg[t][j] += 1
                    if fd is None and t < T:
                        fd = t
                x = W[t] ^ W1[t]
                ham[t][j] += bin(x).count("1") / max(W[t].bit_length(), W1[t].bit_length(), 1)
                J = j - CUM[t]
                if exit_moved:
                    c = J - k + 1
                    c_exit[t] = c if c_exit[t] is None else max(c_exit[t], c)
                    if j >= CUM[t] + k + S[t]:
                        viol_exit += 1
                if let_moved:
                    c = J - k + 1
                    c_let[t] = c if c_let[t] is None else max(c_let[t], c)
                    if j >= CUM[t] + S[t] + 1:
                        viol_let += 1
                if core_moved and j >= CUM[t] + k + S[t]:
                    origin = None
                    for tt in range(t):
                        if AG[tt] != AG1[tt]:
                            origin = tt
                            break
                    highj.append(dict(
                        t=t, j=j,
                        exit_same=not exit_moved,
                        letter_same=not let_moved,
                        all_letters_same=all(S[tt] == S1[tt] for tt in range(t + 1)),
                        X_same=((3 ** D[t] * W[t] - 3 ** D1[t] * W1[t]) % (1 << k)) == 0,
                        depth_diff=D[t] - D1[t],
                        origin=origin,
                        origin_resonant=(origin is not None and S[origin] == S1[origin]
                                         and D[origin] == D1[origin]
                                         and D[origin] == h(S[origin])),
                    ))
            firstdiv[j].append(fd if fd is not None else T)
            if j >= 200:
                late_pairs += 1
                if fd is not None:
                    late_letter += 1

    budget = [b / nb for b in budget]
    ROWS = [0, 1, 2, 3, 5, 8, 12, 16, 20, 30, 40]

    def prob(mat, t, lo=1, hi=8):
        return sum(mat[t][j] / max(cnt[j], 1) for j in range(lo, hi + 1)) / (hi - lo + 1)

    def maxj(mat, t):
        return max([j for j in range(1, B) if mat[t][j] > 0], default=-1)

    # ---------------------------------------------------------------- PART 1
    say("PART 1 -- change probabilities per block; %d valid starts" % nb)
    say("  P(.) = probability that the quantity at block t differs after flipping bit j, averaged over j = 1..8")
    say("  budget = mean cumulative sigma_0 + .. + sigma_{t-1}; maxj = largest j with any change at block t, over all starts")
    say("    t   budget   P_core   P_exit   P_letter   maxj_core  maxj_exit  maxj_letter   Hamming(w_t, j<=8)")
    for t in ROWS:
        hl = sum(ham[t][j] / max(cnt[j], 1) for j in range(1, 9)) / 8
        say("  %3d  %6.1f    %6.3f   %6.3f   %6.3f       %4d       %4d        %4d           %6.3f"
            % (t, budget[t], prob(core_chg, t), prob(exit_chg, t), prob(let_chg, t),
               maxj(core_chg, t), maxj(exit_chg, t), maxj(let_chg, t), hl))
    pc = [prob(core_chg, t) for t in range(1, T + 1)]
    pe = [prob(exit_chg, t) for t in range(1, T + 1)]
    pl = [prob(let_chg, t) for t in range(1, T + 1)]
    say("  never spent: over blocks t = 1..%d, P(core mod 2^%d changed | bit j in 1..8 flipped) ranges %.3f .. %.3f"
        % (T, k, min(pc), max(pc)))
    say("               P(exit mod 2^%d changed) ranges %.3f .. %.3f; P(letter s_t changed) ranges %.3f .. %.3f"
        % (k, min(pe), max(pe), min(pl), max(pl)))
    say("  P_core by block, t = 1..%d: %s" % (T, " ".join("%.2f" % p for p in pc)))
    say("  P_letter by block, t = 1..%d: %s" % (T, " ".join("%.2f" % p for p in pl)))
    say()

    # ---------------------------------------------------------------- PART 2
    JS = [1, 2, 4, 8, 16, 24, 32, 48, 64, 96, 128, 160, 200, 250]
    say("PART 2 -- first block at which the LETTER s_t differs after flipping bit j (mean over starts; %d = never within %d blocks)" % (T, T))
    say("     j : " + " ".join("%5d" % j for j in JS))
    say("   t_1 : " + " ".join("%5.1f" % (sum(firstdiv[j]) / len(firstdiv[j])) for j in JS))
    say("   j/4 : " + " ".join("%5.1f" % (j / 4) for j in JS))
    say("  bits j >= 200: %d (start, j) pairs, %d with any letter change within %d blocks (mean budget at block %d: %.1f)"
        % (late_pairs, late_letter, T, T, budget[T]))
    say("  P(s_t changed | bit j flipped), rows t = 1, 2, 4, 8, 16; columns j = 1..64 (digit = round(10 P), '-' = 0):")
    for t in [1, 2, 4, 8, 16]:
        row = "".join(("%d" % min(9, round(10 * let_chg[t][j] / cnt[j]))) if cnt[j] and let_chg[t][j] else "-"
                      for j in range(1, 65))
        say("   t=%2d " % t + row)
    say()

    # ---------------------------------------------------------------- PART 3
    say("PART 3 -- locality of the exit and the letter; the core artifact")
    say("  sharp per-start bound: exit changes with j >= sum_{i<t} sigma_i + k + s_t: %d; letter changes with j >= sum_{i<t} sigma_i + s_t + 1: %d"
        % (viol_exit, viol_let))
    check("exit locality: no change of x_exit(t) mod 2^k at j >= sum_{i<t} sigma_i + k + s_t", viol_exit == 0)
    check("letter locality: no change of s_t at j >= sum_{i<t} sigma_i + s_t + 1", viol_let == 0)
    say("  smallest uniform c per block such that no exit / letter change occurs at j >= sum_{i<t} sigma_i + k + c")
    say("  (the sharp bound gives c_exit <= max s_t and c_letter <= max s_t + 1 - k, maxima over the starts; 'none' = no change at any j)")
    say("    t   c_exit  c_letter  max s_t")
    for t in ROWS:
        ce = "none" if c_exit[t] is None else "%d" % c_exit[t]
        cl = "none" if c_let[t] is None else "%d" % c_let[t]
        say("  %3d   %5s   %6s    %4d" % (t, ce, cl, s_max[t]))
    n_hi = len(highj)
    say("  core changes at j >= sum_{i<t} sigma_i + k + s_t (where the exit cannot move): %d events" % n_hi)
    by_t = {}
    for e in highj:
        by_t[e["t"]] = by_t.get(e["t"], 0) + 1
    say("    by block: " + (", ".join("t=%d: %d" % (t, by_t[t]) for t in sorted(by_t)) if by_t else "none"))

    def count(key):
        return sum(1 for e in highj if e[key])

    dd = {}
    for e in highj:
        dd[e["depth_diff"]] = dd.get(e["depth_diff"], 0) + 1
    say("    exit x_exit(t) mod 2^k unchanged: %d / %d" % (count("exit_same"), n_hi))
    say("    letter s_t unchanged: %d / %d; every letter s_0..s_t unchanged: %d / %d"
        % (count("letter_same"), n_hi, count("all_letters_same"), n_hi))
    say("    underlying integer X_t = 3^{d_t} w_t unchanged mod 2^k: %d / %d" % (count("X_same"), n_hi))
    say("    depth d_t differs: %d / %d; d_t(base) - d_t(flipped) takes the values %s"
        % (sum(1 for e in highj if e["depth_diff"] != 0), n_hi,
           ", ".join("%+d (x%d)" % (v, dd[v]) for v in sorted(dd)) if dd else "none"))
    say("    an earlier block t* < t with a different 3-gain a_{t*}: %d / %d; the first such block resonant, d = h(s) = v_3(2^s - 1), same (s, d) in both runs: %d / %d"
        % (sum(1 for e in highj if e["origin"] is not None), n_hi, count("origin_resonant"), n_hi))
    check("every high-j core change leaves the exit, every letter and X_t mod 2^k unchanged",
          count("exit_same") == n_hi and count("all_letters_same") == n_hi and count("X_same") == n_hi)
    check("every high-j core change is a factor of 3 moved between w and d at an earlier resonant step",
          count("origin_resonant") == n_hi and all(e["depth_diff"] != 0 for e in highj))
    say()

    # ---------------------------------------------------------------- PART 4
    say("PART 4 -- decorrelation: P(s_16 changed | bit j flipped) against 2/3 = 1 - sum_j 2^{-2j} (two independent ledger draws differ)")
    say("    j = 1..8 individually: " + " ".join("%.3f" % (let_chg[16][j] / cnt[j]) for j in range(1, 9)))
    say("    mean over j = 1..8: %.4f;  mean over j = 1..32: %.4f;  2/3 = %.4f"
        % (prob(let_chg, 16, 1, 8), prob(let_chg, 16, 1, 32), 2 / 3))
    say("    the same mean (j = 1..8) at t = 8, 30, 40: %.4f, %.4f, %.4f"
        % (prob(let_chg, 8), prob(let_chg, 30), prob(let_chg, 40)))
    say("    (descriptive; no pass/fail)")
    say()

    say("SUMMARY: %d checks, %d failures%s" % (CHECKS, len(FAILS),
                                                (": " + "; ".join(FAILS)) if FAILS else ""))
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(LINES) + "\n")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
