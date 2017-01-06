from django.db import models


# Create your models here.


class Book(models.Model):
    isbn = models.IntegerField(default=0, null=True)
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=63)
    translator = models.CharField(max_length=63, default='', null=True)
    description = models.CharField(max_length=511)
    page_count = models.IntegerField(default=0)
    publisher = models.CharField(max_length=127)
    price = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='static/media/photos/books/', blank=True, null=True, default='')


class Address(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    address = models.CharField(max_length=511)
    phone_number = models.IntegerField(default=0)
    zip_code = models.IntegerField(default=0)


class Order(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    status = models.CharField(max_length=127)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default='')


class User(models.Model):
    user_name = models.CharField(max_length=32, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.IntegerField(default=0)
    user_type = models.IntegerField(default=1)
    password_hash = models.CharField(max_length=511)


class BookReview(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    rate = models.IntegerField(default=0)


class Vendor(models.Model):
    user_name = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=127)
    address = models.CharField(max_length=511)
    phone_number = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    password_hash = models.CharField(max_length=511)


class BlogAdmin(models.Model):
    user_name = models.CharField(max_length=32, primary_key=True)
    name = models.IntegerField(default=0)
    password_hash = models.CharField(max_length=511)


class BlogPost(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=127)
    context = models.CharField(max_length=2047)
    author = models.CharField(max_length=32)
    date = models.DateTimeField(default=0)


class BlogComment(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    author = models.CharField(max_length=32)
    date = models.DateTimeField()


class ReadingProgram(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    current_page = models.IntegerField(default=0)


class SupportTicket(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    date = models.DateTimeField()
