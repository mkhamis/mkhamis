---
title: "SIRIUS Lab - Publications"
layout: gridlay
excerpt: "SIRIUS Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

## Group highlights

(For a full list see [below](#full-list) or go to [Google Scholar](https://scholar.google.com/citations?user=0OupgU0AAAAJ), [OrcID](https://orcid.org/0000-0001-7051-5200))

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
{% if publi.award != "" %}
  <p class="text-danger"><strong> {{ publi.award }}</strong></p>
{% endif %}
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>


## Journal articles

{% for publi in site.data.publist %}

{% if publi.type == "journal" %}

{{ publi.title }} <br />
<em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endif %}

{% endfor %}

## Book Chapters

{% for publi in site.data.publist %}
	
{% if publi.type == "bookchapter" %}

{{ publi.title }} <br />
<em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endif %}

{% endfor %}

## Magazine articles

{% for publi in site.data.publist %}

{% if publi.type == "magazine" %}

{{ publi.title }} <br />
<em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endif %}

{% endfor %}

## Conference papers

{% for publi in site.data.publist %}

{% if publi.type == "conference" %}

{{ publi.title }} <br />
<em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endif %}

{% endfor %}

## Other publications (peer-reviewed workshop papers and proposals, and juried late-breaking-work papers).

{% for publi in site.data.publist %}

{% if publi.type == "workshop" && publi.type == "Late-Breaking-Work" && publi.type == "conference" %}

{{ publi.title }} <br />
<em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endif %}

{% endfor %}

