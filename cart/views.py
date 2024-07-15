from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
from products.models import Product


def cart_view(request):
    """ A view to display the cart """
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_cost = sum(item.get_total_price() for item in cart_items)

    else:
        cart = request.session.get('cart', [])
        cart_items = []
        for item in cart:
            product = get_object_or_404(Product, pk=item['product_id'])
            cart_item = {
                'product': product,
                'quantity': item['quantity'],
                'get_total_price': product.price * item['quantity']
            }

            cart_items.append(cart_item)
        total_cost = sum(item['get_total_price'] for item in cart_items)

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_cost': total_cost})  # noqa


def add_to_cart(request, product_id):
    """ View to add items to the cart"""
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product
        )

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

    else:
        cart = request.session.get('cart', [])
        for item in cart:
            if item['product_id'] == str(product_id):
                item['quantity'] += quantity
                break
        else:
            cart.append({'product_id': str(product_id), 'quantity': quantity})
        request.session['cart'] = cart

    return redirect('cart_view')


def remove_from_cart(request, cart_item_id):
    """ A view to remove items from the cart"""
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)  # noqa
        print(cart_item)
        cart_item.delete()
    else:
        cart = request.session.get('cart', [])
        cart_item_id = int(cart_item_id)
        cart.pop(cart_item_id)
        request.session['cart'] = cart
    return redirect('cart_view')


def update_cart(request, product_id):
    """ A view to update quantity of cart item """
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        cart_item = get_object_or_404(CartItem, user=request.user, product=product)  # noqa
        quantity = int(request.POST.get('quantity'))
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart = request.session.get('cart', [])
        for item in cart:
            if item['product_id'] == str(product_id):
                item['quantity'] = int(request.POST.get('quantity'))
                break
        request.session['cart'] = cart
    return redirect('cart_view')


def create_order(user, email_ad, shipping_add, cart_items):
    """ A view to create customers orders from the associated cart items """
    total_price = sum(item.get_total_price for item in cart_items)
    order = Order.Objects.create(
        user=user,
        total_price=total_price,
        shipping_address=shipping_add,
    )
    for item in cart_items:
        OrderItem.Objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.get_total_price
        )
    return order


def checkout_view(request):
    """ A view to display the checkout form and handle order creation"""
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            shipping_address = form.cleaned_data.get('shipping_address')

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
                for item in cart]

        order = create_order(user, email, shipping_address, cart_items)

        if request.user.is_authenticated:
            cart_items.delete()
        else:
            request.session['cart'] = []

        return redirect('order_confirmation', order_id=order.id)

    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form})


@login_required
def order_confirmation(request, order_id):
    """ A view to display the order confirmation page."""
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})
