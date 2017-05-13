from django.db import models

from accounts.models import UserProfile
from product.models import Product


class Address(models.Model):
    Province = models.CharField(max_length=128)
    city = models.CharField(max_length=256)
    phone_number = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
    address = models.CharField(max_length=1024)


class ShoppingbagAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Product, on_delete=models.CASCADE)
    book_count = models.IntegerField(default=1)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
