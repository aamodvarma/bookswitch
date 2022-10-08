from django.urls import path, include
from . import views


urlpatterns = [
        path('products/', views.ProductList.as_view()),
        path('products/<int:pk>/', views.ProductDetail.as_view()),
        path('shipping/', views.ShippingList.as_view()),
        path('users/', views.UserList.as_view()),
        path('users/<int:pk>/', views.UserDetail.as_view()),
        path('auth/', include('rest_framework.urls')),
        ]

