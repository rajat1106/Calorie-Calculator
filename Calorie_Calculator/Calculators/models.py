from django.db import models
from django.db.models.base import Model

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=40)
    cpassword = models.CharField(max_length=40)



