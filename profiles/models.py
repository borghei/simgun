from django.db import models
from accounts.models import UserProfile

from ketabkhor.models import Book


class WishlistBook(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_profile) + ' - ' + str(self.book)
