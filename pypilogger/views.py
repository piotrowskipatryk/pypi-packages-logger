import os
from django.shortcuts import render
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch
from django.core.paginator import Paginator
from pypilogger.documents import PackageDocument

def index(request):
    q = request.GET.get('q', False)
    p = request.GET.get('page', 1)
    per_page = os.environ.get('PACKAGES_ON_SITE', 5)
    context = {"packages": []}
    if q:
        query = MultiMatch(query=q, fields=['author', 'author_email', 'author', 'description', 'title', 'keywords', 'version', 'maintainer', 'maintainer_email'], fuzziness=1)
        s = Search(index='packages')[0:70].query(query)
        context["packages"] = Paginator(s.execute(), per_page).page(p)
    else:
        s = Search(index='packages')
        context["packages"] = Paginator(s.execute(), per_page).page(p)

    return render(request, 'index.jinja', context)
