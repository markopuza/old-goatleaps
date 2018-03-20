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
  <div class="column">
    <a href="/art/media/Sporadic-inspiration.html"><img src="{{ site.baseurl }}/assets/icon/sporadic.png" align="left" style="width:40%; margin-right: 10px;"></a>

  </div>
</div>
