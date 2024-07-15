from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order
import uuid


@receiver(pre_save, sender=Order)
def set_order_number(sender, instance, **kwargs):
    if not isinstance.order_number:
        instance.order_number = str(uuid.uuid4())
