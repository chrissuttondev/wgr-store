from django.contrib import admin
from .models import Order, Order_item


class OrderItemInline(admin.TabularInline):
    model = Order_item
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user',
                    'total_price',  'created_at']
    readonly_fields = ['order_number',  'created_at']
    inlines = [OrderItemInline]


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_item)
