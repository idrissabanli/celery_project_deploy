from django.db import models
import math
# Create your models here.

class Category(models.Model):
    title = models.CharField('Title', max_length=25)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField('Name', max_length=25)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField('Price', max_digits=5, decimal_places=2)
    image = models.ImageField('Image', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.category.title

    def get_rounded_price(self):
        return math.ceil(self.price)