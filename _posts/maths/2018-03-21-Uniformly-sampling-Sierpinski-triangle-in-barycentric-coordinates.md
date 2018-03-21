---
layout: post
title:  "Sampling the Sierpiński triangle uniformly"
date:   2018-03-21 01:36:59 +0000
category-string: "Maths"
categories: maths tools
icon: siperpinskisampling
---

The other day, I found myself in a desperate need to sample uniformly from the Sierpiński triangle, but I couldn't find any standard way to do this. It turns out that one can do this in a straightforward manner using barycentric coordinates. Barycentric coordinates are a very curious topic by themselves; given a triangle $$ABC$$, we can specify any point $$p$$ on the plane with coordinates $$p \equiv (\lambda_1, \lambda_2, \lambda_3)$$, additionally constrained by $$\lambda_1 + \lambda_2 + \lambda_3 = 1 $$. This can be interpreted as "If we placed weight $$\lambda_1$$ into vertex $$A$$, weight $$\lambda_2$$ into vertex $$B$$ and weight $$\lambda_3$$ into vertex $$C$$, the centre of mass would be in $$p$$". We will only make use of a few facts holding in this coordinate system.


The Sierpiński triangle can be represented in barycentric coordinates as the set of points $$S := \{(u, v, w) = (0.u_1u_2u_3\dots,\  0.v_1v_2v_3\dots,\ 0.w_1w_2w_3\dots)\ \mid\ u_i + v_i + w_i = 1 \text{ for all } i\}$$ where each of the coordinates is written in __binary__ (The sum of the three coordinates is then obviously $$0.111\dots = 1$$, as expected.).  

We may easily sample from the Sierpiński triangle in this representation as follows (Clearly a uniform sampling, as every point is chosen equiprobably):

> For each $$i$$, flip a 3-sided fair "coin" to set $$(u_i, v_i, w_i)$$ to one of $$(1, 0, 0)$$, $$(0, 1, 0)$$ or $$(0, 0, 1)$$.

Once we have obtained $$(u, v, w)$$, we can readily convert to Cartesian coordinates using >>[standard formulae](https://en.wikipedia.org/wiki/Barycentric_coordinate_system#Conversion_between_barycentric_and_Cartesian_coordinates)<<. Let $$(x_A, y_A), (x_B, y_B), (x_C, y_C)$$ be the Cartesian coordinates of the vertices of the triangle we are computing barycentric coordinates with respect to. For an equilateral triangle (that is how the Sierpiński triangle is usually depicted), these will be $$(0, 0), (1, 0), \left(\frac 1 2, \frac {\sqrt{3}} 2\right)$$. Let $$prec$$ be our working precision (We will only approximate the points with $$prec$$ many binary digits). Then the sampling algorithm is:


- Generate $$(u, v, w) = (0.u_1u_2u_3\dots u_{prec},\  0.v_1v_2v_3\dots v_{prec},\ 0.w_1w_2w_3\dots w_{prec})$$ as described above.
- Convert binary $$(u, v, w)$$ to decimal $$(u', v', w')$$:

$$
\begin{align*}
  u' = \sum_{i = 1}^{prec} \frac {u_i}{2^i} && v' = \sum_{i = 1}^{prec} \frac {v_i}{2^i} && w' = \sum_{i = 1}^{prec} \frac {w_i}{2^i}
\end{align*}
$$

- By conversion formulate, the Cartesian coordinates of our sample will be:

$$
\begin{align*}
  x &= u' x_A + v' x_B + w' x_C = u' 0 + v' 1 + w' \frac 1 2 = v' + \frac {w'} 2 \\
   &= \sum_{i = 1}^{prec} \frac {v_i}{2^i} + \sum_{i = 1}^{prec} \frac {w_i}{2^{i+1}} =  \sum_{i = 1}^{prec} \left(v_i + \frac {w_i} 2\right) \frac 1 {2^i} \\
  y &= u' y_A + v' y_B + w' y_C = u' 0 + v' 0 + w' \frac {\sqrt{3}} 2 =  \frac {\sqrt{3} w'} 2 \\
   &= \frac {\sqrt 3} 2  \sum_{i = 1}^{prec} \frac {w_i} {2^i}
\end{align*}
$$

Quite remarkably, the whole sampling process boils down to a simple loop.

{% highlight python %}
from random import randint

def sample(precision=25):
    x = y = 0
    for i in range(1, precision):
        rand = randint(1, 3) # picking which coordinate gets 1
        v_i, w_i = int(rand==1), int(rand==2)

        x += (v_i + w_i/2) / (1 << i)
        y += w_i / (1 << i)
    return x, 3**0.5 * y / 2
{% endhighlight %}

You can try the sampling algorithm below:


<div class="row" style="width:75%;">
<div class="column"> <span> Number of samples: </span></div> <div class="column"><input id="samples" type="text" style="width:30%" value="25000"/> </div>
</div> <div class="row" style="width:75%;">
<div class="column"> <span> Point width (px): </span></div>  <div class="column"><input id="pxwidth" type="text" style="width:30%" value="1"/> </div>
<div class="column"> <span> Precision: </span></div>  <div class="column"><input id="precision" type="text" style="width:30%" value="25"/> </div>
</div>
<button type="button" onClick="runRho();" onClick="runSampling();"> Sample! </button>
<center>
<canvas id="canvas" style="width:70%;"></canvas>
</center>

<!--                    JAVASCRIPT                    -->

<script>
function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
}

function sample(precision=25) {
  var x = 0, y = 0;
  var rand, v_i, w_i;

  for (var i = 1; i <= precision; i++) {
    rand = getRndInteger(1, 3);
    v_i = 1.0 ? (rand == 1) : 0.0;
    w_i = 1.0 ? (rand == 2) : 0.0;

    x += (v_i + w_i / 2) / (1.0 << i);
    y += w_i / (1.0 << i);
  }
  return [x, y * Math.sqrt(3) / 2];
}

var canvas = document.getElementById('canvas');
canvas.width = canvas.clientWidth;
canvas.height =  canvas.clientWidth;

var margin = Math.round(canvas.width * 0.1);
var true_width = Math.round(canvas.width * 0.8);

var ctx = canvas.getContext("2d");
ctx.fillStyle="#000000";

function printSamples(samples=25000, pw=1, prec=25) {
  for (var i = 0; i <= samples; i++) {
    smp = sample(prec);
    ctx.fillRect(Math.round(margin + smp[0] * true_width), Math.round(canvas.width - margin - smp[1] * true_width), pw, pw);
  }
}

function runSampling() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  var samples = document.getElementById("samples").value;
  var pw = document.getElementById("pxwidth").value;
  var prec = document.getElementById("precision").value;
  printSamples(samples, pw, prec);
}

printSamples();
</script>
