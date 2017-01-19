from django.db import models
from accounts.models import UserProfile

from books.models import Book


class WishlistBook(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_profile) + ' - ' + str(self.book)


class ShoppingbagBook(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_count = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user_profile) + ' - ' + str(self.book)


class Address(models.Model):
    ostan = models.CharField(max_length=128)
    city = models.CharField(max_length=256)
    phone_number = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
    address = models.CharField(max_length=1024)