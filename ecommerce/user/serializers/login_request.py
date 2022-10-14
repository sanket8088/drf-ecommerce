from rest_framework import serializers


class LoginRequestSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=254)
    password = serializers.CharField(max_length=16)