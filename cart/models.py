from django.db import models
from products.models import Product


# Create your models here.
class Cart(models.Model):
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.items.title}'
