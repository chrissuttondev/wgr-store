from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'price',
        'rate',
        'image_local',
    )

    ordering = ('category',)


# Register your models here.
admin.site.register(Product, ProductAdmin)
