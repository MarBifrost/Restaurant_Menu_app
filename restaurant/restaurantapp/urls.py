from django.urls import path
from .views import RestaurantListView, MenuCategoryListView, MenuSubCategoryListView, SubCategoryDetailView

app_name = 'restaurant'

urlpatterns = [
    path('rest/api/', RestaurantListView.as_view(), name='register'),
    path('menucategories/', MenuCategoryListView.as_view(), name='menu_categories'),
    path('subcategories/', MenuSubCategoryListView.as_view(), name='sub_categories'),
    path('subcategories/<int:subcategory_id>/', SubCategoryDetailView.as_view(), name='category_detailed'),
]