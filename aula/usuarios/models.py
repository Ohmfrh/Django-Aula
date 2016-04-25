from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=50)
    last_names = models.CharField(max_length=100)
    date_added = models.DateTimeFIeld('Fecha de alta')
