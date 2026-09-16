"""Independent check of the arithmetic core of viz/comb_explorer.html against a fresh
Python implementation of comb.md section 18, on either sign (18.8).

Supports: briefs/comb-explorer-brief.md (the comb explorer); briefs/signed-comb-brief.md
(the explorer opened at any of the four roots); comb.md section 18.

What it does:
  1. Reads viz/comb_explorer.html, extracts the text between the two marker lines
     `// === COMB CORE BEGIN ===` and `// === COMB CORE END ===`, appends a small
     harness (a list of {fn, args} requests read from stdin as JSON, results printed
     as JSON with every BigInt rendered as a decimal string) and runs it under node.
     If node is not on the PATH the script says so and exits with status 2; it never
     passes vacuously.
  2. Implements the same rules independently here, with exact Python integers, from
     the wiki's own definitions -- not from the JavaScript -- for either sign:
       state (w,d): w a nonzero odd integer, 3 does not divide w, d >= 1 (spine.md
         3.5; itinerary.md 14.15.6 for the negative odd integers);
       peak A = 3^d w - 1 = 2^s y, s = v2(A), y the exit by exact signed division
         (comb.md 18.1.1);
       door recovery y + 1 = 2^m 3^a W -> state (W, m+a), W of the sign of y + 1;
         y = -1 is the door of no state (reverse.md 14.6.5.1; itinerary.md 14.15.6.1);
       F(w,d) = state(y), undefined exactly when y = -1 (spine.md 3.7; 14.14.1.1);
       doors y_a = 2^(D-a) 3^a W - 1, alive iff 3 does not divide y_a (14.5.1);
       residues mod 3 in {0,1,2} (-5 = 1, -7 = 2), the parity rule of 14.1.1;
       comb parent (18.2.1): s >= 3 the state at branch s-2 on the same door,
         s <= 2 the door parent F(w,d); ring nodes have none (they are the roots
         of their components, 18.8.2): (1,1); (-1,1), whose door parent state(-1)
         does not exist; the fixed state (-1,2); the ring (-1,4), (-5,3), (-11,1);
       children (18.2.3): the cascade child at branch s+2 on the node's own door,
         computed here by 14.10.1's identity N(y,s+2) = 4 N(y,s) - 3 with N = 3^D W,
         and one door child per live door at the lowest admissible branch (14.1.1's
         parity rule); a child that is a ring node is excluded (the self-loops of
         (1,1) and (-1,2); the ring children of the 2-cycle's ring nodes);
       the raw descent (18.1.3, 18.4.1): computed here by iterating the raw map
         Col (3x+1 on odd, x/2 on even, either sign) from the representative x_a
         until the door y, tagging each point from its position and Lemma 18.1.2(iii);
       the two distances (18.3.1, 18.8.2): eta by iterating F to an F-periodic ring
         node, or to the first state with exit -1 in the singular component -- the
         definition, not the page's door-edge count -- and lambda by counting parent
         edges to the ring.
  3. Compares the two on the canaries of both briefs (hard-coded expectations here,
     checked against BOTH implementations), on 2,000 random positive and 2,000 random
     negative states (|w| < 10^6, 3 does not divide w, d <= 40) for every function,
     on 300 random odd x of each sign, |x| < 10^12, for the go-to path (the ring
     reached, eta, lambda, the full path), and on 200 random representatives of each
     sign for the raw descent; it also runs the page's own selfTest() under node and
     reports its line.
  4. Rendering test: loads both of the page's script blocks under node with a stubbed
     `document` (elements are plain objects holding innerHTML and click listeners),
     drives the go-to box for (137, 517), for 213, for the state of a random 300-digit
     odd integer, for a state whose path exceeds the page's render cap of 5,000 nodes,
     for -17, for the state of a random negative 100-digit odd integer, and for -13,1
     from the default root (the selector must switch to the fixed state), and measures
     on the produced tree HTML with Python's own html.parser: (a) the maximum element
     nesting depth under the tree container, at most DEPTH_BOUND = 3; (b) the number
     of rendered rows, which must equal the visible nodes computed here from the
     Python children rule (the path nodes, one stub per ancestor with children left
     unshown, the ring's own note rows, and the fold row under the render cap) and be
     far below the count of all the ancestors' children; (c) no exception. The go-to
     message is checked for the comma reading, the counts, the component switch, and
     the refusal of the singular door -1.
  5. Prints per-function counts and `TOTAL: checks = N, failures = 0`.

Fresh code: imports nothing from any other file in this repository. Exact integers at
every pass/fail decision. Seed 20260915. Single reproducing command:

    python experiments/comb_explorer_check.py

The script prints its report and also writes it to
experiments/comb_explorer_check_output.txt (the committed output), so no shell
redirection is involved. The node version line is the only machine-dependent line.
"""

import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser

SEED = 20260915
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGE = os.path.join(ROOT, "viz", "comb_explorer.html")
OUT = os.path.join(HERE, "comb_explorer_check_output.txt")
BEGIN = "// === COMB CORE BEGIN ==="
END = "// === COMB CORE END ==="

LINES = []


def out(s=""):
    print(s)
    LINES.append(s)


# ----------------------------------------------------------------------------
# The independent Python implementation (comb.md section 18, either sign)
# ----------------------------------------------------------------------------

def exact_div(a, b):
    assert b != 0 and a % b == 0
    return a // b


def v2(n):
    assert n != 0
    n = abs(n)
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def v3(n):
    assert n != 0
    n = abs(n)
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def mod3(n):
    return n % 3          # in {0,1,2} for either sign


def is_valid(w, d):
    return w != 0 and w % 2 == 1 and w % 3 != 0 and d >= 1


def exit_data(w, d):
    A = 3 ** d * w - 1
    s = v2(A)
    return A, s, exact_div(A, 2 ** s)


def state_of_odd(y):
    if y == -1:
        return None
    n = y + 1
    m = v2(n)
    u = exact_div(n, 2 ** m)
    a = v3(u)
    return (exact_div(u, 3 ** a), m + a)


def F(w, d):
    return state_of_odd(exit_data(w, d)[2])


def node_at(y, s):
    N = 2 ** s * y + 1
    assert N % 3 == 0, "not an admissible branch"
    d = v3(N)
    return (exact_div(N, 3 ** d), d)


def door_list(W, D):
    return [(a, 2 ** (D - a) * 3 ** a * W - 1) for a in range(D)]


def lowest_branch(y):
    # 14.1.1: s odd iff y = 1 mod 3, s even iff y = 2 mod 3
    return 1 if mod3(y) == 1 else 2


RINGS = {"pos": [(1, 1)], "sing": [(-1, 1)], "fix": [(-1, 2)], "two": [(-1, 4), (-5, 3), (-11, 1)]}
FCYCLE = {"pos": {(1, 1)}, "sing": set(), "fix": {(-1, 2)}, "two": {(-1, 4), (-5, 3)}}
RING_OF = {}
for _k, _l in RINGS.items():
    for _st in _l:
        RING_OF[_st] = _k


def parent(w, d):
    if (w, d) in RING_OF:
        return None
    A, s, y = exit_data(w, d)
    if s >= 3:
        # the state at branch s-2 on the same door: 2^(s-2) y + 1 = (A/4) + 1
        N = exact_div(A, 4) + 1
        dd = v3(N)
        return ((exact_div(N, 3 ** dd), dd), "cascade")
    return (F(w, d), "door")


def children(W, D):
    A, s, y = exit_data(W, D)
    # cascade child by 14.10.1: N(y, s+2) = 4 N(y, s) - 3, N(y, s) = A + 1 = 3^D W
    N2 = 4 * (3 ** D * W) - 3
    dd = v3(N2)
    casc = (exact_div(N2, 3 ** dd), dd)
    cd = (None if y == -1 else v3(y + 1), y)
    lst, dead, excluded = [], [], []
    if casc in RING_OF:
        excluded.append((cd[0], cd[1], s + 2, casc, False, "cascade"))
    else:
        lst.append((casc, "cascade", s + 2, cd))
    for a, ya in door_list(W, D):
        if ya % 3 == 0:
            dead.append((a, ya))
            continue
        s0 = lowest_branch(ya)
        # the 14.1.1 predecessor at branch s0 on door ya
        N = 2 ** s0 * ya + 1
        dd = v3(N)
        st = (exact_div(N, 3 ** dd), dd)
        if st == (W, D):
            excluded.append((a, ya, s0, st, True, "door"))
            continue
        if st in RING_OF:
            excluded.append((a, ya, s0, st, False, "door"))
            continue
        lst.append((st, "door", s0, (a, ya)))
    return lst, dead, excluded


def raw_descent(w, d, a):
    """Iterate the raw map from x_a to the door y; tag from position and 18.1.2(iii)."""
    A, s, y = exit_data(w, d)
    x = 2 ** (d - a) * 3 ** a * w - 1
    pts = []
    phase = "rise"
    while True:
        if x == y:
            pts.append((x, "door", None))
            break
        if phase == "rise":
            if x == A:
                pts.append((x, "peak", None))
                phase = "cascade"
            elif x == 2 * A:
                pts.append((x, "max", None))
            elif x % 2 == 1:
                pts.append((x, "odd", None))
            else:
                pts.append((x, "rise", None))
        else:
            # a cascade even 2^j y; a peak iff = 2 mod 3 (Lemma 18.1.2(iii)), then the
            # peak of the sibling at branch j on door y
            if mod3(x) == 2:
                pts.append((x, "sibpeak", node_at(y, v2(x))))
            else:
                pts.append((x, "cascade", None))
        x = 3 * x + 1 if x % 2 == 1 else exact_div(x, 2)
    return pts


def eta_by_F(w, d, k, cap=100000):
    """The reduced distance by its definition: F-steps to an F-periodic node of ring k,
    or to the first state with exit -1 when k is the singular component."""
    n = 0
    st = (w, d)
    while st not in FCYCLE[k]:
        if exit_data(*st)[2] == -1:
            return n if k == "sing" else None
        st = F(*st)
        n += 1
        if n > cap:
            return None
    return n


def path_to_root(w, d, cap):
    path = []
    cur = (w, d)
    door_edges = casc_edges = steps = 0
    cap_hit = False
    while True:
        A, s, y = exit_data(*cur)
        p = parent(*cur)
        path.append((cur, A, s, y, None if p is None else p[1]))
        if p is None:
            break
        if steps >= cap:
            cap_hit = True
            break
        if p[1] == "door":
            door_edges += 1
        else:
            casc_edges += 1
        cur = p[0]
        steps += 1
    ring = None if cap_hit else RING_OF.get(path[-1][0])
    lam = None if cap_hit else door_edges + casc_edges
    return path, cap_hit, door_edges, casc_edges, lam, ring


# ----------------------------------------------------------------------------
# Normalisation to the JSON shape the page's core produces (ints -> decimal strings)
# ----------------------------------------------------------------------------

def S(st):
    return [str(st[0]), str(st[1])]


def n_exit(w, d):
    A, s, y = exit_data(w, d)
    return {"A": str(A), "s": str(s), "y": str(y)}


def n_state(st):
    return None if st is None else S(st)


def n_doors(W, D):
    return [{"a": str(a), "y": str(y), "alive": y % 3 != 0} for a, y in door_list(W, D)]


def n_parent(w, d):
    p = parent(w, d)
    return None if p is None else {"state": S(p[0]), "type": p[1]}


def n_children(W, D):
    lst, dead, exc = children(W, D)
    return {
        "list": [{"state": S(st), "type": t, "s": str(s), "door": {"a": None if dr[0] is None else str(dr[0]), "y": str(dr[1])}} for st, t, s, dr in lst],
        "dead": [{"a": str(a), "y": str(y), "dead": True} for a, y in dead],
        "excluded": [{"a": None if a is None else str(a), "y": str(y), "s": str(s), "state": S(st), "self": sf, "ring": True, "type": t} for a, y, s, st, sf, t in exc],
    }


def n_descent(w, d, a):
    return [{"x": str(x), "tag": t, "sib": None if sib is None else S(sib)} for x, t, sib in raw_descent(w, d, a)]


def n_path(w, d, cap):
    path, cap_hit, de, ce, lam, ring = path_to_root(w, d, cap)
    eta = None if ring is None else eta_by_F(w, d, ring)
    return {
        "path": [{"state": S(st), "A": str(A), "s": str(s), "y": str(y), "edge": e} for st, A, s, y, e in path],
        "capHit": cap_hit,
        "doorEdges": str(de),
        "cascadeEdges": str(ce),
        "ring": ring,
        "lambda": None if lam is None else str(lam),
        "eta": None if eta is None else str(eta),
    }


# ----------------------------------------------------------------------------
# Running the page's core under node
# ----------------------------------------------------------------------------

HARNESS = r"""
const __chunks = [];
process.stdin.setEncoding('utf8');
process.stdin.on('data', c => __chunks.push(c));
process.stdin.on('end', () => {
  const reqs = JSON.parse(__chunks.join(''));
  const fns = { v2, v3, mod3, exactDiv, isValidState, ringOf, exitData, stateOfOdd, F, nodeAt, lowestBranch, doors, parent, children, rawDescent, etaOf, pathToRoot, selfTest };
  const res = reqs.map(r => fns[r.fn](...r.args.map(a => (typeof a === 'string' && /^-?\d+$/.test(a)) ? BigInt(a) : a)));
  process.stdout.write(JSON.stringify(res, (k, v) => typeof v === 'bigint' ? v.toString() : v));
});
"""


def extract_core():
    with open(PAGE, encoding="utf-8") as f:
        lines = f.read().split("\n")
    b = [i for i, l in enumerate(lines) if l.strip() == BEGIN]
    e = [i for i, l in enumerate(lines) if l.strip() == END]
    if len(b) != 1 or len(e) != 1 or b[0] >= e[0]:
        out("ERROR: the core markers were not found exactly once each in %s" % PAGE)
        sys.exit(2)
    core = "\n".join(lines[b[0] + 1:e[0]])
    for bad in ("document.", "window.", "getElementById"):
        if bad in core:
            out("ERROR: the core block contains DOM access (%s)" % bad)
            sys.exit(2)
    return core, e[0] - b[0] - 1


def run_node(core, reqs):
    node = shutil.which("node")
    if node is None:
        out("ERROR: node is not on the PATH; the page's core cannot be run. Nothing was checked.")
        sys.exit(2)
    ver = subprocess.run([node, "--version"], capture_output=True, text=True).stdout.strip()
    with tempfile.TemporaryDirectory() as td:
        js = os.path.join(td, "comb_core_run.js")
        with open(js, "w", encoding="utf-8") as f:
            f.write(core + "\n" + HARNESS)
        proc = subprocess.run([node, js], input=json.dumps(reqs), capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        out("ERROR: node exited with status %d" % proc.returncode)
        out(proc.stderr[:4000])
        sys.exit(2)
    return ver, json.loads(proc.stdout)


# ----------------------------------------------------------------------------
# The rendering test: the page's two script blocks under a stubbed document
# ----------------------------------------------------------------------------

DEPTH_BOUND = 3      # the largest element nesting depth allowed under the tree container
RENDER_CAP = 5000    # the page's own cap on rendered path length (nodes)
ANC_SHOWN = 200      # ancestors rendered below the ring when the cap is exceeded

RENDER_HARNESS = r"""
const __fs = require('fs');
const __html = __fs.readFileSync(process.argv[2], 'utf8');
const __blocks = [...__html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
if (__blocks.length !== 2) { process.stdout.write(JSON.stringify({ error: 'expected 2 script blocks, found ' + __blocks.length })); process.exit(0); }
const __els = {}, __listeners = {};
function __el(id){
  if (!__els[id]) {
    // innerHTML and textContent share one store, as in a real element
    const e = { id, _c: '', value: '', addEventListener: (t, f) => { (__listeners[id] = __listeners[id] || {})[t] = f; }, scrollIntoView: () => {} };
    Object.defineProperty(e, 'innerHTML', { get: () => e._c, set: v => { e._c = v; } });
    Object.defineProperty(e, 'textContent', { get: () => e._c, set: v => { e._c = v; } });
    __els[id] = e;
  }
  return __els[id];
}
global.document = { getElementById: id => __el(id), querySelector: () => ({ scrollIntoView: () => {} }) };
global.window = {};
const __chunks = [];
process.stdin.setEncoding('utf8');
process.stdin.on('data', c => __chunks.push(c));
process.stdin.on('end', () => {
  const cases = JSON.parse(__chunks.join(''));
  const out = { selftest: null, cases: [] };
  try { new Function(__blocks[0] + '\n' + __blocks[1])(); out.selftest = __els.selftest.textContent; }
  catch (e) { out.error = 'load: ' + e; process.stdout.write(JSON.stringify(out)); return; }
  for (const c of cases) {
    const r = { name: c.name };
    try {
      __els.root.value = 'pos'; __listeners.root.change({ target: { value: 'pos' } });
      __listeners.resetBtn.click();
      __els.goto.value = c.input;
      __listeners.goBtn.click();
      r.tree = __els.tree.innerHTML;
      r.msg = __els.msg.innerHTML;
      r.root = __els.root.value;
      r.note = __els.treenote.innerHTML;
      r.detailLen = __els.detail.innerHTML.length;
    } catch (e) { r.error = String(e && e.stack ? e.stack : e); }
    out.cases.push(r);
  }
  process.stdout.write(JSON.stringify(out));
});
"""


class TreeMeasure(HTMLParser):
    """Depth and row statistics of the tree container's innerHTML."""

    VOID = {"br", "img", "input", "hr", "meta", "link"}

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.max_depth = 0
        self.rows = 0
        self.cards = 0
        self.stubs = 0
        self.greys = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            return
        self.depth += 1
        self.max_depth = max(self.max_depth, self.depth)
        if self.depth == 1:
            self.rows += 1
            cls = dict(attrs).get("class", "")
            if "card" in cls.split():
                self.cards += 1
            elif "stub" in cls.split():
                self.stubs += 1
            elif "grey" in cls.split():
                self.greys += 1

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        self.depth -= 1


def note_rows(st):
    """The grey note rows a fully shown node carries: excluded children, dead doors, and the
    singular root's missing-parent note."""
    lst, dead, exc = children(*st)
    return len(dead) + len(exc) + (1 if st == (-1, 1) else 0)


def expected_rows(path, ring):
    """Visible rows after a go-to from a freshly reset tree, from the Python children rule.

    path: the list of states from the node to the ring node it reaches. Every ring node
    is displayed in full (its card plus its note rows, as reset leaves it), the other
    ring nodes with their children too; every other ancestor shows its card, its path
    child, and one stub row when children or notes remain unshown; the node shows its
    card. Past RENDER_CAP path nodes the ancestors other than the last ANC_SHOWN are
    replaced by one fold row. Returns (rows, cards, stubs, greys, full_rows, hidden_count).
    """
    L = len(path)
    hidden = set()
    if L > RENDER_CAP:
        hidden = set(range(ANC_SHOWN + 1, L - 1))
    rows = cards = stubs = greys = 0
    full_rows = 0
    for r in RINGS[ring]:
        lst, dead, exc = children(*r)
        full_rows += 1 + len(lst) + note_rows(r)
        if r == path[-1]:
            continue
        rows += 1 + len(lst) + note_rows(r)     # a ring node not on the path: shown in full
        cards += 1 + len(lst)
        greys += note_rows(r)
    for i in range(L - 1, -1, -1):
        st = path[i]
        if i == L - 1:                      # the ring node reached, shown in full (reset expanded it)
            rows += 1 + note_rows(st)
            cards += 1
            greys += note_rows(st)
            lst, dead, exc = children(*st)
            extra = len(lst) - (0 if L == 1 else 1)   # its other children, collapsed; the path child is counted below
            rows += extra
            cards += extra
            continue
        if i == 0:                          # the node itself, collapsed
            rows += 1
            cards += 1
            continue
        lst, dead, exc = children(*st)
        full_rows += len(lst) + note_rows(st)
        if i in hidden:
            continue
        rows += 1
        cards += 1
        if (len(lst) - 1) + note_rows(st) > 0:
            rows += 1
            stubs += 1
    if hidden:
        rows += 1
        greys += 1
    return rows, cards, stubs, greys, full_rows, len(hidden)


def run_render(cases):
    node = shutil.which("node")
    if node is None:
        out("ERROR: node is not on the PATH; the rendering test cannot run.")
        sys.exit(2)
    with tempfile.TemporaryDirectory() as td:
        js = os.path.join(td, "comb_render_run.js")
        with open(js, "w", encoding="utf-8") as f:
            f.write(RENDER_HARNESS)
        proc = subprocess.run([node, js, PAGE], input=json.dumps(cases), capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        out("ERROR: node exited with status %d in the rendering test" % proc.returncode)
        out(proc.stderr[:4000])
        sys.exit(2)
    return json.loads(proc.stdout)


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

CHECKS = 0
FAILS = 0
FAIL_LINES = []


def check(ok, what):
    global CHECKS, FAILS
    CHECKS += 1
    if not ok:
        FAILS += 1
        if len(FAIL_LINES) < 40:
            FAIL_LINES.append("  FAIL: " + what)


def main():
    rng = random.Random(SEED)
    out("comb_explorer_check.py -- seed %d, 2026-09-16 (signed revision)" % SEED)
    core, ncore = extract_core()
    out("core block: %d lines between the markers, no DOM access" % ncore)

    def rand_state(sign):
        while True:
            w = rng.randrange(1, 10 ** 6, 2)
            if w % 3 != 0:
                break
        return sign * w, rng.randrange(1, 41)

    states = [rand_state(1) for _ in range(2000)] + [rand_state(-1) for _ in range(2000)]
    xs = [rng.randrange(1, 10 ** 12, 2) for _ in range(300)] + [-rng.randrange(3, 10 ** 12, 2) for _ in range(300)]
    reps = []
    for i in range(400):
        w, d = rand_state(1 if i < 200 else -1)
        reps.append((w, d, rng.randrange(0, d)))

    canary_states = [(1, 1), (1, 2), (11, 1), (43, 1), (19, 3), (7, 1), (1, 4), (107, 1), (7, 3), (37, 1), (37, 2), (167, 1), (251, 1),
                     (-1, 1), (-5, 1), (-7, 2), (-85, 1), (-341, 1), (-7, 1), (-7, 3), (-1, 2), (-13, 1), (-1, 3), (-17, 1), (-31, 1),
                     (-1, 4), (-5, 3), (-11, 1), (-5, 2), (-181, 1), (-109, 1), (-11, 2), (-49, 1), (-73, 1), (-1, 5), (-121, 1), (-1543, 3)]
    all_states = canary_states + states

    # Build the request list for node, one batch.
    reqs = []
    idx = {}

    def req(fn, *args):
        idx.setdefault(fn, []).append(len(reqs))
        reqs.append({"fn": fn, "args": [a if isinstance(a, str) else str(a) for a in args]})

    req("selfTest")
    for w, d in all_states:
        req("exitData", w, d)
        req("F", w, d)
        req("doors", w, d)
        req("parent", w, d)
        req("children", w, d)
        req("pathToRoot", w, d, 10000)
    for w, d in all_states:
        req("stateOfOdd", exit_data(w, d)[2])
    for x in xs:
        req("stateOfOdd", x)
        st = state_of_odd(x)
        req("pathToRoot", st[0], st[1], 10000)
    for w, d, a in reps:
        req("rawDescent", w, d, a)
    req("rawDescent", 107, 1, 0)          # the descent of 213
    req("rawDescent", -7, 1, 0)           # the descent of -15
    req("pathToRoot", 107, 1, 2)          # the cap
    req("nodeAt", 1, 1)
    for s in (3, 5, 7, 9):
        req("nodeAt", 1, s)
    for s in (2, 4, 6):
        req("nodeAt", 5, s)
    for s in (2, 4, 6, 8, 10):
        req("nodeAt", -1, s)
    for y in (-5, -7, -17, -25, -41, -9):
        req("mod3", y)
    req("stateOfOdd", -1)
    for st in ((1, 1), (-1, 1), (-1, 2), (-1, 4), (-5, 3), (-11, 1), (-5, 1), (-1, 3)):
        req("ringOf", st[0], st[1])

    ver, res = run_node(core, reqs)
    out("node %s; %d requests answered" % (ver, len(res)))

    # --- the page's own self-test, as exercised under node
    st = res[idx["selfTest"][0]]
    out("--- the page's selfTest() under node ---")
    out("  self-test: %s checks, %d failures" % (st["checks"], len(st["failures"])))
    check(int(st["checks"]) > 0 and len(st["failures"]) == 0, "page selfTest: " + "; ".join(st["failures"][:5]))
    page_checks = st["checks"]

    # --- canaries against hard-coded expectations, on BOTH implementations
    out("--- canaries (both briefs' lists; JS and Python each against the expected values) ---")
    n0 = CHECKS

    def canary(fn, args, expected, what):
        i = idx[fn].pop(0)
        js = res[i]
        check(js == expected, "JS " + what + " got " + json.dumps(js)[:200])
        return js

    exc = lambda a, y, s, st, sf, t: {"a": a, "y": y, "s": s, "state": st, "self": sf, "ring": True, "type": t}
    # root's only child; door 1 chain; door 5; (7,3); (1,2) dead door; distances; descent of 213
    exp_root = {"list": [{"state": ["1", "2"], "type": "cascade", "s": "3", "door": {"a": "0", "y": "1"}}], "dead": [],
                "excluded": [exc("0", "1", "1", ["1", "1"], True, "door")]}
    check(n_children(1, 1) == exp_root, "PY root children")
    chain1 = {1: (1, 1), 3: (1, 2), 5: (11, 1), 7: (43, 1), 9: (19, 3)}
    for s, stt in chain1.items():
        check(node_at(1, s) == stt, "PY door 1 branch %d" % s)
    chain5 = {2: ((7, 1), 20), 4: ((1, 4), 80), 6: ((107, 1), 320)}
    for s, (stt, A) in chain5.items():
        check(node_at(5, s) == stt and exit_data(*stt)[0] == A and exit_data(*stt)[1] == s, "PY door 5 branch %d" % s)
    exp73 = {"list": [{"state": ["251", "1"], "type": "cascade", "s": "4", "door": {"a": "1", "y": "47"}},
                      {"state": ["37", "1"], "type": "door", "s": "1", "door": {"a": "0", "y": "55"}},
                      {"state": ["37", "2"], "type": "door", "s": "2", "door": {"a": "1", "y": "83"}},
                      {"state": ["167", "1"], "type": "door", "s": "2", "door": {"a": "2", "y": "125"}}],
             "dead": [], "excluded": []}
    check(n_children(7, 3) == exp73 and exit_data(251, 1)[0] == 752, "PY (7,3) children")
    check(n_doors(1, 2) == [{"a": "0", "y": "3", "alive": False}, {"a": "1", "y": "5", "alive": True}], "PY (1,2) doors")
    dist = {(1, 2): (1, 1), (11, 1): (1, 2), (7, 1): (2, 2), (107, 1): (2, 4), (1, 1): (0, 0)}
    for stt, (eta, lam) in dist.items():
        p = n_path(stt[0], stt[1], 10000)
        check(p["eta"] == str(eta) and p["lambda"] == str(lam) and not p["capHit"] and p["ring"] == "pos", "PY distances %s" % (stt,))
    exp213 = [("213", "odd", None), ("640", "max", None), ("320", "peak", None), ("160", "cascade", None), ("80", "sibpeak", ["1", "4"]),
              ("40", "cascade", None), ("20", "sibpeak", ["7", "1"]), ("10", "cascade", None), ("5", "door", None)]
    check(n_descent(107, 1, 0) == [{"x": x, "tag": t, "sib": s} for x, t, s in exp213], "PY descent of 213")
    # --- the negative canaries (signed-comb brief, Items A-B)
    check(state_of_odd(-1) is None and state_of_odd(-3) == (-1, 1) and exit_data(-1, 1) == (-4, 2, -1) and F(-1, 1) is None, "PY (-1,1): peak -4, exit -1, no F-image; -1 is no door")
    check(state_of_odd(-5) == (-1, 2) and state_of_odd(-7) == (-1, 2) and F(-1, 2) == (-1, 2), "PY (-1,2) fixed")
    check(F(-1, 4) == (-5, 3) and F(-5, 3) == (-1, 4) and [y for a, y in door_list(-1, 4)] == [-17, -25, -37, -55] and [y for a, y in door_list(-5, 3)] == [-41, -61, -91], "PY the 2-cycle and its doors")
    check(node_at(-17, 1) == (-11, 1) and exit_data(-5, 3) == (-136, 3, -17) and exit_data(-11, 1)[1:] == (1, -17) and exit_data(-1, 4)[1:] == (1, -41), "PY the ring of three")
    chainM1 = {2: (-1, 1), 4: (-5, 1), 6: (-7, 2), 8: (-85, 1), 10: (-341, 1)}
    for s, stt in chainM1.items():
        check(node_at(-1, s) == stt and exit_data(*stt)[1:] == (s, -1) and stt[1] == 1 + v3(s), "PY door -1 branch %d" % s)
        if s > 2:
            check(parent(*stt) == (chainM1[s - 2], "cascade"), "PY door -1 cascade parent at branch %d" % s)
    exp_sing = {"list": [{"state": ["-5", "1"], "type": "cascade", "s": "4", "door": {"a": None, "y": "-1"}}],
                "dead": [{"a": "0", "y": "-3", "dead": True}], "excluded": []}
    check(n_children(-1, 1) == exp_sing, "PY (-1,1): one child (-5,1), door -3 dead")
    exp_fix = {"list": [{"state": ["-13", "1"], "type": "cascade", "s": "3", "door": {"a": "0", "y": "-5"}},
                        {"state": ["-1", "3"], "type": "door", "s": "2", "door": {"a": "1", "y": "-7"}}],
               "dead": [], "excluded": [exc("0", "-5", "1", ["-1", "2"], True, "door")]}
    check(n_children(-1, 2) == exp_fix, "PY (-1,2): two children, door -5 excluded")
    exp14 = {"list": [{"state": ["-109", "1"], "type": "cascade", "s": "3", "door": {"a": "0", "y": "-41"}},
                      {"state": ["-11", "2"], "type": "door", "s": "2", "door": {"a": "1", "y": "-25"}},
                      {"state": ["-49", "1"], "type": "door", "s": "2", "door": {"a": "2", "y": "-37"}},
                      {"state": ["-73", "1"], "type": "door", "s": "2", "door": {"a": "3", "y": "-55"}}],
             "dead": [], "excluded": [exc("0", "-17", "1", ["-11", "1"], False, "door")]}
    exp53 = {"list": [{"state": ["-181", "1"], "type": "cascade", "s": "5", "door": {"a": "0", "y": "-17"}},
                      {"state": ["-1", "5"], "type": "door", "s": "2", "door": {"a": "1", "y": "-61"}},
                      {"state": ["-121", "1"], "type": "door", "s": "2", "door": {"a": "2", "y": "-91"}}],
             "dead": [], "excluded": [exc("0", "-41", "1", ["-1", "4"], False, "door")]}
    exp111 = {"list": [{"state": ["-5", "2"], "type": "door", "s": "1", "door": {"a": "0", "y": "-23"}}],
              "dead": [], "excluded": [exc("0", "-17", "3", ["-5", "3"], False, "cascade")]}
    check(n_children(-1, 4) == exp14 and n_children(-5, 3) == exp53 and n_children(-11, 1) == exp111, "PY the ring nodes' children")
    ndist = {(-7, 1): ("sing", 1, 2), (-5, 1): ("sing", 0, 1), (-341, 1): ("sing", 0, 4), (-7, 3): ("sing", 5, 7), (-1, 1): ("sing", 0, 0),
             (-1, 3): ("fix", 1, 1), (-13, 1): ("fix", 1, 1), (-17, 1): ("fix", 2, 2), (-31, 1): ("fix", 4, 4), (-1, 2): ("fix", 0, 0),
             (-5, 2): ("two", 2, 1), (-181, 1): ("two", 1, 1), (-109, 1): ("two", 1, 1), (-11, 2): ("two", 1, 1), (-1543, 3): ("two", 14, 17),
             (-11, 1): ("two", 1, 0), (-1, 4): ("two", 0, 0), (-5, 3): ("two", 0, 0)}
    for stt, (k, eta, lam) in ndist.items():
        p = n_path(stt[0], stt[1], 10000)
        check(p["ring"] == k and p["eta"] == str(eta) and p["lambda"] == str(lam) and not p["capHit"], "PY negative distances %s" % (stt,))
        check(int(p["eta"]) - int(p["doorEdges"]) in (0, 1), "PY eta - door edges in {0,1} at %s" % (stt,))
    exp15 = [("-15", "odd", None), ("-44", "max", None), ("-22", "peak", None), ("-11", "door", None)]
    check(n_descent(-7, 1, 0) == [{"x": x, "tag": t, "sib": s} for x, t, s in exp15], "PY descent of -15")
    # the same expectations on the JS side (these requests were issued above)
    canary("nodeAt", (1, 1), ["1", "1"], "nodeAt(1,1)")
    for s in (3, 5, 7, 9):
        canary("nodeAt", (1, s), S(chain1[s]), "door 1 branch %d" % s)
    for s in (2, 4, 6):
        canary("nodeAt", (5, s), S(chain5[s][0]), "door 5 branch %d" % s)
    for s in (2, 4, 6, 8, 10):
        canary("nodeAt", (-1, s), S(chainM1[s]), "door -1 branch %d" % s)
    for y, r in zip((-5, -7, -17, -25, -41, -9), ("1", "2", "1", "2", "1", "0")):
        canary("mod3", (y,), r, "mod3(%d)" % y)
    check(res[idx["stateOfOdd"][-1]] is None, "JS stateOfOdd(-1) is null")
    for stt, k in zip(((1, 1), (-1, 1), (-1, 2), (-1, 4), (-5, 3), (-11, 1), (-5, 1), (-1, 3)), ("pos", "sing", "fix", "two", "two", "two", None, None)):
        canary("ringOf", stt, k, "ringOf%s" % (stt,))
    cap = res[idx["pathToRoot"][-1]]
    check(cap["capHit"] is True and cap["lambda"] is None and cap["eta"] is None and cap["ring"] is None and len(cap["path"]) == 3, "JS cap hit on (107,1) at cap 2")
    js_root = res[idx["children"][0]]
    check(js_root == exp_root, "JS root children")
    js_73 = res[idx["children"][canary_states.index((7, 3))]]
    check(js_73 == exp73, "JS (7,3) children")
    js_12d = res[idx["doors"][canary_states.index((1, 2))]]
    check(js_12d == [{"a": "0", "y": "3", "alive": False}, {"a": "1", "y": "5", "alive": True}], "JS (1,2) doors")
    for stt, (eta, lam) in dist.items():
        p = res[idx["pathToRoot"][canary_states.index(stt)]]
        check(p["eta"] == str(eta) and p["lambda"] == str(lam) and not p["capHit"] and p["ring"] == "pos", "JS distances %s" % (stt,))
    for stt, exp in (((-1, 1), exp_sing), ((-1, 2), exp_fix), ((-1, 4), exp14), ((-5, 3), exp53), ((-11, 1), exp111)):
        check(res[idx["children"][canary_states.index(stt)]] == exp, "JS children of %s" % (stt,))
    check(res[idx["F"][canary_states.index((-1, 1))]] is None and res[idx["parent"][canary_states.index((-1, 1))]] is None, "JS (-1,1): no F-image, no parent")
    for stt, (k, eta, lam) in ndist.items():
        p = res[idx["pathToRoot"][canary_states.index(stt)]]
        check(p["ring"] == k and p["eta"] == str(eta) and p["lambda"] == str(lam) and not p["capHit"], "JS negative distances %s" % (stt,))
    js_213 = res[idx["rawDescent"][len(reps)]]
    check(js_213 == [{"x": x, "tag": t, "sib": s} for x, t, s in exp213], "JS descent of 213")
    js_15 = res[idx["rawDescent"][len(reps) + 1]]
    check(js_15 == [{"x": x, "tag": t, "sib": s} for x, t, s in exp15], "JS descent of -15")
    out("  canaries: %d checks so far, %d failures" % (CHECKS - n0, FAILS))

    # --- per-state comparison, every function
    out("--- 2,000 random positive and 2,000 random negative states (|w| < 10^6, 3 does not divide w, d <= 40) plus %d canary states, every function ---" % len(canary_states))
    counts = {}
    ring_counts = {}
    for k, (w, d) in enumerate(all_states):
        pairs = [("exitData", n_exit(w, d)), ("F", n_state(F(w, d))), ("doors", n_doors(w, d)), ("parent", n_parent(w, d)),
                 ("children", n_children(w, d)), ("pathToRoot", n_path(w, d, 10000))]
        for fn, py in pairs:
            js = res[idx[fn][k]]
            check(js == py, "%s(%d,%d): JS %s vs PY %s" % (fn, w, d, json.dumps(js)[:160], json.dumps(py)[:160]))
            counts[fn] = counts.get(fn, 0) + 1
        y = exit_data(w, d)[2]
        js = res[idx["stateOfOdd"][k]]
        check(js == n_state(state_of_odd(y)) and js == n_state(F(w, d)), "stateOfOdd(%d) on the exit of (%d,%d)" % (y, w, d))
        counts["stateOfOdd"] = counts.get("stateOfOdd", 0) + 1
        r = pairs[5][1]["ring"]
        check((r == "pos") == (w > 0), "sign of the component at (%d,%d)" % (w, d))
        ring_counts[r] = ring_counts.get(r, 0) + 1
    for fn in ("exitData", "F", "stateOfOdd", "doors", "parent", "children", "pathToRoot"):
        out("  %-11s %5d states compared" % (fn, counts[fn]))
    lam_max = max(int(n_path(w, d, 10000)["lambda"]) for w, d in states)
    out("  largest lambda among the random states: %d; every path reached its ring (positive %d; singular %d, fixed %d, 2-cycle %d among all states)"
        % (lam_max, ring_counts.get("pos", 0), ring_counts.get("sing", 0), ring_counts.get("fix", 0), ring_counts.get("two", 0)))

    # --- go-to on random odd x
    out("--- 300 random odd x of each sign, |x| < 10^12: stateOfOdd(x) and the path to the ring (eta, lambda, full path) ---")
    base = len(all_states)
    lam_max = eta_max = 0
    for k, x in enumerate(xs):
        st = state_of_odd(x)
        js = res[idx["stateOfOdd"][base + k]]
        check(js == S(st), "stateOfOdd(%d)" % x)
        # the recovered state has x as its door a = v3(x+1), and the sign of x
        a = v3(x + 1)
        check(door_list(*st)[a][1] == x and (st[0] > 0) == (x > 0), "door recovery of %d" % x)
        py = n_path(st[0], st[1], 10000)
        jsp = res[idx["pathToRoot"][base + k]]
        check(jsp == py, "pathToRoot from x = %d" % x)
        lam_max = max(lam_max, int(py["lambda"]))
        eta_max = max(eta_max, int(py["eta"]))
    out("  600 x compared; largest lambda %d, largest eta %d; no cap hit" % (lam_max, eta_max))

    # --- raw descents
    out("--- 200 random representatives of each sign (state as above, a in 0..d-1): the raw descent by iterating Col ---")
    npts = 0
    nsib = 0
    for k, (w, d, a) in enumerate(reps):
        py = n_descent(w, d, a)
        js = res[idx["rawDescent"][k]]
        check(js == py, "rawDescent(%d,%d,%d)" % (w, d, a))
        npts += len(py)
        nsib += sum(1 for p in py if p["tag"] == "sibpeak")
        # every sibling peak named is a lower sibling on the same door with that peak
        A, s, y = exit_data(w, d)
        for p in py:
            if p["tag"] == "sibpeak":
                sw, sd = int(p["sib"][0]), int(p["sib"][1])
                A2, s2, y2 = exit_data(sw, sd)
                check(y2 == y and s2 < s and A2 == int(p["x"]), "sibling peak %s in the descent of (%d,%d,%d)" % (p["x"], w, d, a))
    out("  400 descents compared, %d points, %d lower-sibling peaks named" % (npts, nsib))

    # --- the rendering test
    out("--- rendering under a stubbed document: go-to (137,517), 213, a random 300-digit odd x, a path past the render cap, -17, a random negative 100-digit odd x, -13,1 ---")
    x300 = rng.randrange(10 ** 299, 10 ** 300) | 1
    xn100 = -(rng.randrange(10 ** 99, 10 ** 100) | 1)
    big_w = (2 ** 10003 + 1) // 3          # door 1's chain at branch 10003: level 5001, path 5002 nodes
    assert big_w % 3 != 0 and node_at(1, 10003) == (big_w, 1)
    cases = [
        {"name": "(137,517)", "input": "137,517", "state": (137, 517), "comma": True},
        {"name": "213", "input": "213", "state": state_of_odd(213), "comma": False},
        {"name": "300-digit x", "input": str(x300), "state": state_of_odd(x300), "comma": False},
        {"name": "render cap", "input": "%d,1" % big_w, "state": (big_w, 1), "comma": True},
        {"name": "-17", "input": "-17", "state": state_of_odd(-17), "comma": False},
        {"name": "-100-digit x", "input": str(xn100), "state": state_of_odd(xn100), "comma": False},
        {"name": "-13,1", "input": "-13,1", "state": (-13, 1), "comma": True},
    ]
    res_r = run_render([{"name": c["name"], "input": c["input"]} for c in cases])
    check("error" not in res_r, "rendering harness: " + str(res_r.get("error"))[:300])
    out("  page load under the stub, footer: %s" % res_r.get("selftest"))
    check(res_r.get("selftest") == "self-test: %s checks, 0 failures" % page_checks, "footer line matches selfTest() under node")
    out("  depth bound stated: %d (tree container > row > span > abbreviation or exponent)" % DEPTH_BOUND)
    for c, r in zip(cases, res_r.get("cases", [])):
        w, d = c["state"]
        path, cap_hit, de, ce, lam, ring = path_to_root(w, d, 10000)
        eta = eta_by_F(w, d, ring)
        exp_rows, exp_cards, exp_stubs, exp_greys, full_rows, hid = expected_rows([p[0] for p in path], ring)
        if "error" in r:
            check(False, "%s: exception %s" % (c["name"], r["error"][:300]))
            out("  %-12s EXCEPTION: %s" % (c["name"], r["error"][:200]))
            continue
        m = TreeMeasure()
        m.feed(r["tree"])
        out("  %-12s %s; path %d nodes (lambda %d, eta %d): max nesting depth %d, rendered rows %d (cards %d, stubs %d, note rows %d), no exception; a full expansion of the ancestors would render %d rows%s"
            % (c["name"], ring, len(path), lam, eta, m.max_depth, m.rows, m.cards, m.stubs, m.greys, full_rows,
               ("; %d ancestors folded" % hid) if hid else ""))
        check(m.max_depth <= DEPTH_BOUND, "%s: nesting depth %d > %d" % (c["name"], m.max_depth, DEPTH_BOUND))
        check(m.rows == exp_rows and m.cards == exp_cards and m.stubs == exp_stubs and m.greys == exp_greys,
              "%s: rows %d/%d cards %d/%d stubs %d/%d notes %d/%d (page/expected)" % (c["name"], m.rows, exp_rows, m.cards, exp_cards, m.stubs, exp_stubs, m.greys, exp_greys))
        check(m.rows < full_rows or len(path) <= 2, "%s: rows %d not below a full expansion's %d" % (c["name"], m.rows, full_rows))
        check(True, "%s: no exception" % c["name"])
        text = r["msg"]
        check(r["root"] == ring, "%s: the root selector reads %s, expected %s" % (c["name"], r["root"], ring))
        check((ring == "pos") == ("census counts to level 27" in r["note"]) and (ring != "pos") == ("18.8.3" in r["note"]), "%s: the tree note names the census only at the positive root" % c["name"])
        check(("Placed (%d, %d)" % (w, d) if len(str(w)) <= 24 else "Placed (") in text and ("level %s" % format(lam, ",")) in text and ("η = %s" % format(eta, ",")) in text, "%s: message places the node at level %d with eta %d" % (c["name"], lam, eta))
        check(("%s ancestors on the path shown" % format(len(path) - 1, ",")) in text, "%s: message states the ancestor count" % c["name"])
        if ring != "pos":
            check("the root selector switched to it" in text and ("census: see comb.md 18.8" in r["tree"]), "%s: the switch is announced and the census line defers to 18.8" % c["name"])
        else:
            check("root selector switched" not in text, "%s: no switch from the default root" % c["name"])
        if c["comma"]:
            joined = c["input"].replace(",", "")
            lead = "read as the state ("
            check(text.startswith(lead), "%s: message begins with the comma reading" % c["name"])
            if int(joined) % 2 == 1:
                check(('data-x="%s"' % joined) in text and "type it without the comma" in text, "%s: the odd-integer alternative is offered as a link" % c["name"])
        if c["name"] == "(137,517)":
            check(len(path) == 1365 and lam == 1364 and eta == 1056, "(137,517): path 1365, lambda 1364, eta 1056")
            check(text.startswith("read as the state (137, 517) — for the odd integer 137517, "), "(137,517): the message's opening")
        if c["name"] == "render cap":
            check(hid > 0 and "ancestors not shown" in r["tree"] and "folded into one row" in text, "render cap: the fold row and the message")
        if c["name"] == "-17":
            check(path == [((-1, 4), -82, 1, -41, None)] and lam == 0 and eta == 0 and text.startswith("x = -17 is the door y<sub>0</sub> of exactly one state"), "-17: the ring node (-1,4) itself, its top door")
        if c["name"] == "-13,1":
            check(text.startswith("read as the state (-13, 1) — for the odd integer -131, ") and "fixed state" in text, "-13,1: the comma reading and the switch to the fixed state")
    # the comma reading that is not a state but whose digits joined are odd: the integer reading is offered
    res_c = run_render([{"name": "9,1", "input": "9,1"}, {"name": "-1", "input": "-1"}, {"name": "-2", "input": "-2"}])
    rc = res_c.get("cases", [{}])[0]
    check("error" not in rc and "not a valid state" in rc.get("msg", "") and 'data-x="91"' in rc.get("msg", ""), "9,1: invalid state, integer 91 offered")
    out("  9,1 (not a state): refused, the odd integer 91 offered as a link")
    rm = res_c.get("cases", [{}, {}])[1]
    check("error" not in rm and rm.get("msg", "").startswith("−1 is the singular door") and rm.get("root") == "pos", "-1: refused in one line, nothing placed")
    out("  -1: refused in one line (the singular door; the door of no state)")
    re2 = res_c.get("cases", [{}, {}, {}])[2]
    check("error" not in re2 and "must be an odd integer" in re2.get("msg", ""), "-2: refused")

    out("")
    for l in FAIL_LINES:
        out(l)
    out("TOTAL: checks = %d, failures = %d" % (CHECKS, FAILS))
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(LINES) + "\n")
    sys.exit(0 if FAILS == 0 else 1)


if __name__ == "__main__":
    main()
