from django.test import TestCase
from app.forms import *

class ProductFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'product1',
            'price': 123.5
        }
        self.invalid_data = {
            'name': 'skdlnf',
            'price': 12234.5
        }

    def test_product_form(self):
        form = ProductForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        form = ProductForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
