# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagenes', '0001_initial'),
        ('usuarios', '0007_usersys_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersys',
            name='images',
            field=models.ManyToManyField(default=None, to='imagenes.Image'),
        ),
    ]
