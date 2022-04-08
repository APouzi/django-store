from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import ShippingAddress, UserOrders, WishList, EndUser, UserProfile
from rest_framework_simplejwt.tokens import RefreshToken

class EndUserWithToken(ModelSerializer):
    token = SerializerMethodField(read_only=True)
    class Meta:
        model = EndUser
        fields = ["email", "username", "first_name", "last_name", "password","token" ]
        extra_kwargs = {"password":{"write_only":True}}
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        token["email"] = obj.email
        return str(token.access_token)
    
    # Move this logic over to the Object manager so the signals can be activated (possibly not having to creat eh signals.)
    def create(self, validated_data):
        endUser = EndUser.objects.create_user(**validated_data)
        userprofile = UserProfile.objects.create(user = endUser)
        ShippingAddress.objects.create(userProfile = userprofile)
        UserOrders.objects.create(userProfile = userprofile)
        WishList.objects.create(userProfile = userprofile)
        return endUser
    