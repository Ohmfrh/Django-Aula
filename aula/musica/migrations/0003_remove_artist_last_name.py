# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 21:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0002_auto_20160426_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='last_name',
        ),
    ]