from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import *
from django.contrib import messages

def home(request,**kwargs):
    posts=Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])

    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def single(request,pid):
    if request.method=='POST':
        form=CommentForms(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment was submited')
        else:
            messages.add_message(request,messages.ERROR,"your comment didn't submited")

    n_post=Post.objects.filter(status=1)
    posts=get_object_or_404(n_post,id=pid)
    comments = Comment.objects.filter(post=posts.id,approve=True).order_by('-created_date')
    context = {'posts':posts,'comments':comments}
    return render(request,'blog/blog-single.html',context)


def test(request):
    return render(request,'test.html')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method=='GET':
        posts=posts.filter(content__contains=request.GET.get('s'))
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)