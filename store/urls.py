from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('store', views.store, name="store"),
    path('product/<int:uploadid>', views.productdetails, name='productdetails'),
    path('give', views.give, name="give"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('login', views.loginpage, name="loginpage"),
    path('logout', views.logoutuser, name="logoutuser"),
    path('register', views.register, name="register"),
    path('delete/<int:uploadid>', views.delete_book, name="delete_book"),

]
