from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        # get values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check pw are equal
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # check username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'email is already taken')
            return redirect('register')

        # looks good
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        # auth.login(request, user)
        user.save()
        messages.success(request, 'You are now registered and can log in')
        return redirect('login')
        
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        messages.error(request, 'TEST alert')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')