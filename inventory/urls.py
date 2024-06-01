from django.urls import path

from inventory import views

urlpatterns = [
    path("", views.Products.as_view(), name="inventory"),
    path("create/", views.CreateProduct.as_view(), name="create"),
]
