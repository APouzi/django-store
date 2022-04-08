from django.contrib import admin
from .models import EndUser, UserProfile, WishList, UserOrders, ShippingAddress
# Register your models here.
admin.site.register(EndUser)
admin.site.register(UserProfile)
admin.site.register(WishList)
admin.site.register(UserOrders)
admin.site.register(ShippingAddress)