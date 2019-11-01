from django.test import TestCase
from app.models import *
from decimal import Decimal 
import math

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Un memulati")

    def test_get_category(self):
        self.assertEqual(self.category.title, Category.objects.get(id=1).title)

    def test_str(self):
        created_object = Category.objects.get(id=1)
        self.assertEqual(self.category.title, created_object.__str__())


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Un memulati")
        self.product = Product.objects.create(name="Sirniyyat", category=self.category, price=Decimal(123.05))
        self.product2 = Product.objects.create(name="Sirniyyat2", category=self.category, price=Decimal(123.04))

    def test_get_category(self):
        self.assertEqual(self.product, Product.objects.get(id=1))
        self.assertEqual(self.product2, Product.objects.get(id=2))

    def test_str(self):
        created_object = Product.objects.get(id=1)
        self.assertEqual(self.product.name + " "+ self.category.title, created_object.__str__())
        created_object = Product.objects.get(id=2)
        self.assertEqual(self.product2.name + " "+ self.category.title, created_object.__str__())

    def test_rounded_price(self):
        self.assertEqual(math.ceil(self.product.price), Product.objects.get(id=1).get_rounded_price())
        self.assertEqual(math.ceil(self.product2.price), Product.objects.get(id=2).get_rounded_price())