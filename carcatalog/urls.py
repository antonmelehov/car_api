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
    path('debug/', include('debug_toolbar.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]

admin.site.site_header = 'Car catalog administration'