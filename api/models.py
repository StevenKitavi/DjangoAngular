from django.db import models




class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True)
    year = models.IntegerField(blank=True)
