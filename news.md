---
layout: page
title: News
description: Announcements, releases, and reports from the PESO Project.
section_tag: Updates
permalink: /news
---

<div class="log">
{% for news in site.data.news %}
<div class="log-row"><span class="log-date mono">{{ news.date }}</span><a href="{{ news.link }}">{{ news.title }}</a></div>
{% endfor %}
</div>
