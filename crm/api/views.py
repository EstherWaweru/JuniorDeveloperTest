from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from api.EmailBackEnd import EmailBackEnd
from django.urls import reverse
from django.contrib.auth.decorators import login_required,permission_required
from api.models import Company,CustomUser


# Create your views/controllers here.
def loginPage(request):
    return render(request,'login.html')
def home(request):
    return render(request,'dashboard.html')
#log in a user using an email and a password
def user_login(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
         user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
         if user!=None:
             login(request,user)
             return HttpResponseRedirect('/dashboard')
          

         else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

#logs out a logged in user
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
def user_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,"user_profile.html",{"user":user})
#create a company
@login_required
def manage_companies(request):
    companies=Company.objects.all()
    context={"companies":companies}
    return render(request,"manage_companies.html",context)
@login_required
def add_company(request):
    return render(request,"add_company.html")

@login_required
def add_company_save(request):
    """
    This method is for adding a new organization.

    Extended description of function.
    arg(request)

    """
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        merchant_name=request.POST.get("merchant_name")
        merchant_id=request.POST.get("merchant_id")
        phoneNumber=request.POST.get("phoneNumber")
        email=request.POST.get("email")
        commission=request.POST.get("commission")
        commission_type=request.POST.get("commission_type")
        try:
            merchant_model=Merchant(name=merchant_name,merchant_id=merchant_id,phone_number=phoneNumber,email=email,commission_type=commission_type,commission=commission)
            merchant_model.save()
            messages.success(request,"Successfully Added A Merchant")
            return HttpResponseRedirect(reverse("add_institution"))
        except:
            messages.error(request,"Failed to Add A Merchant")
            return HttpResponseRedirect(reverse("add_institution"))
