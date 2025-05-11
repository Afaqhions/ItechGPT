# importing db 
from django.db import models
# Creating table
class message(models.Model):
    usr_name = models.CharField(max_length=50,unique=True)
    usr_message = models.TextField()