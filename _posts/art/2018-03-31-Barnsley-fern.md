---
layout: post
title:  "Barnsley's fern"
date:   2018-03-31 01:36:59 +0000
category-string: "Art"
categories: media maths programming tools
icon: fern
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
</style>


Starting with $$x = y = 0$$, at each iteration, we perform the transformation:

$$ (x, y) \mapsto \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} + \begin{pmatrix} e \\ f \end{pmatrix}$$

where the values $$a, b, c, d, e, f$$ are chosen from the following rows, with each row having its relative probability (the last column) of being chosen. That is the whole iterative process of creating the >>[Barnsley's fern](https://en.wikipedia.org/wiki/Barnsley_fern)<< fractal. Depending on how the parameters $$a,b,c,d,e,f$$ and the probabilities are chosen, one can end up with biologically convincing genera of ferns (check the presets below), as well as more abstract fractals. For more information, see the amazing book >>[Fractals Everywhere](https://www.amazon.co.uk/Fractals-Everywhere-Prof-Michael-Barnsley/dp/0120790610)<< by Prof. Michael Barnsley.

### Can you create your own cool fern?

<!-- Canvas -->



<center>  
  <canvas id="canvas" style="width:70%;"></canvas>
</center>

<!-- Controls -->
<button onclick="ctx.translate(-canvas.width/50, 0); draw_fern();" class="button"> &larr; </button>
<button onclick="ctx.translate(canvas.width/50, 0); draw_fern();" class="button"> &rarr; </button>
<button onclick="ctx.translate(0, -canvas.width/50); draw_fern();" class="button"> &uarr; </button>
<button onclick="ctx.translate(0, canvas.width/50); draw_fern();" class="button"> &darr; </button>


<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:12%;"> </div>
  <div class="column" style="font-weight:bold; width:12%;"> a </div>
  <div class="column" style="font-weight:bold; width:12%;"> b </div>
  <div class="column" style="font-weight:bold; width:12%;"> c </div>
  <div class="column" style="font-weight:bold; width:12%;"> d </div>
  <div class="column" style="font-weight:bold; width:12%;"> e </div>
  <div class="column" style="font-weight:bold; width:12%;"> f </div>
  <div class="column" style="font-weight:bold; width:12%;"> Relative probability </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:12%;"> Stem </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="a1" style="width:90%" value="0.0"/> </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="b1" style="width:90%" value="0.0"/> </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="c1"  style="width:90%" value="0.0"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="d1"  style="width:90%" value="0.16"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="e1"  style="width:90%" value="0.0"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="f1"  style="width:90%" value="0.0"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="0.0" max="2.0" id="p1"  style="width:90%" value="0.01"/>  </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" align="center" style="margin-top: -5px; width:12%;">  </div>
  <div class="column" align="center" id="a1o" style="margin-top: -5px; width:12%;"> 0.00 </div>
  <div class="column" align="center" id="b1o" style="margin-top: -5px; width:12%;"> 0.00 </div>
  <div class="column" align="center" id="c1o" style="margin-top: -5px; width:12%;"> 0.00 </div>
  <div class="column" align="center" id="d1o" style="margin-top: -5px; width:12%;"> 0.16 </div>
  <div class="column" align="center" id="e1o" style="margin-top: -5px; width:12%;"> 0.00 </div>
  <div class="column" align="center" id="f1o" style="margin-top: -5px; width:12%;"> 0.00 </div>
  <div class="column" align="center" id="p1o" style="margin-top: -5px; width:12%;"> 0.01 </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:12%;"> Leaflets </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="a2"  style="width:90%" value="0.85"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="b2"  style="width:90%" value="0.04"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="c2"  style="width:90%" value="-0.04"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="d2"  style="width:90%" value="0.85"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="e2"  style="width:90%" value="0.0"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="f2"  style="width:90%" value="1.60"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="0.0" max="2.0" id="p2"  style="width:90%" value="0.85"/> </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" align="center" style="margin-top: -5px; width:12%;">  </div>
  <div class="column" align="center" id="a2o" style="margin-top: -5px; width:12%;"> 0.85 </div>
  <div class="column" align="center" id="b2o" style="margin-top: -5px; width:12%;"> 0.04 </div>
  <div class="column" align="center" id="c2o" style="margin-top: -5px; width:12%;"> -0.04 </div>
  <div class="column" align="center" id="d2o" style="margin-top: -5px; width:12%;"> 0.85 </div>
  <div class="column" align="center" id="e2o" style="margin-top: -5px; width:12%;"> 0.00 </div>
  <div class="column" align="center" id="f2o" style="margin-top: -5px; width:12%;"> 1.60 </div>
  <div class="column" align="center" id="p2o" style="margin-top: -5px; width:12%;"> 0.85 </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:12%;"> Big left-leaflet </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="a3"  style="width:90%" value="0.20"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="b3"  style="width:90%" value="-0.26"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="c3"  style="width:90%" value="0.23"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="d3"  style="width:90%" value="0.22"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="e3"  style="width:90%" value="0.0"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="f3"  style="width:90%" value="1.60"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="0.0" max="2.0" id="p3"  style="width:90%" value="0.07"/>  </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" align="center" style="margin-top: -5px; width:12%;">  </div>
  <div class="column" align="center" id="a3o" style="margin-top: -5px; width:12%;"> 0.20 </div>
  <div class="column" align="center" id="b3o" style="margin-top: -5px; width:12%;"> -0.26 </div>
  <div class="column" align="center" id="c3o" style="margin-top: -5px; width:12%;"> 0.23 </div>
  <div class="column" align="center" id="d3o" style="margin-top: -5px; width:12%;"> 0.22 </div>
  <div class="column" align="center" id="e3o" style="margin-top: -5px; width:12%;"> 0.00 </div>
  <div class="column" align="center" id="f3o" style="margin-top: -5px; width:12%;"> 1.60 </div>
  <div class="column" align="center" id="p3o" style="margin-top: -5px; width:12%;"> 0.07 </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" style="font-weight:bold; width:12%;"> Big right-leaflet </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="a4"  style="width:90%" value="-0.15"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="b4"  style="width:90%" value="0.28"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="c4"  style="width:90%" value="0.26"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="d4"  style="width:90%" value="0.24"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="e4"  style="width:90%" value="0.0"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="-2.0" max="2.0" id="f4"  style="width:90%" value="0.44"/>  </div>
  <div class="column" style="font-weight:bold; width:12%;">  <input type="range" class="slider" oninput="update_captions()"  step="0.01" min="0.0" max="2.0" id="p4"  style="width:90%" value="0.07"/> </div>
</div>
<div class="row" style="width:100%;">
  <div class="column" align="center" style="margin-top: -5px; width:12%;">  </div>
  <div class="column" align="center" id="a4o" style="margin-top: -5px; width:12%;"> -0.15 </div>
  <div class="column" align="center" id="b4o" style="margin-top: -5px; width:12%;"> 0.28 </div>
  <div class="column" align="center" id="c4o" style="margin-top: -5px; width:12%;"> 0.26 </div>
  <div class="column" align="center" id="d4o" style="margin-top: -5px; width:12%;"> 0.24 </div>
  <div class="column" align="center" id="e4o" style="margin-top: -5px; width:12%;"> 0.00 </div>
  <div class="column" align="center" id="f4o" style="margin-top: -5px; width:12%;"> 0.44 </div>
  <div class="column" align="center" id="p4o" style="margin-top: -5px; width:12%;"> 0.07 </div>
</div>

<div class="row">
  <div class="column" style="width:12%; font-weight:bold;"> Presets: </div>
  <div class="column" style="width:12%" align="center"> <a onclick="set_preset('barnsley')"> »Barnsley«</a> </div>
  <div class="column" style="width:12%" align="center"> <a onclick="set_preset('barnsley2')"> »Barnsley 2«</a> </div>
  <div class="column" style="width:12%" align="center"> <a onclick="set_preset('cyclosorus')"> »Cyclosorus«</a> </div>
  <div class="column" style="width:12%" align="center"> <a onclick="set_preset('culcita')"> »Culcita«</a> </div>
  <div class="column" style="width:12%" align="center"> <a onclick="set_preset('fishbone')"> »Fishbone«</a> </div>
  <div class="column" style="width:12%" align="center"> <a onclick="set_preset('tree')"> »Tree«</a> </div>
  <div class="column" style="width:12%" align="center"> <button onclick="set_random()" class="button"> Randomize! </button> </div>
</div>

<div class="row">
  <div class="column" style="width:12%; font-weight:bold;"> </div>
  <div class="column" style="width:12%" align="center"> <a onclick="set_preset('sierpinski')"> »Sierpinski«</a> </div>
  <div class="column" style="width:12%" align="center"> <a onclick="set_preset('square')"> »Square«</a> </div>
  <div class="column" style="width:12%" align="center">  <a onclick="set_preset('castle')"> »Castle«</a>  </div>
  <div class="column" style="width:12%" align="center">  </div>
  <div class="column" style="width:12%" align="center">  </div>
  <div class="column" style="width:12%" align="center">  </div>
  <div class="column" style="width:12%" align="center">  </div>
</div>

<div style="padding-top: 25px;">
<input type="range" min="5000" max="500000" value="100000" step="5000" class="slider" id="samples_slider" oninput="update_samples(); draw_fern();" style="width:95%;">
<p id="samples_output" style="font-weight:bold;"> Number of samples: 100000 </p>
</div>

<div style="padding-top: 25px;">
<input type="range" class="slider" id="scale_slider" oninput="update_scale(); draw_fern();" style="width:95%;">
<p style="font-weight:bold;"> Scale </p>
</div>

 <div align="center" class="row"> <input type="text" class="jscolor" id="colorinput" value="000000"> <button class="button" onclick="set_colour()"> Throw in some colour! </button> </div>

<!-- Gallery  -->



### Gallery
<div align="center">
<div class="row">
<div class="column" style="width:23%;"><img src="/assets/image/bernsleys_fern_gallery/1.png"></div>
<div class="column" style="width:23%;"><img src="/assets/image/bernsleys_fern_gallery/2.png"></div>
<div class="column" style="width:23%;"><img src="/assets/image/bernsleys_fern_gallery/3.png"></div>
<div class="column" style="width:23%;"><img src="/assets/image/bernsleys_fern_gallery/4.png"></div>
</div>

<div class="row">
<div class="column" style="width:23%;"><img src="/assets/image/bernsleys_fern_gallery/5.png"></div>
<div class="column" style="width:23%;"><img src="/assets/image/bernsleys_fern_gallery/6.png"></div>
<div class="column" style="width:23%;"><img src="/assets/image/bernsleys_fern_gallery/7.png"></div>
<div class="column" style="width:23%;"><img src="/assets/image/bernsleys_fern_gallery/8.png"></div>
</div>
</div>

### Fan-art
Magnificent Borovica made by Olivia:
<div align="center">
<img src="/assets/image/bernsleys_fern_gallery/borovica.png" style="width:23%;">
<img src="/assets/image/bernsleys_fern_gallery/leafy.png" style="width:23%;">
</div>



<!-- Javascript -->

<script>
  var canvas = document.getElementById('canvas');
  canvas.width = canvas.clientWidth;
  canvas.height =  canvas.clientWidth;
  var ctx = canvas.getContext("2d");
  var clr = '#000000';

  var scale = canvas.height/11;
  document.getElementById('scale_slider').min = scale/10;
  document.getElementById('scale_slider').step = scale/5;
  document.getElementById('scale_slider').max = scale*20;
  document.getElementById('scale_slider').value = scale;


  function hexToRgb(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
  }


  function update_scale() {
    scale = parseFloat(document.getElementById('scale_slider').value);
  }

  function update_captions() {
    for (v in {a:'a', b:'b', c:'c', d:'d', e:'e', f:'f', p:'p'}) {
      for (n in {'1':'1', '2':'2', '3':'3', '4':'4'}) {
        vid = v + n;
        document.getElementById(vid + 'o').innerHTML = parseFloat(document.getElementById(vid).value).toFixed(2);
      }
    }
    draw_fern();
  }
  function update_samples() {
    var samples = parseInt(document.getElementById("samples_slider").value);
    document.getElementById("samples_output").innerHTML = "Number of samples: " + samples;
  }


  function draw_fern() {
    // clean the canvas
    ctx.save();
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.restore();

    var samples = parseInt(document.getElementById("samples_slider").value);

    // normalize row probabilities
    var p1 = parseFloat(document.getElementById("p1").value);
    var p2 = parseFloat(document.getElementById("p2").value);
    var p3 = parseFloat(document.getElementById("p3").value);
    var p4 = parseFloat(document.getElementById("p4").value);
    var sump = p1 + p2 + p3 + p4;
    p1 = p1/sump; p2 = p2/sump; p3 = p3/sump; p4=p4/sump;

    var x = 0, y = 0;


    var rv = {
      '1': [parseFloat(document.getElementById("a1").value), parseFloat(document.getElementById("b1").value),
            parseFloat(document.getElementById("c1").value), parseFloat(document.getElementById("d1").value),
            parseFloat(document.getElementById("e1").value), parseFloat(document.getElementById("f1").value)],

      '2': [parseFloat(document.getElementById("a2").value), parseFloat(document.getElementById("b2").value),
            parseFloat(document.getElementById("c2").value), parseFloat(document.getElementById("d2").value),
            parseFloat(document.getElementById("e2").value), parseFloat(document.getElementById("f2").value)],

      '3': [parseFloat(document.getElementById("a3").value), parseFloat(document.getElementById("b3").value),
            parseFloat(document.getElementById("c3").value), parseFloat(document.getElementById("d3").value),
            parseFloat(document.getElementById("e3").value), parseFloat(document.getElementById("f3").value)],

      '4': [parseFloat(document.getElementById("a4").value), parseFloat(document.getElementById("b4").value),
            parseFloat(document.getElementById("c4").value), parseFloat(document.getElementById("d4").value),
            parseFloat(document.getElementById("e4").value), parseFloat(document.getElementById("f4").value)]
    }

    var a, b, c, d, e, f;

    for (var i = 0; i < samples; i++) {
      // Roll a die to choose the row
      var die = Math.random();
      if (die <= p1) {
        a = rv['1'][0]; b = rv['1'][1]; c = rv['1'][2]; d = rv['1'][3]; e = rv['1'][4]; f = rv['1'][5];
      } else if (die <= p1 + p2) {
        a = rv['2'][0]; b = rv['2'][1]; c = rv['2'][2]; d = rv['2'][3]; e = rv['2'][4]; f = rv['2'][5];
      } else if (die <= p1 + p2 + p3) {
        a = rv['3'][0]; b = rv['3'][1]; c = rv['3'][2]; d = rv['3'][3]; e = rv['3'][4]; f = rv['3'][5];
      } else {
        a = rv['4'][0]; b = rv['4'][1]; c = rv['4'][2]; d = rv['4'][3]; e = rv['4'][4]; f = rv['4'][5];
      }

      var oldx = parseFloat(x), oldy = parseFloat(y);
      x = a*oldx + b*oldy + e;
      y = c*oldx + d*oldy + f;

      ctx.fillRect(canvas.width/2 + scale*x, canvas.height - scale*y - 20, 1, 1);
    }
  }

  draw_fern();

  function set_preset(name) {
    fern = ferns[name];
    for (key in fern) {
      document.getElementById(key).value = fern[key];
    }
    update_captions();
    draw_fern();
  }

  function set_random() {
    for (key in ferns["barnsley"]) {
      var altvalue = parseFloat(document.getElementById(key).value) + (Math.random() - 0.5)/8;

      document.getElementById(key).value = Math.max(parseFloat(document.getElementById(key).min), Math.min(parseFloat(document.getElementById(key).max),
      altvalue));
    }
    update_captions();
    draw_fern();
  }

  function set_colour() {
    ctx.fillStyle = "#" + document.getElementById("colorinput").value;
    draw_fern();
  }

  ferns = {
    "barnsley": {
      "a1": 0.00,
      "b1": 0.00,
      "c1": 0.00,
      "d1": 0.16,
      "e1": 0.00,
      "f1": 0.00,
      "p1": 0.01,

      "a2": 0.85,
      "b2": 0.04,
      "c2": -0.04,
      "d2": 0.85,
      "e2": 0.00,
      "f2": 1.60,
      "p2": 0.85,

      "a3": 0.20,
      "b3": -0.26,
      "c3": 0.23,
      "d3": 0.22,
      "e3": 0.00,
      "f3": 1.60,
      "p3": 0.07,

      "a4": -0.15,
      "b4": 0.28,
      "c4": 0.26,
      "d4": 0.24,
      "e4": 0.00,
      "f4": 0.44,
      "p4": 0.07
    },

    "culcita": {
      "a1": 0.00,
      "b1": 0.00,
      "c1": 0.00,
      "d1": 0.25,
      "e1": 0.00,
      "f1": -0.14,
      "p1": 0.02,

      "a2": 0.85,
      "b2": 0.02,
      "c2": -0.02,
      "d2": 0.83,
      "e2": 0.00,
      "f2": 1.00,
      "p2": 0.84,

      "a3": 0.09,
      "b3": -0.28,
      "c3": 0.3,
      "d3": 0.11,
      "e3": 0.00,
      "f3": 0.60,
      "p3": 0.07,

      "a4": -0.09,
      "b4": 0.28,
      "c4": 0.3,
      "d4": 0.09,
      "e4": 0.00,
      "f4": 0.70,
      "p4": 0.07
    },

    "fishbone": {
      "a1": 0.00,
      "b1": 0.00,
      "c1": 0.00,
      "d1": 0.25,
      "e1": 0.00,
      "f1": -0.4,
      "p1": 0.02,

      "a2": 0.95,
      "b2": 0.002,
      "c2": -0.002,
      "d2": 0.93,
      "e2": -0.002,
      "f2": 0.5,
      "p2": 0.84,

      "a3": 0.035,
      "b3": -0.11,
      "c3": 0.27,
      "d3": 0.01,
      "e3": 0.047,
      "f3": 0.06,
      "p3": 0.07,

      "a4": -0.04,
      "b4": 0.11,
      "c4": 0.27,
      "d4": 0.01,
      "e4": 0.047,
      "f4": 0.06,
      "p4": 0.07
    },

    "cyclosorus": {
      "a1": 0.00,
      "b1": 0.00,
      "c1": 0.00,
      "d1": 0.25,
      "e1": 0.00,
      "f1": -0.4,
      "p1": 0.02,

      "a2": 0.95,
      "b2": 0.005,
      "c2": -0.005,
      "d2": 0.93,
      "e2": -0.002,
      "f2": 0.5,
      "p2": 0.84,

      "a3": 0.035,
      "b3": -0.2,
      "c3": 0.16,
      "d3": 0.04,
      "e3": -0.09,
      "f3": 0.02,
      "p3": 0.07,

      "a4": -0.04,
      "b4": 0.2,
      "c4": 0.16,
      "d4": 0.04,
      "e4": 0.083,
      "f4": 0.12,
      "p4": 0.07
    },

    "barnsley2": {
      "a1": 0.00,
      "b1": 0.00,
      "c1": 0.00,
      "d1": 0.2,
      "e1": 0.00,
      "f1": -0.12,
      "p1": 0.01,

      "a2": 0.845,
      "b2": 0.035,
      "c2": -0.035,
      "d2": 0.82,
      "e2": 0.00,
      "f2": 1.60,
      "p2": 0.85,

      "a3": 0.20,
      "b3": -0.31,
      "c3": 0.255,
      "d3": 0.245,
      "e3": 0.00,
      "f3": 0.29,
      "p3": 0.07,

      "a4": -0.15,
      "b4": 0.24,
      "c4": 0.25,
      "d4": 0.2,
      "e4": 0.00,
      "f4": 0.68,
      "p4": 0.07
    },

    "tree": {
        "a1": 0.00,
        "b1": 0.00,
        "c1": 0.00,
        "d1": 0.5,
        "e1": 0.00,
        "f1": 0.0,
        "p1": 0.05,

        "a2": 0.42,
        "b2": -0.42,
        "c2": 0.42,
        "d2": 0.42,
        "e2": 0.00,
        "f2": 0.2,
        "p2": 0.4,

        "a3": 0.42,
        "b3": 0.42,
        "c3": -0.42,
        "d3": 0.42,
        "e3": 0.00,
        "f3": 0.2,
        "p3": 0.4,

        "a4": 0.1,
        "b4": 0.0,
        "c4": 0.0,
        "d4": 0.1,
        "e4": 0.00,
        "f4": 0.2,
        "p4": 0.15
      },

      "sierpinski": {
          "a1": 0.5,
          "b1": 0.00,
          "c1": 0.00,
          "d1": 0.5,
          "e1": 1.0,
          "f1": 1.0,
          "p1": 0.33,

          "a2": 0.5,
          "b2": 0.0,
          "c2": 0.0,
          "d2": 0.5,
          "e2": 1.0,
          "f2": 50,
          "p2": 0.33,

          "a3": 0.5,
          "b3": 0.0,
          "c3": 0.0,
          "d3": 0.5,
          "e3": 50,
          "f3": 50,
          "p3": 0.34,

          "a4": 0.0,
          "b4": 0.0,
          "c4": 0.0,
          "d4": 0.0,
          "e4": 0.00,
          "f4": 0.0,
          "p4": 0.0
        },

        "square": {
            "a1": 0.5,
            "b1": 0.00,
            "c1": 0.00,
            "d1": 0.5,
            "e1": 1.0,
            "f1": 1.0,
            "p1": 0.25,

            "a2": 0.5,
            "b2": 0.0,
            "c2": 0.0,
            "d2": 0.5,
            "e2": 50.0,
            "f2": 1.0,
            "p2": 0.25,

            "a3": 0.5,
            "b3": 0.0,
            "c3": 0.0,
            "d3": 0.5,
            "e3": 1.0,
            "f3": 50.0,
            "p3": 0.25,

            "a4": 0.5,
            "b4": 0.0,
            "c4": 0.0,
            "d4": 0.5,
            "e4": 50.0,
            "f4": 50.0,
            "p4": 0.25
          },

          "castle": {
              "a1": 0.5,
              "b1": 0.00,
              "c1": 0.00,
              "d1": 0.5,
              "e1": 0.0,
              "f1": 0.0,
              "p1": 0.25,

              "a2": 0.5,
              "b2": 0.0,
              "c2": 0.0,
              "d2": 0.5,
              "e2": 2.0,
              "f2": 0.0,
              "p2": 0.25,

              "a3": 0.4,
              "b3": 0.0,
              "c3": 0.0,
              "d3": 0.4,
              "e3": 0.0,
              "f3": 1.0,
              "p3": 0.25,

              "a4": 0.5,
              "b4": 0.0,
              "c4": 0.0,
              "d4": 0.5,
              "e4": 2.0,
              "f4": 1.0,
              "p4": 0.25
            }
  }
</script>
