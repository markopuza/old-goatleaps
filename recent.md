---
layout: page
title: Recent
permalink: /recent/
---

<div style="overflow-x: auto;">
<table class="recent-table">
  <tr>
    <th> Post </th>
    <th> Category </th>
    <th> Date </th>
  </tr>
    {% for post in site.posts %}
    {% unless post.categories contains 'noshow' %}
    <tr>
      {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
      <td>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </td>
      <td>
        {{ post.category-string }}
      </td>
      <td>
        <span class="post-meta"> {{ post.date | date: date_format }}</span>
      </td>
    </tr>
    {% endunless %}
    {% endfor %}
</table>
</div>
