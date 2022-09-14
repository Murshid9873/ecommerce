from django.shortcuts import render

# Create your views here.

def index(request):
     return render(request,'commontemplate/index.html')

def sellerlogin(request):
     return render(request,'commontemplate/sellerlogin.html')

def customerlogin(request):
     return render(request,'commontemplate/customerlogin.html')

def sellersignup(request):
     return render(request,'commontemplate/sellersignup.html')

def customersignup(request):
     return render(request,'commontemplate/customersignup.html')     

def changepassword(request):
     return render(request,'commontemplate/changepassword.html')     
