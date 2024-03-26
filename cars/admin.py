from django.contrib import admin
from django.utils.html import format_html

from .models import CarModel, Manufacturer, CarImage

@admin.register(CarModel)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'model', 'year', 'price', 'color', 'engine_capacity', 'image_tag')
    list_display_links = ('id', 'manufacturer',)
    ordering = ('manufacturer', 'model', 'year', 'price', 'color',)
    list_editable = ('model', 'year', 'price', 'color', 'engine_capacity')
    list_per_page = 5
    search_fields = ('model__startswith', 'manufacturer__name')
    list_filter = ('model', 'manufacturer__name', 'year', 'price', 'color', 'engine_capacity')

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.get().image.url))


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country',)
    list_editable = ('name', 'country',)
    ordering = ('name', 'country', )
    list_per_page = 5

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display_links = ('car',)
    list_display = ('id', 'car', 'image_tag')
    #list_editable = ('image', )
    list_per_page = 5

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'