from http import HTTPStatus

import unittest
from django.test import Client


class WeatherTests(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_form_display(self):
        response = self.client.get('/')
        self.assertIn('form', response.context)
