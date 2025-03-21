""" This file contains the views for the shop app """

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product


def index(request):
    """A view that displays the index page"""

    products_object = Product.objects.all()

    # Search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products_object = products_object.filter(title__icontains=item_name)

    # Pagination functionality
    paginator = Paginator(products_object, 4)
    page = request.GET.get('page')
    products_object = paginator.get_page(page)

    context = {
        'products_object': products_object
    }

    return render(request, 'shop/index.html', context)


def detail(request, product_id):
    """A view that displays the product detail page"""

    product_object = Product.objects.get(id=product_id)

    context = {
        'product_object': product_object
    }

    return render(request, 'shop/detail.html', context)
