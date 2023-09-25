from django.db import models
from django.contrib.auth.models import User
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.CharField(max_length=255)
    year = models.IntegerField()
    artist = models.TextField()
    amount = models.PositiveIntegerField()
    date_added = models.DateField(auto_now_add=True)