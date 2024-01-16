from django.db import models

# Create your models here.


class Musicians(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Phone_number = models.BigIntegerField()
    Instrument_Type = models.CharField(max_length=40)

    def __str__(self):
        return self.First_Name
