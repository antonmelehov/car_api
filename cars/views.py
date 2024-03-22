import django_filters
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework import generics
from rest_framework.response import Response

from .filters import CarModelFilter
from .serializers import CarSerializer, CarImageSerializer
from .models import CarModel, CarImage


def page_not_found(request, exception):
    return HttpResponseNotFound('Page not found')

class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = CarModelFilter

class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CarImageAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)