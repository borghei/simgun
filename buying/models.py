from django.db import models

from accounts.models import UserProfile
from books.models import Book
from profiles.models import Address


class ShoppingbagAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_count = models.IntegerField(default=1)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
