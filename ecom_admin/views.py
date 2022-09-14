from django.shortcuts import render
# Create your views here.

def login(request):
     return render(request,'ecom_admintemplate/login.html')

def home(request):
     return render(request,'ecom_admintemplate/home.html')

def approvesellers(request):
     return render(request,'ecom_admintemplate/approvesellers.html')     

def viewsellers(request):
     return render(request,'ecom_admintemplate/viewsellers.html') 

def viewcustomer(request):
     return render(request,'ecom_admintemplate/viewcustomer.html') 

def viewsellerorders(request):
     return render(request,'ecom_admintemplate/viewsellerorders.html')

