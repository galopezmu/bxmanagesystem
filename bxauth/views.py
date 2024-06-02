from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from bxauth.forms import LoginForm


class Login(View):
    """Login view class."""

    def get(self, request: HttpRequest):
        """Login page."""
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request: HttpRequest):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                messages.success(request, f"Bienvenido {user}")
                return redirect("inventory")
        messages.error(request, "Usuario o contraseña inválida")
        return redirect("login")
