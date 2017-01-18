# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='image/')),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
    ]
