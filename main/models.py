from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)