---
layout: post
title:  "Project Euler 624"
date:   2018-04-12 01:00:59 +0000
category-string: "Maths"
categories: euler maths
icon: euler624
---

{% include euler_declaration.md %}


### Two heads are better than one

Let $$M$$ be the random variable counting the number of times we toss an unbiased coin until we obtain two consecutive heads. Let $$P(n)$$ denote the probability $$\mathbb P(n \text{ divides } M)$$. The problem revolves about computing $$P(n)$$ for large values precisely.

As a helper variable, define $$Q(n)$$ to denote the __probability that after $$n$$ tosses, we obtain precisely a sequence of the form $$\dots, H, H$$, where in the $$\dots$$ part (the first $$n-2$$ tosses) no two consecutive heads appear__. Define also $$R(n)$$ to be the number of sequences of tosses of length $$n$$, such that no two consecutive heads appear. We have a clear relationship $$Q(n) = \frac {R(n - 3)} {2^n}$$ between $$Q$$ and $$R$$ (because the last three tosses in the sequence where we have encountered a pair of heads for the first time _must be_ precisely $$T, H, H$$). We can express $$P$$ in terms of $$R$$ as

$$P(n) = \sum_{i=1}^\infty Q(in) = \sum_{i=1}^\infty \frac{R(in - 3)} {2^{in}}$$

and thus we turn into reasoning about $$R$$ first. We can obtain a recursive relationship $$R(n) = R(n - 1) + R(n - 2)$$ by discerning two cases for the last coin toss in the sequence ($$R(n-1)$$ comes from the case where the last toss is $$tails$$, $$R(n-2)$$ from the case where the last toss is $$heads$$, as then the second to last toss must have necessarily been $$tails$$). Noticing furthermore that the first values of $$R$$ are $$R(0) = 1, R(1) = 2$$, which are precisely the second and third terms of the Fibonacci sequence, the recursive relationship $$R(n) = R(n - 1) + R(n - 2)$$
actually tells us that $$R$$ _is_ the Fibonacci sequence $$\{F_i\}$$ and

 $$
 \begin{align*}
 R(n) &= F_{n+2}\\
 P(n) &= \sum_{i=1}^\infty \frac{F_{in - 1}} {2^{in}}
 \end{align*}
 $$

 The trick for being able to calculate this efficiently is to turn the expression into a geometric series! For this we may use the fact that the Fibonacci numbers can be obtained by matrix exponentiation. In particular, the $$n$$-th Fibonacci number is the $$[0][0]$$ entry of the matrix $$\mathbb F^{n-1}$$ where

 $$\mathbb F = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$.

 We may hence rewrite:

$$
\begin{align*}
 P(n) &= \sum_{i=1}^\infty \frac{F_{in - 1}} {2^{in}}\\
      &= \left( \sum_{i=1}^\infty \frac{\mathbb F^{in - 2}} {2^{in}} \right) [0][0] \ \ \ \ \ \ \ \ \text{ (the } [0][0] \text{ entry of) }\\
      &= \left( \mathbb F^{-2} \sum_{i=1}^\infty \left(\frac{\mathbb F^n} {2^n}\right)^i \right)[0][0]
\end{align*}
$$

The determinant of $$\frac {\mathbb F} {2}$$ is smaller than one, hence the geometric series $$\sum_{i=1}^\infty \left(\frac{\mathbb F^n} {2^n}\right)^i$$ converges to:

$$\frac{\frac{\mathbb F^n} {2^n}}{ \mathbb I_2 - \frac{\mathbb F^n} {2^n}} = \frac{\mathbb F^n}{ 2^n \mathbb I_2 - \mathbb F^n}$$

Finally, we obtain:

$$ \begin{align*}
P(n) &= \left( \mathbb F^{-2} \frac{\mathbb F^n}{ 2^n \mathbb I_2 - \mathbb F^n} \right)[0][0]\\
  &= \left( \frac{\mathbb F^{n-2}}{ 2^n \mathbb I_2 - \mathbb F^n} \right)[0][0]
\end{align*}$$

At last, calculating $$Q(P(n), 10^9+9)$$ is nothing else than working out $$P(n)$$ using modular arithmetic. The following succinct piece of Julia code gives answer in mere $$0.005$$ seconds.

{% highlight julia %}
using Nemo
R = ResidueRing(ZZ, 10^9+9)
F = matrix(R, [1 1; 1 0])
Q(n) = (F^# <REMOVED>
@time Q(10^18)
{% endhighlight %}
