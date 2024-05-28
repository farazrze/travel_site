from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

#def login_view(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #password = request.POST['password']
        #user = authenticate(request,username=username,password=password)
        #if user is not None:
            #login(request,user)
            #return redirect('/')
    #if request.user.is_authenticated:
        #msg=f'user is authenticated as {request.user.username}'
        #return HttpResponse(f'user is authenticated as {request.user.username}')
    #else:
        #return HttpResponse('user is not authenticated')
        #msg='user is not authenticated'
        #context ={'msg':msg}
    #return render(request,'accounts/login.html')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
        form=AuthenticationForm()
        context={'form':form}
        return render(request,'accounts/login.html')
    else:
        return redirect('/')

def logout_view(request):
    return render(request,'accounts/logout.html')

def signup_view(request):
    return render(request,'accounts/signup.html')