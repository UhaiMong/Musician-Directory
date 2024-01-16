from django.db import models
from musician.models import Musicians

# Create your models here.


class MyAlbum(models.Model):
    Album_Name = models.CharField(max_length=50)
    Album_release_date = models.DateTimeField()
    RATING_CHOICE = (
        ('One', '1'),
        ('Two', '2'),
        ('Three', '3'),
        ('Four', '4'),
        ('Five', '5'),
    )
    Rating = models.CharField(max_length=10, choices=RATING_CHOICE)
    # One-to-Many Relationships with musician model
    music = models.ForeignKey(
        Musicians, on_delete=models.CASCADE, verbose_name='Musician')

    def __str__(self):
        return self.Album_Name
