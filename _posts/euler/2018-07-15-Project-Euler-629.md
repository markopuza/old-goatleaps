---
layout: post
title:  "Project Euler 629"
date:   2018-07-15\ 01:00:58 +0000
category-string: "Maths"
categories: euler maths
icon: euler629
---

{% include euler_declaration.md %}


### Scatterstone Nim

The problem tasks us with finding the number of winning positions in a certain variation of >>[Nim](https://en.wikipedia.org/wiki/Nim)<< defined by parameters $$n, k$$. We will, in the beginning, focus on one particular given pair $$n, k$$. To reiterate, the game goes like this:

- Two players start the game with some number of piles of $$n$$ stones in total.
- They take turns, where they pick one pile and split it into $$p\ (2 \leq p \leq k)$$ nonzero piles.
- Whoever doesn't have any valid move anymore, loses.

This being a combinatorial impartial game, the >>[Sprague-Grundy theorem](https://en.wikipedia.org/wiki/Sprague–Grundy_theorem)<< guarantees that we will be able to analyse it with >>[Grundy numbers (nimbers)](https://en.wikipedia.org/wiki/Nimber)<<. Consider the set $$T$$ of (sorted) tuples $$t = (t_1, t_2, \dots, t_k)$$ with $$\sum_{i=1}^k t_i = n$$; these will represent all possible positions in our game ($$t_i$$ is the size of $$i$$-th pile).
Each position $$t$$ will be associated with its Grundy number, which is standardly defined recursively as:

$$\mathcal G(t) = \begin{cases}
0 & t = (1, 1, \dots, 1) \\
\text{mex}_{t' \text{ reachable from } t \text{ via valid move }}\mathcal G(t') & \text{ otherwise}
\end{cases} \ \ \ \ \ \ \ \ \ \ \ (1)$$

The $$\text{mex}$$ in the above expression stands for the minimal excludant: $$\text{mex}\ S := \min \{i \not\in S\ \mid\ i = 0, 1, 2, \dots\}$$. The standard combinatorial game theory tells us that position $$t$$ will be losing if and only if $$\mathcal G(t) = 0$$, and moreover, we can understand playing the position $$t$$ as playing the games in positions $$(t_1), (t_1), \dots, (t_k)$$ simultaneously. The nimber addidion gives us the relation ($$\oplus$$ denotes the logical *xor*):

$$\mathcal G(t) = \bigoplus_{t_i \in t} \mathcal G((t_i))$$

The calculation of Grundy numbers using $$(1)$$ is quite expensive, but the above tells us that we may find any $$\mathcal G(t)$$ readily just by precalculating all $$\mathcal G((i))$$ for $$i = 1, \dots, n$$. For the precalculation of these singleton positions, we shall use $$(1)$$. But before dwelling unnecessarily into brute force, there are helpful simplifications worth noting:

**Theorem:** If $$k = 2$$, then $$\mathcal G((i)) = (i + 1) \text{ mod } 2$$.

*Proof*. Comes from the fact that we can split an even pile only into two piles of equal parity, and that we can split an odd pile only into two piles of distinct parity.

**Theorem:** If $$k \ge 4$$, then $$\mathcal G((i)) = i - 1$$.

*Proof*. The claim holds for $$i = 1$$, since $$\mathcal G(1) = 0$$. We will now show by induction that if we have a pile of size $$i$$, positions with Grundy numbers $$j = 0, 1, \dots, i - 2$$ are reachable. In particular, we may perform splits (for any valid $$r \ge 1$$):

$$(i) \rightarrow \begin{cases}
(i-1, 1) & \text{ giving Grundy number } \mathcal G((i - 1)) \oplus \mathcal G((1)) &= i - 2\\
(i-2r, r, r) & \text{ giving Grundy number } \mathcal G((i - 2r)) \oplus \mathcal G((r))  \oplus \mathcal G((r)) &= i - 2r - 1\\
(i-2r-1, r, r, 1) & \text{ giving Grundy number } \mathcal G((i - 2r - 1)) \oplus \mathcal G((r))  \oplus \mathcal G((r))  \oplus \mathcal G((1)) &= i - 2r - 2
\end{cases}$$

Thus the only case for $$k$$ where we actually need to compute the Grundy numbers is $$k = 3$$. In that case, letting $$P_k(n)$$ denote the set of integer partitions of $$n$$ of cardinality $$k$$, we use:

$$\mathcal G((n)) = \text{mex}_{t \in P_2(n) \cup P_3(n)} \left( \bigoplus_{i=1}^{|t|} \mathcal G((t_i)) \right)$$

{% highlight python %}
def P(n, k, l=1):
    if k < 1:
        raise StopIteration
    if k == 1:
        if n >= l:
            yield (n,)
        raise StopIteration
    for i in range(l,n+1):
        for result in P(n-i,k-1,i):
            # <REMOVED>

grundy3 = [0, 0]
for n in range(2, maxn):
    grundy3.append(mex([xor([grundy3[i] for i in t]) for t in P(n, 3)] + [xor([grundy3[i] for i in t]) # <REMOVED>

def grundy(n, k):
    if k == 2:
        return 0 if n&1 else 1
    if k == 3:
        return grundy3[n]
    else:
        return # <REMOVED>
{% endhighlight %}

Once we have computed all Grundy numbers, it will be quite easy to write a recursive function to count the number $$f(n, k)$$ of winning positions; these are just the ones with Grundy number $$> 0$$. Specifically, we are looking for the number of integer partitions of $$n$$ such that the *xor* sum of the Grundy numbers of components is nonzero.

{% highlight python %}
@memoize
def F(n, k, M, xor):
    if n == 0:
        return int(xor != 0)
    res = 0
    for i in range(1, min(M, n) + 1):
        res += # <REMOVED>
        res %= MOD
    return res

@memoize
def f(n, k):
    return F(n, k, n, 0)
{% endhighlight %}


{% highlight python %}
def g(n):
    res = 0
    for k in range(2, n+1):
        res += f(n, min(k, 4))
        res %= MOD
    return res
{% endhighlight %}

This piece of Python code returns the answer in about 9 seconds when run using PyPy.
