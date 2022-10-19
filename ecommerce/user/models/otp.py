from statistics import mode
from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Otp(models.Model):

    otp = models.IntegerField(validators=[MinValueValidator(100000),
                                       MaxValueValidator(999999)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)