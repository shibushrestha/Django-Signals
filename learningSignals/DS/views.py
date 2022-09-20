from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def home(request):
    return HttpResponse('You are at the homepage')


class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'DS/userRegister.html'
    success_url = reverse_lazy('DS:home')