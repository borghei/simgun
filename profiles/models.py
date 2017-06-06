from django.db import models
from accounts.models import UserProfile

from product.models import Product


class Bag(models.Model):
    date = models.DateTimeField(auto_now=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class ShoppingbagBook(models.Model):
    bag = models.ForeignKey(Bag, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=1)
    price = models.IntegerField(default=0)


