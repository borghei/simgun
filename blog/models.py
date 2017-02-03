from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    content = models.CharField(max_length=9096)
