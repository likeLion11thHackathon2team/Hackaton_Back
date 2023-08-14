from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Request

class RequestBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class RequestHelpModelSerializer(ModelSerializer):
    class Meta(RequestBaseModelSerializer.Meta):
        fields = ['id', 'category', 'content', 'mentiLatitude', 'mentiLongitude', 'menti', 'requestTime']


class RequestAcceptModelSerializer(ModelSerializer):
    class Meta(RequestBaseModelSerializer.Meta):
        fields = ['mento', 'acceptTime']


