# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 22:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_auto_20160428_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersys',
            name='date_added',
            field=models.DateField(default=datetime.date(2016, 4, 30), verbose_name='Fecha de alta'),
        ),
    ]
