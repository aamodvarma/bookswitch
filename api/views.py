from rest_framework.response import Response
from rest_framework import permissions 
from rest_framework.decorators import api_view
from store.models import * 
from .permissions import *

from rest_framework import mixins

from .serializers import * 
from django.contrib.auth.models import User

from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics








class UserList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer






class ProductList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ShippingList(generics.ListCreateAPIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingSerializer




class ProductDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]


    def get_object(self, pk):
        try:
            return Product.objects.get(uploadid=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        
        product = self.get_object(pk)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            if request.user.profile == Product.owner:
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
        product = self.get_object(pk)
        if request.user.profile == Product.owner:
            product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#
#class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                      IsOwnerOrReadOnly]
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer
#
