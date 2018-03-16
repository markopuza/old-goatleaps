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
          <img class="post-icon" src="/assets/icon/{{ post.icon }}.png">
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
    <img src="https://projecteuler.net/profile/sparkyyyy.png" style="padding-bottom:23px">
    <p>
     Below, you can find some guidance for Project Euler problems. If you are looking for a readily available copy/paste answer, you will not find it here. All of the code snippets in the posts have been stripped of some crucial lines (these are clearly marked). It is my aim that anyone able to replicate the answer based on such snippets will have to understand the solution conceptually in the first place.
    </p>
    <ul class="post-list">
      {% for post in site.posts %}
      <li>
        {% if post.categories contains 'euler' %}
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
</div>
