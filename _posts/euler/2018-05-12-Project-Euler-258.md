---
layout: post
title:  "Project Euler 258"
date:   2018-05-07\ 01:00:59 +0000
category-string: "Maths"
categories: euler maths
icon: euler258
---

{% include euler_declaration.md %}


### A lagged Fibonacci sequence

The problem tasks us with solving a Fibonacci-like recurrence

$$g(k) = \begin{cases}1 & 0 \leq k < 2000 \\ g(k-2000) + g(k-1999) & k \ge 2000 \end{cases}$$

for a large value of $$k$$. The first approach that comes to mind is to use matrix exponentiation in the same way as one does for calculating large values of the Fibonacci sequence; this however does not work by far fast enough due to the size of the matrix needed. There are, however, employable simplifications.

Let $$M$$ be the $$2000 \times 2000$$ matrix corresponding to the recurrence, that is:

  $$ M = \begin{pmatrix} 0 & 0 & \cdots & 0 & 1 & 1 \\
                           &   & & & & 0\\
                              &   & \mathbb I_{1999}  & & & \vdots \\ &   &  & & & 0 \end{pmatrix}$$

The matrix $$M$$ has by definition the property that:

$$ M^n \begin{pmatrix} 1 \\ 1 \\ \vdots \\ 1\end{pmatrix} = M^n \mathbf 1 = \begin{pmatrix} g(n + 1999) \\ g(n + 1998) \\ \vdots \\ g(n) \end{pmatrix}$$

and we are thus looking for a way to compute $$M^{10^{18}} \mathbf 1$$, whereupon the bottommost entry of this will be the sought $$g(10^{18})$$. The power is clearly too large; and this is where the >>[Cayley-Hamilton theorem](https://en.wikipedia.org/wiki/Cayley–Hamilton_theorem)<< comes to the rescue! The theorem states that every square matrix satisfies its characteristic equation. What is the characteristic equation of $$M$$? Well, this can be read off easily from the recurrence itself: $$X^{2000} = 1 + X$$.

From this it follows that $$M^{10^{18}}$$ may be rewritten as a polynomial of degree $$< 2000$$, this being the corresponding representative in the quotient ring $$ \frac{\mathbb Z [X]} {(X^{2000} - 1 - X)}$$. Let this polynomial be $$\sum_{i = 0}^{1999} a_i M^i$$ (This can without fancy terms be understood as the _unique_ polynomial of degree $$< 2000$$ such that $$M^{10^{18}} = g(M) (X^{2000} - 1 - X) + \sum_{i = 0}^{1999} a_i M^i$$ for some polynomial $$g$$; i.e. a polynomial version of the concept of remainder.). But then:

$$M^{10^{18}} \mathbf 1 = \left(\sum_{i = 0}^{1999} a_i M^i \right) \mathbf 1 = \sum_{i = 0}^{1999} a_i M^i \mathbf 1$$

Reading off the bottommost entries in the above equation, we obtain:

$$g(10^{18}) =  \sum_{i = 0}^{1999} a_i g(i) = \sum_{i = 0}^{1999} a_i$$


Hence the only thing that we need to do is to find the polynomial representing $$X^{10^{18}}$$ in $$\frac{\mathbb Z [X]} {(X^{2000} - 1 - X)}$$ and sum up its coefficients! The following piece of Julia code returns the answer in about 0.1 seconds.

{% highlight julia %}
using Nemo
P, x = PolynomialRing(ResidueRing(ZZ, 20092010), "x")
#<REMOVED>
evaluate(data(RR(x)^(10^18)), 1)
{% endhighlight %}
