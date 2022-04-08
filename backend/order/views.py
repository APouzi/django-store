from typing import List
from django.shortcuts import render

from user.models import UserProfile
from .models import Cart, CartItem
from product.models import Product
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CartList(ListAPIView):
    serializer_class = CartItemSerializer
    def get_queryset(self):
        userProf = UserProfile.objects.get(user = self.request.user)
        cartList = Cart.objects.get(userProfile = userProf).cartitem_set.all()
        return cartList


# APIVIEW just because, would usually use ListAPIView but here is this
class CartHandler(APIView):
    
    def get(self, request, format = None):
        userProf = UserProfile.objects.get(user = request.user)
        cartList = Cart.objects.get(userProfile = userProf).cartitem_set.all()
        serializer = CartItemSerializer(cartList, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        userProf = UserProfile.objects.get(user = request.user) #This can be taken care of through the frontend, but for now will do this. Remove this for optimization, unneeded query
        cartList = Cart.objects.get(userProfile = userProf)
        productToAdd = Product.objects.get(id = request.data['product'])
        newCartItem = CartItem(cartOf = cartList, quantity = request.data['quantity'])
        newCartItem.save()
        newCartItem.product.add(productToAdd)
        serializer = CartItemSerializer(cartList.cartitem_set.all(), many = True)
        return Response(serializer.data)

#For now, this updates the quantity, can do other behavior later. 
    def put(self, request, format = None):
        cartItem = CartItem.objects.get(id = request.data['cart_item'])
        cartItem.quantity = request.data['quantity']
        cartItem.save()
        return self.get(request=request)
    

    def delete(self, request, format = None):
        userProf = UserProfile.objects.get(user = request.user)
        cartList = Cart.objects.get(userProfile = userProf)
        cartItem = CartItem.objects.get(id = request.data['cart_item'])      
        cartList.cartitem_set.remove(cartItem) #Method only exists if foreignkey null == true
        cartItem.delete() # Can just have this alone and take out the ".remove()", just wanted to test
        serializer = CartItemSerializer(cartList.cartitem_set.all(), many = True)
        return Response(serializer.data)
    
        

        
