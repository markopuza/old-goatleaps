---
layout: page
title: "Art/Media"
permalink: /media/
---



<div class="row">
  <div class="column">
    <h2></h2>

    <ul class="post-list">
      {% for post in site.posts %}
      <li>
        {% if post.categories contains 'media' %}
        {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
        <div>
          <a class="post-link" href="{{ post.url | relative_url }}">
          <img class="post-icon" src="/assets/icon/{{ post.icon }}.png">
            {{ post.title | escape }}
          </a>
          <span class="post-meta"> {{ post.date | date: date_format }}</span>
        </div>
        {% endif %}
      </li>
      {% endfor %}
    </ul>


  </div>
  <div class="column" align="center">
    <h1> Sporadic inspiration </h1>
    <a href="/art/media/Sporadic-inspiration.html"><img src="{{ site.baseurl }}/assets/icon/sporadic.png" align="center" style="width:40%; margin-right: 10px;"></a>
  </div>
</div>


<div align="center">
  <h1> The Chaos game </h1>
  <a class="post-link" href="/media/maths/programming/tools/The-Chaos-Game.html">
  <img src="/assets/image/chaos_game_gallery/1.png" style="width:22%;">
  <img src="/assets/image/chaos_game_gallery/2.png" style="width:22%;">
  <img src="/assets/image/chaos_game_gallery/3.png" style="width:22%;">
  <img src="/assets/image/chaos_game_gallery/7.png" style="width:22%;">
  </a>
</div>
