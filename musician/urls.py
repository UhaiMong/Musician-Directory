from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addMusician, name='musician'),
    path('edit_musician/<int:id>', views.editMusician, name='edit_musician'),
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
]
