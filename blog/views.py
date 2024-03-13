from django.shortcuts import render
from .models import Post

def home(request):
    posts=Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def single(request):
    return render(request,'blog/blog-single.html')