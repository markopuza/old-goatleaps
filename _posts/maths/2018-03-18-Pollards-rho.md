---
layout: post
title:  "Pollard's rho factorization algorithm"
date:   2018-03-16 01:36:59 +0000
category-string: "Maths"
categories: programming maths
icon: pollardrho
---

It is well known that there are fairly efficient algorithms for determining whether an integer $$ n $$ is a prime, however, it is
a whole other story for integer factorization. I will describe here an interesting randomized algorithm for integer factorization, which
has a bunch of desirable properties:
  - It is fast, with expected runtime being roughly $$ n^{\frac 1 4} $$ gcd (greatest common divisor) operations.
  - It only uses a constant amount of space.

It goes like this. Assume a given integer $$ n $$ divisible by at least two prime factors (it is not a prime power), so we can write $$ n = p q $$ where $$p, q$$ are coprime and $$ p < q $$. To emphasise, in the following we _will not know_ what $$p, q$$ are, we will only make use of the fact that they exist. Also, our goal will be to find one of these.

Imagine sampling numbers $$ x_1, x_2, \dots, x_l $$ from $$\mathbb Z_n$$ _without replacement_, where we will stop sampling as soon as the newly sampled number $$x_l$$ satisfies

$$
\begin{align*}
&x_l \equiv x_i\  (\text{ mod } p)\ \ \ \ \  \text{ for some } 1 \leq i < l\ \ \ \ \ \ \ \ \ (1)\\
\iff & p\ \mid\ (x_l - x_i) \\
\iff & p\ \mid\ gcd(x_l - x_i, n)
\end{align*}
$$

Any occurrence of (1) we will refer to as _collision_. Notice that there are only $$ p $$ available bins modulo $$ p $$, hence, by the pigeonhole principle, the above is guaranteed to stop _at most_ after $$p + 1$$ samples. Most importantly, notice that after we stop, we have $$ x_l \neq x_i, -n < x_l - x_i < n$$ and thus $$ p \leq gcd(x_l - x_i, n) < n$$. Then we are finished, as $$ gcd(x_l - x_i, n) $$ is a non-trivial factor of $$n$$!

Consider thus the following algorithm:
  - Keep sampling numbers $$x_1, x_2, \dots, x_l$$ as described above, one by one.
  - Check the condition $$gcd(x_j - x_i, n)\ \mid n $$ for all $$ 1 \leq i < j \leq l $$.

How many samples $$l$$ do we need to gather until we fulfil the condition $$gcd(x_j - x_i, n)\ \mid n $$? Well, the discussion in the previous paragraph this is _at most_ as many as we need for the collision (1) to occur. The question can be therefore rephrased as: How many samples $$l$$ do we need until $$ x_j \equiv x_i\  (\text{ mod } p) $$ for some $$ 1 \leq i < j \leq l $$? But this is nothing else than the Birthday paradox!

"What is the probability that two people in a room share a birthday?" is completely analogous to our question "What is the probability that among $$l$$ samples $$\{x_i\}$$ two of them fall into same equivalence class modulo $$p$$?". The answer can be bounded:

$$
\begin{align*}
  \mathbb P (\text{some }x_j \equiv x_i\  \text{ mod } p) &= 1 - \mathbb P (\text{all }x_j \not\equiv x_i\  \text{ mod } p) \\
  &= 1 - \prod_{i = 1}^{l - 1} \left(1  - \frac i p \right) \\
  &\ge 1 - \prod_{i = 1}^{l - 1} e^{- \frac i p}\ \ \ \ \ \ \text{since } 1 - x \leq e^{-x} \\
  &= 1 - \exp\left({- \frac 1 p \frac{l(l-1)} 2}\right) \\
  &\approx  1 - \exp\left({- \frac 1 p \frac{l^2} 2}\right)
\end{align*}
$$

And so already with $$l \approx 2 \sqrt p$$ we have the probability of collision around $$1 - e^{-2} \approx 0.86 $$. This tells us to expect that the collision occurs after taking only around $$O(\sqrt p)$$ samples. Since we considered $$p$$ to be given by $$n = pq;\ p < q$$, the amount of samples that we expect to need is $$O(\sqrt p) = O(\sqrt{\sqrt n}) = O(n^{\frac 1 4})$$.


The backbone of the Pollard's rho factorization will be the following heuristic. Choose an integer $$x_0 \in \mathbb Z_n$$ and a polynomial $$ f : \mathbb Z_n \rightarrow \mathbb Z_n $$ (Usual choice is 2 and $$f(x) = x^2 + 1$$.). Instead of randomly sampling the sequence $$\{x_i\}$$ without replacement, we will generate it _deterministically_, obtaining a pseudo-random sequence:

$$x_i = f(x_{i - 1})$$

To make any rigorous statements about the sufficiency of "randomness" introduced this way is very tough. However, there are (perhaps less satisfying) empirical reasons why using a pseudo-random sequence like this is sufficient: the Pollard's factorization seems to be working well. One of the algorithm's successes was factorization of the ninth [Fermat number](https://en.wikipedia.org/wiki/Fermat_number):

$$F_8 = 1238926361552897 \cdot 93461639715357977769163558199606896584051237541638188580280321$$

In any case, we are now in position to describe the algorithm in its fullness. Consider (conceptually) a graph whose vertices are the elements of $$\mathbb Z_p$$. Having chosen $$x_0$$ and polynomial $$f$$, we will consider an oriented edge between vertices $$x_i (\text{ mod } p)$$ and $$x_{i+1} (\text{ mod } p)$$ (both $$\in \mathbb Z_p$$) precisely when $$x_{i+1} (\text{ mod } p) = f(x_i) (\text{ mod } p)$$ for some $$i$$. As there are finitely many $$\mathbb Z_p$$ and our generation of the sequence by $$x_j = f(x_{j - 1})$$ is completely deterministic, we will cycle in the graph after a while. The whole situation looks like this (And this is where the $$\rho$$ in the name of the algorithm comes from.):

<img src="/assets/image/pollard_rho.png" style="width: 40%; display: block; margin-left: auto; margin-right: auto;">

Believing that the pseudo-random sequence behaves itself, the Birthday paradox discussion tells us that the length of the cycle will be around $$O(n^{\frac 1 4})$$. Now, how do we detect a cycle in this conceptual graph? Well, using (1) we can test whether $$x_i$$ and $$x_j$$ fall to the same vertex in the graph by testing whether $$gcd(x_j - x_i, n)$$ is a non-trivial factor of n. And this operation is all we need in order to employ the >>[Floyd's Tortoise and Hare cycle detection algorithm](https://en.wikipedia.org/wiki/Cycle_detection)<< (Tortoise and Hare move on the graph with speeds 1 and 2 respectively. The first vertex that they meet at must be contained in a cycle.), which can detect a cycle in time proportional to the length of the cycle (and constant space). Summarizing, we can expect to find a cycle and thus a proper factor of $$n$$ in time of performing $$O(n^{\frac 1 4})$$ gcd operations. And all of that with a remarkably short and simple code:

{% highlight python %}
from fractions import gcd

def pollards_rho(n, x0=2, f=lambda x: x*x + 1, max_iter=10**6):
    x, y = x0, x0
    for _ in range(max_iter):
        x, y = f(x) % n, f(f(y)) % n # tortoise, hare
        d = gcd(abs(x - y), n)
        if d > 1:
            return d
    return n
{% endhighlight %}

Here, I have included an upper bound on the length of the sequence $$\{x_i\}$$, so we avoid infinite loops by giving up prematurely. It is important to note that, whether due to the generation of $$x_i$$ being non-random or due to $$n$$ being a prime (power), _the Pollard's rho algorithm as described may not terminate_. For any practical applications it is reasonable to check whether your integer is a prime power before starting Pollard's rho. As a general consequence of how we reasoned about the algorithm, the smaller factor your integer has, the faster Pollard's rho will tend to be. This is why it was successful with factoring $$F_8$$, whose first factor 1238926361552897 is relatively "small".

As the last thing, let's see how the above procedure deals with randomly chosen integers between $$10^{19}$$ and $$10^{20}$$, running on PyPy3, 2.7 GHz Intel Core i5:

| Integer $$n$$    | Factorization           | Time taken (s)  | Notes |
| ------------- |:-------------:| -----:| ---------:|
| 96764544874272622169 | 230237209 x 420281957441 | 0.060839 |
| 55758240055524291931 | 131 x 425635420271177801 | 0.000058 |
| 52595570150902145711 | 2713 x 19386498396941447 | 0.000287 |
| 54530065810466921693 | 54530065810466921693 x 1 | 4.221130 | Prime |
| 76937877947075472797 | 37 x 2079402106677715481 | 0.000028 |
| 87081594094471557253 | 29 x 3002813589464536457 | 0.000070 |
| 86157342400390552069 | 3461 x 24893771280089729 | 0.000111 |
| 28197957983033436721 | 28197957983033436721 x 1 | 4.274322 | Prime |
| 29951290030313188349 | 59 x 507648983564630311 | 0.000032 |
| 74279717678385918737 | 84509 x 878956296706693 | 0.002071 |
| 44657213935372994281 | 44657213935372994281 x 1 | 4.510721 | Prime |
| 97912152549056935669 | 74531 x 1313710436584199 | 0.001908 |
| 20228236878280923857 | 23 x 879488559925257559 | 0.000026 |
| 51555948593461122523 | 9497 x 5428656269712659 | 0.000365 |
| 53229062465988471241 | 131 x 406328721114415811 | 0.000071 |
| 31315421851347505283 | 10513 x 2978733173342291 | 0.000107 |
| 89179931205901546169 | 43 x 2073951888509338283 | 0.000041 |
| 53196997219848404297 | 59 x 901644020675396683 | 0.000039 |
| 50597420757695715781 | 421 x 120183897286688161 | 0.000130 |
| 85242256987119573301 | 23 x 3706185086396503187 | 0.000026 |
| 11855105309203805442489519385571 | 22801765463 x 519920500385852312917 | 0.300823 |
