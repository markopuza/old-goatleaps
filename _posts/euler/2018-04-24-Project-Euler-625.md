---
layout: post
title:  "Project Euler 625"
date:   2018-04-24\ 01:00:59 +0000
category-string: "Maths"
categories: euler maths
icon: euler625
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

### Gcd sum

The problem requires us to compute the double sum $$G(n) := \sum_{j=1}^n \sum_{i=1}^j gcd(i, j)$$. We need to find $$G(n)$$ for a large value $$n=10^{11}$$, so we better find a sublinear algorithm. We will start by trying to rewrite the sum into a more enlightening form.

Notice that we may rewrite the internal sum by equating the condition $$gcd(i, n) = e$$ with $$e \mid n;\ e \mid i;\ gcd(\frac i e, \frac n e) = 1$$ for any $$1 \leq i \leq n$$:

$$
\begin{align*}
\sum_{i=1}^n gcd(i, n) &= \sum_{e \mid n} \sum_{\substack{1 \leq i \leq n \\ gcd(i, n) = e}} e \\
&= \sum_{e \mid n} \sum_{\substack{1 \leq i \leq n \\ e \mid i;\ e \mid n\\gcd(\frac i e, \frac n e) = 1}} e \\
&= \sum_{e \mid n} e \sum_{\substack{1 \leq i \leq n \\ e \mid i;\ e \mid n\\gcd(\frac i e, \frac n e) = 1}} 1 \\
&= \sum_{e \mid n} e \phi\left(\frac n e\right)
\end{align*}
$$

Where $$\phi$$ is the Euler's totient function (Given $$n$$, counts the number of coprime integers $$1 \leq i \leq n$$ to $$n$$). The sum $$\sum_{i=1}^n gcd(i, n)$$ is by the way also known as the >>[Pillai's arithmetical function](https://en.wikipedia.org/wiki/Pillai%27s_arithmetical_function)<<. From here, we obtain $$G$$ being:

$$G(n) = \sum_{j=1}^n \sum_{e \mid j} e \phi\left(\frac j e\right)\ \ \ \ \ \ \ \ \ \ \ \ (1)$$

As for any positive numbers $$a, b$$ such that $$1 \leq ab \leq n$$, the term $$a \phi\left(b\right)$$ will appear exactly once in the summation (corresponding $$a = e;\ b = \frac j e$$), we may conveniently rewrite this sum as:

$$ \begin{align*}
G(n) &= \sum_{a=1}^n \sum_{b=1}^{\lfloor \frac n a \rfloor} a \phi(b)\\
&= \sum_{a=1}^n a \sum_{b=1}^{\lfloor \frac n a \rfloor} \phi(b)\\
&= \sum_{a=1}^n a \Phi\left(\left\lfloor \frac n a \right\rfloor\right)
\end{align*}$$

where we define $$\Phi(n)$$ to be the summatory function of the euler totients up to $$n$$:

$$ \Phi(n) := \sum_{i = 1}^n \phi(i)$$

As the next step in finding a sublinear algorithm we need to realize that there is only $$O(n^{0.5})$$ possible values $$x = \left\lfloor \frac n a \right\rfloor$$. Moreover, for any given value $$x$$, $$x = \left\lfloor \frac n a \right\rfloor$$ holds precisely with $$a$$'s for which $$\left\lfloor \frac n {x+1} \right\rfloor < a \leq \left\lfloor \frac n x \right\rfloor$$. Let $$S(n) := \sum_{i=1}^n i = \frac{n(n+1)}{2}$$ be the sum of the first $$n$$ natural numbers. We continue the derivation of $$G$$:

$$ \begin{align*}
G(n) &= \sum_{a=1}^n a \Phi\left(\left\lfloor \frac n a \right\rfloor\right)\\
&= \sum_x \sum_{a = \left\lfloor \frac n {x+1} \right\rfloor + 1}^{ \left\lfloor \frac n x \right\rfloor} \Phi(x)\\
&= \sum_x \Phi(x) \left(S\left(\left\lfloor \frac n {x} \right\rfloor\right) - S\left(\left\lfloor \frac n {x+1} \right\rfloor\right) \right)
\end{align*}$$

What are now the possible values of $$x$$? Well, defining $$u := \lfloor \sqrt n \rfloor$$ for clarity, any $$x > u$$ will appear in the summation exactly once, at $$x = \lfloor \frac n {a} \rfloor$$ for some $$a \leq u$$. Any $$x \leq u$$ will appear in the summation $$\left(S\left(\left\lfloor \frac n {x} \right\rfloor\right) - S\left(\left\lfloor \frac n {x+1} \right\rfloor\right) \right)$$ times. We thus divide our sum into two:

$$ \begin{align*}
G(n) &= \sum_{x \leq u} \Phi(x) \left(S\left(\left\lfloor \frac n {x} \right\rfloor\right) - S\left(\left\lfloor \frac n {x+1} \right\rfloor\right) \right) + \sum_{x > u} \Phi(x) \left(S\left(\left\lfloor \frac n {x} \right\rfloor\right) - S\left(\left\lfloor \frac n {x+1} \right\rfloor\right) \right) \\
&= \sum_{x \leq u} \Phi(x) \left(S\left(\left\lfloor \frac n {x} \right\rfloor\right) - S\left(\left\lfloor \frac n {x+1} \right\rfloor\right) \right) + \sum_{a \leq u} a \Phi\left(\left\lfloor \frac n {a} \right\rfloor\right) \ \ \ \ \ \ \ \ (2)
\end{align*}$$

Now, provided that we can compute $$\Phi$$, all is good - we only have $$O(n^{0.5})$$ summands. Cracking the problem now turns into the following goal:

> Find a sublinear way to compute $$\Phi$$.

For this we will actually use a similar trick as we did in the first time (>>[Dirichlet hyperbola method](http://planetmath.org/dirichlethyperbolamethod)<<). Recall from elementary number theory (or Wikipedia) that we can write $$n = \sum_{d\mid n} \phi(d)$$. We may trickily obtain a sum similar to (1):

$$ \left(\sum_{j=1}^n j =\right) S(n) = \sum_{j=1}^n \sum_{d\mid j} \phi(d) = \sum_{j=1}^n \sum_{d\mid j} \phi\left( \frac j d \right)$$

Analogously, for any positive numbers $$a, b$$ such that $$1 \leq ab \leq n$$, the term $$\phi\left(b\right)$$ will appear exactly once in the summation (corresponding $$a = d;\ b = \frac j d$$) and we conveniently rewrite:

$$\begin{align*}
 S(n) &= \sum_{a = 1}^n \sum_{b = 1}^{\lfloor \frac n a \rfloor} \phi(b) \\
  &= \sum_{a = 1}^n \Phi\left(\left \lfloor \frac n a \right \rfloor \right)\\
\Phi(n) &= S(n) - \sum_{1 < a \leq n} \Phi\left(\left \lfloor \frac n a \right \rfloor \right)
\end{align*}$$

Exposing again the fact that there are only $$O(n^{0.5})$$ possible values of $$\left \lfloor \frac n a \right \rfloor$$, in the exactly same way as we did to obtain (2), we find:

$$
\begin{align*}
  \sum_{1 < a \leq n} \Phi\left(\left \lfloor \frac n a \right \rfloor \right) = \sum_{1 < a \leq \lfloor \sqrt n \rfloor} \Phi\left(\left \lfloor \frac n a \right \rfloor \right) + \sum_{1 \leq x \leq \lfloor \sqrt n \rfloor} \left(\left\lfloor \frac n {x} \right\rfloor - \left\lfloor \frac n {x+1} \right\rfloor \right)\Phi\left(x \right)
\end{align*}
$$

And finally:

$$\Phi(n) = S(n) - \sum_{1 < a \leq \lfloor \sqrt n \rfloor} \Phi\left(\left \lfloor \frac n a \right \rfloor \right) - \sum_{1 \leq x \leq \lfloor \sqrt n \rfloor} \left(\left\lfloor \frac n {x} \right\rfloor - \left\lfloor \frac n {x+1} \right\rfloor \right)\Phi\left(x \right) \ \ \ \ \ \ \ (3)$$

Using the recurrence (3) to compute $$\Phi$$ will take $$O(n^{\frac 3 4})$$ time; with precomputing some number of the first values of $$\Phi$$ this can be made faster. The following Julia code gives answer in about 80 seconds.

{% highlight julia%}
using Nemo
R = ResidueRing(ZZ, 998244353)
n = 10^11

sqrtn = floor(Int, n^0.5)
precompute_bound = floor(Int, n^0.7)

# Sieves Euler's totient up to n
function phis(n)
    phis = collect(1:n)
    for p=2:2:n
        phis[p] >>= 1
    end
    for p=3:2:n
        if phis[p] == p
            phis[p] -= 1
            for j=2p:p:n
                phis[j] -= div(phis[j], p)
            end
        end
    end
    return phis
end

# Sum of the first n numbers
S(n) = n % 2 == 0 ? R(div(n, 2)) * R(n + 1) : R(n) * R(div(n+1, 2))

# firstΦs[i] = Φ(i)
println("Precomputing first Phis.")
@time firstΦs = map(x -> R(x), accumulate( #<REMOVED>

# secondΦs[i] = Φ(n//i)            Iteratively applies the recurrence (3)
println("Precomputing second Phis.")
secondΦs = [R(0) for i=1:div(n, precompute_bound)]
@time for j = div(n, precompute_bound):-1:1
    k = div(n, j)
    ksqrt = floor(Int, k^0.5)
    for i = ksqrt:-1:2
        if div(k, i) > precompute_bound
            secondΦs[j] -= secondΦs[div(n, div(k, i))]
        else
            secondΦs[j] -= firstΦs[div(k, i)]
        end
        #<REMOVED>
    end
    secondΦs[j] -= R(k - div(k, 2)) * firstΦs[1]
    if div(k,ksqrt) == ksqrt
        secondΦs[j] += firstΦs[ksqrt]
    end
    secondΦs[j] += #<REMOVED>
end

G(n) = #<REMOVED>

# Computing G(n)
println("Computing G(n)")
@time G(n)
{% endhighlight %}
