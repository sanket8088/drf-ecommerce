from rest_framework import serializers


class OtpRequestSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=254)
    otp = serializers.IntegerField()