# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagenes', '0011_auto_20160501_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='users',
            field=models.ManyToManyField(blank=True, through='imagenes.UserImage', to='usuarios.Usersys'),
        ),
    ]