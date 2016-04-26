# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 02:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('identificacion', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='D',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('last_names', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(verbose_name='Fecha de alta')),
                ('identification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identificacion.Identify')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]