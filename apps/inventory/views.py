from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['sku', 'name']
    ordering_fields = ['price', 'quantity']
    
    