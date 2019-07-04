---
layout: post
title:  "Newton flowers"
date:   2019-07-03 01:36:59 +0000
category-string: "Art"
categories: media maths programming tools
icon: newtonfractals
---


<script src="/assets/script/jscolor.min.js"></script>



<!-- Controls of the game -->

<style>
.slidecontainer {
    width: 100%;
}

.slider {
    -webkit-appearance: none;
    width: 100%;
    height: 8px;
    background: #d3d3d3;
    outline: none;
    opacity: 0.7;
    -webkit-transition: .2s;
    transition: opacity .2s;
}

.slider:hover {
    opacity: 1;
}

.slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 25px;
    height: 14px;
    background: #777;
    cursor: pointer;
}

.slider::-moz-range-thumb {
    width: 12px;
    height: 12px;
    background: #4CAF50;
    cursor: pointer;
}

.button {
    background-color: #e7e7e7;
    color: black;
    border: none;
    padding: 1px 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
  }

  #myProgress {
    width: 100%;
    background-color: #ddd;
  }

  #myBar {
    width: 1%;
    height: 30px;
    background-color: #4CAF50;
  }
</style>

The »[Newton fractal](https://en.wikipedia.org/wiki/Newton_fractal)« (flower) for a given complex function $$ f $$ is constructed by coloring each complex number $$ z $$ (or rather each point on a finite grid). We iteratively apply Newton's method to construct the sequence $$z_0 = z,\ z_1 = z_0 - \frac {f(z_0)} {f'(z_0)},\ \dots,\ z_k = z_{k-1} - \frac {f(z_{k-1})} {f'(z_{k-1})}, \ \dots $$. If we detect that the sequence converges after $$ n $$ terms (that is, if the difference between $$n$$-th and previous term is smaller than a fixed convergence threshold constant), we will paint the pixel corresponding to $$ z $$ according to $$red(n)$$, $$green(n)$$ and $$blue(n)$$. If the sequence does not converge after a fixed number of iterations, we deem it divergent and paint the pixel black. Note that if the sequence does converge, it is to some root of function $$ f $$.

The renderer implements two generalizations of »[Newton fractals](https://en.wikipedia.org/wiki/Newton_fractal)«.

### Nova fractals

The Newton method step $$ z_k = z_{k-1} - \frac {f(z_{k-1})} {f'(z_{k-1})} $$ in the above is substituted by a generalized

$$
z_k = z_{k-1} - a \frac {f(z_{k-1})} {f'(z_{k-1})} + c
$$

for some complex constants $$a, c$$.

### Repetitions
A new layer of complexity can be implanted into the fractal in the following way. Repeated a fixed amount of times, when we detect convergence at the term $$ z_n  $$, we simply restart the sequence by setting $$z_n = z - z_n$$ and continue with $$z_{n+1}$$ (restarting simultaneously the counter of the maximal number of iterations). The effects can be seen below, for repetitions set to 1 (usual Newton fractal), 2 and 5 respectively.

<div align="center">
<img src="/assets/image/newton_fractal_gallery/dem1.png" style="width:15%;">
<img src="/assets/image/newton_fractal_gallery/dem2.png" style="width:15%;">
<img src="/assets/image/newton_fractal_gallery/dem3.png" style="width:15%;">
</div>



#### Function and its derivative
##### Must be a JavaScript expression. Available complex functions: .add(), .sub(), .mul(), .div(), .pow(), .sin(), .cos(), .abs(), .tan()
##### Complex number must be entered as "new Complex(real, imag)".

<center>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:20%;"> f(z) = </div>
  <div class="column" style="font-weight:bold; width:75%;"> <input id="functionInput" type="text" style="width:100%" value="z.pow(3).mul(3).sub( z.pow(2).mul(2) ).add(z).sub(1)"/> </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:20%;"> f'(z) = </div>
  <div class="column" style="font-weight:bold; width:75%;"> <input id="derivativeInput" type="text" style="width:100%" value="z.pow(2).mul(9).sub( z.mul(4) ).add(1)"/> </div>
</div>
</center>


#### Parameters for the Newton's method
##### Sets parameters a, c for the modified Newton's method. Increase repetitions for added complexity.
<center>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:20%;"> a = </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="aInput" type="text" style="width:100%" value="new Complex(1, 0)"/> </div>

  <div class="column" style="font-weight:bold; width:20%;"> c = </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="cInput" type="text" style="width:100%" value="new Complex(0, 0)"/> </div>
</div>

<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:20%;"> Repetitions </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="repInput" type="text" style="width:100%" value="2"/> </div>

  <div class="column" style="font-weight:bold; width:20%;"> Maximum iterations </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="maxIterInput" type="text" style="width:100%" value="32"/> </div>

  <div class="column" style="font-weight:bold; width:20%;"> Convergence threshold = </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="thresInput" type="text" style="width:100%" value="0.0001"/> </div>
</div>
</center>

#### The color scheme
##### Sets the color for a point as a function of n, the number of iterations until convergence. Needs to be a JavaScrip expression.

<center>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:20%;"> Red(n) = </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="redInput" type="text" style="width:100%" value="3*n"/> </div>

  <div class="column" style="font-weight:bold; width:20%;"> Green(n) = </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="greenInput" type="text" style="width:100%" value="2*n"/> </div>

  <div class="column" style="font-weight:bold; width:20%;"> Blue(n) = </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="blueInput" type="text" style="width:100%" value="4*n"/> </div>
</div>
</center>

#### Display window and resolution
##### Sets the part of complex plane to be displayed and the number of pixels. More pixels will cause slower rendering.

<center>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:20%;"> Bottom </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="bottomInput" type="text" style="width:100%" value="-1"/> </div>

  <div class="column" style="font-weight:bold; width:20%;"> Top </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="topInput" type="text" style="width:100%" value="1"/> </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:20%;"> Left </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="leftInput" type="text" style="width:100%" value="-1"/> </div>

  <div class="column" style="font-weight:bold; width:20%;"> Right </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="rightInput" type="text" style="width:100%" value="1"/> </div>

  <div class="column" style="font-weight:bold; width:20%;"> Pixels </div>
  <div class="column" style="font-weight:bold; width:10%;"> <input id="pixelsInput" type="text" style="width:100%" value="300"/> </div>
</div>

<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:100%;"> </div>
</div>

<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:100%;"> <button type="button" style="width:50%; font-weight:bold;  font-size: 16px;" onClick="parseAndPaint();"> Paint! </button> </div>
</div>

<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:100%;"> </div>
</div>

<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:100%;"> </div>
</div>
</center>


##### Controls: left-click on canvas to *zoom*, right-click to *unzoom*. Click on the below arrows for *shift*.

<button onclick="move('left')" class="button"> &larr; </button>
<button onclick="move('right')" class="button"> &rarr; </button>
<button onclick="move('up');" class="button"> &uarr; </button>
<button onclick="move('down');" class="button"> &darr; </button>

<center>  
  <canvas id="canvas" style="width:90%;"></canvas>
</center>


## Gallery
##### Click on image to render the fractal.


<div align="center">
<img src="/assets/image/newton_fractal_gallery/1.png" style="width:23%;" onclick="loadSettings(1);">
<img src="/assets/image/newton_fractal_gallery/2.png" style="width:23%;" onclick="loadSettings(2);">
<img src="/assets/image/newton_fractal_gallery/3.png" style="width:23%;" onclick="loadSettings(3);">
<img src="/assets/image/newton_fractal_gallery/4.png" style="width:23%;" onclick="loadSettings(4);">
</div>

<div align="center" style="padding-top: 5px;">
<img src="/assets/image/newton_fractal_gallery/5.png" style="width:23%;" onclick="loadSettings(5);">
<img src="/assets/image/newton_fractal_gallery/6.png" style="width:23%;" onclick="loadSettings(6);">
<img src="/assets/image/newton_fractal_gallery/7.png" style="width:23%;" onclick="loadSettings(7);">
<img src="/assets/image/newton_fractal_gallery/8.png" style="width:23%;" onclick="loadSettings(8);">
</div>

<div align="center" style="padding-top: 5px;">
<img src="/assets/image/newton_fractal_gallery/9.png" style="width:23%;" onclick="loadSettings(9);">
<img src="/assets/image/newton_fractal_gallery/10.png" style="width:23%;" onclick="loadSettings(10);">
<img src="/assets/image/newton_fractal_gallery/11.png" style="width:23%;" onclick="loadSettings(11);">
<img src="/assets/image/newton_fractal_gallery/12.png" style="width:23%;" onclick="loadSettings(12);">
</div>

<!-- Javascript -->


<script>
function Complex(r, i) {
        this.r = r;
        this.i = i;
    }
    Complex.prototype.add = function(other) {
      if (typeof(other) == "number") {
        return new Complex(this.r + other, this.i);
      }

      return new Complex(this.r + other.r, this.i + other.i);
    }
    Complex.prototype.sub = function(other) {
      if (typeof(other) == "number") {
        return new Complex(this.r - other, this.i);
      }

        return new Complex(this.r - other.r, this.i - other.i);
    }
    Complex.prototype.mul = function(other) {
      if (typeof(other) == "number") {
        return new Complex(this.r * other, this.i*other);
      }
      return new Complex(this.r * other.r - this.i * other.i,
                     this.i * other.r + this.r * other.i);
    }
    Complex.prototype.div = function(other) {
      if (typeof(other) == "number") {
        return new Complex(this.r / other, this.i / other);
      }

        var denominator = other.r * other.r + other.i * other.i;
        return new Complex((this.r * other.r + this.i * other.i) / denominator,
                       (this.i * other.r - this.r * other.i) / denominator);
    }
    Complex.prototype.abs = function() {
        return Math.sqrt(this.r * this.r + this.i * this.i);
    }
    Complex.prototype.cos = function() {
      return new Complex(Math.cos(this.r) * Math.cosh(this.i), -Math.sin(this.r) * Math.sinh(this.i) );
    }
    Complex.prototype.sin = function() {
      return new Complex(Math.sin(this.r) * Math.cosh(this.i), Math.sinh(this.i) * Math.cos(this.r) );
    }
    Complex.prototype.tan = function() {
      return this.sin().div(this.cos());
    }
    Complex.prototype.pow = function(exp) {
      if (exp == 0) {
        return new Complex(1, 0);
      }
      if (exp == 1) {
        return new Complex(this.r, this.i);
      }

      var p = this.pow(Math.floor(exp/2));
      if (exp % 2 == 0) {
        return p.mul(p);
      }
      else {
        return p.mul(p).mul(this);
      }
    }
</script>


<script>
  var canvas = document.getElementById('canvas');
  canvas.width = canvas.clientWidth;
  canvas.height =  canvas.clientWidth;
  canvas.addEventListener('click', zoom );
  canvas.addEventListener('contextmenu', unzoom );
  var requestId;
  var runID;

  var ctx = canvas.getContext("2d");
  var clr = "rgb(155, 102, 102)";
  ctx.fillStyle = clr;

  function newton(z, f, f_der, maxIter=32, howClose=0.00001, a=1, c=0) {
      var old = new Complex(1000000, 1000000);
      var curr = z;

      for (var iters=0; iters < maxIter; iters++) {
        if (curr.sub(old).abs() < howClose) {
          return [iters, curr];
        }

        old = curr;
        curr = curr.sub(f(curr).div(f_der(curr)).mul(a)).add(c);
      }
      return [0, curr];
  }

  function replicateNewton(z, f, f_der, rep=3, maxIter=32, howClose=0.00001, a=1, c=0) {
    var n = 0;
    var curr = z;

    for (var i = 0; i < rep; i++) {
      var nw = newton(curr, f, f_der, maxIter, howClose, a, c);
      n += nw[0];
      curr = nw[1].sub(curr);
    }
    return n;
  }



  function paintFractal(f, f_der, reps, maxIter, howClose, a, c, pixels, left, right, top, bottom, colorScheme) {
    canvas.width = pixels;
    canvas.height = pixels;
    var dx = (right - left) / pixels;
    var dy = (top - bottom) / pixels;

      for (var i = 0; i < pixels; i++) {
        for (var j = 0; j < pixels; j++) {
          var n = replicateNewton( new Complex(left + i*dx, top - j*dy), f, f_der, reps, maxIter, howClose, a, c);

          ctx.fillStyle = colorScheme( n );
          ctx.fillRect(i, j, 1, 1);
        }
      }
  }

  function zoom(event) {
    var x = event.offsetX / event.srcElement.clientWidth;
    var y = event.offsetY / event.srcElement.clientWidth;

    var left = parseFloat(document.getElementById("leftInput").value);
    var right = parseFloat(document.getElementById("rightInput").value);
    var top = parseFloat(document.getElementById("topInput").value);
    var bottom = parseFloat(document.getElementById("bottomInput").value);

    var scalex = right - left;
    var scaley = top - bottom;

    var cx = right * x + left * (1.0 - x);
    var cy = bottom * y + top * (1.0 - y);

    document.getElementById("leftInput").value = cx - scalex * 0.42;
    document.getElementById("rightInput").value = cx + scalex * 0.42;
    document.getElementById("topInput").value = cy + scaley * 0.42;
    document.getElementById("bottomInput").value = cy - scaley * 0.42;

    parseAndPaint();
  }

  function unzoom(event) {
    var x = event.offsetX / event.srcElement.clientWidth;
    var y = event.offsetY / event.srcElement.clientWidth;
    event.preventDefault();

    var left = parseFloat(document.getElementById("leftInput").value);
    var right = parseFloat(document.getElementById("rightInput").value);
    var top = parseFloat(document.getElementById("topInput").value);
    var bottom = parseFloat(document.getElementById("bottomInput").value);

    var scalex = right - left;
    var scaley = top - bottom;


    var cx = right * x + left * (1.0 - x);
    var cy = bottom * y + top * (1.0 - y);

    document.getElementById("leftInput").value = cx - scalex * 0.58;
    document.getElementById("rightInput").value = cx + scalex * 0.58;
    document.getElementById("topInput").value = cy + scaley * 0.58;
    document.getElementById("bottomInput").value = cy - scaley * 0.58;

    parseAndPaint();

  }

  function move(dir) {    
    var left = parseFloat(document.getElementById("leftInput").value);
    var right = parseFloat(document.getElementById("rightInput").value);
    var top = parseFloat(document.getElementById("topInput").value);
    var bottom = parseFloat(document.getElementById("bottomInput").value);

    var scalex = right - left;
    var scaley = top - bottom;

    if (dir == "left") {
      document.getElementById("leftInput").value = left + scalex*0.15;
      document.getElementById("rightInput").value = right + scalex*0.15;
    }
    if (dir == "right") {
      document.getElementById("leftInput").value = left - scalex*0.15;
      document.getElementById("rightInput").value = right - scalex*0.15;
    }
    if (dir == "down") {
      document.getElementById("topInput").value = top + scaley*0.15;
      document.getElementById("bottomInput").value = bottom + scaley*0.15;
    }
    if (dir == "up") {
      document.getElementById("topInput").value = top - scaley*0.15;
      document.getElementById("bottomInput").value = bottom - scaley*0.15;
    }

    parseAndPaint();
  }

  function parseAndPaint() {
    var f = eval("z => " + document.getElementById("functionInput").value);
    var f_der = eval("z => " + document.getElementById("derivativeInput").value);

    var a = eval(document.getElementById("aInput").value);
    var c = eval(document.getElementById("cInput").value);

    var reps = parseInt(document.getElementById("repInput").value);
    var maxIter = parseInt(document.getElementById("maxIterInput").value);
    var howClose = parseFloat(document.getElementById("thresInput").value);

    var red = eval("n => " + document.getElementById("redInput").value);
    var green = eval("n => " + document.getElementById("greenInput").value);
    var blue = eval("n => " + document.getElementById("blueInput").value);

    function colorScheme(n) {
      return "rgb(" + red(n).toString() + ", " + green(n).toString() + ", " + blue(n).toString() + ")";
    }

    var pixels = parseInt(document.getElementById("pixelsInput").value);
    var left = parseFloat(document.getElementById("leftInput").value);
    var right = parseFloat(document.getElementById("rightInput").value);
    var top = parseFloat(document.getElementById("topInput").value);
    var bottom = parseFloat(document.getElementById("bottomInput").value);




    runID = 4;
    requestId = undefined;
    var p = [parseInt(pixels), parseInt(pixels/3), parseInt(pixels/8), parseInt(pixels/16), parseInt(pixels/32)]
    function animate() {
        if (runID >= 0) {
            paintFractal(f, f_der, reps, maxIter, howClose, a, c, p[runID], left, right, top, bottom, colorScheme);
            runID--;
            requestId = requestAnimationFrame(animate);
        }
    }
    animate();
  }

  function loadSettings(n) {
    if (n == 1) {
      document.getElementById("functionInput").value = "z.pow(3).sub(1).sin()";
      document.getElementById("derivativeInput").value = "z.pow(3).sub(1).cos().mul(z.pow(2)).mul(2)";
      document.getElementById("repInput").value = "3";
      document.getElementById("maxIterInput").value = "32";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(1, 0)";
      document.getElementById("cInput").value = "new Complex(0, 0)";
      document.getElementById("redInput").value = "4*n";
      document.getElementById("greenInput").value = "n/3";
      document.getElementById("blueInput").value = "(n*n)%100";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-1.3";
      document.getElementById("rightInput").value = "1.3";
      document.getElementById("topInput").value = "1.3";
      document.getElementById("bottomInput").value = "-1.3";
    }
    if (n == 2) {
      document.getElementById("functionInput").value = "z.pow(4).sub( new Complex(0, 1) )";
      document.getElementById("derivativeInput").value = "z.pow(3).mul(4)";
      document.getElementById("repInput").value = "2";
      document.getElementById("maxIterInput").value = "32";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(1, 0)";
      document.getElementById("cInput").value = "new Complex(0, 0)";
      document.getElementById("redInput").value = "Math.sin(n) * 166";
      document.getElementById("greenInput").value = "n*n/15";
      document.getElementById("blueInput").value = "(n*n*n)%100";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-0.13";
      document.getElementById("rightInput").value = "0.13";
      document.getElementById("topInput").value = "0.13";
      document.getElementById("bottomInput").value = "-0.13";
    }
    if (n == 3) {
      document.getElementById("functionInput").value = "z.pow(3).mul(3).sub( z.pow(2).mul(2) ).add(z).sub(1)";
      document.getElementById("derivativeInput").value = "z.pow(2).mul(9).sub( z.mul(4) ).add(1)";
      document.getElementById("repInput").value = "2";
      document.getElementById("maxIterInput").value = "32";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(1, 0)";
      document.getElementById("cInput").value = "new Complex(0, 0)";
      document.getElementById("redInput").value = "3*n";
      document.getElementById("greenInput").value = "3*n";
      document.getElementById("blueInput").value = "8*n";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-1";
      document.getElementById("rightInput").value = "1";
      document.getElementById("topInput").value = "1";
      document.getElementById("bottomInput").value = "-1";
    }
    if (n == 4) {
      document.getElementById("functionInput").value = "z.sin().cos()";
      document.getElementById("derivativeInput").value = "z.sin().sin().mul(-1).mul(z.cos())";
      document.getElementById("repInput").value = "1";
      document.getElementById("maxIterInput").value = "32";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(1, 0)";
      document.getElementById("cInput").value = "new Complex(0, 0)";
      document.getElementById("redInput").value = "n+10";
      document.getElementById("greenInput").value = "n*n";
      document.getElementById("blueInput").value = "2*n*n";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-1.5";
      document.getElementById("rightInput").value = "1.5";
      document.getElementById("topInput").value = "1.5";
      document.getElementById("bottomInput").value = "-1.5";
    }
    if (n == 5) {
      document.getElementById("functionInput").value = "z.pow(4).sub( new Complex(0, 1) )";
      document.getElementById("derivativeInput").value = "z.pow(3).mul(4)";
      document.getElementById("repInput").value = "2";
      document.getElementById("maxIterInput").value = "32";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(1, 0)";
      document.getElementById("cInput").value = "new Complex(0, 0)";
      document.getElementById("redInput").value = "(n*n*n)%300";
      document.getElementById("greenInput").value = "(n*n*n)%200";
      document.getElementById("blueInput").value = "(n*n*n)%100";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "1.1";
      document.getElementById("rightInput").value = "1.7";
      document.getElementById("topInput").value = "1.7";
      document.getElementById("bottomInput").value = "1.1";
    }
    if (n == 6) {
      document.getElementById("functionInput").value = "z.pow(4).sub(1).div(z.pow(3))";
      document.getElementById("derivativeInput").value = "(new Complex(1, 0)).add( (new Complex(3, 0)).div(z.pow(4)) )";
      document.getElementById("repInput").value = "4";
      document.getElementById("maxIterInput").value = "2000";
      document.getElementById("thresInput").value = "0.00001";
      document.getElementById("aInput").value = "new Complex(1, 0)";
      document.getElementById("cInput").value = "new Complex(0, 0)";
      document.getElementById("redInput").value = "n/3";
      document.getElementById("greenInput").value = "1.8*n";
      document.getElementById("blueInput").value = "n/3";
      document.getElementById("pixelsInput").value = "200";
      document.getElementById("leftInput").value = "-10";
      document.getElementById("rightInput").value = "10";
      document.getElementById("topInput").value = "10";
      document.getElementById("bottomInput").value = "-10";
    }
    if (n == 7) {
      document.getElementById("functionInput").value = "z.pow(4).sub( new Complex(0, 1) )";
      document.getElementById("derivativeInput").value = "z.pow(3).mul(4)";
      document.getElementById("repInput").value = "2";
      document.getElementById("maxIterInput").value = "80";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(1, 0)";
      document.getElementById("cInput").value = "new Complex(0, 0)";
      document.getElementById("redInput").value = "Math.sin(n) * 200";
      document.getElementById("greenInput").value = "n*n/60";
      document.getElementById("blueInput").value = "(n*n*n)%166";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-200";
      document.getElementById("rightInput").value = "200";
      document.getElementById("topInput").value = "200";
      document.getElementById("bottomInput").value = "-200";
    }
    if (n == 8) {
      document.getElementById("functionInput").value = "z.pow(3).mul(3).sub( z.pow(2).mul(2) ).add(z).sub(1)";
      document.getElementById("derivativeInput").value = "z.pow(2).mul(9).sub( z.mul(4) ).add(1)";
      document.getElementById("repInput").value = "2";
      document.getElementById("maxIterInput").value = "100";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(0.3, 0.3)";
      document.getElementById("cInput").value = "new Complex(0, 0.1)";
      document.getElementById("redInput").value = "2*n";
      document.getElementById("greenInput").value = "2*n";
      document.getElementById("blueInput").value = "6*n";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-5.100622176183018";
      document.getElementById("rightInput").value = "6.171363207760363";
      document.getElementById("topInput").value = "5.74633687262087";
      document.getElementById("bottomInput").value = "-5.525648511322518";
    }
    if (n == 9) {
      document.getElementById("functionInput").value = "z.pow(2).add(1)";
      document.getElementById("derivativeInput").value = "z.mul(2)";
      document.getElementById("repInput").value = "2";
      document.getElementById("maxIterInput").value = "100";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(0.3, 0.3)";
      document.getElementById("cInput").value = "new Complex(0, 0)";
      document.getElementById("redInput").value = "n*n % 200";
      document.getElementById("greenInput").value = "2*n";
      document.getElementById("blueInput").value = "6*n";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-2.767529970069603";
      document.getElementById("rightInput").value = "2.93478517509781";
      document.getElementById("topInput").value = "2.958975419263552  ";
      document.getElementById("bottomInput").value = "-2.743339725903866";
    }
    if (n == 10) {
      document.getElementById("functionInput").value = "z.sin()";
      document.getElementById("derivativeInput").value = "z.cos()";
      document.getElementById("repInput").value = "3";
      document.getElementById("maxIterInput").value = "32";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(1, 0.2)";
      document.getElementById("cInput").value = "new Complex(0, 0.5)";
      document.getElementById("redInput").value = "n*n*n % 200";
      document.getElementById("greenInput").value = "n*n*n % 200";
      document.getElementById("blueInput").value = "n*n*n % 200";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-2.743803714157303";
      document.getElementById("rightInput").value = "2.6881143658426954";
      document.getElementById("topInput").value = "2.8546234894382017";
      document.getElementById("bottomInput").value = "-2.5772945905617966";
    }
    if (n == 11) {
      document.getElementById("functionInput").value = "z.pow(4).sub( new Complex(0, 2) )";
      document.getElementById("derivativeInput").value = "z.pow(3).mul(4)";
      document.getElementById("repInput").value = "1";
      document.getElementById("maxIterInput").value = "50";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(1, 0)";
      document.getElementById("cInput").value = "new Complex(0, 0.2)";
      document.getElementById("redInput").value = "n*n*n % 100";
      document.getElementById("greenInput").value = "n*n*n % 200";
      document.getElementById("blueInput").value = "n*n*n % 300";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-1.588089440048043";
      document.getElementById("rightInput").value = "0.11510732109716881";
      document.getElementById("topInput").value = "-1.5795355892164056";
      document.getElementById("bottomInput").value = "-3.2827323503616173";
    }
    if (n == 12) {
      document.getElementById("functionInput").value = "z.pow(8).add(z.pow(4).mul(15)).add(-16)";
      document.getElementById("derivativeInput").value = "z.pow(7).mul(8).add(z.pow(3).mul(60))";
      document.getElementById("repInput").value = "2";
      document.getElementById("maxIterInput").value = "120";
      document.getElementById("thresInput").value = "0.0001";
      document.getElementById("aInput").value = "new Complex(1, 0)";
      document.getElementById("cInput").value = "new Complex(0, 0)";
      document.getElementById("redInput").value = "n";
      document.getElementById("greenInput").value = "6*n";
      document.getElementById("blueInput").value = "n*n*n % 300";
      document.getElementById("pixelsInput").value = "300";
      document.getElementById("leftInput").value = "-4.325634514452922";
      document.getElementById("rightInput").value = "4.540499054487089";
      document.getElementById("topInput").value = "4.386394755948951";
      document.getElementById("bottomInput").value = "-4.4797388129910605";
    }


    parseAndPaint();
  }

  function stopAnimation() {
    if (requestId) {
       window.cancelAnimationFrame(requestId);
       requestId = undefined;
    }
  }


  var link = document.createElement('a');

  var cnter = 0;
  var download = function() {
    cnter += 1;
    link.download = cnter.toString();
    link.href = document.getElementById('canvas').toDataURL();
    link.click();

    document.getElementById("leftInput").value = (parseFloat(document.getElementById("leftInput").value) * 0.95).toString();
    document.getElementById("rightInput").value = (parseFloat(document.getElementById("rightInput").value) * 0.95).toString();
    document.getElementById("topInput").value = (parseFloat(document.getElementById("topInput").value) * 0.95).toString();
    document.getElementById("bottomInput").value = (parseFloat(document.getElementById("bottomInput").value) * 0.95).toString();
    parseAndPaint();
  }

  loadSettings(4);

</script>
