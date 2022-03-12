from email.policy import default
from operator import mod
from re import T
from xmlrpc.client import DateTime
from django.db import models
from django.db.models import Model
from django.forms import DateTimeField


# from django.contrib.auth.models import User
# SERVICE_CHOICES = (
#     ("Web Development", "Web Development"),
#     ("Digital Marketing", "Digital Marketing"),
#     ("Blogging", "Blogging"),
#     ("V-logging", "V-logging"),
#     ("Later", "Later"),
# )

# Create your models here.

class Client(models.Model):
 name= models.CharField(max_length=100)
 email= models.EmailField(max_length=100)
 password= models.CharField(max_length=50)
 created = models.DateField(DateTimeField, null=True)
#  service_type = models.CharField(max_length = 20,choices = SERVICE_CHOICES,default = '1')
#  files = models.FileField(upload_to='files/', null=True, blank=True)


 def __str__(self):
  return self.name



