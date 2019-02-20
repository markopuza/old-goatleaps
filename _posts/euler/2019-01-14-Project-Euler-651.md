---
layout: post
title:  "Project Euler 651"
date:   2019-01-14\ 01:00:58 +0000
category-string: "Maths"
categories: euler maths
icon: euler651
published: false
---

{% include euler_declaration.md %}

### Patterned Cylinders

In the problem number 651, we are interested in the number of colorings $$f(m, a, b)$$ with **exactly** $$m$$ colors of a tiled infinite cylinder whose circumference fits $$b$$ equally sized tiles. The colorings of the infinite cylinder are, however, restricted to the fact that they should be periodic with period $$a$$ (along the "infinite direction" of the cylinder). After a little bit of thought, we realize that the colorings that we are looking for are the colorings of a *torus* which fits $$a$$ tiles and $$b$$ tiles respectively across its two defining cycles.

<div align="center">
<img src="/assets/image/euler651_torus.png" width="30%">
</div>

Moreover, two colorings are considered equivalent if they can modified to each other via a combination of rotations and reflections. This is a pretty common theme, in which we recognize that the [>>Burnside's lemma<<](https://en.wikipedia.org/wiki/Burnside%27s_lemma) will come handy (recall for example [>>Problem 626<<](www.goatleaps.xyz/euler/maths/Project-Euler-626.html))!

Crucial realization here is that the reflections and rotations (the symmetries) responsible for two colorings being equivalent form a *group* $$G$$. Since any element of this group acting on the colored tiles gives just a permutation of the tiles, $$G$$ is a subset of the symmetric group $$S_{ab}$$. Now, using $$G$$, the Burnside's lemma gives us precisely what we need.

> The **[>>cycle index<<](https://en.wikipedia.org/wiki/Cycle_index)** of a subgroup $$G$$ of a symmetric group with degree $$n$$ is defined to be the following polynomial (in $$x_1, x_2, \dots, x_n$$):
>
$$ Z(G) := \frac 1 {|G|} \sum_{g \in G} \prod_{k = 1}^n x_k^{j_k(g)}
$$
>
where $$j_k(g)$$ is the number of cycles of length $$k$$ in $$g$$.

> The number of distinct (in the sense described above) colorings of our torus with **at most $$m$$ colors** is then, by the Burnside's lemma
>
$$\frac 1 {|G|} Z(G; x_1=x_2=\cdots=x_n=m)
$$


The work that remains now is to find out what the cycle index of $$G$$ is (or how does $$G$$ actually look like), and then move from the value when using **at most m colors** to the value when using **exactly m colors**. Implicitly hidden in the problem statement, we first realize that we only care about the case where $$a$$ and $$b$$ are **coprime** (indeed, in the problem statement, all of the values $$a, b$$ are two consecutive Fibonacci numbers, and these are always coprime). It follows that we may apply the reflections and rotations *independently* on the two defining cycles of the torus, yielding the direct product of [>>dihedral groups<<](https://en.wikipedia.org/wiki/Dihedral_group) $$G = D_a \times D_b$$. We now proceed to find $$Z( D_a \times D_b)$$.

It is not hard to find in tables/textbooks the cycle index of a dihedral group:

$$Z(D_n) = \frac 1 {2n} \sum_{d | n} \phi(d) x_d^{\frac n d}  + \begin{cases}
\frac 1 2 x_1 x_2^{\frac {n-1} 2} & n \text{ is odd} \\
\frac 1 4 \left(x_1^2x_2^{\frac {n-2} 2} + x_2^{\frac n 2}\right) &  n \text{ is even}
\end{cases}$$

But how do we find the cycle index of a direct product of two permutation groups? The derivation can be found, for example, in the following [>>paper<<](https://www.sciencedirect.com/science/article/pii/0012365X9390015L). We introduce a peculiar concept of (randomly denoted) $$\bowtie$$ multiplication of two polynomials.

> $$
\begin{align*}
f(x_1, x_2, \dots, x_u) &= \sum a_{i_1, i_2, \dots, i_u} x_1^{i_1} x_2^{i_2} \cdots x_u^{i_u} \\
g(x_1, x_2, \dots, x_v) &= \sum b_{j_1, j_2, \dots, j_v} x_1^{j_1} x_2^{j_2} \cdots x_v^{j_v} \\
& \\
f \bowtie g &:= \sum a_{i_1, i_2, \dots, i_u} b_{j_1, j_2, \dots, j_v} \prod_{\substack{1 \leq l \leq u \\ 1 \leq m \leq v}} x_{lcm(l, m)}^{i_l j_m gcd(l, m)}
\end{align*}
$$


Then $$Z(G_1 \times G_2 \times \cdots \times G_n) = Z(G_1) \bowtie Z(G_2) \bowtie \cdots \bowtie Z(G_n)$$, and, in particular:

> $$
Z(D_a \times D_b) = Z(D_a) \bowtie Z(D_a)$$

Gluing everything together, we have found an explicit formula for the number $$f'(m, a, b)$$ of colourings with **at most** $$m$$ colors:

$$\begin{align*} f'(m, a, b) &= \frac 1 {|D_a \times D_b|} Z(D_a \times D_b; x_1=x_2=\cdots=x_n=m) \\
        &= \frac 1 {4ab} [Z(D_a) \bowtie Z(D_b); x_1=x_2=\cdots=x_n=m]
\end{align*}$$

To find the the number $$f(m, a, b)$$ of colourings with **exactly** $$m$$ colors, we simply employ the following recursion:

$$f(m, a, b) = f'(m, a, b) - \sum_{k = 1}^{m-1} {m \choose k} f(k, a, b)$$


What remains now is to code up the cumbersome expressions above. In Python 3, these are all of the ingredients that we will need:

- Memoization.
{% highlight python %}
  from functools import lru_cache
{% endhighlight %}

- Factorization of a number.
{% highlight python %}
  from pyprimesieve import primes, factorize
{% endhighlight %}

- Fibonacci numbers.
{% highlight python %}
  N = 40
  fib = [0, 1]
  while len(fib) <= N:
      fib.append(sum(fib[-2:]))
{% endhighlight %}

- GCD and LCM.
{% highlight python %}
  gcd = lambda x, y: max(x, y) if not min(x, y) else gcd(y, x%y)
  lcm = lambda x, y: x*y//gcd(x,y)
{% endhighlight %}

- Modular inverse.
{% highlight python %}
  MOD = 10**9 + 7
  inv = lambda x: pow(x, MOD-2, MOD)
{% endhighlight %}

- Divisors of a number.
{% highlight python %}
  def divisors(n):
      for i in range(1, int(n**0.5 + 1)):
          if n % i == 0:
              yield i
              if i*i != n:
                  # <REMOVED>
{% endhighlight %}

- Binomials.
{% highlight python %}
  def choose(n, k):
      result = 1
      for i in range(k):
          result *= n - i
          result *= inv(i + 1)
          result %= MOD
      return result
{% endhighlight %}

- Euler's totient function.
{% highlight python %}
  @lru_cache(maxsize=None)
  def phi(n):
      totient = n
      for p, _ in factorize(n):
          totient -= totient//p
      return totient
{% endhighlight %}

- Bowtie multiplication (here, care needs to be taken to handle fractions -- modular inverses).
{% highlight python %}
  # A, B represented as a polynomial [(coeff, [(index, exponent),... ]), ...]
  def bowtie(A, B):
      res = []
      for a, xsa in A:
          for b, xsb in B:
              inv_coeff = a*b
              xsab = # <REMOVED>
              res.append((inv_coeff, xsab))
      return res
{% endhighlight %}

- Burnside's lemma
{% highlight python %}
  def burnside(Z, m, group_size):
      return sum(c * pow(m, sum(e for _, e in xs), MOD) % MOD for c, xs in Z) * inv(group_size)
{% endhighlight %}

- Cycle indices of dihedral groups.
{% highlight python %}
  def z_dihedral(n):
      ''' Return order and Cycle index of the n-th dihedral group '''
      if n == 2:
          return 2, [(1, [(1,2)]), (1, [(2,1)])]
      order = 2*n
      Z = # <REMOVED>
      if n%2 == 1:
          Z += [(n, [(1,1), (2,n//2)])]
      else:
          Z += [(n//2, [(1,2), (2,(n-2)//2)]), (n//2, [(2,n//2)])]
      return order, Z
{% endhighlight %}

- Function for $$f$$.
{% highlight python %}
  @lru_cache(maxsize=None)
  def f(m, a, b):
      orda, ZDa, ordb, ZDb = *z_dihedral(a), *z_dihedral(b)
      return (burnside(bowtie(ZDa, ZDb), m, orda*ordb) - # <REMOVED>
{% endhighlight %}

With the above tower of implemented concepts, PyPy 3 gives us the answer in about 1 second.

{% highlight python %}
  print(sum(f(i, fib[i-1], fib[i]) for i in range(4, N+1)) % MOD)
{% endhighlight %}
