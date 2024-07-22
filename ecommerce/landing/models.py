from django.db import models
from django.core.validators import MinValueValidator, MinValueValidator

# Create your models here.
class message(models.Model):
    Fullname = models.CharField(max_length=120)
    Email = models.EmailField()
    phone = models.CharField(max_length=12,validators=[MinValueValidator(11),MinValueValidator(1)])
    message = models.TextField(max_length=500)
    def __str__(self):
        return self.Fullname
