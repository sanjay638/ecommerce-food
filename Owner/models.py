from django.db import models

# Create your models here.




class AdminModel(models.Model):
    Productname = models.CharField(max_length=100)
    Productid = models.IntegerField()
    Quality = models.IntegerField()
    uploadimage = models.ImageField()
    gram = models.IntegerField()
    Description = models.CharField(max_length=100)
    amount = models.IntegerField()


class Adminregister_Model(models.Model):
    adminid = models.IntegerField()
    name= models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=10)
    phoneno=models.CharField(max_length=15)
    address=models.CharField(max_length=500)
    dob=models.CharField(max_length=20)