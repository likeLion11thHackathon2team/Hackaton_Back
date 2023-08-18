from django.shortcuts import render
from .serializers import UserSerializer, UserLoginSerializer, UserProfileSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import generics


# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#로그인
class UserLogin(APIView):
    def post(self, request):
        user = User.object.get(username=request.id)
        UserSerializer = UserLoginSerializer(user)
        return Response(UserSerializer)
    
#프로필
# class UserProfile():
#     def get(self, request):
#         profile = User.object.all()
#         = UserProfileSerializer()
class UserProfileViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=False, methods=['post'])
    def create_profile(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)