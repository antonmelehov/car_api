from rest_framework import serializers
from .models import CarModel, Manufacturer, CarImage

class CarSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CarModel
        fields = '__all__'

class CarImageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CarImage
        fields = ('id', 'image', 'user')