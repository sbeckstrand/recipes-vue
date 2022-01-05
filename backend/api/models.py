from django.db import models
import os

# Create your models here.

class Recipe(models.Model):
    difficulty_levels = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=800)
    picture = models.FileField()
    difficulty = models.CharField(choices=difficulty_levels, max_length=10)
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    guide = models.TextField()

    def __str__(self):
        return self.name