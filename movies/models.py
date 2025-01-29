from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=60)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    director = models.CharField(null=True, max_length=100)
    winner_oscar = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.rating}"
