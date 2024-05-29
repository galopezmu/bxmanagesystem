from django.urls import path

from inventory import views

urlpatterns = [
    path("", views.get_products, name="inventory"),
    path("create/", views.create_product, name="create"),
]
