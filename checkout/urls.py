from django.urls import path
from . import views


urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path(
        'order_confirmation/ <int:order_id>/',
        views.order_confirmation,
        name='order_confirmation'
        ),
]
