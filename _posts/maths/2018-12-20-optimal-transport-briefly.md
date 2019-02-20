---
layout: post
title:  "Optimal Transport briefly"
date:   2018-12-19 03:38:59 +0000
category-string: "Maths"
categories: maths programming
icon: ott
published: false
---

[>>Transportation theory<<](https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)) is a very interesting young-ish field of Mathematics finding applications in many unusual places. In [>>another post<<](http://goatleaps.xyz/maths/programming/ott-face-interpolation.html) you can see how the optimal transport can be used to interpolate between faces, but before that, we dwell into the foundational concepts of the transport theory.

The problem of optimal transportation goes all the way to the Frenchman [>>Gaspard Monge<<](https://en.wikipedia.org/wiki/Gaspard_Monge) in 1781. The question he was interested in goes as follow:

> Given a mass of sand in its initial configuration, what is the best way to transport it to a desired, final configuration, for the least overall effort?

<div align="center">
  <img src="/assets/image/ott/dunes.png" width="50%">
</div>

## The Monge Problem
In modern mathematical terms, the Monge Problem can be formulated as the following optimisation problem:

- Let $$X, Y \in \mathbb R^d$$ be the **domain and target spaces**.

- We represent the mass on $$X$$ with a **probability density** $$f$$ and the mass on $$Y$$ with a probability density $$g$$ ($$f$$ and $$g$$ being probability densities means that $$\int_X f(x)dx = \int_Y g(y)dy = 1$$). We impose this restriction to ensure that the source and target spaces contain the same amount of mass.

<div align="center">
<img src="/assets/image/ott/illustration.png" width="50%">
</div>

- Let $$c: X \times Y \rightarrow [0, \infty)$$ be the **cost function**. This function describes the amount of effort needed to transport mass from a point $$x \in X$$ to a point $$y \in Y$$ (the amount of effort is $$c(x, y)$$).

> To describe the process of mass transportation, we will consider so-called **mass-preserving transport maps** $$T: X \rightarrow Y$$. The mass preservation condition is formally
>
 $$T_\# f = g \qquad \iff \qquad \int_A g(y) dy = \int_{T^{-1}(A)} f(x)dx \qquad \text{ for all } A \subset Y. $$
>
> We say that $$g$$ is a **push-forward** of $$f$$ under the map $$T$$. The push-forward condition ensures that no mass is created nor lost during the process of transportation. The above formula says nothing more than: **the amount of mass in any subset $$A \subset Y$$ is the same as in the subset $$T^{-1}(A) \subset X$$**.

- Given a particular transport map $$T$$, we may calculate its **transport cost** as

  $$ M(T) = \int_X c(x, T(x))f(x)dx.$$

> The Monge Problem seeks to find the **minimal possible transport cost** $$\mathcal T_c(f, g)$$ among all transport maps.
>
 $$ \boxed{\mathcal T_c(f, g) := \inf_{T:\ T_\# f = g}  M(T)} $$

# Solving the Monge problem

The Monge problem is quite intuitive to state, but turns out to be hard. For about 150 years after Monge had stated the problem in his paper, no real breakthrough was made in finding a satisfactory solution (and this is despite the fact that a monetary prize was offered for a progress in the topic). To illustrate why this was so, these are three immediate snags encountered when analysing the problem:

# Existence

- It may be the case that **no transport map exists**, let alone an optimal one.

As an example, we may take a space $$X$$ comprising of a single discrete point (with a [>>Dirac mass<<](https://en.wikipedia.org/wiki/Dirac_measure) sitting on it) and space $$Y$$ comprising of two discrete points. No transport map exists here, since there are no *functions* mapping a single point into two.

<div align="center">
  <img src="/assets/image/ott/nonexistence.png" width="22%">
</div>

- The **infimum in the Monge problem [>>may not be a minimum<<](https://math.stackexchange.com/questions/342749/what-is-the-difference-between-minimum-and-infimum)**. There are examples where no matter which transport map you choose, a different transport map with strictly smaller cost will always exist.

# Uniqueness

- When an optimal transport map exists, it is **not necessarily unique**.

As an example, consider the following "book-shifting". Let $$X$$ comprise of two discrete "books" of mass $$\frac 1 2$$ sitting at 0, 1 and $$Y$$ comprise of two "books" sitting at 1, 2. Let the cost function be $$c(x, y) =  \mid x - y \mid$$. Our objective can be interpreted as shifting the books from 0,1 to 1,2 optimally. There are two obvious ways to do this:

<div align="center">
  <img src="/assets/image/ott/nonuniqueness.png" width="44%">
</div>

The cost of the first way is

$$ M(T_1) = c(0, 1) \frac 1 2 + c(1, 2) \frac 1 2 = |0 - 1|\frac 1 2 + |1 - 2|\frac 1 2 = 1.$$

The cost of the second way is

$$ M(T_2) = c(0, 2) \frac 1 2 + c(1, 1) \frac 1 2 = |0 - 2|\frac 1 2 + |1 - 1|\frac 1 2 = 1.$$

Both of these transport maps give total transport cost 1, which can be shown to be optimal.

## The Kantorovich Problem
In 1942, the problem got finally tackled by a Soviet Mathematician [Leonid Kantorovich](https://en.wikipedia.org/wiki/Leonid_Kantorovich). His revolutionary idea was very neat. He would simply change the point of view: *generalize* the Monge problem into a more managable form, then go back and reason about it.

The relaxation of Kantorovich was very straightforward. Rather than sending mass from a single point of $$X$$ to a single point of $$Y$$,
>**allow splitting of the mass**.

That is, we will allow the mass from a single point in $$X$$ to be distributed among multiple points in $$Y$$. This is effectively achieved by replacing transport maps (*functions*) with transport plans (*measures*). In mathematical terms:


- Let $$X, Y \in \mathbb R^d$$ be the **domain and target spaces**.

- We represent the mass on $$X$$ with a **>>[probability measure](https://en.wikipedia.org/wiki/Probability_measure)<<** (a generalization of probability densities) $$\mu$$ and the mass on $$Y$$ with a probability measure $$\nu$$.

- Let $$c: X \times Y \rightarrow [0, \infty)$$ be the **cost function**.

> To describe the process of mass transportation, we will consider so-called (mass-preserving) **transport plans** $$\gamma$$: probability measures on the space $$X \times Y$$ with marginals $$\mu$$ and $$\nu$$. We also note that transport plans are a generalization of transport maps (a transport map *is* a transport plan, but not vice versa).
>
<div align="center">
  <img src="/assets/image/ott/gamma.png" width="44%">
</div>

Intuitivelly, for any $$A \subset X$$ and $$B \subset Y$$, the value $$\gamma(A \times B)$$ describes the amount of mass moved from $$A$$ to $$B$$.

> The Kantorovich Problem seeks to find the **minimal possible transport cost** $$\mathcal T_c(f, g)$$ among all transport plans.
>
 $$ \boxed{\mathcal T_c(\mu, \nu) := \inf_{\gamma} \int_{X \times Y} c(x, y) d\gamma } $$

# What did we earn?

- The Kantorovich problem is a **linear optimisation problem** with linear constraints (which was not the case for the Monge problem).

- The optimal solution to the Kantorovich problem **always exists** (under minor assumptions on the cost function).

- Not only the optimal solution exists, it can also be **characterized** (and computed) using techniques of duality.

- For some classes of cost functions (for example, strictly convex), the optimal solution is **unique**.

- For some classes of cost functions, the **optimal transport plan** can be shown to be the **optimal transport map**.

The above means that, choosing a reasonable cost function, the optimal transport maps/plans can be computed. This fact underlies, for example, the usefulness of the [>>Wasserstein metric<<](https://en.wikipedia.org/wiki/Wasserstein_metric) and its applications. More about the Wasserstein metric can be found in the [>>next post<<]([>>another post<<](http://goatleaps.xyz/maths/programming/ott-face-interpolation.html)).
