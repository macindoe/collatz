"""Independent check of the arithmetic core of viz/spider_explorer.html against a
fresh Python implementation of spiders.md section 19 (the spider layer), built on
the comb.md section 18 primitives it shares with viz/comb_explorer.html (positive
comb only -- the spider explorer never takes a negative input).

Supports: briefs/spider-explorer-brief.md; spiders.md section 19 (Definition
19.1.1, Lemma 19.1.2, Lemma 19.1.3, Lemma 19.1.5, Lemma 19.1.6, Definition 19.2.1,
Theorem 19.2.2, Definition 19.3.1); comb.md 18.2.1-18.2.3, 18.3.

What it does:
  1. Reads viz/spider_explorer.html, extracts the text between the two marker
     lines `// === SPIDER CORE BEGIN ===` and `// === SPIDER CORE END ===`,
     refuses the block if it contains DOM access, appends a stdin/stdout JSON
     harness (requests {fn, args}, nested arrays and strings of digits read as
     BigInt, results with every BigInt rendered as a decimal string) and runs it
     once under node (v20 is installed; `shutil.which`). If node is not on the
     PATH the script says so and exits with status 2 -- it never passes
     vacuously.
  2. Implements owner, legs, hair, spider, the classes and the continuation
     rules independently here, in fresh Python, from spiders.md's own
     definitions -- not from the page's JavaScript:
       the classification (Definition 19.1.1): abdomen D>=2, fork/link by
         Omega mod 3 at D=1, root only (1,1);
       a link's one child, always a fork of depth 1 (Lemma 19.1.2);
       a fork's two children (cascade, depth t+1, and top-door, depth t, same
         core (4*Omega-1)/3^t, t = v3(4*Omega-1) >= 1) and the exact class
         split at t=1 by Omega mod 9 (Lemma 19.1.3);
       owner(state): ascend through comb parents while the class stays
         depth-1, terminating at an abdomen or the root (Theorem 19.2.2);
       legs(abdomen): the abdomen's depth-1 children, with the rule that
         produced each (cascade, or door a) and the leg's own class;
       hair(leg): the chain from a leg to where it ends, class/residues/t at
         each node, and the child spiders every fork spawns along the way
         (its cascade child always, its top-door child too when t>=2,
         Definition 19.3.1);
       spider(abdomen): the abdomen, its legs, its hairs, its size, every
         child spider it spawns (from the abdomen's own a=1 and top-door
         children when they are not legs, and from every hair fork), and its
         parent spider owner(comb parent(abdomen)); the root is handled by a
         dedicated root_piece(), not the D>=2 abdomen formula.
  3. Compares the two on the canaries of the brief and spiders.md's own
     Verified paragraphs (the spider of (1,2) with its four child spiders per
     the corrected hand derivation; (17,1) an orphan link owned by (5,2); the
     leg (13,1) of (5,2) with children (17,2)/(17,1); the leg (7,1) with
     children (1,4)/(1,3); the root's own piece), on 1,000 random abdomens
     (Omega < 10^6, 2 <= D <= 12, seed 20260923) for the FULL spider -- size,
     legs with rules, every hair node by node with class and rule, the
     child-spider list with spawning nodes and rules, the parent spider -- on
     500 random depth-1 nodes for owner, and on 300 random odd x < 10^12 for
     the go-to (door recovery then owner).
  4. Rendering test: loads both of the page's script blocks under node with a
     stubbed `document`, drives the go-to box for (1,2), for the odd integer
     17, and for the random abdomen (among the 1,000 above) whose spider has
     the longest single hair, measuring on the produced #content HTML with
     Python's own html.parser: the maximum element nesting depth under the
     container (a small stated constant, DEPTH_BOUND) and the rendered row
     count and per-kind row breakdown against the count computed here from the
     Python spider structure's own row-generation rule (mirroring the page's
     renderSpider exactly: one abdomen/root row; per hair, one leg-head row
     plus one node row and one rule row per hair node; one "the borders"
     header row, one row per child spider, and one parent-spider row).
  5. Prints per-function counts and `TOTAL: checks = N, failures = 0`.

Fresh code: imports nothing from any other file in this repository. Exact
integers at every pass/fail decision. Seed 20260923. Single reproducing command:

    python experiments/spider_explorer_check.py

The script prints its report and also writes it to
experiments/spider_explorer_check_output.txt (the committed output, written by
the script itself -- no shell redirection, no BOM).
"""

import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser

SEED = 20260923
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGE = os.path.join(ROOT, "viz", "spider_explorer.html")
OUT = os.path.join(HERE, "spider_explorer_check_output.txt")
BEGIN = "// === SPIDER CORE BEGIN ==="
END = "// === SPIDER CORE END ==="

LINES = []


def out(s=""):
    print(s)
    LINES.append(s)


# ----------------------------------------------------------------------------
# The independent Python implementation (comb.md section 18, positive comb;
# spiders.md section 19)
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
    return n % 3


def modn(n, k):
    return n % k


def is_valid_state(w, d):
    return w != 0 and w % 2 == 1 and w % 3 != 0 and d >= 1


def is_root(w, d):
    return w == 1 and d == 1


def exit_data(w, d):
    A = 3 ** d * w - 1
    s = v2(A)
    y = exact_div(A, 1 << s)
    return A, s, y


def state_of_odd(y):
    if y == -1:
        return None
    n = y + 1
    m = v2(n)
    u = exact_div(n, 1 << m)
    a = v3(u)
    return (exact_div(u, 3 ** a), m + a)


def F(w, d):
    A, s, y = exit_data(w, d)
    return state_of_odd(y)


def node_at(y, s):
    N = (y << s) + 1
    d = v3(N)
    return (exact_div(N, 3 ** d), d)


def lowest_branch(y):
    return 1 if mod3(y) == 1 else 2


def door_list(W, D):
    lst = []
    for a in range(D):
        y = (W << (D - a)) * 3 ** a - 1
        lst.append((a, y, mod3(y) != 0))
    return lst


def comb_parent(w, d):
    if is_root(w, d):
        return None
    A, s, y = exit_data(w, d)
    if s >= 3:
        return (node_at(y, s - 2), 'cascade')
    return (state_of_odd(y), 'door')


def comb_children(W, D):
    """(list, dead, excluded): list of (state, type, a, y); dead of (a, y);
    excluded of (state, type, a, y) -- children that are the root (comb.md
    Proposition 18.2.3)."""
    A, s, y = exit_data(W, D)
    lst, dead, excluded = [], [], []
    casc = node_at(y, s + 2)
    cd_a = v3(y + 1)
    if is_root(*casc):
        excluded.append((casc, 'cascade', cd_a, y))
    else:
        lst.append((casc, 'cascade', cd_a, y))
    for a, dy, alive in door_list(W, D):
        if not alive:
            dead.append((a, dy))
            continue
        s0 = lowest_branch(dy)
        st = node_at(dy, s0)
        if st == (W, D):
            excluded.append((st, 'door-self', a, dy))
            continue
        if is_root(*st):
            excluded.append((st, 'door', a, dy))
            continue
        lst.append((st, 'door', a, dy))
    return lst, dead, excluded


def node_class(state, parent_depth):
    """root | abdomen | leg | orphan link | hair fork (spiders.md Definition
    19.1.1, Definition 19.2.1); parent_depth is read only for a depth-1 node."""
    w, d = state
    if is_root(w, d):
        return 'root'
    if d >= 2:
        return 'abdomen'
    own_link = (mod3(w) == 2)
    if parent_depth is not None and parent_depth >= 2:
        return 'leg'
    return 'orphan link' if own_link else 'hair fork'


def owner(state):
    """Ascend through comb parents while the class stays depth-1, terminating
    at an abdomen or the root (Theorem 19.2.2)."""
    cur = state
    while True:
        if is_root(*cur) or cur[1] >= 2:
            return cur
        cur = comb_parent(*cur)[0]


def legs(abdomen):
    W, D = abdomen
    lst, dead, excluded = comb_children(W, D)
    result = []
    for st, etype, a, y in lst:
        if st[1] == 1:
            rule = ('cascade', None) if etype == 'cascade' else ('door', a)
            result.append({'state': st, 'rule': rule, 'class': node_class(st, D)})
    return result


def hair(leg_state):
    """The chain from a leg to where it ends (Definition 19.2.1). Every node
    carries a structured ruleKind -- 'link' (Lemma 19.1.2), 'fork-continue' or
    'fork-end' (Lemma 19.1.3) -- never prose, matching the page's core. Every
    fork spawns its cascade child (always an abdomen); when it ends the hair
    (t >= 2) it also spawns its top-door child (Definition 19.3.1)."""
    nodes = []
    spawned = []
    cur = leg_state
    first = True
    while True:
        w = cur[0]
        cls = 'leg' if first else node_class(cur, 1)
        rec = {'state': cur, 'class': cls, 'mod3': mod3(w), 'mod8': modn(w, 8),
               'mod9': modn(w, 9), 'mod24': modn(w, 24), 't': None, 'ruleKind': None, 'ruleNext': None}
        first = False
        if mod3(w) == 2:
            child = 4 * w - 1
            rec['ruleKind'] = 'link'
            nodes.append(rec)
            cur = (child, 1)
            continue
        t = v3(4 * w - 1)
        rec['t'] = t
        core = exact_div(4 * w - 1, 3 ** t)
        spawned.append({'from': cur, 'state': (core, t + 1), 'ruleKind': 'cascade', 't': t})
        if t == 1:
            nine = modn(w, 9)
            rec['ruleKind'] = 'fork-continue'
            rec['ruleNext'] = 'fork' if nine == 1 else 'link'
            nodes.append(rec)
            cur = (core, 1)
            continue
        rec['ruleKind'] = 'fork-end'
        spawned.append({'from': cur, 'state': (core, t), 'ruleKind': 'top-door', 't': t})
        nodes.append(rec)
        break
    return {'nodes': nodes, 'spawned': spawned}


def root_piece():
    return {'abdomen': (1, 1), 'legs': [], 'hairs': [], 'size': 1,
            'childSpiders': [{'from': (1, 1), 'state': (1, 2), 'ruleKind': 'root-child', 't': None}],
            'parentSpider': None, 'isRoot': True}


def spider(abdomen):
    """The whole piece (Definition 19.2.1, Definition 19.3.1). Refuses
    gracefully at the root: root_piece(), not the D>=2 abdomen formula, since
    the root's own cascade child (1,2) is an abdomen -- a fact the general
    formula (whose cascade child is always a leg, Lemma 19.1.6) does not
    cover."""
    W, D = abdomen
    if is_root(W, D):
        return root_piece()
    leg_list = legs(abdomen)
    hairs = [hair(l['state']) for l in leg_list]
    size = 1
    spawned = []
    for h in hairs:
        size += len(h['nodes'])
        spawned.extend(h['spawned'])
    lst, dead, excluded = comb_children(W, D)
    for st, etype, a, y in lst:
        if etype == 'door' and a == 1 and st[1] >= 2:
            spawned.append({'from': abdomen, 'state': st, 'ruleKind': 'a1', 't': None})
        if etype == 'door' and a == 0 and st[1] >= 2:
            spawned.append({'from': abdomen, 'state': st, 'ruleKind': 'top-door-abdomen', 't': None})
    p_state, p_type = comb_parent(W, D)
    parent_spider = owner(p_state)
    return {'abdomen': abdomen, 'legs': leg_list, 'hairs': hairs, 'size': size,
            'childSpiders': spawned, 'parentSpider': parent_spider, 'parentEdge': p_type, 'isRoot': False}


# ----------------------------------------------------------------------------
# Wire format: converts the Python spider() structure to the same shape
# JSON.stringify(spider(...)) produces on the JS side (every integer a decimal
# string, via the BigInt replacer both scripts use), for direct dict equality.
# ----------------------------------------------------------------------------

def w_state(st):
    return None if st is None else [str(st[0]), str(st[1])]


def w_int(n):
    return None if n is None else str(n)


def w_leg(l):
    rule = {'kind': l['rule'][0]}
    if l['rule'][0] == 'door':
        rule['a'] = str(l['rule'][1])
    return {'state': w_state(l['state']), 'rule': rule, 'class': l['class']}


def w_node(n):
    return {'state': w_state(n['state']), 'class': n['class'], 'mod3': w_int(n['mod3']), 'mod8': w_int(n['mod8']),
            'mod9': w_int(n['mod9']), 'mod24': w_int(n['mod24']), 't': w_int(n['t']),
            'ruleKind': n['ruleKind'], 'ruleNext': n['ruleNext']}


def w_spawn(c):
    return {'from': w_state(c['from']), 'state': w_state(c['state']), 'ruleKind': c['ruleKind'], 't': w_int(c['t'])}


def w_hair(h):
    return {'nodes': [w_node(n) for n in h['nodes']], 'spawned': [w_spawn(s) for s in h['spawned']]}


def w_spider(sp):
    d = {'abdomen': w_state(sp['abdomen']), 'legs': [w_leg(l) for l in sp['legs']],
         'hairs': [w_hair(h) for h in sp['hairs']], 'size': w_int(sp['size']),
         'childSpiders': [w_spawn(c) for c in sp['childSpiders']],
         'parentSpider': w_state(sp['parentSpider']), 'isRoot': sp['isRoot']}
    if not sp['isRoot']:
        d['parentEdge'] = sp['parentEdge']
    return d


# ----------------------------------------------------------------------------
# The node harness: extracts the core, runs it under node
# ----------------------------------------------------------------------------

HARNESS = r"""
function __toBig(x){
  if (x === null) return null;
  if (Array.isArray(x)) return x.map(__toBig);
  if (typeof x === 'string' && /^-?\d+$/.test(x)) return BigInt(x);
  return x;
}
const __chunks = [];
process.stdin.setEncoding('utf8');
process.stdin.on('data', c => __chunks.push(c));
process.stdin.on('end', () => {
  const reqs = JSON.parse(__chunks.join(''));
  const fns = { v2, v3, mod3, modN, exactDiv, isValidState, isRoot, exitData, stateOfOdd, F, nodeAt, lowestBranch, doors, parent, children, nodeClass, owner, legs, hair, spider, selfTest };
  const res = reqs.map(r => fns[r.fn](...r.args.map(__toBig)));
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
        js = os.path.join(td, "spider_core_run.js")
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

RENDER_HARNESS = r"""
const __fs = require('fs');
const __html = __fs.readFileSync(process.argv[2], 'utf8');
const __blocks = [...__html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
if (__blocks.length !== 2) { process.stdout.write(JSON.stringify({ error: 'expected 2 script blocks, found ' + __blocks.length })); process.exit(0); }
const __els = {}, __listeners = {};
function __el(id){
  if (!__els[id]) {
    const e = { id, _c: '', value: '', addEventListener: (t, f) => { (__listeners[id] = __listeners[id] || {})[t] = f; } };
    Object.defineProperty(e, 'innerHTML', { get: () => e._c, set: v => { e._c = v; } });
    Object.defineProperty(e, 'textContent', { get: () => e._c, set: v => { e._c = v; } });
    __els[id] = e;
  }
  return __els[id];
}
global.document = { getElementById: id => __el(id) };
global.window = {};
const __chunks = [];
process.stdin.setEncoding('utf8');
process.stdin.on('data', c => __chunks.push(c));
process.stdin.on('end', () => {
  const cases = JSON.parse(__chunks.join(''));
  const out = { selftest: null, cases: [] };
  try { new Function(__blocks[0] + '\n' + __blocks[1])(); out.selftest = __els.selftest.textContent; }
  catch (e) { out.error = 'load: ' + (e && e.stack ? e.stack : e); process.stdout.write(JSON.stringify(out)); return; }
  for (const c of cases) {
    const r = { name: c.name };
    try {
      __els.goto.value = c.input;
      __listeners.goBtn.click();
      r.content = __els.content.innerHTML;
      r.msg = __els.msg.textContent;
    } catch (e) { r.error = String(e && e.stack ? e.stack : e); }
    out.cases.push(r);
  }
  process.stdout.write(JSON.stringify(out));
});
"""


class ContentMeasure(HTMLParser):
    """Depth and per-kind row statistics of #content's innerHTML. A row is a
    direct child <div> of the container; its `kind` is the second class token
    of `class="row <kind>"`, or 'node' for a bare `class="row"` (a hair node)."""

    VOID = {"br", "img", "input", "hr", "meta", "link"}

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.max_depth = 0
        self.rows = 0
        self.by_kind = {}

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            return
        self.depth += 1
        self.max_depth = max(self.max_depth, self.depth)
        if self.depth == 1:
            self.rows += 1
            cls = dict(attrs).get("class", "")
            toks = cls.split()
            kind = toks[1] if len(toks) > 1 else "node"
            self.by_kind[kind] = self.by_kind.get(kind, 0) + 1

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        self.depth -= 1


DEPTH_BOUND = 3   # container(0) > row(1) > link-or-span(2) > abbreviated-integer span(3)


def expected_rows(sp):
    """The row count and per-kind breakdown renderSpider() produces from a
    spider structure, mirrored exactly: one abdomen/root row; per hair, one
    leg-head row plus one node row and one rule row per hair node; when shown
    (always, in practice: a non-root spider always has a parent, the root
    always has its one child spider), one "the borders" header row (class
    `leghead`, folded into that count), one row per child spider, and one
    parent-spider row for a non-root spider."""
    leghead = len(sp['hairs'])
    node = sum(len(h['nodes']) for h in sp['hairs'])
    rule = node
    rows = 1 + leghead + node + rule
    border = 0
    parentrow = 0
    show_borders = len(sp['childSpiders']) > 0 or (not sp['isRoot'])
    if show_borders:
        leghead += 1
        rows += 1
        border = len(sp['childSpiders'])
        rows += border
        if not sp['isRoot']:
            parentrow = 1
            rows += 1
    by_kind = {'abdomen': 1, 'leghead': leghead, 'node': node, 'rule': rule, 'border': border, 'parentrow': parentrow}
    by_kind = {k: v for k, v in by_kind.items() if v > 0}
    return rows, by_kind


def run_render(cases):
    node = shutil.which("node")
    if node is None:
        out("ERROR: node is not on the PATH; the rendering test cannot run.")
        sys.exit(2)
    with tempfile.TemporaryDirectory() as td:
        js = os.path.join(td, "spider_render_run.js")
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
        if len(FAIL_LINES) < 60:
            FAIL_LINES.append("  FAIL: " + what)


def S(st):
    return None if st is None else [str(st[0]), str(st[1])]


def main():
    rng = random.Random(SEED)
    out("spider_explorer_check.py -- seed %d, 2026-09-23" % SEED)
    core, ncore = extract_core()
    out("core block: %d lines between the markers, no DOM access" % ncore)

    def rand_depth1():
        w = rng.randrange(1, 10 ** 6, 2)
        if w % 3 == 0:
            w += 2
        return w

    def rand_abdomen():
        w = rand_depth1()
        d = rng.randrange(2, 13)
        return (w, d)

    abdomens = [rand_abdomen() for _ in range(1000)]
    depth1_nodes = [(rand_depth1(), 1) for _ in range(500)]
    xs = [rng.randrange(1, 10 ** 12, 2) for _ in range(300)]

    canary_abdomens = [(1, 2), (1, 1), (5, 2), (7, 3)]
    all_abdomens = canary_abdomens + abdomens
    canary_states = [(17, 1), (13, 1), (7, 1)] + depth1_nodes

    # --- build the request list for node, one batch
    reqs = []
    idx = {}

    def req(fn, *args):
        idx.setdefault(fn, []).append(len(reqs))
        reqs.append({"fn": fn, "args": list(args)})

    req("selfTest")
    for w, d in all_abdomens:
        req("spider", [str(w), str(d)])
    for w, d in canary_states:
        req("owner", [str(w), str(d)])
    for x in xs:
        st = state_of_odd(x)
        req("owner", [str(st[0]), str(st[1])])
        req("stateOfOdd", str(x))

    ver, res = run_node(core, reqs)
    out("node %s; %d requests answered" % (ver, len(res)))

    # --- the page's own self-test, as exercised under node
    st = res[idx["selfTest"][0]]
    out("--- the page's selfTest() under node ---")
    out("  self-test: %s checks, %d failures" % (st["checks"], len(st["failures"])))
    check(int(st["checks"]) > 0 and len(st["failures"]) == 0, "page selfTest: " + "; ".join(st["failures"][:5]))
    page_checks = st["checks"]

    # --- canaries: spiders.md's own Verified paragraphs and briefs/spider-layer-findings.md
    out("--- canaries (the spider of (1,2); the root's piece; (17,1)/(13,1)/(7,1)) ---")
    n0 = CHECKS
    sp12 = spider((1, 2))
    check(len(sp12['legs']) == 2 and sorted(l['state'] for l in sp12['legs']) == [(7, 1), (11, 1)],
          "PY spider(1,2) legs, got %s" % (sp12['legs'],))
    check(sp12['size'] == 4, "PY spider(1,2) size, got %d" % sp12['size'])
    child_set = sorted(c['state'] for c in sp12['childSpiders'])
    check(child_set == [(1, 3), (1, 4), (19, 2), (19, 3)], "PY spider(1,2) four child spiders, got %s" % child_set)
    h11 = next(h for h in sp12['hairs'] if h['nodes'][0]['state'] == (11, 1))
    check(len(h11['nodes']) == 2 and h11['nodes'][1]['state'] == (43, 1) and h11['nodes'][1]['t'] == 2,
          "PY hair (11,1)->(43,1), t=2 at (43,1)")
    h7 = next(h for h in sp12['hairs'] if h['nodes'][0]['state'] == (7, 1))
    check(len(h7['nodes']) == 1 and h7['nodes'][0]['t'] == 3, "PY hair (7,1) alone, t=3")
    check(sp12['parentSpider'] == (1, 1), "PY spider(1,2) parent spider is the root's piece")
    sp_root = spider((1, 1))
    check(sp_root['isRoot'] and sp_root['size'] == 1 and [c['state'] for c in sp_root['childSpiders']] == [(1, 2)],
          "PY spider(1,1) is the root's piece with child spider (1,2)")
    p17 = comb_parent(17, 1)
    check(p17 == ((13, 1), 'door'), "PY parent(17,1) = (13,1), got %s" % (p17,))
    check(node_class((17, 1), p17[0][1]) == 'orphan link', "PY nodeClass (17,1) orphan link")
    gp17 = comb_parent(*p17[0])[0]
    check(owner((17, 1)) == owner(gp17) == (5, 2), "PY owner(17,1) = owner(grandparent) = (5,2), got %s" % (owner((17, 1)),))
    check(owner((13, 1)) == (5, 2) and node_class((13, 1), 2) == 'leg', "PY (13,1) a leg of (5,2)")
    c13 = sorted(st for st, *_ in comb_children(13, 1)[0])
    check(c13 == [(17, 1), (17, 2)], "PY (13,1) children (17,1),(17,2), got %s" % c13)
    c7 = sorted(st for st, *_ in comb_children(7, 1)[0])
    check(c7 == [(1, 3), (1, 4)], "PY (7,1) children (1,3),(1,4), got %s" % c7)
    check(node_class((7, 1), 2) == 'leg', "PY (7,1) leg")
    out("  %d canary checks so far, %d failures" % (CHECKS - n0, FAILS))

    # the same expectations against the JS side (issued in the requests above)
    js_sp12 = res[idx["spider"][0]]
    check(js_sp12 == w_spider(sp12), "JS spider(1,2) matches the Python structure exactly")
    js_sp_root = res[idx["spider"][1]]
    check(js_sp_root == w_spider(sp_root), "JS spider(1,1) matches the Python root's-piece structure exactly")
    js_sp52 = res[idx["spider"][2]]
    check(js_sp52 == w_spider(spider((5, 2))), "JS spider(5,2) matches the Python structure exactly")
    js_sp73 = res[idx["spider"][3]]
    check(js_sp73 == w_spider(spider((7, 3))), "JS spider(7,3) matches the Python structure exactly")
    for st in canary_states[:3]:
        i = canary_states.index(st)
        js_own = res[idx["owner"][i]]
        check(js_own == S(owner(st)), "JS owner%s = %s, got %s" % (st, owner(st), js_own))

    # --- the full comparison: spider() on 1,000 random abdomens
    out("--- 1,000 random abdomens (Omega < 10^6, 2 <= D <= 12) plus %d canary abdomens: the full spider ---" % len(canary_abdomens))
    n1 = CHECKS
    sizes = []
    longest_hair = (-1, None)
    for k, (w, d) in enumerate(all_abdomens):
        py = spider((w, d))
        js = res[idx["spider"][k]]
        wire = w_spider(py)
        check(js == wire, "spider(%d,%d): JS vs PY mismatch" % (w, d))
        sizes.append(py['size'])
        for h in py['hairs']:
            if len(h['nodes']) > longest_hair[0]:
                longest_hair = (len(h['nodes']), (w, d))
    out("  %d spiders compared, 0 mismatches expected; size range %d..%d, mean %.3f"
        % (len(all_abdomens), min(sizes), max(sizes), sum(sizes) / len(sizes)))
    out("  longest single hair among the 1,000 random abdomens: %d nodes, in the spider of (%d,%d)"
        % (longest_hair[0], longest_hair[1][0], longest_hair[1][1]))
    out("  full-spider comparison: %d checks so far (cumulative), %d failures" % (CHECKS - n0, FAILS - (n0 - n0)))

    # --- owner on 500 random depth-1 nodes
    out("--- 500 random depth-1 nodes: owner ---")
    n2 = CHECKS
    for k, st in enumerate(depth1_nodes):
        py_own = owner(st)
        js_own = res[idx["owner"][3 + k]]
        check(js_own == S(py_own), "owner%s: JS %s vs PY %s" % (st, js_own, S(py_own)))
        check(node_class(py_own, None) in ('abdomen', 'root'), "owner%s is an abdomen or the root" % (st,))
    out("  %d checks, 0 failures expected" % (CHECKS - n2))

    # --- the go-to: 300 random odd x < 10^12, door recovery then owner
    out("--- 300 random odd x < 10^12: the go-to (stateOfOdd then owner) ---")
    n3 = CHECKS
    base = 3 + len(depth1_nodes)
    for k, x in enumerate(xs):
        py_state = state_of_odd(x)
        js_state = res[idx["stateOfOdd"][k]]
        check(js_state == S(py_state), "stateOfOdd(%d): JS %s vs PY %s" % (x, js_state, S(py_state)))
        py_own = owner(py_state)
        js_own = res[idx["owner"][base + k]]
        check(js_own == S(py_own), "owner of stateOfOdd(%d) = %s: JS %s vs PY %s" % (x, py_state, js_own, S(py_own)))
    out("  %d checks, 0 failures expected" % (CHECKS - n3))

    # --- the rendering test
    out("--- rendering under a stubbed document: go-to (1,2), the odd integer 17, and the longest-hair abdomen (%d,%d) ---"
        % (longest_hair[1][0], longest_hair[1][1]))
    long_w, long_d = longest_hair[1]
    cases = [
        {"name": "(1,2)", "input": "1,2", "state": (1, 2)},
        {"name": "17", "input": "17", "state": state_of_odd(17)},
        {"name": "longest-hair abdomen (%d,%d)" % (long_w, long_d), "input": "%d,%d" % (long_w, long_d), "state": (long_w, long_d)},
    ]
    res_r = run_render([{"name": c["name"], "input": c["input"]} for c in cases])
    check("error" not in res_r, "rendering harness: " + str(res_r.get("error"))[:300])
    out("  page load under the stub, footer: %s" % res_r.get("selftest"))
    check(res_r.get("selftest") == "self-test: %s checks, 0 failures" % page_checks, "footer line matches selfTest() under node")
    out("  depth bound stated: %d (container > row > link-or-span > abbreviated-integer span)" % DEPTH_BOUND)
    for c, r in zip(cases, res_r.get("cases", [])):
        w, d = c["state"]
        own = owner((w, d))
        py_sp = spider(own)
        exp_rows, exp_kinds = expected_rows(py_sp)
        if "error" in r:
            check(False, "%s: exception %s" % (c["name"], r["error"][:300]))
            out("  %-32s EXCEPTION: %s" % (c["name"], r["error"][:200]))
            continue
        m = ContentMeasure()
        m.feed(r["content"])
        out("  %-32s owner %s, spider size %d: max nesting depth %d, rendered rows %d %s"
            % (c["name"], own, py_sp['size'], m.max_depth, m.rows, m.by_kind))
        check(m.max_depth <= DEPTH_BOUND, "%s: nesting depth %d > %d" % (c["name"], m.max_depth, DEPTH_BOUND))
        check(m.rows == exp_rows, "%s: rows %d (page) vs %d (expected)" % (c["name"], m.rows, exp_rows))
        check(m.by_kind == exp_kinds, "%s: row kinds %s (page) vs %s (expected)" % (c["name"], m.by_kind, exp_kinds))
        check("error" not in r, "%s: no exception" % c["name"])
        check(("owned by the spider of" in r["msg"]) or ("root" in r["msg"]), "%s: message names the owner" % c["name"])
    out("  a full expansion is not applicable here: the page never precomputes a neighbour spider beyond its stub (spiders.md 19.2's own guard)")

    out("")
    for l in FAIL_LINES:
        out(l)
    out("TOTAL: checks = %d, failures = %d" % (CHECKS, FAILS))
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(LINES) + "\n")
    sys.exit(0 if FAILS == 0 else 1)


if __name__ == "__main__":
    main()
