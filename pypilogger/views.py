from django.shortcuts import render
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch
from pypilogger.documents import PackageDocument

def index(request):
    q = request.GET.get('q', False)
    context = {"packages": []}
    if q:
        query = MultiMatch(query=q, fields=['author', 'author_email', 'author', 'description', 'title', 'keywords', 'version', 'maintainer', 'maintainer_email'], fuzziness='AUTO')
        s = Search(index='packages').query(query)
        context["packages"] = s.execute()
    else:
        s = Search(index='packages')
        context["packages"] = s.execute()

    return render(request, 'index.jinja', context)
