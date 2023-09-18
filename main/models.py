from django.db import models

class Item(models.Model):
    album = models.CharField(max_length=255)
    year = models.IntegerField()
    artist = models.TextField()
    date_added = models.DateField(auto_now_add=True)