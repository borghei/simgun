from django.db import models

from product.models import Product


class MainShowcase(models.Model):
    img = models.ImageField(upload_to='static/site-media/photos/profiles/', null=False)
    book = models.OneToOneField(Product, on_delete=models.CASCADE)