from rest_framework import serializers
from .models import Cart, CartItem
# from .serializers import 

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["product","quantity"]
        depth = 1

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["userProfile"]