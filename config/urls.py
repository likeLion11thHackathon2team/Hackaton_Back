from django.contrib import admin
from django.urls import path, include

from requests.views import RequestList, RequestMenti, RequestMento, RequestDatail
from rest_framework.routers import DefaultRouter

from django.urls import re_path
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),
    # path('checks/', include('checks.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/signup/', include('rest_auth.registration.urls')),

    path('requests/', include('requests.urls', namespace='requests')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
