from django.urls import path
from .views import RegisterView, ProfileView

app_name='accounts'
urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', ProfileView.as_view(), name='profile'),
]