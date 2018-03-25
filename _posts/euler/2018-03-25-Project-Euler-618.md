---
layout: post
title:  "Project Euler 618"
date:   2018-03-25 01:36:59 +0000
category-string: "Maths"
categories: euler maths
icon: euler618
---

# WARNING: The text below provides a guidance for a Project Euler problem.

- If you pride yourself in tackling problems entirely on your own, you are encouraged to exit this post right now.

- If you are simply looking for a hint for the problem, please visit the >>[Project Euler's official forum](https://projecteuler.chat/index.php)<<. You may find some hints here, but if you don't want your problem spoiled, scroll cautiously.

- If you are looking for a readily available copy/paste answer, you will not find it here. __All of the code snippets in the post have been stripped of some crucial lines__ (these are clearly marked). It is my aim that anyone able to replicate the answer based on such snippets will have to understand the solution conceptually. At that point, by virtue of learning something new, I believe he deserves it anyway.

\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
\\
$$$$

### Numbers with a given prime factor sum

Let $$f(n) := \sum_{i} \alpha_i p_i$$ be the function giving the sum of all prime factors of $$n$$ (with prime decomposition $$n = \prod_i p_i^{\alpha_i}$$), with multiplicity. The problem revolves about computing the sum of all possible $$n$$'s with a fixed value $$f(n) = k$$:

$$ S(k) := \sum_{f(n) = k} n $$

A reasonable approach to try for this sort of problem is dynamic programming, which turns out to give a fast enough solution. In order to compute $$S(k)$$, we will vary over possible $$k$$'s and the maximal prime in the factorisation of $$n$$. Define $$v(k, j)$$ to be the sum of all possible $$n$$'s such that $$f(n) = k$$ and __only the first $$j$$ primes__ appear in the prime factorization of $$n$$. Clearly, $$S(k) = v(k, J)$$, where $$J$$ is the index of the first prime greater than $$k$$ (If a greater prime than $$k$$ appeared in the factorization of $$n$$, we couldn't have $$f(n) = k$$). Formally:


$$v(k, j) = \sum_{\substack{f(n) = k \\ n = p_1^{\alpha_1}p_2^{\alpha_2} \cdots p_j^{\alpha_j}}} n \ \ \ \ \ \text{ where all } \alpha_1, \alpha_2, \dots, \alpha_j \ge 0$$

This can be split into two sums according to whether $$\alpha_j = 0$$ or $$\alpha_j > 0$$, obtaining a recursive relationship (Or more easily, one can just persuade himself that the relationship holds):

$$ \begin{align*}
 v(k, j) &= \sum_{\substack{f(n) = k \\ n = p_1^{\alpha_1}p_2^{\alpha_2} \cdots p_j^{\alpha_j}}} n \\
  &= \left(\sum_{\substack{f(n) = k \\ n = p_1^{\alpha_1}p_2^{\alpha_2} \cdots p_{j-1}^{\alpha_{j-1}} p_j^0}} n\right)
+ \left(\sum_{\substack{f(p_jn) = k \\ n = p_1^{\alpha_1}p_2^{\alpha_2} \cdots p_{j}^{\alpha_{j} - 1}}} p_j n \right)\\
  &= \left(\sum_{\substack{f(n) = k \\ n = p_1^{\alpha_1}p_2^{\alpha_2} \cdots p_{j-1}^{\alpha_{j-1}}}} n \right)
  + p_j \left(\sum_{\substack{f(n) = k - p_j \\ n = p_1^{\alpha_1}p_2^{\alpha_2} \cdots p_{j}^{\alpha_{j} - 1}}} n \right)\\
    v(k, j) &= v(k, j-1) + p_j v(k - p_j, j)
\end{align*} $$

The biggest $$k$$ for which we will be computing $$S(k)$$ is from the problem statement the 24th Fibonacci number, that is 75025. The fact that $$v(k, j)$$ only depends on $$v(k, j-1)$$ and $$p_j v(k - p_j, j)$$ will allow us to compute the values $$v$$ iteratively in columns $$v(l, j), l = 0, 1, \dots, k$$ _without storing more than the previous column_. All in all, with precomputing the Fibonacci numbers and sufficiently many primes, the whole solution can be compressed just to a few lines:

{% highlight python %}
v = # <REMOVED>
for p in primes:
    for k in range(p, fib[-1] + 1):
        v[k] = # <REMOVED>
print(sum(v[fib[i]] for i in range(2, 25)) % MOD)
{% endhighlight %}

The runtime of this piece of code on my computer with PyPy3 is about 30 seconds.

# Generating functions approach

Let's now venture into a more mathematical approach using generating functions. We are looking for a generating function of the sequence $$S(k)$$, that is, a (formal) representation:

$$ \begin{align*}
G(x) &= \sum_{k = 0} ^ \infty S(k)\ x^k \\
    &= \prod_{p \text{ prime}} \left(1 + px^p + p^2x^{2p} + p^3x^{3p} + \dots \right) = \prod_{p \text{ prime}} \left(\sum_{i = 0}^\infty (p x^p)^i  \right)
\end{align*}$$

To see that the coefficient of $$x^k$$ in the expanded version of the product is indeed $$S(k)$$, one can just see that once the product is expanded, any terms $$n x^k$$ are precisely those where $$n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_m^{\alpha_m}$$ such that $$f(n) = \sum_{i = 1}^m \alpha_i p_i = k$$. Summing them up, the coefficient of $$x^k$$ is precisely $$S(k)$$. Now, using the fact that each $$\sum_{i = 0}^\infty (p x^p)^i$$ is a formal geometric series, we can sum it up to obtain $$\frac 1 {1 - p x^p}$$. Thus:

$$
G(x) = \prod_{p \text{ prime}} \left(\frac 1 {1 - p x^p} \right) = \frac 1 {\prod_{p \text{ prime}} (1 - p x^p)}
$$

This can be implemented in Julia plainly as it is, without any optimisations, which returns the result in about 6 minutes.

{% highlight julia %}
fib(n) = n < 2 ? 1 : fib(n - 1) + fib(n - 2)
R, x = PowerSeriesRing(ResidueRing(ZZ, 10^9), fib(24), "x")
@time G = inv(# <REMOVED>
println(sum(coeff(G, fib(i)) for i=2:24))
{% endhighlight %}
