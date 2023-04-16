from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    role=[
        ('team member','Team Member'),
        ('team head','Team Head'),
        ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=50,choices=role,default="team Members")
    

    def __str__(self):
        return self.name 

class Employees(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)#
    role=[
        ('team member','Team Member'),
        ('team head','Team Head'),
        ]
    empid = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=50,choices=role,default="team Members")
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
       # emp = models.ForeignKey(Employees, on_delete=models.CASCADE, null=True)
    ptitle = models.CharField(max_length=100)
    pdesc = models.CharField(max_length=200)
    
    def __str__(self):
        return self.ptitle


class Task(models.Model):
    status=[
        ('Started','Started'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
        ]
    
    ptitle = models.OneToOneField(Project,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50,choices=status,default="In Progress")
    


    