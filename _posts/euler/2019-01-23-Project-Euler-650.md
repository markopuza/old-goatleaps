---
layout: post
title:  "Project Euler 650"
date:   2019-01-23\ 01:00:58 +0000
category-string: "Maths"
categories: euler maths
icon: euler650
---

{% include euler_declaration.md %}

### Divisors of Binomial Product

The problem number 650 is less demanding conceptually and harder in terms of finding an efficient implementation. Denoting $$\sigma$$ the sum of divisors function,
we define a slightly nauseating chain of quantities:

$$\begin{align*}
B(n) &:= \prod_{k = 0}^n {n \choose k} = \prod_{k = 0}^n \frac{n!}{(n-k)!k!} = \frac{n!^{n+1}}{(0! 1! 2!\cdots n!)^2} = B(n-1) \frac{n^n}{n!} \\
D(n) &:= \sigma(B(n))\\
S(n) &:= \sum_{k=1}^n D(k)
\end{align*}$$

The task is to calculate $$S(40)$$. Knowing the prime factorization of a number, recall the basic formula for calculating the sum of divisor function:

  $$\sigma\left(\prod_{i = 1}^r p_i^{\alpha_i} \right) = \prod_{i = 1}^r \frac {p_i^{\alpha_i + 1} - 1} {p_i - 1} $$

In order to calculate $$S(n)$$, the only information we need to know about $$B(n)$$ is its prime factorization. Let `factor` represent the prime factorization of a number as a dictionary-like object. It is then easy to find the factorization of a product of numbers by simply noting that: $$\text{factor}(ab) = \text{factor}(a) \oplus \text{factor}(b)$$, where $$\oplus$$ represents "addition" of dictionaries (merge the keys, sum up the values for each key). Similarly, let $$d^n := d \oplus d \oplus \dots \oplus d$$ represent the $$n$$-fold "addition" of dictionaries (multiply the values in $$d$$ by $$n$$; this corresponds to taking powers) and $$\ominus$$ represent "subtraction" of dictionaries (this corresponds to division). To find the prime factorization of $$B(n)$$, we may use the following recursive relations:

$$\begin{align*}
\text{factor}(n!) &= \text{factor}((n-1)!) \oplus \text{factor}(n) \\
\text{factor}(B(n)) &= \text{factor}(B(n-1)) \oplus \text{factor}^n(n) \ominus \text{factor}(n!)
\end{align*}$$

The following piece of Julia code gives answer in about 20 seconds.

{% highlight julia %}
  using Nemo, Primes, Memoize
  R = ResidueRing(ZZ, 10^9+7)
  factor = Primes.factor

  @memoize fact(n) = n == 1 ? factor(1) : merge(+, factor(n), fact(n-1))
  @memoize B(n) = n == 1 ? factor(1) : merge( # REMOVED
  sigma(f) =  prod( (R(p)^(e+1)-R(1)) * R(p-1)^-1 for (p, e) in f )
  S(n) = R(1) + sum(sigma(B(k)) for k=2:n)

  @time S(20000)
{% endhighlight %}
