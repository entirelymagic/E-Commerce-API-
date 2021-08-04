from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    # Operations to be performed
    queryset = Category.objects.all().order_by('-created_at')
    # Class responsible for serializing the data 
    serializer_class = CategorySerializer
