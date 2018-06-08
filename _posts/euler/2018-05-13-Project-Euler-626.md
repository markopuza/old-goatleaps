---
layout: post
title:  "Project Euler 626"
date:   2018-05-13\ 01:00:59 +0000
category-string: "Maths"
categories: euler maths
icon: euler626
---

{% include euler_declaration.md %}

### Counting Binary Matrices

This amazingly set problem can provide a good learning opportunity. It tasks us with finding the number of $$n \times n$$ binary matrices up to the equivalence where we proclaim two matrices equivalent if we can turn one into the other using some sequence of row/column swaps and row/column binary flips.

The core of the solution is the >>[Burnside's lemma](https://en.wikipedia.org/wiki/Burnside%27s_lemma)<<; a group theoretic theorem used for example to find the number of states in which the Rubik's cube can be in, up to the symmetries of the cube. It goes like this:

> Let $$G$$ be a finite group acting on a set $$X$$. For each $$g \in G$$ let $$fix(g) := \{x \in X\ \mid\ g \cdot x = x \}$$ be the set of elements that $$g$$ fixes. Then:
>
 $$\mid X / G\mid = \frac 1 {\mid G\mid} \sum_{g \in G} \mid fix(g)\mid$$

Let $$X$$ be the set of all $$n \times n$$ binary matrices and $$G$$ be the group of permissible operations on matrices that we are allowed to do (with the implicit group structure). That is:

$$G = (S_n \times T)^2$$

where $$S_n$$ is the $$n$$-th symmetric group (the group of all permutation of $$n$$ elements) and $$T$$ is the set $$2^{\{1, 2, \dots, n\}}$$ of all subsets of $${\{1, 2, \dots, n\}}$$. An element of $$G$$ looks like $$(\sigma \times m_1) \times (\rho \times m_2)$$ and signifies the following: flip all rows with indices in the set $$m_1$$ and permute the rows according to $$\sigma$$; flip all columns with indices in $$m_2$$ and permute the columns according to $$\rho$$.

We need to find $$\mid X / G\mid$$, and by the Burnside's lemma this is equal to $$\frac 1 {\mid G\mid} \sum_{g \in G} \mid fix(g)\mid$$. There are now two quantities that we need to compute. $$\mid G\mid$$, which is easy:

$$\mid G\mid = (n!2^n)^2$$

and $$\sum_{g \in G} \mid fix(g)\mid$$, which is harder. The key observation is that we can afford to be concerned only about the cycle types of the permutations; for any $$(\sigma \times m_1) \times (\rho \times m_2) \in G$$ and $$(\sigma' \times m_1') \times (\rho' \times m_2')$$ with $$\sigma, \sigma'$$ and $$\rho, \rho'$$ of the same cycle type will fix the same number of matrices.

Let $$\#(\mathbf c)$$ denote the number of permutations of cycle type $$\mathbf c$$, where under the cycle type $$\mathbf c$$ we will understand $$\mathbf c = (c_1, c_2, \dots, c_k)$$ with $$\sum_{i=1}^k c_i = n$$; all $$c_i \ge 1$$; $$c_i > c_{i+1}$$ for all $$i = 1, \dots, k-1$$ (that is, $$\mathbf c$$ is the sorted array of lengths of cycles present in a permutation). For example, the permutation $$(1 2 3)(5 6)$$ of $$6$$ elements has the cycle type $$\mathbf c = (3, 2, 1)$$.

$$\#$$ can be, after a simple combinatorial contemplation, computed as follows:

$$\#(\mathbf c) = \frac{1}{\prod_l (\text{number of cycles of length }l \text{ in }\mathbf c)!} \sum_{i = 1}^{\mid \mathbf c\mid} {\sum_{j = i}^{\mid \mathbf c\mid} \choose c_i}(c_i - 1)!$$

The denominator accounts for the order of two cycles of same length not having any importance. For each cycle in the cycle type, we consecutively choose $$c_i$$ of the remaining elements, which can give rise to distinct $$(c_i - 1)!$$ cycles. Then, for the main sum:


$$\begin{align*}
\sum_{g \in G}\mid fix(g) \mid &= \sum_{\sigma \in S_n} \sum_{\rho \in S_n} \sum_{m_1 \in T} \sum_{m_2 \in T} \mid fix((\sigma \times m_1) \times (\rho \times m_2)) \mid\\
&= \sum_{\text{cycle type } \mathbf c} \sum_{\text{cycle type } \mathbf k} \#(\mathbf c) \#(\mathbf k) \sum_{m_1 \in T} \sum_{m_2 \in T} \mid fix(\mathbf c, \mathbf k, m_1, m_2) \mid
\end{align*}$$

where as a small abuse of notation we write $$\mid fix(\mathbf c, \mathbf k, m_1, m_2) \mid\ :=\ \mid fix((\sigma \times m_1) \times (\rho \times m_2)) \mid$$ with $$\sigma$$ being some permutation of cycle type $$\mathbf c$$ and $$\rho$$ some permutation of cycle type $$\mathbf k$$.

Ignoring the flips for the time being, every pair of cycle types $$\mathbf c, \mathbf k$$ divides the matrix into $$\mid \mathbf c \mid \cdot \mid \mathbf k \mid$$ "subarrays", of sizes $$c_i \times k_j$$. In order for any matrix to be fixed by the permutations of these cycle types, every subarray $$c_i \times k_j$$ is further divided into $$gcd(c_i, k_j)$$ parts (the distinct orbits in the joint 2-dimensional permutation $$c_i \times k_j$$), each of which must contain the same number everywhere. For each of these parts, we have two options (either we set the bit at every position within the part to $$0$$ or $$1$$), so any pair of cycle types $$\mathbf c, \mathbf k$$ fixes precisely $$\prod_{c_i \in \mathbf c} \prod_{k_j \in \mathbf k} 2^{gcd(c_i, k_j)}$$ matrices. The above sum becomes:

$$\begin{align*}
\sum_{g \in G}\mid fix(g) \mid &= \sum_{\text{cycle type } \mathbf c} \sum_{\text{cycle type } \mathbf k} \#(\mathbf c) \#(\mathbf k) \left( flips(\mathbf c, \mathbf k) \prod_{c_i \in \mathbf c} \prod_{k_j \in \mathbf k} 2^{gcd(c_i, k_j)}\right)
\end{align*}$$

with $$flips(\mathbf c, \mathbf k)$$ being the number of permissible sets $$m_1, m_2 \subseteq T$$ of flips of rows/columns, such that any two permutations of cycle types $$\mathbf c, \mathbf k$$ that fix a matrix, will also fix it after we flip rows indexed by $$m_1$$ and columns indexed by $$m_2$$. We now turn into finding $$flips(\mathbf c, \mathbf k)$$.

Let $$f_i$$ denote the number of indices of rows in the cycle $$c_i$$ that are flipped, and similarly, $$g_j$$ the number of indices of columns in the cycle $$k_j$$ that are flipped. The key realisation is that _any_ flip sets $$m_1, m_2$$ are going to fix the matrix already fixed by permutations, as long as the following condition holds for all $$c_i, k_j$$. The condition can be interpreted as: "When we successively apply $$(\mathbf c, \mathbf k)$$ on any element of the matrix, when it comes back to its original position, it must have undergone an even number of flips."

$$f_i \frac{lcm(c_i, k_j)}{c_i} + g_j \frac{lcm(c_i, k_j)}{k_j} \equiv 0 \ (\text{mod } 2)$$

In the binary world of ours, we can now consider the variables $$f_i, g_j$$ to be the unknowns and the above conditions specifying a system of linear equations. Let $$M$$ be the $$(\mid \mathbf c \mid + \mid \mathbf k \mid) \times (\mid \mathbf c \mid \cdot \mid \mathbf k \mid)$$ matrix representing this system of linear equations. That is, the $$row$$-th condition specifies the row in the matrix $$M$$:

$$M_{row, col} = \begin{cases} \frac{lcm(c_i, k_j)} {c_i} & \text{if } col = i \\ \frac{lcm(c_i, k_j)} {k_j} & \text{if } col = \mid \mathbf c\mid + j \\ 0 & \text{otherwise} \end{cases}$$

Then simply $$flips(\mathbf c, \mathbf k) = 2^{2n - rank(M)}$$ (the exponent here is the number of free variables that we are left with).

All of the cycle types for a given $$n$$ can be precomputed quite easily.

{% highlight python %}
cycle_types = []
def construct(prefix, last, sofar):
    if sofar == n:
        cycle_types.append(tuple(prefix))
    else:
        for i in range(1, min(last+1, n+1)):
            if sofar + i > n:
                break
            # <REMOVED>
construct([], n, 0)
{% endhighlight %}

The $$\#$$ function:

{% highlight python %}
def ncycle_types(c):
    res, left, counter = 1, n, defaultdict(int)
    for ci in c:
        res *= choose[left][ci] * fact[ci - 1]
        left -= ci
        counter[ci] += 1
    for v in counter.values():
        # <REMOVED>
    return res
{% endhighlight %}

Finding the rank of matrix $$M$$ (which I do not include here) and thus computing $$flips$$ can be done in $$\mathcal O(\mid \mathbf c \mid \cdot \mid \mathbf k \mid)$$ time, providing a solution which gives the full answer to the problem in about a second, on PyPy3.
