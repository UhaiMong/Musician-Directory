from django.shortcuts import render, redirect
from . forms import albumForm
from . import models
# Create your views here.


def addAlbum(request):
    if request.method == 'POST':
        album = albumForm(request.POST)
        if album.is_valid():
            album.save()
            redirect('album')
    else:
        album = albumForm()
    return render(request, 'album.html', {'form': album})


def editAlbum(request, id):
    edit_album = models.MyAlbum.objects.get(pk=id)
    album = albumForm(instance=edit_album)
    if request.method == 'POST':
        album = albumForm(request.POST, instance=edit_album)
        if album.is_valid():
            album.save()
            redirect('homepage')
    return render(request, 'album.html', {'form': album})


def deleteRecord(request, id):
    delete_record = models.MyAlbum.objects.get(pk=id)
    delete_record.delete()
    return redirect('homepage')
