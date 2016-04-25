from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Identify(models.Model):
    string = models.CharField(max_length=255)

class Type():
    name = models.CharField(max_length=50)
    identify = models.ForeignKey(Identify, on_delete=models.CASCADE)
