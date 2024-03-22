from django_filters import rest_framework as filters
from .models import CarModel

from django_filters import rest_framework as filters


import django_filters
from .models import CarModel

class CarModelFilter(django_filters.FilterSet):
    manufacturer = django_filters.CharFilter(field_name='manufacturer__name', lookup_expr='exact')
    model = django_filters.CharFilter(field_name='model', lookup_expr='icontains')
    year = django_filters.NumberFilter(field_name='year', lookup_expr='exact')
    engine_capacity = django_filters.NumberFilter(field_name='engine_capacity', lookup_expr='exact')
    color = django_filters.CharFilter(field_name='color', lookup_expr='icontains')
    price = django_filters.CharFilter(field_name='price', lookup_expr='exact')

    class Meta:
        model = CarModel
        fields = ['manufacturer', 'model', 'year', 'engine_capacity', 'color', 'price']
