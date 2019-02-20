---
layout: post
title:  "Radial tree visualization"
date:   2018-11-24 01:36:59 +0000
category-string: "Programming"
categories: media maths programming
icon: radialtree
published: false
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


<!-- Canvas -->
<center>  
  <canvas id="canvas" style="width:70%;"></canvas>
</center>



<script>
  var canvas = document.getElementById('canvas');
  canvas.width = canvas.clientWidth;
  canvas.height =  canvas.clientWidth;
  var ctx = canvas.getContext("2d");
  var clr = '#000000';

  // auxiliary variables
  var n = 5000;
  var visited = new Array(n);
  var coors = new Array(n);
  var edges = [];

  // random tree generation
  var tree = {};
  for (var i = 0; i < n; ++i) {
    tree[i] = [];
    if (i > 0) {
        tree[Math.floor(i/2)].push(i);
    }

    visited[i] = false;
    coors[i] = [0, 0];
  }
  visited[0] = true;

  var num_leaves = 0;
  for (var i = 0; i < n; ++i) {
    num_leaves += tree[i].length == 0;
  }
  var angle = 2*Math.PI/(n + 1);

  var maxx = 0; var maxy = 0;

  // coordinate determination
  var counter = 0;
  function rec(node, cx, cy) {
    for (var i = 0; i < tree[node].length; ++i) {
      var ne = tree[node][i];
      if (!visited[ne]) {
        visited[ne] = true;
        coors[ne] = [cx + Math.cos(counter*angle), cy + Math.sin(counter*angle)];
        maxx = Math.max(maxx, Math.abs(coors[ne][0]));
        maxy = Math.max(maxy, Math.abs(coors[ne][1]));
        edges.push([[cx, cy], [cx + Math.cos(counter*angle), cy + Math.sin(counter*angle)]]);
        if (tree[ne].length == 0) {
          counter += 1;
        }
        rec(ne, coors[ne][0], coors[ne][1]);
      }
    }
  }
  rec(0, 0, 0);

  // plotting
  var cx = canvas.width/2;
  var cy = canvas.height/2;
  var scale = Math.min(cx / (maxx + 1), cy / (maxy + 1));

  for (var i = 0; i < edges.length; ++i) {
    ctx.beginPath();
    ctx.moveTo(cx - scale*edges[i][0][0], cy - scale*edges[i][0][1]);
    ctx.lineTo(cx - scale*edges[i][1][0], cy - scale*edges[i][1][1]);
    ctx.stroke();
  }

  ctx.beginPath();
  ctx.arc(cx, cy, 4, 0, 2 * Math.PI);
  ctx.fill();

  for (var i = 0; i < coors.length; ++i) {
    ctx.beginPath();
    ctx.arc(cx - scale*coors[i][0], cy - scale*coors[i][1], 2, 0, 2 * Math.PI);
    ctx.fill();
  }

  console.log(coors);

</script>
