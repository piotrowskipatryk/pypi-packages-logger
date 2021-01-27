from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from pypilogger.documents import PackageDocument


class PackageDocumentSerializer(DocumentSerializer):
    class Meta:
        document = PackageDocument
        fields = (
            'title',
            'description',
            'author',
            'author_email',
            'maintainer',
            'maintainer_email',
            'version',
        )
