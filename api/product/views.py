from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


# Product View
class ProductViewSet(viewsets.ModelViewSet):
    # Operations to be performed
    queryset = Product.objects.all().order_by('id')
    # Class responsible for serializing the data 
    serializer_class = ProductSerializer
