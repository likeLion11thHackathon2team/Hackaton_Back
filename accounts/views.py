from django.shortcuts import render
from .serializers import UserSerializer, UserLoginSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics




# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#로그인
class UserLogin(APIView):
    def post(self, request):
        user = User.objects.get(username=request.POST['id'])
        UserSerializer = UserLoginSerializer(user)
        user_profile = []
        return Response(UserSerializer.data)