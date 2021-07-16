from rest_framework import serializers 
from myapi.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                  'product_name',
                  'product_category',
                  'product_desc')