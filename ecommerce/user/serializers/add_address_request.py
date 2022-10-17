from rest_framework import serializers


class AddAddressRequestSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=254)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    pincode = serializers.CharField(max_length=50)