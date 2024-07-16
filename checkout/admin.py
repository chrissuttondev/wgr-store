from django.contrib import admin
from .models import Order, Order_item


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'total_price',  'created_at', 'status']  # noqa
    readonly_fields = ['order_number']


# Register your models here.
admin.site.register(Order)
admin.site.register(Order_item)
