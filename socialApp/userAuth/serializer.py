from rest_framework import serializers
from userAuth.models import coustomerUser

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = coustomerUser
        fields = "__all__"

