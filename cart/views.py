from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
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
