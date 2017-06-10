from datetime import datetime

from django.db import models

from accounts.models import UserProfile


class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


def _get_image_filename():
    return 'static/site-media/photos/product/'


class Product(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=2048)  # max_length is in chars
    price = models.IntegerField(default=0)
    mainPic = models.ImageField(upload_to=_get_image_filename, blank=True, null=True, default='')
    # boundary will be chekckeed on views
    itemCount = models.IntegerField(default=0)
    off = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    orderCount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def get_cost(self):
        return self.price * ((100 - self.off)/100)

    def __str__(self):
        return self.title  # + ' - ' + self.publisher



class ProductImage(models.Model):
    post = models.ForeignKey(Product, default=None)
    image = models.ImageField(upload_to=_get_image_filename,
                              verbose_name='Image', )


class Review(models.Model):
    text = models.CharField(max_length=512)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title + ' - ' + str(self.book)


class Rating(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return str(self.book) + ' - ' + str(self.user_profile) + ' - ' + str(self.rate)