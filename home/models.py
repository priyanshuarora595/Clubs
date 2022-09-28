from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=30,null=True)
    semester = models.CharField(max_length=10,null=True)
    contact_number = models.CharField(max_length=10,null=True)
    email_id = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class incharge(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    
    def __str__(self):
        return self.name
    
class club(models.Model):
    club_name= models.CharField(max_length=50,primary_key=True)
    club_description = models.TextField()
    club_incharge = models.ForeignKey(incharge,on_delete=models.SET_DEFAULT,null=True,blank=True,default="None")
    
    def __str__(self):
        return self.club_name
    
    
class Gaming(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=30,null=True)
    semester = models.CharField(max_length=10,null=True)
    contact_number = models.CharField(max_length=10,null=True)
    email_id = models.EmailField(max_length=100)
    
    
    def __str__(self):
        return self.first_name + " " + self.last_name