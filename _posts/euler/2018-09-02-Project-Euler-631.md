---
layout: post
title:  "Project Euler 631"
date:   2018-09-02\ 01:00:58 +0000
category-string: "Maths"
categories: euler maths
icon: euler631
---

{% include euler_declaration.md %}


### Constrained permutations

This problem, being one of the harder recent ones, tasks us with counting a certain type of permutations (we will call these *valid*). The constraint on permutations is that they should not contain any sub-permutation of type $$(1243)$$ and contain at most $$m$$ sub-permutations of type $$(21)$$; where the containment is defined in the problem. In line with how the containment is defined, we will consider the permutations to be, informally, finite sequences of integers. We are supposed to count valid permutations for $$m=40$$ and which are of length at most $$10^{18}$$. The single key realization that paves the path to a successful solution is that there *are not* that many valid permutations, and that they can be counted in a brute-force manner. This observation can be put into solid ground with the following claim:

**Claim**: Any valid permutation fixes all $$k$$ where $$k \ge m + 3$$.

*Proof*. Let $$\sigma$$ be a valid permutation and $$x$$ be the *largest* integer to the right of which one can find a smaller integer in $$\sigma$$. Then, we can find in $$\sigma$$ a subsequence:

$$l_1, l_2, \dots, l_a, x, r_1, r_2, \dots, r_b$$

where $$a \ge 0$$, $$b \ge 1$$, $$a + b + 1 = x$$ and all $$l_i, r_j$$ are smaller than $$x$$. Since $$\sigma$$ is a valid permutation and thus contains no sub-permutations of type $$(1243)$$, the integers $$l_1, l_2, \dots, l_a$$ must be in decreasing order. This means that $$\sigma$$ contains at the very least these sub-permutations of type $$(21)$$:
- All $$(x, r_j)$$. There is $$b$$ of these.
- Any pair $$(l_i, l_j), i < j$$. There is $$a\frac{a-1}{2}$$ of these.
But again, since $$\sigma$$ is valid, this gives us:

$$
\begin{align*}
b + \frac{a(a-1)}{2} = x - a - 1 + \frac{a(a-1)}{2} &\leq m\\
x &\leq m + 1 - \frac{a(a-3)}{2} \leq m + 2
\end{align*}$$

Coming back to how $$x$$ was defined, this means that for all $$k \ge m+3$$, there are no smaller integers to the right of $$k$$. From this, all $$k \ge m + 3$$ must be fixed. $$\square$$


How does this help us to brute-force the solution? Well, there is going to be only a certain number of minimal valid prefixes $$p$$ consisting of $$1, 2, \dots, \mid p \mid$$ (where the word *minimal* indicates that the prefix *does not* fix $$\mid p \mid$$, and that all integers greater than $$\mid p \mid$$ will be necessarily fixed in a permutation with $$p$$ as prefix). Each such prefix will then contribute to the total result with $$n - \mid p \mid + 1$$ valid permutations:

$$\begin{align*}
&p_1, p_2, \dots, p_{\mid p \mid}\\
&p_1, p_2, \dots, p_{\mid p \mid}, \mid p\mid + 1\\
&p_1, p_2, \dots, p_{\mid p \mid}, \mid p\mid + 1, \mid p\mid + 2\\
&\ \ \ \vdots
\end{align*}$$

To construct all of the valid minimal prefixes, we can try all of the possible placements of the successive integers $$1, 2, 3, \dots $$, recording any present sub-permutations $$(21)$$ to avoid having more than $$m$$ of them, recording occurrences of $$(12)$$ to avoid any containment of sub-permutation $$(1243)$$, and pruning wherever possible.

The following piece of Python code gives the answer in about 17 seconds, when run with PyPy.
{% highlight python %}
def solve(n=10**18, m=40, MOD=1000000007):
    result = # <REMOVED>
    def explore(lst=[0]*min(n, m+4), num=1, rightmost=-1, remain21=m, first12=n+1):
        nonlocal result
        empty_thus, min_thus = 0, n+1
        for i in range(len(lst)):
            if lst[i]:
                min_thus = min(min_thus, lst[i])
            else:
                lst[i] = num
                newfirst12 = # <REMOVED>
                if (newfirst12 <= i and empty_thus == 0) or (num == len(lst)):
                    result = (result + n - rightmost) % MOD
                elif remain21 - empty_thus >= 0:
                    explore(# <REMOVED>
                lst[i] = 0

                empty_thus += 1
                if i > first12:
                    break
    explore()
    return result
{% endhighlight %}
