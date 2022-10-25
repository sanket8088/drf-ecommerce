from rest_framework import serializers


class AddToCartRequestSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
