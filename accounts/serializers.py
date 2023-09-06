from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import User

class UserSignupSerializer(ModelSerializer):
    def create(self, validated_date):
        user = User.objects.create_user(
            username = validated_date['username'],
            password = validated_date['password'],
            # phoneNumber = validated_date['phoneNumber']
        )
        return user
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'image', 'phoneNumber', 'gender', 'role', 'email']


# class UserLoginSerializer(ModelSerializer): # 이거 그냥 안 씀
#     class Meta:
#         model = User
#         fields = ['id']
#         fields = ['id', 'name', 'role'] 프로필 세팅 만들고 나서 넣어야됨

        