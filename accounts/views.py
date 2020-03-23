from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        error = {}
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_c = request.POST['password_c']
        if password == password_c:
            try:
                user = User.objects.get(username = username)
                #email_check = User.objects.get(email  = email)
                # if username_check:
                #     error['username'] = 'username is already taken. Please choose another'
                # if email_check:
                #     error['email'] = 'email is already taken. Please try again or login'
                error['username'] = 'username is already taken. Please choose another'
                return render(request,'accounts/register.html',{'error':error})
            except User.DoesNotExist:
                user = User.objects.create_user(username,email,password,first_name = fname,last_name = lname)
                auth.login(request,user)
                return redirect('home')
        else:
            error['password_match'] = 'Password did not match. Please try again.'
            return render(request,'accounts/register.html',{'error':error})
    else:
        return render(request,'accounts/register.html')

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
    else:
        return redirect('home')
    print('hello')
