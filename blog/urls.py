from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',home,name='home'),
    path('<int:pid>',single,name='single'),
    path('test',test,name='test'),
    path('category/<str:cat_name>',home,name='category'),
    path('author/<str:author_username>',home,name='author'),
    path('search/',blog_search,name='search'),
    path('tag/<str:tag_name>',home,name='tag'),
]       