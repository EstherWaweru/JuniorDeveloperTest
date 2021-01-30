from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.files.images import get_image_dimensions



#table for Companies
def validate_image(fieldfile_obj):
    if  fieldfile_obj:
        w, h = get_image_dimensions(fieldfile_obj)
    if w < 100:
        raise ValidationError("The image is %i pixel narrow. It's supposed to be wider than 100px" % w)
    if h < 100:
        raise ValidationError("The image is %i pixel low. It's supposed to be higher than 100px" % h)
class Company(models.Model):
    name=models.CharField(max_length=50,blank=False,unique=True)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    logo=models.ImageField( upload_to="logo",validators=[validate_image],blank=True,null=True)
    website=models.URLField(max_length=250,db_index=True, unique=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
# def clean(self):
#     if  self.logo:
#         w, h = get_image_dimensions(self.logo)
#         if w < 100:
#             raise ValidationError("The image is %i pixel narrow. It's supposed to be wider than 100px" % w)
#         if h < 100:
#             raise ValidationError("The image is %i pixel low. It's supposed to be higher than 100px" % h)
#table for Custom User
class CustomUser(AbstractUser):
   
    company=models.ForeignKey(Company,blank=True,null=True,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
    phone_number=models.CharField(validators=[mobile_num_regex],max_length=12)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)





