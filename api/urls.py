from django.urls import path
from . import views


urlpatterns = [
        path('', views.getData),
        path('delete/<int:uploadid>/', views.deleteProduct),
        path('add/', views.addProduct)
        ]
