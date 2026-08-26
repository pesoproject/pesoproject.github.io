---
layout: page
title: PESO Project Thrusts
description: Six parallel work areas, each shipping into the same shared scientific software ecosystem.
section_tag: Program structure
permalink: /thrusts
---

Efforts in the PESO Project are organized into six thrust areas, each focusing on a specific aspect of scientific software development and deployment in the context of advanced high-performance computing (HPC). These thrusts are designed to address key challenges and opportunities in the field, with the goal of advancing the state of the art in scientific computing and enabling researchers to leverage the full potential of HPC resources.

They are parallel, not sequential — each ships independently into the same shared ecosystem.

<div class="thrust-grid" style="margin-top:8px;">
{% for t in site.data.thrusts %}
{% if t.link %}<a class="thrust" href="{{ t.link }}">{% else %}<div class="thrust">{% endif %}
    <span class="thrust-code">{{ t.code }}</span>
    <h3>{{ t.title }}</h3>
    <p>{{ t.description }}</p>
{% if t.link %}</a>{% else %}</div>{% endif %}
{% endfor %}
</div>
