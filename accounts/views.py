from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserCreateForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        error = {}
        password = request.POST['password']
        password_c = request.POST['password_c']
        form = UserCreateForm(request.POST)
        if password == password_c:
            if form.is_valid():
                user = form.save()
                auth.login(request,user)
                return redirect('home') 
            return render(request,'accounts/register.html',{'form':form})
        else:
            error['password_match'] = 'Password did not match. Please try again.'
            return render(request,'accounts/register.html',{'form':form,'error':error})
    else:
        form = UserCreateForm()
        return render(request,'accounts/register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        error = {}
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            error['notAuth'] = "Wrong username/password. Please try again."
            return render(request,'accounts/login.html',{'error':error})
    else:
        return render(request,'accounts/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        
    return redirect('home')
    