from django.db import models

class Recipe(models.Model):
    RECIPE_NM = models.CharField(max_length=50)
    def __str__(self):
        return str({'RECIPE_NM': self.RECIPE_NM})