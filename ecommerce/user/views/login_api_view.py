from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import LoginRequestSerializer
from user.models import User
from rest_framework.authtoken.models import Token

# Create your views here.

class LoginView(APIView):

    def post(self,request):
        req_data = request.data
        request_data = LoginRequestSerializer(data=req_data)
        login_request_data = request_data.is_valid(raise_exception=True)
        request_data = request_data.validated_data
        email = request_data["email"]
        password = request_data["password"]
        qs = User.objects.filter(email = email)
        if qs.exists():
            user_instance = qs[0]
            password_check = user_instance.check_password(password)
            if password_check:
                if not user_instance.otp_verified:
                    return Response({"msg" : "OTP not validated"}, status = 400)        
                token, created = Token.objects.get_or_create(user=user_instance)
                return Response({"key" : token.key}, status = 200)
            else:
                return Response({"msg" : "Invalid password"}, status = 400)        
        else:
            return Response({"msg" : "Invalid email id"}, status = 400)