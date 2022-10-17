from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import AddAddressRequestSerializer
from user.models import Address
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AddAddressView(APIView):

    permission_classes = [(IsAuthenticated)]

    def post(self,request):
        req_data = request.data
        request_data = AddAddressRequestSerializer(data=req_data)
        login_request_data = request_data.is_valid(raise_exception=True)
        request_data = request_data.validated_data
        user = request.user
        qs = Address.objects.create(address = request_data.get("address"),
                                city = request_data.get("city"),
                                state = request_data.get("state"),
                                pincode = request_data.get("pincode"),
                                user   = user  )
        return Response({"id" : qs.id, "address" : qs.address, "city" : qs.city}, status = 200)
    
    def get(self,request):
        user = request.user
        qs = Address.objects.filter(user = user)
        all_address = []
        for data in qs:
            all_address.append({"id" : data.id, "address" : data.address, "city" : data.city, "state" : data.state, "pincode" : data.pincode, "created_at" : data.created_at})
        return Response({"data" : all_address}, status = 200)