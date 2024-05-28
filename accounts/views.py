from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    #if request.user.is_authenticated:
        #msg=f'user is authenticated as {request.user.username}'
        #return HttpResponse(f'user is authenticated as {request.user.username}')
    #else:
        #return HttpResponse('user is not authenticated')
        #msg='user is not authenticated'
        #context ={'msg':msg}
    return render(request,'accounts/login.html')

def logout_view(request):
    return render(request,'accounts/logout.html')

def signup_view(request):
    return render(request,'accounts/signup.html')