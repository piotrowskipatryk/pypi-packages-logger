from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from pypilogger.tasks import import_newest_packages


class TasksTestCase(TestCase):

    def test_import_newest_packages(self):
        """
            Tests if newest packages can be downloaded.
            This test has to be done with elasticsearch test server started.
        """
        self.assertEqual(import_newest_packages(), 'ok')


class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_api_packages_get(self):
        """ Tests if packages can be got from API. """
        response = self.client.get(reverse('packages-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), list)

    def test_api_packages_searching(self):
        """ Tests if packages can be searched. """
        response = self.client.get(f"{reverse('packages-list')}?search=title|pypi")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), list)
