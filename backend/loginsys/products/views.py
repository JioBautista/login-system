from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from products.models import Products
from products.serializers import ProductSerializer


# Create your views here.
@api_view(["GET", "POST"])
def products(request):
    if request.method == "GET":
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
