from rest_framework import serializers
from .models import Restaurant, MenuCategory, MenuSubCategory, Dishes, Ingredients

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name')


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ('id', 'name')

class MenuSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSubCategory
        fields = ('name', 'cover_photo')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'name')

class DishesSerializer(serializers.ModelSerializer):
    ingredients=IngredientSerializer(many=True)
    class Meta:
        model = Dishes
        fields = ('id', 'name','dishes_photo', 'ingredients')

class SubCategoriesDetailsSerializer(serializers.ModelSerializer):
    dishes=DishesSerializer(many=True)

    class Meta:
        model = MenuSubCategory
        fields = ('id', 'name', 'cover_photo', 'dishes')
