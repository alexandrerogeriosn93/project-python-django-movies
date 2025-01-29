from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=60)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    winner_oscar = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.rating}"
