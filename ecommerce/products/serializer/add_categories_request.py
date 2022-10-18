from rest_framework import serializers


class AddCategoriesRequestSerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)