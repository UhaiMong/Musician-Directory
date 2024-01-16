from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addAlbum, name='album'),
    path('edit/<int:id>', views.editAlbum, name='edit'),
    path('delete/<int:id>', views.deleteRecord, name='delete'),
]
