from django_elasticsearch_dsl import DocType, fields, Index
from pypilogger.models import Package

package_index = Index("packages")

package_index.settings(number_of_shards=1, number_of_replicas=0)

@package_index.doc_type
class PackageDocument(DocType):
    title = fields.TextField(attr="title", fields={"suggest": fields.Completion()})
    description = fields.TextField(attr="description", fields={"suggest": fields.Completion()})
    author = fields.TextField(attr="author", fields={"suggest": fields.Completion()})
    author_email = fields.TextField(attr="author_email", fields={"suggest": fields.Completion()})
    keywords = fields.TextField(attr="keywords", fields={"suggest": fields.Completion()})
    version = fields.TextField(attr="version", fields={"suggest": fields.Completion()})
    maintainer = fields.TextField(attr="maintainer", fields={"suggest": fields.Completion()})
    maintainer_email = fields.TextField(attr="maintainer_email", fields={"suggest": fields.Completion()})
