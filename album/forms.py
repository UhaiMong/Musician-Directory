from django import forms
from . models import MyAlbum


class albumForm(forms.ModelForm):
    class Meta:
        model = MyAlbum
        fields = '__all__'
        widgets = {
            'Album_release_date': forms.DateInput(attrs={'type': 'date'}),
        }
