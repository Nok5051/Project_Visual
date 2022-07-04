# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'


class Recipe(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recipe_nm = models.CharField(db_column='RECIPE_NM', max_length=20)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=10)  # Field name made lowercase.
    qnt = models.CharField(db_column='QNT', max_length=10)  # Field name made lowercase.
    recipe = models.CharField(db_column='RECIPE', max_length=2000)  # Field name made lowercase.
    ingredients = models.CharField(db_column='INGREDIENTS', max_length=1000)  # Field name made lowercase.
    units = models.CharField(db_column='UNITS', max_length=1000)  # Field name made lowercase.
    total_price = models.CharField(db_column='TOTAL_PRICE', max_length=2000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recipe'


class StandardPrice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ingredient_nm = models.CharField(db_column='INGREDIENT_NM', max_length=20)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=10)  # Field name made lowercase.
    price = models.CharField(db_column='PRICE', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Standard_Price'

