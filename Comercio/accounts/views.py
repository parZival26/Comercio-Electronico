from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy

from .forms import LoginForm



class Login(LoginView):
    redirect_authenticated_user = True
    template_name = "accounts/user_form.html"
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = "Iniciar sesión"
        return context


@login_required
def log_out(request):
    logout(request)
    return redirect('index')