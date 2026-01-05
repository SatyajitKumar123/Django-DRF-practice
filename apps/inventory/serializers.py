from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'description', 'price', 'quantity', 'created_at', 'updated_at']
        read_only = ['created_at', 'updated_at']