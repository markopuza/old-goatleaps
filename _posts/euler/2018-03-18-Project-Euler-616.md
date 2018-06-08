---
layout: post
title:  "Project Euler 616"
date:   2018-03-18 01:36:59 +0000
category-string: "Maths"
categories: euler maths
icon: euler616
---

{% include euler_declaration.md %}

### Creative numbers

The problem asks us to sum up so-called _creative_ numbers.
Number $$n$$ is __creative__ if, starting from list $$L = \{n\}$$, any integer greater than one is reachable via sequence of steps of two types:
- Remove $$a, b$$ from $$L$$ and substitute them by $$a^b$$. (For example $$\{2,3\} \rightarrow \{9\} $$)
- Remove any integer of the form $$a^b; a, b > 1$$ from the list and substitute it by $$a, b$$. (For example $$\{16\} \rightarrow \{2, 4\}$$)

We need to get a better grasp on which numbers are creative. Well, for starters, any number $$n$$ that is not on the form $$a^b; a, b > 1$$ cannot be creative, as we will get stuck in the beginning. So we consider only numbers of this form. What if both $$a$$ and $$b$$ are prime? In such case the only course of action available to us is:

$$\{a^b\} \rightarrow \{a, b\} \rightarrow \begin{cases} \{a^b\}\\\{b^a\} \end{cases}$$

  and we are stuck again. What if the exponent $$b$$ is composite? Then we find ourselves able to reach:

$$\{a^{bc} \} = \{ (a^b)^c\} \rightarrow \{a^b, c\} \rightarrow \{a, b, c\};\ a,b,c > 1$$

What if the number we are taking power of is composite? Then we can reach:

 $$\{(ab)^c\} \rightarrow \{ ab, c\} \rightarrow \{c^{ab}\} \rightarrow \{a, b, c\};\ a,b,c > 1$$

After these simple observations we arrive at the claim that is the backbone of the whole problem.


__Claim__. Any number $$m > 1$$ is reachable from $$\{a, b, c\};\ a,b,c > 1$$, unless $$a = b = c = 2$$.\\
_Proof_. In case $$a = b = c = 2$$, we are stuck as the only reachable lists are $$\{2,2,2\}, \{2, 4\}, \{16\}$$. So let from now on $$c \geq 3$$. We may obtain:

$$ \{a, b, c\} \rightarrow \{a^{b^c}\} = \{(a^{b^{c-1}})^b\} \rightarrow \{a^{b^{c-1}}, b\} \rightarrow \{a, b, b, c-1\}$$

By the following chain of steps we can grow our number in magnitude:

$$ \{a, b, b, c-1\} \rightarrow \{b^{b^{a^{c-1}}}\} \rightarrow \{b^{b^{a^{c-1} -1}}, b\} \rightarrow \{b^{b^{b^{a^{c-1} -1}}}\} \rightarrow \{b^{b^{b^{a^{c-1} -1} -1}}, b\} \rightarrow  \{b^{b^{b^{b^{a^{c-1} -1} -1}}}\} \rightarrow \cdots $$

Eventually, we can reach, for any $$m > 2$$, some number $$b^{b^x}$$ where $$x > m + 1$$. Then we simply do:

$$ \{b^{b^x}\} \rightarrow \{b^{b^m}, b^{x - m}\} \rightarrow \{b, b, m, b^{x - m}\} $$

whereupon we have reached $$m$$. $$\square$$

Finally, the problem tasks us with finding $$\sum_{i = 1}^{k} i \cdot \mathbb 1_{i \text{ is creative}}$$ (Where $$\mathbb 1_{i \text{ is creative}}$$ is $$1$$ if $$i$$ is creative and $$0$$ otherwise.) which is by the previous discussion equal to (Any $$a^b$$ with at least one of $$a, b$$ composite can be written as $$b^p$$ where $$b$$ is composite and $$p$$ prime.):

$$\sum_{\substack{b \text{ composite}\\ p \text{ prime}} \\b^p \neq 16 \\ b^p \leq k} b^p$$

A straightforward implementation seems to be fast enough with PyPy3 runtime just below one second.

{% highlight python %}
def solve(lim):
    sqrtlim = round(lim ** 0.5) + 1
    # primes, composites
    P, C = primes(sqrtlim), [False, False] + [True for _ in range(sqrtlim)]
    for p in P:
        C[p] = False
    result = set()
    # <REMOVED>
        if C[b]:
            cand, next_prime = b * b, 1
            while cand <= lim:
                result.add(cand)
                # <REMOVED>
                next_prime += 1
    return sum(result)
{% endhighlight %}
