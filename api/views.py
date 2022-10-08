from rest_framework.response import Response
from rest_framework.decorators import api_view
from store.models import * 
from .serializers import ProductSerializer



@api_view(['GET'])
def getData(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)



@api_view(['POST'])
def  addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def  deleteProduct(request,uploadid):
    product = Product.objects.get(uploadid=uploadid)
    product.delete()
    return Response(status=204)

