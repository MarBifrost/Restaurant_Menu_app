from rest_framework import serializers
from .models import Restaurant, MenuCategory, MenuSubCategory, Dishes, Ingredients

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name')
