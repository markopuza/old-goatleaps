---
layout: post
title:  "Project Euler 622"
date:   2018-03-14 01:36:59 +0000
category-string: "Maths"
categories: euler maths
icon: euler622
---
# Riffle Shuffles

For $$ n = 2m $$ a positive even number, the >>[riffle/out shuffle](https://en.wikipedia.org/wiki/Out_shuffle)<< is defined as the permutation:

  $$ \pi_{2m} = \begin{pmatrix}
    0 & 1 & 2 & 3 & \cdots & 2m-2 & 2m-1 \\
    0 & m & 1 & m+1 & \cdots &  m-1 & 2m -1
  \end{pmatrix} $$

The function $$ s(n) $$ is the (group-theoretic) order of the permutation $$\pi_n$$ and the Project Euler problem tasks us with computing the sum of inverses of $$s$$, that is:

> \\[ \text{What is } S(k) := \sum_{n \in s^{-1}(k)} n \ \ ? \\]

For start, let's try and see what $$s$$ actually is. It is not hard to see that we can understand $$s$$ to be the order of 2 in the cyclic group $$\mathbb Z_{n - 1}$$.
\\
\\
_Proof_. Upon applying $$\pi_{n}$$, the 0-th and (n-1)-th (first and last) cards remain fixed. It is easy to see that any other card at position $$ i;\ 0 < i < n-1 $$ will be sent to $$ 2i $$ mod $$n - 1$$. Therefore, the card number $$1$$ will reach its original position no sooner than after $$k$$ shuffles, where $$k$$ is the smallest number such that $$2^k = 1$$ mod $$n - 1$$. But after such number of shuffles, all of the cards will be at their original positions, which gives $$s(n) = k$$. $$\square$$

{% highlight python %}
def s(n):
    assert n % 2 == 0
    if n == 2:
        return -1
    curr, cnt = 2, 1
    while curr != 1:
        curr, cnt = (2 * curr) % (n - 1), cnt + 1
    return cnt
{% endhighlight %}

The value $$s(n)$$ hence satisfies the relation $$2^{s(n)} \equiv 1 \text{ mod } n - 1 \iff (n - 1) \text{ divides } 2^{s(n)} - 1$$, which is obviously a necessary but not sufficient condition that $$s(n)$$ must satisfy. This allows us to compute $$s^{-1}(k) = \{d : (d - 1) \text{ divides } 2^k - 1 \text{ and } s(d) = k \}$$ and $$S(k) = \sum_{d \mid 2^k - 1;\ s(d) = k} (d+1)$$.

{% highlight python %}
def s_inverse(k):
    factors = list(chain(*[[prime] * exp for prime, exp in factorize(2**k - 1)]))
    # Compute all divisors of 2^k - 1. These are candidates d-1 for s(d) = k
    divisors = set([reduce(mul, subset, 1) for subset in powerset(factors)])
    return [x + 1 for x in divisors if s(x + 1) == k]

def S(k):
    return sum(s_inverse(k))
{% endhighlight %}

Which turns out fast enough on the problem input with runtime around $$0.1$$ seconds. Should one not feel good about rewriting ordinary number theoretic functions in pure python as above, the whole solution can be compressed into a one-liner using SymPy.

{% highlight python %}
from sympy.ntheory import n_order, divisors
S = lambda k: sum(x + 1 for x in divisors(2**k - 1) if n_order(2, x) == k)
{% endhighlight %}


The most expensive part of our approach is checking whether $$s(d+1) == k$$. It turns out that this can be avoided using a small trick involving the [Möbius inversion](https://en.wikipedia.org/wiki/Möbius_inversion_formula). Writing $$ S'(k) :=  \sigma_0(2^k - 1) + \sigma_1(2^k - 1) =  \sum_{d \mid 2^k - 1} (d+1) $$ where $$ \sigma $$ is the >>[divisor function](https://en.wikipedia.org/wiki/Divisor_function)<<, we deduce:

$$
\begin{align}
  S'(k) &= \sum_{d \mid 2^k - 1} (d+1) \\
        &= \sum_{m=0}^k\  \sum_{d \mid 2^k - 1; s(d) = m} (d+1)\\
        &= \sum_{m|k} S(m) \ \ \ \ \ \ \ (\text{as } s(d) | k)
\end{align}  
$$

This can be inverted by Möbius, giving us

$$S(k) = \sum_{m \mid k} \mu(m) S'\left( \frac k m \right) = \sum_{m \mid k} \mu(m) \left( \sigma_0(2^{\frac k m} - 1) + \sigma_1(2^{\frac k m} - 1) \right) $$

Using SymPy again we obtain a pretty fast solution.
{% highlight python %}
from sympy.ntheory import mobius, divisor_sigma, divisors
S = lambda k: sum(mobius(m) * (divisor_sigma(2**(k//m) - 1, 0) + divisor_sigma(2**(k//m) - 1, 1)) for m in divisors(k))
{% endhighlight %}

Source code:

- [euler622.py](/assets/code/euler622.py)
