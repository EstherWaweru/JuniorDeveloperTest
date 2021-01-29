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
    This method is for adding a new company

    Extended description of function.
    arg(request)

    """
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        company_name=request.POST.get("company_name")
        
        email=request.POST.get("email")
        website=request.POST.get("website")
        logo=request.POST.get("logo")
        try:
            merchant_model=Company(name=company_name,email=email,website=website,logo=logo)
            merchant_model.save()
            messages.success(request,"Successfully Added A Company")
            return HttpResponseRedirect(reverse("add_company"))
        except:
            messages.error(request,"Failed to Add A Company")
            return HttpResponseRedirect(reverse("add_company"))
@login_required
def edit_company(request,company_id):
    company=Company.objects.get(id=company_id)
    return render(request,"edit_company.html",{"company":company,"id":company_id})
@login_required
def edit_company_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        company_id=request.POST.get("company_id")
        print("*******",company_id)
        name=request.POST.get("company_name")
        email=request.POST.get("email")
        logo=request.POST.get("logo")
        website=request.POST.get("website")
        print("we",website)
        try:
            company=Company.objects.get(id=company_id)
            company.name=name
            company.logo=logo
            company.website=website
            company.email=email
            company.save()
            messages.success(request,"Successfully Edited Company ")
            return HttpResponseRedirect(reverse("manage_companies"))
        except:
            messages.error(request,"Failed to Edit Company Details")
            return HttpResponseRedirect("/edit_company/"+company_id)
@login_required
def delete_company(request,company_id):
    if request.method!="POST":
        company=Company.objects.get(id=company_id)
        return render(request,"delete_company.html",{"company":company,"id":company_id})
    else:
        try:
            company=Company.objects.get(id=company_id)
            company.delete()
            messages.success(request,"Successfully Deleted Company ")
            return HttpResponseRedirect(reverse("manage_companies"))
        except:
            messages.success(request,"Successfully Deleted Company ")
            return HttpResponseRedirect(reverse("manage_companies"))

#employees controllers
@login_required
def manage_employees(request):
    employees=CustomUser.objects.all()
    context={"employees":employees}
    return render(request,"manage_employees.html",context)
