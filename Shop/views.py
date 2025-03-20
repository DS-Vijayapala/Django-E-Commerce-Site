from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    """A view that displays the index page"""

    products_object = Product.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products_object = products_object.filter(title__icontains=item_name)

    context = {
        'products_object': products_object
    }

    return render(request, 'shop/index.html', context)
