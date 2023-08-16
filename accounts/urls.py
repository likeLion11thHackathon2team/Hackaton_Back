from django.urls import path, include
from . import views
from rest_framework import urls

#회원가입

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),                     #수정할것, signup 논의
    path('api-auth/', include('rest_framework.urls')),
]
