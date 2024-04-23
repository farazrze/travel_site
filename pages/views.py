from django.shortcuts import render
from .models import *
from pages.forms import *

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('name')
        message=request.POST.get('message')

        c = Contact()
        c.name=name
        c.email=email
        c.subject=subject
        c.message=message

        c.save()
    print(request.method)
    return render(request,'contact.html')

def elements(request):
    return render(request,'elements.html')

def index(request):
    return render(request,'index.html')


def test_view(request):
    if request.method=='POST':
        form=ContactForms(request.POST)
        if form.is_valid():
            form.save()


    form = ContactForms()
    return render(request,'test_view.html',{'form':form})
