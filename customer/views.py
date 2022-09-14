from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request, 'customer_template/home.html')


def customer_cart(request):
    return render(request, 'customer_template/cart.html')


def customer_product(request):
    return render(request, 'customer_template/product_details.html' )    

def customer_order(request):
    return render(request, 'customer_template/order.html')

def changepassword(request):
    return render(request, 'customer_template/changepassword.html')

def name(request):
    return render(request, 'customer_template/name.html')    