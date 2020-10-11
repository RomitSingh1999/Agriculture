from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Data(models.Model):
    Name = models.CharField(max_length=30,default=None)
    Minimum = models.CharField(max_length=10,default=None)
    Rainfall = models.CharField(max_length=10,default=None)
    Humid = models.BooleanField(default=False)
    Soil = models.CharField(max_length=200,default=None)
    Area = models.CharField(max_length=200,default=None)
class savedata(models.Model):
    city = models.CharField(max_length=30)
    temp = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
    wind =models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)