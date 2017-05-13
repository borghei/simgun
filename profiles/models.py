from django.db import models
from accounts.models import UserProfile

from product.models import Product


class WishlistBook(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_profile) + ' - ' + str(self.book)


class ShoppingbagBook(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Product, on_delete=models.CASCADE)
    book_count = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user_profile) + ' - ' + str(self.book)


class ReadingProgram(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Product, on_delete=models.CASCADE)
    current_page = models.IntegerField(default=0)

    def get_reading_percent(self):
        return int(float(self.current_page / self.book.page_count) * 100)

    def __str__(self):
        return str(self.user_profile) + ' - ' + str(self.book)
