from django.shortcuts import render

def home(request):
    return render(request,'blog/blog-home.html')

def single(request):
    return render(request,'blog/blog-single.html')