from django.urls import path
from . import views



urlpatterns=[
    path('login', views.login),
    path('home', views.home),
    path('approvesellers', views.approvesellers),
    path('viewsellers', views.viewsellers),
    path('viewcustomer', views.viewcustomer),
    path('viewsellerorders', views.viewsellerorders),
    

    
]   


