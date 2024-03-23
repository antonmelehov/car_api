import django_filters
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .filters import CarModelFilter
from .permissions import IsOwnerOrReadOnly
from .serializers import CarSerializer, CarImageSerializer
from .models import CarModel, CarImage


def page_not_found(request, exception):
    return HttpResponseNotFound('Page not found')

class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = CarModelFilter
    ordering_fields = ['manufacturer', 'year', 'price', 'engine_capacity']
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset



class CarAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CarAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated, )



class ImageAPIList(generics.ListCreateAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ImageAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ImageAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = (IsAuthenticated, )
