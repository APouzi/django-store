from rest_framework import serializers

from .models import Product
from user.models import WishList

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "inv_num"]

    

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['userProfile', 'products']
        depth = 1

    