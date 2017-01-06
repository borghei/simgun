from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Book(models.Model):
    isbn = models.IntegerField(default=0, null=True)
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=63)
    translator = models.CharField(max_length=63, default='', null=True, blank=True)
    description = models.CharField(max_length=511)
    page_count = models.IntegerField(default=0)
    publisher = models.CharField(max_length=127)
    price = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='static/media/photos/books/', blank=True, null=True, default='')

    def __str__(self):
        return self.title + ' - ' + self.publisher