"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from api import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage, name='loginPage'),
    # path('',views.demo,name='loginPage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete_company_ajax',views.delete_company_ajax,name='delete_company_ajax'),
    path('user_login', views.user_login, name="user_login"),
    path('logout_user', views.user_logout, name="user_logout"),
    path('dashboard', views.home, name="dashboard"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('manage_companies', views.manage_companies,
         name='manage_companies'),
    path('add_company', views.add_company, name="add_company"),
    path('add_company_save', views.add_company_save,name="add_company_save"),
    path('edit_company/<str:company_id>',views.edit_company, name="edit_company"),
    path('delete_company/<str:company_id>',views.delete_company, name="delete_company"),
    path('edit_company_save', views.edit_company_save,name="edit_company_save"),
    
    path('manage_employees', views.manage_employees,name='manage_employees'),
    path('add_employee', views.add_employee, name="add_employee"),
    path('edit_employee/<str:employee_id>',views.edit_employee, name="edit_employee"),
    path('company/<str:company_id>',views.company_detail, name="company_detail"),
    path('delete_employee/<str:employee_id>',views.delete_employee, name="delete_employee"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
