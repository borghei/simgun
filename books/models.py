from datetime import datetime

from django.db import models

from accounts.models import UserProfile


class BookCategory(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Book(models.Model):
    isbn = models.IntegerField(default=0, null=True)
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=63)
    translator = models.CharField(max_length=63, default='', null=True, blank=True)
    description = models.CharField(max_length=1024)
    page_count = models.IntegerField(default=0)
    publisher = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='static/site-media/photos/books/', blank=True, null=True, default='')
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title + ' - ' + self.publisher


class BookReview(models.Model):
    text = models.CharField(max_length=512)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title + ' - ' + str(self.book)


class BookRating(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
