from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuCategory)
admin.site.register(MenuSubCategory)
admin.site.register(Dishes)
admin.site.register(Ingredients)