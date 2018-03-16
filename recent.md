---
layout: page
title: Recent
permalink: /recent/
---

<div style="overflow-x: auto;">
<ul class="post-list">
  {% for post in site.posts limit: 15 %}
  <li>
    {% if  true %}
    {% unless post.categories contains 'noshow' %}
    {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
    <div class="row">
      <div class="column">
        <a class="post-link" href="{{ post.url | relative_url }}">
        <img class="post-icon" src="/assets/icon/{{ post.icon }}.png">
          {{ post.title | escape }}
        </a>
      </div>

      <div class="column">
      <span> {{ post.category-string }}  </span> <span class="post-meta">{{ post.date | date: date_format }}</span>
    </div>
    </div>
    {% endunless %}
    {% endif %}
  </li>
  {% endfor %}
</ul>
</div>
