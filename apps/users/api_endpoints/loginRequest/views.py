import serializer
from rest_framework.views import APIView
from .serializers import UserLoginRequestSerializer
from rest_framework.response import Response
from apps.users.models import User

class LoginRequestAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginRequestSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            phone_number = serializer.data.get("phone_number")
            if not User.object.filter(phone_number=phone_number).exists():
             return Response({"success": True})
        return Response({"success": False, "errors": serializer.errors})

        code = generate_random_6_digits()
        print(code)
        cache.set(f"otp_{phone_number}", code, 60)
        return Response({"success":True, "massage":"We jave sent sms to verify your number"})
        return Response({"success":False,"errors": serializer.errors})
