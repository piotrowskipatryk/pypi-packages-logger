from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FacetedSearchFilterBackend,
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from pypilogger.documents import PackageDocument
from pypilogger.serializers import PackageDocumentSerializer


class PackageViewSet(DocumentViewSet):
    document = PackageDocument
    serializer_class = PackageDocumentSerializer
    lookup_field = 'title'

    filter_fields = {
        'title': 'title',
    }

    filter_backends = [
        DefaultOrderingFilterBackend,
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = (
        'author',
        'author_email',
        'author',
        'description',
        'title',
        'keywords',
        'version',
        'maintainer',
        'maintainer_email'
    )
