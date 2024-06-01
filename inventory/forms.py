from django import forms

FORM_CONTROL_CLASS = "form-control form-control-user"
INVENTORY_CHOICES = [(1, "Sustraer"), (2, "Añadir")]


class CreateForm(forms.Form):
    """Create form class."""

    name = forms.CharField(
        label="name",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
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
                "class": FORM_CONTROL_CLASS,
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
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Precio",
                "id": "price",
            }
        ),
    )
    qty = forms.IntegerField(
        min_value=1,
        max_value=1000,
        label="qty",
        widget=forms.NumberInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Cantidad",
                "id": "qty",
            }
        ),
    )


class EditForm(forms.Form):
    """Edit form class."""

    name = forms.CharField(
        label="name",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Nombre",
                "id": "name",
                "readonly": "readonly",
            }
        ),
        required=False,
    )
    description = forms.CharField(
        label="description",
        max_length=250,
        widget=forms.TextInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Descripción",
                "id": "description",
                "readonly": "readonly",
            }
        ),
        required=False,
    )
    price = forms.IntegerField(
        min_value=100,
        max_value=10000000,
        label="price",
        widget=forms.NumberInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Precio",
                "id": "price",
            }
        ),
    )


class EditQtyForm(forms.Form):
    """Edit qty form class."""

    name = forms.CharField(
        label="name",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Nombre",
                "id": "name",
                "readonly": "readonly",
            }
        ),
        required=False,
    )
    qty = forms.IntegerField(
        min_value=1,
        max_value=1000,
        label="qty",
        widget=forms.NumberInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Cantidad",
                "id": "qty",
                "readonly": "readonly",
            }
        ),
    )
    operation_type = forms.ChoiceField(
        choices=INVENTORY_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select form-control form-control-user",
                "id": "operationType",
            }
        ),
    )
    new_qty = forms.IntegerField(
        min_value=1,
        max_value=1000,
        label="new_qty",
        widget=forms.NumberInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Cantidad a operar",
                "id": "qty",
            }
        ),
    )
