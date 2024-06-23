from rest_framework import serializers
from .models import HomeProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProduct
        fields = ['id', 'name', 'price', 'image', 'category', 'type']
        