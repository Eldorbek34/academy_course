#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#from rest_framework_simplejwt.views import TokenObtainPairView

#class UserLoginSerializer(TokenObtainPairSerializer):
    #@classmethod
    #def get_token(cls, user):
      #  token = super().get_token(user)

       # token['full_name'] = user.full_name
         # return token

from rest_framework import serializers
from apps.users.models import User

class UserLoginRequestSerializer(serializers.ModelSerializer):
    class Meta:
        def post(self, request, *args, **kwargs):
         model = User
         fields = ("phone_number", )
         return{"success": True}



