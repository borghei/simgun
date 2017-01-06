from django.db import models


# Create your models here.


class Book(models.Model):
    isbn = models.IntegerField(default=0)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    translator = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    page_count = models.IntegerField(default=0)
    publisher = models.CharField(max_length=128)
    price = models.IntegerField(default=0)


class Address(models.Model):
    address = models.CharField(max_length=511)
    phone_number = models.IntegerField(default=0)
    zip_code = models.IntegerField(default=0)


class Order(models.Model):
    status = models.CharField(max_length=127)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default='')


class BookReview(models.Model):
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    rate = models.IntegerField(default=0)


class BlogPost(models.Model):
    title = models.CharField(max_length=127)
    context = models.CharField(max_length=2047)
    author = models.CharField(max_length=32)
    date = models.DateTimeField(default=0)


class BlogComment(models.Model):
    title = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    author = models.CharField(max_length=32)
    date = models.DateTimeField()


class ReadingProgram(models.Model):
    current_page = models.IntegerField(default=0)


class SupportTicket(models.Model):
    title = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    date = models.DateTimeField()
