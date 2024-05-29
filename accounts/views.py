from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required

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

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')