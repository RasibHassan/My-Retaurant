from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='shop'),
    path('menu/', views.menu,name="menu"),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.Contact,name="ContactUs"),
    path('checkout/', views.checkout,name="Checkout"),
]
