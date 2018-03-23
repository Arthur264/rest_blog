from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%d-%m')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'date_joined')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        return user
