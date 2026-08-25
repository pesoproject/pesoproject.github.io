---
title: Documents
description: Annual reports, E4S release notes, papers, and other PESO publications.
section_tag: Updates
layout: page
permalink: /news/documents
---

<div class="log">
{% for item in site.data.news %}
{% if item.category == 'document' %}
<div class="log-row"><span class="log-date mono">{{ item.date }}</span><a href="{{ item.link }}">{{ item.title }}</a></div>
{% endif %}
{% endfor %}
</div>
