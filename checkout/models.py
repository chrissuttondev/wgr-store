import uuid
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# order model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=20, null=True, blank=False)
    email_add = models.EmailField(max_length=20, null=True, blank=False)
    shipping_add = models.TextField(max_length=20, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(
        max_length=36,
        unique=True, editable=False,
        default=uuid.uuid4
        )


# order item model
class Order_item(models.Model):
    order = models.ForeignKey(
          Order,
          related_name="items",
          on_delete=models.CASCADE
        )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
