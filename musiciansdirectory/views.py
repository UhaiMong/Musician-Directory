from django.shortcuts import render
from album.models import MyAlbum


def home(request):
    data = MyAlbum.objects.all()
    print(data)
    return render(request, 'home.html', {'data': data})
