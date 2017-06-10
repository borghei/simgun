from django.db import models

from accounts.models import UserProfile, Vendor
from product.models import Product


class PostPrice(models.Model):
    province = models.CharField(max_length=128)
    city = models.CharField(max_length=256)
    vendor = models.ForeignKey(Vendor)
    price = models.IntegerField(default=0)
    type_choices = ((0, 'پست'), (1, 'پیک'))
    type = models.BooleanField(choices=type_choices)

    cities = [
        ['تهران', ['تهران', 'شمیرانات', 'آزادی']],
        ['البرز', ['کرج', 'مصباح ', 'کرج']]
    ]

    def get_type_str(self):
        return self.type_choices[self.type][1]


class Address(models.Model):
    validity = models.BooleanField(default=1)
    province = models.CharField(max_length=128)
    city = models.CharField(max_length=256)
    phone_number = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
    address = models.CharField(max_length=1024)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    def get_full_address(self):
        return str(self.province) + '-' + str(self.city) + '-' + str(self.address)