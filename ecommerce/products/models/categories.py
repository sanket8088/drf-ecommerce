from statistics import mode
from django.db import models
from user.models import User

class Categories(models.Model):

    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.category_name)