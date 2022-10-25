from rest_framework import serializers
from users.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.base_user import BaseUserManager
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username','email', 'password', 'password2',)
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data
    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=BaseUserManager.normalize_email(validated_data['email']).lower(),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

