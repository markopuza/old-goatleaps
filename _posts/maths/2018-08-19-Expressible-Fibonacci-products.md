---
layout: post
title:  "Positive numbers expressible as a product of Fibonacci numbers"
date:   2018-08-19 01:36:59 +0000
category-string: "Maths"
categories: programming maths
icon: fibonacciproducts
---

While participating in this year's annual >>[GSA Ultra](https://www.gsa-ultra.com/)<< Python competition for UK university students, I grew fond of one particular little problem about prime-like "factorisation into Fibonacci numbers". Even though the problem statement evokes nothing but complications (at least to me):

> Given a positive integer $$n$$, decide whether it is expressible as a product of Fibonacci numbers. That is:
>
> $$n \stackrel{?}{=} \prod_{i = 1}^k f_i^{p_i} \text{ with } f_i \text{ distinct Fibonacci numbers and all } p_i > 0.$$

it turns out to have a very straightforward solution. The numbers expressible as a product of Fibonacci numbers are known and even have their own >>[OEIS sequence](https://oeis.org/A065108)<<, which however does not explain how to find out whether a given number if expressible in this form. The answer is the following procedure which only takes $$\mathcal O(\log n)$$ time:

- Let $$f_1, f_2, \dots, f_k$$ be the finite sequence of Fibonacci numbers smaller or equal to $$n$$, in **decreasing order**, **except 8 and 144**.
- For each $$f_i$$ in this order, divide $$n$$ by $$f_i$$ as many times as possible.
- If the number remaining in the end is $$1$$, $$n$$ is expressible as a product of Fibonacci numbers, otherwise it is not.

*Proof.*
If the remaining number is $$1$$, we have just expressed $$n$$ as a product of Fibonacci numbers. Conversely, assume $$n$$ is expressible as some product of Fibonacci numbers. First off, we substitute any appearance of $$8$$ and $$144$$ in the product for $$2 \cdot 2 \cdot 2$$ and $$2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3$$ respectively. Let $$f_1$$ be the largest Fibonacci number in the product. By **>>[Carmichael's theorem](https://en.wikipedia.org/wiki/Carmichael%27s_theorem)<<**, there exists a prime $$p_1$$ which divides both $$n$$ and $$f_1$$ but none of the other Fibonacci numbers in the product. The number of $$f_1$$ 's in the product must be then equal to the exponent $$e_1$$ of $$p_1$$ in prime factorisation of $$n$$, which is also the "maximal number of times that $$f_1$$ divides $$n$$". Similarly, $$f_2$$ (the second largest Fibonacci number in the product) appears in the product $$e_2$$ times, which is the "maximal number of times that $$f_2$$ divides $$\frac n {f_1^{e_1}}$$". Continuing, the number that remains at the end of the procedure will be $$\frac {n} {f_1^{e_1} f_2^{e_2} \cdots f_k^{e_k}} = 1$$.

A code snippet that does the job is below. It gives the answer instantly for numbers as big as Python's arithmetic allows.
{% highlight python %}
def expressible(n):
    fib, current = [2, 3], n
    while fib[-1] <= n:
        fib.append(sum(fib[-2:]))
    for f in fib[::-1]:
        if f != 8 and f != 144:
            while current%f == 0:
                current //= f
    return current == 1
{% endhighlight %}
