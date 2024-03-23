from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from rest_framework_jwt.serializers import User


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    engine_capacity = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.model)
        super(CarModel, self).save(*args, **kwargs)



    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year})"

class CarImage(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/car_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image of {self.car}"
