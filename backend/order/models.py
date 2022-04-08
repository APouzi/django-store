from django.db import models
from user.models import UserProfile
from product.models import Product
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .services import trackingNumberGenerator
# Create your models here.


class Order(models.Model):
    orderNumber = models.CharField(max_length=40, blank=True)
    trackingNumber = models.CharField(max_length=150)

    

class OrderItem(models.Model):
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField(verbose_name="quantity")
    orderItems = models.ManyToManyField(Order)
    price = models.IntegerField(blank=False,)
    #TODO With the order number we are going to have a signal ask if the orderNumber is blank, which will be everytime an order is created. This signal will then make the variable into a definition and 

    def get_item_price(self):
        return self.price * self.quantity

class OrderList(models.Model):
    userProfile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    orders = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.userProfile.name


class Cart(models.Model):
    userProfile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    
# TODO We want to implement the cart Model here and implement whatever this entails on the view(controller). Could just use Redux and localstorage, but that 
    def __str__(self) -> str:
        return f"{self.userProfile.user.email} Cart"

class CartItem(models.Model):
    product = models.ManyToManyField(Product)
    cartOf = models.ForeignKey(Cart, on_delete=models.CASCADE, null = True)
    quantity = models.IntegerField()
    

    def __str__(self):
        return f"{self.cartOf} Item and id:{self.id}"


@receiver(pre_save, sender=Order)
def save_profile(sender, instance, **kwargs):
    if not instance.orderNumber:
        instance.orderNumber = trackingNumberGenerator()

