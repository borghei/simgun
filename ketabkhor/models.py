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


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.IntegerField(default=0)
    user_type = models.IntegerField(default=1)
    password_hash = models.CharField(max_length=511)


class BookReview(models.Model):
    title = models.CharField(max_length=127)
    author = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    score = models.IntegerField(default=0)


class KetabYar(models.Model):
    name = models.CharField(max_length=127)
    address = models.CharField(max_length=511)
    phone = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    password_hash = models.CharField(max_length=511)


class BlogAdmin(models.Model):
    name = models.IntegerField(default=0)
    password_hash = models.CharField(max_length=511)


class BlogPost(models.Model):
    id = models.IntegerField(default=0)
    title = models.CharField(max_length=127)
    context = models.CharField(max_length=2047)
    author = models.CharField(max_length=32)
    date = models.IntegerField(default=0)
    time = models.IntegerField(default=0)


class BlogPostComment(models.Model):
    title = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    author = models.CharField(max_length=32)
    date = models.IntegerField(default=0)


class StudyProgram(models.Model):
    isbn = models.IntegerField(default=0)
    current_page = models.IntegerField(default=0)


class SupportTicket(models.Model):
    title = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    date = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
