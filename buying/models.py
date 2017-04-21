from django.db import models

from .models import UserProfile
from books.models import Book


class Address(models.Model):
    Province = models.CharField(max_length=128)
    city = models.CharField(max_length=256)
    phone_number = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
    address = models.CharField(max_length=1024)


class ShoppingbagAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_count = models.IntegerField(default=1)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
