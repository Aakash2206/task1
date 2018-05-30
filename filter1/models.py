from django import forms
from django.db import models


# Create your models here.


class Data(models.Model):
    product_name = models.CharField(max_length=150)
    product_id = models.CharField(max_length=50, unique=True)
    cat_id = models.CharField(max_length=2, null=False)
    cat = forms.CharField(max_length=20)


class Subcat(models.Model):
    cat_id = models.ForeignKey('Data', on_delete=models.CASCADE)
    c_id = models.CharField(max_length=2, null=False)
    p_name = models.CharField(max_length=150, null=True)


class Subsubcat(models.Model):
    c_id = models.ForeignKey('Subcat', on_delete=models.CASCADE)
    c_name = models.CharField(max_length=150, null=False)
