from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from products.models import Categories, Product
from products.serializer import AddCategoriesRequestSerializer

# Create your views here.

class GetProductsView(APIView):

    permission_classes = [(IsAuthenticated)]
    
    def get(self,request, category_id):
        qs = Product.objects.filter(category_id = category_id)
        resp = []
        for data in qs:
            resp.append({"id" : data.id, "name" : data.name, "amount" : data.amount})
        
        return Response({"data" : resp}, status =200)
