from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)])
    heatrate = models.IntegerField(default=60, validators=[
                                   MinValueValidator(1), MaxValueValidator(300)])

    def __str__(self):

        return f"\nFirst Name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}"
