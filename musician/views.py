from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def addMusician(request):
    if request.method == 'POST':
        musician = forms.MusicianForm(request.POST)
        if musician.is_valid():
            musician.save()
            redirect('homepage')
    else:
        musician = forms.MusicianForm()
    return render(request, 'musician.html', {'form': musician})


def editMusician(request, id):
    edit_musician = models.Musicians.objects.get(pk=id)
    musician = forms.MusicianForm(instance=edit_musician)
    if request.method == 'POST':
        musician = forms.MusicianForm(request.POST, instance=edit_musician)
        if musician.is_valid():
            musician.save()
            redirect('homepage')
    return render(request, 'musician.html', {'form': musician})
