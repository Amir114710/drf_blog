from django.urls import path
from .apiview import *

app_name = 'api_view'

urlpatterns = [
    path('register' , Register.as_view() , name='register'),
    path('login' , LoginApiView.as_view() , name='register'),
]