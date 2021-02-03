from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from api.models import CustomUser,Company
class UserModel(UserAdmin):
    pass
admin.site.register(CustomUser,UserModel)
admin.site.register(Company)
