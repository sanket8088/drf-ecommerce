from statistics import mode
from django.db import models
from products.models import Categories

class Product(models.Model):

    category = models.ForeignKey(Categories, on_delete =models.CASCADE)
    name = models.CharField(max_length=500)
    picture = models.CharField(max_length=500)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    