from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usersys

# Create your models here.
class Server(models.Model):
    address = models.CharField(max_length=100)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.address


class Image(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    server = models.ForeignKey(Server, blank=True, null=True)
    users = models.ManyToManyField(Usersys, through='UserImage', blank=True, null=True)

    def __str__(self):
        return self.name


class UserImage(models.Model):
    user = models.ForeignKey(Usersys)
    image = models.ForeignKey(Image)
