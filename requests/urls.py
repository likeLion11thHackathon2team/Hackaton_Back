from django.contrib import admin
from django.urls import path, include

from .views import RequestList, RequestMenti, RequestMento, RequestDatail, RequestRecord

app_name = 'requests'

urlpatterns = [
    path('', RequestList.as_view()),
    path('<int:pk>/', RequestDatail.as_view()),
    path('mento/', RequestMento.as_view()),
    path('menti/', RequestMenti.as_view()),
    path('record/<int:pk>/', RequestRecord.as_view()),
]

