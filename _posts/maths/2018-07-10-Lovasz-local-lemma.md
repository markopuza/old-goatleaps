---
layout: post
title:  "Lovász local lemma (Probabilistic method)"
date:   2018-07-10 01:36:59 +0000
category-string: "Maths"
categories: maths
icon: lovasz
---

Carrying a somehow mysterious name, the Lovász Local Lemma is an intriguingly neat technique to give existence proofs. In particular, it is one of the commonly used hammers in the probabilistic method. First, let us recall what the probability method (notoriously advocated by the famous Paul Erdős) is about:

> In order to show existence of a mathematical object with certain properties, one can do the following:
  - Define a probability space of objects and a way of sampling it
  - Show that the probability of the sought object being sampled is non-zero

Written down, this sounds almost blatantly obvious. However, with a speck of creativity, the probabilistic method can provide short and concise non-constructive existence proofs in cases where everything else fails. The *non-constructive* is important here -- it allows us to detach ourselves entirely from the burden of actually constructing (possibly very complex) objects whose existence we are after. We will know that the sought object exists, but have no idea how to find it. Let us examine the method in an example (due to Erdős):

*Example 1*: Let $$G$$ be a complete graph on $$n$$ vertices and $$r$$ a given integer. If  $$2{n \choose r} < 2^{r \choose 2}$$, then there *exists* a coloring of the edges of $$G$$ with two colors, such that every complete subgraph on $$r$$ vertices contains both colors.

*Proof*: Suppose that every edge in the graph is colored randomly with probability $$\frac 1 2$$ of picking either color. Let $$R$$ be the random variable counting the number of complete $$r$$-subgraphs which only contain one color. We also define an indicator variable $$X$$:

$$X(V) = \begin{cases}
  0 & \text{The subgraph with vertices } V \text{ contains } 1 \text{ color.} \\
  1 & \text{The subgraph with vertices } V \text{ contains } 2 \text{ colors.}
 \end{cases}$$

Then, taking expectation, we have:

$$\begin{align*} \mathbb E R &= \mathbb E \sum_{\substack{V\\ \mid V \mid = r}} X(V)\\
&= \sum_{\substack{V\\ \mid V \mid = r}} \mathbb E X(V)\\
&= \sum_{\substack{V\\ \mid V \mid = r}} \mathbb P (\text{all edges between vertices in } V \text{ are of the same color})\\
&= \sum_{\substack{V\\ \mid V \mid = r}} \frac 2 {2^{r \choose 2}} \\
&= {n \choose r} \frac 2 {2^{r \choose 2}}
\end{align*}$$

By assumption, this is smaller than $$1$$ and we thus have $$0 \leq \mathbb E R < 1$$. But this means that $$R$$, being an integer, must be equal to $$0$$ for some colourings (otherwise we would have $$\mathbb E R \ge 1$$).

In the above, we have used reasoning about expectation to show that the probability $$\mathbb P(R = 0) > 0$$. The Lovász local lemma provides a more direct way. We combine the three most common versions of the lemma into one statement:

> Let $$E_1, E_2, \dots, E_k$$ be a sequence of (bad) events, each of which happens with probability *at most* $$p$$, and where each event is dependent on *at most* $$d$$ of them. If either of these conditions holds:
  - $$epd \leq 1\ \ \ \ \ \ (e \text{ is the natural logarithm})$$
  - $$\begin{cases} p < \frac{(d-1)^{(d-1)}}{d^d} & \text{ when } d > 1 \\ p < \frac 1 2 & \text{ when } d = 1 \end{cases}$$\\
then the probability that *none of the event* occurs is positive.

Let's see how the lemma can be applied in an example with the $$k$$-SAT problem. Recall that the >>[$$k$$-SAT problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem)<< problem is, given a set of boolean variables $$\{x_1, x_2, \dots, x_k\}$$, to decide whether a formula in >>[CNF](https://en.wikipedia.org/wiki/Conjunctive_normal_form)<<, where each clause contains precisely $$k$$-literals, is satisfiable (that is, there exists an assignment of truth values to the variables, such that the formula evaluates to truth). An example of a $$3-SAT$$ formula may be:

$$(x_1 \vee \neg x_2 \vee x_4) \wedge (\neg x_1 \vee \neg x_2 \vee x_3) \wedge (x_2 \vee \neg x_3 \vee \neg x_4)$$

*Example 2*: Suppose that each variable in a $$k$$-SAT formula appears in at most $$\frac{2^k}{ek}$$ clauses. Then it is satisfiable.

*Proof*: Suppose that every variable is assigned a truth value randomly, with probability $$\frac 1 2$$ for either option. Let $$E_i$$ denote the event that the $$i$$-th clause evaluates to false. In such a case, all variables in the cause must be "wrong": $$\mathbb P(E_i) \leq 2^{-k} =: p$$. As each variable in the clause is present in at most $$\frac{2^k}{ek}$$ other clauses, the event $$E_i$$ is dependent on at most $$k \frac{2^k}{ek} = \frac{2^k}{e} =: d$$ other events. By the Lovász local lemma, since $$epd = e 2^{-k} \frac{2^k}{e} \leq 1$$ holds, we deduce:

$$\mathbb P(\text{none of the events } E_i \text{ occurs}) > 0 \rightarrow \text{ formula is satisfiable.}$$

Lets take a look at one other example related to hypergraphs. A hypergraph is a tuple $$H = (V, E)$$ of vertices $$V$$ and hyperedges $$E$$. Each hyperedge is a subset of the vertices. A 2-colouring of a hypergraph is an assignment of colors to vertices such that no hyperedge is monochromatic (connects vertices all of the same color).

*Example 3*: Let $$G$$ be a hypergraph where each hyperedge contains at least $$k$$ vertices. Find sufficient conditions for $$G$$ to be 2-colourable.

*Solution*: Assume that each vertex is colored uniformly at random with the $$2$$ colors. Let $$E_e$$ be the event that the hyperedge $$e$$ ends up monochromatic. By assumption on the number of vertices in a hyperedge, we deduce the bound on probability:

$$\mathbb P(E_e) \leq 2 \cdot 2^{-k} = 2^{1 - k} =: p$$

Now suppose that every hyperedge intersects any other hyperedge in at most $$d$$ vertices. By the Lovász Local Lemma, $$G$$ will be $$2$$-colourable if $$epd \leq 1$$, that is:

$$d \leq \frac 1 {pe} = \frac{2^{k-1}} e$$

Thus a sufficient condition is that every hyperedge intersects any other hyperedge in at most $$\frac{2^{k-1}} e$$ vertices.
