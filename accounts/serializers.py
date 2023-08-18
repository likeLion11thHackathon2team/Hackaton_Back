from rest_framework.serializers import ModelSerializer

from .models import User

class UserSerializer(ModelSerializer):
    def create(self, validated_date):
        user = User.objects.create_user(
            username = validated_date['username'],
            password = validated_date['password'],
            # phoneNumber = validated_date['phoneNumber']
        )
        return user
    class Meta:
        model = User
        fields = [ 'username', 'password']

class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RequestBaseModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'