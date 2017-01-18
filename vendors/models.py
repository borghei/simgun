from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/site-media/photos/profiles/', blank=True, null=True,
                               default='static/site-media/photos/profiles/matthew.png')