from django.urls import path
from . import views



urlpatterns=[
    path('sellerhome', views.seller_home),
    path('cart', views.cart),
    path('myorders', views.myorders),
    path('addproducts', views.addproducts),
    path('changepassword', views.changepassword),
    path('updateitem', views.updateitem)
]