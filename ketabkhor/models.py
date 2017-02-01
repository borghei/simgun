from django.contrib.auth.models import User
from django.db import models



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


class SupportTicket(models.Model):
    title = models.CharField(max_length=63)
    context = models.CharField(max_length=511)
    date = models.DateTimeField()
