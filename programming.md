---
layout: page
title: Programming
permalink: /programming/
---


<ul class="post-list">
  {% for post in site.posts %}
  <li>
    {% if post.categories contains 'programming' %}
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
