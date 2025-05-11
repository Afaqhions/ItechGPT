from django.db import models

# Create your models here.
class usrReg(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    user_name = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=25,unique=True)
    password = models.CharField(max_length=25,unique=True)