# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 00:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagenes', '0006_auto_20160430_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userimage',
            old_name='Image',
            new_name='image',
        ),
    ]
