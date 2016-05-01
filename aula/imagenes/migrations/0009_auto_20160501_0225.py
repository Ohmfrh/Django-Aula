# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 02:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imagenes', '0008_auto_20160501_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='multimedia.Server'),
        ),
        migrations.DeleteModel(
            name='Server',
        ),
    ]
