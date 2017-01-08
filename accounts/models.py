from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='static/media/photos/profiles/', blank=True, null=True,
                               default='static/media/photos/profiles/matthew.png')

