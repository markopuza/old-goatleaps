---
layout: post
title:  "GCD Counting (Codeforces ER45)"
date:   2018-06-12 01:38:59 +0000
category-string: "Programming"
categories: programming maths
icon: gcdcountings
---

Below you can find a thorough explanation of the (hardest) >>[GCD Counting](http://codeforces.com/contest/990/problem/G)<< problem of recent >>[Educational Codeforces Round 45](http://codeforces.com/contest/990)<<, as well as a Python solution. I found this problem extraordinarily neat and with the (official editorial) solution, one can learn a nice number theoretic trick:

> Suppose we are given a set S and an arithmetic function $$f$$, where our goal is to determine the cardinality $$\mid \{s \in S \ \mid \ f(s) = n\} \mid$$ for various $$n$$. It may be *much more efficient* to compute cardinalities $$\mid \{s \in S \ \mid \ n \text{ divides } f(s)\} \mid$$ first and then construct from these what we need.

Let me now explain this cryptic statement in the setting of our problem. The Codeforces problem goes:

> Suppose we are given a tree $$T$$ with $$N$$ vertices $$\{1, 2, \dots, N\}$$, where the node $$i$$ is labelled with an integer $$a_i$$ ($$1 \leq a_i \leq 2 \cdot 10^5$$). Let $$g(n)$$ be the number of non-empty simple paths $$p = (p_1, p_2, \dots, p_k)$$ in the tree such that $$gcd(a_{p_1}, a_{p_2}, \dots, a_{p_k}) = n$$. Find $$g(n)$$ for all $$1 \leq n \leq 2 \cdot 10^5$$.

As the first grey paragraph suggests, we may take interest in a "weaker" quantity. Let $$h(n)$$ be the number of non-empty simple paths $$p = (p_1, p_2, \dots, p_k)$$ in the tree such that $$n$$ **divides** $$gcd(a_{p_1}, a_{p_2}, \dots, a_{p_k})$$. We will see that computing $$h$$ is quite easy and we may construct the values of $$g$$ from the values of $$h$$. Indeed, letting $$\mathcal P$$ denote the set of primes between 1 and $$N$$, we can by simple counting (the inclusion-exclusion principle) deduce that:

$$\begin{align*}g(n) &= h(n) - \sum_{\substack{p_1 \in \mathcal P}} h(np_1) + \sum_{\substack{p_1, p_2 \in \mathcal P \\ p_1 \neq p_2}} h(np_1p_2) - \dots \\
  &= \sum_{P \subseteq \mathcal P} (-1)^{\mid P \mid} h\left(n \prod_{p \in P} p\right)
\end{align*}$$

Note that this is just formalized reasoning of: "To count the paths with gcd=n, we take paths with n$$\mid$$gcd, take away all paths with gcd divisible by $$2n, 3n, 5n, \dots$$, then due to overcounting take back all paths with gcd divisible by $$2\cdot 3n, 2\cdot5 n, \dots$$, $$\dots, \dots$$ ". Note also that in the above sum, $$h$$ of any value greater than $$N$$ will clearly be zero. The sum of this form can be by an experienced eye turned into a compter-scientifically nicer form using the [Möbius function](https://en.wikipedia.org/wiki/Möbius_function). Recall its definition:

$$\mu(n) = \begin{cases}0 & p^2 \text{ divides } n \text{ for some prime } p \\ 1 & n \text{ is a product of even number of primes}\\ -1 & n \text{ is a product of odd number of primes} \end{cases}$$

In particular, $$\mu \left(\prod_{p \in P} p \right) = (-1)^{\mid P \mid}$$. We may also use, very conveniently, $$\mu$$ to "disappear" exactly the terms which we don't have in the above summation:

$$g(n) = \sum_{P \subseteq \mathcal P} (-1)^{\mid P \mid} h\left(\prod_{p \in P} p\right) = \sum_{i = 1}^{\lfloor \frac {2\cdot10^5} n \rfloor} \mu(i) h(ni)$$

So how do we compute the values $$h$$? To find $$h(n)$$, consider the subgraph $$T_n$$ of $$T$$ where we retain only the vertices $$i$$ where $$a_i$$ is divisible by $$n$$. It is not hard to see that for any path, its gcd is divisible by $$n$$ if and only if all of its vertices lie in $$T_n$$. Thus we have:

$$h(n) = \# \text{ of simple paths in } T_n = \sum_{C \text{ connected component of } T_n} \frac{ |C| (|C| + 1 )} 2$$

To detect the connected components of $$T_n$$, we may just use the breadth-first search. Putting the solution together in Python (This Python solution *does not* pass the time limits to be accepted by the Codeforces checker, even though any operations were converted to be array-based. It seems that Python is just too slow for some tasks. Anyhow, if you are after passing the time limit, rewriting the below code into a faster language will give you a pass):

{% highlight python %}
import sys
lim = 2*10**5

# precalculate primes
is_prime = [False, False] + [True for _ in range(lim+1)]
for i in range(2, int((lim+1) ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i, (lim+1) // i + 1):
            is_prime[i * j] = False

# precalculate mobius function
mu = [1 for _ in range(lim+1)]
for p, prime in enumerate(is_prime):
    if prime:
        for j in range(p, lim+1, p):
            mu[j] *= -1
        for j in range(p*p, lim+1, p*p):
            mu[j] = 0

# read input
N, a = int(sys.stdin.readline()), list(map(int,  sys.stdin.readline().split()))
tree = [[] for _ in range(N)]
for i in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    tree[x-1].append(y-1)
    tree[y-1].append(x-1)

# inv_a[n] = list of vertices i such that a_i = n
inv_a = [[] for _ in range(lim + 1)]
for i, v in enumerate(a):
    inv_a[v].append(i)

# helper arrays
visited_by = [0 for _ in range(lim + 1)] # will keep track of visits in bfs
good = [0 for _ in range(lim + 1)] # avoids the need to use (slow) % operation
stack = [0 for _ in range(lim + 1)] # will serve as stack in array-based bfs

h = [0 for _ in range(lim + 1)]
for n in range(1, lim+1):
    for j in range(n, lim+1, n):
        good[j] = n
    for j in range(n, lim+1, n): # j = multiples of n
        for vertex in inv_a[j]:
            if visited_by[vertex] < n: # bfs
                head, tail, component_size = 0, 1, 0
                stack[0] = vertex
                while head < tail:
                    root = stack[head]
                    head += 1
                    visited_by[root] = n
                    component_size += 1
                    for ne in tree[root]:
                        if visited_by[ne] < n and good[a[ne]] == n:
                            stack[tail] = ne
                            tail += 1
                h[n] += component_size * (component_size + 1) // 2

for n in range(1, lim+1):
    g_n = sum(mu[i] * h[n*i] for i in range(1, int(lim/n) + 1))
    if g_n:
        sys.stdout.write('{:d} {:d}\n'.format(n, g_n))
{% endhighlight %}

How efficient is the above solution? Consider the worst case scenario when $$N = lim\  (= 2 \cdot 10^5 \text{ in our case})$$. The precalculation of primes with the Sieve of Eratosthenes takes $$\mathcal O (N\ \log\ \log\ N)$$ time, sieving the Möbius function takes $$\mathcal O(N\ \log N)$$ time. The main bottleneck becomes the calculation of $$h$$. Let's first analyze how many operations (cummulatively) will be invoked by the lines that come after "*for vertex in inv_a[j]:*". Vertex $$i$$ appears in *inv_a* $$\sigma_0(a_i)$$ times (the number of divisors of $$a_i$$), and hence, while performing the bfs's, we will visit each vertex *and all of its neighbours* $$\mathcal O(\sigma_0(a_i))$$ times. Altogether, this will give us $$\mathcal O(\sum_{i=1}^N (\deg(i) + 1)\sigma_0(a_i))$$ operations. We may upper-bound this further considering $$\sum_{i=1}^N \deg(i) = \mathcal O(N)$$ and $$\sigma_m := \max_{i=1, \dots, N} \sigma_0(a_i)$$, resulting in bound $$\mathcal O(N \sigma_m)$$. Next, anything that comes before "*for vertex in inv_a[j]:*" will cummulatively result in $$\mathcal O(N\ \log N)$$ operations. The final few lines computing all values $$g(n)$$ will again result in $$\mathcal O(N\ \log N)$$ operations. The overall complexity is $$\mathcal O(N(\log N + \sigma_m))$$.

As the last remark, we note that in case $$N = 2 \cdot 10^5$$, we have $$\sigma_m = 160$$.
