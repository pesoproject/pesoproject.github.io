---
title: Events
description: PI meetings, BOF days, conference presence, and other PESO appearances.
section_tag: Updates
layout: page
permalink: /news/events
---

<div class="log">
{% for item in site.data.news %}
{% if item.category == 'event' %}
<div class="log-row"><span class="log-date mono">{{ item.date }}</span><a href="{{ item.link }}">{{ item.title }}</a></div>
{% endif %}
{% endfor %}
</div>
