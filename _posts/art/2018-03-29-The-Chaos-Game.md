---
layout: post
title:  "The Chaos game on regular n-gons"
date:   2018-03-29 01:36:59 +0000
category-string: "Art"
categories: media maths programming tools
icon: chaosgame
---


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
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
  }
</style>


The Chaos game is a simple iterative way to create fractals. The only thing we need to keep track of is a single point; at each iteration it is moved towards a randomly chosen vertex. You can find a more detailed description at the bottom of this page, as well as a small gallery.

# Meanwhile, can you create your own unique fractal?
Be cautious with the number of samples; the image is rendered in your browser. Feel free to send me your creation!

<div class="slidecontainer">
  <input type="range" min="3" max="25" value="4" class="slider" id="n_slider" oninput="update_n()" style="width:95%;">
  <p id="n_slider_output" style="font-weight:bold;"> Number of vertices: 4 </p>

  <input type="range" min="5000" max="500000" value="100000" step="5000" class="slider" id="samples_slider" oninput="update_samples()" style="width:95%;">
  <p id="samples_output" style="font-weight:bold;"> Number of samples: 100000 </p>

  <input type="range" min="0" max="1" value="0.5" step="0.02" class="slider" id="jump_slider" oninput="update_jump()" style="width:95%;">
  <p id="jump_output" style="font-weight:bold;"> Jumping ratio: 0.50 </p>

  <input type="range" min="0" max="22" value="0" step="1" class="slider" id="rule_slider" oninput="update_rule()" style="width:95%;">
  <p id="rule_output" style="font-weight:bold;"> Rule: None </p>

  <input type="range" min="0" max="5" value="1" step="1" class="slider" id="filter_slider" oninput="update_filter()" style="width:95%;">
  <p id="filter_output" style="font-weight:bold;"> Filter: Sporadic inspiration </p>

  <input type="range" min="0" max="1" value="0.9" step="0.025" class="slider" id="filter_strength_slider" oninput="update_filter_strength()" style="width:95%;">
  <p id="filter_strength_output" style="font-weight:bold;"> Filter strength: 0.9 </p>

  <input type="range" min="0" max="2" value="1" step="0.05" class="slider" id="filter_size_slider" oninput="update_filter_size()" style="width:95%;">
  <p id="filter_size_output" style="font-weight:bold;"> Filter size: 1.0 </p>

  <p> </p>
  <button class="button" id="center_output" style="font-weight:bold;" onclick="update_center()"> Include center: NO </button>

  <button class="button" style="font-weight:bold;" onclick="random_settings()"> Random settings </button>
</div>


<!-- Canvas -->

<center>  
  <canvas id="canvas" style="width:70%;"></canvas>
</center>


<!-- Javascript -->

<script>
var canvas = document.getElementById('canvas');
canvas.width = canvas.clientWidth;
canvas.height =  canvas.clientWidth;
var ctx = canvas.getContext("2d");

var n = 4;                                   // Number of vertices
var x = canvas.width/2, y = canvas.width/2;  // Current point coordinates
var samples = 100000;                        // Number of samples
var last_chosen = -1;                        // Last chosen coordinates
var filter_strength = 0.95;                  // Strength of filter, between 0 and 1
var jump_distance = 1/2;                     // Fraction of jump, between 0 and 1
var include_center = false;                   // Include center as a vertex
var rule_index = 0;                          // Index of the rule being used
var filter_size = 1.0;
var filter_index = 1;                        // Index of the filter being used
var vertices;                                // List holding all vertices


function update_n() {
  n = parseInt(document.getElementById("n_slider").value);
  document.getElementById("n_slider_output").innerHTML = "Number of vertices: " + n;
  runSimulation();
}
function update_samples() {
  samples = parseInt(document.getElementById("samples_slider").value);
  document.getElementById("samples_output").innerHTML = "Number of samples: " + samples;
  runSimulation();
}
function update_jump() {
  jump_distance = parseFloat(document.getElementById("jump_slider").value);
  document.getElementById("jump_output").innerHTML = "Jumping ratio: " + jump_distance.toFixed(2);
  runSimulation();
}
function update_filter_strength() {
  filter_strength = parseFloat(document.getElementById("filter_strength_slider").value);
  document.getElementById("filter_strength_output").innerHTML = "Filter strength: " + filter_strength;
  runSimulation();
}
function update_filter_size() {
  filter_size = parseFloat(document.getElementById("filter_size_slider").value);
  document.getElementById("filter_size_output").innerHTML = "Filter size: " + filter_size.toFixed(2);
  runSimulation();
}
function update_center() {
  include_center = !include_center;
  document.getElementById("center_output").innerHTML = "Include center: " + (include_center ? 'YES' : 'NO');
  runSimulation();
}
function update_filter() {
  filter_index = parseInt(document.getElementById("filter_slider").value);
  document.getElementById("filter_output").innerHTML = "Filter: " + filters[filter_index][1];
  runSimulation();
}
function update_rule() {
  rule_index = parseInt(document.getElementById("rule_slider").value);
  document.getElementById("rule_output").innerHTML = "Rule: " + rules[rule_index][1];
  runSimulation();
}

function random_settings() {
  n = 3 + Math.floor(Math.random() * 12);
  jump_distance = 0.25 + 0.5 * Math.random();
  filter_strength = Math.random();
  filter_size = 2 * Math.random();
  include_center = Math.random() < 0.5 ? true : false;
  filter_index = Math.floor(Math.random() * filters.length);
  rule_index = Math.floor(Math.random() * rules.length);

  document.getElementById("n_slider").value = n;
  document.getElementById("n_slider_output").innerHTML = "Number of vertices: " + n;
  document.getElementById("jump_slider").value = jump_distance;
  document.getElementById("jump_output").innerHTML = "Jumping ratio: " + jump_distance.toFixed(2);
  document.getElementById("filter_strength_slider").value = filter_strength;
  document.getElementById("filter_strength_output").innerHTML = "Filter strength: " + filter_strength;
  document.getElementById("filter_size_slider").value = filter_size;
  document.getElementById("filter_size_output").innerHTML = "Filter size: " + filter_size.toFixed(2);
  document.getElementById("center_output").innerHTML = "Include center: " + (include_center ? 'YES' : 'NO');
  document.getElementById("filter_slider").value = filter_index;
  document.getElementById("filter_output").innerHTML = "Filter: " + filters[filter_index][1];
  document.getElementById("rule_slider").value = rule_index;
  document.getElementById("rule_output").innerHTML = "Rule: " + rules[rule_index][1];

  runSimulation();
}


function drawRegularPolygon(context, x, y, sides, radius, offset, fill, fillColor, stroke, strokeColor, strokeWidth){
    vertices = generatePoints(x,y,sides,radius,offset);
    context.beginPath(vertices[0][0], vertices[0][1]);
    for (var i = 0; i < vertices.length; i++){
        context.lineTo(vertices[i][0],vertices[i][1]);
    }
    context.lineTo(vertices[0][0], vertices[0][1]);
    context.ClosePath
    if(fill == true)
    {
        context.fillStyle = fillColor;
        context.fill();
    }
    if (stroke == true)
    {
        context.strokeStyle = strokeColor;
        context.lineWidth = strokeWidth;
        context.stroke();
    }
}

function drawRegularPolygonSplit(context, x, y, sides, radius, offset, fill, fillColors, stroke, strokeColors, strokeWidth){    
    vertices = generatePoints(x,y,sides,radius,offset);

    for (var i = 0; i < vertices.length; i++){
        context.beginPath(x,y);
        context.lineTo(vertices[i][0],vertices[i][1]);
        context.lineTo(vertices[(i + 1) % vertices.length][0],vertices[(i + 1) % vertices.length][1]);
        context.lineTo(x,y);
        context.ClosePath
        if(fill == true)
        {
            context.fillStyle = fillColors[i];        
            context.fill();
        }
        if(stroke == true)
        {
            context.strokeStyle = strokeColors[i];        
            context.lineWidth = strokeWidth;
            context.stroke();
        }
    }
}

function generatePoints (x, y, sides, radius, offset){      
    var angle = 2 * Math.PI / sides;    
    var points = [];
    for (var i = 0; i < sides; i++)
    {
        var single = [];
        var verticeX = x + radius * Math.sin((i * angle) + offset);  
        var verticeY = y + radius * Math.cos((i * angle) + offset);
        single.push(verticeX);
        single.push(verticeY);
        points.push(single);
    }    
    return points;
}


function next_sample(rule, filter) {
    var nxt_vertex = Math.floor(Math.random() * vertices.length);
    while (!rule(nxt_vertex, last_chosen)) {
      nxt_vertex = Math.floor(Math.random() * vertices.length);
    }
    last_chosen = nxt_vertex;

    xx = Math.round(x * (1.0 - jump_distance) + vertices[nxt_vertex][0] * jump_distance);
    yy = Math.round(y * (1.0 - jump_distance) + vertices[nxt_vertex][1] * jump_distance);

    if (filter(xx, yy) || Math.random() > filter_strength) {
      x = xx; y = yy;
      ctx.fillRect(x, y, 1, 1);
    }
}

rules = [
  [((nxt, l) => true), 'None'],
  [((nxt, l) => nxt != (5*l) % n), '5*last - current (mod n) != 0'],
  [((nxt, l) => nxt != (4*l) % n), '4*last - current (mod n) != 0'],
  [((nxt, l) => nxt != (3*l) % n), '3*last - current (mod n) != 0'],
  [((nxt, l) => nxt != (2*l) % n), '2*last - current (mod n) != 0' ],
  [((nxt, l) => (nxt + l) % n != 0), 'last + current != n'],
  [((nxt, l) => (n + nxt - l) % n != 6 && (n + nxt - l) % n != n - 6), 'Not distance 6 from last'],
  [((nxt, l) => (n + nxt - l) % n != 5 && (n + nxt - l) % n != n - 5), 'Not distance 5 from last'],
  [((nxt, l) => (n + nxt - l) % n != 4 && (n + nxt - l) % n != n - 4), 'Not distance 4 from last'],
  [((nxt, l) => (n + nxt - l) % n != 3 && (n + nxt - l) % n != n - 3), 'Not distance 3 from last'],
  [((nxt, l) => (n + nxt - l) % n != 2 && (n + nxt - l) % n != n - 2), 'Not distance 2 from last'],
  [((nxt, l) => (n + nxt - l) % n != 1 && (n + nxt - l) % n != n - 1), 'Not distance 1 from last' ],
  [((nxt, l) => nxt != (l + 6) % n), 'Not sixth right of last'],
  [((nxt, l) => nxt != (l + 5) % n), 'Not fifth right of last'],
  [((nxt, l) => nxt != (l + 4) % n), 'Not fourth right of last' ],
  [((nxt, l) => nxt != (l + 3) % n), 'Not third right of last'],
  [((nxt, l) => nxt != (l + 2) % n), 'Not second right of last' ],
  [((nxt, l) => nxt != (l + 1) % n), 'Not first right of last'],
  [((nxt, l) => nxt != (l + 1) % n && nxt != (l + 2) % n), 'Not first or second right of last'],
  [((nxt, l) => nxt != (l + 1) % n && nxt != (l + 3) % n), 'Not first or third right of last'],
  [((nxt, l) => nxt != (l + 1) % n && nxt != (l + 4) % n), 'Not first or fourth right of last'],
  [((nxt, l) => nxt != (l + 1) % n && nxt != (l + 2) % n && nxt != (l + 3) % n), 'Not first or second or third right of last'],
  [((nxt, l) => nxt != l), 'Not last']
]

sporadic_coors = [[5, 23], [5, 24], [6, 23], [6, 25], [7, 13], [7, 14], [7, 15], [7, 16], [7, 23], [7, 25], [8, 12], [8, 13], [8, 16], [8, 17], [8, 23], [8, 25], [9, 12], [9, 13], [9, 17], [9, 23], [9, 25], [10, 13], [10, 14], [10, 16], [10, 17], [10, 23], [10, 24], [10, 25], [11, 14], [11, 15], [11, 16], [11, 24], [18, 7], [18, 8], [18, 9], [18, 10], [18, 11], [18, 12], [18, 13], [18, 14], [18, 15], [18, 16], [18, 17], [18, 18], [18, 19], [19, 5], [19, 6], [19, 7], [19, 19], [19, 20], [20, 5], [20, 20], [20, 21], [21, 7], [21, 21], [22, 7], [22, 20], [23, 7], [23, 19], [23, 20], [24, 8], [24, 18], [24, 19], [25, 9], [25, 10], [25, 11], [25, 12], [25, 13], [25, 14], [25, 15], [25, 16], [25, 17], [25, 18]];


function sporadic_filter(xx, yy) {
  var ss = filter_size * canvas.width/3.5;
  var pixs = ss/32;
  var sox = canvas.width/2 - ss/2, soy = canvas.width/2 - ss/2;

  for (var i = 0; i < sporadic_coors.length; i++) {
    var py = sporadic_coors[i][0], px = sporadic_coors[i][1];

    if ((xx >= sox + px * pixs) && (xx < sox + (px + 1) * pixs)) {
      if ((yy >= soy + py * pixs) && (yy < soy + (py + 1) * pixs)) {
        return false;
      }
    }
  }
  return true;
}

filters = [
  [((xx, yy) => true), 'None'],
  [((xx, yy) => sporadic_filter(xx, yy)), 'Sporadic inspiration'],
  [((xx, yy) => Math.sqrt((canvas.width/2 - xx)*(canvas.width/2 - xx) + (canvas.width/2 - yy)*(canvas.width/2 - yy)) >= filter_size * canvas.width/7), 'Disk'],
  [((xx, yy) => Math.sqrt((canvas.width/2 - xx)*(canvas.width/2 - xx) + (canvas.width/2 - yy)*(canvas.width/2 - yy)) >= filter_size * canvas.width/7 || Math.sqrt((canvas.width/2 - xx)*(canvas.width/2 - xx) + (canvas.width/2 - yy)*(canvas.width/2 - yy)) <= filter_size * canvas.width/9), 'Ring'],
  [((xx, yy) => Math.abs(xx - canvas.width/2) + Math.abs(yy - canvas.width/2) >= filter_size * canvas.width/9), 'Square'],
  [((xx, yy) => Math.abs(xx - canvas.width/2) + Math.abs(yy - canvas.width/2) >= filter_size * canvas.width/7 || Math.abs(xx - canvas.width/2) + Math.abs(yy - canvas.width/2) <= filter_size * canvas.width/9), 'Ring Square'],
]



////////////////////////////////////////////////////////////////////////////

function runSimulation() {
  <!-- Reset variables  -->
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  x = canvas.width/2, y = canvas.width/2;
  last_chosen = -1;  

  drawRegularPolygon(ctx, canvas.width/2, canvas.width/2, n, canvas.width/2.5, 0, false, false, true,  0, 2);
  if (include_center) {
      vertices.push([x, y]);
  }

  for (var i = 0; i < samples; i++) {
    next_sample(rules[rule_index][0], filters[filter_index][0]);
  }
}

////////////////////////////////////////////////////////////////////////////


random_settings();
</script>

### Gallery
<div align="center">
<img src="/assets/image/chaos_game_gallery/1.png" style="width:23%;">
<img src="/assets/image/chaos_game_gallery/2.png" style="width:23%;">
<img src="/assets/image/chaos_game_gallery/3.png" style="width:23%;">
<img src="/assets/image/chaos_game_gallery/4.png" style="width:23%;">
<p></p>
<img src="/assets/image/chaos_game_gallery/5.png" style="width:23%;">
<img src="/assets/image/chaos_game_gallery/6.png" style="width:23%;">
<img src="/assets/image/chaos_game_gallery/7.png" style="width:23%;">
<img src="/assets/image/chaos_game_gallery/8.png" style="width:23%;">
<p></p>
<img src="/assets/image/chaos_game_gallery/9.png" style="width:23%;">
<img src="/assets/image/chaos_game_gallery/10.png" style="width:23%;">
</div>

### Fan-art
Magnificent fractals made by Lukas:
<div align="center">
<img src="/assets/image/chaos_game_gallery/fan1.png" style="width:23%;">
<img src="/assets/image/chaos_game_gallery/fan2.png" style="width:23%;">
</div>

Gerda's astounding dotty fractals:
<div align="center">
<img src="/assets/image/chaos_game_gallery/gerda1.png" style="width:23%;">
<img src="/assets/image/chaos_game_gallery/gerda2.png" style="width:23%;">
</div>


### Description of the process
The process follows the following steps:

- Start with a point within the __n-gon__ (e.g. the centre).
- Choose a __rule__. Examples of rules can be: "Don't ever jump towards the same vertex twice in a row", or, "Don't jump towards any neighbouring vertex of the vertex to which you jumped last".
- Choose a __filter__. This is a small area in the centre of the n-gon; we will prevent our point to land in the area during the process.
- Repeat multiple times (This is controlled by __Number of samples__ slider) the next steps:
  - Keep choosing a vertex at random, until it is compliant with your rule.
  - Jump the fraction $$r$$ of the way towards this vertex (This is the __jumping ration__).
  - With probability __filter strength__, check if the point lands in the area of the filter. If it is the case, we skip this iteration altogether.

___
There is also a small article on >>[wikipedia](https://en.wikipedia.org/wiki/Chaos_game)<< worth checking out.
