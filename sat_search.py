"""SAT searches on the torus (Z/kZ)^2 (needs python-sat).

    python sat_search.py find K [SIZE]   # a set of SIZE points (default 2K+2) meeting every line twice
    python sat_search.py none K SIZE     # report UNSAT if no such set of at most SIZE points exists

Lines are the 4K rows, columns, diagonals x-y=c and antidiagonals x+y=c.
Translations act on solutions, so the point (0,0) is assumed to be in A.
"""

import sys

from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool
from pysat.solvers import Cadical153


def lines(k):
    for c in range(k):
        yield [(c, y) for y in range(k)]
        yield [(x, c) for x in range(k)]
        yield [(x, (x - c) % k) for x in range(k)]
        yield [(x, (c - x) % k) for x in range(k)]


def search(k, size):
    pool = IDPool()
    var = lambda p: pool.id(p)
    cnf = CNF()
    for L in lines(k):
        cnf.extend(CardEnc.atleast([var(p) for p in L], 2, vpool=pool, encoding=EncType.seqcounter).clauses)
    cells = [var((x, y)) for x in range(k) for y in range(k)]
    cnf.extend(CardEnc.atmost(cells, size, vpool=pool, encoding=EncType.seqcounter).clauses)
    cnf.append([var((0, 0))])
    with Cadical153(bootstrap_with=cnf.clauses) as s:
        if not s.solve():
            return None
        model = set(l for l in s.get_model() if l > 0)
    return [(x, y) for x in range(k) for y in range(k) if var((x, y)) in model]


if __name__ == "__main__":
    mode, k = sys.argv[1], int(sys.argv[2])
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 2 * k + 2
    A = search(k, size)
    if A is None:
        print(f"k={k}: UNSAT, no set of at most {size} points meets every line twice")
    else:
        print(f"k={k}: found {len(A)} points: {A}")
        S = set(A)
        for x in range(k):
            print(" ".join("#" if (x, y) in S else "." for y in range(k)))
