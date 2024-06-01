from django.urls import path

from inventory import views

urlpatterns = [
    path("", views.Products.as_view(), name="inventory"),
    path("create/", views.CreateProduct.as_view(), name="create"),
    path("edit/<int:_id>/", views.EditProduct.as_view(), name="edit"),
    path("edit/qty/<int:_id>/", views.EditProductQty.as_view(), name="edit_qty"),
]
