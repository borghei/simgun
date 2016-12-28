from django.db import models


# Create your models here.


class Book(models.Model):
    isbn = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=63)
    translator = models.CharField(max_length=63)
    description = models.CharField(max_length=511)
    page_count = models.IntegerField(default=0)
    publisher = models.CharField(max_length=127)
    price = models.IntegerField(default=0)


class Order(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    status = models.CharField(max_length=127)
    address = models.CharField(max_length=511)
    phone_number = models.IntegerField(default=0)
    zip_code = models.IntegerField(default=0)
