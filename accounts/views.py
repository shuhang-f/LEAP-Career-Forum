from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import CustomUser

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserForm

def signup_view(request):
    users = CustomUser.objects.all()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/home/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form, 'users': users})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password, model=CustomUser)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('/home/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import logging
from django.conf import settings

fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

logging.basicConfig(format=fmt, level=lvl)


def home_view(request):
    user = request.user
    logging.debug(user)
    context = {}
    if str(user) is not '':
        if request.method == 'POST':
            form = CustomUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated.')
        else:
            form = CustomUserForm(instance=user)

        context = {'form': form}
        return render(request, 'home.html', context)
    return render(request, 'home.html', context)


def facebook_callback(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        return redirect('/login/')