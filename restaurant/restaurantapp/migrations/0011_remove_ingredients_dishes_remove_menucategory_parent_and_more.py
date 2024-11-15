# Generated by Django 5.1.1 on 2024-11-15 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0010_menucategory_level_menucategory_lft_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='dishes',
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='restaurants',
        ),
        migrations.RemoveField(
            model_name='menusubcategory',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Dishes',
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.DeleteModel(
            name='MenuCategory',
        ),
        migrations.DeleteModel(
            name='MenuSubCategory',
        ),
    ]
