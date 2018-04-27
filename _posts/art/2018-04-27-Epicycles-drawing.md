---
layout: post
title:  "Epicycles drawing"
date:   2018-04-27 01:36:59 +0000
category-string: "Art"
categories: media maths programming tools
icon: epicyclesdrawing
---

<!-- Fast Fourier Transform library -->
<script src="/assets/script/fft.js"></script>
<!-- Complex number library -->
<script src="/assets/script/complex.min.js"></script>

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

.small_button {
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

.button {
    background-color: #e7e7e7;
    color: black;
    border: none;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
  }
</style>

It is a result of Fourier analysis that any closed path in the complex plane can be arbitrarily approximated by some complex function:

$$p(t) = \sum_{j = 0}^N a_j e^{k_j t i}; \ \ a_j, k_j \in \mathbb C;\ t \in [0, 1)$$

We may obtain such an approximation quite efficiently using the discrete Fourier transform. The sum can be nicely visualized as a chain of epicycles (circles). You can __draw your own path__ below to see it constructed using epicycles!

The origins of epicycles have a curious history. For more information see >>[Wikipedia](https://en.wikipedia.org/wiki/Deferent_and_epicycle)<<.

<div style="width: 70%; height: 70%; padding-bottom: 70%; margin: 0 auto; position: relative; ">
<center>  
    <canvas id="canvas1" style="width:100%; z-index: 1; border:1px solid #000000; position:absolute; left:0px; top:0px;"></canvas>
    <canvas id="canvas2" style="width:100%; z-index: 2; border:1px solid #000000; position:absolute; left:0px; top:0px;" onclick="point_clicked(event);"></canvas>
</center>
</div>

<div style="padding-top:20px;">
<!-- Controls -->
<button onclick="ctx.translate(-canvas.width/50, 0); ctx2.translate(-canvas.width/50, 0); shift_x -= canvas.width/50;" class="small_button"> &larr; </button>
<button onclick="ctx.translate(canvas.width/50, 0); ctx2.translate(canvas.width/50, 0);  shift_x += canvas.width/50;" class="small_button"> &rarr; </button>
<button onclick="ctx.translate(0, -canvas.width/50); ctx2.translate(0, -canvas.width/50);  shift_y -= canvas.width/50;" class="small_button"> &uarr; </button>
<button onclick="ctx.translate(0, canvas.width/50); ctx2.translate(0, canvas.width/50);  shift_y += canvas.width/50;" class="small_button"> &darr; </button>
</div>

<button class="small_button" id="clear_button" style="font-weight:bold; width=30%;" onclick="clear_canvases();"> Clear </button>
<button class="small_button" id="clear_button" style="font-weight:bold; width=30%;" onclick="PAUSE=!PAUSE; if (COLLECT_POINTS) {COLLECT_POINTS=false; run();}; if (!PAUSE) {animate();} "> Pause / Start </button>

<div class="row" style="width:100%;">
  <div class="column" align="center" style="width: 44%;">
    <button class="button" id="sporadic_button" style="font-weight:bold; width=30%;" onclick="PAUSE=false; COLLECT_POINTS=false; clear_canvases(); run(sporadic=true);"> SPORADIC INSPIRATION </button>
  </div>
  <div class="column" align="center" style="width:44%;">
    <button class="button" id="collect_button" style="font-weight:bold; width=30%;" onclick="PAUSE=true; reset_arrays(); clear_canvases(); draw_disk(0, 0, 5); COLLECT_POINTS=true;"> Custom points! </button>
    <p> 1. Click; 2. Define your points (in order); 3. Click the Pause/Start button. </p>
  </div>
</div>

<div style="padding-top: 25px;">
<input type="range" class="slider" id="speed_slider" oninput="update_speed();" style="width:95%;" value="0.02" step="0.005" min="0.005" max="0.2">
<p style="font-weight:bold;"> Speed </p>
</div>

<div style="padding-top: 25px;">
<input type="range" class="slider" id="maxcircles_slider" oninput="update_maxcircles();" style="width:95%;" value="15" step="1" min="1" max="100">
<p style="font-weight:bold;"> Maximum number of circles </p>
</div>

<div style="padding-top: 25px;">
<input type="range" class="slider" id="scale_slider" oninput="update_scale();" style="width:95%;" value="1.0" step="0.01" min="0.1" max="3.0">
<p style="font-weight:bold;"> Scale </p>
</div>

<div style="padding-top: 25px;">
<input type="range" class="slider" id="fps_slider" oninput="update_fps();" style="width:95%;" value="20" step="1" min="1" max="60">
<p style="font-weight:bold;"> Frames per second </p>
</div>

<!-- Main body -->
<script>
var canvas = document.getElementById('canvas1');
canvas.width = canvas.clientWidth;
canvas.height = canvas.clientWidth;
var ctx = canvas.getContext("2d");
ctx.strokeStyle = "#bbbbbb";
var rect = canvas.getBoundingClientRect();

var canvas2 = document.getElementById('canvas2');
canvas2.width = canvas.width;
canvas2.height = canvas.height;
var ctx2 = canvas2.getContext("2d");


var shift_x = 0;
var shift_y = 0;
var MAX_CIRCLES = 15;
var SCALE = 1.0;
var PAUSE = false;
var SPEED = 0.02;
var fpsInterval = 1000 / 20;
var COLLECT_POINTS = false;


var im = []; re = []; bad_times = []; radii = []; exps = [];

var sporadicIM = [-20, -31, -45, -55, -65, -61, -51, -38, -16, 0, 0, -4, -20, -38, -41, 117, 115, 112, 107, 101, 100, 100, 100, 100, 106, 128, 165, 191, 203, 205, 205, 190, 157, 138, 122, 10, -8, -30, -56, -77, -79, -82, -71, -24, -9, -6];
var sporadicRE = [-125, -119, -105, -87, -69, -45, -24, -20, -21, -35, -65, -81, -94, -101, -103, -100, -89, -81, -52, -5, 31, 54, 102, 148, 185, 201, 198, 180, 102, 64, 17, -16, -39, -45, -51, 94, 86, 78, 73, 73, 85, 114, 137, 140, 108, 83];
MOD = 2*Math.PI;
var sporadicBADTIMES = [[-1, 0.1], [1.55, 2.1], [4.55, 5], [6.06, 7]];


var x0 = canvas.width/2; y0 = canvas.width/2;
var rad0 = canvas.width/3;

function point_clicked(event) {
  if (COLLECT_POINTS) {
    var x = event.offsetX - x0 - shift_x;
    var y = event.offsetY - y0 - shift_y;

    draw_disk(x, y, 5);
    im.push(y);
    re.push(x);
  }
}


function update_scale() {
  SCALE = parseFloat(document.getElementById('scale_slider').value);
  clear_canvases();
}

function update_speed() {
  SPEED = parseFloat(document.getElementById('speed_slider').value);
}

function update_maxcircles() {
  MAX_CIRCLES = parseFloat(document.getElementById('maxcircles_slider').value);
  clear_canvases();
}

function update_fps() {
  fpsInterval = 1000 / parseFloat(document.getElementById('fps_slider').value);
}

function clear_canvases() {
  ctx.save();
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.restore();

  ctx2.save();
  ctx2.setTransform(1, 0, 0, 1, 0, 0);
  ctx2.clearRect(0, 0, canvas.width, canvas.height);
  ctx2.restore();
}

function draw_line(frx, fry, tox, toy) {
    ctx.lineWidth=1;
    ctx.beginPath();
    ctx.moveTo(x0 + frx, y0 + fry);
    ctx.lineTo(x0 + tox, y0 + toy);
    ctx.stroke();
}

function draw_circle(x, y, radius, start_angle) {
  ctx.lineWidth=1;
  ctx.beginPath();
  ctx.arc(x0 + x, y0 + y, radius, start_angle, 2*Math.PI);
  ctx.stroke();
}

function draw_disk(x, y, radius) {
  ctx.lineWidth=2;
  ctx.beginPath();
  ctx.arc(x0 + x, y0 + y, radius, 0, 2*Math.PI);
  ctx.fill();
}

eps = 0.0000001;
function draw_epicycles(time) {
  var centre = new Complex([0, 0]);
  draw_disk(centre.re, centre.im, 3);

  for (var i = 0; i < Math.min(radii.length, MAX_CIRCLES); i++) {
      if (radii[i].abs() < eps) {
        continue;
      }
      var circle = radii[i].mul(exps[i].mul(time).exp()).mul(SCALE);
      draw_circle(centre.re, centre.im, circle.abs(), 0);
      draw_line(centre.re, centre.im, centre.add(circle).re, centre.add(circle).im);
      centre = centre.add(circle);
      draw_disk(centre.re, centre.im, 3);
  }

  var good_time = true;
  for (var i = 0; i < bad_times.length; i++) {
    if (bad_times[i][0] < (time % MOD) && bad_times[i][1] > (time % MOD)) {
      good_time = false;
      break;
    }
  }

  if (good_time) {
    ctx2.lineWidth=2;
    ctx2.beginPath();
    ctx2.arc(x0 + centre.re, y0 + centre.im, 4, 0, 2*Math.PI);
    ctx2.fill();
  }
}

then = Date.now();
function animate() {
  if (!PAUSE) {    
    requestAnimationFrame(animate);
  }
    now = Date.now();
    elapsed = now - then;

    if (elapsed > fpsInterval) {
        then = now - (elapsed % fpsInterval);

        ctx.save();
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.restore();

        draw_epicycles(t);
        t += SPEED + SPEED*Math.random()/4;
    }
}

function animate_epicycles() {    
    then = Date.now();
    startTime = then;
    t = 0.0;
    animate();
}

function reset_arrays() {
  im = []; re = []; bad_times = []; radii = []; exps = [];
}

function run(sporadic=false) {
  if (sporadic) {
    reset_arrays();

    for (var i = 0; i < sporadicIM.length; i++) {
      im.push(sporadicIM[i]);
      re.push(sporadicRE[i]);
    }
    for (var i = 0; i < sporadicBADTIMES.length; i++) {
      bad_times.push(sporadicBADTIMES[i]);
    }
  }

  // DFT
  transform(re, im);


  for (var i = 0; i < re.length; i++) {
    radii.push(new Complex([re[i]/re.length, im[i]/re.length]));
    if (i < re.length/2) {
      exps.push(new Complex([0, i]));
    }
    else {
      exps.push(new Complex([0, -(re.length-i)]));
    }
  }


  var l = [];
  for (var i = 0; i < re.length; i++) {
    l.push([radii[i], exps[i]]);
  }

  l.sort(function(a, b) {
      return b[0].abs() - a[0].abs();
    });

  for (var i = 0; i < re.length; i++) {
    radii[i] = l[i][0];
    exps[i] = l[i][1];
  }

  animate_epicycles();
}

run(sporadic=true);
</script>
