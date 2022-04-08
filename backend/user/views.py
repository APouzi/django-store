from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import EndUser
from .serializers import EndUserWithToken
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.cache import caches
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = EndUserWithToken(self.user).data
        
        for k,v in serializer.items():
            data[k] = v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterUser(CreateAPIView):
    serializer_class = EndUserWithToken
    queryset = EndUser.objects.all()



