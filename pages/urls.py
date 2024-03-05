from django.urls import path
from .views import *

urlpatterns = [
    path('about/',about),
    path('contact/',contact),
    path('elements/',elements),
    path('index/',index),
]
