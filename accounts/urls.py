from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserProfileViewSet
from rest_framework import urls


urlpatterns =[
    path('signup/', views.UserCreate.as_view()),                     
    path('api-auth/', include('rest_framework.urls')),
    path('login/', views.UserLogin.as_view()),
    path('profile/', include(router.urls)),
]