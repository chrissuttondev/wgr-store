from django.shortcuts import render
from .models import Cart
from products.models import Product


# Create your views here.
def cart(request):
    """ A view to show the cart"""

    items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in items)

    context = {
        'items': items,
        'total': total,
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    item, created = Cart.objects.get_or_create(product=product,
                                               user=request.user)
    item.quantity += 1
    item.save()
    return render(request, 'cart/cart.html')
