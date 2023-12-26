from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data: dict) -> User:
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        
        token, created = Token.objects.get_or_create(user=user)
        self.validated_data['token'] = token

        return user

    def to_representation(self, instance: User) -> dict:
        return {
            'token': self.validated_data['token'].key
        }
