from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    """A view that displays the index page"""

    products_object = Product.objects.all()

    context = {
        'products_object': products_object
    }

    return render(request, 'shop\index.html', context)