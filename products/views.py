from django.shortcuts import render, get_object_or_404 # noqa
from django.db.models import Q
from .models import Product
from products.forms import SearchForm


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


print('Testing search')


# Search view
def product_search(request):
    """ A view to show products based on user search queries"""
    form = SearchForm()
    query = request.GET.get('query')
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )
    
    context = {
        'form': form,
        'products': products,
    }

    return render(request, 'products_search.html', context)
