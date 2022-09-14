from django.urls import path
from . import views

urlpatterns=[
    path('home',views.customer_home),
    path('cart',views.customer_cart),
    path('product',views.customer_product),
    path('order',views.customer_order),
    path('changepassword',views.changepassword),
    path('name',views.name)
]