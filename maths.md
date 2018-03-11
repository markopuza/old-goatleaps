---
layout: page
title: Maths
permalink: /maths/
---

<div class="row">
  <div class="column">
    <h2></h2>

    <ul class="post-list">
      {% for post in site.posts %}
      <li>
        {% if  post.categories contains 'maths' %}
        {% unless post.categories contains 'euler' %}
        {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
        <div>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
          <span class="post-meta"> {{ post.date | date: date_format }}</span>
        </div>
        {% endunless %}
        {% endif %}
      </li>
      {% endfor %}
    </ul>


  </div>
  <div class="column">
    <h3>Project Euler </h3>
    <img src="https://projecteuler.net/profile/sparkyyyy.png" style="padding-bottom:23px">
    <ul class="post-list">
      {% for post in site.posts %}
      <li>
        {% if post.categories contains 'euler' %}
        {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
        <div>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
          <span class="post-meta"> {{ post.date | date: date_format }}</span>
        </div>
        {% endif %}
      </li>
      {% endfor %}
    </ul>

  </div>
</div>
