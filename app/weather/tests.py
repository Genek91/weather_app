import unittest
from django.test import Client


class WeatherTests(unittest.TestCase):

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
