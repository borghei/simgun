# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-01 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
