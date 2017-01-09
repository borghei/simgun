# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField(default=0, null=True)),
                ('title', models.CharField(max_length=127)),
                ('author', models.CharField(max_length=63)),
                ('translator', models.CharField(blank=True, default='', max_length=63, null=True)),
                ('description', models.CharField(max_length=511)),
                ('page_count', models.IntegerField(default=0)),
                ('publisher', models.CharField(max_length=128)),
                ('price', models.IntegerField(default=0)),
                ('pic', models.ImageField(blank=True, default='', null=True, upload_to='static/media/photos/books/')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.CharField(max_length=512)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='books.BookCategory'),
        ),
    ]
