# Create your views here.
from django.shortcuts import render

from inventory.models import Product


def get_products(request):
    products = Product.objects.all()
    return render(request, "inventory.html", {"products": products})


def create_product(request):
    return render(request, "create.html")
