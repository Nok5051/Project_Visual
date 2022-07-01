from django.db import models


class IngredientPrice(models.Model):
    ingredient_name = models.CharField(max_length=200)
    unit = models.CharField(max_length=100)
    unitprice = models.IntegerField()
    def __str__(self):
        return str({'ingredient_name': self.ingredient_name,'unit': self.unit,'unitprice': self.unitprice})


class RecipeTable(models.Model):
    RECIPE_NM = models.CharField(max_length=20)
    QNT = models.CharField(max_length=10)
    RECIPE = models.CharField(max_length=2000)
    def __str__(self):
        return str({'RECIPE_NM': self.RECIPE_NM,'QNT': self.QNT,'RECIPE': self.RECIPE})



