from django.contrib import admin
from django.urls import path
from .views import MyTokenObtainPairView, RegisterUser

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name = "login_user"),
    path('register/', RegisterUser.as_view(), name = "register_user"),

]