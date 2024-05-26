from django.shortcuts import render, get_object_or_404 # noqa
from .models import Product


# Taken from the boutique ado walkthrough project.
def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


# Taken from the boutique ado walkthrough project.
def product_info(request, product_id):
    """ A view to show individual products info"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)
