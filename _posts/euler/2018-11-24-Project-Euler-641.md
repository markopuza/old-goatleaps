---
layout: post
title:  "Project Euler 641"
date:   2018-11-24\ 01:00:58 +0000
category-string: "Maths"
categories: euler maths
icon: euler641
---

{% include euler_declaration.md %}

### A long row of dice

Striping the problem of its dicey narrative, the task boils down to finding the value $$ f(10^{36}) $$ of the following function $$f$$:

$$f(N) = |\{i\ :\ \sigma_0(i) \equiv 1 \text{ mod } 6,\ i = 1, 2, \dots, N\} \mid$$

where $$\sigma_0(n)$$ is the divisor function, that is a function that counts the number of positive divisors. We now turn to characterise numbers $$n$$ for which it is the case that $$ \sigma_0(n) \equiv 1 \text{ mod } 6$$. For this, recall the standard formula (when we know the prime factorization of $$n = \prod_{i=1}^r p_i^{\alpha_i}$$):

$$ \sigma_0(n) = \prod_{i=1}^r (\alpha_i + 1)$$

Assuming that $$ \prod_{i=1}^r (\alpha_i + 1) \equiv 1 \text{ mod } 6$$, we immediately see that none of the $$(\alpha_i + 1)$$ can be 0, 2, 3, or 4 (by simply looking at this equation modulo 2, 3) modulo 6. Each $$(\alpha_i + 1)$$ thus gives remainder 1 or 5 = -1, and each $$\alpha_i$$ gives remainder 0 or 4 modulo 6. Moreover, the number of $$(\alpha_i + 1)$$'s giving remainder -1 **must be even**. Going back to the prime factorization of number $$n$$, we may rewrite it as:

$$ n = p_1^{6k_1} \cdots p_m^{6k_m} q_1^{6l_1 + 4} \cdots q_{2u}^{6l_{2u} + 4}$$

and pulling together the sixth powers:

$$ n = ( p_1^{k_1} \cdots p_m^{k_m} q_1^{l_1} \cdots q_{2u}^{l_{2u}} )^6  (q_1 \cdots q_{2u})^4 =: A^6 B^4$$

Here now comes the crucial observation: to construct an integer $$n$$ satisfying the above relation, the first chunk $$(q_1 \cdots q_{2u})$$ *can be taken to be any integer $$B$$ for which the Möbius function* $$ \mu(B) = 1$$ (this comes straight from the definition of the Möbius function). Afterwards the first chunk, $$( p_1^{k_1} \cdots p_m^{k_m} q_1^{l_1} \cdots q_{2u}^{l_{2u}} )$$, *can be set to be an arbitrary integer*! For a fixed value of $$B$$, there will be hence $$\left\lfloor \sqrt[6]{\frac N {B^4}} \right\rfloor $$ possible values for $$A$$ among $$1, 2, \dots, N$$. This yields a feasible formula for $$f(N)$$:

$$ f(N) = \sum_{i = 1}^N \mathbb I_{\mu(i) = 1} \left\lfloor \sqrt[6]{\frac N {i^4}} \right\rfloor =  \sum_{i = 1}^{\lfloor \sqrt[4] N \rfloor} \mathbb I_{\mu(i) = 1} \left\lfloor \sqrt[6]{\frac N {i^4}} \right\rfloor$$

The following piece of compact Julia code gives answer in a (somehow) reasonable time. The bottleneck here is the unnecessary computation of all of the values of the Möbius function.

{% highlight julia %}
n = 10^9
μ = ones(n)
result = floor(n^(2/3))
for i = 2:n
    if μ[i] == 1
        μ[i:i:n] *= -i
        μ[i*i:i*i:n] = 0
    end
    if # <REMOVED>
        result += floor((n/i)^(2/3))
    end
end
{% endhighlight %}
