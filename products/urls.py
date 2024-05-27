from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_info, name='product_info'),
    path('search/', views.product_search, name='product_search'),
    path('mens/', views.mens_products, name='mens'),
    path('womens/', views.womens_products, name='womens'),
    path('jewelery/', views.jewelery_products, name='jewelery'),
    path('electronics/', views.electronics_products, name='electronics'),
]
