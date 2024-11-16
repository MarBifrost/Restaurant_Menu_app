from django.urls import path
from .views import RestaurantListView

app_name = 'restaurantapp'

urlpatterns = [
    path('rest/api/', RestaurantListView.as_view(), name='register'),
]