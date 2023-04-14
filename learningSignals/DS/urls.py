from django.urls import path
from . import views
from .views import UserRegister

app_name='DS'

urlpatterns =[
    path('', views.home, name='home'),
    path('register', UserRegister.as_view(), name='user-register'),
]