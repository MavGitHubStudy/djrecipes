# Generated by Django 4.2.6 on 2023-10-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Время приготовления в минутах'),
        ),
    ]