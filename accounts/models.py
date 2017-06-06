from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='static/site-media/photos/profiles/', blank=True, null=True,
                               default='static/site-media/photos/profiles/matthew.png')

    def __str__(self):
        return str(self.user)


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/site-media/photos/profiles/', blank=True, null=True,
                               default='static/site-media/photos/profiles/matthew.png')

    def __str__(self):
        return str(self.user)



