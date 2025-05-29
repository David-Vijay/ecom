from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
class RegisterSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirmPassword']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')  # Remove confirmPassword before creating user
        user = User.objects.create_user(**validated_data)
        return user
