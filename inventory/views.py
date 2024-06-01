# Create your views here.
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from inventory.forms import CreateForm
from inventory.models import Product
from django.contrib import messages
from django.db import IntegrityError

class Products(View):
    """Inventory products view."""

    model = Product

    def get(self, request: HttpRequest, *args, **kwargs):
        products = self.model.objects.all()
        return render(request, "inventory.html", {"products": products})


class CreateProduct(View):
    """Create product view."""

    def get(self, request: HttpRequest, *args, **kwargs):
        form = CreateForm()
        return render(request, "create.html", {"form": form})

    def post(self, request):
        """Create new product."""
        form = CreateForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            try:
                Product.objects.create(
                    name=form.cleaned_data["name"],
                    description=form.cleaned_data["description"],
                    price=form.cleaned_data["price"],
                    qty=form.cleaned_data["qty"],
                )
                messages.success(request, 'Producto creado exitosamente.')
                return redirect("inventory")
            except IntegrityError:
                messages.error(request, 'Error al crear producto: Ya existe uno con el mismo nombre')
        return render(request, "create.html", {"form": form})
