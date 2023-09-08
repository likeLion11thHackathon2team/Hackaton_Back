from django.urls import path, include
from . import views
from rest_framework import urls

#회원가입

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),                     
    path('api-auth/', include('rest_framework.urls')),
    path('login/', views.UserLogin.as_view()),
    path('profile/<int:pk>/', views.UserProfile.as_view()),
]