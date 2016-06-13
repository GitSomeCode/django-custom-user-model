from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse

from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("REGISTRATION FORM VALID!")
            new_user = form.save()

            # Authenticate and log in user
            email = new_user.email
            password = new_user.password

            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('myuser/success.html')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            print("login FORM VALID!")
            #import pdb; pdb.set_trace();
            user = authenticate(email=request.POST['email'], password=request.POST['password'])

            if user is not None and user.is_active:
                login(request, user)
                return redirect('myuser/success.html')
            else:
                print(form.errors)
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    redirect('myuser/base.html')
