from django.shortcuts import render, redirect
from . import forms
from . import models
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def addMusician(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            musician = forms.MusicianForm(request.POST)
            if musician.is_valid():
                musician.save()
                return redirect('album')
        else:
            musician = forms.MusicianForm()
        return render(request, 'musician.html', {'form': musician})
    else:
        return redirect('login')


def editMusician(request, id):
    if request.user.is_authenticated:
        edit_musician = models.Musicians.objects.get(pk=id)
        musician = forms.MusicianForm(instance=edit_musician)
        if request.method == 'POST':
            musician = forms.MusicianForm(request.POST, instance=edit_musician)
            if musician.is_valid():
                musician.save()
                return redirect('homepage')
        return render(request, 'musician.html', {'form': musician})
    else:
        return redirect('login')


# Authentication Start
def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created Successfully!')
            form.save(commit=True)
            return redirect('homepage')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login Function


def userLogin(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userPassword = form.cleaned_data['password']
            user = authenticate(username=name, password=userPassword)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged In Successfully')
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout function


def userLogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')
