---
title: "SIRIUS Lab - Grants"
layout: textlay
excerpt: "SIRIUS Lab -- Grants"
sitemap: false
permalink: /grants/
---

# Grants

{% assign org = none %}

{% for grant in site.data.grants | group_by:"org" %}

{% if grant.org != org %}
### {{ grant.org }}
{% endif %}

{% assign org = grant.org %}

<b>Title: </b> {{ grant.title }}<br>
<b>Amount Awarded: </b> {{ grant.amount }}<br>
{% if grant.link != None %}
More information can be found <a href="{{ grant.link }}">here</a>
{% endif %}

<br>
{% endfor %}

