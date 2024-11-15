from django.db import models
from django.contrib.auth.models import User
from restaurantapp.models import Dishes

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s profile"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart"

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    dishes=models.ForeignKey(Dishes, on_delete=models.CASCADE, related_name='+')
    price=models.ForeignKey(Dishes, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.price*self.dishes if self.dishes else 0

    def save(self, *args, **kwargs):
        if self.dishes:
            self.price=self.dishes.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s cart"