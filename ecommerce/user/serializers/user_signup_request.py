from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    @classmethod

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        
        try:
            instance.save()
            return instance
        except Exception:
            resp = {"message" : "User not able to be created"}
            return resp
        
        

    
    class Meta:

        model = User
        extra_kwargs = {"password": {"write_only": True}}
        fields = ("password", "email", "first_name", "id")


