from django.shortcuts import render, redirect, get_object_or_404
from .models import Order_item, Order
from cart.models import CartItem
from .forms import CheckoutForm


# Create your views here.
def create_order(user, email_add, shipping_add, cart_items):
    """ A view to create customers orders from the associated cart items """
    total_price = sum(item.get_total_price() for item in cart_items)
    order = Order.objects.create(
        user=user,
        total_price=total_price,
        shipping_add=shipping_add,
    )
    for item in cart_items:
        Order_item.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.get_total_price()
        )
    return order


def checkout_view(request):
    """ A view to display the checkout form and handle order creation"""
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email_add')
            shipping_address = form.cleaned_data.get('shipping_add')

            if request.user.is_authenticated:
                user = request.user
                cart_items = CartItem.objects.filter(user=user)
            else:
                user = None
                cart = request.session.get('cart', [])
                cart_items = [
                    CartItem
                    (product_id=item['product_id'],
                     quantity=item['quantity'])
                    for item in cart
                    ]

            order = create_order(user, email, shipping_address, cart_items)

            if request.user.is_authenticated:
                cart_items.delete()
            else:
                request.session['cart'] = []

            return redirect(f'order_confirmation/{order.id}/')

    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {'form': form})


def order_confirmation(request, order_id):
    """ A view to display the order confirmation page."""
    order = get_object_or_404(Order, id=order_id)
    return render(
        request,
        'checkout/order_confirmation.html',
        {'order': order})
