from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from main.models import extendUser


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        email = request.POST['email']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email) 
            user.save() #registered
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)#login
            return redirect('/main')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            messages.error(request, 'Invalid credential')
            return redirect('register')
    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
