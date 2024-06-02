from django import forms

FORM_CONTROL_CLASS = "form-control form-control-user"


class LoginForm(forms.Form):
    """Login form class."""

    username = forms.CharField(
        label="name",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Nombre de usuario",
                "id": "username",
            }
        ),
    )
    password = forms.CharField(
        label="password",
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": FORM_CONTROL_CLASS,
                "placeholder": "Contraseña",
                "id": "password",
            }
        ),
    )
