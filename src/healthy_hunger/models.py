from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField(max_length=1000)
    product_image = models.FileField(upload_to="product/")
    ingredients = models.TextField(max_length=3000)
    nutrition_image = models.FileField(upload_to="nutrition/") 

    def __str__(self) -> str:
        return f"{self.id}_{self.name}"
    
class Query(models.Model):
    name = models.CharField(max_length=300)
    email =models.EmailField(max_length=500)
    query = models.CharField(max_length=3000)

    def __str__(self) -> str:
        return f"{self.email}_{self.query}"
