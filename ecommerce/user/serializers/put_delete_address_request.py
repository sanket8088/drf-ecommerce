import re
from rest_framework import serializers


class PutAddressRequestSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=254, required=False)
    city = serializers.CharField(max_length=50, required=False)
    state = serializers.CharField(max_length=50, required=False)
    pincode = serializers.CharField(max_length=50, required=False)