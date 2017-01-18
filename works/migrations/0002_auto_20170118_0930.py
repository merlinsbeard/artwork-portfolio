# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AddField(
            model_name='workimage',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.Work'),
        ),
    ]
