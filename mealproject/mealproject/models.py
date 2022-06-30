from django.db import models


class IngredientPrice(models.Model):
    ingredient_name = models.CharField(max_length=200)
    unit = models.CharField(max_length=100)
    unitprice = models.IntegerField()

    def __str__(self):
<<<<<<< HEAD
        return str({'myname': self.myname,
                    'mytitle': self.mytitle,
                    'mycontent': self.mycontent,
                    'mydate': self.mydate})


class RecipeTable(models.Model):
    RECIPE_NM = models.CharField(max_length=20)
    QNT = models.CharField(max_length=10)
    RECIPE = models.CharField(max_length=2000)

    def __str__(self):
        return str({'RECIPE_NM': self.RECIPE_NM,
                    'QNT': self.QNT,
                    'RECIPE': self.RECIPE})


=======
        return str({'ingredient': self.ingredient,
                    'unit': self.unit,
                    'unitprice': self.unitprice})

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    potion = models.CharField(max_length=100)
    recipe_text = models.CharField(max_length=500)

    def __str__(self):
        return str({'recipe name': self.recipe_name,
                    'potion': self.potion,
                    'recipe text': self.recipe_text})

class RecipeIngredient(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.JSONField()
    amounts = models.JSONField()
>>>>>>> da601e10bb8ae4a873ee02e3d95c613bc64bf635

