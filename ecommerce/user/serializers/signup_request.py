from rest_framework import serializers


class SignUpRequestSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=254)
    password = serializers.CharField(max_length=16)
    first_name = serializers.CharField(max_length=50)