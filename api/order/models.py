from django.core.validators import MinValueValidator
from django.db import models

from api.product.models import Product
from api.user.models import CustomUser


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_names = models.CharField(max_length=150)
    total_products = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    total_amount = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    transaction_id = models.CharField(max_length=150, default=0)

    def __str__(self):
        return f"{self.product_name}"
