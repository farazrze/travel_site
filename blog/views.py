from django.shortcuts import render,get_object_or_404
from .models import Post

def home(request):
    posts=Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def single(request,pid):
    n_post=Post.objects.filter(status=1)
    posts=get_object_or_404(n_post,id=pid)
    context = {'posts':posts}
    return render(request,'blog/blog-single.html',context)


def test(request):
    return render(request,'test.html')