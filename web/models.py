from django.db import models


# Create your models here.
class house(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    rooms = models.CharField(max_length=100, blank=True, null=True)
    parking = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    metr = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.location
