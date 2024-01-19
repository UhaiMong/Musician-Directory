from django.shortcuts import render, redirect
from . forms import albumForm
from . import models
# Create your views here.


def addAlbum(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            album = albumForm(request.POST)
            if album.is_valid():
                album.save()
                return redirect('homepage')
        else:
            album = albumForm()
        return render(request, 'album.html', {'form': album})
    else:
        return redirect('login')


def editAlbum(request, id):
    if request.user.is_authenticated:
        edit_album = models.MyAlbum.objects.get(pk=id)
        album = albumForm(instance=edit_album)
        if request.method == 'POST':
            album = albumForm(request.POST, instance=edit_album)
            if album.is_valid():
                album.save()
                return redirect('homepage')
        return render(request, 'album.html', {'form': album})
    else:
        return redirect('login')


def deleteRecord(request, id):
    if request.user.is_authenticated:
        delete_record = models.MyAlbum.objects.get(pk=id)
        delete_record.delete()
        return redirect('homepage')
    else:
        return redirect('login')
