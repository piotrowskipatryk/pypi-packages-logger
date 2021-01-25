from pypilogger.models import Package
from pypilogger.celery import app as celery_app


@celery_app.task
def import_newest_packages():
    return "ok"
