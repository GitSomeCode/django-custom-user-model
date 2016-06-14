from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate

from .forms import RegistrationForm, LoginForm


def success_register(request):
    return render(request, 'myuser/success_register.html')


def success_login(request):
    return render(request, 'myuser/success_login.html')


def register(request):
    form = RegistrationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Creates the new user
            new_user = form.save()

            # Authenticate and log in user
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)

            if user and user.is_active:
                django_login(request, user)
                return redirect('success_register')
        else:
            print(form.errors)

    return render(request, 'registration/register.html', {'form': form})


def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            print("login FORM VALID!")
            user = authenticate(email=data['email'], password=data['password'])

            if user and user.is_active:
                django_login(request, user)
                return redirect('success_login')
            else:
                print(form.errors)

    return render(request, 'registration/login.html', {'form': form})


def logout(request):
    django_logout(request)
    return redirect('login')
