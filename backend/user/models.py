from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings
from product.models import Product
# Create your views here.
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)


        if other_fields.get('is_staff') is not True:
            raise ValueError("Not staff member")
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError("must set is_superuser to True")
        
        return self.create_user(email, username, first_name, last_name, password, **other_fields)
    
    def create_user(self, email, username, first_name, last_name, password, **other_fields):
        if not email:
            raise ValueError("Must have email")
        email = self.normalize_email(email)
        user = self.model(email = email,username = username, first_name = first_name, last_name = last_name, **other_fields)#Same as the User(email=email....)
        user.set_password(password)
        user.save()
        return user

class EndUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length = 150, unique=True)
    first_name = models.CharField(max_length = 150, unique=True)
    last_name = models.CharField(max_length = 150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name',  'last_name']

    def __str__(self):
        return self.email
    
    # Could implement Send User Email here.




class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email

class ShippingAddress(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(blank=True, max_length = 1500)
    city = models.CharField(blank=True, max_length=200)
    state = models.CharField(blank=True,max_length = 2)
    zip = models.IntegerField(null=True)
    unit_num = models.IntegerField(null = True)
 
    def __str__(self):
        return self.userProfile.user.email 

class UserOrders(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    def __str__(self):
       return self.userProfile.user.email

class WishList(models.Model):
    userProfile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null = True)
    products = models.ManyToManyField(Product)
    def __str__(self):
        return self.userProfile.user.email