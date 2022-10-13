from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    email = models.EmailField(max_length=254, unique=True, null=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Customize db table"""

        verbose_name_plural = "User"

    def __str__(self):
        return str(self.email)

