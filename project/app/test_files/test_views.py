from django.test import TestCase
import requests
from django.urls import reverse_lazy
from app.forms import ProductForm
from django.views.generic import View
from decimal import Decimal

class MyFormViewTest(TestCase):
    def setUp(self):
        self.req__validdata = {
            'name': 'skjdbf',
            'price': 123.43
        }
        self.req__invaliddata = {
            'name': 'skjdbf',
            'price': 12334.43
        }

    def test_view(self):
        url = reverse_lazy('form_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['view'], View)
        self.assertTemplateUsed(response, 'form_test.html')
        response = self.client.get('http://localhost:8000/form-view/1/')
        self.assertEqual(response.status_code, 404)
        response = self.client.post(url, self.req__validdata)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('test_tags'))
        response = self.client.post(url, self.req__invaliddata)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form_test.html')
        