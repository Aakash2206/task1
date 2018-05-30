from django.db import models


# Create your models here.
class Product(models.Model):
    Product_Id = models.CharField(max_length=50, unique=True)
    Product_Name = models.CharField(max_length=150)
    Category = models.CharField(max_length=20, null=False)

