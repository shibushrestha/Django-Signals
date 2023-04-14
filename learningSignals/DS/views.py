from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.core.signals import request_finished
from django.dispatch import receiver

def home(request):
    return HttpResponse('You are at the homepage')

'''
def my_first_callback(sender, **kwargs):
    print('Request finished')

request_finished.connect(my_first_callback)
'''

@receiver(request_finished)
def my_second_callback(sender, **kwargs):
    print("Request finished with no errors.")

class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'DS/user_register.html'
    success_url = reverse_lazy('DS:home')