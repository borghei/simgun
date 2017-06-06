from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile


class SupportAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    agent = models.ForeignKey(SupportAgent)
    customer = models.ForeignKey(UserProfile)
    status_choices = (
        (0, 'پرسیده شده'),
        (1, 'پاسخ داده شده'),
        (2, 'بسته شده')
    )
    status = models.IntegerField(choices=status_choices)


class Message(models.Model):
    content = models.CharField(max_length=4096)
    ticket = models.ForeignKey(Ticket)
    owner = models.BooleanField(choices=((1, 'agent'), (0, 'customer')))

