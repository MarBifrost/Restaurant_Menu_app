from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='restaurant_photos/')

    def __str__(self):
        return self.name

class MenuCategory(MPTTModel):
    name=models.CharField(max_length=50)
    restaurants=models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='main_categories', blank=True, null=True)
    parent=TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class MenuSubCategory(MPTTModel):
    name=models.CharField(max_length=50)
    cover_photo=models.ImageField(upload_to='restaurant_photos/')
    parent=TreeForeignKey('MenuCategory', on_delete=models.CASCADE, related_name='sub_categories')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Dishes(models.Model):
    name=models.CharField(max_length=50)
    dishes_photo=models.ImageField(upload_to='restaurant_photos/')
    price=models.IntegerField()
    menu_sub_category=models.ForeignKey(MenuSubCategory, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name=models.CharField(max_length=50)
    dishes= models.ForeignKey(Dishes, on_delete=models.CASCADE, related_name='ingredients')
    def __str__(self):
        return self.name
    

