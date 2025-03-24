""" This file contains the views for the shop app """

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Order


def index(request):
    """A view that displays the index page"""

    products_object = Product.objects.all().order_by('id')

    # Search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products_object = products_object.filter(title__icontains=item_name)

    # Pagination functionality
    paginator = Paginator(products_object, 8)
    page = request.GET.get('page')
    products_object = paginator.get_page(page)

    context = {
        'products_object': products_object
    }

    return render(request, 'shop/index.html', context)


def detail(request, id):
    """A view that displays the product detail page"""

    product_object = Product.objects.get(id=id)

    context = {
        'product_object': product_object
    }

    return render(request, 'shop/detail.html', context)


def checkout(request):
    """A view that displays the checkout page"""

    if request.method == 'POST':

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')

        order = Order(name=name, email=email, address=address,
                      city=city, state=state, zip_code=zip_code)
        order.save()

    return render(request, 'shop/checkout.html')
