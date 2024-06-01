from django import forms


class CreateForm(forms.Form):
    """Create form class."""

    name = forms.CharField(
        label="name",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Nombre",
                "id": "name",
            }
        ),
    )
    description = forms.CharField(
        label="description",
        max_length=250,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Descripción",
                "id": "description",
            }
        ),
    )
    price = forms.IntegerField(
        min_value=100,
        max_value=10000000,
        label="price",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Precio",
                "id": "price",
            }
        ),
    )
    qty = forms.IntegerField(
        min_value=1,
        max_value=1000,
        label="name",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Cantidad",
                "id": "qty",
            }
        ),
    )
