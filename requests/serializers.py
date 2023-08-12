from rest_framework.serializers import ModelSerializer

from .models import Request

class RequestBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
