# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0015_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersys',
            name='logged',
            field=models.CharField(choices=[('0', 'No'), ('1', 'Yes')], default=0, max_length=1),
        ),
    ]
