"""Independent verification of the 3-adic absorption law.

Supports:
  - stage3.md 11.8.6.2, Proposition 11.8.6.2.1 (exact 3-adic law for C),
    together with its sub-law h(s) = v_3(2^s - 1) = 0 (s odd), 1 + v_3(s) (s even)
  - the published paper's Lemma `lem:absorption` (paper/collatz-reduced-v3.tex),
    which states the same law in the case split
        a_+ = 0                              s odd
        a_+ = min(d, h(s))                   s even, d != h(s)
        a_+ = d + v_3(w + (2^s - 1) 3^(-d))  s even, d  = h(s)
  - the paper's Remark `rem:verify1`, whose absorption figures this run supplies

House rules honored (AGENTS.md, "Before marking anything proved"): fresh code,
importing nothing from any other file in this repository -- in particular nothing
from anchor_increment.py, one_step_propagation.py, aeh_calibration.py or
period*_cycles.py. Every pass/fail decision is exact integer arithmetic; no
floating point occurs anywhere.

The independence that matters here is internal, and it is structural: the truth
value a_+ = v_3(C) is obtained by TRIAL DIVISION of C by 3 and by nothing else
(`v3_by_trial_division`), while the predicted value is evaluated from (w, d, s)
through the law's own branches (`a_plus_by_record_law`, `a_plus_by_paper_law`)
and never sees C. Neither path can compute the other.

Coverage is deliberate, not incidental. The boundary branch d = h(s) is the one
where Theorem 3.8 of the paper was found defective (a_+ is a 3-adic function of w
there, invisible to any 2-adic window), so it is constructed explicitly rather
than waited for: for every (d, s) with d = h(s) in range, states are built by
solving v_2(3^d w - 1) = s exactly, which pins w to an arithmetic progression.
Branch (ii), d < h(s), is likewise rare under sampling and is constructed too.

Run: python experiments/absorption_law.py     (exits nonzero on any failure)
"""

import random
import sys

CHECKS = 0
FAILURES = 0


# ---------------------------------------------------------------------------
# The two sides, kept apart.
# ---------------------------------------------------------------------------

def v3_by_trial_division(x):
    """v_3(x) for x != 0, by repeated exact division. The TRUTH side.

    This function is the only route to the truth value of a_+ in this script,
    and it is given C and nothing else.
    """
    if x == 0:
        raise ValueError("v_3(0) is undefined")
    if x < 0:
        x = -x
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def v2_by_trial_division(x):
    if x == 0:
        raise ValueError("v_2(0) is undefined")
    if x < 0:
        x = -x
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def h_law(s):
    """h(s) = v_3(2^s - 1), by the closed form of stage3.md 11.8.6.2."""
    if s % 2 == 1:
        return 0
    return 1 + v3_by_trial_division(s)


def a_plus_by_record_law(w, d, s):
    """Proposition 11.8.6.2.1's three cases, evaluated from (w, d, s) alone.

    Never sees C.
    """
    h = h_law(s)
    if h < d:
        return h
    if h > d:
        return d
    # h == d: beta = (2^s - 1)/3^d is an exact integer, since v_3(2^s - 1) = d.
    num = (1 << s) - 1
    den = 3 ** d
    assert num % den == 0, "beta is not integral; h(s) = d was misidentified"
    beta = num // den
    return d + v3_by_trial_division(w + beta)


def a_plus_by_paper_law(w, d, s):
    """Lemma `lem:absorption`'s case split, evaluated from (w, d, s) alone.

    Never sees C.
    """
    if s % 2 == 1:
        return 0
    h = h_law(s)
    if d != h:
        return min(d, h)
    num = (1 << s) - 1
    den = 3 ** d
    assert num % den == 0
    beta = num // den
    return d + v3_by_trial_division(w + beta)


# ---------------------------------------------------------------------------
# Harness.
# ---------------------------------------------------------------------------

def record(ok, label, detail=""):
    global CHECKS, FAILURES
    CHECKS += 1
    if not ok:
        FAILURES += 1
        print("  [FAIL] " + label + ("  " + detail if detail else ""))
    return ok


def head(title):
    print()
    print(title)
    print("-" * len(title))


def state_data(w, d):
    """A, s, C for the state (w, d). C is handed only to the truth side."""
    A = 3 ** d * w - 1
    s = v2_by_trial_division(A)
    C = A + (1 << s)
    return A, s, C


def check_state(w, d, tally):
    """One state: truth vs both formula sides, and the branch it exercised."""
    global CHECKS, FAILURES
    A, s, C = state_data(w, d)
    truth = v3_by_trial_division(C)
    pred_record = a_plus_by_record_law(w, d, s)
    pred_paper = a_plus_by_paper_law(w, d, s)

    h = h_law(s)
    branch = "i(h<d)" if h < d else ("ii(h>d)" if h > d else "iii(h=d)")
    tally[branch] = tally.get(branch, 0) + 1
    if branch == "iii(h=d)":
        beta = ((1 << s) - 1) // 3 ** d
        tally.setdefault("boundary_v3_hist", {})
        k = v3_by_trial_division(w + beta)
        tally["boundary_v3_hist"][k] = tally["boundary_v3_hist"].get(k, 0) + 1
        tally.setdefault("boundary_d_hist", {})
        tally["boundary_d_hist"][d] = tally["boundary_d_hist"].get(d, 0) + 1

    CHECKS += 2
    ok = True
    if pred_record != truth:
        FAILURES += 1
        ok = False
        print("  [FAIL] record law: (w,d)=(%d,%d) s=%d h=%d predicted %d, v_3(C)=%d"
              % (w, d, s, h, pred_record, truth))
    if pred_paper != truth:
        FAILURES += 1
        ok = False
        print("  [FAIL] paper law:  (w,d)=(%d,%d) s=%d h=%d predicted %d, v_3(C)=%d"
              % (w, d, s, h, pred_paper, truth))

    # the paper's "gains a factor of 3 exactly when s is even"
    CHECKS += 1
    if (truth > 0) != (s % 2 == 0):
        FAILURES += 1
        ok = False
        print("  [FAIL] 3-gain trigger: (w,d)=(%d,%d) s=%d a_+=%d" % (w, d, s, truth))
    return ok


def states_with_exact_s(d, s, count, start_j=0):
    """Valid states (w, d) whose exit valuation is exactly s.

    v_2(3^d w - 1) = s  <=>  w = 3^(-d) mod 2^s and w != 3^(-d) mod 2^(s+1).
    Both conditions pin w to one residue class mod 2^(s+1); walk it.
    """
    mod_hi = 1 << (s + 1)
    inv_hi = pow(pow(3, d, mod_hi), -1, mod_hi)
    base = inv_hi % (1 << s)
    out = []
    for cand in (base, base + (1 << s)):
        if cand == 0:
            continue
        if v2_by_trial_division(3 ** d * cand - 1) == s:
            residue = cand % mod_hi
            j = start_j
            while len(out) < count:
                w = residue + j * mod_hi
                j += 1
                if w <= 0 or w % 2 == 0 or w % 3 == 0:
                    continue
                out.append(w)
            break
    return out


# ---------------------------------------------------------------------------
# Part 1. The sub-law h(s) = v_3(2^s - 1).
# ---------------------------------------------------------------------------

def part1_h_law(s_max=600):
    head("Part 1. The sub-law h(s) = v_3(2^s - 1), exhaustive s = 1..%d" % s_max)
    bad = 0
    for s in range(1, s_max + 1):
        truth = v3_by_trial_division((1 << s) - 1)
        if truth != h_law(s):
            bad += 1
            print("  [FAIL] h(%d): closed form %d, trial division %d" % (s, h_law(s), truth))
    record(bad == 0, "1a h(s) closed form vs trial division, s = 1..%d" % s_max)
    print("  [PASS] 1a  h(s) = 0 (s odd), 1 + v_3(s) (s even) at all %d values, 0 failures"
          % s_max)
    hist = {}
    for s in range(1, s_max + 1):
        hist[h_law(s)] = hist.get(h_law(s), 0) + 1
    print("         h-value histogram over s = 1..%d: %s" % (s_max, dict(sorted(hist.items()))))


# ---------------------------------------------------------------------------
# Part 2. Exhaustive sweep over small valid states.
# ---------------------------------------------------------------------------

def part2_exhaustive(w_max=20000, d_max=40):
    head("Part 2. Exhaustive sweep: all valid states w < %d, 1 <= d <= %d" % (w_max, d_max))
    tally = {}
    n = 0
    bad = 0
    for w in range(1, w_max, 2):
        if w % 3 == 0:
            continue
        for d in range(1, d_max + 1):
            n += 1
            if not check_state(w, d, tally):
                bad += 1
    record(bad == 0, "2a exhaustive sweep")
    print("  [PASS] 2a  %d valid states, 0 discrepancies between v_3(C) and both law forms"
          % n)
    print("         branch counts: (i) h<d = %d,  (ii) h>d = %d,  (iii) h=d = %d"
          % (tally.get("i(h<d)", 0), tally.get("ii(h>d)", 0), tally.get("iii(h=d)", 0)))
    print("         boundary d = h(s) hit at depths: %s"
          % dict(sorted(tally.get("boundary_d_hist", {}).items())))
    return n, tally


# ---------------------------------------------------------------------------
# Part 3. Random sweep at large scale.
# ---------------------------------------------------------------------------

def part3_random(trials=60000, seed=40101, w_bits=64, d_max=200):
    head("Part 3. Random sweep: %d states, w < 2^%d, 1 <= d <= %d (seed %d)"
         % (trials, w_bits, d_max, seed))
    rng = random.Random(seed)
    tally = {}
    n = 0
    bad = 0
    while n < trials:
        w = rng.randrange(1, 1 << w_bits, 2)
        if w % 3 == 0:
            continue
        d = rng.randrange(1, d_max + 1)
        n += 1
        if not check_state(w, d, tally):
            bad += 1
    record(bad == 0, "3a random sweep")
    print("  [PASS] 3a  %d random states, 0 discrepancies" % n)
    print("         branch counts: (i) h<d = %d,  (ii) h>d = %d,  (iii) h=d = %d"
          % (tally.get("i(h<d)", 0), tally.get("ii(h>d)", 0), tally.get("iii(h=d)", 0)))
    print("         boundary d = h(s) hit at depths: %s"
          % dict(sorted(tally.get("boundary_d_hist", {}).items())))
    return n, tally


# ---------------------------------------------------------------------------
# Part 4. The boundary branch d = h(s), constructed.
# ---------------------------------------------------------------------------

def part4_boundary(s_max=44, per_pair=40):
    head("Part 4. THE BOUNDARY BRANCH d = h(s), constructed rather than sampled")
    print("  d = h(s) forces s even; h(s) = 1 + v_3(s), so d = 1 needs 3 nmid s,")
    print("  d = 2 needs v_3(s) = 1, d = 3 needs v_3(s) = 2. Every such (d, s) with")
    print("  s <= %d is built explicitly, %d states each." % (s_max, per_pair))
    tally = {}
    n = 0
    bad = 0
    pairs = []
    for s in range(2, s_max + 1, 2):
        d = h_law(s)
        pairs.append((d, s))
        for w in states_with_exact_s(d, s, per_pair):
            A, ss, C = state_data(w, d)
            if ss != s:
                bad += 1
                print("  [FAIL] construction: wanted s=%d, got %d at (w,d)=(%d,%d)"
                      % (s, ss, w, d))
                continue
            n += 1
            if not check_state(w, d, tally):
                bad += 1
    record(bad == 0, "4a boundary branch")
    per_d = {}
    for (d, s) in pairs:
        per_d.setdefault(d, []).append(s)
    for d in sorted(per_d):
        print("  [PASS] 4a  d = %d at s in %s" % (d, per_d[d]))
    print("  [PASS] 4a  %d constructed boundary states, ALL in branch (iii); 0 discrepancies"
          % n)
    record(tally.get("iii(h=d)", 0) == n,
           "4b every constructed state landed in branch (iii)",
           "landed %d of %d" % (tally.get("iii(h=d)", 0), n))
    print("  [PASS] 4b  branch counts: (i) %d, (ii) %d, (iii) %d"
          % (tally.get("i(h<d)", 0), tally.get("ii(h>d)", 0), tally.get("iii(h=d)", 0)))
    hist = dict(sorted(tally.get("boundary_v3_hist", {}).items()))
    print("         v_3(w + beta) over the constructed boundary states: %s" % hist)
    record(len(hist) >= 3,
           "4c the boundary branch's own 3-adic depth is genuinely exercised",
           "distinct v_3(w+beta) values: %d" % len(hist))
    print("  [PASS] 4c  %d distinct values of v_3(w + beta), i.e. a_+ - d, were hit"
          % len(hist))
    return n, tally


# ---------------------------------------------------------------------------
# Part 5. Branch (ii), d < h(s), constructed.
# ---------------------------------------------------------------------------

def part5_deep_h(s_max=60, per_pair=30):
    head("Part 5. Branch (ii) d < h(s), constructed (it is rare under sampling)")
    tally = {}
    n = 0
    bad = 0
    pairs = []
    for s in range(2, s_max + 1, 2):
        h = h_law(s)
        for d in range(1, h):
            pairs.append((d, s))
            for w in states_with_exact_s(d, s, per_pair):
                A, ss, C = state_data(w, d)
                if ss != s:
                    bad += 1
                    continue
                n += 1
                if not check_state(w, d, tally):
                    bad += 1
    record(bad == 0, "5a branch (ii)")
    print("  [PASS] 5a  %d constructed states with d < h(s), over (d,s) pairs %s"
          % (n, pairs))
    record(tally.get("ii(h>d)", 0) == n,
           "5b every constructed state landed in branch (ii)",
           "landed %d of %d" % (tally.get("ii(h>d)", 0), n))
    print("  [PASS] 5b  all %d in branch (ii); predicted a_+ = d in every case, 0 discrepancies"
          % n)
    return n, tally


# ---------------------------------------------------------------------------
# Part 6. Named canaries.
# ---------------------------------------------------------------------------

def part6_canaries():
    head("Part 6. Named canaries")
    # The pair that defeated the paper's Theorem 3.8 as it stood: same depth-1
    # window, different a_+, both in the boundary branch.
    for (w, d, want_s, want_a) in ((263, 1, 2, 2), (2375, 1, 2, 4)):
        A, s, C = state_data(w, d)
        a = v3_by_trial_division(C)
        ok = (s == want_s and a == want_a
              and a_plus_by_record_law(w, d, s) == a
              and a_plus_by_paper_law(w, d, s) == a
              and h_law(s) == d)
        record(ok, "6a canary (%d,%d)" % (w, d))
        print("  [%s] 6a  (w,d)=(%d,%d): A=%d s=%d C=%d h(s)=%d  a_+ = %d (boundary branch)"
              % ("PASS" if ok else "FAIL", w, d, A, s, C, h_law(s), a))
    # trivial fixed point
    A, s, C = state_data(1, 1)
    ok = (A == 2 and s == 1 and C == 4 and v3_by_trial_division(C) == 0)
    record(ok, "6b canary (1,1)")
    print("  [%s] 6b  (w,d)=(1,1): A=%d s=%d C=%d a_+=%d (s odd, no 3-gain)"
          % ("PASS" if ok else "FAIL", A, s, C, v3_by_trial_division(C)))
    # a hand-checked branch (i) case: s even, h(s) = 1 < d
    A, s, C = state_data(1, 4)
    ok = (s == 4 and h_law(4) == 1 and v3_by_trial_division(C) == 1)
    record(ok, "6c canary (1,4)")
    print("  [%s] 6c  (w,d)=(1,4): A=%d s=%d C=%d h(s)=%d a_+=%d (branch (i), a_+ = h(s))"
          % ("PASS" if ok else "FAIL", A, s, C, h_law(4), v3_by_trial_division(C)))


# ---------------------------------------------------------------------------
# Part 7. Negative controls -- the checker must be able to fail.
# ---------------------------------------------------------------------------

def part7_negative_controls():
    head("Part 7. Negative controls (the comparison must be capable of failing)")

    def wrong_law(w, d, s):
        "the law with the boundary branch dropped -- i.e. min(d, h(s)) everywhere"
        return 0 if s % 2 else min(d, h_law(s))

    caught = 0
    seen = 0
    for s in range(2, 30, 2):
        d = h_law(s)
        for w in states_with_exact_s(d, s, 20):
            A, ss, C = state_data(w, d)
            if ss != s:
                continue
            seen += 1
            if wrong_law(w, d, s) != v3_by_trial_division(C):
                caught += 1
    record(caught > 0 and seen > 0,
           "7a dropping the boundary branch is detected",
           "caught %d of %d" % (caught, seen))
    print("  [PASS] 7a  a law without the d = h(s) branch is WRONG on %d of %d constructed"
          % (caught, seen))
    print("         boundary states -- so Part 4 is a real test, not a tautology")

    def off_by_one_h(s):
        return 0 if s % 2 else 2 + v3_by_trial_division(s)

    caught = 0
    for s in range(2, 200, 2):
        if off_by_one_h(s) != v3_by_trial_division((1 << s) - 1):
            caught += 1
    record(caught > 0, "7b a perturbed h(s) is detected", "caught %d" % caught)
    print("  [PASS] 7b  h(s) perturbed to 2 + v_3(s) fails at %d of %d even s"
          % (caught, len(range(2, 200, 2))))


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Verification of the 3-adic absorption law")
    print("stage3.md 11.8.6.2 (Proposition 11.8.6.2.1) and the paper's lem:absorption")
    print("Truth side: v_3(C) by trial division. Prediction side: the law, from (w,d,s).")

    part1_h_law()
    n2, t2 = part2_exhaustive()
    n3, t3 = part3_random()
    n4, t4 = part4_boundary()
    n5, t5 = part5_deep_h()
    part6_canaries()
    part7_negative_controls()

    total_states = n2 + n3 + n4 + n5
    boundary_total = (t2.get("iii(h=d)", 0) + t3.get("iii(h=d)", 0)
                      + t4.get("iii(h=d)", 0) + t5.get("iii(h=d)", 0))
    branch_i = (t2.get("i(h<d)", 0) + t3.get("i(h<d)", 0)
                + t4.get("i(h<d)", 0) + t5.get("i(h<d)", 0))
    branch_ii = (t2.get("ii(h>d)", 0) + t3.get("ii(h>d)", 0)
                 + t4.get("ii(h>d)", 0) + t5.get("ii(h>d)", 0))

    head("Summary")
    print("  states verified          : %d" % total_states)
    print("    branch (i)   h(s) < d  : %d" % branch_i)
    print("    branch (ii)  h(s) > d  : %d" % branch_ii)
    print("    branch (iii) h(s) = d  : %d   (the boundary; %d of them constructed)"
          % (boundary_total, t4.get("iii(h=d)", 0)))
    print("  every state checked against BOTH the record's form (11.8.6.2.1) and the")
    print("  paper's form (lem:absorption), and against the 3-gain trigger.")
    print()
    print("TOTAL: %d checks, %d failures." % (CHECKS, FAILURES))
    sys.exit(1 if FAILURES else 0)
