from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import PutAddressRequestSerializer
from user.models import Address
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PutDeleteAddressView(APIView):

    permission_classes = [(IsAuthenticated)]

    def put(self,request, address_id):
        req_data = request.data
        request_data = PutAddressRequestSerializer(data=req_data)
        login_request_data = request_data.is_valid(raise_exception=True)
        request_data = request_data.validated_data
        user = request.user
        # Address id should be a valid id
        try:
            address_qs = Address.objects.get(id = address_id)
            #user should be address owner
            if address_qs.user != user:
                return Response({"msg" : "Access Denied"}, status = 401)
            
            if "address" in request_data:
                address_qs.address = request_data.get("address")
            if "city" in request_data:
                address_qs.city = request_data.get("city")
            if "state" in request_data:
                address_qs.state = request_data.get("state")
            if "pincode" in request_data:
                address_qs.pincode = request_data.get("pincode")
            address_qs.save()

        except Exception as e:
            return Response({"msg" : "Invalid order ID"}, status = 400)
        return Response({"msg" : "successfully updated"}, status = 200)
    
    def delete(self,request, address_id):
        user = request.user
        try:
            address_qs = Address.objects.get(id = address_id)
            #user should be address owner
            if address_qs.user != user:
                return Response({"msg" : "Access Denied"}, status = 401)
            
            address_qs.delete()
        except Exception as e:
            return Response({"msg" : "Invalid order ID"}, status = 400)
        return Response({"msg" : "successfully deleted"}, status = 200)



