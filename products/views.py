from django.shortcuts import render, get_object_or_404 # noqa
from django.db.models import Q
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


# Search view https://github.com/flatplanet/Django-Ecommerce/blob/main/store/templates/search.html # noqa
def product_search(request):
    """ A view to show products based on user search queries"""
    if request.method == "POST":
        searched = request.POST['searched']
        # Query The Products DB Model
        products = Product.objects.filter(Q(title__icontains=searched) |
                                          Q(description__icontains=searched) |
                                          Q(category__icontains=searched)
                                          )
        # Prepare context
        context = {
            'products': products,
            'searched': searched,
        }
        # Test for null
        if not products.exists():
            return render(request, "products/product_search.html", context)
        else:
            return render(request, "products/product_search.html", context)
    else:
        context = {
            'products': None,
            'searched': '',
        }
        return render(request, "products/product_search.html", context)


# Category Views
def mens_products(request):
    """ A view to show all mens products"""

    products = Product.objects.filter(category="men's clothing")

    context = {
        'products': products,
    }

    return render(request, 'products/products_mens.html', context)


def womens_products(request):
    """ A view to show all womens products"""

    products = Product.objects.filter(category="women's clothing")

    context = {
        'products': products,
    }

    return render(request, 'products/products_womens.html', context)


def jewelery_products(request):
    """ A view to show all jewelery"""

    products = Product.objects.filter(category="jewelery")

    context = {
        'products': products,
    }

    return render(request, 'products/products_jewelery.html', context)


def electronics_products(request):
    """ A view to show all electronics"""

    products = Product.objects.filter(category="electronics")

    context = {
        'products': products,
    }

    return render(request, 'products/products_electronics.html', context)
