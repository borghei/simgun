# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
