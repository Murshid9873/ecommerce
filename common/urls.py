from django.urls import path
from . import views



urlpatterns=[
    path('index', views.index),
    path('sellerlogin', views.sellerlogin),
    path('customerlogin', views.customerlogin),
    path('sellersignup', views.sellersignup),
    path('customersignup', views.customersignup),
    path('changepassword', views.changepassword),
]