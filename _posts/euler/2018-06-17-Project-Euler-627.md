---
layout: post
title:  "Project Euler 627"
date:   2018-06-17\ 01:00:58 +0000
category-string: "Maths"
categories: euler maths
icon: euler627
---

{% include euler_declaration.md %}


### Counting Products

The task of the problem is extraordinarily easy to state. We need to find $$F(m, n)$$, the cardinality of the set of all possible products of $$n$$ numbers between $$1$$ and $$m$$.

$$F(m, n) := \left|\left\{ \prod_{i=1}^n x_i \ :\ 1 \leq x_i \leq m \text{ for all } i \right\}\right|$$

The key insight for solving the problem was to regard this set as the set of lattice points in a particular convex polyhedron. *At the time of writing this post, I have, however, still troubles rigorously justifying that this works, so the "guidance experience" is going to be somehow incomplete.*

Anyway; any number in the set $$E := \left\{ \prod_{i=1}^n x_i \ :\ 1 \leq x_i \leq m \text{ for all } i \right\}$$ can be written in the prime decomposition form $$p_1^{e_{p_1}}\cdots p_k^{e_{p_k}}$$ with $$p_i$$ primes less than or equal to $$m$$. We may thus identify $$E$$ with the set of vectors $$\mathbf e = (e_{p_1}, e_{p_2}, \dots, e_{p_k})^T$$ of exponents in the prime decompositions.

Dually, we may also represent any product in $$E$$ by the vector $$ \mathbf x = (x_2, x_2, \dots, x_m)^T$$, where $$x_i$$ denotes the number of times that the number $$i$$ appears in the product. Between the two representations, we have quite obvious relationship:

$$\mathbf e = A \mathbf x $$

where $$A = (a_{ij})$$ with $$a_{ij} = \max\{e \ \mid\ p_i^e \text{ divides } j\}$$ is just the matrix that counts the exponents of primes in the numbers $$ 2 \leq j \leq m$$. We are also subject to additional constraints:

$$\sum_{j=2}^m x_j \leq n \ \ \ \ \text{ and all } x_j \ge 0$$

This tells us nothing else that the set $$X$$ of all possible vectors $$\mathbf x$$ (where $$\mathbf x$$'s are regarded as vectors over $$\mathbb R$$, rather than $$\mathbb N$$) is, by definition, a *convex polyhedron*. Moreover, the result of applying the linear transformation $$A$$ on $$X$$, which is precisely our scrutinized set $$E$$ of all possible vectors $$\mathbf e$$, must be again a *convex polyhedron* (again regarded as vectors over $$\mathbb R$$)!

We also have a ready way to obtain the vertices of the convex polyhedron $$E$$ -- we just need to map the vertices of $$X$$ under $$A$$. The vertices of $$X$$ are simply:

$$V_X := \{(0, 0, \dots, 0)\} \cup \{(0, 0, \dots, 0, n_{\text{position } j}, 0, \dots 0) \ \mid\ j = 2, \dots, m\}$$

The vertices of $$E$$ are then $$A V_X$$. Finally, we only need the convex hull vertices to define the polyhedron $$E$$. Let thus $$H := \text{convex hull vertices of } AV_X$$. To finish off, we need the following conjecture:

**Conjecture: The lattice points of $$X$$ surject to the lattice points of $$E = AX$$.**

In other words, this equivalently says: "Any lattice point (vector with all integer components) $$\mathbf e \in E$$ can be written as $$A \mathbf x$$ for some lattice point $$\mathbf x \in X$$". The only thing we can say for sure, however, is: "Any lattice point $$\mathbf e \in E$$ can be written as $$A \mathbf x$$ for some (not necessarily lattice point) $$\mathbf x \in X$$".

From what I can see, this conjecture holds in this setting (and definitely doesn't hold for arbitrary matrix $$A$$), perhaps due to the structure of matrix $$A$$. **If you can prove the conjecture or have any other ideas, please contribute to the Project Euler problem discussion, or at least comment below.**

Provided that the conjecture holds, we simply have:

$$F(m, n) = \#\{\text{lattice points in the region bounded by } H\}$$

To find the number of lattice points in a convex polyhedron, I will only refer to the >>[Ehrhart polynomial](https://en.wikipedia.org/wiki/Ehrhart_polynomial)<<. The problem is at this point solvable without actually understanding the theory of Ehrhart polynomials, but I recommend looking into them - it is an interesting read.

The following piece of Sage code gives answer instantaneously.

{% highlight python %}
import numpy as np
from scipy.spatial import ConvexHull

extract =  # <Removed>

def F(m=30, n=10001):
    A = np.matrix([[extract(i, p) for i in range(2, m+1)] for p in primes_first_n(m) if p <= m])
    x_vertices = [np.zeros((m-1,1))] + [(np.eye(1,m-1,i)*n).reshape((m-1,1)) for i in range(m-1)]
    e_vertices =  # <Removed>
    hull = ConvexHull([x.reshape((1, len(A))).tolist()[0] for x in e_vertices])
    P = Polyhedron(vertices=[tuple(map(int, r)) for r in hull.points[hull.vertices].tolist()])
    return # <Removed>
{% endhighlight %}
