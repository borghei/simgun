from django.db import models

from books.models import Book


class MainShowcase(models.Model):
    img = models.ImageField(upload_to='static/site-media/photos/profiles/', null=False)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)