# Generated by Django 4.0.5 on 2022-07-01 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RECIPE_NM', models.CharField(max_length=50)),
            ],
        ),
    ]
