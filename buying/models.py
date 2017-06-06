from django.db import models

from accounts.models import UserProfile, Vendor
from product.models import Product

cities = {
    'تهران': ('تهران'),
    'البرز': ('کرج')
}


class PostPrice(models.Model):
    province = models.CharField(max_length=128)
    city = models.CharField(max_length=256)
    vendor = models.ForeignKey(Vendor)
    price = models.IntegerField(default=0)
    type = models.BooleanField(choices=((0, 'پست'), (1, 'پیک')))


class Address(models.Model):
    province = models.CharField(max_length=128)
    city = models.CharField(max_length=256)
    phone_number = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
    address = models.CharField(max_length=1024)


class ShoppingbagAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=1)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
