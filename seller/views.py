from django.shortcuts import render

# Create your views here.
def seller_home(request):
     return render(request,'sellertemplates/seller_home.html')

def cart(request):
     return render(request,'sellertemplates/cart.html')     

def myorders(request):
     return render(request,'sellertemplates/myorders.html')  

def addproducts(request):
     return render(request,'sellertemplates/addproducts.html')  

def changepassword(request):
     return render(request,'sellertemplates/changepassword.html')       

def updateitem(request):
     return render(request,'sellertemplates/updateitem.html')        