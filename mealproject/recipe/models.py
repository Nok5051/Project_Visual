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


class MapStore(models.Model):
    addr = models.CharField(max_length=255, blank=True, null=True)
    storename = models.CharField(max_length=255, blank=True, null=True)
    storetype = models.CharField(max_length=255, blank=True, null=True)
    callnum = models.CharField(max_length=255, blank=True, null=True)
    menu1 = models.CharField(max_length=255, blank=True, null=True)
    menu2 = models.CharField(max_length=255, blank=True, null=True)
    menu3 = models.CharField(max_length=255, blank=True, null=True)
    menu1_price = models.IntegerField(blank=True, null=True)
    menu2_price = models.IntegerField(blank=True, null=True)
    menu3_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Map_store'


class Recipe(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recipe_nm = models.CharField(db_column='RECIPE_NM', max_length=20)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=10)  # Field name made lowercase.
    qnt = models.CharField(db_column='QNT', max_length=10)  # Field name made lowercase.
    recipe = models.CharField(db_column='RECIPE', max_length=2000)  # Field name made lowercase.
    ingredients = models.CharField(db_column='INGREDIENTS', max_length=1000)  # Field name made lowercase.
    units = models.CharField(db_column='UNITS', max_length=1000)  # Field name made lowercase.

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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
