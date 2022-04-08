from django.urls import path
from .views import CreateProduct, EndUserProductWishList

urlpatterns = [
    path('create-product/', CreateProduct.as_view(), name = "create_product"),
    path('wishlist/', EndUserProductWishList.as_view(), name = "create_product"),
    
    
]