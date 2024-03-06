from django.urls import path
from .views import *
app_name = 'pages'

urlpatterns = [
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('elements/',elements,name='elements'),
    path('index/',index,name='index'),
]
