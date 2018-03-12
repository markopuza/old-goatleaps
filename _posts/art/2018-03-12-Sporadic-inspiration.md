---
layout: post
title:  "Sporadic inspiration"
date:   2018-03-12 01:38:59 +0000
category-string: "Art"
categories: art media
---

<script type="text/javascript" src="/assets/script/instafeed.min.js"></script>
<script type="text/javascript">
    var feed = new Instafeed({
        get: 'user',
        sortBy: 'most-recent',
        userId: '4458149796',
        accessToken: '4458149796.1677ed0.7cea947e0c7a4f59a3561113bf2f82c7',
        resolution: 'low_resolution',
        filter: function(image) {
          return image.likes.count >= 5;
        }
    });
    feed.run();
</script>

<p align="center"> Irregular dose of quality art. Follow on <a href="https://www.instagram.com/sporadic_inspiration/"> >> Instagram  <<</a>. </p>

<img src="{{ site.baseurl }}/assets/icon/sporadic.png" align="left" style="width:60px; margin-right: 10px;">
<h2> Most recent artwork </h2>
<div id="instafeed"></div>
