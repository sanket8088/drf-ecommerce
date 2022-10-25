from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from order.serailizer import AddToCartRequestSerializer
from order.models import Cart
from products.models import Product


# Create your views here.

class AddItemToCart(APIView):

    permission_classes = [(IsAuthenticated)]


    def post(self,request):
        req_data = request.data
        request_data = AddToCartRequestSerializer(data=req_data)
        _ = request_data.is_valid(raise_exception=True)
        request_data = request_data.validated_data
        user = request.user
        product_id = request_data["product_id"]
        product_qs = Product.objects.filter(id = product_id)
        if product_qs.exists():
            cart_data = Cart.objects.filter(user=user, product = product_qs[0])
            if cart_data.exists():
                count = cart_data[0].count
                Cart.objects.filter(user=user, product = product_qs[0]).update(count = count+1)
            else:
                cart_qs = Cart.objects.create(user=user, product = product_qs[0])
            return Response({"msg" : "Item added to cart"}, status = 200)
        else:
            return Response({"msg" : "Invalid item"}, status = 400)

    def get(self,request):
        user = request.user
        resp = []
        cart_qs = Cart.objects.filter(user=user)
        total_cost =0
        for data in cart_qs:
            single_cart_item = {"id" : data.id, "product" :self.get_product(data.product_id), "count" : data.count}
            total_cost_per_iem = single_cart_item["product"]["amount"] * data.count
            total_cost+=total_cost_per_iem
            resp.append(single_cart_item)
        return Response({"amount" : total_cost,"data" : resp}, status = 200)

    def get_product(self, id):
        qs = Product.objects.get(id = id)
        return {"id" : qs.id, "name" : qs.name, "picture" : qs.picture, "amount": qs.amount}
