from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid


class CartItem(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True,
        on_delete=models.CASCADE
        )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"


# order model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField(max_length=20, default='pending')
    order_number = models.CharField(
        max_length=36,
        unique=True, editable=False,
        defaul=uuid.uuid4
        )


# order item model
class Order_item(models.Model):
    order = models.ForgienKey(
          Order,
          related_name="items",
          on_delete=models.CASCADE
        )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
