from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import SignUpRequestSerializer, UserSerializer
from user.models import Otp
import random

# Create your views here.

class SingUpView(APIView):

    def post(self,request):
        req_data = request.data
        request_data = SignUpRequestSerializer(data=req_data)
        signup_request_data = request_data.is_valid(raise_exception=True)
        request_data = request_data.validated_data
        user_instance = UserSerializer.create(request_data)
        if isinstance(user_instance, dict):
            return Response(user_instance, status = 400)
        resp = self.generate_response(user_instance)
        otp = self.generate_otp()
        qs = Otp.objects.create(otp = otp, user = user_instance)
        print(qs.id, qs.otp, "OTP here")
        return Response(resp, status=200)

    def generate_response(self, instance):
        resp = {}
        resp["id"] = instance.id
        resp["first_name"] = instance.first_name
        resp["email"] = instance.email
        return resp

    def generate_otp(self):
        val = random.randint(100000, 999999)
        return val
