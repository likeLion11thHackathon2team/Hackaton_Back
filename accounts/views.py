from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from .serializers import UserSignupSerializer, UserProfileSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

import json




# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer

    def post(self, request, *args, **kwargs):
        if request.data['password'] == request.data['password2']:
            return self.create(request, *args, **kwargs)
        else:
            data = {
                "error": {
                    "password2" : "비밀번호를 올바르게 입력해주세요"
                }
            }
            return JsonResponse(data)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            "userId" : User.objects.get(username=serializer.validated_data['username']).id
        }
        return Response(json.dumps(data), status=status.HTTP_201_CREATED, headers=headers)


#로그인
class UserLogin(APIView):
    def post(self, request):
        username = request.data['id']
        password = request.data['password']
        # user = authenticate(request, username=username, password=password) 뭐 때문에 로그인이 안 됐는지 모름
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user: # 아이디 O
            if authenticate(request, username=username, password=password): # 아이디 O / 비번 O
                data = {
                    "name" : user.name,
                    "userId" : user.id,
                    "ismento" : user.role
                }
                login(request, user)
            else: # 아이디 O / 비번 X
                data = {
                "error": {
                    "id" : None,
                    "password" : "비밀번호를 올바르게 입력해주세요"
                }
            }
        else: # 아이디 X
            data = {
                "error": {
                    "id" : "아이디를 올바르게 입력해주세요",
                    "password" : None
                }
            }
        return JsonResponse(data)

        # if user:
        #     UserSerializer = UserLoginSerializer(data=user)
        #     if UserSerializer.is_valid():
        #         return Response(UserSerializer.data)
        #     else:
        #         return Response(UserSerializer.errors)
        # else:
        #     return Response(status=401)


class UserProfile(APIView): # pk는 user id 값
    def get(self, request, pk):
        pass
    
    def patch(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

