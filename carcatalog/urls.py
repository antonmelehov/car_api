"""
URL configuration for carcatalog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from carcatalog import settings

from cars.views import page_not_found
from django.views.static import serve
from django.conf.urls.static import static
from cars.views import CarListCreateAPIView, CarAPIUpdate, CarAPIDestroy, ImageAPIList, ImageAPIUpdate, ImageAPIDestroy

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('admin/', admin.site.urls),
    path('api/v1/drf-auth', include('rest_framework.urls')),
    path('api/v1/cars/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('api/v1/cars/<int:pk>/', CarAPIUpdate.as_view(), name='car-retrieve-update'),
    path('api/v1/cars/carsdelete/<int:pk>/', CarAPIDestroy.as_view(), name='car-retrieve-destroy'),

    path('api/v1/cars/image/', ImageAPIList.as_view(), name='car-image-create'),
    path('api/v1/cars/<int:pk>/image/', ImageAPIUpdate.as_view(), name='car-image-retrieve-update'),
    path('api/v1/cars/<int:pk>/imagedelete/', ImageAPIDestroy.as_view(), name='car-image-retrieve-destroy'),
    path('__debug__/', include('debug_toolbar.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = 'Car catalog administration'
