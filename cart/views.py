from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from products.models import Product


def cart_view(request):
    """ A view to dispaly the cart"""
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        print(cart_items)
        total_cost = sum(item.get_total_price() for item in cart_items)
        print(total_cost)
    else:
        cart = request.session.get('cart', [])
        cart_items = [CartItem(product_id=item['product_id'],
                      quantity=item['quantity']) for item in cart]
        total_cost = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_cost': total_cost})


def add_to_cart(request, product_id):
    print(f"Adding to cart: {product_id}")
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        print(product)
        cart_item, created = CartItem.objects.get_or_create(
                        user=request.user,
                        product=product)
        if not created:
            cart_item.quantity += 1
            print(cart_item.quantity)
            cart_item.save()
            print(f"Cart Item: {cart_item}")
    else:
        cart = request.session.get('cart', [])
        product_id = str(product_id)
        print(product_id)
        found = False
        for item in cart:
            if item['product_id'] == product_id:
                item['quantity'] += 1
                found = True
                break
        if not found:
            cart.append({'product_id': product_id, 'quantity': 1})
        request.session['cart'] = cart
    return redirect('cart_view')


def remove_from_cart(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(
                    CartItem, pk=cart_item_id,
                    user=request.user)
        print(cart_item)           
        cart_item.delete()
    else:
        cart = request.session.get('cart', [])
        cart = [item for item in cart if item['product_id'] != cart_item_id]
        cart_item.delete()
        request.session['cart'] = cart
    return redirect('cart_view')


def update_cart(request, product_id):
    """ A view to update quantity of cart item """
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        cart_item = get_object_or_404(
                    CartItem, user=request.user,
                    product=product)
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
