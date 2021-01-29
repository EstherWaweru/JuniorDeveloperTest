from django.shortcuts import render

# Create your views here.
def loginPage(request):
    return render(request,'login.html')
def home(request):
    return render(request,'dashboard.html')
