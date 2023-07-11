from django.db import models

def upload_path(instance,filename):
     return '/'.join(['profile',str(instance.FirstName),filename])


class RoleChoices(models.TextChoices):
    GENERAL_USER = 'General User'
    ADMIN = 'Admin'
# Create your models here.
class employee(models.Model):
    FirstName=models.CharField(max_length=20,blank=True,null=True)
    LastName=models.CharField(max_length=20,blank=True,null=True)
    Gender=models.CharField(max_length=20,blank=True,null=True)
    DOB=models.DateField(blank=True,null=True)
    email=models.EmailField(primary_key=True)
    Mobno=models.CharField(blank=True,max_length=10)
    address=models.TextField(max_length=100,blank=True)
    Department=models.CharField(max_length=20,blank=True)
    Designation=models.CharField(max_length=30,blank=True)
    AadharNumber=models.CharField(blank=True,null=True,max_length=20)
    uname=models.CharField(max_length=20,unique=True)
    password=models.CharField(blank=False,max_length=20)
    conpass=models.CharField(blank=True,max_length=20)
    ProfileImage=models.ImageField(blank=True,null=True,upload_to=upload_path)
    AadharImage=models.ImageField(blank=True,null=True,upload_to=upload_path)
    roles=models.CharField(choices=RoleChoices.choices,default=RoleChoices.GENERAL_USER,max_length=12)
    def __str__(self):
        data=f"{self.FirstName}  {self.LastName}"
        return data