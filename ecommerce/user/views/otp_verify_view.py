from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import OtpRequestSerializer
from user.models import User, Otp

# Create your views here.

class OtpView(APIView):


    def post(self,request):
        req_data = request.data
        request_data = OtpRequestSerializer(data=req_data)
        login_request_data = request_data.is_valid(raise_exception=True)
        request_data = request_data.validated_data
        email =request_data["email"]
        otp =request_data["otp"]
        qs = User.objects.filter(email = email)
        if qs.exists():
            user_instance = qs[0]
            otp_qs = Otp.objects.filter(user = user_instance, otp = otp)
            if otp_qs.exists():
                User.objects.filter(email = email).update(otp_verified=True)
                return Response({"msg" : "OTP validated"}, status=200)
            else:
                return Response({"msg" : "Invalid OTP"}, status=400)
        else:
            return Response({"msg" : "Invalid email ID"}, status=400)
        