from rest_framework import serializers
from store.models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__' 

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ShippingAddress
        fields = '__all__'
 

class ProfileSerializer(serializers.ModelSerializer):
    #products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model =  Profile
        fields = ['id', 'email']

        
