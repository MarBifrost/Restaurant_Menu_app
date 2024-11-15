# Generated by Django 5.1.1 on 2024-11-15 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0008_alter_menucategory_restaurants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menucategory',
            name='level',
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='menucategory',
            name='tree_id',
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='restaurants',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_categories', to='restaurantapp.restaurant'),
        ),
    ]
