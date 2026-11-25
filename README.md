# Conjectures 5.1 and 5.4 of Ku's "Monochromatic $k$ in a row"

K.-H. Ku, *Monochromatic $k$ in a row*, [arXiv:2606.12880](https://arxiv.org/abs/2606.12880) (2026), studies saturated configurations of the $k$-in-a-row game. A *configuration* is a set of cells containing no near $k$-line: every $k$-line misses at least two of its cells. $D(k,B)$ is the largest density of a saturated configuration on the board $B$. Section 5 of the paper poses these conjectures for $k\in3\mathbb N$:

- **Conjecture 5.1.** $D(k,\mathbb Z^2)<1-\frac2k$.
- **Conjecture 5.3** (restatement of 5.1). No $A\subseteq(\mathbb Z/k\mathbb Z)^2$ meets every axis-parallel or diagonal line in exactly 2 points.
- **Conjecture 5.4.** No $A\subseteq(\mathbb Z/k\mathbb Z)^2$ with $|A|\le 2k+2$ meets every axis-parallel or diagonal line in at least 2 points.

On the torus $T_k=(\mathbb Z/k\mathbb Z)^2$ the lines are the $4k$ sets $\{x=c\}$, $\{y=c\}$, $\{x-y=c\}$, $\{x+y=c\}$, each of $k$ points. A configuration is exactly the complement of a set $A$ that meets every line at least twice, so $D(k,T_k)=1-\min|A|/k^2$.

## Results

**Theorem 1.** Let $3\mid k$. If $A\subseteq T_k$ meets every line in at least 2 points, then $|A|\ge 2k+2$.

**Corollary.** Conjectures 5.3 and 5.1 are true. For every $k\in3\mathbb N$,

$$D(k,T_k)\le 1-\frac2k-\frac2{k^2},\qquad D(k,\mathbb Z^2)\le 1-\frac2k-\frac1{2k^2-k}.$$

**Theorem 2.** For $k=6,9,12,\dots,33$ and $k=39$ there is a set $A\subseteq T_k$ with $|A|=2k+2$ meeting every line in at least 2 points. The sets are in [solutions.json](solutions.json).

**Corollary.** Conjecture 5.4 is false; the true threshold is $2k+1$ (Theorem 1), and it is sharp. For these $k$,

$$D(k,T_k)=1-\frac2k-\frac2{k^2},\qquad D(k,\mathbb Z^2)\ \ge\ 1-\frac2k-\frac2{k^2}\ >\ 1-\frac2{k-1},$$

which improves the lower bound of Ku's Theorem 1.2.

For $k=6$, the 14 points of $A$ (rows $x=0,\dots,5$, columns $y=0,\dots,5$):

```
# . # . . .
# # . . # .
. . . # # #
. # # . . .
# . . . . #
. . . # # .
```

$A=\{(0,0),(0,2),(1,0),(1,1),(1,4),(2,3),(2,4),(2,5),(3,1),(3,2),(4,0),(4,5),(5,3),(5,4)\}$.

## Proof of Theorem 1

The argument is the one Pólya used for toroidal queens. Write $S=\sum_{c=0}^{k-1}c^2$. For $k=3m$,

$$4S=2m(3m-1)(6m-1)=2m\bigl(1+3m(6m-3)\bigr)\equiv 2m\not\equiv 0 \pmod{3m}.$$

Suppose $|A|\le 2k+1$. The $k$ rows partition $T_k$ and each meets $A$ at least twice, so $|A|\ge 2k$. In each of the four directions the line counts are then either all equal to 2, or all equal to 2 except one line with 3. Let $r,c,d,e$ be the index of that line in the row, column, diagonal and antidiagonal direction. If a direction has no such line, its index is $0$, and the formulas below still hold, because the extra term is then $0$.

For a function $\varphi$ on $\mathbb Z/k\mathbb Z$, summing $\varphi$ of the row index over $A$ gives $2\sum_c\varphi(c)+\varphi(r)$, and likewise for the other directions. Using $2\sum_c c=k(k-1)\equiv0$, the linear sums give

$$\sum_A x\equiv r,\quad \sum_A y\equiv c,\quad \sum_A (x-y)\equiv d,\quad \sum_A (x+y)\equiv e \pmod k,$$

so $e\equiv r+c$ and $d\equiv r-c$. Squares are well defined modulo $k$, so

$$\sum_A x^2\equiv 2S+r^2,\quad \sum_A y^2\equiv 2S+c^2,\quad \sum_A (x-y)^2\equiv 2S+d^2,\quad \sum_A (x+y)^2\equiv 2S+e^2 .$$

Summing the identity $(x+y)^2+(x-y)^2=2x^2+2y^2$ over $A$ gives

$$4S+e^2+d^2\equiv 8S+2r^2+2c^2,\qquad\text{so}\qquad 4S\equiv (r+c)^2+(r-c)^2-2r^2-2c^2=0 \pmod k,$$

which contradicts $4S\equiv 2m$. Hence $|A|\ge 2k+2$. $\square$

## Proof of the corollaries

- **Conjecture 5.3.** A set meeting every line exactly twice has $2k$ points, which Theorem 1 excludes.
- **Bound on $D(k,T_k)$.** This is $D(k,T_k)=1-\min|A|/k^2$.
- **Conjecture 5.1.** By Theorem 1, $D(k,T_k)<1-\frac2k$. Ku's Theorem 3.8 states that $D(k,\mathbb Z^2)>1-\frac2k-\frac1{2k^2-k}$ implies $D(k,T_k)=1-\frac2k$. Its contrapositive gives the bound on $D(k,\mathbb Z^2)$, and in particular Conjecture 5.1.
- **Lower bound on $D(k,\mathbb Z^2)$.** This follows from $D(k,\mathbb Z^2)\ge D(k,T_k)$, which Ku proves by tiling, just before Corollary 3.9. The inequality $1-\frac2k-\frac2{k^2}>1-\frac2{k-1}$ is equivalent to $(k+1)(k-1)<k^2$.

## Remarks

- Conjecture 5.2, $D(k,T_k)<D(k,\mathbb Z^2)$ for $k\in3\mathbb N$, is not settled here. By the results above it amounts to $D(k,\mathbb Z^2)>1-\frac2k-\frac2{k^2}$, so it cannot be reached through the lower bound $1-\frac2{k-1}$.
- Whether $|A|=2k+2$ is attainable for every $k\in3\mathbb N$ with $k\ge6$ is open here; the sets in [solutions.json](solutions.json) were found by SAT search, most of them under the symmetries $(x,y)\mapsto(-x,-y)$ and $(x,y)\mapsto(y,x)$.
- For $k=3$ the minimum is $8$: two points of $T_3$ always lie on a common line, so a line misses at most one point of $A$ only if $|A|\ge 8$.

## Verification

```sh
python3 verify.py                     # no dependencies: checks every set and the congruence
pip install python-sat
python3 sat_search.py find 12         # finds a 26-point set for k = 12
python3 sat_search.py none 6 13       # UNSAT: Theorem 1 at k = 6, checked independently
```

## Author and license

Vishal Singh Baraiya. The code (`verify.py`, `sat_search.py`) is released under the MIT License, and the text and data under CC BY 4.0. See [LICENSE](LICENSE).
