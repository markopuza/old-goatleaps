---
layout: post
title:  "Facebook Hacker Cup 2018 - Qualification in Python"
date:   2018-07-06 01:38:59 +0000
category-string: "Programming"
categories: programming
icon: fb_hc2018_qual
---

The delayed Facebook Hacker Cup 2018 has finished recently with a set of problems that made one scratch their head. Below you can find brief solutions in Python that were fast enough to run on the given input files. The official problem statements/editorials can be found >>[here](https://www.facebook.com/notes/2249775598371662)<<.

# 1. Tourist
{% highlight python %}
for t in range(1, int(input())+1):
    n, k, v = map(int, input().split())
    l = list(zip(range(n), [input().strip() for _ in range(n)]))
    print('Case #{:d}: {:s}'.format(t,' '.join(map(lambda x: str(x[1]), sorted([l[((v-1)*k%n+i)%n] for i in range(k)])))))
{% endhighlight %}

# 2. Interception
{% highlight python %}
for t in range(1, int(input())+1):
    n = int(input())
    _ = [int(input()) for _ in range(n+1)]
    print('Case #{:d}: {:s}'.format(t, '1\n0.0' if (n&1) else '0'))
{% endhighlight %}

# 3. Ethan searches for a string
{% highlight python %}
for t in range(1, int(input())+1):
    s, ce = input().strip(), ''
    for i in range(1, len(s)-1):
        if s[i] == s[0] and not (s[:i] + s).startswith(s):
            ce = s[:i] + s; break
    print('Case #{:d}: {:s}'.format(t, 'Impossible' if len(ce)==0 else ce))
{% endhighlight %}
