from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUPForm


class SignUPView(SuccessMessageMixin,CreateView):

    model = User
    form_class = SignUPForm
    template_name = 'users/signup.html'
    success_message = 'Вы успешно зарегистрированы'
    success_url = reverse_lazy('users:login')