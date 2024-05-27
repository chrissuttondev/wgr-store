from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from products.models import Product


def cart_view(request):
    """ A view to dispaly the cart"""
    if request.user.is_authenticated:
        cart_items = CartItem.Objects.filter(user=request.user)
    else:
        cart = request.session.get('cart', [])
        cart_items = [CartItem(product_id=item['product_id'],
                      quantity=item['quantity']) for item in cart]
    return render(request, 'cart/cart.html', {'cart_items': cart_items})
