from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers

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

class MentoLocationSerializer(serializers.Serializer):
    mentoLatitude = serializers.DecimalField(max_digits=23, decimal_places=20)
    mentoLongitude = serializers.DecimalField(max_digits=23, decimal_places=20)

