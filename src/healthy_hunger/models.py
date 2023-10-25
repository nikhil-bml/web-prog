from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField(max_length=1000)
    product_image = ResizedImageField(size=[600,400],quality=100,upload_to="product/")
    ingredients = models.TextField(max_length=3000)
    nutrition_image = ResizedImageField(size=[700,1350],quality=100,upload_to="nutrition/")
    price = models.FloatField(default=200)

    def __str__(self) -> str:
        return f"{self.id}_{self.name}"
    
class Query(models.Model):
    name = models.CharField(max_length=300)
    email =models.EmailField(max_length=500)
    query = models.CharField(max_length=3000)

    def __str__(self) -> str:
        return f"{self.email}_{self.query}"

class Cart(models.Model):
    user = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE, related_name="cart_orders")
    product = models.ForeignKey(Product, to_field="id", on_delete=models.CASCADE, related_name="ordered_by")
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self) :
        return f"{self.user} has {self.product}"