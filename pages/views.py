from django.shortcuts import render
from .models import *
from pages.forms import *
from django.http import *
from django.contrib import messages

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your information was submited')
        else:
            messages.add_message(request,messages.ERROR,"your information didn't submited")
    form = ContactForms()
    return render(request,'contact.html',{'form':form})

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


def newsletter(request):
    if request.method == 'POST':
        form = Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = Newsletterform()
    return HttpResponseRedirect('/')