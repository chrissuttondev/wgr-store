from django.shortcuts import render, get_object_or_404 # noqa
from django.db.models import Q
from .models import Product
from .forms import SearchForm


# Taken from the boutique ado walkthrough project.
def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all()
    form = SearchForm()

    context = {
        'products': products,
        'form': form,
    }

    return render(request, 'products/products.html', context)


# Taken from the boutique ado walkthrough project.
def product_info(request, product_id):
    """ A view to show individual products info"""

    product = get_object_or_404(Product, pk=product_id)
    form = SearchForm()

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'products/product_info.html', context)


print('Testing search')


# Search view
def product_search(request):
    """ A view to show products based on user search queries"""
    form = SearchForm(request.GET)
    query = request.GET.get('query', '')
    products = Product.objects.all()

    if query:
        query_list = query.split()
        products = products.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )
        for word in query_list:
            products = products.filter(
                Q(title__icontains=word) |
                Q(description__icontains=word) |
                Q(category__icontains=word)
            ). distinct()

    context = {
        'form': form,
        'products': products,
    }

    return render(request, 'products/product_search.html', context)
