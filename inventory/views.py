# Create your views here.
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from inventory.forms import CreateForm, EditForm, EditQtyForm
from inventory.models import Product


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

    def post(self, request: HttpRequest):
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
                messages.success(request, "Producto creado exitosamente.")
                return redirect("inventory")
            except IntegrityError:
                messages.error(
                    request,
                    "Error al crear producto: Ya existe uno con el mismo nombre",
                )
        return render(request, "create.html", {"form": form})


class EditProduct(View):
    """Edit an existing product"""

    def get(self, request: HttpRequest, _id: int):
        item = get_object_or_404(Product, pk=_id)
        form = EditForm(
            initial={
                "name": item.name,
                "description": item.description,
                "price": item.price,
            }
        )
        return render(request, "edit.html", {"form": form})

    def post(self, request: HttpRequest, _id: int):
        item = get_object_or_404(Product, pk=_id)
        form = EditForm(request.POST)
        if form.is_valid():
            item.price = form.cleaned_data["price"]
            item.save()
            messages.success(request, "Producto actualizado exitosamente.")
        return redirect("inventory")


class EditProductQty(View):
    def get(self, request: HttpRequest, _id: int):
        item = get_object_or_404(Product, pk=_id)
        form = EditQtyForm(initial={"name": item.name, "qty": item.qty})
        return render(request, "edit_qty.html", {"form": form})
