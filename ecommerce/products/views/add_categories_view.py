from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from products.models import Categories
from products.serializer import AddCategoriesRequestSerializer

# Create your views here.

class AddCategoriesView(APIView):

    permission_classes = [(IsAuthenticated)]

    # Internal team api
    def post(self,request):
        user = request.user
        if user.is_staff:
            req_data = request.data
            request_data = AddCategoriesRequestSerializer(data=req_data)
            login_request_data = request_data.is_valid(raise_exception=True)
            request_data = request_data.validated_data
            qs = Categories.objects.create(category_name = request_data.get("category_name"), description = request_data.get("description"))
            return Response({"id" : qs.id, "category_name" : qs.category_name}, status = 200)
        else:
            return Response({"msg" : "Access denied"}, status = 401)

    
    def get(self,request):
        qs = Categories.objects.filter(is_active=True)
        resp =[]
        for data in qs:
            resp.append({"id" : data.id, "category_name" : data.category_name, "description" : data.description})
        return Response({"data" : resp}, status = 200)


