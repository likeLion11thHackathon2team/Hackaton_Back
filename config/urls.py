from django.contrib import admin
from django.urls import path, include

from requests.views import RequestList, RequestMenti, RequestMento, RequestDatail
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('requests', RequestModelViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('requests/', include('requests.urls', namespace='requests')),
]
