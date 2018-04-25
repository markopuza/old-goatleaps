---
layout: post
title:  "Karger's mincut algorithm in Python"
date:   2018-04-26 01:38:59 +0000
category-string: "Programming"
categories: programming
icon: kargers
---

I have encountered the Karger's algorithm multiple times in a quick succession; in a Randomness & Computation course and as a solution of a problem in the Week of code 37. Karger's algorithm is a method for computing a _minimum cut_ of a graph. The idea behind the method is pretty simple and is well explained in >>[Wikipedia](https://en.wikipedia.org/wiki/Karger%27s_algorithm)<<. __The code is further down in this post.__

Let our graph have $$n$$ vertices and $$m$$ edges. A brief overview is:


### Contraction
- Select an edge __uniformly at random__ (Uniformly is _the important part_.).
- Contract the endpoints of this edge, decreasing the number of vertices in the graph by one.
  - This removes all of the edges between the endpoints and redirects all of the edges to either endpoint into the new, contracted, vertex.
  <p align="center"> <img src="/assets/image/karger_contraction.png" width="10%"/> </p>
- Repeat the contraction until only two vertices with multiple edges between them are left.
- Consider these edges to comprise the minimum cut of the graph.

### Karger's algorithm

It can be shown that performing a contraction returns the true minimum cut with probability $${n \choose 2}^{-1}$$.
- Well, repeat the contraction algorithm multiple time and from all of these trials, pick the smallest cut.
- In particular, repeating the contraction $${n \choose 2}\ln{n}$$ times will give quite a high probability of success:

$$\mathbb P(\text{true min-cut NOT discovered}) = \left(1 - {n \choose 2}^{-1}\right)^{ {n \choose 2} \ln{n}} \leq \frac{1}{e^{\ln n}} = \frac 1 n$$

With the best known implementation, Wikipedia gives asymptotics of $$O(n^2 m \log n)$$.

### Karger-Stein algorithm
This can be viewed as a sped up version of the Karger's algorithm - with the right implementation, it should be asymptotically an order of magnitude faster.
- If $$n \leq 6$$, use a deterministic algorithm to find the minimum cut.
- Otherwise, do the following twice and choose the smaller result:
  - Keep contracting randomly chosen edges until $$\lceil 1 + \frac{n}{\sqrt 2}\rceil$$ vertices are left in the graph.
  - Recursively run Karger-Stein algorithm on the remaining graph.
- Analysis is in this case more complicated, but running the Karger-Stein algorithm $$O(\log n)$$ times should give a probability of failure $$O(\frac 1 n)$$.

With the best known implementation, Wikipedia gives asymptotics of $$O(n^2 \log^3 n)$$.

___


The following piece of Python 3 code contains a Graph class equipped with three methods for finding the (size of) the minimum cut in the graph:
- (Randomized) Karger's algorithm
- (Randomized) Karger-Stein algorithm
- (Deterministic) >>[Edmonds-Karp](https://en.wikipedia.org/wiki/Edmonds–Karp_algorithm)<< $$O(nm^2)$$ algorithm

> [kargers_mincut.py](/assets/code/kargers_mincut.py)



I have compared the speed of the Karger-Stein method, Edmonds-Karp method and the minimum_cut function from the NetworkX library, on randomly generated graphs (Each possible edge was put into the graph with probability $$\frac 1 2$$ and with random weight.) of increasing size. I run these on PyPy3 and for each size of the graph, multiple runs were averaged.

<p align="center">
  <img src="/assets/image/karger_figure.png" width="60%"/>
</p>

In general, the implemented Karger-Stein method almost always gives the true minimum cut, although of course, here and there, it does not succeed in finding the minimal one. The reliability of the methods was also tested on the following >>[HackerRank problem](https://www.hackerrank.com/contests/w37/challenges/two-efficient-teams)<<, which it has passed.


Finally; my implementation seems to be working quite fast and reliably, but is by no means polished. __Any suggestions/improvements are welcome!__
