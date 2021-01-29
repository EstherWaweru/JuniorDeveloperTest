from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#table for Custom User
class CustomUser(AbstractUser):
   
    company=models.ForeignKey(Company,blank=True,null=True,on_delete=models.CASCADE)
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
    phone_number=models.CharField(validators=[mobile_num_regex],max_length=13,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


#table for Companies
class Company(models):
    name=models.CharField(max_length=50,blank=False,unique=True)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    logo=models.FileField(blank=True,null=True)
    website=models.URLField(max_length=250,db_index=True, unique=True, blank=True)


