# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 23:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20160430_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersys',
            name='images',
        ),
        migrations.RemoveField(
            model_name='usersys',
            name='songs',
        ),
    ]