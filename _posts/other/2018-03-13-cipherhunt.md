---
layout: post
title:  "Cipher Hunt"
date:   2018-03-13
category-string: "Other"
categories: other
icon: ciphericon
---

During the first semester of the 2017/18 university year I took part in organisation of a Cipherhunt (together with a great deal of work by [>>Simon<<](https://uk.linkedin.com/in/simon-holm-b57578106) and [>>Lukas<<](https://github.com/lcapkovic)). This involved
a variety of classical as well as unusual ciphers/teasers being hidden around the campus. Upon solving one of them,
one would obtain instructions on where to collect the next one.

The Cipherhunt is/was online at [www.cipherhunt.info](http://www.cipherhunt.info), but for anyone interested I include the whole content below!


<div align="center">
 <img src="/assets/image/cipherhunt/poster.png" width="80%">

 <a style="font-size: 40px; font-weight:bold; margin:20px; color:#666;" href="/assets/pdf/Cipher_Hunt_Brochure.pdf">
  Instructions
  </a>

</div>

<ul class="post-list">
  {% for post in site.posts reversed %}
  <li>
    {% if  post.categories contains 'cipherhunt' %}
    {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
    <div align="center">
      <a style="font-size: 40px; font-weight:bold; margin:20px; color:#666;" href="{{ post.url | relative_url }}">
        {{ post.title | escape }}
      </a>
    </div>
    {% endif %}
  </li>
  {% endfor %}
</ul>
