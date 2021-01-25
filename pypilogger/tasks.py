import requests
import xmltodict
import dateutil.parser
from pypilogger.models import Package
from pypilogger.celery import app as celery_app
from django.db import transaction


@celery_app.task
def import_newest_packages():
    url = 'https://pypi.org/rss/packages.xml'
    response = requests.get(url)
    data = xmltodict.parse(response.content)

    with transaction.atomic():
        for item in data['rss']['channel']['item']:
            pkg = Package.objects.create(
                title=item['title'],
                link=item['link'],
                guid=item['guid'],
                description=item['description'],
                author_email=item['author'] if 'author' in item else None,
                pub_date=dateutil.parser.parse(item['pubDate']),
            )
            pypi_name = item['link'].split("/")[-2]
            url = f'https://pypi.org/pypi/{pypi_name}/json'
            response = requests.get(url).json()

            pkg.author = response['info']['author']
            pkg.keywords = response['info']['keywords']
            pkg.version = response['info']['version']
            pkg.maintainer = response['info']['maintainer']
            pkg.maintainer_email = response['info']['maintainer_email']
            pkg.save()

    return "ok"
