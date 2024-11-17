from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q, Prefetch
from .models import Restaurant, MenuCategory, MenuSubCategory, Dishes
from .serializers import RestaurantSerializer, MenuCategorySerializer, MenuSubCategorySerializer, \
    SubCategoriesDetailsSerializer


# Create your views here.
class RestaurantListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Restaurant.objects.all()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)


class MenuCategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = MenuCategory.objects.all()
        serializer = MenuCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class MenuSubCategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        parent_id = request.query_params.get('parent_id')
        dish_name = request.query_params.get('dish_name')
        queryset = MenuSubCategory.objects.all()

        if parent_id:
            queryset = queryset.filter(parent_id=parent_id)
        if dish_name:
            queryset = queryset.filter(dishes__name__contains=dish_name)
        serializer = MenuSubCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class SubCategoryDetailView(APIView):
    def get(self, request, subcategory_id):
        # Optional filter by dish name
        dish_name = request.query_params.get('dish_name', None)

        # Retrieve the subcategory
        subcategory = get_object_or_404(MenuSubCategory, id=subcategory_id)

        # Filter dishes by name if provided
        if dish_name:
            subcategory.dishes = subcategory.dishes.filter(name__icontains=dish_name)

        # Serialize the data
        serializer = SubCategoriesDetailsSerializer(subcategory)
        return Response(serializer.data, status=status.HTTP_200_OK)
