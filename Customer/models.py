from tkinter import CASCADE

from django.db import models



# Create your models here.
from Owner.models import AdminModel



class UserRegistration(models.Model):
    firstname = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender =models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Addtocard_Model(models.Model):
    userid = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    salesid = models.ForeignKey(AdminModel, on_delete=models.CASCADE)
    Quality = models.IntegerField()
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    amount = models.IntegerField()
    requeststatus = models.CharField(default='PROCESS', max_length=300)

class Feeback_Model(models.Model):
    name = models.CharField(max_length=50)
    productname = models.CharField(max_length=50)
    ratings = models.CharField(max_length=10)
    feedback = models.CharField(max_length=500,blank=True,null=True)

