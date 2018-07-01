---
layout: post
title:  "Project Euler 628"
date:   2018-06-30\ 01:00:58 +0000
category-string: "Maths"
categories: euler maths
icon: euler628
---

{% include euler_declaration.md %}


### Open chess positions

Yet another problem from the recent "counting" streak tasks us with computing the number $$f(n)$$ of configurations of $$n$$ pawns on an $$n \times n$$ board, such that the following conditions hold:
  - (1) No two pawns share a row or column.
  - (2) It is possible for a rook to get from the bottom-left corner to the top-right corner of the board.

How does a position that satisfies both of the above look like? It seems to be the easiest to work with the complement. We will characterise instead the positions where the pawns are positioned according to the first rule, but the rook has no way of getting from one corner to the other.

<div align="center">
<img src="/assets/image/euler628img.png" width="35%">
</div>

**Lemma**: Rook has no way between the bottom-left corner and top-right corner *if and only if* some of the board's $$2n - 1$$ "subdiagonals" (as represented by different colors in the picture above) is completely obstructed.

*Proof.* If any of the subdiagonals is obstructed, the way between the corners clearly doesn't exist. Suppose that none of the subdiagonals is completely obstructed. Consider the pawn $$C$$ that was placed somewhere in the first column. Without loss of generality, on our picture, this would be on the yellow subdiagonal. On the subdiagonal of this pawn (yellow), there is going to be a sequence of pawns going right-downward, running until the first free square (which exists by assumption). The key realization is then that *any square in the same row as $$C$$ is necessarily free and reachable with the rook from the bottom-left corner*. \\
With a similar logic, there must also be some pawn $$R$$ in the first row. If $$R = C$$, we have already found a way for rook to reach the other corner. Assume therefore that $$R \neq C$$. For this pawn, *any square in the same column as $$R$$ is necessarily free and reachable with the rook from the top-right corner*. But the column of $$R$$ and the row of $$C$$ must intersect, and thus the rook can safely move between the corners at his leisure.


Another handy observation we can make straight away is the fact that *at most 2 subdiagonals* of the board can be completely obstructed - one in the lower-left (triangular) region below the main diagonal, and one in the upper-right region above the main diagonal (For if there were two subdiagonals obstructed on either side, we would need to have more than 1 pawns in the same row/column). Let us get to counting now.

Let $$t(n)$$ be the total number of configurations of pawns that satisfy rule 1. Clearly, $$t(n) = n!$$ (When placing pawns row by row, the number of options after the $$i$$-th pawn was placed is $$i$$).\\
Let $$s(n, l, r)$$ be the total number of configurations of pawns that satisfy rule 1, where subdiagonal of length $$l$$ in the lower-left region below the main diagonal is completely obstructed, and subdiagonal of length $$r$$ in the upper-right region above the main diagonal is completely obstructed. In case no subdiagonal in either region is completely obstructed, we set $$l = 0$$ or $$r = 0$$ respectively. Then:

$$f(n) = t(n) - 1 - \sum_{r = 0}^{n-1} \sum_{l = 0}^{n-1}s(n, l, r) \mathbb I_{\text{not both }l = 0, r = 0} $$

where $$-1$$ comes from the case where the main diagonal itself is obstructed.

By the same combinatorial argument that we used to find $$t(n) = n!$$, we can fix any $$r > 0$$ and determine:

$$\sum_{l = 0}^{n-1} s(n, l, r) = (n - r)!$$

and symetrically for any $$l > 0$$:

$$\sum_{r = 0}^{n-1} s(n, l, r) = (n - l)!$$

For any $$l, r > 0 $$ we also have $$s(n, l, r) = \begin{cases}(n - r - l)! & \text{ if } r + l \leq n \\ 0 & \text{ otherwise} \end{cases}$$.

By carefully treating the indices, we can also rewrite the required double sum:

$$ \begin{align*} \sum_{r = 0}^{n-1}  \sum_{l = 0}^{n-1}s(n, l, r) \mathbb I_{\text{not both }l = 0, r = 0} &= \sum_{r = 1}^{n - 1} \left(\sum_{l = 0}^{n-1} s(n, l, r)\right) + \sum_{l = 1}^{n - 1} \left(\sum_{r = 0}^{n-1} s(n, l, r) \right) - \sum_{r = 1}^{n-1}  \sum_{l = 1}^{n-1}s(n, l, r) \\
 &= \sum_{r = 1}^{n-1} (n-r)! + \sum_{l = 1}^{n-1} (n - l)! - \sum_{r = 1}^{n-1}  \sum_{l = 1}^{n-r} (n - r - l)! \\
 &= \sum_{i = 1}^{n - 1} 2 i! + \sum_{i = 1}^{n - 1} i (n - 1 - i)!
\end{align*}$$

where in the last step, in the second sum, we have just counted how many times $$(n - 1 - i)!$$ appears in $$\sum_{r = 1}^{n-1}  \sum_{l = 1}^{n-r} (n - r - l)!$$. Altogether, we obtain a sum that can be computed in linear time:

$$ f(n) = n! - 1 - \sum_{i = 1}^{n-1} (2i! - i(n - 1 - i)!)$$

The following piece of Python code gives the answer in below 5 seconds, when run with PyPy:

{% highlight python %}
M, n, fact = 1008691207, 10**8, [1]
for i in range(1, n+1):
     #<REMOVED>
res = fact[-1] - 1
for i in range(1, n):
    res += #<REMOVED>
    res %= M
print(res)
{% endhighlight%}
