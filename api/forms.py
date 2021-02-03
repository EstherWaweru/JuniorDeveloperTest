from django import forms
from django.forms import ModelForm
from django.forms import widgets
from .models import Company

class CompanyForm(ModelForm):
    
    class Meta():
        model=Company
        # exclude=('maker',)
        fields='__all__'