from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            nickname = validated_data['nickname'],
            name = validated_data['name'],
            id = validated_data['id'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['nickname', 'name', 'id', 'password']