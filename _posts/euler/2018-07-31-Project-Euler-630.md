---
layout: post
title:  "Project Euler 630"
date:   2018-07-31\ 01:00:58 +0000
category-string: "Maths"
categories: euler maths
icon: euler630
---

{% include euler_declaration.md %}


### Crossed lines

This is a pretty straightforward question, as the number of solvers suggests. Given a set $$P$$ of $$n$$ points in the plane, we take a look at the set $$\mathcal L(P)$$ of all lines that can be formed by joining pairs of points in $$P$$. We need to calculate $$M(\mathcal L(P)) = \mid\mathcal L(P)\mid$$ and $$S(\mathcal L(P)) = $$ *the number of times any two of these lines intersect*.

We can characterize both *equality of lines* and *two lines intersecting* using the slope. Two lines can be declared equal if and only if they have the same slope and share a point. Two distinct lines are going to intersect if and only if they have distinct slopes.

Thus it will make sense to organize all the lines by their slope as the first step. Since all of the points in this problem are going to be integral, we may associate each line with its normalized slope -- which has integral coprime coordinates, and the first non-zero coordinate is positive. Notice that we will be using only integers and thus we need not worry about any possible floating point inaccuracies. Throughout, we will also take care not to include any line that shares a point with any other line with the same slope. Letting $$\#(s)$$ denote the number of lines with slope $$s$$, we simply have:

$$\begin{align*}M(\mathcal L(P)) &= \sum_{\text{slope } s} \#(s) \\
S(\mathcal L(P)) &= \textit{(all pairs of lines)} - \textit{(all non-intersecting pairs)} = {M(\mathcal L(P)) \choose 2} - \sum_{\text{slope } s} {\#(s) \choose 2}
\end{align*}$$

There will be at most $$n^2$$ distinct slopes, so the above quantities can be calculated in $$\mathcal O(n^2)$$ time, given $$\#$$. To compute $$\#$$'s, we will iterate over all pairs of points, computing the normalized slope vector for each pair (this will involve calling the greatest common divisor). The overall complexity is thus $$\mathcal O(n^2 \log C)$$ with $$C$$ being the size of the largest coordinate present in $$P$$.

The following piece of Julia code gives the answer in about 50 seconds.

{% highlight julia %}
using DataStructures
normalize(v) = # <REMOVED>
N = 2500

# generate the points
s = [290797]
for n=1:N*2
    push!(s, s[length(s)]^2 % 50515093)
end
t = rem.(s, 2000)-1000
P = Set([x for x in zip(t[2:2:length(t)], t[3:2:length(t)])]) # points
d = DefaultDict(Array{Tuple{Tuple{Int64,Int64},Tuple{Int64,Int64}},1}, Dict())

for p1 in P
    for p2 in P
        if p2 > p1
            slope = normalize(collect(p2)-collect(p1))
            if #<REMOVED>
                push!(d[slope], (p2, p1))
            end
        end
    end
end
M = sum(length(v) for v in values(d))
L = 2*binomial(M, 2) - 2*sum(binomial(length(v), 2) for v in values(d))
{% endhighlight %}
