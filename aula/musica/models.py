from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    server = models.CharField(max_length=255)

class Artist(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    image = models.ForeignKey(Song, on_delete=models.CASCADE)