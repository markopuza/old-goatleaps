---
layout: post
title:  "Project Euler 623"
date:   2018-03-31 01:00:59 +0000
category-string: "Maths"
categories: euler maths
icon: euler623
---

{% include euler_declaration.md %}


### Lambda Count

The problem tasks us with counting the function $$\Lambda(n)$$; the number of lambda-terms that can be written with at most $$n$$ symbols, up to $$\alpha$$-equivalence. Even though the problem statement involving the $$\alpha$$-equivalence may look appalling at the first glance, it actually brings major simplifications.

The first thing to realize is that any $$\alpha$$-equivalence class (which we are trying to count) has a representative lambda expression where all of the variables in abstractions are _distinct_ (Visually, any $$\lambda$$ symbol appearing in the expression is followed by a different variable). This follows straight from what $$\alpha$$-equivalence does: allowing us to rename any free variables.

The fact that any expression is only of three types (pure variable, application or abstraction) gives us a nudge that the problem could be solvable by dynamic programming, and it is indeed the case. We will consider the function $$\lambda(n, i)$$ giving the _number of lambda-terms (up to $$\alpha$$-equivalence) of length $$n$$, such that they may contain $$i$$ further distinct variables from any previous abstractions_. Then, quite clearly:

$$ \Lambda(n) = \sum_{m = 0}^n \lambda(m, 0)$$

and what remains is to find a suitable recursive relation for $$\lambda$$. Distinguishing by the cases, we find:

$$ \lambda(n, i) = \begin{cases}
  0 & \text{if } n \leq 0 \\
  i & \text{if } n = 1 \text{ since we choose out of } i \text{ variables.}\\
  \lambda(n - 5, i + 1) + \sum_{\substack{k + l = n - 2}} \lambda(k, i) \cdot \lambda(l, i)  & \text{if } n > 1
\end{cases}
$$

where the break-down in the last case comes from our expression being either an application or abstraction. If it is abstraction, it must be of the form $$(\lambda x. \cdots)$$, thus we have used 5 symbols, increasing the number of abstracted variables by $$1$$. If it is an application, it must be of the form $$(\cdots\ \cdots)$$, where we have used 2 symbols (and thus the lengths of the two groups must add up to $$n-2$$) and didn't change the number of previously abstracted variables. \\
To speed up our future implementation and to make fewer recursive calls, we can also make use of the symmetry in the sum $$\sum_{\substack{k + l = n - 2}} \lambda(k, i) \cdot \lambda(l, i)$$, rewriting it as:

$$\sum_{\substack{k + l = n - 2}} \lambda(k, i) \cdot \lambda(l, i) = \sum_{\substack{k + l = n - 2\\ k < l}} 2 \cdot \lambda(k, i) \cdot \lambda(l, i) + \sum_{\substack{k + l = n - 2\\k = l}} \lambda(k, i) \cdot \lambda(l, i) $$

This cuts the number of recursive calls roughly in half. We now estimate the total number of operations to calculatte $$\Lambda(n)$$ using this recurrence. There is at most $$n \cdot \frac n 5$$ values $$\lambda$$ that we will need to calculate ($$n$$ options for the number of symbols, $$\frac n 5$$ options for the number of abstracted variables, as each abstraction takes 5 symbols). For each of these, we will make (at most) $$\frac n 2$$ recursive calls, with the average about $$\frac n 4$$ calls. Overall, for $$n = 2000$$ given by the problem, we thus expect an upper bound of around $$\frac {n^3} {20} = 400000000$$ calls to take place. This turns out to be fast enough indeed.

The following implementation with memoization runs in about 2 seconds using PyPy3. The number of times that $$\lambda$$ was called is 267268795, consistent with the prediction.

{% highlight python %}
MOD = 10**9 + 7

def LAMBDA(n):
    memo = [-1] * (n + 1)**2
    def lambda(symbols, abstracted):
        if symbols <= 1:
            # <REMOVED>
        hash = symbols * n + abstracted
        if memo[hash] >= 0:
            return memo[hash]

        result = lambda(symbols - 5, abstracted + 1)
        for i # <REMOVED>
            if # <REMOVED>
                # <REMOVED>
            elif i == symbols - 2 - i:
                result = (result + lambda(i, abstracted) * lambda(symbols -2 -i, abstracted)) % MOD
            else:
                break
        memo[hash] = result
        return result
    return sum(lambda(i, 0) for i in range(6, n + 1)) % MOD
{% endhighlight %}

The same approach can be implemented _very succintly_ in the Julia programming language, which gives the answer after approximately 4 minutes.

{% highlight julia %}
using Memoize, Nemo
R = ResidueRing(ZZ, 10^9)
@memoize λ(s, a) = (s <= 3 ? # <REMOVED>
Λ(n) = sum(λ(m, 0) for m=0:n)
{% endhighlight %}
