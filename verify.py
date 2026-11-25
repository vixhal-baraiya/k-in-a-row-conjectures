"""Check the results in README.md with plain Python (no dependencies).

1. Every set in solutions.json lies in the torus (Z/kZ)^2, has 2k+2 points,
   and meets each of the 4k lines (rows, columns, diagonals x-y=c,
   antidiagonals x+y=c) in at least two points.
2. The congruence used in Theorem 1: 4*S(k) = 2k/3 (mod k) for 3 | k,
   where S(k) = 0^2 + 1^2 + ... + (k-1)^2.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def line_counts(A, k):
    counts = {}
    for x, y in A:
        for key in (("row", x), ("col", y), ("diag", (x - y) % k), ("anti", (x + y) % k)):
            counts[key] = counts.get(key, 0) + 1
    return [counts.get((d, c), 0) for d in ("row", "col", "diag", "anti") for c in range(k)]


def main():
    with open(os.path.join(HERE, "solutions.json")) as f:
        sols = {int(k): [tuple(p) for p in v] for k, v in json.load(f).items()}
    for k in sorted(sols):
        A = sols[k]
        assert k % 3 == 0
        assert len(set(A)) == len(A) == 2 * k + 2, k
        assert all(0 <= x < k and 0 <= y < k for x, y in A), k
        c = line_counts(A, k)
        assert len(c) == 4 * k and min(c) >= 2, k
        print(f"k={k:2d}: |A| = {len(A)} = 2k+2, every one of the {4 * k} lines meets A at least twice")
    for k in range(3, 3001, 3):
        S = sum(c * c for c in range(k))
        assert (4 * S) % k == 2 * k // 3
    print("4*S(k) = 2k/3 (mod k) for every k = 3, 6, ..., 3000")
    print("all checks passed")


if __name__ == "__main__":
    main()
