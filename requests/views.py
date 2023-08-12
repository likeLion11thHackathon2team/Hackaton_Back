from django.shortcuts import render

from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import RequestBaseModelSerializer

from .models import Request

class RequestModelViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestBaseModelSerializer