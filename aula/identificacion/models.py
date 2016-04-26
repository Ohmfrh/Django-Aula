from __future__ import unicode_literals

from django.db import models
from usuarios.models import Usersys


# Create your models here.
class Identify(models.Model):
    string = models.CharField(max_length=255)
    usersys = models.ForeignKey(Usersys, on_delete=models.CASCADE, default=None)

class Type():
    name = models.CharField(max_length=50)
    #identify = models.ForeignKey(Identify, on_delete=models.CASCADE)
