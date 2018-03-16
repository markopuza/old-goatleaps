---
layout: post
title:  "Project Euler 621"
date:   2018-03-06 01:36:59 +0000
category-string: "Maths"
categories: euler maths
icon: euler621
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
### Expressing an integer as the sum of triangular numbers

The problem tasks us with computing the function $$ G(n) $$ expressing the number of ordered ways to write $$ n $$ as a sum of _three_ triangular numbers. Triangular numbers are numbers of the form $$ T_k = \frac {k(k+1)} 2;\ k = 0, 1, 2, \dots $$.

We can readily convert the problem into somehow better looking equivalent. We can see that expressing $$ n $$ as a sum of three triangular numbers $$ n = T_x + T_y + T_z $$ is equivalent to expressing $$ 8n + 3 $$ as a sum of three _odd positive_ squares:

$$ \begin{align*}
    n &= T_x + T_y + T_z =  \frac 1 2 (x(x+1) + y(y+1) + z(z+1))\\
    2n &= \frac 1 4 ((2x + 1)^2 + (2y+1)^2 + (2z + 1)^2 - 12)\\
    8n + 3 &= (2x + 1)^2 + (2y+1)^2 + (2z + 1)^2
\end{align*}
$$

We thus have $$ G(n) = r_3(8n + 3) $$ where $$ r_k $$ is the [sum of (k) squares function](http://mathworld.wolfram.com/SumofSquaresFunction.html) (tweaked such that the order of squares matters).
{% highlight python %}
def sum_of_three_triangles(n):
    return sum_of_three_squares(8*n+3)
{% endhighlight %}

To compute $$ r_3 $$ we will use its obvious relation to (a simpler) $$ r_2 $$. If we manage to compute $$ r_2 $$ fast enough, this will be sufficient for the problem constraints.
\\[r_3(n) = \sum_{k = 1}^{\lfloor \sqrt n \rfloor} r_2(n - k^2)\\]

{% highlight python %}
def sum_of_three_squares(n):
    return sum(sum_of_two_squares(n - k*k) for k in # <REMOVED>
{% endhighlight %}

The formula for $$ r_2 $$ is standard enough to be found in most Number theory textbooks. Writing the prime factorization of $$ n $$ as \\[ n = 2^\gamma \prod_{p \equiv 1 \text{ mod } 4} p^{\alpha_p} \prod_{q \equiv 3 \text{ mod } 4} q^{\beta_q}, \\]
we have

$$ r_2(n) =
  \begin{cases}
  0 & \text{ if some of the } \beta_q \text{ is odd} \\
  \prod_{p} (\alpha_p + 1) & \text{ otherwise}
  \end{cases}
$$

Notice that if $$ n \text{ mod } 4 = 3 $$ then necessarily some of the $$ \beta_q $$ must be odd, which accounts for a speedup in our function. Also, we take advantage of the binary representation of numbers and use $$ n \& 3 $$ instead of $$ n \text{ mod } 4  $$.

{% highlight python %}
def sum_of_two_squares(n):
    if n <= 1: return 0
    # we do not care about the factors of 2
    # <REMOVED>
    if (n&3) == 3: return 0

    product = 1  # factorize
    for prime in PRIMES:
        if square[prime] > n:
            break
        exp = 0
        while n % prime == 0:
            exp += 1
            n //= prime
        if # < REMOVED >
            return 0
        if (prime&3) == 1:
            product *= exp + 1
    if n > 1:
        product *= 2
    return product
{% endhighlight %}

For the value $$ n = 17526000000000 $$ as required by the problem, this is unfortunately way too slow. Luckily, some time of [researching](http://www.personal.psu.edu/jxs23/p7.pdf)[^1] has brought fruit in form of the recurrence which is very suitable for the problem input. We modify the _"sum_of_three_squares"_ function accordingly.

$$
  r_3(9^\lambda n) =
  \begin{cases}
    3^\lambda r_3(n) & n \equiv 11 \text{ mod } 24 \\
    (2 \cdot 3^\lambda - 1) r_3(n) & n \equiv 19 \text{ mod } 24 \\
    \frac 1 2 (3^{\lambda+1} - 1) r_3(n) & n \equiv 3 \text{ or } 51 \text{ mod } 72
  \end{cases}
$$

{% highlight python %}
def sum_of_three_squares(n):
    lamb = 0
    while n % 9 == 0:
        lamb += 1
        # <REMOVED>
    if lamb > 0:
        if n % 24 == 11:
            return 3**lamb * sum_of_three_squares(n)
        if n % 24 == 19:
            return (2 * 3**lamb - 1) * sum_of_three_squares(n)
        if n % 72 in [3, 51]:
            return (3**(lamb + 1) - 1) * sum_of_three_squares(n) // 2
    return # <REMOVED>
{% endhighlight %}

Altogether, the code runs in 5 seconds, where the prime sieving takes by far the most time.

___
[^1]: Michael D. Hirschhorn and James A. Sellers. ON REPRESENTATIONS OF A NUMBER AS A SUM OF THREE TRIANGLES. Acta Arithmetica 77 (1996), 289 - 301
