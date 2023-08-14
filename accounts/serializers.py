from rest_framework.serializers import ModelSerializer

from .models import User

class RequestBaseModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'