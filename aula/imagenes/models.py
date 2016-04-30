from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    server = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Server(models.Model):
    address = models.CharField(max_length=100)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.address
